---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-008-4-dimensional-convexity-properties-of-the-gaussi
section_title: "Dimensional convexity properties of the Gaussian relative entropy"
section_number: 4
pages: 18-25
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.985
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
[]{#sec: gaussian label="sec: gaussian"} In this section, we will differentiate the relative entropy $D(\cdot \Vert \nu)$, where $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, directly along displacement interpolations without decomposing it into two parts as in the previous section. While we focus on the Gaussian measure, $\nu = \gamma$, we will introduce the relevant setup for a general $\nu$.

In this direction, the presentation is cleaner and more insightful if we use the language of the Bakry--Émery $\Gamma$-calculus. Measures $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, for smooth enough $V$, naturally occur as the equilibrium measure for the semigroup of operators $P_{t} = e^{tL}$, with generator $Lf = \Delta f - \langle \nabla V , \nabla f \rangle$. Introduction of the bilinear form $\Gamma$ (called the carré du champ) on functions, and its iteration $\Gamma_{2}$, reduces the study of many properties regarding convergence to equilibrium to the study of the relationships among $L$, $\Gamma$, and $\Gamma_{2}$.

In the case of $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$ under discussion, when the generator $L$ is as described earlier, the carré du champ and its iteration are given by, $$\begin{split}
    & \Gamma (f,g) = \langle \nabla f , \nabla g \rangle, \\
    & \Gamma_{2} (f,g) = \langle \nabla^{2} f , \nabla^{2} g \rangle + \langle \nabla^{2}V \cdot \nabla f , \nabla g \rangle,
\end{split}$$ where the first inner-product in the expression for $\Gamma_{2}$ is the Hilbert--Schmidt inner product. It is customary to write $\Gamma (f)$ for $\Gamma (f, f)$, and $\Gamma_{2} (f)$ for $\Gamma_{2}(f,f)$. We refer the reader to the text [@BakryGentilLedoux14] for a comprehensive treatment of this subject. However, what we will use in calculating the derivatives of $D(\mu_{t} \Vert \nu)$ is a simple integration-by-parts formula that the reader may verify directly, $$\label{eq: integrationbyparts}
 \int \Gamma (f,g) \textnormal{ d}\nu = - \int f L g \textnormal{ d}\nu.$$

::: exmpl
When $V = 0$, one obtains the *heat semigroup* which has the Lebesgue measure as its equilibrium measure. In this case, $L f= \Delta f$, $\Gamma (f) = \vert \nabla f \vert^{2}$, and $\Gamma_{2} (f) = \Vert \nabla^{2} f \Vert^{2}$. Here $\Vert \cdot \Vert$ denotes the Hilbert--Schmidt norm.
:::

::: exmpl
[]{#exmpl: OU label="exmpl: OU"} When $V$ corresponds to the Gaussian measure on $\mathbb{R}^n$, $\nu = \gamma$, the semigroup obtained is the well-known *Ornstein--Uhlenbeck semigroup*. Then $Lf = \Delta f - \langle x, \nabla f \rangle$, $\Gamma (f) = \vert \nabla f \vert^{2}$, and $\Gamma_{2} (f) = \Vert \nabla^{2} f \Vert^{2} + \vert \nabla f \vert^{2}$.
:::

Let us differentiate $D(\cdot \Vert \nu)$ two times, as needed. The underlying heuristic, namely that $P_{t}  f \textnormal{ d}\nu$ is the gradient flow of $D( \cdot \Vert \nu)$ (starting at $f \textnormal{ d}\nu$) under a natural Riemannian-like structure on $\mathscr{W}_{2}(\mathbb{R}^n)$ introduced by Otto ([@Otto01]), is a powerful tool in the field. However, we will be content with the following simple calculation and refer the reader to [@Villani03 Chapter 8] or [@Villani09 Chapter 15] for more details.

::: lem
[]{#lem: derivativesofentropy label="lem: derivativesofentropy"} Let $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, for smooth $V$. Consider a displacement interpolation $\{ \mu_{t} \}_{t \in [0,1]}$ in $\mathscr{W}_{2}(\mathbb{R}^n)$, with the optimal velocity field $\nabla\theta_{t}$. Suppose $\theta_{t}$ is sufficiently smooth, then $$\begin{split}
    &\frac{\textnormal{ d}}{\textnormal{ d}t} D(\mu_{t} \Vert \nu) = - \int L \theta_{t} \textnormal{ d}\mu_{t}, \\
    &\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}}  D(\mu_{t} \Vert \nu) = \int \Gamma_{2} (\theta_{t}) \textnormal{ d}\mu_{t}., \\
\end{split}$$ where $L, \Gamma_{2}$ are as described earlier.
:::

::: proof
*Proof.* Let $\rho_{t}$ denote the density of $\mu_{t}$ with respect to $\nu$. Then, $$\label{eq: firstderivativeentropycomp}
\begin{split}
\frac{\textnormal{ d}}{\textnormal{ d}t} D(\mu_{t} \Vert \nu) &= \frac{\textnormal{ d}}{\textnormal{ d}t} \int \rho_{t} \log \rho_{t} \textnormal{ d}\nu = \frac{\textnormal{ d}}{\textnormal{ d}t} \int  \log \rho_{t} \textnormal{ d}\mu_{t} \\
&= \int \partial_{t}  \log \rho_{t} \textnormal{ d}\mu_{t} + \int \langle \nabla\log \rho_{t} , \nabla\theta_{t} \rangle \textnormal{ d}\mu_{t} \\
&=  \frac{\textnormal{ d}}{\textnormal{ d}t}\int  \rho_{t} \textnormal{ d}\nu + \int \langle \nabla\log \rho_{t} , \nabla\theta_{t} \rangle \rho_{t} \textnormal{ d}\nu\\
&= 0 + \int \langle \nabla\rho_{t} , \nabla\theta_{t} \rangle \textnormal{ d}\nu = - \int \rho_{t} \, L \theta_{t} \textnormal{ d}\nu = - \int L \theta_{t} \textnormal{ d}\mu_{t}. 
\end{split}$$ In the above computation, the third equality uses the chain rule and the continuity equation [\[eq: continuityeqn\]](#eq: continuityeqn){reference-type="eqref" reference="eq: continuityeqn"}, and the sixth equality is an application of formula [\[eq: integrationbyparts\]](#eq: integrationbyparts){reference-type="eqref" reference="eq: integrationbyparts"} for the semigroup under consideration.

Furthermore, we can differentiate again to compute the second derivative, $$\begin{split}
\frac{\textnormal{ d}^{2}}{\textnormal{ d}t ^{2}}  D(\mu_{t} \Vert \nu) &= -  \frac{\textnormal{ d}}{\textnormal{ d}t} \int  L \theta_{t} \textnormal{ d}\mu_{t} = - \int  L \partial_{t} \theta_{t} \textnormal{ d}\mu_{t} - \int \langle \nabla L \theta_{t} , \nabla\theta_{t} \rangle  \textnormal{ d}\mu_{t}  \\
&= \int  L \left( \frac{|\nabla\theta_{t} |^{2}}{2} \right)  \textnormal{ d}\mu_{t} - \int \langle \nabla L \theta_{t} , \nabla\theta_{t} \rangle  \textnormal{ d}\mu_{t} \\
&= \int \left(  L \left( \frac{|\nabla\theta_{t} |^{2}}{2} \right) -   \langle \nabla L \theta_{t} , \nabla\theta_{t} \rangle \right) \textnormal{ d}\mu_{t} = \int \Gamma_{2} (\theta_{t}) \textnormal{ d}\mu_{t},
\end{split}$$ where in the second equality we use the change rule and the continuity equation [\[eq: continuityeqn\]](#eq: continuityeqn){reference-type="eqref" reference="eq: continuityeqn"}, the third equality uses the Hamilton--Jacobi equation [\[eq: HamiltonJacobi\]](#eq: HamiltonJacobi){reference-type="eqref" reference="eq: HamiltonJacobi"}, while the last equality uses the formula $$\Gamma_{2} (f) =  L \left( \frac{|\nabla f |^{2}}{2} \right) -   \langle \nabla L f , \nabla f \rangle$$ for smooth $f$. This is a well-known weighted version of Bochner's formula, which can be easily obtained from its unweighted counterpart (see, for example, [@Villani09 Chapter 14]). ◻
:::

Therefore, if $S \subseteq \mathscr{W}_{2}(R^{n})$ is a displacement convex set, and we would like to prove that $e^{- a D (\cdot \Vert \nu)}$ is concave on $S$, we must prove that $$\int \Gamma_{2} (\theta_{t}) \textnormal{ d}\mu_{t} \geq a \left( \int L \theta_{t} \textnormal{ d}\mu_{t} \right)^{2},$$ for all displacement interpolations $\{ \mu_{t} \}_{t \in [0,1]}$ in $S$. Actually, in this section, we would like to go a little bit further than the above inequality to also utilize the "curvature" associated with the semigroup. To this end, we introduce the notion of $(\kappa, 1/a)$-convexity of a function defined on a uniquely geodesic space.

::: definition
[@ErbarKuwadaSturm15 Equation 1.2 rephrased] []{#def: knconvexity label="def: knconvexity"} Let $(\mathcal{X},d)$ be a uniquely geodesic metric space. A function $S: \mathcal{X} \to [0, \infty]$ is called *$(\kappa,1/a)$-convex* if for every constant speed geodesic $c : [0,1] \to \mathcal{X}$, we have $$\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} S(c_{t}) \geq \kappa d(c_{0}, c_{1})^{2} + a \left( \frac{\textnormal{ d}}{\textnormal{ d}t}S(c_{t}) \right)^{2},$$ in the distributional sense.
:::

::: rem
A global formulation of the above condition can be found in [@ErbarKuwadaSturm15 Definition 2.7]. We discuss the particular case of $(2,n)$-convexity in Lemma [\[lem: 2ncon\]](#lem: 2ncon){reference-type="ref" reference="lem: 2ncon"}.
:::

Thus, Theorem [\[thm: dimdispconD\]](#thm: dimdispconD){reference-type="ref" reference="thm: dimdispconD"} from previous section establishes $(0, \frac{p}{p-1}n)$-convexity of the relative entropy $D(\cdot \Vert \nu)$ on the geodesic subspace $S = \{ \mu: \int V \textnormal{ d}\mu \leq \frac{n}{p} \} \subseteq \mathscr{W}_{2}(\mathbb{R}^n)$ when $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, where $V$ is a $p$-homogeneous convex function on $\mathbb{R}^n$. In this case, it is possible to trade some of the dependence on $n$ for a dependence on the lower bounds on $\nabla^{2} V$, but we choose not to pursue this direction in the current paper.

We will now specialize to the Gaussian case. Note that this corresponds to the semigroup in Example [\[exmpl: OU\]](#exmpl: OU){reference-type="ref" reference="exmpl: OU"}. Here we aim to obtain a $(\kappa, n)$-convexity of $D(\cdot \Vert \gamma)$ on a suitable class of measures. Thus, we want to obtain an inequality that reads, $$\label{eq: entropiccdkn}
\int \Gamma_{2}(\theta_{t}) \textnormal{ d}\mu_{t} \geq \kappa \mathscr{W}_{2}^{2}(\mu_{0}, \mu_{1}) + \frac{1}{n} \left( \int L \theta_{t} \textnormal{ d}\mu_{t} \right)^{2},$$ that is, $$\int \Vert \nabla^{2} \theta_{t} \Vert^{2} + \vert \nabla\theta_{t} \vert^{2} \textnormal{ d}\mu_{t} \geq  \kappa \mathscr{W}_{2}^{2}(\mu_{0}, \mu_{1}) + \frac{1}{n} \left( \int L \theta_{t} \textnormal{ d}\mu_{t} \right)^{2}.$$ This is remarkably similar to the sufficiency condition in [@KolesnikovLivshyts21] obtained from the Kolesnikov--Milman approach ([@KolesnikovMilman18]) with the exception of the first term on the right. This comparison goes beyond similarity, to the level of the proof itself, since it is the same as in [@EskenazisMoschidis21] albeit presented in a slightly different form. While we claim no originality here, for the sake of completeness we repeat the argument from [@EskenazisMoschidis21] adapted to obtain the statement we want.

::: thm
[]{#thm: 2nconunderconditions label="thm: 2nconunderconditions"} Denote by $S_{n}$ the collection of all even measures $\mu$ in $\mathcal{P}_{2,ac}(\mathbb{R}^n)$ which satisfy the inequality $\int f^{2} \textnormal{ d}\mu \leq \int \vert \nabla f \vert^{2} \textnormal{ d}\mu$ for all odd test functions $f$. Then, $$\int \Gamma_{2} (u) \textnormal{ d}\mu \geq 2 \int \Gamma (u) \textnormal{ d}\mu + \frac{1}{n} \left( \int L u \textnormal{ d}\mu \right)^{2},$$ for all even functions $u$. Here $L$, $\Gamma_{2}$ are the generator and the iterated carré du champ, respectively, for the Ornstein--Uhlenbeck semigroup.

Consequently, if $\{ \mu_{t} \}_{t \in [0,1]}$ is a displacement interpolation that lies entirely in $S_{n}$ and is driven by a smooth velocity field, then $D(\mu_{t}\Vert \gamma)$ is $(2,n)$-convex. In particular, $$\label{eq: dispcongaussiannok}
e^{-\frac{D (\mu_{t} \Vert \gamma)}{n}} \geq (1-t) e^{-\frac{D (\mu_{0} \Vert \gamma)}{n}} + t e^{-\frac{D (\mu_{1} \Vert \gamma)}{n}}.$$
:::

::: rem
If the measure $\mu$ satisfies the inequality $\textnormal{Var}_{\mu}(f) \leq C \int \vert \nabla f \vert^{2} \textnormal{ d}\mu$, we say that $\mu$ satisfies a *Poincaré inequality* with constant $C$. The best possible $C$ is called the *Poincaré constant* of $\mu$. If we assume that the function $f$ is odd and the measure $\mu$ is even, then $\textnormal{Var}_{\mu}(f) = \int f^{2} \textnormal{ d}\mu$. Thus, $S_{n}$ is the collection of even measures, absolutely continuous with respect to the Lebesgue measure and having finite second moment, which satisfy a Poincaré inequality for odd functions with constant $1$.
:::

::: proof
*Proof.* Let $u$ be an even function. Consider $v = u  -  r$, where $r(x) = \frac{\int L u \textnormal{ d}\mu}{2n} |x|^{2}$. We will write $l = \int Lu \textnormal{ d}\mu$ for notational convenience. Note that $\nabla r (x) = \frac{l}{n}x, \nabla^{2} r (x) = \frac{l}{n} I$, where $I$ denotes the identity matrix, and $\Delta r = l$. Therefore, $$\begin{split}
\Vert \nabla^2 u \Vert^{2} 
&= \Vert \nabla^2 v + \nabla^{2} r \Vert^{2} 
= \Vert \nabla^{2} v \Vert^{2} + \frac{2l}{n} \Delta v + \frac{l^2}{n} 
= \Vert \nabla^2 v \Vert^{2} + \frac{2 l}{n} \Delta u - \frac{l^2}{n} \\
&=  \Vert \nabla^2 v \Vert^{2} + \frac{2l}{n} \left(   L u + \langle x , \nabla u\rangle  \right) - \frac{l^2}{n} \\
&= \Vert \nabla^2 v \Vert^{2} + \frac{2l}{n}  \langle x , \nabla u\rangle + \left( \frac{2l}{n} Lu - \frac{l^2}{n} \right).
\end{split}$$ Now, since $v$ is even, $\partial_{i}v$ is an odd function, for each $i$. Therefore, if $\mu \in S_{n}$ then we can apply the Poincaré inequality assumption to $\partial_{i} v$ in the calculation below. $$\begin{split}
 \int \Vert \nabla^2 v \Vert^2 \textnormal{ d}\mu 
 &= \sum_{i} \int \sum_{j} \left( \partial_{j} \partial_{i} v \right)^{2} \textnormal{ d}\mu 
 = \sum_{i} \int \vert \nabla\partial_{i} v \vert^{2} \textnormal{ d}\mu  
  \geq \sum_{i} \int \left( \partial_{i} v \right)^2 \textnormal{ d}\mu \\
  &= \sum_{i} \int \left(  \partial_{i} u_{i} - \frac{l}{n}x_{i} \right)^{2} \textnormal{ d}\mu
  = \int \left( | \nabla u |^{2} - \frac{2l}{n} \langle x , \nabla u \rangle + \frac{l^2}{n^{2}} |x|^{2} \right) \textnormal{ d}\mu.
 \end{split}$$

Putting this inequality into the expression for $\Vert \nabla^{2} u \Vert^{2}$ obtained earlier, $$\begin{split}
 \int  \Gamma_{2} (u) \textnormal{ d}\mu &= \int \left( \Vert \nabla^{2} u \Vert^{2} + \vert \nabla u \vert^{2} \right) \textnormal{ d}\mu  \\
 &= \int \left( \Vert \nabla^2 v \Vert^{2} + \frac{2l}{n}  \langle x , \nabla u\rangle + \left( \frac{2l}{n} Lu - \frac{l^2}{n} \right) + \vert \nabla u \vert^{2} \right) \textnormal{ d}\mu \\
 &\geq \int \left( | \nabla u |^{2} - \frac{2l}{n} \langle x , \nabla u \rangle + \frac{l^2}{n^{2}} |x|^{2}  + \frac{2l}{n}  \langle x , \nabla u\rangle + \left( \frac{2l}{n} Lu - \frac{l^2}{n} \right) + \vert \nabla u \vert^{2} \right) \textnormal{ d}\mu  \\
 &= \int \left( 2 | \nabla u |^{2}  + \frac{l^{2}}{n^{2}} |x|^{2} +  \left( \frac{2l}{n} Lu - \frac{l^2}{n} \right) \right) \textnormal{ d}\mu \\
 &\geq \int \left( \frac{2l}{n} Lu - \frac{l^2}{n} \right) \textnormal{ d}\mu + 2 \int \vert \nabla u \vert^{2} \textnormal{ d}\mu = \frac{1}{n} l^{2} +  2 \int \vert \nabla u \vert^{2} \textnormal{ d}\mu  \\
 &=\frac{1}{n} \left( \int L u \textnormal{ d}\mu \right)^{2} + 2 \int \Gamma (u) \textnormal{ d}\mu.
\end{split}$$ For the second part, observe that a potential $\theta_{t}$ for the velocity field $\nabla\theta_{t}$ corresponding to optimal transport between any two measures $\mu_{0}$ and $\mu_{1}$ in $S_{n}$ must be even, since the measures themselves are even. Further, $\int \Gamma (\theta_{t}) \textnormal{ d}\mu_{t} = \int \vert \nabla\theta_{t} \vert^{2} \textnormal{ d}\mu_{t}$, but the latter quantity equals $\mathscr{W}_{2}^{2}(\mu_{0}, \mu_{1})$ by [@Villani03 Remarks 5.40 (iii), Example 5.42]. Therefore, by the first part, if the displacement interpolation between $\mu_{0}$ and $\mu_{1}$ is contained in $S_{n}$ then the condition of inequality [\[eq: entropiccdkn\]](#eq: entropiccdkn){reference-type="eqref" reference="eq: entropiccdkn"} is satisfied. This establishes the second part of the theorem. ◻
:::

::: rem
As indicated in the Introduction, an affirmative answer to Question [\[qstn: poincare\]](#qstn: poincare){reference-type="ref" reference="qstn: poincare"} for $\mu_{0} = \gamma_{K_{0}}, \mu_{1} = \gamma_{K_{1}}$, for symmetric convex bodies $K_{0}$ and $K_{1}$, would imply the result of Eskenazis--Moschidis ([@EskenazisMoschidis21]).
:::

::: definition
A measure $\mu \in \mathcal{P}(\mathbb{R}^n)$ is said to be *strongly log-concave* if its density with respect to the Gaussian measure $\gamma$ on $\mathbb{R}^n$ exists, and is a log-concave function.
:::

::: exmpl
Let $K$ be a convex body. Then, $\gamma_{K}$ is strongly log-concave because $\frac{\textnormal{ d}\gamma_{K}}{\textnormal{ d}\gamma} = \frac{1}{\gamma(K)} \mathbf 1_{K}$ is a log-concave function.
:::

Returning to our investigation of displacement convexity properties of $S_{n}$, we note that $S_{n}$ itself is displacement convex when $n=1$.

::: thm
The set $S_{1} \subseteq \mathscr{W}_{2}(\mathbb{R})$ is displacement convex. Therefore, in particular, $$e^{-D(\mu_{t} \Vert \gamma)} \geq (1-t) e^{-D(\mu_{0} \Vert \gamma)} + t e^{- D(\mu_{1} \Vert \gamma)},$$ when $\mu_{0}, \mu_{1}$ are even strongly log-concave probability measures.
:::

::: proof
*Proof.* Let $\mu_{0}, \mu_{1} \in S_{1}$. Denote by $T$ the optimal map pushing forward $\mu_{0}$ to $\mu_{1}$ guaranteed by Theorem [\[thm: Brenier\]](#thm: Brenier){reference-type="ref" reference="thm: Brenier"}. Thus, $(T_{t})_{\#}\mu_{0} = \mu_{t}$, $t \in [0,1]$, is the displacement interpolation. Let $f$ be a continuously-differentiable odd function supported within $\textnormal{support}(\mu_{0})$. The main idea is to choose functions $f_{t}$ such that $f'_{t} = f' \circ T_{t}^{-1}$. We let $$f_{t} (x) = \int_{0}^{x} f' (T_{t}^{-1}(y)) \textnormal{ d}y.$$ Therefore, $$\begin{split}
\int \vert f_{t} \vert^{2} \textnormal{ d}\mu_{t} 
&= \int \vert f_{t} (T_{t} (x)) \vert^{2} \textnormal{ d}\mu_{0} (x) = \int \left( \int_{0}^{T_{t}(x)} f' (T_{t}^{-1}(y)) \textnormal{ d}y \right)^{2} \textnormal{ d}\mu_{0} (x) \\
&= \int \left(  \int_{0}^{x} f'(z)T'_{t}(z) \textnormal{ d}z   \right)^{2} \textnormal{ d}\mu_{0}(x) = \int \left( (1-t) \int_{0}^{x} f' + t \int_{0}^{x} f'T' \right)^{2} \textnormal{ d}\mu_{0}, \\
\end{split}$$ which is clearly convex in $t$. Thus, $$\begin{split}
\int \vert  f_{t} \vert^{2} \textnormal{ d}\mu_{t} &\leq (1-t) \int \vert f_{0} \vert^{2} \textnormal{ d}\mu_{0} + t \int \vert f_{1} \vert^{2} \textnormal{ d}\mu_{1}\\
& \leq (1-t) \int \vert f'_{0} \vert^{2} \textnormal{ d}\mu_{0} + t \int \vert f'_{1} \vert^{2} \textnormal{ d}\mu_{1} = \int \vert f'_{t} \vert^{2} \textnormal{ d}\mu_{t},
\end{split}$$ where we have used the fact that the integral $$\int \vert f'_{t} \vert^{2} \textnormal{ d}\mu_{t} = \int \vert f' \circ T_{t}^{-1} \vert^{2} \textnormal{ d}\mu_{t} = \int \vert f' \vert^{2} \textnormal{ d}\mu_{0}$$ remains constant in time $t$. The one-to-one correspondence obtained by the interpolation procedure $f_{t}$ among the test functions supported within each $\textnormal{support}(\mu_{t})$ then concludes the proof of the first assertion. Given the second assertion is about optimal transport between log-concave measures, the regularity of the velocity required to draw the desired conclusion is furnished by Caffarelli's regularity theory ([@Caffarelli90; @Caffarelli92]) and approximation. ◻
:::

For higher dimensions, the fact that not all vector fields are conservative, prevents us from finding the function $f_{t}$ satisfying $\nabla f_{t} = \nabla f \circ T_{t}^{-1}$. Yet, we can derive some partial results.

::: prop
[]{#prop: oneendgaussian label="prop: oneendgaussian"} The following displacement convex subsets of $\mathscr{W}_{2}(\mathbb{R}^n)$ lie completely in $S_{n}$.

1.  The collection of all centered Gaussians whose covariance matrix is dominated by the identity, $\{ ( \Sigma^{1/2} )_{\#} \gamma : 0 < \Sigma \leq I_{n \times n} \} =: S_{n,\mathcal{G}}.$

2.  Geodesic segments $\{ \mu_{t} : t \in [0,1] \}$, when one endpoint is an even strongly log-concave probability measure and the other is $\gamma$ itself.

Moreover, inequality [\[eq: dispcongaussiannok\]](#eq: dispcongaussiannok){reference-type="eqref" reference="eq: dispcongaussiannok"} holds whenever both endpoints lie in any one of these sets.
:::

::: proof
*Proof.* For the first set, use the following facts which are consequences of the Brascamp--Lieb inequality and Theorem [\[thm: Brenier\]](#thm: Brenier){reference-type="ref" reference="thm: Brenier"}.

-   Affine functions are the extremal functions in the Poincaré inequality for Gaussian measures.

-   The collection of the Gaussians considered in the proposition satisfy the Poincaré inequality with constant $1$.

-   The collection of all centered Gaussian measures (that is, all linear images of the standard Gaussian $\gamma$) is a displacement convex set.

We basically prove the convexity of the Poincaré constant in this case. Let $X_{0}, X_{1}$ be random vectors with distributions in the set $S_{n, \mathcal{G}}$. Then their displacement interpolation is represented by a Gaussian random vector $X_{t} = (1-t)X_{0} + t X_{1}$, where $(X_{0},X_{1})$ are optimally coupled. Suppose $f(x) = \langle x, u \rangle$, for some $u \in \mathbb{R}^n$. Then, $$\mathbb{E}f(X_{t})^{2} = \mathbb{E}\langle u , X_{t} \rangle^{2} \leq (1-t) \mathbb{E}\langle u , X_{0} \rangle^{2} + t  \mathbb{E}\langle u , X_{1} \rangle^{2} \leq \vert u \vert^{2} = \mathbb{E}\vert \nabla f (X_{t}) \vert^{2}.$$ This completes the proof of the displacement convexity of the set $S_{n, \mathcal{G}}$. The optimal transport map between Gaussian measures is linear ([@KnottSmith84]), therefore the velocity field has the regularity needed to deduce the inequality [\[eq: dispcongaussiannok\]](#eq: dispcongaussiannok){reference-type="eqref" reference="eq: dispcongaussiannok"} when both endpoints lie in this set.

For the second set, we will use Caffarelli's contraction theorem ([@Caffarelli00]), which says that the optimal map $T$ from $\mu_{0} = \gamma$ to a strongly log-concave measure $\mu_{1}$ is $1$-Lipschitz. Therefore, the $T_{t}$ from Theorem [\[thm: Brenier\]](#thm: Brenier){reference-type="ref" reference="thm: Brenier"} are also $1$-Lipschitz. A standard change of variables argument shows that the Poincaré constant of a $1$-Lipschitz image of $\gamma$ can be at most $1$. This shows that all the $\mu_{t}$ in the second part of the proposition have Poincaré constants $\leq 1$. We use (approximation and) Caffarelli's regularity theory ([@Caffarelli90; @Caffarelli92]) again to obtain the required regularity of velocity fields to deduce inequality [\[eq: dispcongaussiannok\]](#eq: dispcongaussiannok){reference-type="eqref" reference="eq: dispcongaussiannok"}. ◻
:::
