#!/usr/bin/env python3
"""hecke_gs_confluence_n4 — is the Bokut–Shiao-completed Hecke rewriting system
confluent at n = 4?

`UGB.GrobnerShirshov.HeckeGS` refutes `hecke_is_gs_basis` for the *uncompleted*
system: one overlap (Yang–Baxter for `(σ₂,σ₃)` against far-commutation for
`(σ₃,σ₁)`) has an S-polynomial that is irreducible and non-zero.
`UGB.GrobnerShirshov.HeckeCompletion` adds the Bokut–Shiao family and shows that
*that* overlap now resolves — but resolving one composition is necessary, not
sufficient. The Lean side has since enumerated the obligation set (58 overlap
shapes at n = 4, of which 13 are degenerate) without discharging most of it.

This script discharges the whole set **computationally**, exactly, so the Lean
work has a target it is known to be able to reach. It is a witness, not a proof:
it says the theorem is true at n = 4 and gives the reduction chain for every
composition, which is the blueprint each Lean proof has to reproduce.

## Faithfulness to the Lean definitions

Every object here mirrors a Lean declaration, and the correspondence is the
thing to check if this witness is ever doubted:

    heckeRelation i hp         σᵢσᵢ − h·σᵢ − 1                lm [i,i]     lc  1
    yangBaxterRelation i' i    σᵢ'σᵢσᵢ' − σᵢσᵢ'σᵢ             lm [i,i',i]  lc −1
    farCommRelation i j        σᵢσⱼ − σⱼσᵢ        (j+1 < i)   lm [i,j]     lc  1
    bokutShiaoRelation i' i j  bsWord₁ i j − bsWord₂ i' i j   lm bsWord₁   lc  1

    descWord i j  = σᵢ σᵢ₋₁ ⋯ σⱼ
    bsWord₁ i j   = descWord i j ++ [σᵢ]
    bsWord₂ i' i j = [σᵢ', σᵢ] ++ descWord i' j

    OverlapComposition.spoly    lc₂ • (rule₁ · right) − lc₁ • (left · rule₂)
    InclusionComposition.spoly  lc(inner) • outer − lc(outer) • (left · inner · right)

`h` is `q − q⁻¹` (§7a convention), carried as a free symbol: nothing here needs
a numeric `q`, and no float is ever formed. Coefficients live in ℤ[h] and are
serialised as sympy strings.

## Method

`isNormalForm` in the Lean framework asks that **no** monomial of an element
have any rule's leading monomial as an infix — not merely the leading one — and
`SingleStepReduction` may target any such monomial. So reduction here rewrites
the deg-lex-largest reducible monomial first and stops when no monomial of the
element contains any leading monomial. Termination is the usual deg-lex
argument: the quadratic rule drops degree, the other three preserve degree and
drop lex.

Emits `hecke-gs-confluence-n4.witness.json`. Bean qou-auq3.
"""

from __future__ import annotations

import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

N = 4
h = sp.Symbol("h")


# --------------------------------------------------------------------------
# words
# --------------------------------------------------------------------------

def desc_word(i: int, j: int) -> tuple:
    """`descWord i j` = σᵢ σᵢ₋₁ ⋯ σⱼ; empty when i < j."""
    return tuple(k for k in range(N) if j <= k <= i)[::-1]


def bs_word_1(i: int, j: int) -> tuple:
    return desc_word(i, j) + (i,)


def bs_word_2(ip: int, i: int, j: int) -> tuple:
    return (ip, i) + desc_word(ip, j)


# --------------------------------------------------------------------------
# the completed rewriting system
# --------------------------------------------------------------------------

def build_rules() -> list:
    """The 16 rules of `heckeCompletedRewritingSystem 4`, in the Lean order:
    quadratic, Yang–Baxter, far-commutation, then the Bokut–Shiao block."""
    rules = []
    for i in range(N):
        rules.append((f"Q{i}",
                      {(i, i): sp.Integer(1), (i,): -h, (): sp.Integer(-1)},
                      (i, i)))
    for ip in range(N):
        i = ip + 1
        if i < N:
            rules.append((f"Y{ip}{i}",
                          {(ip, i, ip): sp.Integer(1), (i, ip, i): sp.Integer(-1)},
                          (i, ip, i)))
    for i in range(N):
        for j in range(N):
            if j + 1 < i:
                rules.append((f"F{i}{j}",
                              {(i, j): sp.Integer(1), (j, i): sp.Integer(-1)},
                              (i, j)))
    for ip in range(N):
        i = ip + 1
        if i >= N:
            continue
        for j in range(N):
            if j <= ip:
                rules.append((f"B{ip}{i}{j}",
                              {bs_word_1(i, j): sp.Integer(1),
                               bs_word_2(ip, i, j): sp.Integer(-1)},
                              bs_word_1(i, j)))
    return rules


RULES = build_rules()
LM = {name: lm for name, _, lm in RULES}
REL = {name: rel for name, rel, _ in RULES}
LC = {name: REL[name][LM[name]] for name in LM}


# --------------------------------------------------------------------------
# free-algebra arithmetic
# --------------------------------------------------------------------------

def clean(d: dict) -> dict:
    out = {}
    for w, c in d.items():
        c = sp.expand(c)
        if c != 0:
            out[w] = c
    return out


def context_mul(a: tuple, rel: dict, b: tuple) -> dict:
    """`AlgElement.contextMul a rel b`."""
    return {tuple(a) + w + tuple(b): c for w, c in rel.items()}


def combine(d1: dict, d2: dict, scale) -> dict:
    """`d1 + scale · d2`."""
    out = defaultdict(lambda: sp.Integer(0))
    for w, c in d1.items():
        out[w] += c
    for w, c in d2.items():
        out[w] += scale * c
    return clean(out)


def infix_positions(word: tuple, sub: tuple) -> list:
    L = len(sub)
    return [k for k in range(len(word) - L + 1) if word[k:k + L] == sub]


def deglex_key(w: tuple):
    """Deg-lex, largest first: longer wins, then lexicographically larger."""
    return (-len(w), tuple(-x for x in w))


def reduce_to_normal_form(f: dict, max_steps: int = 2000):
    """Rewrite until no monomial contains any rule's leading monomial.

    Returns `(normal_form, chain)` where each chain entry is
    `(target_monomial, rule_name, left_context, right_context, coefficient)`.
    """
    chain = []
    for _ in range(max_steps):
        target = None
        for w in sorted(f.keys(), key=deglex_key):
            for name in LM:
                positions = infix_positions(w, LM[name])
                if positions:
                    target = (w, name, positions[0])
                    break
            if target:
                break
        if target is None:
            return f, chain
        w, name, k = target
        left, right = w[:k], w[k + len(LM[name]):]
        coeff = sp.expand(f[w] / LC[name])
        f = combine(f, context_mul(left, REL[name], right), -coeff)
        chain.append((w, name, left, right, coeff))
    raise RuntimeError(f"no normal form after {max_steps} steps")


# --------------------------------------------------------------------------
# the obligation set
# --------------------------------------------------------------------------

def leading_monomial_set() -> list:
    """`completedLMSet 4` as a set (order irrelevant here)."""
    words = []
    for _, _, lm in RULES:
        if lm not in words:
            words.append(lm)
    return words


def overlap_shapes(words: list) -> list:
    """`overlapTriples 4`: (left, overlap, right) with left++overlap and
    overlap++right leading monomials and overlap non-empty."""
    shapes = []
    for a in words:
        for b in words:
            for s in range(len(a)):
                o = a[s:]
                if b[:len(o)] == o:
                    shapes.append((a[:s], o, b[len(o):]))
    return shapes


def run() -> dict:
    words = leading_monomial_set()
    by_word = defaultdict(list)
    for name, _, lm in RULES:
        by_word[lm].append(name)

    shapes = overlap_shapes(words)
    degenerate = [t for t in shapes if not t[0] and not t[2]]
    proper = [t for t in shapes if t[0] and t[2]]

    overlap_results = []
    for left, o, right in shapes:
        a, b = left + o, o + right
        for n1 in by_word[a]:
            for n2 in by_word[b]:
                s = combine(
                    {w: LC[n2] * c for w, c in context_mul((), REL[n1], right).items()},
                    {w: LC[n1] * c for w, c in context_mul(left, REL[n2], ()).items()},
                    -1,
                )
                nf, chain = reduce_to_normal_form(dict(s))
                overlap_results.append({
                    "rule1": n1, "rule2": n2,
                    "left": list(left), "overlap": list(o), "right": list(right),
                    "degenerate": not left and not right,
                    "spoly_identically_zero": not s,
                    "steps": len(chain),
                    "reduces_to_zero": not nf,
                    "residue": {"".join(map(str, w)): str(c) for w, c in nf.items()},
                })

    inclusion_results = []
    for n_out, rel_out, lm_out in RULES:
        for n_in, rel_in, lm_in in RULES:
            for k in range(len(lm_out) - len(lm_in) + 1):
                if lm_out[k:k + len(lm_in)] != lm_in:
                    continue
                left, right = lm_out[:k], lm_out[k + len(lm_in):]
                s = combine(
                    {w: LC[n_in] * c for w, c in rel_out.items()},
                    {w: LC[n_out] * c
                     for w, c in context_mul(left, rel_in, right).items()},
                    -1,
                )
                nf, chain = reduce_to_normal_form(dict(s))
                inclusion_results.append({
                    "inner": n_in, "outer": n_out,
                    "left": list(left), "right": list(right),
                    "spoly_identically_zero": not s,
                    "steps": len(chain),
                    "reduces_to_zero": not nf,
                    "residue": {"".join(map(str, w)): str(c) for w, c in nf.items()},
                })

    return {
        "words": words,
        "shapes": shapes,
        "degenerate": degenerate,
        "proper": proper,
        "overlap": overlap_results,
        "inclusion": inclusion_results,
    }


def main() -> int:
    started = time.monotonic()
    r = run()

    overlap, inclusion = r["overlap"], r["inclusion"]
    bad_overlap = [x for x in overlap if not x["reduces_to_zero"]]
    bad_inclusion = [x for x in inclusion if not x["reduces_to_zero"]]

    proper_overlap = [x for x in overlap if not x["degenerate"]]
    chain_hist = Counter(x["steps"] for x in proper_overlap)

    w = WitnessBuilder("hecke-gs-confluence-n4", engine="sympy",
                       start_time=started)
    w.set_description(
        "Every overlap and inclusion composition of the Bokut-Shiao-completed "
        "Hecke rewriting system at n = 4 has an S-polynomial that reduces to "
        "zero. Exact over Z[h], h = q - q^-1; no float is formed."
    )

    w.add_parameter("n", N)
    w.add_parameter("rules", len(RULES))
    w.add_parameter("deformation_symbol", "h = q - q^{-1}")
    w.add_parameter("lean_module", "UGB.GrobnerShirshov.HeckeCompletion")

    w.add_assertion("overlap_compositions_failing_to_reduce",
                    computed=str(len(bad_overlap)), expected="0")
    w.add_assertion("inclusion_compositions_failing_to_reduce",
                    computed=str(len(bad_inclusion)), expected="0")
    w.add_assertion("distinct_leading_monomials",
                    computed=str(len(r["words"])), expected="13")
    w.add_assertion("overlap_shapes",
                    computed=str(len(r["shapes"])), expected="58")
    w.add_assertion("degenerate_shapes",
                    computed=str(len(r["degenerate"])), expected="13")
    w.add_assertion("proper_shapes",
                    computed=str(len(r["proper"])), expected="45")

    w.add_data("overlap_compositions", len(overlap))
    w.add_data("inclusion_compositions", len(inclusion))
    w.add_data("overlap_spoly_identically_zero",
               sum(1 for x in overlap if x["spoly_identically_zero"]))
    w.add_data("inclusion_spoly_identically_zero",
               sum(1 for x in inclusion if x["spoly_identically_zero"]))
    w.add_data("proper_overlap_total_steps",
               sum(x["steps"] for x in proper_overlap))
    w.add_data("proper_overlap_max_chain",
               max((x["steps"] for x in proper_overlap), default=0))
    w.add_data("proper_overlap_chain_histogram",
               {str(k): v for k, v in sorted(chain_hist.items())})
    w.add_data("leading_monomials",
               ["".join(map(str, x)) for x in r["words"]])
    w.add_data("compositions", {"overlap": overlap, "inclusion": inclusion})

    w.add_caveat(
        "Computational witness, not a proof. It establishes that the "
        "Lean obligation set at n = 4 is discharge-able and supplies the "
        "reduction chain each Lean proof must reproduce; it does not "
        "discharge it."
    )
    w.add_caveat(
        "n = 4 only. Bokut & Shiao's theorem is for all n, and nothing here "
        "bears on n > 4."
    )
    w.add_caveat(
        "Faithfulness to the Lean definitions is checked by inspection "
        "against the table in this script's docstring, not mechanically."
    )

    path = w.save()

    print(f"rules                          : {len(RULES)}")
    print(f"distinct leading monomials     : {len(r['words'])}")
    print(f"overlap shapes                 : {len(r['shapes'])} "
          f"({len(r['degenerate'])} degenerate, {len(r['proper'])} proper)")
    print(f"overlap compositions           : {len(overlap)}  "
          f"failing: {len(bad_overlap)}")
    print(f"inclusion compositions         : {len(inclusion)}  "
          f"failing: {len(bad_inclusion)}")
    print(f"proper-overlap reduction steps : "
          f"{sum(x['steps'] for x in proper_overlap)} "
          f"(max chain {max((x['steps'] for x in proper_overlap), default=0)})")
    print(f"witness -> {path}")
    return 0 if not (bad_overlap or bad_inclusion) else 1


if __name__ == "__main__":
    raise SystemExit(main())
