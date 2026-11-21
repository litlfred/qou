---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-004-5-large-energy-implies-a-modular-density-increme
section_title: "Large energy implies a modular density increment"
section_number: 5
pages: 4-6
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.927
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
Our next goal is to find a long modular progression on which $f$ has positive average. For an integer $1\leq \ell<m/2$ and a step $d\in\mathbb{Z}_m$, set $$S_d(x):=\sum_{i=0}^{\ell-1}f(x+id),\qquad V_d:=\sum_{x\in\mathbb{Z}_m}\lvert S_d(x)\rvert^2.$$ Thus $S_d(x)$ is the sum of $f$ on the length-$\ell$ modular progression starting at $x$ with step $d$, and $V_d$ is the second moment of these sums as $x$ varies.

::: lemma
[]{#lem:v-identity label="lem:v-identity"} For every $d\in\mathbb{Z}_m$, $$\label{eq:v-identity}
V_d=\sum_{\lvert h\rvert<\ell}(\ell-\lvert h\rvert)R(hd).$$ Also $$\label{eq:v-first-moment}
\sum_{d\in\mathbb{Z}_m}V_d\leq \alpha\ell m^2.$$ Finally, if $\mathcal E(f)\geq\beta m^3$ and $\ell\lesssim \beta m/\alpha^2$, then $$\label{eq:v-second-moment-nonzero}
\sum_{d\in\mathbb{Z}_m^\times}V_d^2\gtrsim \beta\ell^3m^3.$$
:::

::: proof
*Proof.* We first prove [\[eq:v-identity\]](#eq:v-identity){reference-type="eqref" reference="eq:v-identity"}. Expanding the square gives $$V_d = \sum_{x\in\mathbb Z_m}\left(\sum_{i=0}^{\ell-1}f(x+id)\right)^2
 = \sum_{0\leq i,j<\ell}\sum_{x\in\mathbb Z_m}f(x+id)f(x+jd)$$

$$= \sum_{0\leq i,j<\ell}\sum_{y\in\mathbb Z_m}f(y)f(y+(j-i)d)
 = \sum_{0\leq i,j<\ell} R((j-i)d) = \sum_{|h|<\ell}(\ell-|h|)R(hd).$$ Here we used the change of variables $y=x+id$ and then used that there are $\ell-|h|$ pairs $(i,j)$ satisfy $0\leq i<\ell$ and $0\leq i+h<\ell$ such that $h=j-i$. This proves [\[eq:v-identity\]](#eq:v-identity){reference-type="eqref" reference="eq:v-identity"}.

Now we sum [\[eq:v-identity\]](#eq:v-identity){reference-type="eqref" reference="eq:v-identity"} over $d\in\mathbb{Z}_m$. The term $h=0$ contributes $\ell mR(0)$. If $h\neq0$, then $d\mapsto hd$ is a bijection on $\mathbb{Z}_m$, so $$\sum_{d\in\mathbb{Z}_m}R(hd)=\sum_{t\in\mathbb{Z}_m}R(t)=\left(\sum_{x\in\mathbb{Z}_m}f(x)\right)^2=0.$$ Therefore $\sum_{d\in\mathbb{Z}_m}V_d=\ell mR(0)$. Since $R(0)=\sum_{x\in\mathbb{Z}_m}f(x)^2\leq \alpha m$, this proves [\[eq:v-first-moment\]](#eq:v-first-moment){reference-type="eqref" reference="eq:v-first-moment"}.

It remains to prove [\[eq:v-second-moment-nonzero\]](#eq:v-second-moment-nonzero){reference-type="eqref" reference="eq:v-second-moment-nonzero"}. Squaring [\[eq:v-identity\]](#eq:v-identity){reference-type="eqref" reference="eq:v-identity"} and summing over $d\in\mathbb{Z}_m$ gives $$\sum_{d\in\mathbb{Z}_m}V_d^2=
\sum_{\lvert h\rvert,\lvert k\rvert<\ell}(\ell-\lvert h\rvert)(\ell-\lvert k\rvert)
\sum_{d\in\mathbb{Z}_m}R(hd)R(kd).$$ By Lemma [\[lem:pos\]](#lem:pos){reference-type="ref" reference="lem:pos"}, every term with $h,k\neq0$ is nonnegative. Terms with exactly one of $h,k$ equal to $0$ vanish by the preceding discussion. Thus we may obtain a lower bound by considering just the diagonal terms $h=k\neq0$. For $h \neq 0$, multiplication by $h$ is a bijection on $\mathbb{Z}_m$, so $\sum_{d\in\mathbb{Z}_m}R(hd)^2=\mathcal E(f)$. Hence $$\sum_{d\in\mathbb{Z}_m}V_d^2\geq \sum_{0<\lvert h\rvert<\ell}(\ell-\lvert h\rvert)^2\mathcal E(f)
\gtrsim \ell^3\mathcal E(f)\geq \beta\ell^3m^3.$$ This still includes the zero step. For $d=0$, we have $S_0(x)=\ell f(x)$, and therefore $V_0=\ell^2\sum_{x\in\mathbb{Z}_m}f(x)^2\leq \alpha\ell^2m$, so $V_0^2\leq \alpha^2\ell^4m^2$. The assumption $\ell\lesssim \beta m/\alpha^2$, with the implicit constant chosen small enough, makes this smaller than a fixed fraction of $\beta\ell^3m^3$. Removing the zero step gives [\[eq:v-second-moment-nonzero\]](#eq:v-second-moment-nonzero){reference-type="eqref" reference="eq:v-second-moment-nonzero"}. ◻
:::

::: lemma
[]{#lem:modular label="lem:modular"} Assume $\mathcal E(f)\geq\beta m^3$, with $0<\beta\lesssim\alpha^2$, and choose an integer $\ell$ satisfying $$\ell\sim \frac{\beta m}{\alpha^2},\qquad 1\leq \ell<m/2,$$ where the implicit constant is chosen small enough. Then there exist $d\in\mathbb{Z}_m^\times$ and $x\in\mathbb{Z}_m$ such that $$\label{eq:modular-increment}
S_d(x)=\sum_{i=0}^{\ell-1} f(x+id)\gtrsim \frac{\beta}{\alpha}\ell.$$
:::

::: proof
*Proof.* Set $M=\max_{d\in\mathbb{Z}_m^\times}V_d$. By [\[eq:v-second-moment-nonzero\]](#eq:v-second-moment-nonzero){reference-type="eqref" reference="eq:v-second-moment-nonzero"} and [\[eq:v-first-moment\]](#eq:v-first-moment){reference-type="eqref" reference="eq:v-first-moment"}, $$\beta\ell^3m^3\lesssim \sum_{d\in\mathbb{Z}_m^\times}V_d^2
\leq M\sum_{d\in\mathbb{Z}_m}V_d\leq M\alpha\ell m^2.$$ Thus there is a nonzero step $d$ with $$\label{eq:large-vd}
V_d\gtrsim \frac{\beta}{\alpha}\ell^2m.$$

We now extract a large positive value of $S_d(x)$. Since $\lvert S_d(x)\rvert\leq\ell$ for every $x\in\mathbb{Z}_m$, the definition of $V_d$ gives $V_d\leq \ell\sum_{x\in\mathbb{Z}_m}\lvert S_d(x)\rvert$. Using [\[eq:large-vd\]](#eq:large-vd){reference-type="eqref" reference="eq:large-vd"}, we get $$\sum_{x\in\mathbb{Z}_m}\lvert S_d(x)\rvert\gtrsim \frac{\beta}{\alpha}\ell m.$$ Also $\sum_{x\in\mathbb{Z}_m}S_d(x)=\ell\sum_{x\in\mathbb{Z}_m}f(x)=0$. Therefore the total positive mass of $S_d$ is exactly half of $\sum_{x\in\mathbb{Z}_m}\lvert S_d(x)\rvert$, and hence some $x\in\mathbb{Z}_m$ satisfies [\[eq:modular-increment\]](#eq:modular-increment){reference-type="eqref" reference="eq:modular-increment"}. ◻
:::
