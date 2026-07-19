**Projection theorems (require `Field R`)**

**Proposition (Lean: `bar_inv x`).** $\overline{x^{-1}} = (\overline x)^{-1}$ over a field.
*Proof.* If $x = 0$: both sides are $0$ (from $\overline 0 = 0$ + $0^{-1} = 0$ convention). If $x \neq 0$: $\overline x \neq 0$ (bar is injective by involutivity), and $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$, hence $\overline{x^{-1}} = (\overline x)^{-1}$. $\square$

**Proposition (Lean: `bar_half`).** $\overline{1/2} = 1/2$ over a field.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$ via `bar_inv` and `bar_two`. $\square$

**Proposition (Lean: `isBarSymmetric_intCast n`).** Every integer scalar is bar-symmetric.
*Proof.* For $n = \mathrm{ofNat}\, k$: use `bar_natCast`. For $n = \mathrm{negSucc}\, k = -(k+1)$: $\overline{-(k+1)} = -\overline{k+1} = -(k+1)$ via `bar_neg` + `bar_natCast`. $\square$

**Proposition (Lean: `barSymmetricProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{avg}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $\square$

**Proposition (Lean: `barSymmetricProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{avg}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x - x)/2 = 0$. $\square$

**Proposition (Lean: `barSkewProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - (-x))/2 = x$. $\square$

**Proposition (Lean: `barSkewProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - x)/2 = 0$. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_even_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$.
*Proof.* $x^{2n}$ is bar-symmetric by `pow_two_mul`; apply `of_sym`. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_odd_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* $x^{2n+1}$ is bar-anti-sym by `pow_two_mul_add_one`; apply `of_antisym`. **This is "the framework projects away odd-power components" at the formal level.** $\square$

**Theorem (Lean: `barSymmetricProjection_isBarSymmetric x`).** $P_{\mathrm{avg}}(x)$ is bar-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{avg}}(x)} = \overline{(x + \overline x)/2} = \overline{x + \overline x} \cdot \overline{1/2} = (\overline x + x) \cdot (1/2) = P_{\mathrm{avg}}(x)$ via `bar_half`. $\square$

**Theorem (Lean: `barSymmetricProjection_idempotent x`).** $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$.
*Proof.* $P_{\mathrm{avg}}(x)$ is bar-symmetric by the previous theorem; applying $P_{\mathrm{avg}}$ to a bar-symmetric input gives the input back by `of_sym`. $\square$

**Theorem (Lean: `barSkewProjection_isBarAntiSymmetric x`).** $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric.
*Proof.* $\overline{P_{\mathrm{skew}}(x)} = \overline{(x - \overline x)/2} = (\overline x - x) \cdot (1/2) = -P_{\mathrm{skew}}(x)$. $\square$

**Theorem (Lean: `barSkewProjection_idempotent x`).** $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* Analogous to $P_{\mathrm{avg}}$ idempotency via `barSkewProjection_of_antisym`. $\square$

All 33 theorems / definitions in [`bar-involution.lean`](bar-involution.lean) have narrative proofs here and `sorry`-free Lean proofs.
