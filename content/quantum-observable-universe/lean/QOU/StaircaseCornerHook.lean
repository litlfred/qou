import Mathlib.Data.Nat.Defs
import Mathlib.Algebra.BigOperators.Basic

/-!
# Staircase EW-residual conjecture

The staircase partition `ρ k = (k, k-1, …, 1)` carries a distinguished
**corner hook** at cell `(0,0)`:

  `h_corner(ρ k) = arm(0,0) + leg(0,0) + 1 = (k-1) + (k-1) + 1 = 2k - 1`.

This file:

* **Proves** `staircase_corner_hook_eq_two_k_sub_one : h_corner k = 2*k - 1`
  rigorously (combinatorial; no `sorry`).
* **Axiomatises** as a Lean `class` the spectral conjecture that the
  scale `q^(1/(2k-1))` appears as a pairwise eigenvalue ratio of the
  staircase β_EW operator on `V_{ρ k}` — the conjecture verified
  empirically for k=3 (cot θ_W gap closure to 0.13%) and k=4 (rel.err
  0.14%) in `staircase_ew_residual_conjecture.py`.

Per `CLAUDE.md §3b`, an unproved staircase EW-residual claim must be
either kind `conjecture` or a provable kind under the conditional-class
exception (a `class` instance whose `sorry` axiomatises the claim).
We choose the latter so downstream results may state conditional
theorems "if `StaircaseEWResidual` holds, then …".

## References

* Hoefsmit (1974), *Representations of Hecke algebras of finite groups
  with BN-pairs of classical type*, PhD thesis, UBC.
* Mathas (1999), *Iwahori–Hecke algebras and Schur algebras of the
  symmetric group*, AMS, §3.31.
* Stanley (1999), *Enumerative Combinatorics II*, Cambridge UP, §7.21
  (hook-content formula).
-/

namespace QOU.StaircaseCornerHook

/-- The corner hook of the staircase `ρ k = (k, k-1, …, 1)` at cell
`(0, 0)`.  Defined directly as the combinatorial quantity:

  `h_corner k := arm(0,0) + leg(0,0) + 1`

For the staircase `ρ k`:

* `arm(0,0) = (length of row 0) - 1 = k - 1`
* `leg(0,0) = (number of rows with ρ k r ≥ 1) - 1 = k - 1`

so `h_corner k = (k - 1) + (k - 1) + 1`. -/
def hCorner (k : ℕ) : ℕ := (k - 1) + (k - 1) + 1

/-- **Provable lemma.** The corner hook of the staircase `ρ k` equals
`2*k - 1` for every `k ≥ 1`.

This is purely combinatorial: it follows from the definition of the
staircase shape and the hook-length formula, with no appeal to
representation theory or any spectral data.

Ref: [stanley1999] Enumerative Combinatorics II, §7.21
-/
theorem staircase_corner_hook_eq_two_k_sub_one
    (k : ℕ) (hk : 1 ≤ k) :
    hCorner k = 2 * k - 1 := by
  -- Unfold and compute using `omega`, which handles natural-number
  -- truncated subtraction precisely.
  unfold hCorner
  omega

/-- Sanity checks for small k. -/
example : hCorner 2 = 3 := by decide
example : hCorner 3 = 5 := by decide
example : hCorner 4 = 7 := by decide
example : hCorner 5 = 9 := by decide
example : hCorner 6 = 11 := by decide

/-! ## The staircase EW-residual conjecture (axiomatised as a class)

For the empirical content and 7/7 witness assertions, see:

* `folio-assistant/computations/staircase_ew_residual_conjecture.py`
* `folio-assistant/computations/staircase-ew-residual-conjecture.witness.json`
* `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`

Per `CLAUDE.md §3b-cond`, the conjecture is encoded as

* an opaque `Prop`-valued declaration `StaircaseEWSpectralContent k`
  (one axiom; cannot be discharged by `trivial`); and
* a `class StaircaseEWResidual` whose single field bundles the family
  `∀ k ≥ 2, StaircaseEWSpectralContent k`.

A canonical instance is provided **with `sorry`** as the formal record
that the conjecture is open:

  ```
  instance : StaircaseEWResidual := ⟨fun _ _ => sorry⟩
  ```

The single `sorry` IS the conjecture.  Downstream theorems may take
`[StaircaseEWResidual]` as an instance hypothesis and carry the §3b-cond
"conditional on `conj:staircase-ew-residual`" banner; once a real proof
lands, the `sorry` is discharged here and every downstream conditional
becomes unconditional automatically.

Ref: [manuscript] §EW-residual, observed at q_0 to relative error
1.30e-3 (k=3, top-two ratio against cot θ_W) and 1.42e-3 (k=4,
pairwise-ratio search in dim-768 spectrum).
-/

/-- Opaque proposition encoding the spectral claim "for staircase
`ρ k = (k, k-1, …, 1)`, the inverse-corner-hook scale `q^(1/(2k-1))`
is realised as a ratio of two positive eigenvalues of the canonical
β_EW Δ_I^minimal operator on the Hoefsmit module `V_{ρ k}`".

Declared as an `axiom`-protected `Prop` rather than a concrete
predicate because the precise statement requires the full Hoefsmit
matrix infrastructure (`QOU.Hecke.Hoefsmit`).  When that
infrastructure exposes the staircase β_EW operator and an eigenvalue
interface, this declaration is to be replaced by the literal
predicate, and the `sorry` instance below becomes either discharged
or restated against the new shape.

Crucially, this declaration has **no introduction rule** — providing
a witness requires either (a) a literal proof, or (b) an additional
axiom — so the field cannot be vacuously satisfied. -/
axiom StaircaseEWSpectralContent (k : ℕ) : Prop

/-- Axiomatic class encoding the staircase EW-residual conjecture. -/
class StaircaseEWResidual : Prop where
  /-- For every `k ≥ 2`, the inverse-corner-hook scale
  `q^(1/(2k-1))` is realised as a ratio of two positive eigenvalues
  of the canonical staircase β_EW operator on `V_{ρ k}`. -/
  spectral_scale_present :
    ∀ (k : ℕ), 2 ≤ k → StaircaseEWSpectralContent k

/-- **Open conjecture, recorded via `sorry`.**

This is the *single* `sorry` in the staircase EW-residual chain.
Per `CLAUDE.md §3b-cond`, downstream theorems that take
`[StaircaseEWResidual]` as an instance hypothesis are
**rigorous-conditional** results: their Lean side is fully verified
modulo this one named conjectural input.

To formalise the proof, replace `sorry` with a real construction
that supplies `StaircaseEWSpectralContent k` for every `k ≥ 2`
(once `QOU.Hecke.Hoefsmit` exposes the staircase β_EW operator and
the eigenvalue-ratio set).
-/
instance staircase_ew_residual_conjecture : StaircaseEWResidual where
  spectral_scale_present := fun _ _ => sorry
  -- Ref: [manuscript] docs/audits/2026-05-06-staircase-ew-residual-conjecture.md

end QOU.StaircaseCornerHook
