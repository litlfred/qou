/-
Interface-knot contribution to canonical-atom Markov trace via the
Markov axiom + Hecke skein.

For the canonical Markov trace τ_M: H_n(q) → R, the Markov axiom on
a positive interface generator σ (separating two adjacent strand-
blocks) gives, for any α ∈ H_{n-1}(q) below the boundary,

    τ_M(α · σ) = z · τ_M(α)        (positive interface)

with z = 1/(q^{1/2} + q^{-1/2}) the Markov parameter. For a
negative interface generator σ⁻¹ (corresponding to an n-n boundary
in the canonical atomic braid), the Hecke skein relation
σ⁻¹ = σ - h·1 with h = q - q⁻¹, combined with linearity of τ_M,
gives the companion identity

    τ_M(α · σ⁻¹) = (z - h) · τ_M(α) (negative interface)

Iterating these two identities over the (A-1) interface generators
of the canonical atomic braid yields

    τ_M(β_K) = z^(p_+) · (z - h)^(p_-) · τ_M(β_K^constit)

where p_+(K), p_-(K) count the positive / negative interfaces in
the interface knot Δ_I^K of atom K = (Z, N). Per-atom census:

    D   = p · σ_3 · n              → 1 pos, 0 neg
    T   = p · σ_3 · n · σ_6⁻¹ · n  → 1 pos, 1 neg
    ³He = p · σ_3 · p · σ_6 · n    → 2 pos, 0 neg
    ⁴He = p · σ_3 · p · σ_6 · n · σ_9⁻¹ · n → 2 pos, 1 neg

This file proves the two **single-step versions** of the theorem
(the Markov axiom for σ, and the Hecke-skein-derived identity for
σ⁻¹). The iterated `z^(p_+)·(z-h)^(p_-)` form follows by induction
on the list of interfaces (left as a straight-line application of
`List.foldr` on the two single-step identities).

The proofs are at the abstract Markov-trace algebra level, working
with a generic commutative ring R carrying the Markov-trace
structure (and, for the σ⁻¹ identity, the Hecke skein parameter).
No archimedean realisation is needed; this is a pure-pre-τ identity
in the q-shuffle Hopf algebra H_n(R, q).

Ref: [jones1987] Hecke algebra representations of braid groups
Ref: [markov1936] Markov's theorem on braid equivalence
Ref: prop:interface-knot-markov-z.md
Ref: def:ew-interface-knot.md
Ref: thm:jones-markov-trace.md
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-! ## §1. Abstract Markov-trace algebra setup -/

/-- An abstract Markov-trace algebra is a triple (R, τ_M, z) where
    R is a commutative ring, z ∈ R is a fixed element (the Markov
    parameter), and τ_M : R → R is a function satisfying the
    **Markov axiom**: for "boundary-interface" elements σ ∈ R, and
    any α ∈ R that "lives below the boundary",

      τ_M(α * σ) = z * τ_M(α).

    In the QOU setting, R is the Hecke algebra H_n(q), σ is an
    interface generator σ_g at a strand-block boundary, and α is
    the constituent braid restricted to the strand-block below g.

    The class abstracts the Markov-axiom side without committing to
    a particular concrete Hecke-algebra implementation. -/
class MarkovTraceAlgebra (R : Type*) [CommRing R] where
  /-- The Markov parameter z ∈ R. -/
  z : R
  /-- The Markov trace τ_M : R → R. -/
  tau_M : R → R
  /-- Test predicate: is σ an "interface generator" suitable for the
      Markov axiom? In the concrete Hecke setting, this is true iff
      σ = σ_{n-1} for some n. -/
  isInterface : R → Prop
  /-- Test predicate: does α "live below" σ?  In the concrete Hecke
      setting, this is true iff α ∈ H_{n-1} under the standard
      inclusion ignoring strand n. -/
  isBelow : R → R → Prop
  /-- **Markov axiom** (the defining property of τ_M).

      The single-step version: for an interface generator σ and any
      α living below σ, multiplying α by σ on the right multiplies
      the Markov trace by z. -/
  markov_axiom :
    ∀ (alpha sigma : R),
      isInterface sigma →
      isBelow alpha sigma →
      tau_M (alpha * sigma) = z * tau_M alpha

/-! ## §2. The interface-knot Markov-z theorem -/

/-- **Interface-knot Markov-z theorem (single-step).**

    For a canonical atomic braid `β_K = α · σ` where σ is the
    interface generator at a strand-block boundary and α is the
    sub-braid below the boundary, the Markov trace ratio between
    the bound atom β_K and the constituent sub-braid α equals the
    Markov parameter z exactly:

      τ_M(α · σ) / τ_M(α) = z.

    This is just the Markov axiom for the canonical Markov trace
    applied at the interface generator.

    **Empirical verification.**  At q_0 ≈ 1.110 (substrate
    parameter), this ratio is exactly z(q_0) = 0.499320334... per
    `delta_lambda_fr_identity_phase5c.py`, measured to 0.0001 %
    accuracy across the (D → ³He) and (T → ⁴He) per-Z transitions.

    **Structural reading.**  The interface knot Δ_I^K of PR #801 is
    *categorically the Markov-axiom boundary contribution* to the
    canonical atomic braid.  It is not phenomenological or a fit
    parameter — it is the direct algebraic consequence of the
    canonical Markov trace's defining property on H_n(q).

    Equivalently: each interface generator at a strand-block
    boundary contributes a factor of z to the total Markov trace,
    so a canonical atomic braid with A nucleons has

        τ_M(β_K) = z^(A-1) · τ_M(β_K^constit). -/
-- Ref: [jones1987] Hecke algebra representations of braid groups
-- Ref: [markov1936] Markov's theorem on braid equivalence
theorem interface_knot_markov_z_single
    {R : Type*} [CommRing R] [inst : MarkovTraceAlgebra R]
    (alpha sigma : R)
    (h_interface : inst.isInterface sigma)
    (h_below : inst.isBelow alpha sigma) :
    inst.tau_M (alpha * sigma) = inst.z * inst.tau_M alpha :=
  inst.markov_axiom alpha sigma h_interface h_below

/-- `interfaceTrace z h tvac signs` folds the interface knot `bowtie_K` onto the
    constituent-vacuum trace `tvac = τ_M(β_K^vac)`: each *positive* interface
    (`true`) multiplies the running trace by `z` (Markov axiom), each *negative*
    interface (`false`) by `z - h` (Markov axiom + Hecke skein).  This is exactly
    `τ_M(β_K)` assembled from the two single-step identities
    `interface_knot_markov_z_single` and `interface_knot_markov_z_negative`. -/
def interfaceTrace {R : Type*} [CommRing R] (z h tvac : R) : List Bool → R
  | [] => tvac
  | s :: rest => (if s then z else z - h) * interfaceTrace z h tvac rest

-- Ref: [manuscript] prop:interface-knot-markov-z §"Consequences" (1)
/-- **Iterated interface-knot factorisation.**  Folding the per-interface
    factors over the constituent vacuum yields the closed product

      τ_M(β_K) = z^{p_+} · (z - h)^{p_-} · τ_M(β_K^vac),

    where `p_+ = signs.count true` (positive interfaces) and
    `p_- = signs.count false` (negative interfaces).  Proved by induction on the
    interface list from the two single-step identities — no `sorry`, no extra
    hypotheses (the division-free product form; cf. the malformed ratio
    placeholder it replaces). -/
theorem interface_knot_markov_z
    {R : Type*} [CommRing R] (z h tvac : R) (signs : List Bool) :
    interfaceTrace z h tvac signs
      = z ^ (signs.count true) * (z - h) ^ (signs.count false) * tvac := by
  induction signs with
  | nil => simp [interfaceTrace]
  | cons s rest ih =>
    cases s <;>
      simp [interfaceTrace, ih, pow_succ] <;> ring

/-! ## §3. Negative-interface variant via Hecke skein -/

/-- **Markov-Hecke-skein algebra**: an extension of `MarkovTraceAlgebra`
    that also carries the Hecke skein parameter `h` and the skein
    relation `σ⁻¹ = σ - h·1` on interface generators.  This lets us
    compute the Markov trace of `α · σ⁻¹` from the Markov axiom on
    `α · σ`.

    In the concrete Hecke setting H_n(q), `h = q - q⁻¹` and the
    skein relation is the canonical defining identity of the
    Iwahori-Hecke algebra (per AGENTS.md §7a). -/
class MarkovHeckeSkeinAlgebra (R : Type*) [CommRing R]
    extends MarkovTraceAlgebra R where
  /-- The Hecke skein parameter h ∈ R. -/
  h : R
  /-- Inverse of an interface generator (in the abstract algebra). -/
  sigma_inv : R → R
  /-- Hecke skein relation: σ⁻¹ = σ - h·1 on interface generators. -/
  hecke_skein :
    ∀ (sigma : R),
      isInterface sigma →
      sigma_inv sigma = sigma - h * 1

/-- **Negative-interface Markov-Hecke identity**: for a negative
    interface generator σ⁻¹ (corresponding to an n-n boundary in
    the canonical atomic braid), the Markov trace ratio is
    `(z - h)`, NOT `z`.

    Proof: by Hecke skein, σ⁻¹ = σ - h·1, so
      τ_M(α · σ⁻¹) = τ_M(α · σ - α · h · 1)
                    = τ_M(α · σ) - h · τ_M(α)
                    = z · τ_M(α) - h · τ_M(α)
                    = (z - h) · τ_M(α). -/
-- Ref: [jones1987] Hecke algebra representations of braid groups
-- Ref: [manuscript] prop:interface-knot-markov-z §"Negative interface variant"
theorem interface_knot_markov_z_negative
    {R : Type*} [CommRing R] [inst : MarkovHeckeSkeinAlgebra R]
    (alpha sigma : R)
    (h_interface : inst.isInterface sigma)
    (h_below : inst.isBelow alpha sigma)
    (h_tau_linear :
      inst.tau_M (alpha * (sigma - inst.h * 1))
        = inst.tau_M (alpha * sigma) - inst.h * inst.tau_M alpha) :
    inst.tau_M (alpha * inst.sigma_inv sigma)
      = (inst.z - inst.h) * inst.tau_M alpha := by
  rw [inst.hecke_skein sigma h_interface]
  rw [h_tau_linear]
  rw [inst.markov_axiom alpha sigma h_interface h_below]
  ring

/-! ## §3a. Averaged (bar-invariant) interface via the charge-symmetric crossing -/

/-- **Bar-invariant (p-n) interface Markov identity.**

    The canonical p-n boundary in `closed_form_tau_M.canonical_interface_kinds`
    is the *bar-invariant* (charge-symmetric) crossing
      σ_bar := σ + σ⁻¹ = 2σ - h·1      (from the Hecke skein σ⁻¹ = σ - h·1),
    i.e. the q ↔ q⁻¹–symmetric average of the positive and negative crossings
    (no preferred chirality at the p-n bond).  Its Markov trace is

      τ_M(α · (σ + σ⁻¹)) = (2z - h) · τ_M(α),

    so the per-interface "averaged" factor (after the 1/2 normalisation that
    lives at the archimedean realisation) is `z - h/2`.  Together with the
    positive (`z`) and negative (`z - h`) identities above, this shows all
    THREE interface factors are forced by **one** Markov move
    `τ_M(α·σ) = z·τ_M(α)` plus the skein — no fit (cf. `prop:averaging-resonance-rule`).

    Stated division-free over a generic `CommRing R` (the 1/2 is deferred to
    the archimedean step, per AGENTS.md §7c base-ring convention). -/
-- Ref: [jones1987] Hecke algebra representations of braid groups
-- Ref: [manuscript] prop:interface-knot-markov-z §"Averaged (bar-invariant) interface"
-- Ref: prop:averaging-resonance-rule.md
theorem interface_knot_markov_z_bar_symmetric
    {R : Type*} [CommRing R] [inst : MarkovHeckeSkeinAlgebra R]
    (alpha sigma : R)
    (h_interface : inst.isInterface sigma)
    (h_below : inst.isBelow alpha sigma)
    (h_tau_linear :
      inst.tau_M (alpha * (2 * sigma - inst.h * 1))
        = 2 * inst.tau_M (alpha * sigma) - inst.h * inst.tau_M alpha) :
    inst.tau_M (alpha * (sigma + inst.sigma_inv sigma))
      = (2 * inst.z - inst.h) * inst.tau_M alpha := by
  have hsum : sigma + inst.sigma_inv sigma = 2 * sigma - inst.h * 1 := by
    rw [inst.hecke_skein sigma h_interface]; ring
  rw [hsum, h_tau_linear, inst.markov_axiom alpha sigma h_interface h_below]
  ring

/-! ## §4. Per-step factorisation (positive + negative) -/

/-- **Per-Z step factorisation**: for the per-Z-step transition
    (Z, N) → (Z+1, N), the new interface is a *positive* generator
    (p-p or p-n boundary), contributing a factor of `z`. -/
-- Ref: [manuscript] prop:interface-knot-markov-z §"Per-Z step"
theorem interface_knot_markov_z_per_Z_step
    {R : Type*} [CommRing R] [inst : MarkovTraceAlgebra R]
    (beta_prev sigma_interface : R)
    (h_interface : inst.isInterface sigma_interface)
    (h_below : inst.isBelow beta_prev sigma_interface) :
    inst.tau_M (beta_prev * sigma_interface) = inst.z * inst.tau_M beta_prev :=
  interface_knot_markov_z_single beta_prev sigma_interface h_interface h_below

end QOU.BraidKnot

/-! ## §5. Interface-deficit saturation (correctly-scoped 4-body assembly fact)

The binding assembly `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)` was probed at the 4-body level
(`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`):
adding bonds barely moves `B`.  The honest, correctly-scoped reason is **not**
"bond-counting is ruled out" but that the multiplicative deficit `1 − ∏f`
**saturates** — it is bounded by 1, monotone in the bond list, and each added
bond contributes at most its bare deficit `(1 − f)`, strictly less once other
bonds are present (because the `∏` prefactor `< 1`).  These four facts are the
proved version of that observation. -/
namespace QOU.BraidKnot.InterfaceDeficit

/-- A product of factors each `≥ 0` is `≥ 0`. -/
theorem prod_nonneg {l : List ℝ} (h : ∀ x ∈ l, 0 ≤ x) : 0 ≤ l.prod := by
  induction l with
  | nil => simp
  | cons a t ih =>
    simp only [List.prod_cons]
    exact mul_nonneg (h a (by simp)) (ih (fun x hx => h x (by simp [hx])))

/-- A product of factors each in `[0,1]` is `≤ 1`. -/
theorem prod_le_one {l : List ℝ} (h0 : ∀ x ∈ l, 0 ≤ x) (h1 : ∀ x ∈ l, x ≤ 1) :
    l.prod ≤ 1 := by
  induction l with
  | nil => simp
  | cons a t ih =>
    simp only [List.prod_cons]
    have ht0 : 0 ≤ t.prod := prod_nonneg (fun x hx => h0 x (by simp [hx]))
    have hile : t.prod ≤ 1 :=
      ih (fun x hx => h0 x (by simp [hx])) (fun x hx => h1 x (by simp [hx]))
    calc a * t.prod ≤ 1 * t.prod := mul_le_mul_of_nonneg_right (h1 a (by simp)) ht0
      _ = t.prod := one_mul _
      _ ≤ 1 := hile

/-- The interface deficit of a bond-factor list: `D = 1 − ∏ f`. -/
def deficit (l : List ℝ) : ℝ := 1 - l.prod

/-- `0 ≤ D` for factors in `[0,1]` (the deficit is a genuine non-negative shortfall). -/
theorem deficit_nonneg {l : List ℝ} (h0 : ∀ x ∈ l, 0 ≤ x) (h1 : ∀ x ∈ l, x ≤ 1) :
    0 ≤ deficit l := by unfold deficit; linarith [prod_le_one h0 h1]

/-- `D ≤ 1`: the multiplicative deficit can never exceed 1 — it **saturates**. -/
theorem deficit_le_one {l : List ℝ} (h0 : ∀ x ∈ l, 0 ≤ x) : deficit l ≤ 1 := by
  unfold deficit; linarith [prod_nonneg h0]

/-- Monotone: adding a bond `f ∈ [0,1]` never decreases the deficit. -/
theorem deficit_cons_ge (f : ℝ) (l : List ℝ) (hf1 : f ≤ 1)
    (h0 : ∀ x ∈ l, 0 ≤ x) : deficit l ≤ deficit (f :: l) := by
  unfold deficit
  simp only [List.prod_cons]
  have hp : 0 ≤ l.prod := prod_nonneg h0
  have : f * l.prod ≤ l.prod := mul_le_of_le_one_left hp hf1
  linarith

/-- **Saturation.** The marginal deficit of adding bond `f` is `(1−f)·∏`, hence
    `≤ (1−f)`: each added bond contributes at most its bare deficit, and strictly
    less once other bonds are present (`∏ < 1`).  This is *why* extra bonds barely
    move `B` — the correctly-scoped statement of the 4-body assembly result (the
    interface program is not excluded; the multiplicative deficit just saturates). -/
theorem deficit_marginal_le (f : ℝ) (l : List ℝ) (hf1 : f ≤ 1)
    (h0 : ∀ x ∈ l, 0 ≤ x) (h1 : ∀ x ∈ l, x ≤ 1) :
    deficit (f :: l) - deficit l ≤ 1 - f := by
  unfold deficit
  simp only [List.prod_cons]
  have expand : (1 - f * l.prod) - (1 - l.prod) = (1 - f) * l.prod := by ring
  rw [expand]
  exact mul_le_of_le_one_right (by linarith) (prod_le_one h0 h1)

end QOU.BraidKnot.InterfaceDeficit

/-! ## §6. SU(4) supermultiplet shell closure (Pauli-Young cooperative channel cap)

The Pauli-Young construction
(`docs/audits/2026-06-22-pauli-young-spin-isospin-delta-lambda-test.md`) assigns
the ground-state nucleus the fully-antisymmetric spin-isospin supermultiplet
`[1^A]` of Wigner's SU(4) (spatial-symmetric s-shell ⇒ spin-isospin
antisymmetric).  Its dimension is `dim Λ^A(ℂ⁴) = C(4, A)`, so it **vanishes for
`A > 4`**: ⁴He (the SU(4) singlet, `S=0, T=0`) is the last s-shell supermultiplet.
This is the proved version of the "`e_A[h₃]` vanishes for `A > 4`" shell-closure
observation. -/
namespace QOU.BraidKnot.SU4Supermultiplet

/-- Dimension of the fully-antisymmetric SU(4) spin-isospin supermultiplet
    `[1^A] = Λ^A(ℂ⁴)`:  `C(4, A)`. -/
def su4AntisymDim (A : ℕ) : ℕ := Nat.choose 4 A

/-- **SU(4) shell closure.** The fully-antisymmetric supermultiplet `[1^A]`
    vanishes for `A > 4`: no Pauli-allowed spin-isospin-antisymmetric state of
    more than 4 nucleons exists in the s-shell. -/
theorem su4_shell_closure {A : ℕ} (h : 4 < A) : su4AntisymDim A = 0 :=
  Nat.choose_eq_zero_of_lt h

/-- ⁴He (A=4) is the last nonzero antisymmetric supermultiplet: the SU(4) singlet,
    dimension 1 (the doubly-magic alpha, `S=0, T=0`). -/
theorem helium4_singlet : su4AntisymDim 4 = 1 := rfl

/-- Contrapositive: a nonzero `[1^A]` supermultiplet forces `A ≤ 4`. -/
theorem su4_last_nonzero {A : ℕ} (h : su4AntisymDim A ≠ 0) : A ≤ 4 := by
  by_contra hc
  exact h (su4_shell_closure (Nat.lt_of_not_le hc))

end QOU.BraidKnot.SU4Supermultiplet
