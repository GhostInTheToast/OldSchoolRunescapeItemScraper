from playwright.sync_api import sync_playwright

def scrape(url: str) -> None:
    # Start Playwright
    with sync_playwright() as p:
        # Launch a headless browser (you can set headless=False to see the browser)
        browser = p.chromium.launch(headless=True)

        # Open a new page tab/page
        page = browser.new_page()
        
        page.goto(url)

        # Wait for JavaScript to load content (wait for a specific element to appear)
        page.wait_for_selector("#root")  # Waiting for the 'root' div to load (change the selector as needed)

        # Extract content (in this case, the content inside the div with id="root")
        content = page.inner_text("#root")  # You can use inner_text(), text_content(), or other methods

        # Print or process the content
        print(content)

        # Optionally, save the content to a file or perform further processing
        # For example, save content to a text file:
        with open('scraped_data.txt', 'w') as f:
            f.write(content)

        # Close the browser
        browser.close()