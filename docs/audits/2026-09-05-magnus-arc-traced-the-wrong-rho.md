# The Magnus arc traced the wrong ρ — and the b-decay is not there for the right one

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — complete n=9 census at
one q₀. Nothing wired, no witness, no fit. **This is a negative result about my own arc.**

## The claim

Every probe in this arc — roughly twelve merged PRs, all of today — built its `ρ` as

```python
gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
```

and applied a bare `σ_g` per letter. **`atom_braid_word_3A` does not return a braid word.** Its own
docstring says so in capitals (PR #5765; a rename was considered and rejected at 685 call sites
across 382 files, so the misnomer is permanent and the docstring carries the correction). Each triple
`(c, d, g)` denotes the **Hecke element `c·σ_g + d·1`**.

Measured at A=3 (`n=9`), 35 letters:

| letter class | count | what the bare form applies |
|---|---|---|
| `σ` (`d = 0`) | 16 | `σ` ✓ |
| `σ⁻¹` (`d = −h`) | 12 | `σ` ✗ |
| averaged (`σ − (h/2)·1`) | 7 | `σ` ✗ |

**19 of 35 letters — 54 % — were applied as the wrong operator.** So the arc's `ρ` is the *positive
braid on the generator sequence*, not the atom's Hecke element. The averaged letters are not even in
the image of `ρ : B_n → H_n(q)`, so the object the arc traced is not merely a different element — it
is in a different class.

## The measurement

`magnus_true_hecke_element_probe.py` runs the complete n=9 census under both elements through one
kernel, so nothing but the coefficients differs. `c·σ_g + d·1` on a vector is `c·(σ_g v) + d·v`, so
the ≤2-sparse structure that lifted this arc's dim cap (#6729) is untouched.

**The envelope `E(b) = max_{b(λ)=b} tr_λ(X*X)/dim_λ`:**

| b | ρ_bare (what the arc measured) | ρ_true (the atom element) |
|---|---|---|
| 1 | 4147.5518 | 18.758498 |
| 2 | 2527.9007 | 28.880297 |
| 3 | 955.31763 | **31.352745** ← peak |
| 4 | 495.69802 | 27.946757 |
| 5 | 265.95412 | 22.050067 |
| 6 | 62.579996 | 18.926529 |
| 7 | 2.9063514 | 13.001647 |

**Strictly decreasing in `b`: ρ_bare YES ✓ — ρ_true NO ✗.** Under the true element the envelope
*rises* from `b=1` to `b=3` and only then falls.

**And the decay is not merely non-monotone; it is essentially absent.** Total dynamic range across
all seven levels:

- **ρ_bare: 1427×** (4147.55 → 2.906)
- **ρ_true: 2.41×** (31.35 → 13.00)

A quantity that varies by a factor of 2.4 across the whole `b` range cannot carry a row-truncation
error bound no matter how it is ordered. The monotonicity failure is the smaller problem.

**The hook split does not survive either.** Ranking each level by `tr(X*X)/dim` under ρ_true, the
hook is level-**MIN** at `b=2`, level-**MAX** at `b=3, 5, 6, 7`, and 3rd of 5 at `b=4` — no crossing,
and roughly the opposite of the clean level-max → level-min pattern at `b=4` that ρ_bare shows and
that three independent measurements had agreed on.

## But the PRACTICAL claim survives — and is slightly better

`|tr|/dim` is **not** the quantity the row truncation depends on. The bean's operational statement is
about the y-weighted mass `|c_λ| = y_λ·|tr(ρ_λ Ω₂)|`, which weights by `y_λ` and by `dim_λ` — both of
which `|tr|/dim` discards. Measured under both elements, convention D:

| b | λ | `y_λ` | share ρ_bare | share ρ_true |
|---|---|---|---|---|
| 0 | (9) | 0.02212228 | 0.0 % | 0.0 % |
| 1 | (8,1) | 0.01663817 | 70.452 % | **73.499 %** |
| 2 | (7,2) | 0.01188126 | 21.998 % | 17.675 % |
| 3 | (6,3) | 0.007643638 | 7.0228 % | 5.4949 % |
| 4 | (5,4) | 0.003740086 | 0.52712 % | 3.3304 % |

**Monotone decreasing in `b` under BOTH elements**, and `b=1` carries *more* mass under the true
element (73.5 %) than under the one the arc measured (70.5 %). So the defect above does **not** break
the truncation — it breaks the theorem the arc was trying to prove *about* it.

**One figure does not reconcile and I am not going to paper over it.** The bean records *"b=1
reflection rep 86→92 % for A=3→4"*; I measure **70.45 % (bare) / 73.50 % (true)** at A=3. The gap is
unexplained. Candidates, none verified: the 86 % predates the 2026-09-05 word-ordering fix; it was
computed under convention C (where `y_λ ≠ 0` for `ℓ(λ) > 2`, so the denominator has more terms); or
`|c_λ|` was normalised differently. Worth settling before the 86 % is quoted again.

## The bigger thing this exposes: the sum is already linear

Under **convention D** (canonical since the 2026-08-09 owner ruling), `y_λ = 0` for `ℓ(λ) > 2`. So
the sum `Σ_λ y_λ tr(ρ_λ Ω₂)` runs over ≤2-row partitions only. Measured, n = 3…12:

| n | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| partitions `p(n)` | 3 | 5 | 7 | 11 | 15 | 22 | 30 | 42 | 56 | 77 |
| **nonzero `y_λ`** | 2 | 3 | 3 | 4 | 4 | 5 | **5** | 6 | 6 | **7** |
| `⌊n/2⌋+1` | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 7 |

**Exactly `⌊n/2⌋+1` at every n tested — linear, not exponential.** At n=9 that is 5 terms of 30; at
n=12, 7 of 77.

The bean exists to *"upgrade the poly-size row-truncation from heuristic to a rigorous error bound"*.
If the sum being truncated is this one, **the row cap already makes it linear, with no b-decay theorem
required** — the poly-size property the bean wants to establish would be a consequence of convention
D rather than of anything about `b`.

### And the corpus already knew half of this

Rather than ask, I looked. [`atom_bond_dimension_measure.py:94`](../../computations/atom_bond_dimension_measure.py)
says it outright, reached from the other direction by a prior agent:

> *"the 0.2–3.4 % figures are CONVENTION-C measurements … **Under D the ≤2-row truncation is already
> exact**, so this measurement supports no error and no invalidity verdict."*

That is the same fact as my `⌊n/2⌋+1` count, independently arrived at. And it re-scopes the witness
that declared truncation unusable — `active-set-truncation-prototype.witness.json`
(computed 2026-08-15) concluded *"rows≤3 recovers ≥99.9 % … ~10⁻³ TRUNCATION ERROR … **truncation is
INVALID for production**; valid only with a proven tail bound < 10⁻¹⁵"*. Under D that 10⁻³ is not the
truncation error, because the dropped terms carry weight **exactly zero**.

### So the bean's premise needs splitting, and the two halves fare differently

`qou-o6ov` exists to *"upgrade the poly-size **row**-truncation from heuristic to a rigorous error
bound"*. But the arc has spent itself on decay in **`b = n − λ₁`**, and for a ≤2-row shape `(n−k, k)`
we have `b = k`. **Row count and `b` are different gradings, and only one of them is the bean's
stated target:**

- **The ROW truncation (`ℓ(λ) ≤ 2`) is EXACT under convention D**, not heuristic. `y_λ = 0` off it,
  measured. There is no error term, so there is nothing to bound — the thing the bean set out to make
  rigorous is already rigorous, by the 2026-08-09 ruling rather than by any theorem about `b`.
- **A further `b`-truncation is still a real approximation** — dropping `b ≥ 2` discards 26.5 % of the
  mass under ρ_true — but it would take a sum that is **already linear** (`⌊n/2⌋+1` terms) down to a
  constant number of terms. That is a constant-factor win, not a complexity class, and it still needs
  the tail bound the arc has not got.

**That is the load-bearing finding of this document.** The arc's remaining rate work is not worthless,
but it is worth much less than the bean's framing implies, and it is aimed at a different grading than
the bean's stated purpose. Before more effort goes into the rate, that framing should be corrected in
the bean itself.

## What this means for the bean, stated carefully

`qou-o6ov` is a **GAP** bean whose purpose is *"upgrades the poly-size row-truncation from heuristic
to a rigorous error bound"*. The theorem it asks for, in its own words, is

> `|tr(ρ_λ Ω₂)|/dim_λ` decays with `b(λ)`.

**For the atom's Hecke element, at n=9, that statement is false** — `E(1) < E(3)` is an explicit
counterexample to the monotone form, and the 2.41× range refutes the useful form. For the positive
braid on the same generator sequence it holds cleanly, over 1427×.

So the arc's twelve PRs measured a real and fairly strong property of a real object. It is not the
object the bean names.

**Read together with the two sections above, the arc's position is:** the theorem it was proving is
false for the right element; the practical claim that motivated the theorem is true for the right
element; and the poly-size property that motivated the practical claim may follow from the convention-D
row cap without either. That is three levels of "the thing above it did not need this", and the honest
next step is to check the consumer before proving anything further.

## What is NOT affected, and it is the part that was formalized

**Every Lean file in this arc is untouched.** All five are stated over a generic
`{R : Type*} [CommRing R]` with `ρ : A` an *arbitrary* algebra element, and none mentions the atom
word:

- `MagnusCurvatureCommutator.lean` — `trace_mul_commutator_eq`, `trace_mul_commSum_eq_zero_of_commute`
- `MagnusOmega2LocalDecomposition.lean` — `omega2_reduces_to_adjacent`, `trace_rho_commutator_reframe`
- `MagnusHookExteriorPower.lean` — `prod_one_add_mul_eq_sum_esymm`
- `MagnusHookDecayBound.lean` — `abs_esymm_le_esymm_abs` and its two corollaries
- `MagnusGaugeCurvatureHookColumn.lean` — `trace_mul_curvature_eq_sum_word_traces`

These prove things about *any* `ρ`, so which element the numerics fed them is irrelevant to their
truth. **This is what formalize-first bought, and it is worth naming**: the discipline that looked
like overhead is the reason a 54 %-wrong input invalidated no theorem. The numerics were about the
wrong element; the theorems were not about any particular element.

Also unaffected: the **Féray–Śniady prune** (#6822). Its argument is that FS's bound depends on λ
only through the transpose-invariant `max(r(λ), c(λ))` while the measured quantity is
transpose-asymmetric. That is structural — only the 263.16× figure is ρ_bare-specific.

## What is NOT established

- **n=9 only, one q₀.** The counterexample `E(1) < E(3)` refutes monotonicity *at this size for this
  element*; it says nothing about large `n`.
- **The truncation is not wrong** — measured above, it survives and improves. The defect breaks the
  theorem, not the practice.
- **The `⌊n/2⌋+1` count is measured at n ≤ 12, not proved**, and it is a statement about `y_λ` under
  convention D, not about any other sum in the corpus.
- **The row-vs-`b` split is established; the production caller is not.** I have shown `y_λ = 0` off
  ≤2 rows under D, and that the corpus already recorded the ≤2-row truncation as exact. I have **not**
  read the specific production consumer of `P(A) = Σ_λ y_λ tr(ρ_λ Ω₂_λ)` to confirm it truncates in
  `b` at all — it may keep all `⌊n/2⌋+1` terms, in which case there is no approximation anywhere and
  the rate question is moot rather than merely smaller.
- **The 86 % ↔ 70.5/73.5 % gap is unresolved** and I have not determined its cause.
- **Which ρ the bean *should* be about is not settled here.** I have measured that the two differ and
  which statements hold for which. Whether the row truncation in production consumes the Hecke element
  or a braid is a question about the consumer, not about this census.
- **I have not re-run the arc's other legs under ρ_true** — the n=12 work, the two-row sector
  reduction, the sl₃/Kostka handle, the κ decomposition. They are all ρ_bare.

## Method note

**This is the second input-drift finding in one session, and the first one masked the second.** I
found the braid *ordering* change (`7db032fb48`) by chasing a 10 % discrepancy, recomputed the whole
census against it, and wrote that up — and the ordering fix was the smaller of the two defects sitting
in the same function. Reading the docstring properly is what found the larger one, and I only read it
because the ordering hunt had already sent me there.

Every probe in this arc prints its `q₀`, its `dps`, and its `n` — the three inputs that were never in
doubt. None prints the word, its length, or a hash of it. A one-line `hash(tuple(gens))` beside the
dps line would have made both defects visible as a changed number in the header rather than as a
discrepancy chased across two sessions.

The deeper version: `[int(t[2]) for t in ...]` reads as an obviously-correct projection to "the
generator indices", and it *is* — the error is in believing that is all a letter carries. The
function is named `atom_braid_word_3A`, and a braid word's letters **are** bare generators. The name
is doing the misleading, which is exactly why the rejected rename mattered, and why the correction
has to live somewhere a caller will actually hit.
