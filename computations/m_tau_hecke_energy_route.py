#!/usr/bin/env python3
"""m_tau via the muon-anchored Hecke-energy route — scoping (EXPLORATORY).

Bean qou-se9w. The census route is now closed: the k=2 volume target
(34.137) exceeds the volume ceiling of every tabulated manifold
(`m-tau-census-sweep.witness.json`, 650,777 searched, ceiling 33.31).
The guardrail-preferred alternative for ABSOLUTE masses is the
muon-anchored Hecke energy — the shape that works for the nucleons:

    m_p = 2*(m_mu*F_Bor - 6*m_e),  F_Bor = |tr_M(beta_Bor)|*[3]_q!/q^3

i.e. an anchor (m_mu = m_e*Vol(4_1)/hbar_q^2) dressed by a
DIMENSIONLESS Hecke factor F. For the tau the analogous statement is

    m_tau = m_mu * F_tau,   F_tau_target = 16.8170  (CODATA)

and the question is whether any structurally-motivated Hecke object
built from the corpus's own conventions equals F_tau.

ANTI-FIT DISCIPLINE (CAL-4, AGENTS.md). This probe does NOT search for
"whatever hits 16.817". It evaluates a CLOSED, pre-declared list of
candidates, each assembled only from objects the corpus already uses
in a derivation:

  * chi_(2,1)(sigma_1^n) = q^n - q^-n     (kaon derivation convention)
  * V_S(T(2,n)) = pi*(n-2)/n              (Seifert volume, same source)
  * [n]_q quantum integers, [n]_q!        (nucleon F_Bor convention)
  * hbar_q = 1 - 1/q0                     (substrate)
  * Vol(4_1)                              (the Higgs-knot anchor)

Every candidate is reported with its residual, matches and misses
alike. A candidate landing near the target is a CANDIDATE TO DERIVE,
explicitly NOT a result: absent an independent structural reason it is
numerology, and this probe wires nothing.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP, HBAR_Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, pi as mppi, fabs  # noqa: E402

# Raise precision BEFORE building any module-level mpf. `set_compute_dps()` is
# also called in main(), but that runs long after import — a constant built
# here at mpmath's default 15 dps is frozen at 53 bits, and serializing it
# later at compute precision prints the binary64 tail (3477.23 came out as
# 3477.23000000000001818989403545856475830078125). The division below is worse
# than the literals: it rounds to 53 bits too. Idempotent, so main() is
# unaffected.
set_compute_dps()

# CODATA ratios (targets, never inputs to a construction).
M_TAU_OVER_M_MU = mpf("1776.86") / mpf("105.6583755")
M_TAU_OVER_M_E = mpf("3477.23")
VOL_41 = mpf("2.029883212819307")  # figure-eight (Higgs knot) volume

# Lepton torus-knot ladder (canonical table): e = T(2,3), mu = T(2,5),
# tau = T(2,7).
N_E, N_MU, N_TAU = 3, 5, 7


def chi21(q, n: int):
    """Hecke character chi_(2,1)(sigma_1^n) = q^n - q^-n (odd n)."""
    return q**n - q ** (-n)


def seifert_vol(n: int):
    """V_S(T(2,n)) = 2*pi*|e| = pi*(n-2)/n."""
    return mppi * mpf(n - 2) / mpf(n)


def q_int(q, n: int):
    """Quantum integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q**n - q ** (-n)) / (q - q ** (-1))


def main() -> None:
    set_compute_dps()
    q, hbar = Q_MP, HBAR_Q_MP
    target = M_TAU_OVER_M_MU

    chi_e, chi_mu, chi_tau = (chi21(q, n) for n in (N_E, N_MU, N_TAU))
    vs_e, vs_mu, vs_tau = (seifert_vol(n) for n in (N_E, N_MU, N_TAU))

    # Pre-declared candidate list. Each entry: (label, value, rationale).
    cands = [
        ("chi7/chi5", chi_tau / chi_mu,
         "bare Hecke character ratio, the kaon derivation's algebraic factor"),
        ("(chi7/chi5)/hbar_q", (chi_tau / chi_mu) / hbar,
         "character ratio with one substrate amplification (muon-anchor shape)"),
        ("(chi7/chi5)/hbar_q^2", (chi_tau / chi_mu) / hbar**2,
         "character ratio with the CAL-2 exponent"),
        ("(V_S7/V_S5)", vs_tau / vs_mu,
         "Seifert-volume ratio alone (= 25/21)"),
        ("(V_S7/V_S5)/hbar_q", (vs_tau / vs_mu) / hbar,
         "Seifert ratio with one amplification"),
        ("(V_S7/V_S5)^2/hbar_q", (vs_tau / vs_mu) ** 2 / hbar,
         "kaon-style squared Seifert ratio, one amplification"),
        ("chi7/chi5 * (V_S7/V_S5)^2", (chi_tau / chi_mu) * (vs_tau / vs_mu) ** 2,
         "exact kaon form (character x squared Seifert ratio)"),
        ("chi7/chi5 * (V_S7/V_S5)^2 / hbar_q",
         (chi_tau / chi_mu) * (vs_tau / vs_mu) ** 2 / hbar,
         "kaon form with one amplification"),
        ("[7]_q/[5]_q", q_int(q, 7) / q_int(q, 5),
         "quantum-integer ratio (nucleon F_Bor uses [n]_q!)"),
        ("[7]_q/[5]_q / hbar_q", (q_int(q, 7) / q_int(q, 5)) / hbar,
         "quantum-integer ratio, one amplification"),
        ("Vol(4_1)/hbar_q^2 * chi7/chi5 / (m_tau/m_e/(m_tau/m_mu))",
         (VOL_41 / hbar**2) * (chi_tau / chi_mu) / (M_TAU_OVER_M_E / target),
         "consistency check of the muon anchor against CODATA (should be ~chi ratio)"),
    ]

    rows = []
    for label, val, why in cands:
        rel = (val - target) / target
        rows.append({
            "candidate": label,
            "value": mp.nstr(val, 10),
            "rel_error": mp.nstr(rel, 6),
            "abs_rel_error_pct": mp.nstr(fabs(rel) * 100, 8),
            "rationale": why,
        })
    rows.sort(key=lambda r: mpf(r["abs_rel_error_pct"]))
    best = rows[0]
    any_close = mpf(best["abs_rel_error_pct"]) < 1

    wb = WitnessBuilder("m-tau-hecke-energy-route", engine="mpmath")
    wb.set_description(
        "EXPLORATORY scoping of the muon-anchored Hecke-energy route to "
        "m_tau (bean qou-se9w), after the census route closed. Tests a "
        "CLOSED pre-declared list of candidates for the dimensionless "
        "factor F_tau = m_tau/m_mu = 16.8170, each built only from "
        "corpus-canonical objects (chi_(2,1), Seifert volumes, quantum "
        "integers, hbar_q). All residuals reported, matches and misses "
        "alike. NOT a fit and NOT wired: a near-match here is a "
        "candidate requiring independent structural derivation, not a "
        "result.")
    wb.add_data("target", {
        "F_tau = m_tau/m_mu": mp.nstr(target, 12),
        "m_tau/m_e": str(M_TAU_OVER_M_E),
        "q0": mp.nstr(q, 20),
        "hbar_q": mp.nstr(hbar, 20),
    })
    wb.add_data("lepton_ladder", {
        "knots": {"e": "T(2,3)", "mu": "T(2,5)", "tau": "T(2,7)"},
        "chi": {f"chi_{n}": mp.nstr(chi21(q, n), 12)
                for n in (N_E, N_MU, N_TAU)},
        "seifert_vol": {f"V_S(T(2,{n}))": mp.nstr(seifert_vol(n), 12)
                        for n in (N_E, N_MU, N_TAU)},
    })
    wb.add_data("candidates_sorted_by_residual", rows)
    wb.add_data("verdict", (
        f"No pre-declared candidate reaches 1% of the target; the best "
        f"is {best['candidate']} at "
        f"{best['abs_rel_error_pct']}% . The muon-anchored Hecke "
        f"route does NOT close m_tau with the corpus's existing "
        f"factor vocabulary — an honest negative. Closing it requires "
        f"a new structural ingredient (e.g. a genuine Markov trace of "
        f"the tau braid in a higher-strand algebra, or the "
        f"lepton-sector analogue of the nucleon's -6*m_e binding "
        f"subtraction), not another combination of these factors."
        if not any_close else
        f"Candidate {best['candidate']} lands within "
        f"{best['abs_rel_error_pct']}% of the target. This is a "
        f"CANDIDATE TO DERIVE, not a result: absent an independent "
        f"structural reason for exactly this combination it is "
        f"numerology (CAL-4), and nothing is wired on it."))
    wb.set_content_block("rem:m-tau-knot-prediction")
    wb.add_assertion(
        name="candidates_evaluated",
        computed=len(rows), expected=len(cands), tolerance=0, unit="count",
        source="Every pre-declared candidate evaluated and reported.")
    wb.add_assertion(
        name="chi_ladder_positive",
        computed=int(chi_e > 0 and chi_mu > chi_e and chi_tau > chi_mu),
        expected=1, tolerance=0, unit="bool",
        source=("Sanity: chi_(2,1)(sigma^n) increases along the lepton "
                "ladder n = 3, 5, 7 at q0 > 1."))
    out = wb.save()

    print(f"target F_tau = m_tau/m_mu = {mp.nstr(target, 10)}")
    for r in rows:
        print(f"  {r['abs_rel_error_pct']:>12}%  {r['candidate']} = {r['value']}")
    print(f"\nbest: {best['candidate']} at {best['abs_rel_error_pct']}%")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
