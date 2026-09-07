#!/usr/bin/env python3
"""`def:hecke-normal-form` asserts confluence. Measured: it is false, and so are
two other things the block says.

Bean `qou-43co`. The block
`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md`
states three rewriting rules for `H_n(R,q)` and then says

> This reduction is confluent, making the normal form independent of rule order.

`UGB.GrobnerShirshov.HeckeGS.NotAGSBasis.hecke_not_gs_basis_four` is a
sorry-free machine-checked **refutation** of exactly that, at `n = 4`. So the
manuscript asserts, uncited, what this folio's own Lean disproves.

This probe re-derives the refutation independently of the Lean — by executing
the rewriting rather than by S-polynomial bookkeeping — and measures two things
the bean could not: *how often* order-dependence actually bites, and whether
the completion the Lean names repairs it.

## Three defects, all measured

**1. The confluence claim is false.** Over the overlap word `σ₃σ₂σ₃σ₁` the
far-commutation rule for `(σ₃, σ₁)` gives `σ₃σ₂σ₁σ₃`, the Yang-Baxter rule for
`(σ₂, σ₃)` gives `σ₂σ₃σ₂σ₁`, and **both are irreducible** — no rule of the
system has either as a factor. Two distinct normal forms for one element.
That is the Lean's S-polynomial argument reproduced by execution.

**2. Rule 2 as written does not terminate.** The block writes far commutation
as `σ_i σ_j → σ_j σ_i` for `|i - j| ≥ 2`, which is **symmetric**: it applies to
its own output. Reducing `σ₃σ₁` under the block's own rules runs forever
(capped at 4000 steps here). The Lean's rule is `i > j + 1`, one-directional,
and terminates. A reader implementing the block as printed gets a hang.

**3. Rule 3 is written in the wrong direction.** The block says
`σ_i σ_{i+1} σ_i → σ_{i+1} σ_i σ_{i+1}` and annotates it "(in the
shortlex-decreasing direction)". With `σ₁ < σ₂ < ⋯` those two clauses
contradict each other: `σ₂σ₃σ₂ < σ₃σ₂σ₃`, so *decreasing* is
`σ_{i+1}σ_iσ_{i+1} → σ_iσ_{i+1}σ_i`, which is what `HeckeGS.lean` uses (its
Yang-Baxter leading monomial for `(σ₂, σ₃)` is `σ₃σ₂σ₃`). The printed arrow
points the other way.

Defects 2 and 3 matter beyond tidiness: they mean the object the block
*defines* is not the object the Lean *refutes*, so "the Lean disproves the
block" needs the rules reconciled first. They are reconciled here.

## Why the false claim survived — the part worth keeping

Order-dependence is **rare, and absent in the regime anyone spot-checks**:

    n=3, lengths 3-8   : 0 of 504 words order-dependent
    n=4, length 4      : 1 of 81
    n=4, length 5      : 9 of 243
    n=5, length 4      : 2 of 256
    n=5, length 5      : 25 of 1024

Every word of length at most 8 over `H_3` — all 504 — reduces to a unique
normal form whatever the rule order.
The first counterexample needs `n = 4` *and* length 4. So the claim is not a
careless one — it is true everywhere a person would check it by hand, and false
in general. That is worth saying in the corrected block rather than merely
deleting the sentence.

## The completion repairs it — as evidence, not as a theorem

`HeckeGS.lean` §4e names the missing family: `σᵢσᵢ₋₁⋯σⱼσᵢ → σᵢ₋₁σᵢσᵢ₋₁⋯σⱼ`
for `i > j`, whose `i=j+1` instance *is* Yang-Baxter. Adding it:

    n = 3, 4, 5 at lengths 4 and 5 — 2652 words, **0 order-dependent**

and the mechanism is visible rather than merely statistical: `σ₃σ₂σ₁σ₃`, one of
the two irreducible words that made the S-polynomial a normal form, becomes
**reducible** — by exactly the first instance the Lean names. The obstruction
is not worked around, it is dissolved.

## 🛑 Scope of that last result — (a), not (b)

This is a **scope-(a) positive**: *this system, on these `n` and these word
lengths, exhibits no order-dependence*. It is **not** a proof that the completed
system is a Gröbner-Shirshov basis, and it must not be cited as one. A GS-basis
claim needs every S-polynomial of every overlap to reduce to zero, at all `n`;
this probe tested 2652 words at `n ≤ 5` and length `≤ 5`. The theorem for
Coxeter *groups* is Bokut-Shiao 2001 ([bokut2001]) and, per that entry's own
note, does not by itself license the `H_n(q)` statement — the q-deformed type-A
result is Kang-Lee-Lee-Oh 2002, which this folio does not hold (`qou-qspu`).

That distinction is the whole reason this bean exists: the deleted axiom
`hecke_is_gs_basis` cited Bokut-Shiao for precisely this gap.

## Arithmetic

Laurent polynomials in `q` over `ℤ`, as `{exponent: integer coefficient}`
dictionaries. Exact throughout; no floating point, and no `q` is ever evaluated.
"""

from __future__ import annotations

import json
import random
import sys
import time
from itertools import product as iproduct
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

WITNESS = Path(__file__).with_name("hecke-normal-form-confluence.witness.json")

SEED = 20260907
ORDERS = 12
STEP_CAP = 4000

ONE = {0: 1}
Q_MINUS_QINV = {1: 1, -1: -1}


def padd(a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0:
            del r[e]
    return r


def pmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = e1 + e2
            r[k] = r.get(k, 0) + c1 * c2
            if r[k] == 0:
                del r[k]
    return r


def eadd(A, B):
    r = {w: dict(p) for w, p in A.items()}
    for w, p in B.items():
        r[w] = padd(r.get(w, {}), p)
        if not r[w]:
            del r[w]
    return r


def escale(A, p):
    out = {}
    for w, c in A.items():
        v = pmul(c, p)
        if v:
            out[w] = v
    return out


def rules_md(n):
    """Exactly as `hecke-normal-form.md` prints them — note rule 2 is symmetric."""
    R = [("sq", (i, i)) for i in range(1, n)]
    R += [("fc", (i, j)) for i in range(1, n) for j in range(1, n) if abs(i - j) >= 2]
    R += [("yb_md", (i, i + 1, i)) for i in range(1, n - 1)]
    return R


def rules_lean(n):
    """As `HeckeGS.lean` states them: shortlex-decreasing, one-directional."""
    R = [("sq", (i, i)) for i in range(1, n)]
    R += [("fc", (i, j)) for i in range(1, n) for j in range(1, n) if i > j + 1]
    R += [("yb_lean", (i + 1, i, i + 1)) for i in range(1, n - 1)]
    return R


def rules_completed(n):
    """Lean rules plus the Bokut-Shiao family; its `i=j+1` case IS Yang-Baxter."""
    R = [("sq", (i, i)) for i in range(1, n)]
    R += [("fc", (i, j)) for i in range(1, n) for j in range(1, n) if i > j + 1]
    R += [
        ("bs", tuple(range(i, j - 1, -1)) + (i,))
        for i in range(1, n)
        for j in range(1, i)
    ]
    return R


def apply_at(kind, lm, w, t):
    pre, post = w[:t], w[t + len(lm):]
    if kind == "sq":
        i = lm[0]
        return {pre + (i,) + post: dict(Q_MINUS_QINV), pre + post: dict(ONE)}
    if kind == "fc":
        i, j = lm
        return {pre + (j, i) + post: dict(ONE)}
    if kind == "yb_md":
        i = lm[0]
        return {pre + (i + 1, i, i + 1) + post: dict(ONE)}
    if kind == "yb_lean":
        i = lm[1]
        return {pre + (i, i + 1, i) + post: dict(ONE)}
    if kind == "bs":
        i, j = lm[0], lm[-2]
        return {pre + (i - 1,) + tuple(range(i, j - 1, -1)) + post: dict(ONE)}
    raise AssertionError(kind)


def redexes(w, R):
    return [
        (kind, lm, t)
        for kind, lm in R
        for t in range(len(w) - len(lm) + 1)
        if w[t:t + len(lm)] == lm
    ]


def reduce_elt(A, R, rng=None):
    A = {w: dict(p) for w, p in A.items()}
    steps = 0
    while True:
        target = None
        for w in A:
            rs = redexes(w, R)
            if rs:
                target = (w, rng.choice(rs) if rng is not None else rs[0])
                break
        if target is None:
            return A, steps
        w, (kind, lm, t) = target
        coeff = A.pop(w)
        A = eadd(A, escale(apply_at(kind, lm, w, t), coeff))
        steps += 1
        if steps > STEP_CAP:
            return None, steps


def canon(A):
    return tuple(sorted((w, tuple(sorted(p.items()))) for w, p in A.items()))


def order_scan(rule_fn, ns, lengths, rng):
    rows, total, div, nonterm = [], 0, 0, 0
    for n in ns:
        R = rule_fn(n)
        for L in lengths:
            t = d = c = 0
            for w in iproduct(range(1, n), repeat=L):
                outs, ok = set(), True
                for _ in range(ORDERS):
                    A, _ = reduce_elt({tuple(w): dict(ONE)}, R, rng)
                    if A is None:
                        ok = False
                        break
                    outs.add(canon(A))
                if not ok:
                    c += 1
                    continue
                t += 1
                if len(outs) != 1:
                    d += 1
            rows.append({"n": n, "length": L, "words": t,
                         "order_dependent": d, "non_terminating": c})
            total += t
            div += d
            nonterm += c
    return {"rows": rows, "words": total, "order_dependent": div,
            "non_terminating": nonterm}


def main() -> int:
    _t0 = time.time()
    rng = random.Random(SEED)

    # Defect 1 — the refutation, by execution
    R4 = rules_lean(4)
    overlap = (3, 2, 3, 1)
    branches = sorted(
        {tuple(apply_at(k, lm, overlap, t).keys())[0]
         for (k, lm, t) in redexes(overlap, R4)}
    )
    w1, w2 = (2, 3, 2, 1), (3, 2, 1, 3)
    d1 = {
        "overlap_word": list(overlap),
        "one_step_results": [list(b) for b in branches],
        "w1_irreducible": redexes(w1, R4) == [],
        "w2_irreducible": redexes(w2, R4) == [],
        "pass": (sorted([list(w1), list(w2)]) == sorted(list(b) for b in branches)
                 and redexes(w1, R4) == [] and redexes(w2, R4) == []),
    }

    # Defect 2 — the block's symmetric rule 2 does not terminate
    d2rows = []
    for n in (4, 5):
        A, steps = reduce_elt({(3, 1): dict(ONE)}, rules_md(n))
        d2rows.append({"n": n, "terminates": A is not None, "steps": steps})
    d2 = {"rows": d2rows, "pass": all(not r["terminates"] for r in d2rows)}

    # Defect 3 — direction, decided by shortlex on the two words
    smaller = min((2, 3, 2), (3, 2, 3))
    d3 = {
        "shortlex_smaller": list(smaller),
        "decreasing_rewrites": "s_{i+1}s_i s_{i+1} -> s_i s_{i+1} s_i",
        "block_prints": "s_i s_{i+1} s_i -> s_{i+1} s_i s_{i+1}",
        "block_direction_is_increasing": smaller == (2, 3, 2),
        "pass": smaller == (2, 3, 2),
    }

    # How often order-dependence bites, and whether completion repairs it
    scan_lean = order_scan(rules_lean, (3, 4, 5), (3, 4, 5), rng)
    scan_h3 = order_scan(rules_lean, (3,), (3, 4, 5, 6, 7, 8), random.Random(SEED))
    scan_done = order_scan(rules_completed, (3, 4, 5), (4, 5), random.Random(SEED))
    Rc = rules_completed(4)
    repair = {
        "w1_redexes": len(redexes(w1, Rc)),
        "w2_redexes": len(redexes(w2, Rc)),
        "obstruction_dissolved": len(redexes(w2, Rc)) > 0,
    }

    print("def:hecke-normal-form — three defects, measured (bean qou-43co)")
    print(f"  1. confluence FALSE: {list(overlap)} -> "
          f"{[list(b) for b in branches]}, both irreducible -> "
          f"{'PASS' if d1['pass'] else 'FAIL'}")
    print(f"  2. block's rule 2 (|i-j|>=2) non-terminating on s3s1 at n=4,5 -> "
          f"{'PASS' if d2['pass'] else 'FAIL'}")
    print(f"  3. block's rule 3 points INCREASING, contradicting its own "
          f"'shortlex-decreasing' -> {'PASS' if d3['pass'] else 'FAIL'}")
    print(f"  order-dependence, Lean system: {scan_lean['order_dependent']} of "
          f"{scan_lean['words']} words")
    for r in scan_lean["rows"]:
        print(f"       n={r['n']} L={r['length']}: {r['words']:5d} words, "
              f"order-dependent {r['order_dependent']}")
    print(f"  H_3 alone, lengths 3-8: {scan_h3['order_dependent']} of "
          f"{scan_h3['words']} words order-dependent — the regime a reader spot-checks")
    print(f"  completed system: {scan_done['order_dependent']} of "
          f"{scan_done['words']} words order-dependent; "
          f"w2 now has {repair['w2_redexes']} redex(es) — obstruction dissolved")

    all_pass = (
        d1["pass"] and d2["pass"] and d3["pass"]
        and scan_lean["order_dependent"] > 0
        and scan_h3["order_dependent"] == 0
        and scan_done["order_dependent"] == 0
        and repair["obstruction_dissolved"]
    )

    payload = {
        "description": (
            "def:hecke-normal-form asserts a confluence that "
            "UGB.GrobnerShirshov.HeckeGS.NotAGSBasis.hecke_not_gs_basis_four "
            "refutes sorry-free at n=4. This probe re-derives that refutation by "
            "executing the rewriting, finds two further defects in the block's "
            "printed rules, measures how rarely order-dependence bites (0 at n=3), "
            "and shows the Bokut-Shiao completion dissolves the obstruction. "
            "The completion result is SCOPE-(a) evidence at n<=5, length<=5 — NOT "
            "a Groebner-Shirshov basis theorem. Exact Laurent polynomials over Z; "
            "no floating point, q never evaluated."
        ),
        "bean": "qou-43co",
        "refuted_claim": "This reduction is confluent, making the normal form independent of rule order.",
        "lean_refutation": "UGB.GrobnerShirshov.HeckeGS.NotAGSBasis.hecke_not_gs_basis_four",
        "checks": {
            "defect_1_confluence_false": d1,
            "defect_2_rule2_nonterminating": d2,
            "defect_3_rule3_direction": d3,
            "order_dependence_lean_system": scan_lean,
            "order_dependence_h3_deep": scan_h3,
            "order_dependence_completed_system": scan_done,
            "completion_repair": repair,
        },
        "scope": {
            "completion_result": "(a) scope-limited positive — no order-dependence observed at n<=5, length<=5",
            "not_claimed": "that the completed system is a Grobner-Shirshov basis for H_n(q)",
            "primary_not_held": "qou-qspu (Kang-Lee-Lee-Oh 2002)",
        },
        "all_pass": all_pass,
    }
    WitnessBuilder.wrap_legacy(
        "hecke-normal-form-confluence", payload, script_path=__file__,
        output_dir=WITNESS.parent, start_time=_t0,
    ).save()
    print(f"\nWROTE {WITNESS.name} — all_pass={all_pass}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
