---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-007-24-feynman-diagrams-for-the-n-loop-invariant
section_title: "Feynman diagrams for the n-loop invariant"
section_number: 2.4
pages: 8-9
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.946
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.diagrams label="sub.diagrams"}

In this section we give a Feynman diagram formulation of the higher-loop invariants. A Feynman diagram $\mathbf D$ is a finite graph possibly with loops and multiple edges. To every edge in a Feynman diagram we associate the symmetric $N\times N$ propagator matrix

$$\Pi =  \hbar k (-\mathbf B^{-1}\mathbf A + \Delta_{z'})^{-1}\,,$$

and to a vertex with valence $j$ we associate the vertex factor $\Gamma^{(j)}$, which is a tensor of rank $j$ whose only nonzero entries $\Gamma_i^{(j)} := \Gamma_{ii...i}^{(j)} \in F_{G,k}(\!(\hbar)\!)$ lie on the diagonal, and are functions of $m\in (\mathbb Z/k\mathbb Z)^N$ and $\theta$,

$$\begin{array}{rl}
\Gamma^{(0)} &= \displaystyle \frac{\hbar}{8k}f\mathbf B^{-1}\nu 
+ \sum_{n=2}^\infty \frac{\hbar^{n-1}}{n!}\sum_{s=1}^k B_n
\big(\tfrac sk\big) \sum_{i=1}^N{\rm Li}_{2-n}(\zeta^{m_i+s} \theta_i^{-1}) \\[.1cm]
\Gamma_i^{(1)} &=  \displaystyle -\frac{1}{2k}(\mathbf B^{-1}\nu)_i 
- \sum_{n=1}^\infty \frac{\hbar^{n-1}}{k\,n!}\sum_{s=1}^k B_n
\big(\tfrac sk\big){\rm Li}_{1-n}(\zeta^{m_i+s}\theta_i^{-1}) \\[.1cm]
\Gamma_i^{(2)} &= \displaystyle \sum_{n=1}^\infty 
\frac{\hbar^{n-1}}{k^2\,n!}\sum_{s=1}^k B_n\big(\tfrac sk\big)
{\rm Li}_{-n}(\zeta^{m_i+s}\theta_i^{-1}) \\[.1cm]
\Gamma_i^{(j)} &= \displaystyle \sum_{n=0}^\infty 
\frac{(-1)^j\hbar^{n-1}}{k^j\,n!}\sum_{s=1}^k B_n\big(\tfrac sk\big)
{\rm Li}_{2-n-j}(\zeta^{m_i+s}\theta_i^{-1})\qquad (j\geq 3)\,,
\end{array}$$

where $B_n(x)$ are the Bernoulli polynomials, defined by $te^{xt}/(e^t-1) = \sum_{n\geq 0}B_n(x)t^n/n!$ and $F_{G,k}(\!(\hbar)\!)$ denotes the ring of formal Leurent series in $\hbar$ with coefficients in $F_{G,k}$.

Note that each $\Gamma_i^{(j)}$ only depends on $m,\,\theta$ through the combination $\zeta^{m_i}\theta_i^{-1}$. Moreover, all the $l$-polylogarithms appearing here involve non-positive $l$, hence are rational functions. The evaluation $[\mathbf D]_m$ of a diagram is obtained by contracting propagator and vertex indices, and multiplying by a standard symmetry factor $1/|\sigma(\mathbf D)|$, where $\sigma(\mathbf D)$ is the diagram's symmetry group,

$$_m =  \frac{1}{|\sigma(\mathbf D)|} 
\sum_{\text{coincident indices}} \;\;\prod_{\text{edges $e$}} 
\Pi(e)\prod_{\text{vertices $v$}}  \Gamma(v)\,.$$

For example, the diagram in the center of the top row of Figure [\[fig.diags2intro\]](#fig.diags2intro){reference-type="ref" reference="fig.diags2intro"} has an evaluation $[\mathbf D]_m = 
\frac18 \sum_{i,i'=1}^N \Pi_{ii}\Gamma^{(3)}_i \Pi_{ii'}\Gamma^{(3)}_{i'}\Pi_{i'i'}$. To the *trivial* diagram $\bullet$ that consists of one vertex and no edges we associate the vacuum energy $[\bullet]_m=\Gamma^{(0)}$. The next Lemma follows from evaluating the formal Gaussian integral [\[eq.defphi\]](#eq.defphi){reference-type="eqref" reference="eq.defphi"} in terms of Feynman diagrams; see [@BIZ].

::: lemma
[]{#lem.phih label="lem.phih"} For a $\mathbb Z$-non-degenerate Neumann-Zagier datum $\gamma$, we have

$$\phi^+_{\gamma,\zeta}(\hbar)  = 
\mathrm{Av}\bigg[ \exp\bigg( \sum_{\text{connected $\mathbf D$}} [\mathbf D]_m\bigg)\bigg]\, 
\in 1 + \hbar\,\mathbb C[\![\hbar]\!]\,,$$

where the sum is over all connected diagrams $\mathbf D$, including the empty diagram.
:::

Using the above Lemma and Equation [\[def.Sn\]](#def.Sn){reference-type="eqref" reference="def.Sn"}, it follows that in order to compute $S_{\gamma,n}$ for $n\geq 2$, it suffices to consider the finite set of Feynman diagrams with

$$\label{eq.LD}
\text{\#(1-vertices) + \#(2-vertices) + \#(loops)} \leq n \,,$$

and to truncate the formal power series in each of the vertex factors to finite order in $\hbar$. In the next two sections, we give axplicit formulas for the 2 and 3-loop invariants.
