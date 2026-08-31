from __future__ import annotations

import os
import streamlit as st

from services.db import init_db, sellers


def bootstrap():
    init_db()
    try:
        master = str(st.secrets.get("MARKETPLACE_HUB_MASTER_KEY", ""))
        if master:
            os.environ["MARKETPLACE_HUB_MASTER_KEY"] = master
    except Exception:
        pass


def seller_selector(label="Seller attivo") -> int | None:
    data = sellers()
    if not data:
        st.warning("Registra prima almeno un Seller.")
        return None
    labels = {f"{x['name']}  ·  ID {x['id']}": x["id"] for x in data}
    chosen = st.selectbox(label, list(labels), key="global_seller_selector")
    st.session_state["active_seller_id"] = labels[chosen]
    return labels[chosen]
