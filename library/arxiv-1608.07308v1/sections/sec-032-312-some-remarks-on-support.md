---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-032-312-some-remarks-on-support
section_title: "Some remarks on support"
section_number: 3.12
pages: 31-32
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.926
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:knots label="sub:knots"}

We now explore what the endpoints of a braid $\sigma$ say about the sheaf $\mathcal{B}_\sigma$ on $\mathrm{FHilb}_n^\text{dg}$. For any braid $\sigma$, let $w_\sigma \in S_n$ denote the underlying permutation.

::: proposition
(e.g. [@Hog Proposition 2.16]) For any braid $\sigma$ and for all $i\in \{1,...,n\}$, the left action of $x_i$ on the complex $\sigma \in K^b(\mathrm{SBim}_n)$ is homotopic to the right action of $x_{w_{\sigma(i)}}$.
:::

In short, we will say that the left action $R \curvearrowright \sigma$ is homotopic to the right action $\sigma \curvearrowleft_{w(\sigma)} R$, *twisted* by the permutation $w_{\sigma}$. As a consequence, we obtain the following result:

::: corollary
[]{#cor:support rouquier label="cor:support rouquier"} The $R$--module $\mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)} (\mathbf{1},\sigma)$ is supported on the subspace: $$\left\{x_i=x_{w_{\sigma}(i)},\ i=1,\ldots,n\right\}\subset \mathbb{C}^n.$$
:::

Our construction of Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} is predicated on the expectation that: $$\mathop{\mathrm{Hom}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1},\sigma) = R\Gamma(\mathrm{FHilb}_n^\text{dg},\mathcal{B}(\sigma))$$ and that moreover $\mathcal{B}(\sigma)$ can be reconstructed from the spaces $\mathop{\mathrm{Hom}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1},\sigma \cdot \prod_{i=1}^n L_i^{a_i})$ for all sequences of large enough natural numbers $(a_1,...,a_n)$. These Hom spaces in the category $\mathrm{SBim}_n$ are very hard to compute, and all we can say at this stage is that Corollary [\[cor:support rouquier\]](#cor:support rouquier){reference-type="ref" reference="cor:support rouquier"} still applies to them. Therefore, we obtain the following:

::: corollary
[]{#cor:support sheaves label="cor:support sheaves"} The complex $\mathcal{B}(\sigma) = \iota_*(\sigma)$ is supported on the subvariety: $$\mathrm{FHilb}^\emph{dg}_w := \rho^{-1} \left(\left\{x_i=x_{w_{\sigma}(i)},\ i=1,\ldots,n\right\} \right)\subset \mathrm{FHilb}_n^\emph{dg}= \mathrm{FHilb}_n^\emph{dg}(\mathbb{C})$$ where $\rho:\mathrm{FHilb}_n^\emph{dg}(\mathbb{C}) \rightarrow \mathbb{C}^n$ is the map that records the eigenvalues $(x_1,...,x_n)$, akin to [\[eqn:rho\]](#eqn:rho){reference-type="eqref" reference="eqn:rho"}.
:::

::: corollary
Suppose that the closure of $\sigma$ is connected. Then $\mathcal{B}(\sigma)$ is supported on $$\rho^{-1} \left( \left\{x_1=\ldots=x_n \right\} \right)=\mathrm{FHilb}_n(\mathrm{point})\times \mathbb{C}.$$
:::

::: remark
Following Section [\[sub:reduced\]](#sub:reduced){reference-type="ref" reference="sub:reduced"}, one can prove that if the closure of $\sigma$ is connected, then the sheaf $\mathcal{B}(\sigma)$ fibers trivially over $\mathbb{C}$, i.e.: $$\mathcal{B}(\sigma) = \overline{\mathcal{B}(\sigma)}\boxtimes \mathcal{O}_{\mathbb{C}}$$ for some sheaf $\overline{\mathcal{B}(\sigma)}\in D^b\mathrm{Coh}(\mathrm{FHilb}_n(\mathrm{point}))$. Since $\mathrm{FHilb}_n(\mathrm{point})$ is projective, the cohomology of this sheaf is expected to be finite-dimensional. Moreover, our conjectures imply the fact that this cohomology matches the *reduced* Khovanov-Rozansky homology of $\alpha$.
:::

In general, $\mathrm{FHilb}_w^\text{dg}$ may be quite complicated. However, for certain permutations $w=w_\sigma$ we can describe it explicitly. The baby case is when $w = (j,j+1)$ is a transposition.

::: definition
Define the dg subscheme $Z_j \subset \mathrm{FHilb}_n^{\text{dg}}$ by the following equation: $$\label{eqn:z periodic}
\mathcal{O}_{Z_j} := \left[\ldots \longrightarrow \frac {q^2t^2\mathcal{L}_j^2}{\mathcal{L}_{j+1}^{2}} \xrightarrow{y_{j,j+1}} \frac {q^2t\mathcal{L}_j}{\mathcal{L}_{j+1}} \xrightarrow{x_j-x_{j+1}} \frac {qt\mathcal{L}_j}{\mathcal{L}_{j+1}} \xrightarrow{y_{j,j+1}}  q\mathcal{O}\xrightarrow{x_j-x_{j+1}} \mathcal{O}\right].$$ Here $y_{j,j+1}:t\mathcal{L}_j\to \mathcal{L}_{j+1}$ is the map of line bundles induced by the homonymous coefficient of the matrix $Y$ in [\[eqn:triple matrices\]](#eqn:triple matrices){reference-type="eqref" reference="eqn:triple matrices"}, and the fact that $y_{j,j+1}(x_j-x_{j+1})=0$ follows from $[X,Y]=0$.
:::

::: remark
Formula [\[eqn:z periodic\]](#eqn:z periodic){reference-type="eqref" reference="eqn:z periodic"} implies the following exact sequence: $$\label{eqn:Z recursion}
\left[ q\mathcal{O}\xrightarrow{x_j-x_{j+1}}\mathcal{O}\right] \cong \left[\mathcal{O}_{Z_j} \xrightarrow{\text{Id}} \frac {qt\mathcal{L}_j}{\mathcal{L}_{j+1}} \otimes \mathcal{O}_{Z_j} [2] \right]$$
:::

Our motivation for defining $Z_j$ is the fact that: $$\label{eqn:transposition}
\mathcal{O}_{\mathrm{FHilb}_{(j,j+1)}^\text{dg}} = \mathcal{O}_{Z_j}$$ for all $j\in \{1,...,n-1\}$. The following proposition follows directly by iterating [\[eqn:transposition\]](#eqn:transposition){reference-type="eqref" reference="eqn:transposition"}.

::: proposition
[]{#prop:fh eqiv label="prop:fh eqiv"} Suppose that $w$ has cycle structure: $$(1,...,k_1)(k_1+1,...,k_2),...,(k_{r}+1,...,n)$$ for some sequence $0<k_1<\ldots<k_{r}<n$. Then the dg structure sheaf of $\mathrm{FHilb}_w^\emph{dg}$ has the following periodic resolution by locally free sheaves on $\mathrm{FHilb}_n^{\emph{dg}}$: $$\begin{gathered}
\label{eq:mf}
\mathcal{O}_{\mathrm{FHilb}_w^{\emph{dg}}} \cong \bigotimes_{j\notin \{k_1,...,k_r\}} \left[\ldots \longrightarrow \frac {q^2t\mathcal{L}_j}{\mathcal{L}_{j+1}} \xrightarrow{x_j-x_{j+1}} \frac {qt\mathcal{L}_j}{\mathcal{L}_{j+1}} \xrightarrow{y_{j,j+1}}  q\mathcal{O}\xrightarrow{x_j-x_{j+1}} \mathcal{O}\right].
\end{gathered}$$
:::

::: conjecture
[]{#conj:knots label="conj:knots"} Suppose that $\alpha = \prod_{i=0}^{r}(\sigma_{k_i+1}\cdots\sigma_{k_{i+1}-1})$ is a subword of the Coxeter word $\sigma_1\cdots\sigma_{n-1}$, for any sequence $0<k_1<\ldots<k_{r}<n$ as in Proposition [\[prop:fh eqiv\]](#prop:fh eqiv){reference-type="ref" reference="prop:fh eqiv"}. Then: $$\mathcal{B}(\alpha) = \mathcal{O}_{\mathrm{FHilb}_w^{\emph{dg}}}.$$
:::

::: example
[]{#ex:coxeter label="ex:coxeter"} For $\alpha=1$, the conjecture simply reads $\mathcal{B}(\alpha) = \mathcal{O}_{\mathrm{FHilb}_n^{\text{dg}}}$, as prescribed by Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"}. For $\alpha = \sigma_1\cdots\sigma_{n-1}$, the conjecture reads $\mathcal{B}(\alpha) = \mathcal{O}_{\mathrm{FHilb}_n^{\text{dg}}(\mathrm{point})\times \mathbb{C}}$.
:::

Conjecture [\[conj:knots\]](#conj:knots){reference-type="ref" reference="conj:knots"} gives a full description of $\mathcal{B}(\alpha)$ for all braids $\alpha$ on two strands (see Section [\[sec:n=2\]](#sec:n=2){reference-type="ref" reference="sec:n=2"} for the explicit construction in this case). Moreover, it completely describes $\mathcal{B}(\alpha)$ for the braids $\alpha = 1,s_1,s_2,s_1s_2$ on 3 strands, multiplied by arbitrary powers of the twists $\mathbf{FT}_2,\mathbf{FT}_3$. Building upon this, the following conjecture supersedes the main conjecture of [@GN], and it serves as one of the motivating examples of the present work:

::: conjecture
[]{#conj:torus knots label="conj:torus knots"} For $\text{gcd}(m,n)=1$, consider the torus braid $\alpha_{n,m}=(\sigma_1\cdots\sigma_{n-1})^m$. Then $$\label{eq:torus knots}
\mathcal{B}(\alpha_{m,n}) = \left(\bigotimes_{i=1}^n \mathcal{L}_i^{\left\lfloor\frac{im}{n}\right\rfloor-\left\lfloor\frac{(i-1)m}{n}\right\rfloor}\right) \otimes \mathcal{O}_{\mathrm{FHilb}_n^\emph{dg}(\mathrm{point})\times \mathbb{C}}$$
:::

See Sections [\[sec:n=2\]](#sec:n=2){reference-type="ref" reference="sec:n=2"} and [\[sec:n=3\]](#sec:n=3){reference-type="ref" reference="sec:n=3"} for detailed computations for two and three-strand torus braids.

::: remark
It was proved in [@GN] that the equivariant Euler characteristic of the right hand side of [\[eq:torus knots\]](#eq:torus knots){reference-type="eqref" reference="eq:torus knots"} is equal to the "refined Chern-Simons invariant" defined by Aganagic-Shakirov [@AS] and Cherednik [@Ch]. One can therefore consider Conjecture [\[conj:torus knots\]](#conj:torus knots){reference-type="ref" reference="conj:torus knots"} as a categorification of the conjectures in [@AS; @Ch] relating the Poincaré polynomial of Khovanov-Rozansky homology to these "refined invariants".
:::
