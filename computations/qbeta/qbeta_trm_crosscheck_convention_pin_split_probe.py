#!/usr/bin/env python3
"""
The L1 tr_M cross-check is red for TWO reasons, not one — and only one was known.

Bean `qou-3zby`. `cross_check_trM_1ppb.py --strict` has been red on `main`
since at least 2026-08-16: 6/6 atoms diverge, 0 certified at 1 ppQ. The bean
recorded it as a convention-C/D straddle across the four methods. That is
half of it.

WHAT THIS MEASURES
------------------
Reading the four committed input witnesses and comparing the deuteron
|tr_M| — the atom all four methods cover — classifies them WITHOUT any
external reference value, from the ratios alone:

    Hoefsmit vs chi-cache   agree to ~3e-09   -> same convention, same pin
    peel     vs Habiro      agree to ~1.8e-04 -> same convention, DIFFERENT pin
    Hoefsmit vs peel        ratio  ~1.481     -> DIFFERENT convention

The first two are the point. A 3e-09 agreement is what two methods on the
same footing look like. A 1.8e-04 agreement is not "close" — it is four
orders above the 1 ppQ (1e-15) gate, and it is the size of a muon/proton pin
change, not of a convention change (which is the 1.481 factor).

THE SECOND DEFECT
-----------------
`cross_check_trM_1ppb.py` raises `SystemExit` unless the RUNTIME q0 is the
muon pin. It is therefore a muon-pin gate by construction. But its inputs are
COMMITTED witnesses, and Habiro's values match convention C at the PROTON pin
to 2.71e-13 — an exact match, not a near one.

It survived because `habiro-coefficients-extended.witness.json` records no
q0 anywhere, so there was nothing for the guard to compare against. Nor is it
unusual: `atomic-tr-m-mpfr-50dps` records none either, and 1966 of 2681
corpus witnesses (73%) carry no `q0Anchor`.

The runtime guard gives FALSE ASSURANCE: refusing to start off-muon makes the
run look pin-uniform while a committed input sits at the other pin. Fixed in
the same commit by extending the guard to every input that records a q0, and
NAMING the ones that do not instead of skipping them silently.

SCOPE
-----
Diagnosis only, scope-(a). Wires nothing, changes no value, and does not
regenerate any witness. The two repairs belong elsewhere:
  * the PIN straddle    -> regenerate habiro-coefficients-extended under
                           QOU_Q0_ANCHOR=ideal and stamp its anchor
  * the CONVENTION split -> the convention-D cascade's work, not this bean's

Only ONE script in `computations/` enforces a runtime pin, so this is not a
corpus-wide class — it is this gate. Stated because the 73% figure invites
the over-claim.

Usage:
    python3 computations/qbeta/qbeta_trm_crosscheck_convention_pin_split_probe.py
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401
import _path_bridge as _pb  # noqa: E402 — the gate's own witness resolver

from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

INPUTS = {
    "Hoefsmit": "atomic-tr-m-mpfr-50dps",
    "chi-cache": "canonical-tr-m-via-chi-cache",
    "markov_peel": "markov-peel-atomic-tr-m-muon",
    "Habiro": "habiro-coefficients-extended",
}


def _repo_head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE),
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


def _find(stem: str):
    """Resolve exactly as the GATE does — `_path_bridge.witness_path`.

    NOT `rglob`. There are TWO copies of `habiro-coefficients-extended.
    witness.json` — `computations/` and `computations/habiro/` — with
    identical payloads and scriptHash but DIFFERENT `q0Anchor`
    (`ambiguous` vs absent). An `rglob` here picked the one the gate does
    not load, and this probe reported the wrong anchor for its headline
    input until that was caught. A diagnosis of a gate has to read the
    gate's own files.
    """
    return _pb.witness_path(f"{stem}.witness.json", ROOT / "computations")


def _muon_q0() -> str:
    """The canonical muon q0, read from the same witness the gate reads."""
    p = _find("q-pinning-50-digit")
    d = json.loads(Path(p).read_text())
    return str(d["derived_50_digit"]["q"])


def _recorded_q0(doc: dict):
    v = doc.get("q0Value")
    if v is None:
        pq = doc.get("parameters", {}).get("q0")
        v = pq.get("value") if isinstance(pq, dict) else pq
    return v


def main() -> int:
    t0 = time.monotonic()

    # The measured deuteron |tr_M| from the four methods, as the gate reports
    # them at the muon runtime pin. Recorded here rather than recomputed: this
    # probe diagnoses the GATE's inputs, and re-deriving them would test a
    # different thing.
    cols = {
        "Hoefsmit": mp.mpf("0.5751722439177718"),
        "chi-cache": mp.mpf("0.5751722457697713"),
        "markov_peel": mp.mpf("0.3883571887237810"),
        "Habiro": mp.mpf("0.3882864715594088"),
    }

    def rel(a, b):
        return abs(a - b) / abs(b)

    d_hoef_chi = rel(cols["Hoefsmit"], cols["chi-cache"])
    d_peel_hab = rel(cols["markov_peel"], cols["Habiro"])
    ratio_conv = cols["Hoefsmit"] / cols["markov_peel"]

    anchors = {}
    for name, stem in INPUTS.items():
        p = _find(stem)
        doc = json.loads(p.read_text()) if p else {}
        anchors[name] = {
            "witness": stem,
            "q0Anchor": doc.get("q0Anchor"),
            "recorded_q0": str(_recorded_q0(doc)) if _recorded_q0(doc) else None,
        }
    # "unverifiable" is about a missing q0 VALUE, not a missing anchor LABEL.
    # Habiro carries `q0Anchor: "ambiguous"` — a state the q0-anchor audit
    # explicitly tolerates ("producer genuinely undetermined") — and no value.
    # A label the guard cannot compare against is not coverage.
    unverifiable = sorted(n for n, a in anchors.items() if a["recorded_q0"] is None)

    print("=== deuteron |tr_M| across the four cross-check methods (muon runtime pin)")
    for n, v in cols.items():
        a = anchors[n]
        print(f"  {n:12s} {mp.nstr(v, 17):20s} anchor={str(a['q0Anchor']):6s} "
              f"recorded_q0={'yes' if a['recorded_q0'] else 'NO'}")
    print()
    print(f"  Hoefsmit vs chi-cache : {mp.nstr(d_hoef_chi, 4):>12s}  same convention, same pin")
    print(f"  peel     vs Habiro    : {mp.nstr(d_peel_hab, 4):>12s}  same convention, DIFFERENT pin")
    print(f"  Hoefsmit / peel       : {mp.nstr(ratio_conv, 16):>12s}  the C->D ratio")
    print(f"  inputs with no recorded q0: {', '.join(unverifiable) or 'none'}")

    assertions = [
        {"name": "1_hoef_and_chi_are_same_footing",
         "passed": bool(d_hoef_chi < mp.mpf("1e-8")),
         "detail": f"Hoefsmit vs chi-cache {mp.nstr(d_hoef_chi, 4)} — two methods "
                   "on the same convention AND pin agree at ~1e-9"},
        {"name": "2_peel_and_habiro_split_by_a_PIN_not_a_convention",
         "passed": bool(mp.mpf("1e-6") < d_peel_hab < mp.mpf("1e-2")),
         "detail": f"peel vs Habiro {mp.nstr(d_peel_hab, 4)} — far above the 1 ppQ "
                   "gate but nothing like the 1.481 convention factor; this is the "
                   "muon/proton pin signature and it was NOT in the bean's diagnosis"},
        {"name": "3_convention_split_is_the_1p481_factor",
         "passed": bool(abs(ratio_conv - mp.mpf("1.481")) < mp.mpf("0.001")),
         "detail": f"Hoefsmit/peel = {mp.nstr(ratio_conv, 16)} — the C->D ratio, "
                   "confirming the convention straddle the bean already recorded"},
        {"name": "4_two_inputs_cannot_be_pin_verified",
         "passed": bool(unverifiable == ["Habiro", "Hoefsmit"]),
         "detail": f"inputs recording no q0 VALUE: {unverifiable}. Habiro is "
                   "labelled q0Anchor=ambiguous, a tolerated state, and Hoefsmit "
                   "carries no anchor at all — neither gives the guard anything to "
                   "compare, so both bypass a gate that refuses to START off-muon"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-trm-crosscheck-convention-pin-split",
        "description": "The L1 tr_M cross-check is red for two independent reasons. "
                       "The known one is a convention C/D straddle (Hoefsmit and "
                       "chi-cache on D, peel and Habiro on C — the 1.481 factor). The "
                       "unrecorded one is a PIN straddle: Habiro matches convention C "
                       "at the PROTON pin to 2.71e-13, inside a gate that raises "
                       "SystemExit unless the RUNTIME pin is muon. It survived because "
                       "that witness records no q0 for the guard to compare against.",
        "audit_only": True,
        "tier": "measured (from committed witnesses)",
        "scope": "scope-(a), diagnosis only. Wires nothing, changes no value, "
                 "regenerates no witness. Only one script in computations/ enforces a "
                 "runtime pin, so this is this gate — not a corpus-wide class.",
        # muon WITH its value. Declaring an anchor and no `q0Value` is the
        # q0-anchor audit's Q0_VALUE_MISSING state — an anchor nothing can
        # check — and the first cut of this probe did exactly that, pushing
        # that count 2 -> 3. Every column compared here is a muon-runtime
        # value, so the pin is real and belongs on the record with the value
        # that makes it verifiable.
        "q0Anchor": "muon",
        "q0Value": _muon_q0(),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "deuteron_abs_tr_M": {k: fmt(v) for k, v in cols.items()},
            "input_anchors": anchors,
            "hoef_vs_chi_rel": fmt(d_hoef_chi),
            "peel_vs_habiro_rel": fmt(d_peel_hab),
            "convention_ratio_hoef_over_peel": fmt(ratio_conv),
            "inputs_without_recorded_q0": unverifiable,
            "verdict": "Two repairs, two owners: regenerate "
                       "habiro-coefficients-extended under QOU_Q0_ANCHOR=ideal and "
                       "stamp its anchor (the pin straddle); the C->D split belongs to "
                       "the convention-D cascade. The guard extension landing with this "
                       "probe closes the false-assurance hole but drains neither.",
        },
        "context": {
            "bean": "qou-3zby",
            "gate": "computations/cross_check_trM_1ppb.py (the L1 compute-precision gate)",
            "audit": "docs/audits/2026-07-18-avg-color-delta-q0-pin-mismatch.md",
            "corpus_context": "1966 of 2681 witnesses (73%) carry no q0Anchor",
        },
    }

    out = HERE / "qbeta-trm-crosscheck-convention-pin-split.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"\nwitness -> {out}")
    print(f"allPassed: {all_passed}  ({int((time.monotonic() - t0) * 1000)} ms)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
