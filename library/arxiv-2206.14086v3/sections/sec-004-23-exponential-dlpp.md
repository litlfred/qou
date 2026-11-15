---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-004-23-exponential-dlpp
section_title: "Exponential DLPP"
section_number: 2.3
pages: 3-4
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.761
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:DLPP label="sec:DLPP"}

Consider the two-dimensional lattice $\mathbb{Z}_+^2$. Let $(m,n)\in \mathbb{Z}_+^2$. An up/right (i.e., directed) path from $(1,1)$ to $(m,n)$ is a sequence $p=(p_i)_{i=1}^{m+n-1}$, where $p_i\in \mathbb{Z}_+^2$, $p_1=(1,1)$, $p_{m+n-1}=(m,n)$, and $p_{i+1}-p_i\in \{(1,0), (0,1)\}$. The thick lines in Figure [\[fig:ExpDLPP\]](#fig:ExpDLPP){reference-type="ref" reference="fig:ExpDLPP"} are an example of a path in which we connected neighboring integer sites for visual aid. Let $w_s$, $s\in \mathbb{Z}_+^2$, be a collection of independent random variables. The normalized free energy of the directed polymer measure, introduced by Huse and Henley [@Huse-Henley85], is $$F(m,n; \beta)= \frac1{\beta} \log \Big( \sum_{p} e^{\beta E(p)} \Big) \quad  \text{where $E(p)= \sum_{i=1}^{m+n-1} w_{p_i}$, }$$ the sum is over all directed paths $p$ from $(1,1)$ to $(m,n)$, and $\beta>0$ is the inverse temperature. The zero-temperature, $\beta=\infty$, case is called the directed last passage percolation (DLPP). In this case, the normalized free energy becomes $$L(m,n)= \max_{p} E(p),$$ which we call the last passage time, interpreting $E(p)$ as the travel time using path $p$.

<figure id="fig:ExpDLPPdual">

<figcaption>An example of <span class="math inline"><em>G</em><sub><em>t</em></sub></span></figcaption>
</figure>

For the case when $w_s\ge 0$, the DLPP is related to a random growth model. For $t>0$, define the subset of $\mathbb{R}^2$ by $$G_t= \bigcup_{s\in S_t} ( (0,1]^2+s)  \qquad 
    \text{where $S_t= \{(m, n)\in  \mathbb{Z}^2: L(m,n)\le t\}$}$$ and we set $L(m,n)=0$ if $m\le 0$ or $n\le 0$. See Figure [1](#fig:ExpDLPPdual){reference-type="ref" reference="fig:ExpDLPPdual"}. Since $L(m,n)$ is greater than or equal to both $L(m-1, n)$ and $L(m, n-1)$, we see that if $(m,n)\in G_t$, then both points $(m-1, n)$ and $(m,n-1)$ are in $G_t$. The set $G_t$ grows with time $t$. If we regard $G_t$ in the first quadrant as a stack of boxes, we can add a new box only at the corners.

A special case is the exponential DLPP in which $w_s$ are exponentially distributed with mean $1$. In this case, each corner of $G_t$ grows independently of rate $1$, i.e., a unit box can be added to each corner independent at rate $1$. Thus, the boundary of $G_t$ is a rotation of the height function of the corner growth process. More precisely, for the TASEP with the step initial condition and the exponential DLPP, $$\label{eq:heightandDLPP}
    \mathbf{h}(m-n, t )\ge m+n \quad \text{ if and only if } \quad L(m,n)\le t .$$ If the TASEP starts with a different initial condition, we need to consider the exponential DLPP on a subset of $\mathbb{Z}^2$, determined by the initial condition.
