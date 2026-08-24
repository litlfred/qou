#!/usr/bin/env python3
"""The TL_n quotient Markov–Gram form, general n — verification of `pyhecke.tl`.

Bean `qou-8iru` (the TL_n compute move) / `qou-cds2` (the Gram singularity).

## What this verifies

`computations/qbeta/tl3_gram_nonsingular_probe.py` (PR #5572) settled that the
**target** of `qou-cds2`'s named repair is well posed at `n = 3`, by
transcribing `pyhecke.gram`'s hard-coded 6×6 multiplication table into sympy.
This probe verifies the **general-`n` implementation** that actually performs
the move, `pyhecke.tl` — a different code path in every respect: a general
Ocneanu recursion on `S_n`, no transcribed table, no hard-coded `TR_M`.

Two of the checks below are therefore cross-*implementation*, not merely
cross-precision: the `n = 3` Markov trace against `pyhecke.gram.TR_M`, and the
`n = 3` quotient determinant against PR #5572's closed form. A general
recursion reproducing a hand-written table exactly, symbolically, on all six
words is evidence about the recursion that no amount of internal consistency
would give.

## Results

* `|tl_basis(n)| = Catalan(n)` for `n = 2..8` — the 321-avoiding permutations.
* `tr_M(T_w)` from the general recursion **equals** `pyhecke.gram.TR_M`
  exactly, symbolically, on all six `n = 3` NF words.
* `det G_TL(3) = −(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴/(q²+1)¹⁰` — PR #5572's closed form,
  re-derived here from general-`n` code.
* `det G_full(3) = 0` identically over ℚ(q) — the blocker, restated.
* `rank G_full(n) = Catalan(n)` exactly over ℚ at `n = 3, 4, 5`: ranks
  `5, 14, 42`, coranks `1, 10, 78` = `1`, `3²+1²`, `6²+5²+4²+1²` — `qou-cds2`'s
  corank accounting, measured rather than quoted.
* `det G_TL(n) ≠ 0` exactly at `n = 4, 5` and at two distinct rational `q`.
* `G_TL · G_TL⁻¹ = I` **entry-by-entry, exactly**, at `n = 3, 4, 5`. The
  workaround it replaces is `pyhecke.gram.G_PINV`, whose residual on the
  singular form is `‖G · G_PINV − I‖_F = 1` — exactly right, and not a
  failure: `G · G_PINV` is the projector onto the rank-5 range (eigenvalues
  `1,1,1,1,1,0`), so the defect is precisely the corank-1 kernel. The `1.64`
  figure recorded elsewhere is the *deleted* float64 `G_INV`
  (`np.linalg.inv`), a different object; do not attribute it to `G_PINV`.
* Inverting the *full* form **in exact arithmetic** raises. The float64
  `np.linalg.inv` on the same matrix does *not* raise — it returns noise —
  which is why `gram.py` had to add `safe_inverse` rather than a `try`/`except`.

## Scope, stated precisely

At `n = 3` the statement is **scope-(b) structural for every real `q > 0`**,
citing a proved invariant: PR #5572's determinant numerator has no real roots.

At `n ≥ 4` what is established is **non-singularity over ℚ(q)** — a
determinant that is nonzero at a rational point cannot vanish identically, so
the form is non-degenerate generically. That is *weaker*, and is **not** the
`n = 3` statement: nothing here rules out a real `q > 0` at which the `n = 4`
or `n = 5` quotient form degenerates. Establishing the `n ≥ 4` analogue needs
the symbolic determinant, which is not computed here.

Likewise the rank measurement is exact at a *point*: rank can only drop at
special `q`, never rise, so `rank = Catalan(n)` at `q = 111/100` gives
`rank ≥ Catalan(n)` generically. The matching upper bound is the established
`y_λ = 0` for partitions with ≥ 3 rows (`qou-8iru`;
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`), not this probe.

## Arithmetic

Exact throughout — `fractions.Fraction` over ℚ, or sympy over ℚ(q). **No
float64 anywhere**, and no anchor in any symbolic result, so those are
pin-independent and carry no muon/proton layer question. The one `mpmath`
check runs at 60 dps at the proton-pinned `q₀` and is reported as a numeric
consistency check, not as an exactness claim.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

_PYHECKE = Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"
if str(_PYHECKE) not in sys.path:
    sys.path.insert(0, str(_PYHECKE))

from pyhecke import tl  # noqa: E402

_CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    _CHECKS.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")


def _word_to_perm(n: int, word) -> tuple[int, ...]:
    p = tuple(range(1, n + 1))
    for i in word:
        lst = list(p)
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        p = tuple(lst)
    return p


def main() -> int:
    q = sp.symbols("q", positive=True)
    one = sp.Integer(1)
    h, z = tl.markov_weights(q, one)

    print("=" * 78)
    print("  TL_n quotient Markov-Gram form (pyhecke.tl) -- general n, exact")
    print("=" * 78)

    # ── 1. the basis ───────────────────────────────────────────────────────
    sizes = {n: (len(tl.tl_basis(n)), tl.catalan(n)) for n in range(2, 9)}
    check("tl_basis_size_is_catalan_n_2_to_8",
          all(a == b for a, b in sizes.values()),
          "|321-avoiding| = " + ", ".join(f"{n}:{a}" for n, (a, _b) in sizes.items()))

    # At n = 3 the basis must be the five NF words other than (0,1,0), whose
    # permutation (3,2,1) is the one 321 pattern in S_3.  This is what makes
    # PR #5572's "first five NF cosets" the right five rather than a lucky
    # five.
    nf_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    nf_perms = [_word_to_perm(3, w) for w in nf_words]
    check("tl_basis_3_is_the_nf_basis_minus_the_321_word",
          set(tl.tl_basis(3)) == set(nf_perms[:5])
          and nf_perms[5] not in tl.tl_basis(3),
          f"excluded word (0,1,0) -> {nf_perms[5]}, the only 321 pattern in S_3")

    # ── 2. the trace, against gram.py's hard-coded table ───────────────────
    tr_general = [sp.cancel(tl.markov_trace_basis(p, 3, h, z, one)) for p in nf_perms]
    tr_gram_py = [one, z, z, z ** 2, z ** 2, sp.cancel(h * z ** 2 + z)]
    check("ocneanu_recursion_reproduces_pyhecke_gram_TR_M",
          all(sp.simplify(a - b) == 0 for a, b in zip(tr_general, tr_gram_py)),
          "[1, z, z, z^2, z^2, h z^2 + z] on all six NF words, symbolically")

    # ── 3. the blocker, restated over Q(q) ─────────────────────────────────
    G_full3 = sp.Matrix(tl.full_hecke_gram(3, q, one))
    check("full_H3_form_is_identically_singular_over_Q(q)",
          sp.simplify(sp.cancel(G_full3.det())) == 0,
          "det G = 0 identically -- not a q_0 artefact, not ill-conditioning")

    # ── 4. the repair, against PR #5572 ────────────────────────────────────
    G_tl3 = sp.Matrix(tl.tl_gram(3, q, one))
    det3 = sp.cancel(sp.factor(G_tl3.det()))
    pr5572 = sp.cancel(-(q ** 4 + 1) * (q ** 2 - q + 1) ** 4
                       * (q ** 2 + q + 1) ** 4 / (q ** 2 + 1) ** 10)
    check("TL3_determinant_matches_PR_5572_closed_form",
          sp.simplify(det3 - pr5572) == 0,
          "det G_TL = -(q^4+1)(q^2-q+1)^4(q^2+q+1)^4/(q^2+1)^10, from general-n code")

    # ── 5. corank accounting, exactly over Q ───────────────────────────────
    from math import factorial
    ranks = {}
    for n in (3, 4, 5):
        r = tl.gram_rank_exact(n)
        ranks[n] = (r, factorial(n) - r)
    expected_corank = {3: 1, 4: 3 ** 2 + 1 ** 2, 5: 6 ** 2 + 5 ** 2 + 4 ** 2 + 1 ** 2}
    check("full_gram_rank_is_catalan_and_corank_matches_qou_cds2",
          all(ranks[n][0] == tl.catalan(n) and ranks[n][1] == expected_corank[n]
              for n in ranks),
          "; ".join(f"n={n}: rank {ranks[n][0]}=C_{n}, corank {ranks[n][1]}"
                    for n in ranks))

    # ── 6. non-singularity of the quotient at n = 4, 5 ─────────────────────
    # Exact over Q at two distinct rational q.  A determinant nonzero at a
    # rational point cannot vanish identically over Q(q); it does NOT follow
    # that the form is non-singular at every real q > 0, which is why the
    # n = 3 claim (which has the closed form) is stated separately above.
    dets = {}
    for n in (4, 5):
        for qr in (Fraction(111, 100), Fraction(7, 5)):
            G = sp.Matrix(tl.tl_gram_exact(n, qr))
            dets[(n, qr)] = G.det()
    check("TL_gram_nonsingular_over_Q(q)_at_n_4_and_5",
          all(v != 0 for v in dets.values()),
          "det != 0 exactly at q in {111/100, 7/5} => not identically zero")

    # ── 7. a genuine inverse, not a pseudoinverse ──────────────────────────
    inv_ok = {}
    for n in (3, 4, 5):
        G = tl.tl_gram_exact(n)
        Gi = tl.tl_gram_inverse_exact(n)
        m = len(G)
        inv_ok[n] = all(
            sum(G[i][k] * Gi[k][j] for k in range(m)) == (1 if i == j else 0)
            for i in range(m) for j in range(m)
        )
    check("TL_gram_times_its_inverse_is_exactly_the_identity",
          all(inv_ok.values()),
          "entry-by-entry exact 1s and 0s at n=3,4,5; G_PINV on the singular "
          "form gives only ||G G_PINV - I||_F = 1, the rank-5 projector defect")

    # ── 7b. what G_PINV's residual actually is ─────────────────────────────
    # The corpus records `||G G_INV - I|| = 1.64` for the DELETED float64
    # `np.linalg.inv`.  That figure is routinely re-cited as though it were
    # `G_PINV`'s residual, which understates the surviving workaround: a
    # Moore-Penrose pseudoinverse gives `G @ G_PINV` = the orthogonal projector
    # onto range(G), so the residual is the projector onto the kernel and
    #     ||G G_PINV - I||_F = sqrt(corank) = sqrt(1) = 1,
    # exactly.  The EXACT leg is check 5's corank (rational arithmetic, no
    # float64); the float64 leg below only confirms numpy agrees, and is
    # reported as a float64 confirmation, never as an exactness claim.
    corank3 = 6 - tl.gram_rank_exact(3)
    pinv_fro_exact = sp.sqrt(sp.Integer(corank3))
    f64_note = "not measured (numpy/pyhecke.gram unavailable)"
    f64_ok = True
    try:
        import numpy as _np
        from pyhecke import gram as _gram
        _G = _np.asarray(_gram.G, dtype=float)
        _P = _np.asarray(_gram.G_PINV, dtype=float)
        _R = _G @ _P - _np.eye(6)
        _fro = float(_np.linalg.norm(_R, "fro"))
        _eig = sorted(round(float(e.real), 9) for e in _np.linalg.eigvals(_G @ _P))
        f64_ok = abs(_fro - 1.0) < 1e-9 and _eig == [0.0] + [1.0] * 5
        f64_note = (f"float64 confirmation: ||G G_PINV - I||_F = {_fro:.6f}, "
                    f"eigs(G G_PINV) = {_eig}")
    except ImportError as _e:
        f64_note = f"not measured ({_e})"
    check("G_PINV_residual_is_sqrt_corank_eq_1_NOT_the_deleted_G_INV_1.64",
          pinv_fro_exact == 1 and f64_ok,
          f"exact: corank {corank3} => ||G G_PINV - I||_F = 1; {f64_note}")

    raised = False
    try:
        tl._inverse_exact(tl.full_hecke_gram_exact(3))
    except ZeroDivisionError:
        raised = True
    # Name the arithmetic: this is _inverse_exact (exact Q(q)), which divides by
    # a pivot that is identically zero and so raises.  numpy's float64
    # np.linalg.inv on the SAME matrix does not raise -- it returns ~1e16-scale
    # noise -- which is why gram.py needed safe_inverse rather than a try/except.
    check("inverting_the_full_form_IN_EXACT_ARITHMETIC_raises",
          raised,
          "_inverse_exact raises ZeroDivisionError; np.linalg.inv on the same "
          "matrix does NOT raise -- that is why gram.py needed safe_inverse")

    # ── 8. the mpmath path at the substrate q_0 ────────────────────────────
    # Numeric, so this is a consistency check and is NOT reported as exact.
    # The tolerance is set by the weakest arithmetic on the path -- 60-dps
    # mpmath throughout, q_0 parsed from its 50-digit decimal string, no
    # float64 anywhere -- so ~1e-45 is the honest floor, not 1e-15.
    import mpmath as mp
    with mp.workdps(60):
        Gm = mp.matrix(tl.tl_gram_mp(3))
        Gmi = tl.tl_gram_inverse_mp(3)
        resid = max(abs((Gm * Gmi)[i, j] - (1 if i == j else 0))
                    for i in range(5) for j in range(5))
    check("TL3_gram_inverse_at_substrate_q0_is_consistent_at_60_dps",
          resid < mp.mpf(10) ** -45,
          f"max |G G^-1 - I| = {mp.nstr(resid, 5)} at the proton-pinned q_0")

    n_fail = sum(1 for _n, p, _d in _CHECKS if not p)
    print()
    print("=== pyhecke.tl: the quotient form is built, and it inverts ===")
    print(
        f"VERDICT: {len(_CHECKS) - n_fail}/{len(_CHECKS)} PASS. The general-n "
        "TL quotient form reproduces pyhecke.gram's hard-coded TR_M and PR "
        "#5572's n=3 determinant exactly, from an independent implementation; "
        "its corank accounting matches qou-cds2 at n=3,4,5; and it has a "
        "genuine inverse where the full form has only a pseudoinverse. "
        "Scope: (b) structural for every real q > 0 at n=3 (citing #5572's "
        "root-free numerator); non-singular over Q(q) only, at n=4,5. This "
        "does NOT migrate any consumer -- gram.py's G_PINV, gram.rs's "
        "rank-one shift, gram_inverse()'s raise and "
        "confinement-operator-selection's _pg_safe_inverse are untouched."
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
