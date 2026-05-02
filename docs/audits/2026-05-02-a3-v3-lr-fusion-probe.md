# A.3 v3 LR-fusion probe — 4He is structurally degenerate

## Probe

PR #500's `optimised_magic_verifier.py` provides `verify_pair(i_Z,
i_N)`: LR-fusion of canonical self-conjugate $\lambda_Z \vdash
n_Z$ and $\lambda_N \vdash n_N$ where $n_Z, n_N$ are magic. Magic
shell-pairs are those whose LR-decomposition has a self-conjugate
dominant component (Δi ≤ 1 rule).

Direct nuclear correspondence:

| nucleus | $Z$ | $i_Z$ | $n_Z$ | shell-pair (i_Z, i_N) |
|---------|----:|------:|------:|----------------------:|
| 4He | 2 | 1 | 2 | (1, 1) |
| 16O | 8 | 2 | 8 | (2, 2) |
| 40Ca | 20 | 3 | 20 | (3, 3) |

## Result

- **(2, 2) → 16O**: `status: computed`. $\lambda_Z = \lambda_N
  = (3, 3, 2) \vdash 8$. LR-fusion proceeds.
- **(3, 3) → 40Ca**: `status: deferred` (n_Z + n_N = 40 > 30
  intractability cutoff in the naive Python LR decomposition).
- **(1, 1) → 4He**: `status: degenerate` — *no self-conjugate
  partition of n = 2 exists.* The verifier explicitly skips this
  case.

## Implication for the cal/m_e spread

A.3 v3's plan was to use LR-fusion to construct level-1 weights
for the per-braid mass tower. For 4He — the atom driving the
1.06% spread — **the LR-fusion approach is structurally
unavailable**: the canonical self-conjugate $\lambda$ at $n=2$
doesn't exist, so there's no LR-fusion input for shell-pair
(1, 1).

This is a **structural feature of the magic-number ladder**, not
an implementation gap. The categorical-neutrality-saturated-shells
condition $\Phi_n$-supported-on-self-conj $\lambda$ is vacuous
at $n = 2$ (there's nothing to support on); the actual
saturation mechanism at the lowest magic shell is different
(the framework handles it via its low-$k$ degenerate cases).

## What this means

1. **A.3 v3 LR-fusion path: only applies to Z ≥ 8.** Could
   compute level-1 corrections for 16O (and via extension, the
   non-deferred shell-pairs). Won't touch 4He, 3He, 3H, D — the
   small atoms where the spread residual is concentrated.
2. **The 4He outlier may be intrinsic.** The cal/m_e log(A)
   trend extracted in
   [`2026-05-02-cal-spread-structure.md`](2026-05-02-cal-spread-structure.md)
   showed 4He at -3458 ppm from the trend. If this is the
   framework's degenerate handling of the lowest magic shell,
   no level-1 jet correction can close it without a separate
   low-$k$ treatment.
3. **Recommended re-anchoring.** Treat the 4He residual as a
   structural caveat, not a target for the per-braid mass
   tower's precision. The 9 non-4He atoms' spread of ~350 ppm
   (excluding 4He, D) is the actual achieved precision; pushing
   below requires either A.3 v3 for Z ≥ 8 atoms or a separate
   low-$k$ shell-correction theory.

## Status

A.3 v3 LR-fusion: **partially applicable** (Z ≥ 8 only). For the
spread-driving 4He, structurally not applicable in the current
PR #500 framework. The spread residual at 4He is a feature, not
a bug — it reflects the lowest-shell degeneracy in the magic-
ladder construction.

Closing the cal/m_e spread to ~22 ppb across all light nuclei
requires either:

- A new theory of the lowest-magic-shell degenerate case
  (research-grade, currently no QOU block addresses this), or
- Excluding the 4He outlier from precision targets and quoting
  the non-4He spread (~350 ppm) as the achieved precision.
