#!/usr/bin/env python3
"""ε-L1V (bean qou-99qc): does the photon's own vertex channel V = σ₀σ₁⁻¹ break u↔d?

Pre-registered in PREREGISTRATION.md (this directory, commit bc02ecd75c) before this
file was run. Re-asks ε-L1 (gg_twist_channel_np_probe.py, which used L± = σ₀σ₁^{±1})
of the ruled photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ (QOU/Photon.lean).

Elements are given in the ALGEBRA convention: ρ(xy) = ρ(x)ρ(y), so ρ(V) = ρ(σ₀)ρ(σ₁)⁻¹
(the same as #8586's V8 = S1·S2⁻¹ and Photon.lean). The ε-L1 probe instead applies the
letter list [1, -2] in order, i.e. the operator ρ(σ₁⁻¹)ρ(σ₀); that row is kept, labelled
"V (ε-L1 applied order)", for comparison with the ε-L1 witness.

F1  ε-L1's functional verbatim: multiplicity_trace_epsilon_probe.Mmat, ε_tr = Tr M(X·Δ_S)/Tr M(X),
    n→p and p→n. Asymmetry: t_pn − t_np for the numerator and denominator traces.
F2  convention-D trace Tr(K^{⊗3}·)/[2]³ split over W_p (two u) and W_n (one u).
    Channel asymmetry D(X) = tr_Wn(X) − tr_Wp(X) (plain); ε_flavour = (q⁻¹tr_Wn − q·tr_Wp)/[2]³
    is the trace's own K-weighting, reported as context only.
B   Basis check: both F1 asymmetries and D vanish on the six standard words of H₃(q)
    (1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀). All three functionals are linear in ρ(X) and every
    element of H₃(q) is a combination of those six, so vanishing on them is a proof for
    every element, every φ (scope b; exact over ℚ(q)).

Exact sympy over ℚ(q); values at the proton q₀ with mpmath 70 dps, serialised with
_precision.fmt. Nothing is compared to a physical target.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

_HERE = pathlib.Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations/probes", "computations", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from w_braid_reconcile_probe import h, q  # noqa: E402
from word_dressing_chirality_probe import I2, PR, S, Sinv, U, D, kr, on_quarks  # noqa: E402
from word_level_epsilon_probe import deltaS_op  # noqa: E402
from neutron_vector_epsilon_probe import coprod3, vec3, vec3_2  # noqa: E402
from multiplicity_trace_epsilon_probe import Mmat  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
CHECKS: list = []
Q2 = q + 1 / q
a0s, a1s, a01s, b0s, b1s = sp.symbols("phi0 phi1 phi01 psi0 psi1")


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    CHECKS.append({"name": name, "ok": bool(ok), "note": note})


def zero(e):
    return sp.simplify(sp.together(sp.expand(e))) == 0


# ---- representations: 32-dim (F1, quark strands 1-3 + pair) and 8-dim (F2)
G32 = {1: on_quarks(S, 1), 2: on_quarks(S, 2), -1: on_quarks(Sinv, 1), -2: on_quarks(Sinv, 2)}
S8 = {1: kr(S, I2), 2: kr(I2, S)}
S8[-1], S8[-2] = S8[1] - h * sp.eye(8), S8[2] - h * sp.eye(8)


def rho(elem, gens, n):
    """elem: list of (coeff, word) in the algebra convention; word letters ±1, ±2."""
    M = sp.zeros(n)
    for c, w in elem:
        W = sp.eye(n)
        for L in w:
            W = W * gens[L]
        M += c * W
    return M.applyfunc(sp.cancel)


def photon(a0, a1, a01):
    return [(1, []), (a0, [1]), (a1, [2]), (a01, [1, -2])]


def mul(x, y):
    return [(cx * cy, wx + wy) for cx, wx in x for cy, wy in y]


V = [(1, [1, -2])]
GP, GM = photon(0, 0, q * h), photon(0, 0, -h / q)
ELEMS = {
    # arm V: ε-L1 words with L+ -> V, L- -> V^-1
    "V": V, "V^-1": [(1, [2, -1])], "V·V^3": [(1, [1, -2] * 4)], "V^3·V": [(1, [1, -2] * 4)],
    "V·V^-1 (control = 1)": [(1, [1, -2, 2, -1])], "V·σ₀ (e-type slot)": [(1, [1, -2, 1])],
    "V (ε-L1 applied order: σ₁⁻¹σ₀)": [(1, [-2, 1])],
    # arm γ: four-term photon at the corpus-derived eigenvalue pair
    "γ₊ = γ(0,0,qh)": GP, "γ₋ = γ(0,0,-h/q)": GM, "γ₊γ₋ (= V³)": mul(GP, GM), "γ₋γ₊": mul(GM, GP),
}
BASIS = {"1": [(1, [])], "σ₀": [(1, [1])], "σ₁": [(1, [2])], "σ₀σ₁": [(1, [1, 2])],
         "σ₁σ₀": [(1, [2, 1])], "σ₀σ₁σ₀": [(1, [1, 2, 1])]}


# ---- F1 setup, verbatim from gg_twist_channel_np_probe / multiplicity_trace_epsilon_probe
def f1_setup():
    E3, F3 = coprod3()
    ud = PR * vec3_2({(U, D): 1})
    nA = sp.Matrix(kr(ud, sp.Matrix([0, 1])))
    nB = sp.Matrix(kr(sp.Matrix([0, 1]), ud))
    pA, pB = (E3 * nA).applyfunc(sp.cancel), (E3 * nB).applyfunc(sp.cancel)
    uuu = vec3({(U, U, U): 1})
    s_plus = (F3 * uuu).applyfunc(sp.cancel)
    s_minus = (F3 * s_plus).applyfunc(sp.cancel)
    w_plus = [i for i in range(8) if bin(i).count("1") == 1]
    w_minus = [i for i in range(8) if bin(i).count("1") == 2]
    return {"n->p": ([nA, nB], [pA, pB, s_plus], w_plus, (D, U)),
            "p->n": ([pA, pB], [nA, nB, s_minus], w_minus, (U, D))}


SETUP = f1_setup()
DS = deltaS_op()


def f1(X32):
    out = {}
    for dn, (init, fb, fi, pair) in SETUP.items():
        t0 = sp.cancel(Mmat(init, fb, fi, [X32], [], pair).trace())
        t1 = sp.cancel(Mmat(init, fb, fi, [X32], [DS], pair).trace())
        out[dn] = (t0, t1)
    return out


# ---- F2: 8-dim, weight spaces by number of u (index bit 0 = u)
WP = [i for i in range(8) if bin(i).count("1") == 1]   # two u
WN = [i for i in range(8) if bin(i).count("1") == 2]   # one u


def f2(X8):
    tp = sp.factor(sp.cancel(sum(X8[i, i] for i in WP)))
    tn = sp.factor(sp.cancel(sum(X8[i, i] for i in WN)))
    ef = sp.factor(sp.cancel((tn / q - q * tp) / Q2 ** 3))
    return tp, tn, ef


def bar_parity(e):
    if zero(e):
        return "zero"
    if zero(e.subs(q, 1 / q) - e):
        return "even"
    if zero(e.subs(q, 1 / q) + e):
        return "odd"
    return "mixed"


Q0 = mp.mpf(Q_50_DIGIT_STR)


def at_q0(e):
    return sp.lambdify(q, e, "mpmath")(Q0)


def main():
    log(f"q0 = {mp.nstr(Q0, 25)} (proton pin), dps {DPS}")
    check("P0.proton_pin", Q_50_DIGIT_STR.startswith("1.10997858275138"), Q_50_DIGIT_STR[:20])
    check("H0.hecke_8", (S8[1] * S8[1] - h * S8[1] - sp.eye(8)).applyfunc(sp.cancel) == sp.zeros(8),
          "σ² = hσ + 1 on (C²)^⊗3")
    check("H1.photon_pair_is_V3", (rho(mul(GP, GM), S8, 8) - rho([(1, [1, -2] * 3)], S8, 8))
          .applyfunc(sp.cancel) == sp.zeros(8), "γ(0,0,qh)γ(0,0,−h/q) = V³ (algebra convention)")

    # ---- B: basis check (the proof)
    log("basis check over the six standard words of H3(q)")
    basis_rows = {}
    for bn, el in BASIS.items():
        r1 = f1(rho(el, G32, 32))
        tp, tn, _ = f2(rho(el, S8, 8))
        d0 = sp.cancel(r1["p->n"][0] - r1["n->p"][0])
        d1 = sp.cancel(r1["p->n"][1] - r1["n->p"][1])
        dD = sp.cancel(tn - tp)
        basis_rows[bn] = {"F1_t0_np": str(sp.factor(r1["n->p"][0])), "F1_t1_np": str(sp.factor(r1["n->p"][1])),
                          "F1_dt0": str(d0), "F1_dt1": str(d1), "F2_trWp": str(tp), "F2_D": str(dD)}
        check(f"B.{bn}", d0 == 0 and d1 == 0 and dD == 0, "F1 Δt0 = Δt1 = 0 and F2 D = 0")
        log(f"  {bn}: done")

    # ---- arms V and γ
    rows = []
    for name, el in ELEMS.items():
        r1 = f1(rho(el, G32, 32))
        tp, tn, ef = f2(rho(el, S8, 8))
        row = {"element": name}
        eps = {}
        for dn in ("n->p", "p->n"):
            t0, t1 = r1[dn]
            e = sp.factor(sp.cancel(t1 / t0)) if t0 != 0 else None
            eps[dn] = e
            row[f"F1_{dn}"] = {"Tr_M1": str(sp.factor(t0)), "eps_tr": str(e),
                               "eps_tr_q0": fmt(at_q0(e)) if e is not None else None}
        if eps["n->p"] is not None and eps["p->n"] is not None:
            rat = sp.factor(sp.cancel(eps["p->n"] / eps["n->p"]))
            row["F1_ratio_pn_np"] = str(rat)
            row["F1_symmetric"] = bool(zero(rat - 1))
            row["F1_eps_bar_parity"] = bar_parity(eps["n->p"])
        dD = sp.factor(sp.cancel(tn - tp))
        row.update({"F2_trWp": str(tp), "F2_trWn": str(tn), "F2_D": str(dD), "F2_symmetric": dD == 0,
                    "F2_trW_q0": fmt(at_q0(tp)), "F2_eps_flavour": str(ef),
                    "F2_eps_flavour_bar_parity": bar_parity(ef), "F2_eps_flavour_q0": fmt(at_q0(ef))})
        rows.append(row)
        log(f"  {name}: F1 ratio {row.get('F1_ratio_pn_np')}  F2 D {dD}  ε_flavour({row['F2_eps_flavour_bar_parity']}) "
            f"{mp.nstr(at_q0(ef), 12)}")

    # ---- arm φ: symbolic single-crossing weights, first order at φ = ψ = 0
    log("arm φ: γ(φ0,φ1,qh)·γ(ψ0,ψ1,−h/q) and γ(φ0,φ1,φ01)")
    phi_rows = {}
    for nm, el, vars_ in [("pair γ(φ0,φ1,qh)γ(ψ0,ψ1,−h/q)", mul(photon(a0s, a1s, q * h), photon(b0s, b1s, -h / q)),
                           (a0s, a1s, b0s, b1s)),
                          ("single γ(φ0,φ1,φ01)", photon(a0s, a1s, a01s), (a0s, a1s, a01s))]:
        r1 = f1(rho(el, G32, 32))
        tp, tn, _ = f2(rho(el, S8, 8))
        d0 = sp.expand(sp.cancel(r1["p->n"][0] - r1["n->p"][0]))
        d1 = sp.expand(sp.cancel(r1["p->n"][1] - r1["n->p"][1]))
        dD = sp.expand(sp.cancel(tn - tp))
        at0 = {v: 0 for v in vars_ if v in (a0s, a1s, b0s, b1s)}
        coeffs = {str(v): {"F1_dt0": str(sp.simplify(sp.diff(d0, v).subs(at0))),
                           "F1_dt1": str(sp.simplify(sp.diff(d1, v).subs(at0))),
                           "F2_D": str(sp.simplify(sp.diff(dD, v).subs(at0)))} for v in vars_}
        full_zero = zero(d0) and zero(d1) and zero(dD)
        phi_rows[nm] = {"first_order_coefficients": coeffs, "asymmetry_identically_zero": full_zero}
        check(f"Φ.{nm}", full_zero, "F1 and F2 asymmetries vanish identically in all weights")

    allsym = all(r.get("F1_symmetric", True) and r["F2_symmetric"] for r in rows)
    check("R.all_arms_symmetric", allsym, "every arm-V and arm-γ element is u↔d symmetric in F1 and F2")
    res = {
        "producer": "computations/probes/gg_twist_vertex_channel/gg_twist_vertex_channel_np_probe.py",
        "bean": "qou-99qc", "preregistration": "ε-L1V (PREREGISTRATION.md, commit bc02ecd75c)",
        "photon": "gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (QOU/Photon.lean)",
        "arithmetic": "exact sympy over Q(q); q0 values mpmath 70 dps via _precision.fmt",
        "q0_anchor": "proton", "q0": Q_50_DIGIT_STR,
        "verdict": ("u<->d SYMMETRIC: no element of H3(q) breaks it in F1 or F2 (basis proof, scope b)"
                    if all(c["ok"] for c in CHECKS) else "SEE FAILED CHECKS"),
        "checks": CHECKS, "basis_rows": basis_rows, "rows": rows, "phi_arm": phi_rows,
        "physical_target_compared": False,
    }
    _HERE.joinpath("gg-twist-vertex-channel-np.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    failed = [c["name"] for c in CHECKS if not c["ok"]]
    log(f"done: {len(CHECKS) - len(failed)}/{len(CHECKS)} pass" + (f"; FAILED {failed}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
