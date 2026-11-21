---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-028-43-refinement-as-a-twisted-mass-parameter
section_title: "Refinement as a twisted mass parameter"
section_number: 4.3
pages: 63-68
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.997
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
Now, let us discuss the physical interpretation of the general setup considered in this section and the corresponding interpretation of the classical action $S_0 (u,t)$.

As we already reviewed in the beginning of this section, compactification of type II string theory on a toric Calabi-Yau 3-fold $X$ is a natural arena for a "geometric engineering" of ${\mathcal{N}}=2$ supersymmetric gauge theories in the remaining four space-time dimensions. In this setup, BPS states of the "effective" four-dimensional gauge theory are simply the closed BPS states from the vantage point of the Calabi-Yau 3-fold $X$. Moreover, counting *refined* closed BPS states means that, from the viewpoint of the 4d ${\mathcal{N}}=2$ theory, we keep track of their spin $j_3$.

Much of our interest comes from counting *open* refined BPS states in a slight generalization of this setup, with a D4-brane added: $$\begin{matrix}
{\mbox{\rm space-time:}} & \qquad & {\mathbb R}^4 & \times & X \\
& \qquad & \cup &  & \cup \\
{\mbox{\rm D4-brane:}} & \qquad & {\mathbb R}^2 & \times & L
\end{matrix}
\label{surfeng}$$ Since the extra D4-brane here is supported on a special Lagrangian submanifold $L \subset X$, it preserves half of the supersymmetry and, as explained in [@DGH], yields a "geometric engineering" of a half-BPS surface operator in ${\mathcal{N}}=2$ gauge theory on ${\mathbb R}^4$ (see [@Ramified; @Gknothom; @Rigid] for a purely field theoretic definition of surface operators). In a special case when $X$ is the conifold and $L_K$ is the Lagrangian submanifold associated to a knot $K$, the system [\[surfeng\]](#surfeng){reference-type="eqref" reference="surfeng"} becomes identical to the physical setup [\[theoryB\]](#theoryB){reference-type="eqref" reference="theoryB"} discussed in section [\[sec:knots\]](#sec:knots){reference-type="ref" reference="sec:knots"}, after compactification on a circle from M-theory to type IIA string theory.

From the viewpoint of the ${\mathcal{N}}=2$ gauge theory on ${\mathbb R}^4$, the generating function of open BPS invariants $Z_{\text{BPS}}^{\text{open}}$ that plays a central role in this section can be interpreted as the instanton partition function of the gauge theory in the presence of a surface operator [@DGH; @Braverman; @AGGTV; @AFKMY], much like its "closed" counterpart $Z_{\text{BPS}}^{\text{closed}}$ is the K-theory version of the equivariant instanton counting on ${\mathbb R}^4$ without surface operators [@Nekrasov; @NYlectures].

Let $SO(2)_1 \times SO(2)_2$ be the rotation symmetry of ${\mathbb R}^4$ preserved by the surface operator in [\[surfeng\]](#surfeng){reference-type="eqref" reference="surfeng"}, such that $SO(2)_2$ is the rotation symmetry along the ${\mathbb R}^2 \subset {\mathbb R}^4$ and $SO(2)_1$ is the rotation symmetry of its normal bundle. Note, from the viewpoint of the Euclidean ${\mathcal{N}}=(2,2)$ theory on the surface operator, $SO(2)_2$ is a rotation symmetry (part of the two-dimensional Poincaré group), while $SO(2)_1$ is a global R-symmetry. In fact, both symmetries in this brane system were already discussed in section [\[sec:refinedbraid\]](#sec:refinedbraid){reference-type="ref" reference="sec:refinedbraid"}, where we gave them a name $U(1)_P$ and $U(1)_F$, respectively. In particular, the global R-symmetry is: $$U(1)_F \; \cong \; SO(2)_1
\label{U1Fso2}$$

If, as usual, we denote by $\epsilon_1$ and $\epsilon_2$ the equivariant parameters for $SO(2)_1$ and $SO(2)_2$, respectively, then the generating functions $Z_{\text{BPS}}^{\text{closed}}$ and $Z_{\text{BPS}}^{\text{open}}$ are known to have the following form, see *e.g.* [@KreflWalcher; @KlemmHuang]: $$\begin{aligned}
Z_{\text{BPS}}^{\text{closed}} (\epsilon_1, \epsilon_2)
& = & \exp \Bigl(\, \frac{1}{\epsilon_1 \epsilon_2} {\mathcal{F}}(\epsilon_1, \epsilon_2) \, \Bigr) \label{ZclosedW} \\
& = & \exp \Bigl(\, \frac{1}{\epsilon_1 \epsilon_2} {\mathcal{F}}^{(0)}
+ \frac{\epsilon_1 + \epsilon_2}{\epsilon_1 \epsilon_2} {\mathcal{F}}^{(1)} + \ldots \, \Bigr) \nonumber
\end{aligned}$$ and $$Z_{\text{BPS}}^{\text{open}} (\epsilon_1, \epsilon_2)
\; = \; \exp \Bigl(\, \frac{1}{\epsilon_2} \widetilde{\cal W} + \ldots  \, \Bigr)
\label{ZopenW}$$ where ${\mathcal{F}}^{(0)}$ is the prepotential of the four-dimensional ${\mathcal{N}}=2$ theory and $\widetilde{\cal W}$ is the twisted superpotential of the two-dimensional ${\mathcal{N}}=(2,2)$ theory on the surface operator. In particular, as explained in [@AGGTV] (see also [@AwataYamada; @TakiMaruyoshi; @AFKMY]), the twisted superpotential is given by the integral of the Seiberg-Witten differential $v du = \log y \frac{dx}{x}$ over a path: $$\widetilde{\cal W} (u) \; = \; \int^u v du$$ on the curve $A(x,y)=0$.

Now, let us explain how our discussion in this paper compares to the Nekrasov-Shatashvili limit and its relation to quantum integrable systems. There are some similarities and some differences, and both are important. First, the limit considered in [@NS] in our notations is $\epsilon_1 = 0$ with $\epsilon_2$ playing the role of the quantization parameter (in the quantum integrable system). This is very similar to the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"} and the discussion in this section, where $\hbar = - \epsilon_2$ also plays the role of the quantization parameter and the only essential difference is that $\epsilon_1$ (equivalently, $q_1 = e^{\epsilon_1}$) is allowed to take any finite values, so that for small $\hbar$ we have $t = - \frac{q_1}{q_2} \sim - q_1$. In this respect, what we consider can be viewed as a refinement of the Nekrasov-Shatashvili limit, *cf.* Figure [\[fig:qqqt\]](#fig:qqqt){reference-type="ref" reference="fig:qqqt"}.

There is an important difference, however, which has to do with the fact that [@NS] consider the partition function of the 4d gauge theory or, from the vantage point of the Calabi-Yau 3-fold $X$, the generating function of *closed* BPS invariants [\[ZclosedW\]](#ZclosedW){reference-type="eqref" reference="ZclosedW"}. In particular, the Yang-Yang function of the quantum integrable system is identified with the following limit of the instanton partition function in the absence of any surface operators [@NS]: $$\lim_{\epsilon_1 \to 0} \, \epsilon_1 \, \log Z_{\text{BPS}}^{\text{closed}} (\epsilon_1, \epsilon_2)
\; = \; \frac{1}{\epsilon_2} {\mathcal{F}}^{(0)} + {\mathcal{F}}^{(1)} + {\cal O }(\epsilon_2)
\label{YangYang}$$ This expansion should not be confused with a similar-looking expansion in [\[ZopenW\]](#ZopenW){reference-type="eqref" reference="ZopenW"}, which describes the behavior of the *open* BPS partition function or, from the gauge theory viewpoint, represents the contribution of a surface operator. In particular, the leading term ${\mathcal{F}}^{(0)}$ in [\[YangYang\]](#YangYang){reference-type="eqref" reference="YangYang"} depends only on the closed string moduli, whereas a similar leading term $\widetilde{\cal W}$ in [\[ZopenW\]](#ZopenW){reference-type="eqref" reference="ZopenW"} depends on both open and closed string moduli. Thus, the variable $u$ in our discussion or, equivalently, $x = e^u$ is an open string modulus.

Keeping these remarks in mind, we can express the refined volume conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}b) as a statement that the free energy $\log Z_{\text{BPS}}^{\text{open}} (q_1, q_2)$ has a first-order pole in the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"}: $$\log Z_{\text{BPS}}^{\text{open}} (\epsilon_1, \epsilon_2)
\; = \; \frac{S_0 (u,t)}{\hbar} + \ldots
\qquad \text{as~~} \boxed{ \phantom{I} q_2 = e^{\hbar} \to 1
\text{~and~} \frac{q_1}{q_2} = - t = \text{finite}~}~ \,,
\label{logZopenSt}$$ where we used [\[qqqt\]](#qqqt){reference-type="eqref" reference="qqqt"}. This, at the same time, is both *open* and *refined* generalization of [\[YangYang\]](#YangYang){reference-type="eqref" reference="YangYang"}. In particular, in the special case $t = -1$ (or, equivalently, $q_1 = 1$) we recover [\[ZopenW\]](#ZopenW){reference-type="eqref" reference="ZopenW"}, with the twisted superpotential $$\widetilde{\cal W} (u) \; = \; S_0 (u,-1) \,.$$ Therefore, we conclude that $S_0 (u,t)$ which appears in the refined volume conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}b) is a "refinement" of the twisted superpotential in the ${\mathcal{N}}=(2,2)$ surface operator theory[^1] with a twisted mass for the global symmetry $U(1)_F$ (= rotation in the plane orthogonal to the surface operator), *cf.* [\[ZrefdefP\]](#ZrefdefP){reference-type="eqref" reference="ZrefdefP"}: $$\tilde m_F \; = \; \log (-t) \,.
\label{mftrel}$$ As a simple example, let us consider a two-dimensional ${\mathcal{N}}=(2,2)$ theory with a tower of Kaluza-Klein states obtained by reducing a three-dimensional ${\mathcal{N}}=2$ chiral multiplet on a circle. The twisted superpotential of this theory has the familiar form $\widetilde{\cal W} = \textrm{Li}_2(-t x)$, where we assumed that the 3d chiral multiplet on ${\mathbb R}^2 \times {\bf S}^1$ has charge $+1$ with respect to both $U(1)_F$ as well as the global $U(1)$ symmetry with twisted mass $\log x$. Therefore, in the twisted superpotential [\[S0conifold\]](#S0conifold){reference-type="eqref" reference="S0conifold"} we can recognize a contribution of two chiral multiplets. Similarly, in the expression [\[S0C3\]](#S0C3){reference-type="eqref" reference="S0C3"} for the tetrahedron (or ${\mathbb C}^3$) we recognize contribution of a single chiral multiplet. In general, the number of chiral multiplets is equal to the number of dilogarithms in $S_0 (u,t)$, and the charges of chiral multiplets are simply the powers of $t$ and $x$ in the arguments of these dilogarithms. It is easy to recognize such contributions *e.g.* in [\[Pn-saddle\]](#Pn-saddle){reference-type="eqref" reference="Pn-saddle"}.

To summarize, each chiral multiplet in the D4-brane theory [\[surfeng\]](#surfeng){reference-type="eqref" reference="surfeng"} (or, to be more precise, in the five-brane theory on a circle, *cf.* [\[theoryB\]](#theoryB){reference-type="eqref" reference="theoryB"}) contributes to the twisted chiral superpotential a dilogarithm term: $$\text{tetrahedron}~\Delta
\qquad \leftrightarrow \qquad
\text{chiral}~\phi
\qquad \leftrightarrow \qquad
\begin{array}{l}
\text{twisted superpotential} \\[.1cm]
S_0 (\Delta; \vec u, t) = \textrm{Li}_2( e^{\vec n \cdot \vec u + n_F \, \tilde m_F} )
\end{array}$$ where $n_F$ is the charge of the chiral multiplet under the global R-symmetry [\[U1Fso2\]](#U1Fso2){reference-type="eqref" reference="U1Fso2"} and $\vec n$ denotes the charges of the chiral multiplet under all other flavor symmetries (with twisted mass parameters $\vec u$). Here, we also identified the example of a single chiral multiplet (or ${\mathbb C}^3$) discussed in the present section with a single tetrahedron in examples coming from 3-manifolds, *cf.* [@DGH; @DGSdual; @abmodel; @DGG; @CCV].

::: {#tab-nF}
    **Model**     values of $n_F^i$
  ------------- ----------------------
     unknot         $0$, $3$, $3$
   tetrahedron           $1$
    conifold     $1$, $- \frac{1}{2}$

  : Values of $n_F^i$ in prominent examples.
:::

More generally, one can consider a three-dimensional ${\mathcal{N}}=2$ theory $\mathcal{T}$ that contains $N_f$ chiral multiplets $\phi_i$, $i=1, \ldots, N_f$ with charges $n^i_a$ under global flavor symmetries $U(1)_a$, $a = 1, \ldots, N$. This could be either a low-dimensional effective field theory in brane systems [\[theoryB\]](#theoryB){reference-type="eqref" reference="theoryB"} and [\[surfeng\]](#surfeng){reference-type="eqref" reference="surfeng"}, or a three-dimensional ${\mathcal{N}}=2$ theory $T_M$ associated to a triangulation of a 3-manifold $M$, $$M \; = \; \bigcup_i \, \Delta_i \,.$$ In either case, the refinement is achieved by assigning each chiral multiplet $\phi_i$ (resp. each tetrahedron $\Delta_i$) one extra charge $n_F^i$ that describes how $\phi_i$ transforms under the R-symmetry $U(1)_F$, which may already be a part of $\prod_a U(1)_a$. Then, using [\[mftrel\]](#mftrel){reference-type="eqref" reference="mftrel"}, we conclude that passing from unrefined theory to refined theory has the effect of introducing the $t$-dependence in the classical "volume functional" (= twisted superpotential) via a simple rule: $$\widetilde{\cal W} (x_i) = \sum_i \textrm{Li}_2 \big( \prod_a x_a^{n_a^i} \big)
\quad \leadsto \quad
S_0 (x_i, t) = \sum_i \; \textrm{Li}_2 \; \Big( (-t)^{n_F^i} \prod_a x_a^{n_a^i} \Big)$$ modulo logarithmic ambiguities that depend on choices of framing, polarization, *etc.* In other words, at least in such models, the essential information about the refinement is contained in a set of charges $\{ n_F^i \}$ that need to be assigned to chiral multiplets or, in the language of 3-manifolds, to tetrahedra $\Delta_i$. While many examples are considered in the present paper (see Table [1](#tab-nF){reference-type="ref" reference="tab-nF"}), a systematic rule for assigning $\{ n_F^i \}$ will be presented in the follow-up work.

[^1]: To be more precise, it is a three-dimensional ${\mathcal{N}}=2$ theory on a circle that is relevant to the K-theoretic version of the vortex partition function [@DGH].
