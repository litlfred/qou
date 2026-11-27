"""qbeta_bar_odd_qq_coefficient_leg_probe.py — the Q(q)-coefficient leg of the
bar-odd element discriminator (bean qou-0e2p; closes #7118 §4a item (i)).

CONTEXT.  #7118 (`qbeta_bar_odd_element_discriminator_probe.py`) showed that on
the admissible trace span with coefficients in **Q**, Delta_S is bar-odd
everywhere and Delta_L only at the zero trace.  It left open what happens when
the coefficients live in **Q(q)**, where bar: q -> 1/q acts on them too, so the
condition bar(a·A + b·B) = -(a·A + b·B) becomes a *semilinear* functional
equation rather than a linear one.

WHAT THIS PROBE ESTABLISHES (exact sympy over Q(q); the pin enters only at readout).

Write F = Q(q + 1/q) for the bar-fixed subfield, h = q - 1/q, so that
Q(q) = F ⊕ F·h with bar = +1 on F and -1 on h.  For an element with
A := tr_M^{z=q}(Delta) and B := tr_M^{z_D}(Delta), the solution set

    S(Delta) = { (a, b) ∈ Q(q)^2 : bar(aA + bB) = -(aA + bB) }

is an F-vector space (NOT a Q(q)-subspace — bar is only F-linear), cut out by
ONE F-linear equation on the four F-coordinates (a_0, a_1, b_0, b_1) of
(a, b) = (a_0 + a_1 h, b_0 + b_1 h):

    a_0·A_e + h²·a_1·A_o + b_0·B_e + h²·b_1·B_o = 0 ,

so dim_F S(Delta) = 3 for BOTH elements.  Over Q(q) the criterion is therefore
VACUOUS: (a, b) = (h/A, 0) makes ANY nonzero element bar-odd by fiat.  The leg
has content only once the coefficient parity is restricted, and the three
natural restrictions give three different answers — measured, not assumed:

    coefficients in     Delta_S            Delta_L
    Q                   all of Q²          {0}            (reproduces #7118)
    F  (bar-even)       all of F²          ONE F-line, (a:b) = (B_e : -A_e),
                                           q-dependent — never f(q)·(a_0, b_0)
    Q(q)                dim_F 3            dim_F 3        (vacuous)

The F-line is the physically meaningful one: a bar-EVEN coefficient is one
that is itself p<->n neutral.  On that line Delta_L admits exactly one
normalised (eps(1) = 1) bar-odd functional, and it is a q-dependent MIXTURE
of the two admissible Markov traces.  A mixture a·tr_q + b·tr_{z_D} with
ab ≠ 0 is a trace functional (cyclic, linear, kills the (1³) block) but is
NOT a Markov trace for any parameter z':  the Markov property at two levels
forces  (aq + b z_D)² = (a+b)(aq² + b z_D²),  i.e.  ab·(q - z_D)² = 0.
So the unique bar-odd functional on Delta_L over F sits OUTSIDE the Markov
family — it is Option-G territory (a non-Markov admissible functional), and
its value is reported as what it is, not proposed.

Q_BETA REFERENCES — CORRECTING #7118 §5.  That section reported "an
8-significant-figure reference truncated in a corpus that computes at 60 dps"
(rel 8.8e-10).  Measured here, that diagnosis is inverted:

  * `codata_constants.Q_BETA_MEV = 0.78233341(61)` is AME-2020's own published
    precision (σ ≈ 780 ppb; the value is quoted to σ/6).  It is σ-limited, not
    truncated — `codata_2022_source.py` says so at the literal.
  * the fork-pricing witness's reference is `qou_substrate.constants.
    Q_NEUTRON_MEV = M_N_MEV - M_P_MEV - M_E_MEV`, a **float64** subtraction in
    which M_N_MEV is the AME-DERIVED literal 939.56542179 — itself
    M_P + M_E + Q_beta ROUNDED to 8 decimals (drops 0.69e-9 MeV).  The 8.8e-10
    is that dropped rounding, round-tripped.  The witness's reference is the
    degraded one, and it is the one with the float64 path.
  * the CODATA-2022 registry carries `neutron-proton mass difference energy
    equivalent in MeV = 1.29333251(38)`, from which Q_beta = 0.78233355931(38):
    **+191 ppb** above the AME value (0.3σ combined — consistent, but a
    different dataset).  Adopting it moves every c_3 extraction by
    ΔQ/(Q·u³) ≈ +0.31 (a 15 % move on c_3 ≈ -2.07), through the 1/u³
    amplification.  That is a dataset choice with a 116-file blast radius and
    is put to the owner, not made here.

No number is wired; nothing is proposed for adoption.  NO-FLOAT64: sympy exact
throughout, mpmath at compute dps for readout, witness fields as strings.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
for _s in (str(_HERE), str(_HERE.parent), str(_HERE.parent / "substrate")):
    if _s not in sys.path:
        sys.path.insert(0, _s)
import _path_bridge  # noqa: F401, E402
from mpmath import mp, mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV, Q_BETA_MEV_ERR  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_N_MEV_AME_DERIVED, M_N_MINUS_P_MEV, M_P_MEV, M_E_MEV as M_E_SRC, Q_BETA_MEV_AME,
)
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

q = sp.symbols("q", positive=True)
z = sp.symbols("z")
h = q - 1 / q
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
Z_Q = q                       # augmentation = Markov trace at z = q (#7115)
Z_D = q**3 / (q**2 + 1)       # convention D

#: tr_M of each candidate element as a function of the Markov parameter — the
#: same two closed forms #7118 calibrated against the committed witnesses
#: (Delta_S: qbeta_published_form_is_the_inadmissible_z1_probe, affine;
#:  Delta_L: qbeta-delta-element-fork-pricing.witness.json `trM_z_on_long_model`).
N_S = h**2 / 2 - h * z
N_L = -(q - 1) * (q + 1) * (q**4 * z**2 + 2 * q**3 * z + 2 * q**2 - 2 * q * z + z**2) / (4 * q**3)

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def bar(X):
    return sp.simplify(X.subs(q, 1 / q))


def even_part(X):
    return sp.simplify((X + bar(X)) / 2)


def odd_coeff(X):
    """X = X_e + h·X_o with X_e, X_o ∈ F; returns X_o."""
    return sp.simplify((X - bar(X)) / (2 * h))


def is_zero(X) -> bool:
    return sp.simplify(X) == 0


def in_F(X) -> bool:
    return is_zero(bar(X) - X)


def analyse(label: str, N) -> dict:
    print(f"\n== {label} ==")
    A = sp.simplify(N.subs(z, Z_Q))
    B = sp.simplify(N.subs(z, Z_D))
    Ae, Ao, Be, Bo = even_part(A), odd_coeff(A), even_part(B), odd_coeff(B)
    # the parity decomposition is exact and lands in F
    check(f"{label}: parity decomposition A = A_e + h A_o, B = B_e + h B_o, all parts in F",
          is_zero(A - (Ae + h * Ao)) and is_zero(B - (Be + h * Bo))
          and all(in_F(X) for X in (Ae, Ao, Be, Bo)),
          f"A_e = {Ae},  B_e = {Be}")

    # ---- full Q(q): one F-linear equation in four F-unknowns ------------------
    a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")
    a, b = a0 + a1 * h, b0 + b1 * h
    T = a * A + b * B
    E = sp.simplify(even_part(T))          # bar-odd  <=>  even part vanishes
    E_pred = sp.simplify(a0 * Ae + h**2 * a1 * Ao + b0 * Be + h**2 * b1 * Bo)
    check(f"{label}: bar-odd condition on Q(q)-coefficients is ONE F-linear equation",
          is_zero(E - E_pred),
          "even(aA+bB) = a0·A_e + h²a1·A_o + b0·B_e + h²b1·B_o  (a,b split over F)")
    coeffs = [Ae, h**2 * Ao, Be, h**2 * Bo]
    rank = 0 if all(is_zero(c) for c in coeffs) else 1
    dim_F = 4 - rank
    check(f"{label}: dim_F S(Delta) = 3 (codimension one, never {{0}})", dim_F == 3,
          f"coefficient row nonzero ⇒ rank 1 ⇒ dim_F = {dim_F}")
    # vacuity witness: (a, b) = (h/A, 0)
    check(f"{label}: over Q(q) the criterion is VACUOUS — (h/A, 0) is a solution",
          is_zero(bar(h / A * A) + h / A * A),
          "bar(h) = -h, so rescaling any nonzero trace by h/A manufactures bar-oddness")

    # ---- bar-even coefficients (a, b ∈ F) ------------------------------------
    E_F = sp.simplify(E.subs({a1: 0, b1: 0}))
    if is_zero(Ae) and is_zero(Be):
        dim_F_even = 2
        line = None
        check(f"{label}: bar-even coefficients — every (a,b) ∈ F² works (A, B already odd)",
              is_zero(E_F), "A_e = B_e = 0 ⇒ the F-equation is 0 = 0 on (a0, b0)")
    else:
        dim_F_even = 1
        line = (Be, -Ae)
        sol = sp.simplify(E_F.subs({a0: line[0], b0: line[1]}))
        ratio = sp.simplify(Ae / Be)
        check(f"{label}: bar-even coefficients — exactly ONE F-line, (a:b) = (B_e : -A_e)",
              is_zero(sol) and not is_zero(Ae) and not is_zero(Be),
              f"a0·A_e + b0·B_e = 0 with A_e/B_e = {ratio}")
        check(f"{label}: that line is q-DEPENDENT (A_e/B_e ∉ Q), so it is not f(q)·(rational pair)",
              not is_zero(sp.diff(ratio, q)),
              f"d/dq (A_e/B_e) = {sp.factor(sp.diff(ratio, q))}")

    # ---- rational coefficients (a, b ∈ Q) — must reproduce #7118 --------------
    if is_zero(Ae) and is_zero(Be):
        dim_Q = 2
        check(f"{label}: rational coefficients — all of Q² (reproduces #7118)", True,
              "the F-equation restricted to Q² is 0 = 0")
    else:
        ratio = sp.simplify(Ae / Be)
        dim_Q = 0 if not is_zero(sp.diff(ratio, q)) else 1
        check(f"{label}: rational coefficients — only (0,0) (reproduces #7118)", dim_Q == 0,
              "a0·A_e + b0·B_e = 0 with a0, b0 ∈ Q forces a0 = b0 = 0 since A_e/B_e ∉ Q")

    return {"A": str(A), "B": str(B), "A_e": str(Ae), "A_o": str(Ao),
            "B_e": str(Be), "B_o": str(Bo),
            "dim_F_over_Qq": dim_F, "dim_F_over_F": dim_F_even, "dim_Q_over_Q": dim_Q,
            "F_line": None if line is None else {"a": str(line[0]), "b": str(line[1])},
            "_sym": (A, B, Ae, Be, line)}


def main() -> int:
    print("qbeta_bar_odd_qq_coefficient_leg_probe — coefficients in Q(q), F = Q(q+1/q), and Q\n")
    RS = analyse("Delta_S", N_S)
    RL = analyse("Delta_L", N_L)

    # ---- the Markov obstruction for mixtures ----------------------------------
    print("\n== a·tr_q + b·tr_{z_D} is Markov only if ab = 0 ==")
    a, b, zp = sp.symbols("a b zp")
    # Markov traces on H_3 from the defining property alone (#7115 table):
    # tr(1) = 1, tr(σ_i) = z, tr(σ1σ2) = z·tr(σ1) = z².
    eps1, eps_s, eps_ss = a + b, a * Z_Q + b * Z_D, a * Z_Q**2 + b * Z_D**2
    # Markov property for eps with parameter zp: eps(σ1) = zp·eps(1), eps(σ1σ2) = zp·eps(σ1)
    obstruction = sp.simplify(eps_s**2 - eps1 * eps_ss)
    check("Markov property at two levels forces ab·(q - z_D)² = 0",
          is_zero(obstruction + a * b * (Z_Q - Z_D)**2),
          "(aq + b z_D)² − (a+b)(aq² + b z_D²) = −ab(q − z_D)²; q ≠ z_D ⇒ ab = 0")

    # ---- the unique normalised bar-odd functional on Delta_L over F -----------
    print("\n== Delta_L: the unique normalised bar-even-coefficient bar-odd functional ==")
    A, B, Ae, Be, line = RL["_sym"]
    aF, bF = line
    norm = sp.simplify(aF + bF)
    check("normalisation a + b = B_e − A_e is nonzero on the line",
          not is_zero(norm), f"a + b = {sp.factor(norm)}")
    a_n, b_n = sp.simplify(aF / norm), sp.simplify(bF / norm)
    eps_L = sp.simplify(a_n * A + b_n * B)
    check("eps_odd(Delta_L) is bar-odd, eps_odd(1) = 1, and both a, b ∈ F with ab ≠ 0",
          is_zero(bar(eps_L) + eps_L) and is_zero(a_n + b_n - 1)
          and in_F(a_n) and in_F(b_n) and not is_zero(a_n * b_n),
          f"a = {sp.factor(a_n)},  b = {sp.factor(b_n)}")
    check("so the unique bar-odd functional on Delta_L over F is NOT a Markov trace",
          not is_zero(a_n * b_n), "ab ≠ 0 and the obstruction above")

    q0 = sp.Rational(Q_50_DIGIT_STR)
    me = mpf(str(M_E_MEV))
    val = sp.Abs(eps_L * E0).subs(q, q0)
    Q_odd = mpf(str(sp.N(val, mp.dps + 5))) * me
    a_at = mpf(str(sp.N(a_n.subs(q, q0), 30)))
    b_at = mpf(str(sp.N(b_n.subs(q, q0), 30)))
    Q_ame = mpf(str(Q_BETA_MEV))
    err_ame = Q_odd / Q_ame - 1
    print(f"    (a, b) at the proton pin = ({mp.nstr(a_at, 12)}, {mp.nstr(b_at, 12)})")
    print(f"    Q_beta[eps_odd, Delta_L] = {mp.nstr(Q_odd, 20)} MeV   residual vs AME = {mp.nstr(100*err_ame, 8)} %")
    check("readout is a NUMBER, reported not proposed (anti-fit: value is a diagnostic)",
          Q_odd > 0, f"Q = {mp.nstr(Q_odd, 15)} MeV, {mp.nstr(100*err_ame, 6)} % vs AME")

    # ---- calibration against #7118 / #7115 numbers ---------------------------
    print("\n== calibration ==")
    Q_aug = mpf(str(sp.N(sp.Abs(A * E0).subs(q, q0), mp.dps + 5))) * me
    Q_zD = mpf(str(sp.N(sp.Abs(B * E0).subs(q, q0), mp.dps + 5))) * me
    check("Delta_L endpoints reproduce the fork-pricing grid (z=q: +39.32 %, z_D: −15.45 %)",
          abs(Q_aug / Q_ame - 1 - mpf("0.3932395")) < mpf("1e-6")
          and abs(Q_zD / Q_ame - 1 + mpf("0.1545139")) < mpf("1e-6"),
          f"{mp.nstr(100*(Q_aug/Q_ame-1), 8)} % / {mp.nstr(100*(Q_zD/Q_ame-1), 8)} %")

    # ---- Q_beta references: correcting #7118 §5 ------------------------------
    print("\n== Q_beta references ==")
    mn_lit = mpf(str(M_N_MEV_AME_DERIVED))
    mp_ = mpf(str(M_P_MEV))
    me_src = mpf(str(M_E_SRC))
    q_ame = mpf(str(Q_BETA_MEV_AME))
    exact_sum = mp_ + me_src + q_ame
    dropped = exact_sum - mn_lit
    q_witness_ref = mpf(str(Q_NEUTRON_MEV))
    rel_7118 = abs(q_witness_ref - Q_ame) / Q_ame
    print(f"    M_P + M_E + Q_AME = {mp.nstr(exact_sum, 16)};  M_N_MEV_AME_DERIVED literal = {mp.nstr(mn_lit, 16)};  dropped = {mp.nstr(dropped, 4)} MeV")
    print(f"    witness reference Q_NEUTRON_MEV = {Q_NEUTRON_MEV!r} ({type(Q_NEUTRON_MEV).__name__});  rel to AME = {mp.nstr(rel_7118, 4)}")
    check("the 8.8e-10 of #7118 §5 is the ROUNDING of the derived m_n literal, not a truncated Q_beta",
          abs(dropped - mpf("0.69e-9")) < mpf("1e-14")
          and abs(rel_7118 - dropped / Q_ame) < mpf("1e-12"),
          f"dropped/Q = {mp.nstr(dropped/Q_ame, 4)} = witness-vs-AME rel {mp.nstr(rel_7118, 4)}")
    check("Q_BETA_MEV is σ-limited (quoted to σ/6), not truncated",
          abs(mpf(str(Q_BETA_MEV_ERR)) / mpf("1e-8") - 61) < mpf("1e-9"),
          f"0.78233341(61): last quoted digit 1e-8 = σ/61 — a truncated value would carry digits below σ")
    check("the witness's own reference is a float64 path (NO-FLOAT64 defect lives THERE)",
          isinstance(Q_NEUTRON_MEV, float),
          "qou_substrate.constants.Q_NEUTRON_MEV = M_N_MEV - M_P_MEV - M_E_MEV in float")

    row = _codata.codata("neutron-proton mass difference energy equivalent in MeV")
    row_e = _codata.codata("electron mass energy equivalent in MeV")
    q_reg = mpf(row.value_str) - mpf(row_e.value_str)
    q_reg_err = mp.sqrt(mpf(row.uncertainty_str)**2 + mpf(row_e.uncertainty_str)**2)
    shift_ppb = (q_reg / Q_ame - 1) * mpf(10)**9
    sigma_comb = mp.sqrt(q_reg_err**2 + mpf(str(Q_BETA_MEV_ERR))**2)
    print(f"    registry (m_n−m_p) − m_e = {mp.nstr(q_reg, 14)} ± {mp.nstr(q_reg_err, 3)} MeV;  vs AME {mp.nstr(shift_ppb, 6)} ppb = {mp.nstr((q_reg-Q_ame)/sigma_comb, 3)} σ")
    # expected value DERIVED from the corpus's own registry-checked literal
    # (codata_2022_source.M_N_MINUS_P_MEV, audited by codata_table_vintage_audit), not copied
    q_reg_corpus = mpf(str(M_N_MINUS_P_MEV)) - me_src
    check("CODATA-2022 registry Q_beta = (m_n - m_p) - m_e = codata_2022_source.M_N_MINUS_P_MEV - M_E_MEV, +191 ppb from AME, 0.2σ combined",
          abs(q_reg - q_reg_corpus) < mpf("1e-14") and abs(shift_ppb - 191) < 1,
          f"{mp.nstr(shift_ppb, 6)} ppb, {mp.nstr((q_reg-Q_ame)/sigma_comb, 3)} σ — consistent, DIFFERENT dataset")

    # what adopting it would do to c_3 through the 1/u³ ladder-extraction divisor
    q0m = Q_MP
    hm = q0m - 1 / q0m
    hbar = (q0m - 1) / q0m
    bm = mp.sqrt((hm**2 + 3) / (hm**2 + 4))
    u = bm * hbar**2
    dc3 = (q_reg / Q_ame - 1) / u**3
    print(f"    u = {mp.nstr(u, 10)};  Δc_3 ≈ (ΔQ/Q)/u³ = {mp.nstr(dc3, 8)}  on c_3 ≈ −2.069 (≈ {mp.nstr(100*dc3/mpf('2.0693'), 4)} %)")
    check("adopting the registry Q_beta moves c_3 by ≈ +0.31 (≈ 15 %) — a blast radius, put to the owner",
          mpf("0.25") < dc3 < mpf("0.40"), f"Δc_3 = {mp.nstr(dc3, 8)} to leading order in u")

    # ---- witness ----------------------------------------------------------
    wb = WitnessBuilder("qbeta-bar-odd-qq-coefficient-leg", engine="sympy+mpmath")
    wb.set_description(
        "Q(q)-coefficient leg of the bar-odd element discriminator (#7118 §4a (i)). "
        "With F = Q(q+1/q) the bar-fixed field, the solution set of bar(aA+bB) = -(aA+bB) "
        "is an F-space of dimension 3 for BOTH Delta_S and Delta_L — over Q(q) the criterion "
        "is VACUOUS ((h/A, 0) always works). Restricting to bar-EVEN coefficients (a, b in F, "
        "the p<->n-neutral ones): Delta_S admits all of F^2, Delta_L exactly ONE q-dependent "
        "F-line (a:b) = (B_e:-A_e). Restricting to Q reproduces #7118 (F^2 vs {0}). The unique "
        "normalised bar-odd functional on Delta_L over F is a mixture a tr_q + b tr_{z_D} with "
        "ab != 0, and the Markov property at two levels forces ab (q - z_D)^2 = 0, so it is NOT "
        "a Markov trace for any z' — Option-G territory; its readout at the proton pin is "
        "recorded as a diagnostic, not proposed. Also corrects #7118 §5: Q_BETA_MEV = "
        "0.78233341(61) is sigma-limited, not truncated; the 8.8e-10 is the rounding of the "
        "derived m_n literal inside the witness's own float64 reference Q_NEUTRON_MEV. The "
        "CODATA-2022 registry gives Q_beta = 0.78233355931(38), +191 ppb (0.3 sigma), which "
        "would move c_3 by ~+0.31 through 1/u^3 — a dataset choice put to the owner, not made.")
    wb.add_parameter("q0_pin", "proton (q_parameter.Q_50_DIGIT_STR), exact Rational at readout")
    wb.add_parameter("convention", "D: z_D = q^3/(q^2+1); augmentation z = q")
    wb.add_parameter("tower_status", "ORDER-ZERO-ONLY at n=3 (H_3), the algebra D7 names for the decay channel")
    wb.add_data("q0", Q_50_DIGIT_STR)
    for lab, R in (("Delta_S", RS), ("Delta_L", RL)):
        wb.add_data(lab, {k: v for k, v in R.items() if k != "_sym"})
    wb.add_data("markov_obstruction", "(aq + b z_D)^2 - (a+b)(a q^2 + b z_D^2) = -ab (q - z_D)^2")
    wb.add_data("delta_L_unique_bar_odd_functional_over_F", {
        "a": str(sp.factor(a_n)), "b": str(sp.factor(b_n)),
        "eps_odd_Delta_L": str(sp.factor(eps_L)),
        "a_at_q0": fmt(a_at, 25), "b_at_q0": fmt(b_at, 25),
        "Q_beta_MeV": fmt(Q_odd, 30), "err_vs_AME": fmt(err_ame, 20),
        "is_markov_trace": False,
        "status": "diagnostic readout; not proposed, not wired (NO FITTING)",
    })
    wb.add_data("q_beta_references", {
        "codata_constants_Q_BETA_MEV": str(Q_BETA_MEV), "err": str(Q_BETA_MEV_ERR),
        "precision_status": "sigma-limited (quoted to sigma/6), NOT truncated — #7118 §5 corrected",
        "witness_reference_Q_NEUTRON_MEV": repr(Q_NEUTRON_MEV),
        "witness_reference_type": type(Q_NEUTRON_MEV).__name__,
        "m_n_literal_rounding_dropped_MeV": fmt(dropped, 6),
        "rel_7118": fmt(rel_7118, 6),
        "registry_Q_beta_MeV": fmt(q_reg, 20), "registry_err_MeV": fmt(q_reg_err, 6),
        "registry_source": "qou_substrate.codata: 'neutron-proton mass difference energy equivalent in MeV' = "
                           f"{row.value_str}({row.uncertainty_str}) minus 'electron mass energy equivalent in MeV'",
        "shift_vs_AME_ppb": fmt(shift_ppb, 10), "shift_sigma_combined": fmt((q_reg-Q_ame)/sigma_comb, 6),
        "u_proton": fmt(u, 20), "delta_c3_if_adopted": fmt(dc3, 12),
        "decision": "owner — dataset choice (AME-2020 direct vs CODATA-2022 m_n-m_p), 116 consumer files",
    })
    wb.add_data("scope", {
        "tier": "exclusion within the admissible span over Q (#7118) EXTENDED: over F the exclusion "
                "on Delta_L is 'no bar-odd MARKOV trace'; over Q(q) the criterion has no content",
        "established": "the three-row table above, each row a sympy identity",
        "NOT_established": "that bar-even coefficients are THE right restriction — that is an "
                           "interpretive choice (p<->n-neutral normalisation), stated, not derived",
        "premise": "bar is p<->n conjugation (qou-e58e), as in #7118",
    })
    for name, ok, detail in results:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", tolerance="0.5", source=detail)
    out = wb.save()
    npass = sum(1 for _, ok, _ in results if ok)
    print(f"\n  {npass}/{len(results)} checks pass.  Witness: {out}")
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
