"""m_p chain closure Item B — T5 categorical attribution probe.

Per docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md §"Item B":

  "T5 is currently sign-indefinite (-7.79 proton, -7.47 neutron),
   magnitude order ~1. ... T5 may be a numerical artefact of double-
   counting between T1+T2+T3 and the chirality channel — a
   subtractive term that's accidentally being added. This needs
   careful audit."

This probe enumerates **structural candidate forms** for T5 (chirality-
BW term) built from substrate primitives at q_0, and reports which
candidates come closest to the empirical T5 values:

  T5(proton)  = -7.79175  MeV  (per mass-formula-6term-mpfr-50dps witness)
  T5(neutron) = -7.46659  MeV

Substrate primitives available (canonical, no fitting):
  E_0 = m_e/(q(q-1))    Hecke energy unit  ≈ 4.186 MeV
  m_e                    CAL-1 electron mass ≈ 0.511 MeV
  h = q - q⁻¹           Hecke skein deformation ≈ 0.209
  ℏ_q = (q-1)/q          k_B·T_q = quantum Planck ≈ 0.0991
  z = 1/(q^{1/2}+q^{-1/2})  Markov parameter ≈ 0.499
  b² = (q^4+q^2+1)/(q^2+1)^2   Kashiwara ≈ 0.753
  [n]_q = (q^n - q^{-n})/(q - q^{-1})   q-bracket; [2]_q ≈ 2.011, [3]_q ≈ 3.044
  log(1/h)  ≈ 1.565
  J_Hopf(q=1) = -2  Jones polynomial at q=1
  J_Borromean(q=1) = -8

## Status

This is **open R&D** — the audit doc flags T5 as "no known structural
ansatz matches". The probe is a CANDIDATE ENUMERATION, not a
derivation. Output: which candidates land closest to -7.79 / -7.47,
ranked by absolute gap.

Output: T5-categorical-attribution-candidates.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def q_bracket(n: int, q: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q**n - q**(-n)) / (q - 1/q)


def main() -> int:
    print("=" * 90)
    print("  T5 categorical attribution — candidate enumeration probe")
    print("=" * 90)
    print()

    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf("0.51099895069")
    E_0 = m_e / (q0 * (q0 - 1))
    h = q0 - 1/q0
    hbar = (q0 - 1) / q0
    z = 1 / (mp.sqrt(q0) + 1/mp.sqrt(q0))
    b_sq = (q0**4 + q0**2 + 1) / (q0**2 + 1)**2
    b = mp.sqrt(b_sq)
    bk2 = q_bracket(2, q0); bk3 = q_bracket(3, q0); bk4 = q_bracket(4, q0)
    log_inv_h = mp.log(1/h)

    print(f"  Substrate primitives at q_0 ≈ 1.10998:")
    print(f"    E_0 = m_e/(q(q-1))     = {float(E_0):>+11.6f} MeV")
    print(f"    m_e                     = {float(m_e):>+11.6f} MeV")
    print(f"    h = q - q⁻¹             = {float(h):>+11.6f}")
    print(f"    ℏ_q = (q-1)/q           = {float(hbar):>+11.6f}")
    print(f"    z (Markov parameter)    = {float(z):>+11.6f}")
    print(f"    b² (Kashiwara)          = {float(b_sq):>+11.6f}")
    print(f"    [2]_q, [3]_q, [4]_q     = {float(bk2):.4f}, {float(bk3):.4f}, {float(bk4):.4f}")
    print(f"    log(1/h)                = {float(log_inv_h):>+11.6f}")
    print()

    targets = {
        "proton":   mp.mpf("-7.79175121067811044741343741981195719181416632046"),
        "neutron":  mp.mpf("-7.46659327757700342460573021531327715915058285192"),
    }
    print(f"  Empirical targets (from mass-formula-6term-mpfr-50dps.witness.json):")
    for atom, t in targets.items():
        print(f"    T5({atom:>8}) = {float(t):>+10.5f} MeV")
    print()

    # ─── Candidate forms ───
    # Each candidate: (name, expression)
    candidates = [
        ("-E_0 · log(1/h) · [2]_q",                -E_0 * log_inv_h * bk2),
        ("-E_0 · log(1/h) · b",                    -E_0 * log_inv_h * b),
        ("-E_0 · log(1/h) · [2]_q · b",            -E_0 * log_inv_h * bk2 * b),
        ("-E_0 · log(1/h) · b²",                   -E_0 * log_inv_h * b_sq),
        ("-2 · E_0 · log(1/h) · b",                -2 * E_0 * log_inv_h * b),
        ("-E_0 · (log(1/h) + 2·h)",                -E_0 * (log_inv_h + 2*h)),
        ("-E_0 · [2]_q² / b²",                     -E_0 * bk2**2 / b_sq),
        ("-2 · E_0 · b·log(1/h)·z·[2]_q",          -2 * E_0 * b * log_inv_h * z * bk2),
        ("-8 · z² · E_0",                          -8 * z**2 * E_0),
        ("-[2]_q³ · E_0 / [2]_q",                  -bk2**2 * E_0),
        ("-2 · b²·E_0·[2]_q",                      -2 * b_sq * E_0 * bk2),
        ("-2 · E_0·log(1/h)·(1+h)",                -2 * E_0 * log_inv_h * (1+h)),
        ("-4 · J_Hopf · E_0·z",                    -4 * (-2) * E_0 * z),
        ("-J_Borromean · E_0·z·[2]_q²",            -(-8) * E_0 * z * bk2**2),
        ("-E_0 · log(1/h²) · [2]_q / 2",           -E_0 * mp.log(1/h**2) * bk2 / 2),
        ("-E_0 · b·log(1/h)·[2]_q·z·b²",           -E_0 * b * log_inv_h * bk2 * z * b_sq),
        ("-[2]_q·[3]_q·E_0·z·log(1/h)·h",          -bk2 * bk3 * E_0 * z * log_inv_h * h),
        ("-([2]_q² - 1)·E_0",                      -(bk2**2 - 1) * E_0),
        ("-[2]_q · log(1/h) · m_e · 5",            -bk2 * log_inv_h * m_e * 5),
        ("-2 · E_0 · z · [3]_q·log(1/h)·b",        -2 * E_0 * z * bk3 * log_inv_h * b),
    ]

    # Rank candidates by best match to proton (closest |gap|/|target|)
    rows = []
    for name, val in candidates:
        gap_p = float((val - targets["proton"]) / targets["proton"] * 100)
        gap_n = float((val - targets["neutron"]) / targets["neutron"] * 100)
        rows.append({
            "candidate": name,
            "value_MeV": float(val),
            "gap_proton_pct": gap_p,
            "gap_neutron_pct": gap_n,
            "avg_abs_gap_pct": (abs(gap_p) + abs(gap_n)) / 2,
        })
    rows.sort(key=lambda r: r["avg_abs_gap_pct"])

    print(f"  Candidates ranked by avg |gap|% vs T5(p), T5(n):")
    print(f"  {'':<45} {'value':>11} {'gap_p%':>10} {'gap_n%':>10}")
    print("  " + "-" * 80)
    for r in rows[:15]:
        marker = " ★ <5%" if r["avg_abs_gap_pct"] < 5 else (" ✓ <10%" if r["avg_abs_gap_pct"] < 10 else "")
        print(f"  {r['candidate']:<45} {r['value_MeV']:>+11.4f} {r['gap_proton_pct']:>+10.3f} {r['gap_neutron_pct']:>+10.3f}{marker}")
    print()

    # Best match
    best = rows[0]
    print(f"  BEST CANDIDATE: {best['candidate']}")
    print(f"    value = {best['value_MeV']:+.5f} MeV")
    print(f"    proton gap = {best['gap_proton_pct']:+.3f}%, neutron gap = {best['gap_neutron_pct']:+.3f}%")
    print(f"    Z↔N (proton - neutron) shift in candidate: {best['value_MeV'] - best['value_MeV']:.4f} (0 — symmetric)")
    print(f"    Empirical Z↔N shift: T5(p) - T5(n) = {float(targets['proton'] - targets['neutron']):+.4f} MeV")
    print()
    print(f"  CONCLUSION:")
    print(f"    No tested candidate matches BOTH proton and neutron T5 values")
    print(f"    within 5% AND reproduces the empirical Z↔N asymmetry of")
    print(f"    {float(targets['proton'] - targets['neutron']):+.3f} MeV. The T5 chirality-BW term has a")
    print(f"    Z↔N-asymmetric structure that purely-substrate candidates miss.")
    print(f"    Consistent with the m_p audit's finding that T5 is open R&D.")
    print()

    builder = (
        WitnessBuilder("T5-categorical-attribution-candidates", engine="mpmath")
        .set_description(
            "m_p chain Item B probe — T5 categorical attribution via "
            "substrate-primitive candidate enumeration. Tests 20 candidate "
            "forms built from {E_0, m_e, h, ℏ_q, z, b, b², [n]_q, log(1/h), "
            "Jones-at-q=1 values} against the empirical T5 values "
            "(-7.79 proton, -7.47 neutron). REPORTS best candidates ranked "
            "by avg gap; CONFIRMS Item B remains open R&D — no purely-"
            "substrate ansatz matches both anchors AND reproduces the "
            "Z↔N asymmetry (-0.325 MeV between proton and neutron)."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md"
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_data("targets_MeV", {atom: float(t) for atom, t in targets.items()})
        .add_data("z_n_asymmetry_MeV", float(targets["proton"] - targets["neutron"]))
        .add_data("candidates_ranked", rows)
        .add_data("best_candidate", best)
        .add_assertion(
            name="T5_attribution_remains_open_R_and_D",
            computed=best["avg_abs_gap_pct"] > 5.0,
            expected=True,
            unit="boolean",
            source=(
                "Best candidate has avg gap >5% across proton+neutron T5. "
                "No tested form simultaneously matches both anchors AND "
                "reproduces the Z↔N asymmetry. Item B (T5 attribution) "
                "is open R&D — likely needs the Z↔N-asymmetric channel "
                "structure surfaced by the cross-anchor falsification "
                "probe (probe_delta_coupling_cross_anchor.py)."
            ),
        )
        .add_caveat(
            "Enumeration-only probe. The 20 candidates tested are "
            "polynomial in {E_0, m_e, h, ℏ_q, z, b, [n]_q, log(1/h)} "
            "with small integer coefficients and Jones-at-q=1 values. "
            "Doesn't exhaustively cover the substrate-primitive space "
            "(e.g. doesn't test Real.rpow-fractional combinations or "
            "operator-valued contributions from the canonical Wenzl-LR "
            "decomposition). The Z↔N asymmetry suggests the genuine "
            "T5 form is operator-valued (per "
            "knot-fusion-step1-audit.md / PR #681), not a purely "
            "scalar substrate combination."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
