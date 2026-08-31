from __future__ import annotations

import streamlit as st

from services.auth import require_auth

st.set_page_config(page_title="Marketplace Hub",page_icon="🧩",layout="wide")
require_auth()

# Explicit navigation hides the marketplace-specific implementation pages.
pages = [
    st.Page("pages/0_Dashboard.py", title="Dashboard", icon="🏠", default=True),
    st.Page("pages/1_Gestione_Seller.py", title="Gestione Seller", icon="👥"),
    st.Page("pages/2_Fornitori_e_Listini.py", title="Fornitori e Listini", icon="📦"),
    st.Page("pages/2_Provider_IA.py", title="Provider IA", icon="🤖"),
    st.Page("pages/3_Lavora_sui_Listini.py", title="Lavora sui Listini", icon="🧰"),
    st.Page("pages/3_Creazione_Prodotti.py", title="Creazione Prodotti", icon="🧠"),
    st.Page("pages/3_Pubblicazione_Marketplace.py", title="Pubblicazione sui Marketplace", icon="🚀"),
    st.Page("pages/3_Controllo_BuyBox.py", title="Controllo Buy Box", icon="🏆"),
    st.Page("pages/3_Ordini_Marketplace.py", title="Ordini Marketplace", icon="🧾"),
    st.Page("pages/3_Prodotti_Piu_Venduti.py", title="Prodotti più venduti", icon="📈"),
    st.Page("pages/4_Ordini_Cecotec.py", title="Creazione Ordini Cecotec", icon="📤"),
    st.Page("pages/4_Ordini_INNPRO.py", title="Creazione Ordini INNPRO", icon="📦"),
    st.Page("pages/4_Packlink_PRO.py", title="Packlink PRO", icon="📮"),
    st.Page("pages/4_Tracciabilita_Ordini.py", title="Tracciabilità ordini", icon="🚚"),
    st.Page("pages/4_Contabilita.py", title="Contabilità", icon="📊"),
    st.Page("pages/3_Assistenza_Marketplace.py", title="Ticket e messaggi", icon="💬"),
    st.Page("pages/3_Cancellazione_Marketplace.py", title="Cancellazione dai Marketplace", icon="🗑️"),
    st.Page("pages/4_Storico.py", title="Storico", icon="🕘"),
    st.Page("pages/5_Backup_Trasferimento.py", title="Backup e trasferimento", icon="🔁"),
    st.Page("pages/5_Database.py", title="Database", icon="🗄️"),
]

st.navigation(pages, position="sidebar").run()
