from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SessionLocal

import databases


if __name__ == '__main__':
    databases.init_schema()