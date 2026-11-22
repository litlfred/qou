import Mathlib.Algebra.Polynomial.Laurent
import QOU.Archimedean.EmSpectralCompleteness
import QOU.Archimedean.ForceCarrierBringUniqueness


/-!
# QOU.Archimedean.gram_determinant_plancherel_ratio

The Chern-Simons Gram-determinant ratio `κ` appearing in the EM
coupling correction has a closed-form Plancherel-weighted character
expression — no 2-jet hand calculation needed.

  κ = ∏_λ [(dim V_λ / dim_q V_λ) · ([n]_q! / n!)]^{c_λ^(s)·c_λ^(w)}

where `c_λ^(•) = χ_λ(β_•)` are the central-idempotent character
coefficients of the genus-4 torus knots `T_{2,9}` (strong) and
`T_{3,5}` (weak).

LaTeX label: `conj:gram-determinant-plancherel-ratio`

## References

- [leitner2026] §5/gram-determinant-plancherel-ratio
- [jones1987] https://doi.org/10.2307/1971403 — Jones polynomial of torus knots
-/

namespace QOU.Archimedean

/-- A formal placeholder for the central-idempotent character
    coefficients of a braid `β` in `H_n(q)`. -/
structure CharacterDecomposition (n : ℕ) where
  partitions : Finset (List ℕ)         -- partitions of n
  chi : List ℕ → ℝ                     -- χ_λ(β) for each λ ⊢ n
  dim_classical : List ℕ → ℕ           -- dim V_λ
  dim_quantum : List ℕ → ℝ             -- dim_q V_λ at q = q_0

/-- The Plancherel-weighted character product. -/
noncomputable def gramKappa (n : ℕ)
    (q_factorial : ℝ) (n_factorial : ℝ)
    (cs : CharacterDecomposition n)
    (cw : CharacterDecomposition n) : ℝ :=
  cs.partitions.prod fun lam =>
    let dim_cl := (cs.dim_classical lam : ℝ)
    let dim_q := cs.dim_quantum lam
    let exponent := cs.chi lam * cw.chi lam
    ((dim_cl / dim_q) * (q_factorial / n_factorial)) ^ exponent

/-- **Proposition (closed-form κ via Plancherel weights)**.

    The Gram-determinant ratio appearing in the Chern-Simons descent
    is given by the Plancherel-weighted character product over
    Wedderburn blocks `λ ⊢ n`, with no 2-jet hand calculation.

    **🛑 THE STATEMENT BELOW DOES NOT CARRY THAT CLAIM — flagged 2026-09-05,
    not rewritten.** It concludes `∃ κ : ℝ, κ = gramKappa …`, which is true for
    *any* right-hand side whatsoever (`⟨a, rfl⟩`, verified) and says nothing
    about the Chern–Simons Gram ratio. The docstring's content — that the CS
    ratio EQUALS this product — needs a term denoting that ratio, and this file
    has none; `gramKappa` is a definition, so "something equals it" is not a
    theorem about it.

    Left in place rather than restated because supplying that term is a design
    decision in this arc's owner's hands, not a mechanical repair.

    **Correction (2026-09-05).** This said "no detector flags this", and that
    was wrong — I asserted an absence without running the corpus-grep
    checklist. `∃ x, x = e := ⟨e, rfl⟩` is a NAMED class with a DEDICATED
    detector since 2026-08-07: `scripts/lean-vacuous-existential-audit.py`,
    written up in `docs/audits/2026-08-07-lean-vacuous-existential-audit.md`
    (17 found, and the ten then-live have since been drained).

    What is true is narrower and sharper. That detector could not see THIS
    declaration because its bound-variable pattern was `[A-Za-z_][A-Za-z0-9_']*`
    — ASCII-only — and this one binds `κ`. So it reported `0 candidates in 0
    files`, which reads as a clean corpus. Widening the pattern to Unicode on
    the same tree the same day reports **8 in 3 files**, every one bound to a
    Greek name. Nothing had been drained; they had never been seen. The
    detector is fixed and now carries a `--self-test` so a future narrowing
    cannot report zero silently.

    The live audit (`content/pipeline/lean-vacuity-axiom-audit.ts`) still does
    not flag this, and that part is correct as stated: its nearest criterion,
    `proof-no-unused-hypothesis-rfl`, needs an UNUSED binder, and every binder
    here is consumed by `gramKappa n q_factorial n_factorial cs cw`. -/
-- Ref: [leitner2026] §5/gram-determinant-plancherel-ratio
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem gram_determinant_plancherel_ratio
    (n : ℕ) (q_factorial n_factorial : ℝ)
    (cs cw : CharacterDecomposition n) :
    ∃ κ : ℝ, κ = gramKappa n q_factorial n_factorial cs cw := by
  exact ⟨gramKappa n q_factorial n_factorial cs cw, rfl⟩

-- The docstring that stood here belonged to the removed axiom. It is dropped rather than
-- left dangling, because a doc comment attached to nothing followed by another doc comment
-- is a parse error — the SAME failure this very docstring recorded having survived once
-- before ("two docstrings cannot both attach to one declaration, so the file did not
-- parse"). Removing the axiom without it reproduced that error exactly; caught by
-- lean-direct, not by inspection.
--
-- Its one piece of unique content — that the value is `κ ≈ 1.722` at `q₀ ≈ 1.1097` for the
-- genus-4 torus pair `(T_{2,9}, T_{3,5})` — is carried in the replacement theorem's
-- docstring below, which is now the only place it is stated. Its self-description as an
-- "external axiom (§3b-cond pattern)" was inaccurate: §3b-cond axiomatises a conjecture's
-- HYPOTHESES as a class taken by an explicit `[Instance]` binder, whereas this was a bare
-- `axiom` asserting a provable existential with no binder and no class.
-- REMOVED 2026-09-05: `axiom gram_kappa_numerical_value_axiom : ∃ (κ : ℝ), |κ - 1.722| < 0.001`
--
-- It was an `axiom`, and it was PROVABLE — `⟨1.722, by norm_num⟩` closes it, verified
-- lean-direct exit 0. Take κ = 1.722 and |κ − 1.722| = 0 < 0.001. So it assumed something
-- that needs no assuming.
--
-- Worse than redundant, it was VACUOUS AS A PHYSICAL CLAIM. The docstring said "at the
-- substrate value q₀ ≈ 1.1097 for the genus-4 torus pair (T_{2,9}, T_{3,5}), κ ≈ 1.722",
-- but the statement bound `κ` by an existential unconnected to `gramKappa` — no `q`, no
-- `n`, no torus pair, no character data. It asserted only that SOME real lies within
-- 0.001 of 1.722, which 1.722 does. AGENTS.md: "Never launder empirical fits through
-- Lean axioms."
--
-- Restated below as the claim the docstring actually makes: `gramKappa` at the torus-pair
-- data is within 0.001 of 1.722. That statement is FALSIFIABLE — it constrains the
-- product — and it is not proved here, so it carries `sorry` per §1a disposition 2
-- ("state the REAL proposition with `sorry` + a `-- Ref:` citation").
--
-- 2026-11-20: that restatement was itself FALSE (its predicate is a universally
-- quantified parameter, so `fun _ _ => True` is a legal instance). It is replaced by
-- `gram_kappa_numerical_value_refuted` below, which proves the negation.

/-- **The proposition formerly queued here behind `sorry` is FALSE (2026-11-20).**

    Until 2026-11-20 this file carried

    ```
    theorem gram_kappa_numerical_value
        (n : ℕ) (q_factorial n_factorial : ℝ)
        (cs cw : CharacterDecomposition n)
        (IsTorusPairAtQ0 : CharacterDecomposition n → CharacterDecomposition n → Prop)
        (h_torus_pair : IsTorusPairAtQ0 cs cw)
        : |gramKappa n q_factorial n_factorial cs cw - 1.722| < 0.001
    ```

    with its proof left as a placeholder.

    Its docstring rejected an earlier draft because a `(h : True)` hypothesis makes
    the statement universally quantified over the character data, hence false. The
    abstract-predicate version has the same defect one level up: the predicate is
    itself a universally quantified PARAMETER, so a caller may pass
    `fun _ _ => True`, and the statement is again the universal closure. This
    theorem proves its negation: empty character data give `gramKappa = 1`
    (empty product), and `|1 − 1.722| = 0.722`. So the `sorry` could never be
    discharged. It is removed and this refutation stands in its place.

    **Where 1.722 actually comes from.** It is the CS Gram-determinant ratio
    `det G_cl / det G_q` (`def:cs-gram-determinant-ratio`), evaluated at the
    proton pin by `meson_em_sinh_closed_form._alpha_em_inv_derived`:
    `κ_gram(q₀) = 1.7216142017088`
    (`computations/probes/alpha_em_two_term_q0_pull_probe.py`, 70 dps). That number
    does not use `gramKappa` at all. The conjectured identification of the two
    objects is not well-typed as written (the torus knots live in `H₂` and `H₃`,
    the exponents are not integers, `T_{3,5}` is not central — see
    `docs/audits/2026-11-15-sidecar-review-mass-theory/route-other.md` row 16),
    so no `sorry` is queued for it: a well-typed statement has to be designed
    first. Bean `qou-wkgp`. -/
theorem gram_kappa_numerical_value_refuted :
    ¬ (∀ (n : ℕ) (q_factorial n_factorial : ℝ) (cs cw : CharacterDecomposition n)
        (IsTorusPairAtQ0 : CharacterDecomposition n → CharacterDecomposition n → Prop),
        IsTorusPairAtQ0 cs cw →
        |gramKappa n q_factorial n_factorial cs cw - 1.722| < 0.001) := by
  intro h
  have h1 := h 0 1 1 ⟨∅, fun _ => 0, fun _ => 0, fun _ => 0⟩
    ⟨∅, fun _ => 0, fun _ => 0, fun _ => 0⟩ (fun _ _ => True) trivial
  have h2 : gramKappa 0 1 1 ⟨∅, fun _ => 0, fun _ => 0, fun _ => 0⟩
      ⟨∅, fun _ => 0, fun _ => 0, fun _ => 0⟩ = 1 := by
    simp [gramKappa]
  rw [h2, abs_lt] at h1
  norm_num at h1

end QOU.Archimedean
