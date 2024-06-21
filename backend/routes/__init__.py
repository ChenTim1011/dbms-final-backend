from .books import books_bp
from .reading_history import history_bp
from .reading_plan import plan_bp
from .favorites import favorites_bp
from .search import search_bp

try:
    from .notes import notes_bp
except ImportError:
    # Handle the import error here
    pass

def register_routes(app):
    app.register_blueprint(books_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(plan_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(favorites_bp)
    app.register_blueprint(search_bp)
