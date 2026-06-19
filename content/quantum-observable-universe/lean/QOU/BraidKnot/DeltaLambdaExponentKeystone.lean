/-
  Δ_λ binding exponent — keystone (formalize-first, arithmetic core only)

  Owner-directed research item 1 (PR #2485). The per-isotope Δ_λ binding
  exponent is currently a RAW combinatorial crossing count off the atom
  braid word `atom_braid_word_3A(Z, N)`
  (`computations/delta_lambda_exponent_from_crossings.py`):

      σ   = 7Z + 5N − 1      (positive crossings)
      σ⁻¹ = 3Z + 5N − 1      (negative crossings)
      σ + σ⁻¹ = 10A − 2      (Z, N cancel ⇒ slope 10 / nucleon, derived)

  This file formalizes ONLY what is genuinely derived: the crossing-sum
  cancellation and the factorization 5·(2A−1) = 10A−5. These are pure
  arithmetic facts about the crossing bookkeeping; they make NO claim that
  the binding exponent equals them.

  The bridge from the crossing count to the binding exponent — the per-site
  "5" (Bring-quintic degree) and per-nucleon "9" (intra-𝓑₃ count) reading —
  is OPEN and, per `docs/audits/2026-06-15-delta-lambda-q5-per-site-
  mechanism-start.md`, in EMPIRICAL TENSION: the literal q₀^{5(2A−1)}
  exponent overpredicts the measured B_sym/B_lin ratio by 3×→145× and the
  exponent that actually fits is ≈ 1.4 per site, not 5. It is therefore
  recorded below as a `conjecture` (sorry = conjecture, per CLAUDE.md §3b),
  NOT a theorem, with the magnitude caveat in its docstring.

  Audit: docs/audits/2026-06-19-delta-lambda-exponent-keystone-formalize-first.md

  -- Ref: [manuscript] appendix-mass-binding-algorithms, Step 9b (Δ_λ);
  --      docs/audits/2026-06-15-delta-lambda-q5-per-site-mechanism-start.md

  Imports: none — `omega` and `unfold` are core Lean 4 tactics, so this
  arithmetic-core file is self-contained and does not depend on Mathlib.
-/

namespace QOU.BraidKnot

/-- Positive (proton-walk) crossings in the atom braid word for `Z` protons,
`N` neutrons. Closed form from `atom_braid_word_3A`. -/
def protonCrossings (Z N : Nat) : Nat := 7 * Z + 5 * N - 1

/-- Negative (neutron-interface) crossings in the atom braid word. -/
def neutronCrossings (Z N : Nat) : Nat := 3 * Z + 5 * N - 1

/-- **Derived.** The proton and neutron crossing counts sum to `10A − 2`
(`A = Z + N`): the `Z`/`N` coefficients cancel, giving the slope of 10
crossings per nucleon. Requires at least one nucleon (`1 ≤ Z + N`) so the
truncated `ℕ` subtractions are exact. -/
theorem crossing_sum_cancels (Z N : Nat) (h : 1 ≤ Z + N) :
    protonCrossings Z N + neutronCrossings Z N = 10 * (Z + N) - 2 := by
  unfold protonCrossings neutronCrossings
  omega

/-- **Derived (pure arithmetic).** The per-site factorization: `10A − 5`
factors as `5·(2A − 1) = 5 × (A nucleon-sites + (A−1) bond-sites)`. This is
the arithmetic *shape* of the asserted per-site reading; it does not assert
that the binding exponent equals it. -/
theorem exponent_factorization (A : Nat) (h : 1 ≤ A) :
    5 * (2 * A - 1) = 10 * A - 5 := by
  omega

/-- The contested bridge claim, as a precise predicate (not asserted true):
the Δ_λ binding `q₀`-exponent for an isotope with `A` nucleons equals
`5·(2A − 1)` — i.e. exactly `5` per chain-site. Stated so the conjecture
below has a name; the truth value is open. -/
def perSiteFiveClaim (A bindingExponent : Nat) : Prop :=
  bindingExponent = 5 * (2 * A - 1)

/-- **Conditional restatement (proved; the conjectural content is the
hypothesis).** *If* the Δ_λ binding exponent equals `10A − 5`, then the
per-site-`5` claim `perSiteFiveClaim` holds — this direction is the pure
arithmetic factorization. The file asserts nothing about whether the
hypothesis `hexp` is true.

⚠ The hypothesis `hexp` (binding exponent = `10A − 5`, i.e. `5` per chain-
site) is exactly the OPEN, magnitude-contested claim — it is supplied here,
not proved. Two layers of doubt:
1. *Underived.* Why each chain-site contributes exactly `5` (the Bring
   quintic degree) is not derived from the jet order (Step 8) or the
   Gröbner–Shirshov normal form (Step 7); the crossing count merely asserts
   it.
2. *Empirically contested.* Per `2026-06-15-delta-lambda-q5-per-site-
   mechanism-start.md`, the literal `q₀^{5(2A−1)}` exponent overpredicts the
   measured `B_sym/B_lin` ratio by 3×→145×; the fitted exponent is ≈ 1.4 per
   site, consistent with an exp-vs-linear (Kashaev) correction, not a
   `q₀`-power.

The honest next step is to measure the per-site exponent from real compute
before chasing the complex-q mechanism for "why 5". Keeping the contested
claim as a *hypothesis* (rather than a `sorry`-conjecture asserting it) avoids
enshrining a refuted near-match while still recording the precise statement.

  -- Ref: [manuscript] docs/audits/2026-06-19-delta-lambda-exponent-keystone-formalize-first.md
-/
theorem perSiteFive_of_exponent_eq (A bindingExponent : Nat) (h : 1 ≤ A)
    (hexp : bindingExponent = 10 * A - 5) :
    perSiteFiveClaim A bindingExponent := by
  unfold perSiteFiveClaim
  omega

end QOU.BraidKnot
