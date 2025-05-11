from pathlib import Path
import sys

class DB:
    def create_db(self):
        try:
            self.db_path = Path("./db/db.json")
            if not self.db_path.exists():
                self.db_path.write_text("[]")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)