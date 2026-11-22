#!/usr/bin/env python3
"""Electron word, option 1 (σ₀σ₁σ₀) vs option 2 (σ₀³): downstream measurements.

Owner ruling 2026-11-21: option 1 (e⁻ = σ₀σ₁σ₀, closure = Hopf link) is the
ruling for now; option 2 (e⁻ = σ₀³ ∈ B₂, closure trefoil in B₂) is the
documented backup. This probe MEASURES both side by side. It chooses
nothing, edits no producer and writes no witness. Nothing is compared with
experiment.

Conventions (AGENTS.md):
  Hecke   σᵢ² = h σᵢ + 1, h = q − q⁻¹;  σᵢ⁻¹ = σᵢ − h.
  Photon  γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹   (owner ruling 2026-11-20).
  Trace   convention D, z = q³/(q²+1).
  q₀      proton pin, q_parameter.Q_MP.
Arithmetic: sympy over ℚ(q). mpmath only to evaluate exact expressions at q₀
(70 dps) and inside the LP of knot_operator_lp_selection, which is an mpmath
basis-enumeration solver by construction (imported, not edited).

Sections
  A(i)   γγ → e⁻e⁺ channel under each option (corpus basis, and the
         change-of-basis readings option 2 would need)
  A(ii)  annihilation normal forms
  A(iii) Compton-type products γX, Xγ, [γ, X]
  A(iv)  β-decay "e⁻ deficit" reading on the free-neutron-decay nucleon NFs
  A(v)   PSD reading 3 (χ_λ(X) ≥ 0 on blocks with y_λ > 0 at z_D)
  A(vi)  tr_D and Jones
  A(vii) photon_operator_table e⁻ pair counts, re-run under option 2
  B      number-moving consumers: positron/electron LP, confinement
         candidate, H₂O trace excess, Markov-trace electron row
  C      consistency of "leptons in H₂" with option 1

Run:
    python3 -u computations/probes/electron_word_options_downstream_probe.py 2>&1 | tee /tmp/ewo.log

# Ref: [kassel2008] Kassel & Turaev, Braid Groups, §4 (Iwahori–Hecke algebra,
#      standard basis T_w, Ocneanu trace, reduced Burau representation).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

# ── exact H₃(q) model: reuse the merged GS-interaction probe (PR #8724) ─────
_spec = importlib.util.spec_from_file_location(
    "ewgs", COMP / "probes" / "electron_word_gs_interactions_probe.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

q, h, z = E.q, E.h, E.z
elem, mul, add, unit, in_P, support, trace, is_zero = (
    E.elem_of_word, E.mul, E.add, E.unit, E.in_P, E.support, E.trace, E.is_zero)
NAMES = E.NAMES
f0, f1, f01, p0, p1, p01 = E.f0, E.f1, E.f01, E.p0, E.p1, E.p01
photon = E.photon

import mpmath as mp  # noqa: E402
mp.mp.dps = 70
from q_parameter import Q_MP  # noqa: E402
Q0 = mp.mpf(Q_MP)
Q0_RAT = sp.Rational(mp.nstr(Q0, 70))


def at_q0(expr):
    """Evaluate an exact ℚ(q) expression at the proton q₀ (end-of-chain only)."""
    return mp.mpf(str(sp.N(sp.sympify(expr).subs(q, Q0_RAT), 60)))


def fz(v):
    return [sp.factor(sp.simplify(x)) for x in v]


OPT = {
    "opt1": {"word": (1, 2, 1), "name": "σ₀σ₁σ₀"},
    "opt2": {"word": (1, 1, 1), "name": "σ₀³"},
}
for o in OPT.values():
    o["X"] = elem(o["word"])
    o["Cw"] = tuple(-L for L in o["word"])
    o["CX"] = elem(o["Cw"])

K2 = h**2 + 1  # σ₀³ = h·1 + (h²+1)·σ₀


def to_basis_s0cubed(v):
    """Coordinates in B' = {1, σ₀³, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}: σ₀ = (σ₀³ − h)/(h²+1)."""
    a = [sp.simplify(x) for x in v]
    c = a[1] / K2
    return [sp.factor(a[0] - h * c), sp.factor(c)] + [sp.factor(x) for x in a[2:]]


def to_basis_s1cubed(v):
    """B'' = {1, σ₀, σ₁³, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀} (the σ₁³ = X4 embedding)."""
    a = [sp.simplify(x) for x in v]
    c = a[2] / K2
    return [sp.factor(a[0] - h * c), sp.factor(a[1]), sp.factor(c)] + [sp.factor(x) for x in a[3:]]


def section(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def main():
    out = {}
    # sanity: σ₀³ = h + (h²+1)σ₀
    s03 = OPT["opt2"]["X"]
    assert is_zero(add(s03, [h, K2, 0, 0, 0, 0], -1))
    assert is_zero(add(to_basis_s0cubed(s03), [0, 1, 0, 0, 0, 0], -1))
    print("sanity: σ₀³ = h·1 + (h²+1)·σ₀ ;  B'-coordinates of σ₀³ = e₁  OK")

    # ── A(i) γγ → e⁻ e⁺ ─────────────────────────────────────────────────
    section("A(i)  γγ → e⁻e⁺: what defines the e⁻ channel")
    G = mul(photon(f0, f1, f01), photon(p0, p1, p01))
    G = [sp.factor(sp.expand(x)) for x in G]
    ch1 = G[5]
    Gp = to_basis_s0cubed(G)
    Gpp = to_basis_s1cubed(G)
    g1 = to_basis_s0cubed(photon(f0, f1, f01))
    print(f"  opt1 channel (corpus): coeff of σ₀σ₁σ₀ in NF(γγ) = {ch1}")
    print(f"  opt2, corpus basis   : σ₀³ is not a basis word; it lies in the photon span P -> UNDEFINED")
    print(f"  opt2, basis B' (σ₀→σ₀³): σ₀³-coordinate of γγ = {Gp[1]}")
    print(f"  opt2, basis B'' (σ₁→σ₁³): σ₁³-coordinate of γγ = {Gpp[2]}   (different: basis choice is a free choice)")
    print(f"  opt2, B': σ₀³-coordinate of ONE photon γ(φ) = {g1[1]}   (a single photon already 'contains e⁻')")
    print(f"  B' leaves the σ₀σ₁σ₀ coordinate unchanged: {sp.simplify(Gp[5] - ch1) == 0}")
    out["Ai"] = {"opt1_channel": str(ch1), "opt2_Bprime": str(Gp[1]),
                 "opt2_Bdoubleprime": str(Gpp[2]), "opt2_single_photon_Bprime": str(g1[1])}

    # ── A(ii) annihilation ──────────────────────────────────────────────
    section("A(ii) e⁻e⁺ annihilation normal forms")
    for k, o in OPT.items():
        X, CX = o["X"], o["CX"]
        r = {"XC": fz(mul(X, CX)), "CX_X": fz(mul(CX, X)), "sum": fz(add(X, CX)),
             "C(X)": fz(CX)}
        print(f"  {k} {o['name']}:  C(X) = {r['C(X)']}")
        print(f"     X·C(X) = {r['XC']}   C(X)·X = {r['CX_X']}")
        print(f"     X + C(X) = {r['sum']}   in P: {in_P(r['sum'])}")
        out.setdefault("Aii", {})[k] = {kk: [str(x) for x in vv] for kk, vv in r.items()}
        out["Aii"][k]["sum_in_P"] = in_P(r["sum"])

    # ── A(iii) Compton ──────────────────────────────────────────────────
    section("A(iii) Compton-type γX, Xγ, [γ, X]   (γ = γ(φ₀, φ₁, φ₀₁))")
    g = photon(f0, f1, f01)
    for k, o in OPT.items():
        X = o["X"]
        gX = fz(mul(g, X))
        Xg = fz(mul(X, g))
        com = fz(add(gX, Xg, -1))
        sol = sp.solve([sp.numer(sp.together(c)) for c in com if c != 0], [f0, f1, f01], dict=True)
        print(f"  {k} {o['name']}:")
        print(f"     NF(γX) support {support(gX)}   in P: {in_P(gX)}")
        print(f"     NF(Xγ) support {support(Xg)}   in P: {in_P(Xg)}")
        print(f"     [γ,X] = {com}")
        print(f"     [γ,X] = 0 solutions in φ: {sol}")
        out.setdefault("Aiii", {})[k] = {"gX_support": support(gX), "Xg_support": support(Xg),
                                         "gX_in_P": in_P(gX), "Xg_in_P": in_P(Xg),
                                         "commutator": [str(c) for c in com],
                                         "commuting_photons": [{str(a): str(b) for a, b in s.items()} for s in sol]}

    # ── A(iv) β-decay reading ───────────────────────────────────────────
    section("A(iv) β-decay 'e⁻ deficit' reading on free-neutron-decay nucleon NFs")
    W = json.loads((COMP / "free-neutron-decay.witness.json").read_text())
    order = ["ν", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
    nuc = {}
    for n in ("neutron", "proton"):
        d = {t["particle"]: sp.sympify(t["coefficient_symbolic"], locals={"q": q})
             for t in W[n]["nf_terms"]}
        nuc[n] = [d[p] for p in order]
    # independent recomputation: B₃ · typed crossings, B₃ = (σ₀σ₁⁻¹)³
    B3 = elem((1, -2, 1, -2, 1, -2))

    def cross(a, b, gen):
        s = elem((gen + 1,))
        if a == b == "u":
            return s
        sh = h if a == b == "d" else h / 2
        return add(s, [sh, 0, 0, 0, 0, 0], -1)

    recompute = {}
    for n, qs in (("proton", "uud"), ("neutron", "udd")):
        e = B3
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            e = mul(e, cross(qs[i], qs[j], min(i, j, 1)))
        recompute[n] = fz(e)
        match = is_zero(add(recompute[n], nuc[n], -1))
        print(f"  {n}: recomputed B₃·(typed crossings) equals witness symbolic NF: {match}")
        if not match:
            print(f"     recomputed {recompute[n]}\n     witness    {fz(nuc[n])}")
    rows = {}
    for n in ("neutron", "proton"):
        v = nuc[n]
        b = to_basis_s0cubed(v)
        rows[n] = {"opt1_e": sp.factor(v[5]), "opt2_Bprime_e": sp.factor(b[1]),
                   "opt2_Bprime_1": sp.factor(b[0])}
        print(f"  {n}: opt1 e⁻ coeff = {rows[n]['opt1_e']}  @q₀ {mp.nstr(at_q0(v[5]), 15)}")
        print(f"        opt2 (B') σ₀³ coeff = {rows[n]['opt2_Bprime_e']}  @q₀ {mp.nstr(at_q0(b[1]), 15)}")
    d1 = sp.factor(rows["neutron"]["opt1_e"] - rows["proton"]["opt1_e"])
    d2 = sp.factor(rows["neutron"]["opt2_Bprime_e"] - rows["proton"]["opt2_Bprime_e"])
    dnu1 = sp.factor(nuc["neutron"][0] - nuc["proton"][0])
    dnu2 = sp.factor(to_basis_s0cubed(nuc["neutron"])[0] - to_basis_s0cubed(nuc["proton"])[0])
    print(f"  Δe (n−p): opt1 {mp.nstr(at_q0(d1), 15)}   opt2(B') {mp.nstr(at_q0(d2), 15)}")
    print(f"  Δν=Δ(1-coeff) (n−p): opt1 {mp.nstr(at_q0(dnu1), 15)}   opt2(B') {mp.nstr(at_q0(dnu2), 15)}")
    print(f"  witness transition.delta_e = {W['transition']['delta_e']} (float64 record)")
    s1 = {n: mp.sign(at_q0(rows[n]["opt1_e"])) for n in rows}
    s2 = {n: mp.sign(at_q0(rows[n]["opt2_Bprime_e"])) for n in rows}
    print(f"  sign of e-channel @q₀: opt1 {s1}   opt2(B') {s2}  ('deficit' = negative)")
    debt1 = abs(at_q0(dnu1)) + abs(at_q0(d1))
    debt2 = abs(at_q0(dnu2)) + abs(at_q0(d2))
    print(f"  beta-decay-energy-scale Scenario 4 denominator |Δν|+|Δe|: opt1 {mp.nstr(debt1, 15)}  opt2(B') {mp.nstr(debt2, 15)}")
    out["Aiv"] = {
        "recompute_matches_witness": {n: is_zero(add(recompute[n], nuc[n], -1)) for n in recompute},
        "opt1": {n: str(rows[n]["opt1_e"]) for n in rows},
        "opt2_Bprime": {n: str(rows[n]["opt2_Bprime_e"]) for n in rows},
        "delta_e_opt1_q0": mp.nstr(at_q0(d1), 20), "delta_e_opt2_q0": mp.nstr(at_q0(d2), 20),
        "delta_nu_opt1_q0": mp.nstr(at_q0(dnu1), 20), "delta_nu_opt2_q0": mp.nstr(at_q0(dnu2), 20),
        "scenario4_den_opt1": mp.nstr(debt1, 20), "scenario4_den_opt2": mp.nstr(debt2, 20),
        "sign_opt1": {k: int(v) for k, v in s1.items()}, "sign_opt2": {k: int(v) for k, v in s2.items()},
    }

    # ── A(v) PSD reading 3 ──────────────────────────────────────────────
    section("A(v) PSD reading 3: χ_λ(X) ≥ 0 on blocks with y_λ > 0 at z_D")
    t = q**-2
    M0 = sp.Matrix([[-t, 1], [0, 1]]) * q
    M1 = sp.Matrix([[1, 0], [t, -t]]) * q
    for M in (M0, M1):
        assert sp.simplify(M * M - h * M - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(M0 * M1 * M0 - M1 * M0 * M1) == sp.zeros(2)
    print("  2-dim rep (rescaled reduced Burau, t = q⁻²): Hecke + braid relations OK")

    def rep(word, which):
        if which == "3":
            return sp.Matrix([[sp.prod([q if L > 0 else -1 / q for L in word])]])
        if which == "111":
            return sp.Matrix([[sp.prod([-1 / q if L > 0 else q for L in word])]])
        R = sp.eye(2)
        for L in word:
            Mi = M0 if abs(L) == 1 else M1
            R = R * (Mi if L > 0 else Mi.inv())
        return R

    dims = {"3": 1, "21": 2, "111": 1}
    # y_λ from tr_D = Σ y_λ χ_λ on the six basis words
    ys = sp.symbols("y3 y21 y111")
    eqs = []
    for k, w in enumerate(E.BASIS_WORDS):
        sw = tuple(i + 1 for i in w)
        eqs.append(sum(y * rep(sw, lam).trace() for y, lam in zip(ys, ("3", "21", "111"))) - E.TR[k])
    ysol = sp.solve(eqs, ys, dict=True)
    assert len(ysol) == 1
    ysol = {k: sp.factor(v) for k, v in ysol[0].items()}
    print(f"  y_λ at z_D: {ysol}")
    yq0 = {str(k): mp.nstr(at_q0(v), 15) for k, v in ysol.items()}
    print(f"  y_λ @q₀: {yq0}")
    psd = {}
    for k, o in OPT.items():
        for tag, w in (("X", o["word"]), ("C(X)", o["Cw"])):
            chis = {lam: sp.factor(sp.simplify(rep(w, lam).trace())) for lam in dims}
            v0 = {lam: at_q0(c) for lam, c in chis.items()}
            active = [lam for lam, y in zip(("3", "21", "111"), ys) if at_q0(ysol[y]) > 0]
            ok = all(v0[lam] >= 0 for lam in active)
            print(f"  {k} {tag}: χ = {chis}")
            print(f"        @q₀ { {l: mp.nstr(v, 12) for l, v in v0.items()} }  active blocks {active}  reading-3 PASS: {ok}")
            psd[f"{k}_{tag}"] = {"chi": {l: str(c) for l, c in chis.items()},
                                 "chi_q0": {l: mp.nstr(v, 20) for l, v in v0.items()},
                                 "active": active, "pass": ok}
    out["Av"] = {"y": {str(k): str(v) for k, v in ysol.items()}, "y_q0": yq0, "psd": psd}

    # ── A(vi) tr_D and Jones ────────────────────────────────────────────
    section("A(vi) tr_D (convention D) and Jones of the closures")
    for k, o in OPT.items():
        trX = trace(o["X"])
        trC = trace(o["CX"])
        J3 = sp.factor(E.jones(o["word"], 3))
        n2 = 2 if k == "opt2" else 3
        J = sp.factor(E.jones(o["word"] if k == "opt1" else (1, 1, 1), n2))
        print(f"  {k}: tr_D(X) = {trX} @q₀ {mp.nstr(at_q0(trX), 15)};  tr_D(C X) = {trC}")
        print(f"        Jones closure in B₃: {J3} (components {E.components(o['word'])});  in natural B_n: {J}")
        out.setdefault("Avi", {})[k] = {"trD": str(trX), "trD_q0": mp.nstr(at_q0(trX), 20),
                                        "trD_C": str(trC), "jones_B3": str(J3), "jones_natural": str(J)}

    # ── A(vii) photon_operator_table e⁻ pair counts ─────────────────────
    section("A(vii) photon_operator_table e⁻ pair counts (b_i·T·b_j), exact")
    basis = [elem(tuple(i + 1 for i in w)) for w in E.BASIS_WORDS]
    pc = {}
    for k, o in OPT.items():
        n_w0, n_bp = 0, 0
        for i in range(6):
            for j in range(6):
                v = mul(mul(basis[i], o["X"]), basis[j])
                if sp.simplify(v[5]) != 0:
                    n_w0 += 1
                if sp.simplify(to_basis_s0cubed(v)[1]) != 0:
                    n_bp += 1
        pc[k] = {"sigma0sigma1sigma0_coeff_nonzero": n_w0, "Bprime_sigma0cubed_coeff_nonzero": n_bp}
        print(f"  T = {o['name']}: pairs with σ₀σ₁σ₀-coeff ≠ 0: {n_w0}/36;  pairs with B' σ₀³-coeff ≠ 0: {n_bp}/36")
    print("  (photon_operator_table pins T_{2,3} = σ₀σ₁σ₀ at 36; the T_{2,5} row is out of scope here)")
    out["Avii"] = pc

    # ── B number-moving consumers ───────────────────────────────────────
    section("B  number-moving consumers, recomputed under option 2 (no witness overwritten)")
    # B1 LP of prop:knot-operator-lp-selection
    sys.path.insert(0, str(COMP))
    import knot_operator_lp_selection as K  # noqa: E402
    P = K.gram_quotient_pinv_mp(K.DPS, q=K.Q)
    S_cols, tcost = [], []
    for name, word, _ in K.FAMILY:
        S_cols.append(K.nf_of_signed_word(word))
        tcost.append(K.crossing_energy(word))
    Mmat = [[mp.fsum(P[i][j] * S_cols[o][j] for j in range(6)) for o in range(len(K.FAMILY))]
            for i in range(6)]
    lp_targets = {
        "opt1 positron σ₀⁻¹σ₁⁻¹σ₀⁻¹": [(0, -1), (1, -1), (0, -1)],
        "opt1 electron σ₀σ₁σ₀": [(0, 1), (1, 1), (0, 1)],
        "opt2 positron σ₀⁻³": [(0, -1)] * 3,
        "opt2 electron σ₀³": [(0, 1)] * 3,
        "opt2' positron σ₁⁻³": [(1, -1)] * 3,
    }
    lp = {}
    for tn, tw in lp_targets.items():
        c = K.nf_of_signed_word(tw)
        nT = [-x if x < 0 else mp.mpf(0) for x in c]
        r = K.solve_block_lp(Mmat, nT, tcost)
        rec = {"nf": [mp.nstr(x, 15) for x in c], "n_T": [mp.nstr(x, 15) for x in nT],
               "feasible": r["feasible"]}
        if r["feasible"]:
            rec["primal"] = mp.nstr(r["primal_obj"], 20)
            rec["gap"] = mp.nstr(r["duality_gap"], 3)
            rec["active"] = [K.FAMILY[o][0] for o in range(len(K.FAMILY)) if r["x"][o] > K.TOL]
            rec["tight"] = [K.NF_NAMES[i] for i in range(6) if r["y"][i] > K.TOL]
        else:
            rec["farkas"] = None if r.get("farkas_value") is None else mp.nstr(r["farkas_value"], 15)
        lp[tn] = rec
        print(f"  LP {tn}: {rec}")
    out["B_lp"] = lp

    # B2 confinement-operator-selection candidate "e⁻" applied to typed crossings
    conf = {}
    for k, o in OPT.items():
        for n, qs in (("proton", "uud"), ("neutron", "udd")):
            e = o["X"]
            for (i, j) in ((0, 1), (0, 2), (1, 2)):
                e = mul(e, cross(qs[i], qs[j], min(i, j, 1)))
            net = sp.factor(sum(e))
            conf[f"{k}_{n}"] = {"nf_q0": [mp.nstr(at_q0(x), 12) for x in e],
                                "net_q0": mp.nstr(at_q0(net), 15)}
            print(f"  confinement candidate e⁻={o['name']} · typed crossings, {n}: "
                  f"NF@q₀ {conf[f'{k}_{n}']['nf_q0']}  net {conf[f'{k}_{n}']['net_q0']}")
    out["B_conf"] = conf

    # B3 H₂O trace excess tr_D(lone) − tr_D(σ)
    for k, o in OPT.items():
        d = sp.factor(trace(o["X"]) - z)
        out.setdefault("B_h2o", {})[k] = {"delta_tr": str(d), "q0": mp.nstr(at_q0(d), 15),
                                          "frac": mp.nstr(at_q0(d / z), 15)}
        print(f"  H₂O Δtr = tr_D(lone={o['name']}) − z = {d}  @q₀ {mp.nstr(at_q0(d), 15)}  (frac {mp.nstr(at_q0(d / z), 10)})")
    # trivial-character weight used by the molecular angle tables
    for k, o in OPT.items():
        print(f"  molecular 'lone ↦ q^ℓ' weight (trivial character): {k} χ_(3) = {sp.factor(rep(o['word'], '3').trace())}")

    # ── C leptons in H₂ ─────────────────────────────────────────────────
    section("C  'H₂(q) (leptons)' vs each option")
    for k, o in OPT.items():
        inH2 = all(sp.simplify(o["X"][i]) == 0 for i in (2, 3, 4, 5))
        print(f"  {k} {o['name']} lies in H₂ = span{{1, σ₀}} ⊂ H₃: {inH2}")
        out.setdefault("C", {})[k] = inH2

    print("\nJSON-SUMMARY")
    print(json.dumps(out, ensure_ascii=False, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
