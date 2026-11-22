# Pre-registration: sums of words for the 12, and the own-sector premise

Date 2026-11-21, branch `claude/mn-own-identity-2026-11-21`. Owner request (via the
coordinator): search sums of words for the 12, and try to derive the own-sector premise from
the categorical mass formula.

Disclosure: before writing this file I ran an exploratory sympy session (length ≤ 5 words) and
saw two things: `σ₁ + 2σ₁⁻¹` has own-sector quantum trace `q·tr_{W_p} = 3`, and the integer
span of the word traces seems to reach exactly the multiples of 3. Everything below is stated
with that knowledge; the probe re-derives it and extends it to length 6.

## Question 1: integer sums of words

`T_p(x) = q·tr_{W_p}(x)` for `x = Σ c_w w`, `c_w ∈ ℤ`, `w` a signed word in `σ₁^{±1}, σ₂^{±1}`.

Claims to test:
1. The constants `T_p(x) ∈ ℤ` reachable this way are exactly `3ℤ` (words of length ≤ 6).
2. `12` is reachable (`4σ₁ + 8σ₁⁻¹`), and so is every other multiple of 3.
3. The element reaching 12 is not unique (e.g. the `σ₂` analogue, and the kernel).

Expected verdict: sums **allow** 12 but do **not force** it. Choosing multiplicities so that the
constant is 12 would be selection against the target, and is not done. Canonical elements
(Hecke symmetriser, `Σ T_w`, `Σ q^{-ℓ} T_w`, full twist, Jucys–Murphy sum) are evaluated and
reported whether or not their trace is q-independent.

## Question 2: the own-sector premise

Claim to test: the premise cannot follow from `def:mass-identity` as written, because that
mass is a function of the braid class alone and the γγ selection gives p and n the same
element; any such functional gives `m_n = m_p`. What the quantum trace does force: if the
mass is resolved by charge (the `K^{⊗3}` grading), the whole-space quantum trace is the sum
of `q^{wt}·tr_{W_wt}`, so the sector weights `q`, `q⁻¹` are forced, with normalisation `s = 1`
(the K2 reading, which the proton test falsified). The proton-normalised K1 needs a further
`q⁻¹` that the trace does not supply. Prediction: the premise reduces to one structural input
(the constant is charge-resolved, the volume is not), which is not derivable from the current
definition.

No measured value enters either claim.
