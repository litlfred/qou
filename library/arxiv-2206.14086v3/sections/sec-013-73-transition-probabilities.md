---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-013-73-transition-probabilities
section_title: "Transition probabilities"
section_number: 7.3
pages: 10-12
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
text_source: latex
latex_prose_ratio: 0.696
latex_coverage_ratio: 0.988
---
[]{#sec:Bethe label="sec:Bethe"}

We mentioned in Subsection [\[sec:integrablemethod\]](#sec:integrablemethod){reference-type="ref" reference="sec:integrablemethod"} that one way of proving a KPZ limit theorem for the TASEP is to compute the transition probabilities explicitly and then take an appropriate sum to find the finite-time distribution functions. The summation part is often more technical, but here we discuss the transition probabilities to see how [\[eq:Betheeqlimit\]](#eq:Betheeqlimit){reference-type="eqref" reference="eq:Betheeqlimit"} arises.

Suppose that there are only $N$ particles for the TASEP on $\mathbb{Z}$. Let $\mathcal{W}_N= \{ (a_1, \cdots, a_N)\in \mathbb{Z}^N: a_1<\cdots< a_N\}$ be the ordered set of the particle locations. Schütz [@Schutz97] showed that $$\label{eq:tranpro}
    \mathrm{P}_{Y}(X; t) =  \det \left[ \frac1{2\pi \mathrm{i}} \oint s^{j-i+1}(s+1)^{-x_i+y_j+i-j} e^{ts} \mathrm{d}s \right]_{i,j=1}^N$$ for $X$ and $Y$ in $\mathcal{W}_N$, where the contour is a circle that encloses the points $s=0,-1$.

For the periodic TASEP, the particle locations can be represented by the set $$\mathcal{W}_N^L=  \{ (a_1, \cdots, a_N)\in \mathbb{Z}^N: a_1<\cdots< a_N <a_1+L\} .$$ Note that if we consider the TASEP on a ring, this set keeps track of global circulations of the particles.

We showed in [@Baik-Liu18] that $$\label{eq:transprofper}
    \mathrm{P}_{Y}(X; t) = \oint \det \left[ \frac1{L} \sum_{w} \frac{w^{j-i+1}(w+1)^{-x_i+y_j+i-j} e^{tw}}{w+N/L} \right]_{i,j=1}^N  \frac{\mathrm{d}z}{2\pi \mathrm{i}z}$$ for $X, Y\in \mathcal{W}_N^L$, where the integral contour for $z$ is any circle enclosing the origin, and the sum inside is over the roots of the equation $$\label{eq:Betheequation}
    w^N (w+1)^{L-N}=z .$$ See Figure [1](#fig:Betheroots){reference-type="ref" reference="fig:Betheroots"}.

<figure id="fig:Betheroots">
<embed src="Roots1b.pdf" style="width:3cm" />
<embed src="Roots2b.pdf" style="width:3cm" />
<embed src="Roots3b.pdf" style="width:3cm" />
<figcaption>Bethe roots when <span class="math inline"><em>L</em> = 24</span> and <span class="math inline"><em>N</em> = 8</span> for three values of <span class="math inline"><em>z</em></span></figcaption>
</figure>

We now explain the equation [\[eq:Betheequation\]](#eq:Betheequation){reference-type="eqref" reference="eq:Betheequation"}. Due to the periodicity, if $A=(a_1, \cdots, a_N)$ is in $\mathcal{W}_N(L)$, then $A'=(a_2, \cdots, a_N, a_1+L)$ also represents the same particle configuration of the periodic TASEP. Thus, the transition probability should remain the same if we replace $(x_1, \cdots, x_N)$ and $(y_1, \cdots, y_N)$ by $(x_2, \cdots, x_N, x_1+L)$ and $(y_2, \cdots, y_N, y_1+L)$, respectively. We can check directly that the determinant in [\[eq:transprofper\]](#eq:transprofper){reference-type="eqref" reference="eq:transprofper"} is unchanged thanks to the equation [\[eq:Betheequation\]](#eq:Betheequation){reference-type="eqref" reference="eq:Betheequation"}. Equation [\[eq:Betheequation\]](#eq:Betheequation){reference-type="eqref" reference="eq:Betheequation"} takes care of the labeling ambiguity in the periodic case. Here the variable $z$ could have been any fixed constant, but making it as a free parameter turns out to be the right choice. Since [\[eq:tranpro\]](#eq:tranpro){reference-type="eqref" reference="eq:tranpro"} and [\[eq:transprofper\]](#eq:transprofper){reference-type="eqref" reference="eq:transprofper"} were found by solving the Kolmogorov forward equation using the Bethe ansatz method, the roots of [\[eq:Betheequation\]](#eq:Betheequation){reference-type="eqref" reference="eq:Betheequation"} are called the Bethe roots.

Now, if we set $L=2N$, $w= -\frac12 + \frac{s}{2\sqrt{2N}}$, and $z= (-4)^{-N} \zeta$ in [\[eq:Betheequation\]](#eq:Betheequation){reference-type="eqref" reference="eq:Betheequation"}, and let $N\to \infty$, then the equation becomes $e^{-s^2/2}=\zeta$, which is [\[eq:Betheeqlimit\]](#eq:Betheeqlimit){reference-type="eqref" reference="eq:Betheeqlimit"}.

# Integrable differential equations {#sec:integrableDE}

Distribution functions of the KPZ fixed point have connections to deterministic integrable differential equations. As proved in 1994 [@Tracy-Widom94], the Tracy-Widom distribution is expressible in terms of the Painlevé II equation, one of a family of six special nonlinear ordinary differential equations [@Fokas-Its-Kitaev-Novokshenov06]. The papers [@Tracy-Widom03; @Adler-van_Moerbeke05; @Wang08a; @Bertola-Cafasso-2012b; @Quastel-Remenik19b] also found differential equations for equal-time, multi-position distribution functions of the KPZ fixed point. We state the following result for multi-point distributions for both infinite and periodic domains.

Define the parameters $$\mathsf{t}_i= \tau_i/3, 
    \qquad \mathsf{y}_i=\gamma_i, 
    \qquad \mathsf{x}_i= \mathsf{h}_i,$$ and let $$\partial_{\mathsf{t}}= \sum_{i=1}^m \partial_{\mathsf{t}_i}, \qquad
    \partial_{\mathsf{y}}= \sum_{i=1}^m \partial_{\mathsf{y}_i}, \qquad
    \partial_{\mathsf{x}}= \sum_{i=1}^m \partial_{\mathsf{x}_i}.$$

::: theorem
[]{#thm:mKdV label="thm:mKdV"} Let $\mathsf{K}=\mathsf{K}_\zeta$ be the operator in either [\[eq:KPZformula\]](#eq:KPZformula){reference-type="eqref" reference="eq:KPZformula"} or [\[eq:PKPZformula\]](#eq:PKPZformula){reference-type="eqref" reference="eq:PKPZformula"}. If $\det(\mathsf{1}- \mathsf{K})\neq 0$, which holds for all but at most countably many parameters, then $$\partial^2_{\mathsf{x}} \log \det(\mathsf{1}- \mathsf{K}) = - \mathsf{r}^T\mathsf{p}$$ for complex-valued $m\times 1$ vector functions $\mathsf{p}(\mathsf{t}, \mathsf{y}, \mathsf{x})$ and $\mathsf{r}(\mathsf{t}, \mathsf{y}, \mathsf{x})$ which satisfy the equations $$\label{eq:NLS}
    \partial_{\mathsf{y}} \mathsf{p}= \frac12 \partial_{\mathsf{x}}^2 \mathsf{p}-  \mathsf{p}\mathsf{r}^T \mathsf{p}, \qquad
    \partial_{\mathsf{y}} \mathsf{r}= -\frac12 \partial_{\mathsf{x}}^2 \mathsf{r}+  \mathsf{r}\mathsf{p}^T \mathsf{r}$$ and $$\label{eq:mKdV}
    \partial_{\mathsf{t}} \mathsf{p}+ \partial_{\mathsf{x}}^3 \mathsf{p}- 3 (\partial_{\mathsf{x}} \mathsf{p}) \mathsf{r}^T \mathsf{p}- 3 \mathsf{p}\mathsf{r}^T (\partial_{\mathsf{x}} \mathsf{p}) =0 , \quad
    \partial_{\mathsf{t}} \mathsf{r}+ \partial_{\mathsf{x}}^3 \mathsf{r}- 3  (\partial_{\mathsf{x}} \mathsf{r}) \mathsf{p}^T \mathsf{r}-  3 \mathsf{r}\mathsf{p}^T (\partial_{\mathsf{x}} \mathsf{r}) =0.$$
:::

Equation [\[eq:mKdV\]](#eq:mKdV){reference-type="eqref" reference="eq:mKdV"} is a coupled system of vector-valued modified Korteweg-De Vries (mKdV) equations. The scalar mKdV equation is $\partial_{\mathsf{t}} f + \partial_{\mathsf{x}}^3 f - 6 (\partial_{\mathsf{x}} f) f^2  =0$. On the other hand, equation [\[eq:NLS\]](#eq:NLS){reference-type="eqref" reference="eq:NLS"} forms a coupled system of vector-valued nonlinear forward and backward heat equations. They become vector-valued nonlinear Schödinger (NLS) equations if we change $\mathsf{y}_i\mapsto \mathrm{i}\mathsf{y}_i$. NLS and mKdV equations are two of the most famous integrable partial differential equations [@Ablowitz-Clarkson91]. The above two systems of equations can be combined to the Kadomtsev-Petviashvili (KP) equation, another integrable differential equation in three variables.

Theorem [\[thm:mKdV\]](#thm:mKdV){reference-type="ref" reference="thm:mKdV"} was obtained using the fact that the operator is a so-called integrable operator [@IIKS; @Deift99b].

Integrable differential equations have a long history starting with the work of Gardner, Greene, Kruskal, and Miura in 1967. They found a scattering transform method, an equation-specific nonlinear Fourier transform, to solve the Korteweg-De Vries equation. Like the integrable models in the KPZ universality class, integrable differentiable equations are isolated examples of nonlinear differential equations that can often be solved explicitly and analyzed asymptotically. See, for example, [@Ablowitz-Clarkson91; @Deift19]. It is intriguing that integrable probability models are related to integrable differential equations.
