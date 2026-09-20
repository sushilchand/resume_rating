from groq import Groq
from pypdf import PdfReader

from resume_rating.constants import GROQ_API_KEY, LLM_MODEL_NAME
from resume_rating.jd_parser import JobDescription
from resume_rating.resume_parser import ResumeParser
from resume_rating.schema import MatchResultSchema

def main():
    client = Groq(api_key=GROQ_API_KEY)
    response_format = {
        "type": "json_object"
    }
    sys_prompt = f"Extract information strictly based on this json schema {MatchResultSchema.model_json_schema()}"
    sys_message = {
        "role": "system",
        "content": sys_prompt
    }

    parsed_resume_data = ResumeParser.parse_resume(client=client)
    parser_jd = JobDescription.parser_jd(client=client)

    sys_prompt = f"You are an expert HR hiring and return data strictly in this json format {MatchResultSchema.model_json_schema()}"
    sys_message = {
        "role": "system",
        "content": sys_prompt
    }
    prompt = f"Consider this resume {parsed_resume_data.model_dump(mode="json")} and Job description {parser_jd.model_dump(mode="json")} and give a score"
    message = {
        "role": "user",
        "content": prompt
    }
    messages = [sys_message, message]

    response = client.chat.completions.create(
        model=LLM_MODEL_NAME,
        messages=messages,
        response_format=response_format,
        temperature=0
    )
    print(f"Total tokens used are {response.usage.prompt_tokens} and {response.usage.completion_tokens}")
    print(response.choices[0].message.content)
    

if __name__ == "__main__":
    main()