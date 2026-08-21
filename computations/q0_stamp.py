#!/usr/bin/env python3
"""Stamp `q0Anchor` / `q0Value` onto a HAND-WRITTEN witness payload.

`qou_substrate.witness.WitnessBuilder` stamps the pin automatically at write
time (see its `_build` guard). A producer that hand-rolls its witness —
`json.dumps(payload)` straight to `write_text` — bypasses that path entirely
and emits an UNSTAMPED witness, even when the producer IS declared in
`q0_anchor_manifest.json`.

That is not a cosmetic gap. Three such producers
(`e_hartree_round24_molecular_reuse`, `lw2_c2_independent_hopf_test_attempt`,
`sigma_f_electron_shell_chain`) carried `q0Anchor: "muon"` on disk only
because a one-off bulk pass had post-stamped the committed files; re-running
the producer silently DROPPED the stamp, moving each witness from Q0_OK to
Q0_ANCHOR_MISSING in `q0_anchor_consistency_audit`. A witness that does not
say which pin it used cannot be triaged for the mu-p layer straddle, which is
what AGENTS.md q0 rule 4 ("Say which pin you used") exists to prevent.

Use this at the hand-writer's own write site, so the stamp is a property of
the producer rather than of a sweep that happened to run over it:

    from q0_stamp import stamp_q0_anchor
    stamp_q0_anchor(witness, __file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")

An explicit anchor already in the payload always WINS -- a comparison
producer deliberately carrying both pins, or one declaring "independent",
keeps what it wrote. An undeclared producer is left unstamped:
Q0_ANCHOR_MISSING is a tolerated state, and defaulting a pin in would assert
one nobody established.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parents[1]
                        / "tools" / "qou-substrate" / "python"))


_Q0_FIELDS = ("q0", "q_0", "q0_value", "q_0_50dps", "q0_50dps")


def _recorded_q0(payload: dict):
    """Best-effort: the q0 the payload ACTUALLY computed with, as a string."""
    holders = [payload]
    for key in ("data", "result", "parameters"):
        h = payload.get(key)
        if isinstance(h, dict):
            holders.append(h)
            sub = h.get("parameters")
            if isinstance(sub, dict):
                holders.append(sub)
    for h in holders:
        for f in _Q0_FIELDS:
            v = h.get(f)
            if isinstance(v, (str, float, int)):
                return str(v)
    return None


def stamp_q0_anchor(payload: dict, script_path) -> dict:
    """Add `q0Anchor`/`q0Value` to `payload` in place; return it.

    No-op when the producer is undeclared, when the resolved anchor is not a
    concrete pin, or when the payload already states an anchor.

    **Disagreement guard.** The stamp is REFUSED when the payload's own
    recorded q0 does not match the pin the manifest resolves to. Stamping
    regardless is how a Q0_FLIP is manufactured: the audit reads the anchor as
    authoritative, so a producer that silently fell back to the other pin
    would land as Q0_OK while carrying the wrong number.

    This is not hypothetical. 254 producers hardcode the MUON constant
    `1.1099785955573347...` as an import fallback -- 78 of them directly under
    a comment calling it the "proton-anchor re-pin" -- so any run where
    `q_parameter` fails to import computes at the muon pin while the manifest
    declares proton. Refusing to stamp leaves Q0_ANCHOR_MISSING, a tolerated
    and VISIBLE state, instead of a false Q0_OK. Tracked as bean `qou-0hnz`.
    """
    if not isinstance(payload, dict) or "q0Anchor" in payload:
        return payload
    try:
        from qou_substrate.witness import (  # noqa: PLC0415
            q0_anchor_is_declared, resolve_q0_anchor,
        )
        if not q0_anchor_is_declared(script_path):
            return payload
        anchor, value = resolve_q0_anchor(script_path)
        if anchor not in ("muon", "proton"):
            return payload
        recorded = _recorded_q0(payload)
        if recorded is not None and value is not None:
            # Compare on the shared prefix: the payload may carry fewer digits
            # than the 50-dps pin, but the two pins differ at the 11th.
            n = min(len(recorded), len(str(value)), 17)
            if recorded[:n] != str(value)[:n]:
                payload["q0AnchorReason"] = (
                    f"UNSTAMPED: manifest resolves {anchor!r} but this run "
                    f"recorded q0={recorded[:22]}. Refusing to stamp an "
                    f"anchor the value contradicts (see q0_stamp)."
                )
                return payload
        payload["q0Anchor"] = anchor
        if value is not None:
            payload["q0Value"] = value
    except Exception:  # noqa: BLE001 -- stamping never breaks a producer
        pass
    return payload
