# The three bond rules, and whether the sum over bonds needs a length cutoff

**Date** 2026-11-27 · **Brief** C2 (epic `qou-myts`), front E · **Bean** `qou-brng`
**Owner question** (Carl, 2026-11-27): *"bond selection - keep open. exlore all three. why do we need a
lnegth cutoff? can we measure (surrealy) or estimae error bounds?"*
**Lean** [`QOU/Transcendental/MassTheory/BondLengthSumTail.lean`](../../folio/quantum-observable-universe/lean/QOU/Transcendental/MassTheory/BondLengthSumTail.lean):
8 theorems, sorry-free, lean-direct `-DautoImplicit=false -s 65536` exit 0, `#print axioms` ⊆
`[propext, Classical.choice, Quot.sound]`.
**Probes** [`computations/probes/bond_rules_length_bound/`](../../computations/probes/bond_rules_length_bound/):
mpmath 40 dps, convention D, proton pin, no float arithmetic. AME is not read by any probe.
**Scope** (a) for every number. **Nothing is adopted.** The bond rule stays Carl's open decision.

## 0. Answer in one paragraph

The length cutoff is needed only because the current rule (3) has no weight. Bond words of length
`L` number about `(n−2)^L`, and their traces do not shrink: every vertex `V(s) = σ_s σ_{s+1}⁻¹`
fixes the top Schur–Weyl state, so `S = Σ_s V(s)` has eigenvalue `n − 2`. Measured, that is also
its spectral radius and its norm (A = 2: 4, A = 3: 7). Two cutoff-free definitions exist.
**(i) A per-vertex weight `t`.** The sum is then the resolvent `(1 − tS)⁻¹`, it converges exactly for
`|t| < 1/(n−2)`, and the tail after length `L₀` is bounded by `(|t|‖S‖)^{L₀+1}/(1 − |t|‖S‖)`
(Lean `norm_tail_le`). The corpus-scale weights `h`, `qh`, `h/q` (0.19–0.23) are inside the radius at
A = 2 and **outside it from A = 3 on** (radius 1/7 = 0.143). So with an `h`-scale weight the archimedean
sum over all lengths diverges at A ≥ 3; no error bound removes the cutoff there (Lean
`card_le_geom_partial`). **(ii) No weight: the uniform average over bond words of length `L`, `L → ∞`.**
It exists at every A and equals the trivial-block weight, `r_∞ = y_{(n)}/tr(x)` with
`y_{(n)} = [n+1]_q/[2]_q^n`. It passes reading 3. At `q = 1` it is `−ln r = n ln 2 − ln(n+1)`, exactly
the classical reading-3 merge ceiling of `ClassicalReading3MergeBound`. Values: A = 2, 9.119 MeV;
A = 3, 16.093 MeV. The surreal reading (weight
infinitesimal) truncates exactly: the remainder after length `L₀` has order `L₀ + 1` in the weight
(Lean `X_pow_dvd_remainder`), and at leading order the sum is the plain average over the shortest bond
words. That is bookkeeping and says nothing about a real weight.

## 1. The three rules at A = 2 and A = 3 (scorecard)

`B = −E₀ ln r`, tower `E₀ = 4.2274833556` MeV. All values are exact for the stated words (traces
agree with an independent Schur–Weyl trace to 1e-40); the error columns concern the population, not
arithmetic.

| rule | A | what it picks | `−ln r` | `B` (MeV) | is the cutoff an issue? |
|---|---|---|---|---|---|
| (1) cheapest passing pure-junction bond | 2 | `V1³`, `V2³` (length 3, merge 0) | 0.0015040 | 0.00636 | no: lengths 1–2 exhausted, none pass |
| (1) | 3 | 69 tied words of length 5 (960 searched; none of length ≤ 4 pass) | 1.0481 … 2.3247 | **4.431 … 9.828** | no, but the rule does not determine a value: the tie spans a factor 2.2 |
| (2) cheapest passing bond that merges | 2 | `V2V3`, `V3V2` (length 2, merge 2) | 1.3780948 | 5.8259 | no: length 1 exhausted |
| (2) | 3 | `V2V3V4` and cyclic shifts (length 3, merge 2) | 1.3971616 | 5.9065 | no: lengths 1–2 exhausted |
| (3a) weighted sum, all bond words, reading 3 on the summed element | 2 | `t = h / qh / h/q` | 1.8380 / 1.9749 / 1.7544 | 7.770 / 8.349 / 7.417 | removed (exact resolvent); **the summed element FAILS reading 3** at every weight (block (3,3) at level 6) |
| (3a) | 3 | `t = h / qh / h/q`, analytically continued | 3.1686 / — / 2.0075 | 13.395 / ratio < 0 / 8.487 | **no convergence**: every corpus weight exceeds the radius 1/7, so these are values of `(1 − tS)⁻¹`, not sums over words (`Z(h/q) < 0`). Reading 3 on the element: fails / fails / passes. Inside the radius, `t = 1/14`: 12.219 MeV, fails |
| (3b) weighted sum over individually passing words | 2 | truncated at L = 6 | 0.9926 / 0.9835 / 1.0052 | 4.196 / 4.158 / 4.249 | measured to stabilise (L = 5 → 6 moves `B` by 0.007 MeV at `t = h`), but the proved bound is useless (ratio error ≤ 122 at `t = h`, ≤ 21 at `h/q`); at `qh` none is geometric |
| (3b) | 3 | truncated at L = 4 (28 passing words) | 1.3585 / 1.3571 / 1.3600 | 5.743 / 5.737 / 5.749 | no geometric bound at any corpus weight (`7·t·1.199 ≥ 1.58`); only two lengths measured |
| (3∞) uniform limit, no weight | 2 | `y_{(6)}/tr(x)` | 2.1571300 | **9.119** | removed, exact closed form; passes reading 3 |
| (3∞) | 3 | `y_{(9)}/tr(x)` | 3.8068536 | **16.093** | removed, exact closed form; passes reading 3 |

AME (scorecard only): ²H 2.224566 MeV, ³H 8.481796 MeV. No rule is chosen here by its distance to
AME. **One cell lands within 0.06 % of ³H: (3a) at A = 3 with `t = h/q`, 8.487 MeV.** It should not be
read as support. That value is an analytic continuation outside the radius of convergence (it is not a
sum over bond words, and its word count `Z` is negative). The weight `h/q` was not derived as the bond
weight; it is one of three corpus quantities tried. The same weight at A = 2 gives 7.417 MeV against
2.2246 (+233 %), and its neighbours `h` and `qh` at A = 3 give 13.4 MeV and a negative ratio. Picking
`h/q` because of this cell would be selection against the target.

**Rule (1) at A = 3 is a new measurement.** The ceiling probe (lengths ≤ 4) held no passing
pure-junction word. Extending the pure-junction population (`V1, V2, V4, V5`) to length 5 gives 69
passing words out of 960, all of the same crossing count, so "cheapest" ties 69 ways. Their values
fall in four bands; 9 of them **merge 4 and pass reading 3 at q₀**, e.g. `V1V4V2V5V5`
(`−ln r = 2.3247432`, 3.35 merge units, 9.83 MeV). **This revises §2 of
`2026-11-27-binding-ceiling-at-q0.md`:** the measured cap of 2 merges at A = 3 holds only for words of
length ≤ 4. At length 5 a pure-junction word merging 4 passes. The A = 4 finding (cap not 2) therefore
already appears at A = 3. This agrees with fronts A and B, found independently the same day (PR #9587,
nine words; PR #9618, 22 of 284 four-merge classes).

## 2. Why a cutoff, and when it can go

**The obstruction is a fixed vector, not a slow decay.** In the Schur–Weyl module `(ℂ²)^{⊗n}`, `σ_s`
acts on `|0…0⟩` by `q` and `σ_{s+1}⁻¹` by `q⁻¹`, so `V(s)|0…0⟩ = |0…0⟩` (Lean `vertex_fixes`) and
`S|0…0⟩ = (n−2)|0…0⟩` (`sum_fixes`). The same holds on the whole trivial block `λ = (n)` (multiplicity
`n + 1` of the eigenvalue, one per weight space; measured 7 at n = 6, check K2). The Hecke expansion
`T_word = T_perm + O(h)` does **not** give a geometric tail: `σ² = 1 + hσ` keeps the classical term
with coefficient 1 at every length, so an extra crossing does not cost a factor `h`. That suggestion
from the brief is withdrawn on this evidence.

Measured norms (Schur–Weyl, operator 2-norm): `‖V(s)‖ = 1.1988582` (below `q² = 1.2320525`);
`‖S‖ = ρ(S) = n − 2` exactly at A = 2 and A = 3 (measured, not proved); per-vertex growth of words
`μ_k^{1/k}` = 1.199, 1.199, 1.169, 1.158 for k = 1…4 at A = 2.

Consequences:

1. **Weighted sum (3a).** Converges iff `|t| < 1/ρ(S) = 1/(n−2)`. Tail after length `L₀`:
   `‖Σ_{L>L₀}(tS)^L‖ ≤ (|t|‖S‖)^{L₀+1}/(1 − |t|‖S‖)`, and `|tr Y| ≤ ‖Y‖₂` for the normalised quantum
   trace. The bound is checked against the exact resolvent (K5): at A = 2, `t = h/q`, truncation at
   `L₀ = 8` errs by 0.0072 in the ratio against a proved bound of 0.21; at A = 3, `t = 1/14`, by
   0.00035 against 0.030. The bound is valid but loose,
   because the trivial block saturates the norm. At A = 3 every corpus weight lies outside the radius.
2. **Weight-free limit (3∞).** The average over length-`L` bond words is
   `tr(x·Σ_J (−1)^{|J|} S_{−J}^L)/(count_L·tr x)`; as `L → ∞` it converges to the trivial-block
   projection (checks K3, K4: L = 128 agrees with the projector to 1e-11 and the projector with the
   closed form to 1e-25). Convergence is geometric with rate `|λ₂/λ₁|` = 3.291/4 = 0.823 at A = 2
   (measured: `−ln r` 1.399, 1.668, 1.775, 2.021, 2.127, 2.156, 2.1571, 2.1571 at L = 1, 2, 4, …, 128)
   and 6.621/7 = 0.946 at A = 3 (`−ln r` 2.797, 2.897, 3.101, 3.435, 3.674, 3.785, 3.806, 3.80685, at
   L = 2, 4, …, 256; L = 1024 agrees with the projector to 1e-20). The eigenvalue `n − 2` has
   multiplicity `n + 1` (7 and 10), one per weight space of the trivial block. The rate approaches 1
   as `A` grows, so a finite truncation of the uniform average converges more slowly at larger `A`.
3. **Individually filtered sum (3b).** A bound on the unmeasured long passing words must assume they
   could all pass and all have maximal trace; with `count_L ~ (n−2)^L` and `‖K_w‖ ~ 1.16^L` this is
   geometric only for `t(n−2)·1.158 < 1`. At A = 2 it holds for `h` and `h/q` but the resulting interval
   is wider than the ratio itself. **So (3b) needs the length cutoff in practice**, unless the fraction
   of passing words is bounded, which is front B's question.

## 3. Surreal reading (bookkeeping only)

Treat the weight as infinitesimal, `ord_ω(t) = −1` (per `def:surreal-blowup-calculus`,
`conj:surreal-limit-transfer`). `S` has finite entries (ord 0), so the remainder after truncating (3a)
at length `L₀` has `ord_ω ≤ −(L₀+1)`, with equality when the first omitted coefficient is nonzero
(Lean `X_pow_dvd_remainder`, `not_X_pow_succ_dvd_remainder`, in `R⟦X⟧`, generic `R`). In this reading
the series exists at every A, with no radius. The leading term is the plain average over the shortest
bond words: at A = 2 that is `V1`, `V2`, `r = 0.2469340`, `B = 5.913` MeV. Neither word passes reading 3
on its own. This is not a precision claim. At the real weights the archimedean statements of §2 govern,
and at A ≥ 3 they say the series diverges.

## 4. Options for Carl (nothing adopted; default = nothing changes)

The rule stays open. For each option: what it means, its cost, its risk, and what it commits to.

- **(1) Cheapest pure-junction bond (current recommendation on the card).** Unfitted. Gives ²H
  6.4 keV. At A = 3 it ties 69 ways over 4.4–9.8 MeV, so it needs a tie-break, which is a new
  choice. Commits to "pure junction" and "cheapest", neither derived from the binding.
- **(2) Cheapest merging bond.** 5.83 / 5.91 MeV. It is a fit unless the merge requirement is derived;
  the A = 3 length-5 result shows merging is not tied to the shortest word.
- **(3a) Weighted resolvent.** Removes the cutoff at A = 2 only; the summed element fails reading 3; the
  weight `t` is a new undetermined choice (h, qh, h/q differ by 0.9 MeV at A = 2).
- **(3∞) Uniform long-word limit.** No weight, no cutoff, exact closed form, passes reading 3, every A.
  It is the trivial-block weight `y_{(n)}`, so it is extensive: `B ≈ E₀(n ln 2 − ln(n+1))` near q = 1,
  about `E₀·3 ln 2 ≈ 8.8` MeV per nucleon. It does not depend on the bond words at all, which is the
  strongest objection: it reads the free word against the fully symmetrised state.
- **Default (say nothing).** The recorded result stays rule (1); nothing is re-scored.

Agent's judgement, not a finding: (3∞) is the only cutoff-free definition that needs no new choice,
so it is the right reference for Carl's question, but as a bond rule it discards the bond. It is worth
having on record, not adopting.

## 5. Not established

- `‖S‖ = ρ(S) = n − 2` is measured at n = 6, 9 only.
- (3b) beyond the measured lengths; the A = 3 rule-(1) tie-break; reading 3 on (3a) at A = 3 is
  reported for the analytically continued resolvent, which is not a sum over words there.
- The bridge `|tr Y| ≤ ‖Y‖₂` is cited (quantum trace with positive weight), not formalised.
