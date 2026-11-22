---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-001-11-cumulants-in-the-ising-model
section_title: "Cumulants in the Ising model"
section_number: 1.1
pages: 1-2
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.93
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
The Ising model is a mathematical model of ferro-magnetism in statistical physics. It was introduced in 1920 by Wilhelm Lenz who gave it as a problem to his Ph.D. student Ernst Ising [@Ising]. It can be defined on any finite graph, but we restrict ourselves to finite subsets $\Lambda$ of $\mathbb{Z}^d$. For any lattice site $i \in \Lambda$, there is a random variable $\sigma_i$ which is equal to either $1$ or $-1$ and represents the *spin* at site $i$. A *spin configuration* $\omega = (\sigma_i (\omega))_{i \in \Lambda}$ is an assignment of spins to every site of $\Lambda$.

The distribution of spins depends on the magnetic field $h$ and the inverse temperature $\beta$ in a way that will be detailed later (see Section [\[sec:prelimIsing\]](#sec:prelimIsing){reference-type="ref" reference="sec:prelimIsing"}). In particular, spins corresponding to neighbour sites $i$ and $j$ are more likely to be aligned (i.e. both equal to $1$ or both equal to $-1$); the bigger $\beta$ is (i.e. the lower the temperature is), the more important is this phenomenon.

In his Ph.D. thesis [@Ising], Ising solved the model for the one-dimensional case $d=1$, and showed that there is no phase transition. But in 1936, Peierls [@Peierls] showed that, in dimensions $2$ and $3$, when $h=0$, the Ising model undergoes a phase transition at a critical inverse temperature $\beta_c$. He used a combinatorial argument now known as Peierls' argument. The two-dimensional model for $h=0$ was then exactly solved by Onsager [@Onsager] in 1944, using analytic techniques and the transfer matrix method. It turns out that in higher dimensions, there is also a phase transition for $h=0$ (see [@Peierls] or [@Velenik] for a more modern treatment) and no phase transition when there is a magnetic field $h \neq 0$ [@LeeYang; @Yang].

The Ising model is *a priori* defined on a finite subset $\Lambda \subset \mathbb{Z}^d$, but it is well-known that we can take the *thermodynamic limit* $\Lambda \uparrow \mathbb{Z}^d$ (see eg. [@Velenik]).

This defines, for each pair of parameters $(\beta,h)$, a measure $\mu_{\beta,h}$ on the set $\{-1,1\}^{\mathbb{Z}^d}$ of spin configurations on the whole $d$-dimensional lattice $\mathbb{Z}^d$. (In low temperature without magnetic field, i.e. $\beta$ large and $h=0$, this measure is not unique; we will consider the one corresponding to $+$ boundary conditions, see [\[sec:prelimIsing\]](#sec:prelimIsing){reference-type="ref" reference="sec:prelimIsing"} for details.)

The Ising model has since been studied in thousands of research articles, under various aspects. Among many others, a subject of interest has been the decay of joint cumulants of the spins (also called *truncated $k$-point functions* or *Ursell functions* in the physics literature). The joint cumulant of order $r$ of spins $\sigma_{i_1},\dots,\sigma_{i_r}$ is defined as $$\kappa_{\beta,h}(\sigma_{i_1},\dots,\sigma_{i_r}) = [t_1 \dots t_r] \log 
\big\langle \exp(t_1 \sigma_{i_1} + \dots + t_r \sigma_{i_r}) \big\rangle_{\beta,h}.$$ The covariance is the joint cumulant of order $2$ (more detail in Section [\[sec:cumulants\]](#sec:cumulants){reference-type="ref" reference="sec:cumulants"}).

Bounds on cumulants in the physics literature are often called *cluster properties*. There is in fact a hierarchy of cluster properties (corresponding to sharper or weaker bounds on cumulants); we refer to [@Duneau1] or [@Malyshev Chapter 6, §1] for definitions of various kinds of cluster properties.

In the case of the Ising model, a first bound on cumulants was obtained by Martin-Löf [@Lof Eq. (20)] --- see also [@Lebowitz Section 1] ---: he proved that the joint cumulant $\kappa_{\beta,h}(\sigma_i;i \in A)$ decreases exponentially in $\mathop{\mathrm{diam}}(A)/r$, where $\mathop{\mathrm{diam}}(A)$ is the the diameter of $A$ and $r$ the order of the cumulants. In [@Duneau], Duneau, Iagolnitzer and Souillard sharpened this bound in presence of a magnetic field ($h \ne 0$), or for $h=0$ and very high temperature: $\kappa_{\beta,h}(\sigma_i;i \in A)$ decays exponentially in $\ell_T(A)$, the minimum length of a tree connecting vertices of $A$ (see [\[Subsect:Spanning\]](#Subsect:Spanning){reference-type="ref" reference="Subsect:Spanning"} for a formal definition of the tree-length). In [@Malyshev], Malyshev and Minlos have a similar result in the case $h=0$ and very low temperature. Both their approaches use cluster expansion, a powerful tool introduced by Mayer and Montroll [@Mayer] which consists in viewing our model in terms of macroscopic geometrical objects instead of considering its original microscopic components. Both proofs use additional ingredients of different nature: Duneau, Iagolnitzer and Souillard use Lee-Yang circle theorem and complex analysis arguments, while Malyshev's and Minlos' approach relies on combinatorial developments and bounds on joint cumulants for *contours* as an intermediate step (contours will be defined in Section [\[Sect:CE_LT\]](#Sect:CE_LT){reference-type="ref" reference="Sect:CE_LT"}).

These bounds on free cumulants will be our starting point to prove central limit theorems for patterns in the Ising model. In order to make the article more self-contained, we give a simpler and more unified approach of the decays of joint cumulants in regimes, where the cluster expansion converges. The result is stated as follows.

::: theorem
We consider the Ising model on $\mathbb{Z}^d$ with parameters $(\beta,h)$. There exist positive constants $\varepsilon(d)<1$, $\beta_1(d)$, $\beta_2(d)$ and $h_1(d)$ depending on the dimension $d$ with the following property. Assume we are in one of three following regimes:

very low temperature

:   $\beta> \beta_2(d)$ and $h=0$;

very high temperature

:   $\beta < \beta_1(d)$ and $h=0$;

strong magnetic field

:   $h > h_1(d)$.

Then for any $r \ge 1$, there exists a constant $D_r$ such that for all $A=\{i_1, \dots, i_r\} \subset \mathbb{Z}^d$, we have $$\big| \kappa_{\beta,h}(\sigma_{i_1},\dots, \sigma_{i_r}) \big| 
  \le D_r \varepsilon(d)^{\ell_T(A)}.$$ []{#thm:bound_joint_cumulants label="thm:bound_joint_cumulants"}
:::

That the tree-length appears as exponent is important to make the connection with weighted dependency graphs, which we discuss now.
