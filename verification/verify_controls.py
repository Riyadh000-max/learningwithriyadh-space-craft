from playwright.sync_api import sync_playwright

def verify_mobile_controls():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        # Emulate a mobile device (iPhone 12 Pro) to trigger mobile controls
        device = p.devices['iPhone 12 Pro']
        context = browser.new_context(**device)
        page = context.new_page()

        # Navigate to the game
        page.goto("http://localhost:8080/index.html")

        # Wait for game to load (MainMenu)
        # Start game to see controls (they appear in GameLoop)
        # Click "Launch" button
        page.get_by_text("Launch").click()

        # Select "Friendly Chat"
        page.get_by_text("Friendly Chat").click()

        # Click "ENGAGE"
        page.get_by_text("ENGAGE").click()

        # Now in GameLoop, controls should be visible
        # Wait for Fire button
        page.wait_for_selector("text=FIRE")

        # Take screenshot
        page.screenshot(path="verification/mobile_controls.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile_controls()
