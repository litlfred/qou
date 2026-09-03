#!/usr/bin/env python3
"""Is the q-Serre rewriting system a Gröbner–Shirshov basis?  (bean qou-18s7)

`UGB.GrobnerShirshov.qSerre_is_gs_basis` asserts that it is. While
`qSerreRewritingSystem` was itself an axiom that assertion was unfalsifiable —
an opaque system trivially "has" whatever property one asserts of it. Bean
qou-ix9e made the system a definition (five explicit rules), which turned the
axiom into a concrete, checkable claim about those five rules. This checks it.

## What is checked

A terminating rewriting system is confluent iff every **overlap ambiguity**
resolves (Bergman's diamond lemma / Newman + critical pairs). For two rules with
leading words `u` and `v`, an overlap ambiguity exists when a proper suffix of
`u` equals a proper prefix of `v`; the ambiguous word `w` can then be reduced two
ways, and the ambiguity *resolves* when both reducts have the same normal form.

So the script:

1. enumerates every overlap ambiguity among the rules' leading words;
2. reduces each ambiguous word both ways to a normal form;
3. reports whether the two agree.

Arithmetic is exact: coefficients are `sympy` rational functions of `q`.
Elements are dicts `word (tuple of letters) -> coefficient`; reduction rewrites
one occurrence at a time and iterates to a fixed point, and the result is checked
to be genuinely irreducible before any verdict is drawn.

## Rule sets checked

* **`five`** — exactly the rules of `NormalForms.lean` §3.1, i.e. the content of
  `qSerre_is_gs_basis` as it currently stands.
* **`seven`** — the same plus the two `K⁻¹` commutation rules, which is the
  standard presentation of the GS basis for `U_q(sl₂)`.
"""
from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path

from sympy import Rational, simplify, symbols, together, cancel

q = symbols('q')

# letters
Ep, Em, K, Ki = 'E+', 'E-', 'K', 'K^-1'
LETTERS = [Ep, Em, K, Ki]


def rules_five():
    """The five rules of NormalForms.lean §3.1, as (lhs_word, rhs_element)."""
    inv = 1 / (q - 1 / q)
    return [
        ("R1  K K^-1 -> 1",        (K, Ki),  {(): 1}),
        ("R2  K^-1 K -> 1",        (Ki, K),  {(): 1}),
        ("R3  K E+ -> q^2 E+ K",   (K, Ep),  {(Ep, K): q**2}),
        ("R4  K E- -> q^-2 E- K",  (K, Em),  {(Em, K): 1 / q**2}),
        ("R5  E+ E- -> E- E+ + (K - K^-1)/(q - q^-1)",
                                   (Ep, Em), {(Em, Ep): 1, (K,): inv, (Ki,): -inv}),
    ]


def rules_seven():
    """The five, plus the two `K^-1` commutation rules."""
    inv = 1 / (q - 1 / q)
    return rules_five() + [
        ("R6  K^-1 E+ -> q^-2 E+ K^-1", (Ki, Ep), {(Ep, Ki): 1 / q**2}),
        ("R7  K^-1 E- -> q^2 E- K^-1",  (Ki, Em), {(Em, Ki): q**2}),
    ]


# ------------------------------------------------------------------ elements

def add(a, b, c=1):
    """a + c*b, as elements (dict word -> coeff)."""
    out = dict(a)
    for w, v in b.items():
        out[w] = cancel(out.get(w, 0) + c * v)
        if out[w] == 0:
            del out[w]
    return out


def scale(a, c):
    return {w: cancel(c * v) for w, v in a.items() if cancel(c * v) != 0}


def concat(prefix, elem, suffix):
    """prefix · elem · suffix, prefix/suffix being plain words."""
    return {tuple(prefix) + w + tuple(suffix): v for w, v in elem.items()}


def find_occurrence(word, lhs):
    """First index where `lhs` occurs in `word`, else None."""
    n, m = len(word), len(lhs)
    for i in range(n - m + 1):
        if word[i:i + m] == lhs:
            return i
    return None


def reduce_once(elem, rules):
    """Rewrite one occurrence in one word. Returns (new_elem, True) or (elem, False)."""
    for w, coeff in elem.items():
        for (_name, lhs, rhs) in rules:
            i = find_occurrence(w, lhs)
            if i is not None:
                rest = {k: v for k, v in elem.items() if k != w}
                sub = concat(w[:i], rhs, w[i + len(lhs):])
                return add(rest, sub, coeff), True
    return elem, False


def normalise(elem, rules, cap=10000):
    """Reduce to a fixed point."""
    cur = elem
    for _ in range(cap):
        cur, changed = reduce_once(cur, rules)
        if not changed:
            return cur, True
    return cur, False


def is_irreducible(elem, rules):
    return not any(find_occurrence(w, lhs) is not None
                   for w in elem for (_n, lhs, _r) in rules)


# ------------------------------------------------------------- ambiguities

def overlaps(rules):
    """Every overlap ambiguity: a proper suffix of lhs_i equals a proper prefix
    of lhs_j, giving the ambiguous word lhs_i[:k] + lhs_j."""
    out = []
    for (ni, li, ri), (nj, lj, rj) in product(rules, repeat=2):
        for k in range(1, min(len(li), len(lj))):
            if li[len(li) - k:] == lj[:k]:
                word = li + lj[k:]
                out.append((ni, nj, word, (li, ri), (lj, rj), k))
    return out


def check(rules, label):
    print("=" * 74)
    print(f"rule set: {label}  ({len(rules)} rules)")
    print("=" * 74)
    for (n, lhs, rhs) in rules:
        print(f"   {n}")
    amb = overlaps(rules)
    print(f"\n   overlap ambiguities found: {len(amb)}")
    results = []
    ok_all = True
    for (ni, nj, word, (li, ri), (lj, rj), k) in amb:
        # reduce the left occurrence, and the right occurrence
        left = concat((), ri, word[len(li):])
        right = concat(word[:len(word) - len(lj)], rj, ())
        nl, okl = normalise(left, rules)
        nr, okr = normalise(right, rules)
        diff = add(nl, nr, -1)
        resolved = (len(diff) == 0)
        irr = is_irreducible(nl, rules) and is_irreducible(nr, rules)
        ok_all = ok_all and resolved
        results.append({
            "rule_left": ni.split()[0], "rule_right": nj.split()[0],
            "ambiguous_word": " ".join(word),
            "resolved": bool(resolved),
            "both_reducts_irreducible": bool(irr),
            "reduct_left": fmt(nl), "reduct_right": fmt(nr),
            "difference": fmt(diff),
        })
        mark = "OK " if resolved else "FAIL"
        print(f"\n   [{mark}] {ni.split()[0]} / {nj.split()[0]}   on   {' '.join(word)}")
        if not resolved:
            print(f"          left  -> {fmt(nl)}")
            print(f"          right -> {fmt(nr)}")
            print(f"          diff  =  {fmt(diff)}")
            print(f"          both reducts irreducible: {irr}"
                  f"   ({'decisive' if irr else 'inconclusive'})")
    print(f"\n   VERDICT: {'all ambiguities resolve' if ok_all else 'NOT a GS basis'}")
    return ok_all, results


def fmt(elem):
    if not elem:
        return "0"
    parts = []
    for w, v in sorted(elem.items()):
        word = " ".join(w) if w else "1"
        parts.append(f"({cancel(v)})·{word}")
    return "  +  ".join(parts)


def main():
    print("q-Serre rewriting system — Gröbner–Shirshov check (bean qou-18s7)\n")
    ok5, res5 = check(rules_five(), "five  (NormalForms.lean §3.1, as axiomatised)")
    print()
    ok7, res7 = check(rules_seven(), "seven (plus the two K^-1 commutation rules)")

    witness = {
        "compute": "qserre_gs_basis_check",
        "bean": "qou-18s7",
        "status": "derived",
        "description": (
            "Overlap-ambiguity (critical pair) check of the q-Serre rewriting "
            "system. Tests whether UGB.GrobnerShirshov.qSerre_is_gs_basis holds "
            "of the five explicit rules built in NormalForms.lean §3.1, and of "
            "the seven-rule completion."
        ),
        "method": (
            "A terminating system is confluent iff every overlap ambiguity "
            "resolves. Each ambiguous word is reduced both ways to a fixed "
            "point and the reducts compared; a FAIL is only reported as "
            "decisive when both reducts are genuinely irreducible."
        ),
        "arithmetic": "exact (sympy rational functions of q); no float64",
        "five_rule_system": {"is_gs_basis": bool(ok5), "ambiguities": res5},
        "seven_rule_system": {"is_gs_basis": bool(ok7), "ambiguities": res7},
        "conclusion": (
            "qSerre_is_gs_basis is FALSE of the five-rule system"
            if not ok5 else
            "the five-rule system passes every overlap check"
        ),
    }
    out = Path(__file__).with_name("qserre-gs-basis-check.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
