# Somnath Portfolio - Local Server Runner

Write-Host ""
Write-Host "========================================"
Write-Host "  Somnath Portfolio - Local Server"
Write-Host "========================================"
Write-Host ""

# Try Python 3
try {
    Write-Host "Starting server with Python 3..."
    & python3 -m http.server 8000
    exit 0
}
catch {
    Write-Host "Python 3 not found, trying Python..."
}

# Try Python
try {
    Write-Host "Starting server with Python..."
    & python -m http.server 8000
    exit 0
}
catch {
    Write-Host "Python not found, trying Node.js..."
}

# Try Node.js http-server
try {
    Write-Host "Starting server with Node.js..."
    & npx http-server -p 8000
    exit 0
}
catch {
    Write-Host "Node.js not found"
}

# If all fail
Write-Host ""
Write-Host "ERROR: Could not start server"
Write-Host ""
Write-Host "Please install one of:"
Write-Host "1. Python 3: https://www.python.org/downloads/"
Write-Host "2. Node.js: https://nodejs.org/"
Write-Host ""
Read-Host "Press Enter to exit"
exit 1
