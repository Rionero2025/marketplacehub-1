from __future__ import annotations

import base64
import hashlib
import json
import os

from cryptography.fernet import Fernet, InvalidToken


def _fernet() -> Fernet:
    master = os.getenv("MARKETPLACE_HUB_MASTER_KEY", "").strip()
    if not master:
        raise RuntimeError("Configura MARKETPLACE_HUB_MASTER_KEY nei secrets o nelle variabili d'ambiente.")
    key = base64.urlsafe_b64encode(hashlib.sha256(master.encode("utf-8")).digest())
    return Fernet(key)


def encrypt_dict(value: dict) -> str:
    raw = json.dumps(value, ensure_ascii=False).encode("utf-8")
    return _fernet().encrypt(raw).decode("ascii")


def decrypt_dict(value: str) -> dict:
    if not value:
        return {}
    try:
        return json.loads(_fernet().decrypt(value.encode("ascii")).decode("utf-8"))
    except InvalidToken as exc:
        raise RuntimeError("Chiave master errata: impossibile decifrare le credenziali.") from exc


def masked(value: str) -> str:
    value = str(value or "")
    return "••••••••" + value[-4:] if value else "—"
