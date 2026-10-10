---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-014-6-description-of-a-non-semisimple-block
section_title: "Description of a non-semisimple block"
section_number: 6
pages: 37-39
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
text_source: latex
latex_prose_ratio: 0.681
latex_coverage_ratio: 0.923
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
[]{#blockquiver label="blockquiver"}

In this section we give a complete description of nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ for all $d\in\mathbb{Z}_{\geq0}$. In particular, we prove that all nontrivial blocks are equivalent as additive categories. We begin by describing the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$. Next, we show that for fixed $d\in\mathbb{Z}_{\geq0}$, the nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent. We then state a conjecture which would allow us to compare blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with those in $\underline{\operatorname{Re}}\!\operatorname{p}(S_{d-1}; F)$ using a "restriction functor.\" Finally, we use Martin's results on the partition algebras to give a complete description of nontrivial blocks.

## The nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$

In this section we give a complete description of the one nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_0; F)$. In this particular case the constructions of all idempotents are easy enough that we are able to fully describe the block by brute force computations. We expect this method is too computationally complicated in other cases.

Throughout this section we consider the group algebra of the symmetric group $FS_n$ as a subalgebra of the partition algebra $FP_n(0)$ (see Remark [\[Snembedding\]](#Snembedding){reference-type="ref" reference="Snembedding"}). With this in mind, we have the following idempotents:$$\begin{equation*}
 s_n:=\frac{1}{n!}\sum_{\sigma\in S_n}sgn(\sigma)\sigma\in FP_n(0).
\end{equation*}$$

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

Next, define the following morphisms: $$\begin{equation*}
 \alpha_n:=(-1)^n(n+1)!s_{n+1}x^n_{n+1}s_{n},\qquad\beta_n:=\frac{1}{n!}s_nx^{n+1}_ns_{n+1}\quad (n\geq0),
\end{equation*}$$ $$\begin{equation*}
\gamma_n:=(-1)^nns_nx_n^{n-1}x_{n-1}^ns_n\quad(n>0).
\end{equation*}$$

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

## Comparison of non-semisimple blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$.

In this section we show that for fixed $d\in\mathbb{Z}_{\geq0}$, the non-semisimple blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent as additive categories. Thereafter we conjecture that a restriction functor induces an equivalence of categories between certain non-semisimple blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ and $\underline{\operatorname{Re}}\!\operatorname{p}(S_{d-1}; F)$. First, let us fix some notation. Given a block $\mathcal{B}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$, let $\operatorname{Inc}_\mathcal{B}: \mathcal{B}\to\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ and $\operatorname{Proj}_\mathcal{B}: \underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)\to\mathcal{B}$ denote the inclusion and projection functors respectively.

::: proposition
[]{#blocksfixd label="blocksfixd"} Suppose $\mathcal{B}$ is a nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ which is not minimal with respect to $\prec$. There exists a block $\mathcal{B}'$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with $\mathcal{B}'\precneqq\mathcal{B}$ such that $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}:\mathcal{B}\to\mathcal{B}'$ is an equivalence of additive categories. Hence, all nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent as additive categories.
:::

::: proof
*Proof.* First, notice $d\not=0$ as we are assuming a nontrivial block exists in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. Hence, $\operatorname{Lift}_d(L(\Box))=L(\Box)$ (see Example [\[lift1\]](#lift1){reference-type="ref" reference="lift1"}(1)). Let $B=\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ denote the set of Young diagrams corresponding to indecomposable objects in $\mathcal{B}$. Now, let $B'=\{\rho^{(0)}\subset\rho^{(1)}\subset\cdots\}$ be the set of Young diagrams given by Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2), and $\mathcal{B}'$ the corresponding block. By Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"} we have the following $$\begin{array}{rcll}
\operatorname{Lift}_d(L(\lambda^{(0)})) & = & L(\lambda^{(0)}),\\
\operatorname{Lift}_d(L(\lambda^{(i)}))&=&L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})&(i>0),\\
\operatorname{Lift}_d(L(\rho^{(0)}))&=&L(\rho^{(0)}),\\
\operatorname{Lift}_d(L(\rho^{(i)}))&=&L(\rho^{(i)})\oplus L(\rho^{(i-1)})& (i>0).\\
\end{array}$$ Hence, by Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(1) and Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2), $$\begin{array}{rrcll}
\operatorname{Lift}_d(L(\lambda^{(i)})\otimes L(\Box))&=&\operatorname{Lift}_d(L(\lambda^{(i)}))\otimes L(\Box)&=&\operatorname{Lift}_d(L(\rho^{(i)}))\oplus A,\\
\operatorname{Lift}_d(L(\rho^{(i)})\otimes L(\Box))&=&\operatorname{Lift}_d(L(\rho^{(i)}))\otimes L(\Box)&=&\operatorname{Lift}_d(L(\lambda^{(i)}))\oplus B,\\
\end{array}$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ for all $i\geq0$, where $A$ (resp. $B$) is an object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ with no indecomposable summands of the form $L(\rho^{(j)})$ (resp. $L(\lambda^{(j)})$). Thus, by Propositions [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3) and [\[liftsim\]](#liftsim){reference-type="ref" reference="liftsim"}, $L(\lambda^{(i)})\otimes L(\Box)=L(\rho^{(i)})\oplus A'$ and $L(\rho^{(i)})\otimes L(\Box)=L(\lambda^{(i)})\oplus B'$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ for all $i\geq 0$, where $A'$ (resp. $B'$) is an object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with no indecomposable summands of the form $L(\rho^{(j)})$ (resp. $L(\lambda^{(j)})$). Hence, $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}$ and $\operatorname{Proj}_\mathcal{B}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}'}$ are inverse to one another on objects. Moreover, since $(-\otimes L(\Box))$ is self-adjoint and $\operatorname{Proj}_\mathcal{B}$ is both right and left adjoint to $\operatorname{Inc}_{\mathcal{B}}$, it follows that $\operatorname{Proj}_\mathcal{B}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}'}$ is adjoint to $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}$. The result follows. ◻
:::

Next, we use the universal property of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ (see [@Del07 8.3]) to define a restriction functor.

::: definition
Let $\underline{\operatorname{Res}}_{S_{t-1}}^{S_t}:\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)\to\underline{\operatorname{Re}}\!\operatorname{p}(S_{t-1}; F)$ denote the functor given by the universal property of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ which sends $([1], \text{id}_1)\mapsto([1], \text{id}_1)\oplus([0], \text{id}_0)$.
:::

::: conjecture
[]{#conjecture label="conjecture"} For $d\in\mathbb{Z}_{\geq0}$, let $\mathcal{B}_d$ denote the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ containing the object $L(\varnothing)$. Then the functor $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ induces an equivalence of additive categories $\mathcal{B}_{d+1}\cong\mathcal{B}_{d}$.
:::

::: remark
It is not hard to show that $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ is bijective on objects. Hence, to prove Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"} it suffices to show $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ is either full or faithful.
:::

## Description of blocks via Martin

In this section we give a general description of the nontrivial blocks based on the results of Martin. We start by reviewing the main result in [@MR1399030].

Assume $d\not=0$ and let $\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots$ denote the Young diagrams associated to a fixed nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. For each $m\geq|\lambda^{(n)}|$, let $E_m^{(n)}$ denote the simple $FP_m(d)$-module associated to $\lambda^{(n)}$ (see Theorem [\[idemP\]](#idemP){reference-type="ref" reference="idemP"}(1)), and let $P_m^{(n)}$ denote its projective cover. According to [@MR1399030 Proposition 9], these modules have Loewy structure $$\begin{equation*}
\label{loewy}\begin{array}{l}
P_m^{(0)}=\begin{array}{c}
 E^{(0)}_m \\
E^{(1)}_m
\end{array}\quad(m\geq|\lambda^{(1)}|),\\
\\
P_m^{(n)}=\begin{array}{rcl}
& E^{(n)}_m &\\
E^{(n-1)}_m & & E^{(n+1)}_m\\
& E^{(n)}_m &
\end{array}\quad(n>0, m\geq|\lambda^{(n+1)}|).
\end{array}
\end{equation*}$$ In other words, for $m>0$, $P_m^{(0)}$ has a maximal simple submodule $B_0\cong E_m^{(1)}$ with $P_m^{(0)}/B_0\cong E^{(0)}_m$. Moreover, for each $m\geq|\lambda^{(n+1)}|$ there exists a chain of submodules $$\includegraphics{diss73.pdf}$$ with $P_m^{(n)}/A_n\cong E^{(n)}_m, A_n/B_n^{\pm}\cong E^{(n\mp1)}_m, B_n^{\pm}/C_n\cong E^{(n\pm1)}_m$, and $C_n\cong E^{(n)}_m$ for $n>0$. Using the notation above, define the following maps[^1]: $$\begin{equation}
\label{martinmaps}\begin{array}{ll}
\alpha_0=\alpha_{0, m}:P^{(0)}_m\twoheadrightarrow P^{(0)}_m/B_0\cong C_1\hookrightarrow P^{(1)}_m\\
\beta_0=\beta_{0, m}:P^{(1)}_m\twoheadrightarrow P^{(1)}/B_1^+\cong P_m^{(0)}\\
\alpha_n=\alpha_{n,m}: P_m^{(n)}\twoheadrightarrow P_m^{(n)}/B^-_n\cong B^-_{n+1}\hookrightarrow P_m^{(n+1)} &  (n>0) \\
\beta_n=\beta_{n,m}:P_m^{(n+1)}\twoheadrightarrow P_m^{(n+1)}/B^+_{n+1}\cong B^+_n\hookrightarrow P_m^{(n)}  &  (n>0)\\
\gamma_n=\gamma_{n,m}: P_m^{(n)}\twoheadrightarrow P_m^{(n)}/A_n\cong C_n\hookrightarrow P_m^{(n)}  &  (n>0)
\end{array}
\end{equation}$$

We are now ready to give a general description of the nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$.

::: theorem
[]{#blocksviamartin label="blocksviamartin"} Suppose $d$ is a nonnegative integer and $\mathcal{B}$ is a nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. Then $\mathcal{B}$ is equivalent as an additive category to the nontrivial block described in Theorem [\[zeroblock\]](#zeroblock){reference-type="ref" reference="zeroblock"}.
:::

::: proof
*Proof.* We may assume $d\not=0$. Notice $$\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)}(L(\lambda^{(n)}), L(\lambda^{(n')}))=\operatorname{Hom}_{FP_m(d)}(P_m^{(n)}, P_m^{(n')})$$ whenever $m\geq |\lambda^{(n)}|, |\lambda^{(n')}|$. Hence, by Proposition [\[dimstuff\]](#dimstuff){reference-type="ref" reference="dimstuff"}(2), it suffices to prove the maps defined by ([\[martinmaps\]](#martinmaps){reference-type="ref" reference="martinmaps"}) satisfy equations (1)-(7) in Lemma [\[calculations\]](#calculations){reference-type="ref" reference="calculations"}. Equations (1)-(5) are clearly satisfied. The fact that equations (6) and (7) are satisfied follows from the observation that the maps $B^\mp_{n\pm1}\hookrightarrow P_m^{(n\pm1)}\twoheadrightarrow P_m^{(n\pm1)}/B^\pm_{n\pm1}\cong B^\pm_n$ factor through the maps $B^\mp_{n\pm1}\twoheadrightarrow B^\mp_{n\pm1}/C_{n\pm1}\cong C_n\hookrightarrow B^\pm_n$. ◻
:::

::: remark
Our proof of Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} is a bit unsatisfactory since it is based on rather deep results from [@MR1399030]. On the other hand Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} follows from Theorem [\[zeroblock\]](#zeroblock){reference-type="ref" reference="zeroblock"}, Proposition [\[blocksfixd\]](#blocksfixd){reference-type="ref" reference="blocksfixd"}, along with Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"}. Hence a proof of Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"} would complete a proof of Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} which is independent from [@MR1399030].
:::

[^1]: The equations in ([\[martinmaps\]](#martinmaps){reference-type="ref" reference="martinmaps"}) are only defined when $m$ is sufficiently large.
