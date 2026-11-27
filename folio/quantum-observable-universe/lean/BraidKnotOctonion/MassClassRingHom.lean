import BraidKnotOctonion.MassTraceMarkovClass

set_option autoImplicit false

/-!
# The braid-class mass is natural in the ground ring

Bean `qou-5o1v` (constructive item 2.1). Owner ruling 2026-11-27: *mass is valued in the ring*.
`def:mass-identity` defines the mass of a braid class as the framing-corrected trace
`massClass : BraidClass → R`, an element of the ground ring `R` (for example `ℚ(q)`), with no norm.

This file proves that every comparison of that mass with a number is a ring homomorphism applied
after the mass has been computed, never a change of the mass itself:

* `rCheck_map`, `embedPair_map`, `strandBraid_map`, `transport_map`, `hol_map`,
  `siteWeight_map` — the R-matrix, its two-site embedding, the crossing transports, the discrete
  multiplicative integral `hol` and the site weight `K^{⊗n}` are all defined by formulas in
  `q`, `q⁻¹` and the weight, so a ring homomorphism `φ : R →+* S` carries each one to the same
  object built from `φ q`, `φ q⁻¹`, `φ ∘ w`.
* `map_massClass` (**naturality of the mass**) — for every braid class `c`,
  `φ (massClass_R c) = massClass_S c`, where the right side is built from the images of the
  parameters. Specialising `φ` to evaluation at a point, an embedding of a number field into an
  ordered field, or a residue map gives the corresponding comparison; the mass is computed once,
  in `R`.

Absolute values and logarithms appear nowhere here. They belong to the comparison layer
(`QOU/Transcendental/MassTheory/MassComparison.lean`). No numerical value of `q` enters.

**Base ring (§7c).** `R` and `S` are arbitrary commutative rings; inverses are carried as `qi`,
`wi` with witnessing equations, which `φ` transports.
-/

namespace QOU.Torsion.MassClassRingHom

open QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.JonesNormalisation QOU.MathlibExt.SkeinRelation
open QOU.Torsion.MassTraceMarkov QOU.Torsion.MassTraceMarkovClass

variable {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S) (q qi wi : R)

/-! ## The building blocks are natural -/

/-- `φ` carries the R-matrix `Ř(q, qi)` to `Ř(φ q, φ qi)`. -/
theorem rCheck_map : φ.mapMatrix (rCheck q qi) = rCheck (φ q) (φ qi) := by
  ext a b
  simp only [RingHom.mapMatrix_apply, Matrix.map_apply, rCheck, Matrix.of_apply]
  split_ifs <;> simp [map_sub]

/-- `φ` commutes with the two-site embedding into `V^{⊗n}`. -/
theorem embedPair_map {n : ℕ} (i j : Fin n) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    φ.mapMatrix (embedPair i j M) = embedPair i j (φ.mapMatrix M) := by
  ext a b
  simp only [RingHom.mapMatrix_apply, Matrix.map_apply, embedPair_apply]
  split_ifs <;> simp

/-- `φ` carries the braiding of strand `a` to the braiding built from `φ q`, `φ qi`. -/
theorem strandBraid_map {m : ℕ} (a : Fin m) :
    φ.mapMatrix (strandBraid q qi a) = strandBraid (φ q) (φ qi) a := by
  simp only [strandBraid, braidAt, embedPair_map, rCheck_map]

/-- `φ` carries the transport of a letter to the transport built from `φ q`, `φ qi`. -/
theorem transport_map {m : ℕ} (ℓ : Fin m × Bool) :
    φ.mapMatrix (transport q qi ℓ) = transport (φ q) (φ qi) ℓ := by
  unfold transport
  split_ifs
  · exact strandBraid_map φ q qi ℓ.1
  · rw [← strandBraid_map φ q qi ℓ.1]
    ext a b
    simp only [negCrossing, RingHom.mapMatrix_apply, Matrix.map_apply, Matrix.sub_apply,
      Matrix.algebraMap_matrix_apply, Algebra.algebraMap_self, RingHom.id_apply]
    split_ifs <;> simp [map_sub]

/-- **The discrete multiplicative integral is natural.** -/
theorem hol_map {m : ℕ} (ℓs : List (Fin m × Bool)) :
    φ.mapMatrix (hol q qi ℓs) = hol (φ q) (φ qi) ℓs := by
  induction ℓs with
  | nil => simp
  | cons ℓ ℓs ih => rw [hol_cons, hol_cons, map_mul, ih, transport_map]

/-- The site weight `∏ₘ w(aₘ)` is natural. -/
theorem siteWeight_map {n : ℕ} (w : Fin 2 → R) :
    φ.mapMatrix (siteWeight (n := n) w) = siteWeight (φ ∘ w) := by
  ext a b
  simp only [RingHom.mapMatrix_apply, Matrix.map_apply, siteWeight, Matrix.diagonal_apply]
  split_ifs <;> simp [map_prod]

/-- The matrix trace is natural. -/
theorem trace_map {ι : Type*} [Fintype ι] [DecidableEq ι] (M : Matrix ι ι R) :
    φ (Matrix.trace M) = Matrix.trace (φ.mapMatrix M) := by
  simp [Matrix.trace, map_sum]

/-! ## The two framing units are natural -/

/-- `φ` sends an integer power of a unit to the same power of its image. -/
theorem map_val_zpow (u : Rˣ) (k : ℤ) :
    φ ((u ^ k : Rˣ) : R) = ((Units.map (φ : R →* S) u ^ k : Sˣ) : S) := by
  rw [← map_zpow, Units.coe_map]
  rfl

theorem units_map_writheFactor (hqi : q * qi = 1) (hqi' : φ q * φ qi = 1) :
    Units.map (φ : R →* S) (writheFactor q qi hqi) = writheFactor (φ q) (φ qi) hqi' := by
  ext
  simp [writheFactor, qUnit]

/-! ## Naturality of the mass -/

/-- **The braid-class mass is natural in the ground ring.** For a ring homomorphism
`φ : R →+* S` and every braid class `c`, applying `φ` to the mass computed over `R` gives the mass
computed over `S` from the images of `q`, `q⁻¹`, `(1 + q²)⁻¹` and the weight.

So a comparison of the ring-valued mass with a number (evaluation at a point, an embedding into an
ordered field) is a ring homomorphism applied to one ring element; it does not enter the
definition. -/
theorem map_massClass (hqi : q * qi = 1) (w : Fin 2 → R) (hw : (1 + q ^ 2) * wi = 1)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) (c : BraidClass) :
    φ (massClass q qi wi hqi w hw h0 h1 c)
      = massClass (φ q) (φ qi) (φ wi)
          (by rw [← map_mul, hqi, map_one]) (φ ∘ w)
          (by rw [← map_pow, ← map_one φ, ← map_add, ← map_mul, hw])
          (by simp [h0]) (by simp [h1]) c := by
  obtain ⟨m, ℓs, rfl⟩ := exists_word_of_braidClass c
  rw [massClass_wordBraid, massClass_wordBraid]
  simp only [map_mul, map_pow, Units.val_pow_eq_pow_val, val_strandFactor, map_add, map_one]
  rw [map_val_zpow, units_map_writheFactor φ q qi hqi (by rw [← map_mul, hqi, map_one]),
    trace_map, (φ.mapMatrix).map_mul, siteWeight_map, hol_map]

end QOU.Torsion.MassClassRingHom
