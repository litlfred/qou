#!/usr/bin/env python3
"""Knot-operator LP of prop:knot-operator-lp-selection, solved as stated.

# Ref: [leitner2026] prop:knot-operator-lp-selection

The program (block .md, verbatim shape):

    minimise   sum_o t_o x_o
    subject to G^+ S x >= n_T,   x >= 0

* basis      the six-element normal-form basis of H_3(q)
             {1, s0, s1, s0s1, s1s0, s0s1s0} (pyhecke.gram.NF_BASIS);
* G, G^+     the convention-D Frobenius Gram matrix G_ij = tr_M(b_i b_j),
             z = q^3/(q^2+1), and its Moore-Penrose pseudo-inverse
             (pyhecke.gram.gram_matrix_mp / gram_quotient_pinv_mp, built at
             the proton q0 passed in explicitly);
* family     owner ruling 2026-11-21 (A): T_{1,0} and the standard torus
             braids of the six torus knots of prop:torus-embeddable-complete,
             T(p,q) -> (s_1 ... s_{p-1})^q.  B_2 words enter H_3 through the
             standard inclusion B_2 -> B_3, s_1 -> s_0 (0-indexed), the
             embedding computations/knot-operator-table.py already uses
             (T_{2,1} = s0, T_{2,2} = s0^2 in H_3);
* cost t     owner ruling 2026-11-21 (A): t_o = crossing energy of beta(o),
             def:crossing-energy: q per positive crossing, -q^{-1} per
             negative crossing, summed over the crossings of the word;
* S          column o = NF coefficient vector of beta(o);
* n_T        n_T^i = max(0, -c_i) for NF(T) = sum c_i b_i (def:demand-profile).

Targets: no confinement target is fixed by the block. The run covers the
H_3 targets the corpus names, each labelled:
  - positron  e+ = s0^-1 s1^-1 s0^-1   (prf:knot-operator-selection worked
                                         example; breit-wheeler-pair-production)
  - electron  e- = s0 s1 s0            (breit-wheeler-pair-production)
  - borromean beta_Bor = (s0^-1 s1)^3  (BorromeanMarkovTrace.lean; the H_3 core
                                         of def:borromean-baryon)

Solver. The canonical entry points do not solve this program:
`pyhecke.lp_dual_solver.solve_operator_selection_lp` and the
`clarabel-operator-selection-lp` MPFR binary both take (t, G, scalar
n_target) and solve  min t.x  s.t. 1.x = n_target, Gx >= 0, x >= -M.
This producer therefore solves the stated LP directly in mpmath by
exhaustive basis enumeration (13 columns, 6 rows for the primal; 13
columns, 7 rows for the dual), which is exact up to working precision and
needs no tolerance-tuned interior-point stop. Primal and dual are
enumerated independently; the duality gap is the difference of the two
optima. An infeasible primal is certified by a Farkas vector
(y >= 0, (G^+S)^T y <= 0, n_T . y > 0, sum y = 1).

Nothing here is tuned to a target value. NO float64: every number is an
mpmath mpf from the 70-dps proton q0 string; witness values pass through
`fmt`.

Usage:
    cd computations && python3 -u knot_operator_lp_selection.py 2>&1 | tee /tmp/klp.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import itertools
import platform
import sys
import time

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_str as _q_str_proton  # noqa: E402
    from qou_substrate.constants import Q_50_DIGIT_STR as _Q50_PROTON  # noqa: E402
except ImportError:  # pragma: no cover
    sys.path.insert(0, str(_path_bridge.Path(__file__).resolve().parent.parent
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.constants import q_str as _q_str_proton  # noqa: E402
    from qou_substrate.constants import Q_50_DIGIT_STR as _Q50_PROTON  # noqa: E402

from pyhecke.gram import (  # noqa: E402
    NF_BASIS, NF_NAMES, _hm_mp, gram_matrix_mp, gram_quotient_pinv_mp,
    radical_mp,
)

T0 = time.monotonic()
set_compute_dps()
DPS = mp.mp.dps
Q_STR = _q_str_proton(DPS)
Q = mp.mpf(Q_STR)
QI = 1 / Q
H = Q - QI
Z = Q ** 3 / (Q ** 2 + 1)
TOL = mp.mpf(10) ** (-(DPS - 20))  # degeneracy / sign tolerance at working precision

# Markov weights on NF_BASIS, convention D (mirrors pyhecke.gram.tr_m_mp at Q)
TR_M = [mp.mpf(1), Z, Z, Z ** 2, Z ** 2, H * Z ** 2 + Z]


def log(msg: str) -> None:
    print(f"[{time.monotonic() - T0:7.2f}s] {msg}", flush=True)


# ── Hecke normal form of a signed braid word in H_3(q) ─────────────────────
def nf_of_signed_word(word):
    """word: sequence of (gen, sign) with gen in {0,1}, sign in {+1,-1}.
    sigma^{-1} = sigma - h (Hecke relation sigma^2 = h sigma + 1)."""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for gen, sgn in word:
        d = mp.mpf(0) if sgn > 0 else -H
        nf = _hm_mp(nf, mp.mpf(1), d, gen, H)
    return nf


def trace(nf):
    return mp.fsum(nf[i] * TR_M[i] for i in range(6))


def crossing_energy(word):
    """def:crossing-energy: q per positive crossing, -q^{-1} per negative."""
    return mp.fsum(Q if s > 0 else -QI for _, s in word)


def pos(gen, k):
    return [(gen, +1)] * k


def word_str(word):
    if not word:
        return "1"
    return " ".join(f"s{g}" + ("" if s > 0 else "^-1") for g, s in word)


# ── Operator family (owner ruling 2026-11-21 (A)) ──────────────────────────
FAMILY = [
    ("T_{1,0}", [], "unknot; empty word"),
    ("T_{2,3}", pos(0, 3), "(s_1)^3 in B_2 -> s0^3 in H_3"),
    ("T_{2,5}", pos(0, 5), "(s_1)^5 in B_2 -> s0^5 in H_3"),
    ("T_{2,7}", pos(0, 7), "(s_1)^7 in B_2 -> s0^7 in H_3"),
    ("T_{2,9}", pos(0, 9), "(s_1)^9 in B_2 -> s0^9 in H_3"),
    ("T_{3,4}", [(0, 1), (1, 1)] * 4, "(s_1 s_2)^4 in B_3 -> (s0 s1)^4"),
    ("T_{3,5}", [(0, 1), (1, 1)] * 5, "(s_1 s_2)^5 in B_3 -> (s0 s1)^5"),
]

TARGETS = [
    ("positron", [(0, -1), (1, -1), (0, -1)],
     "e+ = s0^-1 s1^-1 s0^-1 (prf:knot-operator-selection worked example)"),
    ("electron", [(0, 1), (1, 1), (0, 1)],
     "e- = s0 s1 s0 (breit-wheeler-pair-production). Its closure is the Hopf "
     "link, not the trefoil; the label is the corpus's"),
    ("borromean", [(0, -1), (1, 1)] * 3,
     "beta_Bor = (s0^-1 s1)^3 (BorromeanMarkovTrace.lean, def:borromean-baryon)"),
]


# ── Linear algebra helpers (mpmath) ────────────────────────────────────────
def solve_square(A_rows, b):
    """Solve A x = b for a square list-of-lists A; None if singular."""
    n = len(A_rows)
    M = mp.matrix(A_rows)
    try:
        d = mp.det(M)
    except ZeroDivisionError:
        return None
    scale = max((abs(v) for row in A_rows for v in row), default=mp.mpf(1))
    if abs(d) <= TOL * (scale ** n if scale > 1 else 1):
        return None
    x = mp.lu_solve(M, mp.matrix(b))
    return [x[i] for i in range(n)]


def enumerate_min(cols, b, c):
    """min c.u s.t. [cols] u = b, u >= 0, by enumerating bases.
    cols: list of column vectors (len m); returns (obj, u) or (None, None)."""
    m = len(b)
    ncol = len(cols)
    best = (None, None)
    for basis in itertools.combinations(range(ncol), m):
        A = [[cols[j][i] for j in basis] for i in range(m)]
        sol = solve_square(A, b)
        if sol is None or any(v < -TOL for v in sol):
            continue
        u = [mp.mpf(0)] * ncol
        for k, j in enumerate(basis):
            u[j] = sol[k] if sol[k] > TOL else mp.mpf(0)
        obj = mp.fsum(c[j] * u[j] for j in range(ncol))
        if best[0] is None or obj < best[0] - TOL:
            best = (obj, u)
    return best


def solve_block_lp(Mmat, n_T, t):
    """Primal: min t.x, Mx >= n_T, x >= 0.  Dual: max n_T.y, M^T y <= t, y >= 0."""
    m, k = len(Mmat), len(t)
    # primal standard form: [M, -I] (x, s) = n_T
    pcols = [[Mmat[i][o] for i in range(m)] for o in range(k)]
    pcols += [[-mp.mpf(1) if i == r else mp.mpf(0) for i in range(m)] for r in range(m)]
    pc = list(t) + [mp.mpf(0)] * m
    p_obj, p_u = enumerate_min(pcols, n_T, pc)
    res = {"feasible": p_obj is not None}
    if p_obj is None:
        # Farkas: y >= 0, M^T y + r = 0, r >= 0, sum y = 1; maximise n_T.y
        fcols = [[Mmat[i][o] for o in range(k)] + [mp.mpf(1)] for i in range(m)]
        fcols += [[mp.mpf(1) if o == r else mp.mpf(0) for o in range(k)] + [mp.mpf(0)]
                  for r in range(k)]
        frhs = [mp.mpf(0)] * k + [mp.mpf(1)]
        fc = [-n_T[i] for i in range(m)] + [mp.mpf(0)] * k
        f_obj, f_u = enumerate_min(fcols, frhs, fc)
        res["farkas_value"] = None if f_obj is None else -f_obj
        res["farkas_y"] = None if f_u is None else f_u[:m]
        return res
    x = p_u[:k]
    slack = p_u[k:]
    # dual standard form: [M^T, I] (y, r) = t, maximise n_T.y == minimise -n_T.y
    dcols = [[Mmat[i][o] for o in range(k)] for i in range(m)]
    dcols += [[mp.mpf(1) if o == r else mp.mpf(0) for o in range(k)] for r in range(k)]
    dc = [-n_T[i] for i in range(m)] + [mp.mpf(0)] * k
    d_obj, d_u = enumerate_min(dcols, list(t), dc)
    y = d_u[:m]
    reduced = d_u[m:]
    primal = mp.fsum(t[o] * x[o] for o in range(k))
    dual = mp.fsum(n_T[i] * y[i] for i in range(m))
    res.update({
        "x": x, "slack": slack, "y": y, "reduced_cost": reduced,
        "primal_obj": primal, "dual_obj": dual, "duality_gap": abs(primal - dual),
    })
    return res


def main():
    log(f"dps={DPS}  q0 (proton) = {mp.nstr(Q, 30)}")
    assert Q_STR.startswith(_Q50_PROTON[:45]), "q_str(70) disagrees with Q_50_DIGIT_STR"

    G = gram_matrix_mp(DPS, q=Q)
    P = gram_quotient_pinv_mp(DPS, q=Q)
    v = radical_mp(DPS, q=Q)
    Gm, Pm = mp.matrix(G), mp.matrix(P)
    pen = [Gm * Pm * Gm - Gm, Pm * Gm * Pm - Pm, (Gm * Pm).T - Gm * Pm, (Pm * Gm).T - Pm * Gm]
    pen_res = [max(abs(E[i, j]) for i in range(6) for j in range(6)) for E in pen]
    Gv = max(abs(mp.fsum(G[i][j] * v[j] for j in range(6))) for i in range(6))
    log(f"Penrose residuals {[mp.nstr(r, 3) for r in pen_res]}  |G v| = {mp.nstr(Gv, 3)}")

    # sanity: Gram first row must be the Markov weights
    gram_row_res = max(abs(G[0][j] - TR_M[j]) for j in range(6))

    # columns of S, costs t
    S_cols, t, fam_rec = [], [], []
    for name, word, note in FAMILY:
        nf = nf_of_signed_word(word)
        te = crossing_energy(word)
        S_cols.append(nf)
        t.append(te)
        fam_rec.append({"operator": name, "braid_word_H3": word_str(word),
                        "note": note, "crossings": len(word),
                        "t_crossing_energy": fmt(te), "nf": [fmt(c) for c in nf],
                        "tr_M": fmt(trace(nf))})
        log(f"{name:8s} word={word_str(word):28s} t={mp.nstr(te, 12)}  "
            f"NF={[mp.nstr(c, 8) for c in nf]}")

    k = len(FAMILY)
    Mmat = [[mp.fsum(P[i][j] * S_cols[o][j] for j in range(6)) for o in range(k)]
            for i in range(6)]

    # validations against independent corpus closed forms
    nf_pos = nf_of_signed_word(TARGETS[0][1])
    expect_pos = [-H - H ** 3, H ** 2, H ** 2, -H, -H, mp.mpf(1)]
    pos_res = max(abs(nf_pos[i] - expect_pos[i]) for i in range(6))
    nf_bor = nf_of_signed_word(TARGETS[2][1])
    bor_lean = (4 + H ** 2 - 3 * H ** 4 - H ** 6) / (H ** 2 + 4)
    bor_res = abs(abs(trace(nf_bor)) - abs(bor_lean))
    log(f"positron NF vs closed form: {mp.nstr(pos_res, 3)};  "
        f"|tr_M(beta_Bor)| vs Lean closed form: {mp.nstr(bor_res, 3)}")

    target_records = {}
    for tname, tword, tnote in TARGETS:
        c = nf_of_signed_word(tword)
        n_T = [-c[i] if c[i] < 0 else mp.mpf(0) for i in range(6)]
        # radical component of n_T (the part G^+ S x can never reach in span(v))
        vv = mp.fsum(vi * vi for vi in v)
        rad = mp.fsum(n_T[i] * v[i] for i in range(6)) / mp.sqrt(vv)
        res = solve_block_lp(Mmat, n_T, t)
        rec = {"target_word": word_str(tword), "note": tnote,
               "nf": [fmt(x) for x in c], "n_T": [fmt(x) for x in n_T],
               "n_T_radical_component": fmt(rad),
               "feasible": res["feasible"]}
        if res["feasible"]:
            x, y = res["x"], res["y"]
            active = [FAMILY[o][0] for o in range(k) if x[o] > TOL]
            tight = [NF_NAMES[i] for i in range(6) if y[i] > TOL]
            rec.update({
                "x_star": {FAMILY[o][0]: fmt(x[o]) for o in range(k)},
                "y_star": {NF_NAMES[i]: fmt(y[i]) for i in range(6)},
                "y0_star": None,
                "y0_star_status": ("absent: the LP of prop:knot-operator-lp-selection "
                                   "has no net (equality) constraint; its only duals "
                                   "are y_star on the six demand rows"),
                "active_set": active,
                "active_constraints": tight,
                "reduced_cost": {FAMILY[o][0]: fmt(res["reduced_cost"][o]) for o in range(k)},
                "constraint_slack": {NF_NAMES[i]: fmt(res["slack"][i]) for i in range(6)},
                "primal_obj": fmt(res["primal_obj"]),
                "dual_obj": fmt(res["dual_obj"]),
                "duality_gap": fmt(res["duality_gap"]),
            })
            log(f"target {tname}: FEASIBLE  primal={mp.nstr(res['primal_obj'], 20)} "
                f"dual={mp.nstr(res['dual_obj'], 20)} gap={mp.nstr(res['duality_gap'], 3)} "
                f"active={active} tight={tight}")
        else:
            rec.update({"y0_star": None, "y_star": None, "active_set": [],
                        "primal_obj": None, "dual_obj": None, "duality_gap": None,
                        "farkas_value": None if res["farkas_value"] is None
                        else fmt(res["farkas_value"]),
                        "farkas_y": None if res["farkas_y"] is None
                        else {NF_NAMES[i]: fmt(res["farkas_y"][i]) for i in range(6)}})
            log(f"target {tname}: INFEASIBLE  Farkas n_T.y = "
                f"{mp.nstr(res['farkas_value'], 20) if res['farkas_value'] is not None else None}")
        target_records[tname] = rec

    w = WitnessBuilder("knot-operator-lp-selection", engine="python")
    w.set_description(
        "The LP of prop:knot-operator-lp-selection, min t.x s.t. G^+ S x >= n_T, x >= 0, "
        "on H_3(q) at the proton q0, convention D, with the owner-ruled family "
        "(T_{1,0} + standard torus braids of T(2,3),T(2,5),T(2,7),T(2,9),T(3,4),T(3,5)) "
        "and crossing-energy cost (def:crossing-energy). Solved by exhaustive basis "
        "enumeration in mpmath; primal and dual enumerated independently.")
    w.set_content_block("prop:knot-operator-lp-selection")
    w.add_parameter("q0", fmt(Q))
    w.add_parameter("compute_dps", DPS)
    w.add_parameter("convention", "D: z = q^3/(q^2+1)")
    w.add_parameter("embedding", "B_2 -> B_3 standard inclusion s_1 -> s0 (0-indexed)")
    w.add_parameter("tolerance", "1e-" + str(DPS - 20))
    w.add_data("nf_basis", NF_NAMES)
    w.add_data("nf_basis_words", [list(b) for b in NF_BASIS])
    w.add_data("family", fam_rec)
    w.add_data("gram_matrix", [[fmt(x) for x in row] for row in G])
    w.add_data("gram_pinv", [[fmt(x) for x in row] for row in P])
    w.add_data("constraint_matrix_GpinvS", [[fmt(x) for x in row] for row in Mmat])
    w.add_data("targets", target_records)
    w.add_data("solver", {
        "method": "exhaustive basis enumeration, mpmath, primal and dual independently",
        "why_not_canonical": ("pyhecke.lp_dual_solver.solve_operator_selection_lp and the "
                              "clarabel-operator-selection-lp binary solve min t.x s.t. "
                              "1.x = n_target, Gx >= 0, x >= -M (scalar target, G not G^+S); "
                              "not the program of this block"),
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__,
                        "executable": sys.executable},
    })
    w.add_assertion("penrose_max_residual", fmt(max(pen_res)), "0", "1e-50",
                    source="gram_quotient_pinv_mp is the Moore-Penrose inverse of G")
    w.add_assertion("gram_radical_residual", fmt(Gv), "0", "1e-50",
                    source="G v = 0, v the q-antisymmetriser")
    w.add_assertion("gram_row0_equals_markov_weights", fmt(gram_row_res), "0", "1e-50")
    w.add_assertion("positron_nf_closed_form", fmt(pos_res), "0", "1e-50",
                    source="(s0-h)(s1-h)(s0-h) expanded by hand")
    w.add_assertion("borromean_trace_vs_lean_closed_form", fmt(bor_res), "0", "1e-50",
                    source="BorromeanMarkovTrace.lean: (4+h^2-3h^4-h^6)/(h^2+4)")
    for tname, rec in target_records.items():
        if rec["feasible"]:
            w.add_assertion(f"{tname}_duality_gap", rec["duality_gap"], "0", "1e-40",
                            source="independent primal/dual enumeration")
    out = w.save({"q0Anchor": "proton", "q0Value": fmt(Q)})
    log(f"witness -> {out}")


if __name__ == "__main__":
    main()
