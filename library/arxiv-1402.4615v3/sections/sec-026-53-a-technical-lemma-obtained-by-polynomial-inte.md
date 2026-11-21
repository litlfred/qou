---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-026-53-a-technical-lemma-obtained-by-polynomial-inte
section_title: "A technical lemma obtained by polynomial interpolation"
section_number: 5.3
pages: 37-38
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.984
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
In order to study asymptotics of large Young diagrams we need to understand some special cases of structure constants. Here, we present some technical, but useful lemma about them:

::: lemma
[]{#lem:SC label="lem:SC"} We have the following identities:

1.  []{#eq:SC-1 label="eq:SC-1"} $g_{\mu,\nu;\rho} = \delta_{\rho, \mu \cup \nu}$ for $|\rho| + \ell(\rho) \geq |\mu| + \ell(\mu) + |\nu| + \ell(\nu)$;

2.  []{#eq:SC-2 label="eq:SC-2"} $g_{\mu,\nu;1^k} = 0$ for $\tilde{\mu} \neq \tilde{\nu}$ and $2k \geq |\mu| + \ell(\mu) + |\nu| + \ell(\nu) - 2$;

3.  []{#eq:SC-3 label="eq:SC-3"} $g_{(k),(k);1^k} = k$;

4.  []{#eq:SC-4 label="eq:SC-4"} $g_{(k),(l);\rho} = 0$ for $|\rho| + \ell(\rho) = k+l+1$.
:::

::: proof
*Proof.* Let $x(\mu,\nu;\rho) :=  |\mu| + \ell(\mu) + |\nu| + \ell(\nu) -  (|\rho| + \ell(\rho))$.

By Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"} we know that $g_{\mu,\nu;\rho}$ is a polynomial in $\gamma$ of degree at most $x(\mu,\nu;\rho)$ and of the same parity as $x(\mu,\nu;\rho)$. Hence, if one wants to prove that for some particular partitions, $g_{\mu,\nu;\rho}$ is identically equal to some constant $c$, it is enough to prove that:

-   $g^{(1)}_{\mu,\nu;\rho} = c$ in the case $x(\mu,\nu;\rho) = 0$;

-   $g^{(2)}_{\mu,\nu;\rho} = c$ in the case $x(\mu,\nu;\rho) = 1$ (necessarily, $c=0$ in this case);

-   $g^{(1)}_{\mu,\nu;\rho} = g^{(2)}_{\mu,\nu;\rho} = c$ in the case $x(\mu,\nu;\rho) = 2$.

Applying this idea, we see that the first item holds true, since this is true for $\alpha = 1$ [@IvanovOlshanski2002 Proposition 4.9.].

Consider now the second item. In this case, $x(\mu,\nu;\rho) \le 2$, hence we need to prove that $g^{(1)}_{\mu,\nu;1^k} = g^{(2)}_{\mu,\nu;1^k} = 0$. We know from Lemma [\[lem:SC1\]](#lem:SC1){reference-type="ref" reference="lem:SC1"} [\[eq:SC1-1\]](#eq:SC1-1){reference-type="eqref" reference="eq:SC1-1"} that $c^{(1)}_{\pi,\rho;1^n} = 0$ for any pair of different partitions $\pi, \rho \vdash n$. It means that for $n$ large enough, thanks to [\[EqCG\]](#EqCG){reference-type="eqref" reference="EqCG"}, we have the following equation: $$0 = \sum_{0 \leq i \leq k+1} g^{(1)}_{\tilde{\pi},\tilde{\rho}; (1^i)} \cdot i! \cdot \binom{n}{i},$$ hence $$g^{(1)}_{\tilde{\pi},\tilde{\rho}; (1^i)} = 0 \quad \text{for each $0\leq i\leq k+1$.}$$ The same holds for $g^{(2)}$ using Lemma [\[lem:SC2\]](#lem:SC2){reference-type="ref" reference="lem:SC2"}. This finishes the case where $\mu$ and $\nu$ have no parts equal to $1$.

The general case follows, since for any $\lambda \vdash n$ one has $$\mathop{\mathrm{Ch}}_\mu(\lambda) = (n-|\tilde{\mu}|)_{m_1(\mu)}\mathop{\mathrm{Ch}}_{\tilde{\mu}}(\lambda).\bigskip$$

In order to prove the third item, we need to prove the equalities $$g^{(1)}_{(k),(k);1^k} = k = g^{(2)}_{(k),(k);1^k}
\text{ (as $x( (k),(k);1^k ))=2$)}.$$ Here, we use Equation [\[EqCG\]](#EqCG){reference-type="eqref" reference="EqCG"} again. We have that $$c^{(1)}_{(k 1^n),(k 1^n);(1^{k+n})} = \frac{1}{k^2} 
\sum_{0 \leq i \leq k+n} g^{(1)}_{(k),(k);(1^i)}    
i! \binom{k+n}{i}.$$ Moreover, the summation index can be restricted to $i \le k$ as $g^{(1)}_{(k),(k);(1^i)}=0$ for $i>k$. By Lemma [\[lem:SC1\]](#lem:SC1){reference-type="ref" reference="lem:SC1"} [\[eq:SC1-2\]](#eq:SC1-2){reference-type="eqref" reference="eq:SC1-2"} one has that $$c^{(1)}_{(k 1^n),(k 1^n);(1^{k+n})} = \binom{k+n}{k} (k-1)!.$$ It gives us $$\binom{k+n}{k} (k-1)! = \frac{1}{k^2} 
\sum_{0 \leq i \leq k} g^{(1)}_{(k),(k);(1^i)}    
i! \binom{k+n}{i}$$ and since both sides of the equation are polynomials in $n$, the equation $g^{(1)}_{(k),(k);(1^k)} = k$ follows (all others $g^{(1)}_{(k),(k);(1^i)}$ vanish). The same proof works for $\alpha=2$, using Lemma [\[lem:SC2\]](#lem:SC2){reference-type="ref" reference="lem:SC2"} [\[eq:SC2-2\]](#eq:SC2-2){reference-type="eqref" reference="eq:SC2-2"}.

Finally, let us prove the last item. As $x( (k),(l),\rho)=1$ in this case, it is enough to prove that $g^{(2)}_{(k),(l);\rho} = 0$. Here, we shall use a different approach. It is proved in [@NousZonal Theorem 5.3] that the coefficient of $$\left(R_2^{(2)}\right)^{s_2}
\left(R_3^{(2)}\right)^{s_3} \cdots$$ in Kerov's expansion of $\mathop{\mathrm{Ch}}^{(2)}_{(k)}\mathop{\mathrm{Ch}}^{(2)}_{(l)} - \mathop{\mathrm{Ch}}^{(2)}_{(k,l)}$ is, up to some constant factor, the number of maps with $2$ faces, $k+l$ edges, $2s_2+ 3s_3 + \cdots$ vertices and some additional properties (the details of which is irrelevant here). But, using the theory of Euler characteristic, such maps may exist only if $$2-(k+l)+2s_2+ 3s_3 + \cdots \le 2,$$ that is $$2s_2+ 3s_3 + \cdots \le k+l.$$ This implies that $$\deg_1\left(\mathop{\mathrm{Ch}}^{(2)}_{(k)}\mathop{\mathrm{Ch}}^{(2)}_{(l)} - \mathop{\mathrm{Ch}}^{(2)}_{(k,l)}\right) = k+l.$$ Expanding it in the Jack characters basis one has $$\mathop{\mathrm{Ch}}^{(2)}_{(k)}\mathop{\mathrm{Ch}}^{(2)}_{(l)} = \mathop{\mathrm{Ch}}^{(2)}_{(k,l)} + \sum_{|\rho|+\ell(\rho) \leq k+l} g^{(2)}_{(k),(l);\rho} \mathop{\mathrm{Ch}}^{(2)}_\rho,$$ which finishes the proof. ◻
:::

::: remark
The equality $g^{(1)}_{(k),(k);(1^k)} = k$ was also established by Kerov, Ivanov and Olshanski [@IvanovOlshanski2002 Proposition 4.12.], using their combinatorial interpretation for $g^{(1)}_{\mu,\nu;\rho}$.
:::
