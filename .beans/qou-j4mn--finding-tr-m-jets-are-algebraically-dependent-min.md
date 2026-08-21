---
# qou-j4mn
title: 'FINDING: tr_M jets are ALGEBRAICALLY DEPENDENT (min degree 7, nullspace dim 3, stability-verified) - forced since all three are in Q(sqrt q), trdeg 1. So JetTransportImpliesIndependence cannot be a transfer of independence; JetOrderIndependence is only a LINEAR rank certificate'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-09T23:10:29Z
updated_at: 2026-08-21T19:50:01Z
---

## Body written 2026-08-21 (archaeology — the bean was filed with no body)

Filed 2026-08-09 with the title as its entire content. Recovered, verified, and
scoped on branch `claude/jet-algebraic-dependence-2026-08-21` (PR #5402).
Full write-up: [`docs/audits/2026-08-21-jet-algebraic-dependence-convention-d.md`](../docs/audits/2026-08-21-jet-algebraic-dependence-convention-d.md).

### Verdict on the title's three claims

| Claim | Verdict |
|---|---|
| Dependence is **forced**, trdeg 1 | **HOLDS** — convention-independent |
| Traces lie in `Q(sqrt q)` | **Convention-C-frame.** Under canonical D: the *smaller* field `Q(q)` |
| **min degree 7, nullspace dim 3** | **DOES NOT REPRODUCE.** Under D the minimum is **3** |
| `JetOrderIndependence` is only a LINEAR rank certificate | **HOLDS** (verified, not inherited) |
| `JetTransportImpliesIndependence` "cannot be a transfer of independence" | **Right verdict, wrong reason** |

### Why the numbers moved: import-cone drift, not a stale producer

The probe's own source is byte-identical since the witness was written (only
`elapsed_sec` formatting changed, `79d21b2fda`). But **both** cone modules moved
in `162d66eb7d`, and `markov_trace_recursive.py:66` now reads

```python
z_sym = q**3 / (q**2 + 1)
```

which is **convention D** (canonical, owner ruling 2026-08-15). The witness
predates that migration and was computed under **convention C**,
`z = sqrt(q)/(q+1)` — which is precisely why the title says `Q(sqrt q)`: under C
the traces genuinely carry a square root. Under D they do not:

| knot | `tr_M` (convention D, exact) |
|---|---|
| `4_1` | `(q^8 - q^6 + q^4 - q^2 + 1) / (q^2 (q^2+1)^2)` |
| `5_2` | `(q^10 - q^8 + 2q^6 - q^4 + 2q^2 - 1) / (q^3 (q^2+1)^2)` |
| `B_3` | `-(q^12 - 3q^10 + 2q^8 - 4q^6 + 2q^4 - 3q^2 + 1) / (q^4 (q^2+1)^2)` |

The `(q^2+1)^2` denominators are the convention-D signature (one per Markov peel).
Per AGENTS.md the degree-7 figures are **correct for C and need scoping, not
correction** — do not "fix" them into 3.

### The measured answer under D

Minimal total degree **3**, via a *two-variable* relation in
`x = tr_M(4_1)`, `z = tr_M(B_3)`:

```
16 x^3 - 5 x^2 z - 19 x^2 + 11 x z - 2 x - 5 z^2 + 4 = 0
```

Three methods sharing no machinery, exact arithmetic throughout (sympy over `Q`,
`Fraction`; no float anywhere — the problem is algebraic):

1. **Field membership** — `free_symbols == {q}` for all three.
2. **Resultant elimination** — a degree-3 factor of the `(4_1, B_3)` resultant.
3. **Exact complete minimal-degree search** on the rational functions themselves,
   no jets and no truncation: nullspace 0 at degree 1–2, dim **1** at degree 3.

Methods 2 and 3 yield the **identical** polynomial by disjoint routes; it vanishes
exactly at `q = 7/3, 2, -5/4, 11/7` under pure-`Fraction` arithmetic.

**Cross-check.** The relation annihilates the committed probe's *own* `jet_series`
to order 40, every coefficient exactly zero — its jets are right; only its recorded
verdict is C-frame. Re-running that producer today gives nullspace **1 / 4 / 12** at
`d = 3 / 4 / 5`, against the witness's `0` at `d = 5`. The 1 and 4 are exactly the
multiples of a single degree-3 relation by monomials of degree `<= 0` and `<= 1`,
which is what confirms 3 is *minimal* rather than merely present.

Producer: [`computations/jet_algebraic_dependence_verification.py`](../computations/jet_algebraic_dependence_verification.py).

### Scope classification (AGENTS.md)

The forcing argument is a **scope-(b) structural exclusion**; the cited invariant
is the **transcendence degree**. `Q(q)` — equally `Q(sqrt q)` — has `trdeg_Q = 1`,
and any two elements of a trdeg-1 extension are algebraically dependent over `Q`;
the Taylor map into `Q((g))` is a field embedding, so the relation transfers to the
jets. No probe can overturn this; a probe can only measure the degree. This is the
one place the convention is irrelevant: `trdeg_Q Q(sqrt q) = trdeg_Q Q(q) = 1`.
**The structural finding is robust; only the measured degree was convention-dependent.**

### The Lean consequence — the actual bug

**`JetOrderIndependence` — the title is right.** It declares
`jacobianRank : ℕ → ℕ` with `full_rank : ∀ N, 3 ≤ N → jacobianRank N = 3`: a claim
about the **rank of a matrix**, i.e. linear algebra. "Only a LINEAR rank
certificate" is correct. This is *not* in tension with the dependence finding —
linear independence of jet coefficient vectors and algebraic dependence of the
underlying functions are logically independent, and here **both hold at once**
(rank 3 at the base order, elimination determinant `1/16`; and a degree-3 algebraic
relation). Nothing needs retracting; the *name* invites the conflation.
Arity note: `full_rank` is a **level-indexed family**, not one proposition, and is
currently **uninstantiated** — see `qou-1n7g` / `qou-xc8t`.

**`JetTransportImpliesIndependence` — right verdict, wrong reason.** The title says
it cannot be a transfer of independence *because* the jets are dependent. That
argument does not go through: **the class never mentions the tr_M jets.** Its
conclusion is about `vol_4_1, vol_5_2, vol_B3` — three real numbers — and (per the
original probe's own scope warning) the `q -> 1` jet of `tr_M` is not an expansion
of `Vol(K)`. The finding does not reach the class by that route.

It is defective for a **different and more basic** reason: it is a §3b-cond
**item-5 self-assuming projection**. Its single field *is* the downstream
conclusion (`nonempty_independence : Nonempty HyperbolicVolumeIndependence`), and
the consumer `hyperbolicVolumeIndependence_of_reduction := R.nonempty_independence.some`
uses **neither** `[JetOrderIndependence]` nor `[SurrealParallelTransportBound E]`.
Both binders are decorative. Filed as a follow-up.

### Follow-ups

1. Scope (do not delete) `jet-algebraic-independence.witness.json` as C-frame.
2. Restructure `JetTransportImpliesIndependence` per §3b-cond item 5 — separate bean.
3. `JetOrderIndependence` remains uninstantiated, correctly (`qou-1n7g`, `qou-xc8t`).
