# Pre-registration: can the γγ construction of hydrogen fix the side of the proton the electron sits on? (2026-11-22)

Branch `claude/electron-placement-gammagamma-2026-11-22`. Written and committed before any probe
number or Lean result for this question is computed.

## Question and why

The 4-strand capture braid of #8804 §43/§46 (proton strands cabled, electron encircling the cable
with the inverse pure braid) gives `S(W_L) = −h²[3]_q/q²` with the proton on strands 0–2 and the
electron on strand 3, and `S(W_R) = +h²[3]_q/q²` with the proton on 1–3 and the electron on 0
(`HydrogenCaptureWeightSpace.capL_S_add_capR_S`, on main). `S = F(O₊) + F(O₋)`,
`F(O) = tr(T³·W·Π_O)`. The question: does any structural ingredient of `def:derived-atom` steps 1–6
derive which placement occurs? Selecting a placement because of the n − p sign it gives is
forbidden and is not done here.

Fixed inputs (owner rulings): photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`; Jimbo `Ř` with `h` on `e₁₀`
(state 0 = `e₁`); convention D; electron as one strand in the capture model (as §43/§46; the ruled
3-strand electron is not used, as there); exact arithmetic over ℚ(q); 60 dps only for display.

## Candidate invariants (stated before any check), and what each predicts

Let `flip` send letter `(i, b)` to `(2 − i, b)` on 4 strands (strand reflection; crossing signs kept),
`X` the bit flip on every strand, `P_rev` the strand-order reversal, `Π = X^{⊗4} ∘ P_rev`.

- **I1 Reflection.** `Π Ř_i Π⁻¹ = Ř_{2−i}`. On the two 4-dimensional weight spaces of
  `HydrogenCaptureWeightSpace` (one zero / one one), `Π` is the identity matrix in the file's bases,
  so the claim is `gA (i, b) = gB (2 − i, b)` letter by letter. Prediction (Lean, all words):
  `S_R(flip w) = −S_L(w)` for every word `w`. This is the §46 mirror identity, which §46 checked
  only on its computed family; here it is predicted to hold for every word and therefore for every
  photon weight and gluon arm (S is linear in the element).
  **Predicts: no placement.** It is an exact symmetry of the letters, the photon form (up to the
  proton-internal half twist) and the capture word.
- **I2 What `Π` does not preserve.** `Π T³ Π⁻¹ = −T³`, `Π K Π⁻¹ = K⁻¹` (`K = q^{2T³}`), and the
  right partial trace becomes the left partial trace. Prediction (Lean, 2 strands): the left partial
  trace of `Ř` with weight `diag(q⁻¹, q)` is `q²·1` (Markov, same `z_D`), and with `diag(q, q⁻¹)` it
  is not a scalar for `q⁴ ≠ 1`. Together with `OverStrandWeight.ptr_markov` /
  `ptr_other_not_scalar`: for the fixed `Ř`, the Markov end and the weight `K` come as a pair
  (right ↔ `diag(q, q⁻¹)`, left ↔ `diag(q⁻¹, q)`), and `u = K = q vector` (#7971) is attached to
  that pair. **Predicts:** placement is defined only relative to the Markov end; "electron on the
  right with the right Markov trace" and "electron on the left with the left Markov trace" give
  equal values of every functional built from `Ř`, `T³`, weight projectors and the matching `K`.
- **I3 Hopf orientation.** `flip` keeps every inverse flag, so the negative capture `A⁻¹` maps to
  the negative capture and the writhe is unchanged (Lean, trivial). **Predicts: no placement.**
- **I4 Charge conservation.** The kept set {proton, e⁻} is neutral in either order; the positron is
  disposed. **Predicts: no placement** (it constrains which strands are kept, not their order).
- **I5 Breit–Wheeler order.** In `γγ → e⁺e⁻` pair creation places no letters (#8804 §50 P1,
  confirmed). **Predicts: no placement from letters.** A cup-nesting argument would need a creation
  order for the e-pair relative to the quark pairs, which the corpus does not give.
- **I6 Tower end.** `def:derived-atom` adds the electron in step 6, after the nucleus. The corpus
  γγ atom (`ShellCondensation.GammaGammaAtom`) puts the nucleus on strand 0 and electron `k` on
  strand `k`, i.e. new strands at the top of the tower `H_{k} ⊂ H_{k+1}`, which is the end where the
  Markov property `tr(xσ_top) = z tr(x)` and the convention-D conditional expectation act (sign
  conventions table §1 fact 3). **Predicts: electron at the Markov end = right with the corpus
  trace = `W_L`**, `S_B1 = −h²[3]_q/q²`. Label: this follows the corpus tower convention, which by
  I2 is mirrored together with `K` and `u`; it is not a consequence of the γγ dynamics.
- **I7 Two-term Lagrangian trace.** `t₁, t₂` are `K`-weighted traces (`WeakVertexTwoTerm`):
  `Σ_m q^m Tr_{W_m}`. **Predicts:** they transform as in I2, so they inherit the Markov-end tie and
  fix nothing beyond I6.

## Probe (exact, after the Lean)

`placement_probe.py`, sympy over ℚ(q), 4 strands, words: capture with gluon arms g ∈ {1, V, σ₁}
as in §46 (proton left and right), plus 6 random words of length ≤ 10 as controls.

- **P1** `B1_R(flip-image)(O₊) = −B1_L(O₋)` and `(O₋) = −(O₊)` exactly, every word (I1).
- **P2** `B2_R[K](O) = −B2_L[K⁻¹](Ō)` exactly, every word (I2), with
  `B2[K](O) = tr(T³·K·W·Π_O)`.
- **P3** On these weight spaces `K` is the scalar `q^{±2}`, so `S_B2^L + S_B2^R = (q² − q⁻²)(F₊^L − F₋^L)`
  for the capture (derived from P1 and I2 before computing). Not predicted: the signs of `S_B2^L`,
  `S_B2^R`, and of their word-dependent parts `S_B2(W) − S_B2(1)`.
- **P4** Left/right partial-trace Markov check of I2 on the 2-strand `Ř` (also in Lean).

## Decision rule

The placement is **derived** only if some invariant among I1–I7 (or one found during the work, to be
reported as found later) is not mapped to itself by `Π` together with `K ↔ K⁻¹` and the Markov
end. If every candidate is `Π`-covariant in that sense, the result is: placement is fixed only
relative to the Markov end, and the absolute left/right choice is the same convention as the Markov
end and `u` (scope (b) for that class, invariant = `Π`). Refutation of I1/I2: any word where P1 or
P2 fails.

## Honesty clause

I know §43/§46 (`S` flips with placement under B1) and the sign of `S_B1` for `W_L`. No placement is
chosen for its n − p sign. The mapping from `S` to "which nucleon is heavier" is not assumed; it is
reported as whatever the corpus establishes.

**Pre-registration completed:** 2026-11-22T15:10:49Z (UTC), before computation.
