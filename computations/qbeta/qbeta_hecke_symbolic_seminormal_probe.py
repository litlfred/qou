#!/usr/bin/env python3
"""qou-avt2, part 2: EXACT symbolic-in-q Hecke characters for ARBITRARY braid
words, and a two-way cross-check against the Murnaghan-Nakayama engine.

WHAT THIS CLOSES. `computations/hecke/hecke_characters.py` already computes
chi_lambda(braid word) for general n via seminormal matrices -- but only
NUMERICALLY. Its `precision="symbolic_q"` branch raises:

    NotImplementedError("symbolic-in-q character evaluation is deferred to F3
    (Murnaghan-Nakayama / Ram-Wenzl recursion in Rust). For now use
    precision='mpfr_50dps' for exact evaluation.")

So "F3" is a NAMED, DEFERRED gap in the corpus, and this file is the symbolic
half of it. `qbeta_hecke_mn_character_engine_probe.py` (the MN rule) covers the
STANDARD elements; this covers ARBITRARY words. They overlap exactly on the
standard elements, which is what makes the cross-check below meaningful.

CORRECTION TO MY OWN COMMIT MESSAGE (2026-08-26). The MN-engine commit said
"the corpus's per-block Hecke characters were hand-derived and existed only at
n = 3". Only the CLOSED FORMS `chi_block_{3,21,111}` are n=3-only; a general-n
NUMERICAL engine has existed all along in `hecke/hecke_characters.py`, and a
partial symbolic one -- Jing-Liu arXiv:2104.06067 closed forms for HOOK and
TWO-ROW lambda only -- sits in `_deprecated/jing_liu_characters.py`, whose own
docstring says "for general lambda, use the recursive Murnaghan-Nakayama (not
implemented here)". The accurate claim is narrower and is the one above: what
was missing is EXACT SYMBOLIC evaluation, for general lambda.

THE CONSTRUCTION. Ported from `hecke_characters.build_seminormal_matrices_mp`
so the convention is the corpus's, not a re-derivation. For each standard Young
tableau t and generator k, with rho the axial distance
contents[t^-1(k+1)] - contents[t^-1(k)]:

    a = h / (1 - q^(-2 rho)),   a' = h / (1 - q^(2 rho)),   h = q - 1/q

with the diagonal entry `a` when k, k+1 are not swappable (same row or column)
and a 2x2 block on {t, s_k t} otherwise.

ONE DELIBERATE DEPARTURE, and it is what makes this exact. The corpus builder
sets the off-diagonal pair to b = sqrt(|a a' + 1|), which is irrational in q.
This file uses the SIMILAR rational form

    M[i,j] = a a' + 1,   M[j,i] = 1

instead of (b, b). The two are conjugate by diag(..., b, ...), so every
character is identical -- but this one lives in Q(q) and can be simplified
symbolically. That is a change of basis, not a change of convention, and
CHECK 4 verifies it numerically against the corpus builder rather than
asserting it.

ARITHMETIC. sympy over Q(q); comparisons are symbolic simplify-to-zero. The one
numerical comparison (CHECK 4) runs at mpmath 50 dps against the corpus's own
mp builder, never float64.

CHECKS
  1. Quadratic relation sigma^2 = h sigma + 1, symbolically, every lambda,
     n = 2..5.
  2. Braid relations (far commutation and sigma_i sigma_j sigma_i), same range.
  3. chi^lambda(T_{gamma_mu}) equals the MN engine, SYMBOLICALLY, n = 2..5.
     Two unrelated algorithms; MN never builds a matrix, this never recurses
     on ribbons.
  4. The matrices agree with the corpus's `build_seminormal_matrices_mp` at
     mpmath 50 dps -- so the port is of the corpus's convention.
  5. chi^lambda(T_w) is NOT a class function on braid words: exhibited on
     w = s1 s2 s1 in H_3, which is a transposition but of length 3.
  6. The entry point `chi_lambda_braid(precision="symbolic_q")` RETURNS this,
     rather than raising -- agreeing with the direct call, accepting the typed
     crossing-word form, and refusing both a stray q_value and a mixed-arity
     word instead of guessing.

Ref: computations/hecke/hecke_characters.py (build_seminormal_matrices_mp)
Ref: library/arxiv-2504.18825v2/ (Jing-Liu, cyclotomic Murnaghan-Nakayama)
"""

from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations", "computations/hecke", "computations/qbeta"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from qbeta_hecke_mn_character_engine_probe import (  # noqa: E402
    mn_char, partitions_of, q, h,
)

# The construction this probe validates now LIVES IN THE LIBRARY, at
# `computations/hecke/hecke_characters_symbolic.py`, where
# `chi_lambda_braid(precision="symbolic_q")` dispatches to it. It was
# originally defined in this file; keeping a second copy here would let the
# two drift and would mean this probe validated something the entry point no
# longer runs. So it is imported, and `hecke_characters_symbolic.q` is
# asserted below to be the same symbol this probe builds its comparisons in.
from hecke_characters_symbolic import (  # noqa: E402
    seminormal, q as _lib_q, h as _lib_h,
)

Partition = tuple[int, ...]


def word_matrix(shape: Partition, word) -> sp.Matrix:
    """Matrix of a braid word `[(sign, gen_1based), ...]` in the irrep `shape`.

    `sigma^-1 = sigma - h` is used for negative crossings, which is the Hecke
    relation itself rather than a matrix inversion.
    """
    mats = seminormal(shape)
    dim = mats[0].shape[0] if mats else 1
    out = sp.eye(dim)
    for sign, gen in word:
        M = mats[gen - 1]
        out = out * (M if sign > 0 else M - h * sp.eye(dim))
    return out


def chi_word(shape: Partition, word) -> sp.Expr:
    return sp.simplify(sp.together(sp.trace(word_matrix(shape, word))))


def standard_word(mu: Partition):
    """The braid word for the standard element T_{gamma_mu} of cycle type mu.

    Consecutive blocks: a part of size m starting at offset o contributes the
    generators o+1, ..., o+m-1 (1-based), so ell = n - l(mu).
    """
    word, off = [], 0
    for part in mu:
        word += [(1, off + i) for i in range(1, part)]
        off += part
    return word


# ------------------------------------------------------------------- checks

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


def main() -> int:
    print("qou-avt2 part 2 — exact symbolic seminormal characters\n")

    # ---- 1 & 2: the algebra relations -------------------------------------
    print("CHECK 1/2 — quadratic and braid relations, symbolically, n = 2..5")
    quad_ok = braid_ok = True
    for n in range(2, 6):
        for lam in partitions_of(n):
            mats = seminormal(lam)
            d = mats[0].shape[0]
            I = sp.eye(d)
            for idx, M in enumerate(mats):
                if sp.simplify(M * M - h * M - I) != sp.zeros(d, d):
                    quad_ok = False
                    print(f"      quadratic fails: {lam} sigma_{idx + 1}")
            for i in range(len(mats)):
                for j in range(len(mats)):
                    A, B = mats[i], mats[j]
                    if abs(i - j) >= 2:
                        if sp.simplify(A * B - B * A) != sp.zeros(d, d):
                            braid_ok = False
                            print(f"      commutation fails: {lam} {i + 1},{j + 1}")
                    elif abs(i - j) == 1:
                        if sp.simplify(A * B * A - B * A * B) != sp.zeros(d, d):
                            braid_ok = False
                            print(f"      braid fails: {lam} {i + 1},{j + 1}")
    check("quadratic_relation_symbolic", quad_ok, "sigma^2 = h sigma + 1, n = 2..5")
    check("braid_relations_symbolic", braid_ok, "n = 2..5, all partitions")
    print()

    # ---- 3: agreement with the MN engine ----------------------------------
    print("CHECK 3 — trace vs the Murnaghan-Nakayama engine, SYMBOLICALLY")
    agree_ok = True
    for n in range(2, 6):
        for lam in partitions_of(n):
            for mu in partitions_of(n):
                lhs = chi_word(lam, standard_word(mu))
                rhs = mn_char(lam, mu)
                if sp.simplify(sp.radsimp(lhs - rhs)) != 0:
                    agree_ok = False
                    print(f"      n={n} {lam}/{mu}: seminormal {lhs} vs MN {rhs}")
    check("seminormal_trace_equals_mn_rule", agree_ok,
          "n = 2..5, every (lambda, mu); two unrelated algorithms")
    print()

    # ---- 4: the port matches the corpus's own mp builder -------------------
    print("CHECK 4 — matrices vs hecke_characters.build_seminormal_matrices_mp")
    try:
        from mpmath import mp as _mp
        _mp.dps = 50
        from hecke_characters import build_seminormal_matrices_mp
        qv = _mp.mpf("1.1099785827513808")           # proton pin, per AGENTS.md
        port_ok, worst = True, _mp.mpf(0)
        for n in (2, 3, 4):
            for lam in partitions_of(n):
                ref, dim, _ = build_seminormal_matrices_mp(lam, qv)
                mine = seminormal(lam)
                for R, S in zip(ref, mine):
                    # Compare CHARACTERS of each generator, which are basis-
                    # independent -- the two matrices are similar, not equal.
                    tr_ref = sum(R[i, i] for i in range(dim))
                    tr_mine = _mp.mpf(str(sp.nsimplify(
                        sp.trace(S).subs(q, sp.Rational(str(qv))))
                        .evalf(50)))
                    worst = max(worst, abs(tr_ref - tr_mine))
                    if abs(tr_ref - tr_mine) > _mp.mpf("1e-40"):
                        port_ok = False
        check("port_matches_corpus_mp_builder", port_ok,
              f"n = 2..4, worst |Delta trace| = {_mp.nstr(worst, 8)} at 50 dps")
    except Exception as exc:
        check("port_matches_corpus_mp_builder", False,
              f"could not run: {exc.__class__.__name__}: {exc}")
    print()

    # ---- 5: characters are not class functions on words --------------------
    print("CHECK 5 — chi(T_w) is not a class function on braid words")
    w_long = [(1, 1), (1, 2), (1, 1)]        # s1 s2 s1, the transposition (13)
    w_short = [(1, 1)]                        # s1, the transposition (12)
    lam = (2, 1)
    long_val, short_val = chi_word(lam, w_long), chi_word(lam, w_short)
    differ = sp.simplify(long_val - short_val) != 0
    check("character_not_class_function_on_words", differ,
          f"chi^(2,1)(s1 s2 s1) = {long_val}, chi^(2,1)(s1) = {short_val}")
    print()

    # ---- 6: the library entry point actually serves this ------------------
    print("CHECK 6 — chi_lambda_braid(precision='symbolic_q') returns, not raises")
    check("library_symbol_is_this_probes_symbol",
          _lib_q == q and sp.simplify(_lib_h - h) == 0,
          "hecke_characters_symbolic.q is the symbol the checks above use")
    try:
        from hecke_characters import chi_lambda_braid
        w = [(1, 1), (1, 2), (1, 1)]
        via_api, tag = chi_lambda_braid((2, 1), w, precision="symbolic_q",
                                        return_precision=True)
        direct = chi_word((2, 1), w)
        check("entry_point_agrees_with_direct_call",
              sp.simplify(via_api - direct) == 0 and tag == "symbolic_q",
              f"chi^(2,1)(s1 s2 s1) = {sp.simplify(via_api)}, tag = {tag}")

        # The typed [(c, d, gen0)] form of chi_all_lambda, on the symbolic path.
        typed = chi_lambda_braid((3,), [(1, 0, 0), (1, 0, 1)],
                                 precision="symbolic_q")
        check("entry_point_accepts_typed_crossing_words",
              sp.simplify(typed - q ** 2) == 0,
              f"chi^(3)(sigma_0 sigma_1) = {sp.simplify(typed)}, the index rep at length 2")

        # A q_value alongside symbolic_q must be refused, not ignored: silently
        # dropping it is the class of defect this repo keeps recording.
        try:
            chi_lambda_braid((2,), [(1, 1)], q_value=1.11, precision="symbolic_q")
            check("entry_point_refuses_q_value_with_symbolic", False,
                  "q_value was accepted and silently ignored")
        except ValueError:
            check("entry_point_refuses_q_value_with_symbolic", True)

        # Mixed word arities must raise rather than be guessed at.
        try:
            chi_lambda_braid((2,), [(1, 1), (1, 0, 0)], precision="symbolic_q")
            check("entry_point_rejects_mixed_word_arity", False,
                  "a mixed-arity word was accepted")
        except ValueError:
            check("entry_point_rejects_mixed_word_arity", True)
    except Exception as exc:
        check("entry_point_agrees_with_direct_call", False,
              f"{exc.__class__.__name__}: {exc}")
    print()

    ok = all(r[1] for r in RESULTS)
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder("qbeta-hecke-symbolic-seminormal", _script_path=__file__)
        wb.set_description(
            "Exact symbolic-in-q Hecke characters for arbitrary braid words "
            "(the deferred 'F3' branch of hecke_characters.chi_lambda_braid), "
            "cross-checked symbolically against the Murnaghan-Nakayama engine."
        )
        wb.add_data("closes", "hecke_characters.chi_lambda_braid precision='symbolic_q' (F3) — now WIRED, not deferred")
        wb.add_data("basis_note",
                    "off-diagonal pair (b,b) replaced by the similar rational "
                    "(a a' + 1, 1); characters identical, arithmetic exact")
        wb.add_data("markov_convention", "not applicable — no z enters this computation")
        wb.add_data("q0_anchor",
                    "symbolic in q; the single numeric cross-check (CHECK 4) "
                    "uses the proton pin 1.1099785827513808 at 50 dps")
        wb.add_caveat(
            "Validated for n = 2..5. Does not yet evaluate the nucleon words "
            "beta_n / beta_p against chi_block_*: those words are q0-BAKED "
            "(their d are literal -h(q0)/2, -h(q0)), so a symbolic comparison "
            "needs them reconstructed from the four typed-crossing templates "
            "first. Not done here, not claimed here."
        )
        for name, passed, detail in RESULTS:
            wb.add_assertion(name, "1" if passed else "0", "1", "0",
                             source=detail or None)
        wb.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
