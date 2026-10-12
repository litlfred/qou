---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity"
section_id: sec-001-2-model-and-results
section_title: "Model and Results"
section_number: 2
pages: 3-7
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity — We establish new lower bounds for the convergence radius of the Ma yer series and the Virial series of a continuous"
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.993
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

## Results

\
As said in the introduction, the bound on the absolute value of the $n^{\rm th}$-order Mayer coefficient $C_n(\b,\L)$ appearing in Theorem 0 has been obtained "indirectly\" using the method of Kirkwood-Salzburg equations. Our main result is the following Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} below which improves strongly Theorem 0 via a direct bound on $C_n(\b,\L)$ by using the old Penrose tree-graph identity proposed in [@Pe67].

::: teorema
[]{#teo1 label="teo1"} Let $V$ be a stable and tempered pair potential with stability constant $B$. Then the $n$-order Mayer coefficient $C_n(\b,\L)$ is bounded by []{#bteo1 label="bteo1"} \|C_n(,̱Ł)\|e\^Ḇnn\^n-2 \[C()̱\]\^n-1n! where []{#hcb label="hcb"} C()̱=\_\^d dx Therefore the Mayer series converges absolutely, uniformly in $\L$, for any complex $\l$ inside the disk []{#radp label="radp"} \|ł\| \<1e\^Ḇ+1 C()̱ I.e. the convergence radius $R$ of the Mayer series admits the following lower bound []{#rnew label="rnew"} RR\^\*
:::

Observe that, according to the definitions ([\[cb\]](#cb){reference-type="ref" reference="cb"}) and ([\[hcb\]](#hcb){reference-type="ref" reference="hcb"}), we have $0\le \hat C(\b)\le C(\b)$.

\
**Remark 1**.\
The improvement given by Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} respect to Theorem 0 is twofold. First, the factor $e^{\b B+1}$ in ([\[rnew\]](#rnew){reference-type="ref" reference="rnew"}) replaces the factor $e^{2\b B+1}$ in ([\[rold\]](#rold){reference-type="ref" reference="rold"}). Second, the factor $\hat C(\b)$ in ([\[rnew\]](#rnew){reference-type="ref" reference="rnew"}) replaces the factor $C(\b)$ in ([\[rold\]](#rold){reference-type="ref" reference="rold"}) and clearly, recalling their definitions ([\[hcb\]](#hcb){reference-type="ref" reference="hcb"}) and ([\[cb\]](#cb){reference-type="ref" reference="cb"}) respectively, we have $\hat C(\b)\le C(\b)$ where the equality only holds if $V$ is non-negative (purely repulsive). Moreover observe that while $\hat C(\b)$ grows at most linearly in $\b$, the factor $C(\b)$ can grow exponentially with $\b$ (for $V$ with an attractive part). So,

the ratio ${R^{*}
/R_{\rm PR}

}$ always greater than one, is the product of two factors, $e^{\b B}$ and $[{\hat C(\b)/ C(\b)}]$, both growing exponentially fast with $\b$ when $V$ has a negative part. Due to this exponential behavior in $\b$, our improvement on the Penrose-Ruelle bound is rather astonishing for attractive potentials (i.e. those with strictly positive stability constant $B$) at non small $\b$ (i.e. low temperatures). To give an idea, for the Lennard-Jones gas at inverse temperature $\b=1$, using the value $B_{\rm LJ}=8.61$ for its stability constant (see [@JI]), our lower bound is at least $8.5\times 10^4$ larger than the Penrose-Ruelle lower bound, while for $\b=10$ is at least $7.26\times 10^{43}$ larger than the Penrose-Ruelle lower bound. On the other hand, for $\b$ small the exponential $e^{\b B}$ is near to one and $\hat C(\b)$ becomes very close to $C(\b)$ so that our improvement is much less sensitive at high temperatures. Finally, for purely repulsive pair potentials (i.e. those with stability constant $B=0$) our bound coincides with the Penrose-Ruelle bound since in this case $e^{\b B}=1$ and $\hat C(\b)=C(\b)$.

\
**Remark 2**. As mentioned above, the density of the system $\r_\L(\b,\l)$ given in ([\[dens\]](#dens){reference-type="ref" reference="dens"}) can also be written, via ([\[pressm\]](#pressm){reference-type="ref" reference="pressm"}), in terms of a power series of the fugacity $\l$. This series allows to express the fugacity $\l$ as a power series of the density $\r_\L$ which, plugged into ([\[pressm\]](#pressm){reference-type="ref" reference="pressm"}), gives the so-called Virial series (see, e.g., [@MM]), i.e., the pressure as a function of the density and temperature, or, in other words, the equation of state of the system. In 1964 Lebowitz and Penrose [@LP] (provided the following lower bound on the convergence radius $\cal R$ of the Virial series of a gas of particles interacting via a stable and tempered pair potential. []{#virialold label="virialold"} R\_LP with $$g(u)= \max_{0<w<1} {[(1+u)e^{-w} -1]w\over u}$$ The authors deduced such a bound, via Lagrange inversion, from the Penrose-Ruelle bounds ([\[bmaru\]](#bmaru){reference-type="ref" reference="bmaru"}) of the Mayer coefficients (see also [@Gr] for an alternative method that deal directly with the coefficients of the Viral series written in terms of two-connected graphs). If one redoes the calculations performed by Lebowitz and Penrose using the new upper bound ([\[bteo1\]](#bteo1){reference-type="ref" reference="bteo1"}) for the absolute value of the $n^{\rm th}$-order Mayer coefficient (with $\hat C(\b)$ in place of $C(\b)$ and $e^{\b B}$ in place of $e^{2\b B}$), then one immediately obtains the following lower bound for the convergence radius ${\cal R}$ of the Viral series []{#virial label="virial"} R\^\*

Observing that $0.1448\le g(u)\le e^{-1}$ for $u\in [1,\infty)$ (see, e.g., Remark 2 below Theorem 1 in [@MP]), we have that the ratio ${\cal R}^{*}/{\cal R}_{\rm LP}$ between the new lower bound ([\[virial\]](#virial){reference-type="ref" reference="virial"}) for the convergence radius of the Viral series and the old Lebowitz-Penrose bound given in ([\[virialold\]](#virialold){reference-type="ref" reference="virialold"}) is of the same order of magnitude of the ratio ${R^*/R_{PR}}$ calculated above.

\
The proof of Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} relies on a non trivial tree-graph inequality on the absolute value of the integrand of the r.h.s. of ([\[urse\]](#urse){reference-type="ref" reference="urse"}) (the so-called Ursell functions) as far as stable pair potentials are considered. This new tree-graph inequality, an additional result of the present paper which we consider interesting *per se*, can be stated as follows.

::: pro
[]{#pro1 label="pro1"} Let $V$ be a stable pair potential with stability constant $B$. Then, for any $n\ge 2$ and any $(x_1,\dots,x_n)\in \mathbb{R}^{dn}$, the following inequality holds []{#nine label="nine"} \|\_g \_n \_{i,j} E_g (e\^-V̱(x_i-x_j)-1)\|   e\^Ḇn\_\_n \_{i,j} E\_ (1-e\^-\|̱ V(x_i-x_j)\|) where ${\mathcal T}_n$ denotes the set of all trees with vertex set $[n]$ (a.k.a. labeled trees with $n$ vertices).
:::

\
The proofs of Proposition [\[pro1\]](#pro1){reference-type="ref" reference="pro1"} and Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} are given in sections 3 and 4 respectively.

# Proof of Proposition [\[pro1\]](#pro1){reference-type="ref" reference="pro1"} {#sec3}

In this section we set $[n]:=\{1, ... ,n\}$ and $E_n:=\{\{i,j\} :\; i,j \in [n], \ i <j \}$. We recall also that ${\mathcal G}_n$ is the set of all connected graphs with vertex set $[n]$ (i.e labeled connected graphs with $n$ vertices) and ${\mathcal T}_n$ is the set of all trees with vertex set $[n]$ (i.e labeled trees with $n$ vertices). Given $g\in {\mathcal G}_n$, we denote $E_g$ its edge set. Given $g\in {\mathcal G}_n$ and $g'\in {\mathcal G}_n$ such that $E_g\subset E_{g'}$, we say that $g$ is a subgraph of $g'$ and write $g\subset g'$. Note that the pair $({\mathcal G}_n, \subset)$ is a partially ordered set. Given $g,g'\in {\mathcal G}_n$ such that $g\subset g'$, we denote $[g,g'] =\{g''\in {\mathcal G}_n: g\subseteq g''\subseteq g'\}$. In other words $[g,g']$ is an interval in $({\mathcal G}_n,\subset)$. Given a set $S$, we denote by $|S|$ its cardinality.
