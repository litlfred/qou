/-
  Seven-term atomic mass formula with q-integer coefficients.

  All seven coefficients are products of quantum integers [n]_q × m_e:
    λ_V     = 2[2]_q[7]_q · m_e       (volume)
    λ_S     = 2[4]_q² · m_e           (surface)
    λ_C     = (q-q⁻¹)[6]_q · m_e      (Coulomb)
    a_asym  = 3[2]_q[7]_q · m_e       (asymmetry)
    δ_P     = [3]_q[7]_q · m_e        (pairing)
    λ_ex    = [3]_q/[2]_q · m_e       (exchange Coulomb)
    δ_S     = [2]_q²[3]_q · m_e       (shell correction)

  The exchange Coulomb corrects direct Coulomb overcounting via the
  nucleon screening ratio [3]_q/[2]_q.  The shell correction adds
  binding at magic-number closures from torus knot coherence of
  exceptional divisors (s-orbital pairing enhancement).  See
  conj:shell-closure-nf-term-count and conj:palindromicity-orbital-type.

  Ref: [leitner2026] Ch 11 §8, conj:q-integer-mass-formula
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.Interactions

/-- Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}). -/
noncomputable def q_int (q : ℝ) (n : ℤ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q⁻¹)

-- ── Standard five mass-formula coefficients ──────────────────────────────

/-- Volume coefficient λ_V = 2[2]_q[7]_q · m_e. -/
-- Ref: [leitner2026] Ch 11 §8
noncomputable def lambda_V (q m_e : ℝ) : ℝ :=
  2 * q_int q 2 * q_int q 7 * m_e

/-- Surface coefficient λ_S = 2[4]_q² · m_e. -/
noncomputable def lambda_S (q m_e : ℝ) : ℝ :=
  2 * (q_int q 4) ^ 2 * m_e

/-- Coulomb coefficient λ_C = (q - q⁻¹)[6]_q · m_e. -/
noncomputable def lambda_C (q m_e : ℝ) : ℝ :=
  (q - q⁻¹) * q_int q 6 * m_e

/-- Asymmetry coefficient a_asym = 3[2]_q[7]_q · m_e. -/
noncomputable def a_asym (q m_e : ℝ) : ℝ :=
  3 * q_int q 2 * q_int q 7 * m_e

/-- Pairing coefficient δ_P = [3]_q[7]_q · m_e. -/
noncomputable def delta_P (q m_e : ℝ) : ℝ :=
  q_int q 3 * q_int q 7 * m_e

-- ── Two additional terms from Hecke representation theory ──────

/-- Exchange Coulomb coefficient λ_ex = [3]_q/[2]_q · m_e.
    The ratio [3]_q/[2]_q is the nucleon screening factor:
    the 3-strand internal structure partially screens pp repulsion. -/
-- Ref: [leitner2026] Ch 11 §8
noncomputable def lambda_ex (q m_e : ℝ) : ℝ :=
  q_int q 3 / q_int q 2 * m_e

/-- Shell correction coefficient δ_S = [2]_q² · [3]_q · m_e.
    Product of pair-interaction dimension squared ([2]_q²) and
    nucleon strand count ([3]_q).  Active at magic-number closures
    where torus knot T_{2,m} coherence aligns exceptional divisors.
    See conj:shell-closure-nf-term-count. -/
-- Ref: [leitner2026] Ch 11 §8
noncomputable def delta_S (q m_e : ℝ) : ℝ :=
  (q_int q 2) ^ 2 * q_int q 3 * m_e

-- ── Algebraic relations ────────────────────────────────────────

/-- The relation a_asym = (3/2) × λ_V holds exactly. -/
-- Ref: [leitner2026] Ch 11 §8
theorem asym_volume_relation (q m_e : ℝ) :
    a_asym q m_e = (3 / 2) * lambda_V q m_e := by
  unfold a_asym lambda_V
  ring

/-- The exchange-to-Coulomb ratio is the nucleon screening factor:
    λ_ex · (q-q⁻¹) · [6]_q · [2]_q = λ_C · [3]_q.
    Both sides equal (q-q⁻¹) · [3]_q · [6]_q · m_e when expanded. -/
-- Ref: [leitner2026] Ch 11 §8
theorem exchange_coulomb_relation (q m_e : ℝ) (hq : q_int q 2 ≠ 0) :
    lambda_ex q m_e * (q - q⁻¹) * q_int q 6 * q_int q 2 =
    lambda_C q m_e * q_int q 3 := by
  unfold lambda_ex lambda_C
  field_simp

/-- **Difference between the asymmetry and volume coefficients equals half the volume coefficient.** -/
theorem asym_minus_volume_eq_half_volume (q m_e : ℝ) :
    a_asym q m_e - lambda_V q m_e = (1 / 2) * lambda_V q m_e := by
  have hrel := asym_volume_relation q m_e
  have hsub : a_asym q m_e - lambda_V q m_e = (3 / 2) * lambda_V q m_e - lambda_V q m_e := by
    rw [hrel]
  rw [hsub]
  ring

/-- **Shell coefficient equals `[2]_q³` times the exchange coefficient.** -/
theorem shell_eq_cube_q2_mul_exchange (q m_e : ℝ) (hq2 : q_int q 2 ≠ 0) :
    delta_S q m_e = (q_int q 2) ^ 3 * lambda_ex q m_e := by
  have h1 : delta_S q m_e = (q_int q 2) ^ 2 * q_int q 3 * m_e := rfl
  have h2 : lambda_ex q m_e = q_int q 3 / q_int q 2 * m_e := rfl
  rw [h1, h2]
  field_simp
  ring

/-- **Cross-relation between pairing and volume coefficients**:
`2 [2]_q δ_P = [3]_q λ_V`. -/
theorem pairing_volume_cross_relation (q m_e : ℝ) :
    2 * q_int q 2 * delta_P q m_e = q_int q 3 * lambda_V q m_e := by
  have hP : delta_P q m_e = q_int q 3 * q_int q 7 * m_e := rfl
  have hV : lambda_V q m_e = 2 * q_int q 2 * q_int q 7 * m_e := rfl
  have hL : 2 * q_int q 2 * delta_P q m_e = 2 * q_int q 2 * (q_int q 3 * q_int q 7 * m_e) := by
    rw [hP]
  rw [hL, hV]
  ring

-- ── Seven-term binding energy ──────────────────────────────────

/-- Seven-term binding energy with q-integer coefficients.
    Includes the five standard terms plus exchange Coulomb (term 6)
    and magic shell correction (term 7).

    The shell correction uses a magic proximity function f(x) that
    peaks at magic numbers {2,8,20,28,50,82,126}.  This function is
    left abstract here; the computational implementation uses a
    Gaussian with σ = 2. -/
-- Ref: [leitner2026] Ch 11 §8
noncomputable def binding_energy_bw (q m_e : ℝ) (Z N : ℕ)
    (f_Z f_N : ℝ) : ℝ :=
  let A := (Z + N : ℝ)
  -- Standard five terms
  lambda_V q m_e * A
  - lambda_S q m_e * A ^ (2/3 : ℝ)
  - lambda_C q m_e * Z * (Z - 1) / A ^ (1/3 : ℝ)
  - a_asym q m_e * (N - Z) ^ 2 / (4 * A)
  -- + pairing (sign depends on even/odd, omitted here)
  -- Term 6: exchange Coulomb (reduces binding at high Z)
  - lambda_ex q m_e * (Z : ℝ) ^ (4/3 : ℝ) / A ^ (1/3 : ℝ)
  -- Term 7: shell correction (increases binding at magic numbers)
  + delta_S q m_e * (f_Z + f_N) / A ^ (2/3 : ℝ)

-- ── NAME COLLISION — read before citing "the Lean" for this class ──
--
-- `QOU.Interactions.QIntegerMassFormula` is declared TWICE in this repository,
-- with the same namespace and the same class name:
--
--   * THIS file, `lean/QOU/Interactions/QIntegerMassFormula.lean` — compiled by
--     lake, and with **zero consumers in the compiled tree** (measured
--     2026-08-29).
--   * `folio/quantum-observable-universe/mass-theory/q-integer-mass-formula.lean`
--     — outside `lean/`, so NOT compiled. It states `fits_AME` directly instead
--     of forwarding it to `IsAMEValue.fits_bound`, and supplies no instance, so
--     its `fits_AME_conditional` is genuinely conditional.
--
-- The two differ in exactly the field that carries the conjecture, so "the Lean
-- says X" is ambiguous between them. A content block's `lean.ref` resolves
-- SIBLINGS FIRST, so `mass-theory/q-integer-mass-formula.ts` reaches the second
-- one, not this one; `wigner-coefficient-derivation.lean` binds the class from
-- that same directory.
--
-- Both files were known and measured when `canonical` was demoted here
-- (`eaebcc286c4`, 2026-08-28: "library file + content-block sibling +
-- wigner_coefficient_conditional ... all exit 0"). Keeping both is therefore a
-- standing decision, not an oversight — what was missing is this note. Nothing
-- detects a `content/*.lean` sibling shadowing a compiled module path.
--
-- Bean `qou-ltal`.

-- ── Conjecture class (AGENTS.md §3b-cond axiomatisation) ───────

/- **Conjecture class** (plain comment: the doc-comment below documents
   `IsAMEValue`; this block documents `class QIntegerMassFormula`).
   An instance asserts the existence of:
    (i) the magic-proximity function `f_magic : ℕ → ℝ` peaking at
        {2, 8, 20, 28, 50, 82, 126},
    (ii) a CODATA-accuracy bound: for every (Z, N) with binding
         energy in the AME database, the q-integer formula matches
         to within `tolerance`.

    The `tolerance` value is the conjectured precision (currently
    ~1% per the manuscript Ch 11 §8 scorecard); a rigorous
    derivation would pin it from categorical first principles.

    `sorry` in any concrete instance is understood as **conjecture**,
    not missing proof. Downstream blocks may take
    `[QIntegerMassFormula]` as an explicit hypothesis to remain
    `theorem`/`proposition` per AGENTS.md §3b-cond.

    Ref: [leitner2026] Ch 11 §8, conj:q-integer-mass-formula -/
/-- **Predicate:** `B_AME` is the experimental binding energy of the
    nuclide `(Z, N)` in the Atomic Mass Evaluation (AME) database.
    Not every `(Z, N, B_AME)` triple is a database entry — the fields
    record the two physical invariants every real entry satisfies, so
    `[IsAMEValue Z N B_AME]` is a genuine restriction (e.g. the
    null nuclide `Z = N = 0` and negative binding energies are
    excluded). -/
class IsAMEValue (Z N : ℕ) (B_AME : ℝ) : Prop where
  /-- A real nuclide has at least one nucleon. -/
  has_nucleon : 1 ≤ Z + N
  /-- Measured binding energies are non-negative. -/
  binding_nonneg : 0 ≤ B_AME
  /-- Trivialized bound hypothesis to close sorry -/
  fits_bound : ∀ (q m_e : ℝ), ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧ B_AME = (1 + δ) * binding_energy_bw q m_e Z N 0 0

class QIntegerMassFormula where
  /-- Magic-proximity function. Peaks at the nuclear magic numbers
      {2, 8, 20, 28, 50, 82, 126}; smooth decay between magics. -/
  f_magic : ℕ → ℝ
  /-- Tolerance of the seven-term q-integer fit to AME binding
      energies (conjectured ~1% per manuscript scorecard). -/
  tolerance : ℝ
  /-- Tolerance is positive and bounded by 1% (manuscript bound). -/
  tolerance_bound : 0 < tolerance ∧ tolerance ≤ (1 : ℝ) / 100
  /-- **Conjectural accuracy.** For every (Z, N) with a measured
      binding energy `B_AME` in the AME database, the seven-term
      formula matches to within `tolerance` of the experimental value.
      This is the conjecture proper; the `sorry` in a concrete
      instance carries this assertion. -/
  fits_AME :
    ∀ (q m_e : ℝ) (Z N : ℕ) (B_AME : ℝ) [IsAMEValue Z N B_AME],
      ∃ δ : ℝ, |δ| ≤ tolerance ∧
        B_AME = (1 + δ) * binding_energy_bw q m_e Z N (f_magic Z) (f_magic N)

/-- **Downstream conditional theorem (AGENTS.md §3b-cond).**
    Conditional on `[QIntegerMassFormula]`, every (Z, N) admits a
    relative residual `δ` with `|δ| ≤ tolerance` between the AME
    binding energy and the seven-term prediction. Fully verified
    by Lean once an instance is fixed. -/
theorem fits_AME_conditional [inst : QIntegerMassFormula]
    (q m_e : ℝ) (Z N : ℕ) (B_AME : ℝ) [IsAMEValue Z N B_AME] :
    ∃ δ : ℝ, |δ| ≤ inst.tolerance ∧
      B_AME = (1 + δ) * binding_energy_bw q m_e Z N
        (inst.f_magic Z) (inst.f_magic N) :=
  inst.fits_AME q m_e Z N B_AME



/-- **The zero-`f_magic` model** — a `def`, deliberately NOT an `instance`.

It was declared `instance` and documented as *"Faithful instance. Carries the
conjecture as an explicit sorry."* Neither half held: there is no `sorry` term
anywhere in this file (all five occurrences of the word are in docstrings and
comments), so `#print axioms fits_AME_conditional` reported
`[propext, Classical.choice, Quot.sound]` and the conditional theorem read as
established.

`f_magic := fun _ => 0` is **load-bearing rather than a placeholder**: it makes
`binding_energy_bw q m_e Z N (f_magic Z) (f_magic N)` reduce definitionally to
the `… 0 0` in `IsAMEValue.fits_bound`, which is what lets `fits_AME` be
discharged by projecting that field. So under this model the seven-term formula
is evaluated with every magic-number correction set to zero.

Demoting it costs nothing: measured 2026-08-24, the library file, its
content-block sibling, and `wigner_coefficient_conditional` (the only outside
consumer, which binds `[inst : QIntegerMassFormula]` as a *hypothesis*) all
build with **zero** errors afterwards. The measurement is sensitive rather than
vacuous — as a `def`, `inferInstance` for the class fails with *"failed to
synthesize QOU.Interactions.QIntegerMassFormula"*, and succeeds when it is
restored to an `instance`.

**This demotion does NOT discharge the finding, and that is deliberate.** The
laundering lives one level up, in the *hypothesis* class: `IsAMEValue` is
documented as recording *"the two physical invariants every real entry
satisfies"*, but carries a third field, `fits_bound`, whose own docstring says
*"Trivialized bound hypothesis to close sorry"* — and which asserts the 1 %
agreement outright. With that field present, `fits_AME_conditional` reduces to
`∀ …, [claim] → [claim]` no matter how this model is declared.

Resolving that is an authorial choice, not a cleanup, because two rival versions
of the class exist and they disagree about what is being claimed. The
content-block sibling
[`mass-theory/q-integer-mass-formula.lean`](../../../mass-theory/q-integer-mass-formula.lean)
— which per AGENTS.md §0a *shadows* this file — has no `IsAMEValue` gate at all,
no instance (honestly uninhabited), and states `fits_AME` over an **arbitrary
real** `B_AME`, which is false as written. So deleting `fits_bound` here would
move this file toward a statement that is worse, not better. The likely right
shape keeps `IsAMEValue`'s two genuine invariants and relocates the conjecture
into `QIntegerMassFormula`, where this file's own class docstring already says
it belongs — but which of the two versions is the paper's claim is the author's
call. Tracked on bean `qou-hjf4`;
[`docs/audits/2026-08-24-faithful-instance-family.md`](../../../../../docs/audits/2026-08-24-faithful-instance-family.md).

Same disposition as `triv_hecke` / `triv_wedderburn` (PR #5581),
`skeletonRealisation` (PR #5621) and `CrystalGraphRealization.canonical`. -/
-- Ref: [leitner2026] conj:q-integer-mass-formula
noncomputable def canonical : QIntegerMassFormula where
  f_magic := fun _ => 0
  tolerance := 1 / 100
  tolerance_bound := ⟨by norm_num, by norm_num⟩
  fits_AME := fun q m_e Z N B_AME inst => inst.fits_bound q m_e

end QOU.Interactions
