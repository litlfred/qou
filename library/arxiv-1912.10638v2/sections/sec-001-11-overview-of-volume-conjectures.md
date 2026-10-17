---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-001-11-overview-of-volume-conjectures
section_title: "Overview of volume conjectures"
section_number: 1.1
pages: 1-3
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.975
---
The volume conjecture of the colored Jones polynomials, discovered by R. Kashaev, H. Murakami and J. Murakami, suggests that the $N$-th colored Jones polynomials of a hyperbolic knot evaluated at the $N$-th root of unity $t=e^{\frac{2\pi i}{N}}$ grow exponentially with exponential growth rate equal to the hyperbolic volume of the knot complement.

::: conjecture
[]{#cvc label="cvc"}[@K97; @MM01] Let $K$ be a hyperbolic knot and $J'_{N}(K;t)$ be the normalized $N$-th colored Jones polynomials of $K$ evaluated at $t$ such that $J'_N(unknot,t)=1$ for all $N\in {\mathbb N}$. We have $$\begin{aligned}
\lim_{N \to \infty} \frac{2\pi}{N} \log|J'_{N}(K;e^{\frac{2\pi i}{N}})| = \operatorname{Vol}({\mathbb S}^{3} \backslash K),
\end{aligned}$$ where $\operatorname{Vol}({\mathbb S}^{3} \backslash K)$ is the hyperbolic volume of the knot complement in ${\mathbb S}^3$.
:::

Later, H. Murakami and J. Murakami extended the above volume conjecture to non-hyperbolic links and suggested that the exponential growth rate captures the simplicial volume of the link complement.

::: conjecture
[]{#cvcMM label="cvcMM"}[@MM01] Let $L$ be a link and $J'_{\vec{N}}(L;t)$ be the $\vec{N}$-th normalized colored Jones polynomials of $L$ evaluated at $t$, where $\vec{N} = (N,\dots, N)$. We have $$\begin{aligned}
\lim_{N \to \infty} \frac{2\pi}{N} \log|J'_{\vec{N}}(L;e^{\frac{2\pi i}{N}})| = v_3||{\mathbb S}^3 \backslash L||,
\end{aligned}$$ where $||{\mathbb S}^3 \backslash L||$ is the simplicial volume of the link complement.
:::

In 2015, Q. Chen and T. Yang discovered a version of volume conjecture for the Turaev-Viro invariants at a primitive $2r$-th root of unity, where $r$ is odd. The conjecture can be stated as follows.

::: conjecture
[]{#vctv label="vctv"}[@CY15] For every hyperbolic 3-manifold $M$ with finite volume, we have $$\begin{aligned}
\lim_{\substack{ r\to \infty \\r \text{ odd}}}\frac{2\pi}{r}\log \left(TV_{r}(M,e^{\frac{2\pi i}{r}})\right) = \operatorname{Vol}(M)
\end{aligned}$$
:::

It turns out when the $3$-manifold is a link complement, the Turaev-Viro invariant is related to the unnormalized colored Jones polynomials of the link evaluated at certain $(N+1/2)$-th root of unity as follows.

::: theorem
[]{#relationship label="relationship"} [@DKY17]. Let L be a link in ${\mathbb S}^3$ with n components. Then given an odd integer $r=2N+1 \geq 3$, we have $$\begin{aligned}
TV_{r}\left({\mathbb S}^3 \backslash L, e^{\frac{2\pi i}{r}}\right) = 2^{n-1}\left( \frac{2\sin(\frac{2\pi}{r})}{\sqrt{r}}\right)^{2} \sum_{1\leq \vec{M} \leq \frac{r-1}{2}}\left|{J}_{\vec{M}}\left(L,e^{\frac{2\pi i }{N+\frac{1}{2}}}\right)\right|^2 .
\end{aligned}$$ Here, $J_{\vec{M}}(L,t)$ is the unnormalized colored Jones polynomials of the link $L$ with $$J_N(U,t) = \frac{t^{\frac{N}{2}} - t^{-\frac{N}{2}}}{t^{\frac{1}{2}}-t^{-\frac{1}{2}}}$$ for the unknot $U$ and any $N \in {\mathbb N}$.
:::

Therefore, by studying the asymptotics of the colored Jones polynomials of links at this $(N+1/2)$-th root of unity, one can relate the volume conjecture of the colored Jones polynomials of a link to the volume conjecture of the Turaev-Viro invariants of its complement. In particular, in [@DKY17], the volume conjecture for the Turaev-Viro invariants is extended to the complement of non-hyperbolic links and this generalization is proved for all knots with zero simplicial volume.

::: conjecture
[]{#tvGM label="tvGM"}[@DKY17] For every link $L$ in ${\mathbb S}^3$, we have $$\lim_{\substack{ r\to \infty \\r \text{ odd}}} \frac{2\pi }{r} \log(TV_r({\mathbb S}^3 \backslash L, e^{\frac{2\pi i}{r}})) = v_3 ||{\mathbb S}^3 \backslash L||,$$ where $v_3$ is the volume of an ideal regular tetrahedron.
:::

Besides, in [@DKY17], R. Detcherry, E. Kalfagianni and T. Yang ask the following question:

::: conjecture
[]{#sVC label="sVC"}(Question 1.7 in [@DKY17]) Is it true that for any hyperbolic link $L$ in ${\mathbb S}^3$, we have $$\lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log|J_{\vec{N}}(L,e^{\frac{2\pi i}{N+\frac{1}{2}}}) | = \operatorname{Vol}({\mathbb S}^3 \backslash L) \quad ?$$
:::

The answer is affirmative when $L$ is the figure eight knot. In fact, for the figure eight knot we can say more. In [@WA17], Thomas Au and the author consider the $M$-th colored Jones polynomials of the figure eight knot evaluated at the $(N+1/2)$-th root of unity $t=e^{\frac{2\pi i}{N+1/2}}$. Here we regard $M$ as a sequence in $N$ and define the limiting ratio $$s = \lim_{N \to \infty} \frac{M}{N+1/2}.$$ As a direct consequence of Theorem 7 (ii) in [@WA17], we have the following result.

::: theorem
[@WA17][]{#WAthm label="WAthm"} For the figure eight knot $4_1$, there exists $\delta > 0$ such that for any $1-\delta < s \leq 1$, we have $$\lim_{N \to \infty} \frac{2\pi }{N+\frac{1}{2}}\log|J_M(4_1, e^{\frac{2\pi i}{N+\frac{1}{2}}}) | =  \operatorname{Vol}\left({\mathbb S}^3 \backslash 4_1, u = 2\pi i (1 - s)\right),$$ where $\operatorname{Vol}\left({\mathbb S}^3 \backslash 4_1, u = 2\pi i (1 - s)\right)$ is the volume of ${\mathbb S}^3 \backslash 4_1$ equipped with the (possibly incomplete) hyperbolic structure such that the logarithm of the holonomy of the meridian is given by $u = 2\pi i (1-s)$.
:::

An important remark is that Theorerm [\[WAthm\]](#WAthm){reference-type="ref" reference="WAthm"} is true for the root of unity $t=e^{\frac{2\pi i}{N+1/2}}$ but false for the original root $t=e^{\frac{2\pi i}{N}}$ [^1]. As a generalization, we propose the generalized volume conjecture for hyperbolic links at $t=e^{\frac{2\pi i}{N+1/2}}$ as follows (c.f. Question 4.6 and Theorem 4.8 in [@C07]).

::: conjecture
[]{#GVCHL label="GVCHL"} (Generalized volume conjecture for hyperbolic links) Let $L$ be a hyperbolic link with $n$ components. Let $M_1, M_2, \dots , M_n$ be sequences of positive integers in $N$. Let $\displaystyle s_i = \lim_{N\to\infty} \frac{M_i}{N+1/2}$. Then there exists $\delta_L > 0$ such that whenever the limiting ratio $s_i \in (1 - \delta_L, 1]$, we have $$\begin{aligned}
\lim_{N\to \infty} \frac{2\pi }{N+\frac{1}{2}} \log| J_{M_1,\dots,M_n}(L,e^{\frac{2\pi i}{N+\frac{1}{2}}})| = \operatorname{Vol}({\mathbb S}^3\backslash L, u_i = 2\pi i (1-s_i)),
\end{aligned}$$ where $\operatorname{Vol}({\mathbb S}^3\backslash L, u_i = 2\pi i (1-s_i))$ is the volume of ${\mathbb S}^3 \backslash L$ equipped with the hyperbolic structure such that the logarithm of the holonomy of the meridian around the $i$-th component is given by $u_i = 2\pi i(1 - s_i)$.
:::

[^1]: This type of generalized volume conjecture has been studied in several literatures (e.g. [@GM08], [@MY07], [@HM13]). Unfortunately, in the original setting, i.e. $t=e^{\frac{2\pi i}{N}}$, this generalization fails even for knots (see Section 4 in [@C07]). Besides, the original volume conjecture is not true for split links due to the choice of normalization. Even if the normalization problem is fixed, in [@V08] R. van der Veen shows that the conjecture is false for the Whitehead chains with more than one belt.

    On the other hand, if we consider the root $q=e^{\frac{2\pi i}{N+1/2}}$ rather than the original root, the above problems disappear and it gives a hope to have a generalized volume conjecture to hyperbolic links. Note that the difference between these two roots of unities has also been discussed in [@WA17].
