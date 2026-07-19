This remark is the $\mathbb{Z}/2\mathbb{Z}$ bar-grading Lean $\leftrightarrow$
paper bridge for the [bar-involution](#def:bar-involution): the bar-grading
subring/module structure and the sorry-free Lean theorems with their
narrative proofs.

Every Lean theorem in [`bar-involution.lean`](bar-involution.lean) has both a narrative proof here and a `sorry`-free formal proof. Theorems split into three sections by structural prerequisite (`CommRing` / `Field`).

**Bar-grading over `CommRing R`**

**Proposition (Lean: `decompose x`).** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition (Lean: `isBarSymmetric_zero`, `isBarSymmetric_one`).** $0$ and $1$ are bar-symmetric.
*Proof.* Direct from `BarInvolution.bar_zero` and `bar_one`. $\square$

**Proposition (Lean: `IsBarSymmetric.add`).** Sum of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition (Lean: `IsBarSymmetric.mul`).** Product of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition (Lean: `IsBarAntiSymmetric.add`).** Sum of bar-anti-symmetric is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem (Lean: `IsBarSymmetric.of_mul_antisym`).** $x, y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. **This is the "anti $\times$ anti = sym" identity that generates the bar-symmetric content from bar-anti-symmetric kernels** (e.g., $h^2$ bar-sym from $h$ bar-anti-sym). $\square$

**Theorem (Lean: `IsBarAntiSymmetric.of_sym_mul`).** $x$ bar-symmetric, $y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition (Lean: `bar_neg x`).** $\overline{-x} = -\overline x$ — bar commutes with negation.
*Proof.* From $x + (-x) = 0$ and bar additive: $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition (Lean: `IsBarSymmetric.neg`, `IsBarAntiSymmetric.neg`).** Negation preserves both grading sectors.
*Proof.* For sym: $\overline{-x} = -\overline x = -x$. For anti-sym: $\overline{-x} = -\overline x = -(-x) = x = -(-x)$. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n}$ bar-symmetric.
*Proof.* Induction on $n$. Base ($n=0$): $x^0 = 1$ bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot (x \cdot x)$; $x^{2k}$ bar-sym by IH, $x \cdot x$ bar-sym by `of_mul_antisym`; product bar-sym by `IsBarSymmetric.mul`. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul_add_one`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n+1}$ bar-anti-symmetric.
*Proof.* $x^{2n+1} = x^{2n} \cdot x$; $x^{2n}$ bar-sym (above), $x$ bar-anti-sym (hypothesis); product bar-anti-sym by `of_sym_mul`. $\square$
