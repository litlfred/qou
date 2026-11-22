---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-002-3-preliminaries
section_title: "Preliminaries"
section_number: 3
pages: 2-3
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.898
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
Write $[N]=\{0,\ldots,N-1\}$ and choose a prime $m$ with $4N<m<8N$, which we may do by Bertrand's postulate. We embed $[N]$ in $\mathbb{Z}_m$ in the obvious way. The point of choosing $m>2N$ is that a three-term progression in $\mathbb{Z}_m$ whose terms all lie in $[N]$ is a genuine integer progression.

Let $\alpha=\lvert A\rvert/N$ be the density of $A$ in $[N]$, and define $f=\mathbf{1}_A-\alpha\mathbf{1}_{[N]}$ on $\mathbb{Z}_m$. Then $f$ has mean zero on $\mathbb{Z}_m$, satisfies $-\alpha\leq f\leq 1$, and is supported on $[N]$. For any function $g\colon\mathbb{Z}_m\to\mathbb R$, set $$\mathcal E(g)=\sum_{t\in\mathbb{Z}_m}\left(\sum_{x\in\mathbb{Z}_m}g(x)g(x+t)\right)^2.$$ For the balanced function $f$, write $R(t)=\sum_{x\in\mathbb{Z}_m}f(x)f(x+t)$, so $\mathcal E(f)=\sum_{t\in\mathbb{Z}_m}R(t)^2$. We will use the following non-negativity property.

::: lemma
[]{#lem:pos label="lem:pos"} For any $h,k\in\mathbb{Z}_m^\times$, one has $$\label{eq:positivity}
\sum_{d\in\mathbb{Z}_m}R(hd)R(kd)\geq 0.$$
:::

::: proof
*Proof.* Let $\lambda=kh^{-1}$. Using $t=hd$, we have $$\sum_{d\in\mathbb{Z}_m}R(hd)R(kd)=\sum_{t\in\mathbb{Z}_m}R(t)R(\lambda t)
=\sum_{a,b,t\in\mathbb{Z}_m} f(a)f(a+t)f(b)f(b+\lambda t).$$ To make the non-negativity explicit, use the bijective change of variables $(a,b,t)\mapsto(a,c,u)$ given by $c=a+t$ and $u=b-\lambda a$. Then $b=u+\lambda a$ and $b+\lambda t=u+\lambda c$, so the last sum becomes $$\sum_{u,a,c\in\mathbb{Z}_m} f(a)f(c)f(u+\lambda a)f(u+\lambda c)
=\sum_{u\in\mathbb{Z}_m}\left(\sum_{a\in\mathbb{Z}_m}f(a)f(u+\lambda a)\right)^2\geq 0.$$ ◻
:::
