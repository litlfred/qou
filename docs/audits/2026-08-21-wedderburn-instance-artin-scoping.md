# An instance of `WedderburnDecomp` would prove nothing — the class is satisfied by a one-dimensional algebra

**Verdict: the halves do not join, and joining them would not have helped.**
Branch `claude/wedderburn-instance-artin-2026-08-21`, PR #5387. Answers item 3 of
bean [`qou-luq7`](../../.beans/qou-luq7--defect-heckewedderburntrace-decomposition-is-self.md); tracked forward as `qou-hah4` and `qou-6dzi`.

## The question

`QOU.Hecke.WedderburnDecomp`
([`QOU/Hecke/Wedderburn.lean:72`](../../content/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean))
carries the Wedderburn diagonalisation of the Markov trace as class fields with
**no instance anywhere in the tree**, so `y_lambda` and
`tr_M = Σ_λ y_λ χ^λ` are assumed rather than derived — and `#print axioms`
cannot see that (bean `qou-fpjy`). The proposal put to this branch was: Mathlib
has Artin–Wedderburn, PR #4857 proved `finrank H_n(q) = n!`, put the two halves
together and ten modules become unconditional.

Three of those four clauses turn out to be wrong, and the fourth is beside the
point.

## 1. The premise about PR #4857 is false

PR #4857 (merged `c3380b19764f`, 2026-08-09) did **not** prove
`finrank H_n(q) = n!`. Read from its own body and from the merged files:

- It added `IsHeckeOfFullRank`
  ([`QOU/Hecke/FullRank.lean:70`](../../content/quantum-observable-universe/lean/QOU/Hecke/FullRank.lean))
  as a **companion predicate** — a hypothesis you assume, carrying
  `free : Module.Free R A` and `finrank_eq : Module.finrank R A = n.factorial`.
  It exists precisely because `QOU.Hecke.HeckeAlgebra` "asks for generators,
  three relations and spanning — never that `A` be free of rank `n!`".
- It proved `finrank_of_rank_recursion` — *if* `d 0 = 1` and
  `d (n+1) = (n+1) · d n` *then* `d n = n!`. Pure arithmetic; no Hecke content.
- It discharged full rank **concretely at n = 2, 3, 4 only**, and says n = 4 is
  "the last level worth instantiating by hand".

Separately,
[`QOU/SchurWeyl/HeckeCoset.lean:426`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeCoset.lean)
proves `finrank_le_factorial : Module.finrank K (Hecke K q qi m) ≤ (m+1)!` —
an **upper bound**, for all m, sorry-free. The all-n equality is in the tree in
neither direction as a single result.

## 2. Mathlib's Artin–Wedderburn does not deliver a partition-indexed decomposition

The relevant declaration is
`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`
(`Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean`, Junyan Xu 2025), with
`IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed` in
`SimpleModule/IsAlgClosed.lean` for the split case:

```lean
theorem IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing :
    ∃ (n : ℕ) (D : Fin n → Type u) (d : Fin n → ℕ) (_ : ∀ i, DivisionRing (D i))
      (_ : ∀ i, Algebra R₀ (D i)), (∀ i, NeZero (d i)) ∧
      Nonempty (R ≃ₐ[R₀] Π i, Matrix (Fin (d i)) (Fin (d i)) (D i))
```

Three structural mismatches, each load-bearing:

1. **Index type.** Mathlib gives `Fin n` — an anonymous index of unknown
   cardinality, obtained existentially. `all_parts : Finset (Partition n)`
   needs the blocks indexed **by partitions of n**. Identifying the simple
   modules of `H_n(q)` with partitions is Dipper–James / Hoefsmit and is **not
   in Mathlib**; the corpus's own `SpechtDimension` docstring says the SYT count
   is awaited "when it lands".
2. **Existential, not constructive.** Extracting `pi_lambda` requires
   `Classical.choice` on a witness that carries no partition labelling, so the
   resulting idempotents cannot be *named* by λ — which is the whole point of
   the class.
3. **Semisimplicity is itself a hypothesis.** `[IsSemisimpleRing R]` is
   required, and the corpus's route to it,
   [`QOU/MathlibExt/HeckeGenericSemisimple.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/HeckeGenericSemisimple.lean)`::isSemisimpleRing_of_qGeneric`,
   is hypothesis-carrying by design: it takes
   `hgram : (∀ x, (∀ y, regTraceForm K A x y = 0) → x = 0) ↔ qFactorial q n ≠ 0`,
   which its own docstring calls "the one thing the concrete Iwahori–Hecke
   construction … must still supply". That is the Schur-element /
   Gram-determinant identity. **It is the wall, and it is a real one.**

## 3. And it would not have mattered — the class is satisfied by `ℚ`

This is the finding that decides the branch, and it is machine-checked:
[`QOU/Hecke/WedderburnRankDegeneracy.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/WedderburnRankDegeneracy.lean)
constructs a complete `WedderburnDecomp (R := ℚ) n 1 ℚ` **at every n**, on the
**one-dimensional** algebra `ℚ`. Every field is the class's genuine equation,
discharged: `idempotent`, `orthogonal`, `central`, `complete`, `trace_decomp`.

```
'QOU.Hecke.RankOneDegeneracy.rankOneWedderburn'
    depends on axioms: [propext, Classical.choice, Quot.sound]
'QOU.Hecke.RankOneDegeneracy.wedderburnDecomp_does_not_pin_rank'
    depends on axioms: [propext, Classical.choice, Quot.sound]
```

The headline pairs the two halves:

```lean
theorem wedderburnDecomp_does_not_pin_rank {n : ℕ} (hn : 2 ≤ n) :
    Nonempty (WedderburnDecomp (R := ℚ) n 1 ℚ) ∧ ¬ IsHeckeOfFullRank ℚ n ℚ
```

**Mechanism.** `WedderburnDecomp` takes `[HeckeAlgebra R n q A]`, and
`QOU.Hecke.InstanceH2.rankOneModel` inhabits *that* class at every n with
`A = R = ℚ`, `q = 1`, `embed := fun _ => 1`. PR #4857 found this degeneracy and
repaired it for `HeckeAlgebra` by adding `IsHeckeOfFullRank`, whose whole
purpose is to exclude the rank-one model. `WedderburnDecomp` never picked that
companion up, so it inherits the hole through its own hypothesis.

**Non-degeneracy of the witness itself.** The three tests the branch was
required to run, and their results:

| test | result |
|---|---|
| **PUnit test** — is the construction satisfiable by `PUnit`/`True`? | Passes, and is *stronger*: the carrier is `ℚ`, which is `Nontrivial`. No `Prop`-variable field, no `True`, no `PUnit`. It is not the `triv_wedderburn` pattern. |
| **Wrong-value test** — does the class accept a concretely wrong decomposition? | **It does, and that is the finding.** A single idempotent `π_λ = [λ = λ₀]` over a 1-dimensional algebra satisfies every field at n = 6, where `H_6(q)` has 720 dimensions and 11 partitions. |
| **Delete-the-lemma test** — remove the load-bearing input; does it still construct? | **It does.** `trace_decomp` was proved over an *arbitrary* index type and an *arbitrary* family summing to `1` — no idempotency, orthogonality, centrality, or Hecke structure. So `trace_decomp` is a consequence of `complete` at `y_lambda := 1`. |

The third row is **not new** and is reported as a re-confirmation:
[`QOU/QBeta/WedderburnTraceDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WedderburnTraceDecomposition.lean)
already records it ("completeness **alone** gives the *unweighted*
`tr x = Σ_λ tr(x π_λ)`. This much is free"), and
`Hecke/Wedderburn.trace_exhaustive` proves the same thing inside the defining
file. What follows from it is that `y_lambda` is **unconstrained** — it appears
in no field but `trace_decomp`.

## 4. The "ten modules" figure is not supported; the real number is zero

Measured over `content/**/lean/QOU`:

| measurement | count | which |
|---|---|---|
| files mentioning `WedderburnDecomp` at all | 4 | `Hecke/Wedderburn.lean` (defines it), `Hecke.lean` (index line 22), `BraidsAndKnots/BorromeanCanonicalTraceDerivation.lean` (docstring, 32/44), `QBeta/WedderburnTraceDecomposition.lean` (defect-report prose) |
| files carrying `[WedderburnDecomp …]` as a **hypothesis binder** outside the defining file | **0** | — |
| files importing `QOU.Hecke.Wedderburn` | 2 | `Hecke.lean`, `Hecke/Hoefsmit.lean` |

So there is no set of ten modules gated on this class, and no module that an
instance would convert from conditional to unconditional. The
`trace_decomposition` hit in `Braiding/hecke_mass_trace.lean:77` is a different
object — a `claim_trace_decomposition` context field, itself a self-assuming
projection (`:106` is `⟨ctx.claim_…, ctx.claim_…⟩`).

## Scope of the negative

Per AGENTS.md §"Before declaring refuted", this is a **structural exclusion
(b)**, and the invariant is a dimension count: `Module.finrank ℚ ℚ = 1` against
`n! ≥ 2` for `n ≥ 2`, recorded as `rankOne_finrank_ne_factorial`.

What is excluded: **"an instance of the class as it currently stands is worth
building"**. What is **not** excluded, and remains open exactly as before: the
Wedderburn decomposition of `H_n(q)` itself; the existence and uniqueness of the
Ocneanu weights (Wedderburn–Artin existence + Schur orthogonality, Mathas 1999
§3.43); and the Gram-determinant identity that would discharge
`isSemisimpleRing_of_qGeneric`'s `hgram`. Every field of `WedderburnDecomp` is a
true and meaningful sentence about a genuine decomposition — the claim here is
only that **the fields do not together pin down the algebra**.

## What would have to change, in order

1. Pair the class with the rank predicate at every hypothesis site
   (`[IsHeckeOfFullRank R n A]`), or make `WedderburnDecomp` extend it.
2. Add the `block_scaling` field `tr(x · π_λ) = y_λ · χ_λ(x)` — the sentence
   already in the class docstring but absent from its fields — and delete
   `trace_decomp`, per `qou-luq7` items 1–2.
3. Only then construct an instance; and the first honest one will be at
   **n = 3**, off the sorry-free `wedderburn₃` in
   `QOU/Machinery/HeckeH3Wedderburn.lean`, not at general n.

Tracked: `qou-hah4`.

## A separate defect found while disambiguating the name

Three distinct objects share the `WedderburnDecomp*` name:

1. `QOU.Hecke.WedderburnDecomp` — `QOU/Hecke/Wedderburn.lean:72`. Class, nine
   genuine-Prop fields. The subject of this document.
2. `QOU.Mathlib.HeckeAlgebra.WedderburnDecomposition` —
   `QOU/Mathlib/HeckeAlgebra.lean:118`. `Prop`-**variable** fields
   (`blocks_sum_to_one : Prop` + `blocks_sum_holds`), filled with `True` by
   `instance triv_wedderburn` at `:166` over `block_proj _ := PUnit.unit`.
   Worse than previously recorded: `instance triv_hecke` at `:151` *also*
   globally registers `IwahoriHeckeAlgebra R n q` with `carrier := PUnit`, so
   even a genuine instance of the Wedderburn class there would be shadowed by
   typeclass search. Tracked: `qou-6dzi`.
3. `QOU.HeckeAlgebra.Wedderburn.WedderburnDecomposition` —
   `QOU/HeckeAlgebra/Wedderburn.lean:68`. Not a class:
   `abbrev … : Type := ∀ (lam : Nat.Partition n), Matrix …`. Carries
   `axiom wedderburnEmbed` at `:110`.

This finding was cited to the branch as bean `qou-h56b`, **which does not
exist** (`beans show` → "bean not found"; grep over `.beans/` for
`triv_wedderburn` → zero files). The code is real and verified above; only the
bean reference was phantom, and `qou-6dzi` now records it under an ID that
resolves.

## Verification

- `lean`-direct **exit 0** on `QOU/Hecke/WedderburnRankDegeneracy.lean`, built
  against its real import cone (`QOU.Hecke.Wedderburn` + `QOU.Hecke.FullRank`,
  both rebuilt from this branch's source into a `/tmp` addon overlay — the
  shared `.lake` was read-only throughout and no `lake build` was run).
- `#print axioms` on all six new declarations: `[propext, Classical.choice,
  Quot.sound]`. No `sorryAx`.
- `grep -nE "sorry|native_decide|axiom|: True|:= trivial"` on the new module:
  **3 hits, all docstring prose** (lines 12, 86, 112 — one of them the sentence
  *asserting the absence* of what the pattern matches). Zero real occurrences.
- The stale-olean hazard was live and was caught: the shared `.lake` olean for
  `QOU.Hecke.Wedderburn` predates the `central` field now in source, and an
  early probe errored `` `central` is not a field ``. Every result above is
  against oleans rebuilt from this branch's source.
