---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-016-44-the-holonomy-yang-baxter-equation
section_title: "The holonomy Yang-Baxter equation"
section_number: 4.4
pages: 17-23
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.986
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:braid groupoids label="sec:braid groupoids"}

Next we show our $R$-matrices satisfy braid relations. We discuss how to use these braid relations to define tangle and link invariants in [@McPhailSnyderVolume], extending [@Kashaev2005]. The holonomy $R$-matrix satisfies a *family* of braid relations parametrized by all admissible choices of colors, which have a natural interpretation in terms of flat $\sla$ connections on the braid complement, equivalently representations of the fundamental group of the complement into $\slg$. Our matrices depend on an additional local choice of log-coloring whose geometric meaning is less clear. However, it turns out that they depend only on certain quantities derived from the log-coloring which have an interpretation in terms of the holonomy of the longitude. These are discussed in detail in [@McPhailSnyderVolume]; here we say just enough to prove the braid relation.

::: definition
[]{#def:RIII-admissible label="def:RIII-admissible"} Choosing characters $\hat \chi_{1}, \hat \chi_{2}, \hat \chi_{3} \in \Wcharhat$ for the top segments determines a $\chi$-coloring of the $\operatorname{R3}$ diagrams in [1](#fig:RIII-before-and-after-chis){reference-type="ref" reference="fig:RIII-before-and-after-chis"}. We say the $\chi$-coloring is if both colorings are admissible. We say that log-colorings for each diagram are if the log-parameters for the boundary regions and segments agree and $\beta + \beta'' = \beta' + \tilde{\beta}'$ (in the notation of [2](#fig:RIII-before-and-after-middle){reference-type="ref" reference="fig:RIII-before-and-after-middle"}).
:::

<figure id="fig:RIII-before-and-after-chis">

<figcaption> <span class="math inline"><em>χ</em></span>-colorings of the braid diagrams occurring in an <span class="math inline">R3 </span> move. </figcaption>
</figure>

<figure id="fig:RIII-before-and-after-middle">

<figcaption> A log-colored <span class="math inline">R3 </span> move is allowed when the log-parameters of the boundary regions and segments are the same on both sides and additionally <span class="math inline"><em>β</em> + <em>β</em>″ = <em>β</em>′ + <em>β̃</em>′</span>. This ensures that the log-longitudes of each component are preserved. </figcaption>
</figure>

This condition has a geometric meaning. Recall that the parameter $m$ of a color $\chi = (a, b, m)$ represents a distinguished eigenvalue of the associated meridian holonomy $\psi(\chi) \in \slg$. For a $\chi$-colored link diagram this choice gives an associated longitude eigenvalue $\ell$ [@McPhailSnyder2022] for each component; the choice of $(m, \ell)$ versus $(m^{-1}, \ell^{-1})$ is called a . A log-coloring determines a logarithm $\mu$ of $m = e^{2\pi i \mu}$ and also a logarithm $\lambda$ of $\ell  = e^{2 \pi i \lambda}$ by taking a certain signed sum of segment log-parameters $\beta_{i}$. These definitions can be extended to tangles like those in [2](#fig:RIII-before-and-after-middle){reference-type="ref" reference="fig:RIII-before-and-after-middle"}, and we call the choice of $(\mu, \lambda)$ for each component of the tangle a . General definitions and more details are given in [@McPhailSnyderVolume]. Here it suffices to consider the condition in [\[def:RIII-admissible\]](#def:RIII-admissible){reference-type="ref" reference="def:RIII-admissible"}, which asserts that the log-decorations on both sides of the $\operatorname{R3}$ move are the same.

::: theorem
[]{#thm:RIII label="thm:RIII"} Fix any $\operatorname{R3}$-admissible $\chi$-colorings and compatible log-colorings of the diagrams $D, D'$ in [1](#fig:RIII-before-and-after-chis){reference-type="ref" reference="fig:RIII-before-and-after-chis"}. By assigning the holonomy braidings of [\[def:R-mat\]](#def:R-mat){reference-type="ref" reference="def:R-mat"} to the crossings of the diagrams in [1](#fig:RIII-before-and-after-chis){reference-type="ref" reference="fig:RIII-before-and-after-chis"} we obtain $\mathcal{U}_{\xi}$-module intertwiners $$\mathcal{J}_{\xi}(D)
    ,
    \mathcal{J}_{\xi}(D')
    :
    \rep{\hat{\chi}_{1}}
    \otimes
    \rep{\hat{\chi}_{2}}
    \otimes
    \rep{\hat{\chi}_{3}}
    \to
    \rep{\hat{\chi}_{3''}}
    \otimes
    \rep{\hat{\chi}_{2''}}
    \otimes
    \rep{\hat{\chi}_{1''}}$$ Then the holonomy $R$-matrices satisfy braid relations in the sense that $\mathcal{J}_{\xi}(D) = \mathcal{J}_{\xi}(D')$.
:::

<figure id="fig:RIII-colored-together">

<figcaption> Invariance under <span class="math inline">R3 </span> moves follows from showing that <span class="math inline">𝒥<sub><em>ξ</em></sub></span> is the identity map on this diagram for every choice of coloring and any log-coloring with trivial log-decoration and matching values on the boundary. A coloring of the whole diagram is determined by the choice of colors <span class="math inline"><em>χ</em><sub>1</sub>, <em>χ</em><sub>2</sub>, <em>χ</em><sub>3</sub></span> on the top. </figcaption>
</figure>

The rest of this section is devoted to the proof of this theorem. It is convenient to instead prove that $$\mathcal{J}_{\xi}(D_{\operatorname{R3}}) : 
  \rep{\hat{\chi}_{1}}
  \otimes
  \rep{\hat{\chi}_{2}}
  \otimes
  \rep{\hat{\chi}_{3}}
  \to
  \rep{\hat{\chi}_{1}}
  \otimes
  \rep{\hat{\chi}_{2}}
  \otimes
  \rep{\hat{\chi}_{3}}$$ is the identity map, where $D_{\operatorname{R3}}$ is the diagram of [3](#fig:RIII-colored-together){reference-type="ref" reference="fig:RIII-colored-together"} with a $\chi$-coloring and log-coloring derived from $D$ and $D'$ in the obvious way. The compatibility condition on the log-parameters of the boundary regions and segments is given in [4](#fig:RIII-log-parameters){reference-type="ref" reference="fig:RIII-log-parameters"}. [\[thm:RIII\]](#thm:RIII){reference-type="ref" reference="thm:RIII"} is equivalent to the claim that $\mathcal{J}_{\xi}(D_{\operatorname{R3}})$ is the identity map for any choice of log-parameters for the internal regions and segments as long as the log-decoration condition $$\label{eq:RIII beta condition}
  \beta_{2} - \beta_{2'} + \beta_{2''} - \beta_{2'''} = 0$$ is satisfied.

<figure id="fig:RIII-log-parameters">

<figcaption> We require the log-parameters of the boundary regions and segments to be compatible as shown. We allow any choice of internal log-parameters as long as <span class="math inline"><em>β</em><sub>2</sub> − <em>β</em><sub>2′</sub> + <em>β</em><sub>2″</sub> − <em>β</em><sub>2‴</sub> = 0</span>. </figcaption>
</figure>

To prove [\[thm:RIII\]](#thm:RIII){reference-type="ref" reference="thm:RIII"} we need to show the space of allowed log-colorings of $D_{\operatorname{R3}}$ is connected. Consider first the space $A_{3}^{0}$ of $\operatorname{R3}$-admissible triples of colors $(\chi_{1}, \chi_{2}, \chi_{3})$ and set $$A_3 = A_3^0 \times ( \mathbb{C} \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}   ).$$ (the last factor is for keeping track of $e^{2 \pi i \gamma}$). Let $\widetilde{A}_3$ be the set of points $$(\gamma, \alpha_1, \alpha_2, \alpha_3, \beta_1, \beta_2, \beta_3, \mu_1, \mu_2, \mu_3)
  \in \mathbb{C}^{10}$$ such that if we set $$\begin{aligned}
  \chi_j =
  \left(
    e^{2\pi i \alpha_{j}}, 
    e^{2\pi i \beta_j},
    e^{2\pi i \mu_j}
  \right)
  \text{ for \(j = 1, 2, 3\) and }
  r = e^{2\pi i \gamma}
\end{aligned}$$ then $(\chi_1, \chi_2, \chi_3, r) \in A_3$.

::: lemma
$\widetilde{A}_{3}$ is path-connected.
:::

::: proof
*Proof.* $A_3$ is obtained by removing finitely many algebraic hypersurfaces from $\mathbb{C}^{10}$, so it is path-connected. $\widetilde{A}_{3}$ is a covering space of $A_{3}$ built by repeatedly taking covers of the same type as the connected infinite cyclic cover $$\zeta \mapsto \exp(2\pi i \zeta) , \mathbb{C}\to \mathbb{C}\setminus \left\{ \def\given{\ \middle| \ }  0 \right\}$$ occurring as the Riemann surface of the complex logarithm, so $\widetilde{A}_3$ is path-connected as well. ◻
:::

::: lemma
[]{#thm:DR3-well-defined label="thm:DR3-well-defined"} $\mathcal{J}_{\xi}(D_{\operatorname{R3}})$ is a well-defined, matrix-valued function on $\widetilde{A}_{3}$.
:::

::: proof
*Proof.* Suppose $\mathfrak{f}$ is a log-coloring of an admissible $\chi$-coloring $\chi$ of $D_{\operatorname{R3}}$. Let $\mathfrak{f}'$ be another log-coloring with the same log-parameters on the boundary as $\mathfrak{f}$. Set $$\lambda
    =
    \beta_{2} - \beta_{2'} + \beta_{2''} - \beta_{2'''} = 0$$ where the $\beta_{i}$ are the segment parameters of $\mathfrak{f}$, and similarly define $\lambda'$ for $\mathfrak{f}'$. We show that $$\label{eq:jfunc-longitude-dep}
    \jfunc(D_{\operatorname{R3}}, \chi, \mathfrak{f})
    =
    \omega^{- (\lambda' - \lambda)\mu_{2}}
    \jfunc(D_{\operatorname{R3}}, \chi, \mathfrak{f})$$ This is a special case of a more general transformation rule given in [@McPhailSnyderVolume]. In particular if $\mathfrak{f}$ and $\mathfrak{f}'$ are $\operatorname{R3}$-compatible log-colorings corresponding to the same point of $\widetilde{A}_{3}$ then $\lambda = \lambda' = 0$, so $\jfunc(D_{\operatorname{R3}}, \chi, \mathfrak{f})
    =
    \jfunc(D_{\operatorname{R3}}, \chi, \mathfrak{f})$ as claimed.

The linear map $\jfunc$ has an explicit description as a state-sum: each segment of $D_{\operatorname{R3}}$ is associated the $\mathcal{U}_\xi$-module $\rep{\alpha, \beta, \mu}$ with log-parameters determined by $\mathfrak{f}$. These log-parameters determine a basis $\left\{ \def\given{\ \middle| \ }  \vbh{n} | n \in \mathbb{Z}/N\mathbb{Z} \right\}$ of each module and $R$-matrices associated to each crossing, and the action of $\jfunc(D, \chi, \mathfrak{f})$ is given by summing over all internal indices.

Consider a region of $D_{\operatorname{R3}}$ with log-parameter $\gamma$. By [\[thm:R-matrix transformation\]](#thm:R-matrix transformation){reference-type="ref" reference="thm:R-matrix transformation"}, changing the value of $\gamma$ to $\gamma + k$ changes each of the $R$-matrices adjacent to the region. There are two changes to understand: one depending on the segment index and one global. For the first factor, observe that in the state-sum defining $\jfunc(D, \chi, \mathfrak{f})$ the sum for a segment $i$ adjacent to the region with parameter $\gamma$ picks up a factor of the form $$\omega^{ \pm n_i (k - k)} = 1$$ where $n_i$ is the index assigned to the segment. Here the two factors of $k$ are from the crossings on each side of the segment. As the signs of the $n_i k_j$ terms in [\[eq:R-matrix transformation:gamma\]](#eq:R-matrix transformation:gamma){reference-type="ref" reference="eq:R-matrix transformation:gamma"} depend only on whether the segment is incoming or outgoing these always cancel as claimed.

The second global factor is more geometric. Suppose our region is adjacent to crossings $1, \dots, p$. Each corner corresponds to an ideal tetrahedron of orientation $\epsilon_i$, and the term $\Gamma$ in [\[eq:R-matrix transformation:gamma\]](#eq:R-matrix transformation:gamma){reference-type="ref" reference="eq:R-matrix transformation:gamma"} says that the state-sum has a global change by $$\omega^{\frac{k}{2}( \epsilon_{1} \zeta_i^0 + \epsilon_2 \zeta_2^0 + \cdots  + \epsilon_p \zeta_p^0)}.$$ Our claim follows from showing that $$\label{eq:edge-flattening}
    \epsilon_{1} \zeta_i^0 + \epsilon_2 \zeta_2^0 + \cdots  + \epsilon_p \zeta_p^0 = 0.$$ This is the logarithmic gluing equation of the edge of the octahedral decomposition lying in this region: saying that it holds is part of the claim that the parameters of [\[eq:flattening-N,eq:flattening-W,eq:flattening-S,eq:flattening-E\]](#eq:flattening-N,eq:flattening-W,eq:flattening-S,eq:flattening-E){reference-type="ref" reference="eq:flattening-N,eq:flattening-W,eq:flattening-S,eq:flattening-E"} define a flattening. One can confirm [\[eq:edge-flattening\]](#eq:edge-flattening){reference-type="eqref" reference="eq:edge-flattening"} by following the same argument as in the proof of [@McPhailSnyder2022 Theorem 3.2]; see also [@McPhailSnyder2022 Figure 13].

Now consider the effect of changing a segment log-parameter $\beta$ with associated index $n$. Changing from $\beta$ to $\beta + l$ picks up index shifts in both adjacent $R$-matrices, which cancel, and also picks up a factor involving $\gamma$s and $\mu$s. The $\gamma$ terms always cancel segment-by-segment. The $\mu$ terms for the log-parameters of components $1$ and $3$ always cancel as well, while for component $2$ an analysis of the relative signs gives [\[eq:jfunc-longitude-dep\]](#eq:jfunc-longitude-dep){reference-type="ref" reference="eq:jfunc-longitude-dep"}. ◻
:::

::: lemma
[]{#thm:scalar-lemma label="thm:scalar-lemma"} There is a continuous function $\Upsilon : \widetilde A_3 \to \mathbb{C}^{\times}$ such that $$\label{eq:Upsilon-def}
    \jfunc(D_{\operatorname{R3}}, \widetilde a) = \Upsilon(\widetilde a) \mathop{\mathrm{id}}$$ for each $\widetilde a \in \widetilde A_3$.
:::

::: proof
*Proof.* Recall from [\[thm:R-matrix-exists\]](#thm:R-matrix-exists){reference-type="ref" reference="thm:R-matrix-exists"} that the $R$-matrices defining $\jfunc$ are characterized up to a scalar as intertwiners of the outer $R$-matrix $\mathcal{R}$ (an algebra automorphism). Because $\mathcal{R}$ satisfies a colored Yang-Baxter equation the $R$-matrices do as well, at least up to a scalar. This scalar is $\Upsilon$, and because $\jfunc$ is continuous it must be as well. ◻
:::

::: lemma
[]{#thm:cocyle-condition label="thm:cocyle-condition"} For any $\widetilde{a} \in \widetilde{A}_{3}$ $$\det \jfunc(D_{\operatorname{R3}}, \widetilde a) = \pm 1
    .\qedhere$$
:::

::: proof
*Proof.* The determinant of $\jfunc(D_{\operatorname{R3}}, \widetilde a)$ is the product of the determinants of braidings for each of the $6$ crossings raised to the $N$th power. It thus suffices to show that the product of these determinants is $\pm 1$. In [\[thm:R-mat-det\]](#thm:R-mat-det){reference-type="ref" reference="thm:R-mat-det"} we showed that the determinant of the braiding at a log-colored crossing $c$ of sign $\epsilon$ is $$\det \tau R
    =
    C^{\epsilon N^2}
    \left[
      e^{\pi i (\gamma_{\lW} - \gamma_{\lE}) }
      e^{2\pi i(\lambda_{1} + \lambda_{2})}
      e^{4\pi i \epsilon(\mu_{1} + \mu_{2})}
    \right]^{N(N-1)}
    e^{- NI(c) / 2\pi i}
    .$$ There are $5$ factors in the determinant:

1.  $C = N/\df{0}^2 = N\exp\left( -2 N^{-1} \sum_{k=0}^{N-1} k \log(1 - \omega^{k}) \right)$ is a constant depending only on $N$,

2.  $\gamma_{\lE}$, $\gamma_{\lW}$ are two of the region log-parameters at the crossing,

3.  $\mu_1$ and $\mu_{2}$ are the log-meridians of the two components at the crossing,

4.  $\lambda_{1}$ and $\lambda_{2}$ are the contributions of the crossing to the log-longitude, and

5.  $I(c)$ is a sum of four dilogarithms.

We can check by elementary methods that the product of terms 1, 2, and 3 over $D_{\operatorname{R3}}$ is $1$. The product of term $4$ over the diagram is $1$ because of our assumption that the total log-longitudes in our log-coloring are $0$. Dealing with the remaining term $5$ is more complicated: the fact that it gives $\pm 1$ is a consequence of the fact that the complex Chern-Simons invariant is well-defined and given by Neumann's sum of lifted dilogarithms [@Neumann2004]; algebraically, this is because the lifted dilogarithm obeys a $5$-term relation. A definition of the complex Chern-Simons invariant for tangles and a detailed proof of invariance is given in [@McPhailSnyderVolume], and this implies that the product of term $5$ over the diagram is $\pm 1$ as claimed. ◻
:::

::: proof
*Proof of [\[thm:RIII\]](#thm:RIII){reference-type="ref" reference="thm:RIII"}.* We need to show that $\Upsilon = 1$ uniformly. Taking the determinant of both sides of [\[eq:Upsilon-def\]](#eq:Upsilon-def){reference-type="ref" reference="eq:Upsilon-def"} and applying [\[thm:cocyle-condition\]](#thm:cocyle-condition){reference-type="ref" reference="thm:cocyle-condition"} shows $$\det \jfunc(D_{\operatorname{R3}}, \widetilde{a})
    =
    \Upsilon(\widetilde{a})^{N^3}
    =
    \pm 1$$ for every $\widetilde{a} \in \widetilde{A}_3$. We conclude that $\Upsilon$ takes values in the discrete set $$\left\{ \def\given{\ \middle| \ }  w \in \mathbb{C}\given w^{N^3} = -1 \right\}$$ of $N^3$th roots of $-1$. Thus $\Upsilon$ is a discrete-valued, continuous function on a connected space, so it must be constant. To show that this constant is $1$ we simply need to check that $\Upsilon(\widetilde{a}_0) = 1$ for some $\widetilde{a}_0 \in \widetilde{A}_3$.

We choose a point $\widetilde{a}_{0}$ defining the Kashaev invariant. The underlying $\chi$-coloring of $\widetilde{a}_0$ has $\chi_1 = \chi_3 = (-1,1,-1)$ and $\chi_2 = (-1,-1,-1)$. To get a point of $\widetilde{A}_3$ we need to choose (part of) a log-coloring. With the labeling of [4](#fig:RIII-log-parameters){reference-type="ref" reference="fig:RIII-log-parameters"} we set $\mu_1, \mu_2, \mu_3 = -1/2$, $\gamma_0 = 0$, $\alpha_1 = \alpha_2 = \alpha_3 = -1/2$, $\beta_1 = 0$, $\beta_2 = -1/2$, and $\beta_3 = -1$.

We want to compute $\jfunc(D_{\operatorname{R3}}, \widetilde{a}_0)$. To do so we need to choose a log-coloring of the internal segments and regions of the diagram. Because all the crossings are pinched is is simplest to choose a *standard* log-coloring as in [\[eq:standard-flattening\]](#eq:standard-flattening){reference-type="ref" reference="eq:standard-flattening"}. This is possible because of our choices of $\beta_1, \beta_2, \beta_3$ above. Choosing a standard log-coloring also ensures we satisfy [\[eq:RIII beta condition\]](#eq:RIII beta condition){reference-type="ref" reference="eq:RIII beta condition"}. By [\[thm:R-mat-pinched\]](#thm:R-mat-pinched){reference-type="ref" reference="thm:R-mat-pinched"} (alternatively by [\[thm:pinched-R-matrix-dual\]](#thm:pinched-R-matrix-dual){reference-type="ref" reference="thm:pinched-R-matrix-dual"}) the $R$-matrices in our diagram are all the same as the $R$-matrix defining the Kashaev invariant. This matrix is well-known to satisfy the braid relation exactly, so we conclude that $\jfunc(D_{\operatorname{R3}}, \widetilde{a}_0) = \mathop{\mathrm{id}}$ and $\Upsilon(\widetilde{a}_0) = 1$. ◻
:::
