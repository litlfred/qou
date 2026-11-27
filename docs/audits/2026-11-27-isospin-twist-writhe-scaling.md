# Where a `1/A` comes from in the braid-channel `T(T+1)` term: the writhe

Date: 2026-11-27. Bean `qou-tcl2` (ledger gap G2), epic `qou-myts`. Follow-up to PR #9685
(Lean, merged) and PR #9706 (wiring, held on the owner's card).
Lean: `QOU/Nuclear/IsospinTwistWrithe.lean`. Probe:
`computations/probes/isospin_twist_writhe_scaling_probe.py` (witness
`isospin-twist-writhe-scaling`).

## 1. The question

#9706 wires `−κ·T(T+1)` (`κ = 2α ln q = 0.78140 MeV`) into the ruled binding. The term
grows as `T²` with no `1/A`, so the median relative `Q_β` error in scorecard Table 3.4b goes
from 92.7 % to 315.8 %, and ²⁰⁸Pb gets −395 MeV. Classically the symmetry energy goes as
`(N−Z)²/A`. The task was to find whether a `1/A` comes out of the categorical structure, and
not to insert one by hand.

## 2. Result (Lean, sorry-free)

Every multiplicative invariant of a Hecke block sees a braid word only through its
**writhe** (exponent sum), and the Murphy product is a word of `N(N−1)` letters.

| statement | Lean |
|---|---|
| any monoid hom `χ : H_N(q) →* M` (`M` commutative) takes one value `a` on all `σ_i` | `chi_σ_eq` |
| `χ(L_k) = a^{2k}`, so `χ(Φ) = a^{N(N−1)}` (from `L_{k+1} = σ_k L_k σ_k` alone; `Φ = Δ²` not needed) | `chi_qJM`, `chi_murphyProd_full` |
| for a word `w` of writhe `e`, `χ(w) = a^e` | `chi_word` |
| on the seminormal block of dimension `d`: `det ρ(w)^{N(N−1)} = (q^{2c})^{d·e}` | `seminormal_det_word_pow` |
| per letter, per dimension: `2c/(N(N−1)) = 2T(T+1)/(N(N−1)) + (N−4)/(2(N−1))` | `perLetter_twoRow` |
| full twist (`e = N(N−1)`): `T(T+1)` coefficient `2`, no `A`-dependence | `fullTwist_coeff` |
| chain (`e = A−1`, `N = 3A`): coefficient in `[1/(9A), 2/(9A)]` for all `A ≥ 2` | `chain_coeff_bounds` |

So under the log law, applied block by block as the block log-determinant (the sum of
`ln|eigenvalue|` over the block, per block dimension), the `T(T+1)` term of a word `w` is

    B_T = −κ · e(w)/(N(N−1)) · T(T+1).

**The coefficient is the writhe over `N(N−1)`.** #9706 used the full twist, whose writhe is
`N(N−1)`, and so got `κ·T(T+1)`. A nucleus word whose writhe grows linearly in `A` gets a
coefficient `Θ(1/A)`. The `n`-only part `e(N−4)/(2(N−1))` is then extensive. That is a
consistency check, not an input: the same scalar `c(λ)` carries both parts, and for the full
twist its `n`-only part `N(N−4)/4` would be quadratic in `A`, i.e. not extensive. So the full
twist cannot be the whole-nucleus word under an extensive energy map, and a linear-writhe word
is the reading under which both parts scale correctly.

## 2a. The bound does not need the bond signs (added the same day)

| statement | Lean |
|---|---|
| a word of `ℓ` letters `σ_i^{±1}` has `|e| ≤ ℓ`, any signs | `abs_writhe_wordOf_le` |
| the nucleon core `(σ_aσ_b⁻¹)³` has `e = 0`; a writhe-zero factor leaves `e` unchanged | `writhe_core`, `writhe_mul_of_writhe_eq_one` |
| `|e| ≤ ℓ` gives `|coeff| ≤ 2ℓ/(3A(3A−1))` | `abs_ttCoeff_le` |
| `|e| ≤ A − 1` gives `|coeff| ≤ 2/(9A)` for all `A ≥ 1` | `abs_ttCoeff_le_of_chain` |

Combined with `QOU.Mass.StrandLayoutForcesChain` (a single generator joins two nucleons
only at `3k+2`, and only consecutive ones), a word made of writhe-zero nucleon cores plus
one bridge letter per nucleon boundary has `|e| ≤ A − 1`, so the `T(T+1)` coefficient is
at most `2κ/(9A)` in size **whatever the bond signs are**. The upper `1/A` scaling no longer
rests on the sign assumption. What still rests on assumptions: the sign of the term (open,
and possibly zero), the energy map (block log-determinant), one bridge letter per boundary
(the corpus word; a word may repeat bridges), and the scale `α`. The full twist is outside
this class: its `N(N−1)` letters are mostly intra-nucleon and transport letters.

## 3. What it gives (comparison only; AME is not used to choose anything)

Same energy map, sign and lowest block as #9706. Only the writhe changes. The writhe of each
bond letter is taken as `+1`.

| word | writhe `e` | median \|ΔQ_β\|/Q_β (Table 3.4b, 1010 rows) | ²⁰⁸Pb share | ¹³²Sn share |
|---|---|---|---|---|
| no term | — | 92.69 % | 0 | 0 |
| full twist (#9706) | `N(N−1)` | 315.8 % | −395.4 MeV | −212.5 MeV |
| chain (ruled law) | `A−1` | 92.36 % | −0.21 MeV | −0.18 MeV |
| T3 valence (#9710) | `3⌊A/2⌋` | 92.19 % | −0.32 MeV | −0.27 MeV |

So the derived `1/A` removes the damage #9706 does, but the term is then about 1000 times
too small to be the symmetry energy (classical comparison: ~23 MeV × (N−Z)²/A, i.e. ~214 MeV
at ²⁰⁸Pb). This is a scope-(a) negative: the braid-channel `T(T+1)` term with the corpus's own
nucleus word and the proxy scale `α` is not, alone, the symmetry energy. It does not exclude
the ingredient.

## 4. The second `1/A`: the block dimension

The two-row block of `N` strands and isospin `T` has dimension
`d_(m,k) = C(N,k)·(m−k+1)/(m+1)`. Its log is

    ln d_T − ln d_0 = ln(2T+1) − 2T²/N + O(T⁴/N³).

The `−2T²/N` piece is a `1/A` that comes out of the representation theory with no word
choice at all. It is the block multiplicity, which is the categorical analogue of the
Fermi-gas level density (the 2026-08-07 options audit, §A3, already recorded that the `1/A`
is "Fermi-gas level density, a separate dynamical input"). At ²⁰⁸Pb (`N = 624`, `T = 22`)
the `ln(2T+1)` piece still dominates (`+3.81` against `−1.55`). With `α` the Gaussian piece is
`α·(2/3)·T²/A = 2.50·T²/A` MeV, about 37 times below the classical comparison. No corpus
energy map for the block multiplicity exists, so this is recorded and not wired.

## 5. What this does not settle

1. **The sign of the bond letters.** The writhe of the nucleus word is the word axis (G5). If
   the bond letters are not all positive, the chain writhe is smaller and can be zero.
2. **The quark-level writhe.** `WeakIsospinT3Grading.lean` (PR #4618) reads `T3` as the sign of
   a quark's own crossing (up `+`, down `−`). If those crossings are in the nucleus word, they
   add `e ⊃ Z − N` (odd in `T_z`), and the term becomes `∝ T_z·T(T+1)/A`. That is a different
   channel and is not computed here. The nucleon core `V³ = (σ_0σ_1⁻¹)³` used by the ruled law
   has writhe `0`.
3. **The block functional.** The log-determinant is the functional that the log law gives
   block by block. A different functional of a non-central word (for example the largest
   eigenvalue) need not factor through the writhe.
4. **The scale.** `α = 8G·m_e` is the proxy's convention. The scale-unification thread owns it.

## 6. Verification

- Probe: `PYTHONPATH=computations python3 computations/probes/isospin_twist_writhe_scaling_probe.py`,
  3/3 checks pass, including that the full-twist variant reproduces #9706's 315.8 %.
- Lean: `lean -DautoImplicit=false -s 65536 QOU/Nuclear/IsospinTwistWrithe.lean` exits 0 against the import cone built by `scripts/lean-direct-cone.sh`; `#print axioms` on `seminormal_det_word_pow`, `chi_word`, `chain_coeff_bounds`, `perLetter_twoRow` gives `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.
- No content block is touched, so no KG JSON-LD node changes.
- No measured value appears in any proof.
