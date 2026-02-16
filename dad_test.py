import streamlit as st
import random
import time

# ────────────────────────────────────────────────
#  De mest pinlige danske far-jokes vi kunne finde på kort tid
# ────────────────────────────────────────────────
jokes = [
    "Hvorfor kan man ikke stole på trapper? De er altid oppe i noget!",
    "Hvad siger en osteelsker når han bliver overrasket? Hallååå Gouda!",
    "Hvorfor blev tomaten rød? Fordi den så salatdressingen!",
    "Hvad kalder man en sovende tyr? En bulldozer!",
    "Hvorfor blev matematikbogen så ked af det? Den havde alt for mange problemer.",
    "Hvad siger den ene væg til den anden væg? Vi mødes i hjørnet!",
    "Hvorfor kan man ikke spille skjul med bjerge? De pikker dig altid ud!",
    "Hvad er en komikers yndlingsbogstav? … B!",
    "Hvorfor tog skelettet ikke med til festen? Han havde ikke noget på hjerte.",
    "Hvad siger en mus når den rammer en mur? Au, det var en hård en!",
    "Hvorfor bliver meteorologer aldrig rige? De taber altid på vejret.",
    "Hvad kalder man en dinosaur med bind for øjnene? Do-you-think-he-saurus!",
    "Hvorfor var kosten så glad? Den havde lige fejet gulvet med alle!",
    "Hvad siger en computer når den er forelsket? Du har fanget min harddisk!",
    "Hvorfor gik cyklen i skole? Den ville lære at stå på egne hjul!",
    "Hvorfor hader spøgelser elevatorer? De er bange for at blive fanget i ånden!",
    "Hvad kalder man en lam med to hjerner? En får-smart!",
    "Hvorfor tog bananen solcreme på? Den ville ikke blive skrællet!",
    "Hvorfor blev 6 bange for 7? Fordi 7 8 9!",
    "Hvad kalder man en fisk uden øjne? Fsk!",
]

st.set_page_config(page_title="Meget Seriøs AI", page_icon="🤖")

st.title("Meget Seriøs AI-assistent 2026")
st.caption("Kunstig intelligens • Høj faglighed • Diskretion garanteret")
st.markdown("---")

# Simpel besked-historik
if "messages" not in st.session_state:
    st.session_state.messages = []

# Vis tidligere beskeder
for role, text in st.session_state.messages:
    if role == "user":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(text)

# Input
prompt = st.chat_input("Skriv hvad du vil have hjælp til...")

if prompt:
    # Gem og vis brugerens besked
    st.session_state.messages.append(("user", prompt))
    st.chat_message("user").markdown(prompt)

    # Byg svar
    with st.chat_message("assistant"):
        prefix = random.choice([
            "Tak for din henvendelse. Jeg har analyseret dit spørgsmål nøje og kan nu svare:",
            "Som din betroede AI vil jeg nu give dig et kvalificeret svar:",
            "Med stor faglig tyngde kan jeg meddele følgende:",
            "Professionel respons aktiveret. Her kommer svaret:",
        ])

        joke = random.choice(jokes)

        # Skrive-effekt (simpel version)
        text = f"{prefix}\n\n**{joke}** 😂🥁"
        placeholder = st.empty()
        displayed = ""

        for char in text:
            displayed += char
            placeholder.markdown(displayed)
            time.sleep(0.012)

        st.session_state.messages.append(("assistant", text))

# Lille nulstil-knap i bunden
st.markdown("---")
if st.button("🗑️ Start forfra (jeg orker ikke mere)"):
    st.session_state.messages = []
    st.rerun()
