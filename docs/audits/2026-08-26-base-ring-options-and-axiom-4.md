# What the base ring can be — and why the stated one fails axiom 4

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Beans:** `qou-y7vg` (T3g base question)
**Trigger:** owner question — *"give the options of what it can be. I want it as
close to the commutative ring as possible. If we need to add in q and its inverse
that's okay… what's needed downstream as a consumer?"*

## The constraint, from the corpus's own axioms

`def:quantum-universe` axiom 4 requires, per block `λ`:

> a Frobenius weight `∫_A p_λ` **invertible in `R`**, and a quantum dimension
> `dim_q(λ)` **invertible in `R`**

and `quantum-universe-axiom-motivation.md` fixes the reading, deliberately:

> Over a field this is just non-vanishing; over a ring it is the stronger demand,
> **and it is the stronger one that is meant.**

So this is not a technicality to be relaxed. It is the binding constraint, and
everything below follows from it.

## The blocking fact

**The units of `ℤ[q, q⁻¹]` are exactly `{±q^k}`** — it is a Laurent polynomial
ring over a domain. But `dim_q(λ)` is a product of quantum integers, and in the
balanced convention the corpus uses (`[2]_q = q + q⁻¹`, §7c):

| bracket | factorisation | polynomial part |
|---|---|---|
| `[2]_q` | `q⁻¹ (q² + 1)` | degree 2 |
| `[3]_q` | `q⁻² (q²−q+1)(q²+q+1)` | degree 4 |
| `[4]_q` | `q⁻³ (q²+1)(q⁴+1)` | degree 6 |
| `[5]_q` | `q⁻⁴ (q⁴−q³+q²−q+1)(q⁴+q³+q²+q+1)` | degree 8 |

Each is a monomial times a polynomial of positive degree, which is never `±1`.

**So no `[m]_q` with `m ≥ 2` is a unit, and `ℤ[q, q⁻¹]` fails axiom 4 for every
block beyond the trivial one.** The ground ring the corpus names for itself does
not satisfy the corpus's own axiom.

## A bonus: convention D is free

`q · [2]_q = q² + 1`. Since `q` is already a unit, **convention D's denominator
`(q² + 1)` costs nothing beyond `[2]_q`.** Inverting the brackets covers the
Markov parameter `z = q³/(q²+1)` automatically; it is not a separate demand.

## The options, weakest first

| # | Ring | Axiom 4 | Field? | Notes |
|---|---|---|---|---|
| 0 | `ℤ[q, q⁻¹]` | ✗ | no | the stated one; units `±q^k` only |
| 1 | `ℤ[q, q⁻¹][ [2]_q⁻¹, …, [N]_q⁻¹ ]` | ✓ | **no** | minimal repair; `N = 18` measured |
| 2 | `ℤ[q, q⁻¹][ Φ_d(q)⁻¹ : d ≥ 2 ]` | ✓ | **no** | "`q` generic"; no `N` to track |
| 3 | Habiro `\widehat{ℤ[q]}` | ✗ | no | see below |
| 4 | `ℚ(q)` | ✓ | yes | works, but abandons the ring character |

**Option 1 is the recommendation.** It is a localisation of the stated ring — the
smallest change that makes the axioms true — stays a commutative ring, stays
non-local and non-field, and keeps `ℤ` coefficients. `N = 18` because hook
lengths for `λ ⊢ n` are `≤ n` and the corpus reaches `H_18`.

**Option 2** is the same idea stated without a cutoff: `[m]_q` factors into
cyclotomics, so inverting all `Φ_d(q)` for `d ≥ 2` covers every rank at once. It
is cleaner to state and strictly larger; prefer it if tracking `N` is annoying.

**Option 3 fails, and the reason is worth stating** because the Habiro ring looks
like the natural home — the corpus already defines it (`def:habiro-ring`,
`def:z-habiro-ring`) and Ch 12 builds on it. But `\widehat{ℤ[q]}` surjects onto
`ℤ[ζ]` at **every** root of unity, and the brackets vanish at exactly those
points. A ring that admits such a specialisation cannot make `[m]_q` a unit. The
Habiro ring is the right home for *elements* (`q`-series with root-of-unity
evaluations); it is the wrong base for a category whose axioms demand invertible
quantum dimensions.

## The tension this exposes

Axiom 4 in its intended strong form says: **`q` may not be a root of unity of
order `≤ N` in any specialisation of `R`.** That is precisely what a localisation
at the brackets enforces — it deletes those points from `Spec R`.

But open problem 5 names **root-of-unity truncation** as the candidate mechanism
for the observable-scale cutoff, and Ch 12's Habiro machinery exists to evaluate
at roots of unity.

**These pull in opposite directions, and the corpus does not record it.** The
resolution has to be that truncation lives *after* a base change out of `R` —
`R → R/Φ_d` or `R → ℤ[ζ_d]` — and not inside the base the category is linear
over. Otherwise axiom 4 and the truncation mechanism cannot both hold.

## Downstream consumers, measured

- **Lean:** of 2215 `QOU/**.lean`, **394** carry `[CommRing R]`, **185** `[Field R]`,
  5 `[DivisionRing]`, 4 `[GroupWithZero]`, 0 `[LinearOrderedField]`; **684** touch
  `ℝ` (the archimedean wall). The `[Field R]` files are where a weaker base would
  have to be re-examined; the `CommRing` majority is already compatible with
  options 1–2.
- **Rank:** `H_18` is the deepest Hecke algebra the corpus reaches, fixing `N = 18`
  for option 1.
- **Half-powers of `q`: not needed.** The only live `sqrt(q)` is
  `computations/all-elements-knot-table.py:19`, `math.sqrt(q)` — a float64
  archimedean evaluation, not a base-ring demand. Every other hit is under
  `_deprecated/` and is convention-C residue. **No `ℤ[q^{±1/2}]` is required.**
- **Archimedean specialisation survives.** Options 1 and 2 admit the ring map
  `R → ℝ`, `q ↦ q₀ ≈ 1.10998`: at real `q₀ > 1` every balanced bracket is
  strictly positive, so nothing that was inverted is sent to zero.

## Three owner follow-ups — including a correction to option 1

### `1/Φ_d(q)` vs `1/[d]_q` — the same ring, two generating sets

For a fixed cutoff these generate **the same localisation**, because a divisor of
a unit is a unit: each `Φ_d` divides a bracket, and each bracket is a product of
cyclotomics. Verified symbolically:

- **unbalanced** `[m]_q = ∏_{d | m, d > 1} Φ_d(q)`
- **balanced** (the corpus convention, §7c) `[m]_q = q^{−(m−1)} ∏_{d | 2m, d ≥ 3} Φ_d(q)`

so `[2]_q = q⁻¹Φ₄`, `[3]_q = q⁻²Φ₃Φ₆`, `[4]_q = q⁻³Φ₄Φ₈`, `[6]_q = q⁻⁵Φ₃Φ₄Φ₆Φ₁₂`.

The difference is what each is *good for*:

- **`Φ_d` is the primitive spelling.** Each is irreducible, so it names exactly
  which points you delete from `Spec` — the primitive `d`-th roots of unity. This
  is the right way to *state* the ring.
- **`[d]_q` is the consumer spelling.** Quantum dimensions are literally products
  of brackets, so this is the right way to write the *conditions* a block must
  satisfy.

One convention trap: because the balanced bracket runs over `d | 2m`, inverting
brackets up to `N` reaches cyclotomics up to `2N`, not `N`. Anyone converting
between the two spellings must say which convention they are in.

**Recommendation: define the ring in `Φ_d`, state the per-block conditions in
`[d]_q`.**

### 🛑 `N = 18` was wrong as a bound — it is `3A`, and `A` is not fixed

Option 1 above is stated with `N = 18`. That number is the current compute
ceiling, **not a structural bound**, and the distinction matters.

The braid rank is `n = 3A` — stated verbatim in
`computations/aK_via_lp_dual_full.py:11`, *"For each atom (Z, N) with n = 3A
strands"*. So `H_18` is `A = 6` (⁶Li) and `H_21` is `A = 7` (⁷Li). The
`dashboard-sweep` skill already targets ⁵⁶Fe, which is `A = 56` — **`H_168`**.

So `N` is `3 ×` (heaviest isotope attempted), and it moves whenever someone
computes one isotope further. **A base ring whose definition changes when you
extend a table is a bad base ring.**

This is the decisive argument for **option 2 over option 1**: inverting every
`Φ_d(q)` for `d ≥ 2` has no cutoff to maintain, covers every rank at once, and
removes exactly the locus axiom 4 forbids — `q` a nontrivial root of unity.
Option 1 remains the honest *minimal* answer for a fixed, declared rank ceiling;
it is not the right answer for a framework that intends to keep climbing `A`.

### "`R` commutative, localised at `q`" — three readings, none of them the fix

- **Invert the multiplicative set `{q^k}`.** `ℤ[q][1/q] = ℤ[q, q⁻¹]` — this is
  option 0 exactly, and it is the thing that fails axiom 4.
- **Localise at the prime ideal `(q)`.** `ℤ[q]_{(q)}` inverts everything *outside*
  `(q)`, so `q` lands in the maximal ideal and becomes a **non-unit**. That is
  strictly worse: Laurent structure is lost.
- **Localise at `ker(ℤ[q,q⁻¹] → ℝ, q ↦ q₀)`.** If `q₀` is transcendental over `ℚ`
  that kernel is `(0)` and the localisation is `Frac = ℚ(q)` — option 4. If `q₀`
  were algebraic you would get a DVR: a local ring at one point, discarding the
  whole `q`-family the framework is built on. (Whether `q₀` is transcendental is
  not settled here.)

The unifying point: **inverting `q` is free and already assumed — it is not the
missing ingredient.** What axiom 4 needs is the *brackets* inverted, and brackets
are not monomials. Option 0 → option 2 is precisely "keep inverting `q`, and
additionally invert what the axioms actually demand."

## Follow-on measured: is `[Field R]` real field dependence?

The 185 `[Field R]` files looked like the main obstacle to a non-field base.
Measured, they are mostly not.

**Only 4 of 185 declare `[Field R]` and never divide at all** — outright
gratuitous, and directly downgradeable to `[CommRing R]`:
`MathlibExt/SDPEmptyConstraints`, `BraidKnot/DepthStratifiedFrobeniusReciprocityVariance`,
`BraidKnot/HeckeFullTwistProduct`, `BraidKnot/HeckeJucysMurphyReduction`.

The other 181 do divide — but by **what** is the decision-relevant question, and
the answer is lopsided. Counting every inverse across those files:

| denominator | occurrences |
|---|---:|
| `q` | **1597** |
| local variables (`D`, `v`, `x`, `s`, `a^2`, `L_k`, `t`, `G`, `u`, `B`, …) | ~205 |
| `q^n`, `q^2`, `q + q⁻¹` | ~21 |
| `(2 : ℂ)` | 17 |

**About 88 % of all field usage is literally `q⁻¹`**, which `ℤ[q, q⁻¹]` already
supplies — no field needed, and no localisation either. The next tier
(`q^n`, `q²`, `q + q⁻¹`) is exactly what options 1 and 2 invert. The `(2 : ℂ)⁻¹`
hits are archimedean-side, past the wall, and say nothing about the base.

So `[Field R]` here is overwhelmingly a **convenience for writing `q⁻¹`** without
carrying an `Invertible q` instance, not a structural demand. The 185 count is
not evidence of deep field dependence, and it should not be read as an argument
against options 1–2.

**Scope of this measurement, stated honestly.** It counts the *syntactic shape*
of denominators, not their semantics. The ~205 local-variable inverses need
per-file inspection to tell a generic nonzero (which genuinely wants a field)
from a name bound to a `q`-expression (which does not). That residue is the only
part of the `[Field R]` surface still unmeasured, and it is where a migration
would actually have to do work.

## The residue, measured: ~10 files, not 185

The `[Field R]` sweep left ~205 local-variable inverses unclassified. Resolved by
checking how each variable is **bound** in its own file:

| class | occurrences | files | |
|---|---:|---:|---|
| generic — explicit `v ≠ 0`, no `q` binding | **88** | **6** | wants a field *as written* |
| bound to a `q`-expression | 15 | 7 | option 2 covers |
| neither pattern matched | 84 | — | needs eyes |

The six genuinely-generic files are `Hecke/ClosedFormInterfaceFactors`,
`Knot/HomflySkeinReference`, `QBeta/A3AntiSelfAdjointLift`,
`QBeta/DTIndexAmplitudeE`, `QBeta/SuperBerezinianA3Magnitude`,
`Torsion/YekutieliTriple`.

**And they have a clean ring-level fix.** Spot-checking the largest (`D`, 42
occurrences, `A3AntiSelfAdjointLift`) shows Berezinian / Schur-complement blocks:

```lean
def crossTerm {R : Type*} [Field R] (B C D : R) : R := B * D⁻¹ * C
```

with hypotheses `(hA : A ≠ 0) (hB : B ≠ 0) (hD : D ≠ 0)`. The file's own comment
already says *"scalar inverses `D⁻¹`, `A⁻¹` genuinely required"* — and that is
true, but it is a demand for **an inverse of a specific scalar**, not for a field.

Over a commutative ring the faithful spelling is `[Invertible D]` with `⅟D`:

```lean
def crossTerm {R : Type*} [CommRing R] (B C D : R) [Invertible D] : R := B * ⅟D * C
```

This is *more* faithful to the corpus's own stated intent, not less —
`quantum-universe-axiom-motivation.md` says in as many words that over a ring
invertibility is the stronger demand and *"it is the stronger one that is meant"*.
A `v ≠ 0` hypothesis is the field-flavoured weakening; `[Invertible v]` is the
ring-flavoured strengthening the axioms already ask for elsewhere.

**So the migration is roughly ten files, not 185:**

1. **4 files** — `[Field R]` → `[CommRing R]`, nothing else (they never divide).
2. **6 files / 88 occurrences** — `h : v ≠ 0` → `[Invertible v]`, `v⁻¹` → `⅟v`.
   Mechanical and local.
3. **84 occurrences** still need an eye, and are the only genuinely open part.

Everything else — the 1597 `q⁻¹`, the `q^n`/`q²`/`q+q⁻¹` tier, the archimedean
`(2 : ℂ)⁻¹` — is already compatible with option 2 and needs no change at all.

## What is not settled here

This answers *which ring makes the axioms true*. It does **not** answer the T3g
question of which **base scheme** the gerbe lives over — `Spec R` for whichever
`R` is chosen, versus the Reeb spectral base `Spec(ξ_q)`. Fixing `R` is a
prerequisite for that, not a substitute.

---

## 🛑 CORRECTED 2026-08-26 — "fails axiom 4" was too strong, and the tension does not exist

Owner question: *state the QOU axioms as generically as possible for a ring `R`;
what properties does `R` need — an injection into the canonical ring?* Answering
it required reading the Lean, and the Lean corrects two claims above.

### `R` needs only `CommRing`, and the axioms already say so

`structure QuantumUniverse (R : Type*) [CommRing R]`, with

```lean
frobWeight : blocks → R
dimQ       : blocks → R
frobWeight_isUnit : ∀ b, IsUnit (frobWeight b)
dimQ_isUnit       : ∀ b, IsUnit (dimQ b)
```

The invertibility is quantified over **this universe's own blocks**. It is a
condition on the pair `(R, C)`, never on `R` alone. The definition is already
maximally generic and should not be touched.

**`IsQGeneric` therefore does not belong in the definition.** It belongs to the
*construction* of a Hecke-type universe, where `dimQ b` is a bracket product and
the property is what discharges `dimQ_isUnit`. Adding it to
`def:quantum-universe` would over-constrain the definition to serve one family of
instances.

### No injection — and the direction is the other way

The canonical ring is **initial** for the property, so the unique map runs
`R_can → R`, *out of* it. An injection `R ↪ R_can` would be backwards, and would
exclude exactly the specialisations the framework depends on: `ℝ` at the
substrate anchor, `ℚ` at `q = 1`, `ℤ[ζ]` at a root of unity are **evaluations and
quotients, not subrings**. Injectivity must not be required even in the correct
direction — `R_can → ℚ` at `q = 1` kills `(q-1)` by design.

Nor should any map appear in the definition: for a universe over `R` the
invertibility fields are already given, so relating `R` to `R_can` adds nothing.

### The root-of-unity "tension" was mine, not the corpus's

This audit claimed axiom 4 conflicts with root-of-unity truncation and that *"the
corpus does not record it."* **Both halves are wrong.** `quantum-universe.lean`
records *and resolves* it, at the `blocks` field:

> **`blocks` indexes the NON-NEGLIGIBLE blocks, and vanishing elsewhere is
> permitted.** `dimQ_isUnit` below is therefore a specification of what `blocks`
> ranges over, NOT a prohibition on the ambient category. This matters at a root
> of unity (and in char p), where some `dim_q(λ)` really does vanish: those λ are
> *negligible* — they form a tensor ideal … Read as a prohibition, the field
> would exclude the root-of-unity categories outright; read as an index
> specification, it says the decomposition is that of the semisimplified
> quotient.

So axiom 4 never forbade roots of unity. My tension was an artifact of reading
the `.md` without the `.lean`.

### And "fails axiom 4" is too strong

Under the index-specification reading, `ℤ[q, q⁻¹]` does not *fail* the axioms —
it satisfies them **degenerately**, with the block index collapsed to the trivial
block, since no `[m]_q` with `m ≥ 2` is a unit there. The localisation is what
makes a **non-degenerate** universe available, carrying the framework's actual
Hecke decomposition. That is a weaker and more accurate statement than the one
this audit opened with, and `quantum-universe.md` has been rewritten to match.

The recommendation is unchanged: `R = ℤ[q,q⁻¹][Φ_d(q)⁻¹ : d ≥ 2]` as the
canonical **instance**, with the definition left at `CommRing`.

---

## 🛑 CORRECTED again — `q` is emergent, and the twist emits `v = q^{1/2}`

Owner: *"since `q` is emergent from the axioms, why do we need anything more? We
start with the base ring `R`, we emerge `q`, and then tensor product?"* Correct
on every count, and it corrects two more things here.

### Nothing more is needed, and the axioms already say why

`QuantumUniverse` has **no `q` field**. Its docstring:

> This is what makes the substrate parameter `q` *derivable rather than
> carried*. On the defining representation the twist axiom forces
> `θ_V = q^{1/2} · id_V`, so `q` is read off the structure; there is
> deliberately **no `q` field**, since a distinguished element would smuggle in
> as data the thing the framework claims to derive.

So the order of construction is exactly as stated: take `R : CommRing`; build an
`R`-linear braided `C` with `unitEndEquiv : R ≃+* End(𝟙)`; the **tensor and
braiding** are what produce the twist, and `q` is read off it into `End(𝟙) ≅ R`.
The invertibility the axioms want is then a statement about that emergent
element, already carried by `dimQ_isUnit` / `frobWeight_isUnit`.

**`IsQGeneric R q` takes `q` as a parameter, which is precisely the shape the
axioms refuse.** It is construction-side only — for building `H_n(q)`, where `q`
genuinely is an input — and must not be threaded into the definition. The Lean
file is rescoped accordingly.

### The half-powers claim was scoped wrong, and it matters for the ring

This audit says *"half-powers of `q`: not needed"*, on a measurement of
`computations/`. That measurement is sound but answers the **archimedean**
question, not the categorical one.

`rem:sqrt-q-ribbon-structure` states: *"The element `v := q^{1/2}` … On the
defining `SU_q(2)` representation, the twist axiom forces `Θ_V = q^{1/2} id_V`.
The binary sign choice on `v` dictates the spin structure on the realized
worldline."*

So the **ribbon structure emits `v = q^{1/2}`**, and it carries physical content
— the spin structure is the sign choice on `v`. A base carrying the ribbon twist
therefore contains `v`, not merely `q`.

**Consequence for the chosen ring, and it is the owner's call.** If the universal
example is to contain the emergent twist scalar, it is generated by `v` rather
than `q`:

    Z[v, v^{-1}][ … ]   with   q = v²

which is **Lusztig's convention**. The irony is worth stating plainly: earlier in
this audit I described `ℤ[v, v⁻¹]` as a *neighbouring community's related but
different* ring. On this evidence it may be the canonical one, and `ℤ[q, q⁻¹]`
the derived subring.

Not decided here. What is established is that the twist scalar is `v`, that it
is emergent rather than adjoined, and that the choice between `q` and `v`
generators is therefore a question about the ribbon structure and not about
convenience.
