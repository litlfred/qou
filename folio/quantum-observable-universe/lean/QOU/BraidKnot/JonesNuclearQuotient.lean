/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# QOU.BraidKnot.JonesNuclearQuotient — the nuclear quotient braid Jones value

Infrastructure for the **open Part-4** of
[`conj:jet-filtered-knot-factor`](../../../quantum-observable-universe/mass-theory/jet-filtered-knot-factor.md):
the Bethe–Weizsäcker knot factor `a(Z,N)` is *conjectured* to equal the Jones
polynomial `J_β̄(q)` of the **nuclear quotient braid** `β̄` — each nucleon
collapsed to one effective inter-nucleon crossing (the quotient tracks the
`A(A−1)/2` inter-nucleon crossings, suppressing internal nucleon structure). The
conjecture's `.md` maps the quotient knot type by shell structure:

  odd `Z`        → trefoil   `(2,3)` torus link
  even `Z`       → Hopf link `(2,2)` torus link
  double-magic   → unknot    `(2,1)` torus link

This file builds the **RHS** `jonesQuotient` of that conjecture: the Jones value
of the `(2,k)` torus link as the Markov trace `tr_M(σ₁^k)` in `H_n(q)`, plus the
shell-structure classifier `Z,N ↦ k ∈ {1,2,3}` selecting which torus link a
nucleus maps to. Per AGENTS.md §"Axiomatization is NOT a Proof", **constructing
the RHS is infrastructure, not closure** — this does NOT prove `a(Z,N)` *equals*
`jonesQuotient` (`jet_filtered_knot_factor.factor_is_jones` stays the open §3b
conjecture). It only supplies a concrete, compute-verified realisation of the
conjecture's right-hand side so downstream work can test the identification.

## The `(2,k)` torus-link Jones values (compute-verified)

In `H_2(q)` with the Hecke relation `σ² = h·σ + 1` (`h = q − q⁻¹`, AGENTS.md
§7a), `σ^k = a_k·σ + b_k` with `(a_0,b_0)=(0,1)`,
`(a_{k+1},b_{k+1}) = (h·a_k + b_k, a_k)`. The Markov trace is
`tr_M(σ^k) = a_k·z + b_k` with the canonical Markov parameter
`z = 1/(√q + 1/√q)` (`MarkovTraceTower`), giving

  unknot  `(2,1)`:  `z`
  Hopf    `(2,2)`:  `h·z + 1`
  trefoil `(2,3)`:  `(h²+1)·z + h`

The `k=2` value **coincides with** `JonesViaMarkovTrace.jonesHopf` — the already
formalised & verified Hopf closed form `(q^{5/2}−q^{1/2}+q²+q)/(q²+q)`. The
algebraic identity `h·z + 1 = (q^{5/2}−q^{1/2}+q²+q)/(q²+q)` is **sympy-verified**
(the difference simplifies to `0`), which is what pins the recursion into the
framework's Markov normalisation; the three closed forms above are cross-checked
in `computations/deltalambda/nuclear_quotient_jones_torus_link_probe.py`
(+ witness). The formal `rpow`-normalisation bridge lemma
`jonesHopfLink_eq_jonesHopf` (`h·z + 1 = jonesHopf`) is now **proved sorry-free**
below — the `Real.sqrt`↔`rpow` rewriting is discharged via `Real.sqrt_eq_rpow`
+ `Real.sq_sqrt`, both sides reducing to `√q − 1/√q + 1`.

Base ring (§7c): the Markov parameter and trace values are archimedean
(`Real.sqrt q`, `q > 1` Wenzl regime), so this file is legitimately `ℝ`-valued.

Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-filtered-knot-factor.md
-/
import QOU.BraidKnot.JonesViaMarkovTrace
import Mathlib.Data.List.Basic

namespace QOU.BraidKnot.JonesNuclearQuotient

open QOU.Braiding

/-- The Hecke parameter `h = q − q⁻¹` (AGENTS.md §7a: `σ² = h·σ + 1`). -/
noncomputable def heckeH (q : ℝ) : ℝ := q - 1 / q

/-- The canonical Markov parameter in **convention D**, `z = q³/(q² + 1)` — the
    same value carried by `markovTraceTower_canonical`.

    **Migrated from convention C 2026-08-26 (bean `qou-cxjq`).** This read
    `1/(√q + 1/√q)` = `√q/(q+1)`, convention C. The "same value carried by
    `markovTraceTower_canonical`" clause is why this file had to move in the same
    tranche as that instance: the tower migrated to D first, which made this
    docstring's claim FALSE for exactly as long as the two disagreed. A
    cross-reference between two same-named quantities is only as good as the
    convention they share. -/
noncomputable def markovZ (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- **Jones value of the unknot** `= (2,1)` torus link `= tr_M(σ₁) = z`. -/
noncomputable def jonesUnknot (q : ℝ) : ℝ := markovZ q

/-- **Jones value of the Hopf link** `= (2,2)` torus link `= tr_M(σ₁²) = h·z + 1`.
    Coincides with `JonesViaMarkovTrace.jonesHopf` (sympy Δ = 0). -/
noncomputable def jonesHopfLink (q : ℝ) : ℝ := heckeH q * markovZ q + 1

/-- **Jones value of the trefoil** `= (2,3)` torus link
    `= tr_M(σ₁³) = (h²+1)·z + h`. -/
noncomputable def jonesTrefoil (q : ℝ) : ℝ := (heckeH q ^ 2 + 1) * markovZ q + heckeH q

/-- **The Hopf-value bridge**: the `(h·z + 1)` Hopf value here equals the
    canonical closed form `jonesHopf` of [`JonesViaMarkovTrace`].

    **Under convention D this stopped needing an `rpow` normalisation at all**
    (2026-08-26, bean `qou-cxjq`). It used to be "the `rpow`-normalisation
    bridge, previously deferred pending the LSP": both sides reduced to
    `√q − 1/√q + 1`, and the proof had to convert `Real.sqrt q ↔ q ^ (1/2 : ℝ)`,
    establish `q ^ (5/2) = q² · √q`, and clear denominators around a square root.

    Under D both sides are the *same rational function* `(q⁴ + 1)/(q² + 1)` — the
    Markov axiom fixes `tr_M(σ₁²) = h·z + 1`, and at `z = q³/(q²+1)` that is
    exactly the tower's migrated `trM_sigma1_sq`. The square roots are gone from
    both, so the bridge is `field_simp; ring`.

    Worth noting against the general expectation that a convention migration costs
    proof effort: here it *removed* a proof obligation that had been deferred. -/
theorem jonesHopfLink_eq_jonesHopf (q : ℝ) (hq : 1 < q) :
    jonesHopfLink q = jonesHopf q (T := markovTraceTower_canonical q hq) := by
  rw [jonesHopf_canonical q hq]
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hq' : q ≠ 0 := ne_of_gt hq0
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  unfold jonesHopfLink heckeH markovZ
  field_simp
  ring

/-- The nuclear magic numbers (closed-shell nucleon counts). -/
def magicNumbers : List ℕ := [2, 8, 20, 28, 50, 82, 126]

/-- Whether `n` is a magic number (closed shell). -/
def isMagicNumber (n : ℕ) : Bool := magicNumbers.contains n

/-- **Crossing power `k` of the nuclear quotient braid** `β̄`, per
    `jet-filtered-knot-factor.md`: `1` (unknot) if double-magic, else `2` (Hopf)
    if `Z` even, else `3` (trefoil, `Z` odd). -/
def nuclearCrossingPower (Z N : ℕ) : ℕ :=
  if isMagicNumber Z = true ∧ isMagicNumber N = true then 1
  else if Z % 2 = 0 then 2 else 3

/-- The crossing power is always one of the three torus-link indices `{1,2,3}`. -/
theorem nuclearCrossingPower_mem (Z N : ℕ) :
    nuclearCrossingPower Z N = 1 ∨ nuclearCrossingPower Z N = 2 ∨
      nuclearCrossingPower Z N = 3 := by
  unfold nuclearCrossingPower
  split
  · exact Or.inl rfl
  · split
    · exact Or.inr (Or.inl rfl)
    · exact Or.inr (Or.inr rfl)

/-- **The nuclear quotient braid Jones value** — the RHS of the (open) Part-4
    conjecture `a(Z,N) = J_β̄(q)`. Selects the `(2,k)` torus-link Jones value by
    the shell-structure crossing power `k = nuclearCrossingPower Z N`. This is the
    concrete construction of `jet_filtered_knot_factor.jonesQuotient`; it does
    **not** assert equality with the BW knot factor `a(Z,N)` (the open
    conjecture). -/
noncomputable def nuclearQuotientJones (q : ℝ) (Z N : ℕ) : ℝ :=
  if nuclearCrossingPower Z N = 1 then jonesUnknot q
  else if nuclearCrossingPower Z N = 2 then jonesHopfLink q
  else jonesTrefoil q

/-- A **double-magic** nucleus maps to the unknot value. -/
theorem nuclearQuotientJones_doubleMagic (q : ℝ) (Z N : ℕ)
    (hZ : isMagicNumber Z = true) (hN : isMagicNumber N = true) :
    nuclearQuotientJones q Z N = jonesUnknot q := by
  have hk : nuclearCrossingPower Z N = 1 := by
    unfold nuclearCrossingPower; rw [if_pos ⟨hZ, hN⟩]
  simp [nuclearQuotientJones, hk]

/-- An **even-`Z`, non-double-magic** nucleus maps to the Hopf-link value. -/
theorem nuclearQuotientJones_evenZ (q : ℝ) (Z N : ℕ)
    (hmagic : ¬ (isMagicNumber Z = true ∧ isMagicNumber N = true))
    (hZ : Z % 2 = 0) :
    nuclearQuotientJones q Z N = jonesHopfLink q := by
  have hk : nuclearCrossingPower Z N = 2 := by
    unfold nuclearCrossingPower; rw [if_neg hmagic, if_pos hZ]
  simp [nuclearQuotientJones, hk]

/-- An **odd-`Z`, non-double-magic** nucleus maps to the trefoil value. -/
theorem nuclearQuotientJones_oddZ (q : ℝ) (Z N : ℕ)
    (hmagic : ¬ (isMagicNumber Z = true ∧ isMagicNumber N = true))
    (hZ : ¬ Z % 2 = 0) :
    nuclearQuotientJones q Z N = jonesTrefoil q := by
  have hk : nuclearCrossingPower Z N = 3 := by
    unfold nuclearCrossingPower; rw [if_neg hmagic, if_neg hZ]
  simp [nuclearQuotientJones, hk]

/-! ### Positivity in the Wenzl regime `q > 1`

All three torus-link Jones values are positive for `q > 1` (so `nuclearQuotientJones`
is positive, a valid normalisation), mirroring `JonesViaMarkovTrace.jonesHopf_pos`. -/

theorem markovZ_pos (q : ℝ) (hq : 0 < q) : 0 < markovZ q := by
  unfold markovZ
  positivity

theorem heckeH_pos (q : ℝ) (hq : 1 < q) : 0 < heckeH q := by
  unfold heckeH
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have h1 : 1 / q < 1 := by rw [div_lt_one hq0]; exact hq
  linarith

theorem jonesUnknot_pos (q : ℝ) (hq : 1 < q) : 0 < jonesUnknot q :=
  markovZ_pos q (lt_trans zero_lt_one hq)

theorem jonesHopfLink_pos (q : ℝ) (hq : 1 < q) : 0 < jonesHopfLink q := by
  unfold jonesHopfLink
  have h1 := heckeH_pos q hq
  have h2 := markovZ_pos q (lt_trans zero_lt_one hq)
  have h3 : 0 < heckeH q * markovZ q := mul_pos h1 h2
  linarith

theorem jonesTrefoil_pos (q : ℝ) (hq : 1 < q) : 0 < jonesTrefoil q := by
  unfold jonesTrefoil
  have h1 := heckeH_pos q hq
  have h2 := markovZ_pos q (lt_trans zero_lt_one hq)
  have h3 : 0 < heckeH q ^ 2 + 1 := by positivity
  have h4 : 0 < (heckeH q ^ 2 + 1) * markovZ q := mul_pos h3 h2
  linarith

/-- **`nuclearQuotientJones` is positive** in the Wenzl regime — every branch of
    the selection is a positive torus-link value. -/
theorem nuclearQuotientJones_pos (q : ℝ) (hq : 1 < q) (Z N : ℕ) :
    0 < nuclearQuotientJones q Z N := by
  unfold nuclearQuotientJones
  split
  · exact jonesUnknot_pos q hq
  · split
    · exact jonesHopfLink_pos q hq
    · exact jonesTrefoil_pos q hq

end QOU.BraidKnot.JonesNuclearQuotient
