---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-027-71-the-two-variable-colored-jones-invariant
section_title: "The two-variable colored Jones invariant"
section_number: 7.1
pages: 24-26
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.944
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:color-jones-polyn-2 label="sec:color-jones-polyn-2"}

Part of the following overlaps [@H:rims2001 Section 3.3], where some results are stated without proofs.

It follows from the results in the previous sections that we have $$J_K=J_T=\sum_{n\ge 0}J_K(P''_n)\sigma _n\in Z(\tUqv)
  \cong\varprojlim_{k}\modZ [q,q^{-1}][C^2]/(\sigma _k).$$ Thus $J_K$ may be regarded as an invariant with two variables $q$ and $C$. It is useful to introduce variables $t$ and $\alpha$ satisfying $$\alpha ^2=C^2-4=t+t^{-1}-2.$$ Then $Z(\tUqv)$ may be identified with $$\Lambda := \varprojlim_{k}\modZ [q,q^{-1}][t+t^{-1}]/(\sigma _k) \cong
  \varprojlim_{k}\modZ [q,q^{-1}][\alpha ^2]/(\sigma _k),$$ where $$\sigma _k
  =\prod_{i=1}^k(t+t^{-1}-q^i-q^{-i})
  =\prod_{i=1}^k(\alpha ^2-q^i-q^{-i}+2)$$

::: remark
[]{#r27 label="r27"} $\Lambda$ can be naturally regarded as a subring of $$\tilde\Lambda :=\varprojlim_{k}\modZ [q,q^{-1},t,t^{-1}]/(\sigma _k)
    \cong\varprojlim_k\modZ [q,q^{-1},t,t^{-1}]/
      \Bigl(\prod_{-k\le i\le k,\ i\neq0}(t-q^i)\Bigr).$$ In fact, $\Lambda$ consists of the elements of $\tilde\Lambda$ which are invariant under the involutive continuous ring automorphism of $\tilde\Lambda$ defined by $f(q,t)\mapsto f(q,t^{-1})$.
:::

By abuse of notation, we write $$J_K(t,q)=J_K\in \Lambda .$$

For $i\in \modZ$, let $$\theta _i\zzzcolon \modZ [q,q^{-1}][t+t^{-1}] \rightarrow  \modZ [q,q^{-1}]$$ be the unique $\modZ [q,q^{-1}]$-algebra homomorphism such that $\theta _i(t+t^{-1})=q^i+q^{-i}$. We have $$\label{e80}
  \theta _i(\sigma _k)=\prod_{j=1}^k(q^i+q^{-i}-q^j-q^{-j}).$$

If $i\neq0$, then $\theta _i$ induces a homomorphism $$\hat\theta _i\zzzcolon \Lambda  \rightarrow  \modZ [q,q^{-1}],$$ since it follows from [\[e80\]](#e80){reference-type="eqref" reference="e80"} that $\theta _i(\sigma _j)=0$ for all $j\ge |i|$. Since we have $\theta _i=\theta _{-i}$, it follows that $\hat\theta _i=\hat\theta _{-i}$. By [\[e89\]](#e89){reference-type="eqref" reference="e89"}, it follows that for $i>0$ $$\label{e51}
  \theta _i(J_K)=J_K(q^i,q) = J_K(\V'_{i-1}),$$ where $\V'_{i-1}=\V_{i-1}/[i]$. Thus $J_K(q^i,q)\in \modZ [q,q^{-1}]$ is the $(i-1)$st normalized colored Jones polynomial. Hence, it may be natural to call $J_K(t,q)\in \Lambda$ the *two-variable colored Jones invariant* of $K$. For the comparison with the well-known, two-variable power series expansion of the colored Jones polynomials, known as the Melvin-Morton expansion, see Section [\[sec:melv-mort-expans\]](#sec:melv-mort-expans){reference-type="ref" reference="sec:melv-mort-expans"} below.

Now, consider the case $i=0$. $\theta _0$ induces a continuous ring homomorphism $$\hat\theta _0\zzzcolon \Lambda  \rightarrow  \Zqh, \quad f(t,q)\mapsto f(1,q),$$ since it follows from [\[e80\]](#e80){reference-type="eqref" reference="e80"} that $\theta _0(\sigma _k)=(-1)^k(\{k\}!^2)\in \modZ [q,q^{-1}]$ is divisible by ${(q)_k}^2$. For $\zeta \in \calZ$ with $r=\ord(\zeta )$, by [\[e51\]](#e51){reference-type="eqref" reference="e51"}, we have $$\mods _\zeta (J_K(1,q))=J_K(1,\zeta )=J_K(\zeta ^r,\zeta )=\mods _\zeta (J_K(q^r,q))
  =\mods _\zeta (J_K(\V'_{r-1})).$$ The right-hand side is known as the *Kashaev invariant* of $K$ at $\zeta$ [@Kashaev; @Murakami-Murakami]. Hence, $J_K(1,q)\in \Zqh$ may be regarded as a *unified Kashaev invariant*. Essentially the same observation has been made in [@H:rims2001 Section 3.3] (without proof). Using a different method, Huynh and Le [@Huynh-Le] have given a proof of the existence of the unified Kashaev invariant in the above sense.
