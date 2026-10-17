---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-006-3-examples-coming-from-knots
section_title: "Examples coming from knots"
section_number: 3
pages: 8-15
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.98
---
[]{#sec:knots label="sec:knots"}

In this section, we illustrate the refined / categorified volume conjectures stated in the general form in [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} and [\[VCparamref\]](#VCparamref){reference-type="eqref" reference="VCparamref"} for a large class of examples coming from knots. In these examples, the invariants $P_n (q,t)$ whose recursive behavior is captured by the conjectures encode the graded dimensions of the homological knot invariants.

There are many different kinds of homological knot invariants: doubly-graded and triply-graded, reduced and unreduced, with different choices of framing and grading conventions. And, in our discussion we will need at least a basic understanding of these concepts in order to have most fun with the conjectures ([\[VCquantref\]](#VCquantref){reference-type="ref" reference="VCquantref"}a) and ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a). In other words, we will need to have at least a rough understanding of the relation between different types of knot invariants shown in Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}. Luckily, much of this picture can be explained building on the relations between polynomial knot invariants, which hopefully are more familiar to the reader.

![Categorification of quantum knot invariants. To help the reader navigate through this picture we suggest to keep track of the variables $a$, $q$, $t$, as well as the rank of $sl(N)$. Note, the polynomial (resp. homological) knot invariants which have $a$-dependence (resp. $a$-grading) are *not* labeled by $sl(N)$.](categorification.eps){#fig:superpolunmial_hier width="4.0in"}

We start with the lower left corner of the Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"} that describes the simplest family of polynomial knot invariants $J^{\frak{g}, R} (K;q)$ labeled by a representation $R$ of a Lie algebra $\frak{g} = \text{Lie} (G)$. In the special case when $R = V_n$ is the $n$-dimensional representation of $\frak{g} = sl(2)$, the quantum group invariant $J_n (K;q) := J^{sl(2),V_n} (K;q)$ is the $n$-colored Jones polynomial of a knot/link $K$ that we already encountered in the review of the generalized volume conjectures [\[VCparam\]](#VCparam){reference-type="eqref" reference="VCparam"} and [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"}. In general, a mathematical definition of $J^{\frak{g}, R} (K;q)$ involves associating a quantum R-matrix to every crossing in a plane diagram of a knot $K$. Physically, these quantum group invariants are simply the normalized expressions for the partition function of Chern-Simons gauge theory [@Witten_Jones]: $$Z_{G}^{\text{CS}}(M,K_R;q)
\; := \; \int [dA] \, W_R(K)[A] \, e^{ik S_{\text{CS}}[A;M]}
\label{ZCSdef}$$ with a Wilson loop operator $W_R(K)[A]:={\rm Tr}_R \text{P} \exp\left[\oint_K A\right]$ supported on a knot $K$ and decorated by a representation $R$. Here, $S_{\rm CS}[A;M]$ is the famous Chern-Simons action functional on a 3-manifold $M$, $$\begin{aligned}
S_{\text{CS}}[A;M] \; = \; \frac{1}{4\pi}\int_M {\rm Tr}_{\text{adj}}
\left( A\wedge dA+\frac{2}{3}A\wedge A\wedge A\right) \,.
\label{SCSdef}
\end{aligned}$$ In general, the partition function [\[ZCSdef\]](#ZCSdef){reference-type="eqref" reference="ZCSdef"} is a rather complicated function of the coupling constant $k$ or, equivalently, the "quantum" parameter $q=e^{\frac{2\pi i}{k+h}}$. However, once normalized by that of the unknot, it magically becomes a polynomial in $q$ with integer coefficients, at least when $M={\bf S}^3$: $$\begin{aligned}
J^{\frak{g}, R} (K;q) \; =\; \frac{Z_{G}^{\rm CS}({\bf S}^3,K_R;q)}{Z_{G}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_R;q)} \,.
\label{JasZZratio}
\end{aligned}$$ The fact that the final result turns out to be a polynomial, let alone integer coefficients, is not at all obvious in either R-matrix or path integral formulation of $J^{\frak{g}, R} (K;q)$. This nice property, however, is a precursor of knot homologies, which beautifully explain it.

Another nice property comes from a closer look at $\frak{g} = sl(N)$, which will be the focus our paper. (Although there are straightforward analogs for other classical groups, we will not consider them here.) Then, not only $J^{sl(N), R} (K;q)$ turn out to be polynomials in $q$, they exhibit a very simple dependence on $N$. Namely, for each $R$ (= Young tableaux) there exists a polynomial invariant $P^R (K;a,q)$ of a knot $K$, such that $$J^{sl(N), R} (K;q) \; = \; P^R (K; a = q^N, q) \,.
\label{JfromP}$$ This relation is represented by a vertical arrow on the left in Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}. The polynomial $P^R (K;a,q)$ is called the colored HOMFLY polynomial of $K$. To be more precise, it is the *normalized* HOMFLY polynomial, meaning that $P^R ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}) = 1$.

Once we explained the left side of Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}, we can easily describe its categorification shown on the right. To categorify $J^{sl(N), R} (K;q)$ means to construct a doubly-graded homology theory ${\cal H }^{sl(N),R}_{i,j} (K)$, with gradings $i$ and $j$, such that the polynomial $J^{sl(N), R} (K;q)$ is its $q$-graded Euler characteristic: $$J^{sl(N), R} (K;q) \; = \; P^R (K; a = q^N, q) \; = \; \sum_{i,j} (-1)^j q^i \dim {\cal H }^{sl(N),R}_{i,j} (K) \,.
\label{JfromH}$$ Similarly, a categorification of $P^R (K;a,q)$ is a triply-graded homology theory ${\cal H }^{R}_{i,j,k} (K)$, with gradings $i$, $j$ and $k$, whose graded Euler characteristic is $$P^R (K;a,q) \; = \; \sum_{i,j,k} (-1)^k a^i q^j \dim {\cal H }^{R}_{i,j,k} (K) \,.
\label{PfromH}$$ The relations [\[JfromH\]](#JfromH){reference-type="eqref" reference="JfromH"} and [\[PfromH\]](#PfromH){reference-type="eqref" reference="PfromH"} are represented by horizontal arrows in Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}. Sometimes, it is convenient to express these relations as specializations of the corresponding Poincaré polynomials ${\cal P}^{sl(N),R} (q,t)$ and ${\cal P}^R (a,q,t)$ at $t=-1$. For example, the Poincaré polynomial of the triply-graded homology theory ${\cal H }^{R}_{i,j,k} (K)$ is defined as follows $$\text{``superpolynomial''} \qquad
{\cal P}^R (K; a,q,t) \; := \; \sum_{i,j,k} \, a^i q^j t^k \, \dim {\cal H }^{R}_{i,j,k} (K)
\label{superPdef}$$ and often is called the colored superpolynomial. To be more precise, just like below eq. [\[JfromP\]](#JfromP){reference-type="eqref" reference="JfromP"} we pointed out that $P^R (a,q) = {\cal P}^R (a,q,t=-1)$ is the *normalized* colored HOMFLY polynomial, it is important to emphasize that ${\cal P}^R (K; a,q,t)$ is the Poincaré polynomial of the *reduced* homology theory, in a sense that ${\cal P}^R ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}) = 1$.

If one naively combines [\[JfromH\]](#JfromH){reference-type="eqref" reference="JfromH"} and [\[PfromH\]](#PfromH){reference-type="eqref" reference="PfromH"} one may be tempted to conclude that ${\cal P}^{sl(N),R} (q,t)$ is a specialization of the superpolynomial at $a=q^N$, as was stated *e.g.* in [@AS] and in some other recent papers. We emphasize that, in general, this is *not* the case: $${\cal P}^R (a=q^N,q,t) \; \ne \;
{\cal P}^{sl(N),R} (q,t) \equiv \sum_{i,j} q^i t^j \dim {\cal H }^{sl(N),R}_{i,j} (K) \,.
\label{superwrong}$$ The reason is very simple and becomes crystal clear if one attempts to test [\[superwrong\]](#superwrong){reference-type="eqref" reference="superwrong"} even in the basic case of $N=1$ and, say, $R = \Box$. Indeed, the $sl(1)$ theory is trivial in any approach to knot polynomials / homologies. In other words, for any knot the $sl(1)$ homology ${\cal H }^{sl(1),\Box}_{i,j} (K)$ is one-dimensional and the corresponding quantum group invariant $J^{sl(1),\Box} (K;q)$ consists of a single monomial.

This fact has a nice manifestation in the relation [\[JfromP\]](#JfromP){reference-type="eqref" reference="JfromP"}, which says that almost all terms in the HOMFLY polynomial $P^{\Box} (a,q)$ cancel out in the specialization $a=q$, leaving behind a single term. This remarkable property of the HOMFLY polynomial can be viewed as a non-trivial constraint on the coefficients of the polynomial $P^{\Box} (a,q)$. Since the coefficients of $P^{\Box} (a,q)$ can be positive and negative, this condition indeed can be satisfied if the total number of "minuses" (counted with multiplicity) is balanced by the total number of "pluses."

This, of course, can not work for [\[superwrong\]](#superwrong){reference-type="eqref" reference="superwrong"} where the superpolynomial ${\cal P}^{\Box} (a,q,t)$ has only positive coefficients, due to [\[superPdef\]](#superPdef){reference-type="eqref" reference="superPdef"}. Therefore, setting $a=q$ will never reduce the total sum of the coefficients in this polynomial, and there is no way it can be equal to the Poincaré polynomial ${\cal P}^{sl(1),R} (q,t)$ of a one-dimensional homology ${\cal H }^{sl(1),R}_{i,j} (K)$.

A more conceptual reason why [\[superwrong\]](#superwrong){reference-type="eqref" reference="superwrong"} can not be true is that, while a specialization to $a=q^N$ is perfectly acceptable at the polynomial level (the left side of Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}), it has to be replaced by a suitable operation from homological algebra in order to make sense at the higher categorical level (the right side of Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}). As explained in [@DGR], the suitable operation, which categorifies the specializations $a=q^N$, involves taking homology in the triply-graded theory with respect to differentials $d_N$, $N \in {\mathbb Z}$. Indeed, the "extra terms" in the superpolynomial ${\cal P}^R (a,q,t)$ that are not part of ${\cal P}^{sl(N),R} (q,t)$ and otherwise would cancel upon setting $t=-1$ always come in pairs, so that a more proper version of [\[superwrong\]](#superwrong){reference-type="eqref" reference="superwrong"} reads $${\cal P}^R (a,q,t) \; = \;
R^{sl(N),R} (a,q,t) + (1 + a^{\alpha} q^{\beta} t^{\gamma}) Q^{sl(N),R} (a,q,t) \,,
\label{superright}$$ where $R^{sl(N),R} (a,q,t)$ and $Q^{sl(N),R} (a,q,t)$ are polynomials with non-negative coefficients, such that the $sl(N)$ homological invariant is a specialization of the "remainder" (not the full superpolynomial as in [\[superwrong\]](#superwrong){reference-type="eqref" reference="superwrong"}): $$R^{sl(N),R} (a=q^N,q,t) \; = \; {\cal P}^{sl(N),R} (q,t) \,,
\label{PRright}$$ whereas the extra pairs of terms in [\[superright\]](#superright){reference-type="eqref" reference="superright"} that come from $Q^{sl(N),R} (a,q,t)$ are killed by the differential $d_N$ of $(a,q,t)$-degree $(\alpha,\beta,\gamma)$.

Now, once we introduced the cast of characters and explained the relations between them, we can get straight down to business. We start in the next subsection with the calculation of colored superpolynomials for $(2,2p+1)$ torus. Then, in section [\[sec:knotrecursions\]](#sec:knotrecursions){reference-type="ref" reference="sec:knotrecursions"} we use the results of these calculations to derive and study the recursion relations, *a.k.a.* the quantum volume conjecture ([\[VCquantref\]](#VCquantref){reference-type="ref" reference="VCquantref"}a). Starting in section [\[sec:knotrecursions\]](#sec:knotrecursions){reference-type="ref" reference="sec:knotrecursions"}, we focus on the $a=q^2$ specializations of $S^r$-colored superpolynomial, which we denote as $$P_n (q,t) \; := \; {\cal P}^{S^{n-1}} (a=q^2,q,t) \,.
\label{Pq2special}$$ In section [\[sec:homological\]](#sec:homological){reference-type="ref" reference="sec:homological"} we present some evidence that in the refined volume conjectures [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} and [\[VCparamref\]](#VCparamref){reference-type="eqref" reference="VCparamref"} one can replace this definition of $P_n (q,t)$ with a true $sl(2)$ homological knot invariant [\[Pnoptimistic\]](#Pnoptimistic){reference-type="eqref" reference="Pnoptimistic"}. Finally, in section [\[sec:knotS0\]](#sec:knotS0){reference-type="ref" reference="sec:knotS0"} we consider the classical limit and discuss the leading "volume" term $S_0 (u,t)$ that dominates the asymptotic behavior ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a) of these homological knot invariants. According to [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}, this semi-classical limit is controlled by the $t$-deformed algebraic curve, $A^{\text{ref}} (x,y;t) = 0$, whose quantization will be revisited in section [\[sec:quantizability\]](#sec:quantizability){reference-type="ref" reference="sec:quantizability"}.

In a physical realization of knot homologies [@GSV], the superpolynomial ${\cal P}^{S^{n-1}} (a,q,t)$ and its specialization [\[Pq2special\]](#Pq2special){reference-type="eqref" reference="Pq2special"} are certain indices that count refined BPS invariants, essentially identical to $Z_{\text{BPS}}^{\text{open}} (u,q,t)$ where $u = q^n$. Motivated by this, in the later section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"} we perform a similar analysis of more general refined open BPS partition functions and find many similar patterns.

## $S^r$ homological invariants of $(2,2p+1)$ torus knots

Our goal in this section is to compute the colored superpolynomials ${\cal P}^{R} (a,q,t)$ for $(2,2p+1)$ torus knots and symmetric and anti-symmetric representations, $R=S^r$ and $R=\Lambda^r$. In performing this calculation, we first review the analogous computation of the polynomial knot invariants (on the left side of Figure [1](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}) in Chern-Simons gauge theory and then "refine" it. We should stress right away, however, that the refined calculation is *not* done in a topological 3d gauge theory or, at least, such a 3d gauge theory interpretation of the formal steps that we are going to take is not known at present.

In Chern-Simons gauge theory, one can efficiently compute [\[ZCSdef\]](#ZCSdef){reference-type="eqref" reference="ZCSdef"} using the topological invariance of the theory. Dividing a 3-manifold $M$ into two pieces $M_1$ and $M_2$ along a surface $\Sigma$, one can express the partition function $Z_{SU(N)}^{\rm CS}(M,K_R;q)$ as a pairing between the two elements $|\psi_{M_1;K_R}\rangle$ and $|\psi_{M_2;K_R}\rangle$ in the physical Hilbert space ${\cal H}_{\Sigma}$: $$\begin{aligned}
Z_{SU(N)}^{\rm CS}(M,K_R;q)={}_{\Sigma}\langle \psi_{M_2;K_R}|\psi_{M_1;K_R}\rangle_{\Sigma} \,.
\label{ZHilbert}
\end{aligned}$$ The physical Hilbert space ${\cal H}_{\Sigma}$ is obtained by the canonical quantization of the Chern-Simons gauge theory on $\Sigma\times \mathbb{R}$, and the following correspondence is found in [@Witten_Jones; @EMSS]:

::: center
${\cal H}_{\Sigma} \; \simeq \; \bigl\{$ conformal blocks for $G/G$ WZW model on $\Sigma~\bigr\}$,
:::

where $G=SU(N)$. If the knot $K_R$ meets the surface $\Sigma$ at $m$ points, the physical Hilbert space ${\cal H}_{\Sigma;R_1\cdots R_m}$ consists of conformal blocks for $m$-point functions which carry representations $R_a = R$ or $\overline{R}$ ($a=1,\cdots ,m$) depending on the orientation at the intersection.

<figure id="Braid_Slice">
<div class="center">
<embed src="braid.eps" style="width:8cm" />
</div>
<figcaption>Slicing and braiding.</figcaption>
</figure>

Here we will focus on the torus knots $T^{2,2p+1}$ in a 3-sphere and follow the steps of [@RGK]. Among various choices of the surface $\Sigma$, we will consider a slicing of ${\bf S}^3$ into a pair of 3-dimensional balls ${\bf B}^3$ connected by a cylinder, as in Figure [2](#Braid_Slice){reference-type="ref" reference="Braid_Slice"}. The physical Hilbert space ${\cal H}_{{\bf S}^2; R\, R \, \overline{R}\,\overline{R}}$ for this slice consists of conformal blocks for the four point function: $$\begin{aligned}
\phi_Q(R,R,\overline{R},\overline{R}),\quad Q\in R\otimes R,
\end{aligned}$$ whose the intermediate state carries an irreducible representation $Q \in R\otimes R$. In general, ${\cal H}_{{\bf S}^2; R_1 R_2 R_3 R_4}$ is spanned by orthonormal states: $$\begin{aligned}
\langle\phi_{Q^{\prime}}(R_1,R_2,R_3,R_4)
|\phi_{Q}(R_1,R_2,R_3,R_4)\rangle=\delta_{QQ^{\prime}},\quad
Q,Q^{\prime}\in R_1\otimes R_2.
\end{aligned}$$

<figure id="fig:Conf_block">
<div class="center">
<embed src="block.eps" style="width:5cm" />
</div>
<figcaption>Conformal block <span class="math inline">$\phi_{Q^{\prime}}(R_1,R_2,\overline{R}_3,\overline{R}_4)$</span> for the four point function.</figcaption>
</figure>

For a state $|\psi_0(R_1,R_2)\rangle\in {\cal H}_{{\bf S}^2;R_1R_2\overline{R}_2\overline{R}_1}$ associated with the lower half of the 3-ball in Figure [2](#Braid_Slice){reference-type="ref" reference="Braid_Slice"}, the following expansion can be considered: $$\begin{aligned}
|\psi_0(R_1,R_2)\rangle \; = \; \sum_{Q\in R_1\otimes R_2}\mu^Q_{R_1R_2}|\phi_{Q}(R_1,R_2,\overline{R}_2,\overline{R}_1)\rangle \,.
\label{three_ball}
\end{aligned}$$ The coefficient $\mu^Q_{R_1R_2}$ is determined by taking a pairing of this state with itself: $$\begin{aligned}
\langle \psi_0(R_1,R_2)|\psi_0(R_1,R_2)\rangle &=& \sum_{Q\in R_1\otimes R_2}\left(\mu^Q_{R_1R_2}\right)^2
\nonumber \\
&=& Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_1}{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_2};q) \,.
\end{aligned}$$ Since the two unknots here are not linked, we can separate them by an application of another slicing along a surface $\Sigma_2 \simeq {\bf S}^2$, as in Figure [4](#fig:Another_S2){reference-type="ref" reference="fig:Another_S2"}: $$Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_1}{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_2};q)
Z_{SU(N)}^{\rm CS}({\bf S}^3;q)
\; = \; Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_1};q)
Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_2};q).$$

<figure id="fig:Another_S2">
<div class="center">
<embed src="surj.eps" style="width:15cm" />
</div>
<figcaption>Slicing along <span class="math inline">$\Sigma_2 \simeq {\bf S}^2$</span>.</figcaption>
</figure>

The partition function of the unknot ${\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_R$ in ${\bf S}^3$ is given by the quantum dimension: $$\frac{Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R};q)}
{Z_{SU(N)}^{\rm CS}({\bf S}^3;q)} \; = \; \dim_q R \,.
\label{unknotdimqR}$$ Here, the quantum dimension $\dim_qR$ is a specialization of the Schur polynomial $s_R(x)$: $$\dim_q R \; = \; s_R(q^{\varrho}),\quad \varrho=(\varrho_1,\cdots,\varrho_N),\quad \varrho_i=\frac{N+1}{2}-i \,,
\label{dimqRsR}$$ which enjoys the following identity: $$s_{R_1}(x)s_{R_2}(x) \; = \sum_{Q\in R_1\otimes R_2}s_Q(x) \,.
\label{irr_decomp_schur}$$ Using these relations, the coefficient $\mu_Q$ can be determined as: $$\left(\mu^Q_{R_1R_2}\right)^2
\; = \; s_Q(q^{\varrho})\cdot Z_{SU(N)}^{\rm CS}({\bf S}^3;q) \,.
\label{muCS}$$

The state $|\psi_{2p+1}(R_1,R_2)\rangle$ associated with the top part of the picture [2](#Braid_Slice){reference-type="ref" reference="Braid_Slice"} is constructed by acting $2p+1$ times with the braid operator ${\cal B}_{R_1R_2}$ on the 3-ball state $|\psi_{0} (R_1,R_2)\rangle$: $$\begin{aligned}
|\psi_{2p+1}(R_1,R_2)\rangle \; = \; {\cal B}_{R_1R_2}^{2p+1}|\psi_{0}(R_1,R_2) \rangle \,.
\end{aligned}$$ The action of the braid operator ${\cal B}_{R_1R_2}$ on the conformal block $\phi_Q(R_1,R_2,R_3,R_4)$ obeys a monodromy transformation. The eigenvalue of the monodromy for the conformal block is determined by the conformal weights $h_{R_a}$ of primary states in the $G/G$ WZW model [@Moore_Seiberg]: $$\begin{aligned}
\lambda_Q^{\prime}(R_1,R_2) \; = \;
\epsilon_{R_1R_2}^Qe^{\pi i(h_{R_1}+h_{R_2}-h_Q)}
\; = \; \epsilon_{R_1R_2}^Qq^{\frac{1}{2}(C_2(R_1)+C_2(R_2)-C_2(Q))} \,.
\end{aligned}$$ The quadratic Casimir $C_2(R)$ for a representation $R$ of $SU(N)$ is given by $$\begin{aligned}
C_2(R) \;= \; \frac{1}{2}\left(\kappa_R+N |R|-\frac{|R|^2}{N}\right) \,,
\end{aligned}$$ where $R_i$ denotes the number of boxes in the $i$-th row of the Young diagram for the representation $R$, and $|R|:=\sum_i R_i$, and $\kappa_R=|R|+\sum_iR_i(R_i-2i)$. The sign $\epsilon_{R_1R_2}^Q=\pm 1$ is determined by whether $Q$ appears symmetrically or antisymmetrically in $R_1\otimes R_2$. In order to keep the canonical framing for the Chern-Simons partition function, it is necessary to make a correction to the eigenvalue for the braid operator by a factor $q^{\frac{1}{2}(C_2(R_1)+C_2(R_1)+|C_2(R_1)-C_2(R_2)|)}$ [@RGK; @Witten_Jones]. Therefore, the resulting eigenvalue of the braid operator is given by $$\begin{aligned}
\lambda_Q^{(+)}(R_1,R_2)=\epsilon_{R_1R_2}^Qq^{C_2(R_1)+C_2(R_2)+|C_2(R_1)-C_2(R_2)|/2-C_2(Q)/2} \,.
\label{unrefeigl}
\end{aligned}$$

Combining the above formulae, we can evaluate the braid operator ${\cal B}_{RR}^{2p+1}$ sandwiched between two 3-ball states $|\psi_0(R,R)\rangle$: $$\begin{aligned}
Z_{SU(N)}^{\rm CS}({\bf S}^3,T^{2,2p+1}_R;q)
& =& \langle \psi_0(R,R)|{\cal B}_{RR}^{2p+1}|\psi_0(R,R)\rangle
\label{ZT22p1braid} \\
& = & \sum_{Q\in R\otimes R}\lambda^{(+)}_Q(R,R)^{2p+1}\left(\mu^Q_{RR}\right)^2
\nonumber \\
& = & Z_{SU(N)}^{\rm CS}({\bf S}^3;q)\sum_{Q \in R \otimes R}\lambda^{(+)}_Q(R,R)^{2p+1}{\rm dim}_qQ \,.
\nonumber
\end{aligned}$$ Our next goal is to categorify / refine this computation.

In practice, this will amount to replacing every ingredient with its analog that depends not only on $q$, but also on the new variable $t$ or, rather, two variables $q_1$ and $q_2$ (that are related to $q$ and $t$ via a simple change of variables [\[GSvarchng\]](#GSvarchng){reference-type="eqref" reference="GSvarchng"}): $$\begin{aligned}
\underline{\text{~~CS gauge theory~~}} && \underline{\text{~~refined invariants~~}}
\nonumber \\
Z_{SU(N)}^{\rm CS}({\bf S}^3,K_R;q)
&\qquad \leadsto \qquad&
Z^{\text{ref}}_{SU(N)}({\bf S}^3,K_R;q_1,q_2)
\nonumber \\
\dim_q R = s_R(q^{\varrho})
&\qquad \leadsto \qquad&
M_R(q_2^{\varrho};q_1,q_2)
\nonumber \\
q^{C_2(R)}
&\qquad \leadsto \qquad&
q_1^{\frac{1}{2}||R||^2}q_2^{-\frac{1}{2}||R^{t}||^2}q_2^{\frac{N}{2}|R|}q_1^{-\frac{1}{2N}|R|^2}
\label{Casimir_ref} \\
& \vdots & \nonumber
\end{aligned}$$
