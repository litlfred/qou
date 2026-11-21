---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-067-161-the-wrt-invariants-as-limiting-values-of-hol
section_title: "The WRT invariants as limiting values of holomorphic functions"
section_number: 16.1
pages: 61-62
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.983
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:wrt-invariants-as label="sec:wrt-invariants-as"} As explained in the introduction, the invariant $J_M$ for an integral homology sphere $M$ unifies the WRT invariants $\tau _\zeta (M)$ for all the roots of unity in an algebraic way. It should be remarked that there is another *analytic* approach to "unify" the WRT invariants by realizing the radial limiting values of a holomorphic function defined on the unit disk $\{z\in \C;\;|z|<1\}$, studied in [@Lawrence:integrality; @Lawrence:holomorphic; @Lawrence-Rozansky; @Lawrence-Zagier; @Hikami1; @Hikami3; @Hikami4; @Hikami5].

Unfortunately, the invariant $J_M\in \Zqh$ does not immediately determine such a holomorphic function, i.e., there is no natural homomorphism from the ring $\Zqh$ to the ring of holomorphic function on $|q|<1$. However, some expressions for $J_M$ may define well-defined holomorphic functions for on $|q|<1$ as we explain below for the Poincaré homology sphere $\Sigma (2,3,5)$.

We have $$\label{e11}
  J_{\Sigma (2,3,5)}
  =\sum_{n\ge 0}q^n\frac{(1-q^{n+1})(1-q^{n+2})\cdots(1-q^{2n+1})}{1-q}\in \Zqh.$$ The modified WRT invariant $W(\zeta )=\zeta (\zeta -1)\tau _\zeta (\Sigma (2,3,5))$, $\zeta \in \calZ$, defined by Lawrence and Zagier [@Lawrence-Zagier], is unified into $$W(q)=q(q-1)J_{\Sigma (2,3,5)}\in \Zqh.$$ For our purpose, it is useful to modify it further as $$\label{e7}
  \begin{split}
    B(q)&=1-W(q) = 1+q(1-q)J_{\Sigma (2,3,5)}\\
    &=\sum_{n\ge 0}q^n(q^n;q)_n,
  \end{split}$$ where $(q^n;q)_n=(1-q^n)(1-q^{n+1})\cdots (1-q^{2n-1})$. A beautiful observation by Lawrence and Zagier [@Lawrence-Zagier] is that the series $$A(q)=\sum_{n\ge 1}\chi _+(n)q^{\frac{n^2-1}{120}}=1+q+q^3+q^7-q^8-\dots \in \modZ [[q]],$$ which converges on $|q|<1$, converges radially at each root of unity $\zeta$ to $2(1-W(\zeta ))=2B(\zeta )$. They also showed that the radial asymptotic expansion of $A(q)$ at $q=1$ gives $2$ times the Ohtsuki series $\tau ^O(M)$.

Note that the formula [\[e7\]](#e7){reference-type="eqref" reference="e7"} for $B(q)$ can also define a power series in $q$. (Actually, [\[e7\]](#e7){reference-type="eqref" reference="e7"} defines an element of $\varprojlim_{n}\modZ [q]/(q^n(q)_n)\cong\Zqh\times \modZ [[q]]$.) Let $B(q)_{\modZ [[q]]}\in \modZ [[q]]$ denote this element. Hikami [@Hikami4] proved $$A(q)=B(q)_{\modZ [[q]]}\in \modZ [[q]].$$ Thus, there are two ways to obtain the value of the (modified) WRT invariants from $B(q)$. One is just to evaluate at roots of unity, and the other is to expand it in $q$, take the radial limit at roots of unity and then multiply by $\half$. The meaning of the factor $\half$ is not clear to the author. It would be natural to expect that the radial asymptotic expansion at each root of unity $\zeta$ is $2$ times the power series $\iota _\zeta (B(q))\in \modZ [\zeta ][[q-\zeta ]]$.

It would be natural to expect that certain formulas [\[e11\]](#e11){reference-type="eqref" reference="e11"} for $J_M$ of integral homology spheres $M$ may give a power series in $q$ whose radial asymptotic behavior at a root of unity $\zeta$ is closely related to the "algebraic behavior near $\zeta$" obtained by the map $\iota _\zeta \zzzcolon \Zqh\rightarrow \modZ [\zeta ][[q-\zeta ]]$. For example, for an integral homology sphere $M_{i,j,k}$ with $i,j,k>0$ defined in Section [\[sec:surg-borr-rings\]](#sec:surg-borr-rings){reference-type="ref" reference="sec:surg-borr-rings"}, the formula [\[e20\]](#e20){reference-type="ref" reference="e20"} of $J_{M_{i,j,k}}$ defines an element of $\modZ [[q]]$ which converges on $|q|<1$. Note that the Poincaré homology sphere $\Sigma (2,3,5)$ is the special case $M_{1,1,1}$.
