*Proof.* By definition $\overline p := p.\mathrm{comp}(-X)$; applying to $p = X$ gives $X.\mathrm{comp}(-X) = -X$ (Mathlib `X_comp`). $\square$

**Proposition.** $\overline{-X} = X$.
*Proof.* $(-X).\mathrm{comp}(-X) = -(X.\mathrm{comp}(-X)) = -(-X) = X$ via `neg_comp`, `X_comp`, `neg_neg`. $\square$

**Proposition.** $\overline{C c} = C c$.
*Proof.* Constants are bar-fixed: $(C c).\mathrm{comp}(-X) = C c$ (Mathlib `C_comp`). $\square$

**Proposition.** $\overline{p+q} = \overline p + \overline q$.
*Proof.* Direct from `Polynomial.add_comp`. $\square$

**Proposition.** $\overline{p \cdot q} = \overline p \cdot \overline q$.
*Proof.* Direct from `Polynomial.mul_comp`. $\square$

**Proposition.** $\overline 1 = 1$ and $\overline 0 = 0$.
*Proof.* Direct from `one_comp`, `zero_comp`. $\square$

**Proposition.** $\overline{\overline p} = p$.
*Proof.* $(p.\mathrm{comp}(-X)).\mathrm{comp}(-X) = p.\mathrm{comp}((-X).\mathrm{comp}(-X)) = p.\mathrm{comp}(X) = p$ via `comp_assoc`, `barPoly_neg_X`, and `comp_X`. $\square$

### Power identities

**Proposition.** $\overline{X^2} = X^2$.
*Proof.* $X^2 = X \cdot X$, so $\overline{X^2} = \overline X \cdot \overline X = (-X)(-X) = X^2$. $\square$

**Proposition.** $\overline{X^n} = (-1)^n \cdot X^n$.
*Proof.* Induction on $n$. Base ($n=0$): $\overline 1 = 1$. Step: $\overline{X^{k+1}} = \overline{X \cdot X^k} = (-X) \cdot (-1)^k X^k = (-1)^{k+1} X^{k+1}$. $\square$

**Proposition.** $\overline{X^{2n}} = X^{2n}$.
*Proof.* From `barPoly_X_pow`: coefficient is $(-1)^{2n} = ((-1)^2)^n = 1$. $\square$

**Proposition.** $\overline{X^{2n+1}} = -X^{2n+1}$.
*Proof.* From `barPoly_X_pow`: coefficient is $(-1)^{2n+1} = -1$. $\square$

### Scalar identities

**Proposition.** Every natural-number scalar is bar-fixed in $R[X]$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition.** $\overline{p - q} = \overline p - \overline q$.
*Proof.* $p - q = p + (-1) \cdot q$; bar commutes with $+$ and $\cdot$, and $\overline{-1} = -1$ (from `neg_comp` + `one_comp`). $\square$

**Proposition.** $\overline{-p} = -\overline p$.
*Proof.* Take $p = 0$ in `barPoly_sub`: $\overline{-q} = \overline{0 - q} = 0 - \overline q = -\overline q$. $\square$

### Concrete bar-symmetric polynomials

**Proposition.** $\overline{4 + X^2} = 4 + X^2$.
*Proof.* $\overline 4 = 4$ by `barPoly_natCast` (with $4 = (4:\mathbb{N})$); $\overline{X^2} = X^2$ by `barPoly_X_pow_two`; combine with `barPoly_add`. $\square$

**Proposition.** The polynomial $c_5^{[6]}(X) := -\tfrac{5}{4} - \tfrac{X^2}{16} + \tfrac{X^4}{64} - \tfrac{X^6}{256}$ is bar-symmetric.
*Proof.* Every term has the form $C(c) \cdot X^{2k}$ with $c \in \mathbb{R}$ and $k \in \{0,1,2,3\}$. Constants fixed by `barPoly_C`; even powers fixed by `barPoly_X_pow_even`. Sum and difference of bar-symmetric is bar-symmetric. $\square$

**Proposition.** $\cos^{[6]}(X) := 1 - X^2/2 + X^4/24 - X^6/720$ and $\cosh^{[6]}(X) := 1 + X^2/2 + X^4/24 + X^6/720$ are bar-symmetric.
*Proof.* Same structure as `c5_taylor_6`: each term $C(c) \cdot X^{2k}$ with bar-fixed coefficient and bar-fixed even power. $\square$

**Theorem.** All three layer truncations — series $c_5^{[6]}$, phase $\cos^{[6]}$, gain $\cosh^{[6]}$ — are bar-symmetric in the **same** polynomial ring $\mathbb{R}[X]$ under the **same** bar-involution $X \mapsto -X$.
*Proof.* Conjunction of the three propositions above. The three layer avatars live in the same ambient ring with the same bar — this is the **categorical-derivation unification at the truncated-polynomial level**. $\square$

### Pre-archimedean generic versions

**Proposition.** Over any commutative ring $R$ (no field needed), the polynomial $c_0 + c_1 X^2 + c_2 X^4 + c_3 X^6$ is bar-symmetric for arbitrary $c_0, c_1, c_2, c_3 \in R$.
*Proof.* Per-term: $C(c_i)$ bar-fixed by `barPoly_C`; $X^{2k}$ bar-fixed by `barPoly_X_pow_even`. Sum bar-symmetric by `barPoly_add`. **No archimedean structure invoked.** $\square$

**Theorem.** For any $n \in \mathbb{N}$ and any $c : \mathbb{N} \to R$, the polynomial $P_n(X) := \sum_{k=0}^{n-1} c_k X^{2k}$ is bar-symmetric.
*Proof.* Induction on $n$. Base: empty sum $= 0$ bar-symmetric. Step: $P_{k+1} = P_k + C(c_k) X^{2k}$; IH gives $P_k$ bar-symmetric, per-term argument gives $C(c_k) X^{2k}$ bar-symmetric; sum bar-symmetric. **Holds for arbitrary truncation degree over any CommRing.** $\square$

**Theorem.** Sums of odd-power monomials with arbitrary $R$-coefficients are bar-anti-symmetric.
*Proof.* Induction analogous to even case, using `barPoly_X_pow_odd` to flip sign on each term. $\square$

### Evaluations

**Proposition.** $c_5^{[6]}(0) = -5/4$.
*Proof.* All positive-degree terms vanish at $X = 0$; constant term is $-5/4$. By `Polynomial.eval_*` lemmas. $\square$

**Proposition.** $c_5^{[6]}(1) = -333/256$.
*Proof.* $-5/4 - 1/16 + 1/64 - 1/256 = -320/256 - 16/256 + 4/256 - 1/256 = -333/256$ by `norm_num`. Approximates exact $c_5(1) = -13/10 = -332.8/256$ with relative error $\approx 0.06\%$ (consistent with $O(X^8 / 4^4)$ Taylor truncation at $X = 1$). $\square$

Polynomial-level work is **complete** — every theorem here has a narrative proof above and a `sorry`-free Lean proof in the sibling. Future extensions: `RatFunc R` for rational-function functors realising the proved $c_5 = -3/2 + 1/(X^2 + 4)$ closed form, and `PowerSeries R` for the formal power-series limit of the truncated avatars.
