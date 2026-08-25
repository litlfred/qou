#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""c_knot_not_universal_probe.py — formalize-first prune of the C_knot attack: the deuteron
binding deficit C_knot is NOT a single universal derivable factor. It is convention-dependent
(41× for the deuteron alone) and isotope-dependent — so "derive C_knot = 5.85" is refuted as a
shortcut; C_knot ≡ the full convention-pinned per-partition Δ_λ.

Context (the C_knot gate, from PR #4491 §0)
-------------------------------------------
The master binding formula B = m_e·|Σ_λ (weight)·χ^λ(β_K)·sgn·f^λ| undershoots; the deficit
C_knot = B_AME/(m_e·|Σ|) is an EXPLICITLY FITTED (not derived) ratio = the open Δ_λ gate
(binding_energy_categorical_deuteron.py). "Deriving C_knot" would improve binding — IF C_knot were a
single geometric factor. This probe runs the formalize-first FIRST step (find the invariant / prune the
class) and finds the single-universal-factor hypothesis REFUTED.

THE MEASUREMENT (two independent corpus computations)
-----------------------------------------------------
For the SAME deuteron, two weighting conventions give wildly different naive sums (hence C_knot):

  * interface-inclusive per-λ sum (binding-energy-categorical-deuteron):
        |Σ| = 0.7436,  B_naive = 0.380 MeV,  C_knot(D) = 5.85
  * signed dim_q sum (delta-lambda-multi-atom-crosscheck):
        |Σ| = 0.0181,  B_naive = 0.00926 MeV, C_knot(D) = 240

  ⇒ convention spread for the deuteron alone: 240/5.85 ≈ 41×.

Across isotopes in the signed-dim_q convention: C_knot(D)=240, C_knot(T)=40717, C_knot(³He)=31475.

HONEST CAVEAT (do not over-claim the A-dependence): the signed dim_q naive sum NEARLY CANCELS for the
triton (B_naive(T) = 0.0002 MeV ≪ any reasonable scale) — a bar-even/bar-odd cancellation pathology —
so the extreme 40717× is a convention-specific near-cancellation, NOT clean evidence that a
well-behaved C_knot varies 170× with A. The ROBUST claim is the CONVENTION dependence (41× for D):
two legitimate weightings of the same deuteron give 41×-different deficits.

VERDICT (scope-a) — the single-universal-C_knot hypothesis is REFUTED
--------------------------------------------------------------------
A single derivable constant `C_knot` cannot fit even the deuteron across conventions (5.85 vs 240), let
alone all isotopes. So "improve binding by deriving one geometric factor 5.85" is not available:
`C_knot` ≡ the full per-partition Δ_λ magnitude, and it is not even well-posed until the weighting
convention is PINNED. This narrows the C_knot attack correctly (kills the one-number shortcut) and
connects the gate to the convention-fragility thread of PR #4491 (μ₃, the units pun, the scale
ambiguity — all convention-dependent). It is scope-(a): a refutation of the single-factor SHORTCUT, NOT
a structural exclusion of a Δ_λ derivation (which remains open, bean qou-3q7t).

STRICT anti-fit: C_knot values are read from two committed witnesses; nothing fitted, nothing wired.
Exact (mpmath). EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMP = ROOT / "computations"


def _load(name):
    """Fail fast if a required witness input is absent — do not silently fall back to hard-coded
    constants (that would mask a bad path/rename and make runs non-reproducible)."""
    p = COMP / name
    if not p.exists():
        raise FileNotFoundError(
            f"required witness input missing: {p} — this probe reads C_knot from committed witnesses; "
            f"regenerate them (binding_energy_categorical_deuteron.py / delta_lambda_multi_atom_crosscheck.py) "
            f"before running.")
    return json.loads(p.read_text())


def main() -> int:
    # convention 1: interface-inclusive (deuteron probe) — _load raises if missing (fail fast)
    dprobe = _load("binding-energy-categorical-deuteron.witness.json")
    c_interface = mp.mpf(str(dprobe["data"]["C_knot_deuteron"]))
    # convention 2: signed dim_q (multi-atom crosscheck)
    xcheck = _load("delta-lambda-multi-atom-crosscheck.witness.json")
    cd = mp.mpf(str(xcheck["data"]["D"]["C_knot_needed"]))
    ct = mp.mpf(str(xcheck["data"]["T"]["C_knot_needed"]))
    che = mp.mpf(str(xcheck["data"]["3He"]["C_knot_needed"]))
    bnaive_T = mp.mpf(str(xcheck["data"]["T"]["B_naive_MeV"]))

    convention_spread_D = cd / c_interface                # 41× — the ROBUST claim
    a_spread_signeddim = ct / cd                          # 170× — with near-cancellation caveat
    triton_near_cancellation = bool(bnaive_T < mp.mpf("0.01"))   # B_naive(T) ≪ MeV ⇒ signed sum cancels

    single_factor_refuted = bool(convention_spread_D > 10)   # no single constant fits D across conventions

    result = {
        "deuteron_C_knot_two_conventions": {
            "interface_inclusive": mp.nstr(c_interface, 6),
            "signed_dim_q": mp.nstr(cd, 6),
            "convention_spread_factor": mp.nstr(convention_spread_D, 5) + " (ROBUST — same deuteron)",
        },
        "signed_dim_q_across_isotopes": {
            "C_knot_D": mp.nstr(cd, 6), "C_knot_T": mp.nstr(ct, 6), "C_knot_3He": mp.nstr(che, 6),
            "a_spread_T_over_D": mp.nstr(a_spread_signeddim, 5),
            "triton_naive_MeV": mp.nstr(bnaive_T, 4),
            "triton_near_cancellation": triton_near_cancellation,
            "caveat": "the signed dim_q sum NEARLY CANCELS for T (B_naive=0.0002 MeV ≪ scale) — a "
                      "bar-even/bar-odd cancellation pathology; the 170× is convention-specific, NOT "
                      "clean A-dependence of a well-behaved deficit.",
        },
        "verdict": {
            "single_universal_C_knot_refuted": single_factor_refuted,
            "classification": "scope-(a): the single-universal-C_knot SHORTCUT is refuted. A single "
                              "derivable constant cannot fit even the deuteron across weighting "
                              "conventions (5.85 vs 240, 41×). So 'improve binding by deriving one "
                              "geometric factor 5.85' is not available — C_knot ≡ the full "
                              "convention-pinned per-partition Δ_λ, not well-posed until the weighting "
                              "is pinned. NOT a structural exclusion of a Δ_λ derivation (open, "
                              "bean qou-3q7t); a refutation of the one-number shortcut.",
            "connects_to": "the convention-fragility thread of PR #4491 — μ₃ (baseline-class-relative), "
                           "the units pun (MeV vs dimensionless), the scale ambiguity (C_knot itself). "
                           "C_knot is one more convention-dependent quantity.",
            "anti_fit": "C_knot values read from two committed witnesses; nothing fitted or wired.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "c-knot-not-universal",
        "description": (
            "Formalize-first prune of the C_knot attack: the deuteron binding deficit C_knot is NOT a "
            "single universal derivable factor. The SAME deuteron gives C_knot=5.85 (interface-inclusive "
            "per-λ sum) vs 240 (signed dim_q sum) — a 41× convention spread. Across isotopes the signed "
            "dim_q convention gives 240/40717/31475 (D/T/³He), but the triton naive sum NEARLY CANCELS "
            "(0.0002 MeV) so that 170× is a convention-specific pathology, not clean A-dependence "
            "(honest caveat). ROBUST claim: no single constant fits even the deuteron across "
            "conventions, so 'derive C_knot = 5.85' as a one-number shortcut to improve binding is "
            "REFUTED — C_knot ≡ the full convention-pinned per-partition Δ_λ, ill-posed until the "
            "weighting is pinned. scope-(a) refutation of the SHORTCUT (not a structural exclusion of a "
            "Δ_λ derivation, open, bean qou-3q7t). Connects to the convention-fragility thread of PR "
            "#4491. No fit; nothing wired; values read from two committed witnesses; exact (mpmath)."),
        "audit_only": True,
        "tier": "scope-(a) formalize-first prune (single-universal-C_knot shortcut refuted); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {"axis": "Δ_λ / C_knot derivation — is it one universal factor?",
                    "builds_on": "PR #4491 §0 (C_knot gate), binding-energy-categorical-deuteron, "
                                 "delta-lambda-multi-atom-crosscheck", "bean": "qou-3q7t", "no_fit": True},
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)], cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "c-knot-not-universal.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    print("=== formalize-first: is C_knot one universal derivable factor? NO ===")
    print(f"deuteron C_knot: interface-inclusive = {mp.nstr(c_interface,5)}  signed-dim_q = {mp.nstr(cd,5)}")
    print(f"  CONVENTION spread (same deuteron) = {mp.nstr(convention_spread_D,4)}×  (ROBUST)")
    print(f"signed-dim_q across isotopes: D={mp.nstr(cd,5)} T={mp.nstr(ct,5)} ³He={mp.nstr(che,5)}")
    print(f"  triton naive sum = {mp.nstr(bnaive_T,4)} MeV ≪ scale ⇒ NEAR-CANCELLATION "
          f"(so the {mp.nstr(a_spread_signeddim,4)}× is convention pathology, not clean A-dependence)")
    print()
    print("VERDICT (scope-a): single-universal-C_knot REFUTED — no constant fits even D across "
          "conventions (41×). C_knot ≡ full convention-pinned Δ_λ; the one-number shortcut to improve "
          "binding is not available. Δ_λ derivation remains open (bean qou-3q7t). No fit.")
    print(f"witness -> {out.name}")

    assert single_factor_refuted, "convention spread must refute a single universal factor"
    assert triton_near_cancellation, "triton signed sum must be flagged as near-cancelling"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
