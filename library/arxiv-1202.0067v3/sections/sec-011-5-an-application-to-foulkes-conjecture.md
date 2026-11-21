---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-011-5-an-application-to-foulkes-conjecture
section_title: "An application to Foulkes' Conjecture"
section_number: 5
pages: 18-22
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.959
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
[]{#sec:Foulkes label="sec:Foulkes"}

For $m$, $n \in \mathbf{N}$, let $\phi^{(m^n)}$ be the permutation character of $S_{mn}$ acting on all unordered set partitions of $\{1,2,\ldots,mn\}$ into $n$ sets each of size $m$. Equivalently, $\phi^{(m^n)} = \mathop{\mathrm{Ind}}_{S_m \wr S_n}^{S_{mn}} 1$. Foulkes' Conjecture asserts that if $m \le n$ then $$\left< \phi^{(m^n)}, \chi^\lambda \right> \ge 
\left< \phi^{(n^m)}, \chi^\lambda \right>$$ for all partitions $\lambda$ of $mn$. Equivalent formulations of Foulkes' Conjecture exist in the language of general linear groups, symmetric polynomials, and geometric invariant theory. Despite having been attacked from all these directions (and more), it has only been proved when $m \le 4$ (see [@DentSiemons] and [@McKay]), asymptotically when $n$ is very large compared to $m$ (see [@Brion page 352]) and, in a computational result of Müller and Neunhöffer [@MN], when $m+n \le 17$. For further background, and some recent results on the constituents of $\phi^{(m^n)}$, we refer the reader to [@PagetWildon] and [@Giannelli].

In this section we use character deflations to prove a new recursive formula for the character multiplicities in Foulkes' Conjecture. Firstly, using Frobenius reciprocity, then the inflation-deflation reciprocity relation $$\label{eq:reciprocity}
\left< \mathop{\mathrm{Def}}_{S_n} \psi, \chi  \right> = 
\left< \psi, \mathop{\mathrm{Inf}}_{S_n}^{S_m \wr S_n} \!\chi  \right>,$$ where $\psi$ is a character of $S_m \wr S_n$ and $\chi$ is a character of $S_n$, we observe that $$\left< \phi^{(m^n)}, \chi^\lambda \right> = 
\left< \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda} ,  1_{S_n} \right>.$$

::: proposition
[]{#prop:Foulkes label="prop:Foulkes"} Let $m$, $n \in \mathbf{N}$. If $\lambda$ is a partition of $mn$ then $$\left< \phi^{(m^n)}, \chi^\lambda \right>
 = \displaystyle\frac1{n} \displaystyle\sum_{\ell=1}^n \displaystyle\sum_{\mu}
\varepsilon_\ell(\lambda / \mu) 
\left< \phi^{(m^{n-\ell})}, \chi^\mu \right>$$ where the second sum is over all partitions $\mu$ of $\ell m$ such that there exists an $m$-border strip tableau of shape $\lambda / \mu$ and type $(\ell)$.
:::

::: proof
*Proof.* We have seen that $$\left< \phi^{(m^n)}, \chi^\lambda \right> = 
\left< \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda} ,  1_{S_n} \right>=\displaystyle\frac1{n!} \displaystyle\sum_{g \in S_n} (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda}) (g).$$ We may write each $g \in S_n$ as a product of an $\ell$-cycle containing the letter $1$ and some $h \in S_{n - \ell}$ acting on the remaining letters. The number of possible such $\ell$-cycles is $(n-1)!/ (n-\ell)!$, hence $$\left< \phi^{(m^n)}, \chi^\lambda \right> = \displaystyle\frac1{n!}  \displaystyle\sum_{\ell =1}^n \displaystyle\frac{(n-1)!}{(n-\ell)!} \displaystyle\sum_{h \in S_{n-\ell}} (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda}) (xh)$$ where $x$ is the $\ell$-cycle $(1 \, 2 \, \ldots \, \ell)$. We now apply Proposition [\[prop:defres_decomp\]](#prop:defres_decomp){reference-type="ref" reference="prop:defres_decomp"} to see that $$\left< \phi^{(m^n)}, \chi^\lambda \right> =
 \displaystyle\frac1{n}  \displaystyle\sum_{\ell =1}^n \displaystyle\frac1{(n-\ell)!} \displaystyle\sum_{h \in S_{n-\ell}} 
\displaystyle\sum_{\mu} (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_\ell} \chi^{\lambda/\mu}) (x)
 (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{n-\ell}} \chi^{\mu}) (h),$$ where the sum is over partitions $\mu \subseteq \lambda$ with $|\lambda /\mu|=m \ell$. Since $x$ is an $\ell$-cycle, Proposition [\[prop:basecase\]](#prop:basecase){reference-type="ref" reference="prop:basecase"} shows that $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_\ell} \chi^{\lambda/\mu}) (x)$ is $\varepsilon_\ell(\lambda/\mu)$ if there exists an $m$-border strip tableau of shape $\lambda / \mu$ and type $(\ell)$ and is zero otherwise. Thus $$\begin{aligned}
\left< \phi^{(m^n)}, \chi^\lambda \right>& =&
 \displaystyle\frac1{n}  \displaystyle\sum_{\ell =1}^n 
\displaystyle\sum_{\mu}   \varepsilon_\ell(\lambda/\mu)
\displaystyle\frac1{(n-\ell)!} \displaystyle\sum_{h \in S_{n-\ell}} 
 (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{n-\ell}} \chi^{\mu}) (h) \\  & =& 
 \displaystyle\frac1{n}  \displaystyle\sum_{\ell =1}^n 
\displaystyle\sum_{\mu}   \varepsilon_\ell(\lambda/\mu)
 \left< \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{n-\ell}} \chi^{\mu} ,  1_{S_{n-\ell}} \right>\\
&=&  \displaystyle\frac1{n} \displaystyle\sum_{\ell=1}^n \displaystyle\sum_{\mu}
\varepsilon_\ell(\lambda / \mu) 
\left< \phi^{(m^{n-\ell})}, \chi^\mu \right>
\end{aligned}$$ where, in each case, the second sum is over all partitions $\mu \subseteq \lambda$ for which there exists an $m$-border strip tableau of shape $\lambda / \mu$ and type $(\ell)$. ◻
:::

Proposition [\[prop:Foulkes\]](#prop:Foulkes){reference-type="ref" reference="prop:Foulkes"} gives an algorithm for testing Foulkes' Conjecture for a single character $\chi^{\lambda}$ of $S_{mn}$ that is far faster than more direct methods, such as those requiring the character values of $\phi^{(m^n)}$ and $\phi^{(n^m)}$ to be calculated on all partitions of $mn$. Timings suggest that it can be significantly faster than the algorithm used by symmetrica [@Kerber], although some of this gain comes at the expense of increased use of memory. For example, to calculate all the multiplicities $\langle \phi^{(6^{11})}, \chi^\lambda \rangle$ for $\lambda$ a partition of $66$ takes $34$ minutes using the Haskell [@PeytonJones] implementation of Proposition [\[prop:Foulkes\]](#prop:Foulkes){reference-type="ref" reference="prop:Foulkes"} available from the third author's website[^1], compared to $350$ minutes for symmetrica using the function `COMPLETE_COMPLETE_PLET`, both running on the same machine.

The graphs in Figures [1](#fig:FoulkesGraph){reference-type="ref" reference="fig:FoulkesGraph"} and [2](#fig:FoulkesGraphsComp){reference-type="ref" reference="fig:FoulkesGraphsComp"} show a number of intriguing features of the character multiplicities appearing in Foulkes' Conjecture. In particular, it seems plausible that if Foulkes' Conjecture is false, then a counterexample occurs when $m$ is near to $n$ and the relevant partition is either very large or very small in the lexicographic order on partitions of $mn$ with at most $n$ parts.

<figure id="fig:FoulkesGraph">

<figcaption>The left-hand graph shows <span class="math inline">log<sub>2</sub>⟨<em>ϕ</em><sup>(7<sup>8</sup>)</sup>,<em>χ</em><sup><em>λ</em></sup>⟩</span> for all partitions of <span class="math inline">56</span> with at most <span class="math inline">8</span> parts. Partitions are ordered lexicographically, with the smallest partition <span class="math inline">(7<sup>8</sup>)</span> at the far right. If the multiplicity is zero then the point is placed below the <span class="math inline"><em>x</em></span> axis. Vertical lines separate partitions with equal largest parts. The right-hand graph shows an enlarged view of the multiplicities for partitions with first part <span class="math inline">19</span>; the range of these partitions is indicated by the arrow in the left-hand graph.</figcaption>
</figure>

<figure id="fig:FoulkesGraphsComp">
<div class="picture">
<p>(10,16) (-0.75,8) (-0.75,.2)</p>
</div>
<figcaption>The top graph shows <span class="math inline">log<sub>2</sub>&lt;<em>ϕ</em><sup>(7<sup>8</sup>)</sup>, <em>χ</em><sup><em>λ</em></sup>&gt; − log<sub>2</sub>&lt;<em>ϕ</em><sup>(8<sup>7</sup>)</sup>, <em>χ</em><sup><em>λ</em></sup>&gt;</span> for the partitions of <span class="math inline">56</span> with at most <span class="math inline">7</span> parts for which the smaller multiplicity is non-zero. To increase their visibility a small number of points have been enlarged. Partitions are ordered lexicographically, with the smallest partition <span class="math inline">(8<sup>7</sup>)</span> at the far right. The lower graph shows <span class="math inline">log<sub>2</sub>&lt;<em>ϕ</em><sup>(7<sup>8</sup>)</sup>, <em>χ</em><sup><em>λ</em></sup>&gt;</span> for those partitions for which <span class="math inline">&lt;<em>ϕ</em><sup>(8<sup>7</sup>)</sup>, <em>χ</em><sup><em>λ</em></sup>&gt; = 0</span>; if <span class="math inline">&lt;<em>ϕ</em><sup>(7<sup>8</sup>)</sup>, <em>χ</em><sup><em>λ</em></sup>&gt; = 0</span> then the point is drawn below the axis.</figcaption>
</figure>

Using symmetrica, Foulkes' Conjecture has been checked for all $m$ and $n$ with $m+n \le 17$ in [@MN]. Using Proposition [\[prop:Foulkes\]](#prop:Foulkes){reference-type="ref" reference="prop:Foulkes"} and the software already mentioned, we have extended this range. The relevant data is available from the third author's website.

::: corollary
[]{#cor:computation label="cor:computation"} If $m \le n$ and $m+n \le 19$

then $$\left< \phi^{(m^n)}, \chi^\lambda \right> \ge 
\left< \phi^{(n^m)}, \chi^\lambda \right>$$ for all partitions $\lambda$ of $mn$.0◻
:::

[^1]: See [www.ma.rhul.ac.uk/\~uvah099/](www.ma.rhul.ac.uk/~uvah099/){.uri}.
