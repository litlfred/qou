import Mathlib.Tactic

/-
Per-term weight assembly for the six-term mass formula.

Stub formalisation of `conj:six-term-per-derivation-weights`.
The full proof requires several upstream pieces that are
currently in flight:
  - The descended Markov trace evaluation (T₁) at the
    β-decay scale `E_0_β = 0.7823 MeV`.
  - The Borromean-Catalan binding scale `α = m_e · 8G`
    proven in `BindingScaleCatalan.lean`.
  - The corrected Kashaev integration identity
    `∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V)` (proven on
    `claude/categorical-mass-divergence-audit`,
    commit a43d7f1fa, witness
    `kashaev-integration-identity.witness.json`).

For now this file declares the assembly interface and an
axiomatised `binding_assembly` constant so the content block's
`lean.ref` resolves; the full proof is gated on the upstream
formalisations above.

Empirical witness (Python, sub-percent on A ≤ 9):
  `paper_six_term_isotope_sweep.assemble_per_derivation_weights`
  (mean 0.184 %, max 0.525 % vs CODATA atomic mass).
-/

namespace QOU.BraidKnot.SixTermPerDerivationWeights

/-- **The six-term binding-energy assembly**
([`conj:six-term-per-derivation-weights`](../../../mass-theory/six-term-per-derivation-weights.md)),
as a proposition over caller-supplied data:

      B = E_0_β · (T1_free − T1_atom)
        + α · (T23_atom − T23_free)
        + m_e · (T4_atom − T4_free)
        + E_0_β · (a_K − 1) · T1_atom
        + (T6_atom − T6_free)

**Named, not asserted.**  This is the declaration the block's `lean.ref`
actually resolves to — see the note below on what it replaced.

Nothing here constructs the descended Markov trace `T1`, the `Φ_q` vertex
terms `T2`/`T3`, `τ(C_dim_q)` (`T4`), the cyclotomic residue sum `T6`, the
chirality coefficient `a_K`, or the Borromean–Catalan scale `α = m_e·8G`;
they are reals the caller supplies.  So this states which quantities are
combined and how, not why they are the ones that appear. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/six-term-per-derivation-weights.md
def binding_assembly (B E_0_β α m_e a_K T1_free T1_atom
    T23_free T23_atom T4_free T4_atom T6_free T6_atom : ℝ) : Prop :=
  B = E_0_β * (T1_free - T1_atom)
    + α * (T23_atom - T23_free)
    + m_e * (T4_atom - T4_free)
    + E_0_β * (a_K - 1) * T1_atom
    + (T6_atom - T6_free)

/-- **No binding when free and bound agree** — derived.

If every per-term value coincides between the free and atomic
configurations and the chirality coefficient is `a_K = 1`, the assembly
gives `B = 0`.  Each of the five terms is a difference that vanishes, the
fourth through its `(a_K − 1)` factor.

The sanity check the assembly must pass to be a *binding* energy at all, and
the reason the shape is worth naming: it is a hypothesis something is proved
from. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/six-term-per-derivation-weights.md
theorem binding_assembly_eq_zero_of_no_separation
    {B E_0_β α m_e T1 T23 T4 T6 : ℝ}
    (h : binding_assembly B E_0_β α m_e 1 T1 T1 T23 T23 T4 T4 T6 T6) :
    B = 0 := by
  simp only [binding_assembly] at h
  rw [h]; ring

/-- **The assembly is refutable at freely-chosen data**, which is why it is
named rather than carried as a `sorry`.

With every term zero it reads `1 = 0`. -/
theorem not_binding_assembly_of_free_data :
    ¬ binding_assembly 1 0 0 0 0 0 0 0 0 0 0 0 0 := by
  simp [binding_assembly]

/-! ### 2026-09-03 — what `binding_assembly` was, and the file it shadowed

Until this change `binding_assembly` was `opaque binding_assembly (Z N : Nat)
: Float` — an **opaque constant**, asserting nothing, with a `Float` standing
for a mass in MeV.  The block's `lean.ref` resolved to it, so the
proposition's formal handle carried no statement at all.

It also **shadowed** a second declaration of the same fully-qualified name in
[`SixTermPerDerivationWeights/binding_assembly.lean`](SixTermPerDerivationWeights/binding_assembly.lean),
which held `BindingAssemblyContext` and projected its own conclusion field.
`resolveCanonicalLean` takes the direct module path first when that file
declares the named decl, so this file always won and that one was never read.
It is now a drained shell; the projection is gone.

Neither module is imported anywhere, and nothing outside them names either
declaration (measured across `content/`, 2026-09-03).

Bean `qou-z9ws`.
-/

/-- The genuinely-open empirical inputs for the sub-percent
    accuracy claim: for an isotope `(Z, N)`, the per-derivation
    assembled atomic mass `assembled_mass` and the measured AME
    atomic mass `measured_mass` (both in MeV, `measured_mass > 0`).
    A categorical derivation of these from the substrate is open;
    they are carried as hypotheses (pattern C), not asserted. -/
class SixTermAssemblyData where
  /-- The per-derivation assembled atomic mass (MeV). -/
  assembled_mass : Nat → Nat → ℝ
  /-- The measured AME atomic mass (MeV). -/
  measured_mass : Nat → Nat → ℝ
  /-- Measured masses are positive. -/
  measured_pos : ∀ Z N, 0 < measured_mass Z N

/-- **Six-term per-derivation weights — sub-percent accuracy.**

Names (pattern C of the vacuity-fix playbook) the conditional
conjecture that, across the proton..⁹Be spectrum (`A = Z + N ≤ 9`),
the per-derivation assembly recovers the AME atomic mass to within
the empirical max relative error `0.0053` (= 0.53 %, from the
`A ≤ 9` sweep).  This is a *proposition* — honestly named, not a
vacuous `: True := trivial`: the mass data live on
`[SixTermAssemblyData]`, and an instance discharging the bound is
the open empirical claim (none = honest open state).

This `Prop` is the comparison boundary of
`conj:six-term-per-derivation-weights`: `measured_mass` is AME data and
`0.0053` is a measured error, so nothing here is a formal consequence of the
assembly `binding_assembly`, which takes every energy scale as a parameter.

Ref: paper_six_term_isotope_sweep.py (assemble_per_derivation_weights)
Ref: docs/audits/2026-05-04-per-derivation-weights-result.md -/
-- Ref: [leitner2026] conj:six-term-per-derivation-weights
def binding_assembly_subpercent [data : SixTermAssemblyData]
    (Z N : Nat) (_hA : Z + N ≤ 9) : Prop :=
    |data.assembled_mass Z N - data.measured_mass Z N| / data.measured_mass Z N ≤ 0.0053

end QOU.BraidKnot.SixTermPerDerivationWeights
