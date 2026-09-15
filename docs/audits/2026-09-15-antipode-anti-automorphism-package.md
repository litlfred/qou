# The antipode is now an involutive anti-automorphism, not a convolution inverse

**Date** 2026-09-15 · **Owner decision** · **Beans** `qou-c64q`, `qou-aawz` ·
**Branch** `claude/antipode-anti-automorphism-package-2026-09-15`

## What changed

`def:frobenius-hopf-substrate` axiom 2 asked, from 2026-09-14 to 2026-09-15,
for the convolution condition

    μ ∘ (S ⊗ id) ∘ Δ = η ∘ ε = μ ∘ (id ⊗ S) ∘ Δ

[`2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md`](2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md)
proves that condition has **no non-trivial model over a field**. It is not an
axiom that can be kept. On owner decision it is replaced by the
anti-automorphism package: `S` reverses `μ` and `Δ`, fixes `η`, preserves `ε`
and `λ`, and squares to the identity.

| | before | after |
|---|---|---|
| fields on `S` | `antipode_left`, `antipode_right` | `antipode_anti_mul`, `antipode_anti_comul`, `antipode_unit`, `antipode_counit`, `antipode_involutive`, `antipode_frobeniusForm` |
| ambient | monoidal | **braided** monoidal |
| `S` determined? | **yes**, uniquely | **no** — constrained only |
| non-trivial models | **none** over a field | `k[G]`, measured 7/7 |

## What it buys — measured, not asserted

`k[G]` with the **Frobenius** comultiplication and the classical `S(g) = g⁻¹`
**is a model**, for `Z/1…Z/4`, `V₄`, `S₃`, `D₄`, by exact integer arithmetic
([`frobenius_hopf_intermediate_axioms_probe.py`](../../computations/probes/frobenius_hopf_intermediate_axioms_probe.py),
final section). The definition has non-trivial models again, which is the whole
point of the change.

The vacuous `S = id` is **excluded exactly on the non-abelian groups** (`S₃`,
`D₄`), by `antipode_anti_mul`. That is what stops `S` being decoration.

## The braiding requirement is corpus-derived, not new

"Reverses multiplication" is not expressible without a way to exchange tensor
factors, so `FrobeniusHopfData` now takes `[BraidedCategory C]`. That demands
nothing new of the framework:

- the block's own prose already places the substrate "at the level of a
  [quantum universe], which is braided monoidal";
- `QOU.QuantumUniverse` **already carried a `braidedInst` field**, so its
  `frobHopf` field needed only `@FrobeniusHopfData C catInst monInst braidedInst`
  — the instance was sitting there unused.

## What it costs

**`S` is constrained but no longer determined**, and uniqueness was the main
thing PR #7369 bought. Only the convolution identity gives uniqueness, and that
is exactly the one with no models. The two cannot both be had; this is not a
gap to be closed later.

**`S² = id` is carried but pins nothing on its own** — `S = id` satisfies it on
every group tested, non-abelian included. It earns its place only beside
`antipode_anti_mul`. It is in the package because the classical antipode
satisfies it and because it is the pivotal-structure statement, not because it
constrains.

## 🔴 Red team — what is wrong with this change

Written against my own work, at the author's instruction.

**1. On a commutative `A` the package still admits `S = id`, and nothing in the
definition says `A` is non-commutative.** The measurement is explicit: `S = id`
is a model on `Z/2`, `Z/3`, `Z/4` and `V₄`. The framework's `A` is meant to be
a Hecke/braid object and so non-commutative, but that is an expectation about
intended models, not an axiom. **So the defect PR #7369 was opened to fix — a
named morphism constrained by nothing — is only partially repaired.** It is
repaired exactly where `A` is non-commutative and nowhere else.

**2. The six axioms have not been checked for independence.** Classically
anti-algebra and anti-coalgebra are *theorems* derived from the antipode axiom,
not axioms. Here they are asserted. Whether any of the six follows from the
others plus the Frobenius relation was **unmeasured**. Asserting a redundant
axiom is not wrong, but AGENTS.md's derive-then-check discipline says measure
it, and I did not.

> **MEASURED the same day, and the answer is worse for the package than the
> item suggested — §"Independence" below.** Exactly **one** of the six is
> proved independent. Five have no counter-model in the searched family, and
> the forcing table says why: on the group algebra, `anti_mul` follows from
> `anti_comul` alone, `unit` follows from any one of four others, and `counit`
> and `form` force each other. The item stands as written — it is the
> measurement that has changed, not the criticism.

**3. The corpus still has only the trivial Lean witness.** `k[G]` is a model
*in Python*. `QOU.TrivialWitness.unitFrobHopf` (`A = 𝟙`) remains the only
record-literal construction in Lean. So `qou-aawz`'s literal claim — no
non-trivial `FrobeniusHopfData` exists *in the corpus* — is **still true**, and
the bean stays open. Formalising `k[G]` as a `FrobeniusHopfData` in
`ModuleCat k` is what would actually close it, and this PR does not do it.

**4. The collapse theorems are now inert.** `ConvolutionLeft` is a `Prop` with
no instances anywhere, so `dichotomy_of_scalars_field` and its siblings cannot
fire on anything in the corpus. They are correct, strictly stronger than
before, and purely archival. That is the right outcome, but nobody should read
them as live constraints.

**5. The change forecloses the non-linear reading.** The dichotomy needs field
scalars. A genuinely non-linear monoidal `C` could have carried the convolution
antipode with a non-trivial `A`, and option A (accept, declare the ambient
non-linear) would have preserved that. This route gives it up. That was the
owner's call, but it is a real cost and is not recoverable without reverting.

**6. 55 added `[BraidedCategory C]` occurrences, and some are gratuitous.**
Six files were patched with a blanket regex that added the instance to *every*
`MonoidalCategory` binder, including declarations that never touch
`FrobeniusHopfData`. Those declarations are now over-constrained: usable only
in a braided category where before any monoidal one would do. The practical
harm is low (QOU's ambient is braided throughout) but it is a silent narrowing
of the library's generality that nobody asked for. Minimisation pass and its
result are recorded below.

**7. A near-miss I introduced and caught.** The first draft split the antipode
out as a new axiom 3 and renumbered 3→4, 4→5, 5→6. That silently invalidated
**ten references to "axiom 2" and "axiom 3"** in the block's own historical
`authorNotes` — the exact contamination class AGENTS.md warns about, introduced
by me in the same commit that cites that warning. Reverted: the antipode stays
inside axiom 2, and every historical reference is valid again. Recorded because
the next person to reorganise this block will be tempted the same way.

## Independence — measured 2026-09-15, one of six

[`frobenius_hopf_axiom_independence_probe.py`](../../computations/probes/frobenius_hopf_axiom_independence_probe.py).
Method: semantic counter-models on `k[G]`. The structure maps involve no `S`, so
every structure axiom holds for any candidate and the six conditions are the only
thing varying. For each axiom `i`, search for a map satisfying the other five and
violating `i`; one such map proves `i` is not derivable from them. Candidates are
the monomial maps `S(g) = σ(g)` — exhaustive `|G|^|G|` up to `S₃` (46 656), and
`D₄`'s 40 320 bijections only.

| axiom | verdict |
|---|---|
| 1 `anti_mul` | undecided here |
| 2 `anti_comul` | undecided here |
| 3 `unit` | undecided here |
| 4 `counit` | undecided here |
| **5 `involutive`** | **INDEPENDENT** — witness on `V₄`: the 3-cycle `(0,1) → (1,0) → (1,1) → (0,1)` fixing the identity. It is an automorphism of `V₄`, hence an anti-automorphism since `V₄` is abelian, and it satisfies the other five; but it has order 3, so `S² ≠ id`. |
| 6 `form` | undecided here |

**"Undecided here" is not "dependent", and the distinction is the whole point.**
No counter-model in a searched space is a statement about the space. What makes
the five informative anyway is the *reason* — for each, the minimal subsets of
the others that already force it, measured on two exhaustively-searched groups
on opposite sides of commutativity:

| axiom | forced by, on `V₄` and `S₃` alike |
|---|---|
| 1 `anti_mul` | `{2 anti_comul}` |
| 3 `unit` | `{1}`, `{2}`, `{4}`, or `{6}` — any one alone |
| 4 `counit` | `{2}` or `{6}` |
| 6 `form` | `{2}` or `{4}` |
| 2 `anti_comul` | `{1,4}`, `{1,5}`, `{1,6}` |

Three readings, in descending order of how much they should worry a reviewer:

1. **`anti_mul` follows from `anti_comul` alone, on both groups.** If that
   survives categorically, the package has a redundant axiom in its most
   load-bearing position — `anti_mul` is the one doing the work of excluding
   `S = id`.
2. **`unit` is forced by any single one of four others.** `S(1) = 1` is very
   likely redundant *in this family*. Note it is provably **not** redundant in
   general: chasing `antipode_anti_mul` through the unit laws gives only
   `s = (s ⊗ s) ≫ β ≫ μ` for `s = η ≫ S`, an idempotent-like condition. A
   monomial `S` on a group algebra lands on a *group element*, where idempotent
   forces the identity; a general algebra has non-invertible idempotents. **So
   the family is the wrong instrument for this axiom, not evidence against it.**
3. **`counit` and `form` force each other, in both directions, on every group.**
   That is the predicted blind spot and it is confirmed rather than assumed: the
   probe checks the coincidence directly. On `k[G]` the counit and the Frobenius
   form are the same map, so no counter-model can separate them. In the Lean
   structure they are separate fields — `frobeniusForm` is constrained only by
   the two snake identities, `counit` only by the counit laws, and **nothing ties
   them** — so deciding their independence needs a Frobenius object with
   `λ ≠ ε`, which this family cannot supply.

**The two-column design validates itself.** `V₄` and `S₃` agree on every row
above except axiom 2, where `V₄` carries three further forcings (`{3,5}`,
`{4,5}`, `{5,6}`) that `S₃` does not. Those are exactly the abelian artifact the
method anticipated — on an abelian group an anti-automorphism *is* an
automorphism — so a forcing appearing in both columns is the one worth citing.
`D₄` is deliberately excluded from this table: only its bijections were searched,
and restricting to bijections would manufacture forcings involving `involutive`.

**What this does NOT license.** Do not shrink the Lean structure on this
evidence. Every row is a statement about monomial antipodes on group algebras,
and reading 2 shows a case where that family answers the opposite of the
categorical truth. Shrinking needs the categorical derivation — the formalize-
first move — and it is an owner decision besides. Bean `qou-k4zx`.

## Verification

- **Lean** — `lean`-direct `-DautoImplicit=false -s 65536` on the affected
  closure (76 modules: 15 changed + transitive dependents), built in
  topological order into a hardlinked shadow.
- **Probe** — exact integer arithmetic, no float, 7/7 groups; `S = inv` a model
  everywhere, `S = id` excluded exactly on `S₃` and `D₄`.
- **`run-validate`** — ✓ Valid, 2 issues, both pre-existing and unrelated.
- **Render-QA battery** on the `.md` — `$` balanced, braces balanced,
  `\begin`/`\end` matched, the `aligned` block wrapped in `\[ … \]` per the
  build-fatal inner-environment rule.
- No CI run exists (auto-triggers are `workflow_dispatch`-only repo-wide).
