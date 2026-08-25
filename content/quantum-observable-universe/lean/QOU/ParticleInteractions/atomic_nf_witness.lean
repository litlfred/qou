import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.atomic_nf_witness

**Canonical declaration** for content block
[`prop:atomic-nf-witness`](../../../quantum-observable-universe/particle-interactions/atomic-nf-witness.md): *Atomic braid normal form witness*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

## Base ring (§7c)

The nucleon/electron indices, mass numbers and word caps are `ℕ`. The scalars
are Hecke-trace quantities -- the `Φ₁` cost, and the certificate's
`tr_alt(q_0)`, `net(q_0)` and `F_Pauli = |tr_alt / net|`. They are compared,
divided and taken in absolute value, which needs an ordered field, but nothing
archimedean; so the scalars are a generic `R` and the substrate certificate is
the instantiation `R := ℝ`.
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Abstract context for the `atomic_nf_witness` claim —
    manuscript-themed typed fields below; sub-claims encode the
    five steps of the atomic braid construction (nucleon ordering /
    electron placement / GB convergence / NF accumulation /
    certificate output). -/
class AtomicNfWitnessContext (R : Type*) [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- The braid representative type. -/
  Braid : Type
  /-- `Φ₁` cost of an ordering (indexed by nucleon-permutation index). -/
  Phi_1 : ℕ → R
  /-- Ground-state ordering index `π*` that minimises `Φ₁`. -/
  pi_star : ℕ
  /-- `Φ₁` cost as a function of electron position (greedy step). -/
  Phi_1_electron : ℕ → R
  /-- The greedy-chosen electron position `e*`. -/
  electron_pos_star : ℕ
  /-- Predicate: GB reduction at construction step `k` converges. -/
  gb_converges : ℕ → Prop
  /-- Word-count cap `W_max(A)` for mid-construction stripping. -/
  W_max : ℕ → ℕ
  /-- Predicate: NF element accumulated without stripping at mass `A`. -/
  NF_no_strip : ℕ → Prop
  /-- The `F_Pauli` value recorded in the witness certificate. -/
  F_Pauli : R
  /-- The `tr_alt(q_0)` and `net(q_0)` values from the certificate. -/
  trAlt : R
  net : R
  /-- External theorem / missing input: atomic NF certificate facts. -/
  atomic_nf_witness_field : (∀ π : ℕ, Phi_1 pi_star ≤ Phi_1 π) ∧
    (∀ p : ℕ, Phi_1_electron electron_pos_star ≤
                Phi_1_electron p) ∧
    (∀ k : ℕ, gb_converges k) ∧
    (∀ a : ℕ, a ≤ 9 → NF_no_strip a) ∧
    F_Pauli = |trAlt / net|

/-- **Proposition statement** (from manuscript):

For each atom $(Z, N)$ with $Z = 1$--$20$, the atomic braid
construction produces an element of $H_{A+Z}(q)$ that is verified
to be in Gröbner--Shirshov normal form.  Specifically:*

1. *The ground-state nucleon ordering is the global minimum of
   $\Phi_1$ over all $\binom{A}{Z}$ permutations (exact for
   $\binom{A}{Z} \leq 50000$, steepest descent otherwise).*

2. *Each electron is inserted at the position minimizing $\Phi_1$
   (greedy, verified to produce ep pairs adjacent to protons).*

3. *At each construction step (adding strand $k$ with crossings
   to all previous strands $0, \ldots, k-1$): the
   Gröbner--Shirshov reduction is run to convergence
   ([inductive reduction](#prop\:inductive-gb-reduction)).  Convergence
   is guaranteed by the Diamond Lemma (the three rewriting rules
   satisfy all overlap ambiguities).*

4. *The final NF element is accumulated without mid-construction
   stripping for $A \leq 9$ (exact).  For $A > 9$, the element is
   stripped at controlled thresholds (200k--500k words) and the
   stripped contributions are accumulated into the Pauli character
   $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}/\mathrm{net}|$.*

5. *Certificates (JSON) are committed to the repository for each
   computed atom.  Each certificate records: $F_{\mathrm{Pauli}}$,
   $\mathrm{tr}_{\mathrm{alt}}(q_0)$, $\mathrm{net}(q_0)$,
   computation time, word count, and engine version.
-/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/atomic-nf-witness.ts
theorem atomic_nf_witness (ctx : AtomicNfWitnessContext R) :
    (∀ π : ℕ, ctx.Phi_1 ctx.pi_star ≤ ctx.Phi_1 π) ∧
    (∀ p : ℕ, ctx.Phi_1_electron ctx.electron_pos_star ≤
                ctx.Phi_1_electron p) ∧
    (∀ k : ℕ, ctx.gb_converges k) ∧
    (∀ a : ℕ, a ≤ 9 → ctx.NF_no_strip a) ∧
    ctx.F_Pauli = |ctx.trAlt / ctx.net| :=
  ctx.atomic_nf_witness_field

end QOU.ParticleInteractions
