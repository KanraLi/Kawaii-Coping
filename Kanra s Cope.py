import webview

# URL of your web game
url = "https://fataltotheflesh.com"

# Create window
webview.create_window(
    "Kanra's Cope",    # Window title
    url,
    width=1000,
    height=600,
    resizable=True,
    fullscreen=False
)

# Start the app
webview.start()
