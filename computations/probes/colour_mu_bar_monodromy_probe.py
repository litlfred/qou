#!/usr/bin/env python3
"""Milnor's mu-bar on the Bring monodromy image — closing F5 of qou-dg07.

Two probes led here. `colour_sign_line_pure_braid_probe` showed the two
colour sign lines are different sections, separated by `ker(B_3 -> S_3)`,
and named one residual (its F5): the separation is unconditional on
`B_3`, but whether THIS fibration's monodromy image realises a
witnessing pair was open. `bring_monodromy_braid_lift_probe` then lifted
the six local monodromies to `B_3` and found the image's pure part
nontrivial — narrowing that residual without closing it, because

    a NONTRIVIAL pure braid can still have mu-bar = 0.

This probe computes `mu-bar_123` for the closures of the pure braids in
the image, which is the difference between "the two functions differ
somewhere" and "they demonstrably differ HERE".

METHOD (Milnor via Magnus, the route Mellor-Melvin state and the dg07
audit already cites). For a PURE braid the Artin image is a conjugation

    x_i  |-->  w_i x_i w_i^{-1},

and `w_i` is the i-th longitude of the closure. Milnor's invariants are
Magnus coefficients of the longitudes:

    mu-bar_{123}  =  eps_{12}(w_3),

the coefficient of `X_1 X_2` in the Magnus expansion of `w_3` -- a SINGLE
coefficient, matching the corpus's own validated tower
(`gap2_he4_borromean_mu_bar.mu`: "coeff of X_{i_1}..X_{i_{k-1}} in the
Magnus image of l_{i_k}"). Milnor's cyclic symmetry makes
`eps_{12}(w_3) = eps_{23}(w_1) = eps_{31}(w_2)`, so this probe computes
all three and reports their agreement as a free internal check on every
braid. The invariant is well defined modulo the gcd of the pairwise
linking numbers, and unambiguously when those vanish (the Brunnian
case). Pairwise linking is the degree-1 coefficient,
`lk(i,j) = eps_i(w_j)`.

    CORRECTION, made by the self-test below before any result was
    produced: this probe was first written with
    `mu-bar = eps_{12}(w_3) + eps_{23}(w_1) + eps_{31}(w_2)`, summing
    three quantities that Milnor's cyclic symmetry makes EQUAL. It
    returned `-3` on the Borromean rings against the known `+-1` -- an
    exact factor of 3, which is what a triple-count looks like. The
    summed form never reached a witness, an audit doc or a bean; it
    existed only in this file's first draft. The corpus was checked and
    carries the single-coefficient form in both
    `gap2_he4_borromean_mu_bar.py` and the tower it cites.

Everything is exact integer arithmetic on truncated non-commutative
power series (degree <= 2 suffices for a triple invariant). No floating
point, no anchor, no `q`.

SELF-TEST FIRST, and it is not decoration. The method is validated
against two braids whose answers are known independently before it is
applied to anything: `(sigma_1 sigma_2^-1)^3`, the Borromean rings, must
give all `lk = 0` and `mu-bar = -1`; the trivial braid, the 3-component
unlink, must give `0`. A method that cannot separate those two cannot be
trusted on the monodromy image, where there is no independent answer to
check against.

RESULT, and it did not need a search. The six local monodromies give
only TWO distinct ELEMENTS of `B_3`, and those two already generate:

    sigma_1      = g0^{-1},        g0 = sigma_1^{-1}       (loops 0, 3, 4)
    sigma_2^{-1} = g0^{-1} g1 g0,  g1 = sigma_1^{-1} sigma_2^{-1} sigma_1
                                        (loops 1, 2, 5)

CORRECTED: this said "four distinct braid words". Four distinct REDUCED
WORDS do appear, but two of them are the same element written another
way -- each coincidence needs a braid relation, which free reduction
cannot apply, so the word-level count over-counted. `same_element_classes`
now decides it with the faithful Artin representation. Two elements
generating `B_3` is a tighter result than four, not a weaker one; the
conclusion below is unchanged. Contributed by the sibling verification on
PR #6458 and re-derived here before being accepted.

so the monodromy image contains both Artin generators, is a subgroup of
`B_3` by construction, and therefore IS `B_3` -- its pure part is all of
`P_3`. The Borromean braid `(sigma_1 sigma_2^{-1})^3` is consequently an
element of the image, built here FROM the loop lifts rather than
imported for comparison, and it is Brunnian with `mu-bar_123 = -1`. The
identity is also in the image, with `mu-bar_123 = 0`. Both are pure, so
both carry sign character `+1`. The two sign lines agree as sign
characters and disagree on `mu-bar`, on this fibration: F5's
vacuous-agreement escape is CLOSED, on the very invariant the Milnor
route locates colour antisymmetry in rather than on a lower one.

The sampling route is kept and reported because it MISLEADS, which is
the more transferable finding. All six pure pairwise products of the
loop words have nonzero pairwise linking, hence indeterminacy 1, hence a
vacuous `mu-bar`; a radius-5 Cayley ball turns up 100 Brunnian pure
elements and every one gives `0`. Read alone that sample says the escape
stands. It is a fact about short words -- the Borromean braid needs 12
generator-letters -- and says nothing about the image. A negative from a
finite sample bounds the sample.

Cross-references:
  - `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §9, §10
  - `computations/probes/colour_sign_line_pure_braid_probe.py`  (F4, F5)
  - `computations/probes/bring_monodromy_braid_lift_probe.py`   (the lifts)
  - `library/0110001v3` (Mellor-Melvin) for the Magnus/longitude route
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

WITNESS_OUT = HERE / "colour-mu-bar-monodromy-probe.witness.json"
LIFT_WITNESS = HERE / "bring-monodromy-braid-lift-probe.witness.json"

N = 3  # three colour tubes


# ── Free group words ──────────────────────────────────────────────


def reduce_word(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def inv_word(w):
    return tuple(-g for g in reversed(w))


def artin_gen(i, inverse=False):
    img = {k: (k,) for k in range(1, N + 1)}
    if not inverse:
        img[i] = reduce_word((i, i + 1, -i)); img[i + 1] = (i,)
    else:
        img[i] = (i + 1,); img[i + 1] = reduce_word((-(i + 1), i, i + 1))
    return img


def apply_auto(img, w):
    out = []
    for g in w:
        piece = img[abs(g)]
        out.extend(piece if g > 0 else inv_word(piece))
    return reduce_word(out)


def braid_auto(word):
    auto = {k: (k,) for k in range(1, N + 1)}
    for g in word:
        nxt = artin_gen(abs(g), inverse=(g < 0))
        auto = {k: apply_auto(nxt, auto[k]) for k in range(1, N + 1)}
    return auto


def word_perm(word):
    p = list(range(N))
    for g in word:
        i = abs(g)
        p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


# ── Magnus expansion, truncated at degree 2 ───────────────────────
#
# A series is a dict from index-tuples to integer coefficients:
#   ()      -> constant term
#   (i,)    -> coefficient of X_i
#   (i, j)  -> coefficient of X_i X_j   (order matters: non-commutative)


def series_mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = ka + kb
            if len(k) > 2:
                continue
            out[k] = out.get(k, 0) + va * vb
    return {k: v for k, v in out.items() if v}


def magnus(word):
    """Magnus image of a free-group word: x_i -> 1 + X_i,
    x_i^{-1} -> 1 - X_i + X_i^2 (truncated at degree 2)."""
    s = {(): 1}
    for g in word:
        i = abs(g)
        f = {(): 1, (i,): 1} if g > 0 else {(): 1, (i,): -1, (i, i): 1}
        s = series_mul(s, f)
    return s


def eps1(s, i):
    return s.get((i,), 0)


def eps2(s, i, j):
    return s.get((i, j), 0)


# ── Longitudes and mu-bar ─────────────────────────────────────────


def longitudes(word):
    """For a PURE braid, return (w_1, ..., w_N) with x_i |-> w_i x_i w_i^{-1}.

    The reduced image is `w_i x_i w_i^{-1}` with `w_i` not ending in
    `x_i^{+-1}` (otherwise it would cancel), hence has odd length
    `2*len(w_i) + 1` and `w_i` is its first half.  Every extraction is
    checked by RECONSTRUCTION -- a conjugator read off by slicing is a
    guess until the slice is fed back through and reproduces the image.

    `w_i` is the i-th longitude of the closure, up to powers of `x_i`,
    which do not move any `eps_{jk}` with `j, k != i` (an `x_i^k` factor
    contributes only `X_i`), so `mu-bar_123` is unaffected by the choice.
    """
    auto = braid_auto(word)
    ws = {}
    for i in range(1, N + 1):
        u = auto[i]
        if len(u) % 2 != 1:
            raise ValueError(f"x_{i} image has even length {len(u)} — not a conjugation")
        half = (len(u) - 1) // 2
        w = u[:half]
        if reduce_word(w + (i,) + inv_word(w)) != u:
            raise ValueError(f"conjugator reconstruction failed for x_{i}")
        ws[i] = w
    return ws


def linking(ws):
    """lk(i, j) = eps_i(w_j), the degree-1 Magnus coefficient."""
    return {
        (i, j): eps1(magnus(ws[j]), i)
        for i in range(1, N + 1)
        for j in range(1, N + 1)
        if i != j
    }


def mu_bar_cyclic(ws, indeterminacy=0):
    """The three cyclically-equivalent readings of mu-bar_{123}.

    Milnor's cyclic symmetry `mu-bar(123) = mu-bar(231) = mu-bar(312)`
    holds MODULO the indeterminacy -- the gcd of the pairwise linking
    numbers -- not on the nose.  So the three readings are computed
    separately and their agreement is enforced only where the invariant
    is actually well defined (`indeterminacy == 0`, the Brunnian case);
    elsewhere the spread is data, not an error.

    This distinction was NOT in the first draft, which enforced literal
    equality always and duly aborted on the first non-Brunnian closure
    in the monodromy image (readings `[0, 0, 1]`).  Indeterminacy is the
    same subtlety `gap2_he4_borromean_mu_bar.py` handles with its
    `welldef = (g == 0)` gate; that producer was the corpus precedent
    and this now matches it.

    Returns (value, [three readings], well_defined).
    """
    trio = [
        eps2(magnus(ws[3]), 1, 2),  # mu-bar_{123}
        eps2(magnus(ws[1]), 2, 3),  # mu-bar_{231}
        eps2(magnus(ws[2]), 3, 1),  # mu-bar_{312}
    ]
    well_defined = indeterminacy == 0
    if well_defined and len(set(trio)) != 1:
        raise ValueError(
            f"cyclic symmetry violated at zero indeterminacy: readings "
            f"{trio} disagree — the Magnus machinery or the longitude "
            "extraction is wrong"
        )
    if not well_defined:
        residues = {v % indeterminacy for v in trio}
        if len(residues) != 1:
            raise ValueError(
                f"cyclic symmetry violated mod {indeterminacy}: readings "
                f"{trio} — the machinery is wrong"
            )
    return trio[0], trio, well_defined


def analyse(word):
    """Full reading of one braid word.  Returns None-free dict."""
    perm = word_perm(word)
    pure = perm == tuple(range(N))
    rec = {
        "word": list(word),
        "permutation": list(perm),
        "pure": pure,
        "exponent_sum": sum(1 if g > 0 else -1 for g in word),
    }
    if not pure:
        rec["note"] = "not pure — no longitudes, mu-bar undefined"
        return rec
    ws = longitudes(word)
    lk = linking(ws)
    rec["longitudes"] = {f"w_{i}": list(ws[i]) for i in range(1, N + 1)}
    rec["linking_numbers"] = {f"lk({i},{j})": v for (i, j), v in sorted(lk.items())}
    rec["brunnian"] = all(v == 0 for v in lk.values())
    indet = 0
    for v in lk.values():
        indet = math.gcd(indet, abs(v))
    rec["mu_bar_indeterminacy"] = indet
    val, trio, welldef = mu_bar_cyclic(ws, indet)
    rec["mu_bar_123"] = val
    rec["mu_bar_cyclic_readings"] = trio
    rec["mu_bar_well_defined"] = welldef
    return rec


# ── Self-test: two braids with independently known answers ────────

BORROMEAN = (1, -2, 1, -2, 1, -2)  # (sigma_1 sigma_2^-1)^3
TRIVIAL = ()
HOPF_PLUS_SPLIT = (1, 1)  # sigma_1^2: Hopf link + a split third component


def self_test():
    checks = []

    bor = analyse(BORROMEAN)
    checks.append(
        {
            "name": "borromean_is_pure",
            "expected": True,
            "actual": bor["pure"],
            "passed": bor["pure"] is True,
        }
    )
    checks.append(
        {
            "name": "borromean_all_linking_zero",
            "expected": True,
            "actual": bor["brunnian"],
            "passed": bor["brunnian"] is True,
        }
    )
    checks.append(
        {
            "name": "borromean_mu_bar_is_unit",
            "expected": "|mu-bar| == 1",
            "actual": bor["mu_bar_123"],
            "passed": abs(bor["mu_bar_123"]) == 1,
        }
    )

    triv = analyse(TRIVIAL)
    checks.append(
        {
            "name": "unlink_mu_bar_zero",
            "expected": 0,
            "actual": triv["mu_bar_123"],
            "passed": triv["mu_bar_123"] == 0,
        }
    )
    checks.append(
        {
            "name": "unlink_all_linking_zero",
            "expected": True,
            "actual": triv["brunnian"],
            "passed": triv["brunnian"] is True,
        }
    )

    # A NON-Brunnian control: the method must also see linking when there
    # is some, or "all lk = 0" above would be uninformative.
    hopf = analyse(HOPF_PLUS_SPLIT)
    lk12 = hopf["linking_numbers"]["lk(1,2)"]
    checks.append(
        {
            "name": "hopf_linking_detected",
            "expected": "|lk(1,2)| == 1",
            "actual": lk12,
            "passed": abs(lk12) == 1,
        }
    )

    # Cross-check against the corpus's OWN Milnor tower, which specifies
    # longitudes by hand rather than deriving them from a braid.  The
    # standard Brunnian presentation has l_i = [x_j, x_k]; if this file's
    # braid-derived longitudes are right, the two routes must agree.
    # (`computations/gap2_he4_borromean_mu_bar.py`, `mu()`; and the
    # validated tower it cites, `binding_mn_milnor_linking.py`.)
    def comm(a, b):
        return (a, b, -a, -b)

    model = {1: comm(2, 3), 2: comm(3, 1), 3: comm(1, 2)}
    model_val, _, _ = mu_bar_cyclic(model)
    checks.append(
        {
            "name": "agrees_with_corpus_commutator_model",
            "expected": f"|mu-bar| == 1 from hand-given longitudes l_i = [x_j, x_k]",
            "actual": model_val,
            "passed": abs(model_val) == 1,
        }
    )
    checks.append(
        {
            "name": "braid_route_matches_model_route",
            "expected": f"|{model_val}| == |braid-derived|",
            "actual": bor["mu_bar_123"],
            "passed": abs(model_val) == abs(bor["mu_bar_123"]),
        }
    )

    return checks, {
        "borromean": bor,
        "trivial": triv,
        "hopf_plus_split": hopf,
        "corpus_commutator_model_mu_bar": model_val,
    }


# ── The monodromy image ───────────────────────────────────────────


def load_pure_products():
    """Read the pure pairwise products found by the lift probe.

    Re-derived here from the six loop words rather than trusted from the
    sibling witness's summary: the words are the datum, the pure list is
    a conclusion, and a conclusion is what this probe is re-checking.
    """
    if not LIFT_WITNESS.exists():
        raise SystemExit(f"missing sibling witness: {LIFT_WITNESS}")
    data = json.loads(LIFT_WITNESS.read_text())
    loops = data["loops"]
    words = [tuple(l["braid_word_reduced"]) for l in loops]
    out = []
    for a, b in itertools.combinations(range(len(words)), 2):
        prod = reduce_word(words[a] + words[b])
        if word_perm(prod) == tuple(range(N)):
            out.append(((a, b), prod))
    return words, out


def same_element_classes(words):
    """Partition the loop lifts by EQUALITY IN B_3, not by reduced word.

    The Artin representation is faithful (Artin 1947), so two braids are
    equal exactly when their automorphisms of `F_3` agree. Free reduction
    is strictly weaker: it cannot apply a braid relation, so it reports
    `sigma_2 sigma_1 sigma_2^-1 sigma_1^-1 sigma_2^-1` and `sigma_1^-1`
    as different when they are the same element. That gap is what made
    the first version of this probe say "four distinct".
    """
    autos = [braid_auto(w) for w in words]
    classes = []
    for i, a in enumerate(autos):
        for c in classes:
            if autos[c[0]] == a:
                c.append(i)
                break
        else:
            classes.append([i])
    return [{"loops": c, "word": list(words[c[0]])} for c in classes]


def full_twist_relation(words):
    """Check `(ab)^3 = Delta^-2`, the B_3 lift of `(H_1 H_2)^3 = id`.

    `Delta = sigma_1 sigma_2 sigma_1` is the half twist and `Delta^2`
    generates the centre of `B_3`. The two distinct lifts `a`, `b` sit in
    angular order `ababab`, so their product around all six branch points
    is `(ab)^3` -- and it is the INVERSE FULL TWIST, not the identity.

    This is the same fact `rem:holonomy-trefoil` records as
    `(H_1 H_2)^3 = id` on SO(3): the SU(2) map kills the full twist, which
    is exactly why it is a surjection onto a proper quotient rather than
    an isomorphism. Verified here rather than cited.
    """
    cls = same_element_classes(words)
    if len(cls) != 2:
        return {"checked": False, "reason": f"{len(cls)} distinct elements, expected 2"}
    a, b = tuple(cls[0]["word"]), tuple(cls[1]["word"])
    lhs = braid_auto(reduce_word((a + b) * 3))
    delta = (1, 2, 1)
    rhs = braid_auto(reduce_word(inv_word(delta + delta)))
    return {
        "checked": True,
        "a": list(a),
        "b": list(b),
        "angular_order": [c["loops"] for c in cls],
        "identity": "(ab)^3 = Delta^-2  where Delta = sigma_1 sigma_2 sigma_1",
        "holds": lhs == rhs,
        "note": (
            "the B_3 lift of rem:holonomy-trefoil's (H_1 H_2)^3 = id; the "
            "SU(2) map kills the full twist, hence is a surjection onto a "
            "proper quotient and not an isomorphism"
        ),
    }


def prove_image_is_all_of_B3(gens):
    """Exhibit `sigma_1` and `sigma_2` as words in the six loop lifts.

    This supersedes searching. The six loops give only TWO distinct
    ELEMENTS of `B_3` -- not four, as this probe and the audit first said.
    Four distinct REDUCED WORDS appear, but two of them are the same
    element written differently: loop 4's `sigma_2 sigma_1 sigma_2^-1
    sigma_1^-1 sigma_2^-1` reduces to `sigma_1^-1` by the braid relation,
    and loop 5's `sigma_1^-1 sigma_2^-1 sigma_1` equals `sigma_2
    sigma_1^-1 sigma_2^-1`. So the lifts are

        a = sigma_1^-1                 on loops {0, 3, 4}
        b = sigma_2 sigma_1^-1 sigma_2^-1   on loops {1, 2, 5}

    and TWO elements generate all of `B_3` -- a tighter statement than
    the one this function used to make. Free reduction cannot see either
    coincidence (both need a braid relation), which is why the word-level
    count came out at four; `same_element_classes` below decides it with
    the faithful Artin representation instead. Correction contributed by
    the sibling verification on PR #6458 and re-derived here.

    Two of them already generate:

        sigma_1      = g0^{-1}                with g0 = sigma_1^{-1}
        sigma_2^{-1} = g0^{-1} g1 g0          with g1 = sigma_1^{-1} sigma_2^{-1} sigma_1

    so the image contains both Artin generators. The image is a subgroup
    of `B_3` by construction, hence the monodromy image IS `B_3`, its
    pure part IS `P_3` in full, and every question about "does the image
    contain such-and-such a braid" collapses to "does `B_3`".

    Both expressions are verified here by free reduction, not asserted.
    Returns a dict of the exhibited words; raises if either fails.
    """
    have = {tuple(g) for g in gens}
    g0, g1 = (-1,), (-1, -2, 1)
    if g0 not in have or g1 not in have:
        raise ValueError(
            f"expected loop lifts {g0} and {g1} among the image generators; "
            f"got {sorted(have)}"
        )
    s1 = inv_word(g0)
    s2_inv = reduce_word(inv_word(g0) + g1 + g0)
    if s1 != (1,):
        raise ValueError(f"g0^-1 reduced to {s1}, expected sigma_1")
    if s2_inv != (-2,):
        raise ValueError(f"g0^-1 g1 g0 reduced to {s2_inv}, expected sigma_2^-1")
    return {
        "generators_distinct_words": [list(w) for w in sorted(have)],
        "generators_distinct_elements": same_element_classes(gens),
        "sigma_1_as": {"word_in_gens": "g0^{-1}", "reduces_to": list(s1)},
        "sigma_2_inv_as": {
            "word_in_gens": "g0^{-1} g1 g0",
            "reduces_to": list(s2_inv),
        },
        "conclusion": (
            "the monodromy image contains both Artin generators of B_3 and "
            "is a subgroup of B_3, hence equals B_3; its pure part is all "
            "of P_3"
        ),
    }


def borromean_in_image(gens):
    """Build the Borromean braid FROM the loop lifts and measure it.

    With `sigma_1` and `sigma_2^{-1}` exhibited above, `(sigma_1
    sigma_2^{-1})^3` is a word in the loop lifts -- a genuine element of
    the monodromy image, not an outside example imported for comparison.
    """
    g0, g1 = (-1,), (-1, -2, 1)
    s1, s2_inv = inv_word(g0), reduce_word(inv_word(g0) + g1 + g0)
    w = reduce_word((s1 + s2_inv) * 3)
    if w != BORROMEAN:
        raise ValueError(f"built {w}, expected the Borromean braid {BORROMEAN}")
    rec = analyse(w)
    rec["built_from_loop_lifts"] = "(g0^{-1} . g0^{-1} g1 g0)^3"
    return rec


def search_image_for_brunnian(gens, max_len):
    """BFS the subgroup generated by the six loop words for a BRUNNIAN
    pure element -- one whose closure has every pairwise linking number
    zero, which is exactly the condition making `mu-bar_123` a genuine
    integer rather than an element of Z/gcd.

    The pairwise products are only a 15-element sample of the image; if
    none of them is Brunnian that bounds the sample, not the image. This
    walks the Cayley ball instead, on the generators AND their inverses,
    deduplicating by reduced word.

    Scope stays (a) whatever the answer: a ball of radius `max_len` is
    still a finite piece of an infinite group. A hit is a proof; a miss
    bounds only the ball, and the returned count says how big it was.
    """
    alphabet = [g for w in gens for g in (w, inv_word(w))]
    seen = {(): None}
    frontier = [()]
    hits = []
    for _ in range(max_len):
        nxt = []
        for w in frontier:
            for a in alphabet:
                cand = reduce_word(w + a)
                if cand in seen:
                    continue
                seen[cand] = None
                nxt.append(cand)
                if not cand or word_perm(cand) != tuple(range(N)):
                    continue
                rec = analyse(cand)
                if rec["brunnian"]:
                    hits.append(rec)
        frontier = nxt
        if not frontier:
            break
    return hits, len(seen)


def main():
    checks, examples = self_test()
    failed = [c for c in checks if not c["passed"]]
    if failed:
        print("SELF-TEST FAILED — not applying the method:")
        for c in failed:
            print(f"  {c['name']}: expected {c['expected']}, got {c['actual']}")
        raise SystemExit(1)
    print(f"self-test: {len(checks)}/{len(checks)} passed")
    print(f"  borromean mu-bar_123 = {examples['borromean']['mu_bar_123']}")

    loop_words, pure = load_pure_products()
    print(f"\nsix monodromy loop words: {[list(w) for w in loop_words]}")
    print(f"pure pairwise products: {len(pure)} of 15")

    records = []
    for (a, b), w in pure:
        rec = analyse(w)
        rec["pair"] = [a, b]
        records.append(rec)
        print(
            f"  loops {a},{b}: len {len(w):2d}  "
            f"brunnian={str(rec['brunnian']):5s} "
            f"indet={rec['mu_bar_indeterminacy']}  "
            f"mu-bar_123={rec['mu_bar_123']:+d} "
            f"({'well-defined' if rec['mu_bar_well_defined'] else 'mod ' + str(rec['mu_bar_indeterminacy'])})"
        )

    # A nonzero reading only counts when the invariant is WELL DEFINED:
    # at nonzero indeterminacy `mu-bar` lives in Z/gcd and a nonzero
    # representative asserts nothing.
    nonzero = [
        r for r in records if r["mu_bar_123"] != 0 and r["mu_bar_well_defined"]
    ]
    linked = [r for r in records if not r["brunnian"]]

    proof = prove_image_is_all_of_B3(loop_words)
    twist = full_twist_relation(loop_words)
    proof["full_twist_relation"] = twist
    print("\nimage generation:")
    print(f"  distinct reduced WORDS:    {proof['generators_distinct_words']}")
    print("  distinct ELEMENTS of B_3:  "
          f"{[(c['loops'], c['word']) for c in proof['generators_distinct_elements']]}")
    print(f"  sigma_1      = {proof['sigma_1_as']['word_in_gens']}"
          f"  ->  {proof['sigma_1_as']['reduces_to']}")
    print(f"  sigma_2^{{-1}} = {proof['sigma_2_inv_as']['word_in_gens']}"
          f"  ->  {proof['sigma_2_inv_as']['reduces_to']}")
    print(f"  => {proof['conclusion']}")
    if twist["checked"]:
        print(f"  {twist['identity']}:  {twist['holds']}")
        print(f"     (the B_3 lift of rem:holonomy-trefoil's (H_1H_2)^3 = id)")

    bor = borromean_in_image(loop_words)
    print(f"\n  {bor['built_from_loop_lifts']} = {bor['word']}")
    print(f"    brunnian={bor['brunnian']}  indeterminacy="
          f"{bor['mu_bar_indeterminacy']}  mu-bar_123={bor['mu_bar_123']:+d}"
          f"  (well-defined={bor['mu_bar_well_defined']})")

    ball_radius = int(os.environ.get("QOU_MU_BALL", "5"))
    print(f"\ncorroborating Cayley-ball scan (radius {ball_radius}) — "
          "not the proof, just a check that the short words behave:")
    hits, ball_size = search_image_for_brunnian(loop_words, ball_radius)
    hit_nonzero = [h for h in hits if h["mu_bar_123"] != 0]
    print(f"  {ball_size} distinct reduced words visited; {len(hits)} "
          f"Brunnian pure, {len(hit_nonzero)} of them with mu-bar != 0")
    print("  (the Borromean braid needs 12 generator-letters, so a "
          f"radius-{ball_radius} ball cannot contain it — a miss here "
          "bounds the ball, not the image)")

    verdict = (
        "CLOSED, and by the Milnor invariant itself. The six local "
        "monodromies give only TWO distinct ELEMENTS of B_3, and those "
        "two generate: sigma_1 = g0^-1 and sigma_2^-1 = "
        "g0^-1 g1 g0. So the monodromy image is not a proper subgroup "
        "of B_3 — it IS B_3, and its pure part is all of P_3. The "
        "Borromean braid (sigma_1 sigma_2^-1)^3 is therefore an element "
        f"of the image; built from the loop lifts it has every pairwise "
        f"linking number zero (indeterminacy {bor['mu_bar_indeterminacy']}, "
        f"so mu-bar is a genuine integer) and mu-bar_123 = "
        f"{bor['mu_bar_123']:+d}, against 0 for the identity, which is "
        "also in the image. Both are pure, so both carry sign character "
        "+1. The two colour sign lines agree as sign characters and "
        "disagree on mu-bar, ON THIS FIBRATION — the vacuous-agreement "
        "escape of F5 is closed on the very invariant the Milnor route "
        "locates colour antisymmetry in, not merely on a lower one."
    )
    print(f"\n{verdict}")

    aside = (
        "Aside, and it is the reason the search was abandoned for a "
        f"proof: all {len(records)} pure PAIRWISE products have "
        "indeterminacy 1, so mu-bar is vacuous on every one of them, and "
        f"the radius-{ball_radius} ball's {len(hits)} Brunnian elements "
        "all give 0. Read alone, that sample says the escape stands. It "
        "is a fact about short words, not about the image."
    )
    print(f"\n{aside}")

    witness = {
        "schema": "qou-probe/v1",
        "probe": "colour_mu_bar_monodromy_probe",
        "bean": "qou-dg07",
        "question": (
            "Does the Bring monodromy image contain a pure braid whose "
            "closure has a nonzero Milnor mu-bar_123, i.e. does this "
            "fibration REALISE the sign-line separation proved on B_3?"
        ),
        "method": (
            "Artin representation B_3 -> Aut(F_3); for a pure braid the "
            "image is x_i |-> w_i x_i w_i^{-1}; w_i is the i-th longitude "
            "of the closure; Milnor's invariants are its Magnus "
            "coefficients. Exact integer arithmetic on non-commutative "
            "power series truncated at degree 2. No floating point."
        ),
        "self_test": checks,
        "self_test_examples": examples,
        "monodromy_loop_words": [list(w) for w in loop_words],
        "pure_products": records,
        "image_generation_proof": proof,
        "borromean_in_image": bor,
        "cayley_ball_scan": {
            "radius": ball_radius,
            "distinct_reduced_words": ball_size,
            "brunnian_pure_elements_found": len(hits),
            "of_those_with_nonzero_mu_bar": len(hit_nonzero),
            "note": (
                "corroboration only; the Borromean braid needs 12 "
                "generator-letters so this ball cannot reach it. A miss "
                "bounds the ball, not the image."
            ),
        },
        "aside_short_words_mislead": aside,
        "counts": {
            "pure_products": len(records),
            "mu_bar_nonzero_and_well_defined": len(nonzero),
            "non_brunnian": len(linked),
            "brunnian_in_ball": len(hits),
            "brunnian_in_ball_with_nonzero_mu_bar": len(hit_nonzero),
        },
        "verdict": verdict,
        "scope_note": (
            "The verdict is now a PROOF of group membership plus an exact "
            "integer computation, not a sample, so it is not scope-(a): "
            "the image equals B_3 by exhibiting both Artin generators as "
            "words in the loop lifts, and mu-bar_123 = -1 on an element "
            "of it. What remains conditional is the INPUT — the six loop "
            "words come from bring_monodromy_braid_lift_probe's numerical "
            "continuation, guarded but numerical. If those words are "
            "right, this conclusion is exact."
        ),
        "superseded_scope": (
            "Scope-(a) either way: this reads the six local monodromies "
            "lifted by bring_monodromy_braid_lift_probe and their pairwise "
            "products, not the whole image group. A zero here bounds what "
            "these words show, and excludes nothing about the image."
        ),
    }
    from witness_base import WitnessBuilder  # noqa: E402

    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python"
    )
    witness["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {WITNESS_OUT.name}")


if __name__ == "__main__":
    main()
