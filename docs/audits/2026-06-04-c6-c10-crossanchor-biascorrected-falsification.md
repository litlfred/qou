# c_6..c_10 closed forms — cross-anchor vs bias-corrected extraction (2026-06-04)

> **⮕ Encoded in the authoritative registry**
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
> (§3: c_6/c_7 self-consistent, c_8/c_9/c_10 pattern breaks). Read the registry
> for the consolidated c_k / d_k status.

> **Finding**: against PR #1824's **bias-corrected** q₀ extraction, the
> Pell-Lucas σ-action closed forms are **anchor-stable** (proton↔muon swing
> 2.4×10⁻⁷ %) and **exact at the silver ratio**, but the pattern **breaks at
> the first FREE rung c_8** (closed +2.27 vs bias-corrected −0.215, wrong
> sign). c_6/c_7 are *imposed* in the extraction, so their recovery is
> self-consistency, not independent validation. Tier unchanged: `empirical —
> silver-anchored`. No production change.

## Supersedes the raw-extraction first cut (PR #1833)

The first cut of this probe (PR #1833) compared the closed forms against the
**raw** `(R−1)/(b^k·ℏ^{2k})` extraction (c_8 ≈ 7649, c_9 ≈ 8.98×10⁵). PR #1824
(merged the same day) landed a **truncation-bias-corrected** extraction
(`ck_bias_corrected_leading`) that supersedes those raw values. This audit
re-runs the test against the corrected series; the verdict (forms are
silver-only) is unchanged, but the numbers and the framing are sharper.

## The applied-vs-free distinction (the key honesty point)

The canonical extraction (`qbeta_decay_sdp_extended_ck.py`) **imposes** closed
forms at rungs c_2..c_7 to advance the residual `R`, then extracts c_8, c_9,
c_10 **freely** (no form imposed). Therefore:

- **c_6, c_7 are APPLIED.** The bias correction recovering them (3.011 ≈ 4·b²,
  −8.021 ≈ −8) is a self-consistency check on the *bias-correction method* —
  **not** an independent confirmation of the forms.
- **c_8 is the FIRST FREE RUNG.** Its bias-corrected value (−0.215) is the
  first genuine test of the Pell-Lucas continuation — and it does **not** match
  the predicted 4·b⁴ ≈ +2.27 (wrong sign).

## Result

[`qbeta/qbeta_c6_c10_crossanchor_falsification.py`](../../computations/qbeta/qbeta_c6_c10_crossanchor_falsification.py)
→ [witness](../../computations/qbeta/qbeta-c6-c10-crossanchor-falsification.witness.json) (4/4 assertions)

| rung | closed(q₀) | bias-corrected | raw (old #1833) | role | match |
|------|-----------|----------------|-----------------|------|-------|
| c_6 | 3.011 (4·b²) | 3.0107 | 3.498 | **APPLIED** | ✓ 0.005% |
| c_7 | −8 | −8.021 | 57.15 | **APPLIED** | ✓ 0.26% |
| c_8 | 2.266 (4·b⁴) | **−0.215** | 7649 | **FREE** | ✗ wrong sign |
| c_9 | −6.02 (−8·b²) | −297.3 | 897808 | FREE | ✗ |
| c_10 | 1.706 (4·b⁶) | 1.054×10⁸ | 1.054×10⁸ | FREE | ✗ |

- **Silver exactness**: all of c_6..c_10 hit 7/2, −8, 49/16, −7, 343/128. ✓
- **§8 form swing** (proton↔muon): max 2.4×10⁻⁷ % ≪ 1 % → anchor-stable. ✓
- **Free-rung continuation**: the pattern breaks at c_8. ✗

## Interpretation

The Pell-Lucas σ-action closed forms are **silver-ratio structural identities**,
not q₀ production coefficients. They are exact at q = 1+√2 and smooth/stable in
`q`, but the *free* q₀ extraction (the first rung where no form is imposed) does
not continue the pattern even after bias correction. Same shape as the c_3
[3]_q/25 rigidity finding
([`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)):
a smooth real-q form is exact at one structural anchor and does not represent
the q₀ residual structure (a fibre-level object per CLAUDE.md §"Im(q) at fibre
vs observable level").

## Consequences

1. **Tier unchanged.** c_6/c_7 and c_8/c_9/c_10 stay `empirical`. Registry rows
   updated: c_6/c_7 carry a self-consistency caveat; c_8-c_10 record the
   pattern-break at the first free rung (vs the now-superseded raw ratios).

2. **The silver-ratio result is real but bounded.** The closed forms are exact
   at q = 1+√2 (Lean `norm_num`-trivial, built via the `QBetaCnAtSilver.lean`
   mirror). They are not q₀ production coefficients.

3. **No production wire.** §8 flip-flop guard stands.

## Cross-refs

- c_8/c_9/c_10 closed forms + silver Lean: PR #1793; Lake mirror + raw-extraction first cut: PR #1833
- bias-corrected extraction: PR #1824 (`qbeta_ck_truncation_bias_correction_probe.py`)
- c_3 [3]_q/25 cross-anchor rigidity: [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
- CLAUDE.md §"Critical framing — Im(q) at fibre vs observable level"
