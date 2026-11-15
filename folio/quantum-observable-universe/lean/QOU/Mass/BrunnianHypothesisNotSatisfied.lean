/-
Copyright (c) 2026 litlfred. All rights reserved.

# `CrossingModel.NoIsolatedPairEnergy` is NOT satisfied by the L6a4 carrier — and the corpus already proves it

`QOU.Mass.CrossingModelPairLocality` defines

    def Brunnian : Prop := ∀ i j, C.w2 i j = 0

— *"a pair measured in isolation carries no mutual energy"* — and its docstring
adds: *"(`QOU.Mass.BrunnianBindingChannel` establishes that the ³He/⁴He carrier
`L6a4` has this property.)"*

**That cross-reference is false, and the cited file proves the opposite.**
`BrunnianBindingChannel` establishes that L6a4 has vanishing pairwise **Gauss
linking number** (`n₊ = n₋`), and then proves — `brunnian_binding_survives`,
sorry-free — that the mutual energy of such a pair is **strictly positive**:

    0 < countChannel m m q     for  0 < m,  1 < q

Its own docstring says so in as many words: *"the mutual energy is nonzero even
though the pairwise linking number is zero. This is the crux of `qou-brng`'s
surviving route."*  The whole point of that file is that binding **survives**
the Brunnian vanishing.

So there are two distinct properties sharing one name:

| name | condition | true of L6a4? |
|---|---|---|
| topological Brunnian | pairwise linking number `= 0`, i.e. `n₊ = n₋` | **yes** |
| `CrossingModel.NoIsolatedPairEnergy` | pairwise mutual *energy* `w₂ = 0` | **no** |

and the corpus proves the first does **not** imply the second.  `QOU/Mass/`
currently carries **three** unrelated `Brunnian` definitions
(`CrossingModelPairLocality`, `MilnorIndeterminacyGate`, and
`FreedmanHeGenusHandleNeedsVanishingLinking.BrunnianAt`), which is how the
conflation survives reading.

## What this costs downstream

`b3_eq_neg_tripleMutual_of_brunnian` — *"with a Brunnian carrier the pair terms
vanish, so the whole of `b₃` is the irreducibly three-body channel"* — is a
correct theorem whose **hypothesis L6a4 does not satisfy**.  It therefore does
not license reading the measured `b₃` as a clean measurement of the triple
channel; the pair contamination it discards is not zero.

The same misreading is committed to a witness:
`computations/probes/pair-locality-shortfall.witness.json` asserts in its
`description` that *"With a Brunnian carrier the pair terms vanish and b3 is
exactly the triple channel"* — while recording, in the same file,
`b₂ = 2.2245662` MeV.  A nonzero `b₂` refutes `CrossingModel.NoIsolatedPairEnergy` outright,
by exactly the contrapositive the corpus already uses one theorem over for `b₃`.

## What is here

Two theorems, mirroring `not_pairLocal_of_b3_ne_zero` one hypothesis down.
Neither refutes anything in `CrossingModelPairLocality`: every theorem there
remains true.  What they establish is that this particular hypothesis is not
available for this particular carrier.

§7c: `not_brunnian_of_pair_binding_ne_zero` is over a generic `CommRing`; the
count-channel bridge needs `ℝ` because `countChannel` and the ordering `1 < q`
are archimedean.  Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md
-/
import QOU.Mass.CrossingModelPairLocality
import QOU.Mass.BrunnianBindingChannel

namespace QOU.Mass.BrunnianHypothesisNotSatisfied

open QOU.Mass.CrossingModelPairLocality QOU.Mass.BrunnianBindingChannel

variable {R : Type*} [CommRing R]

/-- **The data-side refutation: a nonzero pair binding refutes `Brunnian`.**

AME2020 measures `b₂ = 2.2245662` MeV
(`computations/probes/pair-locality-shortfall.witness.json`), and the pair
cumulant of the induced binding map is `−w₂`.  So the measured two-body channel
refutes `CrossingModel.NoIsolatedPairEnergy` on the physical carrier — the same move
`not_pairLocal_of_b3_ne_zero` makes for the three-body channel, one hypothesis
down. -/
theorem not_noIsolatedPairEnergy_of_pair_binding_ne_zero {C : CrossingModel R} {i j : Fin 4}
    (h : C.toBindingMap.pair i j ≠ 0) : ¬ C.NoIsolatedPairEnergy := by
  intro hB
  exact h (by rw [CrossingModel.toBindingMap_pair, hB i j, neg_zero])

/-- **The structure-side refutation: a crossing pair at `q > 1` refutes `Brunnian`.**

If a pair's isolated mutual energy is the count channel of a topologically
Brunnian pair — which is exactly what `brunnian_energy_is_count_channel` says it
is, the signed channel being empty — then for any actual crossing (`0 < m`) at a
substrate modulus `q > 1` that energy is strictly positive, so `w₂ ≠ 0`.

L6a4 is a crossing pair: its six crossings distribute two to each component pair,
with `n₊ = n₋ = 1`, so `m = 1 > 0`.  Hence `CrossingModel.NoIsolatedPairEnergy` fails for it
on structural grounds alone, with no appeal to data. -/
theorem not_noIsolatedPairEnergy_of_countChannel {C : CrossingModel ℝ} {i j : Fin 4}
    {m : ℕ} {q : ℝ} (hm : 0 < m) (hq : 1 < q)
    (hw : C.w2 i j = countChannel m m q) : ¬ C.NoIsolatedPairEnergy := by
  intro hB
  have hpos : 0 < countChannel m m q := brunnian_binding_survives m hm q hq
  rw [hB i j] at hw
  exact absurd hw.symm (ne_of_gt hpos)

/-- **The two refutations agree**, which is the point worth recording: the
structural route (a crossing pair has positive count-channel energy) and the
empirical route (AME measures `b₂ ≠ 0`) independently deny the same hypothesis.
Stated as the contrapositive: a `Brunnian` model has BOTH a vanishing pair
binding and no crossing-pair count-channel energy. -/
theorem noIsolatedPairEnergy_forces_both {C : CrossingModel ℝ} (hB : C.NoIsolatedPairEnergy) (i j : Fin 4) :
    C.toBindingMap.pair i j = 0 ∧ C.w2 i j = 0 :=
  ⟨by rw [CrossingModel.toBindingMap_pair, hB i j, neg_zero], hB i j⟩

end QOU.Mass.BrunnianHypothesisNotSatisfied
