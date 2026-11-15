---
doc_id: arxiv-2104.06067v1
doc_title: "On irreducible characters of the Iwahori-Hecke algebra in type A"
section_id: sec-002-3-applications-of-the-hook-and-two-row-formulas
section_title: "Applications of the hook and two-row formulas"
section_number: 3
pages: 11-12
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.967
doc_brief: "On irreducible characters of the Iwahori-Hecke algebra in type A — We use vertex operators to compute irreducible characters of the Iwahori-Hecke algebra of type A."
---
Let $V=V_{\bar{0}}\bigoplus V_{\bar{1}}$ be a $\mathbb{Z}_2$-graded vector space over $\mathbb{C}(q)$ with basis $\{v_1,v_2,\cdots,v_a\}$ for the even subspace $V_{\bar 0}$ and basis $\{v_{a+1},v_{a+2},\cdots,v_{a+b}\}$ for the odd subspace $V_{\bar 1}$. Let $\pi$ be the endomorphism of $V\otimes V$ by $$\begin{aligned}
(v_k\otimes v_l)\pi=
\begin{cases}
(-1)^{|v_k||v_l|}v_l\otimes v_k+(q-1)v_k\otimes v_l, k<l\\
\frac{(-1)^{|v_k|}(q+1)+q-1}{2}v_k\otimes v_l, k=l\\
(-1)^{|v_k||v_l|}tv_l\otimes v_k, k>l,
\end{cases}
\end{aligned}$$ and let $\pi_i$ be the endomorphism of $V^{\otimes n}$ by letting $\pi$ acting on the $(i, i+1)$ factor and identity elsewhere, $i=1, \cdots, n-1$. It is known [@Mit] that the map $\Phi^{q,n}_{a,b}: H_n(q)\longrightarrow \mathrm{End}_{\mathbb{C}(t)}(V^{\otimes n})$ defined by $$\begin{aligned}

T_i\longmapsto\pi_i
\end{aligned}$$ gives rise to a representation of $H_n(q)$ called the sign $q$-permutation representation.

Let $\varphi^{n}_{a,b}$ be the character of $\Phi^{q,n}_{a,b}$ and let $s_{a,b}(\lambda)$ be the number of $(a,b)$-semi standard tableaux of shape $\lambda$ [@Sag]. Then $\varphi^{n}_{a,b}$ decomposes as follows [@Zhao]: $$\begin{aligned}
\varphi^{n}_{a,b}=\sum\limits_{\lambda\in H(a,b;n)}s_{a,b}(\lambda)\chi^{\lambda}
\end{aligned}$$ where $H(a,b;n)=\{\lambda\vdash n\mid \lambda_{a+1}\leq b\}$ and $\chi^{\lambda}$ is the irreducible character of $H_n(q)$ labeled by $\lambda\vdash n$.

We consider two special cases $a=b=1$ and $a=2, b=0$. Then $$\begin{aligned}
\label{e:1,1}
\varphi^{n}_{1,1}&=\sum\limits_{k=0}^{n-1}\chi^{(n-k,1^k)}\\\label{e:2,0}
\varphi^{n}_{2,0}&=\sum\limits_{k=0}^{[n/2]}(n-2k+1)\chi^{(n-k,k)}
\end{aligned}$$

::: thm
For $\mu\vdash n$ with $l(\mu)=l$, we have that $$\begin{aligned}
\label{e:hooksum}
\varphi^n_{1,1}(T_{\gamma_{\mu}})&=\sum\limits_{i=0}^{n-1}\chi^{(n-i,1^i)}_{\mu}(q)
=(-1)^{n-l}2^{l-1}\prod\limits_{i=1}^{l}[\mu_i]_{-q},
\\\label{e:twosum}
\varphi^n_{2,0}(T_{\gamma_{\mu}})&=\sum\limits_{i=0}^{[n/2]}(n-2i+1)\chi^{(n-i,i)}_{\mu}(q)

=q^{n-2l(\mu)}\prod\limits_{i=1}^{l}(1+q+\mu_i(q-1)).
\end{aligned}$$
:::

::: proof
*Proof.* It follows from the hook formula [\[e:hook\]](#e:hook){reference-type="eqref" reference="e:hook"} that $$\begin{aligned}
\sum\limits_{i=0}^{n-1}\chi^{(n-i,1^i)}_{\mu}(q)
=&\sum\limits_{i=0}^{n-1}(-1)^{l+i}\sum\limits_{j=n-i}^{n}a_{j}(\mu;q)q^{j}\\
=&(-1)^{n+l-1}\sum\limits_{j=1}^{[n/2]}a_{2j-1}(\mu;q)q^{2j-1}\\
=&(-1)^{n-l}\sum\limits_{j=0}^{n}\frac{(-1)^j-1}{2}a_{j}(\mu;q)q^j\\
=&(-1)^{n-l}2^{l-1}\prod\limits_{i=1}^{l}[\mu_i]_{-q},
\end{aligned}$$ where we have used Lemma [\[l:ab\]](#l:ab){reference-type="ref" reference="l:ab"} and the identity $\sum_{i=0}^na_i(\mu; q)q^i=0$.

Similarly, using the two-row formula [\[e:two\]](#e:two){reference-type="eqref" reference="e:two"} and [\[e:bv\]](#e:bv){reference-type="eqref" reference="e:bv"} we have that $$\begin{aligned}
&\sum\limits_{i=0}^{[n/2]}(n-2i+1)\chi^{n-i,i}_{\mu}(q)\\
=&\sum\limits_{i=0}^{[n/2]}(n-2i+1)q^{n-l}(b_{n-i}(\mu;q)-b_{n-i+1}(\mu;q))\\
=&q^{n-l}\sum_{i=0}^nb_i(\mu; q)\\
=&q^{n-2l(\mu)}\prod\limits_{i=1}^{l}(1+q+\mu_i(q-1)).
\end{aligned}$$ ◻
:::

We remake that Zhao [@Zhao] obtained a negated version of [\[e:hooksum\]](#e:hooksum){reference-type="eqref" reference="e:hooksum"} as a $q$-analog Berele-Regev formula [@BR] by the Murnaghan-Nakayama rule.
