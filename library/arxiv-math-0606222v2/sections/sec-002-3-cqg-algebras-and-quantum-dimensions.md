---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-002-3-cqg-algebras-and-quantum-dimensions
section_title: "CQG algebras and quantum dimensions"
section_number: 3
pages: 6-10
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.977
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#CQG label="CQG"}

The category of Compact Quantum Group algebras ([CQG ]{.sans-serif}) is a full subcategory of the category of Hopf $*$-algebras that includes the standard noncommutative deformations of algebras of representative functions on compact Lie groups. In particular, [CQG ]{.sans-serif}algebras are Hopf $*$-algebras with positive definite Haar functionals which have natural analogs of the Peter-Weyl decomposition and the Schur orthogonality relations. This leads to the notion of the quantum dimension of an irreducible, finite dimensional comodule over a given [CQG ]{.sans-serif}algebra. One of the main aims of the paper is to explicitly compute quantum dimensions of irreducible comodules which arise in the context of (quantum) Grassmannians. Following [@DK], we recall in this section the definition of a [CQG ]{.sans-serif} algebra and its basic properties. We furthermore discuss the notion of a quantum Gelfand pair in the context of [CQG ]{.sans-serif}algebras (cf. [@F]), and the associated quantum zonal spherical functions.

Let $A$ be a Hopf $*$-algebra with comultiplication $\Delta$, counit $\epsilon$ and antipode $S$. A linear functional $h: A\rightarrow \mathbb{C}$ is called a normalized Haar functional if $h(1)=1$ and $$\bigl(h\otimes \hbox{Id}_A\bigr)\bigl(\Delta(a)\bigr)=
h(a)1_A=\bigl(\hbox{Id}_A\otimes h\bigr)\bigl(\Delta(a)\bigr),\qquad a\in A.$$ A Haar functional $h$ on $A$ is called positive definite if $h(a^*a)>0$ for all $0\not=a\in A$. There are different equivalent definitions of Dijkhuizen's and Koornwinder's [@DK] notion of a [CQG ]{.sans-serif}algebra, the following is a convenient starting point for our purposes.

::: defi
We call the Hopf $*$-algebra $A$ a Compact Quantum Group [(]{.upright}[CQG]{.sans-serif}[)]{.upright} algebra if there exists a positive definite Haar functional on $A$.
:::

The positive definite Haar functional on a [CQG ]{.sans-serif}algebra $A$ is unique. Several concrete examples of [CQG ]{.sans-serif}algebras (such as the algebra of representative functions on a compact group, the basic commutative example) will be discussed in detail in the following two sections.

Let $A$ be a [CQG ]{.sans-serif}algebra with normalized, positive definite Haar functional $h$. The following results are all from [@DK]. Any finite-dimensional right $A$-comodule is unitarizable, hence completely reducible. We denote $\Sigma$ for the set of equivalence classes of finite dimensional, (unitary) irreducible right $A$-comodules. For $\alpha\in\Sigma$ let $\pi_\alpha: L_\alpha\rightarrow L_\alpha\otimes A$ be a representative of the corresponding irreducible, finite dimensional $A$-comodule. Let $\pi_\alpha^*: L_\alpha^*\rightarrow
L_\alpha^*\otimes A$ be the corresponding dual right $A$-comodule, defined by requiring $$\bigl(\pi_\alpha^*(\phi)\bigr)\bigl(v\otimes 1_A)=
\bigl(\phi\otimes S\bigr)\bigl(\pi_\alpha(v)\bigr),\qquad v\in L_\alpha,\,\,\phi\in L_\alpha^*,$$ where $1_A$ denotes the unit element of $A$. Then $\{L_\alpha^*\otimes L_\alpha \, | \, \alpha\in\Sigma \}$ is a complete set of representatives of the irreducible, finite dimensional $A\otimes A$-comodules.

Consider $A$ as a right $A\otimes A$-comodule by $$R(a)=\sum_{(a)}a_{(2)}\otimes S(a_{(1)})\otimes a_{(3)},\qquad a\in A,$$ where we use the standard Sweedler notation for (iterated) applications of the comultiplication. The first key property of [CQG ]{.sans-serif} algebras is the irreducible decomposition $$A\simeq \bigoplus_{\alpha\in\Sigma}L_\alpha^*\otimes L_\alpha$$ of $A$ as right $A\otimes A$-comodule (the Peter-Weyl Theorem for [CQG ]{.sans-serif}algebras). Concretely, the isomorphism is realized by mapping $\phi\otimes v\in L_\alpha^*\otimes L_\alpha$ to $(\phi\otimes\hbox{Id}_A)(\pi_\alpha(v))\in A$. We denote $A_h$ for the Hilbert space completion of $A$ with respect to the pre-Hilbert structure $$\langle a,b\rangle_h:=h(b^*a).$$

Let $(\pi, V)$ be a finite dimensional, irreducible, right $A$-comodule. Consider the canonical linear isomorphism $\varphi: V\rightarrow V^{**}$ defined by $\varphi(v)f:=f(v)$ for $f\in V^*$ and $v\in V$. We turn $V$ into a finite dimensional Hilbert space such that $(\pi, V)$ is a unitary right $A$-comodule (such scalar product is unique up to a strictly positive scalar multiple). Since the double-dual right $A$-comodule $(\pi^{**},V^{**})$ is equivalent to $(\pi, V)$, there exists a unique positive definite, linear isomorphism $F=F_V: V\rightarrow V$ such that $$\hbox{Tr}_V(F)=\hbox{Tr}_V(F^{-1})>0$$ and such that $\varphi\circ F: (\pi, V)\rightarrow (\pi^{**}, V^{**})$ is an intertwiner of right $A$-comodules (see [@DK Prop. 3.6]).

::: defi
[]{#qDimdef label="qDimdef"} Let $A$ be a [CQG ]{.sans-serif}algebra, $(\pi,V)$ a finite dimensional, irreducible right $A$-comodule and $F: V\rightarrow V$ the linear isomorphism as defined above. Then $$\textup{Dim}_A(V):=\textup{Tr}_V\bigl(F\bigr)$$ is called the quantum dimension of the right $A$-comodule $(\pi, V)$.
:::

A second key property of [CQG ]{.sans-serif}algebras is the generalized Schur orthogonality relations [@DK Prop. 3.4 & 3.5], which we now proceed to recall.

::: prop
[]{#Schur label="Schur"} Let $A$ be a [CQG ]{.sans-serif}algebra. Let $(\pi,V)$ and $(\pi',V')$ be finite dimensional, irreducible, unitary right $A$-comodules with associated scalar products $\langle \cdot,\cdot\rangle_{\pi}$ and $\langle \cdot,\cdot\rangle_{\pi'}$.

1.  If $\pi \not\simeq\pi'$, then $$\langle \langle \pi(u),v\rangle_{\pi},
    \langle \pi'(u'), v'\rangle_{\pi'}\rangle_h=0$$ for $u,v\in V$ and $u^\prime, v^\prime\in V'$.

2.  For $u_1,u_2,v_1,v_2\in V$ we have $$\langle \langle \pi(u_1),v_1\rangle_\pi,
    \langle \pi(u_2), v_2\rangle_\pi\rangle_h= \frac{\langle
    u_1,u_2\rangle_\pi\langle F_V^{-1}v_2,v_1\rangle_\pi}
    {\textup{Dim}_A(V)}.$$
:::

Let $A$ be a [CQG ]{.sans-serif}algebra. A quantum subgroup of $A$ is a pair $(B,p)$ with $B$ a Hopf $*$-algebra and $p: A\rightarrow B$ a surjective Hopf $*$-algebra homomorphism. In this situation, we write $$A_B=\{a\in A \, | \, \bigl(\hbox{Id}_A\otimes p\bigr)\bigl(\Delta(a)\bigr)=a\otimes 1_B \}$$ for the $*$-subalgebra of right $B$-invariant elements in $A$. The $*$-subalgebra $A_B\subset A$ is a right $A$-comodule under the right regular co-action $$\rho_B(a)=\sum_{(a)}a_{(2)}\otimes S(a_{(1)}),\qquad a\in A_B.$$ By the Peter-Weyl Theorem for $A$, the right $A$-comodule $A_B$ decomposes into irreducibles as $$\label{PWB}
A_B\simeq \bigoplus_{\alpha\in\Sigma} L_\alpha^*\,{}^{ \textup{Dim}_{\mathbb{C}}(L_\alpha^B)},$$ where for a right $A$-comodule $(\pi, V)$, $$V^B=\{v\in V \, | \, \bigl(1\otimes p)\bigl(\pi(v)\bigr)=v\otimes 1_B\}$$ is the space of $B$-invariant elements in $V$.

::: defi
[]{#qGelfandPair label="qGelfandPair"} A [CQG ]{.sans-serif}algebra $A$ with quantum subgroup $(B,p)$ is called a quantum Gelfand pair if $$\textup{Dim}_{\mathbb{C}}(L_\alpha^B)\leq 1\qquad
\forall\,\alpha\in\Sigma,$$ [(]{.upright}compare with [@F][)]{.upright}.
:::

We fix a quantum Gelfand pair $(A,B)$. We call a finite dimensional, irreducible $A$-comodule $B$-spherical if it has nonzero $B$-invariant vectors. We denote $\Sigma_B\subset\Sigma$ for the corresponding subset of equivalence classes of the $B$-spherical, irreducible, finite dimensional right $A$-comodules.

In the various examples associated to (quantum) Grassmannians which we discuss in the following sections, we will identify $\Sigma_B$ with a certain fixed set of partitions. An important, but case-by-case different, aspect is the concrete characterization of the spherical irreducibles in terms of their parameterizing set $\Sigma_B$. To maintain uniform notations as much as possible, it will therefore be convenient to denote irreducible comodules labeled by $\Sigma_B$ by new symbols $\{V_{\alpha}~|~ \alpha \in \Sigma_B \}$.

We write $\langle \cdot,\cdot\rangle_\alpha$ for a scalar product on $V_\alpha$ that turns $V_\alpha$ into a unitary right $A$-comodule. Note that $\Sigma_B$ is invariant under $\circ$, were $\circ$ is the involution on $\Sigma$ such that $V_\alpha^*\simeq V_{\alpha^\circ}$ for all $\alpha\in \Sigma$. In fact, if we fix a nonzero vector $v_\alpha\in V_\alpha^B$ ($\alpha\in\Sigma_B$), then $\langle
\cdot,v_\alpha\rangle_\alpha\in V_\alpha^*{}^B$. Combined with [\[PWB\]](#PWB){reference-type="eqref" reference="PWB"}, we obtain the multiplicity free irreducible decomposition $$\label{AB}
A_B=\bigoplus_{\alpha\in\Sigma_B}V_\alpha$$ as right $A$-comodules.

From the present perspective, the natural definition of the quantum zonal spherical functions would be $$\widetilde{\varphi}_\alpha=\langle\pi_\alpha(v_\alpha), v_\alpha\rangle_\alpha, \qquad
\forall\,\alpha\in\Sigma_B,$$ since they form a $\mathbb{C}$-basis of the $*$-algebra $${}_BA_B=\{a\in A \, | \, \bigl(\hbox{Id}_A\otimes p\otimes p\bigr)R(a)=a\otimes 1_B\otimes 1_B\}$$ of $B$-biinvariant elements in $A$. It turns out though that the following slightly modified definition of the quantum zonal spherical functions is a better choice.

::: defi
[]{#qzs label="qzs"} The quantum zonal spherical functions associated to the quantum Gelfand pair $(A,B)$ are defined by $$\varphi_\alpha=\langle \pi_\alpha(v_\alpha), F_{V_{\alpha}}^{\frac{1}{2}}v_\alpha\rangle_\alpha\in A,\qquad
\forall\,\alpha\in\Sigma_B,$$ where $0\not=v_\alpha\in V_\alpha^B$ and $F_{V_\alpha}^{\frac{1}{2}}$ is the square root of the positive definite linear operator $F_{V_\alpha}$ on $V_\alpha$.
:::

Note that the quantum zonal spherical function $\varphi_\alpha$ ($\alpha\in\Sigma_B$) is uniquely determined up to nonzero scalar multiples. The square root of the positive definite operator $F_{V_\alpha}$ naturally appears in the definition of quantum zonal spherical functions on quantum homogeneous spaces using Noumi's [@N] two-sided coideal approach. It is this approach, and its generalization in terms of coideal algebras by Letzter (see [@L] and references therein), which has led to the identification of Macdonald polynomials as radial parts of quantum zonal spherical functions, see also Section [\[quantum\]](#quantum){reference-type="ref" reference="quantum"} for the quantum complex Grassmannian.

It now follows from the preceding discussions that we have the following expression for the quantum dimension of $V_\alpha$ in terms of the associated quantum zonal spherical function $\varphi_\alpha$ and the associated $B$-invariant vector $v_\alpha\in V_\alpha^B$.

::: prop
[]{#propqdim label="propqdim"} Let $(A,B)$ be a quantum Gelfand pair. For $\alpha\in\Sigma_B$ we have $$\textup{Dim}_A\bigl(V_\alpha\bigr)=\frac{\|v_\alpha\|_\alpha^4}{\|\varphi_\alpha\|_h^2}.$$
:::

::: proof
*Proof.* This follows directly using the definition of $\varphi_\alpha$ and the generalized Schur orthogonality relations (Proposition [\[Schur\]](#Schur){reference-type="ref" reference="Schur"}b). ◻
:::
