---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-003-4-no-progressions-imply-large-energy
section_title: "No progressions imply large energy"
section_number: 4
pages: 3-4
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.961
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
For functions $f_1,f_2,f_3\colon\mathbb{Z}_m\to\mathbb R$, define $$\Lambda(f_1,f_2,f_3):=\sum_{x,r\in\mathbb{Z}_m} f_1(x)f_2(x+r)f_3(x+2r).$$ If $A\subset [N]\subset\mathbb{Z}_m$, then $\Lambda(\mathbf{1}_A,\mathbf{1}_A,\mathbf{1}_A)$ is the number of three-term arithmetic progressions in $A$, including the trivial progressions with $r=0$. Hence, if $A$ contains no nontrivial three-term progressions, then $\Lambda(\mathbf{1}_A,\mathbf{1}_A,\mathbf{1}_A)=\lvert A\rvert$. On the other hand, $\Lambda(\mathbf{1}_{[N]},\mathbf{1}_{[N]},\mathbf{1}_{[N]})\gtrsim N^2$, since $[N]$ contains $\gtrsim N^2$ three-term progressions.

::: lemma
[]{#lem:lambda-energy label="lem:lambda-energy"} Let $g_1,g_2,g_3\colon\mathbb{Z}_m\to\mathbb R$ be bounded in absolute value by an absolute constant. Then $$\lvert\Lambda(g_1,g_2,g_3)\rvert^4
        \lesssim m^5\min_{1\leq i\leq3}\mathcal E(g_i).$$
:::

::: proof
*Proof.* It suffices to prove the following estimate. Let $F,h_1,h_2\colon\mathbb{Z}_m\to\mathbb R$, with $h_1,h_2$ bounded, and let $a,b\in\mathbb{Z}_m^\times$ with $a\neq b$. Then $$\left|\sum_{y,r\in\mathbb{Z}_m}F(y)h_1(y+ar)h_2(y+br)\right|^4
        \lesssim m^5\mathcal E(F).$$ The three possible choices of the distinguished slot in $\Lambda$ are obtained, after a change of variables, from this estimate by taking $(a,b)=(1,2)$, $(-1,1)$, and $(-2,-1)$.

Let $T$ denote the sum inside the fourth-power. Put $\lambda=ba^{-1}$ and change variables from $r$ to $u=y+ar$. Then $$T=\sum_{y,u\in\mathbb{Z}_m}F(y)h_1(u)h_2((1-\lambda)y+\lambda u).$$ By Cauchy--Schwarz in $u$, $$\lvert T\rvert^2\lesssim m\sum_{u\in\mathbb{Z}_m}
\left|\sum_{y\in\mathbb{Z}_m}F(y)h_2((1-\lambda)y+\lambda u)\right|^2.$$ Expanding the square, then putting $t=y'-y$ and $z=(1-\lambda)y+\lambda u$, gives $$\begin{aligned}
\lvert T\rvert^2
&\lesssim m\sum_{t\in\mathbb{Z}_m}
\left(\sum_{y\in\mathbb{Z}_m}F(y)F(y+t)\right) \\
&\qquad\qquad\times
\left(\sum_{z\in\mathbb{Z}_m}h_2(z)h_2(z+(1-\lambda)t)\right).
\end{aligned}$$ A final Cauchy--Schwarz in $t$ gives $$\begin{aligned}
\lvert T\rvert^2
&\lesssim m\mathcal E(F)^{1/2}
\left(\sum_{t\in\mathbb{Z}_m}
\left(\sum_{z\in\mathbb{Z}_m}h_2(z)h_2(z+(1-\lambda)t)\right)^2
\right)^{1/2} \\
&\lesssim m^{5/2}\mathcal E(F)^{1/2},
\end{aligned}$$ using that $|h_2|\leq 1$. Squaring proves the estimate. Applying this with each $g_i$ as the distinguished function gives the minimum on the right. ◻
:::

::: lemma
[]{#lem:trilinear-discrepancy label="lem:trilinear-discrepancy"} Let $u,v\colon\mathbb{Z}_m\to\mathbb R$ be bounded in absolute value by an absolute constant, and put $f=u-v$. Then $$\lvert\Lambda(u,u,u)-\Lambda(v,v,v)\rvert^4\lesssim m^5\mathcal E(f).$$
:::

::: proof
*Proof.* We telescope one slot at a time: $$\begin{aligned}
\Lambda(u,u,u)-\Lambda(v,v,v)
&=\bigl(\Lambda(u,u,u)-\Lambda(v,u,u)\bigr)
 +\bigl(\Lambda(v,u,u)-\Lambda(v,v,u)\bigr)  \\
&\qquad
 +\bigl(\Lambda(v,v,u)-\Lambda(v,v,v)\bigr)  \\
&=\Lambda(f,u,u)+\Lambda(v,f,u)+\Lambda(v,v,f).
\end{aligned}$$ Each term is bounded by $m^{5/4}\mathcal E(f)^{1/4}$ by Lemma [\[lem:lambda-energy\]](#lem:lambda-energy){reference-type="ref" reference="lem:lambda-energy"}, since in each term the other two factors are bounded. The claim follows after raising to the fourth power. ◻
:::

::: lemma
[]{#lem:energy label="lem:energy"} If $A\subset[N]$ is 3AP-free and $N\gtrsim\alpha^{-3}$, then $$\mathcal E(f)\gtrsim\alpha^{12}m^3.$$
:::

::: proof
*Proof.* Put $u=\mathbf{1}_A$ and $v=\alpha\mathbf{1}_{[N]}$. Then $f=u-v$ and $\lvert u\rvert,\lvert v\rvert\leq1$. Since $A$ has no nontrivial three-term progressions, $\Lambda(u,u,u)=\lvert A\rvert=\alpha N$, while $\Lambda(v,v,v)=\alpha^3\Lambda(\mathbf{1}_{[N]},\mathbf{1}_{[N]},\mathbf{1}_{[N]})\gtrsim\alpha^3N^2$. If $N\gtrsim\alpha^{-3}$, then $\lvert\Lambda(u,u,u)-\Lambda(v,v,v)\rvert\gtrsim\alpha^3N^2$. Lemma [\[lem:trilinear-discrepancy\]](#lem:trilinear-discrepancy){reference-type="ref" reference="lem:trilinear-discrepancy"} therefore gives $\alpha^{12}N^8\lesssim m^5\mathcal E(f)$. Since $m\sim N$, this gives $\mathcal E(f)\gtrsim\alpha^{12}m^3$. ◻
:::
