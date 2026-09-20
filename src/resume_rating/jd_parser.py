import json

from groq import Groq

from resume_rating.constants import GROQ_API_KEY, LLM_MODEL_NAME
from resume_rating.schema import JobDescriptionSchema


class JobDescription:
    @staticmethod
    def parser_jd(client: Groq) -> JobDescriptionSchema:
        with open("static/job_description.txt", "r") as fp:
            jd = fp.read()

        response_format = {"type": "json_object"}
        sys_prompt = f"Your are an expert HR and extract the information strictly in this json schema {JobDescriptionSchema.model_json_schema()}"
        sys_message = {"role": "system", "content": sys_prompt}

        job_requirement = f"Consider the {jd} and return the data"
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
        response_data = JobDescriptionSchema.model_validate(
            json.loads(response.choices[0].message.content)
        )
        # print(response_data)
        return response_data
