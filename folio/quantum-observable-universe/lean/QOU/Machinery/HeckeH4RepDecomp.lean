import QOU.Machinery.HeckeH4Wedderburn
import QOU.Machinery.BilinearTraceRepBasis

/-!
# The five `H₄(q)` Wedderburn blocks as a `BilinearTrace` representation family

`BilinearTraceRepBasis.gram_symm_of_rep_decomp_of_basis` turns a *basis-level*
trace decomposition into Gram symmetry, hence (via `cyclic_of_gram_symm`) into
cyclicity of the Markov trace. To apply it at `H₄` one needs the five Wedderburn
blocks packaged as a single family

  `ρ : ∀ l, (Fin 24 → K) → Matrix (dim l) (dim l) K`

that is **multiplicative on `mulNF₄`** and **linear** in the coordinate vector.

Both come for free from `wedderburnHom₄`, and that is the point of this file.
It is an `AlgHom` out of `H4A K (q - q⁻¹)`, whose `Add`/`SMul`/`Mul` instances
are coordinatewise on the `.v` field and whose components are exactly
`chiNF₄ q`, `chiNF₄ (-q⁻¹)`, `blockOf22 q`, `blockOf31 q`, `blockOf211 q`
**by `rfl`** (`wedderburnHom₄_apply`). So `map_mul` / `map_add` / `map_smul`
discharge every structural obligation with no fresh computation on the 24-word
normal form.

This route also sidesteps a real obstacle: the per-block linearity lemmas
`blockOf22_add`, `blockOf22_smul` (and their `31` / `211` counterparts) are
`private`, hence unusable from any other file. Re-deriving them here would mean
editing the block-map modules — measured here at 941 s / 5.5 GB and 916 s /
6.5 GB, so the expensive thing to touch.

## What is NOT here

The **24 scalar identities** `trM4 z (q - q⁻¹) (e i) = ∑_λ w_λ · tr (ρ_λ (e i))`
at the closed-form Markov weights. That is the arithmetic content of the
decomposition and it is genuinely open in Lean; it is carried below as an
explicit hypothesis (`hbasis`) rather than assumed, so the conditional result is
honest about what it rests on.

**This is not the route that retired the ASCII chain.** `QOU/Machinery/
H4Cyclicity.lean` proved `trM4_cyclic` from the generator actions, the chain has
since been deleted, and its cone is under 10 minutes. What this file offers is a
*second, structurally different* route to the same Gram symmetry — via the
Wedderburn blocks rather than the generators — which is worth having only on
its own merits, not because anything depends on it.

Base ring (§7c): generic `[Field K]` — inherited from `wedderburnHom₄`, which
needs inverses for `-q⁻¹`. No ordering and no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [leitner2026] bean `qou-x64l`, step 4.
-/

namespace QOU.Machinery.H4

open QOU.Machinery.BilinearTrace

variable {K : Type*} [Field K]

/-- The five Wedderburn blocks of `H₄(q)`, indexed by the partitions of 4 that
survive: `(4)`, `(3,1)`, `(2,2)`, `(2,1,1)`, `(1,1,1,1)`. -/
inductive Block where
  | four | threeOne | twoTwo | twoOneOne | oneOneOneOne
  deriving DecidableEq

/-- Block dimensions `1, 3, 2, 3, 1` — the `∑ d² = 24` of the rank-4
Wedderburn decomposition. -/
abbrev Block.dim : Block → Type
  | .four => Fin 1
  | .threeOne => Fin 3
  | .twoTwo => Fin 2
  | .twoOneOne => Fin 3
  | .oneOneOneOne => Fin 1

instance (l : Block) : Fintype l.dim := by cases l <;> infer_instance

instance : Fintype Block := ⟨{.four, .threeOne, .twoTwo, .twoOneOne, .oneOneOneOne}, by
  intro l; cases l <;> decide⟩

/-- A scalar as a `1 × 1` matrix — the carrier of the two one-dimensional
characters. -/
def scalarBlock (a : K) : Matrix (Fin 1) (Fin 1) K := Matrix.of fun _ _ => a

@[simp] theorem scalarBlock_trace (a : K) : (scalarBlock a).trace = a := by
  simp [scalarBlock, Matrix.trace_fin_one]

@[simp] theorem scalarBlock_mul (a b : K) :
    scalarBlock a * scalarBlock b = scalarBlock (a * b) := by
  ext i j; fin_cases i; fin_cases j
  simp [scalarBlock, Matrix.mul_apply]

/-- The five blocks as one representation family on the NF coordinate vector. -/
noncomputable def rho (q : K) : ∀ l : Block, (Fin 24 → K) → Matrix l.dim l.dim K
  | .four => fun v => scalarBlock (chiNF₄ q v)
  | .threeOne => fun v => blockOf31 q v
  | .twoTwo => fun v => blockOf22 q v
  | .twoOneOne => fun v => blockOf211 q v
  | .oneOneOneOne => fun v => scalarBlock (chiNF₄ (-q⁻¹) v)

section Structural

variable (q : K)

-- The Wenzl genericity hypotheses are bound explicitly in each statement below
-- rather than as section variables: they appear only in the proofs, so
-- auto-inclusion leaves them out of the signature (and silently shifts `l`
-- into the slot the call sites pass `hq` in).

/-- Packaging a coordinate vector as an `H4A` element. -/
private def wrap (h : K) (v : Fin 24 → K) : H4A K h := ⟨v⟩

/-- **Multiplicativity.** Each block is multiplicative on `mulNF₄`, because
`wedderburnHom₄` is an `AlgHom` and `H4A`'s multiplication *is* `mulNF₄` on the
coordinate field. -/
theorem rho_mul (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (l : Block) (u v : Fin 24 → K) :
    rho q l (mulNF₄ (q - q⁻¹) u v) = rho q l u * rho q l v := by
  have hmul := map_mul (wedderburnHom₄ q hq h2 h3) (wrap (q - q⁻¹) u) (wrap (q - q⁻¹) v)
  simp only [wedderburnHom₄_apply] at hmul
  cases l
  · have := congrArg (fun p => p.1) hmul
    simpa [rho, wrap, scalarBlock_mul] using congrArg scalarBlock this
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.1) hmul
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.1) hmul
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.2) hmul
  · have := congrArg (fun p => p.2.1) hmul
    simpa [rho, wrap, scalarBlock_mul] using congrArg scalarBlock this

/-- **Additivity**, from `map_add` on the same `AlgHom`. -/
theorem rho_add (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (l : Block) (u v : Fin 24 → K) :
    rho q l (u + v) = rho q l u + rho q l v := by
  have hadd := map_add (wedderburnHom₄ q hq h2 h3) (wrap (q - q⁻¹) u) (wrap (q - q⁻¹) v)
  simp only [wedderburnHom₄_apply] at hadd
  cases l
  · have := congrArg (fun p => p.1) hadd
    ext i j; fin_cases i; fin_cases j; simpa [rho, wrap, scalarBlock] using this
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.1) hadd
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.1) hadd
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.2) hadd
  · have := congrArg (fun p => p.2.1) hadd
    ext i j; fin_cases i; fin_cases j; simpa [rho, wrap, scalarBlock] using this

/-- **Homogeneity**, from `map_smul` on the same `AlgHom`. -/
theorem rho_smul (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (l : Block) (c : K) (v : Fin 24 → K) :
    rho q l (c • v) = c • rho q l v := by
  have hsm := map_smul (wedderburnHom₄ q hq h2 h3) c (wrap (q - q⁻¹) v)
  simp only [wedderburnHom₄_apply] at hsm
  cases l
  · have := congrArg (fun p => p.1) hsm
    ext i j; fin_cases i; fin_cases j; simpa [rho, wrap, scalarBlock] using this
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.1) hsm
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.1) hsm
  · simpa [rho, wrap] using congrArg (fun p => p.2.2.2.2) hsm
  · have := congrArg (fun p => p.2.1) hsm
    ext i j; fin_cases i; fin_cases j; simpa [rho, wrap, scalarBlock] using this

end Structural

/-! ## The conditional cyclicity statement

Everything structural is discharged above. What remains is arithmetic: the 24
scalar identities pinning `TRM4` against the block traces at the Markov weights.
Those are carried as `hbasis` — an explicit hypothesis, not an assumption
dressed up as a proof — so the statement below is a genuine conditional result
and names exactly what `qou-x64l` step 4 still owes. -/

/-- **Gram symmetry of `trM4` from the Wedderburn blocks, conditional on the
basis-level Markov decomposition.**

Given the 24 scalar identities `hbasis`, the level-4 Markov trace is
Gram-symmetric on the subscript normal-form basis — with no reference to the
ASCII presentation and no 576-entry closure. -/
theorem trM4_gram_symm_of_markov_basis (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (z : K) (w : Block → K)
    (hbasis : ∀ i, trM4 z (q - q⁻¹) (e (R := K) i)
      = ∑ l ∈ (Finset.univ : Finset Block), w l * (rho q l (e (R := K) i)).trace)
    (i j : Fin 24) :
    trM4 z (q - q⁻¹) (mulNF₄ (q - q⁻¹) (e (R := K) i) (e (R := K) j))
      = trM4 z (q - q⁻¹) (mulNF₄ (q - q⁻¹) (e (R := K) j) (e (R := K) i)) :=
  gram_symm_of_rep_decomp_of_basis (mulNF₄ (q - q⁻¹)) (trM4 z (q - q⁻¹))
    Finset.univ w (rho q)
    (fun l u v => rho_mul q hq h2 h3 l u v)
    (fun u v => trM4_add z (q - q⁻¹) u v)
    (fun c v => trM4_smul z (q - q⁻¹) c v)
    (fun l u v => rho_add q hq h2 h3 l u v)
    (fun l c v => rho_smul q hq h2 h3 l c v)
    hbasis i j

end QOU.Machinery.H4
