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
  (H4) **alpha-cluster signature**: ⁸Be = 2α, ¹²C = 3α (Hoyle); test whether the
       α-conjugate cluster nuclei track ⁴He's under-binding (clustering) or the
       ⁶Li/⁷Li non-magic trend.

A refutation of H3 (⁴He NOT an under-binding peak vs neighbors) would falsify the
"magic-shell deficit" reading. The DEFINITIVE H3 test is the *second* doubly-magic
point ¹⁶O (Z=N=8) — see the feasibility-wall note below for why it is deferred.

## Compute path + the feasibility wall (2026-06-16)

The trace is `tr_m_atom_via_transfer.tr_m_atom_zn`, which sums χ^λ over **all
`p(3A)` partitions** via the fine-Bratteli transfer matrix (lossless — no `max_dim`
cap). Empirically (this session, `pyhecke_native` 0.9.0 installed):

    ⁴He  n=12  p=77      0.09 s
    ⁸Be  n=24  p=1575   ~11   s
    ¹²C  n=36  p=17977  ~  (this run)
    ¹⁶O  n=48  p=147273 ~hours  ← DEFERRED (feasibility wall)

Wall scales ≈ `p(3A)^1.6`; ¹⁶O (p=147 273 ≈ 93× ⁸Be) projects to several hours.
**Installing the Rust engine does NOT by itself unlock ¹⁶O** via this path — the
cost is the full `p(3A)` partition enumeration, not the per-word reduction. The
per-block branching combiner (`canonical_tr_m_via_branching`) that would avoid
enumerating `p(3A)` is currently end-to-end only for A=2. So this probe computes
up to `--max-a` (default 12 = ¹²C) and records ¹⁶O as a deferred target with its
projected cost. See
`docs/audits/2026-06-16-bsym-residual-16o-feasibility-wall.md`.
"""
from __future__ import annotations

import argparse
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402

import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent

# Number of partitions of n = 3A (= |chi_atom|), used for the wall projection.
_P3A = {12: 77, 24: 1575, 36: 17977, 48: 147273}

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
    ("12C", 6, 6, "B_c12_MeV",      False, "3-alpha cluster (alpha-conjugate, N=Z)"),
    ("16O", 8, 8, "B_o16_MeV",      True,  "doubly-magic (8,8) — 2nd magic point"),
]


def _E0():
    from q_parameter import Q
    from codata_constants import M_E_MEV
    q0 = float(Q() if callable(Q) else Q)
    return float(M_E_MEV) / (q0 * (q0 - 1.0))


def _ame():
    return json.loads(
        (HERE.parent / "ame-2020-binding-energies.witness.json").read_text()
    )["data"]


def _L(Z, N, dps=30):
    from tr_m_atom_via_transfer import tr_m_atom_zn
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=dps)
    return math.log(float(tf) / float(ta))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-a", type=int, default=12,
                    help="compute trace for A <= MAX_A; larger isotopes are "
                         "recorded as deferred (feasibility wall). Default 12 "
                         "(¹²C). Pass 16 to attempt ¹⁶O (~hours).")
    args = ap.parse_args()

    t0 = time.monotonic()
    E0 = _E0()
    ame = _ame()
    rows = []
    deferred = []
    print(f"  E0={E0:.4f} MeV   chasing B_sym residual (deuteron + magic-shell)"
          f"   max_a={args.max_a}")
    for label, Z, N, key, magic, note in ISOTOPES:
        A = Z + N
        n = 3 * A
        if A > args.max_a:
            deferred.append({
                "label": label, "Z": Z, "N": N, "A": A, "n_3A": n,
                "doubly_magic": magic, "note": note,
                "n_partitions": _P3A.get(n),
                "reason": (f"feasibility wall: tr_m_atom_zn enumerates all "
                           f"p({n})={_P3A.get(n)} partitions; wall ~p^1.6 "
                           f"projects to hours. Re-run with --max-a {A}."),
                "B_AME_MeV": float(ame[key]) if key in ame else None,
            })
            print(f"  {label:>4} A={A:<2} {'MAGIC' if magic else '     '}  "
                  f"DEFERRED (p({n})={_P3A.get(n)}, ~hours)  {note}", flush=True)
            continue
        ts = time.monotonic()
        try:
            L = _L(Z, N)
        except Exception as e:  # pragma: no cover
            print(f"  {label:>4} A={A:<2} SKIP ({type(e).__name__}: "
                  f"{str(e)[:80]})", flush=True)
            continue
        wall = time.monotonic() - ts
        B_sym = E0 * L
        B_ame = float(ame[key])
        delta_sym = B_ame / B_sym
        rows.append({"label": label, "Z": Z, "N": N, "A": A,
                     "doubly_magic": magic, "note": note,
                     "L": round(L, 5), "B_sym_MeV": round(B_sym, 4),
                     "B_AME_MeV": round(B_ame, 4),
                     "delta_lambda_sym": round(delta_sym, 4),
                     "B_per_A_AME": round(B_ame / A, 4),
                     "wall_s": round(wall, 2), "n_partitions": _P3A.get(n)})
        print(f"  {label:>4} A={A:<2} {'MAGIC' if magic else '     '}  "
              f"B_sym={B_sym:7.2f}  B_AME={B_ame:7.2f}  Δ_λ^sym={delta_sym:5.2f}  "
              f"({wall:6.1f}s)  {note}", flush=True)

    by = {r["label"]: r for r in rows}
    # H1 deuteron over-binds; H2 A=3 ≈ 1; H3 ⁴He under-binding peak vs neighbors
    h1 = "D" in by and by["D"]["delta_lambda_sym"] < 0.8
    h2 = all(k in by and 0.8 < by[k]["delta_lambda_sym"] < 1.25 for k in ("T", "3He"))
    he4 = by.get("4He", {}).get("delta_lambda_sym")
    neigh = [by[k]["delta_lambda_sym"] for k in ("3He", "6Li") if k in by]
    h3 = he4 is not None and neigh and he4 > max(neigh)  # magic = local under-binding peak
    # H4 alpha-cluster signature across ⁸Be (2α) and ¹²C (3α)
    cluster = {k: by[k]["delta_lambda_sym"] for k in ("8Be", "12C") if k in by}

    w = WitnessBuilder("bsym-residual-shell-structure", engine="python+mpmath", start_time=t0)
    (w.set_description(
        "EXPLORATORY: structure of the B_sym residual Δ_λ^sym=B_AME/B_sym (α=E₀ "
        "derived) across D..¹²C, the real target after the q₀⁵-vs-B_pred refutation. "
        "Tests: (H1) deuteron over-binds (Δ_λ^sym<1, pairing/halo), (H2) A=3 normal "
        "≈1, (H3) doubly-magic ⁴He is a local under-binding peak (shell closure > "
        "single-knot trace), (H4) α-cluster signature across ⁸Be (2α) + ¹²C (3α). "
        "No fit; NOT wired. The DEFINITIVE H3 recurrence test (2nd magic point ¹⁶O, "
        "Z=N=8) is DEFERRED: tr_m_atom_zn enumerates all p(48)=147273 partitions, "
        "wall ~p^1.6 ≈ hours — installing the Rust engine does not lift this; the "
        "per-block branching combiner that would (no p(3A) enumeration) is A=2-only.")
     .add_parameter("E0_MeV", round(E0, 6))
     .add_parameter("max_a", args.max_a)
     .add_data("rows", rows)
     .add_data("deferred", deferred)
     .add_data("hypotheses", {
         "H1_deuteron_over_binds": bool(h1),
         "H2_A3_clean_near_1": bool(h2),
         "H3_4He_magic_under_binding_peak": bool(h3),
         "H4_alpha_cluster_deltas": cluster,
         "deuteron_delta": by.get("D", {}).get("delta_lambda_sym"),
         "4He_delta": he4,
     })
     .add_data("feasibility_wall", {
         "compute_path": "tr_m_atom_via_transfer.tr_m_atom_zn (full p(3A) "
                         "fine-Bratteli transfer matrix; lossless, no max_dim cap)",
         "scaling": "wall ~ p(3A)^1.6 (empirical: ⁴He 0.09s @p77, ⁸Be ~11s @p1575)",
         "16O_projection": "p(48)=147273 ≈ 93× ⁸Be → several hours; infeasible "
                           "this session",
         "rust_engine_note": "pyhecke_native 0.9.0 installed this session; it "
                             "accelerates per-word reduction, NOT the p(3A) "
                             "enumeration that dominates large-A. So the Rust "
                             "install does NOT unlock ¹⁶O via this path.",
         "real_blocker": "canonical_tr_m_via_branching (per-block combiner, no "
                         "p(3A) enumeration) is end-to-end only for A=2; "
                         "extending it to A>=3 is the genuine unlock for ¹⁶O.",
     })
     .add_data("interpretation",
               "B_sym = generic hyperbolic binding; residual deviations are the "
               "SEMF pairing term (deuteron over-binding) below and shell-closure "
               "(⁴He doubly-magic under-binding) above; cleanest (~1) at A=3.")
     .add_data("followup", "extend canonical_tr_m_via_branching to A>=3 so the "
                           "2nd doubly-magic ¹⁶O (8,8) becomes computable, then "
                           "confirm H3 recurs at the next shell closure")
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
    print(f"  H4 α-cluster Δ_λ^sym: {cluster}")
    if deferred:
        print(f"  DEFERRED (feasibility wall): {[d['label'] for d in deferred]}")
    print(f"  Wrote {out.name} ({len(rows)} isotopes computed, "
          f"{len(deferred)} deferred)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
