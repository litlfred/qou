---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-005-6-finding-a-genuine-integer-progression
section_title: "Finding a genuine integer progression"
section_number: 6
pages: 6-9
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.984
---
We now show how to pass from a density increment on a modular progression to one on a genuine integer progression.

::: lemma
[]{#lem:rect label="lem:rect"} Suppose $d\in\mathbb{Z}_m^\times$ and $x\in\mathbb{Z}_m$ satisfy $\sum_{i=0}^{\ell-1}f(x+id)\geq\eta\ell$ for some $0<\eta\leq1$. If $\ell\gtrsim\eta^{-2}$, then there is an arithmetic progression $P\subset[N]$ such that $$\lvert P\rvert\gtrsim\eta\sqrt{\ell}
\qquad\text{and}\qquad
\frac{\lvert A\cap P\rvert}{\lvert P\rvert}\geq\alpha+c\eta$$ for an absolute constant $c>0$.
:::

::: proof
*Proof.* We find a short subprogression of the original progression whose step is represented by a small integer, then intersect it with $[N]$.

Apply the pigeonhole principle to the $\lfloor\sqrt{\ell}\rfloor+1$ elements $0,d,2d,\ldots,\lfloor\sqrt{\ell}\rfloor d$ in $\mathbb{Z}_m$: two of these have a difference represented by an integer of size $\lesssim m/\sqrt{\ell}$. Hence there is an integer $q$, with $1\le q\le\sqrt{\ell}$, such that $qd$ is represented by an integer $s$ with $\lvert s\rvert\lesssim m/\sqrt{\ell}$. Since $m\sim N$, after enlarging the absolute constant in $\ell\gtrsim\eta^{-2}$, we may assume $\lvert s\rvert<N$.

Taking every $q$th term of the original progression gives $q$ subprogressions, each with step represented by $s$. Divide each of these into consecutive progressions of length $K\sim\sqrt{\ell}$, choosing the implicit constant in $K$ small enough that each subprogression has length at least $K$ and every progression travels distance $<m/10$ before reduction modulo $m$. Merging any incomplete final progression into its predecessor, we may assume every progression has length $\sim\sqrt{\ell}$. These progressions still partition the original $\ell$ terms. Since the original average of $f$ is at least $\eta$, one block $\widetilde P$ satisfies $$\sum_{u\in\widetilde P} f(u)\geq \eta\lvert\widetilde P\rvert.$$

It remains to intersect $\widetilde P$ with $[N]$. On the integer line, the copies of $[N]$ modulo $m$ are separated by gaps of length $m-N>3m/4$, while $\widetilde P$ travels distance $<m/10$. Thus $\widetilde P$ cannot meet $[N]$, leave $[N]$, and later meet $[N]$ again. Hence the terms of $\widetilde P$ lying in $[N]$ form one consecutive subprogression; call it $P$. Since $f=0$ outside $[N]$, passing from $\widetilde P$ to $P$ does not change the sum of $f$. As $f\leq1$, we get $\lvert P\rvert\geq\eta\lvert\widetilde P\rvert\gtrsim\eta\sqrt{\ell}$, and the average of $f$ on $P$ is at least $\eta$. Finally, $P$ is an ordinary integer arithmetic progression: all its terms lie in $[N]$, and its step is represented by the integer $s$ with $\lvert s\rvert<N$. Since $f=\mathbf{1}_A-\alpha$ on $[N]$, $$\frac{\lvert A\cap P\rvert}{\lvert P\rvert}
    =\alpha+\frac{1}{\lvert P\rvert}\sum_{u\in P}f(u)
    \geq \alpha+\eta.$$ This completes the proof. ◻
:::

Combining this with Lemma [\[lem:energy\]](#lem:energy){reference-type="ref" reference="lem:energy"} gives the following density increment.

::: proposition
[]{#prop:increment label="prop:increment"} Let $A\subset[N]$ have density $\alpha$, and suppose that $A$ contains no nontrivial three-term arithmetic progression. If $N\gtrsim\alpha^{-32}$, then there is an arithmetic progression $P\subset[N]$ such that $$\lvert P\rvert\gtrsim\alpha^{16}N^{1/2}
\qquad\text{and}\qquad
\frac{\lvert A\cap P\rvert}{\lvert P\rvert}\geq\alpha+c\alpha^{11}.$$
:::

::: proof
*Proof.* By Lemma [\[lem:energy\]](#lem:energy){reference-type="ref" reference="lem:energy"}, $\mathcal E(f)\gtrsim\alpha^{12}m^3$. Put $\beta\sim\alpha^{12}$ and choose $\ell\sim\beta m/\alpha^2\sim\alpha^{10}m$. The hypothesis $N\gtrsim\alpha^{-32}$ ensures that such an integer $\ell$ satisfies $1\leq\ell<m/2$. Lemma [\[lem:modular\]](#lem:modular){reference-type="ref" reference="lem:modular"} gives $d\in\mathbb{Z}_m^\times$ and $x\in\mathbb{Z}_m$ with $\sum_{i=0}^{\ell-1}f(x+id)\gtrsim \alpha^{11}\ell$. Set $\eta\sim\alpha^{11}$. Again using $N\gtrsim\alpha^{-32}$, we have $\ell\gtrsim\eta^{-2}$. Lemma [\[lem:rect\]](#lem:rect){reference-type="ref" reference="lem:rect"} gives an arithmetic progression $P\subset[N]$ with density increment $\gtrsim\alpha^{11}$ and length $$\lvert P\rvert\gtrsim \eta\sqrt{\ell}\gtrsim \alpha^{11}\alpha^5m^{1/2}
\gtrsim \alpha^{16}N^{1/2}.$$ ◻
:::

# Proof of Roth's theorem and the quantitative bound

::: proof
*Proof of Theorem [\[thm:roth\]](#thm:roth){reference-type="ref" reference="thm:roth"}.* Fix $\alpha_0>0$ and suppose, for contradiction, that there are arbitrarily large $N$ and 3AP-free sets $A\subset[N]$ with $\lvert A\rvert\geq\alpha_0N$. Applying Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}, then rescaling the progression it gives back to an interval, produces a new 3AP-free set with density increased by at least $c\alpha_0^{11}$. Repeating this, the density exceeds $1$ after $O(\alpha_0^{-11})$ steps.

It remains only to ensure that the iteration can be run for that many steps. At each step the ambient length is replaced by a progression of length at least $c\alpha_0^{16}N_j^{1/2}$. Since the number of steps depends only on $\alpha_0$, choosing the original $N$ sufficiently large in terms of $\alpha_0$ keeps every intermediate interval above the threshold in Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}. This contradiction proves the theorem. ◻
:::

A more careful analysis gives an explicit double-logarithmic bound.

::: corollary
[]{#cor:quantitative label="cor:quantitative"} There is an absolute constant $C>0$ such that $$r_3(N)\leq C\frac{N}{(\log\log N)^{1/11}}$$ for all sufficiently large $N$.
:::

::: proof
*Proof.* Let $A\subset[N]$ be 3AP-free, and write $\alpha=\lvert A\rvert/N$. Set $J=\lfloor c_0\alpha^{-11}\rfloor$, where $c_0>0$ is a sufficiently small absolute constant. If the density increment can be applied $J$ times, then each step increases the density by at least $c\alpha^{11}$, since the densities only increase. After $J$ steps the density would exceed $1$, which is impossible.

It remains to check that the lengths stay large enough for $J$ steps. At each step, after rescaling the subprogression back to an interval, Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"} gives $$\alpha_{j+1}\geq \alpha_j+c\alpha_j^{11},
        \qquad
        N_{j+1}\geq c\alpha_j^{16}N_j^{1/2}.$$ Since $\alpha_j\geq\alpha$, the length estimate implies $$\log N_{j+1}\geq \frac12\log N_j-C\log(e/\alpha).$$ Iterating this crude bound gives $$\log N_j\geq 2^{-j}\log N-C\log(e/\alpha).$$ Thus, if $\log N\geq C2^J\log(e/\alpha)$, then every $N_j$ with $j\leq J$ remains larger than a fixed power of $\alpha^{-1}$, and in particular remains above the threshold required by Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}. Since $J\sim\alpha^{-11}$, this condition follows from $$\log\log N\geq C\alpha^{-11},$$ after increasing $C$.

Therefore, if $\log\log N$ were larger than a sufficiently large constant times $\alpha^{-11}$, the iteration could run for $J$ steps and force the density above $1$. Hence $\log\log N\lesssim\alpha^{-11}$, so $\alpha\lesssim(\log\log N)^{-1/11}$. Since $\alpha=\lvert A\rvert/N$, this gives $$r_3(N)\lesssim \frac{N}{(\log\log N)^{1/11}}.$$ This proves the corollary. ◻
:::
