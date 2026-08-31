from __future__ import annotations

import hmac
import os

import streamlit as st


def _truthy(value: str | None, default: bool = False) -> bool:
    if value is None:
        return bool(default)
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def require_auth() -> None:
    """Protect the online app with an environment-backed admin login.

    Local/Windows installs remain unchanged unless MARKETPLACE_HUB_REQUIRE_AUTH
    is explicitly enabled. Render sets this flag to true in render.yaml.
    """
    if not _truthy(os.getenv("MARKETPLACE_HUB_REQUIRE_AUTH"), default=False):
        return

    expected_user = str(os.getenv("MARKETPLACE_HUB_ADMIN_USERNAME") or "").strip()
    expected_password = str(os.getenv("MARKETPLACE_HUB_ADMIN_PASSWORD") or "")

    if not expected_user or not expected_password:
        st.error(
            "Accesso online non configurato. Imposta MARKETPLACE_HUB_ADMIN_USERNAME "
            "e MARKETPLACE_HUB_ADMIN_PASSWORD nelle variabili d'ambiente del servizio."
        )
        st.stop()

    if st.session_state.get("_marketplace_hub_authenticated") is True:
        with st.sidebar:
            st.caption(f"Accesso: {expected_user}")
            if st.button("Esci", key="marketplace_hub_logout"):
                st.session_state.pop("_marketplace_hub_authenticated", None)
                st.rerun()
        return

    st.title("Marketplace Hub")
    st.subheader("Accesso riservato")
    with st.form("marketplace_hub_login", clear_on_submit=False):
        username = st.text_input("Utente")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Accedi", type="primary")

    if submitted:
        valid_user = hmac.compare_digest(str(username), expected_user)
        valid_password = hmac.compare_digest(str(password), expected_password)
        if valid_user and valid_password:
            st.session_state["_marketplace_hub_authenticated"] = True
            st.rerun()
        st.error("Credenziali non valide.")
    st.stop()
