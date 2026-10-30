#!/usr/bin/env python3
"""Build mouthoffmedia.com into ./public (static, GitHub Pages)."""
import os, json, html, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public')
SITE = 'https://mouthoffmedia.com'
# ---- single source of truth for contact details (confirmed by owner) ----
CONTACT_EMAIL = 'sahwisdom@gmail.com'
CONTACT_PHONE = '516-603-5264'
CONTACT_TEL = '+15166035264'
VER = datetime.date.today().isoformat()
BRAND = 'Mouth Off Media'
LEGAL = 'WealthEdge Ventures Inc., doing business as Wisdom Digital'
TAG = 'Websites that speak up.'
E = html.escape
GA_ID = 'G-Y7R5K9NMW0'  # Google Analytics 4, one property shared by all sites
GA_HEAD = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>'
           f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}",' + json.dumps({'site_brand': BRAND}) + ');</script>')

WORK = [  # (domain, title, kind, blurb, https)
 ('manhattancrystalmarket.com','Manhattan Crystal Market','Shopify storefront','A crystal shop storefront with a multi-item cart that checks out through one shared Shopify store, plus clear walk-in directions to the shop at 2 W 14th St.',1),
 ('namastecrystalshop.com','Namaste Crystal Shop','Shopify storefront','Crystals A to Z with meanings, kits and pocket stones, organized for search and for shoppers who know what they want.',1),
 ('namastecandles.com','Namaste Candles','Shopify storefront','Ritual, intention, reiki and chakra candles, with its own look and copy, selling from the same live inventory.',1),
 ('namastegreatfinds.com','Namaste Great Finds','Gift-finder storefront','Spiritual gifts sorted by price point (under $10, $25 and $50) so gift shoppers get to a decision fast.',1),
 ('nyctarotreaders.com','NYC Tarot Readers','Local directory','A New York City tarot reader directory with listing pages, featured in-house readers with booking pages, and a claim-your-listing flow.',1),
 ('nycpsychicreaders.com','NYC Psychic Readers','Local directory','A sister directory for psychics, mediums and palm readers across NYC, built to rank for local search.',1),
 ('namastebeads.com','Namaste Beads','Shopify storefront','Beaded crystal bracelets and malas, with a mobile-first product grid and a link-preview card made for sharing.',1),
 ('namastebeadshop.com','Namaste Bead Shop','Shopify storefront','Malas, prayer beads and meditation tools, written for its own niche rather than copied from its siblings.',1),
 ('namastebeadstore.com','Namaste Bead Store','Shopify storefront','Stone bead bracelets shopped by stone and by intention.',1),
 ('namastecrystaljewelry.com','Namaste Crystal Jewelry','Shopify storefront','Crystal and gemstone jewelry with filters, a sticky cart and one-tap checkout.',1),
 ('namastejewelryshop.com','Namaste Jewelry Shop','Shopify storefront','Sterling silver gemstone jewelry with its own brand voice.',1),
 ('namastejewelrystore.com','Namaste Jewelry Store','Gift storefront','Crystal jewelry gifts under $30, built around a single clear buying angle.',1),
 ('namasteincense.com','Namaste Incense','Shopify storefront','An incense shop storefront covering sticks, cones, resins and smudge, with in-store pickup directions.',1),
 ('namasteincenseshop.com','Namaste Incense Shop','Shopify storefront','An incense satellite storefront focused on its own slice of the catalog.',0),
 ('namasteincensestore.com','Namaste Incense Store','Shopify storefront','A third incense storefront with a different angle, still on one inventory.',0),
]
SERVICES = [
 ('web','Web design','Custom, fast, mobile-first websites with a voice of their own. No bloated templates. Every page is built to load quickly and to push visitors toward one clear next step.',['Mobile-first layouts tested on real phone sizes','Copy and structure built around how your customers actually buy','Fast static hosting where it fits, so you are not paying for servers you do not need']),
 ('shop','Ecommerce and Shopify storefronts','Branded storefronts that sell from your existing Shopify inventory. Multiple sites can share one catalog and one checkout, so you launch new brands without running new stores.',['Multi-item carts that hand off to Shopify checkout','Live prices and stock pulled from your catalog','Product grids, filters and sticky carts that work with one thumb']),
 ('app','Web apps and PWAs','Installable web apps that work on iPhone and Android straight from the browser, with no app-store wait. Add-to-home-screen, offline pages and app-like speed.',['Web app manifest, icons and service worker','Works offline for key pages','Dashboards, booking flows and internal tools']),
 ('seo','SEO and AI-search visibility','Technical SEO done properly, plus the newer work of being findable by AI assistants like ChatGPT. Clean markup, structured data, sitemaps and llms.txt.',['JSON-LD structured data (LocalBusiness, Product, Organization)','Sitemaps, canonical tags and robots.txt that welcome AI crawlers','Original, niche-specific copy for every page, never duplicated across sites']),
 ('local','Local business presence','For shops with a door: make sure people searching nearby find you, understand where you are, and walk in.',['Address, map and walk-in directions on every page','Local landing pages that follow Google guidelines','Click-to-call and directions buttons above the fold']),
 ('brand','Branding and link-preview images','When someone shares your link in iMessage, WhatsApp or Slack, the preview should look like a brand, not a broken crop. We design the logo, colors and 1200x630 share cards.',['Open Graph and Twitter card images for every site','Logos, app icons and favicons','A consistent look across every page and every share']),
 ('net','Multi-site networks','A family of focused sites, each with its own niche, wording and brand, all honestly disclosed as part of one business and all feeding one inventory.',['Shared toolkit so updates reach every site at once','Each site gets distinct content and a distinct audience','Built to stay on the right side of search-engine spam policies']),
]
STEPS = [
 ('Talk','We start with a call or a message. You tell us what you sell, who buys it and what is not working. We tell you straight what we would do.'),
 ('Plan','We map the pages, the angle and the one action each page should drive. You approve the plan before we build.'),
 ('Build','We design and build mobile-first, then test on phone-sized screens, check every image and fix anything that overflows or loads slowly.'),
 ('Launch','We connect your domain, set up HTTPS, submit the sitemap and make sure link previews look right when people share.'),
 ('Grow','After launch we keep tuning copy, speed and search visibility based on what real visitors do.'),
]
NAV = [('/', 'Home'), ('/services/', 'Services'), ('/work/', 'Work'), ('/process/', 'Process'), ('/about/', 'About'), ('/contact/', 'Contact')]

LOGO = '<svg class="logo-mark" viewBox="0 0 64 64" aria-hidden="true"><path d="M8 10h48a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H30l-14 12v-12H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="#ff3d2e"/><path d="M15 38V18h5l5 9 5-9h5v20h-5V27l-5 8-5-8v11zM40 28c0-6 4-10 9-10s9 4 9 10-4 10-9 10-9-4-9-10zm5 0c0 3 2 5 4 5s4-2 4-5-2-5-4-5-4 2-4 5z" fill="#0d0d0f" transform="translate(-3 0)"/></svg>'

def jsonld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": SITE + "/#org", "name": BRAND, "url": SITE + "/",
         "logo": SITE + "/icons/icon-512.png", "image": SITE + "/og.jpg",
         "email": CONTACT_EMAIL, "telephone": CONTACT_TEL,
         "legalName": "WealthEdge Ventures Inc.", "alternateName": ["Wisdom Digital"],
         "address": {"@type": "PostalAddress", "addressLocality": "New York", "addressRegion": "NY", "addressCountry": "US"}},
        {"@type": "ProfessionalService", "@id": SITE + "/#service", "name": BRAND, "url": SITE + "/",
         "image": SITE + "/og.jpg", "parentOrganization": {"@id": SITE + "/#org"},
         "email": CONTACT_EMAIL, "telephone": CONTACT_TEL,
         "description": "Web design, Shopify storefronts, web apps and PWAs, SEO and AI-search visibility for businesses in New York City and beyond.",
         "areaServed": [{"@type": "City", "name": "New York"}, {"@type": "Country", "name": "United States"}],
         "address": {"@type": "PostalAddress", "addressLocality": "New York", "addressRegion": "NY", "addressCountry": "US"},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[1]}} for s in SERVICES]}},
        {"@type": "WebSite", "@id": SITE + "/#site", "name": BRAND, "url": SITE + "/", "publisher": {"@id": SITE + "/#org"}}]}

def page(path, title, desc, body, active='', extra_ld=None, noindex=False):
    url = SITE + path
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{n}</a>' for h, n in NAV)
    ld = [jsonld()] + ([extra_ld] if extra_ld else [])
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{GA_HEAD}
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="theme-color" content="#0d0d0f">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" href="/icons/favicon.svg" type="image/svg+xml"><link rel="icon" href="/icons/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Mouth Off">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Mouth Off Media: websites that speak up">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{SITE}/og.jpg">
<link rel="stylesheet" href="/assets/site.css?v={VER}">
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0], separators=(",", ":"))}</script>
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="/" aria-label="{BRAND} home">{LOGO}<span>Mouth&nbsp;Off<b>Media</b></span></a>
<button class="menu" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span></button>
<nav id="nav" class="nav">{nav}<a class="btn btn-sm" href="/contact/">Start a project</a></nav>
</div></header>
<main id="main">{body}</main>
<footer class="ftr"><div class="wrap ftr-in">
<div><a class="brand" href="/">{LOGO}<span>Mouth&nbsp;Off<b>Media</b></span></a>
<p class="muted">Web design and digital solutions from New York City. {BRAND} is a brand of {LEGAL}.</p>
<p class="contact-line"><a href="tel:{CONTACT_TEL}">{CONTACT_PHONE}</a><br><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p></div>
<div><h4>Explore</h4>{''.join(f'<a href="{h}">{n}</a>' for h, n in NAV)}</div>
<div><h4>Services</h4>{''.join(f'<a href="/services/#{s[0]}">{s[1]}</a>' for s in SERVICES)}</div>
</div><div class="wrap legal"><span>&copy; {datetime.date.today().year} WealthEdge Ventures Inc. dba Wisdom Digital</span><a href="/privacy/">Privacy</a><a href="/sitemap.xml">Sitemap</a></div></footer>
<div class="callbar"><a href="tel:{CONTACT_TEL}">Call</a><a href="/contact/" class="hot">Start a project</a></div>
<script src="/assets/site.js?v={VER}" defer></script>
</body></html>'''

def work_card(w, big=False):
    d, t, k, b, s = w
    slug = d.split('.')[0]; url = ('https://' if s else 'http://') + d + '/'
    return f'''<article class="wcard{' big' if big else ''}"><a href="{url}" target="_blank" rel="noopener">
<div class="shot"><img src="/assets/work/{slug}.jpg" alt="Screenshot of {E(t)} ({d})" width="960" height="600" loading="lazy" decoding="async"></div>
<div class="wmeta"><span class="kind">{E(k)}</span><h3>{E(t)}</h3><p>{E(b)}</p><span class="dom">{d} &#8599;</span></div></a></article>'''

def cta():
    return f'''<section class="cta"><div class="wrap"><h2>Got something to say?<br><em>Let&rsquo;s make it loud.</em></h2>
<p>Tell us about your business and what you want your site to do. We reply with a straight answer.</p>
<div class="btns"><a class="btn" href="/contact/">Start a project</a><a class="btn ghost" href="tel:{CONTACT_TEL}">Call {CONTACT_PHONE}</a></div></div></section>'''

def home():
    svc = ''.join(f'<a class="svc" href="/services/#{s[0]}"><span class="n">{i+1:02d}</span><h3>{E(s[1])}</h3><p>{E(s[2].split(". ")[0])}.</p></a>' for i, s in enumerate(SERVICES))
    steps = ''.join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in STEPS)
    feat = ''.join(work_card(w) for w in WORK[:6])
    return page('/', 'Mouth Off Media | Web Design, Shopify Storefronts & Web Apps in NYC',
        'Mouth Off Media builds bold, fast, mobile-first websites, Shopify storefronts, installable web apps and SEO/AI-search visibility for businesses in New York City and beyond.',
        f'''<section class="hero"><div class="wrap">
<p class="eyebrow">Web design &amp; digital solutions &middot; NYC</p>
<h1>Your business has a voice.<br><em>Your website should use it.</em></h1>
<p class="lede">We design and build websites, Shopify storefronts and installable web apps that load fast, look sharp on a phone, show up in Google and AI search, and turn visitors into customers.</p>
<div class="btns"><a class="btn" href="/contact/">Start a project</a><a class="btn ghost" href="/work/">See live work</a></div>
<ul class="ticker" aria-label="What we build"><li>Websites</li><li>Shopify storefronts</li><li>Web apps &amp; PWAs</li><li>SEO</li><li>AI-search visibility</li><li>Local presence</li><li>Branding</li></ul>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-h"><p class="eyebrow">What we do</p><h2>Built to be heard.</h2></div><div class="svcs">{svc}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="sec-h"><p class="eyebrow">Live work</p><h2>Real sites. Live right now.</h2>
<p class="muted">Every project below is live on the web today. Click through and try them on your phone.</p></div>
<div class="work">{feat}</div><p class="center"><a class="btn ghost" href="/work/">All {len(WORK)} live sites</a></p></div></section>
<section class="sec"><div class="wrap two"><div><p class="eyebrow">How we work</p><h2>No mumbling. No mystery.</h2><p class="muted">Five clear steps from first message to launch, and we keep going after that.</p><a class="link" href="/process/">Our process &rarr;</a></div><ol class="steps">{steps}</ol></div></section>
{cta()}''', '/')

def services():
    blocks = ''.join(f'''<section class="svc-full" id="{s[0]}"><span class="n">{i+1:02d}</span><div><h2>{E(s[1])}</h2><p>{E(s[2])}</p><ul>{''.join(f"<li>{E(x)}</li>" for x in s[3])}</ul></div></section>''' for i, s in enumerate(SERVICES))
    return page('/services/', 'Services | Web Design, Shopify, PWAs, SEO & AI Search | Mouth Off Media',
        'Web design, Shopify storefronts, web apps and PWAs, SEO and ChatGPT/AI-search visibility, local business presence, branding and multi-site networks from Mouth Off Media.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">Services</p><h1>Everything your business needs <em>to speak up online.</em></h1><p class="lede">Pick one service or bring us the whole thing. We handle design, build, launch and visibility.</p></div></section>
<div class="wrap">{blocks}</div>{cta()}''', '/services/')

def work():
    return page('/work/', 'Work | Live Websites & Storefronts We Built | Mouth Off Media',
        'Live websites built by Mouth Off Media: Shopify storefronts, gift finders and NYC local directories, all live on the web today.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">Work</p><h1>Live sites. <em>Go poke at them.</em></h1>
<p class="lede">These are real, live websites. They are our in-house network for Namaste Bookshop, a sister business under the same ownership on West 14th Street in Manhattan. Each site has its own brand and niche, and all of them sell from one shared Shopify inventory and checkout.</p></div></section>
<section class="sec"><div class="wrap"><div class="work all">{''.join(work_card(w) for w in WORK)}</div>
<p class="muted small">Screenshots taken from the live sites. Some storefronts are still finishing their HTTPS setup and may open over http for now.</p></div></section>{cta()}''', '/work/')

def process():
    steps = ''.join(f'<section class="svc-full"><span class="n">{i+1:02d}</span><div><h2>{E(a)}</h2><p>{E(b)}</p></div></section>' for i, (a, b) in enumerate(STEPS))
    return page('/process/', 'Process | How We Plan, Build & Launch | Mouth Off Media',
        'How Mouth Off Media works: talk, plan, build, launch and grow. A clear process for websites, storefronts and web apps.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">Process</p><h1>Straight talk, <em>start to finish.</em></h1><p class="lede">You always know what is happening, what is next and what we need from you.</p></div></section>
<div class="wrap">{steps}</div>
<section class="sec"><div class="wrap"><div class="sec-h"><h2>What every launch includes</h2></div><ul class="checks">
<li>Mobile testing on phone-sized screens</li><li>HTTPS on your own domain</li><li>sitemap.xml and robots.txt</li><li>Structured data (JSON-LD)</li><li>llms.txt for AI assistants</li><li>Designed 1200x630 link-preview image</li><li>Custom 404 page</li><li>Privacy page</li></ul></div></section>{cta()}''', '/process/')

def about():
    return page('/about/', 'About | Mouth Off Media, a Wisdom Digital brand in NYC',
        'Mouth Off Media is the web design and digital solutions brand of WealthEdge Ventures Inc., doing business as Wisdom Digital, based in New York City.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">About</p><h1>Loud on purpose.</h1>
<p class="lede">Most business websites whisper. Same template, same stock photos, same vague copy. We think your site should say what you do, clearly and with confidence, and then make it easy to buy, book or walk in.</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>Who we are</h2></div><div>
<p>{BRAND} is the web design and digital solutions brand of <strong>WealthEdge Ventures Inc.</strong>, a New York corporation doing business as <strong>Wisdom Digital</strong>, based in New York City.</p>
<p>We build and run our own network of storefronts and directories for Namaste Bookshop, a sister retail business on West 14th Street in Manhattan. That work is our proving ground: the tools and methods we use for clients are the ones we use on our own sites every day.</p>
<p>We work with shops, service businesses and founders who want a site that loads fast, looks right on a phone, shows up in search and actually brings in customers.</p>
<a class="btn" href="/contact/">Talk to us</a></div></div></section>''', '/about/')

def contact():
    opts = ''.join(f'<label class="chip"><input type="checkbox" name="svc" value="{E(s[1])}"><span>{E(s[1])}</span></label>' for s in SERVICES)
    return page('/contact/', 'Contact | Start a Project with Mouth Off Media',
        f'Start a website, Shopify storefront or web app project with Mouth Off Media. Call {CONTACT_PHONE} or email {CONTACT_EMAIL}.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">Contact</p><h1>Start a project.</h1>
<p class="lede">Tell us what you are building. The form opens your email app with everything filled in, so nothing gets lost.</p>
<div class="direct"><a class="dcard" href="tel:{CONTACT_TEL}"><span>Call</span><b>{CONTACT_PHONE}</b></a><a class="dcard" href="mailto:{CONTACT_EMAIL}"><span>Email</span><b>{CONTACT_EMAIL}</b></a></div></div></section>
<section class="sec"><div class="wrap narrow">
<form id="inquiry" class="form" data-to="{CONTACT_EMAIL}" novalidate>
<div class="row"><label>Your name<input name="name" autocomplete="name" required></label><label>Your email<input type="email" name="email" autocomplete="email" required></label></div>
<div class="row"><label>Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label><label>Business or website<input name="biz" autocomplete="organization"></label></div>
<fieldset><legend>What do you need?</legend><div class="chips">{opts}</div></fieldset>
<label>Timeline<select name="when"><option value="">Choose one</option><option>As soon as possible</option><option>In the next month</option><option>In 1 to 3 months</option><option>Just exploring</option></select></label>
<label>Tell us about the project<textarea name="msg" rows="5" required placeholder="What do you sell or do, who are your customers, and what should the site do for you?"></textarea></label>
<p class="err" role="alert" hidden></p>
<button class="btn" type="submit">Send project details</button>
<p class="muted small">Submitting opens your email app with a message to {CONTACT_EMAIL}. Nothing is stored on this website. See our <a href="/privacy/">privacy page</a>.</p>
</form></div></section>''', '/contact/')

def privacy():
    return page('/privacy/', 'Privacy | Mouth Off Media', 'Privacy information for mouthoffmedia.com.',
        f'''<section class="hero sm"><div class="wrap"><p class="eyebrow">Privacy</p><h1>Privacy</h1></div></section>
<section class="sec"><div class="wrap narrow prose">
<p>This website is operated by {LEGAL} ("{BRAND}"), New York, NY.</p>
<h2>What we collect</h2><p>This site has no accounts. We use Google Analytics to count visits and see which pages are useful, and to count when someone taps call, email or sends the project form; Google may set cookies to do this. The project form does not send data to our servers. When you submit it, your own email app opens a message addressed to {CONTACT_EMAIL}, and you choose whether to send it.</p>
<h2>What happens when you contact us</h2><p>If you email or call us, we use your details only to respond to you and to work on your project. We do not sell your information.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages. GitHub may process standard technical data such as IP addresses in server logs to deliver and secure the site.</p>
<h2>App and offline use</h2><p>If you install this site as an app, your device stores a copy of some pages so they work offline. You can remove it at any time by uninstalling the app or clearing site data.</p>
<h2>Questions</h2><p>Email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> or call <a href="tel:{CONTACT_TEL}">{CONTACT_PHONE}</a>.</p>
<p class="muted small">Last updated {VER}.</p></div></section>''', '/privacy/')

def notfound():
    return page('/404.html', 'Page not found | Mouth Off Media', 'That page does not exist.',
        '''<section class="hero"><div class="wrap"><p class="eyebrow">404</p><h1>Well, this is awkward.<br><em>That page went quiet.</em></h1><p class="lede">The link may be old or mistyped. Try one of these instead.</p><div class="btns"><a class="btn" href="/">Home</a><a class="btn ghost" href="/work/">Our work</a><a class="btn ghost" href="/contact/">Contact</a></div></div></section>''', noindex=True)

def offline():
    return page('/offline/', 'Offline | Mouth Off Media', 'You are offline.',
        f'''<section class="hero"><div class="wrap"><p class="eyebrow">Offline</p><h1>No signal.<br><em>We&rsquo;ll be right here.</em></h1><p class="lede">You are offline. Pages you have already opened still work. You can also call us at <a href="tel:{CONTACT_TEL}">{CONTACT_PHONE}</a>.</p><div class="btns"><a class="btn" href="/">Try home</a></div></div></section>''', noindex=True)

PAGES = {'index.html': home, 'services/index.html': services, 'work/index.html': work, 'process/index.html': process,
         'about/index.html': about, 'contact/index.html': contact, 'privacy/index.html': privacy, '404.html': notfound, 'offline/index.html': offline}

def main():
    for p, fn in PAGES.items():
        f = os.path.join(OUT, p); os.makedirs(os.path.dirname(f), exist_ok=True); open(f, 'w').write(fn())
    urls = ['/', '/services/', '/work/', '/process/', '/about/', '/contact/', '/privacy/']
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{VER}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User', 'Claude-SearchBot', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot', 'Applebot-Extended', 'Bingbot', 'Googlebot', 'CCBot', 'meta-externalagent', 'DuckAssistBot']
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + f'Sitemap: {SITE}/sitemap.xml\n')
    llms = f'''# {BRAND}

> {BRAND} is the web design and digital solutions brand of WealthEdge Ventures Inc. (a New York corporation) doing business as Wisdom Digital, based in New York City. We design and build websites, Shopify storefronts, web apps and PWAs, and handle SEO and AI-search visibility.

Contact: phone {CONTACT_PHONE}, email {CONTACT_EMAIL}. Pricing is quoted per project; no public price list.

## Pages
- [Home]({SITE}/): overview of services, process and live work
- [Services]({SITE}/services/): {"; ".join(s[1] for s in SERVICES)}
- [Work]({SITE}/work/): live sites we built (our in-house network for Namaste Bookshop, a sister business)
- [Process]({SITE}/process/): talk, plan, build, launch, grow
- [About]({SITE}/about/): ownership and background
- [Contact]({SITE}/contact/): start a project

## Live work
''' + ''.join(f'- [{w[1]}](https://{w[0]}/): {w[2]}. {w[3]}\n' for w in WORK)
    open(os.path.join(OUT, 'llms.txt'), 'w').write(llms)
    man = {"name": "Mouth Off Media", "short_name": "Mouth Off", "description": "Web design, storefronts, web apps and SEO from NYC.",
           "id": "/", "start_url": "/?source=pwa", "scope": "/", "display": "standalone", "orientation": "portrait-primary",
           "background_color": "#0d0d0f", "theme_color": "#0d0d0f", "categories": ["business", "productivity"],
           "icons": [{"src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                     {"src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                     {"src": "/icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
           "shortcuts": [{"name": "Start a project", "url": "/contact/", "icons": [{"src": "/icons/icon-192.png", "sizes": "192x192"}]},
                         {"name": "Our work", "url": "/work/", "icons": [{"src": "/icons/icon-192.png", "sizes": "192x192"}]}]}
    json.dump(man, open(os.path.join(OUT, 'manifest.webmanifest'), 'w'), indent=1)
    shots = sorted(f'/assets/work/{x}' for x in os.listdir(os.path.join(OUT, 'assets/work')))
    pre = ['/', '/services/', '/work/', '/process/', '/about/', '/contact/', '/privacy/', '/offline/', '/404.html',
           f'/assets/site.css?v={VER}', f'/assets/site.js?v={VER}', '/manifest.webmanifest', '/icons/icon-192.png', '/icons/favicon.svg', '/og.jpg']
    sw = open(os.path.join(ROOT, 'scripts', 'sw.tmpl.js')).read().replace('__VER__', VER + '-' + str(int(datetime.datetime.now().timestamp()))).replace('__PRE__', json.dumps(pre)).replace('__LAZY__', json.dumps(shots))
    open(os.path.join(OUT, 'sw.js'), 'w').write(sw)
    open(os.path.join(OUT, 'CNAME'), 'w').write('mouthoffmedia.com\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print('built', len(PAGES), 'pages')
main()
