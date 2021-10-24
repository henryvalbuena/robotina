import sqlite3

from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")

DB = "tokens.db"


def add(token, limit):
    try:
        conn = sqlite3.connect(DB)
        logger.info(f"adding {token} to db")

        conn.execute(
            f"INSERT INTO TOKENS (TOKEN,LIMITS) \
            VALUES ({token}, {limit})"
        )
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        logger.error(err)
        return False


def remove(token):
    try:
        conn = sqlite3.connect(DB)
        logger.info(f"removing {token} to db")

        conn.execute(f"DELETE from TOKENS where TOKEN={token}")
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        logger.error(err)
        return False


def update(token, limit):
    try:
        conn = sqlite3.connect(DB)
        logger.info(f"updating {token} to db")

        conn.execute(f"UPDATE TOKENS set LIMITS={limit} where TOKEN={token}")
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        logger.error(err)
        return False


def tokens():
    try:
        conn = sqlite3.connect(DB)
        logger.info("list of tokens in db")

        cursor = conn.execute("SELECT * FROM TOKENS")
        conn.close()

        tokens = [{"token": token, "limit": limit} for token, limit in cursor]

        return tokens
    except Exception as err:
        logger.error(err)
        return False
