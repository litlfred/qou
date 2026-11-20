#!/usr/bin/env python3
"""E_unit higher-order counit terms via NA-Stokes / Magnus order 2 — the deuteron −9.2%.

CONTEXT (read first, in order):
  * docs/audits/2026-07-19-eunit-source-is-the-counit.md (merged #4117): E_unit's source is
    the COUNIT — μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.6295 MeV, first-order, 0 free params; the deuteron
    rotational form E_rot = μ₀·ℏ_q·J_q²(j=3) = 2.0196 MeV vs AME 2.2245662 (−9.2%). The −9.2%
    is the size of the missing higher-order (co)unit / NA-Stokes terms, to be organized along
    the exact ring identity (q−q⁻¹) = (v−v⁻¹)·[2]_v, v = √q.
  * binding_qhamiltonian_rotational_scale.py — the canonical rotational-tier frame reused here
    (D/T/³He/⁴He vs AME, j = n/2, n = 3A strands; forward-only, no AME inversion).
  * library/arxiv-math-ph-0012035v3/0012035v3.pdf (Broda, NA-Stokes): P exp(i∮_∂S A) = 𝒫 exp(i/2 ∫_S 𝓕), with the
    path-dependent curvature 𝓕(x) = U⁻¹(x,O) F(x) U(x,O) and F = dA − i[A,A].
  * library/phys-rep09/phys-rep09.pdf (Blanes–Casas–Oteo–Ros, Phys. Rep. 470 (2009) 151, Thm 1 eq (32)):
    Magnus:  Ω(t) = ∫A dt₁ + ½∫∫_{t₂<t₁} [A(t₁), A(t₂)] dt₂ dt₁ + ⋯  — the order-2 term is
    the double-integral COMMUTATOR ½∮∮[A,A]; every Magnus term of order k ≥ 2 is a Lie element
    (sum of nested commutators).
  * Sibling PR #4127 (octahedral 4-dilogarithm route B — the COMPLEMENTARY attack; this probe
    is the analytic Magnus route A of that PR's own plan, bean qou-dp32, run from the merged
    #4142 workplan item W2 on a different branch per the parallel-exploration policy).

WHAT THIS PROBE ESTABLISHES (symbolic assertions + forward numerics; audit-only, NO FIT):

  S. Structural / symbolic (proved identities, sympy):
    S1  h = q − q⁻¹ is bar-ODD (bar: q ↦ q⁻¹); the first-order counit weight.
    S2  h = (v − v⁻¹)·[2]_v at the v = √q level (exact ring identity).
    S3  h² is bar-EVEN — the order-2 scalar shape.  General grading: Magnus order k carries
        h^k with bar-parity (−1)^k (letters log σ are bar-odd: bar(σ) = σ⁻¹).
    S4  h² = x·[2]_v²  with x = (v−v⁻¹)² — one x-ladder unit (the 5g-form deformation
        parameter) dressed by [2]_v²: the q ↔ √q passage of the order-2 term.
    S5  E_rot = μ₀·ℏ_q·J_q²(j) ≡ m_e·(2/3)·J_q²(j)/(1+q) — the counit weight h CANCELS
        between μ₀ ∝ 1/h and ℏ_q = h/(1+q).
    S6  1/(1+q) = ½·(1 − t) with t = (q−1)/(q+1) = (v−v⁻¹)/[2]_v bar-ODD: the first-order
        rotational form is bar-IMPURE — bar-even part E⁺ = m_e·J_q²(j)/3, bar-odd impurity −t·E⁺.
    S7  [X, X] = 0 and bar-parity of a commutator of two bar-odd letters is bar-EVEN
        ([−X, −Y] = [X, Y]).

  N. Matrix-level (2-dim Hecke rep of B₃ = rescaled reduced Burau, mpmath 50 dps):
    N1  Rep checks: braid relation, Hecke relation (σ−q)(σ+q⁻¹)=0, exp(log σ) roundtrip.
    N2  DEUTERON channel word σ₁³ (single generator, the 3-crossing pn/trefoil pattern):
        Magnus Ω₂ = ½Σ_{k>l}[A_k, A_l] = 0 IDENTICALLY (all letters equal ⇒ [a,a] = 0).
        In fact the whole tower Ω_k, k ≥ 2 vanishes: the single-generator holonomy is abelian
        and exp(Ω₁) is EXACT. Proved vanishing — the analytic Magnus order-2 inter-crossing
        commutator contributes ZERO to the deuteron counit holonomy.
    N3  A ≥ 3-type word (σ₁σ₂⁻¹)³ (adjacent generators): Ω₂ ≠ 0 at the operator level, BUT
        tr(Ω₂) = 0 (trace of a commutator) — every trace-level (Markov/Jones) observable and
        the 1-dim counit character ε kill Ω₂ (and every Ω_k, k ≥ 2: Lie elements) LINEARLY.
        STRONGER (found by this probe's own numerics, then proved by cyclicity): the order-3
        trace term tr(Ω₁·Ω₂) ALSO vanishes identically for every B₃ word — with only two
        distinct letters a, b, every constituent tr(X[X,Y]) = tr(Y[X,Y]) = 0 by cyclicity.
        So the first surviving inter-crossing trace-level correction is ORDER 4
        (tr(Ω₂²), tr(Ω₁²Ω₂) ≠ 0) — automatically bar-EVEN, magnitude ~h⁴ ≈ 0.19 %.
    N4  Magnitude ladder at q₀: h ≈ 0.2091, h² ≈ 4.37 %, h³ ≈ 0.91 %, t ≈ 5.21 %.

  F. Forward-only comparison (canonical rotational-tier frame; muon-vs-proton pin immaterial
     at this scale — both computed):
    F1  E_rot table D/T/³He/⁴He reproduces the canonical witness (−9.2 / −48.6 / −43.5 / −72.2 %).
    F2  Exact residual decomposition (deuteron): E_rot = E⁺·(1−t); the −9.2 % splits into the
        bar-odd parity impurity −t ≈ −5.21 % and a remaining bar-even gap +4.41 % on E⁺.
    F3  The remaining bar-even gap equals the natural order-2 unit h² to ≈ 0.8 %:
        (B_AME/E⁺ − 1)/h² ≈ 1.008.  E⁺·(1+h²) = 2.2238 MeV (−0.03 %).  NEAR-MATCH TIER:
        the coefficient 1 is NOT derived — deriving it (from the octahedral e₂ / NA-Stokes
        surface-curvature term) is the named open object. NOT wired anywhere.
    F4  A ≥ 3 is untouched: E⁺·(1+h²) leaves T −43 %, ³He −38 %, ⁴He −69 % — the per-rep
        A ≥ 3 deficit is NOT an order-2 effect (consistent with the corpus diagnosis).

VERDICT (honest): the inter-crossing Magnus order-2 commutator is EXACTLY ZERO for the
deuteron (single-generator word) and is killed linearly by trace/counit functionals for every
braid — so the −9.2 % is NOT an inter-crossing Magnus effect; within the NA-Stokes
organization the surviving second-order candidates are PER-CROSSING (the octahedral e₂ of
PR #4127's route B) or the surface-curvature pairing ½𝒫∬∬[𝓕,𝓕] (needs surface data the
corpus lacks — a wall). The bar-parity split then measures the residual forward: bar-odd
impurity −t + bar-even gap ≈ h² (coefficient ≈ 1.008, underived). Nothing closes; nothing wired.

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
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
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

# muon-canonical pin (computations/ layer canonical, q-pinning-50-digit witness);
# Q_50_DIGIT_STR resolves to the environment's anchor (proton in package-layer envs).
# Both are computed below; they differ by ~11.5 ppb — immaterial at this audit's 1e-4 scale.
# Muon leg read BY NAME (bean qou-9ugp, 2026-09-03). It was the 17-dp literal
# 1.10997859555733471 -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22 when that anchor was re-derived to the CODATA-2022 lepton ratio
# (+0.0769 ppb). This probe is an explicit env-vs-muon COMPARISON, so it needs
# both legs (exception E1 of the 2026-08-30 ruling); a comparison whose muon
# leg is a retired literal is comparing live-proton against yesterday's muon.
Q0_MUON_STR = mp.nstr(q_muon_at(50), 50, strip_zeros=False)


# ----------------------------------------------------------------------------- symbolic
def symbolic_layer() -> dict:
    q, v = sp.symbols("q v", positive=True)
    J = sp.Symbol("J", positive=True)  # stands for J_q^2(j), bar-even (S: q-integers)
    m_e = sp.Symbol("m_e", positive=True)

    h = q - 1 / q
    hbar_q = 1 - 1 / q
    mu0 = m_e / (3 * h / 2)
    t = (q - 1) / (q + 1)

    s1 = sp.simplify(h.subs(q, 1 / q) + h) == 0                        # h bar-odd
    s2 = sp.simplify(((v - 1 / v) * (v + 1 / v) - h.subs(q, v**2))) == 0
    s3 = sp.simplify((h**2).subs(q, 1 / q) - h**2) == 0                # h^2 bar-even
    x = (v - 1 / v) ** 2
    s4 = sp.simplify(x * (v + 1 / v) ** 2 - (h**2).subs(q, v**2)) == 0
    s5 = sp.simplify(mu0 * hbar_q * J - m_e * sp.Rational(2, 3) * J / (1 + q)) == 0
    s6a = sp.simplify(1 / (1 + q) - sp.Rational(1, 2) * (1 - t)) == 0
    s6b = sp.simplify(t.subs(q, 1 / q) + t) == 0                       # t bar-odd
    s6c = sp.simplify(t.subs(q, v**2) - (v - 1 / v) / (v + 1 / v)) == 0
    # S7: commutator identities on generic 2x2 symbolic matrices
    a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols("a11 a12 a21 a22 b11 b12 b21 b22")
    X = sp.Matrix([[a11, a12], [a21, a22]])
    Y = sp.Matrix([[b11, b12], [b21, b22]])
    com = lambda A, B: A * B - B * A
    s7a = sp.simplify(com(X, X)) == sp.zeros(2, 2)
    s7b = sp.simplify(com(-X, -Y) - com(X, Y)) == sp.zeros(2, 2)       # odd·odd = even
    s7c = sp.simplify(sp.trace(com(X, Y))) == 0                        # trace kills Ω₂
    # S8: two-letter order-3 cyclicity — tr(X[X,Y]) = tr(Y[X,Y]) = 0 identically,
    # so tr(Ω₁Ω₂) ≡ 0 for every two-generator (B₃) braid word.
    s8 = (sp.simplify(sp.trace(X * com(X, Y))) == 0
          and sp.simplify(sp.trace(Y * com(X, Y))) == 0)

    return {
        "S1_h_bar_odd": bool(s1),
        "S2_h_eq_vlevel_2v": bool(s2),
        "S3_h2_bar_even": bool(s3),
        "S4_h2_eq_x_times_2v_sq": bool(s4),
        "S5_h_cancels_mu0_hbarq": bool(s5),
        "S6_one_over_1plusq_even_odd_split": bool(s6a and s6b and s6c),
        "S7_commutator_identities": bool(s7a and s7b and s7c),
        "S8_two_letter_order3_trace_vanishes": bool(s8),
    }


# ------------------------------------------------------------------------- matrix layer
def hecke_rep(q):
    """2-dim Hecke rep of B₃: reduced Burau at t=q², rescaled by −1/q.
    Eigenvalues of each generator: (q, −q⁻¹) — the Hecke pair."""
    s1 = mp.matrix([[q, -1 / q], [0, -1 / q]])
    s2 = mp.matrix([[-1 / q, 0], [-q, q]])
    return s1, s2


def mat_log_hecke(M, q):
    """log of a Hecke generator via spectral projectors (eigenvalues q, −1/q).
    Principal branch: log(−1/q) = −ln q + iπ (fibre-level Im is permitted;
    the archimedean Im(q₀)=0 constraint applies to q, not to the fibre log)."""
    lam_p, lam_m = mp.mpf(q), -1 / mp.mpf(q)
    I2 = mp.eye(2)
    Pp = (M - lam_m * I2) / (lam_p - lam_m)
    Pm = (M - lam_p * I2) / (lam_m - lam_p)
    return mp.log(lam_p) * Pp + (mp.log(1 / q) + mp.mpc(0, mp.pi)) * Pm


def commutator(A, B):
    return A * B - B * A


def magnus_omega12(letters):
    """Ω₁, Ω₂ for a piecewise-constant connection given by ordered letters
    (unit time each). Phys. Rep. 470 eq (32): Ω₂ = ½ Σ_{k>l} [A_k, A_l]."""
    n = len(letters)
    O1 = mp.zeros(2, 2)
    for A in letters:
        O1 = O1 + A
    O2 = mp.zeros(2, 2)
    for k in range(n):
        for l in range(k):
            O2 = O2 + commutator(letters[k], letters[l])
    return O1, 0.5 * O2


def maxabs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def matrix_layer(q) -> dict:
    s1, s2 = hecke_rep(q)
    # N1 rep checks
    braid_res = maxabs(s1 * s2 * s1 - s2 * s1 * s2)
    I2 = mp.eye(2)
    hecke_res = max(maxabs((s1 - q * I2) * (s1 + I2 / q)),
                    maxabs((s2 - q * I2) * (s2 + I2 / q)))
    a = mat_log_hecke(s1, q)
    b = mat_log_hecke(s2, q)
    roundtrip = max(maxabs(mp.expm(a) - s1), maxabs(mp.expm(b) - s2))

    # N2 deuteron channel word σ₁³ — single generator
    O1_D, O2_D = magnus_omega12([a, a, a])
    deuteron_O2 = maxabs(O2_D)

    # N3 A≥3-type word (σ₁ σ₂⁻¹)³ — adjacent generators; letter of σ₂⁻¹ is −b
    word = [a, -b, a, -b, a, -b]
    O1_B, O2_B = magnus_omega12(word)
    borr_O2_norm = maxabs(O2_B)
    borr_O2_trace = abs(O2_B[0, 0] + O2_B[1, 1])
    O1O2 = O1_B * O2_B
    tr_O1O2 = abs(O1O2[0, 0] + O1O2[1, 1])
    # order-4 trace terms — the first surviving inter-crossing trace corrections
    O2sq = O2_B * O2_B
    tr_O2sq = abs(O2sq[0, 0] + O2sq[1, 1])
    O1sqO2 = O1_B * O1_B * O2_B
    tr_O1sqO2 = abs(O1sqO2[0, 0] + O1sqO2[1, 1])

    return {
        "N1_braid_residual": mp.nstr(braid_res, 5),
        "N1_hecke_residual": mp.nstr(hecke_res, 5),
        "N1_explog_roundtrip": mp.nstr(roundtrip, 5),
        "N2_deuteron_word_O2_maxabs": mp.nstr(deuteron_O2, 5),
        "N3_a3_word_O2_maxabs": mp.nstr(borr_O2_norm, 8),
        "N3_a3_word_trace_O2": mp.nstr(borr_O2_trace, 5),
        "N3_a3_word_trace_O1O2_order3": mp.nstr(tr_O1O2, 8),
        "N3_a3_word_trace_O2sq_order4": mp.nstr(tr_O2sq, 8),
        "N3_a3_word_trace_O1sqO2_order4": mp.nstr(tr_O1sqO2, 8),
        "_flags": {
            "rep_ok": bool(braid_res < mp.mpf("1e-45") and hecke_res < mp.mpf("1e-45")
                           and roundtrip < mp.mpf("1e-40")),
            "deuteron_O2_vanishes": bool(deuteron_O2 < mp.mpf("1e-45")),
            "a3_O2_nonzero": bool(borr_O2_norm > mp.mpf("0.001")),
            "trace_kills_O2": bool(borr_O2_trace < mp.mpf("1e-40")),
            "order3_trace_vanishes_two_letter_cyclicity": bool(tr_O1O2 < mp.mpf("1e-45")),
            # tr(Ω₁²Ω₂) ALSO vanishes: tr(S·[a,b]) = 0 for every symmetrized
            # degree-≤2 word S (only the antisymmetric part ab−ba pairs with the
            # commutator). The surviving order-4 term is tr(Ω₂²) (and tr(Ω₁Ω₃)).
            "order4_symmetrized_term_also_vanishes": bool(tr_O1sqO2 < mp.mpf("1e-45")),
            "order4_trace_O2sq_nonzero": bool(tr_O2sq > mp.mpf("1e-6")),
        },
    }


# ------------------------------------------------------------------------ forward layer
def forward_layer(q_str) -> dict:
    q = mp.mpf(q_str)
    m_e = mp.mpf(str(M_E_MEV))
    h = q - 1 / q
    hbar_q = 1 - 1 / q
    mu0 = m_e / (3 * h / 2)
    t = (q - 1) / (q + 1)

    def br(x):
        return (q**x - q**(-x)) / (q - 1 / q)

    AME = {"D": (6, mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))),
           "T": (9, mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION))),
           "3He": (9, mp.mpf(str(AME_B_HE3_MEV_VALIDATION))),
           "4He": (12, mp.mpf(str(AME_B_HE4_MEV_VALIDATION)))}

    table = {}
    for iso, (n, B) in AME.items():
        j = mp.mpf(n) / 2
        J = br(j) * br(j + 1)
        E_rot = mu0 * hbar_q * J          # canonical first-order (μ₀) form
        E_even = m_e * J / 3              # bar-even projection (h cancels; S5+S6)
        E_even_h2 = E_even * (1 + h**2)   # + unit-coefficient bar-even order-2 (near-match)
        table[iso] = {
            "E_rot_MeV": mp.nstr(E_rot, 8),
            "err_rot_pct": mp.nstr((E_rot / B - 1) * 100, 4),
            "needed_mult_corr_pct": mp.nstr((B / E_rot - 1) * 100, 4),
            "E_even_MeV": mp.nstr(E_even, 8),
            "err_even_pct": mp.nstr((E_even / B - 1) * 100, 4),
            "E_even_times_1p_h2_MeV": mp.nstr(E_even_h2, 8),
            "err_even_h2_pct": mp.nstr((E_even_h2 / B - 1) * 100, 4),
            "B_AME_MeV": mp.nstr(B, 8),
        }

    B_D = AME["D"][1]
    J_D = br(3) * br(4)
    E_even_D = m_e * J_D / 3
    E_rot_D = mu0 * hbar_q * J_D
    decomp_residual = abs(E_rot_D - E_even_D * (1 - t))
    g2_gap_measured = (B_D / E_even_D - 1) / h**2

    return {
        "q0_used": mp.nstr(q, 20),
        "ladder": {"h": mp.nstr(h, 12), "h2": mp.nstr(h**2, 12),
                   "h3": mp.nstr(h**3, 12), "t_bar_odd_impurity": mp.nstr(t, 12),
                   "x_vlevel": mp.nstr((mp.sqrt(q) - 1 / mp.sqrt(q))**2, 12),
                   "two_v_sq": mp.nstr(q + 2 + 1 / q, 12)},
        "mu0_MeV": mp.nstr(mu0, 10),
        "rotational_tier_forward": table,
        "deuteron_decomposition": {
            "E_rot_eq_Eeven_times_1_minus_t_residual": mp.nstr(decomp_residual, 5),
            "t_pct": mp.nstr(t * 100, 6),
            "bar_even_gap_pct": mp.nstr((B_D / E_even_D - 1) * 100, 6),
            "g2_gap_measured_equals_gap_over_h2": mp.nstr(g2_gap_measured, 8),
        },
        "_flags": {
            "decomp_exact": bool(decomp_residual < mp.mpf("1e-40")),
            "D_err_matches_canonical_witness": bool(
                abs((E_rot_D / B_D - 1) * 100 + mp.mpf("9.2")) < mp.mpf("0.15")),
            "g2_gap_near_unity_0p9_1p1": bool(mp.mpf("0.9") < g2_gap_measured < mp.mpf("1.1")),
            "A3_untouched": all(
                mp.mpf(table[iso]["err_even_h2_pct"]) < -35 for iso in ("T", "3He", "4He")),
        },
        "_g2gap": g2_gap_measured,
    }


def main() -> int:
    sym = symbolic_layer()
    q_env = Q_MP
    mat = matrix_layer(q_env)
    fwd_env = forward_layer(Q_50_DIGIT_STR)
    fwd_muon = forward_layer(Q0_MUON_STR)
    pin_delta_g2gap = abs(fwd_env["_g2gap"] - fwd_muon["_g2gap"])

    wb = WitnessBuilder("eunit-magnus-order2", engine="mpmath",
                        output_dir=str(_HERE))
    wb.set_description(
        "E_unit higher-order counit terms via NA-Stokes/Magnus order 2 (the deuteron −9.2%). "
        "PROVED structural results: (i) the deuteron 3-crossing channel word σ₁³ is "
        "single-generator, so the Magnus order-2 commutator Ω₂ = ½∮∮[A,A] (Phys.Rep.470 eq 32) "
        "VANISHES IDENTICALLY — exp(Ω₁) is exact and the −9.2% is NOT an inter-crossing "
        "Magnus effect; (ii) for every braid, trace functionals (Markov/Jones) and the 1-dim "
        "counit character kill Ω_k (k≥2, Lie elements) linearly, AND the order-3 trace term "
        "tr(Ω₁Ω₂) vanishes identically for every two-generator (B₃) word by cyclicity "
        "(tr(X[X,Y]) = tr(Y[X,Y]) = 0) — the first surviving inter-crossing trace correction "
        "is ORDER 4, automatically bar-EVEN, magnitude ~h⁴ ≈ 0.19% ≪ 9.2%; (iii) bar-parity "
        "grading: Magnus order k carries h^k with parity (−1)^k, "
        "h² = x·[2]_v² bar-EVEN. Forward decomposition of the −9.2%: E_rot = E⁺·(1−t) with "
        "bar-odd impurity t = (v−v⁻¹)/[2]_v ≈ 5.21% and bar-even gap on E⁺ = m_e·J_q²/3 of "
        "+4.41% ≈ h² (measured coefficient 1.008 — NEAR-MATCH, underived, not wired). "
        "E⁺·(1+h²) = 2.2238 MeV (−0.03%) for D; A≥3 untouched (−43/−38/−69%). The surviving "
        "order-2 candidates are per-crossing (octahedral e₂, PR #4127 route B) or the "
        "NA-Stokes surface-curvature pairing (surface data = wall). No fit; nothing closed.")
    wb.set_audit_only("docs/audits/2026-07-24-eunit-magnus-order2.md")
    wb.add_parameter("q0_env_pin", Q_50_DIGIT_STR)
    wb.add_parameter("q0_muon_canonical", Q0_MUON_STR)
    wb.add_parameter("pin_note",
                     "muon-vs-proton q0 differ ~11.5 ppb — immaterial at this audit's 1e-4 "
                     "relative scale; g2 gap-coefficient shift between pins recorded below")
    wb.add_data("symbolic", sym)
    wb.add_data("matrix_layer", {k: v for k, v in mat.items() if k != "_flags"})
    wb.add_data("forward_env_pin", {k: v for k, v in fwd_env.items()
                                    if k not in ("_flags", "_g2gap")})
    wb.add_data("forward_muon_pin_deuteron",
                fwd_muon["rotational_tier_forward"]["D"])
    wb.add_data("pin_robustness", {"g2_gap_shift_between_pins": mp.nstr(pin_delta_g2gap, 5)})
    wb.add_caveat(
        "NEAR-MATCH tier: the bar-even order-2 gap coefficient g2 (g for gap, owner-picked; NOT the Q_beta ladder c_k) ≈ 1.008 is measured forward, "
        "NOT derived. Deriving it (octahedral e₂ / surface-curvature term) is the open object. "
        "The parity projection E⁺ assumes the corpus mass-side bar-even discipline applies to "
        "the rotational tier — a structural assumption, stated, not proved.")
    wb.add_caveat(
        "Branch convention: log(−q⁻¹) taken on the principal branch (+iπ); the letter of "
        "σ⁻¹ is −log σ (path reversal), not the principal log of σ⁻¹. Fibre-level Im is "
        "permitted (archimedean Im(q₀)=0 constrains q, not the fibre log).")

    for name, flag in sym.items():
        wb.add_assertion(f"sym_{name}", computed=str(bool(flag)), expected="True")
    for name, flag in mat["_flags"].items():
        wb.add_assertion(f"mat_{name}", computed=str(bool(flag)), expected="True")
    for name, flag in fwd_env["_flags"].items():
        wb.add_assertion(f"fwd_{name}", computed=str(bool(flag)), expected="True")
    wb.add_assertion("pin_robust_g2_gap_shift_below_1e6",
                     computed=str(bool(pin_delta_g2gap < mp.mpf("1e-6"))), expected="True")
    # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
    # pins deliberately, so it belongs to neither anchor list. The stamp
    # carries the values ACTUALLY COMPUTED WITH, so the audit re-checks each
    # leg against its canonical pin instead of tautologically re-reading it.
    out = wb.save(q0_comparison(
        muon=mp.mpf(Q0_MUON_STR),
        proton=Q_MP,
        reason='measures the inter-crossing Magnus order-2 term at BOTH the environment (proton) pin and the muon pin, and reports g2_gap_shift_between_pins; both pins are read on purpose and each is reported under its own key',
    ))

    print("=== E_unit Magnus order-2 (NA-Stokes route A; complementary to #4127 route B) ===")
    print("symbolic:", sym)
    print("matrix:", mat["_flags"])
    print(f"  deuteron word sigma_1^3: max|Omega_2| = {mat['N2_deuteron_word_O2_maxabs']}  (EXACT 0)")
    print(f"  (s1 s2^-1)^3: |Omega_2| = {mat['N3_a3_word_O2_maxabs']}, tr Omega_2 = "
          f"{mat['N3_a3_word_trace_O2']}, tr(Omega_1 Omega_2) = {mat['N3_a3_word_trace_O1O2_order3']}"
          f" (two-letter cyclicity zero); order-4: tr(Omega_2^2) = {mat['N3_a3_word_trace_O2sq_order4']},"
          f" tr(Omega_1^2 Omega_2) = {mat['N3_a3_word_trace_O1sqO2_order4']}")
    d = fwd_env["rotational_tier_forward"]
    for iso in ("D", "T", "3He", "4He"):
        r = d[iso]
        print(f"  {iso:4s} E_rot {r['E_rot_MeV']} ({r['err_rot_pct']}%)  "
              f"E+ {r['E_even_MeV']} ({r['err_even_pct']}%)  "
              f"E+(1+h2) {r['E_even_times_1p_h2_MeV']} ({r['err_even_h2_pct']}%)")
    print("  deuteron decomposition:", fwd_env["deuteron_decomposition"])
    print("VERDICT: inter-crossing Magnus order-2 = 0 for the deuteron (proved); trace/counit "
          "kill all Omega_k (k>=2) linearly; order-3 trace term = 0 by two-letter cyclicity; "
          "first inter-crossing trace correction is order 4 (~h^4 = 0.19%) << 9.2%. "
          "Residual decomposes as bar-odd impurity t (5.21%) + bar-even gap ~ h^2 (g2 = "
          f"{mp.nstr(fwd_env['_g2gap'], 6)}, NEAR-MATCH, underived). A>=3 untouched. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
