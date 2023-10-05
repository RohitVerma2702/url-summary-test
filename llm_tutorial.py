from secret_key import secret_key
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

os.environ["OPENAI_API_KEY"] = secret_key

llm = OpenAI(temperature=0.6)


def generate_controls(risk):
    prompt_teamplate_name = PromptTemplate(
        input_variables=["risk"],
        template="Read the article on {risk} link and identify what type of risk is this, a 'Loss Event' or an 'Emerging Topic'. Also list out the Countries it affects and Organisations it affects from the article summary. Please also check when was the article published by looking at any time related information like '3 hours ago' or '23 August 2023'.",
    )
    # print(prompt_teamplate_name.format(risk="Mexican"))
    name_chain = LLMChain(llm=llm, prompt=prompt_teamplate_name, output_key="controls")

    # prompt_template_information = PromptTemplate(
    #     input_variables=["controls"],
    #     template="Provide me a list of 5 policies that {controls} must follow. Please provide 2 lines worth of information about them as well. Please make each point is separated by @ symbol.",
    # )

    # item_chain = LLMChain(
    #     llm=llm, prompt=prompt_template_information, output_key="policies"
    # )

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=["risk"],
        output_variables=["controls"],
    )

    response = chain({"risk": risk})

    return response


if __name__ == "__main__":
    print(generate_controls(risk="Whistleblowing"))
