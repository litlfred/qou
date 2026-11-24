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

What vanishes is the target-flip difference, not the type dependence. Generator $\sigma_1$ operates on strands $1$ and $2$. This is the **control–control crossing**. A target-flip acts on strand $3$, leaving strands $1$ and $2$ unchanged. Parent and daughter therefore carry the **same** $\sigma_1$ crossing type, hence the same $\hat{V}_1$. This forces:

$$
  \Delta_1 = \hat{V}_1^{(\mathrm{par})} - \hat{V}_1^{(\mathrm{dau})} = 0
$$

for every target-flip transition. This occurs because the control crossing is fixed, not because $\hat{V}_1$ is type-independent.

**Target-flip amplitude.**
Since $\Delta_1 = 0$, the $1$-jet formula reduces to:

$$
  P_{\mathrm{flip}} = \hat{V}_1 \cdot \Delta_0
  = z \cdot \bigl(\hat{V}_0^{(\mathrm{par})} -
    \hat{V}_0^{(\mathrm{dau})}\bigr)
$$

The chain at $\sigma_0$ contains two crossings: $(0,1)$ and $(0,2)$. The target flip changes the $(0,2)$ crossing type but leaves the $(0,1)$ crossing unchanged. Chain reduction gives $\hat{V}_0 = z \cdot a_0 + b_0$, where $a_0, b_0$ depend on both crossings. The difference $\Delta_0$ factors. The unchanged $(0,1)$ crossing contributes its coefficient $c_{01}$ as a **prefactor**. The changing $(0,2)$ crossing contributes the same core difference regardless of the $(0,1)$ type.

Therefore $\Delta_0 = c_{01} \cdot \Delta_{02}(q)$, where $c_{01} = 1$ is the crossing coefficient of the control–control pair and $\Delta_{02}$ is the core difference at the changing crossing. However, in $P_{\mathrm{flip}} = \hat{V}_1^{(\mathrm{par})}\,\Delta_0$, the prefactor $\hat{V}_1^{(\mathrm{par})} = z + d_{01}$ varies across the three control pairs $\mathfrak{p}\mathfrak{p}$, mixed, and $\mathfrak{n}\mathfrak{n}$ through $d_{01} \in \{0, -\tfrac{q-q^{-1}}{2}, -(q-q^{-1})\}$, yielding the three distinct values of item 2 rather than a single control-independent amplitude.

**All-proton q-AND and reverse flip.**
For the all-proton control pair $(c_{01}, d_{01}) = (1, 0)$, substituting $z = q^3/(q^2+1)$ gives
$$
  P_{7,6}(q) = -\,\frac{(q-1)(q+1)\bigl(q^{6} + q^{4} + 2q^{2} + 1\bigr)}{2q\,(q^{2}+1)^{2}},
$$
establishing item 3. Evaluating the reverse transition from its own parent input column replaces the sextic factor by $2q^6 + q^4 + q^2 + 1$, giving $P_{6,7}(q) \neq -P_{7,6}(q)$ (item 4).

**Classical limit.**
At $q = 1$, $q - q^{-1} = 0$, so all crossing types coincide and $\Delta_0 = 0$; every target-flip amplitude carries the factor $(q - 1)$ (item 5).

**Toffoli diagonals.**
For the all-proton ordering every crossing has $(c, d) = (1, 0)$, so $\hat{V}_1 = z$ and $\hat{V}_0 = 1 + (q - q^{-1})z$, giving $P_{7,7}(q) = \hat{V}_0\hat{V}_1 = z + (q - q^{-1})z^2$. Substituting $z = q^3/(q^2+1)$ yields $P_{7,7}(q) = q^3(q^4+1)/(q^2+1)^2$, and the analogous product on the even parity sector yields $P_{6,6}(q) = (q^4+1)(q^4+q^2+2)/\bigl(4q(q^2+1)^2\bigr)$, both strictly positive on $(0,\infty)$ (item 6). $\square$
