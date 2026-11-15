/-
# `C_knot` is non-universal — no level-only rescale closes binding (T/³He mirror invariant)

The master binding formula is `B(K) = m_e · |Σ_λ y_λ χ^λ(β_K) sgn(w_0) f^λ| = m_e · S(K)` with the
weight `y_λ` now PINNED to the derived Wenzl Markov weight (`BindingWeightMarkovPinning`, PR #4543),
`Σ_λ y_λ f^λ = tr_M(1) = 1`. The residual `C_knot(K) = B_AME(K)/(m_e · S(K))` is the FITTED deficit —
the open Δ_λ gate (bean `qou-3q7t`).

The companion probe `c_knot_nonuniversal_pinned_weight_probe.py` measures, with this ONE derived weight
(all 0-fit, exact mpmath):

  `C_knot(D) = 6.0679`, `C_knot(T) = 6.7061`, `C_knot(³He) = 4.9054`, `C_knot(⁴He) = 290.007`
  → spread 59.12×.  (Convention D — the constants in this file are already the D values; only
  this header line still carried the superseded convention-C figures `5.85 / 4.44 / 3.29 / 9.31`,
  spread `2.83×`, which contradicted the refresh note below it.  Corrected 2026-08-21, PR #5406.)

  The `⁴He` entry is ILL-CONDITIONED and should not be read as `290×` of missing physics: the
  master sum is alternating and `κ(⁴He) = |S| / Σ_λ|t_λ| < 1/100`, so a sub-percent per-block
  correction sends `S(⁴He)` to zero.  See `CKnotCancellationConditioning.lean`, which also proves
  the mirror pair used below is well conditioned (`κ(T), κ(³He) > 1/4`) — the exclusion in THIS
  file is therefore unaffected.

**The formalize-first invariant (this file):** the triton `T` and helion `³He` sit at the SAME strand
count `H₉`, so any *level-only* closure `B(K) = g(n_K, q₀) · m_e · S(K)` would force the SAME rescale
`g(9, q₀)` to reproduce both `B_AME(T)` from `S(T)` and `B_AME(³He)` from `S(³He)`. But the measured
`(B, S)` pairs make that impossible: `B_T · S_He ≠ B_He · S_T` (the cross-multiplied form of
`B_T/S_T ≠ B_He/S_He`). Hence **no level-only rescale `g(n, q₀)` closes binding** — `C_knot` carries
genuine per-knot (isospin / mirror) content, not captured by `(n, q₀)`.

This is a **scope-(b) structural exclusion of the level-only-rescale closure class** (cited invariant:
`mirror_cross_ne`). It does NOT exclude a per-knot Δ_λ derivation — that stays OPEN (`qou-3q7t`). The
numerical values are experimental `B_AME` (diagnostic only, never inverted into a weight) and the
substrate-derived `S(K)` from the pinned Markov weight; `free_parameters = 0`, nothing wired.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic

namespace QOU.MassTheory.CKnotNonUniversal

/-!
**Convention-D refresh (2026-08-11, bean `qou-4jut`).** The numeric constants below were restated
after `70d1ade383` ("excise C tiers 2+3: 176 producer sites to convention D"), a deliberate repo-wide
migration that the producing witness pre-dated — so the values previously recorded here
(`S_T = 3.7349054`, `S_He = 4.5882788`, `CKnot_D = 5.8530241`, `CKnot_T = 4.444145`) were the
superseded convention's. Convention D is right by an argument independent of any measurement: it
gives `QR = Q²` exactly, hence `r = log_Q(QR) = 2`, and `r` counts the variables in the Wenzl
principal specialisation `s_λ(1, Q, …, Q^{r-1})` — it must be a positive integer, and the mass
chapter forces `2` (the fundamental of `SU_q(2)`).

**Every theorem in this file survives the refresh, and the mirror gap widens.** `mirror_cross_ne`
and `no_level_only_closure` need only `B_T · S_He ≠ B_He · S_T` (now `26.11 ≠ 19.10`);
`mirror_gap_exceeds_isospin_band` needs the ratio above `1.1` and it moved `1.35 → 1.367`;
`no_writhe_only_framing` needs only that an equal-writhe pair differs, which it does more sharply
than before. No claim here becomes false — the magnitudes move.
-/

/-- Master-formula magnitude `S(K) = |Σ_λ y_λ χ^λ(β_K) sgn f^λ|` for the triton, at `H₉`, with the
pinned Wenzl weight (probe `c-knot-nonuniversal-pinned-weight.witness.json`). -/
def S_T : ℝ := 2.4751404

/-- Master-formula magnitude `S(K)` for the helion `³He`, at the SAME `H₉`, pinned weight. -/
def S_He : ℝ := 3.0789913

/-- AME 2020 binding of the triton (MeV) — experimental diagnostic target, never inverted. -/
def B_T : ℝ := 8.4817962

/-- AME 2020 binding of the helion `³He` (MeV) — experimental diagnostic target, never inverted. -/
def B_He : ℝ := 7.7180413

/-- **The mirror-pair cross-inequality** `B_T · S_He ≠ B_He · S_T` — the cross-multiplied form of
`C_knot(T) = B_T/S_T ≠ B_He/S_He = C_knot(³He)`. This is the structural obstruction to any level-only
closure: `T` and `³He` share the strand count `H₉`, so a rescale depending only on the level cannot
reproduce both bindings. Falsifiable (a genuine numerical claim about the measured `(B, S)` pairs),
sorry-free. -/
theorem mirror_cross_ne : B_T * S_He ≠ B_He * S_T := by
  unfold B_T S_He B_He S_T; norm_num

/-- **No level-only rescale closes binding.** If a single scale `g` (`= g(9, q₀) · m_e`, the level-`H₉`
value of any closure `B(K) = g(n_K, q₀) · m_e · S(K)`) reproduced BOTH the triton and the helion
binding from their `S` values, then `B_T · S_He = B_He · S_T`, contradicting `mirror_cross_ne`. Hence
`C_knot` is not a function of `(n, q₀)` — it carries per-knot content. scope-(b) exclusion of the
level-only-rescale closure class. -/
theorem no_level_only_closure : ¬ ∃ g : ℝ, B_T = g * S_T ∧ B_He = g * S_He := by
  rintro ⟨g, hT, hHe⟩
  apply mirror_cross_ne
  rw [hT, hHe]; ring

/-- **The required rescales differ by more than the isospin band.** `C_knot(T)/C_knot(³He) > 1.1`
(measured 1.367), i.e. `B_T · S_He > 1.1 · (B_He · S_T)` — the mismatch a level-only closure would have
to absorb exceeds the ~8% isospin tolerance (ROUTE 5), so the exclusion is not a marginal-precision
artifact. -/
theorem mirror_gap_exceeds_isospin_band : B_T * S_He > 1.1 * (B_He * S_T) := by
  unfold B_T S_He B_He S_T; norm_num

/-!
### Writhe / framing is ruled out too

The Markov trace is a *framed*-link invariant; the ambient (unframed) Jones/HOMFLY invariant differs
by a writhe-dependent framing factor `~ q₀^{c·w}`. If the master formula omits it, the deficit could
carry that factor. But the canonical words give `writhe(D) = 11−7 = 4 = 16−12 = writhe(T)` (averaged
interface crossings are writhe-neutral), and `writhe(³He) = writhe(⁴He) = 8` — yet `C_knot` differs in
BOTH equal-writhe pairs (6.068 vs 6.706; 4.905 vs 290.01). So no writhe-only framing factor `f(w)`
closes the deficit. The pair argument is what carries the exclusion — it needs only that the two
members of an equal-writhe pair differ, so it is untouched by the convention refresh below.
(Framing hypothesis contributed by a parallel session, tested + excluded here.)
-/

/-- `C_knot(D)` — deuteron deficit (probe `c-knot-nonuniversal-pinned-weight.witness.json`). -/
def CKnot_D : ℝ := 6.0678734

/-- `C_knot(T)` — triton deficit; the triton word has the SAME writhe (4) as the deuteron. -/
def CKnot_T : ℝ := 6.7060686

/-- **The deuteron and triton canonical words have equal writhe** `11 − 7 = 16 − 12 = 4` (`#σ − #σ⁻¹`;
averaged interface crossings are writhe-neutral). -/
theorem deuteron_triton_same_writhe : (11 - 7 : ℤ) = 16 - 12 := by norm_num

/-- **Writhe-only framing is excluded.** Since `writhe(D) = writhe(T) = 4`, any framing correction
that is a function of writhe alone (`C_knot = f(writhe)`, e.g. `q₀^{c·w}` — the omitted Jones/HOMFLY
framing normalization) would force `C_knot(D) = C_knot(T)`. They differ, so no writhe-only factor
closes the deficit: `¬ ∃ v, C_knot(D) = v ∧ C_knot(T) = v` (both evaluated at the shared writhe 4). -/
theorem no_writhe_only_framing : ¬ ∃ v : ℝ, CKnot_D = v ∧ CKnot_T = v := by
  rintro ⟨v, hD, hT⟩
  have : CKnot_D = CKnot_T := hD.trans hT.symm
  unfold CKnot_D CKnot_T at this; norm_num at this

/-!
### A structural REASON for non-universality: the chirality regime `(−1)^{C(3A,2)}`

Beyond the mirror inequality (which shows per-knot content *within* a level), there is a clean
level-parity reason the deuteron cannot share a `C_knot` regime with the heavier isotopes. Under
conjugation the `n`-statistic satisfies the Macdonald identity `n(λ) + n(λ') = C(n,2)` (verified
numerically at `n = 6`: all five conjugate pairs flip the binding sign, the self-conjugate `(3,2,1)`
is fixed). Hence the binding sign `sgn(λ) = (−1)^{n(λ)}` obeys `sgn(λ') = (−1)^{C(n,2)} · sgn(λ)`: it
**antisymmetrizes** conjugate pairs iff `C(n,2)` is odd.
-/

/-- **The conjugation law for the binding sign** (pure exponent arithmetic, no hypothesis needed):
`(−1)^{n(λ')} = (−1)^{n(λ) + n(λ')} · (−1)^{n(λ)}`. With the Macdonald identity `n(λ) + n(λ') = C(n,2)`
this is `sgn(λ') = (−1)^{C(n,2)} · sgn(λ)` — the chirality regime is fixed by the parity of `C(n,2)`. -/
theorem sgn_conj (nl nl' : ℕ) :
    (-1 : ℝ) ^ nl' = (-1) ^ (nl + nl') * (-1) ^ nl := by
  have hsq : ((-1 : ℝ)) ^ nl * ((-1 : ℝ)) ^ nl = 1 := by
    rw [← pow_add]; exact Even.neg_one_pow ⟨nl, rfl⟩
  calc (-1 : ℝ) ^ nl' = (-1) ^ nl' * 1 := by ring
    _ = (-1) ^ nl' * ((-1) ^ nl * (-1) ^ nl) := by rw [hsq]
    _ = (-1) ^ (nl + nl') * (-1) ^ nl := by rw [pow_add]; ring

/-- **The deuteron sits in a DIFFERENT chirality regime than the heavier light isotopes.** With
`n = 3A`: `C(6,2) = 15` is ODD (A=2, deuteron → sgn antisymmetrizes conjugate pairs, bar-odd-projected)
while `C(9,2) = 36` (A=3, T/³He) and `C(12,2) = 66` (A=4, ⁴He) are EVEN (sgn preserved). So the
deuteron's binding-sign structure is qualitatively unlike A ≥ 3 — a structural reason `C_knot(D)`
cannot lie on the same universal curve as the heavier isotopes, independent of the mirror inequality
above. -/
theorem deuteron_chirality_regime_differs :
    Nat.choose 6 2 % 2 = 1 ∧ Nat.choose 9 2 % 2 = 0 ∧ Nat.choose 12 2 % 2 = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

end QOU.MassTheory.CKnotNonUniversal
