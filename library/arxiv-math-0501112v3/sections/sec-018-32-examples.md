---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-018-32-examples
section_title: "Examples"
section_number: 3.2
pages: 13-18
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.984
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
All examples presented in this section not only have the character factorization property but additionally are as in Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"}.

::: example
[]{#example:1 label="example:1"} It is easy to check that if $\rho_q$ is the left-regular representation of $S_q$ then for any permutations $\sigma_1,\dots,\sigma_n$ with disjoint supports $$k(\sigma_1,\dots,\sigma_n) q^{
\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2} } = \begin{cases} 1 &
\text{if } n=1 \text{ and } \sigma_1=e, \\ 0 & \text{otherwise.}
\end{cases}$$ It follows from condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} that the left-regular representation has the character factorization property and that the mean and the covariance of the free cumulants are given by $$\label{eq:kerov1} \lim_{q\to\infty} {\mathbb{E}}(R_{l+1})
q^{-\frac{l+1}{2} } = \begin{cases} 1 & \text{if } l=1 , \\
0 & \text{if } l\geq 2, \end{cases}$$ and $$\label{eq:kerov2} \lim_{q\to\infty} \mathop{\mathrm{Cov}}(R_{l_1+1},R_{l_2+1} )
q^{-\frac{l_1+l_2}{2}} = \begin{cases} l_1 & \text{if } l_1=l_2\geq
2, \\ 0 & \text{if } l_1=l_2=1, \\ 0 & \text{if } l_1\neq l_2.
\end{cases}$$ By applying Corollary [\[coro:gaussian\]](#coro:gaussian){reference-type="ref" reference="coro:gaussian"} we recover Kerov central limit theorem for the Plancherel measure [@Kerov1993gaussian; @IvanovOlshanski2002].
:::

::: example
[]{#example:2 label="example:2"} For some integer $d_q\geq 1$ let $\rho_q$ be the representation of ${{S}}_{q}$ acting on $({\mathbb{C}}^{d_q})^{\otimes q}$ by permutation of factors. This representation appears naturally within Schur-Weyl duality. It is easy to check that for permutations $\sigma_1,\dots,\sigma_n$ with disjoint supports $$k(\sigma_1,\dots,\sigma_n) q^{
\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2} }= \begin{cases}
\left( \frac{\sqrt{q}}{d_q}\right)^{|\sigma_1|} & \text{if } n=1,
\\ 0 & \text{otherwise,} \end{cases}$$ hence if the limit ${p}:=\lim_{q\to\infty} \frac{\sqrt{q}}{d_n}$ exists then (condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}) the sequence $(\rho_q)$ has the character factorization property and the mean and the covariance of the free cumulants are given by $$\lim_{q\to\infty} {\mathbb{E}}(R_{l+1})
q^{-\frac{l+1}{2} }=  {p}^{l-1},$$ and $$\lim_{q\to\infty}
\mathop{\mathrm{Cov}}(R_{l_1+1},R_{l_2+1} ) q^{-\frac{l_1+l_2}{2}}= \sum_{r\geq 2}
\binom{l_1}{r} \binom{l_2}{r} r \ {p}^{l_1+l_2-2 r}$$ for all integers $l,l_1,l_2\geq 1$. Note that for ${p}=0$ we recover the fluctuations of the Plancherel measure.

Some asymptotic results for this representation were proved by Biane [@Biane2001approximate].
:::

::: example
[]{#example:3 label="example:3"} Let $c>0$ be a constant and let $(\lambda_q)$ be a sequence of Young diagrams. We assume that $\lambda_q$ has $q$ boxes and it has at most $c \sqrt{q}$ rows and columns. Suppose that the shapes of rescaled Young diagrams $q^{-\frac{1}{2} } \lambda_q$ converge to some limit. The convergence of the shapes of Young diagrams implies convergence of the free cumulants and it follows (condition [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"}) that the sequence $(\rho^{\lambda_q})$ of the corresponding irreducible representations has the characters factorization property.

In this example the cumulants [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} and [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} vanish for $n\geq 2$ since the Young diagrams are non-random and the corresponding limits for $n=1$ are determined by the limit of the shape of the Young diagrams.
:::

The above three examples are the building blocks from which one can construct some more complex representations with the help of the operations on representations presented below.

::: theorem
Suppose that the sequence of representations $(\rho_q)$ has the character factorization property. Let a sequence of integers $(r_q)$ be given, such that $r_q\geq q$ and the limit ${p}=\lim_{q\to\infty}
\frac{q}{r_q}$ exists.

Let $\rho'_q$ denote the restriction of the representation $\rho_{r_q}$ to the subgroup $S_q\subseteq S_{r_q}$. Then the sequence $(\rho'_q)$ has the factorization property of characters. The fluctuations of the free cumulants are determined by $$c_{l+1}':=\lim_{q\to\infty} {\mathbb{E}}(R'_{l+1}) q^{-\frac{l+1}{2} }=
{p}^{\frac{l-1}{2}} \lim_{q\to\infty} {\mathbb{E}}(R_{l+1}) q^{-\frac{l+1}{2}
}= {p}^{\frac{l-1}{2}} c_{l+1}, \label{equ:restrictionA}$$ $$\begin{gathered}
 \lim_{q\to\infty} \mathop{\mathrm{Cov}}(R'_{l_1+1},R'_{l_2+1})
q^{-\frac{l_1+l_2}{2}}= \\ {p}^{\frac{l_1+l_2}{2}} \Bigg[
\lim_{q\to\infty} \mathop{\mathrm{Cov}}(R_{l_1+1},R_{l_2+1}) q^{-\frac{l_1+l_2}{2}} -
 l_1 l_2 c_{l_1+1} c_{l_2+1} \left( {p}^{-1}- 1\right) + \\
\sum_{r\geq 1}\sum_{\substack{a_1,\dots,a_r\geq 1\\
a_1+\dots+a_r=l_1}}  \sum_{\substack{b_1,\dots,b_r\geq 1\\
b_1+\dots+b_r=l_2}} \frac{l_1 l_2}{r} c_{a_1+b_1} \cdots c_{a_r+b_r}
\left(  {p}^{-r}-1 \right) \Bigg] \label{mul:restrictionB}
\end{gathered}$$ for all $l,l_1,l_2\geq 1$, where the quantities $R'_i,c'_i$ concern the representations $(\rho'_q)$ while $R_i,c_i$ concern the representations $(\rho_q)$.

In particular, for ${p}=0$ we recover the fluctuations of the Plancherel measure.
:::

::: proof
*Proof.* Notice that for any permutations $\sigma_1,\dots,\sigma_n$ the value of the cumulant $k(\sigma_1,\dots,\sigma_n)$ is the same for the representation $\rho'_q$ of $S_q$ and for the representation $\rho_{r_q}$ of $S_{r_q}$. It follows that $$\begin{gathered}
 \lim_{q\to\infty} k_{\rho'_q}(\sigma_1,\dots,\sigma_n)
q^{\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2}}= \\
{p}^{\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2}}
\lim_{q\to\infty}k_{\rho_{r_q}}(\sigma_1,\dots,\sigma_n)
(r_q)^{\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2}}
\end{gathered}$$ Since the original representations $(\rho_q)$ fulfill condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} hence restricted representations $(\rho'_q)$ fulfill [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} as well. Equations [\[equ:restrictionA\]](#equ:restrictionA){reference-type="eqref" reference="equ:restrictionA"} and [\[mul:restrictionB\]](#mul:restrictionB){reference-type="eqref" reference="mul:restrictionB"} follow as special cases for $n=1,2$. ◻
:::

::: remark
Please notice that the above theorem concerns restrictions of the form $\rho_{r_q}\big\downarrow^{S_{r_q}}_{S_{q}}$ while it is even more interesting to ask about the asymptotics of the restrictions of the form $\rho''_q=\rho_{r_q}\big\downarrow^{S_{r_q}}_{S_{q}\times
S_{r_q-q}}$. A typical question is the following one: let $[\lambda^{(1)}]\times [\lambda^{(2)}]$ be a random irreducible component of $\rho''_q$; is it true that the joint distribution of the free cumulants $\big(R_i(\lambda^{(r)})\big)_{r\in\{1,2\};
i\geq 2}$ converges after appropriate rescaling to a family of Gaussian variables? The answer for this question is positive and the Reader may easily prove it using the methods presented in Section [\[sec:Proof-main-result\]](#sec:Proof-main-result){reference-type="ref" reference="sec:Proof-main-result"}.
:::

Such representations are no longer representations of symmetric groups (but products of such groups) and the original definition of representations with the approximate factorization property does not fit into this setup. Nevertheless

In the work of Pittel and Romik [@PittelRomik04] some interesting results concerning restrictions of irreducible representations corresponding to rectangular Young diagrams were proved.

::: theorem
[]{#theo:outerproduct label="theo:outerproduct"} Suppose that for $i\in\{1,2\}$ the sequence of representations $(\rho^{(i)}_q)$ has the character factorization property. Let sequences of positive integers $r^{(i)}_q$ be given, such that $r^{(1)}_q+r^{(2)}_q=q$ and the limits ${p}^{(i)}:=\lim_{q\to\infty} \frac{r^{(i)}}{q}$ exist.

Let $\rho'_q=\rho^{(1)}_{r^{(1)}_q} \circ \rho^{(2)}_{r^{(2)}_q}$ denote the outer product of representations. Then the sequence $(\rho'_q)$ has the factorization property of characters with $$\label{eq:outerA} c_{l+1}':=\lim_{q\to\infty} {\mathbb{E}}(R'_{l+1})
q^{-\frac{l+1}{2} }=  \left({p}^{(1)}\right)^{\frac{l+1}{2}}
c^{(1)}_{l+1} + \left({p}^{(2)}\right)^{\frac{l+1}{2}}
c^{(2)}_{l+1},$$ and with an explicit (but involved) covariance of free cumulants. The appropriate disjoint covariance is given by $$\begin{gathered}
 \lim_{q\to\infty}
\mathop{\mathrm{Cov}}_{\rho'_q}^{\bullet}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2}}= \\\shoveleft{({p}^{(1)}
)^{\frac{l_1+l_2}{2}} \lim_{q\to\infty}
\mathop{\mathrm{Cov}}_{\rho^{(1)}_{q}}^{\bullet}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2}}+} \\
({p}^{(2)} )^{\frac{l_1+l_2}{2}}  \lim_{q\to\infty}
\mathop{\mathrm{Cov}}_{\rho^{(2)}_{q}}^{\bullet}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2}}.
\end{gathered}$$
:::

::: proof
*Proof.* By definition, $$\rho'_q=\big( \rho^{(1)}_{r^{(1)}_q} \times
\rho^{(2)}_{r^{(2)}_q} \big) \big\uparrow_{S_{r^{(1)}_q} \times
S_{r^{(2)}_q}}^{S_q}$$ and we can use the Frobenius reciprocity between the induction and restriction of representations. It follows that the corresponding normalized characters fulfill for all $l_1,\dots,l_n\geq 1$ $$\chi_{\rho'} (\Sigma_{l_1} \bullet \cdots \bullet \Sigma_{l_n})=
\big(\chi_{\rho^{(1)}} \otimes \chi_{\rho^{(2)}} \big) \big(
(\Sigma_{l_1}\otimes 1+1 \otimes \Sigma_{l_1}) \bullet \cdots
\bullet (\Sigma_{l_n}\otimes 1+1 \otimes \Sigma_{l_n})  \big).$$ We can treat the left-hand side as a mixed moment ${\mathbb{E}}(\Sigma_{l_1}
\bullet \cdots \bullet \Sigma_{l_n})$ in the algebra of conjugacy classes equipped with the disjoint product; analogous interpretation is possible also for the right-hand side. Since equality holds for all $l_1,\dots,l_n\geq 2$ it follows that the joint distributions of the family of random variables $(\Sigma_i)_{i\geq 2}$ coincides with the joint distribution of random variables $(\Sigma_{i}\otimes 1+1
\otimes \Sigma_{i})_{i\geq 2}$; in particular their cumulants are equal: $$\begin{gathered}
\label{eq:kumulantyok}
k^{\bullet}_{\rho'}(\Sigma_{l_1},\dots,\Sigma_{l_n})=
k^{\bullet}_{\rho^{(1)}\otimes \rho^{(2)}}(\Sigma_{l_1}\otimes
1+1\otimes \Sigma_{l_1},\dots,\Sigma_{l_n}\otimes 1+1\otimes
\Sigma_{l_n})=\\
k^{\bullet}_{\rho^{(1)}}(\Sigma_{l_1},\dots,\Sigma_{l_n})+
k^{\bullet}_{\rho^{(2)}}(\Sigma_{l_1},\dots,\Sigma_{l_n}).
\end{gathered}$$ In the last equality we used that the cumulant is linear with respect to each of the arguments and that the mixed cumulant of independent random variables vanishes.

It follows that $$\begin{gathered}
 \lim_{q\to\infty}
k_{\rho'_q}^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})
q^{-\frac{l_1+\cdots+l_n-n+2}{2}}= \\({p}^{(1)}
)^{\frac{l_1+\cdots+l_n-n+2}{2}}  \lim_{q\to\infty}
k_{\rho^{(1)}_{r^{(1)}_q}}^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})
(r^{(1)}_q)^{-\frac{l_1+\cdots+l_n-n+2}{2}}+ \\
({p}^{(2)} )^{\frac{l_1+\cdots+l_n-n+2}{2}}  \lim_{q\to\infty}
k_{\rho^{(2)}_{r^{(2)}_q}}^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})
(r^{(1)}_q)^{-\frac{l_1+\cdots+l_n-n+2}{2}}.
\end{gathered}$$ It follows that if the representations $\rho^{(i)}$ fulfill condition [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} then representations $\rho'_q$ fulfill [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} as well. Equation [\[eq:outerA\]](#eq:outerA){reference-type="eqref" reference="eq:outerA"} results as a special case of $n=1$ and we leave it as a simple exercise to the Reader to study the case $n=2$ and to find the covariance of the free cumulants, analogous to [\[equ:restrictionA\]](#equ:restrictionA){reference-type="eqref" reference="equ:restrictionA"}. ◻
:::

::: theorem
Suppose that the sequence of representations $(\rho_q)$ has character factorization property. Let a sequence of integers $r_q$ be given, such that $r_q\leq q$ and the limit ${p}=\lim_{q\to\infty}
\frac{r_q}{q}$ exists.

Let $\rho'_q=\rho_{r_q}\uparrow_{S_{r_q}}^{S_q}$ denote the induced representation. Then the sequence $(\rho'_q)$ has the characters factorization property with $$c'_{l+1}=\begin{cases} {p}^{\frac{l+1}{2}} c_{l+1} & \text{for } l\geq 2, \\
1 & \text{for } l=1, \end{cases}$$ and with an explicit (but involved) covariance of free cumulants.
:::

::: proof
*Proof.* It is enough to adapt the proof of Theorem [\[theo:outerproduct\]](#theo:outerproduct){reference-type="ref" reference="theo:outerproduct"}. ◻
:::

::: theorem
Suppose that for $i\in\{1,2\}$ the sequence of representations $(\rho^{(i)}_q)$ has character factorization property. Then the tensor product $\rho'_q=\rho^{(1)}_q \otimes \rho^{(2)}_q$ has the property of factorization of characters. Furthermore, the limit distribution and the fluctuations are the same as for the Plancherel measure [\[eq:kerov1\]](#eq:kerov1){reference-type="eqref" reference="eq:kerov1"} and [\[eq:kerov2\]](#eq:kerov2){reference-type="eqref" reference="eq:kerov2"}.
:::

::: proof
*Proof.* Since the normalized characters fulfill for any $\pi\in S_q$ $$\chi_{\rho'_q}(\pi)= \big( \chi_{\rho^{(1)}_q} \otimes
\chi_{\rho^{(2)}_q} \big) (\pi \otimes \pi)$$ hence also the corresponding cumulants are equal: $$k_{\rho'_q}(\sigma_1,\dots,\sigma_n)=k_{\rho^{(1)}_q\otimes \rho^{(2)}_q}
(\sigma_1\otimes \sigma_1,\dots,\sigma_n\otimes \sigma_n).$$ Theorem [\[theo:leonovsiraev\]](#theo:leonovsiraev){reference-type="ref" reference="theo:leonovsiraev"} of Leonov and Sirjaev can be used to calculate the right-hand side. Lemma [\[lem:connections\]](#lem:connections){reference-type="ref" reference="lem:connections"} together with the condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} for $\rho^{(i)}$ show that the right-hand side is of order $O(q^{-(|\sigma_1|+\cdots+|\sigma_n|+n-1)})$ hence condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} is fulfilled for $\rho'$. It also follows that the limits in Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"} are given by $$c_{l+1}=\lim_{q\to\infty} {\mathbb{E}}(\sigma)
q^{ \frac{l-1}{2} }= \begin{cases} 1 & \text{if } l=1, \\ 0 &
\text{if } l\geq 2, \end{cases}$$ $$\lim_{q\to\infty} \mathop{\mathrm{Cov}}(\sigma_1,\sigma_2)
q^{\frac{l_1+l_2}{2} }= 0,$$ where $\sigma$, $\sigma_1$, $\sigma_2$ are disjoint cycles with lengths, respectively, $l$, $l_1$, $l_2$. ◻
:::
