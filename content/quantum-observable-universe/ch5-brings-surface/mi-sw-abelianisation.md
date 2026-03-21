Let $E_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch
point $z_c$ ([Remark](#rem:brings-smoothness)), and let
$(\nabla_A q,\; L \wedge F^+)$ be the connection--curvature pair of the
mass identity ([Definition](#def:mass-identity)).  Then for each
vertical degree $n \geq 0$ in the Reeb decomposition, the restriction
of the nonabelian multiplicative integral to $E_c$ abelianises to the
$n$-th prolonged Seiberg--Witten period:

```tex
\begin{equation}\label{eq:mi-sw-abelianisation}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_c}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert_{J^n}
  \;=\;
  \bigl\lvert a_D^{(n)}\bigr\rvert
  \;=\;
  \biggl\lvert\oint_{E_c}\lambda_{\mathrm{SW}}^{(n)}\biggr\rvert,
\end{equation}
```

where $\lVert\cdot\rVert_{J^n}$ denotes the Killing-form norm projected
onto the $n$-th jet component, and $\lambda_{\mathrm{SW}}^{(n)}$ is the
$n$-th prolonged Seiberg--Witten differential.

---

The proof proceeds in three steps.

*Step 1: Abelianisation of the connection.*
On the exceptional divisor $E_c \cong \mathbb{P}^1(\mathbb{C})$ the principal
$\mathrm{SU}(2)$-bundle $P$ trivialises (every $\mathrm{SU}(2)$-bundle
over $S^2$ is classified by $\pi_1(\mathrm{SU}(2)) = 0$).  The
connection $\nabla_A$ therefore reduces to a $\mathfrak{su}(2)$-valued
$1$-form $A|_{E_c}$.  By the weight-space decomposition
([Remark](#rem:weight-space-decomposition)), the restriction splits as

$$
  A\big|_{E_c}
  \;=\;
  A^0 \otimes H
  \;+\;
  A^+ \otimes E_+
  \;+\;
  A^- \otimes E_-,
$$

where $H, E_\pm$ are the standard generators of $\mathfrak{su}(2)$.
The Cartan component $A^0$ is a $\mathrm{U}(1)$-valued $1$-form on
$E_c$.  Since $E_c \cong \mathbb{P}^1(\mathbb{C})$ the spectral curve
([Remark](#rem:chiral-bundles)) restricts to a single sheet, and the
Higgs-field eigenvalue is the chiral coordinate $X$.  The abelian
component therefore satisfies $A^0 = X\,dz = \lambda_{\mathrm{SW}}$,
recovering the Seiberg--Witten differential.

*Step 2: Fake-flatness and the $2$-form datum.*
The fake-flatness condition $F_A = B$ identifies
the curvature $2$-form $L \wedge F^+$ on $E_c$ with the
$\mathfrak{su}(2)$-valued $2$-form $B|_{E_c}$.  The simplicity constraint
forces $B|_{E_c} = F_A^+|_{E_c}$, which on the $2$-sphere $E_c$ is
proportional to the volume form $\mathrm{vol}_{E_c}$.  Consequently
the pair $(\nabla_A q,\; L \wedge F^+)$ restricted to $E_c$ is
*abelian*: both components lie in the Cartan subalgebra after
projection onto the weight-$0$ sector, and the nonabelian MI integral
reduces to the ordinary (abelian) multiplicative integral, which equals
the exponential of the classical contour integral.  Taking the norm
yields the absolute value of the period.

*Step 3: Jet prolongation and vertical degree.*
At vertical degree $n = 0$ the Killing-form projection onto $J^0$
recovers the base differential $\lambda_{\mathrm{SW}}^{(0)} = X\,dz$
and the electron period $a_D^{(e)}$.  At vertical degree $n \geq 1$ the
jet prolongation ([Proposition](#prop:jet-prolongation)) lifts the
connection to $J^n E$, replacing $X\,dz$ with the $n$-th prolonged
differential $\lambda_{\mathrm{SW}}^{(n)}$: the $1$-jet component is
$dX$ (the implicit derivative of the color tube
cubic), and higher jets follow by induction.
The MI integral at jet level $n$ is the abelian integral of
$\lambda_{\mathrm{SW}}^{(n)}$ over $E_c$ by the same argument as
Steps 1--2 applied to the prolonged connection $A'$ on $J^n E$.
