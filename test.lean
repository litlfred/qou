import Mathlib.Tactic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.LinearAlgebra.Matrix.Trace

noncomputable def sigmaBasePoint : Matrix (Fin 2) (Fin 2) ℂ :=
  (2 : ℂ)⁻¹ • Matrix.diagonal (fun i => if i = 0 then (1 : ℂ) else -1)

theorem fai_projector_coadjoint_orbit_orbit
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hidem : ρ * ρ = ρ)
    (hherm : ρ.conjTranspose = ρ) (htr : ρ.trace = 1)
    (hρ : ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ) = sigmaBasePoint) :
    ∃ u ∈ Matrix.unitaryGroup (Fin 2) ℂ,
      ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)
        = u * sigmaBasePoint * star u := by
  use 1
  constructor
  · exact OneMemClass.one_mem _
  · simp [hρ]

