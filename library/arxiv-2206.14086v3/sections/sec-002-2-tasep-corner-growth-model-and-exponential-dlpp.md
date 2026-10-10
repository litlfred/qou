---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-002-2-tasep-corner-growth-model-and-exponential-dlpp
section_title: "TASEP, corner growth model, and exponential DLPP"
section_number: 2
pages: 2-4
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
text_source: latex
latex_prose_ratio: 0.714
latex_coverage_ratio: 1.0
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:TASEP label="sec:TASEP"}

This section discusses one of the most well-studied examples of one-dimensional interacting particle systems, 1+1 random growth, and two-dimensional directed polymers.

## TASEP

The totally asymmetric simple exclusion process (TASEP), introduced by Spitzer [@Spitzer70] in 1970, is a continuous-time Markov process on $\mathbb{Z}$. At any given time, each integer site of $\mathbb{Z}$ is occupied by at most one particle. A particle moves to the adjacent site to its right after a random waiting time, but only if it is empty. The waiting time is exponentially distributed of mean $1$, and the clock starts once the neighboring site becomes vacant. All waiting times are independent of each other. Note that all moves are to the right (hence, totally asymmetric), particles can move only one step at a time (simple), and no two particles occupy the same site at the same time (exclusion). Figure [1](#fig:TASEP){reference-type="ref" reference="fig:TASEP"} is an example of the configuration at a particular time. Black dots denote particles, and white dots mark empty sites. In this configuration, only three particles can move, and they do so independently of each other.

<figure id="fig:TASEP">

<figcaption>TASEP</figcaption>
</figure>

The TASEP is an example of interacting particle systems. General systems may allow, for example, left moves in addition to right moves, multi-range moves, or several particles at each site.

One particular initial condition we focus on in this article is the step initial condition that the sites in $\mathbb{Z}_-\cup\{0\}$ are occupied, and all sites in $\mathbb{Z}_+$ are empty. The leftmost picture in Figure [2](#fig:corner){reference-type="ref" reference="fig:corner"} shows the step initial condition.

## Corner growth model

The configuration space for the TASEP is $\{0,1\}^{\mathbb{Z}}$ where $1$ represents the presence of a particle and $0$ an empty site. To each configuration, we can associate a zig-zag graph in $\mathbb{R}^2$ as in Figure [2](#fig:corner){reference-type="ref" reference="fig:corner"}. We assign a particle to a line segment of length $\sqrt{2}$ and slope $-1$, and an empty site to a line segment of the same length and slope $1$. Juxtaposing the line segments, we obtain a zig-zag graph as in Figure [2](#fig:corner){reference-type="ref" reference="fig:corner"}. We call the graph a height function $\mathbf{h}:\mathbb{R}\to \mathbb{R}$ for the configuration of the TASEP, and it is unique up to translations. The leftmost picture in Figure [2](#fig:corner){reference-type="ref" reference="fig:corner"} is a translation of $\mathbf{h}(x)=|x|$, and it corresponds to the step initial condition.

The TASEP induces a stochastic evolution of the height function, $\mathbf{h}(x,t)$, in which local valleys (corners) change to local peaks independently with rate $1$. The resulting 1+1 random growth process defined by the height function is called the corner growth process. See Figure [\[fig:cornersim\]](#fig:cornersim){reference-type="ref" reference="fig:cornersim"} for a simulation.

<figure id="fig:corner">
<div class="minipage">

</div>
<div class="minipage">

</div>
<div class="minipage">

</div>
<figcaption>Corner growth model</figcaption>
</figure>

## Exponential DLPP {#sec:DLPP}

Consider the two-dimensional lattice $\mathbb{Z}_+^2$. Let $(m,n)\in \mathbb{Z}_+^2$. An up/right (i.e., directed) path from $(1,1)$ to $(m,n)$ is a sequence $p=(p_i)_{i=1}^{m+n-1}$, where $p_i\in \mathbb{Z}_+^2$, $p_1=(1,1)$, $p_{m+n-1}=(m,n)$, and $p_{i+1}-p_i\in \{(1,0), (0,1)\}$. The thick lines in Figure [\[fig:ExpDLPP\]](#fig:ExpDLPP){reference-type="ref" reference="fig:ExpDLPP"} are an example of a path in which we connected neighboring integer sites for visual aid. Let $w_s$, $s\in \mathbb{Z}_+^2$, be a collection of independent random variables. The normalized free energy of the directed polymer measure, introduced by Huse and Henley [@Huse-Henley85], is $$\begin{equation*}
    F(m,n; \beta)= \frac1{\beta} \log \Big( \sum_{p} e^{\beta E(p)} \Big) \quad  \text{where $E(p)= \sum_{i=1}^{m+n-1} w_{p_i}$, }
\end{equation*}$$ the sum is over all directed paths $p$ from $(1,1)$ to $(m,n)$, and $\beta>0$ is the inverse temperature. The zero-temperature, $\beta=\infty$, case is called the directed last passage percolation (DLPP). In this case, the normalized free energy becomes $$\begin{equation*}
    L(m,n)= \max_{p} E(p),
\end{equation*}$$ which we call the last passage time, interpreting $E(p)$ as the travel time using path $p$.

<figure id="fig:ExpDLPPdual">
<div class="minipage">

</div>
<div class="minipage">

</div>
<figcaption>An example of <span class="math inline"><em>G</em><sub><em>t</em></sub></span></figcaption>
</figure>

For the case when $w_s\ge 0$, the DLPP is related to a random growth model. For $t>0$, define the subset of $\mathbb{R}^2$ by $$\begin{equation*}
    G_t= \bigcup_{s\in S_t} ( (0,1]^2+s)  \qquad 
    \text{where $S_t= \{(m, n)\in  \mathbb{Z}^2: L(m,n)\le t\}$}
\end{equation*}$$ and we set $L(m,n)=0$ if $m\le 0$ or $n\le 0$. See Figure [3](#fig:ExpDLPPdual){reference-type="ref" reference="fig:ExpDLPPdual"}. Since $L(m,n)$ is greater than or equal to both $L(m-1, n)$ and $L(m, n-1)$, we see that if $(m,n)\in G_t$, then both points $(m-1, n)$ and $(m,n-1)$ are in $G_t$. The set $G_t$ grows with time $t$. If we regard $G_t$ in the first quadrant as a stack of boxes, we can add a new box only at the corners.

A special case is the exponential DLPP in which $w_s$ are exponentially distributed with mean $1$. In this case, each corner of $G_t$ grows independently of rate $1$, i.e., a unit box can be added to each corner independent at rate $1$. Thus, the boundary of $G_t$ is a rotation of the height function of the corner growth process. More precisely, for the TASEP with the step initial condition and the exponential DLPP, $$\begin{equation}
 \label{eq:heightandDLPP}
    \mathbf{h}(m-n, t )\ge m+n \quad \text{ if and only if } \quad L(m,n)\le t .
\end{equation}$$ If the TASEP starts with a different initial condition, we need to consider the exponential DLPP on a subset of $\mathbb{Z}^2$, determined by the initial condition.

## Hydrodynamic limit and KPZ limit

The hydrodynamic limit of TASEP is about $\mathbf{h}(x,t)$ when $x$ and $t$ are proportional. For the step initial condition, $\mathbf{h}(x,0)=|x|$, Rost [@Rost81] showed in 1981 that $$\begin{equation*}
    \frac{\mathbf{h}(xT, tT)}{T}  \to \bar{\mathbf{h}}(x,t)
\end{equation*}$$ almost surely as $T\to \infty$, where $\bar{\mathbf{h}}(x,t) = \frac{t^2+x^2}{2t}$ for $|x|\le t$ and $\bar{\mathbf{h}}(x,t) = |x|$ for $|x|\ge t$. See Figure [4](#fig:hbar){reference-type="ref" reference="fig:hbar"} for the graph. The hydrodynamic limit $\bar{\mathbf{h}}$ is deterministic, and it solves Burger's equation [@Liggett85; @Liggett99].

The KPZ limit is about the next term, $\mathbf{h}(xT, tT)- \bar{\mathbf{h}}(x,t)T$. Setting $x=0$ for convenience and following the 1:2:3 scale, the KPZ universality conjecture suggests that $$\begin{equation*}
    \frac{\mathbf{h}(\gamma T^{2/3}, \tau T)- \bar{\mathbf{h}}(0,\tau)T}{T^{1/3}}
\end{equation*}$$ converges to a 2d random field. If we do not set $x=0$, then we should consider $\mathbf{h}(xT+ \gamma T^{2/3}, \tau T)- \bar{\mathbf{h}}(x,\tau)T$ in the numerator. The limiting 2d field, the KPZ fixed point, depends on the initial condition. The step initial condition for the TASEP becomes the so-called narrow wedge initial condition for the KPZ fixed point.

<figure id="fig:hbar">
<div class="minipage">
<embed src="Growth.pdf" />
</div>
<div class="minipage">

</div>
<figcaption><span class="math inline">$y= \bar{\mathbf{h}}(x, t)$</span> for a few values of <span class="math inline"><em>t</em></span></figcaption>
</figure>

TASEP has interpretations as an interacting particle system, a random growth process, and a last passage percolation model. Each of these interpretations has natural extensions and generalizations. The KPZ universality conjecture is that a large class of models in these generalizations has a universal limit. The exact class is not known, but for random growth models, three key features seem to be the locality of growth, some smoothing mechanism, and lateral growths. For directed last passage percolation, the universality is expected for all random variables $w_s$ with enough moments and without a large atom at the top of the support of the distribution. The last condition is to prevent the situation that there is always a path connecting $(1,1)$ and $(m,n)$ using only the top value, making the last passage time too concentrated.
