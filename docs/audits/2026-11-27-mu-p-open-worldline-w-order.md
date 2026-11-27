# μ–p residual: open-worldline projector insertions on 4₁ do not force the w² dressing

Date: 2026-11-27. Bean `qou-6gf9` (compute-accuracy C3, epic `qou-myts`).
Owner choice (decision card, 2026-11-27): "both" of the two new research paths
left open by PR #9445. This audit is the open-worldline path. The full-Hecke-weights
path (`y₁₁₁ ≠ 0`, symbolic Ocneanu parameter) went to a sibling thread.
Lean: `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuPOpenWorldlineWOrder.lean`.
Probe: `computations/probes/mu_p_open_worldline_w_order_probe.py`, witness
`computations/probes/mu-p-open-worldline-w-order.witness.json` (4/4 assertions).

## Question

PR #9445 (`2026-11-27-mu-p-projector-insertion-w-order.md`) showed that
photon-projector insertions into `4₁ = (σ₁σ₂⁻¹)²`, normalised by the closed knot
trace `tr_M(4₁)`, do not force a `w²` coefficient (`w = q + q⁻¹ − 2`), so they
cannot derive the unwired candidate `−(3α/4π)·w²` for the +211.2 ppb μ–p residual.
It also found that the closed class's `w`-expansions grow about 10× per order,
because `tr_M(4₁)` vanishes at `w* = 2cos(π/10) − 2 = −0.0979`. It named an
open-worldline reduction "with its own normalisation" as untested.

## Class tested

Leave the muon worldline open: the `(1,1)`-tangle reduction, normalised by the
unknot (`tr_M(1) = y₃ + 2y₂₁ = 1`, Lean `trM_one`) and not by the knot. The
observables are the un-normalised traces `tr_M(X·4₁)`. They use the same
3-dimensional representation and SU(2) Markov weights (`y₁₁₁ = 0`, convention D)
as #9445. The covariant members are:

- the knot trace `tr_M(4₁)` itself;
- the bar-symmetric single insertion `tr_M((e₁+e₂)·4₁)`;
- `S₁`, the sum over all single insertions;
- `D`, the sum over all double insertions;
- `C`, the connected doubles.

Any Markov-property partial trace of strands 2–3 lands here, since
`tr_M = tr_M ∘ E`, so the open class differs from the closed one only by the
normalisation.

## Results (exact; claim, then evidence)

1. **The closed class is the open class divided by the knot trace.** Lean
   `open_closed_ratio` (definitional), and the probe checks it exactly on the pair.
2. **Closed forms in `s = [2]_q`.** The open pair is `(s⁴−6s²+7)/s²` and
   `tr_M(4₁) = (s⁴−5s²+5)/s²` (Lean `openPair_eq`, `trM41_eq_s`, generic field).
   At `q = 1` they are `−1/4` and `1/4` (`open_at_one`).
3. **The only pole is `w = −2`, so the radius is 2.** Every open denominator is a
   power of `w + 2 = [2]_q` (probe: powers 2, 2, 2, 4, 4). The closed class had
   radius `0.0979`. The pin sits at `w/2 = 0.00545`, against `w/|w*| = 0.111`
   closed. So the large coefficients of #9445 (`−203`, `−8811/4`, …) come entirely
   from dividing by `tr_M(4₁)`. In the open class they are O(1).
4. **Exact `w`-Taylor data.** These are exact remainder identities
   `N − den·(c₀+c₁w+c₂w²) = w³·g`. Lean derives the knot trace and the pair from
   the matrices. The `D` and `C` numerators come from the probe.

   | observable | O(1) | O(w) | O(w²) | Lean |
   |---|---|---|---|---|
   | tr_M(4₁) | 1/4 | 11/4 | 31/16 | `knot_taylor` |
   | pair | −1/4 | 9/4 | 37/16 | `open_pair_taylor` |
   | S₁ | −1 | 9 | 37/4 | (4 × pair) |
   | D | −11/4 | 24 | 99/4 | `open_doubles_taylor` |
   | C | −27/8 | 141/4 | −229/16 | `open_connected_taylor` |

5. **The w² coefficient is not forced.** The 3×5 coefficient matrix (rows O(1),
   O(w), O(w²); columns 1, tr_M, S₁, D, C) has rank 3. The `O(1) = O(w) = 0`
   kernel is 3-dimensional, and on it `w²` takes the values `32/11, 345/44,
   −3445/88`. Already within `{1, tr_M(4₁), pair}`, the combination
   `(5c/8, −9c/8, 11c/8)` kills O(1) and O(w) and gives O(w²) = c for every `c`
   (Lean `open_w2_not_forced`). No single member has a vanishing leading term
   (`open_leading_terms_nonzero`).

## Comparison (this is where the empirical claim lives; no proof uses it)

The candidate needs a `w²` coefficient of `3α/4π = 1.742 × 10⁻³` (CODATA α). The
smallest natural `|w²|` coefficient in the open class is `31/16 = 1.9375`, about
1.1 × 10³ larger. The open normalisation closes five orders of the gap #9445
found (smallest 203), but no member is forced to the candidate. The three
remaining orders are not evidence for or against an explicit α per insertion.
That would need a derived vertex weight, and none is on record. These ratios are
diagnostics, not targets.

## Verdict and scope

**Scope (a).** The open-worldline projector-insertion class on 4₁ does not derive
`−(3α/4π)·w²`. No member has vanishing O(1) or O(w), and once both are cancelled
by a choice of non-structural ratios, the `w²` coefficient is free. This bars a
derivation through this class. It is not a structural exclusion (b) of a `w²`
dressing. The candidate stays an unwired working assumption.

What this adds beyond #9445 is a structural fact: the closed class's
divergent-looking `w`-series (radius 0.098) is an artifact of the `1/tr_M(4₁)`
normalisation. The open class is analytic out to `|w| = 2`.

Not covered: the full Hecke weights with `y₁₁₁ ≠ 0` (sibling thread; note it
leaves convention D); insertions of the full photon `γ = 1 + φ₀σ₀ + φ₁σ₁ +
φ₀₁·σ₀σ₁⁻¹` rather than the projector, whose coefficients `φ` are not derived.

## Corpus-grep note

I searched `docs/audits` (mu-p, open worldline, long knot, (1,1)-tangle), the
`qou-6gf9` bean body and #9445's audit. The only prior treatment is #9445's
closed class; this is the first unknot-normalised one.
