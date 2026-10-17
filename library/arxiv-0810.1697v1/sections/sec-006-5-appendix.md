---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA"
section_id: sec-006-5-appendix
section_title: "Appendix"
section_number: 5
pages: 12-14
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.857
doc_brief: "ON THE CABLE EXPANSION FORMULA — In this paper, a generalized version of Morton’s formula [8] is proved."
---
[]{#apendix label="apendix"} []{#appendix label="appendix"} Now we will present a proof of lemma 3 and lemma 4.

::: proof
*Proof of lemma 3.* By change of variables, we have $$\sum_{k\ge 0}f(k+1)g(k+1)\delta(k-t-pk')=\sum_{k^{''}\ge 1}f(k^{''})g(k^{''})\delta(k^{''}-t-1-pk')$$ and $$\begin{aligned}
\sum_{k\ge 0}f(k+1)g(k+1)\delta(k+t+2+pk')&=\sum_{k^{''}\ge 1}f(k^{''})g(k^{''})\delta(k^{''}+t+1+pk')\notag\\
&=\sum_{k^{''}\le -1}f(-k^{''})g(-k^{''})\delta(-k^{''}+t+1+pk')\notag\\
&=-\sum_{k^{''}\le -1}f(k^{''})g(k^{''})\delta(k^{''}-t-1-pk')\notag
\end{aligned}$$ So $$\begin{aligned}
&\sum_{k\ge 0}f(k+1)g(k+1)\{\delta(k-t-pk')-\delta(k+t+2+pk')\}\notag\\
                       &=\sum_{k^{''}\ne 0}f(k^{''})g(k^{''})\delta(k^{''}-t-1-pk')\notag\\
                       &=\sum_{k^{''}\in Z}f(k^{''})g(k^{''})\delta(k^{''}-t-1-pk')\notag\\
                       & since\ f(0)=0\notag\\
                       &=f(pk'+t+1)g(pk'+t+1)\notag
\end{aligned}$$ ◻
:::

::: proof
*Proof of lemma 4.* $$\begin{aligned}
&\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\sinh(\alpha_3k'+\zeta)\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')(\sinh(\alpha_3k')\cosh(\zeta)+\cosh(\alpha_3k')\sinh(\zeta))\notag
\end{aligned}$$

And $$\begin{aligned}
&\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\sinh(\alpha_3k')\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1(-k')^2-\alpha_2k')\sinh(-\alpha_3k')\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N -\exp(\alpha_1{k'}^2-\alpha_2k')\sinh(\alpha_3k')\notag\\
&=1/2\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2)\sinh(\alpha_3k')(\exp(\alpha_2k')-\exp(-\alpha_2k'))\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2)\sinh(\alpha_3k')\sinh(\alpha_2k')\notag
\end{aligned}$$

Apply this trick to $$\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\cosh(\alpha_3k')$$ we have $$\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\cosh(\alpha_3k')=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2)\cosh(\alpha_3k')\cosh(\alpha_2k')$$

So $$\begin{aligned}
&\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\sinh(\alpha_3k'+\zeta)\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2)(\sinh(\alpha_2k')\sinh(\alpha_3k')\cosh(\zeta)+\cosh(\alpha_2k')\cosh(\alpha_3k')\sinh(\zeta))\notag
\end{aligned}$$

In this expression, $\alpha_2$ and $\alpha_3$ are symmetric, and our formula follows. ◻
:::
