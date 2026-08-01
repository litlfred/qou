# C1's explicit formal solution at ∞ and its q-Gevrey-½ divergence (2026-08-01)

**Branch:** `claude/c3-w2-inf-formal-solution-2026-08-01`. **Feeds:** W2 (`qou-xufp`), the
Birkhoff-matrix ∞-side of the C1 module. Concrete forward step in the dedicated ∞-Stokes
work; the actual Stokes multipliers remain the residual.

## The explicit formal solution

Solving `L1 f = 0` at `∞` (`L1 = (q²x−1)σ² − (q−1)σ − (q−1)`, `C1`) with the ansatz
`f(x) = ∑_{n≥0} cₙ x^{−n}` gives the exact coefficient recurrence
(witness `computations/qbeta/c3_w2_inf_formal_solution.witness.json`):

  `c_{m+1} = c_m·(1 + (q−1)q^m + (q−1)q^{2m})`,   `c_0 = 1`.

So `c_n = ∏_{m=0}^{n−1} (1 + (q−1)q^m + (q−1)q^{2m})`. The ratio `c_{m+1}/c_m` has leading
term `(q−1)q^{2m}`, q-degree `2m+1`; hence

  **`deg_q(cₙ) = ∑_{m<n}(2m+1) = n²`**   (verified symbolically for `n ≤ 9`).

## Why this is the ∞ Stokes signature

`deg_q(cₙ) = n²` means the coefficients grow like `q^{n²}` — the formal series is
**q-Gevrey (divergent)**, not convergent. A convergent (Fuchsian) solution would have
bounded-degree coefficients; the `q^{n²}` growth is exactly the irregular slope-½ behaviour.
Consequently:

- the formal solution must be **q-Borel/Laplace summed** (the kernel is the theta family,
  `QBorelKernel`); the summation is sector-dependent;
- the **Stokes multiplier(s) `U ∈ ℂ²`** are the difference between the summed solutions across
  the two sectors (`F(P₁,P₂) ≅ Matr(ℂ)²`, RSZ §3.3). This sector-difference / Borel–Laplace
  summation (RSZ §4–5, q-analog of Birkhoff–Malgrange–Sibuya) is the **residual** — genuinely
  RSZ-wild, beaned `qou-xufp`.

## What landed

- `computations/qbeta/c3_w2_inf_formal_solution.py` + witness — the explicit recurrence and
  the `deg_q(cₙ) = n²` growth.
- `QOU/Mass/C1FormalSolutionGrowth.lean` (sorry-free) — the growth identity
  `c1FormalDeg n = ∑_{m<n}(2m+1) = n²` (`c1FormalDeg_eq_sq`) and the per-step increment
  `2n+1` (`c1FormalDeg_step`).
- Building blocks from earlier: `QBorelKernel` (theta kernel), `QCharacter.ratio_qInvariant`
  (why the sums differ by an elliptic/theta factor).

## Honest status

The ∞ formal solution is now **explicit and its divergence proved** (`deg = n²`). The
remaining step — actually summing it and extracting the two Stokes multipliers — is the
RSZ-wild analytic core, not a session brick. No fit; nothing wired; no `symbol=C1` claim.

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§3.3 q-Borel, §4-5 Stokes)
-- Ref: [manuscript] docs/audits/2026-08-01-c1-inf-slope-half-rsz-stokes.md
