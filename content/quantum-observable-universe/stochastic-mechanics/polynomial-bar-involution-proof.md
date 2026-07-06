*Proof.* By definition, $\overline p := p.\mathrm{comp}(-X)$. Evaluating at $p = X$ yields $X.\mathrm{comp}(-X) = -X$. $\square$

**Proposition (Lean: `barPoly_neg_X`).** $\overline{-X} = X$.
*Proof.* We compute $(-X).\mathrm{comp}(-X) = -(X.\mathrm{comp}(-X)) = -(-X) = X$. $\square$

**Proposition (Lean: `barPoly_C c`).** $\overline{C c} = C c$.
*Proof.* Constants are bar-fixed. We have $(C c).\mathrm{comp}(-X) = C c$. $\square$

**Proposition (Lean: `barPoly_add p q`).** $\overline{p+q} = \overline p + \overline q$.
*Proof.* This follows directly from `Polynomial.add_comp`. $\square$

**Proposition (Lean: `barPoly_mul p q`).** $\overline{p \cdot q} = \overline p \cdot \overline q$.
*Proof.* This follows directly from `Polynomial.mul_comp`. $\square$

**Proposition (Lean: `barPoly_one`, `barPoly_zero`).** $\overline 1 = 1$ and $\overline 0 = 0$.
*Proof.* These follow from `one_comp` and `zero_comp`. $\square$

**Proposition (Lean: `barPoly_involutive p`).** $\overline{\overline p} = p$.
*Proof.* We evaluate $(p.\mathrm{comp}(-X)).\mathrm{comp}(-X) = p.\mathrm{comp}((-X).\mathrm{comp}(-X)) = p.\mathrm{comp}(X) = p$. $\square$

### Power identities

**Proposition (Lean: `barPoly_X_pow_two`).** $\overline{X^2} = X^2$.
*Proof.* We expand $\overline{X^2} = \overline X \cdot \overline X = (-X)(-X) = X^2$. $\square$

**Proposition (Lean: `barPoly_X_pow n`).** $\overline{X^n} = (-1)^n \cdot X^n$.
*Proof.* We proceed by induction on $n$. The base case is $\overline 1 = 1$. For the inductive step, $\overline{X^{k+1}} = \overline{X \cdot X^k} = (-X) \cdot (-1)^k X^k = (-1)^{k+1} X^{k+1}$. $\square$

**Proposition (Lean: `barPoly_X_pow_even n`).** $\overline{X^{2n}} = X^{2n}$.
*Proof.* The coefficient is $(-1)^{2n} = 1$. $\square$

**Proposition (Lean: `barPoly_X_pow_odd n`).** $\overline{X^{2n+1}} = -X^{2n+1}$.
*Proof.* The coefficient is $(-1)^{2n+1} = -1$. $\square$

### Scalar identities

**Proposition (Lean: `barPoly_natCast n`).** Every natural-number scalar is bar-fixed in $R[X]$.
*Proof.* We proceed by induction on $n$. The base case gives $\overline 0 = 0$. The inductive step gives $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Lean: `barPoly_sub p q`).** $\overline{p - q} = \overline p - \overline q$.
*Proof.* We rewrite subtraction as addition: $p - q = p + (-1) \cdot q$. The bar involution is a ring homomorphism and fixes $-1$. $\square$

**Proposition (Lean: `barPoly_neg p`).** $\overline{-p} = -\overline p$.
*Proof.* We apply subtraction to $0 - p$. $\square$

### Concrete bar-symmetric polynomials

**Proposition (Lean: `barPoly_c5_denominator`).** $\overline{4 + X^2} = 4 + X^2$.
*Proof.* The bar involution fixes the integer scalar $4$ and the even power $X^2$. It therefore fixes their sum. $\square$

**Proposition (Lean: `barPoly_c5_taylor_6`).** The polynomial $c_5^{[6]}(X) := -\tfrac{5}{4} - \tfrac{X^2}{16} + \tfrac{X^4}{64} - \tfrac{X^6}{256}$ is bar-symmetric.
*Proof.* Every term has the form $c \cdot X^{2k}$ with $c \in \mathbb{R}$. The bar involution fixes constants and even powers, so it fixes the sum. $\square$

**Proposition (Lean: `barPoly_cos_truncated_6`, `barPoly_cosh_truncated_6`).** $\cos^{[6]}(X) := 1 - X^2/2 + X^4/24 - X^6/720$ and $\cosh^{[6]}(X) := 1 + X^2/2 + X^4/24 + X^6/720$ are bar-symmetric.
*Proof.* These polynomials consist of even powers with scalar coefficients. They are bar-symmetric. $\square$

**Theorem (Lean: `three_layer_truncated_all_bar_symmetric`).** All three layer truncations — series $c_5^{[6]}$, phase $\cos^{[6]}$, gain $\cosh^{[6]}$ — are bar-symmetric in the same polynomial ring $\mathbb{R}[X]$ under the same bar-involution $X \mapsto -X$.
*Proof.* This concatenates the three prior propositions. The three layer avatars reside in the same ambient ring with the same bar involution. $\square$

### Pre-archimedean generic versions

**Proposition (Lean: `barPoly_evenPoly_6 c0 c1 c2 c3`).** Over any commutative ring $R$, the polynomial $c_0 + c_1 X^2 + c_2 X^4 + c_3 X^6$ is bar-symmetric for arbitrary coefficients.
*Proof.* The bar involution fixes each constant $c_i$ and each even power $X^{2k}$. The sum is therefore bar-symmetric. $\square$

**Theorem (Lean: `barPoly_even_truncated_arbitrary n c`).** For any $n \in \mathbb{N}$ and any $c : \mathbb{N} \to R$, the polynomial $P_n(X) := \sum_{k=0}^{n-1} c_k X^{2k}$ is bar-symmetric.
*Proof.* We proceed by induction on $n$. The empty sum is zero, which is bar-symmetric. The inductive step adds the bar-symmetric term $c_k X^{2k}$. $\square$

**Theorem (Lean: `barPoly_odd_truncated_arbitrary n c`).** Sums of odd-power monomials with arbitrary $R$-coefficients are bar-anti-symmetric.
*Proof.* The induction proceeds as in the even case, using the bar-anti-symmetry of odd powers. $\square$

### Evaluations

**Proposition (Lean: `c5_taylor_6_eval_zero`).** $c_5^{[6]}(0) = -5/4$.
*Proof.* All positive-degree terms vanish at $X = 0$. $\square$

**Proposition (Lean: `c5_taylor_6_eval_one`).** $c_5^{[6]}(1) = -333/256$.
*Proof.* We evaluate the sum. This approximates the exact value $c_5(1) = -13/10 = -332.8/256$ with relative error $\approx 0.06\%$. $\square$

This completes the polynomial-level work. Every theorem possesses a narrative proof above and a formal Lean proof. Future extensions include rational-function functors realizing the closed form $c_5 = -3/2 + 1/(X^2 + 4)$, and formal power-series limits.
