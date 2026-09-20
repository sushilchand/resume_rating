# Resume Rating

Resume Rating compares a candidate's resume with a job description using a Groq-hosted language model. It extracts structured data from both documents, validates the extracted data with Pydantic, and returns a match score with an explanation.

## How It Works

1. Reads the resume PDF from `static/Sushil_Resume.pdf`.
2. Reads the job description from `static/job_description.txt`.
3. Uses Groq to extract resume and job requirements as structured JSON.
4. Asks the model to score the candidate against the job description.
5. Prints token usage and a JSON result containing:

```json
{
	"candidate_name": "Candidate name",
	"final_score": 85.0,
	"reason": "Explanation of the score"
}
```

## Requirements

- Python 3.12 or newer
- A Groq API key
- [uv](https://docs.astral.sh/uv/) for environment and dependency management

## Setup

From the repository root:

```bash
uv sync
cp src/resume_rating/.env.example .env
```

Add your credentials and model name to `.env`:

```dotenv
GROQ_API_KEY=your-groq-api-key
LLM_MODEL_NAME=your-groq-model-name
```

The application loads these values when it starts.

## Run

The default inputs are the files in `static/`. Replace them with the resume and job description you want to evaluate, then run:

```bash
python src/resume_rating/rating.py
```

The command prints the model's JSON match result to the terminal.

## Development

Run the configured formatting and validation hooks with:

```bash
uv run pre-commit run --all-files
```

The project uses:

- Groq for language-model requests
- `pypdf` for extracting text from resume PDFs
- Pydantic for validating structured model responses
- `black` and `isort` for formatting
