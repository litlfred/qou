#!/usr/bin/env python3
"""What operation actually intertwines ``V_lambda`` with ``V_{lambda'}``?

``eigenbasis-structural-lemmas`` item 2 asserts:

    "The bar involution q -> q^{-1} swaps the seminormal eigenvalues
     q <-> -q^{-1} and intertwines V_lambda with the conjugate channel
     V_{lambda'}.  Thus chi_lambda(q^{-1}) = eps_lambda * chi_{lambda'}(q)
     for some eps_lambda in {+1,-1}."

PR #4826 showed the premise is wrong: the bar involution of
``def:bar-involution`` (``sigma_i -> sigma_i^{-1}``, ``q -> q^{-1}``) *fixes*
each Hecke eigenchannel rather than swapping them.  This probe settles the
two questions that leaves open.

**Q1 -- what does produce the swap?**  The sign-twisted map

    hash: sigma_i -> -sigma_i^{-1}     (coefficients untouched)

sends a ``q``-eigenvector to eigenvalue ``-q^{-1}`` and back.  It is checked
here to be an algebra automorphism (Hecke relation + braid relation
preserved), and it is the operation that carries ``V_lambda`` to
``V_{lambda'}``.  This is the Iwahori-Matsumoto-type sign twist, not the bar
involution; the two differ by exactly the sign.

**Q2 -- does the stated character identity survive?**  Tested on every braid
word up to length 6 in ``H_2`` and ``H_3``.  The identity holds, but the sign
is **not** a function of ``lambda``: it is ``(-1)^L`` in the word length ``L``.
So the conclusion is sound and the labelling ``eps_lambda`` is not -- writing
the sign with a ``lambda`` subscript claims a per-channel constant that the
characters do not have.  On the self-conjugate channel ``(2,1)`` of ``H_3``
the same ``(-1)^L`` appears, which is a sharper statement than the block
makes.

Note this makes item 2 a corollary of item 1 (parity): given
``chi(-q) = (-1)^L chi(q)``, the identity is equivalent to the *unsigned*
statement ``chi_lambda(-q^{-1}) = chi_{lambda'}(q)`` -- i.e. exactly the
eigenvalue swap ``q -> -q^{-1}``, applied to the character variable.  That is
the honest form: the swap is real, it is just not the bar involution.

Scope: this tests the character identity and the intertwiner, on ``H_2`` and
``H_3``.  It does not re-derive item 1 or item 3.

Conventions
-----------
Hecke relation ``sigma^2 = h*sigma + 1`` with ``h = q - q^{-1}``, eigenvalues
``q`` and ``-q^{-1}`` (AGENTS Hecke-Skein convention).  Everything is exact in
sympy over ``QQ(q)``; no substrate pin is used or needed.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate import WitnessBuilder  # noqa: E402

q = sp.Symbol("q")
h = q - 1 / q


def bar(expr):
    """The coefficient half of def:bar-involution: q -> q^{-1}."""
    return sp.simplify(sp.together(expr.subs(q, 1 / q)))


def h2_reps():
    """Irreps of H_2: lambda = (2) and (1,1), each 1-dimensional."""
    return {
        "(2)": [sp.Matrix([[q]])],
        "(1,1)": [sp.Matrix([[-1 / q]])],
    }


def h3_reps():
    """Irreps of H_3: (3), (2,1) [2-dim Hoefsmit], (1,1,1)."""
    s1 = sp.Matrix([[q, 1], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [1, q]])
    return {
        "(3)": [sp.Matrix([[q]]), sp.Matrix([[q]])],
        "(2,1)": [s1, s2],
        "(1,1,1)": [sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])],
    }


CONJUGATE = {
    "(2)": "(1,1)",
    "(1,1)": "(2)",
    "(3)": "(1,1,1)",
    "(1,1,1)": "(3)",
    "(2,1)": "(2,1)",  # self-conjugate
}


def char(gens, word):
    """Character of the positive braid word ``word`` (a tuple of generator
    indices) in the representation given by ``gens``."""
    m = sp.eye(gens[0].shape[0])
    for i in word:
        m = m * gens[i]
    return sp.simplify(sp.together(m.trace()))


def main() -> int:
    wb = WitnessBuilder("hecke-conjugation-duality-sign", engine="python")
    wb.set_description(
        "The V_lambda <-> V_{lambda'} intertwiner is the sign-twisted map "
        "sigma -> -sigma^{-1}, not the bar involution. The character identity "
        "of eigenbasis-structural-lemmas item 2 holds, but its sign is "
        "(-1)^L in the word length, not a per-channel eps_lambda."
    )
    wb.set_content_block("prop:eigenbasis-structural-lemmas")

    checks: dict[str, bool] = {}

    # ---- Q1. The sign-twisted map is an automorphism, and it swaps. -----
    s1 = sp.Matrix([[q, 1], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [1, q]])
    ident = sp.eye(2)
    checks["h3_rep_satisfies_hecke"] = all(
        sp.simplify(s * s - h * s - ident) == sp.zeros(2, 2) for s in (s1, s2)
    )
    checks["h3_rep_satisfies_braid"] = (
        sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2, 2)
    )

    # hash(sigma) = -sigma^{-1}
    t1, t2 = sp.simplify(-s1.inv()), sp.simplify(-s2.inv())
    checks["signtwist_preserves_hecke"] = all(
        sp.simplify(t * t - h * t - ident) == sp.zeros(2, 2) for t in (t1, t2)
    )
    checks["signtwist_preserves_braid"] = (
        sp.simplify(t1 * t2 * t1 - t2 * t1 * t2) == sp.zeros(2, 2)
    )
    # On eigenvalues: q -> -q^{-1} and -q^{-1} -> q.  (1-dim reps suffice.)
    checks["signtwist_swaps_eigenvalues"] = (
        sp.simplify(-(sp.Matrix([[q]]).inv())[0, 0] - (-1 / q)) == 0
        and sp.simplify(-(sp.Matrix([[-1 / q]]).inv())[0, 0] - q) == 0
    )
    # The bar involution, by contrast, FIXES them (PR #4826).
    checks["bar_fixes_eigenvalues_not_swaps"] = (
        sp.simplify(bar((s1.inv())[0, 0]) - q) == 0
    )
    # The sign twist carries the (3) rep onto the (1,1,1) rep.
    checks["signtwist_carries_triv_to_sign"] = (
        sp.simplify(-(sp.Matrix([[q]]).inv())[0, 0] - (-1 / q)) == 0
    )

    # ---- Q2. Test the character identity over many words. ---------------
    results = []
    n_words = 0
    for label, reps, ngen in [("H_2", h2_reps(), 1), ("H_3", h3_reps(), 2)]:
        for L in range(1, 7):
            for word in itertools.product(range(ngen), repeat=L):
                n_words += 1
                for lam, gens in reps.items():
                    lamp = CONJUGATE[lam]
                    chi_lam = char(gens, word)
                    chi_lamp = char(reps[lamp], word)
                    lhs = bar(chi_lam)
                    # Solve for the sign that makes the identity hold.  When
                    # the character vanishes identically BOTH signs work, so
                    # the word determines no sign at all -- record that as
                    # "either" rather than silently picking +1 (which would
                    # manufacture a spurious counterexample to eps = (-1)^L).
                    vanishes = sp.simplify(chi_lamp) == 0 and sp.simplify(lhs) == 0
                    if vanishes:
                        eps = "either"
                    elif sp.simplify(lhs - chi_lamp) == 0:
                        eps = 1
                    elif sp.simplify(lhs + chi_lamp) == 0:
                        eps = -1
                    else:
                        eps = None
                    results.append(
                        {
                            "algebra": label,
                            "word": "".join(f"s{i + 1}" for i in word),
                            "L": L,
                            "lambda": lam,
                            "lambda_conj": lamp,
                            "eps": eps,
                            "eps_matches_minus1_pow_L": (
                                eps == "either" or (eps is not None and eps == (-1) ** L)
                            ),
                        }
                    )

    checks["identity_holds_for_every_word"] = all(
        r["eps"] is not None for r in results
    )
    checks["sign_is_always_minus1_pow_L"] = all(
        r["eps_matches_minus1_pow_L"] for r in results
    )

    # The decisive negative: eps is NOT a function of lambda alone.  For a
    # fixed lambda it takes both values as L varies.
    by_lambda: dict[str, set] = {}
    for r in results:
        if r["eps"] != "either":  # vanishing characters constrain nothing
            by_lambda.setdefault(r["lambda"], set()).add(r["eps"])
    checks["eps_is_not_a_function_of_lambda"] = all(
        v == {1, -1} for v in by_lambda.values()
    )
    # ...including on the self-conjugate channel, where the block's phrasing
    # would predict a single constant.
    checks["self_conjugate_channel_also_varies"] = by_lambda.get(
        "(2,1)"
    ) == {1, -1}
    # Record how many words determined no sign, so the vanishing case is
    # visible rather than quietly folded into the pass.
    n_vanishing = sum(1 for r in results if r["eps"] == "either")

    # ---- The honest unsigned form: chi_lambda(-q^{-1}) = chi_{lambda'}(q).
    # Equivalent to the above given item 1's parity chi(-q) = (-1)^L chi(q).
    unsigned_ok = True
    for label, reps, ngen in [("H_2", h2_reps(), 1), ("H_3", h3_reps(), 2)]:
        for L in range(1, 5):
            for word in itertools.product(range(ngen), repeat=L):
                for lam, gens in reps.items():
                    lhs = sp.simplify(
                        sp.together(char(gens, word).subs(q, -1 / q))
                    )
                    rhs = char(reps[CONJUGATE[lam]], word)
                    if sp.simplify(lhs - rhs) != 0:
                        unsigned_ok = False
    checks["unsigned_swap_form_holds"] = unsigned_ok

    all_pass = all(checks.values())

    wb.add_parameter("exact", "sympy over QQ(q); no substrate pin used")
    wb.add_parameter("q_0_pin", "not applicable (symbolic in q)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_data("checks", {k: bool(v) for k, v in checks.items()})
    wb.add_data("n_words_tested", n_words)
    wb.add_data("n_character_evaluations_with_vanishing_character", n_vanishing)
    wb.add_data(
        "eps_values_by_lambda",
        {k: sorted(x for x in v if x is not None) for k, v in by_lambda.items()},
    )
    wb.add_data("sample_rows", results[:12])

    wb.add_assertion(
        "checks_failed", sum(1 for v in checks.values() if not v), 0,
        source="sympy exact",
    )
    wb.add_assertion(
        "n_lambda_with_a_constant_sign",
        sum(1 for v in by_lambda.values() if len(v) == 1), 0,
        source="sympy exact; a constant eps_lambda would make this nonzero",
    )

    wb.add_data(
        "interpretation",
        {
            "the_intertwiner": (
                "sigma_i -> -sigma_i^{-1} (the Iwahori-Matsumoto-type sign "
                "twist) is an algebra automorphism that swaps the eigenvalues "
                "q <-> -q^{-1} and carries V_lambda to V_{lambda'}. The bar "
                "involution does not: it fixes each eigenchannel. The two "
                "differ by exactly the sign."
            ),
            "the_identity_holds": (
                "chi_lambda(q^{-1}) = eps * chi_{lambda'}(q) is true on every "
                "braid word tested in H_2 and H_3, so the block's conclusion "
                "-- and the matter/antimatter reading built on it -- stands."
            ),
            "but_the_sign_is_not_per_channel": (
                "eps = (-1)^L in the word length L, not a constant eps_lambda "
                "attached to the partition. For every lambda tested, "
                "including the self-conjugate (2,1), eps takes both values as "
                "L varies. Writing eps_lambda claims a per-channel invariant "
                "that does not exist."
            ),
            "honest_restatement": (
                "chi_lambda(-q^{-1}) = chi_{lambda'}(q), unsigned. Combined "
                "with item 1's parity chi(-q) = (-1)^L chi(q) this reproduces "
                "the signed form, and it says plainly what the operation is: "
                "the eigenvalue swap q -> -q^{-1}."
            ),
        },
    )

    wb.add_caveat(
        "Verified on H_2 and H_3 over braid words of length <= 6 (length <= 4 "
        "for the unsigned form). Not a proof for general n; the Hoefsmit "
        "2-dimensional (2,1) rep is the only multi-dimensional channel "
        "exercised."
    )
    wb.add_caveat(
        "Positive braid words only (no sigma_i^{-1} letters). The parity "
        "bookkeeping (-1)^L is stated for L = word length in that setting; "
        "for words with negative letters L should be read as the exponent "
        "sum, which is not tested here."
    )

    path = wb.save()

    print("=" * 70)
    print("Hecke conjugation duality -- what swaps V_lambda and V_{lambda'}?")
    print("=" * 70)
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print(f"  words tested: {n_words}   "
          f"(evaluations with a vanishing character: {n_vanishing})")
    print("  eps values seen, by channel:")
    for k, v in by_lambda.items():
        print(f"    {k:10s} -> {sorted(x for x in v if x is not None)}")
    print()
    print("  intertwiner  : sigma -> -sigma^{-1}   (NOT the bar involution)")
    print("  identity     : holds, with eps = (-1)^L")
    print("  honest form  : chi_lambda(-1/q) = chi_{lambda'}(q), unsigned")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
