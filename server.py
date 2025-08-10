from flask import Flask, request, send_file, abort
from playwright.sync_api import sync_playwright
import tempfile
import os

app = Flask(__name__)

@app.route("/pdf", methods=["GET"])
def generate_pdf():
    itinerary_id = request.args.get("id")
    if not itinerary_id:
        abort(400, "Missing id parameter")

    url = f"https://letstrip.world/dashboard/pdf-preview?id={itinerary_id}"

    # Temp file for PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        pdf_path = tmp_pdf.name

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")  # waits for network requests to finish
        page.wait_for_selector("body")

        # Generate PDF in A4 format, auto-paginated
        page.pdf(
            path=pdf_path,
            format="A4",               # standard size
            print_background=True
        )

        browser.close()

    return send_file(pdf_path, as_attachment=True, download_name="itinerary.pdf")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
