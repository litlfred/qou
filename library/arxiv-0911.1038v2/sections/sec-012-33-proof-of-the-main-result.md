---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-012-33-proof-of-the-main-result
section_title: "Proof of the main result"
section_number: 3.3
pages: 16-18
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.746
---
::: proof
*Proof of Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}.* We know by Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"} that for any integer $g\geq 1$ there exist inhomogeneous symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$, having maximal degree $4g$, such that $$\begin{aligned}
L_k := L'_k := k\ K_{k,k+1-2g} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}_g(\mu) \mathcal{Q}_\mu.
\end{aligned}$$ By applying Lemma [\[lem:sie-dzieli\]](#lem:sie-dzieli){reference-type="ref" reference="lem:sie-dzieli"} for $\Delta=0$ we obtain that $$\begin{aligned}
k\ K_{k,k+1-2g} &=  k\ \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}'_g(\mu) \mathcal{R}_\mu \\ 
 &= k\ \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h'}_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $\tilde{f}'_g, \tilde{h}'_g$ are symmetric functions of degree at most $4g-1$.

Let $$\begin{aligned}

L_k := L'_k := K_{k,k+1-2g} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}'_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}'_g(\mu) \mathcal{Q}_\mu.
\end{aligned}$$ Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}[\[lem:gal_a\]](#lem:gal_a){reference-type="ref" reference="lem:gal_a"} shows that Lemma [\[lem:sie-dzieli\]](#lem:sie-dzieli){reference-type="ref" reference="lem:sie-dzieli"} can be applied for $\Delta=0$, thus $$\begin{aligned}
K_{k,k+1-2g} &=  k\ \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}''_g(\mu) \mathcal{R}_\mu \\ 
 &= k\ \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}''_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $\tilde{f}''_g, \tilde{h}''_g$ are symmetric functions of degree at most $4g-2$.

Let $$\begin{aligned}
L_k := L'_k := \frac{A K_{k,k+1-2g}}{k} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! A\ \tilde{f}''_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}A\ \tilde{h}''_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $A$ is the common multiple of the denominators of coefficients of $\tilde{h}''_g$ and $\tilde{f}''_g$. We know that $L_{p-1} = L'_{p-1}$ has integer coefficients as polynomial in $R_2,R_3,\dots$ and we know, thanks to Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}[\[lem:gal_b\]](#lem:gal_b){reference-type="ref" reference="lem:gal_b"}, that for infinitely many prime numbers $p$ the coefficients of $(p-1)L_{p-1} = (p-1)L'_{p-1}$ are divisible by $p$, hence coefficients of $L_{p-1} = L'_{p-1}$ are also divisible by $p$, because $p-1$ and $p$ are coprime. Then we can apply Lemma [\[lem:sie-dzieli\]](#lem:sie-dzieli){reference-type="ref" reference="lem:sie-dzieli"} for $\Delta=-1$ and we obtain that there exist symmetric functions $\tilde{f}'''_g,
\tilde{h}'''_g$ of degree at most $4g-3$ such that $$\begin{aligned}
K_{k,k+1-2g} &=  k\ (k+1)\ \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}'''_g(\mu) \mathcal{R}_\mu \\ 
 &= k\ (k+1)\ \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}'''_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $\tilde{f}''_g, \tilde{h}''_g$ are symmetric functions of degree at most $4g-3$.

Similarly as before, thanks to Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}[\[lem:gal_c\]](#lem:gal_c){reference-type="ref" reference="lem:gal_c"} and thanks to the fact that for prime number $p>2$ the numbers $p$ and $p+1$ are coprime and the numbers $p+2$ and $p$ are coprime, we can apply Lemma [\[lem:sie-dzieli\]](#lem:sie-dzieli){reference-type="ref" reference="lem:sie-dzieli"} for $\Delta=1$ for $$\begin{aligned}
L_k := L'_k := \frac{B K_{k,k+1-2g}}{k(k+1)} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! B\ \tilde{f}'''_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}B\ \tilde{h}'''_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $B$ is the common multiple of the denominators of coefficients of $\tilde{h}'''_g$ and $\tilde{f}'''_g$ and we obtain that there exist symmetric functions $\tilde{f}''''_g,
\tilde{h}''''_g$ of degree at most $4g-4$ such that $$\begin{aligned}
K_{k,k+1-2g} &= (k-1)\ k\ (k+1)\ \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}''''_g(\mu) \mathcal{R}_\mu \\ 
 &= (k-1)\ k\ (k+1)\ \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}''''_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ which finishes the proof. ◻
:::
