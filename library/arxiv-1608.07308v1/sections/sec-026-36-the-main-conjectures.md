---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-026-36-the-main-conjectures
section_title: "The main conjectures"
section_number: 3.6
pages: 24-26
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.724
latex_coverage_ratio: 0.861
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:mainconj label="sub:mainconj"}

For the remainder of this Section, we will write $\mathrm{FHilb}_n^\text{dg}= \mathrm{FHilb}_n^\text{dg}(\mathbb{C})$ and $\mathcal{E}_n = \mathcal{E}_n(\mathbb{C})$, in the notation of Section [\[sec:flag\]](#sec:flag){reference-type="ref" reference="sec:flag"}. Our main Conjecture can be restated more precisely as follows:

::: Conjecture
There exists a pair of adjoint functors: $$\label{eqn:funk}
K^b(\mathrm{SBim}_n) \xtofrom[\iota^*]{\iota_*} D^b\left(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*} \left( \mathrm{FHilb}_n^{\emph{dg}} \right) \right)$$ where $\iota^*$ is monoidal and fully faithful. Moreover, we have: $$\label{eqn:sk}
\iota_*(\iota^*N_1 \otimes M \otimes \iota^*N_2) \cong N_1 \otimes \iota_*(M) \otimes N_2$$ for all $N_1,N_2 \in D^b\left(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*} \left( \mathrm{FHilb}_n^{\emph{dg}}\right) \right)$ and $M \in K^b(\mathrm{SBim}_n)$. In addition: $$\label{eqn:nice 1}
\iota_* \mathbf{1} = \mathcal{O}\quad \text{and} \quad L_k = \iota^{*}(\mathcal{L}_k) \qquad \stackrel{\eqref{eqn:sk}}\Longrightarrow$$ $$\label{eqn:nice 2}
\stackrel{\eqref{eqn:sk}}\Longrightarrow \qquad \iota_* L_k = \mathcal{L}_k \quad \forall \ k\in \{1,...,n\},$$ where $\mathcal{O}$ is the structure sheaf of $\mathrm{FHilb}_n^{\emph{dg}}$ and $\mathcal{L}_k$ is the line bundle [\[eqn:taut line\]](#eqn:taut line){reference-type="eqref" reference="eqn:taut line"}. Finally, the following diagrams of functors commute (we write $\iota = \iota_{(n)}$ to keep track of $n$): $$\label{eqn:diag1}
\includegraphics{3_20.png}$$ $$\label{eqn:diag2}
\includegraphics{3_21.png}$$ where the map $\pi : \mathrm{FHilb}_{n+1}^\emph{dg}\rightarrow \mathrm{FHilb}_n^\emph{dg}\times \mathbb{C}$ is the particular case of [\[eqn:tower\]](#eqn:tower){reference-type="eqref" reference="eqn:tower"} for $* = \mathbb{C}$.
:::

In broad strokes, the functor $\iota_*$ is given by sending each object $M \in K^b(\mathrm{SBim}_n)$ to: $$\label{eqn:general 1}
\iota_* M = \bigoplus_{a_1,...,a_n \in \mathbb{N}} \text{Hom}_{K^b(\mathrm{SBim}_n)} \left(\mathbf{1}, M \bigotimes_{k=1}^n L_k^{a_k} \right)$$ which is naturally a module for the $\mathbb{N}^n$--graded dg algebra: $$\label{eqn:general 2}
A = \bigoplus_{a_1,...,a_n \in \mathbb{N}} \text{Hom}_{K^b(\mathrm{SBim}_n)} \left(\mathbf{1}, \bigotimes_{k=1}^n L_k^{a_k} \right)$$ This algebra is commutative and $\iota_*M$ gives rise to a coherent sheaf on $(\mathrm{Spec}\ A)/(\mathbb{C}^*)^n$. Our conjecture entails the fact that this sheaf is actually supported on the $n$--fold iterated projectivization $\mathrm{Proj}A \hookrightarrow (\mathrm{Spec}\ A)/(\mathbb{C}^*)^n$, and that in fact: $$\label{eqn:general 3}
\mathrm{Proj}\ A = \mathrm{FHilb}_n^\text{dg}$$ To upgrade to the setting of Remark [\[rem:a grading\]](#rem:a grading){reference-type="ref" reference="rem:a grading"}, we must replace the Hom spaces by RHom in [\[eqn:general 1\]](#eqn:general 1){reference-type="eqref" reference="eqn:general 1"} and [\[eqn:general 2\]](#eqn:general 2){reference-type="eqref" reference="eqn:general 2"}. We expect that this can be dealt with as in the following conjecture.

::: conjecture
[]{#conj:a grading label="conj:a grading"} Given the setup of Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} we consider the object: $$T_n  = \iota^*(\mathcal{T}_n) \in K^b(\mathrm{SBim}_n)$$ Then we claim that for any object $M \in K^b(\mathrm{SBim}_n)$, we have an isomorphism: $$\label{eqn:rhom vs hom}
\mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1}, M) \cong \mathop{\mathrm{Hom}}_{K^b(\mathrm{SBim}_n)}\left(\mathbf{1}, M \otimes \wedge^\bullet T^\vee_n \right)$$ which is functorial with respect to the action of the algebra $A \curvearrowright M$ of [\[eqn:general 2\]](#eqn:general 2){reference-type="eqref" reference="eqn:general 2"}.
:::

Assuming Conjecture [\[conj:a grading\]](#conj:a grading){reference-type="ref" reference="conj:a grading"}, one may ask if there is a sheaf on the flag Hilbert scheme which is defined by replacing Hom with RHom in [\[eqn:general 1\]](#eqn:general 1){reference-type="eqref" reference="eqn:general 1"}. By [\[eqn:rhom vs hom\]](#eqn:rhom vs hom){reference-type="eqref" reference="eqn:rhom vs hom"} and [\[eqn:sk\]](#eqn:sk){reference-type="eqref" reference="eqn:sk"}, this sheaf would be: $$\iota_* \left(M \otimes \iota^*\left(\wedge^\bullet \mathcal{T}_n^\vee \right)\right) = \iota_*M \otimes \wedge^\bullet \mathcal{T}_n^\vee$$ This sheaf should naturally be thought to live on $\mathrm{Tot}_{\mathrm{FHilb}_n^\text{dg}} (\mathcal{T}_n[1]) = \mathrm{Spec}_{\mathrm{FHilb}_n^\text{dg}} \left(\wedge^\bullet \mathcal{T}_n^\vee \right)$, as in Remark [\[rem:a grading\]](#rem:a grading){reference-type="ref" reference="rem:a grading"}. The entire picture presented in this Subsection will be explained in more detail in Section [\[sec:geometry\]](#sec:geometry){reference-type="ref" reference="sec:geometry"}, when we develop the formalism of categories over schemes in general.

::: proof
*Proof of Corollary [\[cor:1\]](#cor:1){reference-type="ref" reference="cor:1"}.* The fact that $\iota^*$ is a monoidal functor, together with [\[eqn:nice 1\]](#eqn:nice 1){reference-type="eqref" reference="eqn:nice 1"}, imply that: $$\sigma := \prod_{k=1}^n \mathbf{FT}_k^{a_k} = \prod_{k=1}^n \iota^{*}(\det \mathcal{T}_k)^{\otimes a_k} = \iota^*\left(\bigotimes_{k} (\det \mathcal{T}_k)^{\otimes a_k}\right).$$ Corollary [\[cor:inv 1\]](#cor:inv 1){reference-type="ref" reference="cor:inv 1"} below implies that: $$\mathop{\mathrm{HHH}}( \sigma ) := \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1}, \sigma)= \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\sigma^{-1} , \mathbf{1})$$ while [\[eqn:rhom vs hom\]](#eqn:rhom vs hom){reference-type="eqref" reference="eqn:rhom vs hom"} implies that: $$\mathop{\mathrm{HHH}}( \sigma ) = \mathop{\mathrm{Hom}}_{K^b(\mathrm{SBim}_n)}(\sigma^{-1} \otimes \wedge^\bullet T_n, \mathbf{1}) = \mathop{\mathrm{Hom}}_{K^b(\mathrm{SBim}_n)} \left[ \iota^*\left(\bigotimes_{k} (\det \mathcal{T}_k)^{-a_k} \otimes \wedge^\bullet \mathcal{T}_n \right) , \mathbf{1} \right]$$ The adjunction of $\iota^*$ and $\iota_*$, together with the conjectured fact that $\iota_*\mathbf{1} = \mathcal{O}$, imply that: $$\mathop{\mathrm{HHH}}( \sigma ) = \mathop{\mathrm{{RHom}}}_{\mathrm{FHilb}_n^\text{dg}} \left( \bigotimes_{k} (\det \mathcal{T}_k)^{-a_k} \otimes \wedge^\bullet \mathcal{T}_n, \mathcal{O}\right)$$ Dualizing the RHom produces the desired result. ◻
:::

##  {#sub:topological computations}

Proposition [\[prop:dg scheme\]](#prop:dg scheme){reference-type="ref" reference="prop:dg scheme"} describes flag Hilbert schemes as projective towers, which implies that: $$\mathcal{E}_n \cong \pi_*(\mathcal{L}_{n+1}) \in D^b \left(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*} \left( \mathrm{FHilb}_n^\text{dg}\right) \right)$$ Define the following object: $$\label{eqn:def e}
E_n := \mathop{\mathrm{Tr}}(L_{n+1}) \in K^b(\mathrm{SBim}_n)$$ Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} implies that: $$\label{eqn:relation e}
\iota_*(E_n) = \iota_*(\mathop{\mathrm{Tr}}(L_{n+1})) = \pi_*(\iota_*(L_{n+1})) = \pi_*(\mathcal{L}_{n+1})) \cong \mathcal{E}_n.$$

::: conjecture
[]{#conj:main label="conj:main"}

The following topological facts hold for all $n\geq 0$.

-   $E_n$ is an explicit complex in terms of $I(E_{n-1})$ and $L_n$, as in [\[eqn:explicit\]](#eqn:explicit){reference-type="eqref" reference="eqn:explicit"} below.

-   The following equation holds in $K^b(\mathrm{SBim}_n[x_{n+1}])$: $$\label{eqn:conjmain}
    S^k E_n \cong \mathop{\mathrm{Tr}}(L_{n+1}^k) \quad \forall \ k\ge 0.$$

-   The Koszul complex $$\label{eqn:koszul topology}
    \left[... \stackrel{\eta}\longrightarrow I(\wedge^2 E_n) \otimes L_{n+1}^{-2} \stackrel{\eta}\longrightarrow I(E_n) \otimes L_{n+1}^{-1} \stackrel{\eta}\longrightarrow R \right]$$ is acyclic, where $I(E_n) \stackrel{\eta}\rightarrow L_{n+1}$ denotes the adjoint map to [\[eqn:def e\]](#eqn:def e){reference-type="eqref" reference="eqn:def e"}.
:::

Statement (a) implies that $E_n$ lies in the monoidal subcategory of $K^b(\mathrm{SBim}_n)$ generated by $L_1,...,L_n$. Since this subcategory is symmetric and Karoubian, the objects $S^k E_n$ and $\wedge^k E_n$ that appear in (b) and (c) are well-defined: as in [@Deligne], they are simply the projections of $E_n^{\otimes k}$ defined by the symmetric and antisymmetric projectors in the symmetric group $S_k$, respectively. The following result is proved in Section [\[sub:proof\]](#sub:proof){reference-type="ref" reference="sub:proof"}, and will show how to reduce our main Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} to the topological computations of Conjecture [\[conj:main\]](#conj:main){reference-type="ref" reference="conj:main"} (a)--(c).

::: theorem
[]{#thm:one implies the other label="thm:one implies the other"} Conjecture [\[conj:main\]](#conj:main){reference-type="ref" reference="conj:main"} implies Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"}.
:::
