*Proof.*
On $3$ strands, the chain reduction ([transfer matrix product](#prop:skein-polynomial-transfer-matrix)) produces two generators $\sigma_0, \sigma_1$ with traced volumes $\hat{V}_0(q), \hat{V}_1(q)$.

**Single-crossing type-blindness (key lemma).**
Generator $\sigma_1$ contains one crossing (strand $1$ with strand $2$). The traced volume is $\hat{V}_1 = z \cdot c + d$, where $(c, d)$ depends on the crossing type. Direct computation yields:

$$
  \hat{V}_1^{(\mathrm{pp})} = z \cdot 1 + 0 = z
$$

$$
  \hat{V}_1^{(\mathrm{mix})}
  = z \cdot 1 - \tfrac{q - q^{-1}}{2}
  = z - \tfrac{q - q^{-1}}{2}
$$

$$
  \hat{V}_1^{(\mathrm{nn})}
  = z \cdot 1 - (q - q^{-1})
  = z - (q - q^{-1})
$$

These three values are **not** equal. They differ in the $d$ coefficient. A single crossing therefore carries type information: $\hat{V}_1^{(\mathrm{mix})} - \hat{V}_1^{(\mathrm{pp})} = -\tfrac{q - q^{-1}}{2}$ and $\hat{V}_1^{(\mathrm{nn})} - \hat{V}_1^{(\mathrm{pp})} = -(q - q^{-1})$. 

What vanishes is the target-flip difference rather than the type dependence. Generator $\sigma_1$ operates on strands $1$ and $2$. This is the **control–control crossing**. A target-flip acts on strand $3$, leaving strands $1$ and $2$ unchanged. Parent and daughter therefore carry the **same** $\sigma_1$ crossing type, hence the same $\hat{V}_1$. This forces:

$$
  \Delta_1 = \hat{V}_1^{(\mathrm{par})} - \hat{V}_1^{(\mathrm{dau})} = 0
$$

for every target-flip transition. This occurs because the control crossing is fixed rather than because $\hat{V}_1$ is type-independent.

**Target-flip amplitude.**
Since $\Delta_1 = 0$, the $1$-jet formula reduces to:

$$
  P_{\mathrm{flip}} = \hat{V}_1 \cdot \Delta_0
  = z \cdot \bigl(\hat{V}_0^{(\mathrm{par})} -
    \hat{V}_0^{(\mathrm{dau})}\bigr)
$$

The chain at $\sigma_0$ contains two crossings: $(0,1)$ and $(0,2)$. The target flip changes the $(0,2)$ crossing type but leaves the $(0,1)$ crossing unchanged. Chain reduction gives $\hat{V}_0 = z \cdot a_0 + b_0$, where $a_0, b_0$ depend on both crossings. The difference $\Delta_0$ factors. The unchanged $(0,1)$ crossing contributes its coefficient $c_{01}$ as a **prefactor**. The changing $(0,2)$ crossing contributes the same core difference regardless of the $(0,1)$ type.

Therefore $P_{\mathrm{flip}} = c_{01} \cdot \Delta_{02}(q)$, where $c_{01}$ is the crossing coefficient of the control–control pair and $\Delta_{02}$ is the core difference at the changing crossing. Under the canonical convention $z_D = q^3/(q^2+1)$, the resulting flip amplitude evaluates to $P_{7,6}(q) = -(q-1)(q+1)(q^6+q^4+2q^2+1)/\bigl(2q(q^2+1)^2\bigr)$ (distinct from the closed form $\Phi(q)$, which does not lie in the image of the Toffoli construction under any indexing or convention). The factorisation into a prefactor from the unchanged crossing times a common core from the changing crossing holds independently of the trace normalization.

**The $S_3$ orbit.**
The three choices of target strand in the ordering $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}]$ give:

| Target | Control pair | $c$ | Amplitude |
|:------:|:----------:|:---:|:---------:|
| strand $2$ | $\mathfrak{p}\mathfrak{p}$ | $1$ | $\Phi$ |
| strand $1$ | $\mathfrak{p}\mathfrak{n}$ | $1$ | $\Phi$ |
| strand $0$ | $\mathfrak{p}\mathfrak{n}$ | $1$ | $\Phi$ |

The Toffoli selects the governor: the target with $c = 1$ (unit weight). In the $(1, -(q - q^{-1}))$ convention, all crossing types share $c = 1$. The distinction moves to the $d$ coefficient.

**Antisymmetry.**
The reverse transition swaps parent and daughter, negating $\Delta_0$. Hence, $P_{6,7} = -P_{7,6}$.

**Classical limit.**
At $q = 1$, $q - q^{-1} = 0$. All crossing types coincide, giving $\Delta_0 = 0$. The factor $(q - 1)$ in $\Phi$ confirms this.

**Golden ratio zero of $P_{7,7}$.**
The numerator $q + q^{1/2} - 1$ vanishes when $q^{1/2} = (\sqrt{5} - 1)/2 = 1/\varphi$. This gives $q = 1/\varphi^2 = (3 - \sqrt{5})/2$. $\square$
