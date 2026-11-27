#!/usr/bin/env python3
"""Exact optimal-face characterisation of the a_K operator-selection LP.

Beans `qou-ssf9` (trace of the #9395 witness movers) and `qou-fu8c` (the a_K
LP dual degenerates under convention D). Predictions are pre-registered in
`PREREGISTRATION.md` beside this file, committed before this script existed.

## What it does

`computations/aK_via_lp_dual_full.py` solves, per atom, the LP of
`pyhecke.lp_dual_solver.solve_operator_selection_lp`

    primal:  min  Σ_j t_j x_j   s.t.  Σ_j x_j = n,  (G x)_i ≥ 0,  x_j ≥ −M
    dual:    max  n·y0 − M Σ_j w_j  s.t.  y0 + Σ_i G_ij u_i + w_j = t_j,
             u_i ≥ 0,  w_j ≥ 0

with `t = |c|`, `G = diag(|c|)`, `c_λ` = the chi-cache `contribution`,
`n = tr_M_at_q0`, `M = 10^6`, and publishes `u_λ` as `u_lambda_star`.

Here the same LP is solved in EXACT rational arithmetic (the chi-cache 50-digit
decimal strings read as exact rationals, `sympy.solvers.simplex.linprog`), and
then every primal and dual coordinate is minimised and maximised over the
optimal face. A coordinate whose min equals its max is IDENTIFIED (the LP fixes
it); otherwise it ranges over an interval and any solver may return any point
of it.

No float64 anywhere: inputs are `str -> Fraction -> sympy.Rational`; all
reported values are exact rationals or the token "+inf".

## Scope

This characterises the LP *as posed* by the producer at the proton q0 chi
caches (the data the producer reads). It says nothing about whether this LP is
the right object for a_K — `qou-fu8c` and `probes/ak_lp_dual_quotient_probe.py`
already record that it is not.

Run:  PYTHONPATH=tools/qou-substrate/python:tools/pyhecke/python:computations \
          python3 computations/probes/ak_lp_dual_face/ak_lp_dual_face_probe.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent.parent
REPO = COMP.parent
sys.path.insert(0, str(COMP))

ATOM_CHI = {
    "proton":   "chi-proton-h3-at-q0-50dps.witness.json",
    "neutron":  "chi-neutron-h3-at-q0-50dps.witness.json",
    "deuteron": "chi-deuteron-h6-at-q0-50dps.witness.json",
    "tritium":  "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "helium-4": "chi-helium-4-h12-at-q0-50dps.witness.json",
}
M_BOUND = sp.Integer(10) ** 6           # the solver's default M_bound = 1e6
WITNESS = COMP / "a-K-via-lp-dual-full.witness.json"
# Pre-refresh witness: parent of the #9395 refresh commit 235ed5b1a7e.
OLD_REV = "235ed5b1a7e^"


def R(s: str) -> sp.Rational:
    f = Fraction(s)
    return sp.Rational(f.numerator, f.denominator)


def conj(lam):
    return [sum(1 for p in lam if p > i) for i in range(lam[0])] if lam else []


def show(v):
    if v is None:
        return "+inf"
    if v == 0:
        return "0"
    return str(v) if v.q == 1 else f"{sp.N(v, 30)} (exact rational, q={len(str(v.q))} digits)"


def _simplex_std(A, b, c):
    """Exact two-phase simplex, Bland's rule: min c·x s.t. A x = b, x >= 0.

    Entries are Fractions. Bland's rule guarantees termination on degenerate
    LPs (sympy 1.14's `linprog` cycles on the degenerate dual here — measured:
    no termination in 600 s on a 7-variable proton dual). Returns
    ("opt", value, x) or ("unbounded", None, None); raises on infeasible.
    """
    m, nvar = len(A), len(c)
    A = [row[:] for row in A]
    b = b[:]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-v for v in A[i]]
            b[i] = -b[i]
    # tableau with artificials nvar..nvar+m-1
    T = [A[i] + [Fraction(int(i == k)) for k in range(m)] + [b[i]] for i in range(m)]
    basis = [nvar + i for i in range(m)]
    N = nvar + m

    def pivot(r, col):
        pv = T[r][col]
        T[r] = [v / pv for v in T[r]]
        for i in range(m):
            if i != r and T[i][col] != 0:
                f = T[i][col]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[r])]
        basis[r] = col

    def run(cost, allowed):
        while True:
            # reduced costs
            red = []
            for j in range(N):
                if j not in allowed or j in basis:
                    continue
                rc = cost[j] - sum(cost[basis[i]] * T[i][j] for i in range(m))
                if rc < 0:
                    red.append(j)
            if not red:
                return "opt"
            col = min(red)                      # Bland: lowest index
            best = None
            for i in range(m):
                if T[i][col] > 0:
                    ratio = T[i][-1] / T[i][col]
                    key = (ratio, basis[i])     # Bland tie-break
                    if best is None or key < best[0]:
                        best = (key, i)
            if best is None:
                return "unbounded"
            pivot(best[1], col)

    cost1 = [Fraction(0)] * nvar + [Fraction(1)] * m
    run(cost1, set(range(N)))
    if sum(T[i][-1] for i in range(m) if basis[i] >= nvar) != 0:
        raise RuntimeError("infeasible LP")
    # drive artificials out of the basis where possible
    for i in range(m):
        if basis[i] >= nvar:
            for j in range(nvar):
                if T[i][j] != 0:
                    pivot(i, j)
                    break
    cost2 = [Fraction(v) for v in c] + [Fraction(0)] * m
    allowed = set(range(nvar)) | {basis[i] for i in range(m) if basis[i] >= nvar}
    st = run(cost2, allowed)
    if st == "unbounded":
        return "unbounded", None, None
    x = [Fraction(0)] * nvar
    for i in range(m):
        if basis[i] < nvar:
            x[basis[i]] = T[i][-1]
    return "opt", sum(Fraction(cv) * xv for cv, xv in zip(c, x)), x


def lp_min(c, A_eq, b_eq, bounds, A_ub=None, b_ub=None):
    """Exact min of c·v over {A_eq v = b_eq, A_ub v <= b_ub, bounds}.

    bounds[k] = (lo, None) or (None, None); lo may be any rational. Returns
    (value, point) as sympy Rationals, or (None, None) if unbounded below.
    """
    F = lambda v: Fraction(int(sp.Rational(v).p), int(sp.Rational(v).q))
    nv = len(c)
    # variable map: v_k = lo_k + s  (s>=0)   or   v_k = s+ - s-  (free)
    cols, shift = [], []
    for k, (lo, hi) in enumerate(bounds):
        assert hi is None
        if lo is None:
            cols.append((k, 1)); cols.append((k, -1)); shift.append(Fraction(0))
        else:
            cols.append((k, 1)); shift.append(F(lo))
    rows, rhs = [], []
    def add(row, r, slack):
        rr = [Fraction(0)] * len(cols)
        for ci, (k, sgn) in enumerate(cols):
            rr[ci] = sgn * F(row[k])
        rhs_v = F(r) - sum(F(row[k]) * shift[k] for k in range(nv))
        rows.append((rr, slack)); rhs.append(rhs_v)
    for row, r in zip([list(x) for x in (A_eq.tolist() if hasattr(A_eq, "tolist") else A_eq)],
                      list(b_eq)):
        add(row, r, False)
    if A_ub is not None:
        for row, r in zip(A_ub.tolist(), list(b_ub)):
            add(row, r, True)
    nsl = sum(1 for _, s in rows if s)
    A, si = [], 0
    for rr, s in rows:
        sl = [Fraction(0)] * nsl
        if s:
            sl[si] = Fraction(1); si += 1
        A.append(rr + sl)
    cc = [sgn * F(c[k]) for (k, sgn) in cols] + [Fraction(0)] * nsl
    st, val, x = _simplex_std(A, rhs, cc)
    if st == "unbounded":
        return None, None
    v = [shift[k] for k in range(nv)]
    for ci, (k, sgn) in enumerate(cols):
        v[k] += sgn * x[ci]
    val = sum(F(c[k]) * v[k] for k in range(nv))
    return sp.Rational(val.numerator, val.denominator), \
        [sp.Rational(z.numerator, z.denominator) for z in v]


def analyse(atom: str, exact_d_zeros: bool = False) -> dict:
    """`exact_d_zeros`: replace the cache's l(lambda) >= 3 entries by the exact
    0 that convention D fixes (`qou-u2jg`, Lean: every Ocneanu weight with a
    third row vanishes at z = q^3/(q^2+1)). Used only as a labelled sensitivity
    arm for helium-4, whose cache carries ~1e-73 residue there instead of 0."""
    data = json.loads((COMP / ATOM_CHI[atom]).read_text())
    rows = data["by_partition"]
    parts = [list(r["partition"]) for r in rows]
    y = [R(r["y_lambda"]) for r in rows]
    c = [R(r["contribution"]) for r in rows]
    if exact_d_zeros:
        for i, lam in enumerate(parts):
            if len(lam) >= 3:
                y[i] = sp.Integer(0)
                c[i] = sp.Integer(0)
    n = R(data["tr_M_at_q0"])
    d = len(parts)
    t = [abs(ci) for ci in c]
    Z = [i for i in range(d) if c[i] == 0]
    Y0 = [i for i in range(d) if y[i] == 0]

    # ---- primal: v = x_0..x_{d-1}, bounds x >= -M -------------------------
    pb = [(-M_BOUND, None)] * d
    A_ub = sp.zeros(d, d)
    for i in range(d):
        A_ub[i, i] = -t[i]          # -(G x)_i <= 0
    b_ub = sp.zeros(d, 1)
    p_opt, _ = lp_min(t, [[1] * d], [n], pb, A_ub, b_ub)

    # ---- dual: v = [y0, u_0..u_{d-1}, w_0..w_{d-1}] ------------------------
    nv = 1 + 2 * d
    db = [(None, None)] + [(0, None)] * (2 * d)
    Aeq = []
    for j in range(d):
        row = [0] * nv
        row[0] = 1
        row[1 + j] = t[j]           # Σ_i G_ij u_i, G diagonal
        row[1 + d + j] = 1
        Aeq.append(row)
    beq = list(t)
    dobj = [n] + [0] * d + [-M_BOUND] * d    # n*y0 - M*Σw  (maximise)
    neg = [-v for v in dobj]
    dmin, _ = lp_min(neg, Aeq, beq, db)
    d_opt = -dmin

    # ---- optimal dual face: add n*y0 - M Σ w = d_opt -----------------------
    Aface = Aeq + [dobj]
    bface = beq + [d_opt]

    def rng(k):
        e = [0] * nv
        e[k] = 1
        lo, _ = lp_min(e, Aface, bface, db)
        hi_neg, _ = lp_min([-v for v in e], Aface, bface, db)
        hi = None if hi_neg is None else -hi_neg
        return lo, hi

    y0_rng = rng(0)
    u_rng = [rng(1 + i) for i in range(d)]
    w_rng = [rng(1 + d + i) for i in range(d)]

    # ---- optimal primal face: add t·x = p_opt ------------------------------
    PA = [[1] * d, list(t)]
    Pb = [n, p_opt]

    def prng(k):
        e = [0] * d
        e[k] = 1
        lo, _ = lp_min(e, PA, Pb, pb, A_ub, b_ub)
        hn, _ = lp_min([-v for v in e], PA, Pb, pb, A_ub, b_ub)
        return lo, (None if hn is None else -hn)

    x_rng = [prng(i) for i in range(d)]

    return dict(atom=atom, d=d, parts=parts, y=y, c=c, n=n, Z=Z, Y0=Y0,
                p_opt=p_opt, d_opt=d_opt, y0=y0_rng, u=u_rng, w=w_rng, x=x_rng)


def published_u(witness: dict, atom: str):
    for r in witness["data"]["rows"]:
        if r["atom"] == atom:
            return [(p["partition"], p.get("u_lambda_star_str"),
                     p.get("is_active")) for p in r["per_partition"]], r
    return None, None


def main() -> int:
    new_w = json.loads(WITNESS.read_text())
    try:
        old_txt = subprocess.run(
            ["git", "-C", str(REPO), "show",
             f"{OLD_REV}:computations/a-K-via-lp-dual-full.witness.json"],
            check=True, capture_output=True, text=True).stdout
        old_w = json.loads(old_txt)
    except subprocess.CalledProcessError:
        old_w = None

    results = []
    checks = []
    runs = [(a, False) for a in ATOM_CHI] + [("helium-4", True)]
    for atom, dz in runs:
        t0 = time.monotonic()
        a = analyse(atom, exact_d_zeros=dz)
        label = atom + (" [l>=3 set to exact 0, convention D arm]" if dz else "")
        el = time.monotonic() - t0
        print(f"\n== {label}  d={a['d']}  |Z|={len(a['Z'])}  "
              f"primal*={show(a['p_opt'])}  dual*={show(a['d_opt'])}  "
              f"y0 in [{show(a['y0'][0])}, {show(a['y0'][1])}]  ({el:.1f}s)",
              flush=True)
        newpub, newrow = published_u(new_w, atom)
        oldpub, _ = published_u(old_w, atom) if old_w else (None, None)
        prow = []
        for i, lam in enumerate(a["parts"]):
            lo, hi = a["u"][i]
            xlo, xhi = a["x"][i]
            ident = (hi is not None and lo == hi)
            nu = newpub[i][1] if newpub else None
            ou = oldpub[i][1] if oldpub else None
            in_face_new = (nu is not None and Fraction(nu) >= 0 and
                           (hi is None or abs(Fraction(nu) - Fraction(str(hi))) <=
                            Fraction(1, 10**15)))
            in_face_old = (ou is None or (Fraction(ou) >= 0 and
                           (hi is None or abs(Fraction(ou) - Fraction(str(hi))) <=
                            Fraction(1, 10**15))))
            prow.append(dict(
                partition=lam, self_conjugate=(lam == conj(lam)),
                y_lambda_is_zero=(a["y"][i] == 0), c_is_zero=(a["c"][i] == 0),
                u_min=str(lo), u_max=("+inf" if hi is None else str(hi)),
                u_identified=ident,
                w_min=str(a["w"][i][0]),
                w_max=("+inf" if a["w"][i][1] is None else str(a["w"][i][1])),
                x_min=str(xlo), x_max=("+inf" if xhi is None else str(xhi)),
                x_identified=(xhi is not None and xlo == xhi),
                published_u_new=nu, published_u_old=ou,
                published_is_active_new=(newpub[i][2] if newpub else None),
                published_new_in_face=in_face_new,
                published_old_in_face=in_face_old,
            ))
            if a["c"][i] == 0 or i < 3:
                print(f"   {str(lam):20s} c==0:{a['c'][i]==0!s:5s} "
                      f"u in [{show(lo)}, {show(hi)}]  x in [{show(xlo)}, {show(xhi)}]  "
                      f"pub new {str(nu)[:12]} old {str(ou)[:12]}")
        Zs = set(a["Z"])
        nonZ_ok = all(r["u_identified"] and r["u_min"] == "1"
                      for i, r in enumerate(prow) if i not in Zs)
        Z_ok = all(r["u_min"] == "0" and r["u_max"] == "+inf"
                   for i, r in enumerate(prow) if i in Zs)
        y0_ok = (a["y0"][0] == 0 and a["y0"][1] == 0)
        w_ok = all(r["w_min"] == "0" and r["w_max"] == "0" for r in prow)
        chir_Z = [r["partition"] for i, r in enumerate(prow)
                  if i in Zs and not r["self_conjugate"]]
        sc_Z = [r["partition"] for i, r in enumerate(prow)
                if i in Zs and r["self_conjugate"]]
        checks.append(dict(
            atom=label,
            P0_Z_equals_ylambda_zero=(a["Z"] == a["Y0"]),
            P1_Z_rows_u_in_0_inf=Z_ok,
            P2_nonZ_rows_u_identified_eq_1=nonZ_ok,
            P3_y0_identified_zero_and_opt_zero=(y0_ok and a["p_opt"] == 0
                                                and a["d_opt"] == 0),
            P4_w_identified_zero=w_ok,
            P5_chirality_dual_sum_not_identified=bool(chir_Z),
            P5_self_conjugate_dual_sum_not_identified=bool(sc_Z),
            P6_published_new_in_face=all(r["published_new_in_face"] for r in prow),
            P6_published_old_in_face=all(r["published_old_in_face"] for r in prow),
            n_Z=len(a["Z"]), n_partitions=a["d"],
            x_identified_count=sum(r["x_identified"] for r in prow),
            Z_non_self_conjugate=chir_Z, Z_self_conjugate=sc_Z,
        ))
        results.append(dict(atom=label, n_target=str(a["n"]),
                            primal_opt=str(a["p_opt"]), dual_opt=str(a["d_opt"]),
                            y0_min=str(a["y0"][0]),
                            y0_max=("+inf" if a["y0"][1] is None else str(a["y0"][1])),
                            per_partition=prow))
        print("   checks:", {k: v for k, v in checks[-1].items()
                             if k.startswith("P")}, flush=True)

    # P5 is a per-atom REPORT, not a pass/fail: a dual sum is unidentified
    # exactly when its row set meets Z, and whether it does is a property of
    # the atom (proton/neutron have no self-conjugate partition in Z). It is
    # kept in `checks` and left out of the pass/fail aggregate.
    pre = [c for c in checks if "arm" not in c["atom"]]
    allP = {k: all(c[k] for c in pre) for k in pre[0]
            if k.startswith("P") and not k.startswith("P5")}
    allP["P5_some_dual_sum_unidentified_on_every_atom"] = all(
        c["P5_chirality_dual_sum_not_identified"]
        or c["P5_self_conjugate_dual_sum_not_identified"] for c in pre)
    w_fail = {c["atom"]: [k for k in c if k.startswith("P") and not
                         k.startswith("P5") and c[k] is False] for c in checks}
    print("\nALL ATOMS:", allP)

    import _path_bridge  # noqa: F401 — puts substrate/ (witness_base) on sys.path
    from witness_base import WitnessBuilder  # JSON writer only; no arithmetic
    w = WitnessBuilder("ak-lp-dual-face", engine="sympy")
    w.set_content_block("prop:mass-coefficient-shadow-price")
    w.set_description(
        "Exact (rational) optimal-face characterisation of the a_K "
        "operator-selection LP posed by aK_via_lp_dual_full.py. For every "
        "primal and dual coordinate, min and max over the optimal face. Tests "
        "whether u_lambda* is identified on y_lambda = 0 rows (beans qou-ssf9, "
        "qou-fu8c); predictions pre-registered in PREREGISTRATION.md.")
    w.add_parameter("arithmetic", "exact: fractions.Fraction -> sympy.Rational; no float64")
    w.add_parameter("solver", "sympy.solvers.simplex.linprog (exact simplex)")
    w.add_parameter("M_bound", "10^6 (lp_dual_solver default)")
    w.add_parameter("inputs", "chi-*-at-q0-50dps.witness.json (proton q0), decimal strings read exactly")
    w.add_data("checks", checks)
    w.add_data("all_atoms", allP)
    w.add_data("failed_predictions_by_atom", w_fail)
    w.add_data("atoms", results)
    w.add_caveat(
        "The LP's own data are the decimal strings in the chi caches. The "
        "producer passes them to Clarabel through float64 (np.array), so the "
        "LP it actually solves differs in the last digits of the nonzero |c|; "
        "zeros stay zero, so the face structure reported here is unchanged.")
    for k, v in allP.items():
        w.add_assertion(k, computed=v, expected=True,
                        source="PREREGISTRATION.md prediction")
    path = w.save({"q0Anchor": "proton"})
    print("witness:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
