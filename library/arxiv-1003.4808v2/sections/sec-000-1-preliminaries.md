---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-000-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 2-6
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.963
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
[]{#sec:basics label="sec:basics"}

Let $K$ be an oriented knot (or link) in the three-sphere $S^3$. The original volume conjecture [@Kashaev-1997; @Mur-Mur] relates the $N$-colored Jones polynomial of $K$ to the hyperbolic volume of the knot complement $S^3\backslash K$:

$$\begin{array}{c@{\qquad}c@{\qquad}c} \text{$N$-colored Jones poly of $K$} & \longleftrightarrow & \text{hyperbolic volume of $S^3\backslash K$} \\
\text{(combinatorial, rep. theory)} & & \text{(geometric)\,.}
\end{array} \label{VCtext}$$

We begin by reviewing some of the definitions and ingredients that enter on the two sides here in order to make this statement more precise, and to serve as a precursor for its subsequent generalization.

### Jones polynomials

The (non-colored) Jones polynomial $J(K;q)$ of a knot or link can be defined combinatorially via the skein relation

$$q\,J({\,\raisebox{-.13cm}{\includegraphics[width=.5cm]{overcrossing}}\,}) - q^{-1}J({\,\raisebox{-.13cm}{\includegraphics[width=.5cm]{undercrossing}}\,}) = (q^\frac12-q^{-\frac12})\,J({\,\raisebox{-.13cm}{\includegraphics[width=.5cm]{smoothing}}\,})\,, \label{skein}$$

along with the normalization[^1]

$$J({\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,}) = q^\frac12+q^{-\frac12} \quad\qquad \text{for ${\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,}=$ unknot}\,, \label{JU}$$

and the rule

$$J(K_1\sqcup K_2) = J(K_1)\,J(K_2)\,$$

for any disjoint union of knots or links. Thus, for example, the (right-handed) trefoil and figure-eight knots have Jones polynomials

$$\begin{aligned}
 J(\mathbf{3_1}) &= q^{-\frac12}+q^{-\frac32}+q^{-\frac52}-q^{-\frac92}\,, \\
J(\mathbf{4_1}) &= q^{\frac52}+q^{-\frac52}\,.
\end{aligned}$$

In general, $J(K,q)$ is a Laurent polynomial, $J(K,q)\in {\mathbb{Z}}[q^\frac12,q^{-\frac12}]$.

The combinatorial construction of the Jones polynomial is intimately related to representation theory of $SU(2)$ --- or the closely related representation theories of the quantum group $U_q(su(2))$ or the affine Lie algebra $\widehat{su(2)}$. In particular, the classical Jones polynomial above is obtained by "coloring" the knot (or link) $K$ in $S^3$ with the 2-dimensional representation of $SU(2)$. More generally, such a knot or link can be colored with any finite-dimensional representation $R$ of $SU(2)$, leading to a colored Jones polynomial $J_R(K,q)$. The *N-colored* Jones polynomial $J_N(K,q)$ takes $R$ to be the irreducible $N$-dimensional representation [@Wit-Jones; @Resh-Tur; @Kir-Mel]. The colored Jones polynomial can again be computed in a purely algebraic/combinatorial manner, by using the two rules

$$\label{NJ}
\begin{equation}
 J_{\oplus_iR_i}(K;q) = \sum_i J_{R_i}(K;q)\, \vspace{-.5cm}\end{equation}
and
\begin{equation}J_R(K^n;q) = J_{R^{\otimes n}}(K;q)\,,\,  \end{equation}$$

together with

$$J_R(K_1\sqcup K_2) = J_R(K_1)J_R(K_2)\,,$$

and the fact that $J_1(K;q)=J_{R=\oslash}(K;q)\equiv 1$. The first rule says that if $R$ is reducible, then $J_R$ splits as a sum over irreducible components. The second rule says that the $R$-colored Jones polynomial for the $n$-cabling of a knot (formed by taking $n$ copies of the knot or link, slightly displaced away from one another[^2]) is equal to the colored Jones polynomial of the original knot but in representation $R^{\otimes n}$.

For example, from ([\[NJ\]](#NJ){reference-type="ref" reference="NJ"}a-b) and the fact that $J_{N=2}(K,q) = J(K,q)$, it is easy to see that

$$J_N({\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,}) = \frac{q^{\frac N2}-q^{-\frac N2}}{q^{\frac12}-q^{-\frac12}}\,.$$

More generally, for any knot $K$, relations [\[NJ\]](#NJ){reference-type="eqref" reference="NJ"} can be used to reduce $J_N(K;q)$ to ordinary Jones polynomials of $K$ and its cablings. We have

$$\begin{aligned}
J_1(K;q) &= 1\,, \\
J_2(K;q) &= J(K;q)\,, \\
J_3(K;q) &= J(K^2;q)-1\,, \\
J_4(K;q) &= J(K^3;q)-2J(K;q)\,, \\
 &\;\;\ldots,
\end{aligned}$$

where the expressions for $J_3$, $J_4$, etc. follow from the rules for decomposing representations of $SU(2)$: $\mathbf{2}^{\otimes2} = \mathbf{1}\oplus\mathbf{3}$ ,  $\mathbf{2}^{\otimes 3}=(\mathbf{1}\oplus\mathbf{3})\otimes \mathbf{2}=\mathbf{2}\oplus\mathbf{2}\oplus\mathbf{4}$ , etc. Since $J(K;q) \in {\mathbb{Z}}[q^\frac12,q^{-\frac12}]$ for any $K$, it is clear that the colored Jones polynomials $J_N(K;q)$ will also be elements of ${\mathbb{Z}}[q^\frac12,q^{-\frac12}]$ .

We have explained the left side of [\[VCtext\]](#VCtext){reference-type="eqref" reference="VCtext"}, completely, if somewhat tersely, in terms of algebra and combinatorics. The right side has a very different interpretation.

### Hyperbolic volumes

It was conjectured by Thurston [@thurston-1982] (and is now proved [@Perelman-geometrization]) that every three-manifold may be decomposed into pieces that admit exactly one of eight different geometric structures. The most common structure by far is hyperbolic. Indeed, in the case of knot complements in $S^3$ this statement can be made exact: a knot complement has a hyperbolic structure if and only if it is not a torus or satellite knot [@thurston-1982]. By definition, a "hyperbolic structure" refers to a geodesically-complete metric of constant curvature $-1$. If a hyperbolic structure does exist on a manifold $M$, then it is unique, and the corresponding hyperbolic volume ${\rm Vol}(M)$ is a well-defined topological invariant.

In fact, there also exists a natural complexification of the hyperbolic volume of a three-manifold $M$, obtained as

$${\rm Vol}(M) + i {\rm CS}(M)\,, \label{VolCS}$$

where ${\rm CS}(M)$ is the so-called Chern-Simons invariant of $M$. To understand this, suppose that $M$ allows a spin structure (as all knot/link complements in $S^3$ do) and consider flat $SL(2,{\mathbb{C}})$ connections on $M$ in place of hyperbolic metrics.

[^3]

There exists a flat connection ${\cal A}$ whose real and imaginary parts can be interpreted, respectively, as the vielbein and spin connection of the hyperbolic metric. The real part of the quantity

$$\frac{i}{2}I_{CS}({\cal A}) = \frac{i}{2}\int_M\Big({\cal A}\wedge d{\cal A}+\frac{2}{3}{\cal A}\wedge{\cal A}\wedge{\cal A}\Big) \label{ICS}$$

then reproduces ${\rm Vol}(M)$, while the imaginary part defines ${\rm CS}(M)$. The expression $I_{CS}({\cal A})$ is the so-called Chern-Simons functional of ${\cal A}$. Further details can be found *e.g.* in [@Wit-CSGrav; @witten-1991] or [@gukov-2003; @DGLZ]. Under gauge transformations acting on ${\cal A}$, the functional $I_{CS}({\cal A})$ is only well-defined up to shifts of $8\pi^2$, leading to an ambiguity of $4\pi^2$ in the definition of ${\rm CS}(M)$. Because of this, it is often convenient to exponentiate the complexified volume [\[VolCS\]](#VolCS){reference-type="eqref" reference="VolCS"}, writing it in the unambiguous form

$$Z(M) =  e^{\frac{i}{4\pi}I_{CS}({\cal A})} = e^{\frac{1}{2\pi}\big({\rm Vol}(M)+i{\rm CS}(M)\big)}\,. \label{Zcl}$$

For hyperbolic knot complements, the full complexified volume $Z(M)$ can be efficiently computed in terms of ideal hyperbolic triangulations, *cf.* [@snap; @neumann-2004; @zickert-2008].

### The Volume Conjecture

We have not said much yet about the variable $q$ appearing in the Jones polynomials. Strictly speaking, this variable should be a root of unity

[^4]

$$q = e^{\frac{2\pi i}{k}}\,, \qquad k \in {\mathbb{Z}}_+\,.$$

At the special value $k=N$, all Jones polynomials $J_N(K;q)$ vanish, but the ratio

$$V_N(K,q) =  \frac{J_N(K;q)}{J_N({\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,};q)}$$

remains finite. The original volume conjecture [@Kashaev-1997; @Mur-Mur] then states that

$$\lim_{N\to\infty} \frac{2\pi\log\big|V_N(K;q=e^{\frac{2\pi i}{N}})\big|}{N} = {\rm Vol}(M)\,.$$

It is also possible to remove the absolute value and exponentiate to obtain the complexified generalization (*cf.* [@Mur-cx])

$$\boxed{V_N(K;q=e^{\frac{2\pi i}{N}}) \;\overset{N\to\infty}{\sim}\;  Z(M)^N = e^{\frac{N}{2\pi}\big({\rm Vol}(M)+i{\rm CS}(M)\big)}}\,.  \label{VC}$$

![The figure-eight knot, $\mathbf{4_1}$](knot41){#fig:41 width="1.5in"}

As an example, consider the figure-eight knot (Figure [1](#fig:41){reference-type="ref" reference="fig:41"}), the simplest hyperbolic knot. The colored Jones polynomial (see *e.g.* [@Kashaev-1997] or [@Habiro-Jones]) is

$$V_N(\mathbf{4_1};q=e^{\frac{2\pi i}{N}}) = \sum_{m=0}^{N-1}(q)_m(q^{-1})_m\,,\qquad (x)_m := (1-x)(1-x^2)\cdots(1-x^m)\,.$$

The hyperbolic volume of the figure-eight knot complement is

$${\rm Vol}(S^3\backslash\mathbf{4_1}) = 2\,{\rm Vol}(\Delta) = 2.02988...\,, \label{vol41}$$

where ${\rm Vol}(\Delta) = {\rm Im}\,{\rm Li}_2(e^{i\frac{\pi}{3}})$ denotes the volume of a regular hyperbolic ideal tetrahedron. The Chern-Simons invariant ${\rm CS}(S^3\backslash\mathbf{4_1})$ vanishes. It is fairly straightforward (and an informative exercise[^5]) to show that in the limit $N\to\infty$ one has, as expected,

$$\lim_{N\to\infty} \frac{2\pi \log V_N(\mathbf{4_1};e^{\frac{2\pi i}{N}})}{N} = {\rm Vol}(S^3\backslash\mathbf{4_1})\,.$$

[^1]: The most common normalization for the unknot seen in the mathematics literature is $J(\raisebox{-.05cm}{\includegraphics[width=.3cm]{unknot}})=1$. For the connection with topological quantum field theory, however, [\[JU\]](#JU){reference-type="eqref" reference="JU"} is much more natural.

[^2]: This displacement must be done in a way that produces zero linking number between the various copies.

[^3]: Recall that a "$G$-connection" on a principal $G$-bundle $E\to M$ can be written locally as a ${\frak{g}}$-valued one-form ${\cal A}$. The bundle $E$ is typically taken to be trivial in the present context, $E=G\times M$. A gauge transformation (a change of coordinates on $E$) induced by an element $g\in\Gamma(E)$ acts locally on the connection as ${\cal A}\mapsto g^{-1}{\cal A}g+g^{-1}dg$.

[^4]: In terms of representation theory, the integer $k$ is identified as the level of the affine Lie algebra $\widehat{su(2)}_k$. The representation theory of the quantum group $U_q(su(2))$ also (crucially) simplifies greatly when $q$ is a root of unity, becoming essentially equivalent to the representation theory of $\widehat{su(2)}_k$. See also Sections [\[sec:TQFT_CS\]](#sec:TQFT_CS){reference-type="ref" reference="sec:TQFT_CS"}-[\[sec:path\]](#sec:path){reference-type="ref" reference="sec:path"}.

[^5]: One method involves analytically continuing the summand as a ratio of quantum dilogarithm functions (*cf.* [@Fad-Kash; @DGLZ]), approximating the sum by an integral, and evaluating it at its saddle point.
