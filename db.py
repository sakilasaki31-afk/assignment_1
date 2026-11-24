
import sqlite3
import streamlit as st
import pandas as pd
from pathlib import Path

# Database path
DB_PATH = Path(__file__).resolve().parent / "brickview.db"


# Database connection
def get_conn():
    return sqlite3.connect(DB_PATH)


# Create all database tables
def create_tables():
    conn = get_conn()

    try:
        # 1. Listings table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT,
                city TEXT,
                property_type TEXT,
                price REAL,
                area REAL,
                bedrooms INTEGER,
                bathrooms INTEGER,
                listing_date TEXT,
                agent TEXT
            )
        """)

        # 2. Sales table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                listing_id INTEGER,
                price REAL,
                days_on_market INTEGER,
                sale_date TEXT
            )
        """)

        # 3. Agents table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS agents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT
            )
        """)

        # Insert sample listings
        count = conn.execute(
            "SELECT COUNT(*) FROM listings"
        ).fetchone()[0]

        if count == 0:
            conn.executemany("""
                INSERT INTO listings
                (location, city, property_type, price, area,
                 bedrooms, bathrooms, listing_date, agent)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                ("Anna Nagar", "Chennai", "Apartment", 8500000, 1200, 3, 2, "2026-10-01", "Arun"),
                ("Velachery", "Chennai", "Villa", 12000000, 1800, 4, 3, "2026-10-05", "Priya"),
                ("Tambaram", "Chennai", "Apartment", 5500000, 950, 2, 2, "2026-10-10", "Kumar"),
                ("OMR", "Chennai", "Plot", 4500000, 1500, 0, 0, "2026-10-15", "Divya"),
                ("Porur", "Chennai", "Apartment", 7000000, 1100, 3, 2, "2026-10-20", "Arun")
            ])

        # Insert sample sales
        sales_count = conn.execute(
            "SELECT COUNT(*) FROM sales"
        ).fetchone()[0]

        if sales_count == 0:
            conn.executemany("""
                INSERT INTO sales
                (listing_id, price, days_on_market, sale_date)
                VALUES (?, ?, ?, ?)
            """, [
                (1, 8400000, 30, "2026-10-15"),
                (2, 11800000, 45, "2026-10-20"),
                (3, 5400000, 25, "2026-10-22")
            ])

        # Insert sample agents
        agents_count = conn.execute(
            "SELECT COUNT(*) FROM agents"
        ).fetchone()[0]

        if agents_count == 0:
            conn.executemany("""
                INSERT INTO agents
                (name, email, phone)
                VALUES (?, ?, ?)
            """, [
                ("Arun", "arun@gmail.com", "9876543210"),
                ("Priya", "priya@gmail.com", "9876543211"),
                ("Kumar", "kumar@gmail.com", "9876543212"),
                ("Divya", "divya@gmail.com", "9876543213")
            ])

        conn.commit()

    finally:
        conn.close()


# Fetch records
def run_query(sql, params=()):
    conn = get_conn()

    try:
        return pd.read_sql_query(
            sql, conn, params=params
        )
    finally:
        conn.close()


# Insert, Update and Delete
def execute(sql, params=()):
    conn = get_conn()

    try:
        conn.execute(sql, params)
        conn.commit()

    finally:
        conn.close()

    st.cache_data.clear()
