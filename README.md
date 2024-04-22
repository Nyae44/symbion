# Symbion

Welcome to Symbion! Symbion is a CRM (Customer Relationship Management) web application designed to help you manage your records effectively.

### Quick Start Guide

1. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate  # Unix/Mac
   env\Scripts\activate  # Windows


```bash
python3 -m venv env
```
2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Make database migrations**

```bash
python3 manage.py makemigrations
```

then

```bash
python3 manage.py migrate
```

4. **Run server**

```bash
python3 manage.py runserver
```
