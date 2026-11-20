#!/usr/bin/env python3
"""P3 (bean qou-99qc): beta-decay energy as a change of normal-form q-degree / Bruhat length.

Pre-registration: PREREGISTRATION.md (same directory), committed before this file.

Exact arithmetic in Q(q) (sympy) on the T_w basis of H_3(q), sigma^2 = h sigma + 1,
h = q - 1/q. The right-multiplication operators are the ones proved in Lean
(QOU/QBeta/NormalFormLengthInvariants.lean: act1, act2). Numbers at the proton pin,
70 dps, serialised with qou_substrate.precision.fmt. No scale is derived here:
the required scale per unit is REPORTED as a ratio to m_e, against two reference
values, as a comparison only.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at, M_E_MEV_STR  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

DPS = 70
Q_EXP_STR = "0.78233341"      # m_n - m_p - m_e, comparison only
Q_SCORED_STR = "0.325433929"  # T3 weight-split cell (PR #8586), comparison only

q = sp.symbols("q", positive=True)
h = q - 1 / q
LEN = [0, 1, 1, 2, 2, 3]          # e, s1, s2, s1s2, s2s1, s1s2s1
NAMES = ["e", "s1", "s2", "s1s2", "s2s1", "s1s2s1"]


def act(i, v):
    """Right multiplication by sigma_{i+1}; identical to Lean act1 / act2."""
    if i == 0:
        return [v[1], v[0] + h * v[1], v[4], v[5], v[2] + h * v[4], v[3] + h * v[5]]
    return [v[2], v[3], v[0] + h * v[2], v[1] + h * v[3], v[5], v[4] + h * v[5]]


def act_letter(c, d, i, v):
    """(c sigma_i + d) on the right."""
    a = act(i, v)
    return [sp.together(c * x + d * y) for x, y in zip(a, v)]


def ev(letters):
    v = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for c, d, i in letters:
        v = act_letter(c, d, i, v)
    return [sp.factor(sp.simplify(x)) for x in v]


SIG = lambda i: (1, 0, i)                    # noqa: E731
SIGINV = lambda i: (1, -h, i)                # noqa: E731  sigma^-1 = sigma - h


def word_to_letters(w):
    return [SIG(i) for i in w]


# ---------- rewrite-order dependence of the step count (contrast; R3 #8632) ----------
def reduce_count(word, strategy):
    terms = {tuple(word): sp.Integer(1)}
    nquad = 0
    while True:
        pick = None
        for w, c in terms.items():
            pos = [(k, "q") for k in range(len(w) - 1) if w[k] == w[k + 1]]
            pos += [(k, "b") for k in range(len(w) - 2) if w[k:k + 3] == (1, 0, 1)]
            if pos:
                pos.sort()
                pick = (w, c, pos[0] if strategy == "left" else pos[-1])
                break
        if pick is None:
            break
        w, c, (k, kind) = pick
        del terms[w]
        if kind == "q":
            nquad += 1
            out = [(w[:k] + w[k + 1:], c * h), (w[:k] + w[k + 2:], c)]
        else:
            out = [(w[:k] + (0, 1, 0) + w[k + 3:], c)]
        for nw, nc in out:
            terms[nw] = sp.simplify(terms.get(nw, 0) + nc)
            if terms[nw] == 0:
                del terms[nw]
    basis = {(): 0, (0,): 1, (1,): 2, (0, 1): 3, (1, 0): 4, (0, 1, 0): 5}
    vec = [sp.Integer(0)] * 6
    for w, c in terms.items():
        vec[basis[w]] += c
    return [sp.factor(x) for x in vec], nquad


# ---------- invariants ----------
def laurent_range(expr):
    expr = sp.together(sp.expand(expr))
    if expr == 0:
        return None
    num, den = sp.fraction(expr)
    pn = sp.Poly(sp.expand(num), q)
    pd = sp.Poly(sp.expand(den), q)
    assert len(pd.terms()) == 1, f"non-monomial denominator {den}"
    dd = pd.degree()
    degs = [m[0] for m, _ in pn.terms()]
    return (min(degs) - dd, max(degs) - dd)


def inv(v, q0):
    supp = [k for k in range(6) if sp.simplify(v[k]) != 0]
    chi = sp.factor(sp.simplify(sum(v[k] * q ** LEN[k] for k in range(6))))
    chis = sp.factor(sp.simplify(sum(v[k] * (-1 / q) ** LEN[k] for k in range(6))))
    rngs = [laurent_range(v[k]) for k in supp]
    vals = [mp.mpf(sp.lambdify(q, v[k], "mpmath")(q0)) for k in range(6)]
    return {
        "nf": {NAMES[k]: str(v[k]) for k in supp},
        "support": len(supp),
        "leadLen": max(LEN[k] for k in supp),
        "minLen": min(LEN[k] for k in supp),
        "coef_qdeg_min": min(r[0] for r in rngs),
        "coef_qdeg_max": max(r[1] for r in rngs),
        "chi": chi, "chi_range": laurent_range(chi), "chi_sign": chis,
        "A1": sum(abs(x) for x in vals),                                   # sum |c|
        "N": sum(abs(vals[k]) * q0 ** LEN[k] for k in range(6)),          # sum |c| q^l
        "E_gs": sum(abs(vals[k]) * LEN[k] for k in range(6)),             # thm:groebner-shirshov-energy
    }


def tensor(a, b):
    """Invariants of a (x) b on disjoint strands (parabolic product: lengths add)."""
    return {
        "support": a["support"] * b["support"],
        "leadLen": a["leadLen"] + b["leadLen"], "minLen": a["minLen"] + b["minLen"],
        "coef_qdeg_min": a["coef_qdeg_min"] + b["coef_qdeg_min"],
        "coef_qdeg_max": a["coef_qdeg_max"] + b["coef_qdeg_max"],
        "chi": sp.factor(a["chi"] * b["chi"]), "chi_sign": sp.factor(a["chi_sign"] * b["chi_sign"]),
        "A1": a["A1"] * b["A1"], "N": a["N"] * b["N"],
        "E_gs": a["E_gs"] * b["A1"] + a["A1"] * b["E_gs"],
    }


def h2_inv(word_len, q0):
    """sigma^k in H_2 (basis e, s; lengths 0, 1). Returns invariants of the trefoil etc."""
    a, b = sp.Integer(1), sp.Integer(0)        # a e + b s
    for _ in range(word_len):
        a, b = b, sp.expand(a + h * b)         # (a + b s) s = b + (a + h b) s
    v = [sp.factor(a), sp.factor(b)]
    supp = [k for k in range(2) if sp.simplify(v[k]) != 0]
    vals = [mp.mpf(sp.lambdify(q, x, "mpmath")(q0)) for x in v]
    rngs = [laurent_range(v[k]) for k in supp]
    chi = sp.factor(v[0] + v[1] * q)
    return {"nf": {"e": str(v[0]), "s": str(v[1])}, "support": len(supp),
            "leadLen": max(supp), "minLen": min(supp),
            "coef_qdeg_min": min(r[0] for r in rngs), "coef_qdeg_max": max(r[1] for r in rngs),
            "chi": chi, "chi_sign": sp.factor(v[0] - v[1] / q),
            "A1": abs(vals[0]) + abs(vals[1]), "N": abs(vals[0]) + abs(vals[1]) * q0,
            "E_gs": abs(vals[1])}


UNIT = {"support": 1, "leadLen": 0, "minLen": 0, "coef_qdeg_min": 0, "coef_qdeg_max": 0,
        "chi": sp.Integer(1), "chi_sign": sp.Integer(1), "A1": mp.mpf(1), "N": mp.mpf(1), "E_gs": mp.mpf(0)}


def main() -> int:
    mp.mp.dps = DPS
    q0 = q_at(DPS)
    me = mp.mpf(M_E_MEV_STR)
    lnq = mp.log(q0)
    checks = []

    # contrast: one word, two strategies
    T35 = (0, 1) * 5
    nfL, nL = reduce_count(T35, "left")
    nfR, nR = reduce_count(T35, "right")
    nfE = ev(word_to_letters(T35))
    same = all(sp.simplify(a - b) == 0 for a, b in zip(nfL, nfR)) and \
        all(sp.simplify(a - b) == 0 for a, b in zip(nfL, nfE))
    checks.append(("T35: left/right rewrite and Lean act give one normal form", same))
    checks.append(("T35: quadratic-step count is order dependent (R3: 25 vs 30)", nL != nR))

    # Lean statements, re-checked
    V3 = ev([SIG(0), SIGINV(1)] * 3)
    chiV3 = sp.simplify(sum(V3[k] * q ** LEN[k] for k in range(6)))
    checks.append(("lenWeighted(V^3) = 1 (Lean lenWeighted_V3)", chiV3 == 1))

    # elements
    from pyhecke.atom import nucleon_word_letters
    PL = ev([(c, d, g) for c, d, g in nucleon_word_letters(["u", "u", "d"], q=q)])
    NL = ev([(c, d, g) for c, d, g in nucleon_word_letters(["u", "d", "d"], q=q)])
    PS = [0, -h / 2, 0, 1, 0, 0]
    NS = [h ** 2 / 2, -h, -h / 2, 1, 0, 0]
    dS = [sp.simplify(a - b) for a, b in zip(NS, PS)]
    checks.append(("short model: n - p = Delta_S = (h^2/2, -h/2, -h/2, 0,0,0)",
                   all(sp.simplify(a - b) == 0 for a, b in zip(dS, [h**2/2, -h/2, -h/2, 0, 0, 0]))))
    els = {"p_short": inv(PS, q0), "n_short": inv(NS, q0), "p_long": inv(PL, q0), "n_long": inv(NL, q0),
           "V3": inv(V3, q0)}
    lep = {"trefoil_sigma1^3_H2": h2_inv(3, q0), "gg_sigma1sigma2sigma1_H3": inv(ev(word_to_letters((0, 1, 0))), q0)}

    models = {"short": ("n_short", "p_short"), "long": ("n_long", "p_long"), "V3_both": ("V3", "V3")}
    rows = {}
    for mname, (ni, pi) in models.items():
        for lname, L in lep.items():
            init = tensor(els[ni], UNIT)
            fin = tensor(tensor(els[pi], L), UNIT)
            r = {}
            for key in ("support", "leadLen", "minLen", "coef_qdeg_min", "coef_qdeg_max"):
                r["d_" + key] = fin[key] - init[key]
            ratio = sp.factor(sp.simplify(fin["chi"] / init["chi"]))
            r["chi_ratio"] = str(ratio)
            r["chi_ratio_monomial"] = bool(sp.Poly(sp.fraction(sp.together(ratio))[0], q).is_monomial and
                                           sp.Poly(sp.fraction(sp.together(ratio))[1], q).is_monomial)
            rv = mp.mpf(sp.lambdify(q, ratio, "mpmath")(q0))
            r["dlogq_chi_q0"] = mp.log(abs(rv)) / lnq if rv != 0 else None
            r["dlogq_N_q0"] = mp.log(fin["N"] / init["N"]) / lnq
            r["d_E_gs_q0"] = fin["E_gs"] - init["E_gs"]
            # nucleon-only differences (lepton removed)
            r["nucleon_only_d_leadLen"] = els[pi]["leadLen"] - els[ni]["leadLen"]
            r["nucleon_only_chi_p_minus_n"] = str(sp.factor(sp.simplify(els[pi]["chi"] - els[ni]["chi"])))
            r["nucleon_only_d_E_gs_q0"] = els[pi]["E_gs"] - els[ni]["E_gs"]
            rows[f"{mname}|{lname}"] = r

    # required scale per unit (comparison only)
    Qe, Qs = mp.mpf(Q_EXP_STR), mp.mpf(Q_SCORED_STR)
    E0 = me / (q0 * (q0 - 1))
    req = {}
    for k, r in rows.items():
        for key in ("d_leadLen", "dlogq_chi_q0", "dlogq_N_q0", "d_E_gs_q0", "nucleon_only_d_E_gs_q0"):
            dv = r[key]
            if dv is None or dv == 0:
                req[f"{k}|{key}"] = None
                continue
            dv = mp.mpf(dv)
            req[f"{k}|{key}"] = {"delta": dv,
                                  "kappa_over_me_Qexp": Qe / (abs(dv) * me),
                                  "kappa_over_me_Qscored": Qs / (abs(dv) * me),
                                  "kappa_over_E0_Qexp": Qe / (abs(dv) * E0)}

    # checks on pre-registered predictions
    checks.append(("P-c: V3 nucleon-only Delta = 0 for every invariant",
                   rows["V3_both|trefoil_sigma1^3_H2"]["nucleon_only_d_leadLen"] == 0 and
                   rows["V3_both|trefoil_sigma1^3_H2"]["nucleon_only_chi_p_minus_n"] == "0" and
                   rows["V3_both|trefoil_sigma1^3_H2"]["nucleon_only_d_E_gs_q0"] == 0))
    checks.append(("P-d: short-model chi(p) - chi(n) = h(q+1/q)/2 (Lean lenWeighted_nucN_sub_nucP)",
                   sp.simplify(els["p_short"]["chi"] - els["n_short"]["chi"] - h * (q + 1 / q) / 2) == 0))
    checks.append(("P-d: leading Bruhat length equal for n and p in every model",
                   all(els[a]["leadLen"] == els[b]["leadLen"] for a, b in models.values())))
    # post-registration observation (not pre-registered): chi(p)/chi(n) in the typed models
    for m in ("short", "long"):
        rr = sp.simplify(els["p_" + m]["chi"] / els["n_" + m]["chi"])
        checks.append((f"post-reg: chi(p)/chi(n) = q^2 in the {m} typed model", sp.simplify(rr - q**2) == 0))
    # post-registration: can ONE linear scale kappa on the chi q-degree give both
    # m_n - m_p > 0 (neutron heavier) and m_e > 0? deg(p) - deg(n) = +2 and deg(e) = +3:
    # E = kappa*deg needs kappa < 0 for the nucleons and kappa > 0 for the electron.
    sign_conflict = True
    for m in ("short", "long"):
        dn = sp.simplify(sp.log(els["p_" + m]["chi"] / els["n_" + m]["chi"]) / sp.log(q))
        sign_conflict &= bool(dn > 0)
    checks.append(("post-reg: chi-degree sign conflict (proton higher q power but lighter; electron "
                   "higher q power and massive) in both typed models", sign_conflict))

    # ---------- print ----------
    print(f"T35 quadratic steps: leftmost {nL}, rightmost {nR}; normal forms agree: {same}")
    for k, v in {**els, **lep}.items():
        print(f"{k:28s} supp={v['support']} lead={v['leadLen']} min={v['minLen']} "
              f"coefdeg=[{v['coef_qdeg_min']},{v['coef_qdeg_max']}] chi={v['chi']} "
              f"N={mp.nstr(v['N'], 12)} E_gs={mp.nstr(v['E_gs'], 12)}")
    for k, r in rows.items():
        print(k, {kk: (mp.nstr(vv, 12) if isinstance(vv, mp.mpf) else vv) for kk, vv in r.items()})
    for k, v in req.items():
        if v:
            print("required", k, {kk: mp.nstr(vv, 12) for kk, vv in v.items()})
    for n, ok in checks:
        print(("PASS " if ok else "FAIL ") + n)

    def ser(x):
        if isinstance(x, mp.mpf):
            return fmt(x)
        if isinstance(x, (sp.Basic,)):
            return str(x)
        if isinstance(x, dict):
            return {k: ser(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [ser(v) for v in x]
        return x

    from witness_base import WitnessBuilder
    wb = WitnessBuilder("qbeta-p3-nf-qdegree-energy", engine="mpmath+sympy",
                        output_dir=Path(__file__).resolve().parent)
    wb.set_description(
        "P3 of bean qou-99qc. Energy of n -> p e- nubar read off rewrite-order-independent invariants "
        "of the H3(q) normal form (leading Bruhat length, coefficient q-degree range, length-weighted "
        "functional chi = sum c_w q^l(w) = index character, length-weighted norm, corpus "
        "thm:groebner-shirshov-energy E = sum |c_w| l(w)). Required scale per unit reported as a ratio "
        "to m_e, comparison only; nothing is wired.")
    wb.add_data("q0_anchor", "proton")
    wb.add_data("q0", fmt(q0))
    wb.add_data("T35_quadratic_steps", {"leftmost": nL, "rightmost": nR, "same_normal_form": same})
    wb.add_data("elements", ser({k: {kk: vv for kk, vv in v.items()} for k, v in {**els, **lep}.items()}))
    wb.add_data("deltas", ser(rows))
    wb.add_data("required_scale_comparison_only", ser(req))
    wb.add_data("reference_Q_MeV_comparison_only", {"experimental": Q_EXP_STR, "scored_cell_8586": Q_SCORED_STR})
    for n, ok in checks:
        wb.add_assertion(name=n, computed=str(int(bool(ok))), expected="1", tolerance=0, source="sympy exact Q(q)")
    wb.add_caveat("The lepton states (trefoil sigma1^3 in H2; sigma1 sigma2 sigma1 in H3) and the disjoint-strand "
                  "tensor product for the final state are model choices recorded in PREREGISTRATION.md, not derived.")
    wb.add_caveat("No scale per unit q-degree or length is derived. kappa columns are comparisons only.")
    out = wb.save()
    print("witness:", out)
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
