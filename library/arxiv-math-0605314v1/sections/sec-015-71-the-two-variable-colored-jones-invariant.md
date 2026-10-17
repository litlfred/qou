---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-015-71-the-two-variable-colored-jones-invariant
section_title: "The two-variable colored Jones invariant"
section_number: 7.1
pages: 24-28
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.965
doc_brief: "arXiv:math/0605314v1 [math.GT] 11 May 2006 — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring Z[q] such that the evaluation at"
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
  \theta _i(J_K)=J_K(q^i,q) = J_K(\V'_{i-1}),$$ where $\V'_{i-1}=\V_{i-1}/[i]$. Thus $J_K(q^i,q)\in \modZ [q,q^{-1}]$ is the $(i-1)$st normalized colored Jones polynomial. Hence, it may be natural to call $J_K(t,q)\in \Lambda$ the *two-variable colored Jones invariant* of $K$. For the comparison with the well-known, two-variable power series expansion of the colored Jones polynomials, known as the Melvin-Morton expansion, see Section [0.1](#sec:melv-mort-expans){reference-type="ref" reference="sec:melv-mort-expans"} below.

Now, consider the case $i=0$. $\theta _0$ induces a continuous ring homomorphism $$\hat\theta _0\zzzcolon \Lambda  \rightarrow  \Zqh, \quad f(t,q)\mapsto f(1,q),$$ since it follows from [\[e80\]](#e80){reference-type="eqref" reference="e80"} that $\theta _0(\sigma _k)=(-1)^k(\{k\}!^2)\in \modZ [q,q^{-1}]$ is divisible by ${(q)_k}^2$. For $\zeta \in \calZ$ with $r=\ord(\zeta )$, by [\[e51\]](#e51){reference-type="eqref" reference="e51"}, we have $$\mods _\zeta (J_K(1,q))=J_K(1,\zeta )=J_K(\zeta ^r,\zeta )=\mods _\zeta (J_K(q^r,q))
  =\mods _\zeta (J_K(\V'_{r-1})).$$ The right-hand side is known as the *Kashaev invariant* of $K$ at $\zeta$ [@Kashaev; @Murakami-Murakami]. Hence, $J_K(1,q)\in \Zqh$ may be regarded as a *unified Kashaev invariant*. Essentially the same observation has been made in [@H:rims2001 Section 3.3] (without proof). Using a different method, Huynh and Le [@Huynh-Le] have given a proof of the existence of the unified Kashaev invariant in the above sense.

## Melvin-Morton expansions and Rozansky's rationality theorem {#sec:melv-mort-expans}

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
