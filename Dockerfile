# 1. Base image (Python install karo)
FROM python:3.12-slim

# 2. Dabbe ke andar ek folder banao
WORKDIR /app

# 3. Samaan ki list (requirements) copy karo
COPY requirements.txt .

# 4. Saare tools install karo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Apna saara code aur model dabbe mein dalo
COPY . .

# 6. Dabba khulte hi Waiter (API) ko chala do
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]