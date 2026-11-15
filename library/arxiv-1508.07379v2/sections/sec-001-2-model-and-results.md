---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity"
section_id: sec-001-2-model-and-results
section_title: "Model and Results"
section_number: 2
pages: 3-4
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.979
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity — We establish new lower bounds for the convergence radius of the Mayer series and the Virial series of a continuous"
---
[]{#sec2 label="sec2"}

## Model

We consider a continuous system of classical particles in the $d$-dimensional Euclidean space $\mathbb{R}^d$. Denote by $x_i\in \mathbb{R}^d$ the position vector of the $i^{\rm th}$ particle of the system and by $\|x_i\|$ its Euclidean norm. We suppose hereafter that particles interact through a pair potential $V:\mathbb{R}^d\to \mathbb{R}\cup\{+\infty\}$ such that $V(-x)=V(x)$ and we set shortly $\mathbb{R}^*\doteq \mathbb{R}\cup\{+\infty\}$. Given a configuration $(x_1,\dots,x_n)\in {\mathbb R}^{dn}$ of the system such that $n$ particles are present, the energy $U(x_1,\dots,x_n)$ of this configuration is defined as $$U(x_1,\dots,x_n)=\sum_{1\le i< j\le n}V(x_i-x_j)$$ We work in the Grand Canonical Ensemble, where the statistical mechanics of the system is governed by the following partition function []{#1.1 label="1.1"} \_Ł(ł,)̱=\_n=0\^ \_Łdx_1 ...\_Łdx_n e\^-U̱(x_1,...,x_n) where $\L\subset{\mathbb R}^d$ is typically a $d$-dimensional cube with center in the origin, $\lambda\in (0,+\infty)$ is the activity of the system and $\b\in (0,+\infty)$ is the inverse temperature.

\
The connection with thermodynamics is obtained by taking the logarithm of the partition function. Namely, the pressure $P_\L(\b,\l)$ and the density $\r_\L(\b,\l)$ of the system at fixed values of the thermodynamic parameters inverse temperature $\b$, fugacity $\l$ and volume $\L$, are given by []{#press label="press"} P_Ł(,̱ł)= 1\|̱Ł\|\_Ł(ł,)̱ []{#dens label="dens"} ̊\_Ł(,̱ł) =  ł\|Ł\|ł\_Ł(ł,)̱

\
It is a long known fact [@MM] that $\log \Xi_{\L}(\l,\b)$ can be expanded as a power series of the fugacity. Namely, []{#pressm label="pressm"} 1\|Ł\|\_Ł(ł,)̱  =  ł+ \_n=2\^C_n(,̱Ł)ł\^n The series above is the so-called Mayer series and its coefficients $C_n(\b,\L)$, known nowadays as *Mayer coefficients*, admit the following explicit expression. []{#urse label="urse"} C_n(,̱Ł) = 1\|Ł\|1n!\_Ł dx_1 ...\_Ł dx_n\_g\_n \_{i,j}E_g where ${\mathcal G}_n$ denotes the set of all connected graphs with vertex set $\{1,2,\dots,n\}$ (a.k.a. labeled connected graphs with $n$ vertices) and $E_g$ denotes the edge set of $g\in {\mathcal G}_n$.

\
Clearly, via Mayer series one can write both pressure ([\[press\]](#press){reference-type="ref" reference="press"}) and density ([\[dens\]](#dens){reference-type="ref" reference="dens"}) as expansions in power of the fugacity $\l$.

\
Some conditions on the potential $V$ must be imposed to have hope to control the series. Stability and temperedness are commonly considered as minimal conditions to guarantee a good statistical mechanics behavior of the system (see, e.g., [@Ru] and [@Ga]).

::: defi
A pair potential $V$ is said to be stable if []{#stabi label="stabi"} B:=\_n\_(x_1,...,x_n)\^dn-1nU(x_1,...,x_n) \< + We call $B$ the stability constant of the pair potential $V$.
:::

::: defi
A pair potential $V$ is said to be tempered if there exists $r_0\ge 0$ such that []{#temp label="temp"} \_x̍̍r_0 \|V(x)\| dx \<
:::

Observe that the stability constant of any tempered potential $V$ is non-negative.

\
As mentioned in the introduction, the best rigorous upper bound on $|C_n(\b,\L)|$ so far (and hence the best lower bound on the convergence radius of the Mayer series) for stable and tempered pair potentials is that obtained by Penrose and Ruelle in 1963 [@Pe63; @Ru63].

\
**Theorem 0 (Penrose Ruelle 1963)** *Let $V$ be a stable and tempered pair potential with stability constant $B$. Then the $n$-order Mayer coefficient $C_n(\b,\L)$ defined in ([\[urse\]](#urse){reference-type="ref" reference="urse"}) is bounded by []{#bmaru label="bmaru"} \|C_n(,̱Ł)\|e\^2Ḇ (n-1)n\^n-2 \[C()̱\]\^n-1n! where []{#cb label="cb"} C()̱=\_\^d dx   \|e\^-V̱(x)-1\| Therefore the Mayer series ([\[pressm\]](#pressm){reference-type="ref" reference="pressm"}) converges absolutely, uniformly in $\L$, for any complex $\l$ inside the disk []{#radm label="radm"} \|ł\| \<1e\^2Ḇ+1 C()̱ I.e. the convergence radius $R$ of the Mayer series admits the following lower bound []{#rold label="rold"} RR\_PR  1e\^2Ḇ+1 C()̱*

\
Observe that the non-negative quantity $C(\b)$ defined in ([\[cb\]](#cb){reference-type="ref" reference="cb"}) is finite if $V$ is stable and tempered (see e.g. [@Ru]).
