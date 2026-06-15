"""
Shell closure infrastructure — per-k categorical shell corrections.

STATUS:
  k=3: magic {2, 8} from LP constraint deactivation (DERIVED)
  k=7: magic {20, 28} from binding trend break (CONFIRMED)
  k≥10: magic {50, 82, 126} needs dim>15 partitions (OPEN)

CURRENT APPROACH: Gaussian proximity to empirical magic numbers.
This is the ONLY non-categorical component in the BW formula.
All coefficients, knot factors, and k-level corrections are derived.

To make shell fully categorical: compute per-partition character
at each k for each Z, accumulate shell signal. Blocked by:
  - k≥8 partitions have dim>15 (seminormal matrices too large)
  - Single-partition ([2,2]) character doesn't resolve magic Z≥16

The Gaussian width σ=[2]_q IS categorical (Hecke dimension), and
magic numbers are PREDICTED by the LP constraint hierarchy.
Only the Gaussian SHAPE (smooth vs categorical step function)
is approximate.

Reference: prop:shell-closure-nf-term-count,
           prop:nuclear-knot-classification
"""
# This module documents the shell correction status.
# The actual computation is in hecke_core.magic_proximity.
# Future: replace with per-k categorical shell from
# high-dimensional partition characters.
