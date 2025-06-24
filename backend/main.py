from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai_story_generator import generate_user_stories
from code_generator import generate_code
from bug_resolver import fix_buggy_code
# import other routers similarly

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to SmartSDLC API"}

@app.post("/ai/generate-user-stories")
def user_stories_endpoint(pdf_text: str):
    stories = generate_user_stories(pdf_text)
    return {"user_stories": stories}

@app.post("/ai/generate-code")
def code_generation_endpoint(task_description: str):
    code = generate_code(task_description)
    return {"code": code}

@app.post("/ai/fix-bug")
def bug_fix_endpoint(code_snippet: str):
    fixed_code = fix_buggy_code(code_snippet)
    return {"fixed_code": fixed_code}

# Add other endpoints similarly
