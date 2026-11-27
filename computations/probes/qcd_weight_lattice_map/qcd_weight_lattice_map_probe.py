#!/usr/bin/env python3
"""Helon twist lattice (Chester-Arsiwalla-Kauffman, arXiv:2501.03260v1) vs our gl3 weight map.

Pre-registration: PREREG.md in this directory (pushed before this script existed).
Exact sympy arithmetic over Q and Q(sqrt2, sqrt3). No float, no q0.

Map Phi: twist vector t = (t1,t2,t3), position c = colour c  ->  gl3 weight sum_c t_c eps_c.
  sl3 part mu = t - (T/3)(1,1,1); centre T; charge candidate Q = T/3;
  raw D-residual charge N3 = t3; traceless form <t, (1,1,-2)>.

Checks P1-P12 as registered. A FAIL is kept as a FAIL.
"""
import hashlib
import itertools
import json
import os
import sys

import sympy as sp

R = sp.Rational
s2, s6 = sp.sqrt(2), sp.sqrt(6)
s23 = sp.sqrt(R(2, 3))
ONE = sp.Matrix([1, 1, 1])

checks = []


def check(cid, ok, detail, predicted=True):
    """Record a check. `predicted` is the pre-registered expectation of `ok`."""
    verdict = "PASS" if bool(ok) == bool(predicted) else "FAIL"
    checks.append({"id": cid, "holds": bool(ok), "predicted": bool(predicted),
                   "verdict": verdict, "detail": detail})
    print(f"[{verdict}] {cid}: holds={bool(ok)} predicted={bool(predicted)} :: {detail}")


def vec(*a):
    return sp.Matrix([sp.nsimplify(x) if not isinstance(x, sp.Basic) else x for x in a])


def tup(v):
    return tuple(sp.simplify(x) for x in v)


def s(v):
    return [str(sp.simplify(x)) for x in v]


# ---------------------------------------------------------------- CAK data (as transcribed)
# Eqs. (31)-(34): (w1, w2, Q) on A2 (+) A1.
CAK_W = {
    "e": [vec(0, 0, -1)],
    "ubar": [vec(0, s23, R(-2, 3)), vec(1 / s2, -1 / s6, R(-2, 3)), vec(-1 / s2, -1 / s6, R(-2, 3))],
    "d": [vec(0, -s23, R(-1, 3)), vec(-1 / s2, 1 / s6, R(-1, 3)), vec(1 / s2, 1 / s6, R(-1, 3))],
    "nu": [vec(0, 0, 0)],
}
# Eq. (35): weight coords -> twist coords.
M = sp.Matrix([[-1 / s2, -1 / s6, 1], [1 / s2, -1 / s6, 1], [0, s23, 1]])

# Table 1 (Lambek): particle -> (F, a_i, a_j, a_k). Antiparticles negated.
LAMBEK = {
    "e-": (1, -1, -1, -1), "nu": (1, 0, 0, 0),
    "u_r": (1, 0, 1, 1), "u_b": (1, 1, 0, 1), "u_g": (1, 1, 1, 0),
    "d_r": (1, -1, 0, 0), "d_b": (1, 0, -1, 0), "d_g": (1, 0, 0, -1),
}
for k, v in list(LAMBEK.items()):
    bar = {"e-": "e+", "nu": "nubar"}.get(k, k[0] + "bar" + k[1:])
    LAMBEK[bar] = tuple(-x for x in v)

# Standard charges (comparison only) and hypercharges Y = 2(Q - I3) for the SM reading.
SM_Q = {"nu": 0, "e": -1, "u": R(2, 3), "d": R(-1, 3)}
SM_Y = {("nu", "L"): -1, ("e", "L"): -1, ("e", "R"): -2,
        ("u", "L"): R(1, 3), ("u", "R"): R(4, 3), ("d", "L"): R(1, 3), ("d", "R"): R(-2, 3)}

# ---------------------------------------------------------------- P1
Mdet = sp.simplify(M.det())
twists = {}
p1_ok = Mdet != 0
for name, ws in CAK_W.items():
    ts = []
    for w in ws:
        t = sp.simplify(M * w)
        ts.append(t)
        integral = all(sp.simplify(x).is_integer for x in t)
        sumcheck = sp.simplify(sum(t) - 3 * w[2]) == 0
        p1_ok = p1_ok and integral and sumcheck
    twists[name] = ts
colsum = [sp.simplify(sum(M[:, j])) for j in range(3)]
p1_ok = p1_ok and colsum == [0, 0, 3]
check("P1", p1_ok,
      f"det M = {Mdet}; column sums {colsum}; M(w,Q) integral twist vectors "
      f"{ {k: [s(t) for t in v] for k, v in twists.items()} }; T = 3Q on every state")

# Full twist set: CAK negative-charge states and their conjugates.
STATES = {}  # label -> twist (sympy Matrix)
STATES["nu"] = twists["nu"][0]
STATES["e-"] = twists["e"][0]
STATES["e+"] = -twists["e"][0]
for i, t in enumerate(twists["d"]):
    STATES[f"d_{i}"] = t
    STATES[f"dbar_{i}"] = -t
for i, t in enumerate(twists["ubar"]):
    STATES[f"ubar_{i}"] = t
    STATES[f"u_{i}"] = -t


def mu_of(t):
    return sp.simplify(t - (sum(t) / 3) * ONE)


# ---------------------------------------------------------------- P2: one linear L for all states
Minv = sp.simplify(M.inv())
# (w1,w2) = rows 0,1 of Minv applied to t. Since Minv * ONE * Q contributes only to Q-row,
# check (w1,w2) depends on mu alone: Minv[0:2,:] * ONE == 0.
L = Minv[0:2, :]
p2_ok = all(sp.simplify(x) == 0 for x in (L * ONE))
for name, ws in CAK_W.items():
    for w, t in zip(ws, twists[name]):
        p2_ok = p2_ok and all(sp.simplify(a - b) == 0 for a, b in zip(L * mu_of(t), w[0:2]))
check("P2", p2_ok,
      f"L = rows 1-2 of M^-1 = {[[str(sp.simplify(x)) for x in L.row(r)] for r in range(2)]}; "
      "L(1,1,1)=0 so (w1,w2) = L·mu for every state, Q = T/3: one fixed linear map, no per-state fix")

# ---------------------------------------------------------------- P3: Lambek
p3a = True
lam_rows = {}
for k, (F, a, b, c) in LAMBEK.items():
    base = k.replace("bar", "").replace("-", "").replace("+", "")
    flav = base.split("_")[0]
    qstd = SM_Q["e" if flav == "e" else flav] * (-1 if F < 0 else 1)
    q3 = R(a + b + c, 3)
    lam_rows[k] = {"F": F, "a": [a, b, c], "Q_sum_over_3": str(q3), "Q_std": str(qstd)}
    p3a = p3a and q3 == qstd
check("P3a", p3a, "Lambek (a_i+a_j+a_k)/3 = standard charge for all 16 states")
literal = all(sum(v[1:]) == (SM_Q["e" if k[0] == "e" else k.split("_")[0].replace("bar", "")]
                              * (-1 if v[0] < 0 else 1)) for k, v in LAMBEK.items())
check("P3b", literal, "literal reading 'the three components sum to the charge' "
      "(fails: e- sums to -3, u_r to +2)", predicted=False)
# Lambek twist sets equal the CAK-M twist sets (as sets per flavour, colour labels free)
lam_sets = {}
for k, v in LAMBEK.items():
    lam_sets.setdefault(k.split("_")[0], set()).add(tuple(v[1:]))
cak_sets = {"e-": {tup(STATES["e-"])}, "e+": {tup(STATES["e+"])}, "nu": {tup(STATES["nu"])},
            "nubar": {tup(STATES["nu"])},
            "d": {tup(STATES[f"d_{i}"]) for i in range(3)}, "dbar": {tup(STATES[f"dbar_{i}"]) for i in range(3)},
            "u": {tup(STATES[f"u_{i}"]) for i in range(3)}, "ubar": {tup(STATES[f"ubar_{i}"]) for i in range(3)}}
p3c = all({tuple(sp.Integer(x) for x in t) for t in lam_sets[k]} == cak_sets[k] for k in lam_sets)
check("P3c", p3c, "Lambek (i,j,k) twist sets = M-image twist sets per flavour (CAK §3 vs §6 consistent)")

# ---------------------------------------------------------------- P4: exterior algebra
configs = set()
for sign in (1, -1):
    for sub in itertools.product((0, 1), repeat=3):
        configs.add(tuple(sign * x for x in sub))
ext_weights = {}
for k in range(4):
    for sub in itertools.combinations(range(3), k):
        w = tuple(1 if i in sub else 0 for i in range(3))
        ext_weights[w] = ("Lambda", k)
        ext_weights[tuple(-x for x in w)] = ("Lambda*", k)
state_set = {tuple(int(x) for x in t) for t in STATES.values()}
p4 = (len(configs) == 15 and set(ext_weights) == configs and state_set <= configs
      and all(sum(w) == (k if lab == "Lambda" else -k) for w, (lab, k) in ext_weights.items()))
check("P4", p4, f"{len(configs)} no-mixed-sign configs = weights of Λ•C^3 ⊕ Λ•(C^3)* (each multiplicity 1); "
      f"centre on Λ^k is ±k so Q = ±k/3; first-generation fermions use {len(state_set)} of them")

# ---------------------------------------------------------------- P5: colour multiplets
FUND = {tup(sp.Matrix([1 if i == c else 0 for i in range(3)]) - R(1, 3) * ONE) for c in range(3)}
AFUND = {tuple(-x for x in w) for w in FUND}
def mult(prefix):
    return {tup(mu_of(STATES[f"{prefix}_{i}"])) for i in range(3)}
rep = {}
for p in ("u", "d", "ubar", "dbar"):
    m = mult(p)
    rep[p] = "fund(eps)" if m == FUND else ("antifund(eps)" if m == AFUND else "other")
lept = all(tup(mu_of(STATES[x])) == (0, 0, 0) for x in ("nu", "e-", "e+"))
p5 = rep["u"] == rep["d"] and rep["ubar"] == rep["dbar"] and rep["u"] != rep["ubar"] and "other" not in rep.values() and lept
check("P5", p5, f"colour reps in eps-convention: {rep}; leptons sl3 singlets: {lept}. "
      "CAK names d '3' and ubar '3bar'; the eps-convention names are the conjugates — a label choice, consistent")

# ---------------------------------------------------------------- P6: Q vs N3
p6a = all(sp.simplify(sum(t) / 3 - (t[2] - mu_of(t)[2])) == 0 for t in STATES.values())
check("P6a", p6a, "Q = N3_raw - mu_3 on every state (raw N3 = t3 carries the centre)")


def ntl(t):
    return sp.simplify(t[0] + t[1] - 2 * t[2])


# witnesses: same (Q,Y) different traceless N3; same traceless N3 different Q
u0, u2 = STATES["u_0"], STATES["u_1"]
pairs_same_QY = [(a, b) for a, b in itertools.combinations([f"u_{i}" for i in range(3)], 2)
                 if ntl(STATES[a]) != ntl(STATES[b])]
same_ntl_diffQ = ntl(STATES["nu"]) == ntl(STATES["e-"]) and sum(STATES["nu"]) != sum(STATES["e-"])
p6b = bool(pairs_same_QY) and same_ntl_diffQ
check("P6b", p6b, f"traceless N3=<t,(1,1,-2)> differs inside the u colour triplet at fixed (Q,Y) {pairs_same_QY[:1]}; "
      f"nu and e- share traceless N3 = 0 but Q = 0 vs -1: N3 (traceless) is neither Q nor Y, "
      "and Q is not a function of it")

# ---------------------------------------------------------------- P7: (C^3)^{⊗n} centre fixed at n
Tvals = sorted({int(sum(t)) for t in STATES.values()})
neg = any(int(x) < 0 for t in STATES.values() for x in t)
p7 = len(Tvals) > 1 and neg
check("P7", p7, f"twist centres T in {Tvals} (not constant) and negative entries occur; every weight of "
      "(C^3)^{⊗n} is non-negative with centre n, so no single strand module carries the twist lattice "
      "and Q = T/3 is invisible to the centre of the strand module (=n)")

# ---------------------------------------------------------------- P8: D-visible sector N3 = 0
visible = sorted(k for k, t in STATES.items() if t[2] == 0)
p8 = "e-" not in visible and "e+" not in visible
check("P8", p8, f"states with t3 = 0 (the only sector D's trace sees, if t is read as a colour weight): {visible}")

# ---------------------------------------------------------------- P9: Y not a function of twist
p9 = SM_Y[("u", "L")] != SM_Y[("u", "R")]
check("P9", p9, "u_L and u_R carry the same twist vector (CAK Table 2: chirality lives in the braid) "
      f"but Y = {SM_Y[('u','L')]} vs {SM_Y[('u','R')]}: twist fixes Q, not Y (SM values, comparison only)")

# ---------------------------------------------------------------- P10: electron braid
def perm_of(word, n):
    """word: list of (i, sign), 0-indexed generators. Return permutation as list."""
    p = list(range(n))
    for i, _ in word:
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def cycles(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i not in seen:
            c, j = [], i
            while j not in seen:
                seen.add(j); c.append(j); j = p[j]
            out.append(c)
    return out


corpus_e = [(0, 1), (1, 1), (0, 1)]            # sigma0 sigma1 sigma0
cak_eL = [(0, -1), (1, 1)]                      # sigma1^-1 sigma2 (1-indexed)
cak_eR = [(1, 1), (0, -1)]                      # sigma2 sigma1^-1
info = {}
for nm, w in (("corpus e = s0 s1 s0", corpus_e), ("CAK e_L = s1^-1 s2", cak_eL), ("CAK e_R = s2 s1^-1", cak_eR)):
    info[nm] = {"components": len(cycles(perm_of(w, 3))), "writhe": sum(x for _, x in w), "length": len(w)}
p10_same = info["corpus e = s0 s1 s0"] == info["CAK e_L = s1^-1 s2"]
check("P10", p10_same, f"{info}: corpus electron closes to a 2-component link (Hopf), writhe 3; "
      "CAK electron braid closes to 1 component, writhe 0", predicted=False)

# ---------------------------------------------------------------- P11: up quark as one strand
need_t = R(2, 3) * 3
w2 = sp.Matrix([2, 0, 0])
mu2 = mu_of(w2)
SYM2 = {tup(sp.Matrix([int(i == a) + int(i == b) for i in range(3)]) - R(2, 3) * ONE)
        for a in range(3) for b in range(a, 3)}
in_trip = tup(mu2) in FUND or tup(mu2) in AFUND
p11_conflict = (not in_trip) and tup(mu2) in SYM2 and need_t not in (-1, 0, 1)
check("P11", p11_conflict, f"one strand, Q = t/3 = 2/3 needs t = {need_t} (outside CAK's {{-1,0,1}}); "
      f"its colour weight 2eps_c has mu = {s(mu2)}, a weight of S^2C^3 (the 6), not of 3 or 3bar")

# ---------------------------------------------------------------- P12: uud on three strands
t_p = sp.Matrix([2, 2, -1])
p12_conflict = sp.simplify(sum(t_p) / 3) == 1 and tup(mu_of(t_p)) != (0, 0, 0)
cak_p = STATES["u_0"] + STATES["u_1"] + STATES["d_2"]
# CAK proton: u_r + u_g + d_b (colours distinct). Find a colour-distinct u,u,d triple summing to (1,1,1)
cak_singlet = any(tup(STATES[f"u_{a}"] + STATES[f"u_{b}"] + STATES[f"d_{c}"]) == (1, 1, 1)
                  for a, b, c in itertools.permutations(range(3)))
check("P12", p12_conflict and cak_singlet,
      f"strand twists (u,u,d) = (2,2,-1) at positions r,g,b: Q = 1 but mu = {s(mu_of(t_p))} != 0, not a colour "
      f"singlet (singlet needs t1=t2=t3, i.e. equal quark charges); CAK's three-braid sum u+u+d = (1,1,1) "
      f"is a singlet: {cak_singlet}")

# ---------------------------------------------------------------- state table
table = []
for k in sorted(STATES):
    t = STATES[k]
    table.append({"state": k, "twist_t": s(t), "T": str(sum(t)), "Q_T_over_3": str(sp.simplify(sum(t) / 3)),
                  "mu_sl3": s(mu_of(t)), "N3_raw": str(t[2]), "N3_traceless": str(ntl(t)),
                  "CAK_w1w2": s(L * mu_of(t)), "D_visible_t3_eq_0": bool(t[2] == 0)})

npass = sum(c["verdict"] == "PASS" for c in checks)
print(f"SUMMARY {npass}/{len(checks)}")

here = os.path.dirname(os.path.abspath(__file__))
with open(__file__, "rb") as fh:
    script_hash = hashlib.sha256(fh.read()).hexdigest()[:12]
out = {
    "schema": "probe-witness/v1",
    "probe": "qcd_weight_lattice_map",
    "issue": 9096,
    "scriptHash": script_hash,
    "arithmetic": "exact sympy over Q(sqrt2, sqrt3); no float; q0 not used",
    "q0Anchor": "independent",
    "q0AnchorReason": "exact sympy over Q(sqrt2, sqrt3); q0 never read",
    "source": "Chester-Arsiwalla-Kauffman arXiv:2501.03260v1 §2-3, §6 Eqs.(31)-(35), Tables 1-2; "
              "NOT held in library/, transcribed via a summarising fetch of the arXiv HTML",
    "map": "t -> sum_c t_c eps_c (colour = position, K0); mu = t - (T/3)(1,1,1); Q = T/3; N3 = t3",
    "L_w_from_mu": [[str(sp.simplify(x)) for x in L.row(r)] for r in range(2)],
    "lambek": lam_rows,
    "states": table,
    "electron_braids": info,
    "checks": checks,
    "summary": f"{npass}/{len(checks)}",
}
with open(os.path.join(here, "qcd_weight_lattice_map.witness.json"), "w") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
sys.exit(0 if npass == len(checks) else 1)
