# FastAPI + PostgreSQL CRUD API

## Overview
This is a simple CRUD REST API built using FastAPI, SQLAlchemy, and PostgreSQL.  
It demonstrates backend development with database integration and REST API design.

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn


## Features
- Create product
- Read all products
- Read product by ID
- Update product
- Delete product
- PostgreSQL database integration
- SQLAlchemy ORM

### How to Run

## 1. Clone repository
```bash
git clone https://github.com/RamaKallam/fastapi-postgresql-api.git
cd fastapi-postgresql-api

## 2. Create virtual environment
python -m venv myenv
source myenv/bin/activate   # Mac/Linux

## 3. Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

## 4.Setup PostgreSQL database
 Create database:
CREATE DATABASE fastapi_db;

Update .env file:
DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_db

## 5. Run server
uvicorn main:app --reload

## 6. Start PostgreSQL
brew services start postgresql

## API Documentation

FastAPI automatically provides interactive API documentation (Swagger UI).

You can access it here:

-> http://127.0.0.1:8000/docs

This page allows you to:
- Test all API endpoints
- View request/response models
- Interact with the backend directly from the browser