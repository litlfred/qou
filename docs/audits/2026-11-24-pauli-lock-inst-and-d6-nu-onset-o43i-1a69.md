# Audit Ledger: Pauli-Lock Spin/Isospin Diagnostic (`qou-o43i`) and Depth-1 $\nu_{n-1}$ Closed Form + $n_1 = 8$ Onset (`qou-1a69`)

**Date:** 2026-11-24
**Branch:** `claude/pauli-lock-inst-d6-nu-o43i-1a69-20261124`
**Beans:** `qou-o43i`, `qou-1a69` (epic `qou-s028` / programme `qou-10v9`)
**Status:** Verified (`0 sorry`, `0` custom axioms, `0` non-circular application sites of `separable_interface_degenerate` preserved under `scripts/separable-interface-instantiation-audit.py --strict`, 80-dps + exact-`Fraction` witness green).

---

## 1. Executive Summary

| Bean | Scope | Deliverable | Key Mathematical Result |
|---|---|---|---|
| `qou-o43i` | Pauli-lock equal-scalars diagnosis & spin/isospin obstruction | `QOU/Nuclear/PauliLockSpinIsospinDiagnostic.lean` | Proves that under unit-sum normalization (`s₊ + s₋ = 1`, `μ₊ + μ₋ = 1`, `f_ℓ ≠ 0`), S-wave separable channel degeneracy holds **if and only if** `(s₊, s₋) = (μ₊, μ₋)`; connects `isoMuPlus` / `isoMuMinus` directly to `InterfaceScalar` (`H₂` weights) and `GramSignature` (`H₃` branching + band separation); derives exact two-row `SU(2)` rational closed forms `μ₊(q) = (q⁴+q²+1)/(q²+1)²`, `μ₋(q) = q²/(q²+1)²`, `1 - 4μ₊μ₋ = (q⁴+1)²/(q²+1)⁴ > 0`; proves `A5Irrep` has zero 2D spinor irreps (`dims = [1,3,3,4,5]`) whereas `2I ⊂ SU(2)` carries two 2D spinors (`2 ⊗ 2 = 1 ⊕ 3`), and undeformed spin weights `(3/4, 1/4)` equal `(μ₊(q), μ₋(q))` **iff** `q² = 1` (discrepancy `(q²-1)² / (4(q²+1)²)`). |
| `qou-1a69` | D6 depth-1 $\nu_{n-1}$ closed form & $n_1 = 8$ sign onset | `QOU/BraidsAndKnots/YoungDiagramTailSecondInstance.lean` | Proves **end-to-end** on `YoungDiagramKernelPincer.nuV` for **every** $n \ge 4$ (`0 sorry`, no cap, `Nat.choose_pos` discharged) that $\nu_{n-1}(n) = \frac{(n-1)(n-4)(n^3 - 11n^2 + 32n - 30)\binom{2n-6}{n-3}}{3\,n!}$, verifies the exact rational values at $n = 4..9$ (`0, -4/3, -5/3, -1/6, 119/60, 88/27`) against `wlambda-covariance-epic-A2-tail-second-instance.witness.json`, and proves the complete sign equivalences (`= 0 ↔ n = 4`, `< 0 ↔ n ∈ {5,6,7}`, `> 0 ↔ 8 ≤ n`, `≥ 0 ↔ n = 4 ∨ 8 ≤ n`). |

---

## 2. Detailed Findings on `qou-o43i`

1. **Why `separable_interface_degenerate` remains at `0` corpus application sites:**
   - On the isospin side, `InterfaceScalar` and `GramSignature` determine the `H₂` projector scalars
     $$\mu_+(q, z) = \frac{z + q^{-1}}{q + q^{-1}}, \qquad \mu_-(q, z) = \frac{q - z}{q + q^{-1}}, \qquad \mu_+ + \mu_- = 1.$$
   - On the spin side, neither `BringFiberAction` (`A5Irrep → IcosahedralRotation`, where `A5Irrep` has dimensions `[1, 3, 3, 4, 5]` and zero 2-dimensional spinor irreps) nor `SpinFromSo3Fiber` (`levelCoeff : ℕ → R` on the 3-strand Borromean `h^{2n}` expansion) constructs a two-channel spin projector scalar pair. Instantiating `fSpin := fIso` by hand would posit the antecedent rather than check a corpus construction; `scripts/separable-interface-instantiation-audit.py --strict` continues to gate `0` applications.
2. **Sharp equivalence and obstruction theorems (`QOU/Nuclear/PauliLockSpinIsospinDiagnostic.lean`):**
   - `unit_sum_channel_degenerate_iff_equal_scalars`: over any integral domain, when $s_+ + s_- = 1$, $\mu_+ + \mu_- = 1$, and $f_\ell \neq 0$,
     $$s_+ \mu_- f_\ell = s_- \mu_+ f_\ell \iff (s_+ = \mu_+ \land s_- = \mu_-),$$
     because $s_+ \mu_- - s_- \mu_+ = s_+ - \mu_+$.
   - At the two-row $SU(2)$ Markov parameter $z = q^3 / (q^2 + 1)$, the isospin scalars reduce to
     $$\mu_+(q) = \frac{q^4 + q^2 + 1}{(q^2 + 1)^2}, \qquad \mu_-(q) = \frac{q^2}{(q^2 + 1)^2}, \qquad 1 - 4\mu_+(q)\mu_-(q) = \frac{(q^4 + 1)^2}{(q^2 + 1)^4} > 0.$$
   - Passing from `I ⊂ SO(3)` (`A5Irrep`) to its binary icosahedral double cover `2I ⊂ SU(2)` introduces two 2-dimensional spinor irreps (`binaryIcosahedral_two_dim_spinors`) whose tensor square decomposes dimensionally as $1 + 3 = 4$ (`A ⊕ T₁`). On that undeformed spin decomposition, the normalized weights $(3/4, 1/4)$ satisfy
     $$\mu_+(q) - \frac{3}{4} = \frac{1}{4} - \mu_-(q) = \frac{(q^2 - 1)^2}{4(q^2 + 1)^2},$$
     vanishing **if and only if** $q^2 = 1$ (`classicalSpin_eq_twoRowIso_iff_q_sq_eq_one`). At the canonical proton pin $q_0 = 1.1099785827\dots$, this discrepancy is $2.70211325196540159\times 10^{-3} > 0$.

---

## 3. Detailed Findings on `qou-1a69`

1. **Full general-$n$ derivation on `YoungDiagramKernelPincer.nuV` (`QOU/BraidsAndKnots/YoungDiagramTailSecondInstance.lean`):**
   - Using `DepthOneHookClassification.mul_sytDim_twoCorner`, $(n - 1) f^{(i+2, 2, 1^{n-4-i})} = (u(n, i+2) - (n - 1))\binom{n}{i+2}$ with $u(n, j) = j(n - j)$.
   - Multiplying $6 \sum_{\lambda \in \text{depthOneShapes}(n)} (f^\lambda)^2 \omega_3(n, \lambda)$ by $(n - 1)^2$ unites $[n]$ ($j = n$), $1^n$ ($j = 0$), the two vanishing hooks ($j = 1, n - 1$), and all $n - 3$ two-corner shapes ($2 \le j \le n - 2$) into
     $$2(n - 1) \sum_{j=0}^n \bigl(u(n, j) - (n - 1)\bigr)^2 \bigl(n(n - 2) - 3 u(n, j)\bigr) \binom{n}{j}^2.$$
   - Symmetric binomial absorption $u(m+2, k+1)\binom{m+2}{k+1} = (m+2)(m+1)\binom{m}{k}$ evaluates the $u^0, u^1, u^2, u^3$ moments in division-free form, collapsing the sum to `nuV_depthOne_closed_form` for **every** $n \ge 4$.
2. **Onset $n_1 = 8$ and probe witness verification:**
   - Because $n^3 - 11n^2 + 32n - 30 = (n - 8)\bigl((n - 2)^2 + (n - 1) + 5\bigr) + 34$ (single real root $\rho = 7.077574223045071\dots \in (7, 8)$), `nuV n (n - 1)` is `0` at $n = 4$, strictly negative at $n = 5, 6, 7$ (`-4/3, -5/3, -1/6`), and strictly positive for all $n \ge 8$ (`119/60` at $n = 8$, `88/27` at $n = 9$), matching `computations/deltalambda/wlambda-covariance-epic-A2-tail-second-instance.witness.json` on all 22 rows ($n = 4..25$) and verified in exact `Fraction` + 80-dps `mpmath` through $n = 40$ in `computations/probes/pauli_lock_and_d6_nu_onset_probe.py`.
