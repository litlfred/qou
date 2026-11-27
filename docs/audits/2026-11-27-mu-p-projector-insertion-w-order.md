# μ–p residual: Hecke projector insertions on 4₁ do not force the w² dressing

Date: 2026-11-27. Bean `qou-6gf9` (compute-accuracy C3, epic `qou-myts`). PR #9445.
Owner choice (decision card, 2026-11-27): option 1, "derive or refute −(3α/4π)·w²".
Lean: `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuPProjectorInsertionWOrder.lean`.
Probe: `computations/probes/mu_p_projector_insertion_w_order_probe.py`, witness
`computations/probes/mu-p-projector-insertion-w-order.witness.json` (4/4 assertions).

## Question

At the proton pin, `m_μ/m_e = Vol(4₁)/ℏ_q²` overshoots CODATA-2022 by +211.2 ppb
(9.5σ, σ = 22.2 ppb). The data determine the gap to about one significant digit
(10.5 %). PR #9362 (audit `2026-11-24-muon-41-fbor-poincare-worldline-adjudication.md`
§4.2) left two bar-even candidates as UNWIRED working assumptions. The closer one is
`−(3α/4π)·w²` with `w = q + q⁻¹ − 2`, at −206.86 ppb. It would count as derived only if
some natural observable of the muon carrier `4₁ = (σ₁σ₂⁻¹)²` had vanishing `O(w⁰)`
and `O(w¹)` terms and a forced `w²` coefficient. That audit had already measured
the naive one-vertex `O(w)` scale as 90× too large.

## Class tested

The photon projector `e_i = (q − σ_i)/[2]_q`, inserted once or twice into the 4₁ word.
The setup uses the corpus's 3-dimensional representation and the SU(2) Markov weights
`y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²` and `y₁₁₁ = 0`, normalised by
`tr_M(4₁) = (q¹⁰+1)/(q²(q²+1)³)`. The covariant observables are:

- the bar-symmetric single insertion `⟨e₁⟩ + ⟨e₂⟩`;
- `S₁`, the sum over all single insertions (slots and generators);
- `D`, the sum over all double insertions;
- `C`, the connected doubles `⟨e e'⟩ − ⟨e⟩⟨e'⟩`.

## Results (exact; claim, then evidence)

1. **Single insertions are slot-independent, and the `e₁` and `e₂` insertions are bar
   images of each other.** Sympy exact over ℚ(q). Lean `trace_E1_word41` and
   `trace_E2_word41` give the closed forms `−(q⁶+q²−1)/(q⁴(q²+1))` and
   `(q⁶−q⁴−1)/(q²+1)`.
2. **The bar-symmetric single insertion is `(s⁴−6s²+7)/(s⁴−5s²+5)`, with
   `s = [2]_q`.** Lean `pairCorr_eq`, generic field. At `q = 1` it equals −1
   (`pairCorr_at_one`), so the leading term does not vanish.
3. **Exact `w`-Taylor data:**

   | observable | O(1) | O(w) | O(w²) |
   |---|---|---|---|
   | ⟨e₁⟩+⟨e₂⟩ | −1 | 20 | −203 |
   | S₁ | −4 | 80 | −812 |
   | D | −11 | 217 | −8811/4 |
   | C | −21 | 617 | −41051/4 |

   Lean `pair_taylor`, `doubles_taylor` and `connected_taylor` are exact remainder
   identities `N − den·(c₀+c₁w+c₂w²) = w³·g`. The rational `w`-forms of D and C come
   from the probe; only the single insertion is derived in Lean from the matrices.
4. **Radius of convergence.** The common denominator `s⁴ − 5s² + 5` equals
   `(q¹⁰+1)/(q⁵s)`, which is `tr_M(4₁)` up to units. Its nearest root is
   `s = 2cos(π/10)`, so `w* = 2cos(π/10) − 2 = −0.097887`. The proton pin sits at
   `w/|w*| = 0.1113`. Every `w`-expansion of this class therefore grows by roughly
   10× per order. That growth is why the coefficients above get large, and it is a
   property of the trace normalisation, not a choice.
5. **The w² coefficient is not forced.** The 3×4 coefficient matrix (rows O(1), O(w),
   O(w²); columns 1, S₁, D, C) has rank 3. Already within `{1, S₁, D}`, the
   combination `x₀ = −3c/4`, `x₁ = 217c/16`, `x₂ = −5c` kills O(1) and O(w) and gives
   O(w²) = c for every `c` (Lean `w2_coeff_not_forced`). Cancelling the two lower
   orders takes a two-constraint choice of non-structural ratios (−217/80, 3/20), and
   after that the `w²` coefficient is whatever one wants.

## Comparison (this is where the empirical claim lives; no proof uses it)

The candidate needs a `w²` coefficient of 3α/4π = 1.742 × 10⁻³ (CODATA α). The
smallest natural `|w²|` coefficient in this class is 203, five orders larger. Even an
explicit factor of α (2.0 × 10⁻³ per insertion pair) leaves the class's natural `w²`
terms 10²–10⁴ times larger than the candidate. These ratios are diagnostics, not
targets.

## Verdict and scope

**Scope (a).** The Hecke photon-projector insertion class on 4₁ does not derive
`−(3α/4π)·w²`. No member has vanishing O(1) or O(w), and once both are cancelled by
choice, the w² coefficient is free. This bars a derivation through this class; it is
not a structural exclusion (b) of a w² dressing from every construction. The
candidate stays an unwired working assumption, and its 0.2σ agreement remains
selection-shaped under the 10.5 % entropy bound.

Not covered, and still open: an open-worldline (non-closed, non-Markov) reduction
with its own normalisation; insertions in the full Hecke algebra with nonzero
`y₁₁₁`. The parallel Σ(2,3,5) Borel-resummation route (PR #9459, audit
`2026-11-27-sigma235-borel-resummation-mu-p.md`) closed in scope (a) on the same
day: its trans-series sectors at q₀ are 4.3 × 10⁻² and 8 × 10⁻⁶⁸, and the residual
falls between them.

## Corpus-grep note

Searched: `docs/audits` (mu-p, projector, double-commutator), bean `qou-6gf9` (full
body), `qou-1ozb`, `qou-2002`, and PR #9362's audit §4.2. The only prior projector
numbers are #9362's three point values at `q_p` (−0.54762, +0.11671, +0.60499). This
audit is the first exact ℚ(w) treatment, and the first to look at whether the w²
coefficient is forced.
