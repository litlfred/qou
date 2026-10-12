---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-014-6-description-of-a-non-semisimple-block
section_title: "Description of a non-semisimple block"
section_number: 6
pages: 37-39
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.686
---
[]{#blockquiver label="blockquiver"}

In this section we give a complete description of nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ for all $d\in\mathbb{Z}_{\geq0}$. In particular, we prove that all nontrivial blocks are equivalent as additive categories. We begin by describing the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$. Next, we show that for fixed $d\in\mathbb{Z}_{\geq0}$, the nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent. We then state a conjecture which would allow us to compare blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with those in $\underline{\operatorname{Re}}\!\operatorname{p}(S_{d-1}; F)$ using a "restriction functor.\" Finally, we use Martin's results on the partition algebras to give a complete description of nontrivial blocks.

## The nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$

In this section we give a complete description of the one nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$. In this particular case the constructions of all idempotents are easy enough that we are able to fully describe the block by brute force computations. We expect this method is too computationally complicated in other cases.

Throughout this section we consider the group algebra of the symmetric group $FS_n$ as a subalgebra of the partition algebra $FP_n(0)$ (see Remark [\[Snembedding\]](#Snembedding){reference-type="ref" reference="Snembedding"}). With this in mind, we have the following idempotents:$$s_n:=\frac{1}{n!}\sum_{\sigma\in S_n}sgn(\sigma)\sigma\in FP_n(0).$$

::: proposition
[]{#sgn label="sgn"} In $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$, $([n], s_n)\cong L((1^n))$ for all $n\geq 0$.
:::

::: proof
*Proof.* The proposition is certainly true when $n=0$, so we assume $n>0$. Since the projection $FP_n(0)\twoheadrightarrow FS_n$ maps $s_n\mapsto s_n$, and in $FS_n$ the idempotent $s_n$ is primitive corresponding to $(1^n)$, we know any orthogonal decomposition of $s_n$ into primitive idempotents in $FP_n(0)$ must contain a summand corresponding to $L((1^n))$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$. Thus, by Example [\[3class\]](#3class){reference-type="ref" reference="3class"}(1) and Proposition [\[dimstuff\]](#dimstuff){reference-type="ref" reference="dimstuff"} it suffices to show $\dim_F s_nFP_n(0)s_n=2$.

Suppose $\mu\in P_{n,n}$ satisfies $\tau\mu=\pi$ for some transposition $\tau\in S_n\subset P_{n,n}$. Then $s_n\mu s_n=s_n\tau\mu s_n=-s_n\pi s_n$, which implies $s_n\mu s_n=0$. Similarly, if $\mu\tau=\mu$ for some transposition $\tau$, then $s_n\mu s_n=0$. The only elements of $\mu\in P_{n,n}$ such that $\tau\mu\not=\mu$ and $\mu\tau\not=\mu$ for all transpositions $\tau\in S_n$ are either elements of $S_n$ or of the form $\sigma x\sigma'$ for some $\sigma, \sigma'\in S_n$ with $x=\text{id}_{n-1}\otimes\pi$ where $\pi\in P_{1,1}$ is as in the proof of Theorem [\[idemP\]](#idemP){reference-type="ref" reference="idemP"}. If $\mu\in S_n$, then $s_n\mu s_n=\pm s_n$. If $\mu=\sigma x\sigma'$ for some $\sigma, \sigma'\in S_n$, then $s_n\mu s_n=\pm s_n x s_n$. Hence, $s_n$ and $s_n x s_n$ span $s_nFP_n(0)s_n$. ◻
:::

As a consequence of Example [\[3class\]](#3class){reference-type="ref" reference="3class"}(1) and Proposition [\[sgn\]](#sgn){reference-type="ref" reference="sgn"}, describing the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$ amounts to describing morphisms among the objects $([n], s_n)$ for $n\geq0$. To describe such morphisms, let $x^1_0$ denote the unique element of $P_{1,0}$ and let $x_n^{n+1}=\text{id}_n\otimes x^1_0$ for all $n>0$. Finally, let $x^n_{n+1}=(x^{n+1}_n)^\vee$ for all $n\geq 0$ as pictured below. $$\includegraphics{diss71.pdf}$$ The following lemma records a couple properties useful in forthcoming calculations.

::: lemma
[]{#calcs label="calcs"} The following identities hold in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$:

\(1\) $s_n x_n^{n+1}s_{n+1}=x_n^{n+1}s_{n+1}$ for all $n\geq 0$.

\(2\) $-ns_nx_n^{n-1}x_{n-1}^ns_n=(n+1)x_n^{n+1}s_{n+1}x^n_{n+1}$ for all $n> 0$.

\(3\) $x_{n-1}^nx_n^{n+1}s_{n+1}=0$ for all $n>0$.
:::

::: proof
*Proof.* To prove part (1), let $s_n'=s_n\otimes\text{id}_1\in FP_{n+1}(0)$ for all $n\geq 0$. Then $s_n x_n^{n+1}s_{n+1}=x_n^{n+1}s_n's_{n+1}=x_n^{n+1}s_{n+1}$.

To prove part (2), notice that for $\sigma\in S_{n+1}$ there are exactly $(n-1)!$ pairs $(\tau_1, \tau_2)$ with $\tau_1, \tau_2\in S_n$ such that $\tau_1x_n^{n-1}x_{n-1}^n\tau_2=x_n^{n+1}\sigma x_{n+1}^n$. Moreover, for such a pair $sgn(\tau_1\tau_2)=-sgn(\sigma)$. Conversely, given any $\tau_1, \tau_2\in S_n$, either $\tau_1x_n^{n-1}x_{n-1}^n\tau_2=0$ or there exists a unique $\sigma\in S_{n+1}$ with $\tau_1x_n^{n-1}x_{n-1}^n\tau_2=x_n^{n+1}\sigma x_{n+1}^n$. Therefore, $-(n!s_n)x_n^{n-1}x_{n-1}^n(n!s_n)=(n-1)!x_n^{n+1}(n+1)!s_{n+1}x^n_{n+1}$ which is equivalent to the identity in part (2).

To prove part (3), let $\tau\in S_{n+1}$ denote the transposition $n\leftrightarrow n+1$. Then $x_{n-1}^nx_n^{n+1}s_{n+1}=(x_{n-1}^nx_n^{n+1}\tau) s_{n+1}=x_{n-1}^nx_n^{n+1}(\tau s_{n+1})=-x_{n-1}^nx_n^{n+1}s_{n+1}$. The result follows. ◻
:::

Next, define the following morphisms: $$\alpha_n:=(-1)^n(n+1)!s_{n+1}x^n_{n+1}s_{n},\qquad\beta_n:=\frac{1}{n!}s_nx^{n+1}_ns_{n+1}\quad (n\geq0),$$ $$\gamma_n:=(-1)^nns_nx_n^{n-1}x_{n-1}^ns_n\quad(n>0).$$

The next lemma contains all calculations needed to describe the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$.

::: lemma
[]{#calculations label="calculations"}The following equations hold in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$:

\(1\) $\alpha_n\not=0$ for $n\geq0$.

\(2\) $\beta_n\not=0$ for $n\geq0$.

\(3\) $\gamma_n\not=0$ for $n>0$.

\(4\) $\gamma_n^2=0$ for $n>0$, hence $\gamma_n$ is not a scalar multiple of $s_n$.

\(5\) $\beta_0\alpha_0=0$.

\(6\) $\beta_n\alpha_n=\gamma_n$ for $n>0$.

\(7\) $\alpha_{n-1}\beta_{n-1}=\gamma_n$ for $n>0$.

\(8\) $\alpha_n\alpha_{n-1}=0$ for $n>0$.

\(9\) $\beta_{n-1}\beta_n=0$ for $n>0$.
:::

::: proof
*Proof.* Up to a nonzero scalar multiple, $\alpha_n$ and $\beta_n^\vee$ are equal. Hence, parts (1) and (8) will follow from parts (2) and (9) respectively.

\(2\) Write $\beta_n=\sum_{\pi\in P_{n+1, n}}b_\pi\pi$. Then $b_{x_n^{n+1}}=\frac{1}{n!(n+1)!}$.

\(3\) Write $\gamma_n=\sum_{\pi\in P_{n+1, n}}c_\pi\pi$. Then $c_{x_n^{n-1}x_{n-1}^{n}}=\frac{(-1)^n}{n!}$.

\(4\) $\gamma_n^2=-n(n+1)s_nx_n^{n-1}x_{n-1}^nx_n^{n+1}s_{n+1}x_{n+1}^n=0$, (Lemma [\[calcs\]](#calcs){reference-type="ref" reference="calcs"}(2)&(3)).

\(5\) $\beta_0\alpha_0=-x_0^1x_1^0=0$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$.

\(6\) $\beta_n\alpha_n=(-1)^{n+1}(n+1)s_nx_n^{n+1}s_{n+1}x_{n+1}^ns_n=\gamma_n$, (Lemma [\[calcs\]](#calcs){reference-type="ref" reference="calcs"}(2)).

\(7\) $\alpha_{n-1}\beta_{n-1}=(-1)^{n}ns_nx_n^{n-1}s_{n-1}x_{n-1}^ns_n=\gamma_n$, (Lemma [\[calcs\]](#calcs){reference-type="ref" reference="calcs"}(1)).

\(9\) $\beta_{n-1}\beta_n=\frac{1}{(n-1)!n!}s_{n-1}x_{n-1}^ns_nx_n^{n+1}s_{n+1}$, which (by Lemma [\[calcs\]](#calcs){reference-type="ref" reference="calcs"}(1)) is equal to $\frac{1}{(n-1)!n!}s_{n-1}x_{n-1}^nx_n^{n+1}s_{n+1}$, which (by Lemma [\[calcs\]](#calcs){reference-type="ref" reference="calcs"}(3)) is equal to zero. ◻
:::

The following theorem describes the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$.

::: theorem
[]{#zeroblock label="zeroblock"} Let $L_n:=L((1^n))$ for all $n\geq 0$. The nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$ has the following associated quiver $$\includegraphics{diss72.pdf}$$ with relations: $\beta_0\alpha_0=0$, $\alpha_{n}\alpha_{n-1}=0$, $\beta_{n-1}\beta_{n}=0$, $\beta_n\alpha_n=\alpha_{n-1}\beta_{n-1}$ for $n>0$.
:::

::: proof
*Proof.* The indecomposable objects in the block follow from Example [\[3class\]](#3class){reference-type="ref" reference="3class"}(1). The fact that the arrows generate all the morphisms between the indecomposable objects follows from Lemma [\[dimstuff\]](#dimstuff){reference-type="ref" reference="dimstuff"} and Lemma [\[calculations\]](#calculations){reference-type="ref" reference="calculations"}(1)-(4)&(6). By Lemma [\[calculations\]](#calculations){reference-type="ref" reference="calculations"}(5)-(9), the relations hold. Finally, the relations imply that the only nonzero compositions of $\alpha$'s and $\beta$'s are of the form $\alpha_n~ (n\geq 0), \beta_n~ (n\geq 0)$, and $\beta_n\alpha_n ~(n> 0)$. By Lemma [\[calculations\]](#calculations){reference-type="ref" reference="calculations"}(4)&(6), $\beta_n\alpha_n$ and $s_n=\text{id}_{L_n}$ are linearly independent. Hence the relations are exhaustive. ◻
:::

::: remark
The block described in Theorem [\[zeroblock\]](#zeroblock){reference-type="ref" reference="zeroblock"} is equivalent to the nontrivial blocks in the *Temperley-Lieb category*. This can be deduced from the results in [@Wes §10].
:::
