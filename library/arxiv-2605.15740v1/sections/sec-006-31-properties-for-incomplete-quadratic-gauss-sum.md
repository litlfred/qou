---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-006-31-properties-for-incomplete-quadratic-gauss-sum
section_title: "Properties for incomplete quadratic Gauss sums"
section_number: 3.1
pages: 13-14
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.91
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
We begin with a general result on an incomplete quadratic Gauss sum. For simplicity, we write $\chi = \chi_{\bm{p}}^{\bm{\ell}}$. Recall that $P:=p_1 p_2 p_3$.

::: lemma
[]{#chiprop label="chiprop"} Assume that

1.  $P \equiv 2 \pmod{4}$,\

2.  if $\chi(n) \neq 0$, then $n$ is odd\

3.  $\chi$ is even modulo $P$, i.e., $\chi(P-n) = \chi(n)$.

If $q$ is a primitive $N$th root of unity, then $$2\sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}} =  \sum_{n=0}^{PN} \chi(n) q^{\frac{n^2}{4P}}.$$
:::

::: proof
*Proof.* We have $$\begin{aligned}
2\sum_{n=0}^{PN}& \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}} \nonumber \\
&= \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}} + \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}} \nonumber \\
&= \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}}  + \sum_{n=0}^{PN} \left(1-\frac{(PN-n)}{PN}\right) \chi(PN-n) q^{\frac{(PN-n)^2}{4P}} \nonumber \\
&= \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}}  + \sum_{n=0}^{PN} \frac{n}{PN} \chi(PN-n) q^{\frac{(P^2N^2 - 2nPN + n^2)}{4P}} \nonumber \\
&= \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}}  + \sum_{n=0}^{PN} \frac{n}{PN} q^{\frac{n^2}{4P}} \chi(PN-n) q^{\frac{N(PN - 2n)}{4}}. \label{tbc}
\end{aligned}$$ Consider the term $$\chi(PN-n) q^{\frac{N(PN - 2n)}{4}}.$$ We have two cases according to the parity of $N$. First, if $N$ is odd then since $P \equiv 2 \pmod{4}$ and $n$ is odd we have that $PN-2n$ is a multiple of $4$. Therefore $q^{\frac{N(PN - 2n)}{4}} = 1$. Moreover, by $(iii)$ we have $\chi(PN - n) =\chi(n)$. Hence $$\chi(PN-n) q^{\frac{N(PN - 2n)}{4}} = \chi(n).$$ If $N$ is even, then $PN-2n \equiv 2 \pmod{4}$ and so $q^{\frac{N(PN - 2n)}{4}} = -1$. Now since $N$ is even we have $\chi(PN - n) = -\chi(n)$. Once again, we find that $$\chi(PN-n) q^{\frac{N(PN - 2n)}{4}} = \chi(n).$$ Using this in [\[tbc\]](#tbc){reference-type="eqref" reference="tbc"} we have $$\begin{aligned}
2\sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}} &= \sum_{n=0}^{PN} \left(1-\frac{n}{PN}\right) \chi(n) q^{\frac{n^2}{4P}}  + \sum_{n=0}^{PN} \frac{n}{PN} q^{\frac{n^2}{4P}} \chi(n) \\
&= \sum_{n=0}^{PN} \chi(n) q^{\frac{n^2}{4P}},
\end{aligned}$$ as desired. ◻
:::

::: remark
[]{#chiproprmk label="chiproprmk"} Note that (i) and (ii) in Lemma [\[chiprop\]](#chiprop){reference-type="ref" reference="chiprop"} are satisfied for all of the functions $\chi_{\bm{p}}^{\bm{\ell}}$ considered in Theorem [\[main\]](#main){reference-type="ref" reference="main"}. Moreover, $p_1 = 2$ and so by [@hikami3 (3.8)] the involution $\sigma_1$ fixes $\bm{\ell} = (1,1,\ell_3)$, i.e., $\chi_{\bm{p}}^{\bm{\ell}}(n+P) = -\chi_{\bm{p}}^{\bm{\ell}}(n)$. Now replace $n$ with $-n$ and use the fact that $\chi_{\bm{p}}^{\bm{\ell}}$ is odd to obtain (iii) in Lemma [\[chiprop\]](#chiprop){reference-type="ref" reference="chiprop"}. Finally, note that $\chi_{\bm{p}}^{\bm{\ell}}$ is odd modulo $NP$ for all even $N$ and even modulo $NP$ for all odd $N$.
:::

Next, we recall a result (see [@hikami1 Proposition 3] or [@tm Corollary 3.9]) which explicitly computes the limiting values of the Eichler integrals $\widetilde{\Phi}_{\bm{p}}^{\bm{\ell}}(\tau)$ as $\tau \to \frac{M}{N}$.

::: proposition
[]{#Elimit label="Elimit"} Let $M$ and $N$ be coprime positive integers. We have $$\lim_{\tau \to \frac{M}{N}} \widetilde{\Phi}_{\bm{p}}^{\bm{\ell}}(\tau) = \sum_{n=0}^{PN} \chi_{\bm{p}}^{\bm{\ell}} \left( 1 - \frac{n}{PN} \right) \zeta_N^{M\frac{n^2}{4P}}.$$
:::
