#!/usr/bin/env python3
"""Two-term QED: is there a DERIVED term, and where would any proton-only term pin q₀?

Owner instruction 2026-11-20: "Derive to make two-term primary". Companion to
`QOU/BraidsAndKnots/QEDHigherOrderCovariance.lean` (this branch), which proves:

  * every covariant local insertion, to ALL orders, is a per-pair scalar rescaling
    (or the mirror), and its exact factor on V³ = (σ₁σ₂⁻¹)³ is 1;
  * the naive photon-exchange double crossing sum is not braid-covariant; its
    completion is S²/2 = 0 on V³;
  * no degree-≤2 (order-α) charge weight couples to the alternating Milnor μ̄₁₂₃.

This probe (a) recomputes the V³ crossing data EXACTLY (Fraction), for proton and
neutron charges, including the non-covariant double sum the Lean shows is not an
invariant; and (b) evaluates, at mp.dps = 70, the three q-pins the corpus's own
closed forms define — the substrate proton identity, the muon identity and the
α_em form-B tower — to answer the joint question independent of any QED term:
a correction that acts ONLY on the proton identity moves q₀ along one line, and
m_μ and α_em⁻¹ are single-valued in q.

No fitting: nothing here chooses a coefficient. The 'relative coupling a needed'
figure is reported as the size a scalar would have to have, and is NOT matched
against any candidate (α, α², α³, …) — doing so would be selection against the
target.

All values mpmath / Fraction; no float on a value path. q-pins solved by
findroot from the closed forms, CODATA read from the registry.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402
from qou_substrate import codata as C  # noqa: E402

mp.mp.dps = 70
mf = mp.mpf

# ── (a) exact V³ crossing data ─────────────────────────────────────────────
BOR = [(0, 1), (1, -1), (0, 1), (1, -1), (0, 1), (1, -1)]
PROTON = {0: Fr(2, 3), 1: Fr(2, 3), 2: Fr(-1, 3)}
NEUTRON = {0: Fr(2, 3), 1: Fr(-1, 3), 2: Fr(-1, 3)}


def letters(word, pos):
    pos = list(pos)
    out = []
    for i, e in word:
        a, b = pos[i], pos[i + 1]
        out.append((a, b, e))
        pos[i], pos[i + 1] = b, a
    return out, pos


def crossing_data(Q, word):
    ls, perm = letters(word, [0, 1, 2])
    w = [e * Q[a] * Q[b] for a, b, e in ls]
    S = sum(w, Fr(0))
    Sq = sum((x * x for x in w), Fr(0))
    D = sum((w[i] * w[j] for i in range(len(w)) for j in range(i + 1, len(w))), Fr(0))
    pairs = {(min(a, b), max(a, b)): 0 for a, b, _ in ls}
    for a, b, e in ls:
        pairs[(min(a, b), max(a, b))] += e
    return {"pairs_exchanged": [(a, b, e) for a, b, e in ls], "final_perm": perm,
            "crossSum": {f"{k[0]}{k[1]}": v for k, v in pairs.items()},
            "S_colored_writhe": S, "Sq": Sq, "D_double_sum": D, "check_2D_plus_Sq_eq_S2": 2 * D + Sq == S * S}


def u1_coloured_exponents(Q, word):
    """U(1)-coloured invariant (QEDHigherOrderCovariance §U), exact.

    The central U(1) R-matrix rescales each letter by t^(e·Q_a·Q_b); the closure adds a
    ribbon-twist factor θ^(Q_c²·w_c) per component c, w_c the self-writhe.  Returns the exact
    exponent of t (= coloured writhe S) and the per-component self-writhes, so the full
    charge dependence is t^S · Π θ^(Q_c² w_c)."""
    ls, perm = letters(word, [0, 1, 2])
    # components of the closure: orbits of the strand permutation (label at slot i -> perm[i])
    comp = {}
    for start in range(3):
        if start in comp:
            continue
        x = start
        while x not in comp:
            comp[x] = start
            x = perm.index(x) if perm.count(x) else x
    t_exp = sum((e * Q[a] * Q[b] for a, b, e in ls), Fr(0))
    selfw = {c: sum(e for a, b, e in ls if comp[a] == c and comp[b] == c) for c in set(comp.values())}
    theta_exp = sum((Q[c] ** 2 * w for c, w in selfw.items()), Fr(0))
    return {"final_perm": perm, "components": sorted(set(comp.values())),
            "t_exponent": t_exp, "self_writhe": selfw, "theta_exponent": theta_exp}


# ── (b) the three q-pins ──────────────────────────────────────────────────
R_PE = mf(C.codata("proton-electron mass ratio").value_str)
R_MUE = mf(C.codata("muon-electron mass ratio").value_str)
AINV = mf(C.codata("inverse fine-structure constant").value_str)
ME_KEV = mf(C.codata("electron mass energy equivalent in MeV").value_str) * 1000
VOL41 = 2 * mp.clsin(2, mp.pi / 3)  # Vol(4_1) = 2·Cl₂(π/3) = 6Λ(π/3)


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def mu_ratio(q):  # m_μ/m_e = Vol(4₁)/ℏ_q², ℏ_q = 1 − q⁻¹
    return VOL41 / (1 - 1 / q) ** 2


def trM_bor(q):  # |tr_M(β_Bor)| (BorromeanMarkovTrace.lean closed form)
    h = q - 1 / q
    return abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def fbor_term(q):  # 2·(m_μ/m_e)·|tr_M|·[3]_q!/q³ — the F_Bor (QCD) term in m_e units
    return 2 * mu_ratio(q) * trM_bor(q) * qb(3, q) * qb(2, q) / q ** 3


def mp_ratio(q):  # m_p/m_e = F_Bor term − 12 (substrate identity, m_p_substrate_identity_50dps.py)
    return fbor_term(q) - 12


def ainv_formB(q):  # alpha_em_schwinger_ladder_probe.py form B
    h2 = (q - 1 / q) ** 2
    T = q * qb(9, q) * qb(10, q) + mf(8) / (12 * mp.pi)
    H = qb(2, q) / (8 * mp.pi)
    roots = mp.polyroots([-H * h2, H, T, -1], maxsteps=200, extraprec=200)
    a = min([mp.re(r) for r in roots if abs(mp.im(r)) < mf(10) ** -60 and mp.re(r) > 0],
            key=lambda r: abs(r - mf("0.0073")))
    return 1 / a


def qbeta_dln_dlnq(q):  # per_observable_100x_status._qbeta_dln_dlnq (Form-A base, closed form)
    return q * ((2 * q - 2) / (q ** 2 - 2 * q - 1) + 1 / (q + 1) - 3 / q)


def ppb(x, ref):
    return (x - ref) / ref * mf(10) ** 9


def main() -> int:
    wb = WitnessBuilder("two-term-qed-derivation-joint-pin", engine="mpmath")
    wb.set_description(
        "Owner 2026-11-20 'derive to make two-term primary'. (a) exact V3 crossing data for "
        "proton/neutron charges: coloured writhe S = 0 for both, so every covariant local "
        "insertion (all orders, QEDHigherOrderCovariance.lean) leaves tr(V3) unchanged; the "
        "naive double sum D = -Sq/2 is nonzero but not braid-covariant. (b) the three q-pins "
        "from the corpus closed forms: proton identity, muon identity, alpha_em form B. "
        "alpha_em pins within 0.053 ppb of the proton pin; the muon pin sits +11.61 ppb away. "
        "A proton-only term can move q0 toward the muon pin but alpha_em^-1 then misses by "
        "+79 ppb: no single q satisfies m_mu and alpha_em together under these forms. "
        "Scope (a): conditional on the alpha_em form B (structurally motivated, not derived; "
        "alpha_em itself conditional on the Witten-kappa sorry).")

    data_a = {}
    for name, Q in (("proton", PROTON), ("neutron", NEUTRON)):
        d = crossing_data(Q, BOR)
        print(f"{name}: S={d['S_colored_writhe']}  Sq={d['Sq']}  D={d['D_double_sum']}  "
              f"crossSum={d['crossSum']}  2D+Sq==S^2: {d['check_2D_plus_Sq_eq_S2']}")
        data_a[name] = {k: (str(v) if isinstance(v, Fr) else v) for k, v in d.items()}
    # R2 non-invariance of D (prefix σ₁σ₁⁻¹), exact
    for name, Q in (("proton", PROTON), ("neutron", NEUTRON)):
        d0 = crossing_data(Q, BOR)["D_double_sum"]
        d1 = crossing_data(Q, [(0, 1), (0, -1)] + BOR)["D_double_sum"]
        print(f"{name}: D(V3)={d0}  D(σ1σ1⁻¹·V3)={d1}  shift={d1 - d0} = -(Q0Q1)^2 = {-(Q[0]*Q[1])**2}")
        data_a[name]["D_shift_under_R2_prefix"] = str(d1 - d0)
    data_a["degree_zero"] = {
        "proton_sumQ2": str(sum(v * v for v in PROTON.values())),
        "proton_sumQaQb": str(PROTON[0] * PROTON[1] + PROTON[0] * PROTON[2] + PROTON[1] * PROTON[2]),
        "neutron_sumQ2": str(sum(v * v for v in NEUTRON.values())),
        "neutron_sumQaQb": str(NEUTRON[0] * NEUTRON[1] + NEUTRON[0] * NEUTRON[2] + NEUTRON[1] * NEUTRON[2]),
    }
    wb.add_data("v3_crossing_data_exact", data_a)

    # (c) U(1)-coloured invariant: charge dependence on V3 (all orders) and controls
    data_c = {}
    for name, Q in (("proton", PROTON), ("neutron", NEUTRON)):
        for wname, word in (("V3", BOR), ("hopf_control", [(0, 1), (0, 1)]),
                            ("sigma1_cubed_control", [(0, 1), (0, 1), (0, 1)])):
            d = u1_coloured_exponents(Q, word)
            print(f"U(1) {name} {wname}: t^{d['t_exponent']} theta^{d['theta_exponent']} "
                  f"selfW={d['self_writhe']} perm={d['final_perm']}")
            data_c[f"{name}_{wname}"] = {"t_exponent": str(d["t_exponent"]),
                                         "theta_exponent": str(d["theta_exponent"]),
                                         "self_writhe": {str(k): v for k, v in d["self_writhe"].items()},
                                         "final_perm": d["final_perm"]}
    data_c["verdict"] = ("On V3 both exponents are exactly 0 for proton and neutron, so the "
                         "U(1)-coloured trace equals the uncoloured trace for every t, theta: the "
                         "coefficient of every charge monomial (Q0Q1Q2*mubar^2, sumQ^2, sumQaQb) "
                         "is 0 in this class. Controls (Hopf, sigma1^3) are nonzero.")
    wb.add_data("u1_coloured_invariant_exact", data_c)

    q_p = mp.findroot(lambda q: mp_ratio(q) - R_PE, mf(Q_50_DIGIT_STR))
    q_mu = mp.findroot(lambda q: mu_ratio(q) - R_MUE, q_p)
    q_al = mp.findroot(lambda q: ainv_formB(q) - AINV, q_p)
    pins = {"proton_identity": q_p, "muon_identity": q_mu, "alpha_em_formB": q_al}
    rows = {}
    for name, q in pins.items():
        r = {"q": fmt(q, 50),
             "dq_vs_proton_ppb": fmt(ppb(q, q_p), 20),
             "m_p_resid_ppb": fmt(ppb(mp_ratio(q), R_PE), 20),
             "m_mu_resid_ppb": fmt(ppb(mu_ratio(q), R_MUE), 20),
             "alpha_inv_resid_ppb": fmt(ppb(ainv_formB(q), AINV), 20),
             "Q_beta_shift_vs_proton_pin_ppb_formA_sensitivity":
                 fmt(qbeta_dln_dlnq(q_p) * ppb(q, q_p), 20)}
        rows[name] = r
        print(f"pin {name:16s} q={mp.nstr(q, 25)}  dq={mp.nstr(ppb(q, q_p), 8)} ppb  "
              f"m_p {mp.nstr(ppb(mp_ratio(q), R_PE), 8)}  m_mu {mp.nstr(ppb(mu_ratio(q), R_MUE), 8)}  "
              f"alpha^-1 {mp.nstr(ppb(ainv_formB(q), AINV), 8)} ppb")
    gap_kev = (mp_ratio(q_mu) - R_PE) * ME_KEV
    a_needed = -(mp_ratio(q_mu) - R_PE) / fbor_term(q_mu)
    sens = {f"dln_{n}_dlnq": fmt(mp.diff(lambda x: mp.log(f(mp.exp(x))), mp.log(q_p)), 20)
            for n, f in (("m_p", mp_ratio), ("m_mu", mu_ratio), ("alpha_inv", ainv_formB))}
    sens["dln_Qbeta_dlnq_formA"] = fmt(qbeta_dln_dlnq(q_p), 20)
    print(f"m_p(q_mu) - CODATA = {mp.nstr(gap_kev, 12)} keV;  scalar on F_Bor needed a = {mp.nstr(a_needed, 12)}")
    print("sensitivities", sens)
    wb.add_data("pins", rows)
    wb.add_data("sensitivities_at_proton_pin", sens)
    wb.add_data("proton_only_term", {
        "m_p_at_muon_pin_minus_codata_keV": fmt(gap_kev, 20),
        "F_Bor_term_at_proton_pin_keV": fmt(fbor_term(q_p) * ME_KEV, 20),
        "scalar_relative_coupling_needed_a": fmt(a_needed, 20),
        "note": ("a scalar (topology-independent) insertion rescales the whole F_Bor term "
                 "(scalar_insertion_shift); it is degenerate with q0 on the proton alone. "
                 "The figure is the size required, NOT matched to any candidate."),
    })
    wb.add_assertion("alpha_pin_near_proton_pin", computed=fmt(abs(ppb(q_al, q_p)), 12),
                     expected="0", tolerance="0.1", source="|q_alpha - q_p| < 0.1 ppb")
    wb.add_assertion("muon_pin_far_from_alpha_pin", computed=("1" if abs(ppb(q_mu, q_al)) > 10 else "0"),
                     expected="1", tolerance="0.5", source="|q_mu - q_alpha| > 10 ppb")
    wb.add_assertion("colored_writhe_zero_both_nucleons",
                     computed=("1" if data_a["proton"]["S_colored_writhe"] == "0"
                               and data_a["neutron"]["S_colored_writhe"] == "0" else "0"),
                     expected="1", tolerance="0.5", source="exact Fraction")
    wb.add_assertion("u1_coloured_charge_independent_on_V3",
                     computed=("1" if all(data_c[f"{n}_V3"]["t_exponent"] == "0"
                                          and data_c[f"{n}_V3"]["theta_exponent"] == "0"
                                          for n in ("proton", "neutron")) else "0"),
                     expected="1", tolerance="0.5", source="exact Fraction; QEDHigherOrderCovariance.u1Trace_borromean")
    wb.add_assertion("u1_controls_see_charges",
                     computed=("1" if data_c["proton_hopf_control"]["t_exponent"] != "0"
                               and data_c["proton_sigma1_cubed_control"]["theta_exponent"] != "0" else "0"),
                     expected="1", tolerance="0.5", source="negative controls (Hopf, sigma1^3)")
    wb.save(q0_comparison(
        muon=q_mu, proton=q_p,
        reason="the subject is where each closed form pins q0: the probe solves the proton, "
               "muon and alpha_em form-B identities itself and reports every pin under its own key"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
