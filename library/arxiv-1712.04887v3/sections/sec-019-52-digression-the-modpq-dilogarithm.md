---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-019-52-digression-the-modpq-dilogarithm
section_title: "Digression: the modpq dilogarithm"
section_number: 5.2
pages: 28-28
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 1.0
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#modpqdilog label="modpqdilog"}

Let $q$ be prime, and $q + 1 \equiv 0 \;\text{\rm mod}\;n$ with $n$ a power of $p$ as before. For convenience of exposition, assume that $p > 3$ so that $D_{\zeta}(1)$ is a perfect $n$th power. Fix an $n$th root of unity $\zeta$ in $\mathbf F_{q^2}$. Then there is a trivialization $\log_{\zeta}: \mathbf F^{\times}_{q^2} \otimes \mathbf Z/n\mathbf Z\simeq \mathbf Z/n\mathbf Z$ sending $\zeta$ to $1$. The isomorphism $B(\mathbf F_q) \otimes \mathbf Z_p
\simeq \mathbf Z/n\mathbf Z$ of Theorem [\[theorem:modpq\]](#theorem:modpq){reference-type="ref" reference="theorem:modpq"} now gives a curious function, the *$p$-$q$ dilogarithm*, which is a function $$L: \,\mathbf F_q \,\rightarrow\, \mathbf F^{\times}_{q^2} \otimes 
\mathbf Z/n\mathbf Z\, \overset{\log_{\zeta}}\rightarrow \, \mathbf Z/n\mathbf Z$$ satisfying the $5$-term relation. What is perhaps surprising is that the quantum *logarithm* suffices to give an explicit formula, as follows.

::: proposition
The function $L$ is given by the formula $$L(a) \;=\;  \sum_{b^{n}=a}\log_\zeta(b)\log_\zeta(1-b) \qquad(a\in\mathbf F_q^\times),$$ where the sum is over the $n$th roots $b$ of $a$ in $\mathbf F_{q^2}^\times$.
:::

::: proof
*Proof.* Since $\mathbf F^{\times}_q$ has order prime to $n$, the element $a$ has a unique $n$th power $c \in \mathbf F^{\times}_q$. Then [\[16\*\]](#16*){reference-type="eqref" reference="16*"} can be rewritten as $L(a) \;=\; \ \sum_{k \;\text{\rm mod}\;n} k \log_{\zeta}(1 - \zeta^k c)$. (Note that $R_\zeta=P_\zeta$ for finite fields, and the assumption that $p > 3$ means that we can ignore the $D_{\zeta}(1)$ factor.) The elements $b = \zeta^k c$ are the $n$th roots of $a$ in $\mathbf F_{q^2}^\times$, and $\log_{\zeta}(b) = k$ because $c$ has order prime to $n$ and thus $\log_{\zeta}(c) = 0$. ◻
:::
