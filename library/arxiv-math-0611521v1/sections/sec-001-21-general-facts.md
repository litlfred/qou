---
doc_id: arxiv-math-0611521v1
doc_title: "The q-analogue of the wild fundamental group"
section_id: sec-001-21-general-facts
section_title: "General facts"
section_number: 2.1
pages: 8-10
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.988
doc_brief: "The q-analogue of the wild fundamental group — We describe an explicit construction of galoisian Stokes operators for irregular linear q-difference equations."
---
[]{#subsection:generalfacts label="subsection:generalfacts"}

#### Notations, general conventions.

We fix $q \in {\mathbf C}$ such that $|q| > 1$. We then define the automorphism $\sigma_q$ on various rings, fields or spaces of functions by putting $\sigma_qf(z) = f(qz)$. This holds in particular for the ring ${{\mathbf C}\{z\}}$ of convergent power series and its field of fractions ${{\mathbf C}(\{z\})}$, the ring ${{\mathbf C}[[z]]}$ of formal power series and its field of fractions ${{\mathbf C}((z))}$, the ring ${\mathcal{O}({\mathbf C}^{*},0)}$ of holomorphic germs and the field ${\mathcal{M}({\mathbf C}^{*},0)}$ of meromorphic germs in the punctured neighborhood of $0$, the ring ${\mathcal{O}({\mathbf C}^{*})}$ of holomorphic functions and the field ${\mathcal{M}({\mathbf C}^{*})}$ of meromorphic functions on ${\mathbf C}^{*}$; this also holds for all modules or spaces of vectors or matrices over these rings and fields. For any such ring (resp. field) $R$, the $\sigma_q$-invariants elements make up the subring (resp. subfield) $R^{\sigma_q}$ of constants. The field of constants of ${\mathcal{M}}({\mathbf C}^{*},0)$ and that of ${\mathcal{M}}({\mathbf C}^{*})$ can be identified with a field of elliptic functions, the field ${\mathcal{M}}({\mathbf{E}_{q}})$ of meromorphic functions over the complex torus ${\mathbf{E}_{q}}= {\mathbf C}^{*}/q^{{\mathbf Z}}$.\
We shall write $\overline{a} = \pi(a) \in {\mathbf{E}_{q}}$ for the image of $a \in {\mathbf C}^{*}$ by the natural projection $\pi: {\mathbf C}^{*} \rightarrow {\mathbf{E}_{q}}$, and $[a;q] = a q^{{\mathbf Z}} = \pi^{-1}(\overline{a}) \subset {\mathbf C}^{*}$ for the preimage of $\overline{a}$ in ${\mathbf C}^{*}$, a discrete $q$-spiral. These notations extend to subsets $A \subset {\mathbf C}^{*}$: $\overline{A} = \pi(A) \subset {\mathbf{E}_{q}}$ and $[A;q] = A q^{{\mathbf Z}} = \pi^{-1}(\overline{A}) \subset {\mathbf C}^{*}$.

#### Categories.

Let $K$ denote any one of the forementioned fields of functions. Then, we write ${\mathcal{D}_{q,K}}= K\left<\sigma,\sigma^{-1}\right>$ for the Öre algebra of non commutative Laurent polynomials characterized by the relation $\sigma . f = \sigma_q(f) . \sigma$. We now define the category of $q$-difference modules in three clearly equivalent ways: $$\begin{aligned}
{DiffMod(K,\sigma_q)}& = & \{(E,\Phi) \;/\; E \text{~a~} K \text{-vector space of finite rank~},
                        \Phi : E \rightarrow E \; 
                               \text{~a~} \sigma_q\text{-linear} \text{~map}\} \\
    & = & \{(K^{n}, \Phi_{A}) \;/\; A \in GL_{n}(K) ,
                                    \Phi_{A}(X) = A^{-1} \sigma_qX \} \\
    & = & \{\text{~finite length left~} {\mathcal{D}_{q,K}}\text{-modules}\}.
\end{aligned}$$ For instance, a morphism from $M_{A} = (K^{n}, \Phi_{A})$ to $M_{B} = (K^{n}, \Phi_{B})$, where $A \in GL_{n}(K)$ and $B \in GL_{p}(K)$, is a $F \in M_{p,n}(K)$ such that $(\sigma_q) F A = B F$. Then, ${DiffMod(K,\sigma_q)}$ is a ${\mathbf C}$-linear abelian rigid tensor category, hence a tannakian category. Moreover, all objects in ${DiffMod(K,\sigma_q)}$ have the form ${\mathcal{D}_{q,K}}/ {\mathcal{D}_{q,K}}P$. In the case of $K = {{\mathbf C}(\{z\})}$, the category ${DiffMod(K,\sigma_q)}$ will be written ${\mathcal{E}}^{(0)}$ (for "equations near $0$").

#### Vector bundles and fiber functors.

To any module $M_{A}$ in ${\mathcal{E}}^{(0)}$, one can associate a holomorphic vector bundle ${\mathcal{F}}_{A}$ over ${\mathbf{E}_{q}}$: $${\mathcal{F}}_{A} = \dfrac{({\mathbf C}^{*},0) \times {\mathbf C}^{n}}{(z,X) \sim (q z,A(z) X)} 
\rightarrow \dfrac{({\mathbf C}^{*},0)}{z \sim q z} = {\mathbf{E}_{q}}.$$ This is the usual construction from equivariant bundles except that the germ $({\mathbf C}^{*},0)$ is only endowed with the action of the semigroup $q^{-{\mathbf N}}$ instead of a group; correspondingly, the projection map is not a covering. The pullback $\tilde{{\mathcal{F}}_{A}} = \pi^{*}({\mathcal{F}}_{A})$ over the open Riemann surface ${\mathbf C}^{*}$ is the trivial bundle ${\mathbf C}^{*} \times {\mathbf C}^{n}$, but with an equivariant action by $q^{{\mathbf Z}}$. The ${\mathcal{O}}_{{\mathbf{E}_{q}}}$-module of sections of ${\mathcal{F}}_{A}$ (also written ${\mathcal{F}}_{A}$) is the sheaf over ${\mathbf{E}_{q}}$ defined by: ${\mathcal{F}}_{A}(V) = 
\{\text{solutions of~} \sigma_qX = A X \text{~holomorphic over~} \pi^{-1}(V)\}$. \>From these two descriptions, the following is immediate:

::: prop
This gives an exact faithful $\otimes$-functor $M_{A} \leadsto {\mathcal{F}}_{A}$ from ${\mathcal{E}}^{(0)}$ to the category $Fib({\mathbf{E}_{q}})$ of holomorphic vector bundles. Taking the fiber of $\tilde{{\mathcal{F}}_{A}}$ at $a \in {\mathbf C}^{*}$ yields a fiber functor $\omega^{(0)}_{a}$ on ${\mathcal{E}}^{(0)}$ over ${\mathbf C}$.
:::

#### Newton polygon.

Any $q$-difference module $M$ over ${{\mathbf C}(\{z\})}$ or ${{\mathbf C}((z))}$, can be given a Newton polygon $N(M)$ at $0$, or, equivalently, a Newton function $r_{M}$ sending the slope [^1] $\mu \in S(M) \subset {\mathbf Q}$ to its multiplicity $r_{M}(\mu) \in {\mathbf N}^{*}$ (and the $\mu$ out of the support $S(M)$ to $0$).\
For instance, the $q$-difference operator $L = q z \sigma^{2} - (1 + z) \sigma + 1 \in {\mathcal{D}_{q,K}}$ gives rise to the $q$-difference equation $q z \sigma_q^{2} f - (1+z) \sigma_qf+ f = 0$, of which the so-called Tschakaloff series $\sum_{n \geq 0}  q^{n(n-1)/2} z^{n}$ is a solution (it is a natural $q$-analogue of the Euler series). By vectorisation, this equation gives rise to the system $\sigma_qX = A X$, where $A = \begin{pmatrix} z^{-1} & z^{-1} \\ 0 & 1 \end{pmatrix}$, and to the module $M = M_{A}$. The latter is isomorphic to ${\mathcal{D}_{q,K}}/{\mathcal{D}_{q,K}}\hat{L}$, where $\hat{L} = \sigma^{2} - (z + 1) \sigma + z = (\sigma - z)(\sigma - 1)$ is the dual operator of $L$. We respectively attach to $\sigma - z$ and $\sigma - 1$ the slopes $-1$ and $0$ and take $S(M) = \{-1,0\}$, with multiplicities $r_{M}(-1) = r_{M}(0) = 1$.

[^1]: It should be noted that the slopes defined and used in the present paper are the *opposites* of the slopes defined in previous papers.
