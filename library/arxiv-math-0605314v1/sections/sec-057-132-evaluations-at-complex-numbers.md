---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-057-132-evaluations-at-complex-numbers
section_title: "Evaluations at complex numbers"
section_number: 13.2
pages: 48-53
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.969
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:expans-at-compl label="sec:expans-at-compl"}

Let $\alpha \in \C$. Then $\mods _\alpha \zzzcolon \modZ [q]\rightarrow \modZ [\alpha ]$ induces $$\hat{\mods }_\alpha \zzzcolon \Zqh\rightarrow \Za=\varprojlim_{n} \modZ [\alpha ]/((\alpha )_n).$$ Thus, one can formally evaluate $J_M$ at any complex number. We can easily verify the following.

1.  If $\alpha =0$, then $\Zx0=0$.

2.  If $\alpha$ is transcendental, then $\hat{\mods }_\alpha \zzzcolon \Zqh\congto\Za$.

3.  If $\alpha \in \calZ$, then $\Za\cong\modZ [\alpha ]$.

The case $\alpha \in \modQ$ is of special interest.

::: proposition
[]{#r12 label="r12"} If $a/b\in \modQ \setminus \{\pm 1\}$ with $a,b\in \modZ ,(a,b)=1$, then we have $$\label{e58}
    \Zx{a/b}
    \cong \varprojlim_{m\in \modN ,(m,ab)=1}\modZ /m\modZ 
    \cong \prod_{p\in P_{ab}}\modZ _p,$$ where, for $n\in \modN$, $P_n$ denote the set of primes $p$ coprime with $n$.
:::

::: proof
*Proof.* We have $$\begin{split}
      \Zx{a/b}
      =\varprojlim_{n}\modZ [1/b]/((a/b)_n)
      \cong\varprojlim_{n}\modZ [1/b]/((b,a)_n),
    \end{split}$$ where we set $$(b,a)_n = b^{\hf n(n+1)}(a/b)_n =(b-a)(b^2-a^2)\cdots(b^n-a^n)\in \modZ .$$ The families of ideals in $\modZ [1/b]$, $X:=\{((b,a)_n)\}_{n\ge 0}$ and $Y:=\{(m)\}_{m\in \modN ,(m,ab)=1}$, are cofinal with each other. (Indeed, $a/b\neq1$ implies $X\subset Y$. Conversely, for $m\in Y$, we have $b^n-a^n\equiv0\mod m$, where $n\ge 1$ is the least common multiple of the orders of $b$ and $a$ in $(\modZ /m\modZ )^\times$. Then $(b,a)_n$ is divisible by $m$.) Therefore, $$\begin{split}
      \Zx{a/b}
      \cong \varprojlim_{m\in \modN ,(m,ab)=1}\modZ [1/b]/(m)
      \cong \varprojlim_{m\in \modN ,(m,ab)=1}\modZ /m\modZ .
    \end{split}$$ Here the latter isomorphism follows from invertibility of $b$ in $\modZ /m\modZ$ for each $m$. The latter isomorphism in [\[e58\]](#e58){reference-type="eqref" reference="e58"} is standard. ◻
:::

By Proposition [\[r12\]](#r12){reference-type="ref" reference="r12"}, we may regard $\mods _{a/b}(J_M)$ as an element in $\prod_{p\in P_{ab}}\modZ _p$. Hence, for each $p\in P_{a,b}$, we can extract a $\modZ _p$-valued function $$\label{e60}
  \tau ^p(M)\zzzcolon U_p(\modQ )\rightarrow \modZ _p,$$ where $U_p(\modQ )$ is the set of $a/b\in \modQ$ with $a,b\in \modZ$, $(a,b)=1$, such that $p$ is coprime with $ab$.

Note that $U_p(\modQ )=\modQ \cap U(\modZ _p)$, where $U(\modZ _p)$ is the group of units in the ring $\modZ _p$. We extend the domain of $\tau ^p(M)$ in the next subsection.

## The $p$-adic WRT functions {#sec:p-adic-wrt}

In this subsection, we show that the WRT function of an integral homology sphere can be extended to a $p$-adic analytic function on the unit circle in the field $\C_p$ of complex $p$-adic numbers.

The field $\C_p$ is defined as follows (see [@Koblitz; @Gouvea] for details). Let $\modQ _p$ be the field of $p$-adic numbers, and let $|\cdot|_p\zzzcolon \modQ _p\rightarrow \R$ be the $p$-adic norm, defined by $$|x|_p=\begin{cases}
  p^{-\ord_p(x)} \quad &\text{if $x\neq0$},\\
  0 &\text{if $x=0$},
  \end{cases}$$ where $\ord_p(x)\in \modZ$ is the $p$-adic ordinal. Let $\bar\modQ _p$ denote the algebraic closure of $\modQ _p$. It is well known that the norm $|\cdot|_p$ on $\modQ _p$ uniquely extends to $\bar\modQ _p$. Then $\C_p$ is defined to be the completion of $\bar\modQ _p$ with respect to the norm $|\cdot|_p$. The norm on $\C_p$ induced by $|\cdot|_p$ on $\bar\modQ _p$ is denoted again by $|\cdot|_p$. It is well known that $\C_p$ is algebraically closed.

Let $\modO _p$ and $\modP _p$ denote the valuation ring and the valuation ideal, respectively, of $\C_p$, i.e., $$\begin{gathered}
  \modO _p=\{x\in \C_p\zzzcolon |x|_p\le 1\},\quad \modP _p=\{x\in \C_p\zzzcolon |x|_p<1\}.
\end{gathered}$$ Let $$U(\modO _p)=\modO _p\setminus \modP _p=\{x\in \C_p\zzzcolon |x|_p=1\}$$ denote the unit circle of $\modO _p$, which consists of the multiplicative units in $\modO _p$. In particular, all the roots of unity in $\C_p$ are contained in $U(\modO _p)$. We may assume that the set $\calZ(\subset \bar\modQ \subset \C)$ of complex roots of unity as a subset of $U(\modO _p)$ (by choosing a field homomorphism $\bar\modQ \hookrightarrow\bar\modQ _p(\subset \C_p$)).

::: lemma
[]{#r46 label="r46"} For each $x\in U(\modO _p)$, the sequence $(x)_n$, $n\ge 0$, of elements in $\modO _p$ is converging to $0$ in $\modO _p$.
:::

::: proof
*Proof.* Since $x\in U(\modO _p)$, there is $\zeta \in \calZ$ such that $x-\zeta \in \modP _p$. Set $r=\ord(\zeta )$. Then $$\begin{split}
    1-x^r &= 1-(\zeta +(x-\zeta ))^r\\
    &=1-\sum_{i=0}^r\binom{r}{i}\zeta ^{r-i}(x-\zeta )^i\\
    &=-\sum_{i=1}^r\binom{r}{i}\zeta ^{r-i}(x-\zeta )^i\in \modP _p.
    \end{split}$$ Since $(x)_{rk}$ is divisible by $(1-x^r)^k$ for each $k\ge 0$, it follows that $(x)_n$ converges to $0$ as $n\rightarrow \infty$. ◻
:::

Lemma [\[r46\]](#r46){reference-type="ref" reference="r46"} implies that for $x\in U(\modO _p)$, the ring homomorphism $\modZ [q]\rightarrow \modO _p$, $f(q)\mapsto f(x)$, induces a continuous ring homomorphism $$\mods _x\zzzcolon \Zqh \rightarrow  \modO _p, \quad f(q)\mapsto f(x).$$ Gathering the $\mods _x$ for all $x\in U(\modO _p)$, we obtain a ring homomorphism $$\mods _{U(\modO _p)}\zzzcolon \Zqh \rightarrow  \Fun(U(\modO _p),\modO _p)$$ such that $\mods _{U(\modO _p)}(f)(x)=\mods _x(f(q))$. For $f\in \Zqh$, the function $$\label{e79}
  \hat{f}=\mods _{U(\modO _p)}(f)\zzzcolon U(\modO _p)\rightarrow \modO _p$$ is $p$-adic analytic of radius of convergence $\ge 1$ everywhere in $U(\modO _p)$. I.e., $\hat{f}$ has a converging power series expansion at any point $x\in U(\modO _p)$ which coincides $\hat{f}$ for all $y\in U(\modO _p)$ with $|y-x|_p<1$.

It is easy to see that the restriction of $\hat{f}$ to $$U(\modZ _p)=\{x\in \modZ _p\zzzcolon |x|_p=1\}=U(\modO _p)\cap \modQ _p$$ takes values in $\modZ _p$.

For any subset $V\subset U(\modO _p)$, $\mods _{U(\modO _p)}$ induces a ring homomorphism $$\mods _V\zzzcolon \Zqh \rightarrow  \Fun(V,\modO _p).$$

::: proposition
[]{#r54 label="r54"} Let $V\subset U(\modO _p)$ be an infinite subset. Suppose that there is a point $x\in U(\modO _p)$ and a sequence $x_i\in V\setminus x$, $i=0,1,\ldots$, such that $\lim_{i\rightarrow \infty }x_i=x$ with respect to the $p$-adic topology. Then $\mods _V$ is injective.
:::

::: proof
*Proof.* Suppose $\mods _V(f)=0$, $f\in \Zqh$. Define $\hat{f}$ as in [\[e79\]](#e79){reference-type="eqref" reference="e79"}. Set $D(x,1)=\{y\in \modO _p\zzzcolon |y-x|_p<1\}$. The restriction $\hat{f}_x=\hat
  f|_{D(x,1)}\zzzcolon D(x,1)\rightarrow \modO _p$ can be expressed as a power series at $q=x$, convergent on $D(x,1)$. The assumption implies that $\hat
  f_x=0$, i.e., $\hat{f}(x)=0$ for all $x\in D(x,1)$.

Since $x\in U(\modO _p)$, we have $D(x,1)\cap \calZ\neq\emptyset$. Moreover, if $\zeta \in D(x,1)\cap \calZ$ and $\xi \in \calZ$ with $\ord(\xi )$ a power of $p$, then $\zeta \xi \in D(x,1)\cap \calZ$. Since for each $\zeta \in D(x,1)\cap \calZ$ we have $f(\zeta )=\hat{f}(\zeta )=0$, it follows from Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"} that $f=0$. ◻
:::

Now we give applications of the above-mentioned facts to the WRT invariants. For each integral homology sphere $M$, define the *$p$-adic WRT function* of $M$ by $$\label{e77}
  \tau ^p(M)=\mods _{U(\modO _p)}(J_M)\zzzcolon U(\modO _p)\rightarrow \modO _p,$$ which is $p$-adic analytic of radius of convergence $\ge 1$ everywhere in $U(\modO _p)$. $\tau ^p(M)$ restricts to $$\tau ^p(M)\zzzcolon U(\modZ _p)\rightarrow \modZ _p.$$ Note that these invariants generalize the one given in [\[e60\]](#e60){reference-type="eqref" reference="e60"}.

If $V$ is as in Proposition [\[r54\]](#r54){reference-type="ref" reference="r54"}, then $J_M$ is determined by the restriction of $\tau ^p(M)$ to $V$. In particular, for $V=U(\modO _p)$, $J_M$ (hence $\tau (M)$) is determined by $\tau ^p(M)\zzzcolon U(\modO _p)\rightarrow \modO _p$ and also by its restriction to $U(\modZ _p)$.

The following generalizes Conjecture [\[r73\]](#r73){reference-type="ref" reference="r73"}.

::: conjecture
[]{#r33 label="r33"} For any integral homology sphere $M$, for any prime $p$, $\tau ^p(M)\zzzcolon U(\modO _p)\rightarrow \modO _p$ is nowhere zero.
:::

If Conjecture [\[r33\]](#r33){reference-type="ref" reference="r33"} is true for at least one prime $p$, then Conjecture [\[r73\]](#r73){reference-type="ref" reference="r73"} is true.

As a partial result of Conjecture [\[r33\]](#r33){reference-type="ref" reference="r33"}, we have the following result, closely related to Corollary [\[r71\]](#r71){reference-type="ref" reference="r71"}.

::: proposition
[]{#r50 label="r50"} If $\zeta \in \calZ\subset U(\modO _p)$ is a root of unity of order $1$, $2$, $3$, $4$ or $6$, then $\tau ^p(M)$ has no zero on $D(\zeta ,1)=\{x\in U(\modO _p)\zzzcolon |x-\zeta |_p<1\}$.
:::

::: proof
*Proof.* The assertion follows from $\tau _\zeta (M)=\pm 1$ and the fact that the power series expansion of $\tau ^p(M)$ at $q=\zeta$ has coefficients in $\modO _p$. ◻
:::

::: remark
[]{#r53 label="r53"} By Corollary [\[r71\]](#r71){reference-type="ref" reference="r71"}, $\tau ^p(M)$ is non-vanishing at $q=\zeta \xi$, where $\xi \in \calZ$ is of any prime power order. It follows from the analyticity that $\tau ^p(M)$ is non-vanishing on some neighborhood of $\zeta \xi$.
:::

## The mod $p$ WRT functions {#sec:mod-p-wrt}

Let $p$ be a prime and let $\Fp$ be the field of $p$ elements. Let $\bFp$ denote the algebraic closure of $\Fp$, and set $\bFp^\times =\Fp\setminus \{0\}$.

For $f(q)\in \Zqh$ and $x\in \bFp^\times$, the value $f(x)\in \bFp$ of $f(q)$ at $x$ is well defined, since we have $(x)_m=0$ whenever $m\ge \ord(x)$. (Recall that any $x\in \bFp^\times$ is a root of unity.) Note that $f(x)$ is contained in the (finite) subfield of $\bFp$ generated by $x$ over $\Fp$. For $f(q)\in \Zqh$, define a function $$\tilde{f}\zzzcolon \bFp^\times \rightarrow \bFp$$ by $\tilde{f}(x)=f(x)$. Then $\tilde{f}$ is Galois equivariant, i.e., for any $\alpha \in \Gal(\bFp/\Fp)$, we have $$f(\alpha (x))=\alpha (f(x)).$$ The correspondence $f(q)\mapsto \tilde{f}$ defines a ring homomorphism $$\mods _{\bFp^\times }\zzzcolon \Zqh\rightarrow \Fung,$$ where $\Fung$ denotes the ring of all Galois-equivariant functions from $\bFp^\times$ to $\bFp$.

Clearly, $\mods _{\bFp^\times }$ is not injective. In fact, it factors through the surjective homomorphism $$\Zqh\rightarrow \Fpqh:=\varprojlim_{n}\Fpq/((q)_n) \bigl(\cong \Zqh\otimes _\modZ \Fp)$$ induced by $\modZ [q]\rightarrow \Fp[q]$. Thus there is a ring homomorphism $$s'_{\bFp^\times }\zzzcolon \Fpqh\rightarrow \Fung$$ induced by $\mods _{\bFp^\times }$.

::: proposition
[]{#r35 label="r35"} $s'_{\bFp^\times }$ is surjective, but not injective. Moreover, we have an isomorphism $$\label{e54}
    \Fung\cong \prod_{r\in \modN _p}\Fpq/(\Phi _r(q)).$$
:::

::: proof
*Proof.* Set $\modN _p=\{r\in \modN \zzzvert \text{$r$ coprime with $p$}\}$. We have the following isomorphisms $$\Fpqh
    \cong\varprojlim_{r\in \modN _p,k\ge 0}\Fpq/((q^r-1)^k)
    \cong\prod_{r\in \modN _p}\varprojlim_{k\ge 0}\Fpq/(\Phi _r(q)^k).$$ The first one follows, since in $\Fpq$ the families of ideals, $\{((q)_n)\}_{n\ge 0}$ and $\{((q^r-1)^k)\}_{r\in \modN _p,k\ge 0}$ are cofinal with each other. (This is a consequence of the identity $q^{rp^e}-1=(q^r-1)^{p^e}$ in $\Fpq$ for $r\in \modN _p$ and $e\ge 1$.) The second isomorphism can be verified using the Chinese Remainder Theorem in a way similar to the arguments in [@H:cyclotomic Section 7.5].

For each $r\in \modN _p$, there is a surjective, non-injective homomorphism $$\varprojlim_{k\ge 0}\Fpq/(\Phi _r(q)^k)\rightarrow \Fpq/(\Phi _r(q)),\quad$$ induced by $\Fpq\rightarrow \Fpq/(\Phi _r(q))$. Hence, there is a surjective, non-injective homomorphism $$\prod_{r\in \modN _p}\varprojlim_{k\ge 0}\Fpq/(\Phi _r(q)^k)\rightarrow \prod_{r\in \modN _p}\Fpq/(\Phi _r(q)).$$

Thus it remains to show the second assertion. Note that $\Fung$ has a natural direct sum decomposition $$\Fung \cong \prod_{r\in \modN _p}\Fun_g(\calZ_r(\bFp),\bFp),$$ where $\calZ_r(\bFp)\subset \bFp$ is the set of primitive $r$th roots of unity, and $\Fun_g(\calZ_r(\bFp),\bFp)$ is the ring of Galois-equivariant functions from $\calZ_r(\bFp)$ into $\bFp$. Since there is a natural $\Fp$-algebra isomorphism $$\Fp[q]/(\Phi _r(q))\cong \Fun_g(\calZ_r(\bFp),\bFp), \quad
    f(q)\mod{(\Phi _r(q))}\mapsto (x\mapsto f(x)),$$ we have the isomorphism [\[e54\]](#e54){reference-type="eqref" reference="e54"}. ◻
:::

Now, set $$\label{e22}
  \tmodp(M)=\mods _{\bFp^\times }(J_M)\in \Fung.$$ We call it the *mod $p$ WRT function* of $M$. For $x\in \bFp^\times$, $$\tau _x(M):=\tmodp(M)(x)$$ may be regarded as the WRT invariant at $x$.

$\tmodp(M)$ is determined by $J_M\mod p\in \Fpqh$, but Proposition [\[r35\]](#r35){reference-type="ref" reference="r35"} implies that this fact gives no information on the range of $\tmodp(M)$.

However, the $\tmodp(M)$ for infinitely many primes $p$ can determine $J_M$ (and hence the WRT invariants) by the following.

::: proposition
[]{#r1 label="r1"} If $P$ is an infinite set of primes, then the ring homomorphism $$(\mods _{\bFp^\times })_{p\in P}
    \zzzcolon \Zqh\rightarrow \prod_{p\in P}\Fun(\bFp^\times ,\bFp)$$ is injective.
:::

::: proof
*Proof.* Suppose $(\mods _{\bFp^\times })_{p\in P}(f(q))=0$, $f(q)\in \Zqh$. It suffices to prove that for any $\zeta \in \calZ$, we have $\mods _\zeta (f(q))=0$. For each $p\in P$ coprime with $n:=\ord(\zeta )$, choose a ring homomorphism $\pi _{\zeta ,p}\zzzcolon \modZ [\zeta ]\rightarrow \bFp$, which maps $\zeta$ to a primitive $n$th root of unity in $\bFp$. By assumption, $\pi _{\zeta ,p}\mods _\zeta (f(q))=0$. This implies that $\mods _\zeta (f(q))\in \modZ [\zeta ]$ is divisible by $p$. Since there are infinitely many such $p$, it follows that $\mods _\zeta (f(q))=0$. Hence, the assertion follows from Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"}. ◻
:::

It is well known that $\bFp$ is isomorphic to the residue class field $\modO _p/\modP _p$. Thus, understanding the property of the function $\tmodp(M)$ may be considered as the first step in understanding the properties of $\tau ^p(M)$. Let $$\pi \zzzcolon \modO _p\rightarrow \modO _p/\modP _p\cong\bFp,$$ denote the projection. Then we have $$\label{e84}
  \tau _{\pi (y)}(M)=\pi (\tau _y(M))$$ for $y\in U(\modO _p)$.

The following conjecture is supported by some computer calculations.

::: conjecture
[]{#r31 label="r31"} For any integral homology sphere $M$ and for any prime $p$, $\tmodp(M)\zzzcolon \bFp^\times \rightarrow \bFp$ is nowhere zero.
:::

Using [\[e84\]](#e84){reference-type="eqref" reference="e84"}, one can easily see that Conjecture [\[r31\]](#r31){reference-type="ref" reference="r31"} implies Conjecture [\[r33\]](#r33){reference-type="ref" reference="r33"}.

::: remark
[]{#r65 label="r65"} One can apply the construction in this section to any invariants of $3$-manifolds and links with values in $\Zqh$ to obtain functions like [\[e77\]](#e77){reference-type="eqref" reference="e77"} and [\[e22\]](#e22){reference-type="eqref" reference="e22"}. For the case of the normalized Jones polynomials $\theta _2(J_T) = J_K(\V'_1)\in \modZ [q,q^{-1}]\subset \Zqh$ for $i\ge 1$ and the unified Kashaev invariant $\theta _0(J_T)\in \Zqh$, the analogues of Conjectures [\[r33\]](#r33){reference-type="ref" reference="r33"} and [\[r31\]](#r31){reference-type="ref" reference="r31"} do not hold. Probably, these conjecture do not hold in general for the normalized colored Jones polynomials $\theta _n(J_T) = J_K(\V'_{n-1})$ for $n\ge 3$.
:::
