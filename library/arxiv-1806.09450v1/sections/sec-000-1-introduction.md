---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.995
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
[]{#sec1 label="sec1"}

The exceptional Jordan algebra $J = J_3^8 = H_3 ({\mathbb O})$ -- the algebra of $3 \times 3$ hermitian matrices with octonionic entries (reviewed in [@McC; @J68; @B; @Be; @BS; @G; @Y]) -- appears to be tailor made for the description of three families of quarks and leptons (like $\begin{pmatrix} u &c &t \\ \nu_e &\nu_{\mu} &\nu_{\tau} \end{pmatrix}$ or $\begin{pmatrix} d &s &b \\ e &\mu &\tau \end{pmatrix}$ of a fixed chirality) -- see [@DV], briefly outlined in Sect. 2. There are three exceptional Lie algebras associated with $J$:

1.  the automorphism or *derivation algebra* $$\label{eq11}
    {\rm Der} \, (J) = {\mathfrak f}_4 \, (= {\rm Lie} \, F_4) = so (9) \, \dot + \, S_9 = so (8) \, \dot + \, S_8^+ \, \dot + \, S_8^- \, \dot + V_8,$$ (we use, following [@BS], the sign $\, \dot + \,$ for the direct sum of vector spaces, to be distinguished from the direct sum $\oplus$ of (mutually commuting) algebras);

2.  the (reduced) *structure algebra* $$\label{eq12}
    {\rm str} \, (J) = {\mathfrak e}_6 \, (= {\rm Lie} \, E_6) = {\mathfrak f}_4 \, \dot + \,  J_0 \, ;$$

3.  the *conformal algebra* $$\label{eq13}
    {\rm co} \, (J) = {\mathfrak e}_7 \, (= {\rm Lie} \, E_7) = {\mathfrak e}_6 \, \dot + \, 2J \, \dot + \, {\mathbb C} \, .$$

Here Lie $G$ stands for the Lie algebra of the Lie group $G$; $S_9$ is the 16-dimensional spinor representation of the rotation Lie algebra $so (9)$; it can be viewed as the direct sum of the two inequivalent 8-dimensional spinor representations $S_8^{\pm}$ of $so (8)$; $V_8$ is the (8-dimensional) vector representation of $so (8)$; $J_0$ is the traceless part of $J$ (the 26 dimensional real vector space of $3 \times 3$ hermitian traceless octonionic matrices, also denoted as $sH_3 ({\mathbb O})$). The construction of the above exceptional Lie algebras involves the *magic square* of Freudenthal and Tits. It is explained in [@BS; @B] -- see the summary in Sect. 3.

The Borel-de Siebenthal theory (see [@BdS; @K]) describes the maximal closed connected subgroups of a compact Lie group that have maximal rank. Our main observation (Sect. 4) is that the intersection of the maximal subgroups ${\rm Spin} \, (9)$, and $\frac{SU (3) \times SU (3)}{{\mathbb Z}_3}$ of the (compact) automorphism group $F_4$ of $J$ is the gauge group of the standard model of particle physics $$\label{eq14}
G_{F_4} = G_{\rm ST} = S(U(2) \times U(3)) = \frac{SU (2) \times SU (3) \times U(1)}{{\mathbb Z}_6}.$$ This result makes it natural to consider as possible extensions of $G_{\rm ST}$ the intersections of appropriate maximal rank subgroups of ${\rm Str} \, (J) = E_6$, $$\label{eq15}
G_{E_6} = S(U(2) \times U(2) \times U(3))$$ and of ${\rm Co} (J) = E_7$; $$\label{eq16}
G_{E_7} = S(U(2) \times U(3) \times U(3)) \, .$$ Note that all three groups, $G_{F_4}$, $G_{E_6}$, $G_{E_7}$ are non-semisimple (i.e. they include $U(1)$ factors) compact subgroups of $F_4 , E_6 , E_7$, of maximal rank ($4,6,7$, respectively).

It would be useful to consider $J$ as a member of the family $H_n ({\mathbb K})$ where ${\mathbb K}$ is an *alternative composition algebra*. We recall that an algebra ${\mathcal A}$ is said to be a *division algebra* if $ab=0$ for $a,b \in {\mathcal A}$ implies that either $a=0$ or $b=0$. It is called an *alternative algebra* if any two elements of ${\mathcal A}$ generate an associative subalgebra. Zorn has proven (in 1933) that there are just four alternative division algebras: the real and the complex numbers, ${\mathbb R}$ and ${\mathbb C}$, the quaternions, ${\mathbb H}$, and the octonions, ${\mathbb O}$. All four admit a multiplicative norm $x \to \vert x \vert \in {\mathbb R}_+$ such that $$\label{eq17}
\vert xy \vert = \vert x \vert \, \vert y \vert \, , \quad \vert x \vert^2 = x \, \bar x = \bar x \, x \quad (>0 \ {\rm for} \ x \ne 0)$$ where $x \to \bar x$ is the (involutive) conjugation in ${\mathbb K}$. Hurwitz has proven back in 1898 that the only normed division algebras are ${\mathbb R}$, ${\mathbb C}$, ${\mathbb H}$ and ${\mathbb O}$. $H_n ({\mathbb K})$ is the algebra of $n \times n$ hermitian matrices (with entries in ${\mathbb K}$) closed under the Jordan multiplication $$\label{eq18}
X \circ Y = \frac12 (XY + YX) \, (= Y \circ X) \, .$$ For ${\mathbb K} = {\mathbb O}$ the resulting algebra only satisfies the *Jordan condition* $$\label{eq19}
(X^2 \, Y) X = X^2 (YX)$$ for $n =1,2,3$. The condition ([\[eq19\]](#eq19){reference-type="ref" reference="eq19"}), on the other hand, characterizes an abstract *Jordan algebra* for which the endomorphism $Z \to X(YZ) - Y(XZ)$ is an (inner) derivation.

Division algebras can be also characterized by the existence of a non-degenerate real trilinear form $t : {\mathbb K}^{\times 3} \to {\mathbb R}$, the *triality form* -- see Sect. 2.4 of [@B]. (We note that it looks nontrivial even for ${\mathbb K} = {\mathbb C}$. In this case, for $z_j = x_j + i \, y_j$, $j=1,2,3$, the form is a multiple of $t(z_1 , z_2 , z_3) = x_1 \, x_2 \, x_3 - x_1 \, y_2 \, y_3 - x_2 \, y_1 \, y_3 - x_3 \, y_1 \, y_2$.) In general, the presence of a hermitian inner product (cf. ([\[eq17\]](#eq17){reference-type="ref" reference="eq17"})) makes the existence of $t$ equivalent to the existence of a ${\mathbb K}$-valued cross product in ${\mathbb K}$.

We shall consider (in Sect. 2 and Sect. 3.3) more general *alternative composition algebras* which have a (not necessarily positive definite) non-degenerate sesquilinear form $\langle x,y \rangle$ satisfying the (square of the) factorization property ([\[eq17\]](#eq17){reference-type="ref" reference="eq17"}): $$\label{eq110}
\langle xy , xy \rangle = \langle x,x \rangle \, \langle y,y \rangle \, ,$$ and have an alternating associator (see Eq. ([\[eq23\]](#eq23){reference-type="ref" reference="eq23"}) below).
