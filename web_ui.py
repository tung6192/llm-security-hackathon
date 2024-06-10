import json
import random
import time

import streamlit as st


def main(targets):
    st.sidebar.title("SG Bits Please")
    st.sidebar.image("input_data/team_logo.png")
    st.sidebar.subheader("Saigon-Style Pushing Bits towards Better Security")
    page = st.sidebar.radio("Menu", options=["Service exploit", "CVE exploit"])
    # Create a mapping from target names to list of CVEs
    target_to_cve = {target["name"]: target["cves"] for target in targets}

    if page == "Service exploit":
        st.title("Service exploit")
        target = st.selectbox("Target", options=list(target_to_cve.keys()))

        default_url = target_to_cve[target][0]["address"]
        url_address = st.text_input("Enter the URL Address", default_url)

        # Run the selected target when a button is clicked
        clicked = st.button("⚡ Attack")

        if clicked:
            for selected_cve in target_to_cve[target]:
                st.success(f"Scanning started for: {target}, {selected_cve['id']}")
                all_logs = ""  # This string will hold combined log lines
                placeholder = st.empty()

                for line in selected_cve["logs"]:
                    all_logs += (
                        "\n" + line
                    )  # Append current line to combined logs string
                    placeholder.text(all_logs)  # Display it
                    sleep_duration = random.choice([1, 2, 3])
                    time.sleep(sleep_duration)  # Delay of 1 second

    elif page == "CVE exploit":
        st.title("CVE exploit")
        st.write("Welcome to the SG Bits Please Home Page!")

        # Get target selection
        target = st.selectbox("Target", options=list(target_to_cve.keys()))

        # Get CVE based on selected target
        cve = st.selectbox("CVE", options=[cve["id"] for cve in target_to_cve[target]])

        # Display details of selected CVE
        selected_cve = next(
            (info for info in target_to_cve[target] if info["id"] == cve), None
        )
        string_data = f"""
            - **Target URL**: {selected_cve['address']}
            - **Description**: {selected_cve['description']}
            - **Level**: {selected_cve['level']}
        """
        st.markdown(string_data)

        # Run the selected tool when a button is clicked
        clicked = st.button("⚡ Attack")

        if clicked:
            st.success(f"Scanning started for: {target}, {selected_cve['address']}")
            all_logs = ""  # This string will hold combined log lines
            placeholder = st.empty()

            for line in selected_cve["logs"]:
                all_logs += "\n" + line  # Append current line to combined logs string
                placeholder.text(all_logs)  # Display it
                sleep_duration = random.choice([1, 2, 3])
                time.sleep(sleep_duration)  # Delay of 1 second


if __name__ == "__main__":
    with open("input_data/hack-phase-cve-targets.json", "r") as f:
        data = json.load(f)

    targets = data["targets"]

    main(targets)
