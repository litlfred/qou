---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity"
section_id: sec-002-22-results
section_title: "Results"
section_number: 2.2
pages: 4-6
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.99
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity — We establish new lower bounds for the convergence radius of the Mayer series and the Virial series of a continuous"
---
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
