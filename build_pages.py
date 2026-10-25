#!/usr/bin/env python3
"""Generate the WebServicers sub-pages.

Run from the project root:  python3 scripts/build_pages.py
Every page is written to the project root as static HTML.
"""

from pathlib import Path
import html as ihtml
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from pages_data import SERVICES, COMPANY, LEGAL, PRICING_PLANS  # noqa: E402

BRAND = "WebServicers"

# --------------------------------------------------------------------------
# Icons
# --------------------------------------------------------------------------
def ico(path, filled=False):
    if filled:
        return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{path}"/></svg>'
    return (
        '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        f'<path d="{path}" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )

ICONS = {
    "search": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="1.7"/><path d="M15.4 15.4 21 21" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4.5" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 19V5M4 19h16" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M7.5 15.5 11 11l3 2.5L19 7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="9" cy="9" r="3.2" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 19c.6-3 2.8-4.6 5.5-4.6s4.9 1.6 5.5 4.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M16 6.5a3 3 0 0 1 0 5.6M17.5 14.6c2 .4 3.3 1.9 3.7 4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3l7 3v5.5c0 4.4-2.9 7.9-7 9.5-4.1-1.6-7-5.1-7-9.5V6l7-3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 12.2l2.2 2.2L15.5 10" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "wallet": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="3" stroke="currentColor" stroke-width="1.7"/><path d="M3 10h18" stroke="currentColor" stroke-width="1.7"/><circle cx="16.5" cy="14.5" r="1.1" fill="currentColor"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3 3.5 7.5 12 12l8.5-4.5L12 3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="m3.5 12.5 8.5 4.5 8.5-4.5M3.5 17l8.5 4.5L20.5 17" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12.5 3H20a1 1 0 0 1 1 1v7.5L11 21.5 2.5 13 12.5 3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="17" cy="7" r="1.4" fill="currentColor"/></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.4-5.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M20 3.5V8h-4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "gauge": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 17a9 9 0 1 1 16 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M12 13.5 16 9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="14" r="1.6" fill="currentColor"/></svg>',
    "wand": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 20 15 9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="m17 3 1 2.5L20.5 7 18 8.5 17 11l-1-2.5L13.5 7 16 5.5 17 3ZM7 4l.7 1.8L9.5 7 7.7 7.8 7 9.5l-.7-1.7L4.5 7l1.8-1.2L7 4Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="3" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="13.5" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M8 7l1.5-2.5h5L16 7" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 20s-7.5-4.4-7.5-9.2A4.3 4.3 0 0 1 12 7.6a4.3 4.3 0 0 1 7.5 3.2C19.5 15.6 12 20 12 20Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13 2 4.5 13.5H11L10 22l8.5-11.5H12L13 2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.7"/><path d="M12 7.5V12l3 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 3h8l4 4v14H6V3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M14 3v5h4M9 12h6M9 16h6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "link": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l2.6-2.6a4 4 0 1 0-5.7-5.7L11.5 7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M14 10a4 4 0 0 0-5.7 0l-2.6 2.6a4 4 0 1 0 5.7 5.7L12.5 17" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.7"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m12 3 2.6 5.6 6.1.8-4.5 4.2 1.2 6-5.4-3.1L6.6 19.6l1.2-6L3.3 9.4l6.1-.8L12 3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "message": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 5h16v11H9l-5 4V5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8 9h8M8 12.5h5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 12h17M12 3.5c5 4.5 5 12.5 0 17-5-4.5-5-12.5 0-17Z" stroke="currentColor" stroke-width="1.7"/></svg>',
    "palette": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3a9 9 0 1 0 0 18c1.4 0 2-1 2-2s-.6-2-.6-2.8c0-1 .8-1.7 1.8-1.7H18a3 3 0 0 0 3-3A9 9 0 0 0 12 3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="8" cy="9" r="1.3" fill="currentColor"/><circle cx="12" cy="7" r="1.3" fill="currentColor"/><circle cx="16" cy="9" r="1.3" fill="currentColor"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3" stroke="currentColor" stroke-width="1.7"/><path d="m4.5 7.5 7.5 6 7.5-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 3.5h3l1.5 4-2 1.5a11 11 0 0 0 5 5l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 5 5.7 2 2 0 0 1 7 3.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "rocket": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M14 4c3-1 6-1 6-1s0 3-1 6-3 5-6 7l-3-3c2-3 4-6 4-9Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="m10 13-4 4M7 9l-3 1 1 3M15 17l-1 3-3-1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="15.5" cy="8.5" r="1.4" fill="currentColor"/></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.7"/><path d="M10 8.5 16 12l-6 3.5v-7Z" fill="currentColor"/></svg>',
    "cart": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 4h2l2.2 10.2h10.5L20 7H6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9" cy="19" r="1.4" fill="currentColor"/><circle cx="17" cy="19" r="1.4" fill="currentColor"/></svg>',
    "arrow": '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 8h8.5M8.5 4.5 12 8l-3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------
def head(title, desc, body_class):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#081512" />
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/styles.css" />
  <link rel="stylesheet" href="assets/css/pages.css" />
  <script>document.documentElement.classList.add('js');</script>
</head>
<body class="{body_class}">
  <a class="skip-link" href="#main">Skip to content</a>
"""


def header():
    return """
  <header class="site-header" id="top">
    <div class="container">
      <div class="header-bar">
        <a class="brand" href="index.html" aria-label="WebServicers — home">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 40 40" fill="none">
              <rect width="40" height="40" rx="12" fill="url(#wsMarkP)"/>
              <path d="M9.5 13.2 14.9 26.8 20 17.6 25.1 26.8 30.5 13.2" stroke="#fff" stroke-width="3.1" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="34.6" cy="7.6" r="2.2" fill="#E4FF6A"/>
              <defs>
                <linearGradient id="wsMarkP" x1="4" y1="2" x2="36" y2="40" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#0C7C5A"/>
                  <stop offset="1" stop-color="#043B2A"/>
                </linearGradient>
              </defs>
            </svg>
          </span>
          <span class="brand-text"><span class="brand-word">Web</span><span class="brand-word--accent">Servicers</span></span>
        </a>

        <nav class="nav" id="primary-nav" aria-label="Main navigation">
          <ul class="nav-list">
            <li class="has-menu">
              <button class="nav-link" type="button" aria-expanded="false" aria-controls="menu-products">
                Products
                <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
              <div class="dropdown" id="menu-products">
                <div class="dropdown-inner">
                  <div class="dropdown-intro">
                    <p class="dropdown-eyebrow">Online success platform</p>
                    <p class="dropdown-copy">Everything your business needs to win online, in one place.</p>
                  </div>
                  <div class="dropdown-cols">
                    <div class="dropdown-col">
                      <p class="dropdown-title">Presence</p>
                      <a href="website.html">Website</a>
                      <a href="website-design.html">Website Design</a>
                      <a href="seo.html">SEO Tool</a>
                      <a href="google-my-business.html">Google My Business</a>
                    </div>
                    <div class="dropdown-col">
                      <p class="dropdown-title">Promote</p>
                      <a href="google-search-ads.html">Google Search Ads</a>
                      <a href="google-shopping-ads.html">Google Shopping Ads</a>
                      <a href="facebook-ads.html">Facebook Advertising</a>
                      <a href="instagram-ads.html">Instagram Advertising</a>
                    </div>
                  </div>
                </div>
                <div class="dropdown-footer">
                  <p>Ready to grow? Our experts handle the marketing.</p>
                  <a class="btn btn-white btn-sm" href="contact.html">Talk to an expert</a>
                </div>
              </div>
            </li>
            <li><a class="nav-link" href="pricing.html">Pricing</a></li>
            <li><a class="nav-link" href="press.html">Blog</a></li>
            <li class="has-menu">
              <button class="nav-link" type="button" aria-expanded="false" aria-controls="menu-company">
                Company
                <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
              <div class="dropdown dropdown--narrow" id="menu-company">
                <div class="dropdown-inner">
                  <div class="dropdown-col">
                    <a href="about.html">About us</a>
                    <a href="careers.html">Career</a>
                    <a href="press.html">Press</a>
                    <a href="help.html">Get help</a>
                  </div>
                </div>
              </div>
            </li>
          </ul>

          <div class="nav-cta">
            <a class="btn btn-ghost" href="login.html">Sign in</a>
            <a class="btn btn-primary" href="pricing.html">Get started</a>
          </div>
        </nav>

        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>
"""


def footer():
    return """
  <footer class="site-footer" id="footer">
    <div class="container">
      <div class="footer-cols">
        <div class="footer-col">
          <h3>Presence</h3>
          <ul>
            <li><a href="website.html">Website</a></li>
            <li><a href="website-design.html">Website Design</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3>Reach</h3>
          <ul>
            <li><a href="seo.html">SEO Tool</a></li>
            <li><a href="google-my-business.html">Google My Business</a></li>
            <li><a href="marketing-analytics.html">Marketing Analytics</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3>Promote</h3>
          <ul>
            <li><a href="google-search-ads.html">Google Search Ads</a></li>
            <li><a href="google-shopping-ads.html">Google Shopping Ads</a></li>
            <li><a href="facebook-ads.html">Facebook Ads</a></li>
            <li><a href="instagram-ads.html">Instagram Ads</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3>Company</h3>
          <ul>
            <li><a href="about.html">About us</a></li>
            <li><a href="help.html">Get help</a></li>
            <li><a href="careers.html">Career</a></li>
            <li><a href="press.html">Press &amp; Media</a></li>
          </ul>
        </div>
        <div class="footer-col footer-col--partner">
          <h3>Partnership</h3>
          <p class="partner-text">We are your Official Google Premier Partner and Meta Business Partner.</p>
          <div class="badges">
            <span class="badge">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M21.35 11.1h-9.17v2.73h6.51c-.33 3.81-3.5 5.44-6.5 5.44C8.36 19.27 5 16.25 5 12c0-4.1 3.2-7.27 7.2-7.27 3.09 0 4.9 1.97 4.9 1.97L19 4.72S16.56 2 12.1 2C6.42 2 2.03 6.8 2.03 12c0 5.05 4.13 10 10.22 10 5.35 0 9.25-3.67 9.25-9.09 0-1.15-.15-1.81-.15-1.81Z"/></svg>
              Google Premier Partner
            </span>
            <span class="badge">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M24 12.07C24 5.44 18.63.07 12 .07S0 5.44 0 12.07c0 5.99 4.39 10.95 10.13 11.85v-8.38H7.08v-3.47h3.05V9.43c0-3.01 1.79-4.67 4.53-4.67 1.31 0 2.69.24 2.69.24v2.95h-1.51c-1.49 0-1.96.93-1.96 1.88v2.25h3.33l-.53 3.47h-2.8v8.38C19.61 23.02 24 18.06 24 12.07Z"/></svg>
              Meta Business Partner
            </span>
          </div>
          <div class="footer-social" aria-label="Social media">
            <a href="facebook-ads.html" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M24 12.07C24 5.44 18.63.07 12 .07S0 5.44 0 12.07c0 5.99 4.39 10.95 10.13 11.85v-8.38H7.08v-3.47h3.05V9.43c0-3.01 1.79-4.67 4.53-4.67 1.31 0 2.69.24 2.69.24v2.95h-1.51c-1.49 0-1.96.93-1.96 1.88v2.25h3.33l-.53 3.47h-2.8v8.38C19.61 23.02 24 18.06 24 12.07Z"/></svg></a>
            <a href="instagram-ads.html" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.4" y="2.4" width="19.2" height="19.2" rx="5.6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.3" fill="currentColor"/></svg></a>
            <a href="google-search-ads.html" aria-label="YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.19a3.02 3.02 0 0 0-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.5A3.02 3.02 0 0 0 .5 6.19C0 8.07 0 12 0 12s0 3.93.5 5.81a3.02 3.02 0 0 0 2.12 2.14c1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14C24 15.93 24 12 24 12s0-3.93-.5-5.81ZM9.55 15.57V8.43L15.82 12l-6.27 3.57Z"/></svg></a>
            <a href="about.html" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13Zm1.78 13.02H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg></a>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p class="copyright">Copyright © 2026 WebServicers</p>
        <ul class="legal">
          <li><a href="terms.html">Terms of Service</a></li>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="sitemap.html">Sitemap</a></li>
        </ul>
      </div>
    </div>
  </footer>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def cta_block(h2, copy, primary="#pricing", primary_label="See plans"):
    return f"""
    <section class="cta">
      <div class="container">
        <div class="cta-card" data-reveal>
          <span class="cta-spark cta-spark--1" aria-hidden="true">✦</span>
          <span class="cta-spark cta-spark--2" aria-hidden="true">✦</span>
          <div class="cta-copy">
            <span class="eyebrow-pill eyebrow-pill--dark">Let's go</span>
            <h2>{h2}</h2>
            <p>{copy}</p>
          </div>
          <div class="cta-actions">
            <a class="btn btn-light btn-lg" href="{primary}">{primary_label}</a>
            <a class="btn btn-glass btn-lg" href="contact.html">Talk to an expert</a>
          </div>
        </div>
      </div>
    </section>
"""


# --------------------------------------------------------------------------
# Mockups
# --------------------------------------------------------------------------
def browser(inner, url="yourbusiness.com"):
    return f"""
      <div class="browser">
        <div class="browser-bar">
          <span class="browser-dots"><i></i><i></i><i></i></span>
          <span class="browser-url">{url}</span>
        </div>
        <div class="browser-body">{inner}</div>
      </div>"""


def monitor(inner):
    return f"""
      <div class="monitor">
        <div class="monitor-screen">{inner}</div>
        <div class="monitor-stand"></div>
        <div class="monitor-base"></div>
      </div>"""


def phone(inner, cls=""):
    return f"""
      <div class="phone {cls}">
        <div class="phone-screen">{inner}</div>
      </div>"""


def m_ads_serp():
    ad = """
          <div class="ad">
            <div class="ad-head"><span class="ad-tag">Sponsored</span><span class="ad-brand">Your Business</span></div>
            <p class="ad-title">24/7 Emergency Plumber · 60-Minute Response</p>
            <p class="ad-url">yourbusiness.com › emergency</p>
            <p class="ad-copy">Licensed local plumbers, fixed quotes and no call-out fee. Book online in 60 seconds.</p>
            <div class="ad-ext"><span>Call now</span><span>Directions</span><span>Get a quote</span></div>
          </div>
          <div class="ad ad--muted">
            <div class="ad-head"><span class="ad-tag">Sponsored</span><span class="ad-brand">City Plumbing Co.</span></div>
            <p class="ad-title">Local Plumbers You Can Trust</p>
            <p class="ad-url">cityplumbing.example › services</p>
            <p class="ad-copy">Same-day repairs across the city. Rated 4.8 by 300 neighbours.</p>
          </div>"""
    inner = f"""
        <div class="serp">
          <div class="serp-top">
            <span class="serp-logo">G</span>
            <div class="serp-field">emergency plumber near me</div>
          </div>
          <div class="serp-tabs"><span class="is-active">All</span><span>Maps</span><span>Shopping</span><span>Images</span></div>
          {ad}
        </div>"""
    return monitor(inner)


def m_rank_browser():
    inner = """
        <div class="serp">
          <div class="serp-top">
            <span class="serp-logo">G</span>
            <div class="serp-field">artisan donuts near me</div>
          </div>
          <div class="serp-tabs"><span class="is-active">All</span><span>Maps</span><span>Images</span></div>
          <div class="serp-highlight">
            <div class="ad-head"><span class="ad-rank">1</span><span class="ad-brand">Flour &amp; Co.</span></div>
            <p class="ad-title">Artisan Donuts Baked Fresh Every Morning</p>
            <p class="ad-url">flourandco.example › menu</p>
            <div class="ad-ext"><span>Menu</span><span>Order online</span><span>Directions</span></div>
          </div>
          <div class="ad"><p class="ad-title">Donut Delivery In 30 Minutes</p><p class="ad-url">donutdelivery.example</p></div>
          <div class="ad"><p class="ad-title">Best Rated Donuts In Town</p><p class="ad-url">citybakes.example</p></div>
        </div>"""
    return browser(inner, "google.com/search?q=artisan+donuts")


def m_shop_phone():
    products = [
        ("Ribbed planter", "£24.00", ""),
        ("Terra pot", "£18.00", "prod-img--2"),
        ("Glazed bowl", "£32.00", "prod-img--3"),
        ("Clay set", "£41.00", "prod-img--4"),
    ]
    grid = "".join(
        f'<div class="prod"><span class="prod-img {cls}"></span><span class="prod-name">{name}</span><span class="prod-price">{price}</span></div>'
        for name, price, cls in products
    )
    return phone(
        f"""
        <div class="phone-head"><strong>Shopping</strong><span class="phone-pill">Free listings</span></div>
        <div class="phone-search">ceramic planters</div>
        <div class="shop-grid">{grid}</div>"""
    )


def m_fb_phone():
    return phone(
        """
        <div class="feed">
          <div class="feed-head">
            <span class="avatar">YB</span>
            <div><strong>Your Business</strong><span>Sponsored · Suggested for you</span></div>
          </div>
          <p class="feed-text">Spring is here. Refresh your space with 20% off handmade planters — this week only.</p>
          <div class="feed-img"></div>
          <div class="feed-cta"><strong>yourbusiness.example</strong><span>SHOP NOW</span></div>
          <div class="feed-social"><span>👍 ❤️ 1.2k</span><span>84 comments · 210 shares</span></div>
        </div>"""
    )


def m_ig_phone():
    return phone(
        """
        <div class="ig-head"><span class="avatar avatar--grad">YB</span><strong>yourbusiness</strong></div>
        <div class="ig-img"><span class="ig-badge">Reel</span></div>
        <div class="ig-actions"><span>♥</span><span>◯</span><span>➤</span></div>
        <p class="ig-caption"><strong>yourbusiness</strong> New drop. Six colours, made in small batches. Tap to shop ✨</p>"""
    )


def m_map_browser():
    inner = """
        <div class="map">
          <span class="map-pin"></span>
          <div class="map-card">
            <div class="map-stars">★★★★★ <span style="color:#716c80;font-size:.56rem">4.9 · 212 reviews</span></div>
            <h4>Flour &amp; Co. Bakery</h4>
            <div class="map-meta"><span>Bakery · Open until 18:00</span><span>12 Market Street</span></div>
            <div class="map-actions"><span>Call</span><span>Directions</span><span>Website</span></div>
          </div>
        </div>"""
    return browser(inner, "google.com/maps › flour-and-co")


def m_dash_browser():
    inner = """
        <div class="dash">
          <div class="dash-head">
            <span class="dash-title">Growth overview</span>
            <span class="dash-live"><i></i> Live</span>
          </div>
          <div class="kpis">
            <div class="kpi"><span>Visitors</span><strong>24.8k <em>+38%</em></strong></div>
            <div class="kpi"><span>Leads</span><strong>412 <em>+19%</em></strong></div>
            <div class="kpi"><span>Revenue</span><strong>£84k <em>+42%</em></strong></div>
          </div>
          <svg class="dash-chart" viewBox="0 0 460 130" preserveAspectRatio="none">
            <defs>
              <linearGradient id="dashFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#12a150" stop-opacity=".22"/>
                <stop offset="1" stop-color="#12a150" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <g stroke="#f0eef6" stroke-width="1">
              <line x1="0" y1="34" x2="460" y2="34"/><line x1="0" y1="70" x2="460" y2="70"/><line x1="0" y1="106" x2="460" y2="106"/>
            </g>
            <path d="M0 108 L58 92 L116 100 L174 70 L232 78 L290 50 L348 58 L406 30 L460 16 L460 130 L0 130 Z" fill="url(#dashFill)"/>
            <path d="M0 108 L58 92 L116 100 L174 70 L232 78 L290 50 L348 58 L406 30 L460 16" fill="none" stroke="#12a150" stroke-width="2.5" stroke-linecap="round"/>
          </svg>
          <div class="dash-legend"><span><i></i> Organic</span><span><i style="background:#ff8a5b"></i> Paid</span><span><i style="background:#f5b301"></i> Direct</span></div>
        </div>"""
    return browser(inner, "analytics.yourbusiness.example")


def m_site_browser():
    inner = """
        <div class="mini-site">
          <div class="mini-site-head">
            <span class="mini-site-logo">FLOUR &amp; CO.</span>
            <div class="mini-site-nav"><span></span><span></span><span></span></div>
          </div>
          <div class="mini-site-hero">
            <div>
              <h3>Any flavor<br />you desire</h3>
              <p>Small-batch donuts, baked every morning.</p>
              <span class="mini-site-btn">Order now</span>
            </div>
            <div class="mini-donuts">
              <span class="mini-donut mini-donut--1"></span>
              <span class="mini-donut mini-donut--2"></span>
              <span class="mini-donut mini-donut--3"></span>
            </div>
          </div>
          <div class="mini-strip">
            <div class="mini-tile"><i></i><span></span></div>
            <div class="mini-tile"><i></i><span></span></div>
            <div class="mini-tile"><i></i><span></span></div>
          </div>
        </div>"""
    return browser(inner, "flourandco.example")


def m_design_browser():
    inner = """
        <div class="design-board">
          <div>
            <div class="wire">
              <div class="wire-line wire-line--dark"></div>
              <div class="wire-line"></div>
              <div class="wire-box"></div>
              <div class="wire-line" style="width:76%"></div>
              <div class="wire-line wire-line--accent"></div>
            </div>
            <div class="wire" style="margin-top:8px">
              <div class="wire-line" style="width:52%"></div>
              <div class="wire-line" style="width:84%"></div>
              <div class="wire-line" style="width:64%"></div>
            </div>
          </div>
          <div class="wire">
            <div class="type-sample">Aa</div>
            <div class="type-label">Poppins · Display</div>
            <div class="swatches"><i></i><i></i><i></i><i></i></div>
            <div class="wire-line" style="margin-top:12px"></div>
            <div class="wire-line" style="width:70%"></div>
          </div>
        </div>"""
    return browser(inner, "figma.com › flour-and-co")


def m_brand_browser():
    inner = """
        <div class="design-board" style="grid-template-columns:1fr 1fr">
          <div class="wire">
            <div class="type-label">Wordmark</div>
            <div style="font-family:var(--display);font-size:1.5rem;font-weight:600;letter-spacing:-.05em;color:#1b1530;margin:8px 0">Flour &amp; Co.</div>
            <div class="swatches"><i></i><i></i><i></i><i></i></div>
          </div>
          <div class="wire">
            <div class="type-label">Type scale</div>
            <div style="font-family:var(--display);font-size:1.4rem;color:#1b1530">Heading</div>
            <div style="font-size:.7rem;color:#6f6a7e;margin-top:4px">Body copy sample for the brand.</div>
            <div class="wire-line" style="margin-top:10px"></div>
            <div class="wire-line" style="width:64%"></div>
          </div>
          <div class="wire" style="grid-column:span 2;display:flex;gap:8px">
            <div class="wire-box" style="flex:1;margin:0;background:#fff1e8"></div>
            <div class="wire-box" style="flex:1;margin:0;background:#eef1ff"></div>
            <div class="wire-box" style="flex:1;margin:0;background:#f6f3ec"></div>
          </div>
        </div>"""
    return browser(inner, "brand.flourandco.example")


def m_feed_table():
    rows = [
        ("Ribbed planter", "£24.00", "Approved", "#e8d7c4"),
        ("Terra pot", "£18.00", "Approved", "#d9e5d6"),
        ("Glazed bowl", "£32.00", "Approved", "#e9def5"),
        ("Clay set", "£41.00", "Needs image", "#f6e7d2"),
    ]
    body = "".join(
        f'<div class="ft-row"><span class="ft-thumb" style="--c:{c}"></span>'
        f'<span class="ft-name">{n}</span><span class="ft-price">{p}</span>'
        f'<span class="ft-status{" ft-status--warn" if s != "Approved" else ""}">{s}</span></div>'
        for n, p, s, c in rows
    )
    inner = f"""
        <div class="ft">
          <div class="ft-head"><span>Product feed</span><span class="mk-pill">98% approved</span></div>
          {body}
        </div>"""
    return browser(inner, "merchant.google.com › products")


def m_ig_grid():
    inner = """
        <div class="ig-grid">
          <span class="ig-tile ig-tile--1"></span>
          <span class="ig-tile ig-tile--2"></span>
          <span class="ig-tile ig-tile--3"></span>
          <span class="ig-tile ig-tile--4"></span>
          <span class="ig-tile ig-tile--5"></span>
          <span class="ig-tile ig-tile--6"></span>
        </div>"""
    return browser(inner, "instagram.com › yourbusiness")


def m_reviews_phone():
    return phone(
        """
        <div class="rev-head"><strong>Reviews</strong><span class="phone-pill">4.9 ★</span></div>
        <div class="rev-score"><strong>212</strong><span>reviews this year</span></div>
        <div class="rev-card">
          <div class="rev-stars">★★★★★</div>
          <p>“Fast, tidy and honest about the price. Booked again for next month.”</p>
          <span>Sarah C. · 2 days ago</span>
        </div>
        <div class="rev-card">
          <div class="rev-stars">★★★★★</div>
          <p>“Turned up on a Sunday and fixed it in an hour. Lifesavers.”</p>
          <span>Tom H. · 1 week ago</span>
        </div>
        <div class="rev-actions"><span>Request a review</span></div>"""
    )


def m_digest_phone():
    return phone(
        """
        <div class="phone-head"><strong>Weekly digest</strong><span class="phone-pill">Mon 08:00</span></div>
        <p class="dg-title">Your week in three numbers</p>
        <div class="dg-kpis">
          <div><strong>£3.2k</strong><span>spend</span></div>
          <div><strong>86</strong><span>leads</span></div>
          <div><strong>4.1x</strong><span>ROAS</span></div>
        </div>
        <div class="dg-note"><strong>Best performer</strong><span>Google Search · £12.40 per lead</span></div>
        <div class="dg-note"><strong>Watch out</strong><span>Meta frequency at 4.1 — refresh creative</span></div>
        <div class="mk-dotline"><i></i> One action for this week: shift £400 to Search.</div>"""
    )


def m_site_phone():
    return phone(
        """
        <div class="mini-site mini-site--phone">
          <div class="mini-site-head">
            <span class="mini-site-logo">FLOUR &amp; CO.</span>
            <span style="font-size:1rem;color:#241b12">≡</span>
          </div>
          <div class="mini-donuts" style="height:110px">
            <span class="mini-donut mini-donut--1" style="width:78px;height:78px"></span>
            <span class="mini-donut mini-donut--2" style="width:52px;height:52px"></span>
          </div>
          <h3 style="font-family:var(--display);font-size:1.3rem;line-height:1.05;letter-spacing:-.03em;color:#241b12;margin-top:6px">Any flavor<br />you desire</h3>
          <p style="font-size:.58rem;color:#857a6b;margin:6px 0 8px">Small-batch donuts, baked every morning.</p>
          <span class="mini-site-btn">Order now</span>
          <div class="mini-strip" style="grid-template-columns:1fr 1fr;margin-top:10px">
            <div class="mini-tile"><i></i><span></span></div>
            <div class="mini-tile"><i></i><span></span></div>
          </div>
        </div>"""
    )


MOCKUPS = {
    "ads_serp": m_ads_serp,
    "rank_browser": m_rank_browser,
    "shop_phone": m_shop_phone,
    "fb_phone": m_fb_phone,
    "ig_phone": m_ig_phone,
    "map_browser": m_map_browser,
    "dash_browser": m_dash_browser,
    "site_browser": m_site_browser,
    "design_browser": m_design_browser,
    "brand_browser": m_brand_browser,
    "feed_table": m_feed_table,
    "ig_grid": m_ig_grid,
    "reviews_phone": m_reviews_phone,
    "digest_phone": m_digest_phone,
    "site_phone": m_site_phone,
}


# --------------------------------------------------------------------------
# Blocks
# --------------------------------------------------------------------------
def crumbs(items):
    parts = []
    for label, href in items:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span class="current">{label}</span>')
        parts.append('<span class="sep">/</span>')
    if parts:
        parts = parts[:-1]
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def results_block(s):
    r = s["results"]
    checks = "".join(f"<li>{c}</li>" for c in r["checks"])
    tags = "".join(f"<span>{t}</span>" for t in r["tags"])
    foot_kicker, foot_value, foot_delta = r["foot"]
    return f"""
    <section class="results">
      <div class="container results-inner">
        <div class="result-panel" data-reveal>
          <div class="gauge" style="--val:{r['gauge'][0]}%">
            <div class="gauge-inner"><strong>{r['gauge'][0]}</strong><span>{r['gauge'][1]}</span></div>
          </div>
          <div class="result-tags">{tags}</div>
          <div class="result-foot">
            <span>{foot_kicker}</span>
            <strong>{foot_value}</strong>
            <em>{foot_delta}</em>
          </div>
        </div>
        <div class="results-copy" data-reveal>
          <span class="eyebrow-pill">Results</span>
          <h2>{r['h2']}</h2>
          <p>{r['copy']}</p>
          <ul class="check-list">{checks}</ul>
        </div>
      </div>
    </section>"""


def pricing_block(s):
    p = s["pricing"]
    cards = ""
    for i, tier in enumerate(p["tiers"]):
        featured = " price-card--featured" if i == 1 else ""
        ribbon = '<span class="price-ribbon">Most popular</span>' if i == 1 else ""
        feats = "".join(f"<li>{f}</li>" for f in tier["features"])
        cards += f"""
            <article class="price-card{featured}">
              {ribbon}
              <p class="price-name">{tier['name']}</p>
              <p class="price-amount">{tier['price']}<small>{tier['period']}</small></p>
              <p class="price-note">{tier['note']}</p>
              <ul class="price-list">{feats}</ul>
              <a class="btn {'btn-primary' if i == 1 else 'btn-outline'}" href="index.html#get-started">{tier['cta']}</a>
            </article>"""
    ent = p["enterprise"]
    ent_feats = "".join(f"<li>{b}</li>" for b in ent["bullets"])
    return f"""
    <section class="pricing" id="pricing">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow-pill">Pricing</span>
          <h2>{p['h2']}</h2>
          <p>{p['copy']}</p>
        </div>
        <div class="price-grid">{cards}
        </div>
        <div class="enterprise">
          <div>
            <h3>Enterprise</h3>
            <p>{ent['note']}</p>
          </div>
          <ul>{ent_feats}</ul>
          <a class="btn" href="index.html#get-started">{ent['cta']}</a>
        </div>
        <p class="pricing-note">All plans exclude ad spend. No setup fees, no lock-in. <a href="help.html">Questions about billing?</a></p>
      </div>
    </section>"""


def features_block(s):
    f = s["features"]
    items = "".join(
        f"""
          <article class="feature" data-reveal>
            <span class="feature-icon">{ICONS.get(key, ICONS['bolt'])}</span>
            <h3>{title}</h3>
            <p>{text}</p>
          </article>"""
        for key, title, text in f["items"]
    )
    return f"""
    <section class="features">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow-pill">{f['eyebrow']}</span>
          <h2>{f['h2']}</h2>
          <p>{f['copy']}</p>
        </div>
        <div class="feature-grid">{items}
        </div>
      </div>
    </section>"""


def showcase_block(s):
    sc = s["showcase"]
    visual = MOCKUPS[sc["visual"]]()
    bullets = "".join(f"<li>{b}</li>" for b in sc["bullets"])
    link = f'<a class="link-arrow link-arrow--dark" href="{sc["link"]}">{sc["link_label"]}</a>' if sc.get("link") else ""
    return f"""
    <section class="showcase">
      <div class="container">
        <div class="showcase-panel">
          <div class="showcase-copy" data-reveal>
            <span class="eyebrow-pill">{sc['eyebrow']}</span>
            <h2>{sc['h2']}</h2>
            <p>{sc['copy']}</p>
            <ul>{bullets}</ul>
            {link}
          </div>
          <div class="showcase-visual" data-reveal>{visual}
          </div>
        </div>
      </div>
    </section>"""


def faq_block(s):
    items = ""
    for i, (q, a) in enumerate(s["faq"]):
        open_attr = " open" if i == 0 else ""
        items += f"""
          <details class="faq-item"{open_attr}>
            <summary>{q}<span class="faq-plus" aria-hidden="true"></span></summary>
            <div class="faq-answer"><p>{a}</p></div>
          </details>"""
    return f"""
    <section class="faq svc-faq" id="faq">
      <div class="container faq-grid">
        <div class="faq-intro">
          <span class="eyebrow-pill">Good to know</span>
          <h2>Questions,<br />answered</h2>
          <p>Everything clients ask before starting {s['crumb']}.</p>
          <div class="help-card">
            <div class="help-avatars" aria-hidden="true"><span>SC</span><span>TH</span><span>SM</span></div>
            <div>
              <strong>Still curious?</strong>
              <a class="link-arrow link-arrow--dark" href="help.html">Visit the help centre</a>
            </div>
          </div>
        </div>
        <div class="faq-list">{items}
        </div>
      </div>
    </section>"""


def service_page(s):
    hero_visual = MOCKUPS[s["visual"]]()
    points = "".join(f"<li>{p}</li>" for p in s["points"])
    fa, fb = s["float_a"], s["float_b"]
    content = f"""
  <main id="main">
    <section class="page-hero">
      <div class="container page-hero-inner">
        <div class="page-hero-copy">
          {crumbs([("Home", "index.html"), ("Services", "pricing.html"), (s['crumb'], None)])}
          <span class="eyebrow-pill eyebrow-pill--dark">{s['eyebrow']}</span>
          <h1>{s['h1']}</h1>
          <p class="page-lead">{s['lead']}</p>
          <div class="hero-actions">
            <a class="btn btn-lg" style="background:var(--accent);color:var(--accent-contrast)" href="#pricing">See pricing</a>
            <a class="link-arrow" href="contact.html">Talk to an expert</a>
          </div>
          <ul class="hero-points">{points}</ul>
        </div>
        <div class="page-hero-visual" aria-hidden="true">
          <span class="hero-float hero-float--a"><strong>{fa[0]}</strong><span>{fa[1]}</span></span>
          <span class="hero-float hero-float--b"><strong>{fb[0]}</strong><span>{fb[1]}</span></span>
          {hero_visual}
        </div>
      </div>
    </section>

    {results_block(s)}
    {pricing_block(s)}
    {features_block(s)}
    {showcase_block(s)}
    {faq_block(s)}
    {cta_block(s['cta']['h2'], s['cta']['copy'], s['cta']['primary'], s['cta']['primary_label'])}
  </main>
"""
    title = f"{s['crumb']} — {BRAND}"
    desc = s["lead"][:155]
    return head(title, ihtml.escape(desc, quote=True), f"page {s['theme']}") + header() + content + footer()


# --------------------------------------------------------------------------
# Company pages
# --------------------------------------------------------------------------
def simple_hero(eyebrow, h1, lead, center=False, extra=""):
    cls = " simple-hero--center" if center else ""
    return f"""
    <section class="simple-hero{cls}">
      <div class="container">
        {crumbs([("Home", "index.html"), (eyebrow, None)]) if not center else ""}
        <span class="eyebrow-pill">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="page-lead">{lead}</p>
        {extra}
      </div>
    </section>"""


def stat_strip(stats):
    cells = "".join(f"<div><strong>{v}</strong><span>{l}</span></div>" for v, l in stats)
    return f'<div class="stat-strip">{cells}</div>'


def about_page(c):
    values = "".join(
        f"""
          <article class="value-card" data-reveal>
            <span class="feature-icon">{ICONS.get(k, ICONS['bolt'])}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </article>"""
        for k, t, d in c["values"]
    )
    team = "".join(
        f"""
          <article class="team-card" data-reveal>
            <div class="team-avatar">{initials}</div>
            <h3>{name}</h3>
            <p>{role}</p>
            <p class="team-quote">{bio}</p>
          </article>"""
        for name, role, bio, initials in c["team"]
    )
    story = "".join(f"<p>{p}</p>" for p in c["story"])
    story_art = """
        <div class="story-art" data-reveal aria-hidden="true">
          <div class="story-tile story-tile--a">
            <div class="t-kicker">Client results</div>
            <div class="t-big">+128%</div>
            <div class="t-small">organic traffic in 6 months</div>
            <div class="t-bars"><i></i><i></i><i></i><i></i><i></i></div>
          </div>
          <div class="story-tile story-tile--b">
            <div class="t-kicker">The team</div>
            <div class="story-avatars"><span>MC</span><span>JB</span><span>PR</span><span>SO</span></div>
            <div class="t-small" style="margin-top:8px">38 specialists, 6 countries</div>
          </div>
          <div class="story-tile story-tile--c">
            <div class="t-kicker">Since 2016</div>
            <div class="t-big">212</div>
            <div class="t-small">businesses launched</div>
          </div>
        </div>"""
    content = f"""
  <main id="main">
    {simple_hero(c['eyebrow'], c['h1'], c['lead'], extra=stat_strip(c['stats']))}

    <section class="content-section">
      <div class="container story-grid">
        <div class="story-copy" data-reveal>
          <span class="eyebrow-pill">Our story</span>
          <h2>{c['story_title']}</h2>
          {story}
          <a class="btn btn-outline" href="careers.html">Come work with us</a>
        </div>
        {story_art}
      </div>
    </section>

    <section class="content-section content-section--cream">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow-pill">Values</span>
          <h2>{c['values_title']}</h2>
        </div>
        <div class="value-grid">{values}
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow-pill">Team</span>
          <h2>{c['team_title']}</h2>
        </div>
        <div class="team-grid">{team}
        </div>
      </div>
    </section>

    {cta_block(c['cta_h2'], c['cta_copy'], "pricing.html", "See plans")}
  </main>
"""
    return head(c["title"], c["desc"], "page theme-violet") + header() + content + footer()


def careers_page(c):
    perks = "".join(
        f"""
          <article class="perk" data-reveal>
            <span class="feature-icon">{ICONS.get(k, ICONS['bolt'])}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </article>"""
        for k, t, d in c["perks"]
    )
    jobs = "".join(
        f"""
          <a class="job" href="help.html">
            <div>
              <h3>{title}</h3>
              <span class="job-team">{team}</span>
            </div>
            <span class="job-meta">{loc}</span>
            <span class="job-meta">{kind}</span>
            <span class="job-arrow">{ICONS['arrow']}</span>
          </a>"""
        for title, team, loc, kind in c["jobs"]
    )
    content = f"""
  <main id="main">
    {simple_hero(c['eyebrow'], c['h1'], c['lead'])}

    <section class="content-section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow-pill">Benefits</span>
          <h2>{c['perks_title']}</h2>
        </div>
        <div class="perks">{perks}
        </div>
      </div>
    </section>

    <section class="content-section content-section--grey">
      <div class="container">
        <div class="section-head section-head--left">
          <span class="eyebrow-pill">Open roles</span>
          <h2>{c['jobs_title']}</h2>
          <p>Every role is listed with the team, location and contract type. No mystery applications.</p>
        </div>
        <div class="job-list">{jobs}
        </div>
      </div>
    </section>

    {cta_block(c['cta_h2'], c['cta_copy'], "help.html", "Say hello")}
  </main>
"""
    return head(c["title"], c["desc"], "page theme-violet") + header() + content + footer()


def press_page(c):
    releases = "".join(
        f"""
          <article class="press-item">
            <span class="press-date">{date}</span>
            <div>
              <h3>{title}</h3>
              <p>{body}</p>
            </div>
            <a class="press-link" href="help.html">Read more {ICONS['arrow']}</a>
          </article>"""
        for date, title, body in c["releases"]
    )
    assets = """
          <article class="asset-card">
            <div class="asset-swatch"><svg viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M9.5 13.2 14.9 26.8 20 17.6 25.1 26.8 30.5 13.2" stroke="#fff" stroke-width="3.1" stroke-linecap="round" stroke-linejoin="round"/><circle cx="34.6" cy="7.6" r="2.2" fill="#E4FF6A"/></svg><b>WebServicers</b></div>
            <h3>Logo pack</h3>
            <p>The Signal W mark and WebServicers lockup in SVG.</p>
            <a href="assets/img/logo.svg">Download ↗</a>
          </article>
          <article class="asset-card">
            <div class="asset-swatch"><i style="background:#0b7a53"></i><i style="background:#ff8a5b"></i><i style="background:#e4ff6a"></i></div>
            <h3>Brand colours</h3>
            <p>Palette values and accessible pairings for print and screen.</p>
            <a href="index.html">Download ↗</a>
          </article>
          <article class="asset-card">
            <div class="asset-swatch asset-swatch--photo"><i></i><i></i><i></i></div>
            <h3>Team photography</h3>
            <p>Approved portraits and office imagery for editorial use.</p>
            <a href="index.html">Download ↗</a>
          </article>"""
    content = f"""
  <main id="main">
    {simple_hero(c['eyebrow'], c['h1'], c['lead'])}

    <section class="content-section">
      <div class="container">
        <div class="section-head section-head--left">
          <span class="eyebrow-pill">Latest news</span>
          <h2>Press releases</h2>
        </div>
        <div class="press-list">{releases}
        </div>
      </div>
    </section>

    <section class="content-section content-section--cream">
      <div class="container">
        <div class="section-head section-head--left">
          <span class="eyebrow-pill">Brand assets</span>
          <h2>Everything you need for the story</h2>
          <p>Please do not alter the logo, change the brand colours or crop team photography without checking with us first.</p>
        </div>
        <div class="asset-grid">{assets}
        </div>
      </div>
    </section>

    {cta_block(c['cta_h2'], c['cta_copy'], "help.html", "Contact the press team")}
  </main>
"""
    return head(c["title"], c["desc"], "page theme-indigo") + header() + content + footer()


def help_page(c):
    topics = "".join(
        f"""
          <a class="help-topic" href="help.html">
            <span class="feature-icon">{ICONS.get(k, ICONS['bolt'])}</span>
            <h3>{t}</h3>
            <p>{d}</p>
            <span>{count} →</span>
          </a>"""
        for k, t, d, count in c["topics"]
    )
    articles = "".join(
        f'<a class="article-row" href="help.html">{title}<span>{meta}</span></a>'
        for title, meta in c["articles"]
    )
    search = """
        <form class="help-search" role="search" onsubmit="return false;">
          <label class="sr-only" for="help-q" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Search help</label>
          <input id="help-q" type="search" placeholder="Search for an answer — websites, SEO, billing…" />
          <button class="btn btn-primary" type="submit">Search</button>
        </form>"""
    content = f"""
  <main id="main">
    {simple_hero(c['eyebrow'], c['h1'], c['lead'], extra=search)}

    <section class="content-section">
      <div class="container">
        <div class="section-head section-head--left">
          <span class="eyebrow-pill">Browse</span>
          <h2>Help by topic</h2>
        </div>
        <div class="help-topics">{topics}
        </div>
      </div>
    </section>

    <section class="content-section content-section--grey">
      <div class="container">
        <div class="section-head section-head--left">
          <span class="eyebrow-pill">Popular</span>
          <h2>Most read this week</h2>
        </div>
        <div class="article-list">{articles}
        </div>
      </div>
    </section>

    {cta_block(c['cta_h2'], c['cta_copy'], "index.html#get-started", "Send a message")}
  </main>
"""
    return head(c["title"], c["desc"], "page theme-indigo") + header() + content + footer()


def legal_page(key, c):
    toc = "".join(
        f'<li><a href="#s{i+1}">{title}</a></li>' for i, (title, _) in enumerate(c["sections"])
    )
    body = ""
    for i, (title, paras) in enumerate(c["sections"]):
        chunks = ""
        for para in paras:
            if para.startswith("- "):
                chunks += f"<ul><li>{para[2:]}</li></ul>"
            else:
                chunks += f"<p>{para}</p>"
        body += f'<h2 id="s{i+1}">{title}</h2>{chunks}'
    content = f"""
  <main id="main">
    {simple_hero(c['eyebrow'], c['h1'], c['lead'])}

    <section class="content-section">
      <div class="container legal-layout">
        <aside class="legal-toc" aria-label="On this page">
          <p>On this page</p>
          <ol>{toc}</ol>
        </aside>
        <div class="prose">
          <span class="legal-updated">{c['updated']}</span>
          <div class="notice">This is a demonstration document for the WebServicers website. It is not legal advice. Have your own terms reviewed before you use them with clients.</div>
          {body}
        </div>
      </div>
    </section>
  </main>
"""
    return head(c["title"], c["desc"], "page theme-indigo") + header() + content + footer()


def sitemap_page():
    groups = {
        "Services": [
            ("Website", "website.html"),
            ("Website Design", "website-design.html"),
            ("SEO Tool", "seo.html"),
            ("Google My Business", "google-my-business.html"),
            ("Marketing Analytics", "marketing-analytics.html"),
            ("Google Search Ads", "google-search-ads.html"),
            ("Google Shopping Ads", "google-shopping-ads.html"),
            ("Facebook Ads", "facebook-ads.html"),
            ("Instagram Ads", "instagram-ads.html"),
        ],
        "Company": [
            ("Talk to an expert", "contact.html"),
            ("About us", "about.html"),
            ("Careers", "careers.html"),
            ("Press &amp; Media", "press.html"),
            ("Help centre", "help.html"),
            ("Pricing", "pricing.html"),
            ("Home", "index.html"),
        ],
        "Account": [
            ("Sign in", "login.html"),
            ("Create account", "signup.html"),
            ("Reset password", "forgot-password.html"),
        ],
        "Legal": [
            ("Terms of Service", "terms.html"),
            ("Privacy Policy", "privacy.html"),
            ("Sitemap", "sitemap.html"),
        ],
    }
    cards = ""
    for title, links in groups.items():
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links)
        cards += f'<div class="sitemap-card"><h2>{title}</h2><ul>{items}</ul></div>'
    content = f"""
  <main id="main">
    {simple_hero("Sitemap", "Every page, one list.", "A complete map of WebServicers — services, plans, company pages and the legal bits.")}
    <section class="content-section">
      <div class="container sitemap-grid">{cards}
      </div>
    </section>
    {cta_block("Not sure where to start?", "Tell us what your business needs and we will point you to the right service — or tell you honestly that you do not need us yet.", "pricing.html", "Compare plans")}
  </main>
"""
    return head("Sitemap — " + BRAND, "All pages on the WebServicers website.", "page theme-indigo") + header() + content + footer()


def pricing_page():
    cards = ""
    lookup = {s["slug"]: s for s in SERVICES}
    for slug, label, price, tag in PRICING_PLANS:
        s = lookup[slug]
        start = s["pricing"]["tiers"][0]["price"]
        icon_key = {
            "google-search-ads": "search",
            "google-shopping-ads": "cart",
            "facebook-ads": "users",
            "instagram-ads": "camera",
            "seo": "chart",
            "google-my-business": "map",
            "marketing-analytics": "gauge",
            "website": "globe",
            "website-design": "palette",
        }[slug]
        cards += f"""
          <article class="plan-card {s['theme']}" data-reveal>
            <span class="plan-icon">{ICONS[icon_key]}</span>
            <h3>{label}</h3>
            <p>{tag} · three plans</p>
            <p class="plan-price">{start}<small>/mo</small></p>
            <a class="plan-link" href="{slug}.html#pricing">View plans {ICONS['arrow']}</a>
          </article>"""
    content = f"""
  <main id="main">
    {simple_hero("Pricing", "Simple plans for every service.", "One price per service, billed monthly, with the work and the reporting included. No setup fees, no percentage of your ad spend, no&nbsp;lock&#8209;in.", center=True)}
    <section class="content-section">
      <div class="container">
        <div class="plan-grid">{cards}
        </div>
        <div class="plan-includes" data-reveal>
          <p class="plan-includes-title">Included in every plan</p>
          <ul>
            <li><strong>A named specialist</strong><span>One person who knows your account and answers the same day.</span></li>
            <li><strong>Monthly reporting</strong><span>A short written report: what changed, what we did next.</span></li>
            <li><strong>No lock-in</strong><span>Monthly billing. Pause or cancel with 30 days' notice.</span></li>
            <li><strong>We never take a cut</strong><span>No percentage of ad spend, no setup fee, no surprises.</span></li>
          </ul>
        </div>
        <p class="pricing-note">All plans exclude advertising spend. Enterprise pricing is quoted per scope — <a href="help.html">talk to us</a>.</p>
      </div>
    </section>
    {cta_block("Not sure which plan fits?", "Tell us your goals and budget. We will recommend the smallest plan that can get you there — and say so if you need less.", "help.html", "Ask an expert")}
  </main>
"""
    return head("Pricing — " + BRAND, "Plans and pricing for websites, SEO, advertising, local listings and analytics.", "page theme-indigo") + header() + content + footer()


# --------------------------------------------------------------------------
# Write
# --------------------------------------------------------------------------
def write(name, content):
    (ROOT / name).write_text(content, encoding="utf-8")
    print("wrote", name)


def main():
    for s in SERVICES:
        write(f"{s['slug']}.html", service_page(s))

    write("about.html", about_page(COMPANY["about"]))
    write("careers.html", careers_page(COMPANY["careers"]))
    write("press.html", press_page(COMPANY["press"]))
    write("help.html", help_page(COMPANY["help"]))

    write("terms.html", legal_page("terms", LEGAL["terms"]))
    write("privacy.html", legal_page("privacy", LEGAL["privacy"]))
    write("sitemap.html", sitemap_page())
    write("pricing.html", pricing_page())


if __name__ == "__main__":
    main()
