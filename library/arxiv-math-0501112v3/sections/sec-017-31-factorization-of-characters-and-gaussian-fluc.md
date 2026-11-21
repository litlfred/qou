---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-017-31-factorization-of-characters-and-gaussian-fluc
section_title: "Factorization of characters and Gaussian fluctuations"
section_number: 3.1
pages: 10-13
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.978
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
The following theorem is the main result of this article. In order not to scare the Reader we postpone its proof to Section [\[sec:Proof-main-result\]](#sec:Proof-main-result){reference-type="ref" reference="sec:Proof-main-result"}.

::: theoremanddefinition
[]{#theo:main label="theo:main"} For each $q\geq 1$ let $\rho_q$ be a representation of $S_q$. We say that the sequence $(\rho_q)$

has the character factorization property if it fulfills one (hence all) of the following equivalent conditions:

-   for any cycles $\sigma_1,\dots,\sigma_n$ with disjoint supports $$\label{eq:faktoryzacja1} k(\sigma_1,\dots,\sigma_n) q^{
    \frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2} }= O(1);$$

-   for any integers $l_1,\dots,l_n\geq 1$ $$\label{eq:faktoryzacja2}
    k^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})  q^{-
    \frac{l_1+\cdots+l_n-n+2}{2}  } = O(1);$$

-   for any integers $l_1,\dots,l_n\geq 1$ $$\label{eq:faktoryzacja3} k(\Sigma_{l_1},\dots,\Sigma_{l_n})
    q^{-\frac{l_1+\cdots+l_n-n+2}{2} }  = O(1);$$

-   for any integers $l_1,\dots,l_n\geq 2$ $$\label{eq:faktoryzacja4} k(R_{l_1},\dots,R_{l_n} )
    q^{-\frac{l_1+\cdots+l_n-2(n-1)}{2}  }= O(1) .$$
:::

::: remark
In Corollary [\[cor:roznegradacjejednadegradacja\]](#cor:roznegradacjejednadegradacja){reference-type="ref" reference="cor:roznegradacjejednadegradacja"} we will prove that if conditions [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} and [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} hold true then they also hold true in a more general situation when conjugacy classes $(\Sigma_{l_i})$ with only one non-trivial cycle are replaced by general conjugacy classes $\Sigma_{l_{i,1},\dots,l_{i,m(i)}}$. Similarly one can show that if condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} holds true then it also holds true in a general situation when we do not assume that $(\sigma_i)$ are cycles.
:::

To show that a given sequence of representations has the character factorization property usually it is the most convenient to verify condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} or condition [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}. Then conditions [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} and [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} are important corollaries (for applications see Corollary [\[coro:gaussian\]](#coro:gaussian){reference-type="ref" reference="coro:gaussian"} below).

Expressions appearing in conditions [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}--[\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} are closely related to each other and knowledge of one of them allows us to compute the others (in fact this is how Theorem and Definition [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"} will be proved). For general $n$ these formulas are quite involved, however in the following we will need only such formulas for $n\in\{1,2\}$ and these are provided by the following theorem.

::: theorem
[]{#theo:main2 label="theo:main2"} Let $(\rho_q)$ has the character factorization property. If the limit of one of the expressions [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}--[\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} exists for $n\in\{1,2\}$ then the limits of all of the expressions [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}--[\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} exist for $n\in\{1,2\}$.

These limits fulfill $$\label{eq:granicamomentow} c_{l+1}:= \lim_{q\to\infty} {\mathbb{E}}(\sigma)
q^{ \frac{l-1}{2} }= \lim_{q\to\infty} {\mathbb{E}}(\Sigma_{l})
q^{-\frac{l+1}{2} }  = \lim_{q\to\infty} {\mathbb{E}}(R_{l+1})
q^{-\frac{l+1}{2} },$$ where $\sigma$ is a cycle of length $l$ and $$\begin{gathered}
\label{eq:granicamomentow2} \lim_{q\to\infty}
\mathop{\mathrm{Cov}}(R_{l_1+1},R_{l_2+1} ) q^{-\frac{l_1+l_2}{2}}
=\lim_{q\to\infty}\mathop{\mathrm{Cov}}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2} }=\\
\shoveleft{ \lim_{q\to\infty} \mathop{\mathrm{Cov}}^{\bullet}
(\Sigma_{l_1},\Sigma_{l_2}) q^{-
\frac{l_1+l_2}{2}  } }+ \\ \shoveright{ \sum_{r\geq 1}\sum_{\substack{a_1,\dots,a_r\geq 1\\
a_1+\dots+a_r=l_1}}  \sum_{\substack{b_1,\dots,b_r\geq 1\\
b_1+\dots+b_r=l_2}} \frac{l_1 l_2}{r} c_{a_1+b_1} \cdots
c_{a_r+b_r}=} \\
\shoveleft{ \lim_{q\to\infty} \mathop{\mathrm{Cov}}(\sigma_1,\sigma_2)
q^{\frac{l_1+l_2}{2} } -l_1 l_2 c_{l_1+1} c_{l_2+1}+} \\
\sum_{r\geq 1}\sum_{\substack{a_1,\dots,a_r\geq 1\\
a_1+\dots+a_r=l_1}}  \sum_{\substack{b_1,\dots,b_r\geq 1\\
b_1+\dots+b_r=l_2}} \frac{l_1 l_2}{r} c_{a_1+b_1} \cdots c_{a_r+b_r}
\end{gathered}$$ where $\sigma_1,\sigma_2$ are disjoint cycles of length $l_1,l_2$, respectively, and where the numbers $c_i$ were defined in [\[eq:granicamomentow\]](#eq:granicamomentow){reference-type="eqref" reference="eq:granicamomentow"}.
:::

Proof of this theorem is also postponed to Section [\[sec:Proof-main-result\]](#sec:Proof-main-result){reference-type="ref" reference="sec:Proof-main-result"}; we will prove it together with Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}. Identity [\[eq:granicamomentow\]](#eq:granicamomentow){reference-type="eqref" reference="eq:granicamomentow"} was proved by Biane [@Biane1998; @Biane2001approximate] and we skip its proof; for Readers acquainted with the results of Section [\[sec:Proof-main-result\]](#sec:Proof-main-result){reference-type="ref" reference="sec:Proof-main-result"} and Section [\[sec:Proof-Theorem-?????\]](#sec:Proof-Theorem-?????){reference-type="ref" reference="sec:Proof-Theorem-?????"} it will be a simple exercise.

::: corollary
[]{#coro:gaussian label="coro:gaussian"} Let $(\rho_q)$ be as in Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"} and let $\lambda$ be a random Young diagram distributed according to the canonical probability measure associated to $\rho_q$.

1.  []{#item:gaba1 label="item:gaba1"}*(Gaussian fluctuations of free cumulants)* Then the joint distribution of the centered random variables $$r_i=q^{-\frac{i-2}{2}} (R_i - {\mathbb{E}}R_i)$$ converges to a Gaussian distribution in the weak topology of probability measures, where $R_i$ denotes the free cumulant of the transition measure $\mu^{\lambda}$.

2.  []{#item:gaba2 label="item:gaba2"} *(Gaussian fluctuations of characters)* Let $\sigma_i$ denote a cycle of length $i$. Then the joint distribution of the centered random variables $$\label{eq:gausowskiecharaktery} q^{ \frac{|\sigma_i|+1}{2} }
    \big(\chi^{\lambda}(\sigma_i)- {\mathbb{E}}\chi^{\lambda}(\sigma_i)\big)$$ converges to a Gaussian distribution in the weak topology of probability measures.

3.  []{#item:gaba3 label="item:gaba3"} *(Gaussian fluctuations of the shape of the Young diagrams)* Then the joint distribution of the centered random variables $$q^{-\frac{i-2}{2}} (\tilde{p}_i - {\mathbb{E}}\tilde{p}_i)$$ converges to a Gaussian distribution in the weak topology of probability measures, where $\tilde{p}_i=\tilde{p}_i(\lambda)$ is the functional of the shape of the Young diagram defined in [\[eq:p-tylda\]](#eq:p-tylda){reference-type="eqref" reference="eq:p-tylda"}.
:::

::: proof
*Proof.* We will prove now point [\[item:gaba1\]](#item:gaba1){reference-type="eqref" reference="item:gaba1"}. Condition [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} implies that if $n\neq 2$ then $$\lim_{q\to\infty} k(r_{i_1},\dots,r_{i_n})=0$$ and therefore the family $(r_i)$ converges in moments to a Gaussian distribution. Since Gaussian measures are uniquely determined by their moments it follows that the convergence holds true also in the weak topology of probability measures.

To proof point [\[item:gaba2\]](#item:gaba2){reference-type="eqref" reference="item:gaba2"} we observe that asymptotically, as $q\to\infty$ random variables [\[eq:gausowskiecharaktery\]](#eq:gausowskiecharaktery){reference-type="eqref" reference="eq:gausowskiecharaktery"} have the same behavior as random variables $$\label{eq:gausowskiecharaktery2} \lambda\mapsto q^{
\frac{-|\sigma_i|+1}{2} } \big(q^{\underline{|\sigma_i|}}
\chi^{\lambda}(\sigma_i)- {\mathbb{E}}q^{\underline{|\sigma_i|}}
\chi^{\lambda}(\sigma_i)\big),$$ where $q^{\underline{k}}=q (q-1) \cdots (q-k+1)$ denotes the falling power. Function on Young diagrams [\[eq:gausowskiecharaktery2\]](#eq:gausowskiecharaktery2){reference-type="eqref" reference="eq:gausowskiecharaktery2"} corresponds (via Fourier transform) to the central function in ${\mathbb{C}}(S_q)$ $$q^{
\frac{-|\sigma_i|+1}{2} } \big(\Sigma_i - {\mathbb{E}}\Sigma_i\big).$$ It follows that we may use [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} in the same way as in the above proof of point [\[item:gaba1\]](#item:gaba1){reference-type="eqref" reference="item:gaba1"}.

Ivanov and Olshanski [@IvanovOlshanski2002] proved that point [\[item:gaba1\]](#item:gaba1){reference-type="eqref" reference="item:gaba1"} implies point [\[item:gaba3\]](#item:gaba3){reference-type="eqref" reference="item:gaba3"}; their proof is a careful analysis of the fact that $\tilde{p}_i$ can be expressed as a polynomial in free cumulants. ◻
:::
