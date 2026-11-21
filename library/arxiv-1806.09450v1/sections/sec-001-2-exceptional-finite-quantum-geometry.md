---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-001-2-exceptional-finite-quantum-geometry
section_title: "Exceptional finite quantum geometry"
section_number: 2
pages: 3-6
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.995
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
[]{#sec2 label="sec2"}

In the approach of almost commutative geometry \[DKM, D, CL, C, CC, CCS, BF\] to the standard model, space-time is viewed as the tensor product of a standard (commutative) 4-dimensional spin manifold with a finite noncommutative space. In the almost classical quantum geometry approach one is led to identify the finite quantum space with the exceptional Jordan algebra.\

To begin with, it was argued in [@DV] that the decomposition of the (8-dimensional, real) vector space ${\mathbb O}$ of octonions[^1] into a direct sum of complex vector spaces, $$\label{eq21}
{\mathbb O} = {\mathbb C} \oplus {\mathbb C}^3$$ naturally corresponds to the splitting of the basic fermions (in one generation) of the standard model into quarks and leptons. Moreover, the color group $SU(3)$ leaves invariant a (complex) volume form on ${\mathbb C}^3$ which is dual with respect to the hermitian scalar product $\langle \ , \ \rangle$ in ${\mathbb C}^3$ to a skew symmetric antilinear cross product ${\bf z} \times {\bf w} = - \, {\bf w} \times {\bf z}$ ($\times : {\mathbb C}^3 \otimes {\mathbb C}^3 \to {\mathbb C}^3$): $Vol({\bf z_1}, {\bf z_2}, {\bf z_3})=<{\bf z_1}\times{\bf z_2}, {\bf z_3}>$. This cross product and the (hermitian) inner product $\langle {\bf z,w} \rangle$ ($\langle \ , \ \rangle : {\mathbb C}^3 \otimes {\mathbb C}^3 \to {\mathbb C}$) can be combined with the usual multiplication of complex numbers and extended to a unique real bilinear multiplication $xy$ in ${\mathbb O}$ that is norm preserving: $$\langle xy , xy \rangle = \langle x,x \rangle \, \langle y,y \rangle \, ,$$ $$\label{eq22}
x = z_0 \oplus {\bm z} \Rightarrow \langle x,x \rangle = \bar z_0 \, z_0 + \sum_{i=1}^3 \bar z_i \, z_i \ (\equiv \vert x \vert^2)$$ ($\bar z$ standing for the complex conjugate of $z \in {\mathbb C}$). The resulting product is non associative but *alternative*: the *associator* $$\label{eq23}
[x,y,z] = (xy)z - x(yz)$$ is an alternating function of $x,y,z$; in particular, it vanishes if any two of the arguments $x,y,z$ coincide. More generally, this is true for any *composition algebra* -- i.e. an algebra with a non-degenerate (but not necessarily positive definite -- thus including the *split octonions*) inner product $\langle \ , \ \rangle$ satisfying the first equation ([\[eq22\]](#eq22){reference-type="ref" reference="eq22"}) (cf. [@BS]).

The significance of the notion of an alternative algebra is illustrated by the following remark. The commutator $$ad_a \, x = [a,x]$$ defines a *derivation* in an associative algebra: $$ad_a \, (xy) = (ad_a \, x) \, y + x \, ad_a \, y \, .$$ This property fails, in general, for a non-associative algebra. If however the algebra ${\mathcal A}$ is *alternative*, every pair of elements $x,y \in {\mathcal A}$ defines a derivation $D_{x,y}$ in ${\mathcal A}$ in terms of the double commutator and the associator: $$\label{eq24}
D_{x,y} (z) = \left[[x,y] , z \right] - 3 \, [x,y,z]$$ (see Eq. (14) of [@B]).

The construction of the octonionic scalar product satisfying ([\[eq22\]](#eq22){reference-type="ref" reference="eq22"}) in terms of the cross product and the inner product in ${\mathbb C}^3$, indicated above (and worked out in [@DV; @TD]) yields the standard multiplication in ${\mathbb O}$ which is conveniently expressed in terms of the Fano plane of imaginary octonionic units recalled in Appendix A. Choosing, say, $e_7$ as the "$i$" in ${\mathbb C}$ we can write the decomposition ([\[eq21\]](#eq21){reference-type="ref" reference="eq21"}) explicitly in the basis $\{e_0 = 1 , e_j , j = 1,\ldots , 7 \}$ as: $$x = x^0 + x^7 \, e_7 + (x^1 + x^3 \, e_7) \, e_1 + (x^2 + x^6 \, e_7) \, e_2 \, +$$ $$\label{eq25}
+ \, (x^4 + x^5 \, e_7) \, e_4 \left( = \sum_{\alpha = 0}^7 x^{\alpha} \, e_{\alpha} \right) .$$

The presence of three generations of quark-lepton doublets $\begin{pmatrix} u &\nu \\ d &e \end{pmatrix}$ (with $u,d$ -- 3-vectors in the color space) suggests combining the octonions into a $3 \times 3$ hermitian matrix: $$\label{eq26}
X = \begin{pmatrix}
\xi_1 &x_3 &\bar x_2 \\
\bar x_3 &\xi_2 &x_1 \\
x_2 &\bar x_1 &\xi_3 \end{pmatrix} , \quad x_i \in {\mathbb O} \, , \quad \xi_i = \xi_i \in {\mathbb R}$$ where the bar over an octonion $x$ stands for octonionic conjugation (changing simultaneously the sign of all imaginary units $e_j$, $j=1,\ldots ,7$).

The matrices ([\[eq26\]](#eq26){reference-type="ref" reference="eq26"}) span a 27-dimensional real vector space which can be given the structure of the exceptional Jordan algebra $J = J_3^8 \, (= H_3 ({\mathbb O}))$ with multiplication defined as the symmetrized matrix multiplication ([\[eq18\]](#eq18){reference-type="ref" reference="eq18"}): $$\label{eq27}
X \circ Y = \frac12 \, (XY + YX) \, .$$ As emphasized in [@DV] the (axiomatic) properties of the (commutative) Jordan product $\circ$ are dictated by the requirement to have a spectral decomposition for (hermitian) observables. In fact, the requirement of *formal reality* ($\underset{i}{\sum} \, x_i^2 = 0 \Rightarrow x_i = 0$ for all $i$) implies that the *Jordan condition* ([\[eq19\]](#eq19){reference-type="ref" reference="eq19"}) $$\label{eq28}
(x^2 \circ y) \circ x = x^2 \circ (y \circ x)$$ is equivalent to power associativity $$\label{eq29}
x^r x^s = x^{r+s} \qquad (x \in J \, , \ r,s \in {\mathbb N})$$ as proven in [@JvNW] (see Theorem 1 of [@DV]). It is clearly necessary for the standard theory of spectral decomposition.

We recall the remark after Eq. ([\[eq19\]](#eq19){reference-type="ref" reference="eq19"}) according to which the Jordan condition ([\[eq28\]](#eq28){reference-type="ref" reference="eq28"}) ensures that the commutator of two left multiplications is a derivation: $$\label{eq210}
[L_x , L_y] \in {\rm Der} \, J \quad \mbox{for} \quad L_x (y) := x \circ y \, , \ x,y \in J$$ (i.e. $[L_x , L_y] \, (z \circ w) = [L_x , L_y] \, (z) \circ w + z \circ [L_x , L_y] \, (w)$).

One also defines a real linear function ${\rm tr} \, X$, a bilinear inner product $\langle X,Y \rangle$ and a symmetric trilinear form ${\rm tr} \, (X,Y,Z)$ on $J$ setting $${\rm tr} \, X = \xi_1 + \xi_2 + \xi_3 \, (= \langle X , {\rm 1\mkern-4mu I}\rangle) \, ,$$ $$\langle X,Y \rangle = {\rm tr} \, (X \circ Y) \, ,$$ $$\label{eq211}
{\rm tr} \, (X,Y,Z) = \langle X , Y \circ Z \rangle = \langle X \circ Y , Z \rangle \, .$$

[^1]: Octonios have been first applied to the standard model by Feza Gürsey and his students [@G]. His work triggered an imaginative development by G. Dixon [@Di] followed by C. Furey [@Fu] among others. A distinguished feature of our approach, started in [@DV], is the fact that we are dealing with an euclidean Jordan algebra suited for a (finite) *observable* algebra.
