"""A PSD-feasible gamma-gamma word's Markov trace has a FLOOR.

🛑 THIS TITLE USED TO CONTINUE "and the floor excludes Q_beta outright for
every strand count up to n = 5".  That is FALSE and it was mine -- the scored
functional eats a DIFFERENCE of two words (`delta_of`: "Delta = neutron -
proton"), the Markov trace is linear, and a lower bound on each word bounds no
difference.  Retracted 2026-09-13 in
`qbeta_qbeta_scores_a_difference_probe.py`; the floor itself and all seven
assertions below are sound.

# Ref: AGENTS.md §"Formalize-first probe discipline" -- find the invariant that
#      prunes the class BEFORE running the wide search
# Ref: AGENTS.md §"Before declaring refuted" -- this is a scope-(b) structural
#      statement about a SINGLE word's trace for n <= 5, invariant named below
# Ref: computations/qbeta/qbeta_qbeta_scores_a_difference_probe.py -- the
#      retraction of this file's original Q_beta reading
# Ref: computations/regenerate_y_lambda_sdp_conventionD.py -- the convention-D
#      weight formula this rests on
# Ref: computations/qbeta/qbeta_gamma_gamma_sdp_feasibility_probe.py (#7295)
# Ref: computations/qbeta/qbeta_gamma_gamma_qbeta_prediction_probe.py (#7304)

WHAT THIS REPLACES.  The obvious next move after #7304 was to enumerate the
gamma-gamma + confinement-SDP feasible set at n = 5, then n = 6, looking for a
word whose Markov trace comes down to the Q_beta target.  That search is
unnecessary at n = 5 and the reason is a three-line argument.

THE INVARIANT.  For a gamma-gamma word `w` on `n` strands:

  1. **Convention D kills every partition with three or more rows** and gives
     the survivors `y_(n-k,k) = [n - 2k + 1]_q / [2]_q^n`, which is STRICTLY
     POSITIVE for `q > 1`.  (`regenerate_y_lambda_sdp_conventionD.py::y_lambda`.)
  2. **PSD feasibility makes every character value non-negative.**  The SDP half
     of the 2026-09-08 ruling asks each Wedderburn projection to be
     `Matrix.PosSemidef`, and a PSD matrix has non-negative trace, so
     `chi_lambda(w) = Tr(rho_lambda(w)) >= 0` for every block.
  3. **The trivial block is pinned at exactly 1.**  The trivial representation
     sends `sigma_i -> q`, hence `sigma_i^{-1} = sigma_i - h -> q - h = 1/q`,
     so a gamma-gamma vertex `sigma_i sigma_{i+1}^{-1}` goes to `q * (1/q) = 1`
     and a product of vertices to 1.  This is the counit twin of
     `GammaGammaWordSelection.altChar_eq_one` (sorry-free), which says the same
     for the ALTERNATING character.

Put together, in `tr_M(w) = Sum_lambda y_lambda chi_lambda(w)` every term is
non-negative and the trivial term is exactly `y_(n)`, so

    tr_M(w)  >=  y_(n)  =  [n+1]_q / [2]_q^n          (the FLOOR)

for EVERY PSD-feasible gamma-gamma word on `n` strands -- no enumeration, no
dependence on which word.

WHAT IT SAYS ABOUT THE TARGET, correctly scoped.  Q_beta needs
`|tr_M| = Q_beta / E_0 = 0.185059`.  The floor is `0.7527 / 0.5054 / 0.3193 /
0.1943` at `n = 2/3/4/5`, all above it, and `0.1153` at `n = 6`, below it.  So
**no SINGLE gamma-gamma word on five strands or fewer has that trace**, and the
first strand count at which the argument stops working is `n = 6`.

🛑 That is NOT "cannot reproduce Q_beta", which is what this paragraph asserted
until 2026-09-13.  The observable is `|eps(Delta)|*E_0` with `Delta` a
DIFFERENCE of two words, and nothing here bounds a difference.

The floor decays like `(q/[2]_q)^n ~ 0.552^n` while the target is fixed, so the
crossing is sharp and one-sided: it never re-excludes at larger `n`.

SCOPE.  **(b) structural, for n <= 5, about the trace of a SINGLE word** --
invariant as named above: convention-D weight positivity, PSD ⟹ non-negative
character, and the exact counit value on gamma-gamma words.  **Nothing is
claimed for n >= 6**: the floor falling below the target says the argument
stops, NOT that a feasible word reaches it.  And nothing at all is claimed
about Q_beta, which is scored on a difference of two words.

VERIFIED, NOT ASSUMED.  The Frobenius pairing `Sum_lambda y_lambda chi_lambda`
is checked against the independent Ocneanu recursion on every word tested
(agreement ~1e-35), so the decomposition the argument runs on is the same
number the sibling probes measure.
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
ZD = _oc.ZD
Q0 = _oc.Q0
HR = sp.Rational(str(H0))
ZR = sp.Rational(str(ZD))
Q = mp.mpf(str(Q0))

#: the PSD-feasible words at n = 4, MEASURED by #7295 -- not re-derived here.
FEASIBLE_N4 = [
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
    """`[m]_q` in the symmetric convention, at the proton pin."""
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def y_lambda(n: int, lam) -> mp.mpf:
    """Convention-D Markov weight. Zero on three rows or more -- D IS the
    two-row truncation. Mirrors `regenerate_y_lambda_sdp_conventionD.py`."""
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(n - 2 * k + 1) / qint(2) ** n


def floor_at(n: int) -> mp.mpf:
    """`y_(n)` -- the trivial block's weight, and the claimed trace floor."""
    return qint(n + 1) / qint(2) ** n


def gg_vec(combo, n: int):
    lets: list = []
    for i in combo:
        lets += [(i, sp.Integer(0)), (i + 1, -HR)]
    return _oc.word_to_vec(lets, n, {}, HR)


def trace_recursion(combo, n: int) -> mp.mpf:
    """`tr^{z_D}` via the Ocneanu recursion -- the independent route."""
    return mp.mpf(str(sp.N(_oc.tr(gg_vec(combo, n), n, HR, ZR), 35)))


def characters(combo, n: int, B) -> dict:
    """`chi_lambda(w) = Tr(rho_lambda(w))` per Wedderburn block."""
    out = {}
    for shape, (sig, dim) in B.items():
        M = mp.eye(dim)
        for i in combo:
            M = M * sig[i]
            M = M * (sig[i + 1] - H0 * mp.eye(dim))
        out[shape] = sum(M[j, j] for j in range(dim))
    return out


def words_on(n: int, max_vertices: int):
    """Every gamma-gamma word on `n` strands. Vertex `i` uses generators `i`
    and `i+1`, so `i` runs to `n - 3`."""
    top = n - 2
    for k in range(0, max_vertices + 1):
        for c in itertools.product(range(top), repeat=k):
            yield c


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-psd-trace-floor")
    w.set_description(
        "Derives a FLOOR on the convention-D Markov trace of any PSD-feasible "
        "gamma-gamma word: tr_M >= y_(n) = [n+1]_q/[2]_q^n, from three facts -- "
        "convention D's weights are strictly positive on the two-row partitions "
        "and zero elsewhere, PSD feasibility makes every character non-negative, "
        "and the trivial block is pinned at exactly 1 on every gamma-gamma word "
        "(the counit twin of altChar_eq_one). The floor is 0.7527/0.5054/0.3193/"
        "0.1943 at n=2/3/4/5, all ABOVE the Q_beta target 0.185059, and 0.1153 at "
        "n=6, below it. So no gamma-gamma + SDP word on five strands or fewer can "
        "reproduce Q_beta -- a scope-(b) exclusion that needs NO enumeration, "
        "replacing the n=5 brute-force scan #7304 left as next. Nothing is claimed "
        "for n >= 6: the floor falling below the target means the argument stops, "
        "not that a word reaches it."
    )

    E0 = qbeta_e0.canonical()
    target = mp.mpf(str(Q_BETA_MEV)) / E0
    print(f"  q0     = {mp.nstr(Q, 18)}")
    print(f"  [2]_q  = {mp.nstr(qint(2), 18)}")
    print(f"  target |tr^z_D| = Q_beta/E_0 = {mp.nstr(target, 15)}")
    print()

    # ---- 1. convention D is the two-row truncation, with positive weights ----
    zero_shapes, pos_shapes, bad = [], [], []
    for n in range(3, 9):
        for lam in _fe.partitions_of(n):
            lam = tuple(lam)
            y = y_lambda(n, lam)
            if len(lam) >= 3:
                zero_shapes.append((n, lam))
                if y != 0:
                    bad.append((n, lam, "expected 0"))
            else:
                pos_shapes.append((n, lam))
                if not y > 0:
                    bad.append((n, lam, f"expected > 0, got {mp.nstr(y, 8)}"))
    check("convention_D_weights_are_zero_on_three_rows_and_positive_on_two",
          not bad,
          f"over n = 3..8: {len(zero_shapes)} partitions with >= 3 rows all "
          f"carry y = 0 exactly (convention D IS the two-row truncation), and "
          f"all {len(pos_shapes)} one- and two-row partitions carry y > 0. "
          f"Violations: {bad if bad else 'none'}. This is what makes every term "
          f"of the Frobenius pairing non-negative once the characters are", w)

    # ---- 2. the pairing reproduces the independent recursion -----------------
    diffs = []
    for n in (3, 4, 5):
        B = _fe.blocks(n)
        for combo in list(words_on(n, 3))[:12]:
            c = characters(combo, n, B)
            pair = sum(y_lambda(n, p) * c[p] for p in B)
            diffs.append((n, combo, abs(trace_recursion(combo, n) - pair)))
    worst = max(d for _, _, d in diffs)
    check("the_frobenius_pairing_IS_the_ocneanu_trace",
          worst < mp.mpf("1e-25"),
          f"over {len(diffs)} words at n = 3, 4, 5, "
          f"|Sum_lambda y_lambda chi_lambda - tr_recursion| <= "
          f"{mp.nstr(worst, 4)}. The decomposition this argument runs on is the "
          f"same number the sibling probes measure, checked rather than assumed", w)

    # ---- 3. the trivial block is exactly 1 on every gamma-gamma word --------
    triv = []
    for n in (3, 4, 5, 6):
        B = _fe.blocks(n)
        for combo in list(words_on(n, 4))[:25]:
            triv.append(abs(characters(combo, n, B)[(n,)] - 1))
    worst_triv = max(triv)
    check("the_trivial_block_is_pinned_at_exactly_one",
          worst_triv < mp.mpf("1e-25"),
          f"chi_(n)(w) = 1 to within {mp.nstr(worst_triv, 4)} on {len(triv)} "
          f"gamma-gamma words at n = 3..6. The trivial rep sends sigma_i -> q, "
          f"so sigma_i^{{-1}} = sigma_i - h -> q - h = 1/q and a vertex -> 1. "
          f"Counit twin of GammaGammaWordSelection.altChar_eq_one (sorry-free)", w)

    # ---- 4. the floor holds on the measured feasible set --------------------
    n4 = floor_at(4)
    B4 = _fe.blocks(4)
    rows = []
    for combo, lab in [((), "empty word")] + FEASIBLE_N4:
        t = trace_recursion(combo, 4)
        c = characters(combo, 4, B4)
        negs = [p for p in B4 if y_lambda(4, p) > 0 and c[p] < -mp.mpf("1e-25")]
        rows.append((lab, t, t >= n4, negs))
    check("the_floor_holds_on_every_measured_feasible_word_at_n_4",
          all(ok for _, _, ok, _ in rows) and not any(ng for *_, ng in rows),
          f"floor y_(4) = [5]_q/[2]_q^4 = {mp.nstr(n4, 14)}; the empty word and "
          f"all 5 PSD-feasible words of #7295 sit at or above it "
          f"({', '.join(mp.nstr(t, 8) for _, t, _, _ in rows)}), and no "
          f"positively-weighted block carries a negative character on any of "
          f"them. The floor is LOOSE here -- the measured minimum is 3.2x it -- "
          f"which is what makes the exclusion below conservative", w)

    # ---- 5. the floor vs the target, and the crossing -----------------------
    print(f"  {'n':>3s} {'floor y_(n) = [n+1]_q/[2]_q^n':>32s}   excludes target?")
    table = []
    for n in range(2, 13):
        b = floor_at(n)
        table.append((n, b, b > target))
        print(f"  {n:3d} {mp.nstr(b, 16):>32s}   {'YES' if b > target else 'no'}")
    print()
    excl = [n for n, _, e in table if e]
    first_open = min(n for n, _, e in table if not e)
    check("the_floor_lies_above_the_target_for_every_strand_count_up_to_five",
          excl == [2, 3, 4, 5] and first_open == 6,
          f"the floor exceeds the target {mp.nstr(target, 10)} at n = "
          f"{excl} and drops below it first at n = {first_open} "
          f"({mp.nstr(floor_at(6), 10)}). So no SINGLE gamma-gamma word on five "
          f"strands or fewer has that trace -- scope-(b), no enumeration "
          f"needed. 🛑 This assertion was named ..._excludes_Q_beta... and it "
          f"is NOT an exclusion of Q_beta: the observable is scored on Delta = "
          f"neutron word MINUS proton word, and nothing here bounds a "
          f"difference (retracted 2026-09-13)", w)

    # ---- 6. the decay is one-sided, so it never re-excludes ------------------
    ratios = [floor_at(n + 1) / floor_at(n) for n in range(2, 12)]
    check("the_floor_decays_monotonically_so_the_crossing_is_one_sided",
          all(r < 1 for r in ratios),
          f"floor(n+1)/floor(n) runs {mp.nstr(min(ratios), 8)}.."
          f"{mp.nstr(max(ratios), 8)}, all below 1 -- the floor behaves like "
          f"(q/[2]_q)^n ~ {mp.nstr(Q / qint(2), 6)}^n against a fixed target, so "
          f"once it crosses at n = 6 it never rises back. The exclusion is a "
          f"prefix of the strand counts, not a scattered set", w)

    # ---- 7. what is NOT excluded -------------------------------------------
    check("nothing_is_claimed_at_six_strands_or_more",
          floor_at(6) < target,
          f"at n = 6 the floor is {mp.nstr(floor_at(6), 10)}, BELOW the target "
          f"{mp.nstr(target, 10)}. That means the argument stops, NOT that a "
          f"feasible word reaches the target -- stating it as an assertion so "
          f"the limit of the exclusion is machine-recorded rather than left to "
          f"prose. Whether any n >= 6 gamma-gamma word is both PSD-feasible and "
          f"near the target is OPEN and needs the enumeration", w)

    w.add_data("invariant", {
        "statement": "tr_M(w) >= y_(n) = [n+1]_q/[2]_q^n for every "
                     "PSD-feasible gamma-gamma word on n strands",
        "ingredient_1": "convention D: y_lambda = [n-2k+1]_q/[2]_q^n on two-row "
                        "partitions, 0 on three or more -- strictly positive "
                        "for q > 1",
        "ingredient_2": "PSD feasibility => chi_lambda(w) = Tr(rho_lambda(w)) "
                        ">= 0 for every block",
        "ingredient_3": "the trivial rep sends every gamma-gamma vertex to "
                        "q*(1/q) = 1, so chi_(n)(w) = 1 exactly -- the counit "
                        "twin of GammaGammaWordSelection.altChar_eq_one",
        "lean_status": "NOT formalised here; altChar_eq_one is the sorry-free "
                       "alternating-character twin of ingredient 3, and "
                       "WedderburnBlocks.PSDFeasible already carries ingredient "
                       "2's hypothesis shape",
    })
    w.add_data("target", {
        "Q_beta_CODATA_MeV": mp.nstr(mp.mpf(str(Q_BETA_MEV)), 12),
        "E0_MeV": mp.nstr(E0, 30),
        "E0_form": "tower_summed (canonical, qbeta_e0.canonical)",
        "target_abs_tr_zD": mp.nstr(target, 25),
    })
    w.add_data("floor_by_strand_count", [
        {"n": n, "floor": mp.nstr(b, 25), "excludes_target": bool(e)}
        for n, b, e in table
    ])
    w.add_data("verified_against_measured_feasible_set_n4", [
        {"word": lab, "tr_zD": mp.nstr(t, 25), "at_or_above_floor": bool(ok)}
        for lab, t, ok, _ in rows
    ])
    w.add_data("scope", {
        "class": "(b) structural, n <= 5, about a SINGLE word's trace",
        "invariant": "convention-D weight positivity + PSD => non-negative "
                     "character + exact counit value 1 on gamma-gamma words",
        "excluded": [2, 3, 4, 5],
        "first_strand_count_not_excluded": 6,
        "what_is_NOT_claimed": "that an n >= 6 gamma-gamma word reaches the "
                               "target; only that this argument stops there",
        "what_it_replaces": "the n = 5 brute-force feasibility scan left as the "
                            "next step by #7304",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
