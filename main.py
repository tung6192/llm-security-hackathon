import asyncio
import streamlit as st
from streamlit_chat import message
from langchain_openai import ChatOpenAI

from exploiter.exploit import exploit_cve


user_prompt = "user_prompt_history"
chat_answers = "chat_answers_history"
chat_history = "chat_history"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

async def main():
    st.header("Langchain Documentation Helper Bot")

    with st.form(key="Prompt", clear_on_submit=False):
        prompt = st.text_input("Enter your prompt here")
        submitted = st.form_submit_button("Submit")

    if submitted:
        cve_name = llm.invoke(f"Extract cve_name from following request: {prompt}.\
                                Example output: 'CVE-211-1234'").content

        st.write(f"Extracted CVE name: {cve_name}")
        message(f"Extracted CVE name: {cve_name}")

        def write_message(key, text, is_user=False, idx=None):
            message(f"{key}: {text}", is_user=is_user,key=idx)

        if prompt:
            with st.spinner("Generating response"):
                router_agent_executor, input_dict = exploit_cve(cve_name)
                print(input_dict)
                idx = 0
                async for chunk in router_agent_executor.astream(input_dict):
                    try:
                        idx += 1
                        # Agent Action
                        if "actions" in chunk:
                            for action in chunk["actions"]:
                                write_message("Calling Tool", f"`{action.tool}` with input `{action.tool_input}`", idx=idx)
                        # Observation
                        elif "steps" in chunk:
                            for step in chunk["steps"]:
                                write_message("Tool Result", f"`{step.observation}`", is_user=True, idx=idx)
                        # Final result
                        elif "output" in chunk:
                            write_message('Final Output', f'{chunk["output"]}', is_user=True, idx=idx)
                        else:
                            raise ValueError()
                    except Exception as e:
                        pass

if __name__ == "__main__":
    asyncio.run(main())