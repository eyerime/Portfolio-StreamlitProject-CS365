from datetime import datetime

import pandas as pd
import streamlit as st

NAME = "Renz Gabriel B. Etcuban"
SECTION = "CSIT 349 · F1"
GITHUB = "https://github.com/eyerime"
ITCH = "https://lenicon.itch.io/kampilan"
ACCENT = "#a8472a"

st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="🎸", layout="wide")

st.markdown(
    """
    <style>
    .block-container {padding-top: 2.2rem; max-width: 1100px;}
    h1, h2, h3 {letter-spacing: -0.01em;}
    .chip {display:inline-block; padding:1px 9px; margin:0 5px 4px 0;
           border:1px solid #c9b99f; border-radius:4px; font-size:.82rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.session_state.setdefault("inbox", [])
st.session_state.setdefault("likes", 0)

SKILLS = pd.DataFrame(
    [
        ("C++", "Programming", 70),
        ("Python", "Programming", 65),
        ("PHP / MySQL", "Programming", 60),
        ("Godot", "Programming", 35),
        ("Music composition", "Music", 80),
        ("Guitar", "Music", 75),
        ("Music theory", "Music", 70),
        ("Cybersecurity", "Security", 45),
        ("Drawing", "Art", 60),
    ],
    columns=["Skill", "Area", "Level"],
)

PROJECTS = [
    {
        "title": "Bionic Reader",
        "kind": "Software",
        "role": "Solo developer",
        "tools": ["C++"],
        "about": "A lightweight reader for books, PDFs and EPUBs that applies bionic "
                 "formatting (bolded word starts) to make text easier to skim.",
        "outcome": "Took roughly 12 to 16 hours because I refused to vibe code it. "
                   "It taught me how much a small, fast program is worth.",
        "link": None,
    },
    {
        "title": "Kampilan",
        "kind": "Game",
        "role": "Composer (soundtrack)",
        "tools": ["Godot", "Aseprite", "Music production"],
        "about": "A 2D pixel-art boss rush where you play Lapu-lapu's son fighting "
                 "Cebuano mythical creatures. Made for Sugbuanon Saga: Game Jam 2025.",
        "outcome": "Released a playable demo with three bosses. I wrote the music for it.",
        "link": ITCH,
    },
    {
        "title": "WildFinds",
        "kind": "Software",
        "role": "Student developer",
        "tools": ["PHP", "MySQL", "JavaScript", "HTML/CSS"],
        "about": "A campus lost and found web app for CIT-U. Faculty log surrendered "
                 "items, students browse them, and claims need proof of ownership.",
        "outcome": "Built for Information Management with a normalized schema, "
                   "hashed passwords and database transactions.",
        "link": "https://github.com/eyerime/WildFinds",
    },
]

MILESTONES = {
    "Music": (
        "Music",
        "Music is what made me who I am. It pulled me out of my lowest points "
        "and kept me going during the highs.",
    ),
    "DAA": (
        "Passing Design and Analysis of Algorithms",
        "DAA was a huge hurdle. I'm not great at proofs, so passing it felt a "
        "little miraculous.",
    ),
    "Game jam": (
        "My first game jam",
        "I was excited to build with a team. I ended up spending nearly all my "
        "time composing the soundtrack and never really touched the codebase. "
        "Still one of my favorite weeks.",
    ),
}

# ---------------- sidebar ----------------
with st.sidebar:
    st.image("photo.png", use_container_width=True)
    st.subheader(NAME)
    st.caption(f"BS Computer Science · 3rd year\nCIT-U · {SECTION}")
    st.divider()
    show_chips = st.checkbox("Show tool tags on projects", value=True)
    compact = st.radio("Project layout", ["Cards", "List"], horizontal=True)
    st.divider()
    st.link_button("GitHub", GITHUB, use_container_width=True)
    st.link_button("Kampilan on itch.io", ITCH, use_container_width=True)

# ---------------- header ----------------
st.title(NAME)
st.markdown("3rd year BSCS student at CIT-U. I code, and I write and play music.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Year level", "3rd")
c2.metric("Projects shown", len(PROJECTS))
c3.metric("Game jams", 1)
c4.metric("Appreciation", st.session_state.likes)

tab_about, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Skills", "Projects", "Contact"]
)

# ---------------- about ----------------
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.image("photo.png", caption="Me, in my graduation sash (SHS)", use_container_width=True)
    with right:
        st.header("Autobiography")
        st.write(
            "I live in Labangon, in a rented house right behind CIT-U, which makes "
            "the walk to class short. I started computer science as a hobby, "
            "something that came naturally from being digitally literate. Over "
            "time it stopped being a hobby and became something I actually care about."
        )
        st.write(
            "After graduation I want to work for a decent company or join a startup."
        )
        st.subheader("Education")
        st.dataframe(
            pd.DataFrame(
                [
                    ("CIT-U", "BS Computer Science", "Ongoing (3rd year)"),
                    ("CIT-U", "Senior High, STEM strand", "Completed"),
                ],
                columns=["School", "Program", "Status"],
            ),
            hide_index=True,
            use_container_width=True,
        )
        st.subheader("Interests")
        st.write("Guitar · Drawing · Cybersecurity · Music theory · Working out")

    st.header("Milestones")
    pick = st.selectbox("Choose a moment", list(MILESTONES))
    title, body = MILESTONES[pick]
    with st.container(border=True):
        st.subheader(title)
        st.write(body)

    with st.expander("A bit more about the music"):
        st.write(
            "I play guitar, study music theory, and compose. The Kampilan "
            "soundtrack is the first music I've written for a finished game."
        )

# ---------------- skills ----------------
with tab_skills:
    st.header("Skills")
    st.caption("Self-rated, 0 to 100.")
    areas = st.multiselect("Areas", sorted(SKILLS["Area"].unique()),
                           default=sorted(SKILLS["Area"].unique()))
    floor = st.slider("Minimum level", 0, 100, 0)
    view = SKILLS[SKILLS["Area"].isin(areas) & (SKILLS["Level"] >= floor)]

    t, ch = st.columns(2, gap="large")
    with t:
        st.dataframe(
            view,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Level": st.column_config.ProgressColumn(
                    "Level", min_value=0, max_value=100, format="%d"
                )
            },
        )
    with ch:
        if view.empty:
            st.info("Nothing matches those filters.")
        else:
            st.bar_chart(view.set_index("Skill")["Level"], color=ACCENT, horizontal=True)

    st.subheader("Average by area")
    st.bar_chart(SKILLS.groupby("Area")["Level"].mean(), color=ACCENT)

# ---------------- projects ----------------
with tab_projects:
    st.header("Projects")
    kinds = st.multiselect("Type", ["Software", "Game"], default=["Software", "Game"])
    shown = [p for p in PROJECTS if p["kind"] in kinds]

    def render(p):
        st.subheader(p["title"])
        st.caption(f"{p['kind']} · Role: {p['role']}")
        if show_chips:
            st.markdown("".join(f'<span class="chip">{t}</span>' for t in p["tools"]),
                        unsafe_allow_html=True)
        st.write(p["about"])
        st.write(f"**Outcome:** {p['outcome']}")
        if p["link"]:
            st.link_button("Open", p["link"], key=f"open_{p['title']}")

    if compact == "Cards":
        cols = st.columns(3, gap="medium")
        for col, p in zip(cols, shown):
            with col.container(border=True):
                render(p)
    else:
        for p in shown:
            with st.container(border=True):
                render(p)

    export = pd.DataFrame(
        [{**p, "tools": ", ".join(p["tools"]), "link": p["link"] or ""} for p in PROJECTS]
    )
    st.download_button("Download project list (CSV)", export.to_csv(index=False),
                       "projects.csv", "text/csv")

# ---------------- contact ----------------
with tab_contact:
    st.header("Contact and feedback")
    col_f, col_s = st.columns([2, 1], gap="large")
    with col_f:
        with st.form("contact", clear_on_submit=True):
            a, b = st.columns(2)
            who = a.text_input("Your name")
            email = b.text_input("Your email")
            topic = st.selectbox("About", ["Feedback", "Collaboration", "Question", "Other"])
            rating = st.radio("How was the site?", ["Poor", "Okay", "Good", "Great"],
                              index=2, horizontal=True)
            msg = st.text_area("Message", height=120)
            ok = st.checkbox("You may reply to me")
            sent = st.form_submit_button("Send")
        if sent:
            if not who.strip() or not msg.strip():
                st.error("Please add your name and a message.")
            else:
                st.session_state.inbox.append(
                    {"Time": datetime.now().strftime("%H:%M"), "From": who,
                     "About": topic, "Rating": rating, "Message": msg}
                )
                st.success(f"Thanks, {who}. Your message was received.")
                st.toast("Message sent")
    with col_s:
        st.write("Or find me here:")
        st.link_button("GitHub", GITHUB, use_container_width=True)
        st.link_button("itch.io", ITCH, use_container_width=True)
        if st.button("Appreciate this site"):
            st.session_state.likes += 1
            st.toast("Appreciated, thanks!")
        st.caption(f"Appreciations this session: {st.session_state.likes}")

    if st.session_state.inbox:
        with st.expander(f"Messages sent this session ({len(st.session_state.inbox)})"):
            st.dataframe(pd.DataFrame(st.session_state.inbox), hide_index=True)

st.divider()
st.caption(f"{NAME} · {SECTION} · Built with Streamlit")
