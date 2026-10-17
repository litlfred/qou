---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-010-42-variable-reduction
section_title: "Variable reduction"
section_number: 4.2
pages: 17-20
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.948
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
[]{#sec.reduction label="sec.reduction"}

In this subsection, we reduce the number of shape parameters by solving the gluing equations for the C and R-edges, and the completeness equation. The following lemma will be used repeatedly.

::: lemma
[]{#lem.red label="lem.red"} Let $f_1,\ldots,f_k$ be functions in variables $x_1,\ldots,x_k$ and fix a solution to $$\exp(f_1) = \cdots = \exp(f_k)=1\,.$$ Suppose that $\exp(f_k)$ is of the form $g(x_1,\ldots,x_{k-1}) \, x_k$ so that we can substitute $x_k$ with $1/g(x_1,\ldots,x_{k-1})$ by solving $\exp (f_k)=1$. Then we have $$\label{eqn.xx}
  \det \left ( \dfrac{\partial (f_1,\ldots,f_k)}{\partial(x_1,\ldots,x_k)} \right)
  = \dfrac{1}{x_k}
\det \left ( \dfrac{\partial (f'_1,\ldots,f'_{k-1})}{\partial(x_1,\ldots,x_{k-1})} \right)$$ where $f'_i$ is obtained from $f_i$ by substituting $x_k$ with $1/g(x_1,\ldots,x_{k-1})$.
:::

::: proof
*Proof.* It follows from $\exp(f_k) = g(x_1,\ldots,x_{k-1}) \, x_k$ that the $(k,j)$-entry of the Jacobian matrix $\partial (f_1,\ldots,f_k)/\partial(x_1,\ldots,x_k)$ is $1/x_k$ for $j=k$, and $g^{-1} \,\partial g / \partial x_j$ for $1 \leq j < k$. Keeping the last row, we make the $i$-row for $i \neq k$ have the last entry 0 by employing elementary row operations. Then the $(i,j)$-entry becomes $$\begin{aligned}
  \frac{\partial f_i}{\partial x_j}- \frac{x_k}{g} \frac{\partial g}{\partial x_j}
  \frac{\partial f_{i}}{\partial x_k} & = \frac{\partial f_i}{\partial x_j}
  - \frac{1}{g^2} \frac{\partial g}{\partial x_j} \frac{\partial f_{i}}{\partial x_k} \\
  &=\frac{\partial f_i}{\partial x_j} + \frac{\partial g^{-1}}{\partial x_j}
  \frac{\partial f_{i}}{\partial x_k} \\
  &=\frac{\partial f_i}{\partial x_j} + \frac{\partial x_k}{\partial x_j}
  \frac{\partial f_{i}}{\partial x_k}\,.
\end{aligned}$$ As the last term is equal to $\partial f'_i/\partial x_j$, we deduce Equation [\[eqn.xx\]](#eqn.xx){reference-type="eqref" reference="eqn.xx"}. ◻
:::

Recall that the gluing equation of an edge $e_i$ of $\mathcal T_{\mathring{D}}$ is of the form $$\sum_{j=1}^N  G_{ij} \log z_j + G'_{ij} \log z'_j
+ G''_{ij} \log z''_j  =2 \pi i \, .$$ We denote by $g_i$ the left-hand side so that $\exp(g_i)=1$. By rearranging the index of edges, we may assume that the first $n+1$ equations $g_1,\ldots, g_{n+1}$ are for O and U-edges and the rest, say $g_{n+2},\ldots, g_N$, are for C and R-edges. By replacing the $(n+1)$-st equation $g_{n+1}$ with $g_\mu$, the logarithm form of the completeness equation of a meridian, the 1-loop invariant is given by (see Remark [\[rmk.der\]](#rmk.der){reference-type="ref" reference="rmk.der"}) $$\label{eqn.t1}
\tau(\mathcal T_{\mathring{D}}) = \pm \frac{1}{2{\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g}}
\det \left(\dfrac{\partial (g_1,\ldots, g_{n}, g_\mu,g_{n+2},\ldots,g_N)}
{\partial (z_1,\ldots,z_N)} \right)$$ where $\boldsymbol f + \boldsymbol g$ is the flattening of $\mathcal T_{\mathring{D}}$ chosen in Section [\[sec.flat\]](#sec.flat){reference-type="ref" reference="sec.flat"}.

In what follows, we solve all C and R-edge equations $g_{n+2},\ldots,g_{N}$ as well as the completeness equation $g_\mu$. This eliminates $N-n$ shape parameters, and we may assume that those are $z_{n+1},\ldots, z_{N}$ by rearranging the index of shape parameters.

-   Recall that a C-edge corresponds to a crossing of $\mathring{D}$. Given that $\mathring{D}$ is given as in Figure [\[fig.planardiagram\]](#fig.planardiagram){reference-type="ref" reference="fig.planardiagram"}, one of E and W-corners at the crossing is non-essential, and thus the gluing equation of the C-edge is either $$z_{N} z_{E} z_{S}  = 1 \quad \textrm{or} \quad z_{N} z_{W} z_{S} =1 \, .$$ where $z_X$ means the shape parameter at the X-corner. Employing Lemma [\[lem.red\]](#lem.red){reference-type="ref" reference="lem.red"}, we eliminate the shape parameter $z_S$ of the S-corner.

-   Similarly, an R-edge corresponds to a region of $\mathring{D}$, and its gluing equation is of the form $z_{i_1} \cdots  z_{i_k}  = 1$ where the S-corner of the topmost crossing and the N-corner of the bottommost crossing contribute one shape parameter. Using Lemma [\[lem.red\]](#lem.red){reference-type="ref" reference="lem.red"}, we eliminate the shape parameter at the N-corner of the bottommost crossing.

-   Lastly, the completeness equation for a meridian is given as $z_{i_1}^{\pm1} z_{i_2}=1$ where $z_{i_1}$ and $z_{i_2}$ are shape parameters placed at corners shown as in Figure [1](#fig.meridian){reference-type="ref" reference="fig.meridian"}. We eliminate the shape parameter $z_{i_2}$ by employing Lemma [\[lem.red\]](#lem.red){reference-type="ref" reference="lem.red"}.

    <figure id="fig.meridian">

    <figcaption>A completeness equation for a meridian.</figcaption>
    </figure>

As mentioned earlier, the above variable reduction eliminates $N-n$ shape parameters $z_{n+1},\ldots,z_N$, and Lemma [\[lem.red\]](#lem.red){reference-type="ref" reference="lem.red"} implies that $$\label{eqn.t2}
\det \left(\dfrac{\partial (g_1,\ldots, g_{n}, g_\mu,g_{n+2},\ldots,g_N)}
  {\partial (z_1,\ldots,z_N)} \right)  = \frac{1}{z_{n+1} \cdots z_N} \det
\left(\dfrac{\partial (g'_1,\ldots, g'_{n})}{\partial (z_1,\ldots,z_{n})} \right)$$ where $g'_i$ is obtained from $g_i$ by eliminating the $N-n$ shape parameters $z_{n+1},\ldots,z_N$. A simple calculation shows that the number $n$ of the remaining variables is equal to the number of variables that are assigned to the open diagram $\mathring{D}$. Namely, the matrix in the right-hand side of Equation [\[eqn.t2\]](#eqn.t2){reference-type="eqref" reference="eqn.t2"} has the same size as the matrix in [\[eqn.OT\]](#eqn.OT){reference-type="eqref" reference="eqn.OT"}.

::: lemma
[]{#lem.cc label="lem.cc"} We have $$\det \left ( x_i \dfrac{\partial}{\partial x_i} \left(x_j\, \dfrac{\partial V}{
\partial x_j} \right)\right)_{1 \leq i,j \leq n} = \pm z_1 \ldots z_{n} \det
\left(\dfrac{\partial (g'_1,\ldots, g'_{n})}{\partial (z_1,\ldots,z_{n})} \right)$$ where $V$ is the potential function of $\mathring{D}$.
:::

::: proof
*Proof.* It is proved in [@MY2018 Theorem 4.1] that the system of equations $x_i \partial V / \partial x_i$ is equivalent to the system of equations $g'_i$. Hence we have $$\begin{aligned}
\det \left (\dfrac{\partial}{\partial x_i} \left(x_j\,
\dfrac{\partial V}{ \partial x_j} \right)\right) &= \pm \det
\left(\dfrac{\partial (g'_1,\ldots, g'_{n})}{\partial (z_1,\ldots,z_{n})} \right)
\det \left(\dfrac{\partial (z_1,\ldots, z_{n})}{\partial (x_1,\ldots,x_{n})} \right) \,.
\end{aligned}$$ If we label the indices of $z_i$ and $x_i$ from the top of the diagram $\mathring{D}$ to the bottom, we have $z_1 =x_1$ and $z_i = x_{i}/x_{i-1}$ or $x_{i-1}/x_{i}$ for $i \geq 2$. A simple induction argument shows that $$\det \left(\dfrac{\partial (z_1,\ldots, z_{n})}{\partial (x_1,\ldots,x_{n})} \right)
= \pm  \frac{z_1 \cdots z_n}{x_1 \cdots x_n} \,.$$ Combining the above two equations, we conclude the lemma. ◻
:::

::: lemma
We have []{#lem.ccc label="lem.ccc"} $$\Omega_1 \Omega_2 =
  \pm \frac{\zeta_1 \cdots \zeta_N}{{\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g}}$$ where $\Omega_1$ and $\Omega_2$ are the normalizing functions of $\mathring{D}$.
:::

::: proof
*Proof.* Recall that the second normalizing function $\Omega_2$ depends on a choice of the orientation of $\mathring{D}$. If we reverse the orientation of $\mathring{D}$, the contribution of the left (resp., right) crossing in Figure [\[fig.omega2\]](#fig.omega2){reference-type="ref" reference="fig.omega2"} to $\Omega_2$ becomes $(y/y')^2$ (resp., $(x/x')^2$). Considering both orientations of $\mathring{D}$, one can define $\Omega_2$ without an orientation choice: $\Omega_2$ is defined as the product of $x'y/xy'$ for the first crossing in Figure [\[fig.omega1\]](#fig.omega1){reference-type="ref" reference="fig.omega1"} and $xy'/x'y$ for the second crossing. It follows that $\Omega_1 \Omega_2$ is given by the product of $(\frac{x'}{x}-1)$ and $(\frac{y}{y'}-1)$ for the first crossing, and $(\frac{x}{x'}-1)$ and $(\frac{y'}{y}-1)$ for the second crossing. From Figure [\[fig.octahedronatd\]](#fig.octahedronatd){reference-type="ref" reference="fig.octahedronatd"} we easily computes that this product is equal to $1/{\boldsymbol \zeta}^{\boldsymbol f}$. This proves that $\Omega_1 \Omega_2
=1/{\boldsymbol \zeta}^{\boldsymbol f}$.

On the other hand, a product of any three zetas around one crossing is 1. Given that $\mathring{D}$ is given as in Figure [\[fig.planardiagram\]](#fig.planardiagram){reference-type="ref" reference="fig.planardiagram"}, we have $$\zeta_1 \cdots \zeta_N = \zeta_1 \zeta_N = \frac{1}{z_1 z_N}$$ where $z_1$ and $z_N$ are the shape parameters that appear first from the top and bottom, respectively, of the diagram. From Remark [\[rmk.ratio\]](#rmk.ratio){reference-type="ref" reference="rmk.ratio"}, we deduce that $z_1 z_N$ is equal ${\boldsymbol \zeta}^{\boldsymbol g}$. This completes the proof. ◻
:::

::: remark
We expect that a similar lemma to the one above holds for all essential diagrams obtained from braid closures of knots; see Appendix [\[sec.appb\]](#sec.appb){reference-type="ref" reference="sec.appb"}.
:::

::: proof
*Proof of Theorem [\[thm.main2\]](#thm.main2){reference-type="ref" reference="thm.main2"}.* Combining Equations [\[eqn.t1\]](#eqn.t1){reference-type="eqref" reference="eqn.t1"} and [\[eqn.t2\]](#eqn.t2){reference-type="eqref" reference="eqn.t2"} together with Lemmas  [\[lem.cc\]](#lem.cc){reference-type="ref" reference="lem.cc"} and [\[lem.ccc\]](#lem.ccc){reference-type="ref" reference="lem.ccc"}, we obtain $$\begin{aligned}
\tau(\mathcal T_{\mathring{D}}) &= \pm \frac{1}{2{\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g}}
\det \left(\dfrac{\partial (g_1,\ldots, g_{n}, g_\mu,g_{n+2},\ldots,g_N)}
{\partial (z_1,\ldots,z_N)} \right) \\
&= \pm \frac{\zeta_{n+1} \cdots \zeta_N}{2{\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g}}
\det \left(\dfrac{\partial (g'_1,\ldots, g'_{n})}{\partial (z_1,\ldots,z_{n})} \right) \\
&=\pm \frac{\zeta_1 \cdots \zeta_N}{2{\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g}}
\det \left ( x_i \dfrac{\partial}{\partial x_i} \left(x_j\, \dfrac{\partial V}{
\partial x_j} \right)\right)  \\
&=\pm \frac{\Omega_1 \Omega_2}{2}   \det \left ( x_i \dfrac{\partial}{\partial x_i}
\left(x_j\, \dfrac{\partial V}{ \partial x_j} \right)\right) = \omega(\mathring{D})\,,
\end{aligned}$$ which concludes the proof of Theorem [\[thm.main2\]](#thm.main2){reference-type="ref" reference="thm.main2"}. ◻
:::
