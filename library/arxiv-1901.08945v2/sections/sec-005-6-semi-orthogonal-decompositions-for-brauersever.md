---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-005-6-semi-orthogonal-decompositions-for-brauersever
section_title: "Semi-orthogonal decompositions for Brauer–Severi schemes"
section_number: 6
pages: 24-27
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.969
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
[]{#sec:brau-severi-vari label="sec:brau-severi-vari"} In this section, we demonstrate how to use the theory of gerbes developed by Giraud to obtain a simple and conceptually appealing proof for the existence of the semi-orthogonal decomposition of the derived category of a Brauer--Severi scheme given by Bernardara [@bernardara-BS-schemes Theorem 4.1]. We start by recalling some basic facts on Brauer--Severi schemes and their trivializing gerbes from [@giraud1971 Example V.4.8].

Let $S$ be an arbitrary algebraic stack. An algebraic stack $P$ over $S$ is called a *Brauer--Severi scheme* over $S$ if it is *fppf*-locally (on $S$) isomorphic to a projectivized vector bundle. Of course $P$ need not be a scheme in general; the terminology is motivated by the fact that the structure morphism to $S$ is representable by schemes.

Given a Brauer--Severi scheme $\pi\colon P \to S$, we consider its *gerbe of trivializations* and denote it by $\beta\colon B \to S$. Let $t\colon T \to S$ be a morphism. The $t$-points of $B$ are pairs $(\mathcal{V}, v)$, where $\mathcal{V}$ is a finite locally free sheaf of $\mathcal{O}_T$-modules and $v\colon P_{T} \xrightarrow{\sim} \mathbb{P}(\mathcal{V}^\vee)$ is an isomorphism over $T$. The gerbe $B$ is endowed with a tautological finite locally free sheaf $\mathcal{E}$ of $\mathcal{O}_{B}$-modules. This is obtained on $t$-points $(\mathcal{V}, v)$ as above by simply forgetting the isomorphism $v$. The gerbe $B$ also has an obvious banding by ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ given on $t$-points as above by the usual action by $\mathcal{O}^\times_{T}(T)$ on $\mathcal{V}$. In particular, the tautological sheaf $\mathcal{E}$ is a $\beta$-twisted sheaf over $S$ in the sense of Definition [\[def:twisted\]](#def:twisted){reference-type="ref" reference="def:twisted"}.

Note that by construction, the gerbe of trivializations fits into a 2-cartesian diagram $$\label{eq:tautological-triv}
  \xymatrix{
    {{\mathbb{P}}(\mathcal{E}^\vee)} \ar[r]^-{\gamma}\ar[d]_-{\rho} 
    & 
    {P} \ar[d]^-\pi\\
    {B} \ar[r]_-\beta 
    & {S,}
  }$$ which we call the *tautological trivialization diagram*.

The class $[\beta]$ of $\beta \colon B \rightarrow S$ (see Theorem [\[t:gerbes-H2\]](#t:gerbes-H2){reference-type="ref" reference="t:gerbes-H2"}) in $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$ is called the *Brauer class* of the Brauer--Severi scheme $\pi\colon P \to S$. This class vanishes if and only if $P$ is a projectivized vector bundle over $S$.

::: remark
[]{#rem-universal-gerbe-of-trivializations label="rem-universal-gerbe-of-trivializations"} Consider the Brauer--Severi scheme $\pi\colon [{\mathbb{P}}^{n - 1}/\mathop{\mathrm{PGL}}_n] \to \mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$. Its gerbe of trivializations can be identified with the ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbe $\alpha \colon \mathop{\mathrm{B}}\mathop{\mathrm{GL}}_n \to \mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$ in Example [\[ex-gerbes\]](#ex-gerbes){reference-type="ref" reference="ex-gerbes"}.[\[it-universal-projective\]](#it-universal-projective){reference-type="ref" reference="it-universal-projective"}. Note that the stack $\mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$ classifies Brauer--Severi schemes. Given a Brauer--Severi scheme $P$ over an arbitrary algebraic stack $S$, its gerbe of trivializations can be identified with the pull-back of $\alpha$ along the morphism $S \to \mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$ corresponding to $P$.
:::

::: theorem
[]{#t:sod-brauer-severi label="t:sod-brauer-severi"} Let $S$ be an algebraic stack and $\pi\colon P \to S$ a Brauer--Severi scheme of relative dimension $n \geq 0$ over $S$. Using the notation from above, we consider the tautological trivialization diagram [\[eq:tautological-triv\]](#eq:tautological-triv){reference-type="eqref" reference="eq:tautological-triv"}. Then the functors $$\label{eq:BS-full-faithful}
  \Phi_i \colon {\operatorname{D}}_{{\operatorname{qc}}, i}(B) \to {\operatorname{D}}_{{\operatorname{qc}}}(P), \qquad
  \mathcal{F} \mapsto \gamma_*(\mathcal{O}(i)\otimes \rho^*\mathcal{F}),$$ are fully faithful for each $i$. Moreover, for each $a \in \mathbb{Z}$, we have a semi-orthogonal decomposition $$\label{eq:BS-sod}
  {\operatorname{D}}_{\operatorname{qc}}(P) = \langle \mathop{\mathrm{Im}}\Phi_a, \ldots, \mathop{\mathrm{Im}}\Phi_{a + n} \rangle$$ into right admissible categories.
:::

::: remark
[]{#r:image-twisted label="r:image-twisted"} In particular (see Corollary [\[cor:twisted-power-derived\]](#cor:twisted-power-derived){reference-type="ref" reference="cor:twisted-power-derived"}), the essential image $\mathop{\mathrm{Im}}\Phi_i$ is equivalent to the category ${\operatorname{D}}_{{\operatorname{qc}}, \beta^i}(S)$ of $\beta^i$-twisted complexes on $S$ in the sense of Definition [\[def:derived-twisted\]](#def:derived-twisted){reference-type="ref" reference="def:derived-twisted"}. Recall that, as explained above, $[\beta] \in \mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$ is the Brauer class of $P$.
:::

::: proof
*Proof.* Since $\rho$ is the projectivization of a vector bundle of rank $n + 1$, it follows from [@BS-conservative Theorem 6.7] that the functors $$\Psi_i \colon {\operatorname{D}}_{\operatorname{qc}}(B) \to {\operatorname{D}}_{{\operatorname{qc}}}(\mathbb{P}(\mathcal{E}^\vee)), \qquad
\mathcal{F} \mapsto \mathcal{O}(i)\otimes \rho^*\mathcal{F},$$ are fully faithful and that $${\operatorname{D}}_{\operatorname{qc}}(\mathbb{P}(\mathcal{E}^\vee)) = \langle \mathop{\mathrm{Im}}\Psi_{a}, \ldots,  \mathop{\mathrm{Im}}\Psi_{a + n}\rangle$$ is a semi-orthogonal decomposition for any $a \in \mathbb{Z}$. Since both $\beta$ and $\gamma$ are ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbes, Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"} provides equivalences $$\prod_{d \in {\mathbb{Z}}} {\operatorname{D}}_{{\operatorname{qc}}, d}(B) 
    \xrightarrow[{}]{\sim}
    {\operatorname{D}}_{\operatorname{qc}}(B),
    \qquad
    \prod_{d \in {\mathbb{Z}}} {\operatorname{D}}_{{\operatorname{qc}}, d}({\mathbb{P}}(\mathcal{E}^\vee)) 
    \xrightarrow[{}]{\sim}
    {\operatorname{D}}_{\operatorname{qc}}({\mathbb{P}}(\mathcal{E}^\vee)).$$ By Proposition [\[p:pull-back-grading-derived\]](#p:pull-back-grading-derived){reference-type="ref" reference="p:pull-back-grading-derived"}, the pull-back $\rho^*$ preserves $d$-homogeneous objects for each $d \in {\mathbb{Z}}$. Since $\mathcal{E}^\vee$ is homogeneous of degree -1 we see from the canonical surjection $\rho^*(\mathcal{E}^\vee) \to
\mathcal{O}(1)$ and Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"} that $\mathcal{O}(1)$ is homogeneous of degree -1. This shows that $\Psi_i$ shifts the degree by $-i$. Hence we get a semi-orthogonal decomposition $${\operatorname{D}}_{{\operatorname{qc}}, 0}(\mathbb{P}(\mathcal{E}^\vee)) = \langle \mathop{\mathrm{Im}}\Psi'_{a}, \ldots,  \mathop{\mathrm{Im}}\Psi'_{a + n}\rangle,$$ where $\Psi'_i$ denotes the restriction of $\Psi_i$ to ${\operatorname{D}}_{{\operatorname{qc}}, i}(B)$. Since $\gamma$ is a gerbe, the pull-back $\gamma^*$ is fully faithful with essential image ${\operatorname{D}}_{{\operatorname{qc}}, 0}(\mathbb{P}(\mathcal{E}^\vee))$ by Proposition [\[t:equivalence-epi-derived\]](#t:equivalence-epi-derived){reference-type="ref" reference="t:equivalence-epi-derived"}. Therefore the theorem follows from the identities $\Phi_i = \gamma_*\circ\Psi'_i$. ◻
:::

::: remark
Note that Theorem [\[t:sod-brauer-severi\]](#t:sod-brauer-severi){reference-type="ref" reference="t:sod-brauer-severi"} differs from the corresponding decomposition in [@bernardara-BS-schemes Theorem 4.1] with respect to the sign of the Brauer class $\beta$. This is simply due to different sign conventions. We follow the convention used by Giraud in [@giraud1971 Example V.4.8].
:::

Similarly, as in the corresponding theorem for projectivized vector bundles (see [@BS-conservative Theorem 6.7, Corollary 6.8]), we also get semi-orthogonal decompositions for the categories of perfect complexes, of locally bounded pseudo-coherent complexes, and for the singularity categories, respectively. Following the notation from [@BS-conservative Section 2.3], we denote these categories by ${\operatorname{D}}_{\operatorname{pf}}(P)$, ${\operatorname{D}}^{\operatorname{lb}}_{\operatorname{pc}}(P)$ and ${\operatorname{D}}^{\operatorname{sg}}_{\operatorname{pc}}(P)$, respectively.

::: corollary
[]{#c:sod-brauer-severi label="c:sod-brauer-severi"} Keep the assumptions from Theorem [\[t:sod-brauer-severi\]](#t:sod-brauer-severi){reference-type="ref" reference="t:sod-brauer-severi"}. The functors $\Phi_i$ induce functors $$\begin{aligned}
\Phi^{\operatorname{pf}}_i & \colon {\operatorname{D}}_{{\operatorname{pf}}, i}(B) \to {\operatorname{D}}_{{\operatorname{pf}}}(P), \qquad
\Phi^{\operatorname{pc}}_i \colon {\operatorname{D}}^{\operatorname{lb}}_{{\operatorname{pc}}, i}(B) \to {\operatorname{D}}^{\operatorname{lb}}_{{\operatorname{pc}}}(P),\\
\Phi^{\operatorname{sg}}_i & \colon {\operatorname{D}}_{{\operatorname{sg}}, i}(B) \to {\operatorname{D}}_{{\operatorname{sg}}}(P),
\end{aligned}$$ where the source categories are the full subcategories of $i$-homogeneous objects in the categories ${\operatorname{D}}_{{\operatorname{pf}}}(B)$, ${\operatorname{D}}^{\operatorname{lb}}_{{\operatorname{pc}}}(B)$ and ${\operatorname{D}}_{\operatorname{sg}}(B)$ introduced above, respectively. Furthermore, for each $a \in \mathbb{Z}$, this yields a semi-orthogonal decomposition $$\begin{aligned}
\label{eq-sod-perfect}
{\operatorname{D}}_{\operatorname{pf}}(P) & = \langle \mathop{\mathrm{Im}}\Phi^{\operatorname{pf}}_a, \ldots, \Phi^{\operatorname{pf}}_{a + n}\rangle,
\intertext{
into admissible subcategories and semi-orthogonal decompositions
}
{\operatorname{D}}^{\operatorname{lb}}_{\operatorname{pc}}(P) & = \langle \mathop{\mathrm{Im}}\Phi^{\operatorname{pc}}_a, \ldots, \Phi^{\operatorname{pc}}_{a + n}\rangle,\\
{\operatorname{D}}_{\operatorname{sg}}(P) & = \langle \mathop{\mathrm{Im}}\Phi^{\operatorname{sg}}_a, \ldots, \Phi^{\operatorname{sg}}_{a + n}\rangle
\end{aligned}$$ into right admissible subcategories. In particular, if $S$ is Noetherian, we get the corresponding decomposition of ${\operatorname{D}}^{\operatorname{b}}_{\operatorname{coh}}(P) = {\operatorname{D}}^{\operatorname{lb}}_{\operatorname{pc}}(P)$.
:::

::: proof
*Proof.* The functors $\Phi_i$ and their right adjoints restrict to the subcategories of perfect complexes and the subcategories of locally bounded pseudo-coherent complexes, respectively. Indeed, this follows from the corresponding properties for $\Psi_i$ (cf. [@BS-conservative Corollary 6.8]) using the notation in the proof of Theorem [\[t:sod-brauer-severi\]](#t:sod-brauer-severi){reference-type="ref" reference="t:sod-brauer-severi"}. Hence the decompositions in the corollary into right admissible categories follow formally from Theorem [\[t:sod-brauer-severi\]](#t:sod-brauer-severi){reference-type="ref" reference="t:sod-brauer-severi"} (see [@BS-conservative Corollary 5.19]). Moreover, the restriction of each $\Psi_i$ to the category of perfect complexes has a left adjoint (cf. [@BS-conservative Corollary 6.8]). ◻
:::

::: remark
[]{#r:bernardara label="r:bernardara"} Let us explain why Bernardara's Theorem 4.1 from [@bernardara-BS-schemes] is a special case of the semi-orthogonal decomposition [\[eq-sod-perfect\]](#eq-sod-perfect){reference-type="eqref" reference="eq-sod-perfect"}. In Bernardara's setting, the base $S$ is a Noetherian, separated scheme with the additional property that any two points is contained in an open affine. In fact, he only states that $S$ should be locally noetherian with the extra condition on points, but the other properties are used implicitly since he uses results from Căldăraru's thesis, where the stronger assumptions are in effect [@caldararu2000 Section 2.1]. Bernardara's category ${\operatorname{D}}(S, \alpha)$ is the derived category of perfect complexes of $\alpha$-twisted coherent sheaves. By the comparison by Lieblich mentioned in Remark [\[rem-twisted-2-cocycle\]](#rem-twisted-2-cocycle){reference-type="ref" reference="rem-twisted-2-cocycle"}, this is equivalent to ${\operatorname{D}}_{\operatorname{pf}}({\ensuremath{\operatorname{Coh}}}_\alpha(S))$, which is easily seen to be equivalent to ${\operatorname{D}}_{\operatorname{pf}}({\ensuremath{\operatorname{Qcoh}}}_\alpha(S))$ by using that every quasi-coherent sheaf on the gerbe corresponding to $\alpha$ is a direct limit of its coherent subsheaves [@lmb2000 Theorem 15.4]. Now this category is equivalent to ${\operatorname{D}}_{{\operatorname{pf}}, \alpha}(S)$ since the functor [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is an equivalence under the assumptions on $S$ (see Remark [\[rem-trivial-case\]](#rem-trivial-case){reference-type="ref" reference="rem-trivial-case"}).
:::
