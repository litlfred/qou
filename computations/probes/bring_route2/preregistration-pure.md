# Route 2: giving pure braids a Bring loop, and the energy of a sum of braids (pre-registration)

Written 2026-10-11, before anything in Part A was computed. On that day the owner picked "1 2 3 4" on the options after `results_signed.md`. Part A carries out option 2: fix route 2's rule so that pure braids, the γγ core among them, get a loop. Part B carries out option 3, but only as far as writing the options down; it computes nothing. Nothing here reads Q_β, CODATA, a mass or any target.

## 0. What is already known

- **γγ words.** On three strands every γγ word is (σ₀σ₁⁻¹)^k. Its image in SL(2,ℤ) is the Fibonacci matrix [[2,1],[1,1]]^k, with trace 3, 7, 18, 47, 123, 322 for k = 1 to 6.
- **The strand permutation.** For 3 ∤ k it is a 3-cycle. For 3 | k it is the identity, i.e. the braid is pure.
- **What route 2 currently does.** `preregistration.md` §1.4 says: use g itself if the permutation fixes exactly one point of P¹(F₂); otherwise use g^m, with m the order of the permutation. A pure braid is then "three classes, out of scope". So a 3-cycle braid is cubed into a pure one, and is then out of scope as well. (`option1_ropelength_probe.route2_row` dropped the cubing step. It reports "no loop" directly, which gives the same final answer.)
- **No Bring length of any pure braid has been computed.**

## Part A: the rule for pure braids (fixed now)

**A1. Three placements.** A pure braid g lies in all three conjugates of Γ₀(2), one for each point p ∈ {∞, 0, 1} of P¹(F₂). For each p, conjugate by `H_TO_INF[p]` and run steps 5–7 of `preregistration.md` §1 unchanged: into H₄, Rosen reduction, then Δ(2,4,5), r, and L.

**A2. The verdict.**
- **If the three lengths L_∞, L₀, L₁ agree to 25 digits**, that common value is the Bring loop length of g.
- **Otherwise g is "ambiguous"**: all three values are reported and none is chosen. The same applies if some placements give a loop and some do not.

**A3. Non-pure braids whose permutation fixes no point (3-cycles).** As in `preregistration.md` §1.4, use g³, which is pure, and apply A1 and A2 to it. Both L(g³) and L(g³)/3 are reported. The second is shown only so that lengths of words of different length can be read side by side. It is not used to compare anything.

**A4. Applied to:**
- (σ₀σ₁⁻¹)^k for k = 1 … 6 (via A3 when 3 ∤ k);
- the 8 signed nucleon terms of `results_signed.md`. They fix exactly one point, so A changes nothing for them, and they serve as a regression check.

**A5. Checks.**
1. On the 8 nucleon terms, A1 restricted to the single fixed point reproduces `results_signed.json` to 25 digits.
2. For each pure braid, each of the three conjugated matrices really lies in Γ₀(2), i.e. c ≡ 0 (mod 2).
3. **Consistency of A3:** for (σ₀σ₁⁻¹)^k with 3 ∤ k, the value of g³ equals the A1/A2 value of (σ₀σ₁⁻¹)^{3k}, which is computed directly as a pure braid.
4. mpmath only, at 80 dps in R2; no float64.

**What a result would mean.** If the γγ core gets a well-defined loop, it can then be compared on Bring's surface with the nucleon terms. **A loop is not an energy, and nothing here ranks or selects.**

## Part B: the energy of a sum of braids (options only, owner decision; not computed)

The canonical nucleon is a sum of four braids with weight ¼ each, because of the two averaged ud letters. A route 2 energy is defined on one braid. Four natural extensions, written down so the choice is made before any number is seen:

- **B1. Minimum over the terms.**
  - *Meaning:* the element is as "short" as its shortest term.
  - *Cost:* nil, since the per-term values exist.
  - *Risk:* it ignores the weights. It is also a selection inside the element, choosing the term that scores best, which is the shape of fitting that AGENTS.md forbids unless the min is derived.
  - *Commits to:* treating the sum as a superposition in which only the cheapest branch counts.
- **B2. Weighted average of the term energies (weights ¼).**
  - *Meaning:* the expected energy if one term is drawn with its weight.
  - *Cost:* nil.
  - *Risk:* the weights ½ come from writing ud as ½(σ+σ⁻¹), which is a Hecke-algebra statement. Averaging lengths, which are nonlinear in the element, has no algebraic meaning.
  - *Commits to:* a probabilistic reading of the ud letter.
- **B3. Evaluate the element in a linear representation, then take a length.**
  - *Meaning:* this is the only option that uses the sum as a sum. The reduced Burau matrix of ρ(element) = ¼Σρ(terms) is well defined, and |tr|/√|det| gives a q-length. Bring loops do not add, so this exists only on the q-length side.
  - *Cost:* small, since the Burau code exists.
  - *Risk:*
    - the ud letter is ½(σ+σ⁻¹) in the **Hecke** normalisation (eigenvalues q, −q⁻¹). The Burau matrix at t has eigenvalues −t and 1, so it matches Hecke only after rescaling σ_H = −q⁻¹σ_B with t = q². The owner-ruled point t = −q₀ is **not** that point.
    - B3 therefore needs a ruling on which normalisation the average is taken in, and a sum of matrices is not an SL(2) element, so "hyperbolic" needs a definition.
  - *Commits to:* a linear (algebra-level) notion of energy.
- **B4. No energy for sums.**
  - *Meaning:* route 2 applies only to single braids. The real nucleon is out of its domain, and the Bring-loop route cannot select the nucleon.
  - *Cost:* nil.
  - *Risk:* closes route 2 for the actual question.
  - *Commits to:* finding selection elsewhere, e.g. the γγ + confinement SDP of bean qou-ales.

**Default if the owner says nothing:** B4. Nothing is computed for the sum, and the per-term table in `results_signed.md` stays as data only.

**Agent's view (judgement, not a finding):** B3 is the only option that treats the element as an algebra element, but it cannot be run until the normalisation is ruled on. B4 is the honest default until then. B1 is a selection and should not be adopted without a derivation.
