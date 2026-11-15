---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-008-31-sr-homological-invariants-of-22p1-torus-knots
section_title: "$S^r$ homological invariants of $(2,2p+1)$ torus knots"
section_number: 3.1
pages: 12-15
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.99
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
Our goal in this section is to compute the colored superpolynomials ${\cal P}^{R} (a,q,t)$ for $(2,2p+1)$ torus knots and symmetric and anti-symmetric representations, $R=S^r$ and $R=\Lambda^r$. In performing this calculation, we first review the analogous computation of the polynomial knot invariants (on the left side of Figure [\[fig:superpolunmial_hier\]](#fig:superpolunmial_hier){reference-type="ref" reference="fig:superpolunmial_hier"}) in Chern-Simons gauge theory and then "refine" it. We should stress right away, however, that the refined calculation is *not* done in a topological 3d gauge theory or, at least, such a 3d gauge theory interpretation of the formal steps that we are going to take is not known at present.

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

Here we will focus on the torus knots $T^{2,2p+1}$ in a 3-sphere and follow the steps of [@RGK]. Among various choices of the surface $\Sigma$, we will consider a slicing of ${\bf S}^3$ into a pair of 3-dimensional balls ${\bf B}^3$ connected by a cylinder, as in Figure [1](#Braid_Slice){reference-type="ref" reference="Braid_Slice"}. The physical Hilbert space ${\cal H}_{{\bf S}^2; R\, R \, \overline{R}\,\overline{R}}$ for this slice consists of conformal blocks for the four point function: $$\begin{aligned}
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

For a state $|\psi_0(R_1,R_2)\rangle\in {\cal H}_{{\bf S}^2;R_1R_2\overline{R}_2\overline{R}_1}$ associated with the lower half of the 3-ball in Figure [1](#Braid_Slice){reference-type="ref" reference="Braid_Slice"}, the following expansion can be considered: $$\begin{aligned}
|\psi_0(R_1,R_2)\rangle \; = \; \sum_{Q\in R_1\otimes R_2}\mu^Q_{R_1R_2}|\phi_{Q}(R_1,R_2,\overline{R}_2,\overline{R}_1)\rangle \,.
\label{three_ball}
\end{aligned}$$ The coefficient $\mu^Q_{R_1R_2}$ is determined by taking a pairing of this state with itself: $$\begin{aligned}
\langle \psi_0(R_1,R_2)|\psi_0(R_1,R_2)\rangle &=& \sum_{Q\in R_1\otimes R_2}\left(\mu^Q_{R_1R_2}\right)^2
\nonumber \\
&=& Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_1}{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_2};q) \,.
\end{aligned}$$ Since the two unknots here are not linked, we can separate them by an application of another slicing along a surface $\Sigma_2 \simeq {\bf S}^2$, as in Figure [3](#fig:Another_S2){reference-type="ref" reference="fig:Another_S2"}: $$Z_{SU(N)}^{\rm CS}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_1}{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_{R_2};q)
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

The state $|\psi_{2p+1}(R_1,R_2)\rangle$ associated with the top part of the picture [1](#Braid_Slice){reference-type="ref" reference="Braid_Slice"} is constructed by acting $2p+1$ times with the braid operator ${\cal B}_{R_1R_2}$ on the 3-ball state $|\psi_{0} (R_1,R_2)\rangle$: $$\begin{aligned}
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
