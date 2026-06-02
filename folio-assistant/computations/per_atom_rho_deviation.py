#!/usr/bin/env python3
"""
Per-atom ρ-deviation diagnostic — path to 1 ppb.

For the small hard-coded light-atom probe in `AME` below (`²H, ³H,
³He, ⁴He`), the canonical Kashaev-law family-1 prediction is
`B_pred = ρ_F · m_e · Vol_hyp(K)` with ρ_F a structural integer
(1 or 2). PR #512 showed that the "true" ρ
(= B_AME / (m_e · Vol_hyp(K))) for ³He is 2.062, not 2 — a +3.1%
substrate-q correction beyond the integer.

This script computes the "true" ρ implied by AME and the canonical
Vol·m_e factor for those four seed atoms, then tests whether the
deviation δρ = ρ_true / ρ_struct − 1 matches any pre-specified
categorical q-arithmetic form. The Z=N regularity is then propagated
through the α-cluster chain (`⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca`) in the
second half of the script. Extending to a full mass-table-ppb sweep is
a follow-up; this focused probe is enough to surface the
+δρ = -([A]_q − A) / ρ_struct regularity that motivates the
`conj:z-eq-n-rho-correction` block.

**No fitting.** All candidate forms for δρ are stated in advance from
the substrate's standard q-anchors (η_q, ℏ_q, 1/c_q, d_H(q), low-order
[n]_q ratios). If none match within the ~10⁻³ scale of the residuals,
that is a negative result that sharpens the next probe.

Usage:
    python3 per_atom_rho_deviation.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, q_int  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_E_MEV,
    VOL_6_2,
    VOL_8_11,
    VOL_L6A4,
    VOL_7_SQ_1,
    EIGHT_G,
)

# For backwards-comparison with the existing mass-table-ppb pipeline,
# we keep the 8·G ("Catalan") form for the magic-A volume input —
# legacy mass_table_ppb.py uses 8·CATALAN_G ≈ 7.327724753417752,
# which differs from the SnapPy VOL_L6A4 = 7.327724753846269 at the
# 10⁻⁹ level. At 1 ppb this matters; both forms are exposed below.
VOL_BORROMEAN_EIGHT_G = EIGHT_G        # legacy magic-A input (8·G)
VOL_BORROMEAN_SNAPPY  = VOL_L6A4       # SnapPy actual link volume
KNOT_VOL = {
    "6_2":  VOL_6_2,
    "8_11": VOL_8_11,
    "L6a4": VOL_BORROMEAN_EIGHT_G,           # match mass_table_ppb baseline
}

# AME2020 light-atom data
AME = {
    # sym  -> (knot, rho_struct, A, B_AME)
    "2H":  ("6_2",     1, 2,  2.22456612),
    "3H":  ("8_11",    2, 3,  8.4817984),
    "3He": ("L6a4",    2, 3,  7.7180375),
    # ⁴He uses 4·8G (magic-A); list separately for direct comparison.
    "4He": ("L6a4_x4", 2, 4, 28.2956912),
}


def qn(q: float, n: int) -> float:
    """
    Local q-integer evaluator [n]_q = (q^n − q^{−n})/(q − q^{−1}) at
    arbitrary q. q_parameter.q_int is module-level (q = q_0 only); we
    need it here at the same q_0 only, so we forward to it when
    q == Q0 and otherwise compute the float form. This avoids
    duplicating the formula while keeping the function usable at
    arbitrary q for downstream sensitivity probes.
    """
    if n == 0:
        return 0.0
    # Use isclose for the fast-path detection (q == Q0 by exact
    # float equality is brittle if q is computed rather than
    # imported — per Copilot review on PR #591).
    if math.isclose(q, Q0, rel_tol=0.0, abs_tol=1e-15):
        return q_int(n)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_anchors(q: float, A: int) -> dict:
    """
    Return categorical δρ candidates, indexed by atom-mass-number A.

    The atom-mass-aware family `±([A]_q − A) / k` for small integer k
    is included here because it is structurally motivated: A counts
    the host generators in the substrate, and `[A]_q − A` is the
    leading-order substrate-fluid correction to the integer host
    count at finite q.  All other candidates are A-independent.
    """
    eta_q   = (2 * q - 1) / q ** 3                # entropy anchor
    hbar_q  = (q - 1) / q                         # q-Planck
    c_q_inv = q - 1                               # 1/c_q
    d_H_q   = (2 * q - 1) ** 2 / q ** 3           # Hausdorff dimension
    qA_minus_A = qn(q, A) - A
    return {
        "η_q":            eta_q,
        "ℏ_q":            hbar_q,
        "1/c_q":          c_q_inv,
        "d_H_q":          d_H_q,
        "[2]_q":          qn(q, 2),
        "[3]_q":          qn(q, 3),
        "[5]_q/[4]_q":    qn(q, 5) / qn(q, 4),
        "ℏ_q²":           hbar_q ** 2,
        "ℏ_q · η_q":      hbar_q * eta_q,
        "η_q²":           eta_q ** 2,
        "(1−η_q)":        1 - eta_q,
        "(q−1)·[3]_q":    (q - 1) * qn(q, 3),
        # Atom-mass-aware family (the structurally motivated A-form).
        f"([{A}]_q−{A})":           qA_minus_A,
        f"([{A}]_q−{A})/2":         qA_minus_A / 2,
        f"([{A}]_q−{A})/3":         qA_minus_A / 3,
        f"([{A}]_q−{A})/A":         qA_minus_A / A,
        f"([{A}]_q−{A})/(A−1)":     qA_minus_A / max(1, A - 1),
    }


def decomposition_row(sym: str, knot: str, rho_struct: int, A: int,
                      b_ame: float, vol_eff: float) -> dict:
    """
    Decompose a single atom's residual into δρ and test against
    pre-specified categorical q-forms.
    """
    b_pred  = rho_struct * M_E_MEV * vol_eff
    err_pct = (b_pred - b_ame) / b_ame * 100.0
    rho_tru = b_ame / (M_E_MEV * vol_eff)
    drho    = rho_tru / rho_struct - 1.0          # signed fractional deviation

    anchors = q_anchors(Q0, A)
    # For each anchor a, test δρ = ±a, δρ = ±(a − 1), and δρ = ±(a − ⌊a⌋)
    # (fractional-part removal — matches the docstring's "−⌊a⌋" notation).
    # No fitting: just record the closest match by absolute residual.
    best = []
    for label, val in anchors.items():
        for sign in (+1, -1):
            for offset_label, offset in (("",       0.0),
                                          ("−1",    1.0),
                                          ("−floor",math.floor(val))):
                cand = sign * (val - offset)
                resid = drho - cand
                best.append({
                    "form": f"{'+' if sign==1 else '-'}{label}{offset_label}",
                    "value":   cand,
                    "residual": resid,
                    "abs_resid": abs(resid),
                })
    best.sort(key=lambda r: r["abs_resid"])
    return {
        "atom":         sym,
        "knot":         knot,
        "rho_struct":   rho_struct,
        "Vol_eff":      vol_eff,
        "B_AME_MeV":    b_ame,
        "B_pred_MeV":   b_pred,
        "err_MeV":      b_pred - b_ame,
        "err_pct":      err_pct,
        "rho_true":     rho_tru,
        "delta_rho":    drho,
        "delta_rho_pct": drho * 100.0,
        "top_5_categorical_matches": best[:5],
    }


def main() -> int:
    # Instantiate WitnessBuilder up front so its `durationMs` field
    # captures the FULL run time (was wrapping at the end → measured
    # only wrap/save time ≈ 0 ms; per Copilot review on PR #591).
    from witness_base import WitnessBuilder
    builder = WitnessBuilder(
        "per-atom-rho-deviation",
        engine="python",
        output_dir=Path(__file__).parent,
    )
    builder.set_audit_only("docs/audits/2026-05-03-z-eq-n-rho-correction-finding.md")

    print("=" * 110)
    print("PER-ATOM ρ-DEVIATION DIAGNOSTIC — path to 1 ppb")
    print(f"  q₀ = {Q0:.16f}   m_e = {M_E_MEV} MeV")
    print("=" * 110)

    rows = []
    for sym, (knot, rho_struct, A, b_ame) in AME.items():
        if knot == "L6a4_x4":
            vol_eff = 4.0 * VOL_BORROMEAN_EIGHT_G
            knot_label = "4·L6a4 (magic-A)"
        else:
            vol_eff = KNOT_VOL[knot]
            knot_label = knot
        row = decomposition_row(sym, knot_label, rho_struct, A, b_ame, vol_eff)
        rows.append(row)

    # Print summary
    fmt = ("  {atom:>5} {knot:>16}  ρ_struct={rho_struct}  "
           "B_AME={B_AME:>9.4f} MeV  err={err_pct:+6.3f}%  "
           "ρ_true={rho_true:>7.4f}  δρ={delta_rho_pct:+6.3f}%")
    for r in rows:
        print(fmt.format(
            atom=r["atom"], knot=r["knot"], rho_struct=r["rho_struct"],
            B_AME=r["B_AME_MeV"], err_pct=r["err_pct"],
            rho_true=r["rho_true"], delta_rho_pct=r["delta_rho_pct"],
        ))

    # Categorical-match summary
    print("-" * 110)
    print("Closest categorical q-form for δρ (lowest |residual| per atom):")
    for r in rows:
        m0 = r["top_5_categorical_matches"][0]
        ok = "✓" if abs(m0["residual"]) < 1e-3 else "✗"
        print(f"  {r['atom']:>5} δρ = {r['delta_rho']:+.6f}  vs  "
              f"{m0['form']:>16} = {m0['value']:+.6f}  "
              f"resid = {m0['residual']:+.6f}  {ok}")

    # Verdict
    print("-" * 110)
    n_matched = sum(
        1 for r in rows
        if abs(r["top_5_categorical_matches"][0]["residual"]) < 1e-3
    )
    print(f"Atoms with δρ matching a pre-specified categorical q-form "
          f"(|residual| < 10⁻³): {n_matched} / {len(rows)}")
    if n_matched == 0:
        print("  → CLEAN NEGATIVE RESULT: the residuals are NOT explained by "
              "any of the standard q-anchors at 10⁻³ precision.")
        print("  → Implication: the per-atom δρ correction has structure "
              "BEYOND the substrate-fluid q-form alone (e.g. depends on the "
              "knot's Hecke representation, not just q itself).")
    elif n_matched < len(rows):
        print(f"  → PARTIAL: {n_matched} atoms align; "
              "remaining atoms expose where the q-anchor list is incomplete.")
    else:
        print("  → FULL MATCH (unexpected): every atom's δρ is given by a "
              "single categorical q-form — write up immediately.")

    # ────────────────────────────────────────────────────────────
    # Z=N propagation test
    # ────────────────────────────────────────────────────────────
    # Empirical finding: for Z=N atoms, δρ = -([A]_q - A) / ρ_struct
    # closes the residual by ~2 orders. Test propagation through the
    # α-cluster formula B(nα) = n·B(⁴He) + C(n,2)·c_αα.
    print()
    print("=" * 110)
    print("Z=N PROPAGATION TEST: corrected B(⁴He) → α-cluster downstream")
    print("=" * 110)

    q4_minus_4 = qn(Q0, 4) - 4
    correction_4He = 1.0 - q4_minus_4 / 2.0          # = ρ_true / 2
    B_4He_corr = 2 * M_E_MEV * 4 * VOL_BORROMEAN_EIGHT_G * correction_4He
    C_ALPHA = M_E_MEV * VOL_7_SQ_1               # 2.4270 MeV (= m_e·Vol(7²_1))

    ALPHA_CHAIN = [
        # (sym, n_alpha, n_pairs, B_AME_MeV)
        ("8Be",   2,  1,  56.49951),
        ("12C",   3,  3,  92.16175),
        ("16O",   4,  6, 127.61929),
        ("20Ne",  5, 10, 160.64486),
        ("24Mg",  6, 15, 198.25690),
        ("40Ca", 10, 45, 342.05212),
    ]
    propagation_rows = []
    print(f"  B(⁴He)_corr = {B_4He_corr:.6f} MeV  (was 29.9557; AME 28.2957)")
    print(f"  c_αα        = {C_ALPHA:.6f} MeV  (= m_e·Vol(7²_1))")
    print()
    print(f"  {'atom':>5}  {'AME':>10}  {'pred(orig)':>11}  err%(orig)  "
          f"{'pred(corr)':>11}  err%(corr)")
    print("  " + "-" * 100)
    for sym, n_a, n_p, B_AME in ALPHA_CHAIN:
        B_orig = n_a * (2 * M_E_MEV * 4 * VOL_BORROMEAN_EIGHT_G) + n_p * C_ALPHA
        B_corr = n_a * B_4He_corr + n_p * C_ALPHA
        err_o = (B_orig - B_AME) / B_AME * 100
        err_c = (B_corr - B_AME) / B_AME * 100
        propagation_rows.append({
            "atom": sym,
            "n_alpha": n_a, "n_pairs": n_p,
            "B_AME_MeV": B_AME,
            "B_pred_orig_MeV": B_orig,
            "err_pct_orig": err_o,
            "B_pred_corr_MeV": B_corr,
            "err_pct_corr": err_c,
            "improvement_factor": abs(err_o) / abs(err_c) if err_c else None,
        })
        print(f"  {sym:>5}  {B_AME:>10.4f}  {B_orig:>11.4f}  {err_o:+8.3f}%  "
              f"{B_corr:>11.4f}  {err_c:+8.3f}%")

    print("-" * 110)
    n_improved = sum(
        1 for r in propagation_rows
        if abs(r["err_pct_corr"]) < abs(r["err_pct_orig"])
    )
    print(f"  Atoms improved by Z=N correction propagation: "
          f"{n_improved} / {len(propagation_rows)}")

    # Witness
    out = {
        "computation":   "per-atom-rho-deviation",
        "computedAt":    datetime.now(timezone.utc).isoformat(),
        "description":   ("Per-atom ρ-deviation decomposition for the "
                          "hard-coded light-atom probe {²H, ³H, ³He, ⁴He}. "
                          "Computes ρ_true = B_AME/(m_e·Vol_hyp(K)) and "
                          "tests δρ = ρ_true/ρ_struct − 1 against "
                          "pre-specified categorical q-forms (no fitting), "
                          "then propagates the Z=N correction through the "
                          "α-cluster chain {⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca}."),
        "parameters": {
            "q_0": Q0,
            "m_e_MeV": M_E_MEV,
            "VOL_BORROMEAN_EIGHT_G": VOL_BORROMEAN_EIGHT_G,
            "VOL_BORROMEAN_SNAPPY":  VOL_BORROMEAN_SNAPPY,
            "KNOT_VOL": KNOT_VOL,
            "VOL_7_SQ_1": VOL_7_SQ_1,
        },
        "rows":          rows,
        "z_eq_n_propagation": {
            "B_4He_corrected": B_4He_corr,
            "correction_4He_factor": correction_4He,
            "c_alpha_MeV": C_ALPHA,
            "rows": propagation_rows,
            "n_improved": n_improved,
            "n_total": len(propagation_rows),
        },
        "summary": {
            "n_atoms": len(rows),
            "n_categorical_matches_lt_1e3": n_matched,
            "z_eq_n_correction_form": "δρ = -([A]_q − A) / ρ_struct",
            "matched_atoms": [
                r["atom"] for r in rows
                if abs(r["top_5_categorical_matches"][0]["residual"]) < 1e-3
            ],
        },
    }
    # Save via the builder created at start of main(). Set the
    # `description` through the builder API (rather than passing it
    # as extra) so the structured fields keep wrap_legacy's order
    # (description BEFORE auditOnly) — otherwise the drift check on
    # the witness pipeline trips on a positional shift.
    builder.set_description(out.pop("description", ""))
    out["computation"] = "per-atom-rho-deviation"
    out_path = builder.save(extra=out)
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
