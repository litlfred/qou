# Axiomatising the Ocneanu-weight input

**Verdict: the dependency is now in the type. Nothing became more proved.**

Owner-directed follow-up to
[#5217](https://github.com/litlfred/qou/pull/5217), which proved
`y_λ = 0 ⟺ ℓ(λ) > r` sorry-free for all `n` and all `r`, and that convention D
is exactly Wenzl level `r = 2`. That work rested on **one** external input —
Wenzl (1988), that the Ocneanu/Markov-trace weights on `H_n(Q)` *are* the
principal specialisations — carried as a `-- Ref:` comment and absent from
every signature.

Lean: [`QOU/QBeta/WenzlWeightVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean).

## Read this first: what did and did not change

Per AGENTS.md §"Axiomatization is NOT a Proof", **axiomatising an input does
not discharge it**. A `class` is an assumption wearing infrastructure. So:

| | before | after |
|---|---|---|
| `schurPrincipal_eq_zero_iff` (the formula vanishes iff `ℓ(λ) > r`) | proved | proved — *unchanged* |
| `wenzlLevel_conventionD` (D is level 2) | proved | proved — *unchanged* |
| the actual Ocneanu weight vanishes iff `ℓ(λ) ≥ 3` | **cited as following from Wenzl, in a comment** | **proved conditional on Wenzl 1988, in the signature** |

The third row is the whole change, and it is a change in *legibility*, not in
epistemic status. The statement was already conditional; a reader had to notice
a comment to know it. Now the compiler carries it.

**Cite the conditional results as "proved conditional on Wenzl 1988", never as
"proved".**

## The class

```lean
class IsOcneanuWeightSystem (Q z : R) (r : ℕ) (y : YoungDiagram → R) : Prop where
  markovParameter_eq : z * (1 - Q ^ r) = Q ^ r * (1 - Q)
  weight_eq_schurPrincipal :
    ∃ Z : R, Z ≠ 0 ∧ ∀ μ : YoungDiagram, y μ = schurPrincipal r Q μ / Z
```

Two fields, doing two different jobs:

- **`markovParameter_eq`** is an *applicability condition* on the setup: the
  trace's Markov parameter `z` is Wenzl's at level `r`, i.e.
  `z = Q^r(1−Q)/(1−Q^r)`, cleared of denominators.
- **`weight_eq_schurPrincipal`** is *the external input*: at that parameter the
  weights are the level-`r` principal specialisations, up to the normaliser `Z`
  fixed by `Σ_λ f^λ y_λ = tr(1) = 1`. Only `Z ≠ 0` is used, so the statement is
  independent of which normalisation convention is in force.

### Why `class` and not `axiom`

Both were on the table; the class wins on four counts, and loses on one.

1. **An `axiom` could never be discharged.** The class can. Whoever formalises
   `H_n(Q)` and its Markov trace supplies the instance, and every conditional
   statement below becomes unconditional **with no edit to this file**. An
   axiom would have to be deleted, and everything depending on it re-audited.
2. **An `axiom` would have to be stated somewhere.** Wenzl's theorem quantifies
   over the Hecke algebra and its trace. Lean cannot see either. An axiom would
   therefore have to be stated either at one fixed `(Q, z, r)` — which is
   weaker than the theorem and useless for the level family — or over a
   formalisation that does not exist. The class is parameterised over
   `(Q, z, r, y)` and states the property *at* whatever instantiation a caller
   brings.
3. **The class is satisfiable and falsifiable, and both are proved** (below).
   An axiom is neither; it is simply asserted.
4. **§3b-cond is the repo's codified pattern** for exactly this situation, and
   it specifies an explicit `[Instance]` hypothesis.

**The cost, stated plainly: the dependency does *not* appear in
`#print axioms`.** A class hypothesis is a binder, not an axiom, so the axiom
report is byte-identical for the conditional and unconditional declarations
(see the table below — this is not a hypothetical, it is the measured output).
The dependency appears in the **type** instead. That is why every conditional
lemma wears `_of_wenzl` in its name, per the Mathlib `_of_` convention AGENTS.md
requires of conditional lemmas. It is also a real gap in the repo's audit
surface, filed as `qou-fpjy`.

### §3b-cond non-degeneracy — the trap, and how it was avoided

The failure mode §3b-cond names is a class that carries **the block's own
conclusion** as a field, with a "theorem" that projects it out
(`:= ctx.claim_foo`). That satisfies the propagation audit while proving
nothing.

Nothing about vanishing appears in either field. The conclusion is **derived**:

```
markovParameter_eq  ──→ level_eq_two_of_conventionD ──→  r = 2
                                                              ╲
weight_eq_schurPrincipal ────────────────────────────────────→ transport
                                                              ╱
schurPrincipal_eq_zero_iff  (unconditional, ~30 lines) ──────╱
                                                    ↓
                        conventionD_ocneanuWeight_eq_zero_iff_of_wenzl
```

The operational test: **delete `schurPrincipal_eq_zero_iff` and the conditional
theorem no longer follows from the class.** It passes.

Both fields do real work, neither is decoration. `markovParameter_eq` is not
merely carried along — it is consumed by `level_eq_two_of_conventionD` to pin
the *integer* `r = 2`, which is what lets the convention-D corollary be stated
without `r` as a hypothesis.

**Said honestly, though:** the transport step itself is short. The mathematical
content lives in the unconditional lemma; the class is a bridge and is
described here as one. What makes it non-degenerate is not that the derivation
is long, but that the conclusion is nowhere among the premises.

### The limitation that matters most: `y` is opaque

The class cannot *quantify over* the actual Ocneanu weight. Lean cannot see
`H_n(Q)`, so `y` is an arbitrary function and the class only names the property
a candidate `y` would have to have.

**This means the class is a faithful statement of the input *as used*, not a
full statement of Wenzl's theorem.** Wenzl's theorem asserts that a particular
object — the Markov trace's Wedderburn weight system — exists and has this
form. What is axiomatised here is the second half only; the first half is not
even expressible. Producing an instance for the real trace weights *is* Wenzl's
theorem, and is exactly what remains unformalised.

This is the honest state, and it is what the last section scopes.

### No instance is registered

`isOcneanuWeightSystem_schurPrincipal` is a plain `theorem`, deliberately **not**
an `instance`, so typeclass search can never silently discharge an
`[IsOcneanuWeightSystem …]` hypothesis. Its docstring says outright that it does
not discharge Wenzl: it establishes only that the *defined* function is its own
principal specialisation, which is `rfl`.

An instance for the real weights should be added **only** by proving Wenzl's
theorem.

## Which declarations became conditional, and which did not

**Unconditional — 16 of 19 declarations.** Untouched in statement; two
docstrings sharpened to say they are about the *formula* and not the Ocneanu
weight.

| Declaration | Status |
|---|---|
| `one_le_hook` | unconditional, pre-existing |
| `colLen_gt_of_content_eq_neg` | unconditional, pre-existing |
| **`schurPrincipal_eq_zero_iff`** | **unconditional, pre-existing** — the mathematical core |
| `wenzlLevel_conventionD` | unconditional, pre-existing |
| `conventionD_weight_eq_zero_iff` | unconditional, pre-existing; docstring sharpened |
| `conventionD_weight_eq_zero_iff_rowLens` | unconditional, pre-existing |
| `conventionD_weight_ne_zero_of_two_rows` | unconditional, pre-existing |
| `not_root_of_unity_of_pos_ne_one` | unconditional, pre-existing |
| `colLen_ofRowLens_one_one_one`, `colLen_ofRowLens_two_one` | unconditional, pre-existing |
| `discriminates_at_n_three` | unconditional, pre-existing |
| `pow_level_mul_eq_of_markovParameter` | **new**, unconditional — pure `ring` |
| `level_unique_of_markovParameter` | **new**, unconditional |
| `level_eq_two_of_conventionD` | **new**, unconditional |
| `isOcneanuWeightSystem_schurPrincipal` | **new**, unconditional — satisfiability |
| `not_isOcneanuWeightSystem_const_one` | **new**, unconditional — falsifiability |

**Conditional on Wenzl 1988 — 3 declarations**, each carrying
`[IsOcneanuWeightSystem …]` in its signature and `_of_wenzl` in its name:

| Declaration | Statement |
|---|---|
| `ocneanuWeight_eq_zero_iff_of_wenzl` | `y μ = 0 ↔ r < μ.colLen 0`, general `r` |
| **`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`** | **`y_λ = 0 ⟺ λ has ≥ 3 rows`** — #5207's statement, about the object #5207 meant |
| `conventionD_ocneanuWeight_ne_zero_of_two_rows_of_wenzl` | the surviving side |

The boundary in one sentence: **everything about `schurPrincipal` is
unconditional; everything about `y` is conditional.**

### The boundary is visible in the signatures

```
@schurPrincipal_eq_zero_iff : ∀ {R} [Field R] {Q : R},
  Q ≠ 0 → (∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) →
  ∀ (r : ℕ) (μ : YoungDiagram), schurPrincipal r Q μ = 0 ↔ r < μ.colLen 0

@ocneanuWeight_eq_zero_iff_of_wenzl : ∀ {R} [Field R] {Q : R} (z : R) {r : ℕ}
  {y : YoungDiagram → R} [hw : IsOcneanuWeightSystem Q z r y],
  Q ≠ 0 → (∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) →
  ∀ (μ : YoungDiagram), y μ = 0 ↔ r < μ.colLen 0
```

`z` and `r` are **explicit arguments** on the conditional lemmas. Neither
appears in the conclusion, so typeclass resolution cannot recover them; leaving
them implicit produces *"typeclass instance problem is stuck"*. Callers must
name the parameter and level they are working at, which is a small usability
cost and, on balance, a documentation benefit.

## New unconditional lemmas, and one thing they do not give

- `pow_level_mul_eq_of_markovParameter : Q^r * (1 − Q + z) = z` — the inversion
  `Q^r = z/(1 − Q + z)` in denominator-free form. Pure `ring`, **no hypotheses
  at all**, which the axiom report confirms: it is the only declaration in the
  file not depending on `Classical.choice`.
- `level_unique_of_markovParameter` — for `Q ≠ 0` and `Q` not a root of unity,
  **at most one** `r` sits at a given `z`. Both hypotheses are load-bearing: at
  `Q = 0` the genericity condition `∀ k ≠ 0, Q^k ≠ 1` holds *vacuously* (since
  `0^k = 0 ≠ 1` for `k ≠ 0`, negative exponents included), and uniqueness
  genuinely fails there — `z = 0` and every `r ≥ 1` satisfy the relation. So
  `hQ0` is an explicit argument rather than something derived from `hQ`.
- `level_eq_two_of_conventionD` — convention D's parameter pins the **integer**
  `r = 2`, not merely `Q^r = Q²`.

**What they do not give: existence.** `level_unique_of_markovParameter` says the
level is unique *if it exists*. So the likely verdict on convention C — that
`Q^r = z_C/(1 − Q + z_C)` has no natural-number solution — is a *non-existence*
statement and follows from nothing in this file. It needs its own proof, and it
will need a monotonicity-in-`r` argument at fixed positive `q`, i.e. it lands
below the §7c archimedean wall unlike the rest of the file. Filed as `qou-7d08`;
flagged to [#5229](https://github.com/litlfred/qou/pull/5229), which owns the
numerics.

## The class is satisfiable, and it is not vacuous

A conditional theorem behind an *unsatisfiable* hypothesis proves nothing; one
behind a hypothesis satisfied by *everything* constrains nothing. Both are ruled
out, in Lean:

- `isOcneanuWeightSystem_schurPrincipal` — some `y` meet the class.
- `not_isOcneanuWeightSystem_const_one` — the constant function `1` **fails** it
  at `Q = 2` over `ℚ`, at level 2, *for every* `z`, because it does not vanish
  on the three-row diagram `(1³)`. So the class genuinely constrains `y`.

Together these bracket the hypothesis from both sides.

## Verification

`lean`-direct against the real import cone, **exit 0**, no warnings, 2.7 s.
Not via `lake build`: this tree is a cache restore with no `.trace` files and
`lake build` would evict it (bean `qou-r13s`). Mathlib olean count **6990**
before and **6990** after; total **7268** before and after.

`#print axioms` on all 19 declarations plus the class:

```
'…one_le_hook'                                        [propext, Classical.choice, Quot.sound]
'…wenzlLevel_conventionD'                             [propext, Classical.choice, Quot.sound]
'…colLen_gt_of_content_eq_neg'                        [propext, Classical.choice, Quot.sound]
'…schurPrincipal_eq_zero_iff'                         [propext, Classical.choice, Quot.sound]
'…conventionD_weight_eq_zero_iff'                     [propext, Classical.choice, Quot.sound]
'…conventionD_weight_eq_zero_iff_rowLens'             [propext, Classical.choice, Quot.sound]
'…conventionD_weight_ne_zero_of_two_rows'             [propext, Classical.choice, Quot.sound]
'…not_root_of_unity_of_pos_ne_one'                    [propext, Classical.choice, Quot.sound]
'…colLen_ofRowLens_one_one_one'                       [propext, Classical.choice, Quot.sound]
'…colLen_ofRowLens_two_one'                           [propext, Classical.choice, Quot.sound]
'…discriminates_at_n_three'                           [propext, Classical.choice, Quot.sound]
'…pow_level_mul_eq_of_markovParameter'                [propext, Quot.sound]
'…level_unique_of_markovParameter'                    [propext, Classical.choice, Quot.sound]
'…level_eq_two_of_conventionD'                        [propext, Classical.choice, Quot.sound]
'…isOcneanuWeightSystem_schurPrincipal'               [propext, Classical.choice, Quot.sound]
'…not_isOcneanuWeightSystem_const_one'                [propext, Classical.choice, Quot.sound]
'…ocneanuWeight_eq_zero_iff_of_wenzl'                 [propext, Classical.choice, Quot.sound]
'…conventionD_ocneanuWeight_eq_zero_iff_of_wenzl'     [propext, Classical.choice, Quot.sound]
'…conventionD_ocneanuWeight_ne_zero_of_two_rows_of_wenzl'  [propext, Classical.choice, Quot.sound]
'…IsOcneanuWeightSystem'                              [propext, Classical.choice, Quot.sound]
```

No `sorryAx`. No `sorry`, no `native_decide`, no Lean `axiom`, no `: True`.

**Read that table for what it does not show.** The three `_of_wenzl`
declarations are conditional on an unformalised published theorem, and the axiom
report cannot tell you so — it is identical to the unconditional rows. That is
correct kernel behaviour and a genuine blind spot in the repo's honesty gate,
which keys on `#print axioms` (AGENTS.md §Phase-4 verification gate) and on
`sorry`/`axiom`/trivial-true patterns (`lean-vacuity-axiom-audit.ts`). A
content-bearing class carrying a cited external theorem matches none of them.
Filed as `qou-fpjy`.

This is a standalone library file with no `.qa.json` sidecar, so nothing but
this check covers it (AGENTS.md §"QA is agent-owned").

## Then what? — the route to unconditional

**Scoped below.** The short answer: the route is to formalise `H_n(q)` and the
Ocneanu trace in Lean and prove Wenzl's theorem, and it is a substantially
larger build than anything in this file.

### What "unconditional" would require

To discharge `IsOcneanuWeightSystem` for the real trace weights you must be able
to **state** Wenzl's theorem, which means having in Lean: the Hecke algebra
`H_n(q)`, its `T_w` basis, its Markov trace, its partition-indexed irreducible
characters, and the Schur function's principal specialisation. Only then is
there an object to prove the theorem *about*.

### What Mathlib already has (measured, not assumed)

Surveyed against the pinned revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(toolchain `leanprover/lean4:v4.24.0`), all 6990 modules of the local build.

| Ingredient | Status in Mathlib |
|---|---|
| Coxeter systems, length, reduced words, descents, inversions | **exists** — `Mathlib/GroupTheory/Coxeter/{Matrix,Basic,Length,Inversion}.lean` |
| `CoxeterSystem.lift` (universal property) | **exists** — the right tool for defining `T_w` |
| Artin–Wedderburn | **exists, strong** — `RingTheory/SimpleModule/WedderburnArtin.lean`, incl. `exists_algEquiv_pi_matrix_divisionRing` |
| `LinearMap.trace`, `Algebra.trace`, `Algebra.traceForm` | **exists** |
| `e/h/p/m` symmetric polynomials + fundamental theorem | **exists** — `RingTheory/MvPolynomial/Symmetric/*` |
| `YoungDiagram`, `.card`, transpose, `rowLen`/`colLen`; `Nat.Partition` | **exists** (this file already uses it) |
| **Iwahori–Hecke algebra `H_n(q)`** | **ABSENT — entirely** |
| **Braid group `B_n`** | **ABSENT** (the eight `Braid*` modules are categorical braidings, a different notion) |
| **Temperley–Lieb algebra** | **ABSENT** |
| **Matsumoto's theorem** | **ABSENT** |
| **`S_n` as a Coxeter group of type A** | **ABSENT** — `CoxeterMatrix.Aₙ` exists as a *matrix* but is never proved to present `Equiv.Perm`; nothing in Mathlib consumes `Coxeter` at all |
| **Specht modules / irreps of `S_n`** | **ABSENT** — no classification of `S_n` irreps by partitions |
| **Schur polynomials `s_λ`** | **ABSENT** (the three `Schur` modules are Schur's *lemma*, the Schur *complement*, and Schur–Zassenhaus) |
| **Principal specialisation, hook lengths, contents** | **ABSENT** |
| **Standard Young tableaux, `f^λ`, RSK** | **ABSENT** — only *semi*standard tableaux exist, with no `Fintype` and no generating function |
| **Frobenius / symmetrising forms** | **ABSENT** |

Two findings worth calling out because they are worse than "not yet ported":

- **Mathlib has no Hecke algebra of any flavour at this pin.** A grep for
  `Hecke` across all 6990 modules matches exactly one file, and that match is a
  bibliography line in the FLT module docstring. There is not even a
  modular-forms Hecke operator to disambiguate from.
- **The Coxeter files are an island.** `Coxeter` appears only inside the four
  `Coxeter/*` modules themselves. So the foundations are good but load-bearing
  nothing, and the `A_n`-presents-`S_n` bridge — the first thing this build
  needs — does not exist.

### The build, in dependency order

Each item depends on the ones above it.

1. **`S_n` is a Coxeter group of type A.** Prove
   `CoxeterSystem (CoxeterMatrix.Aₙ n) (Equiv.Perm (Fin (n+1)))`, bootstrapping
   from `Equiv.Perm.mclosure_swap_castSucc_succ` (generation is there; the
   *presentation* is not). Smallest item, and independently Mathlib-worthy.
2. **`H_n(q)` and its `T_w` basis.** The sharp gap. The standard route to
   well-definedness of the basis is **Matsumoto's theorem**, which is absent —
   so either prove Matsumoto for general Coxeter systems (a real project, but
   `alternatingWord` / `braidWord` / `IsReduced` / the descent lemmas are
   exactly the right substrate), or take the Bourbaki–Iwahori route and
   construct the left/right multiplication operators on the free module
   directly, getting associativity by hand. The second is likely cheaper here
   and does not produce a reusable Mathlib theorem.
3. **Generic semisimplicity of `H_n(q)`.** Artin–Wedderburn is available as a
   black box, but Tits' deformation argument (`H_n(q) ⊗ K ≅ K[S_n]`) is not,
   and neither is the decomposition of `K[S_n]`, since item 4 is missing.
4. **Irreps indexed by partitions.** Specht modules and their `q`-deformation.
   Note this is not an optional convenience: **the indexing set of Wenzl's
   weight formula has no home in Lean without it.** The statement cannot be
   written down.
5. **The weight decomposition `tr = Σ_λ y_λ χ_λ`.** Wedderburn and
   `FDRep.character` both exist, but the general theory of decomposing a trace
   on a semisimple algebra into irreducible characters with weights is not
   packaged, and neither are central primitive idempotents as a labelled family
   — which is precisely the object that indexes the weights.
6. **Schur polynomials and the principal specialisation.** A definition
   (bialternant or SSYT-sum), then `s_λ(1, q, …, q^{r−1})`, whose standard closed
   form is the `q`-hook-content formula — needing hook lengths, contents and
   `q`-integers, none of which exist as symmetric-function tools. `f^λ` and SYT
   are needed for the `q → 1` degeneration checks.
7. **Wenzl's theorem itself**, on top of all of the above.

Honest size: this is a **Mathlib-contribution-scale project, not a session's
work** — plausibly several thousand lines across items 1–6 before item 7 is even
stateable, and items 2 and 4 are each a substantial piece of mathematics to
formalise rather than transcription. Item 1 alone is a respectable standalone
contribution.

### Is there a cheaper route? — one candidate, and two non-routes

**Candidate: prove only the vanishing set, not the weight formula.** What the
corpus actually consumes downstream is not the *values* `y_λ` but the *vanishing
set* — that the trace annihilates exactly the `≥ 3`-row blocks. That is what
gives `radical = ⟨E⁽³⁾⟩`, the `n! − Catalan(n)` coranks, and the `TL_n` compute
quotient (`qou-ondw`). One could get it by defining `TL_n`, showing the Markov
trace factors through `H_n ↠ TL_n`, and identifying `TL_n`'s blocks with the
`≤ 2`-row partitions — which **skips items 5 and 6 entirely**, i.e. the whole
symmetric-function and hook-content stack.

That is a genuine saving and worth costing properly before committing to the
full route. It is not free: it still needs items 1–4, and `TL_n`'s block
structure is its own representation theory. It also yields something weaker
than the class as currently stated, so the class would need re-shaping around
the vanishing set rather than the weight identity.

**Non-route 1: redefine rather than prove.** Declaring the Ocneanu weight to
*be* the principal specialisation makes the class vacuous by fiat. It also
destroys the content: the reason `radical = ⟨E⁽³⁾⟩` means anything is that the
weights are the *trace's* Wedderburn weights. Named here only so nobody reaches
for it as a shortcut.

**Non-route 2: verify at fixed `n` and generalise.** Constructing `H_3(q)`
concretely and solving the Markov conditions is tractable — #5185 already did it
symbolically — but note the class as written quantifies over *all* Young
diagrams with no `n` parameter, so a fixed-`n` instance does not fit it without
reformulation. And at `n = 6` the algebra is 720-dimensional, well past what a
kernel-level decision procedure will absorb. This buys confidence, not
unconditionality.

**One thing to check before starting anything:** whether Hecke algebras are
in flight for Mathlib upstream. Nothing was found at this pin, but the survey
covers the pinned build only, not open PRs. If someone is already landing items
1–3, the cheapest route is to wait and contribute to that.

### Recommendation

**Keep the conditional, and cite it honestly.** The dependency is on a
39-year-old, widely-used published theorem, not on a gap in the framework's own
reasoning; the cost of discharging it in Lean is out of proportion to the risk
that Wenzl is wrong. What was worth doing is what this PR did — making the
dependency impossible to miss.

If any of this build does get done, do it for its own sake — items 1–4 are
independently valuable to the corpus and to Mathlib, and the `TL_n` route in
particular is the same infrastructure `qou-ondw` wants. Discharging this one
class would be a by-product, not the motivation. Filed as `qou-v32l`.

## Scope note

Nothing here is a refutation, and no scope-(b) structural exclusion is claimed.
No previously-proved result is weakened, re-proved, or called into question.
The one negative — the vanishing criterion is false at a root of unity — is
unchanged from #5217 and is a statement about the hypothesis, not the framework.
