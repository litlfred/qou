import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# QOU.BraidKnot.QBetaCKClosedForms

**Closed-form conjectures for c_4, c_5, c_6, c_7 in the Q_β precision ladder.**

The framework PROVES c_3 = J_Hopf(q=1) = -2 via 2-strand sub-braid
extraction (`prop:q-beta-c3-hopf-three-fold-markov`, Fact 3). The
higher rungs c_4..c_7 have empirical closed forms with sub-percent
residuals but no first-principles categorical derivation.

This file axiomatises those closed forms as a single conjecture
class. Per AGENTS.md §3b-cond, downstream provable claims taking
`[QBetaCKClosedForms]` as a hypothesis are rigorous conditional
results modulo this conjecture.

The existing `QBetaPrecisionLadderCoefficients` class in
`q-beta-categorical-precision-ladder.lean` is the natural
integration point: its `qBetaPrecisionLadderCoeffsCanonical`
instance provides the empirical closed forms; this conjecture
formalises the condition under which those instance values are
PROVED rather than FIT.
-/

-- Ref: [khovanov2000] Khovanov, doi:10.1215/S0012-7094-00-10131-7 (Khovanov homology)
-- Ref: [khovanov-rozansky2008] Khovanov-Rozansky, doi:10.4064/fm199-1-1 (matrix factorisations)
-- Ref: [khovanovlauda2009] Khovanov-Lauda, doi:10.1090/S1088-4165-09-00346-X (KLR algebras)
-- Ref: [wenzl1988] doi:10.1007/BF01404457 (Hecke Markov trace)
-- Ref: [hoefsmit1974] (Hoefsmit seminormal forms)
-- Ref: [jones1985] doi:10.2307/1971403 (Hopf-link Jones polynomial)

/-- Hoefsmit off-diagonal coupling on V_(2,1) at H_3(q).
    Re-stated here to keep this conjecture file self-contained;
    the canonical definition lives in
    `q-beta-categorical-precision-ladder.lean`. -/
noncomputable def hoefsmitB (q : ℝ) : ℝ :=
  Real.sqrt (q^4 + q^2 + 1) / (q^2 + 1)

namespace QOU.BraidKnot

/-- **Conjecture: closed forms for c_4..c_7 in the Q_β precision ladder.**

Empirical pattern-matches verified at q_0 to sub-percent residuals
(c_4 0.9%, c_5 2.4%, c_6 14%; c_7 signed-error +114% at leverage
limit). First-principles derivation via Khovanov-Rozansky polynomial
at finite q, or KLR canonical-basis Markov trace formula, remains
open research-grade work.

The class encodes the four conjectured closed forms as functions of
q. The **`def`** `defaultQBetaCKClosedForms` records these — the
`closed_form_*` equations carry the conjectural content and would
need `sorry` if treated as provable lemmas. The class itself does
NOT carry a `sorry`; it just encodes the closed-form CONVENTION.
Downstream theorems taking `[QBetaCKClosedForms]` as a hypothesis
are conditional on this convention being right.

**`defaultQBetaCKClosedForms` is deliberately a `def`, NOT an
`instance`** (demoted 2026-09-14, bean `qou-hjf4`). Its field values
are FITTED — the residuals are in the paragraph above — so as a
parameterless global `instance` it was resolved by instance search
for every `[QBetaCKClosedForms]` binder, which made each
"conditional" downstream result unconditional **on a fit**. That is
the shape AGENTS.md §"Axiomatization is NOT a Proof" rule 2 forbids,
and it is the same demotion `ClassicalLimitStpart` received on
2026-08-24. The class is therefore **uninhabited by instance search**,
which is the honest encoding of an open conjecture; `def` keeps the
values citable by name without discharging anything. -/
class QBetaCKClosedForms where
  /-- Hopf Jones at q=1, the c_3 anchor (derived, not conjectural). -/
  c_3 : ℝ
  c_3_eq : c_3 = -2
  /-- Conjectured c_4 closed form: c_3 · b(q)^4. -/
  c_4 : ℝ → ℝ
  c_4_closed_form : ∀ q, c_4 q = c_3 * (hoefsmitB q)^4
  /-- Conjectured c_5 closed form: −(b(q)² + 1/2). -/
  c_5 : ℝ → ℝ
  c_5_closed_form : ∀ q, c_5 q = -((hoefsmitB q)^2 + 1/2)
  /-- Conjectured c_6 closed form: c_3² · b(q)² = 4·b(q)². -/
  c_6 : ℝ → ℝ
  c_6_closed_form : ∀ q, c_6 q = c_3^2 * (hoefsmitB q)^2
  /-- Conjectured c_7 closed form: c_3³ = -8 (low confidence;
      signed-error +114% at empirical q_0; retained as pattern
      guess at the N=7 leverage limit). -/
  c_7 : ℝ
  c_7_closed_form : c_7 = c_3^3

/-- **Canonical witness** recording the conjectured closed forms.

    The `closed_form_*` equations are discharged by `rfl` against
    the chosen forms — this is NOT a derivation, just the
    encoding of the conjectural assignment.

    **`def`, not `instance`, and that is load-bearing.** These values
    are fitted. As a parameterless global `instance` this was found by
    instance search for every `[QBetaCKClosedForms]` binder in scope,
    so `qbeta_c_k_closed_forms_derived` below — stated as a §3b-cond
    conditional — was in practice discharged against a fit. Demoted
    2026-09-14 (bean `qou-hjf4`); do not restore the `instance`
    keyword without first deriving these forms. -/
noncomputable def defaultQBetaCKClosedForms : QBetaCKClosedForms where
  c_3 := -2
  c_3_eq := rfl
  -- Ref: [leitner2026] prop:q-beta-categorical-precision-ladder § c_4 row
  c_4 := fun q => -2 * (hoefsmitB q)^4
  c_4_closed_form := fun _ => rfl
  -- Ref: [leitner2026] prop:q-beta-categorical-precision-ladder § c_5 row
  c_5 := fun q => -((hoefsmitB q)^2 + 1/2)
  c_5_closed_form := fun _ => rfl
  -- Ref: [leitner2026] prop:q-beta-categorical-precision-ladder § c_6 row
  c_6 := fun q => (-2 : ℝ)^2 * (hoefsmitB q)^2
  c_6_closed_form := fun _ => rfl
  -- Ref: [leitner2026] prop:q-beta-categorical-precision-ladder § c_7 row
  c_7 := (-2 : ℝ)^3
  c_7_closed_form := rfl

-- Ref: [leitner2026] conj:qbeta-c-k-closed-forms
/-- **The canonical instance realises the conjectured `c_4`, `c_5` closed
    forms.** This records that `defaultQBetaCKClosedForms` evaluates to the
    empirical closed forms `c_4 = -2·b(q)^4` and `c_5 = -(b(q)^2 + 1/2)`;
    it is a bookkeeping identity over the instance, NOT a first-principles
    derivation. The genuinely-open claim (deriving these from the categorical
    Markov trace) is carried as the conjectural content of the
    `QBetaCKClosedForms` class itself, whose instance values are FIT, not
    proved. -/
theorem qbeta_c_k_closed_forms_of_instance (q : ℝ) :
    defaultQBetaCKClosedForms.c_4 q = -2 * (hoefsmitB q)^4 ∧
      defaultQBetaCKClosedForms.c_5 q = -((hoefsmitB q)^2 + 1/2) :=
  ⟨rfl, rfl⟩

/-- **Conjecture (open): first-principles derivation of the `c_k` closed
    forms.** That the empirical closed forms recorded above arise from the
    categorical Markov trace (Khovanov–Rozansky polynomial at finite `q`, or
    a KLR canonical-basis Markov-trace formula) rather than being fitted is
    open research-grade work.

    **Correction (2026-08-09): this docstring previously said the content is
    "stated as a conjecture carrier so the `sorry` is honest 'open'". There
    is no `sorry` here.** The body is
    `⟨inst.c_4_closed_form q, inst.c_5_closed_form q⟩` — both conjuncts
    projected verbatim from the `QBetaCKClosedForms` instance argument; the
    prose and the code disagreed about the mechanism, which is the
    `proof-docstring-sorry-mismatch` defect (a reader auditing the prose
    records a queued gap, a reader running `#print axioms` records a proof).
    The honest description: this is a conditional restatement of the class
    fields, open because nothing inhabits the class.

    **Second correction (2026-09-14, bean `qou-hjf4`): that last clause was
    FALSE when it was written.** `defaultQBetaCKClosedForms`, 49 lines above,
    was a parameterless global `instance`, so instance search discharged the
    `[inst : QBetaCKClosedForms]` binder here — and its values are fitted.
    The 2026-08-09 correction fixed the `sorry` half of the mismatch and left
    a second, larger one standing: the file's own class docstring named that
    instance in the same breath as this docstring denied it existed. The
    clause is now true because the declaration was demoted to a `def`, not
    because it was ever accurate. Nothing downstream was laundered — measured
    2026-09-14, the class and both theorems here are referenced by **no other
    file** and this module has no importer — so the defect was contained to
    this file's self-description. -/
-- Ref: [leitner2026] conj:qbeta-c-k-closed-forms
-- Ref: [khovanov-rozansky2008] doi:10.4064/fm199-1-1
theorem qbeta_c_k_closed_forms_derived
    [inst : QBetaCKClosedForms] (q : ℝ) :
    inst.c_4 q = inst.c_3 * (hoefsmitB q)^4 ∧
      inst.c_5 q = -((hoefsmitB q)^2 + 1/2) :=
  ⟨inst.c_4_closed_form q, inst.c_5_closed_form q⟩

end QOU.BraidKnot
