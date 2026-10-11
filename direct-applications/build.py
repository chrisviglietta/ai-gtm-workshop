#!/usr/bin/env python3
"""Builds the Direct Applications static site into ./site.

All page content lives in this file. Edit the dicts below, then run:
    python3 build.py
Placeholders still to confirm are wrapped in tbd("...") so they render as yellow tags.
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")

BRAND = "Direct Applications"
CITY = "Los Angeles"


def tbd(text):
    return f'<span class="tbd">{html.escape(text)}</span>'


PHONE = tbd("Phone TBD")
EMAIL = tbd("Email TBD")
ADDRESS = tbd("New shop address TBD") + f"<br>{CITY}, CA"
HOURS = "Mon–Fri production, weekend rush by arrangement " + tbd("Confirm hours")

# --------------------------------------------------------------------------- icons
ICONS = {
    "uv": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="8" width="36" height="10" rx="1"/><path d="M14 18v4M24 18v4M34 18v4"/><path d="M12 28l2 3M24 28v4M36 28l-2 3" stroke-dasharray="2 3"/><rect x="4" y="36" width="40" height="6" rx="1" fill="currentColor" fill-opacity=".15"/></svg>',
    "cut": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2"><path d="M24 4v14"/><path d="M19 4h10l-2 8h-6z"/><path d="M24 18l0 6" stroke-dasharray="1 2"/><path d="M6 30c6-6 12 6 18 0s12 6 18 0" stroke-dasharray="4 3"/><rect x="4" y="36" width="40" height="6" rx="1" fill="currentColor" fill-opacity=".15"/></svg>',
    "engrave": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 4h8v6l3 6v26a2 2 0 0 1-2 2H19a2 2 0 0 1-2-2V16l3-6z"/><path d="M21 26h6M21 30h6" /><path d="M8 22a16 16 0 0 0 0 12M40 22a16 16 0 0 1 0 12"/><path d="M6 32l2 2 2-2M42 24l-2-2-2 2"/></svg>',
    "printcut": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2"><circle cx="24" cy="24" r="10" fill="currentColor" fill-opacity=".15"/><path d="M24 17l2 5h5l-4 3 2 5-5-3-5 3 2-5-4-3h5z"/><circle cx="24" cy="24" r="16" stroke-dasharray="4 3"/><path d="M4 4h6M4 4v6M44 44h-6M44 44v-6"/></svg>',
    "oversized": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2"><rect x="10" y="10" width="34" height="26" rx="1" fill="currentColor" fill-opacity=".15"/><path d="M10 42h34M10 40v4M44 40v4"/><path d="M4 10v26M2 10h4M2 36h4"/><path d="M16 18h12M16 24h20"/></svg>',
    "check": '<svg viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="18" r="15" stroke-dasharray="3 3"/><path d="M11 18.5l5 5 9-11"/></svg>',
}

# --------------------------------------------------------------------------- content
SOLUTIONS = [
    {
        "slug": "custom-acrylic",
        "nav": "Custom Acrylic Pieces",
        "short": "Covers, menus, table numbers, boxes, and panels. Our largest product line.",
        "title": "Custom Acrylic Printing, Laser Cutting & Engraving in Los Angeles",
        "desc": "Custom acrylic pieces printed, laser cut, and engraved in Los Angeles: printed covers and panels, menus, table numbers, boxes, inserts, and mirror acrylic. Short runs and rush available.",
        "h1": "Custom Acrylic, Cut, Printed, and Engraved",
        "lede": "Acrylic is what we make most. We print it, cut it, engrave it, and assemble it in one shop, so a printed cover or a multi-layer insert comes back from one vendor on one schedule.",
        "covers": [
            ("Printed acrylic covers and panels", "Full-color UV print on clear, frosted, or colored sheet"),
            ("Menus", "Single panels or multi-page, printed one or both sides"),
            ("Table numbers", "Freestanding, engraved, or printed with a white underlay"),
            ("Boxes and inserts", "Cut and assembled, with multi-layer inserts sized to the product"),
            ("Display pieces", "Risers, blocks, plinths, and branded panels"),
            ("Mirror and colored acrylic", "Gold, silver, and tinted sheet for a premium finish"),
        ],
        "proof": [
            ("Printed on both sides", "Front image, back image, and white ink between them, registered to the cut."),
            ("Mounted and assembled", "Standoffs, magnets, and hardware installed before it ships."),
            ("Multi-layer inserts", "Stacked, cut-to-fit layers that hold product in place."),
        ],
        "caps": ["uv-printing", "laser-cutting", "laser-engraving"],
        "audience": "Brands, agencies, hospitality groups, and planners who need acrylic that looks finished out of the box.",
        "tickets": [
            ("Printed acrylic menu covers", "Clear cast acrylic · UV print, both sides · cut to shape", "120 pcs", "Placeholder"),
            ("Mirror acrylic display panel", "Gold mirror acrylic · engraved logo · standoffs installed", "40 pcs", "Placeholder"),
            ("Product box with insert", "Frosted acrylic box · 3-layer cut insert · assembled", "250 pcs", "Placeholder"),
        ],
        "cta": "Upload your artwork for a quote",
    },
    {
        "slug": "displays-packaging",
        "nav": "Retail Displays and Packaging",
        "short": "Point-of-sale displays, branded boxes, and inserts for brand programs.",
        "title": "Retail Displays & Custom Packaging Production | Los Angeles",
        "desc": "Short-run retail displays and custom packaging produced in Los Angeles for brands, packaging firms, and agencies. POS displays, branded boxes, mirror acrylic, insert cutting, and sample runs.",
        "h1": "Displays and Packaging for Brands and Packaging Firms",
        "lede": "Packaging firms and agencies send us the parts they don't make in-house: printed acrylic, cut inserts, display components, and sample runs. We build to your spec and ship on your timeline.",
        "covers": [
            ("Point-of-sale and in-store displays", "Counter units, shelf talkers, risers, and testers"),
            ("Branded covers and boxes", "Printed lids, sleeves, and acrylic boxes"),
            ("Mirror-acrylic displays", "Reflective finishes for beauty and luxury programs"),
            ("Cardboard and insert cutting", "Laser-cut board and foam inserts, no die required"),
            ("Sample runs", "Pre-production samples for client sign-off"),
            ("Program reorders", "The same part, cut from the same file, every season"),
        ],
        "proof": [
            ("Brand programs", "We've produced work for major beauty, footwear, and entertainment brand programs. " + tbd("Confirm which brands can be named")),
            ("No die costs", "Laser-cut inserts and board let you change a design without retooling."),
            ("White-label friendly", "We ship under your name and keep the client relationship yours."),
        ],
        "caps": ["uv-printing", "laser-cutting", "print-and-cut", "oversized-specialty"],
        "audience": "Packaging firms and agencies that subcontract production, and brand teams running in-store programs.",
        "tickets": [
            ("Counter display for a beauty launch", "Mirror acrylic · UV print · cut and assembled", "300 units", "Placeholder"),
            ("Laser-cut box inserts", "Corrugated board · contour cut · no die", "2,000 pcs", "Placeholder"),
            ("Presentation sample set", "Printed lids · acrylic insert · hand assembled", "6 sets", "Placeholder"),
        ],
        "cta": "Request trade pricing",
        "cta_href": "trade.html",
    },
    {
        "slug": "events-weddings",
        "nav": "Event and Wedding Signage",
        "short": "Table numbers, menus, seating charts, invitations, and favors.",
        "title": "Acrylic Wedding & Event Signage, Menus and Invitations | Los Angeles",
        "desc": "Custom acrylic event and wedding signage in Los Angeles: table numbers, menus, seating charts, acrylic invitations, photo moments, and favors. Rush and weekend turnaround.",
        "h1": "Signage, Menus, and Invitations for Events",
        "lede": "Events have a fixed date, so we plan backward from yours. Tell us when the doors open and we'll tell you when artwork needs to be final.",
        "covers": [
            ("Table numbers", "Printed or engraved, freestanding or in stands"),
            ("Menus", "Acrylic, wood, or paper, printed to match the suite"),
            ("Seating charts", "Large-format panels for entrances and foyers"),
            ("Invitations on acrylic", "Clear or frosted, printed with white ink for contrast"),
            ("Photo moments and event builds", "Backdrops, cutout lettering, and branded walls"),
            ("Favors and keepsakes", "Engraved and printed pieces guests take home"),
        ],
        "proof": [
            ("Rush and weekend turnaround", "When the date moves up, we run on the weekend. " + tbd("Publish rush policy")),
            ("Planner partnerships", "Planners get a single point of contact and repeat pricing across events."),
            ("One look, every piece", "Menus, numbers, and signage printed together so colors match."),
        ],
        "caps": ["uv-printing", "laser-cutting", "laser-engraving"],
        "audience": "Event and wedding planners, venues, and couples who need signage that arrives on time.",
        "tickets": [
            ("Wedding table numbers", "Clear acrylic · white + color print · cut stands", "24 pcs", "Placeholder"),
            ("Seating chart panel", "Frosted acrylic · large-format print", "1 pc", "Placeholder"),
            ("Acrylic invitations", "Clear acrylic · UV print with white underlay", "150 pcs", "Placeholder"),
        ],
        "cta": "Tell us your event date",
    },
    {
        "slug": "awards-recognition",
        "nav": "Awards and Recognition",
        "short": "Acrylic awards, engraved plaques, name plates, and annual programs.",
        "title": "Custom Awards, Plaques & Recognition Programs | Los Angeles",
        "desc": "Custom acrylic awards, engraved plaques, name plates, and badges made in Los Angeles. Recurring award programs at stable unit pricing.",
        "h1": "Awards, Plaques, and Recognition Programs",
        "lede": "Many of our award customers come back every year with the same design and new names. We keep your files on hold so a reorder is a list of names, not a new project.",
        "covers": [
            ("Acrylic awards", "Cut shapes, printed color, and engraved names"),
            ("Engraved plaques and name plates", "Wood, acrylic, and metal"),
            ("Badges", "Name badges and ID pieces for staff and events"),
            ("Recurring program awards", "Annual, quarterly, or monthly awards from a saved design"),
        ],
        "proof": [
            ("Stable unit pricing", "Repeat annual programs at the same unit price each cycle."),
            ("Names from a spreadsheet", "Send a list, and we personalize each piece from it."),
            ("Reserve capacity early", "Book ahead of graduation, retirement, and year-end recognition seasons."),
        ],
        "caps": ["laser-engraving", "uv-printing", "laser-cutting"],
        "audience": "HR and people teams, schools, associations, and companies that run recognition every year.",
        "tickets": [
            ("Annual sales awards", "Thick cast acrylic · UV print · engraved names", "35 pcs", "Placeholder"),
            ("Retirement plaques", "Walnut base · engraved brass plate", "12 pcs", "Placeholder"),
            ("Staff name plates", "Two-tone acrylic · engraved", "80 pcs", "Placeholder"),
        ],
        "cta": "Set up a recurring program",
        "season": "Graduation, retirement, and year-end recognition seasons book up. Reserve production capacity ahead of time and lock your date.",
    },
    {
        "slug": "branded-gifts",
        "nav": "Personalized and Branded Gifts",
        "short": "Engraved bottles and glassware, coasters, and gift box lids.",
        "title": "Laser Engraved Bottles, Glassware & Branded Gifts | Los Angeles",
        "desc": "Custom branded gifts made to order in Los Angeles: laser engraving on bottles and glassware, printed coasters, gift box lids, and personalized corporate gifts. Small minimums.",
        "h1": "Custom Branded Gifts Made to Order",
        "lede": "We engrave and print on the item itself, including bottles, glasses, and other round pieces most shops can't handle. Bring your own product or let us source it.",
        "covers": [
            ("Engraved bottles", "Wine, spirits, and water bottles on our rotary attachment"),
            ("Glassware", "Rocks glasses, pint glasses, and stemware"),
            ("Printed coasters", "Acrylic, wood, and cork, full color"),
            ("Gift box lids", "Printed or engraved lids for corporate gift boxes"),
            ("Personalized items", "Individual names for client gifts and team swag"),
            ("Customer-supplied items", "Send us your product and we'll test a sample first"),
        ],
        "proof": [
            ("Rotary engraving", "Cylindrical items engrave all the way around, not just on a flat spot."),
            ("Small minimums", "Ten gifts or a few hundred. " + tbd("Confirm minimum order")),
            ("Every name different", "Personalize each piece from a list at no extra setup."),
        ],
        "caps": ["laser-engraving", "uv-printing"],
        "audience": "Corporate gifting teams, agencies running swag programs, and brands sending client gifts.",
        "tickets": [
            ("Client holiday gift bottles", "Wine bottles · rotary engraved logo + name", "60 pcs", "Placeholder"),
            ("Branded coaster sets", "Walnut · UV print · boxed in sets of 4", "200 sets", "Placeholder"),
            ("Gift box lids", "Printed lid · engraved message", "120 pcs", "Placeholder"),
        ],
        "cta": "Get a gift quote",
    },
    {
        "slug": "prototyping-short-run",
        "nav": "Prototyping and Short-Run Production",
        "short": "Prototype rounds, sampling, and runs from 1 to 2,000 units.",
        "title": "Prototype Laser Cutting & Short-Run Production | Los Angeles",
        "desc": "Prototype laser cutting and short-run production in Los Angeles. Multi-round prototyping, custom boxes with hinges and handles, sampling, and runs from 1 to 2,000 units.",
        "h1": "From One Prototype to a Few Thousand",
        "lede": "Start with one piece. Change it, cut it again, and when it's right, run the quantity you need from the same file. No tooling, no minimum to get the first sample.",
        "covers": [
            ("Prototype rounds", "Fast revisions while the design is still moving"),
            ("Custom boxes", "Boxes with hinges, handles, and fitted lids"),
            ("Sampling", "Small batches for testing, photography, or client review"),
            ("Small production runs", "Tens to a few thousand units"),
            ("Repeat parts", "Brackets, housings, and enclosures cut to order"),
        ],
        "proof": [
            ("Multi-round prototyping", "We expect a few rounds and price for it."),
            ("1 to 2,000 units", "The same file and setup carry from prototype to production."),
            ("Operators who give feedback", "We flag tolerances, kerf, and material issues before the run."),
        ],
        "caps": ["laser-cutting", "oversized-specialty", "uv-printing"],
        "audience": "Product designers, startups, and engineering teams who need parts before they need a factory.",
        "tickets": [
            ("Hinged presentation box", "Birch plywood · laser cut · 3 prototype rounds", "1 → 400 pcs", "Placeholder"),
            ("Electronics enclosure", "Black acrylic · cut and engraved labels", "50 pcs", "Placeholder"),
            ("Mounting brackets", "Light-gauge metal · sheared", "500 pcs", "Placeholder"),
        ],
        "cta": "Start with a prototype",
    },
]

CAPS = [
    {
        "slug": "uv-printing",
        "icon": "uv",
        "nav": "UV Printing",
        "short": "Full color and white ink direct to rigid and unusual materials.",
        "title": "UV Printing on Acrylic, Wood & Metal | Los Angeles",
        "desc": "UV flatbed printing in Los Angeles. Print directly on acrylic, metal, wood, linen, bookcloth, envelopes, and customer-supplied items. White ink, both-sides printing, and short runs.",
        "h1": "UV Printing on Almost Anything Flat",
        "equipment": "Mutoh XPJ-1642UF flatbed with ionizer",
        "what": "Our flatbed UV printer cures ink instantly with UV light, so it prints directly onto rigid and unusual surfaces without a transfer or a label. The ionizer removes static before printing, which keeps dust off acrylic and gives a cleaner print.",
        "points": [
            ("Direct to substrate", "No stickers or laminates; the ink is on the piece."),
            ("White ink", "A white underlay makes colors read on clear and dark materials."),
            ("Customer-supplied items", "Send us your blanks and we'll test a sample first."),
        ],
        "materials": ["Acrylic (clear, frosted, colored, mirror)", "Metal", "Wood and plywood", "Linen and bookcloth", "Envelopes and paper stock", "Customer-supplied items"],
        "specs": [("Max print area", "Spec to confirm"), ("Max material thickness", "Spec to confirm"), ("Ink", "CMYK + white " + tbd("Confirm varnish")), ("Resolution", "Spec to confirm")],
        "jobs": [("Printed acrylic menus, both sides", "custom-acrylic"), ("Linen-wrapped box lids", "displays-packaging"), ("Acrylic invitations", "events-weddings")],
        "solutions": ["custom-acrylic", "displays-packaging", "events-weddings", "branded-gifts"],
    },
    {
        "slug": "laser-cutting",
        "icon": "cut",
        "nav": "Laser Cutting",
        "short": "Acrylic, wood, paper, and board, on two CO2 machines.",
        "title": "Laser Cutting Service in Los Angeles | Acrylic, Wood, Paper",
        "desc": "Precision laser cutting service in Los Angeles for acrylic, wood, paper, and cardboard. Two CamFive CO2 laser systems for prototypes and production volume.",
        "h1": "Laser Cutting with Capacity to Spare",
        "equipment": "Two CamFive CO2 systems (double-head and deep-table)",
        "what": "We run two CO2 laser systems. The double-head machine cuts two parts at once for production runs, and the deep-table machine handles larger sheets and taller pieces. Two machines also mean one job doesn't stop while another runs.",
        "points": [
            ("Clean edges", "Flame-polished edges on cast acrylic, no sanding required."),
            ("Double-head output", "Two heads cutting in parallel for faster production runs."),
            ("No tooling", "Change the file, not the die. Every revision is a new cut file."),
        ],
        "materials": ["Cast and extruded acrylic", "Wood and plywood", "Paper and card stock", "Corrugated cardboard and chipboard", "Foam for inserts " + tbd("Confirm"), "Fabric and leather " + tbd("Confirm")],
        "specs": [("Bed size, double-head", "Spec to confirm"), ("Bed size, deep-table", "Spec to confirm"), ("Max acrylic thickness", "Spec to confirm"), ("Max wood thickness", "Spec to confirm")],
        "jobs": [("Multi-layer acrylic inserts", "custom-acrylic"), ("Corrugated box inserts, no die", "displays-packaging"), ("Hinged plywood boxes", "prototyping-short-run")],
        "solutions": ["custom-acrylic", "displays-packaging", "prototyping-short-run", "events-weddings"],
    },
    {
        "slug": "laser-engraving",
        "icon": "engrave",
        "nav": "Laser and Rotary Engraving",
        "short": "Flat and round items, including bottles and glassware.",
        "title": "Laser Engraving Bottles, Glassware & Plaques | Los Angeles",
        "desc": "Laser and rotary engraving in Los Angeles. Personalize flat and cylindrical items, including bottles, glassware, plaques, and footwear, with small minimums.",
        "h1": "Laser and Rotary Engraving, Flat or Round",
        "equipment": "Epilog laser engraver with rotary attachment",
        "what": "Our Epilog engraver marks names, logos, and artwork into the surface of a piece. The rotary attachment turns bottles, glasses, and tumblers under the laser, so the engraving wraps around the curve instead of sitting on one flat spot.",
        "points": [
            ("Rotary attachment", "Bottles, glassware, and other cylinders engraved evenly around the curve."),
            ("Personalization", "A different name on every piece, from your list."),
            ("Unusual items", "Footwear, leather goods, and customer-supplied products."),
        ],
        "materials": ["Glass and glassware", "Wine and spirits bottles", "Wood", "Acrylic", "Anodized and coated metal", "Leather and footwear"],
        "specs": [("Engraving area", "Spec to confirm"), ("Rotary max diameter", "Spec to confirm"), ("Personalization file", "CSV or spreadsheet of names"), ("Minimum order", "Spec to confirm")],
        "jobs": [("Engraved wine bottles for client gifts", "branded-gifts"), ("Annual award names", "awards-recognition"), ("Engraved table numbers", "events-weddings")],
        "solutions": ["branded-gifts", "awards-recognition", "events-weddings", "custom-acrylic"],
    },
    {
        "slug": "print-and-cut",
        "icon": "printcut",
        "nav": "Print and Cut",
        "short": "Stickers, labels, and decals printed and contour cut in one pass.",
        "title": "Custom Stickers, Labels & Decals, Print and Cut | Los Angeles",
        "desc": "Print and cut in Los Angeles: custom stickers, labels, decals, and film printed and contour cut in one pass on a Mimaki UCJV300-160.",
        "h1": "Print and Cut in One Pass",
        "equipment": "Mimaki UCJV300-160 print-and-cut",
        "what": "Our Mimaki prints on roll media and then cuts around the printed shape on the same machine. Stickers, labels, and decals come off with the cut registered to the print, with no second setup.",
        "points": [
            ("Contour cut to the print", "Any shape, cut along the edge of your artwork."),
            ("Roll media", "Vinyl, film, and label stock for short and long runs."),
            ("Pairs with rigid work", "Labels and decals that match the printed acrylic in the same order."),
        ],
        "materials": ["Vinyl", "Clear and frosted film", "Label stock", "Window and wall decal media", "Backlit film " + tbd("Confirm")],
        "specs": [("Max print width", "Spec to confirm"), ("Cut types", "Kiss cut and contour cut " + tbd("Confirm through-cut")), ("Cut line", "Spot color named CutContour"), ("Minimum order", "Spec to confirm")],
        "jobs": [("Product labels for a sample run", "displays-packaging"), ("Window decals for a pop-up", "events-weddings"), ("Die-cut logo stickers", "branded-gifts")],
        "solutions": ["displays-packaging", "branded-gifts", "events-weddings"],
    },
    {
        "slug": "oversized-specialty",
        "icon": "oversized",
        "nav": "Oversized and Specialty Materials",
        "short": "Large-format cutting, plywood, and light metal work.",
        "title": "Oversized Laser Cutting, Plywood & Light Metal | Los Angeles",
        "desc": "Oversized laser cutting in Los Angeles on a deep-table CamFive system, plus plywood and light metal work on an Accu Cutter metal shear.",
        "h1": "Oversized Sheets and Specialty Materials",
        "equipment": "CamFive deep-table laser and Accu Cutter metal shear",
        "what": "Our deep-table laser takes sheets larger than most trade shops can cut, so big signs and display panels come out as one piece instead of seamed sections. The metal shear handles light-gauge sheet for brackets and simple parts.",
        "points": [
            ("Fewer seams", "Large panels cut in one piece."),
            ("Plywood", "Structural and decorative plywood for builds and fixtures."),
            ("Light metal", "Sheared light-gauge sheet for brackets and plates."),
        ],
        "materials": ["Large-format acrylic sheet", "Plywood", "MDF " + tbd("Confirm"), "Light-gauge sheet metal", "Foam board and display board"],
        "specs": [("Deep-table bed size", "Spec to confirm"), ("Max sheet thickness", "Spec to confirm"), ("Metal shear width", "Spec to confirm"), ("Max metal gauge", "Spec to confirm")],
        "jobs": [("Large-format seating chart", "events-weddings"), ("In-store display wall", "displays-packaging"), ("Sheared mounting brackets", "prototyping-short-run")],
        "solutions": ["displays-packaging", "events-weddings", "prototyping-short-run"],
    },
]

SOL = {s["slug"]: s for s in SOLUTIONS}
CAP = {c["slug"]: c for c in CAPS}

DIFFS = [
    ("Print, cut, and engrave in one shop", "One vendor, one schedule, one invoice for the whole job."),
    ("Print-and-cut on the same job", "Labels and decals registered to the print."),
    ("Oversized-bed cutting", "Larger sheets than most trade shops can take."),
    ("Rotary engraving", "Bottles, glassware, and other round items."),
    ("Short runs and weekend rush", "Prototype first, then production."),
    ("About 10 years in production", "Operators who catch problems before the run."),
]

WORK = [
    ("Printed acrylic menus", "custom-acrylic", "uv-printing laser-cutting", "Clear cast acrylic", "UV print, both sides · cut", "120 pcs", "4 days"),
    ("Mirror acrylic counter display", "displays-packaging", "uv-printing laser-cutting", "Gold mirror acrylic", "UV print · cut · assembled", "300 units", "2 weeks"),
    ("Wedding table numbers", "events-weddings", "uv-printing laser-cutting", "Clear acrylic", "White + color print · cut stands", "24 pcs", "3 days"),
    ("Annual sales awards", "awards-recognition", "laser-engraving uv-printing", "Thick cast acrylic", "Print · engraved names", "35 pcs", "1 week"),
    ("Engraved client gift bottles", "branded-gifts", "laser-engraving", "Wine bottles", "Rotary engraving", "60 pcs", "5 days"),
    ("Hinged plywood box prototype", "prototyping-short-run", "laser-cutting", "Birch plywood", "Laser cut · 3 rounds", "1 → 400 pcs", "3 weeks"),
    ("Corrugated box inserts", "displays-packaging", "laser-cutting oversized-specialty", "Corrugated board", "Contour cut, no die", "2,000 pcs", "1 week"),
    ("Acrylic invitations", "events-weddings", "uv-printing", "Frosted acrylic", "UV print with white underlay", "150 pcs", "1 week"),
    ("Product sample labels", "displays-packaging", "print-and-cut", "Clear label film", "Print and contour cut", "500 pcs", "2 days"),
    ("Engraved staff name plates", "awards-recognition", "laser-engraving laser-cutting", "Two-tone acrylic", "Cut · engraved", "80 pcs", "4 days"),
    ("Printed walnut coasters", "branded-gifts", "uv-printing laser-cutting", "Walnut", "UV print · cut", "200 sets", "1 week"),
    ("Large-format seating chart", "events-weddings", "oversized-specialty uv-printing", "Frosted acrylic", "Large-format print · cut", "1 pc", "2 days"),
]

# --------------------------------------------------------------------------- layout
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wght@400..700&display=swap">'

BRAND_MARK = '<svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><rect x="1" y="1" width="30" height="30" rx="2" fill="var(--ink)"/><rect x="7" y="7" width="12" height="12" fill="var(--cyan)"/><rect x="13" y="13" width="12" height="12" fill="none" stroke="var(--magenta)" stroke-width="1.6" stroke-dasharray="2.6 2"/><circle cx="25" cy="7" r="2" fill="var(--yellow)"/></svg>'


def brand_block():
    return f'<a class="brand" href="index.html">{BRAND_MARK}<span>Direct Applications<small>Print · Cut · Engrave · LA</small></span></a>'


def header(current):
    def cur(slug):
        return ' aria-current="page"' if slug == current else ""

    sol_links = "".join(f'<a href="{s["slug"]}.html"{cur(s["slug"])}>{s["nav"]}<span>{s["short"]}</span></a>' for s in SOLUTIONS)
    cap_links = "".join(f'<a href="{c["slug"]}.html"{cur(c["slug"])}>{c["nav"]}<span>{c["short"]}</span></a>' for c in CAPS)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
{brand_block()}
<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Main">
  <div class="nav-item"><button aria-expanded="false">What We Make</button><div class="menu" hidden>{sol_links}<a class="menu-all" href="what-we-make.html">All solutions →</a></div></div>
  <div class="nav-item"><button aria-expanded="false">How We Make It</button><div class="menu" hidden>{cap_links}<a class="menu-all" href="how-we-make-it.html">All capabilities →</a></div></div>
  <a href="trade.html"{cur("trade")}>Trade Program</a>
  <a href="work.html"{cur("work")}>Work</a>
  <a href="about.html"{cur("about")}>About</a>
  <a class="btn" href="quote.html">Get a Quote</a>
</nav>
</div></header>"""


def diffs_section():
    items = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in DIFFS)
    return f"""<section class="rule-top"><div class="wrap">
<div class="section-head"><span class="eyebrow">Why one shop</span><h2>One vendor for the whole job</h2></div>
<div class="diff">{items}</div>
</div></section>"""


def footer():
    sols = "".join(f'<li><a href="{s["slug"]}.html">{s["nav"]}</a></li>' for s in SOLUTIONS)
    caps = "".join(f'<li><a href="{c["slug"]}.html">{c["nav"]}</a></li>' for c in CAPS)
    return f"""<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
  <div class="foot-brand">{brand_block()}<p>Custom printed, laser-cut, and engraved pieces, made fast and in small runs in Los Angeles.</p>
  <ul class="contact-list"><li>{ADDRESS}</li><li>{PHONE} · {EMAIL}</li></ul></div>
  <div><h4>What we make</h4><ul>{sols}</ul></div>
  <div><h4>How we make it</h4><ul>{caps}</ul></div>
  <div><h4>Company</h4><ul><li><a href="trade.html">Trade Program</a></li><li><a href="work.html">Work</a></li><li><a href="guide.html">Materials and Artwork Guide</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="quote.html">Get a Quote</a></li></ul></div>
</div>
<div class="foot-base"><span>© <span data-year>2026</span> {BRAND}. Made in {CITY}.</span><span>UV print · Laser cut · Engrave · Print and cut</span></div>
</div></footer>
<div class="mobile-cta"><a class="btn" href="quote.html">Get a Quote</a><a class="btn btn--ghost" href="work.html">See Work</a></div>"""


def cta_band(title, text, label, href="quote.html", ghost=None):
    g = f'<a class="btn btn--ghost" href="{ghost[1]}">{ghost[0]}</a>' if ghost else ""
    return f"""<section class="cta-band"><div class="wrap">
<div class="stack"><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn arrow" href="{href}">{label} </a>{g}</div>
</div></section>"""


def page(slug, title, desc, body, current=None, artifact=False, extra_head=""):
    head = f"""<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{FONTS}
<link rel="stylesheet" href="assets/styles.css">{extra_head}"""
    content = f"""{header(current or slug)}
<main id="main">
{body}
{diffs_section() if slug not in ("quote", "contact") else ""}
</main>
{footer()}
<script src="assets/site.js"></script>"""
    if artifact:
        # Artifact host adds the doctype/head/body skeleton for the entry page.
        return f"{head}\n{content}\n"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body{' class="no-mobile-cta"' if slug == "quote" else ""}>
{content}
</body>
</html>
"""


def photo(shot, cls=""):
    return f'<div class="photo {cls}" role="img" aria-label="Photo placeholder: {html.escape(shot)}"><span class="shot"><b>Shot list</b> · {html.escape(shot)}</span></div>'


def crumbs(*pairs):
    parts = ['<a href="index.html">Home</a>']
    for label, href in pairs:
        parts.append("/")
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


# --------------------------------------------------------------------------- home
HERO_ART = """<div class="sheet-art" aria-hidden="true">
<svg viewBox="0 0 500 400">
  <g stroke="var(--ink-2)" stroke-width="1" fill="none">
    <path d="M20 40h-16M40 20v-16M480 40h16M460 20v-16M20 360h-16M40 380v16M480 360h16M460 380v16"/>
    <circle cx="250" cy="14" r="8"/><path d="M238 14h24M250 2v24"/>
    <circle cx="250" cy="386" r="8"/><path d="M238 386h24M250 374v24"/>
  </g>
  <rect x="40" y="40" width="420" height="320" rx="6" fill="var(--sheet)" stroke="var(--rule)" stroke-width="1.5"/>
  <rect x="40" y="40" width="420" height="320" rx="6" fill="var(--cyan)" fill-opacity=".05"/>
  <!-- printed piece: arched menu -->
  <path d="M110 330V150a90 90 0 0 1 180 0v180z" fill="var(--cyan)" fill-opacity=".14"/>
  <path d="M128 316V152a72 72 0 0 1 144 0v164z" fill="var(--sheet)"/>
  <g fill="var(--ink)"><rect x="160" y="140" width="80" height="9" rx="1"/></g>
  <g fill="var(--ink-2)"><rect x="150" y="172" width="100" height="4"/><rect x="164" y="182" width="72" height="4"/><rect x="150" y="206" width="100" height="4"/><rect x="170" y="216" width="60" height="4"/><rect x="150" y="240" width="100" height="4"/><rect x="160" y="250" width="80" height="4"/><rect x="150" y="274" width="100" height="4"/></g>
  <circle cx="200" cy="114" r="10" fill="var(--magenta)" fill-opacity=".85"/>
  <path class="contour" d="M100 340V150a100 100 0 0 1 200 0v190z" fill="none" stroke="var(--magenta)" stroke-width="2"/>
  <!-- engraved round tag -->
  <circle cx="380" cy="130" r="48" fill="var(--sheet)" stroke="var(--ink)" stroke-width="1.5"/>
  <circle cx="380" cy="130" r="40" fill="none" stroke="var(--ink-2)" stroke-dasharray="1 3"/>
  <text x="380" y="126" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="11" fill="var(--ink)">TABLE</text>
  <text x="380" y="148" text-anchor="middle" font-family="Archivo, sans-serif" font-weight="800" font-size="24" fill="var(--ink)">12</text>
  <circle class="contour" cx="380" cy="130" r="56" fill="none" stroke="var(--magenta)" stroke-width="2"/>
  <!-- labels -->
  <g font-family="IBM Plex Mono, monospace" font-size="10" fill="var(--ink-2)">
    <path d="M100 352h200" stroke="var(--ink-2)"/><path d="M100 347v10M300 347v10" stroke="var(--ink-2)"/>
    <text x="200" y="348" text-anchor="middle" dy="-4">CUT PATH</text>
    <text x="336" y="230">UV PRINT  · CMYK+W</text>
    <text x="336" y="246">LASER CUT · CONTOUR</text>
    <text x="336" y="262">ENGRAVE   · RASTER</text>
    <rect x="320" y="223" width="8" height="8" fill="var(--cyan)"/>
    <rect x="320" y="239" width="8" height="8" fill="none" stroke="var(--magenta)" stroke-dasharray="2 1.5"/>
    <rect x="320" y="255" width="8" height="8" fill="var(--ink)"/>
  </g>
</svg></div>"""


def home(artifact=False):
    tiles = "".join(
        f'<a class="tile" href="{s["slug"]}.html"><span class="mono">{i + 1:02d} / 06</span><h3>{s["nav"]}</h3><p>{s["short"]}</p><span class="go">Learn more</span></a>'
        for i, s in enumerate(SOLUTIONS)
    )
    caps = "".join(
        f'<a class="cap" href="{c["slug"]}.html">{ICONS[c["icon"]]}<h3>{c["nav"]}</h3><p>{c["short"]}</p><span class="mono">{c["equipment"]}</span></a>'
        for c in CAPS
    )
    featured = "".join(work_card(w) for w in WORK[:6])
    body = f"""<section class="hero"><div class="wrap hero-grid">
  <div class="hero-copy">
    <span class="eyebrow">UV print · Laser cut · Engrave · {CITY}</span>
    <h1>Printed, <span class="cut">cut</span>, and engraved in <em>{CITY}</em>.</h1>
    <p class="lede">Custom pieces made fast and in small runs. One shop handles the print, the cut, and the engraving, so your job has one vendor and one schedule.</p>
    <div class="btn-row"><a class="btn arrow" href="quote.html">Get a Quote </a><a class="btn btn--ghost" href="work.html">See Our Work</a></div>
  </div>
  {HERO_ART}
</div></section>

<section class="trust"><div class="wrap"><ul>
  <li><b>~10 yrs</b><span>Production experience on the floor</span></li>
  <li><b>1–2,000+</b><span>Units per run, prototype to production</span></li>
  <li><b>Rush</b><span>Weekend turnaround available</span></li>
  <li><b>Made in LA</b><span>Local pickup and delivery {tbd("Service area TBD")}</span></li>
</ul></div></section>

<section><div class="wrap">
  <div class="section-head section-head--split"><div class="stack"><span class="eyebrow">What we make</span><h2>Six things customers order most</h2></div><a class="btn btn--ghost" href="what-we-make.html">All solutions</a></div>
  <div class="tiles">{tiles}</div>
</div></section>

<section class="rule-top"><div class="wrap">
  <div class="section-head section-head--split"><div class="stack"><span class="eyebrow">How we make it</span><h2>Five processes under one roof</h2></div><a class="btn btn--ghost" href="how-we-make-it.html">Equipment and specs</a></div>
  <div class="caps">{caps}</div>
</div></section>

<section class="rule-top"><div class="wrap">
  <div class="section-head section-head--split"><div class="stack"><span class="eyebrow">Featured work</span><h2>Recent jobs off the floor</h2></div><a class="btn btn--ghost" href="work.html">See all work</a></div>
  <div class="work-grid">{featured}</div>
</div></section>

<section class="band"><div class="wrap band-grid">
  <div class="stack"><span class="eyebrow">Trade program</span><h2>Agencies and packaging firms: we're your production floor.</h2>
  <p>Most of our work comes from shops and agencies that bring us their clients' artwork. Get wholesale rates, net terms, and white-label shipping.</p>
  <div class="btn-row"><a class="btn arrow" href="trade.html">Apply for a trade account </a></div></div>
  <ul class="ticks"><li>Wholesale rate card</li><li>Net terms for approved accounts</li><li>Rush and weekend options</li><li>Confidential, white-label production</li><li>Committed-volume and seasonal capacity agreements</li></ul>
</div></section>

<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>From artwork to delivery</h2></div>
  {steps()}
</div></section>

{cta_band("Send us your artwork.", f"We'll reply with a price, a material recommendation, and a ship date. Reach us at {PHONE} or {EMAIL}.", "Get a Quote", ghost=("Contact the shop", "contact.html"))}"""
    ld = '\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Direct Applications","description":"Custom UV printing, laser cutting, and engraving in Los Angeles.","areaServed":"Los Angeles, CA"}</script>'
    return page("index", "Direct Applications | Custom Acrylic, Laser Cutting & UV Printing in Los Angeles",
                "Custom printed, laser-cut, and engraved pieces made fast and in small runs in Los Angeles. UV printing, laser cutting, engraving, and print-and-cut under one roof.",
                body, current="home", artifact=artifact, extra_head=ld)


def steps():
    return """<ol class="steps">
  <li><h3>Send artwork</h3><p>Upload files and tell us quantity, material, and deadline.</p></li>
  <li><h3>Get a quote</h3><p>A price, a material recommendation, and a ship date.</p></li>
  <li><h3>Prototype</h3><p>A sample or proof to approve before the run.</p></li>
  <li><h3>Production</h3><p>Printed, cut, engraved, and assembled in our shop.</p></li>
  <li><h3>Delivery</h3><p>Pickup, local delivery, or shipped to you or your client.</p></li>
</ol>"""


def work_card(w):
    title, sol, proc, mat, process, qty, turn = w
    return f"""<article class="work-card" data-solution="{sol}" data-process="{proc}">
{photo(title)}
<h3>{title}</h3>
<dl><dt>Material</dt><dd>{mat}</dd><dt>Process</dt><dd>{process}</dd><dt>Quantity</dt><dd>{qty}</dd><dt>Turnaround</dt><dd>{turn}</dd></dl>
</article>"""


# --------------------------------------------------------------------------- solution pages
def solution_page(s):
    covers = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in s["covers"])
    proof = "".join(f'<div class="proof-item">{ICONS["check"]}<div><h3 class="h-sm">{a}</h3><p>{b}</p></div></div>' for a, b in s["proof"])
    caps = "".join(f'<a class="pill-link" href="{c}.html">{CAP[c]["nav"]} <span class="mono">{CAP[c]["equipment"].split(" with ")[0]}</span></a>' for c in s["caps"])
    tickets = "".join(
        f"""<article class="ticket"><header><span>JOB TICKET</span><span>{note}</span></header><div class="body">{photo(t)}<h3 class="h-sm">{t}</h3><dl><dt>Spec</dt><dd>{spec}</dd><dt>Qty</dt><dd>{qty}</dd></dl></div></article>"""
        for t, spec, qty, note in s["tickets"]
    )
    cta_href = s.get("cta_href", f"quote.html#{s['slug']}")
    season = ""
    if s.get("season"):
        season = f'<section class="band"><div class="wrap band-grid"><div class="stack"><span class="eyebrow">Seasonal capacity</span><h2>Book your season before it books up.</h2><p>{s["season"]}</p></div><ul class="ticks"><li>Graduation (spring)</li><li>Retirement and service anniversaries</li><li>Year-end recognition (Q4)</li></ul></div></section>'
    body = f"""<section class="page-hero"><div class="wrap hero-grid">
  <div class="hero-copy">{crumbs(("What We Make", "what-we-make.html"), (s["nav"], None))}
  <h1>{s["h1"]}</h1><p class="lede">{s["lede"]}</p>
  <div class="btn-row"><a class="btn arrow" href="{cta_href}">{s["cta"]} </a><a class="btn btn--ghost" href="work.html#{s['slug']}">See examples</a></div></div>
  {photo(s["nav"] + ": finished pieces, raking light, close-up of edge and print", "photo--tall")}
</div></section>

<section><div class="wrap two-col">
  <div class="stack"><span class="eyebrow">What we make</span><h2>What's included</h2><p class="muted">{s["audience"]}</p></div>
  <ul class="covers">{covers}</ul>
</div></section>

<section class="rule-top"><div class="wrap two-col">
  <div class="stack"><span class="eyebrow">Proof points</span><h2>What we do well here</h2></div>
  <div class="proof">{proof}</div>
</div></section>
{season}
<section class="rule-top"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Example jobs</span><h2>Typical orders</h2><p class="muted">Example specs for reference. Photos and real job details will replace these after the shoot.</p></div>
  <div class="tickets">{tickets}</div>
</div></section>

<section class="rule-top"><div class="wrap">
  <div class="section-head"><span class="eyebrow">How we make it</span><h2>Processes used</h2></div>
  <div class="links">{caps}</div>
</div></section>

{cta_band(s["cta"] + ".", "Send files, quantity, and your deadline. We reply with a price, a material recommendation, and a ship date.", s["cta"], cta_href)}"""
    return page(s["slug"], s["title"], s["desc"], body)


# --------------------------------------------------------------------------- capability pages
def cap_page(c):
    points = "".join(f'<div class="proof-item">{ICONS["check"]}<div><h3 class="h-sm">{a}</h3><p>{b}</p></div></div>' for a, b in c["points"])
    mats = "".join(f"<li><b>{m}</b></li>" for m in c["materials"])

    def spec_val(v):
        return tbd(v) if v == "Spec to confirm" else v

    specs = "".join(f"<tr><td>{k}</td><td>{spec_val(v)}</td></tr>" for k, v in c["specs"])
    jobs = "".join(f'<article class="work-card">{photo(j)}<h3>{j}</h3><a class="mono" href="{sol}.html">{SOL[sol]["nav"]} →</a></article>' for j, sol in c["jobs"])
    sols = "".join(f'<a class="tile" href="{s}.html"><h3>{SOL[s]["nav"]}</h3><p>{SOL[s]["short"]}</p><span class="go">Learn more</span></a>' for s in c["solutions"])
    cols = 2 if len(c["solutions"]) % 3 and len(c["solutions"]) % 2 == 0 else 3
    body = f"""<section class="page-hero"><div class="wrap hero-grid">
  <div class="hero-copy">{crumbs(("How We Make It", "how-we-make-it.html"), (c["nav"], None))}
  <span class="eyebrow">{c["equipment"]}</span>
  <h1>{c["h1"]}</h1><p class="lede">{c["what"]}</p>
  <div class="btn-row"><a class="btn arrow" href="quote.html">Get a quote </a><a class="btn btn--ghost" href="guide.html">Artwork guide</a></div></div>
  {photo(c["equipment"] + " running, operator in frame", "photo--tall")}
</div></section>

<section><div class="wrap two-col">
  <div class="stack"><span class="eyebrow">What it does</span><h2>Why customers use it</h2></div>
  <div class="proof">{points}</div>
</div></section>

<section class="rule-top"><div class="wrap two-col">
  <div class="stack"><span class="eyebrow">Materials</span><h2>Materials we work with</h2><p class="muted">Don't see yours? Send a sample and we'll test it.</p></div>
  <ul class="covers">{mats}</ul>
</div></section>

<section class="rule-top"><div class="wrap two-col">
  <div class="stack"><span class="eyebrow">Max sizes and specs</span><h2>Sizes and limits</h2><p class="muted">Exact figures are being confirmed with the shop before launch.</p></div>
  <div class="table-wrap"><table><thead><tr><th>Spec</th><th>Value</th></tr></thead><tbody><tr><td>Equipment</td><td>{c["equipment"]}</td></tr>{specs}</tbody></table></div>
</div></section>

<section class="rule-top"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Example jobs</span><h2>What we run on it</h2></div>
  <div class="work-grid">{jobs}</div>
</div></section>

<section class="rule-top"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Related solutions</span><h2>Where it shows up</h2></div>
  <div class="tiles{' tiles--2' if cols == 2 else ''}">{sols}</div>
</div></section>

{cta_band("Have a file ready?", "Send it over with quantity and deadline, and we'll quote it on this process or suggest a better one.", "Get a Quote")}"""
    return page(c["slug"], c["title"], c["desc"], body)


# --------------------------------------------------------------------------- hub pages
def what_we_make():
    tiles = "".join(f'<a class="tile" href="{s["slug"]}.html"><span class="mono">{i + 1:02d} / 06</span><h3>{s["nav"]}</h3><p>{s["short"]}</p><span class="go">Learn more</span></a>' for i, s in enumerate(SOLUTIONS))
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("What We Make", None))}
<h1>What We Make</h1><p class="lede">Six product lines, ordered by what customers buy most. Each one uses the same shop and the same operators.</p></div></div></section>
<section><div class="wrap"><div class="tiles">{tiles}</div></div></section>
{cta_band("Not sure where your project fits?", "Describe it and send what you have. We'll tell you how we'd make it.", "Get a Quote")}"""
    return page("what-we-make", "What We Make | Custom Acrylic, Displays, Signage, Awards & Gifts | Direct Applications",
                "Custom acrylic, retail displays and packaging, event signage, awards, branded gifts, and short-run production, made in Los Angeles.", body)


def how_we_make_it():
    rows = "".join(f'<tr><td><a href="{c["slug"]}.html">{c["nav"]}</a></td><td>{c["equipment"]}</td><td>{c["short"]}</td></tr>' for c in CAPS)
    caps = "".join(f'<a class="cap" href="{c["slug"]}.html">{ICONS[c["icon"]]}<h3>{c["nav"]}</h3><p>{c["short"]}</p></a>' for c in CAPS)
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("How We Make It", None))}
<h1>How We Make It</h1><p class="lede">Five processes on our own equipment. Because they're in one shop, a single job can be printed, cut, and engraved without leaving the floor.</p></div></div></section>
<section><div class="wrap"><div class="caps">{caps}</div></div></section>
<section class="rule-top"><div class="wrap"><div class="section-head"><span class="eyebrow">Equipment list</span><h2>On the floor</h2></div>
<div class="table-wrap"><table><thead><tr><th>Process</th><th>Equipment</th><th>Used for</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
{cta_band("Pick a process, or let us pick.", "Send the artwork and the goal. We'll recommend the process and material.", "Get a Quote")}"""
    return page("how-we-make-it", "How We Make It | UV Printing, Laser Cutting & Engraving Equipment | Direct Applications",
                "Our equipment: Mutoh UV flatbed, two CamFive CO2 lasers, Epilog engraver with rotary, Mimaki print-and-cut, and an Accu Cutter metal shear.", body)


# --------------------------------------------------------------------------- supporting pages
def trade():
    body = f"""<section class="page-hero"><div class="wrap hero-grid">
<div class="hero-copy">{crumbs(("Trade Program", None))}<span class="eyebrow">For agencies, studios, and packaging firms</span>
<h1>Your Production Partner, Not Another Vendor</h1>
<p class="lede">Most of our revenue comes from trade accounts that subcontract production to us. The program is set up around how you already work: your client, your artwork, your deadline.</p>
<div class="btn-row"><a class="btn arrow" href="#apply">Apply for a trade account </a></div></div>
{photo("Shop floor with trade orders staged for pickup, unbranded boxes", "photo--tall")}
</div></section>

<section><div class="wrap"><div class="section-head"><span class="eyebrow">What you get</span><h2>Program terms</h2></div>
<ul class="covers covers--3">
<li><b>Wholesale rate card</b><span>Trade pricing on our most-ordered items, on request.</span></li>
<li><b>Net terms</b><span>For approved accounts. {tbd("Confirm term length")}</span></li>
<li><b>Rush and weekend options</b><span>For when your client moves the date.</span></li>
<li><b>Confidential, white-label work</b><span>Blind shipping, no branding on packaging, NDAs on request.</span></li>
<li><b>Standing supply agreements</b><span>Committed volume at locked pricing.</span></li>
<li><b>Seasonal capacity reservation</b><span>Hold machine time ahead of your busy season.</span></li>
</ul></div></section>

<section class="band"><div class="wrap band-grid">
<div class="stack"><span class="eyebrow">Who it's for</span><h2>Built for shops that sell production</h2><p>Packaging firms, design studios, event and display agencies, and print brokers.</p></div>
<ul class="ticks"><li>You bring the artwork and the client</li><li>We print, cut, engrave, and assemble</li><li>We ship to you or straight to your client, unbranded</li><li>You keep the relationship and the margin</li></ul>
</div></section>

<section id="apply"><div class="wrap two-col">
<div class="sticky-col"><span class="eyebrow">Apply</span><h2>Apply for a trade account</h2><p class="muted">We review applications within {tbd("X business days")} and send the rate card once you're approved.</p>
<div class="note">Is the trade program a login area or a form? For launch it's a form. A portal can come later.</div></div>
<form class="form" data-form data-thanks="We'll review your application and send the rate card once approved." novalidate>
<div class="form-row"><div class="field"><label for="t-name">Your name <span class="req">*</span></label><input id="t-name" name="name" type="text" required autocomplete="name"></div>
<div class="field"><label for="t-company">Company <span class="req">*</span></label><input id="t-company" name="company" type="text" required autocomplete="organization"></div></div>
<div class="form-row"><div class="field"><label for="t-email">Work email <span class="req">*</span></label><input id="t-email" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="t-phone">Phone</label><input id="t-phone" name="phone" type="tel" autocomplete="tel"></div></div>
<fieldset class="field"><legend>Company type <span class="req">*</span></legend><div class="choices">
<label class="choice"><input type="radio" name="t-type" id="t-type-pack" value="packaging" required><span>Packaging firm</span></label>
<label class="choice"><input type="radio" name="t-type" id="t-type-studio" value="studio"><span>Design studio</span></label>
<label class="choice"><input type="radio" name="t-type" id="t-type-event" value="event"><span>Event or display agency</span></label>
<label class="choice"><input type="radio" name="t-type" id="t-type-print" value="print"><span>Print broker or shop</span></label>
<label class="choice"><input type="radio" name="t-type" id="t-type-other" value="other"><span>Other</span></label></div></fieldset>
<div class="form-row"><div class="field"><label for="t-volume">Typical monthly volume</label><select id="t-volume" name="volume"><option value="">Choose one</option><option>Under $1,000</option><option>$1,000–$5,000</option><option>$5,000–$15,000</option><option>Over $15,000</option></select></div>
<div class="field"><label for="t-terms">Interested in net terms?</label><select id="t-terms" name="terms"><option value="">Choose one</option><option>Yes</option><option>No</option></select></div></div>
<fieldset class="field"><legend>What you'd send us</legend><div class="choices">
<label class="choice"><input type="checkbox" id="t-s-uv" name="services" value="uv"><span>UV printing</span></label>
<label class="choice"><input type="checkbox" id="t-s-cut" name="services" value="cut"><span>Laser cutting</span></label>
<label class="choice"><input type="checkbox" id="t-s-eng" name="services" value="engrave"><span>Engraving</span></label>
<label class="choice"><input type="checkbox" id="t-s-pc" name="services" value="printcut"><span>Print and cut</span></label>
<label class="choice"><input type="checkbox" id="t-s-wl" name="services" value="whitelabel"><span>White-label shipping</span></label></div></fieldset>
<div class="field"><label for="t-notes">Tell us about your work</label><textarea id="t-notes" name="notes" placeholder="Typical jobs, clients you serve, busy seasons"></textarea></div>
<p class="form-error" hidden></p>
<button class="btn arrow" type="submit">Apply for a trade account </button>
<div class="form-status" hidden></div>
</form></div></section>"""
    return page("trade", "Trade Program | Wholesale UV Printing & Laser Cutting for Agencies | Direct Applications",
                "Wholesale production for packaging firms, design studios, and event agencies. Rate card, net terms, rush options, and confidential white-label work in Los Angeles.", body)


def work():
    sol_chips = '<button class="chip" data-filter="solution" data-value="all" aria-pressed="true">All</button>' + "".join(
        f'<button class="chip" data-filter="solution" data-value="{s["slug"]}" aria-pressed="false">{s["nav"]}</button>' for s in SOLUTIONS)
    proc_chips = '<button class="chip" data-filter="process" data-value="all" aria-pressed="true">All</button>' + "".join(
        f'<button class="chip" data-filter="process" data-value="{c["slug"]}" aria-pressed="false">{c["nav"]}</button>' for c in CAPS)
    cards = "".join(work_card(w) for w in WORK)
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("Work", None))}
<h1>Work</h1><p class="lede">Finished pieces from the shop, with the material, process, quantity, and turnaround for each.</p>
<div class="note">Photos and job details below are placeholders until the shoot. Brand logos and program names appear only with customer permission.</div></div></div></section>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter by solution"><span class="label">Solution</span>{sol_chips}</div>
<div class="filters filters--last" role="group" aria-label="Filter by process"><span class="label">Process</span>{proc_chips}</div>
<div class="work-grid" data-work-grid>{cards}</div>
<p class="empty-note" data-work-empty hidden>No jobs match both filters yet. Try another combination.</p>
</div></section>
{cta_band("Want something like this?", "Send a reference photo along with your artwork.", "Get a Quote")}"""
    return page("work", "Our Work | Custom Acrylic, Displays, Signage & Engraving Gallery | Direct Applications",
                "Gallery of custom acrylic, retail displays, event signage, awards, engraved gifts, and prototypes made in Los Angeles.", body)


def guide():
    files = [
        ("Laser cutting", "AI, PDF, SVG, DXF", "Vector only. Cut lines as hairline strokes, no fills. Convert text to outlines."),
        ("UV printing", "PDF, AI, TIFF, PNG", "300 dpi at final size. CMYK. Put white ink on its own layer or spot color named White."),
        ("Engraving", "AI, PDF, SVG; PNG for photos", "Vector for text and logos. Black = engraved. Names as a CSV for personalization."),
        ("Print and cut", "PDF, AI", "Cut path as a spot color named CutContour, 100% magenta, on its own layer."),
        ("Oversized", "AI, PDF, DXF", "Draw at 1:1 scale. Mark the sheet size and grain direction for wood."),
    ]
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in files)
    mats = [("Acrylic", "Clear, frosted, colored, mirror (gold, silver)"), ("Wood", "Plywood, walnut, birch, MDF " + tbd("Confirm")),
            ("Paper and board", "Card stock, envelopes, chipboard, corrugated"), ("Fabric", "Linen, bookcloth, leather"),
            ("Glass", "Bottles and glassware (engraving)"), ("Metal", "Coated and anodized metal, light-gauge sheet"),
            ("Film and vinyl", "Stickers, labels, decals"), ("Your items", "Customer-supplied blanks, tested first")]
    mat_list = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in mats)
    turn = [("Standard", tbd("X business days"), "After artwork approval"), ("Rush", tbd("X business days"), "Subject to capacity, surcharge applies"),
            ("Weekend", tbd("Saturday / Sunday"), "By arrangement"), ("Prototype", tbd("X business days"), "Per round")]
    turn_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in turn)
    faq = [
        ("What file should I send?", "Vector files (AI, PDF, SVG) for anything we cut or engrave. High-resolution PDF or TIFF for printing. If you only have a JPG or a sketch, send it anyway and we'll tell you what we need."),
        ("Can you print white ink?", "Yes. White ink goes under color on clear or dark materials so the colors read correctly. Put white on its own layer, or ask us to generate it."),
        ("What's the smallest order?", "One piece for prototypes. Production minimums depend on the item. " + tbd("Publish minimums")),
        ("Can I send my own items to engrave or print?", "Yes. We'll test one before running the batch. Send a spare in case the test needs a second try."),
        ("Do you offer proofs?", "Every job gets a digital proof. Physical samples are available before production runs."),
        ("Can you ship directly to my client without your branding?", "Yes. Trade accounts can request blind, white-label shipping."),
        ("How do I mark cut lines for print and cut?", "Use a spot color named CutContour (100% magenta), as a hairline stroke on its own layer."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in faq)
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("Materials and Artwork Guide", None))}
<h1>Materials and Artwork Guide</h1><p class="lede">How to set up files, what we can work with, and how long it takes. Getting this right up front saves a round of back-and-forth on your quote.</p>
<div class="links"><a class="pill-link" href="#files">File types</a><a class="pill-link" href="#materials">Materials</a><a class="pill-link" href="#turnaround">Turnaround</a><a class="pill-link" href="#faq">FAQ</a></div></div></div></section>
<section id="files"><div class="wrap"><div class="section-head"><span class="eyebrow">Accepted files and artwork specs</span><h2>File setup by process</h2></div>
<div class="table-wrap"><table><thead><tr><th>Process</th><th>File types</th><th>Setup</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section id="materials" class="rule-top"><div class="wrap two-col"><div class="stack"><span class="eyebrow">Materials</span><h2>What we work with</h2><p class="muted">Thickness and size limits are listed on each capability page.</p></div><ul class="covers">{mat_list}</ul></div></section>
<section id="turnaround" class="rule-top"><div class="wrap two-col"><div class="stack"><span class="eyebrow">Turnaround</span><h2>How long it takes</h2><p class="muted">Turnaround starts when artwork is approved and payment or terms are in place.</p></div>
<div class="table-wrap"><table><thead><tr><th>Option</th><th>Time</th><th>Notes</th></tr></thead><tbody>{turn_rows}</tbody></table></div></div></section>
<section id="faq" class="rule-top"><div class="wrap two-col"><div class="stack"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div><div class="faq">{faq_html}</div></div></section>
{cta_band("Files ready?", "Upload them with your quote request. Large files are fine.", "Get a Quote")}"""
    return page("guide", "Laser Cutting & UV Printing Artwork Guide | File Setup & Materials | Direct Applications",
                "How to set up files for laser cutting, UV printing, engraving, and print and cut. Accepted file types, materials, turnaround, and FAQ.", body)


def quote():
    opts = "".join(f'<option value="{s["slug"]}">{s["nav"]}</option>' for s in SOLUTIONS)
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("Get a Quote", None))}
<h1>Get a Quote</h1><p class="lede">Tell us what you need and attach your artwork. We reply with a price, a material recommendation, and a ship date.</p></div></div></section>
<section><div class="wrap two-col two-col--form">
<form class="form" data-form data-thanks="We have your request and will reply with a quote." novalidate>
<fieldset class="field"><legend>I'm a… <span class="req">*</span></legend><div class="choices">
<label class="choice"><input type="radio" name="buyer" id="q-b-agency" value="agency" required><span>Agency or trade shop</span></label>
<label class="choice"><input type="radio" name="buyer" id="q-b-brand" value="brand"><span>Brand</span></label>
<label class="choice"><input type="radio" name="buyer" id="q-b-event" value="event"><span>Event planner</span></label>
<label class="choice"><input type="radio" name="buyer" id="q-b-ind" value="individual"><span>Individual</span></label></div></fieldset>
<div class="form-row"><div class="field"><label for="q-name">Name <span class="req">*</span></label><input id="q-name" name="name" type="text" required autocomplete="name"></div>
<div class="field"><label for="q-company">Company</label><input id="q-company" name="company" type="text" autocomplete="organization"></div></div>
<div class="form-row"><div class="field"><label for="q-email">Email <span class="req">*</span></label><input id="q-email" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="q-phone">Phone</label><input id="q-phone" name="phone" type="tel" autocomplete="tel"></div></div>
<div class="form-row"><div class="field"><label for="q-solution">What you need <span class="req">*</span></label><select id="q-solution" name="solution" required><option value="">Choose one</option>{opts}<option value="other">Something else</option></select></div>
<div class="field"><label for="q-material">Material, if known</label><input id="q-material" name="material" type="text" placeholder="e.g. 1/8 in clear acrylic"></div></div>
<div class="form-row"><div class="field"><label for="q-qty">Quantity <span class="req">*</span></label><input id="q-qty" name="qty" type="number" min="1" required placeholder="e.g. 150"></div>
<div class="field"><label for="q-deadline">Deadline</label><input id="q-deadline" name="deadline" type="date"><span class="hint">The date you need it in hand.</span></div></div>
<fieldset class="field"><legend>Rush needed?</legend><div class="choices">
<label class="choice"><input type="radio" name="rush" id="q-rush-no" value="no" checked><span>No</span></label>
<label class="choice"><input type="radio" name="rush" id="q-rush-yes" value="yes"><span>Yes, including weekend</span></label></div></fieldset>
<div class="field"><span class="field-label">Artwork</span>
<label class="drop" data-list="q-files" for="q-art"><input id="q-art" name="artwork" type="file" multiple accept=".ai,.pdf,.svg,.dxf,.eps,.png,.jpg,.jpeg,.tif,.tiff,.psd,.zip"><b>Drop files here or choose files</b><span class="mono muted">AI, PDF, SVG, DXF, EPS, TIFF, PNG, JPG, PSD, ZIP · large files welcome</span></label>
<ul class="file-list" id="q-files"></ul></div>
<div class="field"><label for="q-notes">Project details</label><textarea id="q-notes" name="notes" placeholder="Size, colors, finish, assembly, where it ships"></textarea></div>
<p class="form-error" hidden></p>
<button class="btn arrow" type="submit">Send quote request </button>
<div class="form-status" hidden></div>
</form>
<aside class="sticky-col">
<div class="aside-card"><span class="eyebrow">What happens next</span>
<ul class="ticks"><li>We review files and flag anything that needs fixing</li><li>You get a price, material recommendation, and ship date</li><li>Approve a proof or prototype</li><li>We produce and deliver</li></ul></div>
<div class="aside-card"><span class="eyebrow">Prefer to talk?</span><ul class="contact-list"><li><span class="mono">Phone</span>{PHONE}</li><li><span class="mono">Email</span>{EMAIL}</li></ul></div>
<div class="aside-card"><span class="eyebrow">Trade account?</span><p class="muted">Agencies and packaging firms get wholesale rates.</p><a class="btn btn--ghost" href="trade.html">Trade program</a></div>
</aside>
</div></section>"""
    return page("quote", "Get a Quote | Custom Acrylic, Laser Cutting & UV Printing | Direct Applications",
                "Request a quote for custom acrylic, laser cutting, UV printing, and engraving in Los Angeles. Upload artwork and get a price, material recommendation, and ship date.", body)


def about():
    rows = "".join(f'<tr><td>{c["equipment"]}</td><td><a href="{c["slug"]}.html">{c["nav"]}</a></td></tr>' for c in CAPS)
    body = f"""<section class="page-hero"><div class="wrap hero-grid">
<div class="hero-copy">{crumbs(("About", None))}<h1>A Los Angeles shop that gets the job done on time.</h1>
<p class="lede">{BRAND} is a production shop for printed, cut, and engraved pieces. We run our own equipment, and our operators have about ten years of production experience between the machines.</p></div>
{photo("Wide shot of the shop floor, machines running, team at work", "photo--tall")}
</div></section>
<section><div class="wrap two-col">
<div class="stack"><span class="eyebrow">The shop</span><h2>How we work</h2></div>
<div class="stack"><p>Most of our customers are agencies, packaging firms, and brands that need a dependable production partner. They bring the artwork; we figure out how to make it, make a sample, and run the quantity.</p>
<p>Because printing, cutting, and engraving happen in the same building, a job doesn't wait on a second vendor. That's how we keep short runs fast and rush jobs possible.</p>
<p>{tbd("Founding story and owner bio to add")}</p></div>
</div></section>
<section class="rule-top"><div class="wrap two-col">
<div class="stack"><span class="eyebrow">The team</span><h2>Operators, not order takers</h2><p class="muted">About 10 years of production experience on these machines. They'll tell you if a file won't cut cleanly before it costs you a run.</p></div>
<div class="work-grid work-grid--2">{photo("Operator portrait at the UV printer", "photo--tall")}{photo("Operator portrait at the laser", "photo--tall")}</div>
</div></section>
<section class="rule-top"><div class="wrap two-col">
<div class="stack"><span class="eyebrow">The equipment</span><h2>What's on the floor</h2></div>
<div class="table-wrap"><table><thead><tr><th>Equipment</th><th>Process</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="rule-top"><div class="wrap two-col">
<div class="stack"><span class="eyebrow">Made in LA</span><h2>Local manufacturing</h2></div>
<div class="stack"><p>We make everything in Los Angeles. Local customers can pick up, and we deliver across {tbd("service area TBD")}. The shop is moving to a new location; the address will be posted here.</p></div>
</div></section>
{cta_band("Come see the shop.", "Bring a sample or a file and we'll walk you through how we'd make it.", "Contact us", "contact.html", ghost=("Get a Quote", "quote.html"))}"""
    return page("about", "About Direct Applications | Los Angeles Print, Cut & Engraving Shop",
                "Direct Applications is a Los Angeles production shop for UV printing, laser cutting, and engraving, with operators who have about 10 years of production experience.", body)


def contact():
    body = f"""<section class="page-hero"><div class="wrap"><div class="hero-copy">{crumbs(("Contact", None))}
<h1>Contact the Shop</h1><p class="lede">For a price on a specific job, the quote form is fastest. For anything else, reach us here.</p>
<div class="btn-row"><a class="btn arrow" href="quote.html">Get a Quote </a></div></div></div></section>
<section><div class="wrap two-col">
<div class="aside-card"><ul class="contact-list">
<li><span class="mono">Address</span>{ADDRESS}</li>
<li><span class="mono">Phone</span>{PHONE}</li>
<li><span class="mono">Email</span>{EMAIL}</li>
<li><span class="mono">Hours</span>{HOURS}</li>
<li><span class="mono">Service area</span>{CITY} and {tbd("South Bay / service area TBD")}</li>
</ul></div>
<form class="form" data-form data-thanks="We got your message and will get back to you." novalidate>
<div class="form-row"><div class="field"><label for="c-name">Name <span class="req">*</span></label><input id="c-name" name="name" type="text" required autocomplete="name"></div>
<div class="field"><label for="c-email">Email <span class="req">*</span></label><input id="c-email" name="email" type="email" required autocomplete="email"></div></div>
<div class="field"><label for="c-msg">Message <span class="req">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
<p class="form-error" hidden></p>
<button class="btn arrow" type="submit">Send message </button>
<div class="form-status" hidden></div>
</form>
</div></section>"""
    return page("contact", "Contact | Direct Applications, Los Angeles",
                "Contact Direct Applications, a Los Angeles shop for UV printing, laser cutting, and engraving.", body)


# --------------------------------------------------------------------------- build
def build(out=OUT, artifact_index=None):
    os.makedirs(out, exist_ok=True)
    pages = {"index.html": home()}
    for s in SOLUTIONS:
        pages[s["slug"] + ".html"] = solution_page(s)
    for c in CAPS:
        pages[c["slug"] + ".html"] = cap_page(c)
    pages.update({
        "what-we-make.html": what_we_make(), "how-we-make-it.html": how_we_make_it(), "trade.html": trade(),
        "work.html": work(), "guide.html": guide(), "quote.html": quote(), "about.html": about(), "contact.html": contact(),
    })
    for name, content in pages.items():
        with open(os.path.join(out, name), "w") as f:
            f.write(content)
    if artifact_index:
        with open(artifact_index, "w") as f:
            f.write(home(artifact=True))
    print(f"Built {len(pages)} pages into {out}")


if __name__ == "__main__":
    build(artifact_index=sys.argv[1] if len(sys.argv) > 1 else None)
