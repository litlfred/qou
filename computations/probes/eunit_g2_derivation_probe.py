#!/usr/bin/env python3
"""g₂ derivation attempt — cosh/crossing-count, BCH/Bernoulli, and the parity puzzle.

CONTEXT (read first, in order):
  * eunit_magnus_order2_probe.py + docs/audits/2026-07-24-eunit-magnus-order2.md (committed):
    the deuteron −9.2% decomposes as E_rot = E⁺·(1−t) with bar-odd impurity t ≈ 5.21% and a
    bar-even gap on E⁺ of +4.41% = g₂·h², g₂ ≈ 1.0087 (NEAR-MATCH, underived), h = q−q⁻¹.
  * docs/audits/2026-07-19-eunit-source-is-the-counit.md: μ₀ = m_e/(3h/2) — the first-order
    counit ladder is 3 crossings × (h/2) per crossing, i.e. the per-crossing bar-ODD counit
    weight is sinh θ = h/2 with θ = ln q (ε(σ) = q = cosh θ + sinh θ).
  * library/phys-rep09/phys-rep09.pdf (Blanes–Casas–Oteo–Ros, Phys. Rep. 470 (2009) 151): Theorem 1
    eq (32) dΩ/dt = Σ_n (B_n/n!) ad_Ω^n A with BERNOULLI weights B₀=1, B₁=−½, B₂=1/6,
    B₄=−1/30, B_{2m+1}=0 (m≥1); explicit Ω₂ = ½∫∫[A₁,A₂] (eq 43), Ω₃ = (1/6)∫∫∫{nested
    commutators} (eq 45), Ω₄ prefactor 1/12 — every order-k≥2 term is a LIE ELEMENT.
  * library/arxiv-math-ph-0012035v3/0012035v3.pdf (Broda, NA-Stokes): P exp(i∮_∂S A) = 𝒫 exp((i/2)∫_S F_ij dx^i∧dx^j)
    with twisted curvature 𝓕 = U⁻¹FU; the quadratic term of the surface-ordered exponential
    carries the plain Dyson weight 1/2! on [(i/2)∫𝓕]² (§2.1.2 "Ordering", Dyson series).

WHAT THIS PROBE ESTABLISHES (exact sympy + mpmath 50 dps; audit-only, NO FIT):

  M1. Mechanism 1 — cosh/crossing-count (EXACT, all candidates enumerated):
    M1a  Per-crossing counit split ε(σ) = q = cosh θ + sinh θ, θ = ln q: the bar-even
         per-crossing projection is cosh θ = 1 + h²/8 + O(h⁴) — coefficient 1/8 of h², NOT ½
         (½h² would need per-crossing weight h; the counit weight is h/2, per the μ₀ = m_e/(3h/2)
         normalization of #4102/#4117).
    M1b  σ₁³ is SINGLE-GENERATOR ⇒ the holonomy is coherent, exp(3a): the counit's bar-even
         part is cosh(3θ) ⇒ leading coefficient 9·(1/8) = 9/8 (n²/8 at n crossings).
    M1c  Incoherent (independent per-crossing product) variant: (cosh θ)³ ⇒ 3/8.
    M1d  Naive weight-h variants (the task's 3/2 and 9/2): cosh(h)³ ⇒ 3/2; cosh(3h) ⇒ 9/2.
    M1e  EXACT values at q₀:  C_per ≈ 0.1247, C_inc ≈ 0.3760, C_coh ≈ 1.1301,
         C_h·inc ≈ 1.5387, C_h·coh ≈ 4.6495.  Measured g₂ ≈ 1.00865.
         VERDICT (scope-(a)): NO candidate matches g₂ within an h²-order tolerance —
         the closest, coherent cosh(3θ), overshoots by 0.1215 = 2.78·h² (= 0.58·h; inside a
         LOOSE O(h) budget, recorded as an observation, NOT a match). Mechanism 1, alone
         and as-is, does not derive g₂ = 1.0087.
    M1f  Exact identity 2(cosh 2θ − 1) = h²: "g₂ = 1" is exactly the n=2-coherent cosh shape
         at weight 2 — an exact restatement, NOT a derivation (recorded as shape observation).
    M1g  Structural: the 2-dim Hecke-rep trace of σ₁³ is q³ − q⁻³ = 2 sinh 3θ — purely
         bar-ODD. The bar-even cosh channel is a CHARACTER/eigenvalue functional effect;
         the plain rep trace carries none of it.

  M2. Mechanism 2 — BCH/Bernoulli (citation-anchored, exact):
    M2a  Generating function x/(eˣ−1) = Σ B_n xⁿ/n! verified by series: B₀=1, B₁=−½, B₂=1/6,
         B₃=0, B₄=−1/30 (phys-rep09 §1.4 + eq (32); convention-independent check).
    M2b  Every Magnus term of order ≥ 2 multiplies a COMMUTATOR (eq 43/45: ½[A₁,A₂],
         (1/6){[A₁,[A₂,A₃]]+[[A₁,A₂],A₃]}, Ω₄ prefactor 1/12): the Bernoulli tower assigns
         coefficient EXACTLY 0 to any scalar (non-Lie) quadratic term. For the single-generator
         deuteron word σ₁³ all Ω_{k≥2} vanish (re-verified numerically here via the committed
         probe's machinery). VERDICT: the BCH/Bernoulli mechanism predicts C = 0 for the
         bar-even quadratic gap — it CANNOT produce g₂ (class-(b) for the braid-word
         connection; invariants: Lie-element structure + [X,X] = 0).
    M2c  Broda surface-ordered version: the bar-even quadratic term carries the plain Dyson
         1/2! weight on the surface-ordered square of the twisted curvature 𝓕 — evaluating it
         needs the Seifert-surface discretization the corpus lacks (named wall, unchanged).

  M3. The parity puzzle (exact enumeration):
    Residual r = g₂ − 1 ≈ 0.008652.  Ladder units are Laurent monomials
    m(a,b) = (v−v⁻¹)^a [2]_v^b, v = √q (bar-parity = parity of a).  Enumerating
    a ∈ [0,6], b ∈ [−6,6]:
      · closest unit of ANY parity: h³ = m(3,3) ≈ 0.009137, bar-ODD, +5.6% — PARITY-BLOCKED
        (gap/h² is bar-even; a bar-odd unit cannot appear with a real coefficient).
      · closest BAR-EVEN unit: h⁴[2]_v² = m(4,6) ≈ 0.007662, −11.4%; next x = m(2,0)
        ≈ 0.010897, +26.0%.  NO bar-even monomial within 10% of r.
    STRUCTURAL FINDING: the residual r is NOT a next-order bar-even ladder unit — it lives in
    the E⁺ frame definition (the parity-projection prescription) or the crossing-count
    arithmetic, not in the unit ladder.

EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

# reuse the committed probe's rep machinery (same directory; import is side-effect-free)
from eunit_magnus_order2_probe import (  # noqa: E402
    hecke_rep, mat_log_hecke, magnus_omega12, maxabs,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Muon leg read BY NAME (bean qou-9ugp, 2026-09-03). It was the 17-dp literal
# 1.10997859555733471 -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22 when that anchor was re-derived to the CODATA-2022 lepton ratio
# (+0.0769 ppb). This probe is an explicit env-vs-muon COMPARISON, so it needs
# both legs (exception E1 of the 2026-08-30 ruling); a comparison whose muon
# leg is a retired literal is comparing live-proton against yesterday's muon.
Q0_MUON_STR = mp.nstr(q_muon_at(50), 50, strip_zeros=False)


# ----------------------------------------------------------------------------- symbolic
def symbolic_layer() -> dict:
    th = sp.Symbol("theta", positive=True)
    q = sp.exp(th)
    h = q - 1 / q  # = 2 sinh θ

    # M1a: per-crossing counit split and its order-2 coefficient
    s_split = (sp.simplify((q + 1 / q) / 2 - sp.cosh(th)) == 0
               and sp.simplify((q - 1 / q) / 2 - sp.sinh(th)) == 0
               and sp.simplify(h - 2 * sp.sinh(th)) == 0)
    lead = lambda expr: sp.limit(expr, th, 0)
    C_per_lead = lead((sp.cosh(th) - 1) / h**2)            # 1/8
    C_coh_lead = lead((sp.cosh(3 * th) - 1) / h**2)        # 9/8
    C_inc_lead = lead((sp.cosh(th) ** 3 - 1) / h**2)       # 3/8
    C_hinc_lead = lead((sp.cosh(h) ** 3 - 1) / h**2)       # 3/2
    C_hcoh_lead = lead((sp.cosh(3 * h) - 1) / h**2)        # 9/2
    # M1f exact identity: 2(cosh 2θ − 1) = h²
    s_identity = sp.simplify(2 * (sp.cosh(2 * th) - 1) - h**2) == 0
    # M1g: 2-dim rep trace of σ³ = q³ + (−q⁻¹)³ = 2 sinh 3θ (purely bar-odd)
    s_trace_odd = sp.simplify(q**3 - q**-3 - 2 * sp.sinh(3 * th)) == 0

    # M2a: Bernoulli generating function x/(eˣ−1) = Σ B_n xⁿ/n! (convention-independent)
    x = sp.Symbol("x")
    ser = sp.series(x / (sp.exp(x) - 1), x, 0, 5).removeO()
    B = [sp.factorial(n) * ser.coeff(x, n) for n in range(5)]
    s_bernoulli = (B[0] == 1 and B[1] == sp.Rational(-1, 2) and B[2] == sp.Rational(1, 6)
                   and B[3] == 0 and B[4] == sp.Rational(-1, 30))

    return {
        "M1a_per_crossing_split_theta": bool(s_split),
        "M1a_C_per_leading_is_1_8": bool(C_per_lead == sp.Rational(1, 8)),
        "M1b_C_coherent_leading_is_9_8": bool(C_coh_lead == sp.Rational(9, 8)),
        "M1c_C_incoherent_leading_is_3_8": bool(C_inc_lead == sp.Rational(3, 8)),
        "M1d_C_naive_h_leading_3_2_and_9_2": bool(
            C_hinc_lead == sp.Rational(3, 2) and C_hcoh_lead == sp.Rational(9, 2)),
        "M1f_identity_2cosh2t_minus_1_eq_h2": bool(s_identity),
        "M1g_rep_trace_sigma3_pure_bar_odd": bool(s_trace_odd),
        "M2a_bernoulli_weights_B1_m12_B2_16_B3_0_B4_m130": bool(s_bernoulli),
    }


# ------------------------------------------------------------------------ numeric layer
def numeric_layer(q_str: str) -> dict:
    q = mp.mpf(q_str)
    m_e = mp.mpf(str(M_E_MEV))
    B_D = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    h = q - 1 / q
    th = mp.log(q)
    v = mp.sqrt(q)
    vv = v - 1 / v
    c2v = v + 1 / v

    # measured g2 (committed frame: E⁺ = m_e [3]_q[4]_q / 3)
    br = lambda n: (q**n - q**-n) / (q - 1 / q)
    E_plus = m_e * br(3) * br(4) / 3
    g2 = (B_D / E_plus - 1) / h**2
    r = g2 - 1

    # M1 candidates, exact at q0
    C = {
        "C_per_crossing_cosh_theta": (mp.cosh(th) - 1) / h**2,
        "C_incoherent_cosh_theta_cubed": (mp.cosh(th) ** 3 - 1) / h**2,
        "C_coherent_cosh_3theta": (mp.cosh(3 * th) - 1) / h**2,
        "C_naive_h_incoherent_cosh_h_cubed": (mp.cosh(h) ** 3 - 1) / h**2,
        "C_naive_h_coherent_cosh_3h": (mp.cosh(3 * h) - 1) / h**2,
    }
    mismatches = {k: abs(val - g2) for k, val in C.items()}
    min_mismatch = min(mismatches.values())

    # M2b: single-generator word — Magnus tower vanishes with the exact Bernoulli weights
    s1, _s2 = hecke_rep(q)
    a = mat_log_hecke(s1, q)
    _O1, O2 = magnus_omega12([a, a, a])
    deuteron_O2 = maxabs(O2)
    # M1g numeric: rep trace of σ₁³ purely bar-odd
    U = s1 * s1 * s1
    trU = U[0, 0] + U[1, 1]
    trace_res = abs(trU - (q**3 - q**-3))

    # M3: parity-puzzle enumeration m(a,b) = (v−v⁻¹)^a [2]_v^b, a∈[0,6], b∈[−6,6]
    rows = []
    for aa in range(0, 7):
        for bb in range(-6, 7):
            if aa == 0 and bb <= 0:
                continue
            mval = vv**aa * c2v**bb
            dev = abs(mval / r - 1)
            if dev < mp.mpf("0.30"):
                rows.append({
                    "a": aa, "b": bb, "parity": "even" if aa % 2 == 0 else "ODD",
                    "value": mp.nstr(mval, 10), "dev_vs_r": mp.nstr(dev, 6),
                    "_dev": dev,
                })
    rows.sort(key=lambda x: x["_dev"])
    even_devs = [x["_dev"] for x in rows if x["parity"] == "even"]
    # closest-of-any-parity should be h³ = m(3,3), bar-ODD
    closest = rows[0] if rows else None

    return {
        "q0_used": mp.nstr(q, 20),
        "g2_measured": mp.nstr(g2, 12),
        "r_residual_g2_minus_1": mp.nstr(r, 12),
        "h2": mp.nstr(h**2, 12),
        "h3": mp.nstr(h**3, 12),
        "h4": mp.nstr(h**4, 12),
        "mech1_candidates": {k: mp.nstr(val, 10) for k, val in C.items()},
        "mech1_mismatch_vs_g2": {k: mp.nstr(val, 8) for k, val in mismatches.items()},
        "mech1_closest_mismatch_over_h2": mp.nstr(min_mismatch / h**2, 6),
        "mech1_closest_mismatch_over_h": mp.nstr(min_mismatch / h, 6),
        "parity_table_within_30pct_of_r": [
            {k: v for k, v in row.items() if k != "_dev"} for row in rows],
        "h3_over_r": mp.nstr(h**3 / r, 8),
        "_flags": {
            "g2_band_1008_1010": bool(mp.mpf("1.008") < g2 < mp.mpf("1.010")),
            # M1 verdict: NO candidate within h²-order of g2 (near-match tier would need ≲ h²)
            "mech1_no_candidate_within_h2_of_g2": bool(min_mismatch > h**2),
            # observation (not a match): coherent cosh(3θ) is within a loose O(h) budget
            "mech1_coherent_within_loose_h_budget": bool(
                mismatches["C_coherent_cosh_3theta"] < h),
            # M2 verdict: Bernoulli tower gives exactly 0 for the single-generator word
            "mech2_single_generator_magnus_tower_vanishes": bool(
                deuteron_O2 < mp.mpf("1e-45")),
            "m1g_rep_trace_pure_bar_odd": bool(trace_res < mp.mpf("1e-45")),
            # M3 verdicts
            "parity_closest_any_is_h3_bar_odd": bool(
                closest is not None and closest["a"] == 3 and closest["b"] == 3
                and closest["parity"] == "ODD"),
            "parity_h3_within_6pct_but_bar_odd": bool(
                abs(h**3 / r - 1) < mp.mpf("0.06")),
            "parity_no_bar_even_monomial_within_10pct": bool(
                all(d > mp.mpf("0.10") for d in even_devs)),
            "parity_h4_too_small_ratio_below_half": bool(h**4 / r < mp.mpf("0.5")),
        },
        "_g2": g2,
    }


def main() -> int:
    sym = symbolic_layer()
    num_env = numeric_layer(Q_50_DIGIT_STR)
    num_muon = numeric_layer(Q0_MUON_STR)
    pin_shift = abs(num_env["_g2"] - num_muon["_g2"])

    wb = WitnessBuilder("eunit-g2-derivation", engine="mpmath", output_dir=str(_HERE))
    wb.set_description(
        "g2 derivation attempt (the E_unit bar-even gap coefficient g2 = gap/h^2 = 1.00865, "
        "NEAR-MATCH, underived — committed eunit-magnus-order2 witness). Three mechanisms "
        "tested exactly, NO FIT. Mechanism 1 (cosh/crossing-count): the counit per-crossing "
        "split eps(sigma) = q = cosh(theta) + sinh(theta), theta = ln q, gives bar-even "
        "coefficient 1/8 of h^2 per crossing (NOT 1/2 — the counit weight is h/2 per the "
        "mu0 = m_e/(3h/2) ladder); sigma_1^3 is single-generator hence coherent: leading "
        "coefficient 9/8, exact value cosh(3 theta) => C = 1.1301; incoherent product 3/8 "
        "(0.3760); naive weight-h variants 3/2 (1.5387) and 9/2 (4.6495). NO candidate is "
        "within h^2-order of g2 (closest 1.1301 overshoots by 0.1215 = 2.78 h^2) => "
        "scope-(a): mechanism 1 alone, as-is, does not derive g2. Mechanism 2 "
        "(BCH/Bernoulli, phys-rep09 Thm 1 eq 32): every Magnus order >= 2 term is a LIE "
        "element with Bernoulli weights (B1 = -1/2 on [A1,A2] giving Omega_2 = "
        "(1/2) iint [A1,A2], eq 43; 1/6 nested at order 3, eq 45; 1/12 at order 4; "
        "generating function x/(e^x - 1) verified) => assigns EXACTLY 0 scalar quadratic "
        "content; for the single-generator deuteron word sigma_1^3 the whole tower vanishes "
        "=> mechanism 2 predicts C = 0, cannot produce g2 (class-(b), invariants: "
        "Lie-element structure + [X,X] = 0). Broda's surface-ordered quadratic term carries "
        "the plain Dyson 1/2! weight on the twisted-curvature square — evaluation blocked on "
        "the missing Seifert-surface discretization (named wall). Parity puzzle: residual "
        "r = g2 - 1 = 0.008652; enumerating Laurent units (v-1/v)^a [2]_v^b (a in [0,6], "
        "b in [-6,6]): closest of ANY parity is h^3 (bar-ODD, +5.6%, PARITY-BLOCKED); "
        "closest bar-even is h^4 [2]_v^2 (-11.4%); NO bar-even monomial within 10% of r => "
        "STRUCTURAL FINDING: the residual is not a next-order ladder unit — it lives in the "
        "E+ frame definition (parity-projection prescription) or the crossing-count "
        "arithmetic. Nothing closes; nothing wired.")
    wb.set_audit_only("docs/audits/2026-07-25-eunit-g2-derivation-attempt.md")
    wb.add_parameter("q0_env_pin", Q_50_DIGIT_STR)
    wb.add_parameter("q0_muon_canonical", Q0_MUON_STR)
    wb.add_data("symbolic", sym)
    wb.add_data("numeric_env_pin", {k: v for k, v in num_env.items()
                                    if k not in ("_flags", "_g2")})
    wb.add_data("pin_robustness", {"g2_shift_between_pins": mp.nstr(pin_shift, 5)})
    wb.add_caveat(
        "NO FIT: the five mechanism-1 candidates are pre-registered structural shapes "
        "(per-crossing / coherent / incoherent x counit-weight h/2 vs naive weight h); none "
        "was tuned. The verdicts are constraint statements, scope-(a) unless an invariant is "
        "cited. g2 remains NEAR-MATCH tier, underived; nothing here is wired to production.")
    wb.add_caveat(
        "Citations: Blanes-Casas-Oteo-Ros, Phys. Rep. 470 (2009) 151-238, Thm 1 eq (32) + "
        "eqs (43)/(45) [library/phys-rep09/phys-rep09.pdf]; Broda, math-ph/0012035v3 [library/]. "
        "q-rotor lineage (index-verified, abstracts only): Raychev-Roussev-Smirnov, "
        "J. Phys. G 16 (1990) L137-L141; Bonatsos-Daskaloyannis, Prog. Part. Nucl. Phys. 43 "
        "(1999) 537, nucl-th/9909003 — NOTE their q is typically a PHASE (unit-circle) for "
        "rotational-spectra fits; QOU's q0 is real. Comparison is lineage, not equivalence.")

    for name, flag in sym.items():
        wb.add_assertion(f"sym_{name}", computed=str(bool(flag)), expected="True")
    for name, flag in num_env["_flags"].items():
        wb.add_assertion(f"num_{name}", computed=str(bool(flag)), expected="True")
    wb.add_assertion("pin_robust_g2_shift_below_1e6",
                     computed=str(bool(pin_shift < mp.mpf("1e-6"))), expected="True")
    # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
    # pins deliberately, so it belongs to neither anchor list. The stamp
    # carries the values ACTUALLY COMPUTED WITH, so the audit re-checks each
    # leg against its canonical pin instead of tautologically re-reading it.
    out = wb.save(q0_comparison(
        muon=mp.mpf(Q0_MUON_STR),
        proton=Q_MP,
        reason='measures the order-2 g2 coefficient at BOTH the environment (proton) pin and the muon pin, and reports the shift between them as pin_robustness; both pins are read on purpose and each is reported under its own key',
    ))

    print("=== g2 derivation attempt (mechanisms 1-3; audit-only, NO FIT) ===")
    print("symbolic:", sym)
    print(f"g2 measured = {num_env['g2_measured']}   r = g2-1 = {num_env['r_residual_g2_minus_1']}")
    print("mechanism-1 candidates (exact at q0):")
    for k, val in num_env["mech1_candidates"].items():
        print(f"  {k:38s} {val}   |C-g2| = {num_env['mech1_mismatch_vs_g2'][k]}")
    print(f"  closest mismatch = {num_env['mech1_closest_mismatch_over_h2']} x h^2 "
          f"(= {num_env['mech1_closest_mismatch_over_h']} x h)  => NO candidate at near-match tier")
    print("mechanism-2: Bernoulli tower (B1=-1/2, B2=1/6, B3=0, B4=-1/30) multiplies "
          "commutators only => C = 0 for sigma_1^3 (tower vanishes; verified)")
    print("parity table (units within 30% of r):")
    for row in num_env["parity_table_within_30pct_of_r"]:
        print(f"  (v-1/v)^{row['a']} [2]_v^{row['b']:>2d}  = {row['value']:>14s}  "
              f"dev {row['dev_vs_r']:>8s}  {row['parity']}")
    print(f"  h^3/r = {num_env['h3_over_r']} (bar-ODD => parity-blocked); "
          "no bar-even monomial within 10% of r")
    print("VERDICT: mech-1 scope-(a) (no candidate within h^2 of g2); mech-2 class-(b) "
          "C=0 (Lie-element invariant); residual r is NOT a next-order bar-even unit => "
          "it lives in the E+ frame definition or the crossing-count arithmetic. "
          "g2 stays NEAR-MATCH, underived. No fit; nothing wired.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
