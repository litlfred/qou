---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-027-471-cumulants-of-falling-factorials
section_title: "Cumulants of falling factorials"
section_number: 4.7.1
pages: 24-25
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.712
latex_coverage_ratio: 0.94
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Element $\Sigma_{\underbrace{1,\dots,1}_{k \text{ times}} }\in
{\mathbb{C}}(S_q)$ is equal to $q (q-1) \cdots (q+1-k)$, the multiple of identity, therefore no matter which representation we consider we always have $${\mathbb{E}}\Sigma_{\underbrace{1,\dots,1}_{k \text{ times}} }\in
{\mathbb{C}}(S_q)=q (q-1) \cdots (q+1-k).$$ However, it should be stressed that if we consider the algebra of conjugacy classes equipped with the disjoint product then this element is not longer a multiple of identity and $$\Sigma_{\underbrace{1,\dots,1}_{k_1 \text{
times}} }\bullet \Sigma_{\underbrace{1,\dots,1}_{k_2 \text{ times}}
} =\Sigma_{\underbrace{1,\dots,1}_{k_1+k_2 \text{ times}} }.$$

::: lemma
[]{#lem:kumulantyfallingfactorials label="lem:kumulantyfallingfactorials"} For any integers $l_1,\dots,l_n\geq 1$ $$k^{\bullet}(\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{ times}} },\dots,
\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}} })=
O(q^{l_1+\cdots+l_n+1-n}).$$
:::

::: proof
*Proof.* It is easy to check that $$k(\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{ times}}
},\dots,\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}}
})=\begin{cases} q (q-1) \cdots (q+1-l_1) & \text{if } n=1, \\
0 & \text{if } n\geq 2, \end{cases}$$ hence in particular $$k(\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{ times}}
},\dots,\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}} })
q^{-(l_1+\cdots+l_n+1-n)} = O(1).$$ We leave it as a simple exercise to the reader to check that the presented above proof of the implication [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}$\implies$[\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} can be applied here. ◻
:::

::: proof
*Proof of the implication [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} $\implies$ [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}.* Our goal is to estimate the right-hand side of [\[eq:happynewyear\]](#eq:happynewyear){reference-type="eqref" reference="eq:happynewyear"}. The assumption [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} implies that $$k_{\pi_{(1)}}(\sigma_1,\dots,\sigma_n) = O\big(q^{
-\frac{|\sigma_1|+\cdots+|\sigma_n|+2 n-2 \text{(number of blocks of
$\pi_{(1)}$)}}{2} }\big);$$ Lemma [\[lem:kumulantyfallingfactorials\]](#lem:kumulantyfallingfactorials){reference-type="ref" reference="lem:kumulantyfallingfactorials"} implies that $$k^{\bullet}_{\pi_{(2)}} (\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{
times}} },\dots,\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}}
}) = O\big( q^{l_1+\cdots+l_n +\text{(number of blocks of
$\pi_{(2)}$)}  -n} \big).$$ Now it is enough to use Lemma [\[lem:connections\]](#lem:connections){reference-type="ref" reference="lem:connections"}. ◻
:::

We leave the proof of the identity $$\lim_{q\to\infty} \mathop{\mathrm{Cov}}^{\bullet} (\Sigma_{l_1},\Sigma_{l_2}) q^{-
\frac{l_1+l_2}{2}  } =  \lim_{q\to\infty} \mathop{\mathrm{Cov}}(\sigma_1,\sigma_2)
q^{\frac{l_1+l_2}{2} } -l_1 l_2 c_{l_1+1} c_{l_2+1}$$ which is a part of Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"} as a simple exercise.

::: proof
*Proof of [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} $\implies$ [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}.* We use the induction over $n$. We let us split the sum in equation [\[eq:happynewyear\]](#eq:happynewyear){reference-type="eqref" reference="eq:happynewyear"} into the sum of terms with $\pi_{(1)}$ is the maximal partition with only one block and the sum of all the other terms; therefore $$\begin{gathered}
\label{eq:happynewyear} k(\sigma_{1},\dots,\sigma_{n}) {\mathbb{E}}\big(
\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{ times}} }\bullet\cdots
\bullet \Sigma_{\underbrace{1,\dots,1}_{l_n \text{
times}} } \big)= k^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})- \\
\sum_{\pi_{(1)}, \pi_{(2)}}
k_{\pi_{(1)}}(\sigma_{1},\dots,\sigma_{n}) \ k^{\bullet}_{\pi_{(2)}}
(\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{ times}}
},\dots,\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}} }),
\end{gathered}$$ where the sum runs over partitions $\pi_{(1)},\pi_{(2)}$ such as in [\[eq:happynewyear\]](#eq:happynewyear){reference-type="eqref" reference="eq:happynewyear"} with the additional constraint that $\pi_{(1)}$ is not equal to the maximal partition with only one block. We use the inductive hypothesis and estimate the summands on the right-hand side in the same way as in the proof of the opposite implication above. ◻
:::

## Proof of the main theorem: equivalence [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} $\iff$ [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"}

::: proof
*Proof of equivalence [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} $\iff$ [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"}.* It is enough to apply Corollary [\[cor:roznegradacjejednadegradacja\]](#cor:roznegradacjejednadegradacja){reference-type="ref" reference="cor:roznegradacjejednadegradacja"}. ◻
:::

The remaining part of Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"}, namely $$\lim_{q\to\infty} \mathop{\mathrm{Cov}}(R_{l_1+1},R_{l_2+1} ) q^{-\frac{l_1+l_2}{2}}
=\lim_{q\to\infty}\mathop{\mathrm{Cov}}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2} }$$ follows from the relation [\[eq:wolnekumulantyiklasy\]](#eq:wolnekumulantyiklasy){reference-type="eqref" reference="eq:wolnekumulantyiklasy"} between free cumulants and conjugacy classes.

# Proof of Theorem [\[theo:kumulantykombinatoryczne\]](#theo:kumulantykombinatoryczne){reference-type="ref" reference="theo:kumulantykombinatoryczne"} {#sec:Proof-Theorem-?????}

This section is devoted to the proof of Theorem [\[theo:kumulantykombinatoryczne\]](#theo:kumulantykombinatoryczne){reference-type="ref" reference="theo:kumulantykombinatoryczne"} which is the only missing component in the proof of the main theorem. We will use some tools presented in our recent work [@Sniady2003pushing].
