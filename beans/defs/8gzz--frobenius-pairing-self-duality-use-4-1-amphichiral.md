---
# 8gzz
title: 'Frobenius-pairing + self-duality: use 4_1 amphichirality (self-mirror) + Markov-trace Frobenius form in Â_K construction'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-30T20:35:58Z
updated_at: 2026-11-16T19:07:00Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- **Resolution:**
  - Extended `folio/quantum-observable-universe/lean/QOU/Knot/FigureEightSelfDuality.lean` (`0` `sorry`, `0` self-assuming audit hits) with §2 (`Markov-trace Frobenius pairing and 4₁ amphichiral self-duality`) over any `[CommRing R]` and `[Ring A]`:
    - `figureEightCrossingSigns`, `figureEightWrithe`, `figureEightWrithe_eq_zero`: proves writhe vanishing $w(4_1) = 1 - 1 + 1 - 1 = 0$ for $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$.
    - `frobeniusPairing τ σA x y := τ (x * σA y)` and `sigma_frobeniusPairing`: proves $\sigma$-Hermitian symmetry $\sigma(\langle x, y \rangle) = \langle y, x \rangle$ from trace cyclicity, anti-involutivity of $\sigma_A$, and $(\sigma_A, \sigma)$-equivariance of $\tau$.
    - `sigma_frobeniusPairing_self`, `frobeniusPairing_self_barOdd_zero`, `frobeniusPairing_self_barEven_two`: proves every diagonal Frobenius pairing $\langle x, x \rangle$ is $\sigma$-fixed, with zero bar-odd (CS / imaginary) part and bar-even part $2\langle x, x \rangle$.
    - `frobeniusPairing_amphichiral_eq_trace_sq`: proves $\langle u, u \rangle = \tau(u^2)$ for amphichiral ($\sigma_A(u) = u$) elements.
    - `frobeniusPairing_mul_adjoint` and `frobeniusPairing_amphichiral_selfAdjoint`: proves $\langle x \cdot a, y \rangle = \langle x, y \cdot \sigma_A(a) \rangle$ and self-adjointness of right multiplication by an amphichiral element $u$ in the $\hat{A}_{4_1}$ module construction.
  - Status kept at `in-progress` pending PR #8160 merge and owner verification.
