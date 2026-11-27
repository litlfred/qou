# Neutral words have odd cycles, so reading 3 near q = 1 selects pure braids (bean `qou-cds1`)

Date: 2026-11-27. Follows [`2026-11-27-cds1-mod3-rule-counterexample.md`](2026-11-27-cds1-mod3-rule-counterexample.md)
(PR #9624), which showed that the "multiple of 3" rule fails at ten vertices and that the selection
seen in the data is purity, not a count condition. This note proves the q-free half of that.

Lean: [`QOU/MassTheory/NeutralWordOddCycles.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/NeutralWordOddCycles.lean), sorry-free, `scripts/lean-verify.sh` exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]`.

## 1. Statement

Let `w` be a word in the Artin generators `σ_i^{±1}` of `B_n`, with permutation `π(w) ∈ S_n`. Call
`w` **self-neutral** if for every cycle `C` of `π(w)` (a component of the closure) the signed number
of crossings between two strands of `C` is 0. Linking-neutral words (the probe's `neutral`) are
self-neutral.

**Theorem A (parity).** If `w` is self-neutral, every cycle of `π(w)` has odd length.

**Theorem B (q = 1, six strands).** On `n = 6`, if every cycle of `π` has odd length and the two-row
characters of `S_6` are non-negative at `π` (classical reading 3), then `π = 1`.

**Corollary.** A linking-neutral six-strand word `w` passes reading 3 for all `q` in some interval
around 1 if and only if `π(w) = 1`.

*Proof of the corollary.* At `q = 1` the Hecke character `χ_λ(w)` is the `S_6` character `χ_λ(π(w))`,
and it is a Laurent polynomial in `q`, so continuous. If `π(w) = 1` then `χ_λ = dim λ > 0`, which
stays positive near `q = 1`. If `π(w) ≠ 1`, Theorem A gives cycle type `(3,1,1,1)`, `(3,3)` or `(5,1)`,
and on each of these some two-row character is **strictly** negative at `q = 1` (table below), so it
stays negative near `q = 1`. ∎

| cycle type | `a₀ a₁ a₂ a₃` (invariant k-subsets) | failing character at q = 1 |
|---|---|---|
| `(1⁶)` | 1 6 15 20 | none |
| `(3,1,1,1)` | 1 3 3 2 | `χ_(3,3) = a₃ − a₂ = −1` |
| `(3,3)` | 1 0 0 2 | `χ_(5,1) = a₁ − a₀ = −1` |
| `(5,1)` | 1 1 0 0 | `χ_(4,2) = a₂ − a₁ = −1` |

(`χ_(6−k,k) = a_k − a_{k−1}` by Young's rule, as in `ClassicalReading3MergeBound`.)

## 2. Proof of Theorem A

Track two strands `x ≠ y`. Each crossing between them swaps their left-to-right order, and no other
letter changes it. So the number of crossings between `x` and `y` is odd exactly when their order at
the bottom is the reverse of their order at the top, and the signed count has the same parity as the
unsigned one. Summing over the pairs inside a cycle `C` of length `k`, the self-crossing count of `C`
has the parity of the number of inversions of `π` restricted to `C`. In the induced order on `C` that
restriction is a `k`-cycle, whose sign is `(−1)^{k−1}`. Self-neutrality makes the count 0, so `k − 1`
is even. ∎

Nothing here depends on the vertex grammar: Theorem A holds for every braid word on any number of
strands.

## 3. What it explains, and what it does not

- **The data.** Of the 1906 neutral V-words of at most six vertices, the cycle types are `(5,1)` 1422,
  `(3,3)` 224, `(3,1,1,1)` 202 and `(1⁶)` 58. Only the 58 pure words pass reading 3 at q₀, matching
  the corollary. The audit's "every survivor is pure" is therefore the q → 1 shadow of a theorem.
- **At q₀ itself it is still a measurement.** The corollary gives an interval around 1 that depends
  on the word. Whether q₀ lies inside it is not decided by this argument. Measured: no non-pure
  neutral word passes reading 3 at q₀ for 7 vertices (0 of 4848 with a count ≢ 0 mod 3) or
  8 vertices (0 of 16 422) or 9 vertices (0 of 65 538); see §5.
- **Mod 3 is a separate, false-in-general statement** (counterexample `(V₀V₂)⁵`, PR #9624). Pure
  neutral words have counts ≡ 0 mod 3 up to nine vertices and not at ten.

## 4. Lean status

| statement | Lean |
|---|---|
| crossing parity (§2, first step), any word, any strand count | `even_cross_iff` |
| inversions inside a cycle have the parity of `#C − 1` | `neg_one_pow_invOn_cycleOf` (with `sign_eq_signAux`) |
| Theorem A | `odd_of_mem_cycleType` |
| Theorem B (on cycle lengths, `a₀ ≤ a₁ ≤ a₂ ≤ a₃`) | `eq_replicate_of_odd_reading3` |
| self-neutral + classical reading 3 ⇒ `π = 1` on six strands | `perm_eq_one_of_selfNeutral_reading3` |

Not formalised: the character-to-`a_k` bridge (Young's rule, cited as in
`ClassicalReading3MergeBound`) and the continuity step from `q = 1` to an interval. Pure
combinatorics, so no base ring enters; no `q₀` and no measured value appears in any statement.

## 5. Nine-vertex sweep

Every freely reduced V-word of 7, 8 and 9 vertices (all `4^k` index sequences), keeping the
linking-neutral non-pure ones, with the two-row characters evaluated exactly (`Fraction`) at q₀:

| vertices | neutral non-pure words | pass reading 3 at q₀ |
|---|---|---|
| 7 | 4 848 | 0 |
| 8 | 16 422 | 0 |
| 9 | 65 538 | 0 |

Run on 2026-11-27 with `six_strand_neutral_selection_probe` (its `neutral`, `char`, `mats_at`),
1807 s for k = 9. Scope (a): purity at q₀ is measured through nine vertices, proved only near q = 1.
Every non-pure neutral word at these lengths has some vertex count not divisible by 3, so the same
numbers also close the k = 9 line of the mod-3 audit.
