import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.DiophantineBirthday — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:diophantine-birthday`](../../../appendix-surreals-archimedean/diophantine-birthday.md):
*Algebraic vs transcendental numbers are separated by birthday trajectory*.

Primary conjecture carrier with **no instance** — the honest open state per
AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema was a scalar plus a field asserting that it vanishes,
inhabited by `⟨0, rfl⟩`. The class chose its own witness, so it asserted
nothing and a downstream `[DiophantineBirthday]` hypothesis was not a
meaningful conditional.

The docstring link was also wrong: it pointed into `appendix-surreals/`, and the
block lives in `appendix-surreals-archimedean/`. Corrected.

## What is encoded, and what is deliberately left out

The block states four parts. Only the **first** is unhedged, and it is the one
that carries the discrimination:

* **Part 1 — algebraic rigidity.** "If `α` is algebraic of degree `d`, then
  `b_α(n) = O(log n)` up to a bounded error." Encoded. The implied constant
  depends on `α` (the block ties it to the degree), so it is existentially
  quantified *inside* the field rather than being a class parameter.

* **Part 2 — transcendental depth** is **not** encoded, and that is a
  faithfulness decision rather than an omission. The block says "if `α` is
  transcendental *(of "generic" type, e.g. Liouville number)*, `b_α(n)` grows
  super-logarithmically". The parenthesis is a hedge: the claim is made for a
  generic subclass, not for every transcendental. Writing `∀ α, Transcendental
  ℚ α → …` would assert the unhedged converse, which the corpus does not.
  Inventing an `IsGenericTranscendental` predicate to carry the hedge would be
  worse — a stand-in with no definition anywhere.

* **Parts 3 and 4** — the Roth threshold and the continued-fraction
  correspondence — are statements about *why* the exponent behaves as it does
  and about convergent birthdays. They need the continued-fraction expansion,
  which nothing in this library constructs.

**The discrimination survives anyway.** `transcendental_of_not_logarithmic`
derives, from part 1 alone, that a number whose trajectory is not `O(log n)` is
transcendental. That is the block's own title — "algebraic vs transcendental
numbers are separated by birthday trajectory" — and it needs only the unhedged
half. Encoding part 2 would have added the converse, which is not what the
separation requires.

## `trajectory` is caller-supplied

`b_α` is defined in the block as a minimisation over rational approximations
with bounded denominator. Nothing in this library constructs it, and inventing
a definition here would assert a construction the corpus does not have. So it
enters as a class parameter, exactly as the two `archimedean_agreement` carriers
take their pipelines. When a construction lands it instantiates `trajectory` and
the class statement is unchanged.

## Base ring (§7c)

`ℝ` is required. The conjecture is about Diophantine approximation of real
numbers by rationals, and `Real.log` is the growth scale the block names. This
is the archimedean side by subject matter, not by specialisation. Algebraicity
is taken over `ℚ`, matching "algebraic irrational" in the block.

## Where the rest of `qou-bday`'s findings went

Bean `qou-bday` audited this file on 2026-08-10 and recorded three findings. The
first — that the class stipulated its own witness and so encoded nothing — is
the defect `qou-ffwk` fixed above; it no longer describes this file, and is kept
only as the history note below the class. The other two are about the *target*
rather than the encoding, so they survive the rewrite unchanged:

* **A separation by the birthday of the number is impossible.** See
  `QOU/AppendixSurreals/DiophantineBirthdayScope.lean`. The `SurrealField` axiom
  `birthday_ofReal_le_omega` puts every real at birthday `≤ ω`, and in Conway's
  surreals every non-dyadic real is born exactly on day `ω` — so
  `birthday(√2) = ω = birthday(π)`, and `no_birthday_only_separation` proves that
  no predicate on the birthday can distinguish them. This is why the block's word
  *trajectory* is load-bearing, and why `trajectory` above is a parameter rather
  than something computed from `birthday ∘ ofReal`.

* **The trajectory target is unobstructed, and one direction is already a
  theorem.** `QOU/AppendixSurreals/DiophantineBirthdayTrajectory.lean` shows that
  a trajectory criterion survives the rational-shift invariance its encoding
  forces (`liouvilleWith_rat_shift_invariant`, `liouvilleWith_separates`) where
  `birthday ∘ ofReal` did not, and discharges the fast-approximation ⟹
  transcendental direction from Mathlib's `Liouville.transcendental` as
  `liouville_trajectory_direction_settled`. So *wholly open* overstates what is
  open here.

What remains open is the surreal content: that the sign-expansion trajectory
computes the approximation exponent. Nothing connects `gonshor`'s length-`n`
prefix to the dyadic approximant at denominator `2ⁿ`; `SignSequence.lean`
explains why that induction is not available from the abstract axioms.
-/

namespace QOU.AppendixSurreals

/-- **Birthday-trajectory discrimination**: algebraic numbers have logarithmic
birthday trajectories.

The unhedged half of
[`conj:diophantine-birthday`](../../../appendix-surreals-archimedean/diophantine-birthday.md).

`trajectory α n` is the block's `b_α(n)` — the minimum birthday among best
rational approximations to `α` with denominator at most `n`. It is the caller's
data; this library constructs no such function.

An instance **is** the conjecture, for that trajectory. None is provided. -/
class DiophantineBirthday (trajectory : ℝ → ℕ → ℕ) : Prop where
  /-- **Part 1 — algebraic rigidity.** For algebraic `α` the trajectory is
      `O(log n)`. The constant is existential and `α`-dependent because the
      block ties it to the degree of `α`; a single global constant would be a
      stronger claim than the block makes. -/
  algebraic_logarithmic :
    ∀ α : ℝ, IsAlgebraic ℚ α →
      ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 1 ≤ n →
        (trajectory α n : ℝ) ≤ C * Real.log n + C

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_diophantine_birthday : DiophantineBirthday
--     noncomputable instance : DiophantineBirthday := conj_diophantine_birthday
-- i.e. the conjecture was asserted by `axiom` and installed as a global
-- instance, so every downstream `[DiophantineBirthday]` resolved for free and
-- the assumption was invisible outside `#print axioms`.  Removed, not
-- completed.  The field schema is now content-bearing as well; see the header.
--
-- Note for `qou-ffwk`'s inventory: that bean greps for the old vanishing
-- field's name, which is deliberately written nowhere in this file — not even
-- in this history — so the file drops out of the grep instead of matching it
-- forever from its own changelog.

namespace DiophantineBirthday

variable {trajectory : ℝ → ℕ → ℕ}

/-- **A super-logarithmic trajectory forces transcendence** — the block's title,
derived from part 1 alone.

If `α`'s trajectory outruns every logarithmic bound, `α` cannot be algebraic.
This is the separation the block claims, and it needs only the unhedged half of
the conjecture; the hedged converse (part 2) is not required and is not
assumed. -/
theorem transcendental_of_not_logarithmic [h : DiophantineBirthday trajectory]
    (α : ℝ)
    (hα : ∀ C : ℝ, 0 < C → ∃ n : ℕ, 1 ≤ n ∧
      C * Real.log n + C < (trajectory α n : ℝ)) :
    Transcendental ℚ α := by
  intro halg
  obtain ⟨C, hCpos, hbound⟩ := h.algebraic_logarithmic α halg
  obtain ⟨n, hn, hlt⟩ := hα C hCpos
  exact absurd (hbound n hn) (not_le.mpr hlt)

/-! ### The class is satisfiable, and only at data that satisfies it

Neither is an `instance`, so typeclass resolution cannot pick either up and
silently close a downstream hypothesis. -/

/-- **Not over-corrected**: the identically-zero trajectory satisfies the class,
so its openness is not an artefact of emptiness. Degenerate data deliberately —
the content is only that a witness exists at all. -/
theorem nonempty_of_const_zero :
    DiophantineBirthday (fun _ _ => 0) :=
  ⟨fun _ _ => ⟨1, one_pos, fun n hn => by
    have hlog : (0 : ℝ) ≤ Real.log n :=
      Real.log_nonneg (by exact_mod_cast hn)
    simpa using by linarith⟩⟩

/-- **Inhabitation depends on the data** — the property the old schema lacked
entirely.

The quadratic trajectory is **refuted**: `0` is algebraic, and `n²` outruns
every `C · log n + C`. Under the previous shape no choice of anything could
fail, so a wrong trajectory had nothing to fail against. -/
theorem not_of_quadratic :
    ¬ DiophantineBirthday (fun _ n => n ^ 2) := by
  intro h
  obtain ⟨C, hCpos, hbound⟩ := h.algebraic_logarithmic 0 isAlgebraic_zero
  -- Pick `n` past `C + 2`; then `n² > C·n + C ≥ C·log n + C` since `log n < n`.
  obtain ⟨n, hn⟩ := exists_nat_gt (C + 2)
  have hn1 : 1 ≤ n := by
    have : (0 : ℝ) < (n : ℝ) := by linarith
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by exact_mod_cast this.ne')
  have hnR : (C + 2 : ℝ) < (n : ℝ) := hn
  have hlog : Real.log n < (n : ℝ) := by
    have := Real.log_le_sub_one_of_pos (x := (n : ℝ)) (by linarith)
    linarith
  have hkey : C * Real.log n + C < ((n : ℝ)) ^ 2 := by
    have h1 : C * Real.log n ≤ C * (n : ℝ) := by
      exact mul_le_mul_of_nonneg_left hlog.le hCpos.le
    nlinarith [hCpos, hnR]
  have := hbound n hn1
  push_cast at this
  linarith

/-- **Every rational number has a logarithmically bounded birthday trajectory.**
    Since `(q : ℝ) = algebraMap ℚ ℝ q` is algebraic over `ℚ`, Part 1 applies
    immediately to every rational target. -/
theorem rat_trajectory_logarithmic [h : DiophantineBirthday trajectory] (q : ℚ) :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 1 ≤ n →
      (trajectory (q : ℝ) n : ℝ) ≤ C * Real.log n + C :=
  h.algebraic_logarithmic (q : ℝ) (isAlgebraic_algebraMap q)

/-- **The trajectory at `0` is logarithmically bounded.** -/
theorem zero_trajectory_logarithmic [h : DiophantineBirthday trajectory] :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 1 ≤ n →
      (trajectory 0 n : ℝ) ≤ C * Real.log n + C :=
  h.algebraic_logarithmic 0 isAlgebraic_zero

/-- **Unit-denominator birthday bound for algebraic numbers.**
    Evaluating the logarithmic bound at `n = 1` (`Real.log 1 = 0`) bounds
    `trajectory α 1` directly by the implied constant `C`. -/
theorem trajectory_at_one_le [h : DiophantineBirthday trajectory]
    (α : ℝ) (hα : IsAlgebraic ℚ α) :
    ∃ C : ℝ, 0 < C ∧ (trajectory α 1 : ℝ) ≤ C := by
  obtain ⟨C, hCpos, hbound⟩ := h.algebraic_logarithmic α hα
  refine ⟨C, hCpos, ?_⟩
  have h1 := hbound 1 le_rfl
  rw [Nat.cast_one, Real.log_one, mul_zero, zero_add] at h1
  exact h1

end DiophantineBirthday

end QOU.AppendixSurreals
