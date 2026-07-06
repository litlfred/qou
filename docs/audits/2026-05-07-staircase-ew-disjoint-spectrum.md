# Staircase EW disjoint-braid spectrum — restored k=3..5 check

Date: 2026-05-07

Restored `/home/runner/work/qou/qou/computations/staircase_ew_disjoint_spectrum.py` and reran the disjoint braid

$$
\beta_{\mathrm{EW}} = \sigma_1^4 \cdot \sigma_3^6 \cdot \sigma_5^8.
$$

## Verified result in the current checkout

- `ρ₃ = (3,2,1)`, dim `16`: exactly 8 eigenvalue buckets, multiplicity `2` each.
- `ρ₄ = (4,3,2,1)`, dim `768`: exactly 8 eigenvalue buckets, multiplicity `96` each.
- `ρ₅ = (5,4,3,2,1)`, dim `292864`: full diagonalization skipped; the diagonal pure sector has `52224` tableaux, again in the same 8 exact buckets.

The exact bucket values are

$$
q^{\pm 18},\; q^{\pm 10},\; q^{\pm 6},\; q^{\pm 2}.
$$

## Interpretation

In this implementation, the stale `q^{1/(2k-1)}` residual claim does **not** survive for the disjoint braid alone.  The best pairwise scans at `k=3,4` collapse to the degenerate ratio `1`, not to `q^{1/5}` or `q^{1/7}`.

So any nontrivial residual must come from a non-disjoint interface contribution (for example an EW `Δ_I` term), not from `σ₁⁴ σ₃⁶ σ₅⁸` by itself.
