---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-005-25-sign-sequences-and-hook-partitions
section_title: "Sign sequences and hook partitions"
section_number: 2.5
pages: 3-5
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.966
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
For $0 \le \ell \le n-1$, let $\lambda_\ell$ be the hook partition $(n-\ell, 1^\ell)$. We refer to $\ell$ as *leg length*.

::: lemma
[]{#sign seq label="sign seq"} Standard tableaux of shape $\lambda_\ell$ are in bijection with sign sequences $\varepsilon=(\varepsilon_1,\dots,\varepsilon_n)\in \{\pm\}^n$ such that $\varepsilon_1 = +$ and $\ell$ entries equal $-$.
:::

::: proof
*Proof.* Beginning with a standard $\lambda_\ell$-tableau, define $\varepsilon= (\varepsilon_1, \ldots, \varepsilon_n)$ by $$\varepsilon_r = \left\{ \begin {array} {l l}
+, \qquad & \text {if } r \text { appears on the first row} \\
-, \qquad & \text {otherwise}
\end {array} \right.$$ Notice that the box labeled 1 has to be in the corner of the hook, so $\varepsilon_1 = +$. Also, $\ell$ numbers are on the leg of the hook, so there are $\ell$ entries equal to $-$.

For the inverse, starting with a sign sequence $\varepsilon= (\varepsilon_1, \ldots, \varepsilon_n)$ with $\varepsilon_1=+$ and $\ell$ other entries equal to $-$, construct a standard tableau recursively, as follows. Place 1 in the corner of the diagram. Now, for each $r>1$, suppose that the numbers $1, \ldots, r-1$ have been placed. Either add $r$ to the end of the first row or at the bottom of the first column, according to whether $\varepsilon_r$ is $+$ or $-$, respectively. ◻
:::

Using this bijection, we can adapt the semi-normal representation to the combinatorics of sign sequences.

::: thm
[]{#signs irrep thm label="signs irrep thm"} The irreducible module $S(\lambda_\ell)$ has basis $\{x_{\varepsilon}\}$, where $\varepsilon$ runs over sign sequences having $\varepsilon_1=+$ and $\ell$ other entries equal to $-$. The generators $H_1, \ldots, H_{n-1}$ of $\mathcal{H}_n$ act by $$\label {signs s-n formula}
H_r x_\varepsilon= a_r(\varepsilon) x_\varepsilon+ b_r(\varepsilon) x_{s_r\varepsilon}$$ where $s_r \varepsilon$ denotes the sign sequence obtained from $\varepsilon$ by permuting $\varepsilon_r$ and $\varepsilon_{r+1}$, $x_\varepsilon$ is interpreted as zero if $\varepsilon_1 = -$, and $$\begin{aligned}
 \label {diag coeff}
a_r(\varepsilon) &= \left\{ \begin {array} {l l}
v &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (+, +) \\
-v^{-1} &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (-, -) \\
v^r / [r] &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (-, +) \\
-v^{-r} / [r] &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (+, -),
\end {array} \right.\\
\label {off-diag coeff}
b_r(\varepsilon) &= \left\{ \begin {array} {l l}
{[r+1] / [r]} &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (-, +) \\
{[r-1] / [r]} &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (+, -)\\
0&\qquad \text{otherwise.}
\end {array} \right.
\end{aligned}$$ The inverse generators $H_1^{-1}, \ldots, H_{n-1}^{-1}$ act by $$\label {newer}
H_r^{-1} x_\varepsilon= \bar a_r(\varepsilon) x_\varepsilon+ b_r(\varepsilon) x_{s_r\varepsilon}$$ where $\bar a_r(\varepsilon)$ is obtained from $a_r(\varepsilon)$ by replacing $v$ by $v^{-1}$.
:::

::: proof
*Proof.* This is just a translation of Theorem [\[irrep thm\]](#irrep thm){reference-type="ref" reference="irrep thm"} using the bijection from Lemma [\[sign seq\]](#sign seq){reference-type="ref" reference="sign seq"}. Given a sign sequence $\varepsilon\in \{\pm\}^n$ having $\varepsilon_1=+$ and $\ell$ other entries equal to $-$, construct the corresponding standard tableau, and let $(i_1,\dots,i_n)$ be its residue sequence. We have $i_1 = 0$, and for $1 \le r < n$, $$\label {sign to cont}
i_{r+1} = \left\{ \begin {array} {l l}
i_r + 1 &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (+, +) \\
i_r - 1 &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (-, -) \\
i_r + r &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (-, +) \\
i_r - r &\qquad \text {if } (\varepsilon_r, \varepsilon_{r+1}) = (+, -).
\end {array} \right.$$ Given this, the formulae ([\[diag coeff\]](#diag coeff){reference-type="ref" reference="diag coeff"})--([\[off-diag coeff\]](#off-diag coeff){reference-type="ref" reference="off-diag coeff"}) are easily deduced from ([\[abs\]](#abs){reference-type="ref" reference="abs"}). Finally the formula ([\[newer\]](#newer){reference-type="ref" reference="newer"}) is easily deduced from ([\[signs s-n formula\]](#signs s-n formula){reference-type="ref" reference="signs s-n formula"}) since $H_r^{-1} = H_r - (v-v^{-1})$. ◻
:::
