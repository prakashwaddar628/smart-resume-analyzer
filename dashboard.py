import streamlit as st
import plotly.graph_objects as go


def render_dashboard(match_result):
    match_score = match_result.get("match_score", 0)
    matched_skills = match_result.get("matched_skills", [])
    missing_skills = match_result.get("missing_skills", [])

    st.markdown("---")
    st.subheader("📈 Career Match Analytics Dashboard")

    # Gauge chart for match score
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### 🎯 Match Score Gauge")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=match_score,
            title={'text': "Match Score %"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#00cc96"},
                'steps': [
                    {'range': [0, 50], 'color': "#ffcccc"},
                    {'range': [50, 75], 'color': "#ffe680"},
                    {'range': [75, 100], 'color': "#ccffcc"}
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 📊 Skill Category Breakdown")
        skill_data = {
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        }

        fig2 = go.Figure([
            go.Bar(
                x=skill_data["Category"],
                y=skill_data["Count"],
                marker_color=["#28a745", "#dc3545"],
                text=skill_data["Count"],
                textposition='auto'
            )
        ])

        fig2.update_layout(
            xaxis_title="Skill Category",
            yaxis_title="Number of Skills",
            height=350
        )
        st.plotly_chart(fig2, use_container_width=True)