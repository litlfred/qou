import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.BWVacuumRowIsHecke — the keystone value step, categorical

The s5-so3 keystone value map collapsed to one vector `bwS0(λ) = d_q(λ)/D`.
After all four *geometric/analytic* realisation routes were source-refuted —
Σ(2,3,5) (golden, D=2), Σ(3,4,5) (D=6), colored Lawrence–Rozansky residues
(pure ±1 sign), and the q-Bessel family (Tricomi + Hahn–Exton/q-Hankel, using
the Koornwinder–Swarttouw Plancherel kernel) — the standing resolution of the
value step is **redirect (iii)**, the *compact categorical* answer:

    S_{0λ} / S_{00} = d_q(λ).

This file formalises that identity sorry-free. It is the **what**, and it is
near-definitional (the vacuum row of a modular S-matrix is, by construction, the
normalised quantum-dimension vector).

**The non-geometric "why".** Why *this* vector is the selected one — not another
— does not need geometry. It is the **Markov-trace uniqueness / Perron–Frobenius
selection** (Ocneanu; Wenzl): the quantum dimensions are the *unique* positive
block weights making the trace a **Markov trace** (stable under adding a strand),
equivalently the Perron–Frobenius eigenvector of the fusion/branching matrix
under state positivity (the confinement-SDP PSD constraint). That selection is
already in the corpus:
`mass-theory/y-lambda-closed-form-wenzl-bridge.md`,
`mass-theory/wenzl-bridge-applicability-qou.lean`,
`stochastic-mechanics/intro-markov-axioms-braid-link.md`. So the
geometric-realisation program was a *redundant second* "why"; its exhaustion
leaves the value step fully explained.

Audit:
`docs/audits/2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md`;
ledger `docs/coordination/s5-so3-keystone.md`.

**Base ring (§7c).** The identity is pure algebra (a ratio in a field); stated
over a generic `{R : Type*} [Field R]`, no ℝ — the archimedean `q₀` evaluation
of the balanced q-integers `d_q ∈ {[1],[4],[5],[4][3]/[2]}` happens downstream,
past the substrate→archimedean wall.
-/

namespace QOU.BraidKnot

/-- A modular S-matrix **vacuum row** over a fusion-label type `ι`: the entries
    are the quantum dimensions `d` normalised by the total quantum dimension `D`,
    with a distinguished vacuum label `vac` of quantum dimension `1`.  `D` is
    carried abstractly (its value `√(Σ_λ d_λ²)` is archimedean and lives
    downstream); only `D ≠ 0` is used here. -/
structure VerlindeVacuumRow (ι : Type*) (R : Type*) [Field R] where
  /-- Quantum dimension of each fusion block. -/
  d : ι → R
  /-- Total quantum dimension (`√(Σ d_λ²)` downstream; abstract here). -/
  D : R
  /-- The vacuum (trivial object) label. -/
  vac : ι
  /-- The vacuum object has quantum dimension `1`. -/
  d_vac : d vac = 1
  /-- The total quantum dimension is nonzero. -/
  D_ne : D ≠ 0

namespace VerlindeVacuumRow

variable {ι R : Type*} [Field R] (V : VerlindeVacuumRow ι R)

/-- The S-matrix vacuum-row entry `S_{0λ} = d_q(λ) / D`. -/
def S0 (lam : ι) : R := V.d lam / V.D

/-- `S_{00} = 1 / D` — the vacuum entry (its quantum dimension is `1`). -/
theorem S0_vac : V.S0 V.vac = 1 / V.D := by
  unfold S0; rw [V.d_vac]

/-- **The keystone value step (the "what"), sorry-free.** The vacuum-row ratio
    to the vacuum entry is exactly the quantum dimension:
    `S_{0λ} / S_{00} = d_q(λ)`.  This is `bwS0` recognised as the Verlinde
    vacuum row of the SU_q(2)/Hecke modular category (redirect iii). -/
theorem S0_ratio (lam : ι) : V.S0 lam / V.S0 V.vac = V.d lam := by
  unfold S0
  rw [V.d_vac]
  field_simp [V.D_ne]

/-- The vacuum-row vector is a nonzero rescaling of the quantum-dimension vector:
    `S_{0λ} = (1/D) · d_q(λ)`.  Records that `bwS0 ∝ d_q` with the single
    normalisation `1/D` (no per-block freedom) — the content the geometric
    realisations were trying, and failing, to reproduce independently. -/
theorem S0_eq_smul (lam : ι) : V.S0 lam = (1 / V.D) * V.d lam := by
  unfold S0; ring

end VerlindeVacuumRow

end QOU.BraidKnot
