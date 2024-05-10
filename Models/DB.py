from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


class DB:
    """Initialize PostgreSQL database"""
    host = "localhost"
    user = "user"
    password = "5001"
    db = "library"
    table = ""

    def __init__(self, app):
        # Create the PostgreSQL connection URI
        uri = f"postgresql://{self.user}:{self.password}@{self.host}/{self.db}"

        # Set up Flask-SQLAlchemy configuration
        app.config["SQLALCHEMY_DATABASE_URI"] = uri
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Initialize SQLAlchemy
        self.db = SQLAlchemy(app)

    def cur(self):
        """Start a new session (similar to a cursor)"""
        return self.db.session

    def query(self, q):
        """Execute a raw SQL query with the SQLAlchemy session"""
        session = self.cur()

        if len(self.table) > 0:
            q = q.replace("@table", self.table)

        # Run the query using the SQLAlchemy session
        result = session.execute(text(q))

        return result

    def commit(self):
        """Commit the current transaction"""
        self.cur().commit()
