# Q_beta H_4(q) Sign-Block Hypothesis (Audit Note)

**Date:** 2026-06-13
**Probe:** `computations/qbeta/qbeta_h4_sign_block_exact.py`
**Status:** Hypothesis (Unproven)

## 1. The Hypothesis
The 2026-06-13 Deep Audit falsified the necessity of an infinite "precision ladder" ($c_k u^k$) for the $Q_\beta$ nucleon mass split, proposing instead that generation/flavor shifts map to exact categorical subtractions of 1-dimensional "sign" representations.
Specifically, since the nucleons live in the 4-strand fiber $H_4(q)$, the hypothesis states that $\Delta m_{np}$ corresponds structurally to the subtraction of the $(1,1,1,1)$ sign-block representation.

## 2. Probe Findings
The exact symbolic probe using `mp.dps=50` yielded:
- $W_{(1,1,1,1)} = 1 / [4]_q! \approx 0.03975$
- Evaluated over the deformation gap: $W_{(1,1,1,1)} \cdot (q_0 - 1) \approx 0.00437$
- Experimental $\Delta m_{np} / m_p \approx 0.00137$

## 3. Strict "Formalize-First" Directive
While the logarithmic scales align and the categorical trace successfully bypasses float-imprecision, the raw scalar ratio is $\approx 3.17$. 
**We do not wire empirical fits.** The hypothesis remains strictly unproven. 
Before any integration into the core mass formula or the `1ppq-qbeta` backlog is permitted, we must:
1. Prove the exact cross-anchor constraints (proton vs muon calibrations).
2. Establish the exact geometric normalization framing (e.g., is there an missing $1/\pi$ or geometric phase factor from the knot complement volume?).
3. Verify the parity constraints of the nucleon braid over $H_4(q)$.

The `1ppq` integration backlog remains open until the symbolic derivation is exact.
