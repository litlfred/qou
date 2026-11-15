---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-007-3-dimensional-convexity-properties-of-relative-e
section_title: "Dimensional convexity properties of relative entropy for log-concave measures with homogeneous potential"
section_number: 3
pages: 13-18
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.963
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
[]{#sec: dimconhomo label="sec: dimconhomo"} In this section, we fix a measure $\nu$ of the form $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, where $V: \mathbb{R}^n \to \mathbb{R}\cup \{ + \infty \}$ is a convex function. We will break down the proof of the main result of this section into several lemmas, for the convenience of the reader who may wish to generalize our results.

The relative entropy with respect to $\nu$ can be decomposed into two parts. Suppose $\mu$ is a probability measure that has density with respect to $\nu$. Write $\frac{\textnormal{ d}\mu}{\textnormal{ d}x} = f$. Then, $$D(\mu \Vert \nu) = \int f \log \frac{f}{e^{-V}} \textnormal{ d}x = \int f \log f \textnormal{ d}x + \int Vf \textnormal{ d}x = - h(\mu) + \mathcal{V}(\mu) ,$$ where $\mathcal{V}(\mu) = \int V \textnormal{ d}\mu$. Recall that we are interested in the concavity of $$e^{- a D(\cdot \Vert \nu)} = e^{a h(\cdot)} e^{- a \mathcal{V}(\cdot)}.$$ We will deal with the two factors separately.

Firstly, it is known that $e^{\frac{h(\cdot)}{n}}$ is displacement concave on $\mathscr{W}_{2}(\mathbb{R}^n)$. As mentioned earlier, this was obtained by Erbar, Kuwada, and Sturm [@ErbarKuwadaSturm15 Theorem 3.12] in a much more general setup. For completeness we specialize their argument to outline a proof.

::: thm
[]{#thm: EKS15 label="thm: EKS15"} Lebesgue measure on $\mathbb{R}^n$ satisfies the "entropic $CD(0,n)$ condition", that is, $e^{\frac{h(\cdot)}{n}}$ is displacement concave on $\mathscr{W}_{2}(\mathbb{R}^n)$.
:::

::: proof
*Proof outline.* We want to show that the non-negative quantity $e^{\frac{h(\mu_{t})}{n}}$ is concave in $t$. If neither $\mu_{0}$ nor $\mu_{1}$ have density, there is nothing to prove. If one of them has density then the interpolants have density ([@Villani03 Proposition 5.9]), and the result would follow from the corresponding result assuming both endpoints have density, using the upper-semicontinuity of the Shannon--Boltzmann entropy. Therefore we assume that $\mu_{0}, \mu_{1}$ have density with respect to the Lebesgue measure. Suppose $T_{t}= \nabla\phi_{t}$ is the Brenier map from $\mu_{0}$ to $\mu_{t}$. Using the change of variables $f_{t}(\nabla\phi_{t} (x))\det \nabla^{2} \phi_{t} (x) = f_{0} (x)$ (see [@Villani03 Theorem 4.8]) relating the densities $f_{t}$, and the $(1/n)$-concavity of the determinant on the space of positive-definite matrices, one obtains $$\label{eq: dimensionaldensityrelation}
f_{t}((1-t)x + t y)^{-1/n} \geq (1-t)f_{0}(x)^{-1/n} + t f_{1}(x)^{-1/n},$$ $\pi(x,y)-a.e.$, where $\pi$ is the optimal coupling between $\mu_{0}$ and $\mu_{1}$. We define a convex function, $$G_{t}(a,b) = \log \left( (1-t) e^{a} + t e^{b}   \right).$$ Then, by taking logarithms of both sides of the inequality [\[eq: dimensionaldensityrelation\]](#eq: dimensionaldensityrelation){reference-type="eqref" reference="eq: dimensionaldensityrelation"}, and integrating, $$\begin{split}
    \frac{1}{n} h(\mu_{t}) &= \int - \frac{1}{n} \log f_{t} \textnormal{ d}\mu_{t} \\
    &= \int -  \frac{1}{n} \log f_{t}((1-t)x + t y ) \textnormal{ d}\pi (x,y)   \\
    & \geq \int \log \left(  (1-t)f_{0}(x)^{-1/n} + t f_{1}(y)^{-1/n}  \right) \textnormal{ d}\pi (x,y) \\
    &= \int G_{t} \left( - \frac{1}{n} \log f_{0}(x), - \frac{1}{n} \log f_{1}(y) \right) \textnormal{ d}\pi (x,y)\\
    & \geq G_{t} \left(  \int - \frac{1}{n} \log f_{0}(x) \textnormal{ d}\pi (x,y) , \int - \frac{1}{n} \log f_{1}(y) \textnormal{ d}\pi (x,y)    \right) \\
    &= G_{t} \left( \frac{1}{n}h(\mu_{0}) , \frac{1}{n}h(\mu_{1}) \right) = \log \left( (1-t)e^{h(\mu_{0})/n} + t e^{h(\mu_{1})/n}   \right). \qedhere
    \end{split}$$ ◻
:::

::: rem
Let $X,Y$ be $\mathbb{R}^n$-valued random vectors. Then the above theorem says that $$\label{eq: EKS without scales}
e^{h(X+Y)/n} \geq e^{h(X)/n} + e^{h(Y)/n},$$ where $(X,Y)$ are optimally coupled, that is, the distribution of $(X,Y)$ is the optimal coupling between the distributions of $X$ and $Y$. This can be seen by using the scaling property of entropy, $h(\lambda X) = h(X) + n \log \lambda$ for $\lambda \in (0, \infty)$. For a similar result, see the work of Aras and Courtade ([@ArasCourtade21 Corollary 5]), where they give bounds for $h(X+Y)$ based on the amount of dependence allowed between $X$ and $Y$. At one end, when there is no restriction on the dependence, they obtain an inequality like the above. At the other end, when $X$ and $Y$ are assumed to be independent, they obtain the *Entropy Power inequality*: $e^{2h(X+Y)/n} \geq e^{2h(X)/n} + e^{2h(Y)/n}$.
:::

We now turn to the other factor, $e^{-a \mathcal{V}(\cdot)}$. For this purpose, we would like a differential criterion for a function $e^{-a \theta (\cdot)}: [0,1] \to \mathbb{R}$ to be concave.

::: lem
[]{#lem: whatitmeansinderivative label="lem: whatitmeansinderivative"} Let $\theta : [0,1] \to \mathbb{R}$ be a twice continuously differentiable function, $a>0$. If we have $$\theta ''(t) \geq a \left( \theta'(t) \right)^{2},$$ then $e^{- a \theta(t)}$ is concave.
:::

::: proof
*Proof.* We simply use the second-derivative test for concavity, and the following calculation. $$\left( e^{-a \theta } \right)'' = \left( - e^{- a \theta } a \theta ' \right)' = \left( - e^{a \theta} a \theta'' +  e^{-a \theta}a^{2} \left( \theta' \right)^{2}   \right) = a e^{-a \theta} \left(  a \left( \theta' \right)^{2} - \theta''  \right).$$ ◻
:::

Therefore, the quantities of interest are $\frac{\textnormal{ d}}{\textnormal{ d}t} \mathcal{V}(\mu_{t})$ and $\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} \mathcal{V}(\mu_{t})$, which can be calculated using equation [\[eq: continuityeqn\]](#eq: continuityeqn){reference-type="eqref" reference="eq: continuityeqn"} and [\[eq: HamiltonJacobi\]](#eq: HamiltonJacobi){reference-type="eqref" reference="eq: HamiltonJacobi"}.

::: lem
[]{#lem: explicitderivatiesforV label="lem: explicitderivatiesforV"} Suppose $\mathcal{V}(\mu) = \int V \textnormal{ d}\mu$, for a twice continuously differentiable convex function $V$. Let $\nabla\theta_{t}$ be the velocity field associated with the displacement interpolation $\{ \mu_{t} \}_{t \in [0,1]}$. Then, $$\frac{\textnormal{ d}}{\textnormal{ d}t} \mathcal{V}(\mu_{t}) = \int \langle \nabla V, \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t}, \, \frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} \mathcal{V}(\mu_{t}) =  \int \langle \nabla^{2}V \cdot \nabla\theta_{t}, \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t}.$$
:::

::: proof
*Proof.* The formula for the first derivative is the continuity equation [\[eq: continuityeqn\]](#eq: continuityeqn){reference-type="eqref" reference="eq: continuityeqn"} itself. For the second derivative, we compute $$\begin{split}
    \frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} \mathcal{V}(\mu_{t}) &= \frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} \int V (T_{t}(x)) \textnormal{ d}\mu_{0}  = \frac{\textnormal{ d}}{\textnormal{ d}t} \int \langle \nabla V (T_{t}(x)) , \frac{\textnormal{ d}}{\textnormal{ d}t} T_{t} (x) \rangle \textnormal{ d}\mu_{0} (x)\\
    &= \int \langle \nabla^{2}V (T_{t}(x)) \cdot \frac{\textnormal{ d}}{\textnormal{ d}t}T_{t}(x) , \frac{\textnormal{ d}}{\textnormal{ d}t}T_{t}(x) \rangle \textnormal{ d}\mu_{0} + \int \langle \nabla V (T_{t}(x)) , \frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} T_{t} (x) \rangle \textnormal{ d}\mu_{0}  \\
    &= \int   \langle \nabla^{2}V (T_{t}(x)) \cdot \nabla\theta_{t} (T_{t}(x)) , \nabla\theta_{t} (T_{t}(x)) \rangle \textnormal{ d}\mu_{0} + 0 \\
    &= \int \langle \nabla^{2}V \cdot \nabla\theta_{t}, \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t}, \\
\end{split}$$ where $T_{t} = (1-t)I + tT$ denotes the optimal map transporting $\mu_{0}$ to $\mu_{t}$ which is used to define $\nabla\theta_{t}$. ◻
:::

::: rem
[]{#rem: formulatrueforallflows label="rem: formulatrueforallflows"} From the proof, one can observe that the formula for the second derivative only uses the fact that each particle travels along a straight line with constant speed, that is, $\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} T_{t} (x) = 0$.
:::

Therefore, to obtain the concavity of $e^{- a \mathcal{V}(\cdot)}$ on a displacement convex subset of $\mathscr{W}_{2}(\mathbb{R}^n)$, we need to prove the inequality $\int \langle \nabla^{2} V \cdot \nabla\theta_{t} , \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t} \geq a \left( \int \langle \nabla V, \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t} \right)^{2}$ for displacement interpolants $\{\mu_{t} \}$ through that set. The following Cauchy--Schwarz inequality is useful for this purpose:

::: lem
[]{#lem: twistedholder label="lem: twistedholder"} Suppose $A(t)$ is a positive-definite matrix, for every $t$. Then, $$\left(  \int \langle \nabla\theta_{t}, \nabla V \rangle \textnormal{ d}\mu_{t}  \right)^{2} \leq \left( \int \langle A \cdot \nabla\theta_{t} , \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t}  \right) \left( \int \langle A^{-1} \cdot \nabla V , \nabla V \rangle \textnormal{ d}\mu_{t}\right).$$
:::

::: proof
*Proof.* We tread a beaten path. Let $s \in \mathbb{R}$, then $$\begin{split}
    &0 \leq \int \vert A^{1/2} \cdot \nabla\theta_{t} - s A^{-1/2} \cdot \nabla V \vert^{2}_{2} \textnormal{ d}\mu_{t} \\
    &= \left( \int \langle A \cdot \nabla\theta_{t} , \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t}  \right) + s^{2} \left( \int \langle A^{-1} \cdot \nabla V , \nabla V \rangle \textnormal{ d}\mu_{t}\right) - 2s  \left(  \int \langle \nabla\theta_{t}, \nabla V \rangle \textnormal{ d}\mu_{t}  \right). 
\end{split}$$ Now the observation that the quadratic function $As^2 - 2Bs + C$ achieves its minimal value when $s= B/A$ completes the proof. ◻
:::

Using the above lemma with $A = \nabla^{2}V$ gives, $$\label{eq: twisterholderinaction}
\left( \frac{\textnormal{ d}}{\textnormal{ d}t} \mathcal{V}(\mu_{t}) \right)^2  \leq \left( \frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} \mathcal{V}(\mu_{t}) \right) \left( \int \langle \left(\nabla^{2}V\right)^{-1} \cdot \nabla V , \nabla V \rangle \textnormal{ d}\mu_{t}\right).$$ Thus, we can upper bound $\int \langle \left(\nabla^{2}V\right)^{-1} \cdot \nabla V , \nabla V \rangle \textnormal{ d}\mu_{t}$ by $\frac{1}{a}$ to get the concavity of $e^{- a \mathcal{V}(\cdot)}$. When $V$ is *$p$-homogeneous*, that is, when $V( \lambda x) = \lambda^{p} V(x)$ for all $\lambda > 0$, this quantity is a multiple of $V$ itself. In the remainder of this section, all unspecified evaluations should be understood as being evaluated at $x$. For example, $\int \langle \nabla V , x \rangle \textnormal{ d}\mu$ stands for $\int \langle \nabla V (x) , x \rangle \textnormal{ d}\mu (x)$.

::: lem
[]{#lem: the thing when V is p homo label="lem: the thing when V is p homo"} Let $V$ be a $p$-homogeneous convex function. Then, $$\langle \left(\nabla^{2}V\right)^{-1} \cdot \nabla V , \nabla V \rangle = \frac{1}{p-1} \langle \nabla V , x \rangle = \frac{p}{p-1}V.$$
:::

::: proof
*Proof.* If $V$ is $p$-homogeneous, then $\langle \nabla V , x \rangle = \lim_{t \to 0} 
\frac{V(x + tx) - V(x)}{t} = p V$, implying the second equality. Differentiating this equation we get $\nabla^{2}V \cdot x = (p-1) \nabla V$, which implies the first equality in the assertion. ◻
:::

We now bound $\int \langle \nabla V , x \rangle \textnormal{ d}\mu$ for a suitable class of measures (and general $V$), which will give us enough ingredients to put together a displacement concavity statement when $V$ is $p$-homogenous. The main argument of [@KolesnikovLivshyts21 Lemma 5.3] extends to our slightly more general case. Recall that a function $f : \mathbb{R}^n \to \mathbb{R}$ is said to be *radially decreasing* if $f(\lambda x) \leq f(x)$, for all $x \in \mathbb{R}^n, \lambda \geq 1$.

::: lem
[]{#lem: for radially decreasing label="lem: for radially decreasing"} Suppose $\mu \in \mathscr{W}_{2}(\mathbb{R}^n)$ is absolutely continuous with respect to the measure $\nu = e^{-V} \textnormal{ d}x$, $V$ convex. If the density $\frac{\textnormal{ d}\mu }{\textnormal{ d}\nu}$ is radially decreasing, then $\int \langle \nabla V, x \rangle \textnormal{ d}\mu \leq n$.
:::

::: proof
*Proof.* Write $f = \frac{\textnormal{ d}\mu }{\textnormal{ d}\nu}$, so that $\frac{d \mu}{\textnormal{ d}x} = f e^{-V}$. By approximation, we may assume that both $f$ and $V$ are smooth. Now, the function $$F (s) = \int f(sx) \textnormal{ d}\nu (x) = \int f(sx) e^{-V(x)} \textnormal{ d}x,$$ is clearly decreasing in $s$. Therefore, $$\begin{split}
0 &\geq F'(1) = \int \langle \nabla f(x) , x \rangle e^{-V(x)} \textnormal{ d}x = \int \langle \nabla f(x) , x e^{-V(x)} \rangle \textnormal{ d}x \\
&= - \int f(x) \nabla\cdot (x e^{-V(x)}) \textnormal{ d}x 
= - \int f(x) \left( n e^{-V(x)} - \langle x , \nabla V(x) \rangle e^{-V(x)} \right) \textnormal{ d}x \\
&=  \int \langle \nabla V , x \rangle \textnormal{ d}\mu - n. \qedhere
\end{split}$$ ◻
:::

This sets us up to obtain the following displacement concavity result.

::: thm
[]{#thm: dimdispconV label="thm: dimdispconV"} Let $V: \mathbb{R}^n \to [0 , \infty)$ be a $p$-homogeneous convex function, $p \in (1, \infty)$. Let $\nu$ be a probability measure of the form $\textnormal{ d}\nu = e^{-V + c} \textnormal{ d}x$, for some normalizing constant $c$. Then, the following statements are true.

1.  The set $S = \{ \mu : \mathcal{V}(\mu) \leq \frac{n}{p} \}$ is displacement convex and contains all measures whose density with respect to $\nu$ is radially decreasing.

2.  The functional $e^{- \frac{p-1}{n}\mathcal{V}(\cdot)}$, where $\mathcal{V}(\mu) = \int V \textnormal{ d}\mu$, is displacement concave on $S$.
:::

::: proof
*Proof.* First, note that $S$ is a displacement convex set because $\mathcal{V}$ is displacement convex on all of $\mathscr{W}_{2}(\mathbb{R}^n)$ (which is a direct consequence of the convexity of $V$, see [@Villani03 Theorem 5.15 (ii)]). Moreover, $S = \{ \mu :  \int \langle \nabla V , x \rangle \textnormal{ d}\mu \leq n \}$, so by Lemma [\[lem: for radially decreasing\]](#lem: for radially decreasing){reference-type="ref" reference="lem: for radially decreasing"} it contains all measures with radially decreasing density with respect to $\nu$.

For the displacement concavity statement, we begin by assuming that $V$ is twice continuously differentiable. Recall that the derivative criteria Lemma [\[lem: whatitmeansinderivative\]](#lem: whatitmeansinderivative){reference-type="ref" reference="lem: whatitmeansinderivative"} and the Cauchy--Schwarz applied to our case (Equation [\[eq: twisterholderinaction\]](#eq: twisterholderinaction){reference-type="eqref" reference="eq: twisterholderinaction"}) imply that we need to show $$\int \langle \left(\nabla^{2}V\right)^{-1} \cdot \nabla V , \nabla V \rangle \textnormal{ d}\mu \leq \frac{n}{p-1},$$ for all $\mu \in S$. However, this is precisely the defining property of $S$ in light of Lemma [\[lem: the thing when V is p homo\]](#lem: the thing when V is p homo){reference-type="ref" reference="lem: the thing when V is p homo"}.

Finally we relax the smoothness assumption on $V$ using the following argument. Since $V$ is $p$-homogeneous and convex, $V^{1/p}$ is $1$-homogeneous and quasi-convex. Now every $1$-homogeneous quasi-convex function is necessarily convex, thus $V = h_{K}^{p}$ for some convex body $K$, where $h_{K}(x) = \sup_{y \in \mathbb{S}^{n-1}} \langle x , y \rangle$ denotes the support function of $K$. Recall that $K$ can be approximated by an increasing sequence of convex bodies $K_{i}$, with smooth support functions, which converge to $K$ in the Hausdorff metric (see, [@Schneider14 Section 3.4]). Thus, we can obtain an increasing sequence of smooth $p$-homogeneous convex functions $V_{i} = h_{K_i}^p$ converging to $V$ monotonically. By dominated convergence, $\mathcal{V}_i(\mu) \to \mathcal{V}(\mu)$ for all $\mu$. Each $S_i = \{ \mu : \mathcal{V}_{i}(\mu):= \int V_{i} \textnormal{ d}\mu \leq \frac{n}{p} \}$ is a displacement convex set, therefore $S = \bigcap_{i=1}^\infty S_i$ is also displacement convex. Moreover, the functionals $e^{- \frac{p-1}{n}\mathcal{V}_{i}(\cdot)}$ are displacement concave on $S$, so this is also true for their pointwise limit $e^{- \frac{p-1}{n}\mathcal{V}(\cdot)}$. The proof concludes by taking limits. ◻
:::

Now that we know $e^{\frac{h(\cdot)}{n}}$ and $e^{- \frac{p-1}{n}\mathcal{V}(\cdot)}$ are both displacement concave on $S$, Theorem [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"}, restated below, is a straightforward consequence.

::: thm
[]{#thm: dimdispconD label="thm: dimdispconD"} Let $V: \mathbb{R}^n \to [0 , \infty)$ be a $p$-homogeneous convex function, $p \in (1, \infty)$. Let $\nu$ be a probability measure of the form $\textnormal{ d}\nu = e^{-V + c} \textnormal{ d}x$, for some normalizing constant $c$. Then, the functional $e^{- \frac{p-1}{pn}D(\cdot \Vert \nu)}$ is displacement concave on the set $S = \{ \mu : \int V \textnormal{ d}\mu \leq \frac{n}{p} \}$, which contains all measures with radially decreasing density with respect to $\nu$.
:::

::: proof
*Proof.* Observe that, $$e^{- \frac{p-1}{pn}D(\cdot \Vert \nu)} = e^{\frac{p-1}{pn}c} \left( e^{\frac{h(\cdot)}{n}} \right)^{1- \frac{1}{p}} \left( e^{- \frac{p-1}{n}\mathcal{V}(\cdot)} \right)^{\frac{1}{p}},$$ where $\mathcal{V}(\mu) = \int V \textnormal{ d}\mu$. Now, since $(x,y) \mapsto x^{1 - \frac{1}{p}}y^{\frac{1}{p}}$ is concave on $[0, \infty)^{2}$ and increasing in each coordinate, it suffices to prove the displacement concavity of $e^{\frac{h(\cdot)}{n}}$ and $e^{- \frac{p-1}{n}\mathcal{V}(\cdot)}$ separately. Since this has already been achieved in Theorem [\[thm: EKS15\]](#thm: EKS15){reference-type="ref" reference="thm: EKS15"} and Theorem [\[thm: dimdispconV\]](#thm: dimdispconV){reference-type="ref" reference="thm: dimdispconV"} for $S$, the asserted displacement concavity result for $S$ follows. ◻
:::

Finally, observe that the density of $\nu_{K}$ with respect to $\nu$, if $K$ is a star body, is a radially decreasing function. Therefore, Theorem [\[thm: dimdispconD\]](#thm: dimdispconD){reference-type="ref" reference="thm: dimdispconD"} above and Proposition [\[pro: wand\]](#pro: wand){reference-type="ref" reference="pro: wand"}, together imply Theorem [\[thm:main-BM intro\]](#thm:main-BM intro){reference-type="ref" reference="thm:main-BM intro"} restated below.

::: thm
[]{#thm:main-BM label="thm:main-BM"}Let $V:\mathbb{R}^{n}\to[0,\infty)$ be a $p$-homogeneous convex function for $1<p<\infty$, and let $\nu$ be a measure with density $\frac{\mathrm{d}\nu}{\mathrm{d}x}$ proportional to $e^{-V}$. Let $A,B\subseteq\mathbb{R}^{n}$ be star bodies. Then for all $0\le\lambda\le1$ we have $$\text{\ensuremath{\nu\left((1-\lambda)A+\lambda B\right)^{\frac{p-1}{pn}}\ge(1-\lambda)\nu(A)^{\frac{p-1}{pn}}+\lambda\nu\left(B\right)^{\frac{p-1}{pn}}.}}$$
:::

0◻
