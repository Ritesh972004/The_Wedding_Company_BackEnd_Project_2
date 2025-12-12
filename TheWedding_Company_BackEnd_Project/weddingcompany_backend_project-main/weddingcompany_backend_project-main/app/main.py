# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from app.config import settings
from app.utils.database import db_manager
from app.routers import organization, admin

APP_VERSION = "2.0.1"
APP_AUTHOR = "Ritesh Rodge (modified)"

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print(f"🚀 Starting {settings.APP_NAME} ({APP_VERSION})")
        # call connect (sync or async) if available
        if hasattr(db_manager, "connect"):
            res = db_manager.connect()
            if hasattr(res, "__await__"):
                await res
    except Exception as e:
        print("Warning: startup DB connect issue:", e)
    yield
    try:
        if hasattr(db_manager, "close"):
            res = db_manager.close()
            if hasattr(res, "__await__"):
                await res
        print(f"🛑 Shutting down {settings.APP_NAME}")
    except Exception as e:
        print("Warning: shutdown DB close issue:", e)


app = FastAPI(
    title=settings.APP_NAME,
    description="Organization Management Service (White Theme)",
    version=APP_VERSION,
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None
)

# CORS (keep permissive as original)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include original routers
app.include_router(organization.router)
app.include_router(admin.router)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Custom Swagger UI (clean white theme).
    This version hides the version/OAS badges and the subtitle using CSS.
    """
    return HTMLResponse(
        f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{settings.APP_NAME} — API Docs</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
  <style>
    /* Base white theme */
    :root {{
      --bg: #ffffff;
      --panel-bg: #fbfcfd;
      --muted: #6b7280;
      --accent: #2563eb;
      --card-border: rgba(0,0,0,0.06);
    }}
    html, body {{
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: #111827;
      font-family: "Inter", "Segoe UI", Roboto, Arial, sans-serif;
    }}

    /* Topbar */
    .swagger-ui .topbar {{
      background: var(--bg);
      border-bottom: 1px solid var(--card-border);
      box-shadow: none;
      padding: 12px 24px;
    }}
    .swagger-ui .topbar .download-url-wrapper {{ display: none; }}

    /* Content wrapper */
    .swagger-ui .wrapper {{
      max-width: 1200px;
      margin: 20px auto;
      padding: 10px 18px;
    }}

    /* Info */
    .swagger-ui .info {{
      background: linear-gradient(180deg, rgba(245,247,250,1), rgba(255,255,255,1));
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 18px;
      box-shadow: 0 1px 4px rgba(16,24,40,0.04);
    }}
    .swagger-ui .info .title {{
      color: var(--accent);
      font-weight: 700;
      font-size: 28px;
    }}

    /* Operation blocks */
    .swagger-ui .opblock {{
      background: var(--panel-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      margin: 14px 0;
      box-shadow: 0 1px 3px rgba(16,24,40,0.03);
    }}
    .swagger-ui .opblock.opblock-post {{ border-left: 4px solid #10b981; }}
    .swagger-ui .opblock.opblock-get  {{ border-left: 4px solid #3b82f6; }}
    .swagger-ui .opblock.opblock-put  {{ border-left: 4px solid #f59e0b; }}
    .swagger-ui .opblock.opblock-delete {{ border-left: 4px solid #ef4444; }}

    /* Buttons and inputs */
    .btn {{ background: var(--accent) !important; color: #fff !important; border-radius: 8px; }}
    .btn.execute {{ background: linear-gradient(90deg,#059669,#10b981) !important; }}
    input, textarea, select {{ border-radius: 6px; border: 1px solid var(--card-border); }}

    /* ---------- HIDE unwanted badges and subtitle ---------- */
    /* Hide the version/OAS badges on the top/right area */
    .topbar .version-stamp,
    .topbar .download-url-wrapper,
    .swagger-ui .info .base-url,
    .swagger-ui .info .version {{
        display: none !important;
    }}

    /* Hide subtitle or small description line under the title (varies by swagger version) */
    .swagger-ui .info hgroup.main > div,
    .swagger-ui .info .description {{
        display: none !important;
    }}
    /* If the subtitle is elsewhere, hide small muteds */
    .swagger-ui .info .base-url, .swagger-ui .info .version {{ display: none !important; }}

  </style>
</head>
<body>
  <div id="swagger-ui"></div>

  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.onload = function() {{
      window.ui = SwaggerUIBundle({{
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout",
        docExpansion: "none",
        persistAuthorization: true
      }});
    }};
  </script>
</body>
</html>
"""
    )


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "running",
        "version": APP_VERSION,
        "docs": "/docs",
        "health": "/health",
        "author": APP_AUTHOR
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "database": "connected"}
