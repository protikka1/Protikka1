Mobile Stock Data Parser
Overview
This is a simple, self-contained HTML and JavaScript tool designed to help users quickly extract structured financial transaction data from raw, unstructured text, particularly useful for data sourced from mobile devices or plain text reports. It's built to run directly in any standard web browser (including those on Android phones) without requiring server-side processing or complex installations.
The tool is specifically designed to parse two common patterns of stock transaction data that you might encounter:
 * Company Name First (3-line block): For transactions where share quantity and price are not explicitly listed within the block.
   * Example:
     AT&T Limit Sell
Brokerage Apt 11
$230

 * Shares First (4-line block): For transactions that include share details, with the company name appearing at the end of the block.
   * Example:
     90 Share @ 6.56
$790
Brokerage ,Apt 11
8x8 inc Limit Buy

Features
 * Mobile-Friendly: Runs entirely in a web browser on Android (and other) mobile phones.
 * Offline Capability: Once saved, it can be used without an internet connection.
 * Two-Pattern Recognition: Automatically identifies and parses two distinct transaction data patterns.
 * CSV Output: Processes raw text into a clean, comma-separated values (CSV) format.
 * Clipboard Integration: Easily copy the processed CSV data to your device's clipboard for pasting into spreadsheet applications.
 * User-Friendly Interface: Simple text input area, process button, and output display.
How to Use
 * Obtain the Code:
   * Copy the entire HTML code provided in the mobile_stock_parser_html_v2_reprovide immersive.
 * Save the File:
   * Open a plain text editor on your Android phone (e.g., Acode, QuickEdit, or even Google Keep if you save as plain text).
   * Paste the copied HTML code into a new document.
   * Save the file with an .html extension (e.g., stock_parser.html). Ensure it's saved in a location you can easily access (like your "Documents" folder).
 * Open the Tool:
   * Navigate to the saved stock_parser.html file using your phone's file manager.
   * Tap on the file. It should open automatically in your phone's default web browser (e.g., Chrome).
   * Alternatively, if using Acode: Open the file within Acode and use its built-in "Preview" feature.
 * Paste Your Data:
   * In the web page that opens, locate the large text area labeled "Your Raw Data".
   * Paste all your raw stock transaction data (e.g., your 1900 rows) into this text area.
 * Process Data:
   * Tap the "Process Data" button.
   * The tool will parse the data and display the results in CSV format in the "Processed Data" box below.
 * Copy and Use:
   * Tap the "Copy to Clipboard" button to copy the CSV output.
   * Open your preferred spreadsheet application (e.g., Google Sheets, Excel Mobile).
   * Paste the copied data into a cell, and the spreadsheet app should automatically organize it into columns.
Requirements
 * An Android phone (or any device with a modern web browser).
 * A basic text editor app on your phone to save the .html file.
 * A web browser (pre-installed on all Android phones).
Sharing with Others
Since this is a single .html file, you can share it like any other document:
 * Email: Attach stock_parser.html to an email.
 * Messaging Apps: Send the file via apps like WhatsApp, Telegram, etc.
 * Cloud Storage: Upload to Google Drive, Dropbox, or similar, and share the link.
Recipients simply need to download the file and open it in their web browser.
