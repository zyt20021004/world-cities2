import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("World Cities — Home")
st.write(
    """
    Welcome to the World Cities multipage app.
    Use the button below to open the App page (I expect your `pages/app.py` to provide the main functionality).
    """
)

# Try to navigate to the app page by setting query params and rerunning.
# Streamlit's multipage navigation behavior can vary by version; this attempts a best-effort navigation.
if st.button("Open App page"):
    try:
        st.experimental_set_query_params(page="app")
        st.experimental_rerun()
    except Exception:
        st.markdown(
            "Couldn't navigate programmatically. Please open the 'App' page from the Pages sidebar or click the link below."
        )
        st.markdown("[Open App page](./?page=app)")

st.markdown("---")
st.info("If the button doesn't switch pages, open the 'App' page from the sidebar (Pages) or click: [Open App page](./?page=app)")
