# Test Create User
Write-Host "`n=== Testing POST /users ===" -ForegroundColor Green
$userBody = @{
    name = "John Doe"
    email = "john@example.com"
    phone = "1234567890"
    address = "123 Main St"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/users" -Method Post -Body $userBody -ContentType "application/json"

# Test Get User
Write-Host "`n=== Testing GET /users/john@example.com ===" -ForegroundColor Green
Invoke-RestMethod -Uri "http://localhost:8000/users/john@example.com" -Method Get

# Test Create Product
Write-Host "`n=== Testing POST /products ===" -ForegroundColor Green
$productBody = @{
    sku = "PROD-001"
    name = "Laptop"
    price = 999.99
    stock = 50
    description = "High-performance laptop"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/products" -Method Post -Body $productBody -ContentType "application/json"

# Test Get Product
Write-Host "`n=== Testing GET /products/PROD-001 ===" -ForegroundColor Green
Invoke-RestMethod -Uri "http://localhost:8000/products/PROD-001" -Method Get

Write-Host "`n=== All Tests Complete! ===" -ForegroundColor Green
