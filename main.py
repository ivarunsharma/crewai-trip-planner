import warnings
from requests.exceptions import RequestsDependencyWarning

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

import streamlit as st
from crew import TripCrew

st.set_page_config(page_title="Trip Planner", page_icon="✈️", layout="wide")

# ── Header ──────────────────────────────────────────────────────────────────
st.title("✈️ AI Trip Planner")
st.caption("Powered by CrewAI — three specialized agents plan your perfect trip.")
st.divider()

# ── Input form ───────────────────────────────────────────────────────────────
with st.form("trip_form"):
    col1, col2 = st.columns(2)
    with col1:
        origin = st.text_input("🏠 Traveling from", placeholder="e.g. New York")
        date_range = st.text_input("📅 Travel dates", placeholder="e.g. June 10–17, 2025")
    with col2:
        cities = st.text_input("🌆 Destination options", placeholder="e.g. Paris, Rome, Barcelona")
        interests = st.text_input("🎯 Interests & hobbies", placeholder="e.g. art, food, hiking")

    submitted = st.form_submit_button("Generate My Trip Plan", use_container_width=True, type="primary")

# ── Result ───────────────────────────────────────────────────────────────────
if submitted:
    if not origin or not cities or not date_range or not interests:
        st.warning("Please fill in all fields before generating a plan.")
    else:
        # Trip summary card
        st.divider()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("From", origin)
        c2.metric("Destinations", cities)
        c3.metric("Dates", date_range)
        c4.metric("Interests", interests)
        st.divider()

        with st.spinner("Your AI travel crew is working on it... this may take a minute."):
            try:
                trip_crew = TripCrew(origin, cities, date_range, interests)
                result = trip_crew.run()

                # Extract per-task outputs if available
                tasks_output = getattr(result, "tasks_output", None)

                if tasks_output and len(tasks_output) >= 3:
                    itinerary_text   = tasks_output[0].raw
                    city_select_text = tasks_output[1].raw
                    city_guide_text  = tasks_output[2].raw
                else:
                    # Fallback: show everything in one tab
                    itinerary_text   = result.raw if hasattr(result, "raw") else str(result)
                    city_select_text = None
                    city_guide_text  = None

                st.success("Your trip plan is ready!")

                # ── Tabs ─────────────────────────────────────────────────────
                if city_select_text:
                    tab1, tab2, tab3 = st.tabs([
                        "🗺️  7-Day Itinerary",
                        "🏙️  City Selection",
                        "📖  City Guide",
                    ])

                    with tab1:
                        st.markdown("### 🗓️ Your 7-Day Itinerary")
                        st.markdown(itinerary_text)

                    with tab2:
                        st.markdown("### 🏙️ Why This City?")
                        st.markdown(city_select_text)

                    with tab3:
                        st.markdown("### 📖 Local City Guide")
                        st.markdown(city_guide_text)
                else:
                    st.markdown("### 🗓️ Your Trip Plan")
                    st.markdown(itinerary_text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
