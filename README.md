# Joo Travels — Feedback API (Django + DRF + PostgreSQL)

Backend for the customer feedback feature: visitors submit their name, a
1–5 star rating, a message and an optional photo. Submissions stay hidden
until an admin approves them from the Django admin panel; only approved
feedback is returned to the public site.

## 1. Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Create the PostgreSQL database

```sql
CREATE DATABASE joo_travels;
CREATE USER joo_travels_user WITH PASSWORD 'change-this-password';
GRANT ALL PRIVILEGES ON DATABASE joo_travels TO joo_travels_user;
ALTER DATABASE joo_travels OWNER TO joo_travels_user;
```

## 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in `SECRET_KEY`, DB credentials, and
`CORS_ALLOWED_ORIGINS` (the URL your React dev server / production
frontend runs on).

## 4. Migrate and create an admin user

```bash
python manage.py migrate
python manage.py createsuperuser
```

## 5. Run the server

```bash
python manage.py runserver
```

## API endpoints

| Method | Endpoint                  | Description                                   |
|--------|----------------------------|------------------------------------------------|
| GET    | `/api/feedback/`           | List approved feedback (public, newest first). Optional `?limit=5` |
| POST   | `/api/feedback/submit/`    | Submit new feedback as `multipart/form-data`: `name`, `rating` (1-5), `message`, `route` (optional), `photo` (optional image file). Goes in as pending. |
| /admin | `/admin/`                  | Django admin — approve/reject feedback, view/replace photos. |

Approving feedback: log into `/admin/`, open **Feedback**, select the
pending item(s) and use the **Approve selected feedback** action (or tick
"Is approved" on the item and save).

## Notes

- Photos are stored on the local disk (`MEDIA_ROOT`/`media/feedback_photos/`)
  and served at `/media/...`. If you later deploy to a host with an
  ephemeral filesystem (e.g. Render's free tier), move to S3 storage —
  same pattern as the DDR project.
- Anonymous submissions are rate-limited to 20/hour per IP
  (`AnonRateThrottle`) to reduce spam.
- In production set `DEBUG=False`, a real `SECRET_KEY`, and run
  `python manage.py collectstatic`. Whitenoise serves static files;
  put a real web server (nginx) or a host like Render in front of
  gunicorn for media/TLS.
