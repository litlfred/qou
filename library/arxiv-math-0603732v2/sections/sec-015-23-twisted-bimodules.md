---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-015-23-twisted-bimodules
section_title: "Twisted (bi)modules"
section_number: 2.3
pages: 6-8
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.934
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.3 label="xxsec2.3"}

We extend slightly a standard notation for twisted one-sided modules, as follows. Let $A$ be an algebra and let $M$ be an $A$-bimodule. For every pair of algebra automorphisms $\sigma, \tau$ of $A$, we write $^\sigma M^\tau$ for the $A$-bimodule defined by $$a\cdot m\cdot b\; =\; \sigma(a)m\tau(b)$$ for all $a,b\in A$ and all $m\in M$. When one or the other of $\sigma, \tau$ is the identity map we shall simply omit it, writing for example $^\sigma M$ for $^\sigma M^1.$ If $\phi$ is another automorphism of $A$, then the map $x\mapsto \phi(x)$ for all $x\in A$ defines an isomorphism of $A$-bimodules ${^\sigma
A^\tau}\to {^{\phi\sigma}A^{\phi\tau}}$. In particular, $$\begin{aligned}
{^\sigma A^\tau}\; \cong
\; {A^{\sigma^{-1}\tau}} \; \cong \; {^{\tau^{-1}\sigma}A}
\end{aligned}$$ as $A$-bimodules. If $\tau$ is an inner automorphism of $A$, given by conjugation $x \mapsto uxu^{-1}$ by the unit $u$ of $A$, then the map on $A$ given by left multiplication by $u$ shows that $$\begin{aligned}
^{\sigma}A^{\beta} \; \cong \; {^{\tau
\sigma}A^{\beta}} \; \cong \; {^{\sigma} A^{\beta\tau}}
\end{aligned}$$ for all automorphisms $\sigma$ and $\beta$ of $A.$

Let $M$ be an $A$-bimodule. Define $$Z_M (A)\; := \;\{a \in A: am = ma \quad \forall \; m \in M \}.$$ Then $Z_M(A)$ is a subalgebra of $A$. For any algebra automorphism $\sigma$, write $$Z^{\sigma}_A(M)\; =\; \{m\in M\;|\; am=m\sigma(a) \quad
\forall \; a\in A\},$$ so $Z^\sigma (M)$ is a $Z_M(A)$-submodule of $M$. When $M = A$, $Z^\sigma (M)$ is the space of $\sigma^{-1}$-*normal* elements of $A$. We write $Z(M)$ for $Z^{\operatorname{id}_A}(M)$; of course $Z(A)=Z_A(A)$ is just the centre of $A$, and $Z^\sigma (A)$ is a $Z(A)$-module. We shall denote by $N(A)$ the multiplicative subsemigroup of $\mathop{\mathrm{Aut}}_{k{\text{-}}\mathrm{alg}}(A)$ consisting of those automorphisms $\sigma$ such that $A$ contains a $\sigma$-normal element which is not a zero divisor.

::: lemma
Let $A$ be an algebra and let $M$ be an $A$-bimodule.

1.  Under the canonical identification of $M$ with $M^{\sigma}$ as $k$-vector spaces, $$Z^{\sigma}_A(M)\; =\; Z(M^\sigma).$$

2.  Let $\sigma$ and $\tau$ be algebra automorphisms of $A$. Then $\tau$ carries $Z(A^{\sigma\tau})$ to $Z(A^{\tau\sigma})$.

3.  Suppose that $A$ is a Hopf algebra. If $\sigma$ is a Hopf algebra automorphism of $A$, then $^\sigma(L(M))\cong L(^\sigma
    M^\sigma)$. In particular, $$^\sigma(L(^\tau A))\cong L(^{\sigma \tau}A^\sigma)\cong L(^\tau A).$$
:::

::: proof
*Proof.* (a) is simply the definition.

\(b\) By (a) we may regard $Z(A^{\sigma\tau})$ and $Z(A^{\tau\sigma})$ as subsets of $A$. For every $x\in
Z(A^{\sigma\tau})$, $ax=x\sigma\tau(a)$ for all $a\in A$. Then, for all $a\in A$, $$a \tau(x)\; =\; \tau(\tau^{-1}(a)x)\; =\;
\tau(x\sigma\tau\tau^{-1}(a))\;=\;
\tau(x)\tau\sigma(a).$$ This means that $\tau: Z(A^{\sigma\tau})\longrightarrow
Z(A^{\tau\sigma})$ is an isomorphism.

\(c\) The second assertion is a special case of the first, so we consider the first one only. Let $\ast$, $\cdot$ and $\bullet$ be the left action of $A$ on $^\sigma(L(M))$, $L(M)$ and $L(^\sigma M^\sigma)$ respectively. For every $a\in A$ and $m\in M$, $$a\ast m=\sigma(a) \cdot m=\sum \sigma(a)_1
mS(\sigma(a)_2)=:(*).$$ Let $\cdot_\sigma$ be the action of $A$ on $^\sigma M^\sigma$. Since $\sigma$ commutes with product, coproduct and antipode, then we continue $$(*)=\sum \sigma(a_1)
m\sigma(S(a_2))=\sum a_1\cdot_\sigma m\cdot_\sigma
S(a_2)=a\bullet m.$$ ◻
:::
