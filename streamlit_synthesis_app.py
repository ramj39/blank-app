import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import json
import os
st.set_page_config(page_title="Organic Reaction Chatbot")

# Title and instructions
st.title("🧪 Organic Synthesis Reaction Chatbot")
st.markdown("Enter a named *organic reaction* to see information or add a new one below.")

# Initialize reaction database in session_state
if "reaction_guide" not in st.session_state:
    st.session_state.reaction_guide = {
        "aldol condensation": "Forms β-hydroxy carbonyls under basic or acidic conditions.",
        "wittig reaction": "Forms alkenes by reacting aldehydes or ketones with phosphonium ylides.",
        "fischer esterification": "Produces esters by refluxing carboxylic acids with alcohols in acid.",
        "friedel-crafts acylation": "Aromatic substitution using acid chlorides and a Lewis acid like AlCl₃.",
        "grignard reaction": "Grignard reagents add to carbonyls to form alcohols; key for C–C bond formation.",
        "claisen condensation": "Combines two esters or an ester and ketone to form a β-keto ester or ketone.",
        "diels-alder reaction": "A [4+2] cycloaddition forming a six-membered ring from a diene and dienophile.",
        "hell-volhard-zelinsky reaction": "α-Halogenation of carboxylic acids using halogens and PBr₃ or PCl₃."
    }

# Search/query section
st.subheader("🔍 Query a Reaction")
query = st.text_input("Enter reaction name to look up:", key="query_input")

if query:
    # Normalize the key
    qkey = query.strip().lower()
    description = st.session_state.reaction_guide.get(qkey)
    if description:
        st.success(f"{query.title()}: {description}")
    else:
        st.warning(f"No information found for '{query}'. You can add it below!")

# Divider
st.markdown("---")

# Add a new reaction
st.subheader("➕ Add a New Reaction")

# Input fields (with unique keys to avoid duplication error)
new_name = st.text_input("Reaction name:", key="new_reaction_name")
new_info = st.text_area("Reaction description or detail:", key="new_reaction_info")

if st.button("Add Reaction", key="add_reaction_btn"):
    rkey = new_name.strip().lower()
    rinfo = new_info.strip()
    if not new_name or not new_info:
        st.error("Please provide both a reaction name and a description.")
    elif rkey in st.session_state.reaction_guide:
        st.warning(f"The reaction '{new_name}' already exists.")
    else:
        st.session_state.reaction_guide[rkey] = rinfo
        st.success(f"✅ '{new_name.title()}' was added to the chatbot!")

# Optional: Display current stored reactions
with st.expander("📘 Show All Stored Reactions"):
    for name, desc in st.session_state.reaction_guide.items():
        st.markdown(f"• *{name.title()}*: {desc}")
