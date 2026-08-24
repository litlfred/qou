"""The one composition `IsGrobnerShirshovBasis` for the Hecke system still rests on.

The Lean assembly (bean `qou-auq3`, §4bn of `HeckeCompletion.lean`) reduces
`IsGrobnerShirshovBasis` for `heckeCompletedRewritingSystem` to a single
hypothesis `hdeep`: the longest Bokut-Shiao word `bsWord1(i, 0)` overlapping
**itself** in its shared trailing `sigma_i`.  Its S-polynomial is the difference
of two monomials of length `2i + 3` (the two `lm`-length terms cancel):

    A = left * bsWord2      with  left  = descWord(i, 0)
    B = bsWord2 * right           right = descWord(i-1, 0) ++ [sigma_i]
                                  bsWord2 = sigma_{i-1} sigma_i descWord(i-1, 0)

This reduces both under the completed rewriting system and reports whether they
meet.  It is a **probe, not a proof**: it settles small `i` only, and says
nothing about general `i`.  What it buys is the target -- an induction has to
land on the normal form printed here, and now does not have to guess it.

Rules, read off the Lean definitions (`HeckeGS.lean`, `HeckeCompletion.lean`)
rather than off prose, with `H = q - 1/q`:

| rule | leading monomial | rewrites to |
|---|---|---|
| `heckeRelation x`        | `sigma_x sigma_x`             | `H sigma_x + 1` |
| `yangBaxterRelation i' i`| `sigma_i sigma_i' sigma_i`    | `sigma_i' sigma_i sigma_i'` |
| `farCommRelation i j`    | `sigma_i sigma_j`, `j+1 < i`  | `sigma_j sigma_i` |
| `bokutShiaoRelation i' i j` | `bsWord1(i, j)`            | `bsWord2(i', i, j)` |

Each leading monomial is the deg-lex maximum of its relation's support, so the
Yang-Baxter rule's `lc` is `-1` (`DegenerateYbBs.yangBaxter_lc`) and the rewrite
still sends `wHi` to `wLo`; the other three have `lc = 1`.

Arithmetic is exact and symbolic in `q` throughout (sympy).  No float appears
anywhere, per AGENTS.md "PROBES ARE NOT EXEMPT".

Emits no witness: it establishes no value the corpus consumes, only a target
for a Lean induction.
"""

import sys

import sympy as sp

q = sp.Symbol('q', positive=True)
H = q - 1 / q


def descWord(i: int, j: int) -> tuple:
    """`sigma_i sigma_{i-1} ... sigma_j`."""
    return tuple(range(i, j - 1, -1))


def bsWord1(i: int, j: int) -> tuple:
    return descWord(i, j) + (i,)


def bsWord2(i: int, j: int) -> tuple:
    """`sigma_{i-1} sigma_i descWord(i-1, j)`."""
    return (i - 1, i) + descWord(i - 1, j)


def rules(n: int) -> list:
    """Every rule of `heckeCompletedRewritingSystem n`, as (lm, replacement)."""
    out = []
    for x in range(n):
        out.append(((x, x), {(x,): H, (): sp.Integer(1)}))
    for ip in range(n - 1):
        out.append(((ip + 1, ip, ip + 1), {(ip, ip + 1, ip): sp.Integer(1)}))
    for i in range(n):
        for j in range(n):
            if j + 1 < i:
                out.append(((i, j), {(j, i): sp.Integer(1)}))
    for ip in range(n - 1):
        i = ip + 1
        for j in range(ip + 1):
            out.append((bsWord1(i, j), {bsWord2(i, j): sp.Integer(1)}))
    return out


def _find(word: tuple, lm: tuple):
    for k in range(len(word) - len(lm) + 1):
        if word[k:k + len(lm)] == lm:
            return k
    return None


def reduce_elt(elt: dict, rs: list, cap: int = 200000):
    """Rewrite `elt` (word -> coefficient) until no rule applies."""
    elt = dict(elt)
    steps = 0
    while True:
        target = None
        for w in elt:
            if sp.simplify(elt[w]) == 0:
                continue
            for lm, rep in rs:
                k = _find(w, lm)
                if k is not None:
                    target = (w, lm, rep, k)
                    break
            if target:
                break
        if target is None:
            return ({w: sp.cancel(c) for w, c in elt.items()
                     if sp.simplify(c) != 0}, steps)
        w, lm, rep, k = target
        c = elt.pop(w)
        pre, post = w[:k], w[k + len(lm):]
        for rw, rc in rep.items():
            nw = pre + rw + post
            elt[nw] = sp.cancel(elt.get(nw, 0) + c * rc)
        steps += 1
        if steps > cap:
            raise RuntimeError(f"no termination within {cap} steps")


def _classify(lm: tuple) -> tuple:
    """(family, index) of a rule, from the shape of its leading monomial."""
    if len(lm) == 2 and lm[0] == lm[1]:
        return "QUAD", lm[0]
    if len(lm) == 3 and lm[0] == lm[2]:
        return "YB", lm[0]
    if len(lm) == 2:
        return "FC", lm[0]
    return "BS", lm[0]


def census(word: tuple, rs: list) -> tuple:
    """Which rule families fire, reducing `word`.  Returns (counts, quad indices)."""
    elt = {word: sp.Integer(1)}
    counts = {}
    quads = []
    while True:
        target = None
        for w in elt:
            if sp.simplify(elt[w]) == 0:
                continue
            for lm, rep in rs:
                k = _find(w, lm)
                if k is not None:
                    target = (w, lm, rep, k)
                    break
            if target:
                break
        if target is None:
            return counts, quads
        w, lm, rep, k = target
        c = elt.pop(w)
        family, idx = _classify(lm)
        counts[family] = counts.get(family, 0) + 1
        if family == "QUAD":
            quads.append(idx)
        pre, post = w[:k], w[k + len(lm):]
        for rw, rc in rep.items():
            nw = pre + rw + post
            elt[nw] = sp.cancel(elt.get(nw, 0) + c * rc)


def deep_spoly(i: int):
    """The two monomials of the deep self-overlap's S-polynomial."""
    return (descWord(i, 0) + bsWord2(i, 0),
            bsWord2(i, 0) + descWord(i - 1, 0) + (i,))


def predicted_nf(i: int) -> dict:
    """The closed form the reductions land on, for `i >= 2`."""
    head = bsWord2(i - 1, 0)
    return {head + descWord(i, 1): sp.Integer(1),
            head + descWord(i, 0): H}


def _agree(x: dict, y: dict) -> bool:
    return all(sp.simplify(x.get(w, 0) - y.get(w, 0)) == 0
               for w in set(x) | set(y))


def main() -> int:
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    ok = True
    for i in range(1, top + 1):
        n = i + 1
        a, b = deep_spoly(i)
        rs = rules(n)
        nf_a, steps_a = reduce_elt({a: sp.Integer(1)}, rs)
        nf_b, steps_b = reduce_elt({b: sp.Integer(1)}, rs)

        # The S-polynomial resolves iff the two sides meet.
        assert _agree(nf_a, nf_b), f"i={i}: the deep self-overlap does NOT resolve"

        # Reducing under the reversed rule order must find the same normal form.
        # Not a confluence proof, but it would catch a strategy-dependent answer.
        nf_rev, _ = reduce_elt({a: sp.Integer(1)}, list(reversed(rs)))
        assert _agree(nf_a, nf_rev), f"i={i}: normal form depends on rule order"

        note = ""
        if i >= 2:
            assert _agree(nf_a, predicted_nf(i)), f"i={i}: closed form is wrong"
            # Measured, and checked rather than merely stated: under THIS
            # strategy (first applicable rule, first matching word) the left
            # side takes i(i+5)/2 steps and the right side one more.  The count
            # is strategy-dependent and is not a claim about the algebra -- it
            # is a size estimate for the chain a Lean induction has to write.
            assert steps_a == i * (i + 5) // 2, f"i={i}: step count {steps_a}"
            assert steps_b == steps_a + 1, f"i={i}: step counts {steps_a},{steps_b}"
            note = "  [matches closed form, i(i+5)/2 steps]"
        print(f"i={i} (n={n}): A resolves in {steps_a} steps, "
              f"B in {steps_b}; they agree{note}")
        for w, c in sorted(nf_a.items()):
            print(f"      {sp.factor(sp.cancel(c))!s:>26}  *  {w}")

    print()
    print("The deep self-overlap RESOLVES for every i tested. For i >= 2 both")
    print("sides land on the same TWO-term normal form")
    print("    bsWord2(i-1, 0) * descWord(i, 1)  +  H * bsWord2(i-1, 0) * descWord(i, 0)")
    print("(the second word is the first with a trailing sigma_0, since")
    print("descWord(i, 1) ++ [sigma_0] = descWord(i, 0)).  i = 1 is degenerate:")
    print("descWord(i-1, ...) collapses and the normal form has four terms.")
    print()
    print("=== which rules fire ===")
    print(f"{'i':>2} {'side':<4} {'QUAD':>4} {'YB':>3} {'FC':>3} {'BS':>3}  quad indices")
    for i in range(1, top + 1):
        rs = rules(i + 1)
        for label, w in zip(("A", "B"), deep_spoly(i)):
            c, qs = census(w, rs)
            nq, nyb = c.get("QUAD", 0), c.get("YB", 0)
            nfc, nbs = c.get("FC", 0), c.get("BS", 0)
            if i == 1:
                # Degenerate: three quadratic steps, hence the H^2 coefficient
                # and the four-term normal form.
                assert (nq, qs) == (3, [0, 1, 0]), f"i=1 {label}: {nq}, {qs}"
            else:
                # THE structural fact, and the robust one: exactly one
                # coefficient-producing step, always on sigma_0.  It is pinned
                # by the two-term normal form rather than by the strategy --
                # each quadratic step splits a term, and nothing cancels.
                assert nq == 1, f"i={i} {label}: {nq} quadratic steps, expected 1"
                assert qs == [0], f"i={i} {label}: quadratic on {qs}, expected [0]"
                # Measured, not argued.  "Two-term normal form implies one
                # split" is only an argument -- a second split whose branch
                # died would look the same -- so check the count directly
                # under the reversed rule order too.
                c_rev, qs_rev = census(w, list(reversed(rs)))
                assert c_rev.get("QUAD", 0) == 1 and qs_rev == [0], \
                    f"i={i} {label}: reversed order gives {c_rev.get('QUAD',0)} quad {qs_rev}"
            if i >= 3:
                # Strategy-dependent bookkeeping, like the step count: recorded
                # so a change in the rule set shows up, not claimed as algebra.
                assert nyb == 1, f"i={i} {label}: {nyb} Yang-Baxter steps"
                assert nbs == (i if label == "A" else i + 2), f"i={i} {label}: {nbs} BS"
                assert nfc == (i + 4) * (i - 1) // 2 - (0 if label == "A" else 1), \
                    f"i={i} {label}: {nfc} far-commutation steps"
            print(f"{i:>2} {label:<4} {nq:>4} {nyb:>3} {nfc:>3} {nbs:>3}  {qs}")

    print()
    print("For i >= 2 EXACTLY ONE quadratic step fires, always on sigma_0.  It is")
    print("the only coefficient-producing rule, which is why the normal form has")
    print("two terms: the split's `1` branch drops two letters and its `H sigma_0`")
    print("branch drops one, so the two words differ by a trailing sigma_0.  Every")
    print("other step is a length-preserving monomial rewrite.  So the coefficient")
    print("bookkeeping in a Lean proof is one split; the rest is word combinatorics.")
    print("The quadratic count is measured under the reversed rule order too, so")
    print("it is not an artefact of the strategy (the YB/FC/BS split is).")
    print("i = 1 is degenerate: three quadratic steps, hence H^2 and four terms.")
    print()
    print("Step counts are i(i+5)/2 and one more, checked for every i >= 2 tested.")
    print("That is strategy-dependent -- a size estimate for the chain, not a")
    print("fact about the algebra.")
    print()
    print("NOT established: that this holds for all i.  This is a probe; the")
    print("Lean hypothesis `hdeep` remains open, now with a known target.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
