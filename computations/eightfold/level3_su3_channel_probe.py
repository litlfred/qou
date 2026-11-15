#!/usr/bin/env python3
"""level3_su3_channel_probe.py -- the pre-registered level-3 (SU(3)) Hecke
channel test, bean `qou-lxh5`.

Implements EXACTLY the test fixed in
docs/audits/2026-10-10-level3-su3-channel-test.md sections 3 and 4
(pre-registration commit ce171d625e). Nothing below was tuned after that
commit; the verdict rule is applied verbatim.

Construction
------------
* Seminormal (Young) matrices of H_n(q), generators sigma_i with eigenvalues
  q, -1/q, built from standard tableaux; braid + Hecke relations are CHECKED
  (not assumed) over Q(q).
* Level-r normalised Markov trace  tr^(r)(x) = sum_lambda y_lambda chi_lambda(x),
  y_lambda proportional to s_lambda(1, Q, ..., Q^(r-1)), Q = q^2,
  normalised by sum_lambda y_lambda f^lambda = 1.  (Principal specialisation
  via the hook-content formula; cross-checked against the bialternant.)
* Borromean beta = (sigma_1 sigma_2^-1)^3,
  F_Bor^(r) = |tr^(r)(beta)| [3]_q! / q^3,
  R_r = 2 (Vol(4_1)/hbar_q^2) F_Bor^(r) - 12,  Vol(4_1) = 2 Cl_2(pi/3),
  hbar_q = 1 - 1/q.
* Control: r = 2 must equal the closed form (4+h^2-3h^4-h^6)/(h^2+4) used by
  computations/m_p_substrate_identity_50dps.py (difference simplifies to 0).

Evaluation: q_0 from CAL-2 alone (qou_substrate.constants.q_muon_at, CODATA
2022). Proton-pin value is secondary readout only.

PRECISION: sympy exact over Q(q) for every structural quantity; mpmath mpf
(mp.dps = 70) for every numerical one; no float arithmetic.
"""
from __future__ import annotations

import itertools
import sys
from math import factorial
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

from qou_substrate.constants import (  # noqa: E402
    q_muon_at, q_at, vol_4_1_at, _MU_E, _P_E,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 70
DPS = 70

q = sp.symbols("q", positive=True)
Q = q ** 2


# ------------------------------------------------------------------ combinatorics
def partitions(n, cap=None):
    cap = n if cap is None else cap
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def cells(lam):
    return [(i, j) for i, li in enumerate(lam) for j in range(li)]


def hook(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
    return arm + leg + 1


def f_lambda(lam):
    p = 1
    for (i, j) in cells(lam):
        p *= hook(lam, i, j)
    return factorial(sum(lam)) // p


def n_lambda(lam):
    return sum(i * li for i, li in enumerate(lam))


def schur_principal(lam, r):
    """s_lambda(1, Q, ..., Q^(r-1)) by the hook-content formula (exact)."""
    if len(lam) > r:
        return sp.Integer(0)
    num = Q ** n_lambda(lam)
    for (i, j) in cells(lam):
        c = j - i
        num *= (1 - Q ** (r + c)) / (1 - Q ** hook(lam, i, j))
    return sp.cancel(num)


def schur_bialternant(lam, r):
    xs = [Q ** k for k in range(r)]
    lam = list(lam) + [0] * (r - len(lam))
    A = sp.Matrix(r, r, lambda i, j: xs[j] ** (lam[i] + r - 1 - i))
    V = sp.Matrix(r, r, lambda i, j: xs[j] ** (r - 1 - i))
    return sp.cancel(A.det() / V.det())


def markov_weights(n, r):
    lams = list(partitions(n))
    s = {lam: schur_principal(lam, r) for lam in lams}
    norm = sp.cancel(sum(s[lam] * f_lambda(lam) for lam in lams))
    return {lam: sp.cancel(s[lam] / norm) for lam in lams}


# ------------------------------------------------------------------ seminormal form
def standard_tableaux(lam):
    n = sum(lam)
    out = []

    def rec(filled, k):
        if k > n:
            out.append({v: pos for pos, v in filled.items()})
            return
        for i, li in enumerate(lam):
            row = [pos for pos in filled if pos[0] == i]
            j = len(row)
            if j < li and (i == 0 or (i - 1, j) in filled):
                filled[(i, j)] = k
                rec(filled, k + 1)
                del filled[(i, j)]
    rec({}, 1)
    return out  # each: value -> (row, col)


def a_coef(d):
    return sp.cancel((q - 1 / q) / (1 - q ** (-2 * d)))


def seminormal_generators(lam, qval=None):
    """Matrices of sigma_1..sigma_{n-1} on S^lam. M[row, col] = coeff of
    basis[row] in sigma(basis[col])."""
    n = sum(lam)
    tabs = standard_tableaux(lam)
    key = lambda t: tuple(sorted(t.items()))
    idx = {key(t): k for k, t in enumerate(tabs)}
    dim = len(tabs)
    gens = []
    for i in range(1, n):
        M = sp.zeros(dim, dim)
        for k, t in enumerate(tabs):
            (ri, ci), (rj, cj) = t[i], t[i + 1]
            d = (cj - rj) - (ci - ri)
            M[k, k] = a_coef(d)
            if abs(d) != 1:
                t2 = dict(t)
                t2[i], t2[i + 1] = t[i + 1], t[i]
                k2 = idx[key(t2)]
                M[k2, k] = 1 if d > 0 else sp.cancel(a_coef(d) * a_coef(-d) + 1)
        if qval is not None:
            M = M.subs(q, qval)
        gens.append(M)
    return gens


def check_relations(lam, qval=None):
    g = seminormal_generators(lam, qval)
    I = sp.eye(g[0].shape[0]) if g else sp.eye(1)
    qq = q if qval is None else qval
    ok = True
    for i, s in enumerate(g):
        ok &= sp.simplify(s * s - (qq - 1 / qq) * s - I) == sp.zeros(*s.shape)
        if i + 1 < len(g):
            t = g[i + 1]
            ok &= sp.simplify(s * t * s - t * s * t) == sp.zeros(*s.shape)
        for j in range(i + 2, len(g)):
            ok &= sp.simplify(s * g[j] - g[j] * s) == sp.zeros(*s.shape)
    return bool(ok)


def word_matrix(gens, word, dim):
    M = sp.eye(dim)
    for w in word:
        s = gens[abs(w) - 1]
        M = M * (s if w > 0 else s.inv())
    return M


def trace_word(word, n, r, qval=None):
    y = markov_weights(n, r)
    tot = sp.Integer(0)
    for lam in partitions(n):
        if lam not in y or y[lam] == 0:
            continue
        if n == 1:
            chi = sp.Integer(1)
        else:
            g = seminormal_generators(lam, qval)
            chi = word_matrix(g, word, g[0].shape[0]).trace()
        yl = y[lam] if qval is None else y[lam].subs(q, qval)
        tot += yl * chi
    return sp.cancel(sp.simplify(tot))


def reduced_words(n):
    """One reduced word per permutation of S_n (BFS on adjacent transpositions)."""
    start = tuple(range(n))
    seen = {start: ()}
    frontier = [start]
    while frontier:
        nxt = []
        for p in frontier:
            for i in range(n - 1):
                pl = list(p)
                pl[i], pl[i + 1] = pl[i + 1], pl[i]
                pt = tuple(pl)
                if pt not in seen:
                    seen[pt] = seen[p] + (i + 1,)
                    nxt.append(pt)
        frontier = nxt
    return list(seen.values())


# ------------------------------------------------------------------ main pieces
def qint(m):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def to_mp(expr):
    f = sp.lambdify(q, expr, "mpmath")
    return lambda x: f(mpf(x))


def main():
    print("=" * 78)
    print("  level-3 (SU(3)) Hecke channel -- pre-registered test (qou-lxh5)")
    print("=" * 78)
    out = {}

    # --- seminormal relations ------------------------------------------------
    rel = {}
    for n in (2, 3, 4):
        for lam in partitions(n):
            rel[str(lam)] = check_relations(lam)
    for lam in partitions(5):
        rel[str(lam) + "@q=7/5"] = check_relations(lam, sp.Rational(7, 5))
    print("seminormal braid+Hecke relations:", all(rel.values()), f"({len(rel)} irreps)")
    out["seminormal_relations_ok"] = all(rel.values())

    # --- Schur weights cross-check -----------------------------------------
    sw_ok = all(sp.simplify(schur_principal(l, 3) - schur_bialternant(l, 3)) == 0
                for n in (1, 2, 3, 4) for l in partitions(n) if len(l) <= 3)
    print("hook-content == bialternant (r=3, n<=4):", sw_ok)
    out["schur_hook_content_eq_bialternant"] = sw_ok

    # --- z_r -------------------------------------------------------------
    z = {r: trace_word((1,), 2, r) for r in (2, 3)}
    z3_pre = q ** 5 / (q ** 4 + q ** 2 + 1)
    z2_ok = sp.simplify(z[2] - q ** 3 / (q ** 2 + 1)) == 0
    z3_ok = sp.simplify(z[3] - z3_pre) == 0
    z3_alt = sp.simplify(z3_pre - q ** 3 / sp.cancel(qint(3))) == 0
    print("tr^(2)(sigma1) = q^3/(q^2+1):", z2_ok, "  tr^(3)(sigma1) = q^5/(q^4+q^2+1):", z3_ok,
          " = q^3/[3]_q:", z3_alt)
    out["z2_ok"], out["z3_ok"], out["z3_eq_q3_over_q3int"] = z2_ok, z3_ok, z3_alt

    # --- Markov property tr(x sigma_n) = z tr(x), n = 3, 4 ------------------
    mk = {}
    for n, qv in ((3, None), (4, sp.Rational(7, 5)), (4, sp.Rational(3, 2))):
        good = True
        zz = z[3] if qv is None else z[3].subs(q, qv)
        for w in reduced_words(n):
            lhs = trace_word(w + (n,), n + 1, 3, qv)
            rhs = zz * (trace_word(w, n, 3, qv) if w else sp.Integer(1))
            if sp.simplify(lhs - rhs) != 0:
                good = False
                break
        mk[f"n={n}" + ("" if qv is None else f"@q={qv}")] = good
    print("Markov property level 3:", mk)
    out["markov_property_level3"] = mk

    # --- Borromean trace -------------------------------------------------
    beta = (1, -2) * 3
    tr = {r: trace_word(beta, 3, r) for r in (2, 3)}
    h = q - 1 / q
    closed = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)
    ctl = sp.simplify(tr[2] - closed) == 0
    print("CONTROL r=2 == (4+h^2-3h^4-h^6)/(h^2+4):", ctl)
    if not ctl:
        raise SystemExit("control failed -- abort per pre-registration")
    out["control_r2_matches_closed_form"] = ctl
    tr3_fact = sp.factor(sp.cancel(tr[3]))
    print("tr^(3)(beta_Bor) =", tr3_fact)
    out["tr3_beta_exact"] = str(tr3_fact)
    y3 = markov_weights(3, 3)
    out["y_level3_n3_exact"] = {str(k): str(sp.factor(v)) for k, v in y3.items()}
    # character of (1,1,1) on beta is 1; its contribution:
    out["tr3_minus_tr2_exact"] = str(sp.factor(sp.cancel(tr[3] - tr[2])))

    qf3 = qint(3) * qint(2)
    vol = vol_4_1_at(DPS)

    def R_of(texpr):
        tf = to_mp(texpr)
        qf = to_mp(qf3)

        def R(qq):
            hb2 = (1 - 1 / qq) ** 2
            return 2 * (vol / hb2) * (abs(tf(qq)) * qf(qq) / qq ** 3) - 12
        return R

    R2, R3 = R_of(tr[2]), R_of(tr[3])

    # --- q_0 from CAL-2 alone ------------------------------------------------
    q_mu = q_muon_at(DPS)
    q_p = q_at(DPS)
    r_mu = mpf(_MU_E.value_str)
    s_mu = mpf(_MU_E.uncertainty_str)
    R_cod = mpf(_P_E.value_str)
    s_pe = mpf(_P_E.uncertainty_str)

    def q_of_rmu(rm):
        return 1 / (1 - mp.sqrt(vol / rm))

    assert abs(q_of_rmu(r_mu) - q_mu) < mpf(10) ** (-60)

    res = {}
    for name, R in (("r2", R2), ("r3", R3)):
        val = R(q_mu)
        dR = mp.diff(lambda rm: R(q_of_rmu(rm)), r_mu)
        s_model = abs(dR) * s_mu
        s_pred = mp.sqrt(s_model ** 2 + s_pe ** 2)
        diff = val - R_cod
        nsig = abs(diff) / s_pred
        rel_ = abs(diff) / R_cod
        if abs(diff) <= 3 * s_pred:
            verdict = "PASS"
        elif rel_ <= mpf("1e-2"):
            verdict = "NEAR-MATCH"
        else:
            verdict = "FAIL"
        res[name] = dict(R_muon_pin=mp.nstr(val, 30), dR_drmu=mp.nstr(dR, 20),
                         sigma_model=mp.nstr(s_model, 12), sigma_pred=mp.nstr(s_pred, 12),
                         residual=mp.nstr(diff, 20), residual_sigma=mp.nstr(nsig, 12),
                         residual_rel=mp.nstr(rel_, 12), verdict=verdict,
                         R_proton_pin_secondary=mp.nstr(R(q_p), 30),
                         residual_rel_proton_pin=mp.nstr((R(q_p) - R_cod) / R_cod, 12))
        print(f"\n[{name}] R = {mp.nstr(val, 20)}  vs CODATA {mp.nstr(R_cod, 15)}")
        print(f"      residual {mp.nstr(diff, 12)}  rel {mp.nstr(rel_, 8)}  "
              f"sigma_pred {mp.nstr(s_pred, 8)}  -> {mp.nstr(nsig, 8)} sigma  => {verdict}")
        print(f"      (secondary, proton pin) R = {mp.nstr(R(q_p), 20)}")
    out["primary"] = res
    out["inputs"] = {"q0_muon_pin": mp.nstr(q_mu, 50), "q0_proton_pin": mp.nstr(q_p, 50),
                     "m_mu_over_m_e": _MU_E.value_str, "sigma_m_mu_over_m_e": _MU_E.uncertainty_str,
                     "m_p_over_m_e_CODATA": _P_E.value_str, "sigma_m_p_over_m_e": _P_E.uncertainty_str,
                     "Vol_4_1": mp.nstr(vol, 50)}
    out["F_Bor"] = {name: mp.nstr(abs(to_mp(t)(q_mu)) * to_mp(qf3)(q_mu) / q_mu ** 3, 25)
                    for name, t in (("r2", tr[2]), ("r3", tr[3]))}
    out["abs_tr_beta_at_q0_muon"] = {name: mp.nstr(abs(to_mp(t)(q_mu)), 25)
                                     for name, t in (("r2", tr[2]), ("r3", tr[3]))}

    # --- section 4 ---------------------------------------------------------
    sec4 = {}
    sec4["z3_exact"] = str(z3_pre)
    sec4["z3_at_q0_muon"] = mp.nstr(to_mp(z3_pre)(q_mu), 30)
    sec4["z2_at_q0_muon"] = mp.nstr(to_mp(q ** 3 / (q ** 2 + 1))(q_mu), 30)
    dims = [sum(f_lambda(l) ** 2 for l in partitions(n) if len(l) <= 3) for n in range(1, 9)]
    W6 = [1, 2, 6, 23, 103, 513, 2761, 15767]
    sec4["quotient_dims_l_le_3_n1_8"] = dims
    sec4["quotient_dims_match_W6"] = dims == W6
    print("\nquotient dims l<=3:", dims, " match W6:", dims == W6)
    shares = {}
    for n in range(3, 9):
        y = markov_weights(n, 3)
        sh = sp.factor(sp.cancel(sum(y[l] * f_lambda(l) for l in y if len(l) == 3)))
        sh1 = sp.limit(sh, q, 1)
        # classical SU(3) state fraction of 3^(x)n in three-row irreps:
        num = 0
        for l in partitions(n):
            if len(l) == 3:
                dimsu3 = 1
                for (i, j) in cells(l):
                    dimsu3 *= sp.Rational(3 + j - i, hook(l, i, j))
                num += f_lambda(l) * dimsu3
        su3 = sp.Rational(num, 3 ** n)
        shares[n] = {"exact": str(sh), "at_q0_muon": mp.nstr(to_mp(sh)(q_mu), 25),
                     "at_q1": str(sh1), "SU3_state_fraction": str(su3),
                     "q1_consistent": bool(sp.simplify(sh1 - su3) == 0)}
        print(f"n={n}: l=3 Markov share at q0 = {mp.nstr(to_mp(sh)(q_mu), 15)}; q=1: {sh1} vs SU(3) {su3}")
    sec4["l3_markov_shares"] = shares
    t29 = {}
    for r in (2, 3):
        e = trace_word((1,) * 9, 2, r)
        t29[f"r{r}"] = {"exact": str(sp.factor(e)), "at_q0_muon": mp.nstr(to_mp(e)(q_mu), 25)}
    sec4["T29_markov_trace"] = t29
    sec4["T29_note"] = ("2 strands: only (2),(1,1) exist; no l=3 block, so the level enters "
                        "only through z_r (the weight split of (2) vs (1,1))")
    print("T(2,9):", {k: v["at_q0_muon"] for k, v in t29.items()})
    sec4["W_needed"] = (
        "No separate flavour/colour object W was introduced: the only input is the "
        "integer r = 3 (z_3, weights s_lambda(1,Q,Q^2)). But by Jimbo-Schur-Weyl the "
        "level-3 trace IS the normalised trace on V^(x)n for a 3-dimensional "
        "U_q(gl_3)-module V, with Lambda^3 V != 0 (the (1,1,1) weight is the q-"
        "determinant line) and Lambda^4 V = 0. So the channel is equivalent to "
        "choosing a 3-dim object with nonzero Lambda^3: the colour object is "
        "ASSUMED via r, not derived (the audit's 'A collapses into C' risk is realised "
        "in this sense).")
    out["section4"] = sec4

    # --- witness -----------------------------------------------------------
    w = WitnessBuilder("level3-su3-channel", engine="mpmath", output_dir=HERE)
    w.set_description(
        "Pre-registered level-3 (SU(3)) Hecke channel test (bean qou-lxh5): "
        "m_p/m_e from the corpus proton identity with the level-3 Markov trace "
        "on beta_Bor, at q_0 pinned by CAL-2 alone; r=2 control and section-4 "
        "uncompared quantities.")
    w.set_audit_only("docs/audits/2026-10-10-level3-su3-channel-test.md")
    w.add_parameter("mp_dps", DPS)
    w.add_parameter("preregistration_commit", "ce171d625e")
    for k, v in out.items():
        w.add_data(k, v)
    w.add_caveat("Level 3 contradicts the premise of QOU/BraidsAndKnots/"
                 "FibreDimensionForcesTL.lean (mass fibre is 2-dimensional => level 2); "
                 "this probe tests the substitution, it does not overturn that theorem.")
    w.add_caveat("F_Bor and the constants 2, 12 were identified at level 2; carrying them "
                 "unchanged to level 3 is part of the pre-registered hypothesis.")
    p = w.save({"q0Anchor": "comparison",
                "q0Values": {"muon": mp.nstr(q_mu, 50), "proton": mp.nstr(q_p, 50)},
                "q0AnchorReason": "primary evaluation at the CAL-2 (muon) pin because the "
                                  "proton pin is solved from this identity at r=2; the "
                                  "proton-pin value is a secondary readout (E1 comparison)."})
    print("\nwitness:", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
