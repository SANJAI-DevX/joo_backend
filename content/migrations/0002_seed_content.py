from django.db import migrations

HOME_BLOCKS = [
    ("nav_services", "Nav: Services Link", "services", "சேவைகள்"),
    ("nav_how", "Nav: How It Works Link", "how it works", "எப்படி முன்பதிவு செய்வது"),
    ("nav_routes", "Nav: Popular Routes Link", "popular routes", "பிரபலமான வழித்தடங்கள்"),
    ("nav_drivers", "Nav: Our Drivers Link", "our drivers", "எங்கள் டிரைவர்கள்"),
    ("nav_reviews", "Nav: Reviews Link", "reviews", "கருத்துக்கள்"),
    ("nav_book", "Nav: Book Button", "Book on WhatsApp", "வாட்ஸ்அப்பில் முன்பதிவு செய்யவும்"),
    ("hero_title", "Hero: Title", "Your journey, our responsibility", "உங்கள் பயணம், எங்கள் பொறுப்பு"),
    (
        "hero_desc",
        "Hero: Description",
        "Joo Travels offers safe, comfortable and affordable cab and travel services for outstation trips, airport transfers, local rides, weddings and tour packages — driven by trusted local drivers.",
        "Joo Travels நிறுவனம் ஊர் வெளி பயணங்கள், விமான நிலைய போக்குவரத்து, உள்ஊர் பயணங்கள், திருமண வாகனங்கள் மற்றும் சுற்றுலா தொகுப்புகளுக்கு பாதுகாப்பான, வசதியான, மலிவான கார் சேவைகளை நம்பகமான உள்ளூர் டிரைவர்களுடன் வழங்குகிறது.",
    ),
    ("hero_btn", "Hero: Button", "Book a Trip", "பயணத்தை முன்பதிவு செய்யவும்"),
    ("stat_1", "Stat 1 Label", "Happy Travellers", "மகிழ்ச்சியான பயணிகள்"),
    ("stat_2", "Stat 2 Label", "Cities Covered", "நகரங்கள்"),
    ("stat_3", "Stat 3 Label", "Years of Service", "ஆண்டுகள் சேவை"),
    ("stat_4", "Stat 4 Label", "Booking Support", "முன்பதிவு உதவி"),
    ("services_title", "Services: Title", "Our Services", "எங்கள் சேவைகள்"),
    (
        "services_desc",
        "Services: Description",
        "Whatever your travel need, Joo Travels has a ride ready for you. Explore our range of travel services below:",
        "உங்கள் பயண தேவை எதுவாக இருந்தாலும், Joo Travels உங்களுக்காக ஒரு வாகனத்தை தயார் செய்துள்ளது. கீழே உள்ள எங்கள் சேவைகளைப் பாருங்கள்:",
    ),
    ("s1_l1", "Service 1: Line 1", "outstation", "ஊர் வெளி"),
    ("s1_l2", "Service 1: Line 2", "trips", "பயணங்கள்"),
    ("s2_l1", "Service 2: Line 1", "airport", "விமான நிலையம்"),
    ("s2_l2", "Service 2: Line 2", "pickup & drop", "பிக்-அப் & டிராப்"),
    ("s3_l1", "Service 3: Line 1", "local city", "உள்ஊர்"),
    ("s3_l2", "Service 3: Line 2", "rides", "பயணங்கள்"),
    ("s4_l1", "Service 4: Line 1", "wedding &", "திருமணம் &"),
    ("s4_l2", "Service 4: Line 2", "event cars", "நிகழ்ச்சி கார்கள்"),
    ("s5_l1", "Service 5: Line 1", "tour", "சுற்றுலா"),
    ("s5_l2", "Service 5: Line 2", "packages", "தொகுப்புகள்"),
    ("s6_l1", "Service 6: Line 1", "corporate", "நிறுவன"),
    ("s6_l2", "Service 6: Line 2", "travel", "பயணம்"),
    ("learn_more", "Services: Learn More Link", "learn more", "மேலும் அறிக"),
    ("cta_title", "CTA Banner: Title", "Ready to hit the road?", "பயணத்திற்கு தயாரா?"),
    (
        "cta_desc",
        "CTA Banner: Description",
        "Message us on WhatsApp with your pickup point, drop location, date and time — we'll confirm your booking instantly.",
        "உங்கள் பிக்-அப் இடம், டிராப் இடம், தேதி மற்றும் நேரத்துடன் வாட்ஸ்அப்பில் எங்களுக்கு செய்தி அனுப்புங்கள் — உடனடியாக உங்கள் முன்பதிவை உறுதிசெய்வோம்.",
    ),
    ("cta_btn", "CTA Banner: Button", "Book via WhatsApp", "வாட்ஸ்அப் மூலம் முன்பதிவு செய்யவும்"),
    ("routes_title", "Popular Routes: Title", "popular routes", "பிரபலமான வழித்தடங்கள்"),
    (
        "routes_desc",
        "Popular Routes: Description",
        "Some of our most booked routes and trips travelled by our happy customers",
        "எங்கள் மகிழ்ச்சியான வாடிக்கையாளர்கள் அதிகம் முன்பதிவு செய்யும் சில வழித்தடங்கள்",
    ),
    (
        "route_1",
        "Route 1 Description",
        "Chennai to Madurai outstation drop — comfortable AC cars with experienced drivers for family and temple trips.",
        "சென்னை முதல் மதுரை வரை ஊர் வெளி பயணம் — குடும்ப மற்றும் கோவில் பயணங்களுக்கு அனுபவம் வாய்ந்த டிரைவர்களுடன் வசதியான ஏசி கார்கள்.",
    ),
    (
        "route_2",
        "Route 2 Description",
        "Chennai Airport pickup and drop — on-time service with flight tracking, so you're never kept waiting.",
        "சென்னை விமான நிலைய பிக்-அப் மற்றும் டிராப் — விமான நேரத்தை கண்காணித்து சரியான நேரத்தில் சேவை.",
    ),
    (
        "route_3",
        "Route 3 Description",
        "Chennai to Bangalore / Pondicherry round trips — perfect for weekend getaways and business travel.",
        "சென்னை முதல் பெங்களூரு / புதுச்சேரி இரு வழி பயணங்கள் — வார இறுதி மற்றும் வணிக பயணங்களுக்கு ஏற்றது.",
    ),
    ("book_now", "Popular Routes: Book Now Link", "book now", "இப்போது முன்பதிவு செய்யவும்"),
    ("how_title", "How It Works: Title", "How Booking Works", "முன்பதிவு எப்படி செய்வது"),
    (
        "how_desc",
        "How It Works: Description",
        "Book your ride in just a few simple steps",
        "சில எளிய படிகளில் உங்கள் பயணத்தை முன்பதிவு செய்யுங்கள்",
    ),
    ("step1_t", "Step 1 Title", "1. Choose Your Trip", "1. உங்கள் பயணத்தைத் தேர்வு செய்யவும்"),
    (
        "step1_d",
        "Step 1 Description",
        "Decide the type of trip you need — outstation, airport transfer, local ride, wedding car or tour package.",
        "உங்களுக்கு தேவையான பயண வகையை தேர்வு செய்யவும் — ஊர் வெளி, விமான நிலையம், உள்ஊர், திருமணம் அல்லது சுற்றுலா.",
    ),
    ("step2_t", "Step 2 Title", "2. Message Us on WhatsApp", "2. வாட்ஸ்அப்பில் செய்தி அனுப்பவும்"),
    (
        "step2_d",
        "Step 2 Description",
        'Tap the "Book via WhatsApp" button or use the booking form below to start a chat with our team directly.',
        '"வாட்ஸ்அப் மூலம் முன்பதிவு செய்யவும்" பொத்தானை தட்டவும் அல்லது கீழே உள்ள படிவத்தைப் பயன்படுத்தி எங்கள் குழுவுடன் நேரடியாக பேசவும்.',
    ),
    ("step3_t", "Step 3 Title", "3. Share Your Details", "3. உங்கள் விவரங்களைப் பகிரவும்"),
    (
        "step3_d",
        "Step 3 Description",
        "Share your pickup point, drop location, date, time and number of passengers with us on WhatsApp.",
        "உங்கள் பிக்-அப் இடம், டிராப் இடம், தேதி, நேரம் மற்றும் பயணிகள் எண்ணிக்கையை வாட்ஸ்அப்பில் பகிரவும்.",
    ),
    ("step4_t", "Step 4 Title", "4. Get Instant Confirmation", "4. உடனடி உறுதிப்படுத்தல் பெறவும்"),
    (
        "step4_d",
        "Step 4 Description",
        "We'll confirm your car, driver and fare over WhatsApp within minutes.",
        "சில நிமிடங்களில் உங்கள் கார், டிரைவர் மற்றும் கட்டணத்தை வாட்ஸ்அப்பில் உறுதிசெய்வோம்.",
    ),
    ("step5_t", "Step 5 Title", "5. Track Your Driver", "5. உங்கள் டிரைவரைக் கண்காணிக்கவும்"),
    (
        "step5_d",
        "Step 5 Description",
        "On the day of travel, our driver will call or WhatsApp you before arrival at the pickup point.",
        "பயண நாளில், பிக்-அப் இடத்திற்கு வருவதற்கு முன் எங்கள் டிரைவர் உங்களை அழைப்பார் அல்லது வாட்ஸ்அப் செய்வார்.",
    ),
    ("step6_t", "Step 6 Title", "6. Enjoy a Safe Trip", "6. பாதுகாப்பான பயணத்தை அனுபவிக்கவும்"),
    (
        "step6_d",
        "Step 6 Description",
        "Sit back and relax — our experienced drivers ensure a safe and comfortable journey to your destination.",
        "நிம்மதியாக அமருங்கள் — எங்கள் அனுபவமிக்க டிரைவர்கள் பாதுகாப்பான, வசதியான பயணத்தை உறுதி செய்வார்கள்.",
    ),
    ("drivers_title", "Drivers: Title", "Our Drivers", "எங்கள் டிரைவர்கள்"),
    (
        "drivers_desc",
        "Drivers: Description",
        "Meet the experienced, friendly drivers who will take you safely to your destination",
        "உங்களை பாதுகாப்பாக அழைத்துச் செல்லும் அனுபவம் வாய்ந்த, நட்பான டிரைவர்களை சந்திக்கவும்",
    ),
    (
        "driver1_desc",
        "Driver 1 Bio",
        "Friendly and experienced driver, skilled in outstation and local trips. Always punctual and safety-focused.",
        "நட்பான, அனுபவம் வாய்ந்த டிரைவர், ஊர் வெளி மற்றும் உள்ஊர் பயணங்களில் திறமையானவர். எப்போதும் நேரம் தவறாதவர்.",
    ),
    (
        "driver2_desc",
        "Driver 2 Bio",
        "Reliable and courteous driver, well known for safe long-distance driving and clean, well maintained cars.",
        "நம்பகமான, மரியாதையான டிரைவர், நீண்ட தூர பாதுகாப்பான ஓட்டுநர் மற்றும் சுத்தமான கார்களுக்கு பெயர் பெற்றவர்.",
    ),
    ("chat_whatsapp", "Drivers: Chat Button", "Chat on WhatsApp", "வாட்ஸ்அப்பில் பேசவும்"),
    ("reviews_title", "Testimonials: Title", "Testimonials", "வாடிக்கையாளர் கருத்துக்கள்"),
    (
        "reviews_desc",
        "Testimonials: Description",
        "Hear from our happy travellers about their experience with Joo Travels",
        "Joo Travels உடனான அனுபவத்தைப் பற்றி எங்கள் மகிழ்ச்சியான பயணிகள் என்ன சொல்கிறார்கள் என்பதைக் கேளுங்கள்",
    ),
    (
        "review_1",
        "Fallback Review 1",
        "We booked an outstation trip with Joo Travels for a family function. The driver was on time, polite, and drove very safely. Highly recommend for long trips.",
        "குடும்ப நிகழ்ச்சிக்காக Joo Travels-இல் ஊர் வெளி பயணத்தை முன்பதிவு செய்தோம். டிரைவர் நேரம் தவறாமல், மரியாதையாக, பாதுகாப்பாக ஓட்டினார். நீண்ட பயணங்களுக்கு பரிந்துரைக்கிறேன்.",
    ),
    ("review_1_role", "Fallback Review 1 Trip", "Chennai to Madurai", "சென்னை முதல் மதுரை"),
    (
        "review_2",
        "Fallback Review 2",
        "Excellent airport pickup service. The driver was waiting even though our flight was delayed. Very professional and the car was spotless.",
        "சிறந்த விமான நிலைய பிக்-அப் சேவை. விமானம் தாமதமானாலும் டிரைவர் காத்திருந்தார். மிகவும் தொழில்முறையானது, கார் மிகவும் சுத்தமாக இருந்தது.",
    ),
    ("review_2_role", "Fallback Review 2 Trip", "Airport Pickup", "விமான நிலைய பிக்-அப்"),
    (
        "review_3",
        "Fallback Review 3",
        "Booking through WhatsApp was so easy and fast. Got a confirmation within minutes and the fare was exactly as quoted. Will book again.",
        "வாட்ஸ்அப் மூலம் முன்பதிவு செய்வது மிக எளிது, வேகமானது. சில நிமிடங்களில் உறுதிப்படுத்தல் கிடைத்தது. மீண்டும் முன்பதிவு செய்வேன்.",
    ),
    ("review_3_role", "Fallback Review 3 Trip", "Local City Ride", "உள்ஊர் பயணம்"),
    (
        "review_4",
        "Fallback Review 4",
        "We hired a car for our wedding function. The car was well decorated and the driver was very accommodating with our schedule. Thank you Joo Travels!",
        "எங்கள் திருமண நிகழ்ச்சிக்கு கார் வாடகைக்கு எடுத்தோம். கார் அழகாக அலங்கரிக்கப்பட்டிருந்தது, டிரைவர் எங்கள் நேரத்திற்கு ஏற்ப ஒத்துழைத்தார்.",
    ),
    ("review_4_role", "Fallback Review 4 Trip", "Wedding Car Rental", "திருமண கார் வாடகை"),
    (
        "review_5",
        "Fallback Review 5",
        "Great tour package to Pondicherry. The driver knew all the good spots and made our weekend trip memorable and stress-free.",
        "புதுச்சேரிக்கு சிறந்த சுற்றுலா தொகுப்பு. டிரைவருக்கு நல்ல இடங்கள் எல்லாம் தெரியும், எங்கள் வார இறுதி பயணத்தை மறக்க முடியாததாக ஆக்கினார்.",
    ),
    ("review_5_role", "Fallback Review 5 Trip", "Tour Package", "சுற்றுலா தொகுப்பு"),
]

CONTACT_BLOCKS = [
    ("contact_title", "Booking Form: Title", "Book Your Trip", "உங்கள் பயணத்தை முன்பதிவு செய்யவும்"),
    (
        "contact_desc",
        "Booking Form: Description",
        "Fill in your travel details below — we'll open WhatsApp with your booking request ready to send",
        "கீழே உங்கள் பயண விவரங்களை நிரப்பவும் — உங்கள் முன்பதிவு கோரிக்கையுடன் வாட்ஸ்அப் திறக்கப்படும்",
    ),
    ("opt_ask", "Booking Form: 'Just Ask' Option", "Just Ask a Question", "கேள்வி மட்டும் கேட்க"),
    ("opt_book", "Booking Form: 'Book' Option", "Book a Trip", "பயணம் முன்பதிவு செய்ய"),
    ("label_name", "Booking Form: Name Label", "Name*", "பெயர்*"),
    ("ph_name", "Booking Form: Name Placeholder", "Name", "பெயர்"),
    ("label_phone", "Booking Form: Phone Label", "Phone Number*", "தொலைபேசி எண்*"),
    ("ph_phone", "Booking Form: Phone Placeholder", "Phone Number", "தொலைபேசி எண்"),
    ("label_route", "Booking Form: Route Label", "Pickup & Drop Location*", "பிக்-அப் & டிராப் இடம்*"),
    ("ph_route", "Booking Form: Route Placeholder", "e.g. Chennai to Madurai", "எ.கா. சென்னை முதல் மதுரை"),
    (
        "label_message",
        "Booking Form: Message Label",
        "Travel Date, Time & Message*",
        "பயண தேதி, நேரம் & செய்தி*",
    ),
    (
        "ph_message",
        "Booking Form: Message Placeholder",
        "Travel date, time, number of passengers, etc.",
        "பயண தேதி, நேரம், பயணிகள் எண்ணிக்கை போன்றவை",
    ),
    ("send_whatsapp", "Booking Form: Submit Button", "Send via WhatsApp", "வாட்ஸ்அப் மூலம் அனுப்பவும்"),
]

FOOTER_BLOCKS = [
    ("footer_contact", "Footer: Contact Heading", "Contact us:", "எங்களை தொடர்பு கொள்ள:"),
    ("footer_jothi", "Footer: Driver 1 Label", "Jothi (Driver): ", "ஜோதி (டிரைவர்): "),
    ("footer_raja", "Footer: Driver 2 Label", "Raja (Driver): ", "ராஜா (டிரைவர்): "),
    ("footer_area", "Footer: Service Area", "Serving Chennai & Tamil Nadu", "சென்னை & தமிழ்நாடு முழுவதும் சேவை"),
    (
        "footer_whatsapp_btn",
        "Footer: WhatsApp Button",
        "Book Instantly on WhatsApp",
        "வாட்ஸ்அப்பில் உடனே முன்பதிவு செய்யவும்",
    ),
    ("footer_rights", "Footer: Copyright Text", "All Rights Reserved.", "அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை."),
]


def seed_content(apps, schema_editor):
    ContentBlock = apps.get_model("content", "ContentBlock")
    ContactInfo = apps.get_model("content", "ContactInfo")

    for section, blocks in (("home", HOME_BLOCKS), ("contact", CONTACT_BLOCKS), ("footer", FOOTER_BLOCKS)):
        for order, (key, label, en, ta) in enumerate(blocks, start=1):
            ContentBlock.objects.update_or_create(
                key=key,
                defaults={
                    "section": section,
                    "label": label,
                    "value_en": en,
                    "value_ta": ta,
                    "order": order * 10,
                },
            )

    ContactInfo.objects.update_or_create(
        pk=1,
        defaults={
            "whatsapp_number": "919524788173",
            "driver1_name": "Jothi",
            "driver1_phone": "+919524788173",
            "driver2_name": "Raja",
            "driver2_phone": "+919843554143",
        },
    )


def unseed_content(apps, schema_editor):
    ContentBlock = apps.get_model("content", "ContentBlock")
    ContactInfo = apps.get_model("content", "ContactInfo")
    ContentBlock.objects.all().delete()
    ContactInfo.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_content, unseed_content),
    ]
