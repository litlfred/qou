#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical multi-anchor cross-check; the
# q-polynomial in [A-2]_q is computed symbolically in sympy where used.
"""Substrate derivation probe — cross-anchor verification of `[A−2]_q`
as the q-prefactor in `Δ_coupling(Z, N) ≈ [A−2]_q · E_0 · log(1/h)`.

Builds directly on PR #645's `probe_delta_coupling_residual_closure.py`
H7a finding at the doubly-magic anchor (2, 2).  Extends to the
single-magic anchors (2, 1) and (1, 2) (and the trivial (1, 1) base)
to test whether the multiplicative form is *universal* in (Z, N) or
specific to the doubly-magic case.

If H7a generalises across all anchors, the same form

    Δ_coupling(Z, N) ≈ [A - 2]_q · E_0 · log(1/h)

(with the SAME q_0, m_e, and h — no per-atom adjustable parameter)
should close every anchor to a few %, supporting one of the three
substrate-derivation candidates D-1 / D-2 / D-3 in

    docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md.

If it fails at (2, 1) or (1, 2), the doubly-magic match is an
accident of the (2, 2) anchor's pole-structure symmetry and the
substrate derivation must be reformulated.

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `a-minus-2-q-substrate-probe.witness.json`

@module computations/probe_a_minus_2_q_substrate
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def quantum_integer(n: int, q) -> "mpf":
    """[n]_q := (q^n − q^{−n}) / (q − q^{−1}). Symmetric convention."""
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


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
    # Avoid duplicating constants per gemini review on PR #656.  Q_MP,
    # HA_MP, LN_Q_MP are computed at full 50-dps precision in
    # q_parameter.py (Clausen-function path); using them keeps the
    # probe's precision claim honest.
    q0 = Q_MP
    h_q = HA_MP  # = q - q^{-1}
    log_inv_h = mp.log(1 / h_q)  # log(1/h) — distinct from LN_Q_MP which is log(q)
    m_e = M_E_MEV
    E0 = m_e / (q0 * (q0 - 1))

    builder = (
        WitnessBuilder(
            "a-minus-2-q-substrate-probe", engine="mpmath"
        )
        .set_description(
            "Cross-anchor probe of the H7a multiplicative form "
            "Δ_coupling(Z, N) ≈ [A−2]_q · E_0 · log(1/h) across "
            "(1, 1), (2, 1), (1, 2), (2, 2) — tests whether the "
            "[A−2]_q substrate prefactor is universal or specific "
            "to the doubly-magic anchor (2, 2).  Diagnostic only — "
            "does NOT fit Δ_coupling to AME (three-cal discipline)."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("mp_dps", mp.dps)
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_parameter("m_e_MeV_CODATA", mp.nstr(m_e, 12))
        .add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
        .add_parameter("h_q_50dps", mp.nstr(h_q, 50))
        .add_parameter("log_inv_h_50dps", mp.nstr(log_inv_h, 50))
    )

    # ── Anchor definitions (per audit doc) ─────────────────────────
    # (Z, N) → (anchor expression in Δ_cat, A, A−2)
    # The (Z, N) = (2, 2) anchor matches PR #645's definition exactly:
    #   Δ_coupling(2, 2) := Δ_cat(⁴He) − 2 · Δ_cat(³He)
    # Single-magic anchors subtract off the deuteron "two-nucleon"
    # baseline (shared between {T, ³He} and the doubly-magic ⁴He):
    #   Δ_coupling(2, 1) := Δ_cat(³He) − Δ_cat(D)
    #   Δ_coupling(1, 2) := Δ_cat(T)   − Δ_cat(D)
    # (1, 1) base = Δ_cat(D) itself (A = 2 → [A−2]_q = [0]_q = 0;
    # the prediction is identically zero so the gap is undefined; we
    # report the raw Δ_cat(D) value for completeness.)

    anchors = []
    for label, Z, N in (
        ("D",   1, 1),
        ("3He", 2, 1),
        ("T",   1, 2),
        ("4He", 2, 2),
    ):
        A = Z + N
        if (Z, N) == (1, 1):
            anchor = dc["deuteron"]
        elif (Z, N) == (2, 1):
            anchor = dc["he3"] - dc["deuteron"]
        elif (Z, N) == (1, 2):
            anchor = dc["tritium"] - dc["deuteron"]
        elif (Z, N) == (2, 2):
            anchor = dc["he4"] - 2 * dc["he3"]
        else:
            raise NotImplementedError(f"({Z},{N})")

        # H7a prediction
        qint_A_minus_2 = quantum_integer(A - 2, q0)
        h7a_pred = qint_A_minus_2 * E0 * log_inv_h

        # H1 classical-integer baseline for comparison
        h1_pred = (A - 2) * E0 * log_inv_h

        # Gap % computed only when prediction non-zero (A > 2).
        h7a_gap_pct = (
            100 * (h7a_pred - anchor) / anchor if h7a_pred != 0 else None
        )
        h1_gap_pct = (
            100 * (h1_pred - anchor) / anchor if h1_pred != 0 else None
        )

        row = {
            "label": label,
            "Z": Z, "N": N, "A": A,
            "A_minus_2": A - 2,
            "anchor_definition": (
                "Δ_cat(D)" if (Z, N) == (1, 1) else
                "Δ_cat(³He) − Δ_cat(D)" if (Z, N) == (2, 1) else
                "Δ_cat(T) − Δ_cat(D)" if (Z, N) == (1, 2) else
                "Δ_cat(⁴He) − 2·Δ_cat(³He)"  # (2, 2)
            ),
            "anchor_MeV_50dps": mp.nstr(anchor, 50),
            "anchor_MeV_float": float(anchor),
            "q_integer_A_minus_2_50dps": mp.nstr(qint_A_minus_2, 50),
            "H7a_prediction_MeV_50dps": mp.nstr(h7a_pred, 50),
            "H7a_prediction_MeV_float": float(h7a_pred),
            "H7a_gap_pct_50dps": (
                mp.nstr(h7a_gap_pct, 12) if h7a_gap_pct is not None
                else None
            ),
            # Numeric float form for verdict logic (gemini review):
            "H7a_gap_pct": float(h7a_gap_pct) if h7a_gap_pct is not None else None,
            "H1_prediction_MeV_50dps": mp.nstr(h1_pred, 50),
            "H1_prediction_MeV_float": float(h1_pred),
            "H1_gap_pct_50dps": (
                mp.nstr(h1_gap_pct, 12) if h1_gap_pct is not None
                else None
            ),
            "H1_gap_pct": float(h1_gap_pct) if h1_gap_pct is not None else None,
        }
        anchors.append(row)

    builder.add_data("cross_anchor_table", anchors)

    # ── Print human-readable summary ───────────────────────────────
    print("=" * 96)
    print("  [A−2]_q substrate-derivation cross-anchor probe")
    print(f"  q_0 = {mp.nstr(q0, 16)}, "
          f"E_0 = {mp.nstr(E0, 8)} MeV, log(1/h) = {mp.nstr(log_inv_h, 8)}")
    print("=" * 96)
    print()
    print(f"  {'atom':<6}{'(Z,N)':<10}{'A-2':<6}{'[A−2]_q':<14}"
          f"{'anchor (MeV)':<16}{'H7a pred':<14}{'gap %':<10}{'H1 gap %':<10}")
    print("  " + "-" * 86)
    for r in anchors:
        zn = f"({r['Z']},{r['N']})"
        h7a_str = f"{r['H7a_gap_pct']:+8.3f}" if r['H7a_gap_pct'] is not None else "    n/a"
        h1_str = f"{r['H1_gap_pct']:+8.3f}" if r['H1_gap_pct'] is not None else "    n/a"
        print(f"  {r['label']:<6}{zn:<10}{r['A_minus_2']:<6}"
              f"{r['q_integer_A_minus_2_50dps'][:12]:<14}"
              f"{r['anchor_MeV_float']:<16.4f}"
              f"{r['H7a_prediction_MeV_float']:<14.4f}"
              f"{h7a_str:<10}{h1_str:<10}")
    print()

    # ── Cross-anchor verdict ───────────────────────────────────────
    # H7a is UNIVERSAL iff all non-trivial anchors close to within
    # a few % (we'll use 5% as the loose-pass threshold; PR #645's
    # 0.169% at (2, 2) is the tight reference).  Guard against None
    # (A−2 = 0 base) per gemini review on PR #656.
    universal_threshold_pct = 5.0
    nontrivial_anchors = [
        r for r in anchors
        if r["A_minus_2"] > 0 and r["H7a_gap_pct"] is not None
    ]
    all_close = all(
        abs(r["H7a_gap_pct"]) <= universal_threshold_pct
        for r in nontrivial_anchors
    )
    builder.add_data(
        "universality_verdict",
        {
            "threshold_pct": universal_threshold_pct,
            "all_anchors_within_threshold": all_close,
            "doubly_magic_2_2_gap_pct": next(
                r["H7a_gap_pct"] for r in anchors if (r["Z"], r["N"]) == (2, 2)
            ),
            "single_magic_2_1_gap_pct": next(
                r["H7a_gap_pct"] for r in anchors if (r["Z"], r["N"]) == (2, 1)
            ),
            "single_magic_1_2_gap_pct": next(
                r["H7a_gap_pct"] for r in anchors if (r["Z"], r["N"]) == (1, 2)
            ),
            "interpretation": (
                "If all single-magic + doubly-magic gaps are within "
                "5%, the [A−2]_q multiplicative form is empirically "
                "universal across the four-atom probe set, supporting "
                "the substrate-derivation candidates D-1 / D-2 / D-3 "
                "in the audit doc.  If single-magic gaps are large but "
                "doubly-magic is tight, H7a is specific to the (2, 2) "
                "anchor and the substrate derivation must be reformulated "
                "(D-3 would be falsified; D-1 or D-2 may still apply "
                "with additional Z/N-dependent factors)."
            ),
        },
    )

    # Numeric form for WitnessBuilder's tolerance-based comparison
    # (gemini review on PR #656: passing a string here caused the
    # internal assertion logic to mark the row "passed: false" even
    # though 0.169 < 1.0 holds).
    doubly_magic_gap = abs(next(
        r["H7a_gap_pct"] for r in anchors if (r["Z"], r["N"]) == (2, 2)
    ))
    builder.add_assertion(
        name="doubly_magic_2_2_within_1pct",
        computed=float(doubly_magic_gap),
        expected=0.0,
        tolerance=1.0,
    )

    out_path = builder.save()
    print(f"  Verdict: H7a universal across 4 anchors (≤ {universal_threshold_pct}%)? "
          f"{all_close}")
    print(f"  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
