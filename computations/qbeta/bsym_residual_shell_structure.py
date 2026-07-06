#!/usr/bin/env python3
"""bsym_residual_shell_structure.py
====================================

EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).
Chases the **B_sym residual** — the deviation of the exact log-trace binding
`B_sym = α·ln(tr_free/tr_atom)` (α = E₀ derived) from AME — across the light
isotopes, isolating the two features the q₀⁵ refutation pointed to as the *real*
targets: **deuteron over-binding** and the **magic-shell deficit**. Derive-or-
refute, NO FIT; NOT wired.

## Why B_sym (not B_pred)

The `q₀^{5(2A−1)}` law is a `B_pred` artifact — against the better `B_sym` form the
per-site exponent collapses to ≈0–1 (see
`docs/audits/2026-06-15-delta-lambda-offset-open-chain-boundary.md` ⚠ and the
sibling refutation). So `Δ_λ^sym = B_AME/B_sym` is the residual that actually
carries physics. This probe maps its structure.

## Structural hypothesis (falsifiable)

`B_sym` is the GENERIC hyperbolic binding. Its residual `Δ_λ^sym` should:
  (H1) **over-bind the deuteron** (`Δ_λ^sym < 1`): the deuteron is anomalously
       weakly bound (no excited state, halo) — a generic trace over-predicts it;
  (H2) **be ≈ 1 on the non-anomalous A=3 nuclei** (T, ³He): the clean regime;
  (H3) **under-bind the doubly-magic ⁴He** (`Δ_λ^sym ≫ 1`): shell closure binds
       MORE than a single hyperbolic knot (the Borromean-volume / B_magic term);
  (H4) **alpha-cluster signature**: ⁸Be = 2α; test whether its under-binding
       tracks ⁴He's (clustering) or the ⁶Li/⁷Li trend.

A refutation of H3 (⁴He NOT an under-binding peak vs neighbors) would falsify the
"magic-shell deficit" reading. This needs the next doubly-magic ¹⁶O (Z=N=8) for a
second point — flagged as the follow-up (AME ¹⁶O + heavier trace, out of reach of
this registry/sandbox).
"""
from __future__ import annotations

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402

import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent

# (label, Z, N, AME-witness key, doubly_magic, note)
ISOTOPES = [
    ("D",   1, 1, "B_deuteron_MeV", False, "pairing/halo anomaly"),
    ("T",   1, 2, "B_tritium_MeV",  False, "normal A=3"),
    ("3He", 2, 1, "B_he3_MeV",      False, "normal A=3"),
    ("4He", 2, 2, "B_he4_MeV",      True,  "doubly-magic (2,2)"),
    ("5Li", 3, 2, "B_li5_MeV",      False, "resonance"),
    ("6Li", 3, 3, "B_li6_MeV",      False, "non-magic"),
    ("7Li", 3, 4, "B_li7_MeV",      False, "non-magic"),
    ("8Be", 4, 4, "B_be8_MeV",      False, "2-alpha cluster"),
    ("9Be", 4, 5, "B_be9_MeV",      False, "non-magic"),
]


def _E0():
    from q_parameter import Q
    from codata_constants import M_E_MEV
    q0 = float(Q() if callable(Q) else Q)
    return float(M_E_MEV) / (q0 * (q0 - 1.0))


def _ame():
    return json.loads((HERE.parent / "ame-2020-binding-energies.witness.json").read_text())["data"]


def _L(Z, N, dps=30):
    from tr_m_atom_via_transfer import tr_m_atom_zn
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=dps)
    return math.log(float(tf) / float(ta))


def main() -> int:
    t0 = time.monotonic()
    E0 = _E0()
    ame = _ame()
    rows = []
    print(f"  E0={E0:.4f} MeV   chasing B_sym residual (deuteron + magic-shell)")
    for label, Z, N, key, magic, note in ISOTOPES:
        ts = time.monotonic()
        try:
            L = _L(Z, N)
        except Exception as e:  # pragma: no cover
            print(f"  {label:>4} A={Z+N:<2} SKIP ({type(e).__name__})", flush=True)
            continue
        B_sym = E0 * L
        B_ame = float(ame[key])
        delta_sym = B_ame / B_sym
        rows.append({"label": label, "Z": Z, "N": N, "A": Z + N,
                     "doubly_magic": magic, "note": note,
                     "L": round(L, 5), "B_sym_MeV": round(B_sym, 4),
                     "B_AME_MeV": round(B_ame, 4),
                     "delta_lambda_sym": round(delta_sym, 4),
                     "B_per_A_AME": round(B_ame / (Z + N), 4)})
        print(f"  {label:>4} A={Z+N:<2} {'MAGIC' if magic else '     '}  "
              f"B_sym={B_sym:6.2f}  B_AME={B_ame:6.2f}  Δ_λ^sym={delta_sym:5.2f}  "
              f"({time.monotonic()-ts:.1f}s)  {note}", flush=True)

    by = {r["label"]: r for r in rows}
    # H1 deuteron over-binds; H2 A=3 ≈ 1; H3 ⁴He under-binding peak vs neighbors
    h1 = "D" in by and by["D"]["delta_lambda_sym"] < 0.8
    h2 = all(k in by and 0.8 < by[k]["delta_lambda_sym"] < 1.25 for k in ("T", "3He"))
    he4 = by.get("4He", {}).get("delta_lambda_sym")
    neigh = [by[k]["delta_lambda_sym"] for k in ("3He", "6Li") if k in by]
    h3 = he4 is not None and neigh and he4 > max(neigh)  # magic = local under-binding peak
    be8 = by.get("8Be", {}).get("delta_lambda_sym")

    w = WitnessBuilder("bsym-residual-shell-structure", engine="python+mpmath", start_time=t0)
    (w.set_description(
        "EXPLORATORY: structure of the B_sym residual Δ_λ^sym=B_AME/B_sym (α=E₀ "
        "derived) across D..⁹Be, the real target after the q₀⁵-vs-B_pred refutation. "
        "Tests: (H1) deuteron over-binds (Δ_λ^sym<1, pairing/halo), (H2) A=3 normal "
        "≈1, (H3) doubly-magic ⁴He is a local under-binding peak (shell closure > "
        "single-knot trace), (H4) ⁸Be 2α-cluster signature. No fit; NOT wired. Full "
        "magic-number confirmation needs ¹⁶O (Z=N=8) — AME+heavier trace, follow-up.")
     .add_parameter("E0_MeV", round(E0, 6))
     .add_data("rows", rows)
     .add_data("hypotheses", {
         "H1_deuteron_over_binds": bool(h1),
         "H2_A3_clean_near_1": bool(h2),
         "H3_4He_magic_under_binding_peak": bool(h3),
         "H4_8Be_alpha_cluster_delta": be8,
         "deuteron_delta": by.get("D", {}).get("delta_lambda_sym"),
         "4He_delta": he4,
     })
     .add_data("interpretation",
               "B_sym = generic hyperbolic binding; residual deviations are the "
               "SEMF pairing term (deuteron over-binding) below and shell-closure "
               "(⁴He doubly-magic under-binding) above; cleanest (~1) at A=3.")
     .add_data("followup", "second doubly-magic ¹⁶O (8,8) to confirm H3 recurs at "
                           "the next shell closure (needs AME ¹⁶O + A=16 trace)")
     .add_data("discipline", "exploratory; derive-or-refute; no fit; NOT wired"))
    w.add_assertion("deuteron_over_binds_H1", computed=bool(h1), expected=True,
                    source="Δ_λ^sym(D) < 0.8: generic trace over-predicts the "
                           "anomalously weakly-bound deuteron (pairing/halo)")
    w.add_assertion("A3_clean_near_one_H2", computed=bool(h2), expected=True,
                    source="0.8 < Δ_λ^sym(T,³He) < 1.25: B_sym is clean on the "
                           "non-anomalous A=3 nuclei")
    w.add_assertion("4He_magic_under_binding_peak_H3", computed=bool(h3), expected=True,
                    source="Δ_λ^sym(⁴He) > max(³He, ⁶Li): doubly-magic shell closure "
                           "binds more than the single-knot trace")
    out = w.save()
    print(f"\n  H1 deuteron over-binds: {h1}   H2 A=3 clean: {h2}   "
          f"H3 ⁴He magic peak: {h3}")
    print(f"  Wrote {out.name} ({len(rows)} isotopes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
