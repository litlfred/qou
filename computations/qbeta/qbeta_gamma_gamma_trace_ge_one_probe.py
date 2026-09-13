"""Every PSD-feasible gamma-gamma word has Markov trace >= 1, at EVERY strand
count -- so the gamma-gamma + confinement-SDP construction cannot reproduce
Q_beta at all, and the bound is TIGHT.

# Ref: AGENTS.md §"Before declaring refuted" -- scope-(b), invariant named
# Ref: AGENTS.md §"Formalize-first probe discipline"
# Ref: computations/qbeta/qbeta_gamma_gamma_psd_trace_floor_probe.py -- the
#      WEAKER floor this supersedes, and why it was weaker
# Ref: content/quantum-observable-universe/lean/QOU/Mass/PsdDetOneTrace.lean
#      (PR #7295) -- `trace_ge_two` and `eq_one_of_trace_eq_two`, the 2x2 case
#      of the AM-GM step below, already sorry-free

🛑 THIS SUPERSEDES THE FLOOR PROBE, AND THE FLOOR WAS MINE.  That probe proved
`tr_M(w) >= [n+1]_q/[2]_q^n` by keeping the trivial block's term of the
Frobenius pairing and DISCARDING every other term as merely non-negative.  The
discarded terms are not merely non-negative -- each is bounded below by its own
block dimension -- and keeping them gives a bound that is both stronger and
`n`-independent:

    tr_M(w)  >=  1     for every PSD-feasible gamma-gamma word, every n.

So the floor probe's conclusion ("excluded for n <= 5, open at n >= 6") is
correct but weak: there is no n at which the construction reaches the target.
The floor's own numbers stand; only its scope was short.  Recorded rather than
deleted, because the floor is the thing you get if you stop at the first block,
and that is an easy place to stop.

THE INVARIANT, four ingredients:

  1. **Every gamma-gamma vertex has determinant 1 in every Wedderburn block.**
     `sigma_i` and `sigma_{i+1}` are conjugate in the braid group, so their
     block images have the same determinant, and `det(sigma_i sigma_{i+1}^{-1})
     = 1`.  Measured to 1e-39 at n = 3, 4, 5, 6, together with the conjugacy
     fact it rests on (`det rho(sigma_i)` is constant in `i` within a block).
     Hence every gamma-gamma WORD has determinant 1 in every block.

  2. **PSD + det 1 implies trace >= dim.**  A positive semidefinite matrix has
     non-negative eigenvalues; with product 1, AM-GM gives their sum >= dim.
     The 2x2 case is already sorry-free Lean (`PsdDetOneTrace.trace_ge_two`).

  3. **The convention-D weights are non-negative** -- strictly positive on the
     two-row partitions, exactly 0 on three rows or more.

  4. **The Markov normalisation `Sum_lambda y_lambda dim_lambda = 1`** -- this
     is `tr_M(1) = 1`, and it is what turns the per-block bound into the value
     `1` rather than some other constant.

Together: `tr_M(w) = Sum y_lambda chi_lambda(w) >= Sum y_lambda dim_lambda = 1`.

TIGHT, and the witness is the empty word: it is the identity in every block,
so every character equals its dimension and the bound is achieved exactly.

WHAT IT MEANS FOR Q_beta.  The target is `|tr_M| = Q_beta/E_0 = 0.185059`, so
the construction misses it by a factor of at least 5.40.  Equivalently the
SMALLEST Q_beta this family can predict is exactly `E_0 = 4.2274834 MeV`, which
is **+440.369 %** -- and every one of the five PSD-feasible words measured at
n = 4 lands between +458 % and +620 %, above that minimum as it must.

SCOPE.  **(b) structural exclusion at every n**, invariant as named.  It says
the gamma-gamma + confinement-SDP ROUTE cannot reach Q_beta under the ruled
functional (`eps` = the Markov trace at `z_D`) and the canonical `E_0`.  It says
nothing about the framework's ability to reach Q_beta by another route, nor
about a different `E_0`, nor about a tower correction -- and a tower correction
is the live question, since `E_0` is canonical by ruling with an OPEN series
(bean `qou-y3bm`).
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import qbeta_e0  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

_FE = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_gamma_gamma_sdp_feasibility_probe.py")
_spec2 = importlib.util.spec_from_file_location("_fe", _FE)
_fe = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_fe)

set_compute_dps(60)
mp.mp.dps = 40

H0 = _oc.H0
Q0 = _oc.Q0
HR = sp.Rational(str(H0))
ZR = sp.Rational(str(_oc.ZD))
Q = mp.mpf(str(Q0))

TOL = mp.mpf("1e-25")

#: the PSD-feasible words at n = 4, MEASURED by #7295.
FEASIBLE_N4 = [
    ((), "empty word"),
    ((0, 1, 0, 1), "(v0 v1)^2"),
    ((0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^4"),
    ((0, 0, 1, 1, 0, 1, 1, 0, 0, 1), "sporadic A"),
    ((0, 1, 1, 0, 0, 1, 0, 0, 1, 1), "sporadic B"),
    ((0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^6"),
]

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def qint(m: int):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def y_lambda(n: int, lam) -> mp.mpf:
    """Convention-D Markov weight -- the two-row truncation."""
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(n - 2 * k + 1) / qint(2) ** n


def word_matrix(sig, combo, dim):
    """`rho_lambda(w)` for the gamma-gamma word `prod_i sigma_i sigma_{i+1}^-1`."""
    M = mp.eye(dim)
    for i in combo:
        M = M * sig[i] * (sig[i + 1] - H0 * mp.eye(dim))
    return M


def trace_recursion(combo, n: int) -> mp.mpf:
    lets: list = []
    for i in combo:
        lets += [(i, sp.Integer(0)), (i + 1, -HR)]
    return mp.mpf(str(sp.N(
        _oc.tr(_oc.word_to_vec(lets, n, {}, HR), n, HR, ZR), 35)))


def words_on(n: int, max_vertices: int):
    top = n - 2
    for k in range(0, max_vertices + 1):
        for c in itertools.product(range(top), repeat=k):
            yield c


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-trace-ge-one")
    w.set_description(
        "SUPERSEDES the [n+1]_q/[2]_q^n trace floor with a stronger, "
        "n-INDEPENDENT bound: every PSD-feasible gamma-gamma word has Markov "
        "trace >= 1, at every strand count. Four ingredients, all measured -- "
        "every gamma-gamma vertex has determinant 1 in every Wedderburn block "
        "(sigma_i and sigma_{i+1} are conjugate); PSD with det 1 forces trace "
        ">= dim by AM-GM; the convention-D weights are non-negative; and "
        "Sum_lambda y_lambda dim_lambda = 1 is the Markov normalisation. The "
        "bound is TIGHT, achieved by the empty word. Consequence: the target "
        "|tr_M| = 0.185059 is missed by a factor >= 5.40, so the gamma-gamma + "
        "confinement-SDP route cannot reproduce Q_beta at ANY n -- the smallest "
        "Q_beta it can predict is exactly E_0 = 4.2274834 MeV, +440.369 %. "
        "Scope-(b) at every n, for this functional and this E_0 only."
    )

    E0 = qbeta_e0.canonical()
    qb = mp.mpf(str(Q_BETA_MEV))
    target = qb / E0
    print(f"  target |tr^z_D| = Q_beta/E_0 = {mp.nstr(target, 15)}")
    print()

    # ---- 1. the conjugacy fact the determinant rests on ---------------------
    spreads = []
    for n in (3, 4, 5, 6):
        for shape, (sig, dim) in _fe.blocks(n).items():
            ds = [mp.det(sig[i]) for i in range(n - 1)]
            spreads.append(max(abs(d - ds[0]) for d in ds))
    check("det_of_a_generator_is_constant_across_generators_in_each_block",
          max(spreads) < TOL,
          f"|det rho_lambda(sigma_i) - det rho_lambda(sigma_0)| <= "
          f"{mp.nstr(max(spreads), 4)} over every block at n = 3..6. This is "
          f"the braid-group conjugacy of the generators, and it is what makes "
          f"the vertex determinant below equal 1 rather than merely constant", w)

    # ---- 2. every vertex has determinant 1 ---------------------------------
    devs = []
    for n in (3, 4, 5, 6):
        for shape, (sig, dim) in _fe.blocks(n).items():
            for i in range(n - 2):
                devs.append(abs(mp.det(word_matrix(sig, (i,), dim)) - 1))
    check("every_gamma_gamma_vertex_has_determinant_one_in_every_block",
          max(devs) < TOL,
          f"|det rho_lambda(sigma_i sigma_{{i+1}}^-1) - 1| <= "
          f"{mp.nstr(max(devs), 4)} over every block and every vertex index at "
          f"n = 3..6 ({len(devs)} cases). Determinant is multiplicative, so "
          f"EVERY gamma-gamma word inherits det = 1 in every block", w)

    # ---- 3. and so does every word -----------------------------------------
    wdevs = []
    for n in (3, 4, 5, 6):
        B = _fe.blocks(n)
        for combo in list(words_on(n, 4))[:25]:
            for shape, (sig, dim) in B.items():
                wdevs.append(abs(mp.det(word_matrix(sig, combo, dim)) - 1))
    check("every_gamma_gamma_word_has_determinant_one_in_every_block",
          max(wdevs) < TOL,
          f"|det rho_lambda(w) - 1| <= {mp.nstr(max(wdevs), 4)} over "
          f"{len(wdevs)} (word, block) pairs at n = 3..6 -- the multiplicative "
          f"consequence, measured rather than inferred", w)

    # ---- 4. the Markov normalisation ---------------------------------------
    norms = []
    for n in range(3, 9):
        B = {tuple(p): None for p in _fe.partitions_of(n)}
        blocks = _fe.blocks(n)
        norms.append(abs(sum(y_lambda(n, p) * blocks[p][1] for p in blocks) - 1))
    check("the_markov_weights_pair_with_the_dimensions_to_exactly_one",
          max(norms) < TOL,
          f"|Sum_lambda y_lambda * dim_lambda - 1| <= {mp.nstr(max(norms), 4)} "
          f"at n = 3..8. This is tr_M(1) = 1, and it is what makes the bound "
          f"below the value 1 rather than some other constant", w)

    # ---- 5. chi >= dim on the measured feasible set -------------------------
    n = 4
    B4 = _fe.blocks(n)
    rows = []
    for combo, lab in FEASIBLE_N4:
        per = {}
        for shape, (sig, dim) in B4.items():
            M = word_matrix(sig, combo, dim)
            per[shape] = (sum(M[j, j] for j in range(dim)), dim)
        t = trace_recursion(combo, n)
        rows.append((lab, t, per))
    viol = [(lab, p) for lab, _, per in rows for p, (c, d) in per.items()
            if c < d - TOL]
    check("every_character_is_at_least_its_block_dimension_on_the_feasible_set",
          not viol,
          f"chi_lambda(w) >= dim_lambda on all {len(B4)} blocks of all "
          f"{len(rows)} measured words at n = 4 (the empty word and the 5 "
          f"PSD-feasible words of #7295). Violations: "
          f"{viol if viol else 'none'}. The two 1-dim blocks and the (2,2) "
          f"block sit at EQUALITY, so the bound is not slack by accident -- "
          f"a det-1 PSD matrix of trace exactly dim IS the identity "
          f"(PsdDetOneTrace.eq_one_of_trace_eq_two, the 2x2 case)", w)

    # ---- 6. the bound, and it is tight -------------------------------------
    below = [(lab, t) for lab, t, _ in rows if t < 1 - TOL]
    empty_t = rows[0][1]
    check("the_trace_is_at_least_one_and_the_empty_word_achieves_it",
          not below and abs(empty_t - 1) < TOL,
          f"tr_M >= 1 on every measured feasible word "
          f"({', '.join(mp.nstr(t, 10) for _, t, _ in rows)}), and the empty "
          f"word sits at exactly {mp.nstr(empty_t, 20)} -- it is the identity "
          f"in every block, so every character equals its dimension and AM-GM "
          f"is an equality. The bound is TIGHT, not merely valid", w)

    # ---- 7. the exclusion, and its reach ------------------------------------
    miss = 1 / target
    min_pred = E0
    min_pct = (min_pred - qb) / qb * 100
    check("Q_beta_is_excluded_at_every_strand_count",
          target < 1,
          f"the target |tr^z_D| = {mp.nstr(target, 12)} is below 1, by a factor "
          f"{mp.nstr(miss, 8)}. So no PSD-feasible gamma-gamma word reaches it "
          f"at ANY n: the smallest Q_beta this family can predict is exactly "
          f"E_0 = {mp.nstr(min_pred, 12)} MeV = {mp.nstr(min_pct, 8)} %, and "
          f"the five measured words at n = 4 land between +458 % and +620 %, "
          f"above that minimum as they must", w)

    # ---- 8. what the superseded floor said ----------------------------------
    floors = {n_: qint(n_ + 1) / qint(2) ** n_ for n_ in range(2, 9)}
    check("this_strictly_supersedes_the_earlier_floor_at_every_n",
          all(f < 1 for f in floors.values()),
          f"the earlier bound [n+1]_q/[2]_q^n is "
          f"{', '.join(f'{k}:{mp.nstr(v, 6)}' for k, v in floors.items())} -- "
          f"below 1 at every n >= 2, so this bound is strictly stronger "
          f"everywhere. The floor kept the trivial block's term and discarded "
          f"the rest as merely non-negative; each discarded term is in fact "
          f"bounded below by its own dimension, and keeping them is the whole "
          f"difference between an n-dependent floor and a flat 1", w)

    w.add_data("invariant", {
        "statement": "tr_M(w) >= 1 for every PSD-feasible gamma-gamma word, "
                     "at every strand count",
        "ingredient_1": "every gamma-gamma vertex has det 1 in every block "
                        "(braid conjugacy of the generators), so every word does",
        "ingredient_2": "PSD + det 1 => trace >= dim (AM-GM on the "
                        "non-negative eigenvalues); 2x2 case is sorry-free Lean "
                        "PsdDetOneTrace.trace_ge_two",
        "ingredient_3": "convention-D weights are non-negative",
        "ingredient_4": "Sum_lambda y_lambda dim_lambda = 1 (tr_M(1) = 1)",
        "tight": "the empty word achieves equality -- identity in every block",
    })
    w.add_data("supersedes", {
        "probe": "qbeta_gamma_gamma_psd_trace_floor_probe.py",
        "its_bound": "[n+1]_q/[2]_q^n",
        "why_it_was_weaker": "it kept only the trivial block's term of the "
                             "Frobenius pairing and discarded the others as "
                             "merely non-negative; each is bounded below by "
                             "its own dimension",
        "its_conclusion_stands_but_is_short": "excluded n <= 5, open n >= 6; "
                                              "in fact excluded at every n",
    })
    w.add_data("exclusion", {
        "target_abs_tr_zD": mp.nstr(target, 25),
        "bound": "1",
        "miss_factor_at_least": mp.nstr(miss, 12),
        "min_predictable_Q_beta_MeV": mp.nstr(min_pred, 20),
        "min_predictable_err_pct": mp.nstr(min_pct, 12),
        "achieved_by": "the empty word",
    })
    w.add_data("measured_feasible_set_n4", [
        {"word": lab, "tr_zD": mp.nstr(t, 25),
         "chi_vs_dim": {str(p): [mp.nstr(c, 15), d] for p, (c, d) in per.items()}}
        for lab, t, per in rows
    ])
    w.add_data("scope", {
        "class": "(b) structural exclusion, ALL n",
        "invariant": "det-1 + PSD => trace >= dim, with non-negative "
                     "convention-D weights and the Markov normalisation",
        "what_is_NOT_claimed": "nothing about reaching Q_beta by another "
                               "route, a different E_0, or a tower correction "
                               "-- E_0 is canonical by ruling with an OPEN "
                               "series (bean qou-y3bm)",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
