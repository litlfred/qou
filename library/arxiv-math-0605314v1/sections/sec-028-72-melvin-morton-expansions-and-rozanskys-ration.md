---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-028-72-melvin-morton-expansions-and-rozanskys-ration
section_title: "Melvin-Morton expansions and Rozansky's rationality theorem"
section_number: 7.2
pages: 26-28
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.946
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:melv-mort-expans label="sec:melv-mort-expans"}

Rozansky [@Rozansky3] proved that the colored Jones polynomials of a knot $K$ can be repackaged into one invariant $J^\MMR_K\in \modZ [[q-1,\alpha ^2]]$, which is an integer-coefficient version of the Melvin-Morton expansion [@Melvin-Morton]. (In fact, Rozansky proved much stronger results there, see below.)

Let $$\gamma \zzzcolon \Lambda \rightarrow \modZ [[q-1,\alpha ^2]]$$ be the ring homomorphism induced by $\id_{\modZ [q,q^{-1},\alpha ^2]}$. This is well-defined since $\sigma _{2k}\in (\alpha ^{2k},(q-1)^{2k})$ in $\modZ [q,q^{-1},\alpha ^2]$ for $k\ge 0$. As mentioned in [@H:rims2001 Section 3.3], $\gamma (J_K)\in \modZ [[q-1,\alpha ^2]]$ is equal to the Rozansky's integral version of the Melvin-Morton expansion.

The first half of the following proposition was mentioned in [@H:rims2001] without proof, and implies that $J_K$ and $J^\MMR_K$ have the same strength.

::: proposition
[]{#r72 label="r72"} The map $\gamma$ is injective and non-surjective.
:::

::: proof
*Proof.* Let us prove injectivity. Let $f=\sum_{n=0}^\infty f_n(q)\sigma _n\in \Lambda$, where $f_n(q)\in \modZ [q,q^{-1}]$ for $n\ge 0$, and suppose that $\gamma (f)=0$. We can express each $\sigma _n$ as $$\sigma _n= \sum_{k=0}^n g_{n,k}(q)(2-q-q^{-1})^{2n-2k}\alpha ^{2k},$$ where $g_{n,k}(q)\in \modZ [q,q^{-1}]$. Hence, we obtain $$\gamma (f)=\sum_{k=0}^\infty 
    \Bigl(\sum_{n=k}^\infty f_n(q)g_{n,k}(q)(2-q-q^{-1})^{2n-2k}\Bigr)\alpha ^{2k}.$$ Since $\gamma (f)=0$, we have $$\label{e82}
    \sum_{n=k}^\infty f_n(q)g_{n,k}(q)(2-q-q^{-1})^{2n-2k}=0$$ for all $k\ge 0$.

One can show that $g_{n,k}(q)$ is not divisible by $q-1$. (Indeed, one can use induction on $n$ to show that $g_{n,k}(1)\in \modZ$ is positive.) Using this fact and [\[e82\]](#e82){reference-type="eqref" reference="e82"}, one can prove using induction that for any $n,d\ge 0$, $f_n(q)$ is divisible by $(q-1)^d$. Hence $f_n(q)=0$ for all $n$.

Non-surjectivity of $\gamma$ can be verified in several ways. For example, let $u\zzzcolon \modZ [[q-1,\alpha ^2]]\rightarrow \modZ [[q-1]]$ be the continuous $\modZ [[q-1]]$-algebra homomorphism such that $u(\alpha ^2)=0$. Then we have $$u\gamma (\Lambda )=\modZ [q,q^{-1}]\subsetneq\modZ [[q-1]]=u(\modZ [[q-1,\alpha ^2]]).$$ It follows that $\gamma$ is not surjective. ◻
:::

Rozansky [@Rozansky3] also proved that the coefficient of $(q-1)^n$ of the integral Melvin-Morton expansion of a knot $K$ is a rational function in $\alpha ^2$ with denominator a power of the Alexander polynomial $\Delta _K(t)\in \modZ [t+t^{-1}]$ of $K$. (This result generalizes a conjecture of Melvin and Morton [@Melvin-Morton], proved in [@Bar-Natan-Garoufalidis].) More precisely, Rozansky proved that $J^\MMR_K$ has the following power series expansion $$J_K^\MMR = \sum_{n\ge 0}\frac{P_{K,n}(t)}{\Delta _K(t)^{2n+1}}(q-1)^n
  \in \modZ [t+t^{-1},\frac{1}{\Delta _K(t)}][[q-1]],$$ where $P_{K,n}(t)\in \modZ [t+t^{-1}]$ for $n\ge 0$. The $P_{K,n}(t)$ are uniquely determined by $K$ and $n$. Thus $\gamma (J_K)$ is contained in a much smaller ring than $\modZ [[q-1,\alpha ^2]]$. Melvin and Morton's conjecture (essentially) states that $$J_K^\MMR\bigl|_{q=1}=\frac{1}{\Delta _K(t)}.$$ Thus we have $P_{K,0}(t)=1$.

The following conjecture (supported by some computer calculations) generalizes Rozansky's rationality theorem.

::: conjecture
[]{#r44 label="r44"} Let $K$ be a knot and let $d\zzzcolon \modN \rightarrow \{0,1,2,\ldots \}$ be a function which vanishes for all but finitely many elements of $\modN$. Set $$\Delta ^d_K(t) = \prod_{r\in \modN ,d(r)>0}\Delta _K(t^r)^{2d(r)-1}\in \modZ [t+t^{-1}].$$ Then we have $$\Delta ^d_K(t)J_K \in \modZ [t+t^{-1},q,q^{-1}] + \Phi _d(q)\Lambda .$$
:::

Conjecture [\[r44\]](#r44){reference-type="ref" reference="r44"} implies that $J_K^\MMR$ is contained in the image of the natural (injective) homomorphism $$\varprojlim_k \modZ [q,q^{-1},t+t^{-1},\frac{1}{\Delta _K(t^i)}\quad  (i\ge 1)]/((q)_k)
    \rightarrow \modZ [[q-1,\alpha ^2]].$$

Conjecture [\[r44\]](#r44){reference-type="ref" reference="r44"} also implies the following conjecture, in which the case $\zeta =1$ is Rozansky's rationality theorem.

::: conjecture
[]{#r58 label="r58"} Let $\zeta \in \calZ$ with $r=\ord(\zeta )$. Let $$\gamma _\zeta \zzzcolon \Lambda \rightarrow \modZ [\zeta ][[\alpha ^2,q-\zeta ]]$$ be the homomorphism induced by $\modZ [q,q^{-1},\alpha ^2]\subset \modZ [\zeta ][q,q^{-1},\alpha ^2]$. Define $P_{K,\zeta ,k}(t)\in \modZ [\zeta ][[\alpha ^2]]$ for $k\ge 0$ by $$\gamma _\zeta (J_K)=\sum_{k\ge 0}\frac{P_{K,\zeta ,k}(t)}{\Delta _K(t^r)^{2k+1}}(q-\zeta )^k.$$ Then we have $P_{K,\zeta ,k}(t)\in \modZ [\zeta ][t+t^{-1}]$.
:::

Using the injectivity of $\gamma =\gamma _1$, one can prove that the homomorphism $\gamma _\zeta$ is injective.

Conjecture [\[r58\]](#r58){reference-type="ref" reference="r58"} implies that $$J_K(t,\zeta )=\frac{P_{K,\zeta ,0}(t)}{\Delta _K(t^r)}
  \in \frac{1}{\Delta _K(t^r)}\modZ [\zeta ][t+t^{-1}].$$

Some computer calculations support the following conjecture.

::: conjecture
[]{#r64 label="r64"} We have $$J_K(t,-1)=\frac{\Delta _K(-t)}{\Delta _K(t^2)}.$$ Thus we have $P_{K,-1,0}(t)=\Delta _K(-t)$ in the notation of Conjecture [\[r58\]](#r58){reference-type="ref" reference="r58"}.
:::

Presumably, $P_{K,\zeta _r,0}(t)$ with $\zeta _r=\exp\frac{2\pi \sqrt{-1}}{r}$ is the $r$th Akutsu-Deguchi-Ohtsuki invariant [@Akutsu-Deguchi-Ohtsuki], after suitable change of variables. (Recall that the second Akutsu-Deguchi-Ohtsuki invariant of a knot is the Alexander polynomial [@MurakamiJ].) If this is true, then it follows that the Akutsu-Deguchi-Ohtsuki invariants of a knot $K$ determine $J_K$, hence also the colored Jones polynomials $J_K(\V_m)$, $m\ge 0$.
