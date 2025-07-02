import streamlit as st
import plotly.graph_objects as go

def render_dashboard(match_result):
    match_score = match_result.get("match_score", [])
    matched_skills = match_result.get("matched_skills", [])
    missing_skills = match_result.get("missing_skills", [])

    st.subheader("Career Match Analytics Dashboard")

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = match_score,
        title = {'text': "Match Score %"},
        gauge = {'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 50], 'color': "#ffcccc"},
                    {'range': [50, 75], 'color': "#ffe680"},
                    {'range': [75, 100], 'color': "#ccffcc"}
                ]}
    ))

    st.plotly_chart(fig, use_container_width=True)

    skill_data = {
        "Category" : ["Matched Skills", "Missing Skills"],
        "Count" : [len(matched_skills), len(missing_skills)]
    }

    fig2 = go.Figure([
        go.Bar(x=skill_data["Category"], y=skill_data["Count"], marker_color=["green","red"])
    ])

    fig2.update_layout(title="Skill Coverage", xaxis_title="Skill Category", yaxis_title="Count")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("Matched Skills")
    st.write(matched_skills)

    st.markdown("Missing Skills")
    st.write(missing_skills)