import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.atomic_nf_witness

**Canonical declaration** for content block
[`prop:atomic-nf-witness`](../../../nuclear-interactions/atomic-nf-witness.md):
*Atomic braid normal form witness*.

## 2026-09-03 — a five-way conjunction carried as one field

`AtomicNfWitnessContext` carried thirteen data fields and, as
`atomic_nf_witness_field`, the theorem's **entire conclusion verbatim** — all
five sub-claims of the `.md` conjoined — and `atomic_nf_witness` returned it.
AGENTS.md §3b-cond item 5, and the largest carrier in this drain.

The field's own docstring was candid: *"External theorem / missing input:
atomic NF certificate facts."*  It is right that these are inputs.  What made
it a defect is that the *inputs were fields*, so the instance chose
`Phi_1`, `pi_star`, `F_Pauli`, `trAlt`, `net` and the rest, and then asserted
the five claims about its own choices — a `ctx : AtomicNfWitnessContext R`
argument constrains nothing a caller brought.

**Two decorative fields.**  `Braid : Type` and `W_max : ℕ → ℕ` appear in no
sub-claim.  `W_max` is the word-count cap for the `A > 9` stripping regime,
which is exactly the half of claim 4 that is **not** encoded (only
`a ≤ 9 → NF_no_strip a` is) — so the field that would have carried the
missing case was present and unused, which reads as coverage rather than as
the gap it is.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`atomic_nf_witness` is a **`Prop`-valued definition over caller-supplied
data**, so the five sub-claims constrain the caller's construction.  Two
consequences are **derived** from it rather than assumed:

* `fPauli_nonneg` — `F_Pauli = |tr_alt/net|` forces `0 ≤ F_Pauli`.  A Pauli
  character magnitude cannot be negative, and now it is a theorem instead of
  a property nobody checked.
* `groundState_value_unique` — sub-claim 1 says `π*` is a *global* minimum of
  `Φ₁`, so any two minimisers agree in value.  This is the content of "global
  minimum" as opposed to "a minimum found by descent", and it is what makes
  the exact/steepest-descent distinction in the `.md` meaningful.

## What is unencoded, and one part that cannot be

Claims 1–4 are named but unproved: nothing here constructs `H_{A+Z}(q)`, the
atomic braid, `Φ₁`, the Gröbner–Shirshov reduction, or the Diamond-Lemma
convergence argument claim 3 cites. The `A > 9` stripping branch of claim 4
is absent entirely, as above.

**Claim 5 is not a mathematical statement.** *"Certificates (JSON) are
committed to the repository for each computed atom"* is a fact about this
repository, not about `H_{A+Z}(q)`; it is unencodable in Lean by nature, not
by missing infrastructure. Saying so is the honest disposition — it should
never appear as a conjunct that some future instance is expected to
discharge.

## Base ring (§7c)

The nucleon/electron indices and mass numbers are `ℕ`. The scalars are
Hecke-trace quantities — the `Φ₁` cost, and the certificate's `tr_alt(q₀)`,
`net(q₀)` and `F_Pauli = |tr_alt / net|`. They are compared, divided and
taken in absolute value, which needs an ordered field but nothing
archimedean; so they stay a generic `R` and the substrate certificate is the
instantiation `R := ℝ`.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-nf-witness.md
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The claim of `prop:atomic-nf-witness`**, as a proposition over
caller-supplied data — sub-claims 1–4 of the `.md`:

1. `π*` globally minimises the nucleon-ordering cost `Φ₁`;
2. `e*` minimises `Φ₁` over electron positions (the greedy step);
3. the Gröbner–Shirshov reduction converges at every construction step;
4. the NF element accumulates without stripping for `A ≤ 9`;
   and the certificate records `F_Pauli = |tr_alt/net|`.

**Named, not asserted.**  Claim 5 of the `.md` is deliberately absent — see
the module docstring: it is a statement about this repository, not about
`H_{A+Z}(q)`. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-nf-witness.md
def atomic_nf_witness
    (Phi_1 Phi_1_electron : ℕ → R) (pi_star electron_pos_star : ℕ)
    (gb_converges NF_no_strip : ℕ → Prop)
    (F_Pauli trAlt net : R) : Prop :=
  (∀ π : ℕ, Phi_1 pi_star ≤ Phi_1 π) ∧
  (∀ p : ℕ, Phi_1_electron electron_pos_star ≤ Phi_1_electron p) ∧
  (∀ k : ℕ, gb_converges k) ∧
  (∀ a : ℕ, a ≤ 9 → NF_no_strip a) ∧
  F_Pauli = |trAlt / net|

/-- **The Pauli character is non-negative** — derived.

`F_Pauli = |tr_alt/net|` is an absolute value, so `0 ≤ F_Pauli`. Recorded
because it is a property of the certificate that nothing previously checked:
with `F_Pauli` a class field, an instance could have supplied a negative one
and satisfied the carrier only by also choosing `trAlt`/`net` to match. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-nf-witness.md
theorem fPauli_nonneg
    {Phi_1 Phi_1_electron : ℕ → R} {pi_star electron_pos_star : ℕ}
    {gb_converges NF_no_strip : ℕ → Prop} {F_Pauli trAlt net : R}
    (h : atomic_nf_witness Phi_1 Phi_1_electron pi_star electron_pos_star
          gb_converges NF_no_strip F_Pauli trAlt net) :
    0 ≤ F_Pauli := by
  rw [h.2.2.2.2]
  exact abs_nonneg _

omit [IsStrictOrderedRing R] in
/-- **The ground-state cost is well defined** — derived.

Sub-claim 1 says `π*` is a *global* minimum of `Φ₁`, so any other global
minimiser has the same cost. This is what "global minimum" asserts over and
above "a minimum reached by steepest descent", and it is the distinction the
`.md` draws between the exact regime (`C(A,Z) ≤ 50000`) and the descent
fallback. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-nf-witness.md
theorem groundState_value_unique
    {Phi_1 Phi_1_electron : ℕ → R} {pi_star electron_pos_star : ℕ}
    {gb_converges NF_no_strip : ℕ → Prop} {F_Pauli trAlt net : R}
    (h : atomic_nf_witness Phi_1 Phi_1_electron pi_star electron_pos_star
          gb_converges NF_no_strip F_Pauli trAlt net)
    (pi' : ℕ) (hmin : ∀ π : ℕ, Phi_1 pi' ≤ Phi_1 π) :
    Phi_1 pi_star = Phi_1 pi' :=
  le_antisymm (h.1 pi') (hmin pi_star)

/-- **The claim is refutable at freely-chosen data**, which is why it is named
rather than carried as a `sorry`.

At `tr_alt = 0`, `net = 1` the certificate conjunct reads `F_Pauli = 0`, so
`F_Pauli = 1` fails. -/
theorem not_atomic_nf_witness_of_free_data :
    ¬ atomic_nf_witness (R := ℝ) (fun _ => 0) (fun _ => 0) 0 0
        (fun _ => True) (fun _ => True) 1 0 1 := by
  rintro ⟨-, -, -, -, h⟩
  norm_num at h

end QOU.ParticleInteractions
