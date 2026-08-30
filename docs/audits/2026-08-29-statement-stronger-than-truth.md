# The complementary check: is the statement *stronger than the truth*?

**Date:** 2026-08-29 · **Bean:** `qou-k3hh`
**Tool:** [`scripts/unbounded-quantifier-audit.py`](../../scripts/unbounded-quantifier-audit.py) (`--selftest`)
**Companion:** [`2026-08-29-q-ns-conditional-class-audit.md`](2026-08-29-q-ns-conditional-class-audit.md)
**Origin:** the q-RH arc's coordination comment on PR #6041

---

## Two questions, neither subsuming the other

`limit-claim-encoding-audit.py` asks *is the statement **weaker** than its
prose?* — a field documented as a limit that encodes none.

This asks the mirror: *is the statement **stronger** than the truth?* — an
external theorem asserted for every inhabitant of a structure that does not
carry the theorem's hypotheses. Named by the q-RH arc, which proved `False`
from two `hasse-weil-bound` axioms quantified over an arbitrary
`LocalQZetaFunction`.

**A field can pass one and fail the other, and one did.**
`HasQPlancherelCLT.bound` was flagged by the first detector, triaged a false
positive on its own terms (it carries an explicit quantitative bound rather
than an unlocalised one) — and is genuinely refutable under the second. That
pairing is the reusable lesson: neither check is a superset, so a clean run of
one says nothing about the other.

## The detector

Flags a class field that bounds an **arbitrary** quantity by a **fixed**
constant: a `∀`-bound variable that nothing constrains appears on the bounded
side, while the bounding side mentions class data.

`--selftest` is **two-sided** — it requires the detector to flag the known
refutable `HasQPlancherelCLT` shape *and* to **not** flag its repair. The
negative control is the important half; without it, an over-broad detector
reports success by flagging everything.

**Precision was low, and three of the four causes are now fixed** (2026-08-30).
The first pass reported 20 candidates for one genuine defect. Three
false-positive sources were structural rather than inherent:

| cause | shape | rule added |
|---|---|---|
| proof binder | `hn : H.n ≥ 2` — a proof, not a quantity | skip binders whose type is a proposition |
| `∃` witnesses the variable | `∀ M, ∃ q, M < enstrophy q` — unboundedness, satisfiable | skip statements containing `∃` |
| finite index | `i : Fin channels` — boundedly many values | skip `Fin`/`Bool`/`Unit`/`Empty` binders |

Measured A/B on the same tree: **19 → 9 candidates.** (Both numbers on the
current corpus; the original 20 was a different tree and is not comparable.)

**One near-miss worth recording.** The finite-type rule first included
`Finset`, which would have silently skipped the Rosso–Jones defect this
detector found — `∀ (partitions_of_r : Finset Partition), …`. A `Finset` is a
finite set, but the *type* of finite sets is infinite, so such a binder is
arbitrary. Caught before shipping and pinned as a positive control; the
`--selftest` now has five arms — it must flag the `HasQPlancherelCLT` and
Rosso–Jones shapes, and must **not** flag a repaired carrier, a proof binder,
an `∃`-witnessed bound, or a finite index.

The remaining nine still need reading: the residual false positives are fields
where both sides are class data (an instance chooses them together) and binders
over a non-archimedean parameter type (`∀ n : ℕ, (n : K) < omegaSurreal` is
satisfiable exactly because `K` is not archimedean). Construct the cheapest
inhabitant before calling anything a defect.

## The genuine hit: the Rosso–Jones index set

[`QOU/Archimedean/rj_canonical_inner_product.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/rj_canonical_inner_product.lean)
stated `J(τ(r,s)) = Σ_{λ ⊢ r} d_λ(q) · ω_λ^s` with the index set universally
quantified:

```lean
jonesPoly_eq_eval : ∀ (s : ℕ) (partitions_of_r : Finset Partition),
  jonesPoly r s = partitions_of_r.sum (fun lam => rjPairing lam lam * fullTwistEig lam ^ s)
```

The sum is over the partitions **of `r`** — one specific finite set. Quantified
over every `Finset`, the field is instantiable at `∅`, which forces

```
jonesPoly r s = 0   for every s
```

**Machine-checked against the class as it stood on main**, `#print axioms`
clean. Every model of the old class had an identically vanishing Jones
polynomial, so `rj_canonical_inner_product_torus_knot` — the Rosso–Jones
theorem — held only in that degenerate setting. Both theorems propagated the
defect, taking the arbitrary `Finset` as a free argument of their own.

### Why nothing caught it before

The class remained **inhabitable** (take every scalar zero), so this is not the
`False`-derivation shape the q-RH arc found and not the vacuity shape
`qou-hjf4` catalogues. It is *collapse*: consistent, non-vacuous by every
shipped criterion, and empty of the content it names. That is a third failure
mode in this family, and the reason the detector keys on the quantifier rather
than on inhabitability.

### Fix

`partitionsOf : Finset Partition` is now class **data**, and the field quantifies
only over `s`. Both theorems drop the free `Finset` argument. Regression probe:
[`2026-08-29-rosso-jones-index-set-probe.lean`](2026-08-29-rosso-jones-index-set-probe.lean)
proves the old shape collapses **and** exhibits a model of the fixed shape with
a non-vanishing Jones polynomial — so the repair is a correction, not a
different way to say nothing.

## Same session, same family, three repairs

| carrier | what was quantified that should have been fixed | consequence |
|---|---|---|
| `HasQPlancherelCLT.bound` | the sequence `f` and its limit `f_inf` | **uninhabitable** — `False` derivable |
| `ChiralityFactorClass.kauffman_derivation` | the evaluation `a_K` itself (and the error was unbounded) | trivially discharged by `error_term := 0` |
| `HeckeRepRingContext.jonesPoly_eq_eval` | the summation index set | **collapse** — forces `jonesPoly ≡ 0` |

The repair is the same move each time: **the object the claim is about must be
data or a parameter, never existentially or universally quantified inside the
claim.** Quantifying over it turns a statement about a particular
mathematical object into a statement about all objects of its shape — which is
either false, or trivial, or empty, but never the theorem.
