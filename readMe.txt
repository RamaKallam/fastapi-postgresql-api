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

## How to Run

### 1. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary

## Start PostgreSQL
brew services start postgresql

## Run Server
uvicorn main:app --reload

## API Documentation

FastAPI automatically provides interactive API documentation (Swagger UI).

You can access it here:

👉 http://127.0.0.1:8000/docs

This page allows you to:
- Test all API endpoints
- View request/response models
- Interact with the backend directly from the browser