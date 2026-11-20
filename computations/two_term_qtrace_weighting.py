#!/usr/bin/env python3
"""Two-term charge insertion on the nucleon weight spaces under the DERIVED quantum-trace weighting.

Library + producer. Writes `two-term-qtrace-weighting.witness.json` when run.

What is derived (bean qou-99qc, 2026-11-19 05:10Z/05:15Z; owner "A" + "derive instead of 4 choices")
-------------------------------------------------------------------------------------------------
Convention D's Markov trace IS the U_q(sl2) quantum trace on V^{⊗n}:

    tr_M(x) = Tr(K^{⊗n} x) / [2]_q^n,     K = diag(q, q⁻¹) per strand,   [2]_q = q + q⁻¹,

checked here symbolically on one crossing: Tr(K⊗K Ř)/[2]_q² = q³/(q²+1) = z_D. K commutes with
the braid, so on a weight space W of total weight 2T³ the weight is the scalar q^{2T³}:
q on the proton space W_p = (2,1) and q⁻¹ on the neutron space W_n = (1,2). Hence, for an
insertion X on the 3-dim weight spaces of `NucleonWeightSpaceTwoTerm.lean`,

    t_X(W_p) = q · tr(X_p V_p³) / [2]_q³,     t_X(W_n) = q⁻¹ · tr(X_n V_n³) / [2]_q³.

This CLOSES the #8518 weighting menu {plain, KnKp, Kp3, q}. The normalisation is the quantum
dimension [2]_q³ of V^{⊗3} (= 8 at q = 1), not the 1/3 = 1/dim W of the menu entries.

Relation to the old menu (exact in q, `symbolic_map()` below)
------------------------------------------------------------
On the CONNECTED adjacent insertion (static (−2/9)·1 removed from W_n, the object every menu
entry acts on):  'KnKp' = ([2]_q³ / 3) · Δt_derived^{conn}  exactly.  So KnKp has the derived
WEIGHT but the wrong NORMALISATION (1/3 instead of 1/[2]_q³; ratio (q²+1)³/(3q³) = 8/3 at q=1).
'plain', 'Kp3' and 'q' are not proportional to it. On the RAW adjacent insertion (the
pre-registered rule, no connected subtraction) KnKp differs additionally by the static term
(2/27)·q⁻¹·tr(V³).

What is NOT fixed by the corpus (reported side by side, none chosen by residual)
-------------------------------------------------------------------------------
* the insertion: adjacent Q₁₂+Q₂₃ (pre-registered; not braid-covariant, #8552 T2/T3) vs the
  permutation-complete Q₁₂+Q₂₃+Q₁₃ (covariant projection, #8552 T6; static, its connected part
  is identically 0, cf. #8557/#8565);
* raw (pre-registered) vs connected (what the compute scored);
* the overall sign: the pre-registered rule is Δ_EM := +m_e·[t(W_n) − t(W_p)]; the compute's
  connected rows used −m_e·t throughout (|·| on the proton term), selected against the μ–p target
  (2026-11-18 audit, "Control-Neg-1: sign-flipped control doubles tension").
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

LEAN_MODULE = "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm"

#: The one canonical weighting. Menu names are accepted only as labelled historical comparisons.
DERIVED = "derived"
HISTORICAL_WEIGHTINGS = ("plain", "KnKp", "Kp3", "q")
VALID_WEIGHTINGS = (DERIVED,) + HISTORICAL_WEIGHTINGS

#: Sign convention of the compute's connected rows (mass contribution = −m_e · trace).
#: The pre-registered rule uses +1. Not fixed by the corpus for the connected insertion.
COMPUTE_CONNECTED_SIGN = -1
PREREGISTERED_SIGN = +1


# ── exact closed forms (q symbolic → mpmath); Lean names in comments ───────────────────────────

def _P(q):
    q2 = q * q
    return q2**6 - 3 * q2**5 + 3 * q2**4 - 5 * q2**3 + 3 * q2**2 - 3 * q2 + 1


def tr_v3(q):
    """tr(V_p³) = tr(V_n³) = −P(q)/q⁶  (`trace_borromeanV3A`, `trace_borromeanV3B`)."""
    return -_P(q) / q**6


def tr_adj_p(q):
    """tr((Q₁₂+Q₂₃)_p V_p³) = −2(q²−1)⁴(q⁴+q²+1)/(9q⁶)  (`trace_QAdjp_borromeanV3`)."""
    q2 = q * q
    return -2 * (q2 - 1) ** 4 * (q2**2 + q2 + 1) / (9 * q2**3)


def tr_adj_n(q):
    """tr((Q₁₂+Q₂₃)_n V_n³)  (`trace_QAdjn_borromeanV3`)."""
    q2 = q * q
    return (4 * q2**6 - 15 * q2**5 + 24 * q2**4 - 32 * q2**3 + 24 * q2**2 - 15 * q2 + 4) / (9 * q2**3)


def tr_adj_n_conn(q):
    """tr((Q₁₂+Q₂₃)_n V_n³) + (2/9) tr(V_n³) = (q²−1)⁴(2q⁴−q²+2)/(9q⁶)
    (`trace_QAdjn_borromeanV3_connected`)."""
    q2 = q * q
    return (q2 - 1) ** 4 * (2 * q2**2 - q2 + 2) / (9 * q2**3)


def tr_all_p(q):
    """tr((Q₁₂+Q₂₃+Q₁₃)_p V_p³) = 0  (`QPairP_eq_sum`: Q_pair = 0 on W_p)."""
    return mp.mpf(0) * q


def tr_all_n(q):
    """tr((Q₁₂+Q₂₃+Q₁₃)_n V_n³) = −(1/3) tr(V³)  (`QPairN_eq_sum`)."""
    return -tr_v3(q) / 3


def qdim_v3(q):
    """[2]_q³ = (q + q⁻¹)³, the quantum dimension of V^{⊗3}."""
    return (q + 1 / q) ** 3


# ── derived weight-space traces t(W) = Tr_W(K^{⊗3} X V³)/[2]_q³ ─────────────────────────────────

def t_weight(q, nucleon: str, insertion: str = "adjacent", connected: bool = False):
    """t_X(W_N) under the derived quantum-trace weighting.

    insertion ∈ {'adjacent', 'all_pairs'}; connected removes the static scalar part of the
    neutron insertion (−2/9 for adjacent, −1/3 for all-pairs; the proton parts are traceless).
    """
    if nucleon == "p":
        raw = tr_adj_p(q) if insertion == "adjacent" else tr_all_p(q)
        k = q
    elif nucleon == "n":
        if insertion == "adjacent":
            raw = tr_adj_n_conn(q) if connected else tr_adj_n(q)
        elif insertion == "all_pairs":
            raw = (tr_all_n(q) + tr_v3(q) / 3) if connected else tr_all_n(q)
        else:
            raise ValueError(f"unknown insertion {insertion!r}")
        k = 1 / q
    else:
        raise ValueError(f"unknown nucleon {nucleon!r}")
    if insertion not in ("adjacent", "all_pairs"):
        raise ValueError(f"unknown insertion {insertion!r}")
    return k * raw / qdim_v3(q)


def delta_t(q, insertion: str = "adjacent", connected: bool = False):
    """t(W_n) − t(W_p) under the derived weighting."""
    return t_weight(q, "n", insertion, connected) - t_weight(q, "p", insertion, connected)


# ── the compute's connected adjacent quantity, per weighting (derived default) ─────────────────

def connected_trace_p(q, weighting: str = DERIVED):
    """Proton connected adjacent trace as the compute weights it.

    derived : q·tr((Q₁₂+Q₂₃)_p V_p³)/[2]_q³
    plain   : (1/3)·tr(...)          (historical comparison)
    Kp      : (q/3)·tr(...)          (historical comparison; the old `k_weighted=True`)
    """
    base = tr_adj_p(q)
    if weighting == DERIVED:
        return q * base / qdim_v3(q)
    if weighting == "plain":
        return base / 3
    if weighting in ("Kp", "KnKp", "Kp3", "q"):
        return q * base / 3
    raise ValueError(f"unknown proton weighting {weighting!r}; expected derived/plain/Kp")


def connected_trace_diff(q, weighting: str = DERIVED):
    """Δtr_conn = t_conn(W_n) − t_conn(W_p) of the connected adjacent insertion."""
    tp3 = tr_adj_p(q) / 3
    tn3 = tr_adj_n_conn(q) / 3
    if weighting == DERIVED:
        return delta_t(q, "adjacent", connected=True)
    if weighting == "plain":
        return tn3 - tp3
    if weighting == "KnKp":
        return tn3 / q - q * tp3
    if weighting == "Kp3":
        return tn3 - q * tp3
    if weighting == "q":
        return q * (tn3 - tp3)
    raise ValueError(f"unknown weighting {weighting!r}; expected one of {VALID_WEIGHTINGS}")


def m_p_qed_conn_mev(q, m_e, weighting: str = DERIVED):
    """M_p^{QED,conn} in the compute's sign convention: −m_e · t_conn(W_p) (= m_e·|t|, t < 0)."""
    return COMPUTE_CONNECTED_SIGN * m_e * connected_trace_p(q, weighting)


def delta_m_qed_conn_mev(q, m_e, weighting: str = DERIVED):
    """Δm_QED^{conn} in the compute's sign convention: −m_e · Δtr_conn."""
    return COMPUTE_CONNECTED_SIGN * m_e * connected_trace_diff(q, weighting)


def delta_em_charge_insertion_mev(q, m_e, insertion: str = "adjacent"):
    """Pre-registered rule (05:10Z): Δ_EM := +m_e·[t(W_n) − t(W_p)], raw insertion, derived weight."""
    return PREREGISTERED_SIGN * m_e * delta_t(q, insertion, connected=False)


# ── exact symbolic map (sympy) ────────────────────────────────────────────────────────────────

def symbolic_map() -> dict:
    """Exact-in-q identities, each asserted. Returns their printed forms."""
    import sympy as sp

    q = sp.symbols("q", positive=True)
    qi = 1 / q
    h = q - qi
    A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
    A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
    B1 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
    B2 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
    V3A = (A1 * A2.inv()) ** 3
    V3B = (B1 * B2.inv()) ** 3
    R = sp.Rational
    Q12p, Q23p, Q13p = (sp.diag(R(4, 9), R(-2, 9), R(-2, 9)), sp.diag(R(-2, 9), R(-2, 9), R(4, 9)),
                        sp.diag(R(-2, 9), R(4, 9), R(-2, 9)))
    Q12n, Q23n, Q13n = (sp.diag(R(-2, 9), R(-2, 9), R(1, 9)), sp.diag(R(1, 9), R(-2, 9), R(-2, 9)),
                        sp.diag(R(-2, 9), R(1, 9), R(-2, 9)))
    two3 = (q + qi) ** 3
    zero = lambda e: sp.simplify(e) == 0  # noqa: E731

    # weighting derivation: one crossing, Ř on C²⊗C² (basis uu, ud, du, dd), K = diag(q, 1/q)
    Rc = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
    KK = sp.diag(q * q, 1, 1, qi * qi)
    zD = q**3 / (q**2 + 1)
    assert zero((KK * Rc).trace() / (q + qi) ** 2 - zD), "Tr(K⊗K Ř)/[2]² ≠ z_D"

    T = sp.factor(sp.simplify(V3A.trace()))
    Pp = sp.simplify(((Q12p + Q23p) * V3A).trace())
    Nn = sp.simplify(((Q12n + Q23n) * V3B).trace())
    Cn = sp.simplify(Nn + R(2, 9) * V3B.trace())
    assert zero(V3B.trace() - V3A.trace())
    # cross-check the closed forms used numerically above
    for lam, ex in ((tr_v3, T), (tr_adj_p, Pp), (tr_adj_n, Nn), (tr_adj_n_conn, Cn)):
        assert zero(lam(q) - ex), lam.__name__

    D_adj = sp.factor(sp.simplify((qi * Nn - q * Pp) / two3))
    D_conn = sp.factor(sp.simplify((qi * Cn - q * Pp) / two3))
    allp = ((Q12p + Q23p + Q13p) * V3A).trace()
    alln = ((Q12n + Q23n + Q13n) * V3B).trace()
    D_all = sp.factor(sp.simplify((qi * alln - q * allp) / two3))
    D_all_conn = sp.simplify((qi * (alln + R(1, 3) * V3B.trace()) - q * allp) / two3)
    assert zero(D_all_conn), "all-pairs connected part is not 0"
    target_adj = (2 * q**14 - 2 * q**12 - 9 * q**10 + 20 * q**8 - 26 * q**6 + 18 * q**4
                  - 13 * q**2 + 4) / (9 * q**4 * (q**2 + 1) ** 3)
    assert zero(D_adj - target_adj), "pre-registered closed form not reproduced"
    assert sp.limit(D_adj, q, 1) == R(-1, 12)
    assert sp.limit(D_all, q, 1) == R(-1, 8)

    tp3, tn3 = Pp / 3, Cn / 3
    menu = {"plain": tn3 - tp3, "KnKp": tn3 / q - q * tp3, "Kp3": tn3 - q * tp3, "q": q * (tn3 - tp3)}
    ratio_knkp = sp.factor(sp.simplify(menu["KnKp"] / D_conn))
    assert zero(ratio_knkp - (q**2 + 1) ** 3 / (3 * q**3)), "KnKp ∝ derived-connected failed"
    knkp_minus_raw = sp.factor(sp.simplify(menu["KnKp"] - two3 / 3 * D_adj))
    assert zero(knkp_minus_raw - R(2, 27) * qi * T)
    proportional = {}
    for k, v in menu.items():
        r = sp.simplify(v / D_conn)
        proportional[k] = bool(sp.simplify(sp.diff(r * q**3 / (q**2 + 1) ** 3, q)) == 0)
    assert proportional == {"plain": False, "KnKp": True, "Kp3": False, "q": False}
    ratio_p = sp.simplify((q * Pp / two3) / (Pp / 3))
    assert zero(ratio_p - 3 * q**4 / (q**2 + 1) ** 3)
    # Q13 identity of #8552 T3 on this word
    assert zero(((Q13p) * V3A).trace() + Pp)

    return {
        "check_weighting": "Tr(K⊗K Ř)/[2]_q² = q³/(q²+1) = z_D (asserted symbolically)",
        "tr_V3": str(T),
        "Delta_t_adjacent_raw": str(D_adj),
        "Delta_t_adjacent_raw_q1_limit": "-1/12",
        "Delta_t_adjacent_connected": str(D_conn),
        "Delta_t_all_pairs_raw": str(D_all),
        "Delta_t_all_pairs_raw_q1_limit": "-1/8",
        "Delta_t_all_pairs_connected": "0",
        "t_p_adjacent": str(sp.factor(sp.simplify(q * Pp / two3))),
        "t_n_adjacent_raw": str(sp.factor(sp.simplify(qi * Nn / two3))),
        "menu_vs_derived_connected": {
            "KnKp_over_derived": str(ratio_knkp),
            "KnKp_minus_[2]^3/3_times_derived_raw": str(knkp_minus_raw),
            "proportional_to_derived_connected": proportional,
        },
        "proton_derived_over_plain": str(sp.factor(ratio_p)),
    }


# ── producer ────────────────────────────────────────────────────────────────────────────────

def main() -> int:
    import _path_bridge  # noqa: F401
    from qou_substrate.precision import COMPUTE_DPS
    from _precision import fmt
    from codata_constants import M_E_MEV
    from qou_substrate.constants import q_at

    sym = symbolic_map()
    mp.mp.dps = COMPUTE_DPS
    q = q_at(COMPUTE_DPS)
    m_e = mp.mpf(str(M_E_MEV))
    kev = mp.mpf(1000)

    rows = {}
    for ins in ("adjacent", "all_pairs"):
        for conn in (False, True):
            key = f"{ins}_{'connected' if conn else 'raw'}"
            tp = t_weight(q, "p", ins, conn)
            tn = t_weight(q, "n", ins, conn)
            d = tn - tp
            rows[key] = {
                "t_W_p": fmt(tp, 40),
                "t_W_n": fmt(tn, 40),
                "Delta_t": fmt(d, 40),
                "Delta_EM_preregistered_sign_keV": fmt(PREREGISTERED_SIGN * m_e * d * kev, 30),
                "Delta_EM_compute_sign_keV": fmt(COMPUTE_CONNECTED_SIGN * m_e * d * kev, 30),
                "M_p_preregistered_sign_keV": fmt(PREREGISTERED_SIGN * m_e * tp * kev, 30),
                "M_p_compute_sign_keV": fmt(COMPUTE_CONNECTED_SIGN * m_e * tp * kev, 30),
            }
    menu = {}
    for w in VALID_WEIGHTINGS:
        menu[w] = {
            "Delta_m_QED_conn_keV": fmt(delta_m_qed_conn_mev(q, m_e, w) * kev, 30),
            "label": "CANONICAL (derived quantum trace)" if w == DERIVED else "historical comparison",
        }
    mp_conn = {w: fmt(m_p_qed_conn_mev(q, m_e, w) * kev, 30) for w in (DERIVED, "plain", "Kp")}

    pre = delta_em_charge_insertion_mev(q, m_e, "adjacent")
    # Recorded 2026-11-19 05:15Z at the proton pin (bean qou-99qc); reproduced here.
    assert abs(delta_t(q, "adjacent") - mp.mpf("-0.0734705048628237")) < mp.mpf("1e-15")
    assert abs(pre - mp.mpf("-0.0375433509")) < mp.mpf("1e-9")

    witness = {
        "computation": "two-term-qtrace-weighting",
        "description": (
            "Two-term charge insertion on the nucleon weight spaces under the DERIVED weighting "
            "t(W) = Tr_W(K^{⊗3} X V³)/[2]_q³ (convention D's Markov trace = U_q(sl2) quantum trace). "
            "Closes the #8518 weighting menu. Insertion (adjacent vs all-pairs), raw vs connected "
            "and the overall sign are NOT fixed by the corpus and are reported side by side."),
        "script": "computations/two_term_qtrace_weighting.py",
        "lean_module": LEAN_MODULE,
        "lean_theorems": [
            "deltaT_adjacent_raw_eq", "deltaT_adjacent_connected_eq", "deltaT_allPairs_raw_eq",
            "knkp_eq_qdim_div_three_mul_deltaT_connected"],
        "bean": "qou-99qc",
        "q0Anchor": "proton",
        "q0Value": fmt(q, 60),
        "m_e_MeV": fmt(m_e, 30),
        "dps": COMPUTE_DPS,
        "symbolic": sym,
        "preregistered_rule": {
            "rule": "Delta_EM := +m_e·[t(W_n) − t(W_p)], adjacent Q12+Q23, raw, derived weight",
            "preregistered_at": "2026-11-19T05:10Z",
            "Delta_t": fmt(delta_t(q, "adjacent"), 40),
            "Delta_EM_MeV": fmt(pre, 30),
            "Delta_EM_all_pairs_MeV": fmt(delta_em_charge_insertion_mev(q, m_e, "all_pairs"), 30),
            "lattice_comparison_only": "EM part of m_n − m_p ≈ −0.6 to −1.0 MeV (not a target)",
        },
        "by_insertion": rows,
        "connected_adjacent_Delta_m_by_weighting": menu,
        "connected_adjacent_M_p_by_weighting_keV": mp_conn,
        "not_fixed_by_corpus": [
            "insertion: adjacent Q12+Q23 (pre-registered, not braid-covariant #8552) vs all-pairs",
            "raw (pre-registered) vs connected (the compute's scored object)",
            "overall sign: +m_e·t (pre-registered) vs −m_e·t (compute connected rows, selected)",
        ],
    }
    out = _HERE / "two-term-qtrace-weighting.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"Delta_EM_MeV": witness["preregistered_rule"]["Delta_EM_MeV"],
                      "menu": menu, "M_p": mp_conn}, indent=1, ensure_ascii=False))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
