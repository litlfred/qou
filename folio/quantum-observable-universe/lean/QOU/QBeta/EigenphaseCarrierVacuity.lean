/-
# The Q_β eigenphase carrier asserts nothing — and a content-bearing replacement

Bean `qou-cds1`.  Tranche S1 needs a **derivation** of the ladder phase
`α = (z−1)h/2`, because `qbeta_ladder_required_phase_probe.py` prunes the whole
class "`α = (z−1)h/2` with `z` a convention parameter" for convention D: the
required phase is pinned to a window of half-width `≈1.1e-5` rad and `z_D` sits
`≈1.19e-2` rad away, so the *functional form* has to change, not the value of
`z` inside it.

Chasing where `α` is asserted leads to
`folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean`,
whose class `QOU.Interactions.TransferMatrixEigenphase` is documented as
axiomatising the spectral identification

  > `M_β` has spectrum `{e^{+iα}, e^{−iα}}` on the 2-d irrep `V_{(2,1)}` of
  > `H₃(q)`, where `α = (z−1)h/2`.

**Its two fields encode none of that.**  They are

  `-2 ≤ 2 cos(eigenphase q) ∧ 2 cos(eigenphase q) ≤ 2`
  `cos(eigenphase q) = cos(-eigenphase q)`

and both hold for *every real number* in place of the eigenphase
(`Real.neg_one_le_cos` / `Real.cos_le_one`, and `Real.cos_neg`).  So the class
is inhabited for every `q` by a proof that uses nothing about `eigenphase` at
all — it is equivalent to `True`, and a theorem stated
`[TransferMatrixEigenphase q] → P` is just `P`.

This is the `proof-claims-unencoded` failure mode of AGENTS.md §3b-tax: a
carrier whose docstring enumerates named properties that are not encoded as Prop
fields.  It is also the direct reason `α` is *asserted and derived nowhere* —
the carrier meant to hold the assertion holds nothing, so there is no
C-frame content to port to D.

§1 below demonstrates the vacuity.  §2 proposes the minimal honest repair: a
carrier that states the spectral identification with real content and has **no
instance**, which per §3b-tax is how a genuinely open input is represented.

**Scope.**  This does not derive `α`, in either convention, and does not claim
the cos-resummation is false — only that its Lean hypothesis is empty, so the
result is unconditional rather than conditional, and the physical content the
docstring describes is not carried anywhere.  Scope-(a).

**UPDATE 2026-09-03 (bean `qou-eixt`) — the live carrier has been repaired; this
file is now the RECORD, not a live indictment.**
`folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean`
has adopted §2's `TransferMatrixSpectrum` shape: its `TransferMatrixEigenphase`
now takes the `2×2` restriction `M` and pins `M.trace = 2 cos(eigenphase q)`,
`M.det = 1`, with no instance declared there. Its `q_beta_cos_resummation` was
also repaired — separately from the carrier, and this file did not catch that
one: the theorem's proof was `refine ⟨…, rfl, ?_⟩; ring` on `∃ x, x = A ∧ x = A`
and never mentioned the instance, so the result was unconditional *twice over*,
once through the empty carrier and once through a proof that ignored it. It now
rewrites `trace_eq`, and the negative control (same statement, binder dropped)
fails as it must.

**§1's reproduction is kept deliberately** and is the reason this file still
appears in the vacuity audit under `proof-claims-unencoded`: it is the
demonstration copy, and a file whose purpose is to exhibit a defect is not
itself the defect (ledger verdict `legit`,
`deliberate-reproduction-for-demonstration`). Do not "fix" it — deleting it
would delete the proof that the superseded encoding was empty.

**§3 is unaffected and is still the operative finding.** The repair above is
branch 2 of that trichotomy — `M` arbitrary, circularly dischargeable by
`circularWitness` — so it buys a carrier that constrains its argument and a
theorem that is a genuine implication, and buys **no** evidence about the
substrate. Branch 3 (KZ / Kohno–Drinfeld holonomy) remains where a derivation
of `α` must live, and remains uncarried out.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace QOU.QBeta.EigenphaseCarrier

open Real

/-! ## §1 — the existing carrier is vacuous

Definitions reproduced verbatim from the content-block sibling so this file is
self-contained and does not depend on a block's `.lean` staying put. -/

/-- Convention-C Markov parameter, as spelled in the content block. -/
noncomputable def markovZC (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- `h = q − q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- The asserted single-wrap eigenphase `α = (z−1)h/2`. -/
noncomputable def eigenphase (q : ℝ) : ℝ := (markovZC q - 1) * heckeH q / 2

/-- The existing carrier, fields reproduced verbatim.
    (`@marker` opt-out: deliberate reproduction of the superseded vacuous carrier
    for §1's proof of equivalence to `True`.) -/
class TransferMatrixEigenphase (q : ℝ) : Prop where
  symmetrized_character_in_unit_disc :
    -2 ≤ 2 * Real.cos (eigenphase q) ∧ 2 * Real.cos (eigenphase q) ≤ 2
  cos_eigenphase_bar_invariant :
    Real.cos (eigenphase q) = Real.cos (- eigenphase q)

/-- Field 1 holds for an **arbitrary** real, so it says nothing about the
eigenphase. -/
theorem field1_holds_for_any_real (x : ℝ) : -2 ≤ 2 * cos x ∧ 2 * cos x ≤ 2 := by
  constructor
  · nlinarith [neg_one_le_cos x]
  · nlinarith [cos_le_one x]

/-- Field 2 likewise: `cos` is even, for every real. -/
theorem field2_holds_for_any_real (x : ℝ) : cos x = cos (-x) := (cos_neg _).symm

/-- **The carrier is inhabited for every `q`**, by a proof using nothing about
`eigenphase`. -/
instance vacuousWitness (q : ℝ) : TransferMatrixEigenphase q where
  symmetrized_character_in_unit_disc := field1_holds_for_any_real _
  cos_eigenphase_bar_invariant := field2_holds_for_any_real _

/-- **The carrier is equivalent to `True`.**  Hence `[TransferMatrixEigenphase q] → P`
carries exactly the content of `P`; the hypothesis discharges itself. -/
theorem carrier_is_trivial (q : ℝ) : TransferMatrixEigenphase q ↔ True :=
  ⟨fun _ => trivial, fun _ => vacuousWitness q⟩

/-! ## §2 — a content-bearing replacement

A 2×2 real matrix has spectrum `{e^{+iα}, e^{−iα}}` exactly when its trace is
`2 cos α` and its determinant is `1` (the characteristic polynomial is then
`t² − 2cos(α)t + 1`, whose roots are `e^{±iα}`).  Stating *that* is what the
docstring of the existing class describes and its fields omit.

Unlike the original, this carrier is **falsifiable**: it constrains the matrix.
It is deliberately left with **no instance** — per AGENTS.md §3b-tax an unproved
primary is honestly represented by a content-bearing class with no instance, and
supplying a trivial one would reintroduce exactly the defect §1 documents. -/

/-- **Spectral identification of the β-decay transfer matrix** (content-bearing).

`M` is the transfer matrix restricted to the 2-d irrep `V_(2,1)` of `H₃(q)`.
The two fields pin its spectrum to `{e^{+iα}, e^{−iα}}` with `α = eigenphase q`.

Deliberately **uninstantiated**: this is the open input tranche S1 must supply,
and it is the statement a derivation of `α` would have to discharge. -/
class TransferMatrixSpectrum (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop where
  /-- The Markov-symmetrised single-wrap character is `2 cos α`. -/
  trace_eq : M.trace = 2 * Real.cos (eigenphase q)
  /-- Unimodular spectrum: `e^{+iα}·e^{−iα} = 1`. -/
  det_eq : M.det = 1

/-- Concrete non-vacuity witness: a matrix violating the trace condition admits
no instance.  Since `2 cos α ≤ 2 < 3`, the matrix `!![3, 0; 0, 0]` (trace `3`)
is excluded for every `q` — so the class is not satisfied by everything. -/
theorem replacement_excludes_some_matrix (q : ℝ) :
    ¬ (Matrix.trace !![(3 : ℝ), 0; 0, 0] = 2 * Real.cos (eigenphase q)) := by
  have hle : Real.cos (eigenphase q) ≤ 1 := cos_le_one _
  have htr : Matrix.trace !![(3 : ℝ), 0; 0, 0] = 3 := by
    simp [Matrix.trace_fin_two_of]
  rw [htr]
  nlinarith [hle]

/-! ## §3 — the obligation is a trichotomy, and §2 alone is not enough

**Self-correction.**  §2's `TransferMatrixSpectrum` is a genuine improvement on
the vacuous original — it constrains a *given* `M` (`replacement_excludes_some_matrix`).
But it is still not the right obligation, because it does not force `M` to come
from the Hecke data.  Exhibited below: for **every** `α` there is a matrix with
`trace = 2 cos α` and `det = 1`, namely the rotation `exp(αJ)` — built *from `α`
itself*.  So `TransferMatrixSpectrum` can be "discharged" circularly.

Putting that next to the route-3 exclusion
(`QOU.QBeta.Seminormal`, and `qbeta_eigenphase_seminormal_exclusion_probe.py`)
gives a three-way split with only one contentful branch:

1. **`M` in the braid image** — *excluded*.  Every character lies in
   `ℤ[q,q⁻¹] ⊂ ℚ(q,z)`, and `2cos((z−1)h/2)` is transcendental over `ℚ(q,z)`,
   so no such `M` exists as a functional identity.
   **🛑 The reason given here is the WRONG ONE — added 2026-09-04.**  The
   exclusion is real, but transcendence over `ℚ(q,z)` is an *unproved* docstring
   assertion: `BraidImageEigenphaseExclusion` calls it "the transcendence
   assertion", and `PhaseFailsLogFunctionalEquation` records it as "correct but
   needs transcendence theory".  What actually closes branch 1 is
   `BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos` — sorry-free,
   by zero-counting, and per its own docstring closing the character case *and*
   the eigenvalue-pair case.  Cite that.  Note its hypothesis: `α` surjective
   onto the non-positive reals, which the unbounded `(z−1)h/2` family supplies
   and a bounded `arccos` does not — "algebraic, therefore excluded" is not the
   statement.
2. **`M` arbitrary** — *circular*.  `rotationOfPhase` below satisfies the
   obligation for any `α` whatsoever, so it says nothing about the substrate.
3. **`M` an exponential/holonomy of an independently-defined connection whose
   monodromy reproduces the Hecke braiding** — the only remaining option, and
   the only one that could be contentful.  It escapes (1) because a holonomy is
   transcendental, and (2) because the connection is defined without reference
   to `α`, which is then *derived* as its holonomy angle rather than assumed.

Branch 3 is the Kohno–Drinfeld / KZ picture, and the corpus's canonical chain
already invokes exactly that shape ("Yekutieli non-abelian Stokes").  This file
does **not** carry out that construction; it establishes that it is the only
place a derivation of `α` can live.

**🛑 §3 IS SUPERSEDED IN ITS KOHNO–DRINFELD FORM — added 2026-09-04 (bean
`qou-xjh4`).**  The paragraph above is the text as written, kept because the
trichotomy's *structure* still stands and branches 1 and 2 are unaffected.  What
is no longer true is "branch 3 is the only place a derivation can live" read as
an endorsement of the Kohno–Drinfeld route: `QOU.QBeta.HolonomySpectrumSignObstruction`
(2026-08-31, `4471ee72ce`, 6 theorems, sorry-free, beans `qou-pdix` / `qou-cds1`)
**excludes every holonomy whose generator has real spectrum, Kohno–Drinfeld
included.**

The step is residue-independent, which is why it reaches the whole class rather
than one candidate: a real generator eigenvalue `a` gives character
`(eᵃ + e⁻ᵃ)/2 = cosh a ≥ 1` for *every* real `a`, so a `q`-dependent residue only
changes which `a` occurs.  The required correction factor is `0.998399` — below
1, hence unreachable.  At the Kohno–Drinfeld value itself, matching the braiding
`P exp(ħt/2)` to the Hecke eigenvalues `{q, −q⁻¹}` forces `ħ = 2 ln q`; `q₀ > 1`
is real, so that generator is **hyperbolic** (`det A = −(ln q₀)² < 0`) and gives
`1.005448` against the required `0.998399`.  The whole obstruction is
`(x−1)² ≥ 0`.

**Surviving ask, materially narrower:** not "find a connection" but "find one
whose generator is **elliptic** at real `q`" — `det A > 0`, spectrum `±iθ`,
`θ = 0.0565947` — so the imaginarity has to be sourced, and the corpus names
`conj:im-q-physical-role` as the candidate.  Recorded as tier-0 condition **D0**
on `qou-pdix`'s D1–D6 acceptance test.

Two things this does **not** say, matching the audit's own scope: it does not
show that no connection exists, and it does not derive `α`.

Recorded here because this file is cited as the authority on the trichotomy —
`nuclear-interactions/q-beta-cos-resummation.lean` quoted §3 on 2026-09-04 and
propagated "branch 3 is where a derivation must live" into three further places
before the obstruction was noticed.  A file that others cite has to carry its own
supersessions. -/

/-- The rotation `exp(αJ)`, `J² = −I`, written out. -/
noncomputable def rotationOfPhase (a : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![Real.cos a, -Real.sin a; Real.sin a, Real.cos a]

theorem rotationOfPhase_trace (a : ℝ) :
    (rotationOfPhase a).trace = 2 * Real.cos a := by
  simp [rotationOfPhase, Matrix.trace_fin_two_of]; ring

theorem rotationOfPhase_det (a : ℝ) : (rotationOfPhase a).det = 1 := by
  simp [rotationOfPhase, Matrix.det_fin_two_of]
  nlinarith [Real.sin_sq_add_cos_sq a]

/-- **The circularity, stated.**  `TransferMatrixSpectrum` is satisfiable for
every `q` — by a matrix built from the eigenphase itself.  So satisfying it is
not evidence about the substrate; the content is entirely in *which* `M`. -/
instance circularWitness (q : ℝ) :
    TransferMatrixSpectrum q (rotationOfPhase (eigenphase q)) where
  trace_eq := rotationOfPhase_trace _
  det_eq := rotationOfPhase_det _

end QOU.QBeta.EigenphaseCarrier
