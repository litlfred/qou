import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.QuantumObservableUniverses.QSchurWeyl

/-!
# QOU.SchurWeyl.HeckeWedderburnDataGeneral — `HeckeWedderburnData` at every `n`

`HeckeWedderburnData` (`QSchurWeyl.lean`) is the structure the R2 results consume: a
partition-indexed Wedderburn isomorphism together with a Markov trace realised as the weighted
character sum `tr_M = Σ_λ w_λ χ_λ`.  Only `HeckeWedderburnData3` existed, at `n = 3`.

`heckeWedderburn` (SW-7) supplies the isomorphism at **every** `n`, so the structure can now be
built at every `n` — after reindexing each block from `SYT λ` to `Fin d_λ`, which is what the
structure's `Matrix (Fin (dim l))` field asks for.

## What is honestly delivered, and what is not

The **weights are a parameter of this construction, not a result of it.**  Given *any* family
`w : λ ↦ ℝ`, the functional `Σ_λ w_λ χ_λ` is well defined and `markov_eq` holds by `rfl` — it is a
definition, not a theorem.  So this file delivers the *structural* half of SW-8 at general `n`: the
partition-indexed block decomposition, in the packaging downstream results consume.

It does **not** deliver a Markov trace.  What makes a weight family the *Ocneanu* one is the pair of
properties `tr(xy) = tr(yx)` and the Markov condition `tr(x·σ_n) = z·tr(x)`, and those single out a
specific `w_λ(q, z)`.  At `n = 3` those are proved (`HeckeMarkov3.markovWeights_markov_σ1`); at
general `n` they are open, and nothing here should be read as closing them.  Instantiating the
structure with an arbitrary `w` would let a downstream consumer *call* the result a Markov trace
without it being one — so the naming below keeps `weight` visibly a parameter.

## Base ring (§7c)

Same inherited-`ℝ` case as `HeckeProductSurjective`: every `ℝ` here comes from `heckeWedderburn`,
hence from `seminormalRep`, which is `ℝ`-only because `OffDiagNonvanishing.sq_geom_lt` is an
inequality in an *ordered* field.  `check-sidecars.sh` flags it as "likely gratuitous" because the
archimedean construct is one import away rather than in this file; the suggested generalisation to
`[Field R]` is impossible, not merely unnecessary.  Checker gap tracked as `qou-9e7p`.

LaTeX label: `def:hecke-wedderburn-data-general`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

/-- Reindex every block from its `SYT` index to `Fin d_λ`, the shape `HeckeWedderburnData` wants. -/
noncomputable def blockFinReindex (n : ℕ) :
    (∀ lam : Partition (n + 1),
        Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
          (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ)
      ≃ₐ[ℝ] (∀ lam : Partition (n + 1),
        Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) :=
  AlgEquiv.piCongrRight fun lam =>
    Matrix.reindexAlgEquiv ℝ ℝ (Fintype.equivFin (StandardYoungTableau
      (QOU.Mathlib.partitionShape lam)))

/-- The Wedderburn isomorphism in `HeckeWedderburnData`'s indexing. -/
noncomputable def heckeWedderburnFin (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Hecke ℝ q q⁻¹ n ≃ₐ[ℝ]
      (∀ lam : Partition (n + 1), Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) :=
  (heckeWedderburn q hq0 hq2 n).trans (blockFinReindex n)

/-- **`HeckeWedderburnData` for `H_{n+1}(q)`, at every `n`.**

The weight family `w` is an **input**.  `markov_eq` is true by `rfl`, because `markov` is *defined*
as the weighted character sum — so this packages the block decomposition and says nothing about
which `w` makes the functional a Markov trace.  See the module docstring. -/
noncomputable def heckeWedderburnDataOfWeights (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (w : Partition (n + 1) → ℝ) :
    HeckeWedderburnData ℝ (Partition (n + 1)) (Hecke ℝ q q⁻¹ n) where
  dim := dLambda
  weight := w
  iso := heckeWedderburnFin q hq0 hq2 n
  markov := fun h => ∑ l, w l * ((heckeWedderburnFin q hq0 hq2 n h) l).trace
  markov_eq := fun _ => rfl

end QOU.SchurWeyl
