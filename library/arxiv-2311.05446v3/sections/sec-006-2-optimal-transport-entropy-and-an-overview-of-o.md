---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-006-2-optimal-transport-entropy-and-an-overview-of-o
section_title: "Optimal transport, entropy, and an overview of our method"
section_number: 2
pages: 8-13
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.971
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
[]{#sec: overview label="sec: overview"} While the general problem of optimal transport can be posed in a much more abstract setting, we will focus on the setup relevant for our purpose, namely the optimal transport problem in $\mathbb{R}^n$ with quadratic cost. For details beyond the short treatment we present below, the reader is referred to the excellent textbook [@Villani03], especially Chapters 2 and 5.

For $\mu_{0}, \mu_{1} \in \mathcal{P}_{2}(\mathbb{R}^n)$, denote by $\Pi (\mu_{0}, \mu_{1})$ the collection of all couplings between $\mu_{0}$ and $\mu_{1}$. This means, $\Pi (\mu_{0}, \mu_{1})$ consists of probability measures $\pi \in \mathcal{P}(\mathbb{R}^n \times \mathbb{R}^n)$ such that, $$\pi (A \times \mathbb{R}^n) = \mu_{0}(A), \, \pi (\mathbb{R}^n \times B) = \mu_{1}(B),$$ for all Borel sets $A,B \subseteq \mathbb{R}^n$. If $X_{0},X_{1}$ are $\mathbb{R}^n$-valued random vectors with distributions $\mu_{0}, \mu_{1}$, respectively, then $\Pi (\mu_{0}, \mu_{1})$ is the collection of all possible joint distributions for $(X_{0}, X_{1})$.

The optimal transport problem, with quadratic cost, asks to minimize $$I[\pi] = \int  \vert x - y \vert^{2} \textnormal{ d}\pi (x,y),$$ over all $\pi \in \Pi(\mu_{0}, \mu_{1})$. This models the situation where mass distributed according to $\mu_{0}$ in space is to be displaced to mass distributed according to $\mu_{1}$, where $\vert x-y \vert^2$ is the cost of moving a unit mass from the point $x$ to the point $y$. A coupling $\pi$ represents a plan, where the infinitesimal $\textnormal{ d}\pi (x,y)$ is the amount of mass to be moved from $x$ to $y$. The problem then asks to compute the cheapest way to displace $\mu_{0}$ to $\mu_{1}$.

The optimal cost, $$\mathscr{W}_{2}(\mu_{0}, \mu_{1}) = \left( \inf_{\pi \in \Pi (\mu_{0}, \mu_{1})} \int  \vert x - y \vert^{2} \textnormal{ d}\pi (x,y) \right)^{1/2},$$ called the *Wasserstein distance of order $2$* between $\mu_{0}$ and $\mu_{1}$, is in fact a metric on $\mathcal{P}_{2} (\mathbb{R}^n)$. The resulting metric space is called the *$2$-Wasserstein space over $\mathbb{R}^n$*, denoted $\mathscr{W}_{2}(\mathbb{R}^n)$. The Wasserstein space over $\mathbb{R}^n$ is a geodesic space, that is, every two points can be connected by a continuous path $c:[0,1] \to \mathscr{W}_{2}(\mathbb{R}^n)$ such that, $\mathscr{W}_{2}(c(s),c(t)) = \vert t-s \vert \mathscr{W}_{2}(c(0),c(1))$ for any intermediate times $s,t \in [0,1]$. Every optimal coupling $\pi \in \Pi (\mu_{0}, \mu_{1})$ gives rise to a geodesic via $c_{\pi} (t) = (\sigma_{t})_{\#} \pi$, where $\sigma_{t}: (x,y) \mapsto (1-t)x + t y$. Notions related to geodesic-convexity in $\mathscr{W}_{2}(\mathbb{R}^n)$ are given special names, as in the definition below.

::: definition
1.  

2.  A subset $S \subseteq \mathscr{W}_{2}(\mathbb{R}^n)$ is called a *displacement convex set*, if given any two measures $\mu_{0}, \mu_{1} \in S$, $$\Big\{ (\sigma_{t})_{\#}\pi \, : \, \mathscr{W}_{2}^{2} (\mu_{0}, \mu_{1}) = \int \vert x-y \vert^{2} \textnormal{ d}\pi (x,y), t \in [0,1] \Big\} \subseteq S.$$

3.  A map $F: S \to \mathbb{R}\cup \{ + \infty \}$ is called a *displacement convex functional* if the map $t \mapsto F ((\sigma_{t})_{\#}\pi )$ is convex on $[0,1]$, for every $\pi$ such that $\mathscr{W}_{2}^2 (\mu_{0}, \mu_{1}) = \int \vert x-y \vert^{2} \textnormal{ d}\pi (x,y)$. Similarly, $F$ is called *displacement concave* if $-F$ is a displacement convex functional.

4.  If there is a unique constant-speed geodesic $\{ \mu_{t} \}_{t \in [0,1]}$ from $\mu_{0}$ to $\mu_{1}$, then it is called the *displacement interpolation* between $\mu_{0}$ and $\mu_{1}$, and each $\mu_{t}$ is called a *displacement interpolant*.
:::

The geodesically convex subset $\mathcal{P}_{2,ac}(\mathbb{R}^n) \subseteq \mathscr{W}_{2}(\mathbb{R}^n)$ is uniquely geodesic. This is facilitated by a theorem of Brenier ([@Brenier91]), which ensures a unique solution to optimal transport problem if $\mu_{0}$ has density, and describes the structure of the optimal coupling.

::: thm
[@Villani03 Theorem 2.12 (ii)] []{#thm: Brenier label="thm: Brenier"} Let $\mu_{0}, \mu_{1} \in \mathcal{P}_{2}(\mathbb{R}^n)$. If $\mu_{0} \in \mathcal{P}_{2,ac} (\mathbb{R}^n)$ in addition, then there exists a unique convex function $\phi$ such that, $T = \nabla\phi$ pushes forward $\mu_{0}$ to $\mu_{1}$. Moreover, in this case the optimal coupling in the optimal transport problem is unique, and is given by $\pi = \left[ x \mapsto (x, T(x)) \right]_{\#} \mu_{0}$.
:::

The map $T$ in the above theorem is called the *Brenier map from $\mu_{0}$ to $\mu_{1}$*. If the conditions of the above theorem are met, then we can explicitly write the displacement interpolant between $\mu_{0}$ and $\mu_{1}$ as $\mu_{t} = (T_{t})_{\#} \mu_{0}$, where $T_{t} = (1-t) I + t T$ linearly interpolates between the identity map and the Brenier map from $\mu_{0}$ to $\mu_{1}$. This interpolation was introduced in the pioneering work of McCann ([@McCann97]), where the fact that the Jacobian matrix of the *transport maps* $T_{t}$ takes values in the space of positive semidefinite matrices proved to be useful in establishing displacement convexity properties of some important functionals. For example, [@McCann97 Theorem 2.2] contains the following functionals as special cases.

::: exmpl
[]{#exmpl: sbentropy label="exmpl: sbentropy"} The *Shannon--Boltzmann entropy* $h(\mu) = - \int \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}x} \right) \log \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}x} \right) \textnormal{ d}x$ on $\mathcal{P}_{2,ac}(\mathbb{R}^n)$ is displacement concave. In fact, this functional can be meaningfully extended to all of $\mathscr{W}_{2}(\mathbb{R}^n)$ by setting $h(\mu) = - \infty$, when $\mu$ does not have density with respect to the Lebesgue measure.
:::

::: exmpl
[]{#exmpl: renyientropy label="exmpl: renyientropy"} The *exponentiated Rényi entropy* $A(\mu) = e^{\frac{1}{n} h_{(n-1)/n}(\mu)} := \int \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}x} \right)^{1 - \frac{1}{n}} \textnormal{ d}x$ is displacement concave.
:::

Much later, in a considerably broader framework than we need here, Example [\[exmpl: sbentropy\]](#exmpl: sbentropy){reference-type="ref" reference="exmpl: sbentropy"} was strengthened by Erbar, Kuwada, and Sturm ([@ErbarKuwadaSturm15]) in the form below.

::: exmpl
[]{#exmpl: expent label="exmpl: expent"} The exponentiated entropy $e^{h(\mu)/n}$ is displacement concave on $\mathscr{W}_{2}(\mathbb{R}^n)$.
:::

Since $\textnormal{support}(\mu_{t}) \subseteq (1-t) \textnormal{support}(\mu_{0}) + t \textnormal{support}(\mu_{1})$, displacement concavity can be used to obtain sumset inequalities for geometric quantities that admit a variational interpretation in terms of probability measures. For example, if $K \subseteq \mathbb{R}^n$ is a compact set, then $$\sup_{\mu \in \mathcal{P}_{ac}(K)} h(\mu) = \log \textnormal{Vol}_{n} (K), \, \sup_{\mu \in \mathcal{P}_{ac}(K)} A(\mu) = \textnormal{Vol}_{n}(K)^{1/n}.$$ The upper-bounds implicit in both these formulas can be proved by a straightforward application of Jensen's inequality, then one can check that these upper-bounds are attained by the uniform distribution on $K$, leading to the variational expressions above. Suppose $K_{0}$ and $K_{1}$ are compact subsets of $\mathbb{R}^n$. Then, Example [\[exmpl: sbentropy\]](#exmpl: sbentropy){reference-type="ref" reference="exmpl: sbentropy"} implies the $0$-concavity of the Lebesgue measure, while Example [\[exmpl: renyientropy\]](#exmpl: renyientropy){reference-type="ref" reference="exmpl: renyientropy"} and Example [\[exmpl: expent\]](#exmpl: expent){reference-type="ref" reference="exmpl: expent"} imply the (a priori superior) $(1/n)$-concavity of the Lebesgue measure.

In this paper, we appropriately generalize Example [\[exmpl: expent\]](#exmpl: expent){reference-type="ref" reference="exmpl: expent"}. To lift the framework above to deal with an arbitrary reference measure instead of the Lebesgue measure, we now introduce a way to measure entropy with respect to a reference measure.

::: definition
Let $\nu$ be a $\sigma$-additive Borel measure on $\mathbb{R}^n$. We define the following functional on $\mathscr{W}_{2}(\mathbb{R}^n)$, $$D(\mu \Vert \nu) =
\begin{cases}
\int \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}\nu} \right) \log \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}\nu} \right) \textnormal{ d}\nu, & \textnormal{ if } \mu \textnormal{ has density w.r.t. } \nu , \\
+ \infty, & \textnormal{ otherwise, }  \\
\end{cases}$$ called the *relative entropy of $\mu$ with respect to $\nu$*.
:::

::: rem
The relative entropy $D(\mu \Vert \nu)$ is a quantification of how much $\mu$ is "spread out" from the viewpoint of $\nu$. In $\mathbb{R}^n$, we get an absolute measure of spread by looking at negative the amount $\mu$ is spread out from the most spread out measure $\textnormal{Vol}_{n}$, $h( \mu) = - D (\mu \Vert \textnormal{Vol}_{n})$.
:::

Using $D(\cdot \Vert \nu)$, one can obtain a variational formulation of the $\nu$-measure, exactly as in the case of the Shannon--Boltzmann entropy and volume.

::: lem
[]{#lem: numeasureinent label="lem: numeasureinent"} Let $K \subseteq \mathbb{R}^n$ be a compact set, then $$\inf_{\mu \in \mathcal{P}(K)} D (\mu \Vert \nu) = - \log \nu (K),$$ where the supremum is attained by $\nu_{K}$.
:::

::: proof
*Proof.* Let $X$ be an $\mathbb{R}^n$-valued random vector with distribution $\mu \in \mathcal{P}(K)$. Because of the way relative entropy is defined, we only need to consider measures $\mu$ having density, say $f$, with respect to $\nu$. Using Jensen's inequality we obtain, $$- D(\mu \Vert \nu) = - \int f \log f \textnormal{ d}\nu = \mathbb{E} \log \frac{1}{f(X)} \leq \log \mathbb{E} \frac{1}{f(X)} \leq \log \nu (K).$$ The bound is attained when $f$ is constant, that is, when $\mu = \nu_{K}$. This can be verified directly. ◻
:::

Therefore, we have the following general principle formalizing our method.

::: prop
[]{#pro: wand label="pro: wand"} Let $\nu$ be a $\sigma$-finite Borel measure on $\mathbb{R}^n$. Suppose $S \subseteq \mathscr{W}_{2}(\mathbb{R}^n)$ is a displacement convex set containing $\nu_{K}$, for all compact sets in a class $\mathcal{K}$ of compact subsets of $\mathbb{R}^n$. If $e^{- a D(\cdot \Vert \nu)}$ is displacement concave on $S$, $a>0$, then $$\label{eq: wand}
    \nu ((1-t) K_{0} + t K_{1})^{a} \geq (1-t) \nu (K_{0})^{a} + t \nu (K_{1})^{a},$$ for all $K_{0}, K_{1} \in \mathcal{K}$.
:::

::: proof
*Proof.* In the assumed displacement concavity inequality $$e^{-a D(\mu_{t} \Vert \nu )} \geq (1-t) e^{-a D(\mu_{0} \Vert \nu )} + e^{-a D(\mu_{1} \Vert \nu )},$$ we plug in $\mu_{0} = \nu_{K_{0}}, \mu_{1} = \nu_{K_{1}}$. Since $\textnormal{support}(\mu_{t}) \subseteq (1-t)K_{0} + tK_{1}$, we have $e^{-a D(\mu_{t} \Vert \nu )} \leq \nu((1-t)K_{0} + tK_{1})^{a}$ which concludes the proof. ◻
:::

::: rem
When $e^{-a D(\cdot \Vert \nu)}$, $a>0$, is displacement concave on all of $\mathscr{W}_{2}(\mathbb{R}^n)$, we get the $a$-concavity of the measure $\nu$. In this case, the converse is also true thereby extending Borell's characterization (Theorem [\[thm: Borell\]](#thm: Borell){reference-type="ref" reference="thm: Borell"}). This is contained, rather implicitly, in the work of Erbar, Kuwada, and Sturm ([@ErbarKuwadaSturm15]). The corresponding statement for $a=0$, namely the equivalence between displacement convexity of $D(\cdot \Vert \nu)$ and log-concavity of $\nu$, had been known earlier (see, for example [@AmbrosioGigliSavare08 Theorem 9.4.11]).
:::

::: rem
[]{#rem: cdhistory label="rem: cdhistory"} The displacement concavity property of $e^{-a D(\cdot \Vert \nu)}$ on $\mathscr{W}_{2}(\mathbb{R}^n)$, in the language of [@ErbarKuwadaSturm15], is called the *entropic $CD(0,1/a)$ condition* for the metric measure space $(\mathbb{R}^n, \Vert \cdot \Vert_{2}, \nu)$. In this expression, "CD" stands for *curvature-dimension*. Given that a Riemannian manifold (equipped with its volume measure) has Ricci curvature bounded below by some $\kappa \in \mathbb{R}$ and its dimension is at most $n$, several geometric and functional inequalities (in terms of $\kappa$ and $n$) follow. The curvature-dimension condition for Markov diffusions, introduced in the work of Bakry--Émery [@BakryEmery85], allows one to define the notion of "Ricci curvature bounded below by $\kappa$, dimension bounded above by $n$" for weighted Riemannian manifolds (that is, Riemannian manifolds equipped with a measure that is not necessarily the volume measure) admitting consequences akin to the non-weighted case. On the other hand, starting from the work of McCann [@McCann97], through the papers of Otto--Villani [@OttoVillani00], Cordero-Erausquin--McCann--Schmuckenschläger [@Cordero-ErasquinMcCannSchmuckenschlager01], it was eventually established in the work of von Renesse--Sturm [@vonRenesseSturm05] that the "Ricci curvature bounded below by $\kappa$" condition on weighted Riemannian manifolds could equivalently be described using the displacement $\kappa$-convexity of relative entropy on the $2$-Wasserstein space over the Riemannian manifold. In the landmark papers of Sturm [@{Sturm06(i)}; @{Sturm06(ii)}] and Lott--Villani [@LottVillani09], not only were dimensional considerations added (using Rényi entropy) to complete the picture on the displacement convexity-based alternative to the Bakry--Émery approach to curvature-dimension in the weighted Riemannian setting, but the natural extension of this theory to a wide class of metric measure spaces was established and explored. In the setting of (*infinitesimally Hilbertian*) metric measure spaces, the equivalence between the two approaches was established by Erbar--Kuwada--Sturm [@ErbarKuwadaSturm15], in which the authors introduce and study the *$(\kappa , n)$-convexity* (see Definition [\[def: knconvexity\]](#def: knconvexity){reference-type="ref" reference="def: knconvexity"}) of relative entropy on Wasserstein space. Particularly, in the setting of the Euclidean space equipped with a measure $\textnormal{ d}\nu = e^{-V} \textnormal{ d}x$, the $(\kappa, n)$-convexity of $D(\cdot \Vert \nu)$ on $\mathscr{W}_{2}(\mathbb{R}^n)$ is equivalent to the $CD(\kappa,n)$ condition defined in terms of the displacement convexity of (relative) Rényi entropy (perhaps better known as Rényi divergence among information theorists), which is further equivalent to the Bakry--Émery definition of $CD(\kappa, n)$ condition for the Markov semigroup generated by $Lf = \Delta f - \langle \nabla V , f \rangle$. However, such equivalences need not hold over specific choices of Wasserstein geodesics. In the present work, our choice of using exponentiated relative entropy instead of the exponentiated Rényi divergence plays a key role.
:::

Sometimes, to prove the displacement convexity properties of certain functionals it is useful to take an "Eulerian viewpoint". For $\mu_{0}, \mu_{1} \in \mathcal{P}_{2,ac} (\mathbb{R}^n)$, consider the transport maps $T_{t}$ as in the discussion preceding Example [\[exmpl: sbentropy\]](#exmpl: sbentropy){reference-type="ref" reference="exmpl: sbentropy"}. The previous description of the maps $T_{t}$ expresses the displacement in terms of the particle trajectories $T_{t}(x)$, of each particle $x$; this is the "Lagrangian viewpoint". One can equivalently describe the displacement in terms of a time-dependent vector field $v_{t}$ such that, $$v_{t} ( T_{t}(x)) = \frac{\textnormal{ d}}{\textnormal{ d}t} T_{t} (x).$$ The reason why $v_{t}$ can be defined in the above manner is that trajectories in optimal transport do not cross (in an almost-everywhere sense). Further, an argument based on the dominated convergence theorem leads to the *continuity equation*, $$\label{eq: continuityeqn}
\frac{\textnormal{ d}}{\textnormal{ d}t} \int \phi \textnormal{ d}\mu_{t} = \int \langle \nabla\phi , v_{t} \rangle \textnormal{ d}\mu_{t},$$ for all test functions $\phi$. It can be shown that $v_{t}$ is of the form $\nabla\theta_{t}$, and $\theta_{t}$ satisfies a Hamilton--Jacobi equation in the weak sense, $$\label{eq: HamiltonJacobi}
\frac{\partial \theta_{t} }{\partial t} + \frac{\vert \nabla\theta_{t} \vert^{2}}{2} = 0.$$ Roughly speaking, the fact that $v_{t}$ is a gradient field follows from Brenier's theorem and semigroup properties of optimal transport, while the Hamilton--Jacobi equation is a consequence of $T_{t}$ carrying each particle along a straight line. For more details, the reader is referred to [@Villani03 Section 5.4].
