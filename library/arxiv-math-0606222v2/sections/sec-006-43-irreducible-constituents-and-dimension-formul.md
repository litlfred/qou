---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-006-43-irreducible-constituents-and-dimension-formul
section_title: "Irreducible constituents and dimension formulas: the non-Archimedean case"
section_number: 4.3
pages: 14-16
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.972
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#repp label="repp"}

In this subsection we fix a non-Archimedean local field $\mathbb{F}$. Let $\mathcal{O}$ denote the ring of integers and $\mathfrak{p}$ the maximal ideal. The Grassmann representation $\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)$ was studied in [@Hill] and later in [@BO1; @BO2]. Therein it is shown that the irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representations are also parameterized by $\Lambda_n$. We now proceed to recall the explicit construction of the irreducibles. The path to the construction of these representations is completely different compared to the Archimedean case. First of all, there is no (highest) weight theory, in particular there is no concrete description of the full unitary dual $\hat{\mathcal{K}}_{\mathbb{F}}$ as in the Archimedean case. We thus have to resort to a direct construction of the spherical unitary dual $(\mathcal{K}_{\mathbb{F}}/\mathcal{M}_{\mathbb{F}})\hat{~}$ and the concrete construction of the corresponding representations, which has a combinatorial flavor due to the profinite nature of $\mathcal{K}_{\mathbb{F}}$, $$\mathcal{K}_{\mathbb{F}}
\simeq\underset{\longleftarrow}{\textup{lim}}\,\textup{GL}_d(\mathcal{O}/\mathfrak{p}^k).$$ The latter identification is realized by the canonical epimorphisms $\pi_k: \mathcal{K}_{\mathbb{F}}\rightarrow \textup{GL}_d(\mathcal{O}/\mathfrak{p}^k)$ defined by reduction modulo $\mathfrak{p}^k$ ($k\in\mathbb{Z}_{>0}$). Denoting $I_k$ for the kernel of $\pi_k$, one has (cf. [@BO2]) $$\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)\simeq
\underset{\longrightarrow}{\textup{lim}}\,\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)^{I_k}$$ as $\mathcal{K}_{\mathbb{F}}$-representations, where $\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)^{I_k}$ stands for the $\mathcal{K}_{\mathbb{F}}$-module consisting of the $I_k$-fixed vectors in the Grassmann representation. The structure of the Grassmann representation is completely determined by its so-called level $k-1$ components $\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)^{I_k}$ for $k\in\mathbb{Z}_{>0}$. We proceed now to recall the precise structure of these level components.

The set of partitions $\Lambda_n$ parametrizes the isomorphism classes of the finite dimensional $\mathcal{O}$-modules of rank $\leq n$. Concretely, the partition $\lambda\in\Lambda_n$ corresponds to the isomorphism class of the finite $\mathcal{O}$-module $\oplus_{i=1}^n
\mathcal{O}/\mathfrak{p}^{\lambda_i}$. The finite $\mathcal{O}$-modules in the isomorphism class labeled by $\lambda\in\Lambda_n$ are called $\mathcal{O}$-modules of type $\lambda$. Denote $\subseteq$ for the partial order on partitions defined by inclusion of Young diagrams. Fix a module of type $k^d=(k,\ldots,k)$ ($d$ entries). For any type $\lambda \subseteq
k^d$ let $\mathcal{G}(\lambda,k^d;\mathcal{O})$ be the Grassmannian of its submodules of type $\lambda$. Let $\mathbb{C}\bigl(\mathcal{G}(\lambda,k^d;\mathcal{O})\bigr)$ be the vector space of complex valued functions on $\mathcal{G}(\lambda,k^d;\mathcal{O})$. The canonical action of $\mathcal{K}_{\mathbb{F}}$ on $\mathcal{G}(\lambda,k^d;\mathcal{O})$ gives rise to a representation of $\mathcal{K}_{\mathbb{F}}$ on $\mathbb{C}\bigl(\mathcal{G}(\lambda,k^d;\mathcal{O})\bigr)$. The finite Grassmann representations relate to the Grassmann representation $\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)$ by the identification $$\label{identification}
\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)^{I_k}\simeq\mathbb{C}\bigl(\mathcal{G}(k^n,k^d;\mathcal{O})\bigr)$$ as $\mathcal{K}_{\mathbb{F}}$-modules, see [@BO2 Lemma 2.1].

The irreducible constituents of the finite Grassmann representation $\mathbb{C}\bigl(\mathcal{G}(k^n,k^d;\mathcal{O})\bigr)$ have been explicitly described in [@BO2] in terms of the so-called cellular basis of the associated finite Hecke algebra $\hbox{End}_{\mathcal{K}_{\mathbb{F}}}\bigl(\mathbb{C}\bigl(\mathcal{G}(k^n,k^d;\mathcal{O})\bigr)\bigr)$. It leads to a natural parametrization of the irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representations by partitions $\Lambda_n$, as described in the following theorem, which is a direct consequence of [@BO2 Theorem 1].

Denote $\Lambda_n^k$ for partitions $\lambda\in\Lambda_n$ satisfying $\lambda\subseteq k^n$. Furthermore, for an irreducible $\mathcal{K}_{\mathbb{F}}$-module $V$ we denote $\langle V:\mathbb{C}\bigl(\mathcal{G}(\mu,k^d;\mathcal{O})\bigr)\rangle$ for the multiplicity of $V$ in the $\mathcal{K}_{\mathbb{F}}$-module $\mathbb{C}\bigl(\mathcal{G}(\mu,k^d;\mathcal{O})\bigr)$.

::: thm
[]{#pthm label="pthm"} For $\lambda\in\Lambda_n$ there exists a unique irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representation $V_\lambda^{\mathbb{F}}$ satisfying, for all $k\in\mathbb{Z}_{>0}$ such that $\lambda\in\Lambda_n^k$,

1.  $\langle V_\lambda^{\mathbb{F}}:\mathbb{C}\bigl(\mathcal{G}(\mu,k^d;\mathcal{O})\bigr)\rangle\geq 1$ for $\mu\in\Lambda_n^k$ satisfying $\lambda\subseteq\mu$,

2.  $\langle V_\lambda^{\mathbb{F}}:\mathbb{C}\bigl(\mathcal{G}(\mu,k^d;\mathcal{O})\bigr)\rangle=0$ for $\mu\in\Lambda_n^k$ satisfying $\lambda\not\subseteq\mu$.

The $\mathcal{K}_{\mathbb{F}}$-representations $V_\lambda^{\mathbb{F}}$ [(]{.upright}$\lambda\in\Lambda_n$[)]{.upright} form a complete set of representatives of the irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representations.
:::

Theorem [\[pthm\]](#pthm){reference-type="ref" reference="pthm"} gives the multiplicity free irreducible decomposition $$\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{F})\bigr)\simeq\bigoplus_{\lambda \in
\Lambda_n}V^{\mathbb{F}}_{\lambda}$$ as $\mathcal{K}_{\mathbb{F}}$-modules, as well as the identifications $$(\mathcal{K}_{\mathbb{F}}/\mathcal{M}_{\mathbb{F}})\hat{~}\simeq\Lambda_n\simeq\left\{ \text{isomorphism types of
$\mathcal{O}$-modules of rank $\le n$}  \right\}.$$ Furthermore, [\[identification\]](#identification){reference-type="eqref" reference="identification"} and Theorem [\[pthm\]](#pthm){reference-type="ref" reference="pthm"} imply $$\label{irrk}
\mathbb{C}\bigl(\mathcal{G}(k^n, k^d;\mathcal{O})\bigr)\simeq\bigoplus_{\lambda\in\Lambda_n^k}V^{\mathbb{F}}_{\lambda}$$ for $k\in\mathbb{Z}_{>0}$ as $\mathcal{K}_{\mathbb{F}}$-modules, cf. [@BO2 Prop. 2.2]. The following is one of the main results in this paper.

::: thm
[]{#thm-dim-padic label="thm-dim-padic"} Let $t=|\mathcal{O}/\mathfrak{p}|^{-1}$. We have $$\label{padic-dimension}
\textup{Dim}_{\mathbb{C}}(V^{\mathbb{F}}_{\lambda})=t^{-(d-2n+1)|\lambda|-2(\rho,\lambda)}\left[
{n \atop \partial\lambda' }\right]_t
\frac{(t^{d-\lambda'_1-\lambda'_2+2};t)_{\lambda'_1+\lambda'_2}}{(t^{n-\lambda'_1+1};t)_{\lambda'_1}}
\frac{(1-t^{d-2\lambda'_1+1})}{(1-t^{d+1})}$$ for $\lambda\in\Lambda_n$.
:::

Theorem [\[thm-dim-padic\]](#thm-dim-padic){reference-type="ref" reference="thm-dim-padic"} is a direct consequence of the formula $$\label{reldimD0}
\hbox{Dim}_{\mathbb{C}}\bigl(V_\lambda^{\mathbb{F}}\bigr)=
D_0\bigl(\lambda;t^{d-2n+1},t;t),\qquad
t=|\mathcal{O}/\mathfrak{p}|^{-1}$$ from [@OU1], and the explicit evaluation of $D_0(\lambda;a,b;t)$ derived in Theorem [\[padicformula\]](#padicformula){reference-type="ref" reference="padicformula"}. Formula [\[reldimD0\]](#reldimD0){reference-type="eqref" reference="reldimD0"} is obtained in [@OU1] as a consequence of [\[dimforclassical\]](#dimforclassical){reference-type="eqref" reference="dimforclassical"} and the identification of the zonal spherical function $\varphi_\lambda^{\mathbb{F}}$ with a suitable $p$-adic ($q=0$) degeneration of the multivariable little $q$-Jacobi polynomial $P_\lambda^L$.

::: cor
[]{#identity label="identity"} For $k\in\mathbb{Z}_{>0}$ we have $$\sum_{\lambda \subseteq k^n}
t^{-(d-2n+1)|\lambda|-2(\rho,\lambda)}\left[ {n \atop
\partial\lambda' }\right]_t
\frac{(t^{d-\lambda'_1-\lambda'_2+2};t)_{\lambda'_1+\lambda'_2}}{(t^{n-\lambda'_1+1};t)_{\lambda'_1}}
\frac{(1-t^{d-2\lambda'_1+1})}{(1-t^{d+1})} =t^{-n(d-n)(k-1)}\left(
{d \atop n }\right)_{t^{-1}}.$$
:::

::: proof
*Proof.* Since the desired expression is rational in $t$, it suffices to prove the identity with the formal parameter $t^{-1}$ specialized to the cardinality of the residue field of a non-Archimedean local field $\mathbb{F}$. In this case, the identity immediately follows from [\[irrk\]](#irrk){reference-type="eqref" reference="irrk"}, [\[identification\]](#identification){reference-type="eqref" reference="identification"}, [\[padic-dimension\]](#padic-dimension){reference-type="eqref" reference="padic-dimension"} and the easily verified identity (alternatively see e.g. [@BO2 Claim 4.1(1)]) $$\label{cardinality}
|\mathcal{G}(k^n,k^d;\mathcal{O})|=t^{-n(d-n)(k-1)}\left( {d \atop n
}\right)_{t^{-1}},\qquad t=|\mathcal{O}/\mathfrak{p}|^{-1}.$$ ◻
:::

For $n=1$, Corollary [\[identity\]](#identity){reference-type="ref" reference="identity"} reduces to the trivial geometric sum identity $$1+t^{1-d}\frac{(1-t^{d-1})}{(1-t)}+\frac{(1-t^{d-1})(1-t^d)}{(1-t)}
\sum_{m=2}^kt^{(1-d)m}=t^{(1-d)k}\frac{(1-t^d)}{(1-t)}.$$

We end this subsection by discussing the dimension formula [\[padic-dimension\]](#padic-dimension){reference-type="eqref" reference="padic-dimension"} in two cases that the dimensions have been computed before by representation theoretic methods. The dimension formula [\[padic-dimension\]](#padic-dimension){reference-type="eqref" reference="padic-dimension"} yields for $r=1,\ldots,n$, $$\label{padicfundamental}
\hbox{Dim}_{\mathbb{C}}\bigl(V_{\omega_r}^{\mathbb{F}}\bigr)
=t^{r(r-d)}\frac{\bigl(t^{d-r+2};t\bigr)_r(1-t^{d-2r+1})}
{\bigl(t;t\bigr)_r(1-t^{d+1})}=\left( {d \atop r}\right)_{t^{-1}}-\left({d \atop r-1}
\right)_{t^{-1}}$$ where $t=|\mathcal{O}/\mathfrak{p}|^{-1}$. Alternatively, by [\[irrk\]](#irrk){reference-type="eqref" reference="irrk"} $$\mathbb{C}\bigl(\mathcal{G}(\omega_r,1^d;\mathcal{O})\bigr)\simeq
\mathbb{C}\bigl(\mathcal{G}(\omega_{r-1},1^d;\mathcal{O})\bigr)\oplus
V_{\omega_r}^{\mathbb{F}},$$ which implies [\[padicfundamental\]](#padicfundamental){reference-type="eqref" reference="padicfundamental"} in view of [\[cardinality\]](#cardinality){reference-type="eqref" reference="cardinality"}. The latter representation theoretic derivation essentially is the argument from [@D].

A similar analysis applies for the irreducible representations $V_{k}^{\mathbb{F}}$ ($k\in \mathbb{Z}_{\geq 2}\subset \Lambda_1$) arising in the representation $\mathbb{C}\bigl(\mathcal{G}(1,d;\mathbb{F})\bigr)$ associated to the projective space $\mathbb{P}^d(\mathbb{F})=\mathcal{G}(1,d;\mathbb{F})$, see [@Haran] and [@OU1 §4]. In this case, [\[padic-dimension\]](#padic-dimension){reference-type="eqref" reference="padic-dimension"} yields $$\hbox{Dim}_{\mathbb{C}}\bigl(V_{k}^{\mathbb{F}}\bigr)=t^{-(d-1)k}\frac{(1-t^{d-1})(1-t^d)}{(1-t)}
=t^{-(d-1)k}\frac{(1-t^d)}{(1-t)}-t^{-(d-1)(k-1)}\frac{(1-t^d)}{(1-t)}$$ where $t=|\mathcal{O}/\mathfrak{p}|^{-1}$. This dimension formula can be reconfirmed using [\[cardinality\]](#cardinality){reference-type="eqref" reference="cardinality"} and the decomposition $$\mathbb{C}\bigl(\mathcal{G}(k^1,k^d;\mathcal{O})\bigr)\simeq
\mathbb{C}\bigl(\mathcal{G}((k-1)^1,(k-1)^d;\mathcal{O})\bigr)\oplus V_{k}^{\mathbb{F}}$$ as $\mathcal{K}_{\mathbb{F}}$-modules, which is a direct consequence of [\[irrk\]](#irrk){reference-type="eqref" reference="irrk"}.
