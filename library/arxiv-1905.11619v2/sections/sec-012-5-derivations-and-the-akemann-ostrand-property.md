---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-012-5-derivations-and-the-akemann-ostrand-property
section_title: "Derivations and the Akemann-Ostrand property"
section_number: 5
pages: 17-18
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.92
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
[]{#Sect=AO label="Sect=AO"}

In this section we show that quantum Markov semi-groups may be used to prove the Akemann-Ostrand property AO$^+$ of a von Neumann algebra. In particular we find a new range of $q$ for which $q$-Gaussians have AO$^+$. Let us first recall the definition of the Akemann-Ostrand property that is most suitable for us, see [@IsonoTransactions].

::: dfn
A finite von Neumann algebra $M$ has condition AO$^+$ if there exists a $\sigma$-weakly dense unital C$^\ast$-subalgebra $A \subseteq M$ such that:

1.  $A$ is locally reflexive [@NateTaka Section 9];

2.  There exists a ucp map $\theta: A \otimes_{{\rm min}}A^{{\rm op}} \rightarrow B(L_2(M))$ such that $\theta( a \otimes b^{{\rm op}}) - a b^{{\rm op}}$ is compact for all $a,b\in A$.
:::

Let $M$ be a finite von Neumann algebra with faithful normal trace $\tau$. Let $\mathcal{A}$ be a $\ast$-subalgebra that is $\sigma$-weakly dense in $M$ with C$^\ast$-closure $A$. Let $\partial: \mathcal{A}\rightarrow H$ be a closable derivation to an $\mathcal{A}$-$\mathcal{A}$ bimodule $H$. Assume that $\mathcal{A}$ has some linear basis $e_i, i \in I$ with $I$ countable that is moreover orthonormal in $L_2(M)$. Define the linear map, $$\label{Eqn=S}
S: \mathcal{A}\rightarrow H: e_i \mapsto  \frac{\partial(e_i)}{\Vert \partial(e_i) \Vert},$$ where we put any unit vector in $H$ as $S(e_i)$ if $\partial(e_i)=0$. Then the map $S$ is not necessarily bounded on $L_2(M)$ and therefore we state the following assumption.

Assume that $S$ is a bounded map $L_2(M) \rightarrow H$. Further, we assume that $S^*S$ is a Fredholm operator on $L^2(M)$.

Next, for every $x,y \in \mathcal{A}$ we introduce a bounded linear map $$\label{Eqn=Txy}
T_{x,y}: L_2(M) \rightarrow H: \xi \mapsto x S(\xi) y - S(x \xi y).$$ Let $S = V \vert S \vert$ be the polar decomposition of $S$ and note that $1-V^*V$ is a finite rank projection. Denote by $K(L_2(M))$ the **compact operators**.

::: prop
[]{#Prop=Action label="Prop=Action"} Assume that $H$ is weakly contained in the coarse bimodule of $M$ as $\mathcal{A}$-$\mathcal{A}$ bimodules (namely, the assignment $x\otimes y^{\rm op} \in B(L_2(M)\otimes L_2(M))\mapsto xy^{\rm op}\in B(H)$ for $x,y\in \mathcal{A}$ extends to a bounded $\ast$-homomorphism). Suppose that Assumption 2 holds and that $T_{x,y}$ is compact for all $x,y \in \mathcal{A}$. Then there is a ucp map $$\theta: A \otimes_{{\rm min}}A^{{\rm op}} \rightarrow B(L_2(M)),$$ such that $\theta (a \otimes b^{{\rm op}})  - a b^{{\rm op}}$ is compact for all $a,b \in A$.
:::

::: proof
*Proof.* Observe that one can write $T_{x,y} = xy^{\rm op} S - S xy^{\rm op}$ for all $x,y\in \mathcal{A}$, where $x$ and $y^{\rm op}$ mean the corresponding left and right actions. Let $\Pi$ be the quotient map on $B(L_2(M))$ onto the Calkin algebra. Then by the assumption, for $x,y\in \mathcal{A}$, $$\begin{aligned}
    0=\Pi(S^*T_{x,y})
    =\ &\Pi(S^*xy^{\rm op}S)  - \Pi(S^*S x y^{\rm op})\\
    =\ &\Pi(|S|)\Pi(V^*xy^{\rm op}V)\Pi(|S|)  - \Pi(|S|^2)\Pi(xy^{\rm op}).
\end{aligned}$$ It holds that $$\label{Eqn=AO}
    \Pi(|S|^2)\Pi( xy^{\rm op})= \Pi(|S|)\Pi(V^*xy^{\rm op}V)\Pi(|S|).$$ By taking the adjoint of this equation and by exchanging $x,y$ by $x^*,y^*$, we get that $$\Pi(|S|^2)\Pi(xy^{\rm op}) = \Pi(xy^{\rm op})\Pi(|S|^2), \quad \text{for all } x,y\in \mathcal{A},$$ so that $\Pi(|S|)$ commutes with $\Pi(xy^{\rm op})$ for all $x,y\in \mathcal{A}$. Since $\Pi(|S|)$ is invertible by assumption, by applying $\Pi(|S|)^{-1}$ to [\[Eqn=AO\]](#Eqn=AO){reference-type="eqref" reference="Eqn=AO"} from left and right, we get $$\Pi( xy^{\rm op})= \Pi(V^*xy^{\rm op}V) , \quad \text{for all }x,y\in \mathcal{A}.$$ We conclude that $V^*xy^{\rm op}V-xy^{\rm op}$ is compact for all $x,y\in \mathcal{A}$.

Finally by the weak containment assumption, there is a bounded $\ast$-homomorphism $$\varphi\colon \mathcal{A}\otimes \mathcal{A}^{\rm op} \to \mathrm{C}^*\{xy^{\rm op} \in B(H)\mid x,y\in \mathcal{A}\}; \ \varphi(x\otimes y^{\rm op})=xy^{\rm op}.$$ Then if $P:=V^*V=1$, the composition ${\rm Ad}(V^*)\circ \varphi$ works as a desired ucp map $\theta$. For the general case, ${\rm Ad}(V^*)\circ \varphi$ is a ucp map into $P B(L_2(M))P$. Since $1-P$ is compact, by using a fixed state $\phi$ on $A\otimes_{\rm min}A^{\rm op}$, we can consider $\phi(\cdot)(1-P) + {\rm Ad}(V^*)\circ \varphi$ as a desired ucp map. ◻
:::

We now investigate sufficient conditions such that the assumptions of Proposition [\[Prop=Action\]](#Prop=Action){reference-type="ref" reference="Prop=Action"} are satisfied.
