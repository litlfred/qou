import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.NormNum

/-!
# QOU.ParticleInteractions.atomic_lp_stability — bare H is LP-unstable, dressed H is stable

**Proposition** ([`prop:atomic-lp-stability`](../../../nuclear-interactions/atomic-lp-stability.md)).

*The bare hydrogen atom `[e, 𝔭] = σ₀⁻¹` in `H₂(q)` is LP-unstable:
there exists a Markov-normalised operator `X* = α · 𝟙 + β · σ₀`
that annihilates the traced volume (`V = 0`). The 𝓑₃ dressing
(proton internal structure) stabilises the atom: the annihilation
ratio `λ_s / λ_a` changes from `0.537` (bare) to `q⁻¹⁰` (dressed),
so the original annihilator `X*` cannot satisfy the dressed
condition.*

## 2026-09-03 — the docstring described a repair that was never made

This module's header used to say:

> *"Carries the genuine **inputs** … but **not** the conclusion."*
>
> *"Those two facts are therefore stated faithfully and end in `sorry`
> (disposition B)."*

Neither sentence described the code beneath it.  `AtomicLPStabilityContext`
carried **both** conclusions as fields — `bare_unstable` and
`dressed_stable`, each the theorem's statement verbatim — and both theorems
ended in the projection, not in `sorry`.  This is the fourth file in this
drain whose prose asserts the repair while the code does the opposite
(cf. `QOU.Archimedean.knot_operator_selection`,
`QOU.BraidsKnots.skein_mass_from_linking`,
`QOU.Interactions.nucleon_ordering_factorization`).

## The class was inhabitable by junk, and that is now proved

Every other field was data too — `Candidate` is a bare `Type`, and
`normalised`, `bareVolume`, `dressedVolume` are functions the instance
supplies.  So an instance could pick `Candidate := Unit`, `normalised := fun
_ => True`, `bareVolume := fun _ => 0`, `dressedVolume := fun _ => 1`, and
satisfy both "conclusions" with data that has nothing to do with hydrogen,
`H₂(q)`, or a Markov trace.  `atomic_lp_stability_of_junk_data` below
exhibits exactly that instance, so a `[AtomicLPStabilityContext]` binder is
demonstrably not an assumption about anything.

`not_atomic_lp_stability_of_junk_data` gives the other half: the same
carrier type with `bareVolume := fun _ => 1` refutes it.  **Satisfiable and
refutable at freely-chosen data** is the sharpest statement of what the
claim constrains without the Hecke content — nothing.

That is also why `sorry` (disposition B, as the old docstring proposed)
would have been unsound: it reads as "true, not yet proved" over a statement
that is false at free data.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`atomic_lp_stability` is now a **`Prop`-valued definition over
caller-supplied data**.  A caller who has actual `H₂(q)` candidate operators
and Markov pairings supplies them and takes this as a hypothesis, and it
constrains them because the data are theirs.  `bare_is_lp_unstable` and
`dressed_is_lp_stable` remain, as the two halves of that hypothesis — the
legitimate accessor idiom, since what they destructure is something the
caller brought rather than something an instance chose.

## What is still open, and what is proved

**Open, stated rather than implied:** both annihilator-existence facts.  They
are claims about the kernel of a `2 × 2` Markov-trace pairing on `H₂(q)` and
need the Iwahori–Hecke representation theory and Markov-trace machinery — the
eigenvalue structure of `σ₀`, the `(q, −q⁻¹)` versus `(q⁵, −q⁻⁵)` channels —
which the `QOU` library does not carry.  Nothing here constructs `σ₀`, the
pairing, or the Markov normalisation.

**Proved sorry-free:** `annihilation_ratios_distinct`, the arithmetic
mechanism linking the two — the bare and dressed ratios are numerically
distinct, so no single Markov-normalised `X*` can annihilate both volumes.

That result is now stated for **every** `q > 1.1` rather than at one
hard-coded substrate literal.  The old version pinned
`1.109978595554181` — the CODATA-2018 muon derivation — into the statement,
which per AGENTS.md §q₀-anchor is not the default pin and, more to the point,
was never needed: the proof only ever used `q > 1.1`, so the conclusion is
**pin-independent**.  `annihilation_ratios_distinct` instantiates it at the
substrate value and the choice of anchor can no longer affect it.

Bean `qou-z9ws`.
-/

namespace QOU.ParticleInteractions

/-- Bare-hydrogen annihilation ratio `λ_s / λ_a` (Markov-trace
    eigenvalue ratio of `σ₀` in the degree-2 representation). -/
def bareAnnihilationRatio : ℝ := 0.537

/-- Dressed (𝓑₃-twisted) annihilation ratio `q⁻¹⁰` at the substrate
    value `q_0 ≈ 1.109978595554181`. Numerically `≈ 0.352`. -/
noncomputable def dressedAnnihilationRatio : ℝ := (1.109978595554181 : ℝ) ^ (-10 : ℤ)

/-- **The mechanism, pin-independently.**  For *any* `q > 1.1` the dressed
    ratio `q⁻¹⁰` differs from the bare ratio `0.537`.

    `q > 1.1` gives `q¹⁰ > 1.1¹⁰ > 2.5`, hence `q⁻¹⁰ < 0.4 < 0.537`.  The
    substrate anchor never enters, which is the point: the claim does not
    depend on which `q₀` pin is in force. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-lp-stability.md
theorem bare_ne_dressed_ratio (q : ℝ) (hq : (1.1 : ℝ) < q) :
    bareAnnihilationRatio ≠ q ^ (-10 : ℤ) := by
  unfold bareAnnihilationRatio
  have hq0 : (0 : ℝ) < q := by linarith
  rw [zpow_neg, zpow_ofNat]
  have hle : (1.1 : ℝ) ^ 10 ≤ q ^ 10 := by gcongr
  have h10 : (2.5 : ℝ) < q ^ 10 := by nlinarith [hle]
  have hpos : (0 : ℝ) < q ^ 10 := by positivity
  have hinv : (q ^ 10 : ℝ)⁻¹ < 0.4 := by
    rw [inv_lt_iff_one_lt_mul₀ hpos]; nlinarith
  intro hc
  rw [← hc] at hinv
  norm_num at hinv

/-- The bare and dressed annihilation ratios are numerically distinct.

    The substrate instance of `bare_ne_dressed_ratio`; sorry-free, and no
    longer sensitive to which `q₀` pin the literal records. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-lp-stability.md
theorem annihilation_ratios_distinct :
    bareAnnihilationRatio ≠ dressedAnnihilationRatio :=
  bare_ne_dressed_ratio _ (by norm_num)

/-- **The claim of `prop:atomic-lp-stability`**, as a proposition over
caller-supplied data:

* there is a Markov-normalised candidate annihilating the **bare** traced
  volume (the bare hydrogen atom is LP-unstable), and
* there is none annihilating the **dressed** volume (the 𝓑₃ dressing
  stabilises it).

**Named, not asserted.**  See the module docstring for why neither a
projection nor a `sorry` is the honest form here. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP feasibility / kernel of constraint matrix)
-- Ref: [wenzl1990] https://doi.org/10.1007/BF02097372 (Markov trace / dressed eigenvalue channels)
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-lp-stability.md
def atomic_lp_stability {Candidate : Type}
    (normalised : Candidate → Prop)
    (bareVolume dressedVolume : Candidate → ℝ) : Prop :=
  (∃ X : Candidate, normalised X ∧ bareVolume X = 0) ∧
  (¬ ∃ X : Candidate, normalised X ∧ dressedVolume X = 0)

/-- Bare hydrogen is LP-unstable — the first half of the hypothesis. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-lp-stability.md
theorem bare_is_lp_unstable {Candidate : Type} {normalised : Candidate → Prop}
    {bareVolume dressedVolume : Candidate → ℝ}
    (h : atomic_lp_stability normalised bareVolume dressedVolume) :
    ∃ X : Candidate, normalised X ∧ bareVolume X = 0 := h.1

/-- The 𝓑₃ dressing stabilises the atom — the second half of the
hypothesis. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/atomic-lp-stability.md
theorem dressed_is_lp_stable {Candidate : Type} {normalised : Candidate → Prop}
    {bareVolume dressedVolume : Candidate → ℝ}
    (h : atomic_lp_stability normalised bareVolume dressedVolume) :
    ¬ ∃ X : Candidate, normalised X ∧ dressedVolume X = 0 := h.2

/-- **The claim is satisfied by data that has nothing to do with hydrogen.**

One candidate, always normalised, bare volume identically `0` and dressed
volume identically `1`.  No `σ₀`, no `H₂(q)`, no Markov trace.

This is the precise statement of what was wrong with carrying the two
conclusions as class fields: an instance could choose exactly this, so a
`[AtomicLPStabilityContext]` binder assumed nothing whatever. -/
theorem atomic_lp_stability_of_junk_data :
    atomic_lp_stability (Candidate := Unit) (fun _ => True) (fun _ => 0) (fun _ => 1) := by
  refine ⟨⟨(), trivial, rfl⟩, ?_⟩
  rintro ⟨_, -, h⟩
  norm_num at h

/-- **And it is refutable at freely-chosen data**, which is why it is named
rather than carried as a `sorry`.

Same carrier, bare volume identically `1`: nothing annihilates it, so the
first conjunct fails.  Together with `atomic_lp_stability_of_junk_data` this
pins the content of the statement without the Hecke machinery — satisfiable
and refutable, hence constraining nothing about the atom. -/
theorem not_atomic_lp_stability_of_junk_data :
    ¬ atomic_lp_stability (Candidate := Unit) (fun _ => True) (fun _ => 1) (fun _ => 1) := by
  rintro ⟨⟨_, -, h⟩, -⟩
  norm_num at h

end QOU.ParticleInteractions
