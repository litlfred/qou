---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-006-4-borel-de-siebenthal-theory-and-intersections-o
section_title: "Borel-de Siebenthal theory and intersections of maximal subgroups of compact exceptional Lie groups"
section_number: 4
pages: 12-16
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.63
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
[]{#sec4 label="sec4"}

Borel and de Siebenthal [@BdS] described the maximal maximal-rank subgroups of simple compact connected Lie groups noticing that each such subgroup appears as the identity component of the centralizer of its center. This yields the following explicit classification of the maximal subalgebras of the simple compact Lie algebras: $$\begin{aligned}
\label{eq41}
su (n+1) &: &su(p+1) \times su(n-p) \times u(1) \quad (p=1 , \ldots , \left[ \frac n2 \right]); \nonumber \\
so (2n+1) &: &so(2n) \, , \ so (2p+1) \times so (2n-2p) \, , \ so (2n-1) \times u(1) \, , \nonumber \\
&&(p=1,\ldots , n-2); \nonumber \\
sp (2n) &: &sp(2p) \times sp (2n-2p) \, , \ su (n) \times u(1) \quad (p=1, \ldots , \left[ \frac n2 \right]); \nonumber \\
so (2n) &: &so (2p) \times so (2n-2p) \, , \ so (2n-2) \times u(1) \, , \ su (n) \times u(1); \nonumber \\
e_6 &: &su (2) \times su (6) \, , \ su (3) \times su (3) \times su (3) \, , \ so (10) \times u(1); \nonumber \\
e_7 &: &su (2) \times so (12) \, , \ su (3) \times su (6) \, , \ su(8) \, , \ e_6 \times u(1); \nonumber \\
e_8 &: &so(16) \, , \ su (9) \, , \ su (5) \times su (5) \, , \ e_6 \times su (3) \, , \ e_7 \times su (2); \nonumber \\
{\mathfrak f}_4 &: &so(9) \, , \ su (3) \times su (3) \, , \ su (2) \times sp (6) ; \nonumber \\
g_2 &: &su (3) \, , \ su (2) \times su (2) \, .
\end{aligned}$$

Baez and Huerta [@BH] have observed that the intersection of the grand unified theory (GUT) symmetry groups $SU (5)$ (of Georgi-Glashow) and $\frac{{\rm Spin} \, (4) \times {\rm Spin} \, (6)}{{\mathbb Z}_2}$ ($= \, \frac{SU(2) \times SU(2) \times SU(4)}{{\mathbb Z}_2}$ of Pati-Salam) within the ${\rm Spin} \, (10)$ grand unification (also introduced by Georgi in 1974) coincides with the gauge group $G_{\rm ST}$ ([\[eq14\]](#eq14){reference-type="ref" reference="eq14"}) of the standard model. We shall see that the Borel-de Siebenthal theory provides a purely deductive path to this gauge group.

We first note that the intersection of the maximal connected subgroups of $G_2$ is $$\label{eq42}
G_{G_2} = SU(3) \cap \frac{SU (2) \times SU (2)}{{\mathbb Z}_2} = U(2)$$ -- that is, the gauge group for the Weinberg-Salam model. This however destroys our rational for introducing the octonions: the unbroken $SU(3)$ color symmetry. We shall therefore restrict the maximal subgroups of $G_2$ and of the higher rank groups under consideration. A maximal rank subgroup of an exceptional Lie group will be called *admissible* if it contains the color $SU(3)$ subgroup. Thus the only admissible subgroup of $G_2$ is $SU(3)(=SU(3)_c)$ itself.

Assuming that the exceptional Jordan algebra $J$ is a good candidate for the finite geometry underlying the standard model of particle physics, it would be natural to view its automorphism group $F_4$ as (its possible) GUT symmetry. If we then look for the intersection of its maximal admissible subgroups (described by Theorems 2.9.1 and 2.12.2 (but excluding 2.11.2!) of [@Y]): $$\label{eq43}
{\rm Spin} \, (9) \, , \quad \frac{SU (3) \times SU (3)}{{\mathbb Z}_3},$$ one finds precisely the group $G_{\rm ST} = G_{F_4}$ ([\[eq14\]](#eq14){reference-type="ref" reference="eq14"}): $$\label{eq44}
G_{F_4} = S[U(2) \times U(3)] = \frac{SU (3) \times SU (2) \times U(1)}{{\mathbb Z}_6} \, .$$ Similarly, for the compact form $E_6$ of the (reduced) structure group of $J$ we find (according to theorems 3.10.7, and 3.13.5 of [@Y] - the subgroup described by 3.11.4 being inadmissible): $$\begin{aligned}
\label{eq45}
G_{E_6} &= &\frac{{\rm Spin} \, (10) \times U (1)}{{\mathbb Z}_4} \cap \frac{SU (3) \times SU (3) \times SU(3)}{{\mathbb Z}_3} \nonumber \\
&= &S[U(2) \times U(2) \times U(3)] \, , 
\end{aligned}$$ a group with an extra $U(1)$ factor and a remnant of the Pati-Salam model that is favored in [@CCS] (see also [@BF]). Finally, for the compact form of $E_7$ we find (using 4.10.2, 4.11.15 and 4.13.5 and excluding 4.12.5 of [@Y]): $$\begin{aligned}
\label{eq46}
G_{E_7} &= &\frac{E_6 \times U (1)}{{\mathbb Z}_3} \cap \frac{{\rm Spin} \, (12) \times SU (2)}{{\mathbb Z}_2} \cap \frac{SU (6) \times SU (3)}{{\mathbb Z}_3} \nonumber \\
&= &S(U(2) \times U(3) \times U(3)) \, .
\end{aligned}$$

Since the early work of Gürsey, Ramond and Sikivie [@GRS] one uses the 27-dimensional representation of $E_6$ to combine one generation of fermions (the **16** of ${\rm Spin} \, (10) \subset E_6$) with the bosonic representations $\bm{10} \oplus {\bm 1}$ of ${\rm Spin} \, (10)$. A similar interpretation is given to the basic representation $\underline{26}$ of $F_4$ in [@TD]. The interpretation of either of the groups ([\[eq43\]](#eq43){reference-type="ref" reference="eq43"}) ([\[eq45\]](#eq45){reference-type="ref" reference="eq45"}) and ([\[eq46\]](#eq46){reference-type="ref" reference="eq46"}) will depend on the choice of representation of the exceptional Jordan algebra. As pointed out in [@DV] any finite module over $J$ is isomorphic to $J \otimes E$ for some finite dimensional vector space $E$. It was argued in (Sect. 4.4 of) [@DV], another attractive candidate for a finite quantum algebra may be $$\label{eq47}
J_1^2 \oplus J_2^4 \oplus J_3^8 = {\mathbb R} \oplus H_2 ({\mathbb H}) \oplus H_3 ({\mathbb O}) \, .$$ We leave the study of these possibilities and their physical implications to future work.

I.T. thanks for hospitality IHES where the bulk of this work was done and the Theoretical Physics Department of CERN where the paper was completed. The work of I.T. has been supported in part by Project DN 18/1 of the Bulgarian National Science Foundation.

# Appendix A. The Fano plane of imaginary octonions ([@B]) {#secAA}

$$\includegraphics[width=4cm]{Fig1JordanAlgebra.pdf}$$ $$e_1 = (0,0,1) , e_2 = (0,1,0) \Rightarrow e_1 \, e_2 = e_4 = (0,1,1)$$ $$e_3 = (1,0,0) \Rightarrow e_2 \, e_3 = e_5 = (1,1,0)$$ $$e_1 \, e_5 = e_6 = (1,1,1)$$ $$e_4 \, e_5 = e_7 = (1,0,1) \, .$$

**Figure 1.**

Projective plane in ${\mathbb Z}_2^3$ with seven points and seven lines.

The multiplication table for the seven octonionic imaginary units can be recovered from the following properties: $$e_i^2 = -1 \, , \quad i=1,\ldots , 7 \, ; \quad e_i \, e_j = -e_j \, e_i \, ; \eqno ({\rm A}.1)$$ $$e_i \, e_j = e_k \Rightarrow e_{i+1} \, e_{j+1} = e_{k+1} \, , \quad e_{2i} \, e_{2j} = e_{2k} \eqno ({\rm A}.2)$$ where indices are counted modulo seven; and a single relation of the type $$e_1 \, e_2 = e_4 \eqno ({\rm A}.3)$$ producing a quaternionic line. We have displayed on Fig. 1 the points $e_i$ as non-zero triples of homogeneous coordinates taking values $0$ and $1$ such that the product $e_i \, e_j$ (in clockwise order) is obtained by adding the coordinates $(a,b,c)$, $a,b,c \in \{0,1\}$, modulo two.
