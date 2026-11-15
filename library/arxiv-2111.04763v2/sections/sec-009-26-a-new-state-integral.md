---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-009-26-a-new-state-integral
section_title: "A new state-integral"
section_number: 2.6
pages: 19-23
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.96
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.AK41new label="sub.AK41new"}

In the previous section, we saw how the matrix $W^\mathrm{red}(\tau)$ of products of $q$-series and $\tilde{q}$-series [\[Gm01\]](#Gm01){reference-type="eqref" reference="Gm01"} coincides with a matrix of state-integrals. Having found the $q$-series [\[G2\]](#G2){reference-type="eqref" reference="G2"} which complement the series [\[Gm01\]](#Gm01){reference-type="eqref" reference="Gm01"}, it is natural to search for a new state-integral which factorises in terms of all three $q$-series $G_{m}^{(j)}(q)$ for $j=0,1,2$ and their $\tilde{q}$-versions. Upon looking carefully, the series $G_{m}^{(j)}(q)$ for $j=0,1$ were produced from the Andersen--Kashaev state-integral because its integrand had a double pole, hence the contributions came from expanding [\[G41epsilon\]](#G41epsilon){reference-type="eqref" reference="G41epsilon"} up to $O(\varepsilon^2)$. If we expanded up to $O(\varepsilon^3)$, we would capture the new series $G^{(2)}(q)$. Hence the problem is to find a state-integral of the $\mathbf{4}_1$ whose integrand has poles of order $3$. After doing so, one needs to understand how this story, which seems a bit ad hoc and coincidental to the $\mathbf{4}_1$ knot, can generalise to all knots. It turns out that such a state-integral existed in the literature for many years, and in fact was devised by Kashaev [@kas-volume] as a method to convert the state-sums of the Kashaev invariants into state-integrals, using as a building block the Faddeev quantum dilogarithm function at rational numbers, multiplied by $1/\sinh x$. Incidentally, similar integrals have appeared in [@kas-mar] and more recently in the work of two of the authors on the topological string on local $\mathbbm P^2$; see [@GM:top-sting Eqn.3.141]. The integrand of such state-integrals are meromorphic functions with the usual pole structure coming from the Faddeev quantum dilogarithm function, together with the extra poles coming from $1/\sinh x$. The residues of the former give rise to products of $q$-series times $\tilde{q}$-series, but the presence of of $1/\sinh x$ has two effects. On the one hand, it produces, in an asymmetric fashion, poles of the integrand of one order higher, contributing to sums of $q$-series or $\tilde{q}$-series. On the other hand, the produced $q$ and $\tilde{q}$-series look like multidimensional Appell-Lerch sums. An original motivation for converting state-sum formulas for the Kashaev invariants into state-integral formulas was to use such an integral expression for a proof of the Volume Conjecture.

<figure id="contours-fig">
<div class="center">
<img src="contours" style="height:5cm" />
</div>
<figcaption>The contour <span class="math inline">𝒜<sub><em>N</em></sub></span> appears in the integral formula <a href="#car" data-reference-type="eqref" data-reference="car">[car]</a> for the Kashaev invariant of the <span class="math inline"><strong>4</strong><sub>1</sub></span> knot, and it encircles the <span class="math inline"><em>N</em></span> poles <a href="#jones-poles" data-reference-type="eqref" data-reference="jones-poles">[jones-poles]</a>. By doing the integral along the contour <span class="math inline">𝒞</span> and picking the poles in the lower half plane, one obtains a new state-integral with information about the trivial connection.</figcaption>
</figure>

There are two examples that convert state-sums into state-integrals, one given by Kashaev in [@kas-volume] for the $\mathbf{4}_1$ knot and further studied by Andersen--Hansen [@AH], and one in Kashaev--Yokota [@KY:52] for the $\mathbf{5}_2$ knot. In the case of the $\mathbf{4}_1$ knot, the integral considered in [@kas-volume; @AH] is

$$\label{car}
\langle \mathbf{4}_1 \rangle_N

=-{{\rm i}\over 2 {\mathsf{b}}^3} \int_{{\mathcal A}_N}
\tanh\left( {\pi y \over {\mathsf{b}}} \right) {\operatorname{\Phi}_{\mathsf{b}}\left( -y +{{\rm i}\over 2 {\mathsf{b}}} \right)
  \over \operatorname{\Phi}_{\mathsf{b}}\left(y -{{\rm i}\over 2 {\mathsf{b}}} \right)} {\rm d}y.$$

For generic $\mathsf{b}^2\in\mathbb{C}'$ so that $\mathop{\mathrm{Re}}\mathsf{b}>0$, the integrand has the following poles and zeros, all in the imaginary axis:

$$\begin{aligned}
  &\text{simple poles}: \left\{{\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)
    \,\big|\,    m=0,1,2,\ldots\right\},\\
  &\text{double poles}: \left\{
    -{\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)-{\rm i}\mathsf{b}^{-1}(1+n)
    \,\big|\, m,n=0,1,2,\ldots \right\},  \\
  &\text{triple poles}: \left\{-{\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)
    \,\big|\, m=0,1,2,\ldots \right\},\\
  &\text{double zeros}: \left\{ {\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)
    +{\rm i}\mathsf{b}^{-1}(1+n)\,\big|\,m,n=0,1,2,\ldots\right\} \,.
\end{aligned}$$ In the special case where ${\mathsf{b}}^2=N^{-1}$ where $N \in \mathbbm Z_{>0}$, which is the case where [\[car\]](#car){reference-type="eqref" reference="car"} is well-defined, the poles and zeros in the upper half plane conspire so that there are only finite many simple poles located at

$$\label{jones-poles}
y_m={\rm i}{\mathsf{b}}\left(m+{1\over 2} \right), \qquad m=0, \cdots, N-1,$$

and we can define the contour ${\mathcal A}_N$ encircling these points as in Fig. [1](#contours-fig){reference-type="ref" reference="contours-fig"} (left). An application of the residue theorem gives that this integral calculates the Kashaev invariant of the $\mathbf{4}_1$ knot,

$$\label{kas-ex}
\langle \mathbf{4}_1 \rangle_N=\sum_{m=0}^{N-1} (-1)^m \xi^{-m(m+1)/2}
\prod_{\ell=1}^m (1- \xi^\ell)^2, \qquad \xi = {\rm e}^{2\pi {\rm i}\over N}.$$

Now, we can define a new analytic function by changing the contour of integration from $\mathcal A_N$ to the horizontal contour $\mathcal C$ slightly below the horizontal line $\mathop{\mathrm{Im}}(y) = \mathop{\mathrm{Re}}(\mathsf{b}^{-1})/2$,

$$\label{itau-def}
{ \mathcal{Z}}(\tau)= -\frac{{\rm i}}{2\mathsf{b}^3}\int_{\mathcal C} 
\tanh\left( {\pi y \over {\mathsf{b}}} \right) {\operatorname{\Phi}_{\mathsf{b}}\left( -y +{{\rm i}\over 2 {\mathsf{b}}} \right)
  \over \operatorname{\Phi}_{\mathsf{b}}\left(y -{{\rm i}\over 2 {\mathsf{b}}} \right)} {\rm d}y.$$

This is now defined for $\tau= {\mathsf{b}}^2 \in \mathbbm C'$. Although both [\[car\]](#car){reference-type="eqref" reference="car"} and [\[itau-def\]](#itau-def){reference-type="eqref" reference="itau-def"} share the same integrand, it has significant contributions from infinity in the upper half plane, so that we cannot deform the contour $\mathcal{A}_N$ smoothly to the contour $\mathcal{C}$, and [\[car\]](#car){reference-type="eqref" reference="car"} and [\[itau-def\]](#itau-def){reference-type="eqref" reference="itau-def"} are really different. On the other hand, the integrand does have vanishing contributions from infinity in the lower half plane. Consequently we can smoothly deform the new controur $\mathcal{C}$ downwards, and collect the residues of the integrand on the lower half-plane, as shown in Fig. [1](#contours-fig){reference-type="ref" reference="contours-fig"} (right). This integral, in contrast to the Andersen--Kashaev state-integral, contains information about the trivial connection. In particular, we conjecture that, in the region of the complex plane slightly above the positive real axis, the all-orders asymptotic of $\mathcal{Z}(\tau)$ at $\tau=0$ is given by

$${ \mathcal{Z}}(\tau)\sim \Phi^{(\sigma_0)}(\tau).$$

Moreover, this can be upgraded to an exact asymptotic formula by using Borel resummation in the same region, and one has

$$\label{itau-borel}
{ \mathcal{Z}}(\tau)=  s( \Phi^{(\sigma_0)} )(\tau)
-{{\rm i}\over 2}\tau^{-3/2}  s(\Phi^{(\sigma_2)} )(\tau) .$$

It turns out that the change of contour in Fig. [1](#contours-fig){reference-type="ref" reference="contours-fig"} implements the inversion of the Habiro series recently studied in [@park-inverted]: the integral over the contour ${\mathcal A}_N$ leads to the Habiro series, while the integral over $\mathcal{C}$ gives the "inverted" Habiro series, see also Section [\[sub.41statex\]](#sub.41statex){reference-type="ref" reference="sub.41statex"}. This inversion between $q$-series and elements of the Habiro ring was observed 10 years ago by the first author in his joint work with Zagier [@GZ:qseries], under the informal name "upside-down cake".

## A $3 \times 3$ matrix of state-integrals {#sub.3x3state}

Having found a new state-integral whose asymptotics sees the asymptotic series $\Phi^{(\sigma_0)}(\tau)$, we now consider its descendants, and their factorisations to complete the story. The new state-integrals $\mathcal{Z}_{\lambda,\mu}(\tau)$ are defined as follows:

$$\label{inst-def}
{\mathcal{Z}}_{\lambda, \mu}(\tau) = -\frac{{\rm i}}{2\mathsf{b}^3}\int_{\mathcal C}
\tanh\left( {\pi y \over {\mathsf{b}}} \right)
{\operatorname{\Phi}_{\mathsf{b}}\left( -y +{{\rm i}\over 2 {\mathsf{b}}} \right) \over \operatorname{\Phi}_{\mathsf{b}}
  \left(y -{{\rm i}\over 2 {\mathsf{b}}} \right)} {\rm e}^{-2 \pi (\lambda {\mathsf{b}}- \mu {\mathsf{b}}^{-1})} {\rm d}y,$$

where ${\mathsf{b}}$ is related to $\tau$ by $\tau= {\mathsf{b}}^2$ and $\lambda,\mu\in \mathbbm Z$. The integration contour ${\mathcal C}$ is chosen so that, at infinity, it is asymptotic to the line ${\rm Im}(y)=y_2$, where $y_2$ satisfies

$$y_2 < \tfrac{1}{2}\mathop{\mathrm{Re}}\mathsf{b}^{-1} - |\mathop{\mathrm{Re}}(\lambda\mathsf{b}-\mu\mathsf{b}^{-1})|.$$

This guarantees convergence of the integral. We choose $\mathcal C$ so that all poles of the integrand in the lower half plane are below $\mathcal C$. Note that $\mathcal{Z}_{0,0}(\tau)=\mathcal{Z}(\tau)$ is the integral introduced in [\[itau-def\]](#itau-def){reference-type="eqref" reference="itau-def"}, so that the state-integrals with general $\lambda,\mu$ are descendants of $\mathcal{Z}(\tau)$.

::: theorem
[]{#thm-newst label="thm-newst"} The descendant state-integral [\[inst-def\]](#inst-def){reference-type="eqref" reference="inst-def"} can be expressed in terms of the series ([\[Gm01\]](#Gm01){reference-type="ref" reference="Gm01"}), ([\[Gm2\]](#Gm2){reference-type="ref" reference="Gm2"}) as follows:

$$\label{Zlmfac}
  \begin{aligned}
    {\mathcal{Z}}_{\lambda, \mu}(\tau) &= q^{\lambda/2} (-1)^{\mu}
    \left(  G_\lambda^{(2)}(q)+\tau^{-1}
      G_\lambda^{(1)}(q) L_\mu^{(0)}(\tilde{q})
      -\tau^{-2}  G_\lambda^{(0)}(q) L_\mu^{(1)}(\tilde{q}) \right) \\
    & +\frac{1}{2}   q^{\lambda/2} (-1)^{\mu} \left( \tau^{-1}
      G_\lambda^{(1)}(q) G_\mu^{(0)}(\tilde{q})
      - \tau^{-2}  G_\lambda^{(0)}(q) G_\mu^{(1)}(\tilde{q}) \right) 
\end{aligned}$$
:::

::: proof
*Proof.* This follows by applying the residue theorem to the state-integral [\[inst-def\]](#inst-def){reference-type="eqref" reference="inst-def"}, along the lines of the proof of Theorem 1.1 in [@GK:qseries]. One closes the contour to encircle the poles in the lower half-plane, located at

$$y_{m,n}= -{{\rm i}{\mathsf{b}}\over 2} -{\rm i}m {\mathsf{b}}-{\rm i}n {\mathsf{b}}^{-1}, \qquad m,n\ge 0.$$

The poles of the integrand come the poles and the zeros of the quantum dilogarithm as well as from the $\tanh$ function. When $n=0$ they are triple (a double pole comes from the quantum dilogarithm and a simple pole from $\tanh$), while those with $n>0$ are double, coming only from the quantum dilogarithm. The triple poles lead to the series $G_\lambda^{(2)}(q)$. In order to obtain the final result, one also has to use the properties of $E_2(q)$ under modular transformations, i.e.

$$E_2(\tilde{q})= \tau^2 \left( E_2 (q) + {12 \over 2 \pi {\rm i}\tau} \right).$$ ◻
:::

::: remark
The state-integral [\[inst-def\]](#inst-def){reference-type="eqref" reference="inst-def"} can be evaluated for arbitrary rational values of $\tau$ by using the techniques of [@GK:evaluation]. One finds for example, for ${\mathsf{b}}^2=1$,

$$\mathcal{Z} (1)= -2 \sinh^2 \left( {V \over 4 \pi} \right),$$

where $V$ is the hyperbolic volume of $\mathbf{4}_1$.
:::

::: remark
Equation [\[itau-borel\]](#itau-borel){reference-type="eqref" reference="itau-borel"} can be written as

$$\label{nsi-median}
\mathcal{Z}(\tau)= \, s_{\rm med} ( \Phi^{(\sigma_0)} ) (\tau),
\qquad \tau >0.$$
:::

We now discuss an important analytic extension of the matrix $\mathbf J_\mu(q)$ defined for $|q| \neq 1$. We define $$\label{Wgt}
W_{S,\lambda,\mu}(\tau) = \mathbf J_\lambda(\tilde{q})^{-1}
\mathrm{diag}(\tau^{3/2}, \tau^{1/2}, \tau^{-1/2}) \, \mathbf J_\mu(q)
\qquad (\tau \in \mathbbm C\setminus\mathbbm R)\,.$$ As in Section [\[sub.AK41\]](#sub.AK41){reference-type="ref" reference="sub.AK41"}, we find that the domain of $W_{S,\lambda,\mu}$ is independent of the integers $\lambda$ and $\mu$.

::: theorem
[]{#thm.2 label="thm.2"} $W_{S,\lambda,\mu}(\tau)$ extends to a holomorphic function on $\mathbbm C'$ and equals to the matrix $(Z_{\lambda+i,\mu+j}(\tau))$ (for $i,j =0,1,2$), up to left-multiplication by a matrix of automorphy factors.
:::

::: proof
*Proof.* For the bottom block of four entries, this result is already known from [@GGM:resurgent; @GGM:peacock], and it follows from [\[zlmu\]](#zlmu){reference-type="eqref" reference="zlmu"} as was discussed in Section [\[sub.AK41\]](#sub.AK41){reference-type="ref" reference="sub.AK41"}. The top two non-trivial entries $(\sigma_0,\sigma_j)$ of $W_{S,\lambda,\mu}(\tau)$ for $j=1,2$ are given by

$$\tau^{3/2}\left(G_{\mu-1+j}^{(2)}(q)
    +\tau^{-1} G_{\mu-1+j}^{(1)}(q)L_{\lambda}^{(0)}(\tilde{q}) - 
    \tau^{-2} G_{\mu-1+j}^{(0)}(q)L_{\lambda}^{(1)}(\tilde{q}) \right)\,.$$

In view of Theorem [\[thm-newst\]](#thm-newst){reference-type="ref" reference="thm-newst"} and [\[zlmu\]](#zlmu){reference-type="eqref" reference="zlmu"} they can be written as a sum of state-integrals ${\mathcal{Z}}_{\lambda, \mu}(\tau)$ and ${\mathcal{Z}}_{\lambda, \mu+1}(\tau)$, multiplied by holomorphic factors. This proves the theorem. ◻
:::
