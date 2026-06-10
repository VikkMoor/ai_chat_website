import gspread
from google.oauth2.service_account import Credentials

import config


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]


credentials = Credentials.from_service_account_file(
    config.GOOGLE_CREDENTIALS_PATH,
    scopes=SCOPES,
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(config.GOOGLE_SHEET_ID)

worksheet = spreadsheet.worksheet(
    config.GOOGLE_SHEET_WORKSHEET
)


def save_order(order_data: dict):
    worksheet.append_row([
        order_data.get("created_at", ""),
        order_data.get("name", ""),
        order_data.get("contact", ""),
        order_data.get("model", ""),
        order_data.get("quantity", ""),
        order_data.get("address", ""),
        order_data.get("payment", ""),
        order_data.get("telegram_id", ""),
        order_data.get("source", ""),
    ])

