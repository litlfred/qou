#!/usr/bin/env python3
"""N2: does the gamma-gamma + reading-3 selection give DIFFERENT elements for n and p?

Pre-registration: PREREGISTRATION.md in this directory (committed first, eb81985791).

Model (all exact over Z[q, q^-1]; signs read at the proton pin q_0, 70 dps):

* V = span(u, d). Jimbo R-check on V (x) V, basis (uu, ud, du, dd), the convention of
  `QOU/QuarkState/IsospinRaisingRoundTrip.lean::Rc` (#8632):
      Rc = [[q,0,0,0],[0,0,1,0],[0,1,q-q^-1,0],[0,0,0,q]],  Rc^-1 = Rc - (q - q^-1).
* M3: the three-strand weight spaces W_n (one u: udd, dud, ddu) and W_p (two u:
  duu, udu, uud) -- the #8632 bases.
* M4 (named choice C-lep): strand 4 is a lepton line on the same V. The T3 = 0 weight
  space of V^(x)4 splits as N = n (x) nu (strand 4 = u; uddu, dudu, dduu) and
  P = p (x) e (strand 4 = d; duud, udud, uudd). sigma_3 maps between them.

Selection (fixed in the pre-registration):
* candidates: products of k <= 5 vertices V_i = sigma_i sigma_{i+1}^-1, i in {1, 2}
  (1-indexed strands; V_1 is a quark vertex, V_2 touches strand 4); on M3 only V_1;
* state-weighted reading 3 (choice S-w): tr(Pi_s^lambda rho(w)) >= 0 for the H_3 blocks
  lambda in {(3), (2,1)} present in the state s (both have y_lambda^D > 0; (1^3) is absent
  from these weight spaces and has y^D = 0). Pi_s^lambda is built from the central full
  twist Z = (sigma_1 sigma_2)^3, which is q^6 on (3) and 1 on (2,1).
* selected element: minimal non-zero-cost feasible word; ties are listed, not broken.

Nothing here reads AME or CODATA except the single comparison row at the end.
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in ("tools/qou-substrate/python", "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import M_E_MEV, Q_50_DIGIT_STR  # noqa: E402

DPS = 70
set_compute_dps(DPS)
mp.mp.dps = DPS

q = sp.symbols("q", positive=True)
h = q - 1 / q
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    print(("  PASS " if ok else "  FAIL ") + name)
    if not ok:
        raise SystemExit(f"check failed: {name}")


def ex(m):
    return m.applyfunc(lambda e: sp.expand(e))


# ----------------------------------------------------------- R-matrix ----
RC = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
RCI = ex(RC - h * sp.eye(4))
check("Rc * Rc^-1 = 1", ex(RC * RCI) == sp.eye(4))
check("Hecke relation (Rc - q)(Rc + q^-1) = 0",
      ex((RC - q * sp.eye(4)) * (RC + sp.eye(4) / q)) == sp.zeros(4, 4))

U, D = 0, 1  # index of u, d in V


def letter(n: int, i: int, inv: bool = False):
    """sigma_i (1-indexed) on V^(x)n, dimension 2^n."""
    R = RCI if inv else RC
    return ex(sp.kronecker_product(sp.eye(2 ** (i - 1)), R, sp.eye(2 ** (n - i - 1))))


def idx(word: str) -> int:
    v = 0
    for c in word:
        v = 2 * v + (U if c == "u" else D)
    return v


def compress(M, rows, cols):
    return sp.Matrix([[M[idx(r), idx(c)] for c in cols] for r in rows])


BASIS = {
    "Wn": ["udd", "dud", "ddu"],
    "Wp": ["duu", "udu", "uud"],
    "N": ["uddu", "dudu", "dduu"],
    "P": ["duud", "udud", "uudd"],
}

# ------------------------------------------- M3 matches #8632 matrices ----
S3 = {i: letter(3, i) for i in (1, 2)}
S3I = {i: letter(3, i, True) for i in (1, 2)}
sm1 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
sm2 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
sp1 = sp.Matrix([[h, 1, 0], [1, 0, 0], [0, 0, q]])
sp2 = sp.Matrix([[q, 0, 0], [0, h, 1], [0, 1, 0]])
check("M3: sigma_1, sigma_2 on W_n equal #8632 sm1, sm2",
      ex(compress(S3[1], BASIS["Wn"], BASIS["Wn"]) - sm1) == sp.zeros(3, 3)
      and ex(compress(S3[2], BASIS["Wn"], BASIS["Wn"]) - sm2) == sp.zeros(3, 3))
check("M3: sigma_1, sigma_2 on W_p equal #8632 sp1, sp2",
      ex(compress(S3[1], BASIS["Wp"], BASIS["Wp"]) - sp1) == sp.zeros(3, 3)
      and ex(compress(S3[2], BASIS["Wp"], BASIS["Wp"]) - sp2) == sp.zeros(3, 3))

# ---------------------------------------------------------------- M4 ----
S4 = {i: letter(4, i) for i in (1, 2, 3)}
S4I = {i: letter(4, i, True) for i in (1, 2, 3)}
check("M4 braid relation s2 s3 s2 = s3 s2 s3",
      ex(S4[2] * S4[3] * S4[2] - S4[3] * S4[2] * S4[3]) == sp.zeros(16, 16))
W0 = BASIS["N"] + BASIS["P"]


def wspace(M, basis):
    return ex(compress(M, basis, basis))


# letters restricted to the 6-dim T3 = 0 space (it is invariant: Hecke preserves weight)
L6 = {i: wspace(S4[i], W0) for i in (1, 2, 3)}
L6I = {i: wspace(S4I[i], W0) for i in (1, 2, 3)}
check("T3 = 0 space is invariant (sigma_3 has no leak out of W0)",
      all(sum(S4[3][idx(r), idx(c)] for r in W0) == sum(S4[3][idx(r), idx(c)]
          for r in ["".join(t) for t in itertools.product("ud", repeat=4)]) for c in W0))
blkN, blkP = slice(0, 3), slice(3, 6)
check("H_3 letters are block-diagonal on N (+) P",
      all(L6[i][0:3, 3:6] == sp.zeros(3, 3) and L6[i][3:6, 0:3] == sp.zeros(3, 3)
          for i in (1, 2)))
check("N block of sigma_1, sigma_2 = W_n matrices; P block = W_p matrices",
      ex(L6[1][0:3, 0:3] - sm1) == sp.zeros(3, 3) and ex(L6[2][0:3, 0:3] - sm2) == sp.zeros(3, 3)
      and ex(L6[1][3:6, 3:6] - sp1) == sp.zeros(3, 3) and ex(L6[2][3:6, 3:6] - sp2) == sp.zeros(3, 3))
check("sigma_3 mixes N and P (the charge-conserving quark-lepton crossing)",
      L6[3][3:6, 0:3] != sp.zeros(3, 3))

VERT = {1: ex(L6[1] * L6I[2]), 2: ex(L6[2] * L6I[3])}
Z6 = ex((L6[1] * L6[2]) ** 3)
I6 = sp.eye(6)


def proj(Zs, n):
    """isotypic projectors on an H_3-stable state from the full twist."""
    one = sp.eye(n)
    p3 = ex((Zs - one) / (q ** 6 - 1)).applyfunc(sp.cancel)
    p21 = ex((Zs - q ** 6 * one) / (1 - q ** 6)).applyfunc(sp.cancel)
    return {"(3)": p3, "(2,1)": p21}


PRJ = {"N": proj(Z6[0:3, 0:3], 3), "P": proj(Z6[3:6, 3:6], 3)}
for s in ("N", "P"):
    p = PRJ[s]
    check(f"{s}: projectors idempotent, ranks 1 + 2",
          ex(p["(3)"] * p["(3)"] - p["(3)"]).applyfunc(sp.cancel) == sp.zeros(3, 3)
          and sp.cancel(p["(3)"].trace()) == 1 and sp.cancel(p["(2,1)"].trace()) == 2)

q0 = mp.mpf(Q_50_DIGIT_STR)


def at_q0(expr):
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    pn = sp.Poly(num, q)
    pd = sp.Poly(den, q)
    return mp.polyval([mp.mpf(int(c)) for c in pn.all_coeffs()], q0) / \
        mp.polyval([mp.mpf(int(c)) for c in pd.all_coeffs()], q0)


def word_matrix(word):
    M = I6
    for v in word:
        M = ex(M * VERT[v])
    return M


def chis(M, s):
    sl = blkN if s == "N" else blkP
    C = M[sl, sl]
    return {lam: sp.factor(sp.cancel((PRJ[s][lam] * C).trace())) for lam in ("(3)", "(2,1)")}


# ---------------------------------------------------------- selection ----
t0 = time.time()
rows = []
for k in range(1, 6):
    for word in itertools.product((1, 2), repeat=k):
        M = word_matrix(word)
        r = {"word": "".join("V%d" % v for v in word), "k": k, "crossings": 2 * k,
             "touches_strand4": 2 in word}
        for s in ("N", "P"):
            c = chis(M, s)
            r[s] = {lam: c[lam] for lam in c}
            r[s + "_q0"] = {lam: at_q0(c[lam]) for lam in c}
            r[s + "_feasible"] = all(v >= -mp.mpf("1e-50") for v in r[s + "_q0"].values())
        r["same_chars"] = all(sp.simplify(r["N"][l] - r["P"][l]) == 0 for l in ("(3)", "(2,1)"))
        rows.append(r)
print(f"  enumerated {len(rows)} words in {time.time() - t0:.1f} s")

check("P2: every pure-V1 (H_3) word has identical chi on N and P",
      all(r["same_chars"] for r in rows if not r["touches_strand4"]))
n_diff = sum(1 for r in rows if r["touches_strand4"] and not r["same_chars"])
print(f"  strand-4 words whose N and P characters differ: {n_diff} of "
      f"{sum(1 for r in rows if r['touches_strand4'])}")


def selected(s):
    feas = [r for r in rows if r[s + "_feasible"]]
    if not feas:
        return [], None
    kmin = min(r["k"] for r in feas)
    return [r["word"] for r in feas if r["k"] == kmin], kmin


SEL = {s: selected(s) for s in ("N", "P")}
SEL3 = {s: [r["word"] for r in rows if r[s + "_feasible"] and not r["touches_strand4"]]
        for s in ("N", "P")}
for s in ("N", "P"):
    print(f"  {s}: minimal non-zero feasible (k={SEL[s][1]}): {SEL[s][0]}")
    print(f"  {s}: feasible pure-V1 words: {SEL3[s]}")
check("M3 / H_3 sub-selection reproduces #8564 survivors {V^3} within k <= 5",
      SEL3["N"] == SEL3["P"] == ["V1V1V1"])
DISTINCT = set(SEL["N"][0]) != set(SEL["P"][0])
MISMATCH = [r["word"] for r in rows if r["N_feasible"] != r["P_feasible"]]
print(f"  words feasible for exactly one of N, P: {len(MISMATCH)}: {MISMATCH}")
for r in rows:
    if r["k"] <= 2:
        print(f"    {r['word']:10s} N {r['N']}  P {r['P']}  feas N={r['N_feasible']} P={r['P_feasible']}")
print(f"  selected sets distinct: {DISTINCT}")

# ------------------------------------- q-dependence of the coincidence ----
# Every chi above is an exact rational function of q. Collect the real roots in
# (1, 3/2) of every numerator and denominator, then test feasibility exactly (sympy
# Rational) at a rational point inside each sub-interval. This answers: on which q
# intervals do the N and P selections coincide, and is q_0 inside one?
QLO, QHI = sp.Rational(1), sp.Rational(3, 2)
crit = set()
for r in rows:
    for s_ in ("N", "P"):
        for v in r[s_].values():
            nu, de = sp.fraction(sp.cancel(v))
            for f in (nu, de):
                if f.has(q):
                    for rt in sp.Poly(f, q).real_roots():
                        if QLO < rt < QHI:
                            crit.add(rt)
crit = sorted(crit, key=lambda x: float(sp.N(x, 30)))
pts = [QLO] + crit + [QHI]
INTERVALS = []
for a, b in zip(pts[:-1], pts[1:]):
    t = sp.nsimplify(sp.Rational(sp.N((a + b) / 2, 40)).limit_denominator(10 ** 30))
    if not (a < t < b):
        t = (a + b) / 2
    feas = {}
    for s_ in ("N", "P"):
        ok = [rr["word"] for rr in rows
              if all(sp.cancel(v).subs(q, t) >= 0 for v in rr[s_].values())]
        kmin = min(int(len(w_) / 2) for w_ in ok) if ok else None
        feas[s_] = sorted(w_ for w_ in ok if len(w_) / 2 == kmin) if ok else []
    INTERVALS.append({"lo": a, "hi": b, "sel_N": feas["N"], "sel_P": feas["P"],
                      "distinct": feas["N"] != feas["P"]})
for iv in INTERVALS:
    lo_, hi_ = mp.mpf(str(sp.N(iv["lo"], 40))), mp.mpf(str(sp.N(iv["hi"], 40)))
    tag = "  <- q0" if lo_ < q0 < hi_ else ""
    print(f"  q in ({mp.nstr(lo_, 10)}, {mp.nstr(hi_, 10)}): N {iv['sel_N']}  P {iv['sel_P']}"
          f"  distinct={iv['distinct']}{tag}")
Q0_INTERVAL = next(iv for iv in INTERVALS
                   if mp.mpf(str(sp.N(iv["lo"], 40))) < q0 < mp.mpf(str(sp.N(iv["hi"], 40))))
check("q0 lies strictly inside a sub-interval (no root at q0)", Q0_INTERVAL is not None)
FIRST_SPLIT = next((iv for iv in INTERVALS if iv["distinct"]), None)
if FIRST_SPLIT:
    print(f"  first q > 1 where the selections split: {sp.N(FIRST_SPLIT['lo'], 30)}"
          f"  (root of {sp.minimal_polynomial(FIRST_SPLIT['lo'], q) if FIRST_SPLIT['lo'] != 1 else '-'})")

# state difference for the selected words: chi^N - chi^P per block (same element)
STATE_DIFF = []
for wname in sorted(set(SEL["N"][0]) & set(SEL["P"][0])):
    r = next(rr for rr in rows if rr["word"] == wname)
    d = {lam: sp.factor(sp.cancel(r["N"][lam] - r["P"][lam])) for lam in ("(3)", "(2,1)")}
    STATE_DIFF.append({"word": wname, "diff": d, "diff_q0": {k: at_q0(v) for k, v in d.items()}})
    print(f"  chi^N - chi^P on {wname}: {d}  at q0: "
          f"{ {k: mp.nstr(at_q0(v), 15) for k, v in d.items()} }")

# ------------------------------------------------- the flip amplitude ----
FD = sp.Matrix([[0, 1, 1 / q], [1, 0, 1], [q, 1, 0]])   # T- : W_p -> W_n (#8632 Fd)
EU = sp.Matrix([[0, 1, q], [1, 0, 1], [1 / q, 1, 0]])   # T+ : W_n -> W_p (#8632 Eu)
FE = ex(FD * EU)
B2 = q + 1 / q


def epsC(X):
    return sp.factor(sp.cancel((FE * X).trace() / FE.trace()))


def iso_half(X):
    return sp.factor(sp.cancel(((B2 ** 2 * sp.eye(3) - FE) * FE * X).trace()))


E0_ORDER0 = None
amp_rows = []
union = sorted(set(SEL["N"][0]) | set(SEL["P"][0]))
for wname in union:
    r = next(rr for rr in rows if rr["word"] == wname)
    word = [int(c) for c in wname.replace("V", "")]
    M = word_matrix(word)
    A = sp.Matrix(M[blkP, blkN]).applyfunc(sp.factor)        # <P| w |N>
    fro = sp.factor(sp.cancel((A.T * A).trace()))
    num = sp.Poly(sp.numer(sp.together(fro)), q)
    order = 0
    while num.eval(1) == 0:
        num = sp.Poly(sp.quo(num.as_expr(), q - 1), q)
        order += 1
    amp_rows.append({"word": wname, "amplitude_P_from_N": A, "frob_sq": fro,
                     "frob_sq_q0": at_q0(fro), "vanishing_order_q_to_1_of_frob_sq": order})
    print(f"  <P|{wname}|N> = {A.tolist()}  |.|^2 = {fro}  order at q=1: {order}")

# difference element, if the selection distinguishes
diff_rows = []
if DISTINCT:
    for wn in SEL["N"][0]:
        for wp in SEL["P"][0]:
            Mn = word_matrix([int(c) for c in wn.replace("V", "")])
            Mp = word_matrix([int(c) for c in wp.replace("V", "")])
            X = ex(Mn - Mp)[blkN, blkN]
            eps = epsC(X)
            half = iso_half(X)
            y3 = abs(at_q0(eps))
            qb = M_E_MEV * (q0 + 1) * (q0 ** 2 + 1) / (2 * q0 ** 3) * y3
            diff_rows.append({"n": wn, "p": wp, "epsC": eps, "isospin_half": half,
                              "Q_beta_MeV_order0": qb})
            print(f"  Delta = {wn} - {wp} on N: eps_C = {eps}, iso-1/2 part = {half}, "
                  f"Q_beta = {mp.nstr(qb, 12)} MeV")

# -------------------------------------------------------------- witness ----
if __name__ == "__main__":
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("qbeta-n2-state-weighted-selection", engine="python", start_time=t0)
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", fmt(q0))
    w.add_parameter("compute_dps", DPS)
    w.add_parameter("kmax", 5)
    w.add_parameter("choices", ["S-w (state-weighted reading 3)", "C-lep (strand 4 = lepton)",
                                "N ~ W_n by basis order"])
    w.add_data("rows", [{
        "word": r["word"], "crossings": r["crossings"], "touches_strand4": r["touches_strand4"],
        "chi_N": {k: str(v) for k, v in r["N"].items()},
        "chi_P": {k: str(v) for k, v in r["P"].items()},
        "chi_N_q0": {k: fmt(v) for k, v in r["N_q0"].items()},
        "chi_P_q0": {k: fmt(v) for k, v in r["P_q0"].items()},
        "feasible_N": r["N_feasible"], "feasible_P": r["P_feasible"],
        "same_chars": r["same_chars"]} for r in rows])
    w.add_data("selected_N", SEL["N"][0])
    w.add_data("selected_P", SEL["P"][0])
    w.add_data("selected_k", {"N": SEL["N"][1], "P": SEL["P"][1]})
    w.add_data("feasible_pure_V1", SEL3)
    w.add_data("selection_distinguishes_n_p", DISTINCT)
    w.add_data("amplitudes", [{
        "word": a["word"], "P_from_N": [[str(x) for x in row] for row in a["amplitude_P_from_N"].tolist()],
        "frob_sq": str(a["frob_sq"]), "frob_sq_q0": fmt(a["frob_sq_q0"]),
        "vanishing_order_q_to_1_of_frob_sq": a["vanishing_order_q_to_1_of_frob_sq"]}
        for a in amp_rows])
    w.add_data("difference", [{"n": d["n"], "p": d["p"], "epsC": str(d["epsC"]),
                               "isospin_half": str(d["isospin_half"]),
                               "Q_beta_MeV_order0": fmt(d["Q_beta_MeV_order0"])} for d in diff_rows])
    w.add_data("checks", [{"name": n, "pass": ok} for n, ok in CHECKS])
    w.add_data("feasibility_mismatch_words", MISMATCH)
    w.add_data("q_intervals", [{"lo": str(iv["lo"]), "lo_num": fmt(mp.mpf(str(sp.N(iv["lo"], 70)))),
                                "hi": str(iv["hi"]), "hi_num": fmt(mp.mpf(str(sp.N(iv["hi"], 70)))),
                                "selected_N": iv["sel_N"], "selected_P": iv["sel_P"],
                                "distinct": iv["distinct"]} for iv in INTERVALS])
    w.add_data("first_split", None if not FIRST_SPLIT else {
        "q": fmt(mp.mpf(str(sp.N(FIRST_SPLIT["lo"], 70)))),
        "minimal_polynomial": str(sp.minimal_polynomial(FIRST_SPLIT["lo"], q))})
    w.add_data("state_difference_selected", [{"word": d["word"],
        "chiN_minus_chiP": {k: str(v) for k, v in d["diff"].items()},
        "at_q0": {k: fmt(v) for k, v in d["diff_q0"].items()}} for d in STATE_DIFF])
    out = w.save()
    print(f"  {sum(ok for _, ok in CHECKS)}/{len(CHECKS)} checks; witness -> {out}")
