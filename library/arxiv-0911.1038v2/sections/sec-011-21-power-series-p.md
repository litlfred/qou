---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-011-21-power-series-p
section_title: "Power series P"
section_number: 2.1
pages: 8-9
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.837
latex_coverage_ratio: 0.891
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
Following Goulden and Rattan [@GouldenRattan2007] we define

$$C(t)=\frac{1}{1-\sum_{i\geq 2}\mathcal{R}_i t^i} = 



\sum_{\mu} t^{|\mu|} l(\mu)!\ \mathcal{R}_\mu.$$ Let $D=t \frac{d}{dt}$

and define for $m\geq 1$

$$P_m(t)=-\frac{1}{m!}C(t)\big(D+m-2\big)C(t)\cdots
\big(D+1\big)C(t)DC(t).$$

For example, we have $$\begin{aligned}
\nonumber P_1(t)&=-C(t),\\ 
\nonumber P_2(t)&=-\frac{1}{2}C(t)DC(t),\\
\nonumber

P_3(t)&
=-\frac{1}{6}
C(t)(D+1)C(t)DC(t) \\
\nonumber &= -\frac{1}{6}\left[C(t)DC(t)DC(t) + C(t)^2DC(t)\right] \\
\nonumber &= 
-\frac{1}{6}
\left[C(t)D\big(C(t)\cdot DC(t)\big) + C(t)^2DC(t)\right] \\
\nonumber &=
-\frac{1}{6}\left[C(t)\big(DC(t)\big)^2+C(t)^2D^2C(t)+C(t)^2DC(t)\right] .
\end{aligned}$$ Finally, for a partition $\lambda$, we write $P_{\lambda}(t)=\prod_{j=1}^{l(\lambda)} P_{\lambda_j}(t)$.

For $p = (p_0,\dots,p_l) \in \mathbb{N}^{l+1}$ we define

$$E(p) := C(t)^{p_0} D C(t)^{p_1} \cdots D C(t)^{p_l}.$$

::: lemma
[]{#lem:admissible label="lem:admissible"}  

1.  []{#admissible:A label="admissible:A"} Let $p \in \mathbb{N}^{l+1}, q \in \mathbb{N}^{m+1}$ and denote by $|p| := p_0 + \cdots + p_l$ ($|q| = q_0 + \cdots q_m$ respectively). Then $$E(p)\cdot E(q) = \sum_{\substack{r \in \mathbb{N}^{l+m+1}, \\ |r| = |p|+|q|}}c^{p,q}_r
    E(r),$$ where $c^{p,q}_r \in \mathbb{Z}$.

2.  []{#admissible:B label="admissible:B"} For any partition $\lambda$ the fraction $\frac{P_{\lambda}(t)}{C(t)}$ is a linear combination of terms $E(p)$ where $p \in \mathbb{N}^k$ such that $|p| =
    |\lambda|-1$ and $k \leq| \lambda|-l(\lambda)+1$.
:::

::: proof
*Proof.* Let $p = (p_0,\dots,p_l) \in \mathbb{N}^{l+1}$, $q = (q_0,\dots,q_m) \in \mathbb{N}^{m+1}$. We will show part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"} by induction on $l$. It is obvious for $l = 0$. For $l = 1$

we have: $$E(p)\cdot E(q) = E(p_0,p_1 + q_0, q_1,q_2,\dots,q_m) -
E(p_0+p_1,q_0,q_1,\dots,q_m)$$

by the Leibniz rule. Let us assume, that the inductive assertion holds for some $l \geq 1$ and let $p =
(p_0, \dots,p_{l+1})$. Then by the Leibniz rule we have that $$\label{leibnizA}
E(p)\cdot E(q) = C(t)^{p_0}D \left[ E(p')\cdot E(q)\right] -
C(t)^{p_0+p_1}\left[ E(p'')\cdot E(q')\right],$$ where $p' = (p_1,\dots,p_{l+1})$, $p'' = (0,p_2,\dots,p_{l+1})$, $q' =
(0,q_0,\dots,q_m)$.

By the inductive assertion, the right hand side of [\[leibnizA\]](#leibnizA){reference-type="eqref" reference="leibnizA"} is equal to $$\sum_{\substack{\alpha \in \mathbb{N}^{l+m+1}, \\ |\alpha| = |p|+|q|-p_0}} c_\alpha
C(t)^{p_0} D
E(\alpha) - \sum_{\substack{ \beta \in \mathbb{N}^{l+m+2}, \\|\beta| = |p|+|q|}}c_\beta
E(\beta),$$ where $c_\alpha,c_\beta \in \mathbb{Z}$. But it means that $$E(p)\cdot E(q) = \sum_{\substack{r \in \mathbb{N}^{l+m+2}, \\|r| = |p|+|q|}} c^{p,q}_r
E(r),$$ where $c^{p,q}_r \in \mathbb{Z}$ which finishes the proof of part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"}.

For part [\[admissible:B\]](#admissible:B){reference-type="ref" reference="admissible:B"} we notice that each function $P_m(t)$ is a linear combination of $E(p)$, where $p \in \mathbb{N}^k, |p| = m$ and $k \leq m-1$ and we apply part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"}. ◻
:::
