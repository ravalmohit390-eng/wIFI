from app import app

# Vercel needs 'app', not socketio.run()
# Note: WebSockets will NOT work on Vercel unless using an external adapter.
# This deployment will likely fall back to HTTP polling.
app.debug = True
