import json

from groq import Groq
from pypdf import PdfReader

from resume_rating.constants import GROQ_API_KEY, LLM_MODEL_NAME
from resume_rating.schema import ResumeSchema


class ResumeParser:
    @staticmethod
    def parse_resume(client: Groq) -> ResumeSchema:
        reader = PdfReader("static/Sushil_Resume.pdf")
        number_of_pages = len(reader.pages)
        data: str = ""
        for page_num in range(number_of_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            data += text

        response_format = {"type": "json_object"}

        sys_prompt = f"Extract the information strictly in this json schema {ResumeSchema.model_json_schema()}"
        sys_message = {"role": "system", "content": sys_prompt}

        job_requirement = f"Consider the {data} and return the data"
        message = {"role": "user", "content": job_requirement}
        messages = [sys_message, message]

        client = Groq(api_key=GROQ_API_KEY)

        response = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=messages,
            response_format=response_format,
            temperature=0,
        )
        print(f"Total tokens used : {response.usage.completion_tokens}")
        response_data = ResumeSchema.model_validate(
            json.loads(response.choices[0].message.content)
        )
        # print(response_data)
        return response_data
