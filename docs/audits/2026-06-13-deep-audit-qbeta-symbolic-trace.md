# Compute Code Review (DEEP) — 1ppQ $Q_\beta$ Subtraction vs Precision Ladder

**Date:** 2026-06-13
**Subject:** 1ppQ $Q_\beta$ shift (Nucleon $\Delta m_{np}$ tension)
**Target Files:** 
- `content/quantum-observable-universe/mass-endomorphism/qbeta-per-block-chi-closed-forms.md`
- `docs/audits/2026-06-01-habiro-ladder-bridge.md`

## 1. Narrative Check (Mismatch Identified)
The current paper narrative posits that the $Q_\beta$ nucleon shift requires evaluating the Markov trace difference $\Delta\tau_M(q)$ between the proton and neutron channels. 
- The text claims that the canonical Wenzl-Markov weights $y_\lambda(q)$ are "NOT rational in $q$" because they involve the Markov parameter $z = 1/(\sqrt{q} + 1/\sqrt{q})$, thus requiring an infinite "precision ladder" ($c_k u_{\text{ladder}}^k$) and an unknown "lifting map $f$" to match the 1 ppq tension.
- **The Falsification:** The categorical subtraction theorem (derived 2026-06-13) proves that trace differences representing generation/flavor shifts correspond exactly to the topological subtraction of 1-dimensional "sign" representations (like $(1,1,1)$ or $(1,1,1,1)$). Because 1-dimensional characters on braids are exact integers, and the unnormalized quantum dimensions $d_q(\lambda)$ are pure rational polynomials in $q$, the *entire trace difference is a pure rational function of $q$*. 
- **Conclusion:** The $\sqrt{q}$ "problem" is an artifact of forcing the trace into the Jones $z$-parameterization. When evaluated in pure $q$-space using Hecke operators, there is no $f$-map and no infinite ladder.

## 2. Code Review & Structural Gaps
- `qbeta-per-block-chi-closed-forms.lean`: The Lean code constructs a "non-canonical rational surrogate" because it assumes the canonical weights cannot be rationalized. This surrogate code is now obsolete. The true canonical weights are structurally rational when evaluating 1D block anomalies.
- `habiro_ladder_bridge.py`: This script evaluates the trace and tries to map it to a Habiro element power series ($u_{\text{ladder}}^k$). This script must be formally deprecated, as the search for $c_k$ coefficients is value-chasing a finite $q$-difference.

## 3. Recommended Actions (GitHub Issue Draft)
1. **Deprecate the Precision Ladder:** Remove the $c_k$ recursion conjectures and the $f$-map hunt from the `1ppq-qbeta` coordination ledger.
2. **Rewrite $\Delta\tau_M$ in Pure $q$-Space:** Evaluate the $H_4(q)$ trace difference purely as $W_{(1,1,1,1)} \cdot \chi^{(1^4)}(\beta_{nucleon})$, bypassing $z$.
3. **Lean Tactic Upgrade:** Use the `ring` tactic on the exact rational $q$-polynomials instead of getting stuck on `Real.mul_self_sqrt`.

## 4. QA Sidecar Update
The `qbeta-per-block-chi-closed-forms.qa.json` must be invalidated via `/integration-audit` once the exact rational formulation is committed to the Lean repository.
