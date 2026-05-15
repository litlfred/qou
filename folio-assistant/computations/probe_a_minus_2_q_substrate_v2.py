#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical multi-anchor cross-check; the
# q-polynomial in [n]_q is computed symbolically in sympy where used.
"""Substrate derivation probe v2 — Z/N-dependent structural candidates.

Follow-up to `probe_a_minus_2_q_substrate.py` which falsified the
universal `[A − 2]_q` form (gaps +19.5 % at ³He, +3.2 % at T,
−0.169 % at ⁴He).

The two surprises from v1 — doubly-magic saturation + Z↔N asymmetry —
require a Z/N-dependent correction factor.  This probe tests four
structural candidates *without* fitting to AME:

  D-2 (q-Catalan multiplicity):
      Δ_coupling ≈ E_0 · log(1/h) · Cat_q(A − 1, 1)
                  with Cat_q(A − 1, 1) = [A−1]_q [A−2]_q / ([2]_q [A]_q)

  D-4 (shift_NF q-integer):
      Δ_coupling ≈ E_0 · log(1/h) · [shift_NF(Z, N) − shift_NF(D)]_q / [4]_q
                  testing whether the per-nucleon-shift asymmetry
                  (18 vs 21) propagates symbolically.

  D-5 (Boundary-imbalance product):
      Δ_coupling ≈ E_0 · log(1/h) · [Z]_q · [N]_q
                  q-deformed Z·N product (vanishes for D's (1,1)
                  imbalance test, vs symmetric (1,1)).

  D-6 (q-Gaussian binomial):
      Δ_coupling ≈ E_0 · log(1/h) · [A choose 2]_q / [A]_q

For each anchor and candidate, compute the gap.  A candidate
*survives* iff it closes all three non-trivial anchors {(2,1),
(1,2), (2,2)} to ≤ 5 %.

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `a-minus-2-q-substrate-probe-v2.witness.json`

@module folio-assistant/computations/probe_a_minus_2_q_substrate_v2
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def quantum_integer(n, q):
    """[n]_q := (q^n − q^{−n}) / (q − q^{−1}). Works for any n (int or mpf)."""
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_factorial(n, q):
    """[n]_q! := ∏_{k=1..n} [k]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= quantum_integer(k, q)
    return out


def q_binomial(n, k, q):
    """[n choose k]_q := [n]_q! / ([k]_q! [n−k]_q!)."""
    return q_factorial(n, q) / (q_factorial(k, q) * q_factorial(n - k, q))


def q_catalan_first_corr(A, q):
    """q-Catalan multiplicity at k=1 in the bridge fusion
    V_1^{⊗(A-1)} → ⊕ V_{A-1-2k}, specifically the first non-trivial
    bridge correction:

        Cat_q(A - 1, 1) = [A − 1]_q · [A − 2]_q / ([2]_q · [A]_q)
    """
    return (
        quantum_integer(A - 1, q) * quantum_integer(A - 2, q)
        / (quantum_integer(2, q) * quantum_integer(A, q))
    )


def main() -> int:
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        atom_key: _mpf_from_str(pad[atom_key]["delta_cat_MeV_50dps"])
        for atom_key in ("deuteron", "tritium", "he3", "he4")
    }

    # ── Substrate parameters — imported from q_parameter / codata_constants ──
    # Centralised per gemini review on PR #656; q_parameter computes
    # Q_MP / HA_MP at full 50-dps precision via the Clausen-function path.
    q0 = Q_MP
    h_q = HA_MP
    log_inv_h = mp.log(1 / h_q)
    m_e = M_E_MEV
    E0 = m_e / (q0 * (q0 - 1))

    # ── shift_NF table from per-irrep-pole-atom-crystal.witness ────
    # These are categorically derived in main commit 8c4880083.
    shift_NF = {(1, 1): 40, (2, 1): 58, (1, 2): 61, (2, 2): 79}

    builder = (
        WitnessBuilder("a-minus-2-q-substrate-probe-v2", engine="mpmath")
        .set_description(
            "Follow-up to v1 (which falsified universal [A−2]_q).  "
            "Tests four Z/N-dependent structural candidates "
            "(D-2 q-Catalan, D-4 shift_NF q-integer, D-5 [Z]_q·[N]_q, "
            "D-6 q-Gaussian binomial) at the three non-trivial "
            "anchors (2,1), (1,2), (2,2).  Diagnostic only — does NOT "
            "fit Δ_coupling to AME (three-cal discipline)."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("mp_dps", mp.dps)
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
        .add_parameter("log_inv_h_50dps", mp.nstr(log_inv_h, 50))
    )

    # ── Anchor table ──────────────────────────────────────────────
    anchor_definitions = {
        (1, 1): ("D",   dc["deuteron"]),
        (2, 1): ("³He", dc["he3"]    - dc["deuteron"]),
        (1, 2): ("T",   dc["tritium"] - dc["deuteron"]),
        (2, 2): ("⁴He", dc["he4"]    - 2 * dc["he3"]),
    }

    base = E0 * log_inv_h  # the common dimensional scale

    results = []
    for (Z, N), (label, anchor) in anchor_definitions.items():
        A = Z + N
        if (Z, N) == (1, 1):
            # A − 2 = 0 ⇒ [A−2]_q = 0; trivial baseline, skip predictions.
            results.append({
                "label": label, "Z": Z, "N": N, "A": A,
                "anchor_MeV": float(anchor),
                "note": "A = 2 baseline; all candidate predictions vanish.",
            })
            continue

        # ── Candidate predictions ──────────────────────────────────
        # H7a from v1 (universal [A−2]_q) — for reference.
        h7a = quantum_integer(A - 2, q0) * base

        # D-2: q-Catalan first correction
        d2 = q_catalan_first_corr(A, q0) * base

        # D-4: shift_NF q-integer asymmetry
        # Test [shift_NF(Z,N) − shift_NF(D)]_q / [4]_q · base
        s_zn = shift_NF[(Z, N)]
        s_D = shift_NF[(1, 1)]
        d4 = quantum_integer(s_zn - s_D, q0) / quantum_integer(4, q0) * base

        # D-5: [Z]_q · [N]_q boundary-imbalance product
        d5 = quantum_integer(Z, q0) * quantum_integer(N, q0) * base

        # D-6: q-Gaussian binomial [A choose 2]_q / [A]_q
        d6 = (q_binomial(A, 2, q0) / quantum_integer(A, q0)) * base

        def gap_pct(pred):
            return float(100 * (pred - anchor) / anchor)

        results.append({
            "label": label, "Z": Z, "N": N, "A": A,
            "anchor_MeV": float(anchor),
            "H7a_v1":  {"pred_MeV": float(h7a),  "gap_pct": gap_pct(h7a)},
            "D2_qCat": {"pred_MeV": float(d2),   "gap_pct": gap_pct(d2)},
            "D4_shift_NF_q_int": {
                "pred_MeV": float(d4),
                "gap_pct": gap_pct(d4),
                "shift_diff": s_zn - s_D,
            },
            "D5_ZqNq": {"pred_MeV": float(d5),   "gap_pct": gap_pct(d5)},
            "D6_qGauss": {"pred_MeV": float(d6), "gap_pct": gap_pct(d6)},
        })

    builder.add_data("cross_anchor_predictions", results)

    # ── Print summary ──────────────────────────────────────────────
    print("=" * 100)
    print("  Substrate-derivation v2 — Z/N-dependent candidates")
    print(f"  base = E_0 · log(1/h) = {float(base):.6f} MeV")
    print("=" * 100)
    print()
    print(f"  {'atom':<5}{'(Z,N)':<8}{'anchor':<10}"
          f"{'H7a v1':<14}{'D-2 qCat':<14}{'D-4 shift':<14}"
          f"{'D-5 [Z][N]':<14}{'D-6 qGauss':<14}")
    print(f"  {'':<5}{'':<8}{'(MeV)':<10}"
          f"{'(gap %)':<14}{'(gap %)':<14}{'(gap %)':<14}"
          f"{'(gap %)':<14}{'(gap %)':<14}")
    print("  " + "-" * 95)
    for r in results:
        zn = f"({r['Z']},{r['N']})"
        if 'note' in r:
            print(f"  {r['label']:<5}{zn:<8}{r['anchor_MeV']:<10.4f}  "
                  f"{r['note']}")
            continue
        line = (f"  {r['label']:<5}{zn:<8}{r['anchor_MeV']:<10.4f}"
                f"{r['H7a_v1']['gap_pct']:+8.3f}      "
                f"{r['D2_qCat']['gap_pct']:+8.3f}      "
                f"{r['D4_shift_NF_q_int']['gap_pct']:+8.3f}      "
                f"{r['D5_ZqNq']['gap_pct']:+8.3f}      "
                f"{r['D6_qGauss']['gap_pct']:+8.3f}")
        print(line)
    print()

    # ── Verdict per candidate ─────────────────────────────────────
    thresh = 5.0
    candidates = ["H7a_v1", "D2_qCat", "D4_shift_NF_q_int",
                  "D5_ZqNq", "D6_qGauss"]
    nontrivial = [r for r in results if "note" not in r]
    verdicts = {}
    for cand in candidates:
        gaps = [abs(r[cand]["gap_pct"]) for r in nontrivial]
        verdicts[cand] = {
            "max_gap_pct": max(gaps),
            "all_within_5pct": max(gaps) <= thresh,
            "doubly_magic_gap_pct": next(
                r[cand]["gap_pct"] for r in nontrivial
                if (r["Z"], r["N"]) == (2, 2)
            ),
            "z_n_asymmetry_3He_vs_T": (
                next(r[cand]["gap_pct"] for r in nontrivial
                     if (r["Z"], r["N"]) == (2, 1))
                - next(r[cand]["gap_pct"] for r in nontrivial
                       if (r["Z"], r["N"]) == (1, 2))
            ),
        }
    builder.add_data("candidate_verdicts", verdicts)

    survivors = [c for c, v in verdicts.items() if v["all_within_5pct"]]
    print(f"  Survivors (max gap ≤ {thresh} %): {survivors or 'NONE'}")

    builder.add_data("survivors", survivors)
    builder.add_data(
        "interpretation",
        (
            "If 1+ candidate survives across all three non-trivial "
            "anchors, that's the substrate-derivation route to "
            "explore.  If NONE survive, the Z/N-dependent correction "
            "is more complex (likely a product of two q-integers from "
            "the bridge fusion + the boundary-saturation factor)."
        ),
    )

    out_path = builder.save()
    print(f"\n  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
