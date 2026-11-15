---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-009-311-refined-braid-operators-and-gamma-factors
section_title: "Refined braid operators and gamma factors"
section_number: 3.1.1
pages: 15-19
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.997
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
[]{#sec:refinedbraid label="sec:refinedbraid"}

A physical framework for knot homologies was first proposed in [@GSV] and later studied from various viewpoints and in a number of closely related systems in [@Gknothom; @Wknothom; @DGH; @AS]. Regardless of the details and duality frames used, the basic idea is that a graded vector space ${\cal H }^{R} (K)$ associated to a knot $K$ colored by a representation $R$ is identified with the space of refined BPS invariants that carry information not only about the charge of the BPS state but also about the spin content: $${\cal H }^R (K) \; = \; {\cal H }^{\text{ref}}_{\text{BPS}} \, .
\label{HHBPS}$$ This interpretation can be used for performing concrete computations [@GIKV; @AS; @IK11] (see also [@Taki:2008hb; @Awata:2009yc; @Awata:2009sz] and [@Carqueville:2011sj; @ORSG; @Aganagic:2012au]) as well as for studying the structure of ${\cal H }^{\frak g, R}_{i,j} (K)$ for various $\frak g$ and $R$ [@GWalcher; @GS]. In this section, we will use both methods -- based on concrete formulas for torus knots and on structural properties for arbitrary knots -- to compute colored HOMFLY homology and colored superpolynomials of $(2,2p+1)$ torus knots. Furthermore, the physical interpretation of the homological knot invariants in terms of the refined (*a.k.a.* motivic) BPS invariants is what will ultimately allow us to treat the latter in more general systems on the same footing, *cf.* section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"}.

First, let us recall the five-brane configuration relevant to the physical description of the $sl(N)$ knot homologies [@GSV; @Gknothom; @Wknothom]: $$\begin{aligned}
\text{space-time} & : & \qquad {\mathbb R}\times T^* {\bf S}^3 \times M_4 \nonumber \\
N~\text{M5-branes} & : & \qquad {\mathbb R}\; \times \; {\bf S}^3 \; \times \; D \label{theoryA} \\
|R|~\text{M5-branes} & : &  \qquad {\mathbb R}\; \times \; L_K \; \times \; D \nonumber
\end{aligned}$$ where $L_K$ is the total space of the conormal bundle to $K \subset {\bf S}^3$ in the Calabi-Yau space $T^* {\bf S}^3$, and in most of applications one usually takes $D \cong {\mathbb R}^2$ and $M_4 \cong {\mathbb R}^4$. See *e.g.* [@GS] for further details, references, and the outline of the relation between different ways of looking at this physical system.

The precise form of the 4-manifold $M_4$ and the surface $D \subset M_4$ is not important, as long as they enjoy $U(1)_F \times U(1)_P$ symmetry action, where the first (resp. second) factor is a rotation symmetry of the normal (resp. tangent) bundle of $D \subset M_4$. Following [@Wknothom], let us denote the corresponding quantum numbers by $F$ and $P$. These quantum numbers were denoted, respectively, by $2 S_1$ and $2(S_1 - S_2)$ in [@AS] and by $2 j_3$ and $n$ in [@GS].

Something special happens when $K = T^{m,n}$ is a torus knot. Then, as pointed out in [@AS], the five-brane theory in [\[theoryA\]](#theoryA){reference-type="eqref" reference="theoryA"} has an extra $R$-symmetry $U(1)_R$ that acts on ${\bf S}^3$ leaving the knot $K = T^{p,q}$ and, hence, the Lagrangian $L_K \subset T^* {\bf S}^3$ invariant. Following [@AS], we denote the quantum number corresponding to this symmetry by $S_R$, and also introduce the partition function $$Z^{\text{ref}}_{SU(N)}({\bf S}^3, T^{m,n}_R; q, t) \; := \; {\rm Tr \,}_{{\cal H }^{\text{ref}}_{\text{BPS}}} \; (-1)^{S_R} q^{P} t^{F - S_R}
\label{Zrefdef}$$ that "counts" refined BPS states in the setup [\[theoryA\]](#theoryA){reference-type="eqref" reference="theoryA"}. A priori, this partition function is different from the Poincaré polynomial of the $sl(N)$ knot homology, which in these notations reads $${\cal P}^{sl(N), R} (K;q,t) \; = \; {\rm Tr \,}_{{\cal H }^{\text{ref}}_{\text{BPS}}} \; q^{P} t^{F} \,.
\label{ZrefdefP}$$ However, it was argued in [@AS] that for some torus knots all refined BPS states [\[HHBPS\]](#HHBPS){reference-type="eqref" reference="HHBPS"} have $S_R=0$ and the two expressions actually agree.

Similarly, in a dual description after the geometric transition the setup [\[theoryA\]](#theoryA){reference-type="eqref" reference="theoryA"} turns into a system $$\begin{aligned}
\text{space-time} & : & \qquad {\mathbb R}\times X \times M_4 \label{theoryB} \\
\text{M5-branes} & : &  \qquad {\mathbb R}\times L_K \times D \nonumber
\end{aligned}$$ where $X$ is the total space of the ${\cal O }(-1) \oplus {\cal O }(-1)$ bundle over ${\mathbb{C}}{\mathbf{P}}^1$, and BPS states carry a new quantum number which becomes the $a$-grading of ${\cal H }^{\text{ref}}_{\text{BPS}} = {\cal H }^R_{i,j,k} (K)$. One of the main results in [@AS] is that this space has *four* gradings: in addition to the $a$-, $q$- and $t$-grading that in the physics setup correspond to the "winding number" $\beta \in H_2 (X,L_K) \cong {\mathbb Z}$, and to the quantum numbers $P$ and $F$, the space ${\cal H }_{BPS} = {\cal H }^R_{i,j,k} (K)$ has the fourth grading, by $S_R \in {\mathbb Z}$.

Therefore, one of the interesting features of the refined Chern-Simons theory is that it predicts a new grading on the homology of torus knots and links, thereby upgrading ${\cal H }^{sl(N),R}_{i,j} (K)$ to a triply-graded theory (labeled by $\frak g$ and $R$) and similarly upgrading ${\cal H }^{R}_{i,j,k} (K)$ to a homology theory with as much as *four* gradings! It would be very interesting to study these new extra gradings in other formulations of knot homologies. Some hints for the extra gradings of torus knot homologies seem to appear in [@Cherednik].

After the geometric transition, the partition function analogous to [\[Zrefdef\]](#Zrefdef){reference-type="eqref" reference="Zrefdef"} "counts" refined BPS states in the setup [\[theoryB\]](#theoryB){reference-type="eqref" reference="theoryB"}: $$Z^{\text{ref}} ({\bf S}^3, T^{m,n}_R; a, q, t) \; = \; {\rm Tr \,}_{{\cal H }^{\text{ref}}_{\text{BPS}}} \; (-1)^{S_R} a^{\beta} q^{P} t^{F - S_R} \,.
\label{Zrefdefa}$$ When all refined BPS states have $S_R=0$ -- which, following [@AS], will be our working assumption here -- this expression coincides with the colored superpolynomial [\[superPdef\]](#superPdef){reference-type="eqref" reference="superPdef"}, which in these notations reads ${\cal P}^{R} (K;a,q,t) = {\rm Tr \,}_{{\cal H }^{\text{ref}}_{\text{BPS}}} \; a^{\beta} q^{P} t^{F}$. This will be our strategy for obtaining the colored superpolynomials of $(2,2p+1)$ torus knots. In fact, via the relation with refined BPS invariants, we will essentially do the computation twice: first, via direct calculation of the refined Chern-Simons partition function [\[Zrefdef\]](#Zrefdef){reference-type="eqref" reference="Zrefdef"} and its large $N$ version [\[Zrefdefa\]](#Zrefdefa){reference-type="eqref" reference="Zrefdefa"}, and then, in section [\[sec:homological\]](#sec:homological){reference-type="ref" reference="sec:homological"}, by using the structural properties of [\[HHBPS\]](#HHBPS){reference-type="eqref" reference="HHBPS"} that follow from physics.\
Although refined Chern-Simons theory is *not* a gauge theory,[^1] its partition function can be evaluated by mimicking the steps in the ordinary Chern-Simons theory. In particular, one can define "refined analogs" of the $S$ and $T$ modular matrices and the braid operator ${\cal B}_{R_1 R_2}$ used in [\[ZT22p1braid\]](#ZT22p1braid){reference-type="eqref" reference="ZT22p1braid"}. In addition to these ingredients, we will also need a modification of the refined braid operator by the so-called *gamma factor* proposed in [@DMMSS; @Shakirov; @Mironov:2011ym; @MMSS; @Mironov:2012hz]). Modulo this modification, the physical meaning of which is still unclear at present, we need the refined variants of

1.  the partition function of the unknot $Z_{SU(N)}^{\text{CS}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_R;q)$ in order to determine the coefficient $\mu_Q$, and

2.  the quadratic Casimir factor $q^{C_R}$ in the monodromy by the action of the braid operator.

The former, *viz.* the refined partition function of the unknot, is given by the partition function of the refined BPS invariants of the conifold with a D-brane inserted at the appropriate leg of the toric diagram [@IK11]. The resulting partition function is the refined analogue of [\[unknotdimqR\]](#unknotdimqR){reference-type="eqref" reference="unknotdimqR"} and is given simply by the Macdonald polynomial $M_R(x;q_1,q_2)$: $$\frac{Z^{\text{ref}}_{SU(N)}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_R;q_1,q_2)}{Z^{\text{ref}}_{SU(N)}({\bf S}^3;q_1,q_2)}
\; = \; M_R(q_2^{\varrho};q_1,q_2) \, ,
\label{unknotMqtR}$$ see also appendix ([\[sec:macdonald\]](#sec:macdonald){reference-type="ref" reference="sec:macdonald"}). The combinatorial expression for the Macdonald polynomial is $$M_R(q_2^{\varrho};q_1,q_2) \; = \; \prod_{(i,j)\in R}
\frac{q_2^{\frac{N-i+1}{2}}q_1^{\frac{j-1}{2}}-q_2^{-\frac{N-i+1}{2}}q_1^{-\frac{j-1}{2}}}{q_2^{\frac{R^{t}_j-i+1}{2}}q_1^{\frac{R_i-j}{2}}-q_2^{-\frac{R^{t}_j-i+1}{2}}q_1^{-\frac{R_i-j}{2}}} \,,
\label{Mac_sp}$$ where $R^{t}$ denotes the transposition of the Young diagram $R$. Furthermore, the Macdonald polynomial satisfies the analogue of ([\[irr_decomp_schur\]](#irr_decomp_schur){reference-type="ref" reference="irr_decomp_schur"}): $$M_{R_1}(x;q_1,q_2) \, M_{R_2}(x;q_1,q_2) \; = \; \sum_{Q\in R_1\otimes R_2}N^Q_{R_1R_2} M_{Q}(x;q_1,q_2) \,,$$ where $N^{Q}_{R_1R_2}$ is a certain rational function of $q_1$ and $q_2$, namely the Littlewood-Richardson coefficient [@McD]. Therefore, as in [\[muCS\]](#muCS){reference-type="eqref" reference="muCS"}, we can use these relations to determine the refined analogue of the coefficient $\mu^Q_{R_1R_2}$ that enters the expression [\[three_ball\]](#three_ball){reference-type="eqref" reference="three_ball"} for the 3-ball partition function: $$\left( \mu^Q_{R_1R_2} \right)^2 \; = \; N^{Q}_{R_1R_2} \cdot M_Q(q_2^{\varrho};q_1,q_2)
\cdot Z^{\text{ref}}_{SU(N)}({\bf S}^3;q_1,q_2) \,.
\label{mu_refined}$$ Here, following [@AS], we tacitly assumed that generating functions of the refined BPS invariants, such as [\[Zrefdef\]](#Zrefdef){reference-type="eqref" reference="Zrefdef"} and [\[Zrefdefa\]](#Zrefdefa){reference-type="eqref" reference="Zrefdefa"}, can be expressed in the form [\[ZHilbert\]](#ZHilbert){reference-type="eqref" reference="ZHilbert"}, as in a local quantum field theory, with a Hilbert space whose states are labeled by conformal blocks. It would be interesting to understand better the physical basis for this assumption and to study the unitary structure on the "Hilbert space" of the refined Chern-Simons theory. In particular, in the case of $\Sigma\simeq \mathbf{T}^2$, one would hope to understand better the identification of the basis of orthonormal states with integrable representations.

As for the second ingredient, the quadratic Casimir factor $q^{C_2(R)}=e^{2\pi ih_R}$, it is related to the modular transformation $T = \begin{pmatrix}
1 & 1 \cr
0 & 1
\end{pmatrix}$ which acts in the standard way on the homology cycles of $\Sigma=\mathbf{T}^2$ in the WZW model. The modular matrix for the action of the $T$-transformation on the characters of $\widehat{su}(N)_k$ is $$T_{RQ} \; = \; T_{\emptyset\emptyset} \cdot q^{C_2(R)}\cdot \delta_{RQ} \,.$$ In [@AS] the $T$-matrix for the refined Chern-Simons theory is proposed: $$T^{\text{ref}}_{RQ} \; = \; T_{\emptyset\emptyset}\cdot
\frac{q_1^{\frac{1}{2}||R||^2}}{q_2^{\frac{1}{2}||R^{t}||^2}} \frac{q_2^{\frac{N}{2}|R|}}{q_1^{\frac{1}{2N}|R|^2}}\cdot\delta_{RQ} \,,$$ where $||R||^2:=\sum_iR_i^2$. Hence, we adopt a refinement [\[Casimir_ref\]](#Casimir_ref){reference-type="eqref" reference="Casimir_ref"} and the eigenvalue $\lambda^{(+)}_Q(R,R)$ of the braid operator ${\cal B}_{RR}$ for the refined theory: $$\lambda^{(+)}_Q(R,R) \; = \; \epsilon_{RR}^{Q}
\frac{q_1^{||R||^2}}{q_2^{||R^{t}||^2}}\frac{q_2^{N|R|}}{q_1^{\frac{1}{N}|R|^2}}
\frac{q_1^{-\frac{1}{4}||Q||^2}}{q_2^{-\frac{1}{4}||Q^{2}||^2}}
\frac{q_2^{-\frac{N}{4}|Q|}}{q_1^{-\frac{1}{4N}|Q|^2}} \,.
\label{braid_ref}$$ Similar framing factors were considered in [@DMMSS] and also deduced from the physics of refined BPS invariants in [@IK11]. Here we use slightly modified expressions to match [\[unrefeigl\]](#unrefeigl){reference-type="eqref" reference="unrefeigl"} in the unrefined limit $q_1 = q_2$.

Using these ingredients, we find the partition function $Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_R;q_1,q_2)$ for the $T^{2,2p+1}$ torus knot: $$\begin{aligned}
&& Z_{SU(N)}^{\text{ref}} ({\bf S}^3,T^{2,2p+1}_R;q_1,q_2) \nonumber \\
&& \quad = \; Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2) \sum_{Q\in R\otimes R}\gamma^Q_{RR}\cdot
\lambda^{(+)}_Q(R,R)^{2p+1}\cdot N^{Q}_{RR}\cdot M_Q(q_2^{\varrho};q_1,q_2) \,, \label{ZrefTpqq}
\end{aligned}$$ where, following [@DMMSS], we introduced a gamma factor $\gamma^Q_{RR}$. This factor is needed to make the partition function for the torus knot invariant under the obvious symmetry $T^{n,m}\leftrightarrow T^{m,n}$: $$Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{n,m}_R;q_1,q_2) \; = \; Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{m,n}_R;q_1,q_2) \,.
\label{consistency_gen}$$ While the proper physical understanding of the gamma factors is lacking, it does not prevent one from doing calculations. Indeed, the gamma factors can be determined by recursively solving the consistency conditions [\[consistency_gen\]](#consistency_gen){reference-type="eqref" reference="consistency_gen"} for $m=1,\cdots ,n-1$ ($m<n$). In particular, for torus knots $T^{2,2p+1}$, the gamma factors can be found from a single consistency condition for $p=0$, *i.e.* for $T^{2,1} \simeq {\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}$: $$\begin{aligned}
\frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,1}_R;q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)}
&=& \frac{Z_{SU(N)}^{\text{ref}}({\bf S}^3,{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}_R;q_1,q_2)}{Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)} \label{consistency_gamma} \\
&=&\sum_{Q \in R \otimes R} \gamma^Q_{RR}\cdot \lambda^{(+)}_Q(R,R) \cdot N^{Q}_{RR}
\cdot M_Q(q_2^{\varrho};q_1,q_2) = M_R(q_2^{\varrho};q_1,q_2) \,.
\nonumber
\end{aligned}$$

[^1]: At least, such formulation is not known at present.
