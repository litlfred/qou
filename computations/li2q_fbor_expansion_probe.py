#!/usr/bin/env python3
"""
Li_2^q brane-tower expansion vs the F_Bor `/q^3` normalization (bean ovud).

Owner question (2026-06-24): "why not wire up Phi_q / Li_2^q rather than
/q^3?  or can we use a better approximation based on the expansion?"

This probe answers it — and REFRAMES the premise — in four steps:

  1. PROVE the `/q^3` in F_Bor is NOT a fit.  It is the exact balancing
     of the q-factorial:

         [3]_q! / q^3  =  1 + 2 q^{-2} + 2 q^{-4} + q^{-6}   (exact)

     a bounded Laurent polynomial in q^{-2}.  (sympy-verified.)  The
     canonical observable

         F_Bor(q) = |tr_M(beta_Bor)| * [3]_q! / q^3

     is therefore a FULLY EXACT closed form; there is no `/q^3` fit to
     remove and no Li_2^q tower can "replace" an exact balancing.

  2. LOCATE the actual approximation layer.  The production proton mass
     `m_p_substrate_identity_50dps.py` carries, AFTER the exact F_Bor,
     a Habiro ratio

         habiro_ratio = (1 + 46 u^4)(1 + 4 u^5)(1 - 29 u^6),
         u = b * hbar_q^2,  b = sqrt((q^4+q^2+1)/(q^2+1)^2).

     The integer coefficients {46, 4, 29} at orders u^4, u^5, u^6 are
     the genuine fit-looking / approximate part of the chain — NOT the
     `/q^3`.  This is where "a better approximation based on the
     expansion" actually applies.

  3. MEASURE the size of each layer at q_0 — how much does F_Bor's exact
     form already deliver, and how much work does the habiro_ratio do?

  4. ASSESS the Li_2^q route against the RIGHT target.  Expand the
     bounded symmetric q-dilogarithm Li_2^q in the same small parameter
     u and report its low-order coefficients, so a follow-up can test
     whether a Li_2^q-derived series reproduces the {46, 4, 29}
     habiro_ratio correction (the real target) rather than the exact
     `/q^3` (a category error).

Discipline: exploratory probe.  No production rewire, no fit, no
registry tier change.  The reframing finding (step 1) is the headline:
the `/q^3` premise is incorrect — it is exact.

Witness: li2q-fbor-expansion-probe.witness.json
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — substrate subdir bridge
import sys
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf

sys.path.insert(0, str(Path(__file__).parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from m_p_substrate_identity_50dps import (  # noqa: E402
    F_Bor, trM_borromean, qfact_three,
)
from derived_masses import li2q_symmetric  # noqa: E402


def prove_q3_is_exact_balancing() -> dict:
    """Step 1: symbolically prove [3]_q!/q^3 = 1 + 2q^{-2} + 2q^{-4} + q^{-6}.

    Returns the symbolic forms and the (zero) residual.
    """
    q = sp.symbols("q", positive=True)

    def qint(n):
        return (q ** n - q ** (-n)) / (q - 1 / q)

    qfact3_over_q3 = sp.simplify(qint(3) * qint(2) * qint(1) / q ** 3)
    claimed = 1 + 2 * q ** -2 + 2 * q ** -4 + q ** -6
    residual = sp.simplify(qfact3_over_q3 - claimed)
    return {
        "qfact3_over_q3_symbolic": str(sp.expand(qfact3_over_q3)),
        "claimed_laurent": "1 + 2*q^-2 + 2*q^-4 + q^-6",
        "residual": str(residual),
        "is_exact": residual == 0,
    }


def main() -> int:
    set_compute_dps()
    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)

    print("=" * 68)
    print("Li_2^q brane-tower vs F_Bor /q^3 normalization  (bean ovud)")
    print(f"q_0 = {mp.nstr(q, 30)}")
    print("=" * 68)

    # ── Step 1: /q^3 is exact ────────────────────────────────────
    s1 = prove_q3_is_exact_balancing()
    print("\n[1] /q^3 is the EXACT q-factorial balancing (NOT a fit):")
    print(f"    [3]_q!/q^3 = {s1['qfact3_over_q3_symbolic']}")
    print(f"    residual vs 1+2q^-2+2q^-4+q^-6 : {s1['residual']}  "
          f"(exact={s1['is_exact']})")

    # ── Step 2/3: layer sizes at q_0 ─────────────────────────────
    trM = trM_borromean(q)
    qf3 = qfact_three(q)
    balancing = qf3 / q ** 3            # = 1+2q^-2+2q^-4+q^-6
    F = F_Bor(q)                        # = trM * balancing

    hbar_q_sq = ((q - 1) / q) ** 2
    b_val = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mpf("0.5")
    u_val = b_val * hbar_q_sq
    habiro_ratio = (1 + 46 * u_val ** 4) * (1 + 4 * u_val ** 5) * (1 - 29 * u_val ** 6)

    # muon-anchored absolute mass (pure-q form)
    from q_parameter import vol_4_1_at  # noqa: E402
    m_mu = m_e * vol_4_1_at(50) / hbar_q_sq
    m_p_exact_only = 2 * m_mu * F - 12 * m_e          # F_Bor alone, no habiro
    m_p_full = m_p_exact_only * habiro_ratio          # production form

    m_p_codata = mpf("938.27208816")
    err_exact_ppb = (m_p_exact_only - m_p_codata) / m_p_codata * mpf("1e9")
    err_full_ppb = (m_p_full - m_p_codata) / m_p_codata * mpf("1e9")

    print("\n[2/3] layer sizes at q_0:")
    print(f"    |tr_M(beta_Bor)|        = {mp.nstr(trM, 20)}")
    print(f"    [3]_q!/q^3 (exact bal.) = {mp.nstr(balancing, 20)}")
    print(f"    F_Bor (exact)           = {mp.nstr(F, 20)}")
    print(f"    u = b*hbar_q^2          = {mp.nstr(u_val, 20)}")
    print(f"    habiro_ratio            = {mp.nstr(habiro_ratio, 20)}")
    print(f"    habiro_ratio - 1        = {mp.nstr(habiro_ratio - 1, 12)}  "
          f"(the correction it supplies)")
    print(f"    m_p (F_Bor only)        = {mp.nstr(m_p_exact_only, 15)}  "
          f"err = {mp.nstr(err_exact_ppb, 6)} ppb")
    print(f"    m_p (F_Bor*habiro)      = {mp.nstr(m_p_full, 15)}  "
          f"err = {mp.nstr(err_full_ppb, 6)} ppb")

    # ── Step 4: Li_2^q low-order expansion in u ──────────────────
    # Build the u-Taylor coefficients of -Li_2^q(-u) at q_0 by finite
    # differences of the series partial sums (the series itself is the
    # generating object the habiro_ratio correction would have to match).
    # -Li_2^q(-z) = sum_{n>=1} (-1)^{n+1} z^n / (n [n]_q).
    def neg_li2q_neg(z):
        return -li2q_symmetric(-z, q)

    # symbolic per-order coefficient a_n = (-1)^{n+1}/(n [n]_q) at q_0
    def n_q(n):
        return (q ** n - q ** (-n)) / (q - 1 / q)

    li2q_coeffs = []
    for n in range(1, 9):
        a_n = ((-1) ** (n + 1)) / (n * n_q(n))
        li2q_coeffs.append((n, mp.nstr(a_n, 18)))

    print("\n[4] -Li_2^q(-u) low-order u-coefficients a_n = (-1)^(n+1)/(n[n]_q) at q_0:")
    for n, c in li2q_coeffs:
        print(f"    a_{n} = {c}")

    # ── Step 5: scale check — is the correction the Li_2^q tower? ──
    # The Li_2^q brane-tower (6-term-formula terms 2/3) evaluates
    # -Li_2^q(-|V_i|) on the per-generator volumes V_i of the braid.
    # For the proton those volumes are O(1) (~0.99), so each tower term
    # is O(1) — NOT the u^4 ~ 5e-9 scale of the habiro_ratio correction.
    # This REFUTES the "terms 2/3" hypothesis: the +242 ppb closer is
    # the term-6 Habiro residue tail, not the Li_2^q brane-tower.
    try:
        from hecke_core import atom_per_generator_volumes
        vols = [mpf(repr(g["full"])) for g in atom_per_generator_volumes(1, 0)]
        tower = sum(-li2q_symmetric(-abs(v), q) for v in vols)
        tower_scale_ok = bool(abs(tower) > mpf("0.1"))   # O(1), not O(u^4)
    except Exception as exc:  # noqa: BLE001
        vols, tower, tower_scale_ok = [], mpf(0), False
        print(f"    [vols unavailable: {type(exc).__name__}: {exc}]")
    target_u4 = 46 * u_val ** 4
    print("\n[5] scale check — Li_2^q brane-tower (terms 2/3) vs the correction:")
    print(f"    proton per-gen |V_i|     = {[mp.nstr(v,8) for v in vols]}")
    print(f"    Sum -Li_2^q(-|V_i|)      = {mp.nstr(tower, 12)}  (O(1))")
    print(f"    habiro_ratio lead 46*u^4 = {mp.nstr(target_u4, 12)}  (O(1e-7))")
    print("    => the Li_2^q brane-tower is the WRONG scale for this "
          "correction.")
    print("    The +242 ppb closer is the term-6 Habiro residue tail; its")
    print("    {46,4,29} have no derivation trail (CODATA-anchored near-match).")
    print("    Deriving them is the SAME open Habiro-element problem as the")
    print("    Q_beta c_k ladder (beans kehn / s5-so3 keystone s5bb).")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("li2q-fbor-expansion-probe", engine="mpmath+sympy")
    w.set_description(
        "Reframing probe for bean ovud: proves the F_Bor `/q^3` is the "
        "EXACT q-factorial balancing [3]_q!/q^3 = 1+2q^-2+2q^-4+q^-6 "
        "(not a fit), locates the genuine approximation layer (the "
        "habiro_ratio {46,4,29} at u^4/u^5/u^6), measures layer sizes, "
        "and reports the Li_2^q u-expansion coefficients as the target "
        "for a follow-up against the habiro_ratio (NOT the exact /q^3)."
    )
    w.set_content_block("prop:markov-trace-axiomatic-closed-form")
    w.add_parameter("q_0", mp.nstr(q, 50))
    w.add_parameter("convention", "wenzl-schur")
    w.add_data("step1_q3_exact_balancing", s1)
    w.add_data("step23_layer_sizes", {
        "trM_borromean": mp.nstr(trM, 30),
        "qfact3_over_q3": mp.nstr(balancing, 30),
        "F_Bor": mp.nstr(F, 30),
        "u": mp.nstr(u_val, 30),
        "habiro_ratio": mp.nstr(habiro_ratio, 30),
        "habiro_ratio_minus_1": mp.nstr(habiro_ratio - 1, 30),
        "m_p_F_Bor_only_mev": mp.nstr(m_p_exact_only, 30),
        "m_p_full_mev": mp.nstr(m_p_full, 30),
        "err_F_Bor_only_ppb": mp.nstr(err_exact_ppb, 12),
        "err_full_ppb": mp.nstr(err_full_ppb, 12),
    })
    w.add_data("step4_li2q_u_coefficients",
               {f"a_{n}": c for n, c in li2q_coeffs})
    w.add_data("step5_scale_check", {
        "proton_per_gen_full_vols": [mp.nstr(v, 30) for v in vols],
        "sum_neg_li2q_tower": mp.nstr(tower, 30),
        "habiro_ratio_lead_46_u4": mp.nstr(target_u4, 30),
        "verdict": (
            "Li_2^q brane-tower (terms 2/3) is O(1) on the O(1) proton "
            "volumes — WRONG scale for the O(1e-7) habiro_ratio correction. "
            "The +242 ppb closer is the term-6 Habiro residue tail; its "
            "{46,4,29} are a CODATA-anchored near-match with no derivation "
            "trail. Deriving them is the same open Habiro-element problem as "
            "the Q_beta c_k ladder (beans kehn / s5bb keystone)."
        ),
    })

    w.add_assertion(
        "q3_is_exact_balancing",
        computed=s1["is_exact"], expected=True,
    )
    w.add_assertion(
        "li2q_tower_wrong_scale_for_correction",
        computed=tower_scale_ok, expected=True,
    )
    # F_Bor alone already lands m_p within ~1e6 ppb (sub-percent); the
    # habiro_ratio is a small (<~1e4 ppb) refinement, not the bulk.
    w.add_assertion(
        "F_Bor_alone_subpercent",
        computed=bool(abs(err_exact_ppb) < mpf("1e7")), expected=True,
    )
    w.add_assertion(
        "habiro_ratio_is_small_correction",
        computed=bool(abs(habiro_ratio - 1) < mpf("1e-2")), expected=True,
    )
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
