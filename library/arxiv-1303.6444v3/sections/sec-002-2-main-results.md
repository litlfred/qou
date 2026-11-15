---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-002-2-main-results
section_title: "Main Results"
section_number: 2
pages: 2-4
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.971
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
The main results of this paper rely on the particle model of the classical gas. The main parameters in the model are: the inverse temperature $\beta = \frac{1}{kT}$, where $k$ is Boltzmann's constant and $T$ is the temperature; the fugacity $z$; the pressure $P$; and the density $\rho$.

We start with the Grand Canonical Partition function for a classical gas: $$\Xi(z)  = \sum\limits_{N=0}^{\infty}Z_Nz^n$$ Where $Z_N$ is the $N$-particle configuration integral: $$Z_N = \frac{1}{N!}\prod\limits_{i=1}^N\left(\int_{\mathbb{R}^d}\, \mathrm{d}^dx_i\right) e^{-\beta\sum\limits_{1 \leq i<j \leq N}\Phi(x_i,x_j)}$$ We have the relationship $\beta P = \ln \Xi$, which gives us an expansion for pressure. The power series for pressure in terms of fugacity $z$, may be written as: $$\beta P = \sum\limits_{n \geq 1}b_nz^n \label{clusterexp}$$ Using the formula $\rho=z\frac{\partial}{\partial z} (\beta P)$, we have the corresponding fugacity expansion for density: $$\rho = \sum\limits_{n \geq 1} nb_n z^n \label{clusterexp2}$$ We see that the power series expansion for $\rho$ has a zero constant term and non zero $z$ term, where we have that $b_1 \neq 0$ and usually we set it to $1$. It is usual to have a non zero $z$ coefficient in the cluster expansion. This means that it is possible to invert the $\rho-z$ relationship, in order to obtain an expansion for $z(\rho)$. This can be substituted into [\[clusterexp\]](#clusterexp){reference-type="eqref" reference="clusterexp"} in order to get a power series for $P$ in terms of $\rho$: $$P=\sum\limits_{n \geq 1}c_n \rho^n \label{virialexp}$$ The assumptions for the initial cluster expansion bounds used in this article are:

::: assumption
The $N$-particle interaction potential: $U_N(x_1, \cdots, x_N)$ may be written as the sum of pair-potentials: $$U_N(x_1, \cdots, x_N)= \sum\limits_{1 \leq i<j \leq N}\Phi(x_i,x_j)$$ Furthermore, we assume that the pair potentials $\Phi(x_i,x_j)$ are central, that is, they only depend on the distance from $x_i$ to $x_j$.
:::

::: assumption
[]{#ass: stability label="ass: stability"} The potential energy is assumed to be stable, that is, there is a $B>0$, such that for every $N$ and $(x_1, \cdots, x_N) \in \mathbb{R}^{Nd}$, we have: $$U(x_1, \cdots, x_N)=\sum\limits_{1 \leq i<j \leq N}\Phi(x_i,x_j) \geq -BN$$ where $d$ is the dimension of our system.
:::

::: definition
We have two main functions of $\beta$, which play an important rôle in the cluster expansion bounds: $$C(\beta):=\int\limits_{\mathbb{R}^d} \, \left|e^{-\beta \Phi(0,x)}-1\right| \mathrm{d}^dx \label{Cbeta}$$ $$R(\beta):= \left(|\mathbb{B}|r^d+\beta \int\limits_{|y|>r}\, |\Phi(0,y)| \mathrm{d}^dy \right) \label{Rbeta}$$ If the expression [\[Cbeta\]](#Cbeta){reference-type="eqref" reference="Cbeta"} is finite then the potential $\Phi$ is called 'tempered', which we assume for bounds involving $C(\beta)$

The $r$ in [\[Rbeta\]](#Rbeta){reference-type="eqref" reference="Rbeta"} represents the radius of the hard-core interaction. $|\mathbb{B}|$ is the surface area of a $d$-dimensional sphere.
:::

We write $\mathcal{R}_{\text{Vir}}$ for the radius of convergence of the virial expansion.

::: definition
We denote by $W(z)$, the Lambert W-function with domain $\mathbb{R}_+:=\{x \in \mathbb{R} \vert x \geq 0\}$ and range $\mathbb{R}_+$. It is the solution to: $$W(z) e^{W(z)}=z$$
:::

Further notes on the Lambert W-function can be found in [@CJK97]

::: theorem
[]{#thm: general label="thm: general"} Assuming cluster coefficient bounds of the form: $$|nb_n| \leq a \frac{n^{n-1}}{n!}b^n$$ where $a$ and $b$ are non-negative functions of inverse temperature $\beta$, we have the virial coefficient bounds: $$|c_n| \leq \frac{\beta^{-1}}{n}\left(a^{-1} \frac{W\left(\frac{eab}{1+ab}\right)}{\left(W\left(\frac{eab}{1+ab}\right)-1\right)^2}\right)^{n-1}$$ which gives the lower bound on the radius of convergence as: $$\mathcal{R}_{\text{Vir}} \geq a \frac{\left(W\left(\frac{eab}{1+ab}\right)-1\right)^2}{W\left(\frac{eab}{1+ab}\right)}$$
:::

If we apply this general theorem, which is derived in Section [\[sec: general\]](#sec: general){reference-type="ref" reference="sec: general"}, to two specific bounds we have for cluster expansions, we achieve:

::: corollary
[]{#cor:lebpenbound label="cor:lebpenbound"} The cluster expansion bounds: $$|nb_n| \leq \frac{n^{n-1}}{n!}e^{2\beta B(n-1)}C(\beta)^{n-1}$$ give the bound for virial coefficients: $$|c_n| \leq \frac{\beta^{-1}}{n} \left(C(\beta)e^{4\beta B} \frac{W\left(\frac{e}{1+e^{2\beta B}}\right)}{\left(W\left(\frac{e}{1+e^{2\beta B}}\right)-1\right)^2}\right)^{n-1}$$ and the bound for the radius of convergence: $$\mathcal{R}_{\text{Vir}} \geq C(\beta)^{-1} e^{-4\beta B}\frac{\left(W\left(\frac{e}{1+e^{2\beta B}}\right)-1\right)^2}{W\left(\frac{e}{1+e^{2\beta B}}\right)}$$
:::

This is shown in Section [\[sec: oldbounds\]](#sec: oldbounds){reference-type="ref" reference="sec: oldbounds"}

For purely hard-core interactions $B=0$ and the radius of convergence satisfies: $$\mathcal{R}_{\text{Vir}} \geq C(\beta)^{-1} \frac{\left(W\left(\frac{e}{2}\right)-1\right)^2}{W\left(\frac{e}{2}\right)}$$ This is precisely the same as what is obtained by Lebowitz-Penrose.

::: corollary
[]{#cor:mybounds label="cor:mybounds"} For cluster expansion bounds: $$|nb_n| \leq \frac{n^{n-1}}{n!}R(\beta)^{n-1}e^{n\beta B}$$ we have the bound for virial coefficients as: $$|c_n| \leq \frac{\beta^{-1}}{n}R(\beta)^{n-1} \left( \frac{W\left(\frac{e^{\beta B+1}}{1+e^{\beta B}}\right)}{\left(W\left(\frac{e^{\beta B +1}}{1+e^{\beta B}}\right)-1\right)^2}\right)^{n-1}$$ Thus giving the radius of convergence as: $$\mathcal{R}_{\text{Vir}} \geq R(\beta)^{-1} \frac{\left(W\left(\frac{e^{\beta B +1}}{1+e^{\beta B}}\right)-1\right)^2}{W\left(\frac{e^{\beta B+1}}{1+e^{\beta B}}\right)}$$
:::

::: remark
The bounds for the cluster coefficients used in Corollary [\[cor:lebpenbound\]](#cor:lebpenbound){reference-type="ref" reference="cor:lebpenbound"} are obtained in [@R69] and [@LPen64]. The bounds for the cluster coefficients used in Corollary [\[cor:mybounds\]](#cor:mybounds){reference-type="ref" reference="cor:mybounds"} are obtained in [@PU09].
:::

Having a new separate bound is only a good idea, if it is an improvement in certain cases. In Section [\[sec: comparison\]](#sec: comparison){reference-type="ref" reference="sec: comparison"} we understand how the two different bounds compare and conclude:

::: proposition
[]{#prop: comparison label="prop: comparison"} The bound in Corollary [\[cor:mybounds\]](#cor:mybounds){reference-type="ref" reference="cor:mybounds"} is better than that in Corollary [\[cor:lebpenbound\]](#cor:lebpenbound){reference-type="ref" reference="cor:lebpenbound"}, precisely when $$1.6R(\beta) < C(\beta)$$
:::

This is likely to happen at low temperatures (large $\beta$) and for potentials with a hard core and attractive tail. The attractive element of the potential is important, since the improvements are made corresponding to the stability parameter $B$.
