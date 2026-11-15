---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-017-73-transition-probabilities
section_title: "Transition probabilities"
section_number: 7.3
pages: 10-11
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.982
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
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
