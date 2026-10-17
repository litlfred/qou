---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-007-24-second-reciprocity-formula-for-the-q-pochhamm
section_title: "Second reciprocity formula for the q-Pochhammer symbol"
section_number: 2.4
pages: 19-38
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.987
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
[]{#sec:recip2-poch label="sec:recip2-poch"}

::: theorem
[]{#thp label="thp"} Let $4\leq h< k$ with $(h,k)=1$ and $r_0\in \{0, \dotsc, h-1\}$. Let $0\leq r<k$ with $r\equiv r_0~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$. We have $$\begin{aligned}
    \frac{(\ifthenelse{\equal{-{\overline h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -{\overline h}/k\aftergroup\egroup\originalright)}{( -{\overline h}/k)}{( -{\overline h}/k)}{( -{\overline h}/k)}})_{r}\ifthenelse{\equal{-\frac{h}{24k}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -\frac{h}{24k}\aftergroup\egroup\originalright)}{( -\frac{h}{24k})}{( -\frac{h}{24k})}{( -\frac{h}{24k})}}}{(\ifthenelse{\equal{{\overline k}/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline k}/h\aftergroup\egroup\originalright)}{( {\overline k}/h)}{( {\overline k}/h)}{( {\overline k}/h)}})_{r_0}\ifthenelse{\equal{\frac{k}{24h}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \frac{k}{24h}\aftergroup\egroup\originalright)}{( \frac{k}{24h})}{( \frac{k}{24h})}{( \frac{k}{24h})}}}=\exp\bigg(&\frac{k}h\mathop{\mathrm{{\mathfrak L}}}(r/k) -\frac{\pi }k\sum_{\substack{1\leq n\leq r_0}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{ n}{h}+\frac {\pi}k{\mathopen{}\mathclose\bgroup\originalleft\lfloor {\frac rh} \aftergroup\egroup\originalright\rfloor}c_0\Big(\frac{\overline k}h\Big) \\
    {}& + \mathcal{O}_{h,k,r_0}^{z}\Big((1+|z|^4+\mathopen{}\mathclose\bgroup\originalleft|\log(z(1-z))\aftergroup\egroup\originalright|)\Big(1+\log\Big(\frac kh\Big)+\frac k{h^{2}}\Big)\Big)\bigg)
  
\end{aligned}$$ where $z=r/k$, using the notation [\[eq:def-Oh\]](#eq:def-Oh){reference-type="eqref" reference="eq:def-Oh"} with domain $D_2 = \{z\neq 0, \operatorname{Re}(z)\in[0, 1)\}$. Moreover, the term $\mathopen{}\mathclose\bgroup\originalleft|\log(z(1-z))\aftergroup\egroup\originalright|$ can be omitted if $z\in[\frac{r_0}k, 1-\frac{h}k(1-\{\frac{r_0-k}{h}\})]$.
:::

::: proof
*Proof.* In this proof, the notation $\mathcal{O}$ will stand for $\mathcal{O}_{h,k,r_0}^z$ with respect to the domain $D_2 = \{z\neq 0, \operatorname{Re}(z)\in[0, 1)\}$. Applying the identity $\frac{\overline h}{k}+\frac{\overline k}{h}\equiv \frac{1}{hk}~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~1\aftergroup\egroup\originalright)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}$ we have $$\begin{aligned}
    (\ifthenelse{\equal{-{\overline h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -{\overline h}/k\aftergroup\egroup\originalright)}{( -{\overline h}/k)}{( -{\overline h}/k)}{( -{\overline h}/k)}})_{r}&=\prod_{n=1}^r\bigg(1-\ifthenelse{\equal{\frac{n\overline k }h - \frac n{hk}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \frac{n\overline k }h - \frac n{hk}\aftergroup\egroup\originalright)}{( \frac{n\overline k }h - \frac n{hk})}{( \frac{n\overline k }h - \frac n{hk})}{( \frac{n\overline k }h - \frac n{hk})}}\bigg)
    = \mathcal{P}\cdot \prod_{\substack{n=1\\ h\nmid n}}^r\bigg(1-\ifthenelse{\equal{\frac{n\overline k }h - \frac { n}{hk}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \frac{n\overline k }h - \frac { n}{hk}\aftergroup\egroup\originalright)}{( \frac{n\overline k }h - \frac { n}{hk})}{( \frac{n\overline k }h - \frac { n}{hk})}{( \frac{n\overline k }h - \frac { n}{hk})}}\bigg)
  
\end{aligned}$$ where $\mathcal{P}:=\prod_{n=1}^{\lfloor r/h\rfloor}\big(1-\ifthenelse{\equal{-\frac { n}{k}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -\frac { n}{k}\aftergroup\egroup\originalright)}{( -\frac { n}{k})}{( -\frac { n}{k})}{( -\frac { n}{k})}}\big)$. Note that for $x,y\in\mathbb{C}$, we have $$\begin{aligned}
    1-\ifthenelse{\equal{y-x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  y-x\aftergroup\egroup\originalright)}{( y-x)}{( y-x)}{( y-x)}}&= \frac{1}2 (1+\ifthenelse{\equal{-x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -x\aftergroup\egroup\originalright)}{( -x)}{( -x)}{( -x)}})\big (1-\ifthenelse{\equal{y}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  y\aftergroup\egroup\originalright)}{( y)}{( y)}{( y)}}\big)(1-\tan (\pi x) \cot (\pi y)).
  
\end{aligned}$$ Thus, since $\prod_{n=1}^{h-1}(1-\ifthenelse{\equal{\frac{n\overline k }h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \frac{n\overline k }h\aftergroup\egroup\originalright)}{( \frac{n\overline k }h)}{( \frac{n\overline k }h)}{( \frac{n\overline k }h)}})=h$, we have $$\begin{aligned}
\label{feqr2}
    (\ifthenelse{\equal{-{\overline h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -{\overline h}/k\aftergroup\egroup\originalright)}{( -{\overline h}/k)}{( -{\overline h}/k)}{( -{\overline h}/k)}})_{r}&=(\ifthenelse{\equal{{\overline k}/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline k}/h\aftergroup\egroup\originalright)}{( {\overline k}/h)}{( {\overline k}/h)}{( {\overline k}/h)}})_{r_0}\, h^{{\mathopen{}\mathclose\bgroup\originalleft\lfloor { r/h} \aftergroup\egroup\originalright\rfloor}} \cdot \mathcal{P}\cdot \mathcal{M}\cdot \mathcal{L},
  
\end{aligned}$$ where $$\begin{aligned}
    \mathcal{M}=\prod_{\substack{n=1\\ h\nmid n}}^r\frac{1+\ifthenelse{\equal{-\frac{ n}{hk}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -\frac{ n}{hk}\aftergroup\egroup\originalright)}{( -\frac{ n}{hk})}{( -\frac{ n}{hk})}{( -\frac{ n}{hk})}} }2, &&   \mathcal{L}    =   \prod_{\substack{n=1\\ h\nmid n}}^r\bigg(1-\cot\Big( \frac{\pi n\overline k }{h} \Big)\tan\Big( \frac { \pi n}{hk} \Big)\bigg).
  
\end{aligned}$$ First, we examine $\mathcal{M}$. We have $$\begin{aligned}
    \mathcal{M}&=\exp\bigg(-\sum_{\substack{n=1\\ h\nmid n}}^r\frac{\pi i n}{hk}+\sum_{\substack{n=1\\ h\nmid n}}^r\log\Big(\cos\Big(\frac{\pi n}{hk}\Big)\Big)\bigg).
  
\end{aligned}$$ We split the second sum as $\sum_{\substack{1\leq n\leq r}}-\sum_{\substack{1\leq n\leq r-r_0,\, h|n}}$. For any $\varepsilon>0$ we have $\log(\cos(\frac{\pi w}{hk}))\ll_\varepsilon(\frac {|w|}{hk})^2$ for $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Re}(w/(hk))\aftergroup\egroup\originalright|\leq (1-\varepsilon)/2$ and so applying Lemma [\[triab\]](#triab){reference-type="ref" reference="triab"} we obtain, with $z = r/k$, $$\begin{aligned}
\label{bfmm}
    \mathcal{M}&=\exp\bigg(-\sum_{\substack{n=1\\ h\nmid n}}^r\frac{\pi i n}{hk} + \frac{k}{h^2} \mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^3+1) \Big)\bigg)
    = \exp\bigg(-\frac{\pi i (r^2+r)}{2hk}+\frac{k}{h^2}\mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^3+1)\bigg).
  
\end{aligned}$$

We then move to $\mathcal{P}=\exp(\log \mathcal{P})$. Taking the determination which is real on the negative imaginary axis, we have that $\log(\frac{1-\ifthenelse{\equal{-w}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -w\aftergroup\egroup\originalright)}{( -w)}{( -w)}{( -w)}}}{2\pi iw})$ is holomorphic and $O_\varepsilon(|w|)$ for $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Re}(w)\aftergroup\egroup\originalright|<1-\varepsilon$. Thus, by Lemma [\[triab\]](#triab){reference-type="ref" reference="triab"}, $$\begin{aligned}
    \mathcal{P}&=\exp\bigg(\sum_{1\leq n \leq (r-r_0)/h} \log\Big(2\pi i\frac{n}{k}\Big)+\frac{k}{h^2}\mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2+1)\bigg)\\
    &=\exp\bigg( \log\Gamma\Big(1+\frac{r-r_0}h\Big)+\frac{r-r_0}h\log\frac{2\pi i}k+\frac{k}{h^2}\mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2+1)\bigg).
  
\end{aligned}$$ Write $\log (\Gamma(1+w))=(w+1/2)\log(w+1)-w+\mathcal{E}_1(w)$ with $\mathcal{E}_1$ holomorphic and $O(|\log (w+1)|)$ on $\operatorname{Re}(w)>-1$. Abbreviating temporarily $q = \frac{r-r_0}h$, it follows that $$\begin{aligned}
    \mathcal{P}&=\exp\bigg(
    \Big(\frac12+q\Big)\log(1+q)+ q\log\frac{2\pi i}{ke}
    +\mathcal{E}_1(1+q)+\frac{k}{h^2}\mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2+1)
    \bigg)\notag\\
    &=\exp\bigg( {\frac rh}\log\Big(\frac{2\pi i  r}{ke}\Big)- \Big\lfloor \frac{r}h\Big\rfloor\log h+\mathcal{O}((1+\log(k/h)+\tfrac{k}{h^2})(1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2+\mathopen{}\mathclose\bgroup\originalleft|\log(z)\aftergroup\egroup\originalright|)
    \bigg),\label{bfpp}
  
\end{aligned}$$ since $$\begin{aligned}
    &\Big(\frac12-\frac{r_0}{h}\Big)\log\Big(\frac{kz+h-r_0}{h}\Big)+\frac{kz}h\log\Big(1+\frac{h-r_0}{kz}\Big)+{}\\
    &\qquad- \frac{r_0}h\log\frac{2\pi i h}{ke}+\mathcal{E}_1\Big(\frac{kz+h-r_0}h\Big) = \mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright| + \mathopen{}\mathclose\bgroup\originalleft|\log(z)\aftergroup\egroup\originalright|).
  
\end{aligned}$$ Note that the terms $\mathopen{}\mathclose\bgroup\originalleft|\log(z)\aftergroup\egroup\originalright|$ can be omitted if $z\in[\frac{r_0}k, 1)$.

It remains to study $\mathcal{L}$. By Lemma [\[tan_ineq\]](#tan_ineq){reference-type="ref" reference="tan_ineq"} we have $|\tan( \frac{\pi n}{hk})\cot(\pi \frac{n\overline k}h)|<1$ and so we can write $\mathcal{L}=\exp(\log \mathcal{L})$ with the principal determination. First, we consider $$\sum_{\substack{1\leq n\leq r\\ h\nmid n}}\tan\Big(\pi\frac n{hk}\Big)\cot\Big(\pi\frac{n\overline k }h\Big)=\sum_{\substack{1\leq n\leq r\\ h\nmid n}}\frac {\pi n}{hk}\cot\Big(\pi\frac{n\overline k }h\Big)+\sum_{\substack{1\leq n\leq r\\ h\nmid n}}\mathcal{E}_2\Big(\frac n{hk}\Big)\cot\Big(\pi\frac{n\overline k }h\Big),$$ where $\mathcal{E}_2(z):=\tan(\pi z)-\pi z$. Clearly, $\mathcal{E}_2(z)$ is holomorphic and $O_\varepsilon(|z|^2)$ in $|\operatorname{Re}(z)|<(1-\varepsilon)/2$. Thus, dividing in congruence classes modulo $h$, the second summand above is $$\begin{aligned}
    \mathcal{O}\Big((1+|z|^3)\sum_{\ell=1}^h\frac 1\ell\frac k{h^2}\Big) = \mathcal{O}\Big((1+|z|^3)\frac {k\log h}{h^2}\Big).
  
\end{aligned}$$ Also, $$\begin{aligned}
    \sum_{\substack{1\leq n\leq r\\ h\nmid n}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{\pi n}{hk}&=\sum_{\substack{1\leq n\leq r_0}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{\pi n}{hk}+\sum_{\ell=1}^{{\mathopen{}\mathclose\bgroup\originalleft\lfloor {r/h} \aftergroup\egroup\originalright\rfloor}}\sum_{\substack{1\leq n<h}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{\pi (n+\ell h)}{hk}\\
    &=\frac{\pi }k\sum_{\substack{1\leq n\leq r_0}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{ n}{h}-{\mathopen{}\mathclose\bgroup\originalleft\lfloor {\frac rh} \aftergroup\egroup\originalright\rfloor}\frac {\pi}kc_0\Big(\frac{\overline k}h\Big)
  
\end{aligned}$$ since $\sum_{n=1}^{h-1}\cot(\pi\frac{n}h)=0$. Thus, by Lemma [\[madc\]](#madc){reference-type="ref" reference="madc"} we have $$\begin{aligned}
    \mathcal{L}=\exp\bigg(&\frac{\pi i (r^2-rk)}{2kh}+\frac kh\Big(\mathop{\mathrm{{\mathfrak L}}}(r/k)+\frac{\pi i }{12}+\frac rk \log\Big( \frac {2 \pi r}{ke}\Big)\Big)+{}\\
    &+\frac{\pi }k\sum_{\substack{1\leq n\leq r_0}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{ n}{h}    -\frac {\pi}k{\mathopen{}\mathclose\bgroup\originalleft\lfloor {\frac rh} \aftergroup\egroup\originalright\rfloor}c_0\Big(\frac{\overline k}h\Big) \\
    & +\mathcal{O}\Big(\Big(1+\frac{k}{h^2}+\log(k/h)\Big)(1+|z|^4+|\log(1-z)|)\Big)\bigg),
  
\end{aligned}$$ where the error term $\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|$ can be omitted if $z\in[0,1 - \frac{h}k(1-\{\frac{r_0-k}h\})]$. The theorem then follows by [\[feqr2\]](#feqr2){reference-type="eqref" reference="feqr2"}, [\[bfmm\]](#bfmm){reference-type="eqref" reference="bfmm"} and [\[bfpp\]](#bfpp){reference-type="eqref" reference="bfpp"}, since $\frac{ h}{24k}=O(1).$ ◻
:::

# Proof of Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"} {#pmt1}

Throughout the rest of the section, $K$ will denote any hyperbolic knot $K\neq 7_2$ with at most $7$ crossings.

We will use the same notation as in Section [\[ss:1rf\]](#ss:1rf){reference-type="ref" reference="ss:1rf"}. In particular, all error terms will be allowed to depend on $d$ and $\gamma$.

For $n\in\mathbb{N}_{\geq 0}$ and $\alpha=\frac hk\in\mathbb{Q}$, with $(h,k)=1$, we let $$\begin{aligned}
\label{sb}
  [\alpha]_n :=k^{-1/2}  (\ifthenelse{\equal{\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha\aftergroup\egroup\originalright)}{( \alpha)}{( \alpha)}{( \alpha)}})_{n'}, 
\end{aligned}$$ where $n'\equiv n~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~k\aftergroup\egroup\originalright)}{(\textnormal{mod}~k)}{(\textnormal{mod}~k)}{(\textnormal{mod}~k)}$, $0\leq n'<k$.

There exist $m,m_1,\dots,m_4\in\mathbb{N}$, $\iota,\upsilon\in\mathbb{Z}$ and linear functions $\ell_{i,j}(\boldsymbol r)=\sum_{u=1}^m\kappa_{i,j}(u)r_u$ with $\kappa_{i,j}\in\{0,\pm1\}$ such that $$\begin{aligned}
  \mathcal{J}_{K}( x) ={}& \mathop{\mathrm{denom}}(x)^{\iota}\ifthenelse{\equal{\upsilon x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \upsilon x\aftergroup\egroup\originalright)}{( \upsilon x)}{( \upsilon x)}{( \upsilon x)}} \operatornamewithlimits{\sum\nolimits^*}_{0\leq r_1,\dots, r_m<k}\frac{\prod_{j=1}^{m_1}[ x]_{\ell_{1,j}(\boldsymbol r)}\prod_{j=1}^{m_2}\overline{[ x]}_{\ell_{2,i}(\boldsymbol r)}}{\prod_{j=1}^{m_3}[ x]_{\ell_{3,j}(\boldsymbol r)}\prod_{j=1}^{m_4}\overline{[ x]}_{\ell_{4,j}(\boldsymbol r)}} \label{exja} \\
  = {}& \mathop{\mathrm{denom}}(x)^{\iota}\ifthenelse{\equal{\upsilon x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \upsilon x\aftergroup\egroup\originalright)}{( \upsilon x)}{( \upsilon x)}{( \upsilon x)}}  \operatornamewithlimits{\sum\nolimits^*}_{0\leq r_1,\dots, r_m<k} \Pi_K\big([x]_{\ell_{i,j}(\boldsymbol r)}\big), \notag
\end{aligned}$$ where $\operatornamewithlimits{\sum\nolimits^*}$ indicates that the sum is restricted to the terms with $0\leq \ell_{i,j}(\boldsymbol r)<k$ and, here and what follows, we put $$\Pi_K\big(z_{i, j}\big) = \frac{\prod_{j=1}^{m_1} z_{1,j} \prod_{j=1}^{m_2} \overline{z_{2,j}}}{\prod_{j=1}^{m_3} z_{3,j} \prod_{j=1}^{m_4} \overline{z_{4,j}}}.$$ The Kashaev invariants for the knots under consideration has been given for example in [@Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7]. In all these cases, $m+3$ coincides with the number of crossings of $K$, moreover $$\iota=\frac{3-m}2, \qquad m_1+m_2+m_3+m_4 = 3m-1,$$ and the values of $m_i,\ell_{i,j}$ are as in Figure [1](#fig:table-K-param){reference-type="ref" reference="fig:table-K-param"}, where we used the formula $[\alpha]_n [\overline{\alpha}]_{\mathop{\mathrm{denom}}({\alpha})-n}=1$ to write the Kashaev invariants given in [@Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7] as in [\[exja\]](#exja){reference-type="eqref" reference="exja"}. Finally, different variants of the definition of the Kashaev invariant lead to slightly different values for $\upsilon$ (cf. [@Ohtsuki52 p.677 footnote 4] and [@Yokota2003]). In the context of the modularity conjecture it is natural to always take $\upsilon=0$, which we shall do in the following. This choice will lead to the expression [\[eq:J0-approxmod\]](#eq:J0-approxmod){reference-type="eqref" reference="eq:J0-approxmod"} for the reciprocity formula, as conjectured by Zagier. Using [\[expid\]](#expid){reference-type="eqref" reference="expid"} one can then easily deduce the suitable modified reciprocity formula corresponding to other choices of $\upsilon$.

<figure id="fig:table-K-param">
<p><span class="math display">$$\begin{array}{|c|c|l|l|}
      \hline
      K &amp; (m_j)_{1 \leq j \leq 4} &amp; \ell_{i,j} = \ell_{i,j}({\boldsymbol r}) \\ \hline

      4_1 &amp;
      \begin{array}{l}
        (1, 1, 0, 0)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1} = \ell_{2,1} = r
      \end{array} \\ \hline

      5_2 &amp;
      \begin{array}{l}
        (0, 1, 2, 2)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{2,1}=r_1+r_2,\quad \ell_{3,1}=r_1+r_2 \\
        \ell_{3,2}=\ell_{4,1}=r_2,\quad \ell_{4,2}=r_1 \\
      \end{array} \\ \hline

      6_1 &amp;
      \begin{array}{l}
        (0, 2, 3, 3)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{2,1}=r_1+r_2,\quad \ell_{2,2}=r_1+r_2+r_3 \\
        \ell_{3,1}=r_1,\quad \ell_{3,2}=r_1+r_2,\quad \ell_{3,3}=r_1+r_2+r_3 \\
        \ell_{4,1}=r_1,\quad \ell_{4,2}=r_2,\quad \ell_{4,3}=r_3
      \end{array} \\ \hline

      6_2 &amp;
      \begin{array}{l}
        (2, 1, 2, 3)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=r_1,\quad \ell_{1,2}=r_2+r_3,\quad \ell_{2,1}=r_1 \\
        \ell_{3,1}=\ell_{4,1}=r_2,\quad \ell_{3,2}=r_3,\quad \ell_{4,2}=r_1-r_2,\quad \ell_{4,3}=r_2+r_3
      \end{array} \\ \hline

      6_3 &amp;
      \begin{array}{l}
        (1, 1, 3, 3)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=\ell_{2,1}=r_2,\quad \ell_{3,1}=\ell_{4,1}=r_1 \\
        \ell_{3,2}=\ell_{4,2}=r_3,\quad \ell_{3,3}=r_2-r_3,\quad \ell_{4,3}=r_2-r_1
      \end{array} \\ \hline

      7_3 &amp;
      \begin{array}{l}
        (2, 3, 3, 3)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=\ell_{2,1}=r_2,\quad \ell_{1,2}=r_2-r_1 \\
        \ell_{2,2}=\ell_{3,1}=r_2-r_3,\quad \ell_{2,3}= \ell_{3,2}=r_2-r_3-r_4,\quad \ell_{3,3}=r_1 \\
        \ell_{4,1}=r_2-r_1,\quad \ell_{4,2}=r_3,\quad \ell_{4,3}=r_4
      \end{array} \\ \hline

      7_4 &amp;
      \begin{array}{l}
        (3, 0, 4, 4)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=\ell_{4,1}=r_1+r_2,\quad \ell_{1,2}=r_2+r_3 \\
        \ell_{1,3}=\ell_{4,2}=r_3+r_4 \\
        \ell_{3,1}=r_1,\quad \ell_{3,2}=\ell_{4,3}=r_2 \\
        \ell_{3,3}=\ell_{4,4}=r_3,\quad \ell_{3,4}=r_4
      \end{array} \\ \hline

      7_5 &amp;
      \begin{array}{l}
        (2, 2, 3, 4)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=\ell_{2,1}=r_3,\quad \ell_{1,2}=\ell_{4,1}=r_3-r_4 \\
        \ell_{2,2}=\ell_{3,1}=r_2,\quad \ell_{3,2}=\ell_{4,2}=r_1,\quad \ell_{3,3}=r_4 \\
        \ell_{4,3}=r_2-r_1 \\
        \ell_{4,4}=r_3-r_2
      \end{array} \\ \hline

      7_6 &amp;
      \begin{array}{l}
        (2, 1, 4, 4)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=\ell_{4,1}=r_2,\quad \ell_{1,2}=r_3+r_4 \\
        \ell_{2,1}=r_2+r_3,\quad \ell_{3,1}=\ell_{4,2}=r_1,\quad \ell_{3,2}=r_2-r_1 \\
        \ell_{3,3}=\ell_{4,3}=r_3,\quad \ell_{3,4}=\ell_{4,4}=r_4.        
      \end{array} \\ \hline

      7_7 &amp;
      \begin{array}{l}
        (2, 1, 4, 4)
      \end{array} &amp; 
      \begin{array}{l}
        \ell_{1,1}=r_1+r_2, \quad \ell_{1,2}=r_3+r_4 \\
        \ell_{2,1}=r_2+r_3, \quad \forall j\in\{1, 2, 3, 4\},\ \ell_{3,j}=\ell_{4,j}=r_j
      \end{array} \\ \hline
    \end{array}$$</span></p>
<figcaption>Parameters of the Kashaev invariants</figcaption>
</figure>

We divide the sum over ${\boldsymbol r}$ restricting the $r_i$ into congruence classes modulo $q$ and in intervals of length $k/d$: $$\begin{aligned}
\label{splj}
  \mathcal{J}_{K}(\gamma x) = \mathop{\mathrm{denom}}(\gamma x)^{\frac{3-m}2} \sum_{\boldsymbol L\in\{0,\dots,d-1\}^m}\,\sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}} \mathcal{J}_K(\gamma, x; \boldsymbol L,\boldsymbol s)
\end{aligned}$$ where, for $\boldsymbol L=(L_1,\dots,L_m)\in\mathbb{Z}_{\geq 0}^m$, $\boldsymbol s=(s_1,\dots,s_m)\in(\mathbb{Z}/q\mathbb{Z})^m$ we write $$\begin{aligned}
  \mathcal{J}_K(\gamma, x; {\boldsymbol L}, {\boldsymbol s}) =   \operatornamewithlimits{\sum\nolimits^*}_{\substack{0\leq r_1,\dots, r_m<k,\\  {\mathopen{}\mathclose\bgroup\originalleft\lfloor {r_i d/k} \aftergroup\egroup\originalright\rfloor}=L_i,\ \forall i\\ r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i}}
  \Pi_K\big([\gamma x]_{\ell_{i,j}(\boldsymbol r)}\big).
\end{aligned}$$ By Theorem [\[th:Ir\]](#th:Ir){reference-type="ref" reference="th:Ir"} and Remark [\[remplr\]](#remplr){reference-type="ref" reference="remplr"}, we have $$[\gamma x]_{r} = [x]_{\lfloor r d/k\rfloor} A(p,q) \Phi_{r}(\{r d/k\}),$$ where for $s\in\mathbb{Z}/q\mathbb{Z}$, $\lambda\in[0,1)$, we define $$\begin{aligned}
  A(p,q) &= \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big( - \frac{\mathop{\mathrm{s}}(p,q)}2 - \frac 18\Big), \notag\\
  \Phi_{s}(\lambda) &= \exp\bigg(\frac k{qd} \Big(\mathop{\mathrm{{\mathfrak L}}}(\lambda) +\frac{\pi i }{12}\Big)+\frac{\pi i d}{12kq}+ {\mathcal E}_s(\lambda,d/k) \bigg). \label{defb}
\end{aligned}$$ It follows that $$\begin{aligned}
  \mathcal{J}_K(\gamma, x; {\boldsymbol L}, {\boldsymbol s}) =   A(p,q)^{m_1+m_4-m_2-m_3} \operatornamewithlimits{\sum\nolimits^*}_{\substack{0\leq r_1,\dots, r_m<k,\\  {\mathopen{}\mathclose\bgroup\originalleft\lfloor {r_i d/k} \aftergroup\egroup\originalright\rfloor}=L_i,\ \forall i\\ r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i}}
  \Pi_K\big([x]_{\lfloor \ell_{i,j}(\boldsymbol r) d/k\rfloor} \Phi_{\ell_{i,j}(\boldsymbol s)}(\{\ell_{i,j}(\boldsymbol r) d/k\})\big).
\end{aligned}$$ Now, let $\lambda_i=\{r_i d/k\}$. The next lemma shows that the contribution of the terms for which $\ell_{i,j}(\boldsymbol \lambda)\notin[0,1)$ for some $i,j$ is negligible.

::: lemma
[]{#extra_terms label="extra_terms"} There exists $\delta>0$ such that $$\begin{aligned}
    \bigg|\Pi_K\big(\exp\big(\mathop{\mathrm{{\mathfrak L}}}(\ell_{i,j}(\boldsymbol \lambda))\big) \big)\bigg| \leq  \exp\Big(\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}-\delta\Big)
  
\end{aligned}$$ whenever $\ell_{i,j}(\boldsymbol \lambda)\notin[0,1)$ for some $i,j$.
:::

We postpone the proof of Lemma [\[extra_terms\]](#extra_terms){reference-type="ref" reference="extra_terms"} to Section [1.1](#prolex){reference-type="ref" reference="prolex"}. Since $[x]_{r}\asymp 1$ for $0\leq r<d$, applying [\[bdfg\]](#bdfg){reference-type="eqref" reference="bdfg"} and the above lemma we obtain $$\begin{split}\label{reme}
    \mathcal{J}_K(\gamma, x ; \boldsymbol L,\boldsymbol s) &=  A(p,q)^{m_1+m_4-m_2-m_3}
    \Pi_K\big([ x]_{ \ell_{i,j}(\boldsymbol L) }\big)
    \mathcal{J}^*_K(\gamma, x; \boldsymbol L,\boldsymbol s)+{}\\
    &\quad+O\bigg(k^{O(1)}\exp\Big(\Big(\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}-\delta\Big)\frac{k}{qd}\Big)\bigg),
  \end{split}$$ where $$\begin{aligned}
  \mathcal{J}^*_K(\gamma, x; \boldsymbol L,\boldsymbol s) =    \operatornamewithlimits{\sum\nolimits^*}_{\substack{0\leq r_1,\dots, r_m<k,\\  {\mathopen{}\mathclose\bgroup\originalleft\lfloor {r_i d/k} \aftergroup\egroup\originalright\rfloor}=L_i,\ \forall i\\ r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i,\\ 
    \ell_{i,j}(\boldsymbol \lambda)\in[0,1)\ \forall i,j }}
  \Pi_K\big(\Phi_{\ell_{i,j}(\boldsymbol s)}(\{\ell_{i,j}(\boldsymbol r) d/k\})\big).
\end{aligned}$$ We notice that the condition $0\leq \ell_{i,j}({\boldsymbol r})<k$, which is implicit in the summation $\sum^*$, can be written as $0\leq \ell_{i,j}(\boldsymbol L)+\ell_{i,j}(\boldsymbol \lambda)<d$ and so, since $\ell_{i,j}(\boldsymbol \lambda)\in[0,1)$, it is equivalent to $0\leq \ell_{i,j}(\boldsymbol L)<d$. Assuming that $\boldsymbol L$ satisfies this condition, $\mathcal{J}^*_K(\gamma, x; \boldsymbol L,\boldsymbol s)$ can be then rewritten as $$\begin{aligned}
  \mathcal{J}^{*}_K(\gamma, x; \boldsymbol L,\boldsymbol s) =    \sum_{\substack{0 \leq r_i-L_i k/d< k/d\ \forall i,\\  r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i,\\ 
    0\leq \ell_{i,j}({\boldsymbol r}-k \boldsymbol L/d)<k/d\ \forall i,j }}
  \Pi_K\big(\Phi_{\ell_{i,j}(\boldsymbol s)}(\{\ell_{i,j}(\boldsymbol r) d/k\})\big)
\end{aligned}$$ where we used $\{\ell_{i,j}(\boldsymbol r) d/k\}=\ell_{i,j}(\boldsymbol r d/k- \boldsymbol L)$ to rewrite the summation conditions. This sum is essentially the same sum which arises when taking $d=1$, $\gamma=(\begin{smallmatrix}0 & 1\\ -1 &0\end{smallmatrix})$, i.e. the conjugate of the sum arising in the volume conjecture. The only difference in the general case is that ${\boldsymbol r}$ is summed over a box with sides of length $k/d$ and along arithmetic progressions modulo $q$. For fixed $d,q$ these restrictions are negligible from the analytical point of view, and the works [@Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7] can be adapted. For $z\in(\mathbb{C}\smallsetminus\mathbb{R})\cup (0, 1)$, define $$\psi_1(z):={\mathfrak f}(z), \quad \psi_2(z):={\mathfrak f}(1-z), \quad \psi_3(z):=-{\mathfrak f}(z), \quad \psi_4(z):=-{\mathfrak f}(1-z),$$ and let $\boldsymbol \mu=(\mu_1,\dots,\mu_m)$ be the solution described in [@Ohtsuki52 §5.1], [@OhtsukiYokota6 §3.3, §4.3, §5.3] [@Ohtsuki7 §3.3, §4.3, §5.3, §6.3, §7.3] (conjugated to agree with our definition of $\mathcal{J}_K$) to the system of equations $$\begin{aligned}
\label{spe}
  &\sum_{i=1}^4\sum_{j=1}^{m_1}\kappa_{i,j}(u)\psi_i (1-\ell_{i,j}(\boldsymbol \mu)) = 0,\qquad \forall u\in\{1,\dots,m\}
\end{aligned}$$ satisfying $0<\operatorname{Re}(\ell_{i,j}(\boldsymbol \mu))<1$ for all $i,j$. We write $$\nu_i:=\exp(\mu_i), \qquad \nu_i^{1/q}:=\exp(\mu_i/q).$$ It is known [@Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7] that $\mathbb{Q}(\boldsymbol \nu) = F_K$, the trace field of $K$. It will be useful to denote $$F_{K, q} := \mathbb{Q}(\ifthenelse{\equal{1/q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  1/q\aftergroup\egroup\originalright)}{( 1/q)}{( 1/q)}{( 1/q)}},\boldsymbol \nu), \qquad {\tilde F}_{K, q} := \mathbb{Q}(\ifthenelse{\equal{1/q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  1/q\aftergroup\egroup\originalright)}{( 1/q)}{( 1/q)}{( 1/q)}}, \boldsymbol \nu^{1/q}).$$

The following lemma will be proven in Section [1.2](#prolem){reference-type="ref" reference="prolem"}.

::: lemma
[]{#main_terms label="main_terms"} Let $\boldsymbol L\in\{0,\dots, d-1\}^m$, $\boldsymbol s\in(\mathbb{Z}/q\mathbb{Z})^m$ with $0\leq \ell_{i,j}(\boldsymbol L)<d$ for all $i,j$. Then for all $N\geq0$, we have $$\begin{aligned}
    \mathcal{J}^{*}_K(x ; \boldsymbol L,\boldsymbol s) =\frac1{{\mathfrak D}^{1/2}} \Big(\frac{2\pi ik}{ qd}\Big)^{m/2}\exp\Big(\frac{\mathop{\mathrm{Vol}}(K)-i\mathop{\mathrm{cs}}(K)}{2\pi}\frac{k}{qd}+C(\boldsymbol s)\Big)\Big(\sum_{n=0}^N\omega_{\boldsymbol s,n}\Big(\frac{2\pi i qd}{k}\Big)^n+O\Big(\frac{qd}{k}\Big)^{N+1}\Big),
  
\end{aligned}$$ where $0\neq {\mathfrak D}\in F_{K}$, $\omega_{\boldsymbol s,0}:=1$ and $$\begin{aligned}
\label{defcs}
    C(\boldsymbol s)&:=\sum_{i=1}^4\sum_{j=1}^{m_i}C_{i,j}(\boldsymbol s), \qquad C_{i,j}(\boldsymbol s):=\sum_{g=1}^q B_1\Big(\frac{\langle g\overline{p}-\ell_{i,j}(\boldsymbol s)\rangle}q\Big) \psi_i\Big(\frac{g-\ell_{i,j}(\boldsymbol \mu)}q\Big)
  
\end{aligned}$$ where $B_1$ is the $1$-st Bernoulli polynomial. Moreover, for all $n\geq1$, $\omega_{\boldsymbol s,n}\in {\tilde F}_{K,q}$, and for all $\sigma\in\operatorname*{Gal}({\tilde F}_{K,q} / F_{K,q})$, we have $\sigma(\omega_{\boldsymbol s,n})=\omega_{\boldsymbol s-\overline p \boldsymbol u,n}$ if $\sigma$ is given by $$\begin{aligned}
\label{galau}
    \sigma(\nu_i^{1/q})=\nu_i^{1/q}\ifthenelse{\equal{u_i/q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  u_i/q\aftergroup\egroup\originalright)}{( u_i/q)}{( u_i/q)}{( u_i/q)}} \qquad (1\leq i \leq m)
  
\end{aligned}$$ for some $u_1,\dots,u_m\in\mathbb{Z}$.
:::

Applying Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"}, by [\[splj\]](#splj){reference-type="eqref" reference="splj"} and [\[reme\]](#reme){reference-type="eqref" reference="reme"}, and recalling the condition $0\leq \ell_{i,j}(\boldsymbol L)<d$ for all $i,j$, we obtain $$\begin{aligned}
  \frac{ \mathcal{J}_{K}(\gamma x)}{ \mathcal{J}_{K}( x)}& =  \frac{A(p,q)^{m_1+m_4-m_2-m_3}}{{\mathfrak D}^{1/2}} \Big(\frac{ k}{ d}\Big)^{\frac32} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(-m/8) q^{-m/2}  \exp\Big(\frac{\mathop{\mathrm{Vol}}(K)-i\mathop{\mathrm{cs}}(K)}{2\pi}\frac{k}{qd}\Big)\\
  &\quad\times\sum_{\boldsymbol s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp(C(\boldsymbol s))\Big(\sum_{n=0}^N\omega_{\boldsymbol s,n}\Big(\frac{2\pi iqd}{k}\Big)^n+O\Big(\frac{1}{k}\Big)^{N+1}\Big),
\end{aligned}$$ for all $N\geq0$.

Now, $6q \mathop{\mathrm{s}}(p,q)$ is an integer, so $A(p,q)$ is a $24q$ root of unity, and letting $\nu_K = -m_1-m_4+m_2+m_3$, we have $\nu_K \equiv m+1~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~2\aftergroup\egroup\originalright)}{(\textnormal{mod}~2)}{(\textnormal{mod}~2)}{(\textnormal{mod}~2)}$. We deduce $$\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\frac{\nu_K}2 s(p, q) + \frac{\nu-m}8\Big) = \pm \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\frac{\nu_K}2s(p, q)+\frac18\Big) \omega,$$ where $\omega \in \{1, i\}$ is independent of $\alpha$ and $\nu_K$ is as in the following table.

<figure id="fig:nuK">
<table>
<thead>
<tr class="header">
<th style="text-align: center;"><span class="math inline"><em>K</em></span></th>
<th style="text-align: center;"><span class="math inline">4<sub>1</sub></span></th>
<th style="text-align: center;"><span class="math inline">5<sub>1</sub></span></th>
<th style="text-align: center;"><span class="math inline">6<sub>1</sub></span></th>
<th style="text-align: center;"><span class="math inline">6<sub>2</sub></span></th>
<th style="text-align: center;"><span class="math inline">6<sub>3</sub></span></th>
<th style="text-align: center;"><span class="math inline">7<sub>3</sub></span></th>
<th style="text-align: center;"><span class="math inline">7<sub>4</sub></span></th>
<th style="text-align: center;"><span class="math inline">7<sub>5</sub></span></th>
<th style="text-align: center;"><span class="math inline">7<sub>6</sub></span></th>
<th style="text-align: center;"><span class="math inline">7<sub>7</sub></span></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><em>ν</em><sub><em>K</em></sub></span></td>
<td style="text-align: center;"><span class="math inline">0</span></td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">2</span></td>
<td style="text-align: center;"><span class="math inline"> − 2</span></td>
<td style="text-align: center;"><span class="math inline">0</span></td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline"> − 3</span></td>
<td style="text-align: center;"><span class="math inline"> − 1</span></td>
<td style="text-align: center;"><span class="math inline"> − 1</span></td>
<td style="text-align: center;"><span class="math inline"> − 1</span></td>
</tr>
</tbody>
</table>
<figcaption>Values of <span class="math inline"><em>ν</em><sub><em>K</em></sub></span></figcaption>
</figure>

Keeping track of the factor $i$ implicit in $\frac{2\pi}{\hbar} = -i\frac{k}{dq}$, the proof of Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"} follows from the following lemma, upon possibly multiplying the value of ${\mathfrak D}$ by $-1$.

::: lemma
[]{#conste label="conste"} There exists $0\neq U\in F_K$ such that defining $$S_n:= U^{1/2} \sum_{\boldsymbol s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp(C(\boldsymbol s))\omega_{\boldsymbol s,n},\qquad n\in\mathbb{N}_{\geq 0},$$ we have $S_n^q \in F_{K, q}$ for all $n\geq0$. If moreover $S_n\neq0$, then for all $n'\geq0$ we have $S_n^{-1}S_{n'}\in F_{K,q}$.
:::

Note that in Theorems 2.2 and 2.6 of [@DimofteGaroufalidis2018], similar computations are carried out for coefficients of power series constructed by a different process, which are conjectured to match those in the modularity conjecture.

::: proof
*Proof.* For $x\in(-1,1)$ we have $B_1(\langle x\rangle)=x-\frac12+{\mathbf 1}_{x\leq 0}$. Thus, $$\begin{aligned}
    C_{i,j}(\boldsymbol s)&
    =\sum_{g=1}^{q}B_1\Big(\frac{\langle g- \ell_{i,j}(\boldsymbol s)\rangle}q\Big) \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)\\
    &=\sum_{g=1}^{\langle\ell_{i,j}(\boldsymbol s)\rangle} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)+\sum_{g=1}^{q} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)\Big(\frac{ g}q-\frac{ \langle\ell_{i,j}(\boldsymbol s)\rangle}q-\frac12\Big)\\
    &=\sum_{g=1}^{\langle\ell_{i,j}(\boldsymbol s)\rangle} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)+\sum_{g=1}^{q} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)\frac{ g}q- \psi_i(1 -\ell_{i,j}(\boldsymbol \mu))\Big(\frac{ \langle\ell_{i,j}(\boldsymbol s)\rangle}q+\frac12\Big)
  
\end{aligned}$$ where in the last equality we used [\[ff4\]](#ff4){reference-type="eqref" reference="ff4"}. Then, $$\begin{aligned}
\label{cspl}
    C_{i,j}(\boldsymbol s)&=D_{i,j}(\boldsymbol s)+\frac1q{D'_{i,j}}- \psi_i(1 -\ell_{i,j}(\boldsymbol \mu))\Big(\frac{  \ell_{i,j}(\boldsymbol s)}q+\frac12\Big),
  
\end{aligned}$$ with $$\begin{aligned}
    D_{i,j}(\boldsymbol s)&:=\sum_{g=1}^{\langle\ell_{i,j}(\boldsymbol s)\rangle} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big) + \psi_i(1 -\ell_{i,j}(\boldsymbol \mu))\frac{\ell_{i,j}(\boldsymbol s)- \langle\ell_{i,j}(\boldsymbol s)\rangle}q,\label{dfnd}\\
    D'_{i,j}&:=\sum_{g=1}^{q} \psi_i\Big(\frac{\langle gp \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)g.\label{dfndp}
  
\end{aligned}$$ It follows that $$\begin{aligned}
\label{seq}
    \!\sum_{\boldsymbol s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp(C(\boldsymbol s))\omega_{\boldsymbol s,n}&=\exp\Big(\frac1q\sum_{i=1}^4\sum_{j=1}^{m_i}D'_{i,j}-\frac12E\Big)\sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp\Big(\sum_{i=1}^4\sum_{j=1}^{m_i}D_{i,j}(\boldsymbol s)\Big)\omega_{\boldsymbol s,n}
  
\end{aligned}$$ where we used that, by [\[spe\]](#spe){reference-type="eqref" reference="spe"}, $$\begin{aligned}
    E&=2 \sum_{i=1}^4\sum_{j=1}^{m_i} \psi_i(1-\ell_{i,j}(\boldsymbol \mu))\Big(\frac{  \ell_{i,j}(\boldsymbol s)}q+\frac12\Big)=\sum_{i=1}^4\sum_{j=1}^{m_i} \psi_i(1-\ell_{i,j}(\boldsymbol \mu))
  
\end{aligned}$$ is independent of $\boldsymbol s$. In particular, writing $U=\exp(E)$, by the definition of $\psi_i$, [\[dfnd\]](#dfnd){reference-type="eqref" reference="dfnd"}-[\[dfndp\]](#dfndp){reference-type="eqref" reference="dfndp"} and Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"}, we have $S_n^q\in {\tilde F}_{K, q}$. The extension ${\tilde F}_{K, q} / F_{K, q}$ is Galois and $\operatorname*{Gal}({\tilde F}_{K, q} / F_{K, q})$ consists of automorphisms of the form [\[galau\]](#galau){reference-type="eqref" reference="galau"}. Thus, it suffices to show that $S_n^q$ is invariant under any such automorphism $\sigma$. Now, by Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"}, $$\begin{aligned}
    \sigma\big(S_n^q\big)&=\exp\Big(\frac1q\sum_{i=1}^4\sum_{j=1}^{m_i}{D'}^\sigma_{i,j}\Big)\sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp\Big(\sum_{i=1}^4\sum_{j=1}^{m_i}D^\sigma_{i,j}(\boldsymbol s)\Big)\omega_{\boldsymbol s-\overline{p} \boldsymbol u,n}\\
  
\end{aligned}$$ where $$\begin{aligned}
    D^\sigma_{i,j}(\boldsymbol s)&:=\sum_{g=1}^{\langle\ell_{i,j}(\boldsymbol s)\rangle} \psi_i\Big(\frac{\langle gp -\ell_{i,j}(\boldsymbol u) \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)- \psi_i(1 -\ell_{i,j}(\boldsymbol \mu))\frac{\ell_{i,j}(\boldsymbol s)- \langle\ell_{i,j}(\boldsymbol s)\rangle}q,\label{defdp}\\
    (D'_{i,j})^\sigma&:=\sum_{g=1}^{q} \psi_i\Big(\frac{\langle gp -\ell_{i,j}(\boldsymbol u) \rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)g.\notag
  
\end{aligned}$$ The same computation as above gives $$\begin{aligned}
\label{udav}
    &D^\sigma_{i,j}(\boldsymbol s)+\frac1q{{D'}^\sigma_{i,j}}- \psi_i(1 -\ell_{i,j}(\boldsymbol \mu))\Big(\frac{  \ell_{i,j}(\boldsymbol s)}q+\frac12\Big)=C^\sigma_{i,j}(\boldsymbol s)
  
\end{aligned}$$ where $$\begin{aligned}
    &C^\sigma_{i,j}(\boldsymbol s):=\sum_{g=1}^{q}B_1\Big(\frac{\langle g-\ell_{i,j}(\boldsymbol s)\rangle}q\Big) \psi_i\Big(\frac{\langle gp -\ell_{i,j}(\boldsymbol u)\rangle -\ell_{i,j}(\boldsymbol \mu)}q\Big)
  
\end{aligned}$$ so that one finds $$\begin{aligned}
    \sigma\big(S_n^q\big)&=\exp(- q E/2)\bigg(\sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}}\exp\bigg(\sum_{i=1}^4\sum_{j=1}^{m_i}C^\sigma_{i,j}(\boldsymbol s)\bigg)\omega_{\boldsymbol s-\overline{p} \boldsymbol u,n}\bigg)^q.
  
\end{aligned}$$ By the change of variables $g\to g+\overline p\ell_{i,j}(\boldsymbol u)$ one obtains $C^\sigma_{i,j}(\boldsymbol s)=C(\boldsymbol s-\overline p\boldsymbol u)$, so that, after the change of variables $\boldsymbol s\to \boldsymbol s+\overline p \boldsymbol{u}$, one obtains $\sigma(S_n^q)=S_n^q$, and so $S_n^q \in F_{K, q}$, as desired.

Now, assume $S_{n'}\neq0$. By [\[seq\]](#seq){reference-type="eqref" reference="seq"} we have $$\begin{aligned}
    S_n^{-1}S_{n'}&=\bigg(\sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}} \exp\Big(\sum_{i=1}^4\sum_{j=1}^{m_i}D_{i,j}(\boldsymbol s)\Big)\omega_{\boldsymbol s,n}\bigg)^{-1} \sum_{\boldsymbol s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}} \exp\Big(\sum_{i=1}^4\sum_{j=1}^{m_i}D_{i,j}(\boldsymbol s)\Big)\omega_{\boldsymbol s,n'}. 
  
\end{aligned}$$ and so $S_n^{-1}S_{n'}\in {\tilde F}_{K, q}$. Moreover, given an automorphism $\sigma$ as in [\[galau\]](#galau){reference-type="eqref" reference="galau"}, one shows as above that $\sigma(S_n^{-1}S_{n'})=S_n^{-1}S_{n'}$ and so $S_n^{-1}S_{n'}\in F_{K, q}$. ◻
:::

::: remark
[]{#c45 label="c45"} The constant term in Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"} can be worked out from the arguments above as an explicit product of algebraic numbers. In the case $K = 4_1$, we obtain $$\begin{aligned}
  C_{4_1}(\alpha)D_{4_1,0}(\alpha) = {}&{} c \delta_{4_1}^{-1/2} \Lambda_{4_1, \alpha}^{1/c}, \\
  \delta_{4_1} = {}& i\sqrt{3}, \\
  \Lambda_{4_1,\alpha}^{1/c} = {}&{} \Big(\prod_{g=1}^c \mathopen{}\mathclose\bgroup\originalleft|\omega_g\aftergroup\egroup\originalright|^{2g/c}\Big)\sum_{r=1}^c \prod_{g=1}^{r} \mathopen{}\mathclose\bgroup\originalleft|\omega_g\aftergroup\egroup\originalright|^2,
\end{aligned}$$ where $\omega_g = 1-\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(g\alpha - \tfrac5{6c})$. In the case of $K = 5_2$, let $\tau \approx 0.665 + 0.562i$ solve $\tau^3-\tau+1 =0$, and let $\mu_1 \approx 0.224 + 0.045i$ and $\mu_2 \approx 0.164-0.067i$ be such that $\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\mu_1) = \tau^2$ and $\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\mu_2) = \tau^2+\tau$. Then $$\begin{aligned}
  C_{5_2}(\alpha)D_{5_2,0}(\alpha) = {}&{} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\frac{\mathop{\mathrm{s}}(\alpha)}2\Big) c^{1/2} \delta_{5_2}^{-1/2} \Lambda_{5_2, \alpha}^{1/c}, \\
  \delta_{5_2} = {}& 3\tau-2\tau^2, \\
  \Lambda_{5_2,\alpha}^{1/c} = {}&{} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\mu_1\frac{c+1}{2c}\Big) \Big(\prod_{g=1}^c \omega_g^{-g/c}\chi_g^{-2g/c}\Big) \times \\
  &{} \times\sum_{r_1, r_2 =1}^c \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\frac{\mu_1(r_1+r_2) + \mu_2 r_1}c + \frac{r_1}2 - \frac{\alpha}2 r_1(1+r_1+2r_2)\Big) \Big(\prod_{g=1}^{r_1} \omega_g^{-1}\Big) \Big(\prod_{g=1}^{r_2} \chi_g^{-2}\Big),
\end{aligned}$$ where $\omega_g = 1-\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(-g\alpha + \tfrac{\mu_1}c)$ and $\chi_g = 1-\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(g\alpha - \tfrac{\mu_2}c)$, and the logarithms are taken with principal determination. Note that $F_{5_2} = \mathbb{Q}(\tau)$ (see [@Ohtsuki52]).
:::

## Proof of Lemma [\[extra_terms\]](#extra_terms){reference-type="ref" reference="extra_terms"} {#prolex}

For $\lambda\in\mathbb{R}$, let $\Lambda$ denote the Lobachevsky function $$\Lambda(\lambda):=-\operatorname{Re}\Big(\mathop{\mathrm{{\mathfrak L}}}(\lambda)\Big)=-\int_0^{\{\lambda\}} \log(2\sin (\pi t))\mathrm{d}t.$$ where the last equality follows by [\[ff3\]](#ff3){reference-type="eqref" reference="ff3"} and [\[dig\]](#dig){reference-type="eqref" reference="dig"}. Note that $\Lambda$ is $1$-periodic and odd. We need to bound $$\begin{aligned}
  W_K(\boldsymbol \lambda):= -\sum_{i=1}^2\sum_{j=1}^{m_i}\Lambda(\ell_{i,j}(\boldsymbol \lambda)) + \sum_{i=3}^4\sum_{j=1}^{m_i} \Lambda(\ell_{i,j}(\boldsymbol \lambda))
\end{aligned}$$ for all ${\boldsymbol \lambda}\in [0, 1)^m$ such that $\ell_{i,j}({\boldsymbol \lambda}) \not\in [0, 1)$ for some $(i, j)$. Define $$M = \Lambda(1/6) \in[0.16, 0.162].$$ We will require the following simple inequalities: for $\alpha, \beta \in [0, 1]$, $$\begin{aligned}
  \mathopen{}\mathclose\bgroup\originalleft|\Lambda(\alpha)\aftergroup\egroup\originalright| \leq{}& M, \label{eq:ineqLambda-tot} \\
  \Lambda(\alpha) \leq {}& 0, & (\alpha \geq \tfrac12), \label{eq:ineqLambda-pos} \\
  2(\Lambda(\alpha) + \Lambda(\beta)) - \Lambda(\alpha + \beta) \leq {}& 4\Lambda(\tfrac14) < 0.59,  & (\alpha + \beta \leq 1), \label{eq:ineqLambda-sum-1} \\
  2(\Lambda(\alpha) + \Lambda(\beta)) - \Lambda(\alpha + \beta) \leq {}& M,  & (\alpha + \beta \geq 1). \label{eq:ineqLambda-sum-2} \\
  2(\Lambda(\alpha) + \Lambda(\beta)) - \Lambda(\alpha + \beta) \leq {}& 0.45,  & (\alpha + \beta \leq 1, \text{ and } \alpha \geq \tfrac12). \label{eq:ineqLambda-sum-3} \\
  \Lambda(\alpha) - \Lambda(\beta) \leq {}& 0.23, & (\alpha \leq \tfrac12\leq \beta, \text{ and } \beta \leq 2\alpha), \label{eq:ineqLambda-double}
\end{aligned}$$ The bound [\[eq:ineqLambda-double\]](#eq:ineqLambda-double){reference-type="eqref" reference="eq:ineqLambda-double"} is proved by optimizing at $\beta = \min(\frac56, 2\alpha)$. The maximum is achieved at a point $\alpha$ where $\rho = \sin(\pi \alpha)$ solves $\rho(1-\rho^2) = \frac18$. Similarly, the bound [\[eq:ineqLambda-sum-3\]](#eq:ineqLambda-sum-3){reference-type="eqref" reference="eq:ineqLambda-sum-3"} is proved by maximizing at $\alpha$ for which $\rho = \cos(\pi \alpha)$ solves $\rho = 2(1-\rho^2)$.

We consider the situation case by case; in each case, we work under the extra assumption that for some $(i, j)$, we have $\ell_{i,j}({\boldsymbol \lambda}) \not\in[0, 1)$.

-   Case $K = 5_2$. We have $$W_K({\boldsymbol \lambda}) = \Lambda(\lambda_1) +  2\Lambda(\lambda_2).$$ A bound of $2M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.12$ is enough. Assume $\lambda_1 + \lambda_2 \geq 1$. Then $\lambda_i \geq \frac12$ for some $i\in\{1, 2\}$, so that using [\[eq:ineqLambda-tot\]](#eq:ineqLambda-tot){reference-type="eqref" reference="eq:ineqLambda-tot"} and [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"}, we get $$W_K({\boldsymbol \lambda}) \leq 2M$$

-   Case $K = 6_1$. We have $$W_K({\boldsymbol \lambda}) = 2\Lambda(\lambda_1) + \Lambda(\lambda_2) + \Lambda(\lambda_3).$$ A bound of $3M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.01$ is enough. Thus, by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"}, we may assume $\lambda_i\leq \frac12$ for all $i\in\{1, 2, 3\}$. Assume $\lambda_1 + \lambda_2 + \lambda_3 \geq 1$. Then by concavity of $\Lambda$ on $[0, \frac12]$, we have $W_K({\boldsymbol \lambda}) \leq 2\Lambda(\lambda_1) + 2\Lambda(\frac12(\lambda_2 + \lambda_3))$. The bound [\[eq:ineqLambda-double\]](#eq:ineqLambda-double){reference-type="eqref" reference="eq:ineqLambda-double"} can then be applied with $(\alpha,\beta) = (\frac12(\lambda_2 + \lambda_3), 1-\lambda_1)$, and yields $W_K({\boldsymbol \lambda}) \leq 0.46 \leq 3M$. We find in all cases $$W_K({\boldsymbol \lambda}) \leq 3M.$$

-   Case $K = 6_2$. We have $$W_K({\boldsymbol \lambda}) = -2\Lambda(\lambda_1) + 2\Lambda(\lambda_2) + \Lambda(\lambda_3) + \Lambda(\lambda_1 - \lambda_2).$$ A bound of $4M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.05$ is enough. Because of [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"}, we may assume $\lambda_1>\frac12$ and $\lambda_2 \leq \frac12$. Then the case $\lambda_1 \leq \lambda_2$ is excluded, and we may assume $\lambda_2 + \lambda_3 \geq 1$. Then $\lambda_3 \geq \frac12$, and so by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} and [\[eq:ineqLambda-sum-1\]](#eq:ineqLambda-sum-1){reference-type="eqref" reference="eq:ineqLambda-sum-1"} (with $(\alpha, \beta) = (1-\lambda_1, \lambda_2)$), we obtain $W_K({\boldsymbol \lambda}) \leq 4\Lambda(\frac14)$. We obtain in all cases $$W_K({\boldsymbol \lambda}) \leq 4M.$$

-   Case $K = 6_3$. We have $$W_K({\boldsymbol \lambda}) = -2\Lambda(\lambda_2) + 2\Lambda(\lambda_1) + 2\Lambda(\lambda_3) + \Lambda(\lambda_2-\lambda_3) + \Lambda(\lambda_2-\lambda_1).$$ A bound of $5M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.09$ is enough. By symmetry, we may assume $\lambda_2 \leq \lambda_3$. Suppose first $\lambda_2\geq \frac12$. Then $\lambda_2-\lambda_3 \in [-\frac12, 0]$, so by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"}, $\Lambda(\lambda_2-\lambda_3) \leq 0$ and $\Lambda(\lambda_3)\leq 0$. We deduce $W_K({\boldsymbol \lambda}) \leq 5M$ by [\[eq:ineqLambda-tot\]](#eq:ineqLambda-tot){reference-type="eqref" reference="eq:ineqLambda-tot"}. Suppose on the other hand that $\lambda_2 < \frac12$. If $\lambda_3\geq \frac12$, then by [\[eq:ineqLambda-sum-1\]](#eq:ineqLambda-sum-1){reference-type="eqref" reference="eq:ineqLambda-sum-1"}-[\[eq:ineqLambda-sum-2\]](#eq:ineqLambda-sum-2){reference-type="eqref" reference="eq:ineqLambda-sum-2"} with $(\alpha, \beta) = (\lambda_1, 1-\lambda_2)$, we find $W_K({\boldsymbol \lambda}) \leq 4\Lambda(\frac14) + M \leq 5M$. If, finally, $\lambda_3 < \frac12$, then by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} we have $\Lambda(\lambda_2 - \lambda_3) \leq 0$, so that $W_K({\boldsymbol \lambda}) \leq 5M$. In all cases, we find $$W_K({\boldsymbol \lambda}) \leq 5M.$$

-   Case $K = 7_3$. We have $$W_K({\boldsymbol \lambda}) = -2\Lambda(\lambda_2) + \Lambda(\lambda_1) + \Lambda(\lambda_3) + \Lambda(\lambda_4).$$ A bound of $4M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.08$ is enough. Thus, by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"}, we may assume $\lambda_j < \frac12$ for all $j\in\{1, 3, 4\}$, and $\lambda_2 > \frac12$. Assume that $\lambda_2 \leq \lambda_3 + \lambda_4$. By [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} and the concavity of $\Lambda$ on $[0, \frac12]$, we have $$W_K({\boldsymbol \lambda}) \leq -2\Lambda(\lambda_2) + \Lambda(\lambda_3) + \Lambda(\lambda_4) + M \leq 2\Big(\Lambda\Big(\frac{\lambda_3 + \lambda_4}2\Big) - \Lambda(\lambda_2)\Big) + M.$$ By [\[eq:ineqLambda-double\]](#eq:ineqLambda-double){reference-type="eqref" reference="eq:ineqLambda-double"} with $\beta = \frac12(\lambda_3 + \lambda_4)$, we obtain $W_K({\boldsymbol \lambda}) \leq 0.46 +M\leq 4M$. We deduce that in all cases, $$W_K({\boldsymbol \lambda}) \leq 4M.$$

-   Case $K = 7_4$. We have $$W_K({\boldsymbol \lambda}) = -\Lambda(\lambda_2 + \lambda_3) + \Lambda(\lambda_1) + 2\Lambda(\lambda_2) + 2\Lambda(\lambda_3) + \Lambda(\lambda_4).$$ A bound of $5M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.01$ is enough. By [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} and [\[eq:ineqLambda-tot\]](#eq:ineqLambda-tot){reference-type="eqref" reference="eq:ineqLambda-tot"} we may assume without loss of generality $\lambda_2, \lambda_3 < \frac12$. Moreover, by [\[eq:ineqLambda-sum-1\]](#eq:ineqLambda-sum-1){reference-type="eqref" reference="eq:ineqLambda-sum-1"} (note that $0.59 \leq 4M$), we always have $W_K({\boldsymbol \lambda}) \leq 4M + \Lambda(\lambda_1) + \Lambda(\lambda_4)$, and so we may assume $\lambda_1, \lambda_4 < \frac12$ as well. But then, neither of the cases $\lambda_i + \lambda_j \geq 1$ can occur for $(i, j) \in \{(1, 2), (2, 3), (3, 4)\}$. We find in all cases that $$W_K({\boldsymbol \lambda}) \leq 5M.$$

-   Case $K = 7_5$. We have $$W_K({\boldsymbol \lambda}) = -2\Lambda(\lambda_3) + 2\Lambda(\lambda_1) + \Lambda(\lambda_4) + \Lambda(\lambda_2 - \lambda_1) + \Lambda(\lambda_3 - \lambda_2).$$ A bound of $6M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.05$ is enough. We may assume $\lambda_3 > \frac12$ and $\lambda_1, \lambda_4 < \frac12$. Then the case $\lambda_3 \leq \lambda_4$ is excluded. Assume next $\lambda_2 \leq \lambda_1$. Then $\lambda_2 - \lambda_1 \in (-\frac12, 0]$, so that $\Lambda(\lambda_2-\lambda_1) \leq 0$. Similarly, if $\lambda_3 \leq \lambda_2$, then $\lambda_2 > \frac12$, and $\Lambda(\lambda_3 - \lambda_2) \leq 0$. In all cases, we find by [\[eq:ineqLambda-tot\]](#eq:ineqLambda-tot){reference-type="eqref" reference="eq:ineqLambda-tot"} and [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} that $$W_K({\boldsymbol \lambda}) \leq 6M.$$

-   Case $K = 7_6$. We have $$W_K({\boldsymbol \lambda}) = -\Lambda(\lambda_3 + \lambda_4) - \Lambda(\lambda_2 + \lambda_3) + 2\Lambda(\lambda_1) + \Lambda(\lambda_2-\lambda_1) + 2\Lambda(\lambda_3) + 2\Lambda(\lambda_4).$$ A bound of $0.45 + 4M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.03$ is enough; note that $0.59 + 3M < 0.45 + 4M$. In particular, we may assume that $\lambda_1 < \frac12$, since otherwise, by [\[eq:ineqLambda-pos\]](#eq:ineqLambda-pos){reference-type="eqref" reference="eq:ineqLambda-pos"} and [\[eq:ineqLambda-sum-1\]](#eq:ineqLambda-sum-1){reference-type="eqref" reference="eq:ineqLambda-sum-1"}-[\[eq:ineqLambda-sum-2\]](#eq:ineqLambda-sum-2){reference-type="eqref" reference="eq:ineqLambda-sum-2"}, we get $W_K({\boldsymbol \lambda}) \leq 0.59 + 2M$. Assume first $\lambda_3 + \lambda_4 \geq 1$. Then by [\[eq:ineqLambda-sum-2\]](#eq:ineqLambda-sum-2){reference-type="eqref" reference="eq:ineqLambda-sum-2"}, we obtain $W_K({\boldsymbol \lambda}) \leq 5M$, which is acceptable. Next, assume that $\lambda_2 + \lambda_3 \geq 1$. If $\lambda_3 \leq \frac12$, then $\lambda_2 + \lambda_3 \in [1, \frac32]$ and by [\[eq:ineqLambda-sum-2\]](#eq:ineqLambda-sum-2){reference-type="eqref" reference="eq:ineqLambda-sum-2"} we have $W_K({\boldsymbol \lambda}) \leq 0.59 + 3M$. If on the other hand $\lambda_3 > \frac12$, then by [\[eq:ineqLambda-sum-3\]](#eq:ineqLambda-sum-3){reference-type="eqref" reference="eq:ineqLambda-sum-3"}, we get $W_K({\boldsymbol \lambda}) \leq 0.45 + 4M$. Both bounds are acceptable. Finally, assume that $\lambda_2 \leq \lambda_1$. Then $\lambda_2 - \lambda_1 \in (-\frac12, 0]$, and so $\Lambda(\lambda_2-\lambda_1) \leq 0$, and we again obtain $W_K({\boldsymbol \lambda}) \leq 0.59 + 3M$. We find in all cases that $$W_K({\boldsymbol \lambda}) \leq 0.45 + 4M.$$

-   Case $K = 7_7$. We have $$W_K({\boldsymbol \lambda}) = 2(\Lambda(\lambda_1)+\Lambda(\lambda_2)+\Lambda(\lambda_3)+\Lambda(\lambda_4)) - \Lambda(\lambda_1 + \lambda_2) - \Lambda(\lambda_2+\lambda_3) - \Lambda(\lambda_3+\lambda_4).$$ Assume $\lambda_i + \lambda_j \geq 1$ for some $(i, j)\in \{(1, 2), (2, 3), (3, 4)\}$. Then by [\[eq:ineqLambda-sum-2\]](#eq:ineqLambda-sum-2){reference-type="eqref" reference="eq:ineqLambda-sum-2"} and [\[eq:ineqLambda-tot\]](#eq:ineqLambda-tot){reference-type="eqref" reference="eq:ineqLambda-tot"}, we have $$W_K({\boldsymbol \lambda}) \leq 7M \leq \frac{\mathop{\mathrm{Vol}}(K)}{2\pi} - 0.08.$$

Summarizing the above, we find that in all cases considered for $K$, there holds $$\label{eq:values-EK}
  E_K:=\sup\{W_K(\boldsymbol \lambda)\mid \boldsymbol \lambda\in[0,1)^n,\ \exists i,j,\ \ell_{i,j}(\boldsymbol \lambda)\notin[0,1)\} \leq \frac{\mathop{\mathrm{Vol}}K}{2\pi}-0.01.$$ This proves Lemma [\[extra_terms\]](#extra_terms){reference-type="ref" reference="extra_terms"}.

::: remark
The analogue of Lemma [\[extra_terms\]](#extra_terms){reference-type="ref" reference="extra_terms"} for the knot $7_2$ is false as stated. It is likely that this obstacle can be lifted by processing the contour integral arguments underlying Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"} more carefully (see [@Ohtsuki7 Remark 8.1]). For sake of clarity, and since our main point is rather to stress how the modularity conjecture can be reduced to the arithmeticity conjecture, we chose to omit the case $K = 7_2$.
:::

## Proof of Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"} {#prolem}

::: remark
[]{#conjex label="conjex"} We have $\overline{\mathop{\mathrm{{\mathfrak L}}}(\lambda)}=-\mathop{\mathrm{{\mathfrak L}}}(1-\lambda)$ for $\lambda\in[0,1)$ and $\overline {{\mathfrak f}(z)}={\mathfrak f}(1-\overline z)$ for $z\in (\mathbb{C}\setminus \mathbb{R})\cup(0,1)$. In particular we can write the conjugates of $\Phi_{r}(\lambda)$ and $g_d(\lambda)$ given in [\[defb\]](#defb){reference-type="eqref" reference="defb"} and [\[defg2\]](#defg2){reference-type="eqref" reference="defg2"} ([\[defg\]](#defg){reference-type="eqref" reference="defg"} if $\lambda=0$) as $$\begin{aligned}
    \overline{\Phi_{r}(\lambda)} &= \exp\bigg(-\frac k{qd} \Big(\mathop{\mathrm{{\mathfrak L}}}(1-\lambda) +\frac{\pi i }{12}\Big)-\frac{\pi i d}{12kq}+ {{\mathcal E}_r^*(\lambda,d/k)} \bigg)\\
    {  {\mathcal E}_r^*(\lambda,d/k)}&:= \frac12 f\Big(\frac{q-\langle pr\rangle+\lambda}q\Big)+ \sum_{g=1}^q i\int_{0}^\infty   \bigg( \frac{{\mathfrak f}(\frac{q-g+\lambda}q - i\frac{dt}k)}{\ifthenelse{\equal{ -\frac{g\overline{p}-r}q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   -\frac{g\overline{p}-r}q\aftergroup\egroup\originalright)}{(  -\frac{g\overline{p}-r}q)}{(  -\frac{g\overline{p}-r}q)}{(  -\frac{g\overline{p}-r}q)}}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}-   \frac{{\mathfrak f}(\frac{q-g+\lambda}q + i\frac{dt}k)}{\ifthenelse{\equal{ \frac{g\overline{p}-r}q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   \frac{g\overline{p}-r}q\aftergroup\egroup\originalright)}{(  \frac{g\overline{p}-r}q)}{(  \frac{g\overline{p}-r}q)}{(  \frac{g\overline{p}-r}q)}}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}\bigg)\mathrm{d}{t},\quad (\lambda\neq0)
  
\end{aligned}$$ and ${\mathcal E}_r^*(0,d/k)=\overline { {\mathcal E}_r(0,d/k)}$. In particular, we can extend $\overline{\Phi_{r}(\lambda)}$ to a holomorphic function of $\lambda$ in the strip $0<\operatorname{Re}(\lambda)<1$.
:::

In the following lemmas we give some properties of the expansion of ${\mathcal E}_r$ and ${\mathcal E}_r^*$.

::: lemma
[]{#expg0 label="expg0"} Assume $\operatorname{Re}(\lambda)\in(\varepsilon,1-\varepsilon)$ with $\varepsilon\in(0,1/2)$ and let $s\in\mathbb{Z}/q\mathbb{Z}$. Then, for all $M\geq0$ uniformly in $\lambda$ we have $$\begin{aligned}
 \label{gexp}
    {\mathcal E}_s(\lambda,d/k)=\sum_{\ell=0}^M\Big(\frac {qd}k\Big)^\ell {\mathcal E}_{s,\ell}(\lambda) +O_\varepsilon\Big(\frac {qd}k\Big)^{M+1},\quad
    {\mathcal E}_s^*(\lambda,d/k)=\sum_{\ell=0}^M\Big(\frac {qd}k\Big)^\ell {\mathcal E}_{s,\ell}^*(\lambda) +O_\varepsilon\Big(\frac {qd}k\Big)^{M+1},
  
\end{aligned}$$ where $$\begin{aligned}
    {\mathcal E}_{0,\ell}(\lambda)&:=
    \sum_{g=1}^q f\Big(\frac{g-\lambda}q \Big)  B_{1}\Big( \frac{\langle g\overline{p}-s\rangle }q\Big),\qquad
    {\mathcal E}^*_{0,\ell}(\lambda):=
    \sum_{g=1}^q f\Big(\frac{g-\lambda}q \Big)  B_{1}\Big( \frac{\langle g\overline{p}-s\rangle }q\Big),\\
    {\mathcal E}_{s,\ell}(\lambda)&:=  \frac{(-1)^\ell}{q^\ell (\ell+1)!} \sum_{g=1}^q{\mathfrak f}^{(\ell)}\Big(\frac{g-\lambda}q \Big)   \tilde B_{\ell+1}\Big( \frac{g\overline{p}-s}q\Big),\qquad \ell\geq1,\\
    {\mathcal E}^*_{s,\ell}(\lambda)&:=  \frac{(-1)^\ell}{q^\ell (\ell+1)!} \sum_{g=1}^q{\mathfrak f}^{(\ell)}\Big(\frac{1-g+\lambda}q \Big)   \tilde B_{\ell+1}\Big( \frac{g\overline{p}-s}q\Big),\qquad \ell\geq1.
  
\end{aligned}$$
:::

::: proof
*Proof.* For $\operatorname{Re}(\lambda)\in(\varepsilon,1-\varepsilon)$ we have $\inf_{g\in\mathbb{Z}}\|\frac{g-\lambda}q\| \gg_\varepsilon 1$. Thus, since $$\begin{aligned}
    {\mathfrak f}'(z) = \pi (\cot(\pi z)+i),\qquad {\mathfrak f}^{(\nu)}(z) = (-1)^{\nu-1}(\nu-1)! \sum_{n\in\mathbb{Z}} \frac{1}{(z-n)^\nu},\qquad (z\notin\mathbb{Z},\ \nu\geq2), 
  
\end{aligned}$$ we have that ${\mathfrak f}^{(\nu)}(\frac{g-\lambda+it}q)\ll_{q,\nu,\varepsilon} (1+|t|^\varepsilon)$ for all $\nu\geq0$, $t\in\mathbb{R}$. The Lemma then follows immediately by expanding in Taylor series and applying Lemma [\[lem:B-integral\]](#lem:B-integral){reference-type="ref" reference="lem:B-integral"}. ◻
:::

::: lemma
[]{#expg label="expg"} Assume $\operatorname{Re}(\tilde \lambda)\in(0,1)$ and let $s\in\mathbb{Z}/q\mathbb{Z}$. Let $h_{s,\ell}$ be either ${\mathcal E}_{s,\ell}$ or ${\mathcal E}^*_{s,\ell}$. Then, for all $\ell,M\geq0$, and all $\lambda$ in a neighborhood of $\tilde\lambda$, we have $$\begin{aligned}
\label{exp1}
    h_{s,\ell}(\lambda)&= \sum_{v=0}^M (2\pi i)^{\ell+v} C_{s,\ell,v}(\tilde \lambda)(\lambda-\tilde \lambda)^v+O(|\lambda-\tilde \lambda|^{M+1}),
  
\end{aligned}$$ where, for $(v,\ell)=(0,0)$, $$\begin{aligned}
    C_{0,0}(\tilde \lambda)&= \sum_{g=1}^q f\Big(\frac{g-\tilde\lambda}q \Big)  B_{1}\Big( \frac{\langle g\overline{p}-s\rangle }q\Big),&& \text{if }h_{s,\ell}={\mathcal E}_{s,\ell}\label{exp01}\\
    C_{0,0}(\tilde \lambda)&= \sum_{g=1}^q f\Big(\frac{q-g+\tilde\lambda}q \Big)  B_{1}\Big( \frac{\langle g\overline{p}-s\rangle }q\Big),&& \text{if }h_{s,\ell}={\mathcal E}^*_{s,\ell}.\label{exp02}
  
\end{aligned}$$ Moreover, for $(v,\ell)\neq(0,0)$ we have $C_{s,\ell,v}(\tilde \lambda)\in\mathbb{Q}(\ifthenelse{\equal{\tfrac{1}{q}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac{1}{q}\aftergroup\egroup\originalright)}{( \tfrac{1}{q})}{( \tfrac{1}{q})}{( \tfrac{1}{q})}},\ifthenelse{\equal{\tfrac{\tilde\lambda}{q}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac{\tilde\lambda}{q}\aftergroup\egroup\originalright)}{( \tfrac{\tilde\lambda}{q})}{( \tfrac{\tilde\lambda}{q})}{( \tfrac{\tilde\lambda}{q})}})$; also if $$\sigma\in \textnormal{Gal}\big(\mathbb{Q}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\tfrac{1}{q}),\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\tfrac{\tilde\lambda}{q}))/\mathbb{Q}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\tfrac{1}{q}),\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}(\tilde\lambda))\big)$$ is such that $\sigma(\ifthenelse{\equal{\tilde\lambda/q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tilde\lambda/q\aftergroup\egroup\originalright)}{( \tilde\lambda/q)}{( \tilde\lambda/q)}{( \tilde\lambda/q)}})=\ifthenelse{\equal{\tilde(\lambda+u)/q}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tilde(\lambda+u)/q\aftergroup\egroup\originalright)}{( \tilde(\lambda+u)/q)}{( \tilde(\lambda+u)/q)}{( \tilde(\lambda+u)/q)}}$ for some $u\in\{0,\dots,q-1\}$, then $$\begin{aligned}
\label{pdc}
    \sigma(C_{s,\ell,v}(\tilde \lambda))=C_{s-u\overline p,\ell,v}(\tilde \lambda).
  
\end{aligned}$$
:::

::: proof
*Proof.* The equations [\[exp1\]](#exp1){reference-type="eqref" reference="exp1"}-[\[exp02\]](#exp02){reference-type="eqref" reference="exp02"} follow immediately by Taylor expansion. Moreover, if $\ell\geq1$, $v\geq0$ and $h_{r,\ell}={\mathcal E}_{r,\ell}$ then $$\begin{aligned}
    C_{r,\ell,v}(\tilde \lambda)=  \frac{(-1)^\ell}{q^\ell (\ell+1)!}  \frac{1}{q^v v!}\sum_{g=1}^q (2 \pi i)^{\ell+v}{\mathfrak f}^{(\ell+v)}\Big(\frac{g-\tilde \lambda}q \Big)   \tilde B_{\ell+1}\Big( \frac{g\overline{p}-r}q\Big),
  
\end{aligned}$$ so that $C_{r,\ell,v}(\tilde \lambda)\in \mathbb{Q}(\ifthenelse{\equal{\tfrac{1}{q}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac{1}{q}\aftergroup\egroup\originalright)}{( \tfrac{1}{q})}{( \tfrac{1}{q})}{( \tfrac{1}{q})}},\ifthenelse{\equal{\tfrac{\tilde\lambda}{q}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac{\tilde\lambda}{q}\aftergroup\egroup\originalright)}{( \tfrac{\tilde\lambda}{q})}{( \tfrac{\tilde\lambda}{q})}{( \tfrac{\tilde\lambda}{q})}})$ since ${\mathfrak f}'(z) = \pi (\cot(\pi z)+i)= \frac{2 i}{1-\ifthenelse{\equal{-z}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -z\aftergroup\egroup\originalright)}{( -z)}{( -z)}{( -z)}}}$ and [\[pdc\]](#pdc){reference-type="eqref" reference="pdc"} follows by the change of variables $g\to g+j$. The case $\ell=0$, $v\geq1$ and the analogous property for $\tilde {\mathcal E}_{r,\ell}$ can be proven in the same way. ◻
:::

::: proof
*Proof of Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"}.* As mentioned in the introduction, for the knots under consideration, the asymptotic expansion stated in Lemma [\[main_terms\]](#main_terms){reference-type="ref" reference="main_terms"} will be essentially reduced to a proof of the asymptotic expansion in the volume conjecture for those knots. Thus, we shall frequently refer to [@Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7] where this asymptotic expansion was proven for hyperbolic knots with $5,6$ and $7$ crossings. The case of the knot $4_1$ is easier, since there is a dominant critical point on $(0,1)$, and the method of stationary phase can be applied, similarly as in the proof of Theorem [\[th:2\]](#th:2){reference-type="ref" reference="th:2"} below. Thus, we will focus here on the case $K\neq 4_1$. Recall also that we assume $K\neq 7_2$.

By Remark [\[conjex\]](#conjex){reference-type="ref" reference="conjex"}, for $0\leq \ell_{i,j}(\boldsymbol L)<d$ we can write $J^{*}_K$ as $$\begin{aligned}
    \mathcal{J}^{*}_K(x ; \boldsymbol L,\boldsymbol s) =   \sum_{\substack{ {\boldsymbol r}d/k-\boldsymbol L\in \mathcal  D,\\  r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i}}
    \exp\Big(\frac{k}{qd}  V_{\boldsymbol s,d/k}(d{\boldsymbol r}/k -\boldsymbol L )\Big),
  
\end{aligned}$$ where $\mathcal D=\{\boldsymbol n\in [0,1)^m\mid \ell_{i,j}(\boldsymbol n)\in[0,1)\, \forall i,j\}$, $$\begin{aligned}
    V_{\boldsymbol s,\kappa}(\boldsymbol n):=\hat V(\boldsymbol n)+q\kappa \Big(U_{\boldsymbol s,\kappa}(\boldsymbol n)+\frac{ \pi i(m_1+m_4-m_2-m_3)}{12q}\kappa\Big)
  
\end{aligned}$$ and $$\begin{aligned}
    \hat V(\boldsymbol n)&=\sum_{j=1}^{m_1}\Big(\mathop{\mathrm{{\mathfrak L}}}(\ell_{1,j}(\boldsymbol n))+\frac{\pi i}{12}\Big) -\sum_{j=1}^{m_2}\Big(\mathop{\mathrm{{\mathfrak L}}}(1-\ell_{2,j}(\boldsymbol n))+\frac{\pi i}{12}\Big) \\
    &\quad-\sum_{j=1}^{m_3}\Big(\mathop{\mathrm{{\mathfrak L}}}(\ell_{3,j}(\boldsymbol n))+\frac{\pi i}{12}\Big)+\sum_{j=1}^{m_4}\Big(\mathop{\mathrm{{\mathfrak L}}}(1-\ell_{4,j}(\boldsymbol n))+\frac{\pi i}{12}\Big),\\
    U_{\boldsymbol s,\kappa}(\boldsymbol n)&= \sum_{j=1}^{m_1}{\mathcal E}_{\boldsymbol s}(\ell_{1,j}(\boldsymbol n),\kappa)+\sum_{j=1}^{m_2}{\mathcal E}_{\boldsymbol s}^*(\ell_{2,j}(\boldsymbol n),\kappa)-\sum_{j=1}^{m_3}{\mathcal E}_{\boldsymbol s}(\ell_{3,j}(\boldsymbol n),\kappa)-\sum_{j=1}^{m_4}{\mathcal E}_{\boldsymbol s}^*(\ell_{4,j}(\boldsymbol n),\kappa).
  
\end{aligned}$$ The function $\hat V(\boldsymbol n)$ coincides, up to conjugation, with the limiting value of the potential function of the hyperbolic structure of the knot complement given in [@Ohtsuki52 (10)], [@OhtsukiYokota6 p.297, p.308, p.322] and [@Ohtsuki7 p.12, p.26, p.38, p.50, p.63]. We remark that the expressions for $\hat V$ given there differ from the one we have here, however it is easy to see that the two expressions actually coincide upon using the dilogarithm identity (or the formula [\[ff1\]](#ff1){reference-type="eqref" reference="ff1"}) $$\mathop{\mathrm{{\mathfrak L}}}(1-\lambda)+\mathop{\mathrm{{\mathfrak L}}}(\lambda)=-\pi i B_2(\lambda).$$ In [@Ohtsuki52 Lemma 2.1], [@OhtsukiYokota6 §3.2, §4.2, §5.2] and [@Ohtsuki7 §3.2, §4.2, §5.2, §6.2, §7.2] it was shown that for all knots under consideration $\operatorname{Re}(\hat V)$ is smaller than $\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}$ on the boundary of $\mathcal D$. More precisely, there exists a domain $\mathcal D'\subset\mathcal D$ with $\textnormal{dist}(\mathcal D',\partial \mathcal D)>0$ such that $\operatorname{Re}(\hat V(\boldsymbol n))<\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}-\delta'$ for all $\boldsymbol n\in \mathcal{D}\setminus\mathcal D'$ and some $\delta'>0$. Thus, by [\[bdfg\]](#bdfg){reference-type="eqref" reference="bdfg"}, we have $$\begin{aligned}
    \mathcal{J}^{*}_K(\gamma, x;\boldsymbol L,\boldsymbol s) =   \sum_{\substack{ {\boldsymbol r}d/k-\boldsymbol L\in \mathcal  D',\\  r_i\equiv s_i ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)},\ \forall i}}
    \exp\Big(\frac{k}{qd}  V_{\boldsymbol s,d/k}(d{\boldsymbol r}/k -\boldsymbol L )\Big)+O\bigg(k^m\exp\Big(\Big(\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}-\delta'\Big)\frac{k}{qd}\Big)\bigg).
  
\end{aligned}$$ We now apply Poisson summation formula in the form of [@Ohtsuki52 Proposition 4.6] (with $k/d$ playing the role of $N$ of [@Ohtsuki52]). Note that our sum are restricted to arithmetic progressions modulo $q$; since $q$ is fixed, this does not affect the argument. By [@Ohtsuki52 Lemma 5.1], [@OhtsukiYokota6 Lemma 3.4, 4.3 and 5.2] and [@Ohtsuki7 Lemma 3.2, 4.2, 5.2, 6.2 and 7.2] we have that $\hat V(\boldsymbol n)-\frac{\mathop{\mathrm{Vol}}(K)}{2\pi }$ satisfies the conditions (41)-(42) of [@Ohtsuki52 Proposition 4.6] and by [@Ohtsuki52 Remark 4.8] and Lemma [\[expg0\]](#expg0){reference-type="ref" reference="expg0"} we can apply Proposition 4.6 of [@Ohtsuki52] to $V_{\boldsymbol s,\boldsymbol L,d/k}(\boldsymbol n)$ rather than $\hat V(\boldsymbol n)$. We find $$\begin{aligned}
\label{intf}
    \mathcal{J}^{*}_K(\gamma, x; \boldsymbol L,\boldsymbol s) = \Big(\frac k{qd}\Big)^m   \iint_{\mathcal D'}
    \exp\Big(\frac{k}{qd}  V_{\boldsymbol s,d/k}(\boldsymbol z)\Big)\mathrm{d}\boldsymbol z+O\bigg(\exp\Big(\Big(\frac{\mathop{\mathrm{Vol}}(K)}{2\pi}-\delta''\Big)\frac{k}{qd}\Big)\bigg),
  
\end{aligned}$$ for some $\delta''>0$, where the extra factor $q^{-m}$ comes from the restriction to the congruence classes. One can then apply the saddle point method in the form of [@Ohtsuki52 Proposition 3.5 and Remark 3.6] as done in [@Ohtsuki52 p.705-706 and §5.2] (cf. also [@Yokota2011]), [@OhtsukiYokota6 p.297 and §3.5; p.309 and §4.5; p.47 and §5.5] and [@Ohtsuki7 p.13 and §3.5; p.26 and §4.5; p.39 and §5.5; p.50 and §6.5; p.64 and §7.5]. Notice that both $V_{\boldsymbol s,d/k}(\boldsymbol z)$ and the corresponding functions studied in these papers converge uniformly to $\hat V$, so the same computations apply. We then find that for all $N\geq1$ the first summand on the right of [\[intf\]](#intf){reference-type="eqref" reference="intf"} is equal to $$\begin{aligned}
    \Big(\frac{2\pi k}{ qd}\Big)^{m/2}\frac1{\det(-\operatorname{Hess})^{1/2}}
    \exp\Big(\frac{k}{qd} \hat  V(\boldsymbol \mu)+C(\boldsymbol s)\Big)\bigg(1+\sum_{n=1}^N\omega_{\boldsymbol s,n}\big(\frac{2\pi i qd}{k}\Big)^n+O\Big(\frac{1}{k^{N+1}}\Big)\bigg)
  
\end{aligned}$$ where $\boldsymbol \mu$ is a critical point of $\hat V(\boldsymbol z)$ (and thus satisfies [\[spe\]](#spe){reference-type="eqref" reference="spe"}) with $0<\operatorname{Re}(\ell_{i,j}(\boldsymbol \mu))<1$ for all $i,j$, such that $\hat V(\boldsymbol \mu)=\frac{\mathop{\mathrm{Vol}}(K)-i\mathop{\mathrm{cs}}(K)}{2\pi }$ and $\operatorname{Hess}$ is the Hesse matrix of $\hat V$ at $\bm\mu$. In particular, $\det(-\operatorname{Hess})\in (\pi i)^m F_{K}$. By Lemma [\[expg\]](#expg){reference-type="ref" reference="expg"} the coefficients $\omega_{\boldsymbol s,n}$ are in ${\tilde F}_{K, q}$ for all $n\geq1$ and if $\sigma$ is as in [\[galau\]](#galau){reference-type="eqref" reference="galau"}, then $\sigma(\omega_{\boldsymbol s,n})=\omega_{\boldsymbol s-\overline p\boldsymbol u,n}$. Finally, by [\[exp01\]](#exp01){reference-type="eqref" reference="exp01"}-[\[exp02\]](#exp02){reference-type="eqref" reference="exp02"} we have that $C(\boldsymbol s)$ is as in [\[defcs\]](#defcs){reference-type="eqref" reference="defcs"}. ◻
:::

# Proof of Theorems [\[th:2\]](#th:2){reference-type="ref" reference="th:2"} {#pmt2}

We proceed in a similar way as in the proof of Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"}. For $x=\overline{h}/k$, with $(h,k)=1$ and $1\leq h<k$, we write $\mathcal{J}_{4_1}( x)$ as in [\[exja\]](#exja){reference-type="eqref" reference="exja"} and we divide the sum into congruence classes modulo $h$, that is we write $$\begin{aligned}
\label{splj2}
  \mathcal{J}_{4_1}(\overline{h}/k) = k^{\frac{3-m}2} \sum_{0\leq s\leq h-1}\mathcal{J}_{4_1}(\overline{h}/k; s)
\end{aligned}$$ where, for $0\leq s\leq h-1$, we write $$\begin{aligned}
\label{splik2}
  \mathcal{J}_{4_1}(\overline{h}/k; s) =   \sum_{\substack{0\leq r<k,\\ r\equiv s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}}{| [ \overline{h}/k]_{r}|^2}.
\end{aligned}$$ with $[\cdot]_r$ as in [\[sb\]](#sb){reference-type="eqref" reference="sb"}. We apply Theorem [\[thp\]](#thp){reference-type="ref" reference="thp"}, which for $0\leq s<h$, $s\equiv r~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$, gives $$\begin{aligned}
\label{arf2}
  | [\overline{h}/k]_{r}|^2 = | [\overline{k}/h]_{s}|^2 \Phi_s^\dagger(r /k)\exp\Big(- \frac {2\pi r}{hk}c_0({\overline k}/h)+{\mathcal E}^\dagger_s(r/k)\Big)
\end{aligned}$$ for some ${\mathcal E}^\dagger_s(r/k)$ satisfying $|{\mathcal E}^\dagger_s(r/k)|\ll E(h,k)$ for all $0\leq r<k$, where $$\begin{aligned}
  E(h,k):= 1+ \log \frac kh+\frac{k}{h^2}+\max_{r'=0,\dots, h-1}\Big|\sum_{\substack{1\leq n\leq r'}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{ n}{hk}\Big|, 
\end{aligned}$$ (note that if $0\leq r_0 <h$ with $r_0\equiv r ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~q\aftergroup\egroup\originalright)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}{(\textnormal{mod}~q)}$, then $\frac{r}k \in[\frac{r_0}k, 1-\frac hk(1-\{\frac{r_0-k}h\})]$), and where for $\lambda\in[0,1]$, we define $$\begin{aligned}
  \Phi_s^\dagger(\lambda) &= \exp\bigg(2\frac k{h}\operatorname{Re}\Big(\mathop{\mathrm{{\mathfrak L}}}(\lambda) \Big)\bigg)=\exp\bigg(\frac k{h}\int_0^\lambda\log(4\sin(\pi t)^2)\,dt\bigg),
\end{aligned}$$ by [\[ff3\]](#ff3){reference-type="eqref" reference="ff3"} and [\[dig\]](#dig){reference-type="eqref" reference="dig"}. By positivity, it follows that $$\begin{aligned}
\label{erfac}
  \mathcal{J}_{4_1}(\overline{h}/k; s)= \exp\big(O(E(h,k)+|c_0({\overline k}/h)|/h)\big)|[ \overline{k}/h]_{ s}|^2
  \sum_{\substack{0\leq r<k\\ r\equiv s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}}{ \Phi_s^\dagger(r/k)}.
\end{aligned}$$ Now, the function $\lambda\to \int_0^\lambda\log(4\sin(\pi t)^2)\,dt$ is continuous on $[0,1]$ and it has a unique maximum in this interval, located at $\lambda=5/6$. Moreover, it can be expanded in a neighborhood of this point as $$\begin{aligned}
\label{apin}
  \int_0^\lambda\log(4\sin(\pi t)^2)\mathrm{d}t=\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}-\pi\sqrt 3(\lambda-\tfrac56)^2+O(|\lambda-\tfrac56|^3).
\end{aligned}$$ since $\int_0^{5/6}\log(4\sin(\pi t)^2)\mathrm{d}t=\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}$. It follows that $$\begin{aligned}
\label{eastp}
  \sum_{\substack{0\leq r<k\\ r\equiv s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}} \Phi_s^\dagger(r/k)=\sqrt{\frac{k}{h\sqrt 3}}\exp\Big(\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}\frac kh\Big)(1+O(h/k))=\exp\Big(\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}\frac kh+O(\log (1+k/h))\Big),
\end{aligned}$$ where the first step is justified in a standard way [@FlajoletSedgewick2009 p.517], e.g. by smoothly restricting the sum to the terms where $r/k$ is in a neighborhood of $5/6$, using [\[apin\]](#apin){reference-type="eqref" reference="apin"} and applying the Poisson summation formula. The second step instead follows immediately by positivity.

By [\[splj2\]](#splj2){reference-type="eqref" reference="splj2"}, [\[erfac\]](#erfac){reference-type="eqref" reference="erfac"} and [\[eastp\]](#eastp){reference-type="eqref" reference="eastp"} we then find $$\begin{aligned}
\label{exts}
  \mathcal{J}_{4_1}(\overline{h}/k)=  \mathcal{J}_{4_1}(\overline{k}/h)\exp(O(E(h,k)+|c_0({\overline k}/h)|/h)),
\end{aligned}$$ as desired.

With a similar argument we can prove the following theorem, which deals with the case where the dominating term on the right hand side of [\[arf2\]](#arf2){reference-type="eqref" reference="arf2"} is $\exp(- \frac {2\pi r}{hk}c_0({\overline k}/h))$.

::: theo
[]{#th:4 label="th:4"} Let $1\leq h\leq k$ with $(h,k)=1$ and assume $\mathop{\mathrm{c_0}}({\overline k}/h)<0$. Then, $$\label{eq:srf}
    \begin{split}
      \log |\mathcal{J}_{4_1,0}\big(\ifthenelse{\equal{{\overline{h}}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline{h}}/k\aftergroup\egroup\originalright)}{( {\overline{h}}/k)}{( {\overline{h}}/k)}{( {\overline{h}}/k)}}\big)|&=\log |\mathcal{J}_{4_1,0}\big(\ifthenelse{\equal{{\overline k}/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline k}/h\aftergroup\egroup\originalright)}{( {\overline k}/h)}{( {\overline k}/h)}{( {\overline k}/h)}}\big)|- \frac{2\pi}{h} \mathop{\mathrm{c_0}}\big({\overline k}/h\big)+O\Big(\frac k h+\max_{0\leq r' < h}\Big|\sum_{\substack{1\leq n\leq r'}}\cot\Big(\pi\frac{n\overline k }h\Big)\frac{ n}{hk}\Big|\Big).
    \end{split}$$
:::

To prove [\[eq:srf\]](#eq:srf){reference-type="eqref" reference="eq:srf"} first we observe we can assume $k>2h$ since otherwise the result is trivial. Also, we observe that, bounding trivially $\Phi_s^\dagger$, one can write [\[arf2\]](#arf2){reference-type="eqref" reference="arf2"} as $$\begin{aligned}
  | [\overline{h}/k]_{r}|^2 = | [\overline{k}/h]_{s}|^2 \exp\Big(- \frac {2\pi r}{hk}c_0({\overline k}/h)+O(E(h,k)+k/h)\Big)
\end{aligned}$$ and so $$\begin{aligned}
  \mathcal{J}_{4_1}(\overline{h}/k; s)= \exp\big(O(E(h,k)+k/h)\big) |[ \overline{k}/h]_{ s}|^2
  \sum_{\substack{0\leq r<k\\ r\equiv s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}}\exp\Big(- \frac {2\pi r}{hk}c_0({\overline k}/h)\Big).
\end{aligned}$$ Now, if $x\geq0$, we have $\sum_{0\leq n\leq m}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{nx}=\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{mx+O(m)}$, and thus if $x$ is large the sum is roughly dominated by the last term. Then for $c_0({\overline k}/h)<0$, we have $$\begin{aligned}
  \sum_{\substack{0\leq r<k\\ r\equiv s ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}}\exp\Big(- \frac {2\pi r}{hk}c_0({\overline k}/h)\Big)=\exp\Big(- \frac {2\pi r'}{hk}c_0({\overline k}/h)+O(k/h)\Big)
\end{aligned}$$ where $r'$ is the maximum integer satisfying $0\leq r'< k$ with $r'\equiv s~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$. Then, $k-h\leq r'<k$ and so in particular $\frac{r'}{hk}c_0({\overline k}/h)=\frac{1}{h}c_0({\overline k}/h)+O(\frac{1}{k}|c_0({\overline k}/h)|)$ and the result follows.

# Proof of Theorem [\[theo:cfep\]](#theo:cfep){reference-type="ref" reference="theo:cfep"} {#fise}

Before starting, we state some basic properties of continued fractions (see [@Kin] for a reference). Given $h/k\in\mathbb{Q}\cap(0,1)$ with $h,k\in\mathbb{N}$, $(h,k)=1$, we denote by $[0;b_1,\dots,b_r]$ the continued fraction expansion of $h/k$. Then for $0\leq s\leq r$ the convergents of $h/k$ are the fractions $[0;b_1,\dots,b_s]=\frac{u_s}{v_s}$ with $(u_s,v_s)=1$ (as usual $u_0/v_0=0/1$, $v_{-1}:=0$, $u_{-1}:=1$); the $v_s$ are called the partial quotients. The partial quotients satisfy the bounds $v_s\ll 2^{-s/2}$, $v_{r-s}\ll  k2^{-s/2}$ for $0\leq s\leq r$, and $v_{s}/v_{s-1}\leq b_{s}+1$ for $1\leq s\leq r$. Also, $r\ll \log k$. For all $1\leq s\leq r$ we have $v_su_{s-1}-v_{s-1}u_s=(-1)^{s}$ and so $\frac{\overline{v_{s-1}}}{v_s}\equiv (-1)^{s+1}\frac{u_s}{v_s}~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~1\aftergroup\egroup\originalright)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}$. Moreover, if $1\leq h'\leq k$ is such that $h'\equiv (-1)^{r+1}\overline h~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~k\aftergroup\egroup\originalright)}{(\textnormal{mod}~k)}{(\textnormal{mod}~k)}{(\textnormal{mod}~k)}$, then the Euclid algorithm on $h'$ and $k$ can be written as $$\label{eq:aaa}
  \begin{aligned}
    &v_r=k,\qquad v_{r-1}= h',\\
    &v_{\ell+1}=b_{\ell+1}v_{\ell}+v_{\ell-1},\qquad \ell=0,\dots, r-1.\\
  \end{aligned}$$

The following technical result, proved in [@BettinDrappeaub], will be needed in the proof of Theorem [\[theo:cfep\]](#theo:cfep){reference-type="ref" reference="theo:cfep"}.

::: lemma
[]{#parcot label="parcot"} Let $1\leq h<k$ with $(h,k)=1$. Let $v_0,\dots,v_r$ be the partial quotients of $h/k$. Then uniformly for $1\leq c\leq k$, we have $$\begin{aligned}
    &\sum_{\substack{1\leq n\leq c}}\cot\Big(\pi\frac{n h }k\Big)\frac{ n}{k}\ll \sum_{m=0}^{r-1} v_m\log(v_{m+1}/v_{m})+k.
  
\end{aligned}$$
:::

::: proof
*Proof of Theorem [\[theo:cfep\]](#theo:cfep){reference-type="ref" reference="theo:cfep"}.* Since $J$ is even, applying repeatedly the reciprocity formula [\[eq:frf\]](#eq:frf){reference-type="eqref" reference="eq:frf"} and the recurrence relation [\[eq:aaa\]](#eq:aaa){reference-type="eqref" reference="eq:aaa"}, we see that for all $0\leq s\leq r$ $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ { h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   { h}/k\aftergroup\egroup\originalright)}{(  { h}/k)}{(  { h}/k)}{(  { h}/k)}}) = {}& \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ \overline{ v_{r-1}}/v_r}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   \overline{ v_{r-1}}/v_r\aftergroup\egroup\originalright)}{(  \overline{ v_{r-1}}/v_r)}{(  \overline{ v_{r-1}}/v_r)}{(  \overline{ v_{r-1}}/v_r)}}) = C\sum_{\ell=s+1}^{r}\bigg(\frac{v_{\ell}}{v_{\ell-1}}+E({v_{\ell-1}}/{v_{\ell}})\bigg)+    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ \overline{ v_{s-1}}/v_{s}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   \overline{ v_{s-1}}/v_{s}\aftergroup\egroup\originalright)}{(  \overline{ v_{s-1}}/v_{s})}{(  \overline{ v_{s-1}}/v_{s})}{(  \overline{ v_{s-1}}/v_{s})}}),
  
\end{aligned}$$ with $C=\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}$ and $E$ satisfying [\[eq:ber\]](#eq:ber){reference-type="eqref" reference="eq:ber"}. Now, by Lemma [\[parcot\]](#parcot){reference-type="ref" reference="parcot"} $$\begin{aligned}
    \sum_{\ell=1}^{r}\max_{r'=0,\dots,v_{\ell-1}-1}\Big|\sum_{\substack{1\leq n\leq r'}}\cot\Big(\pi\frac{n\overline v_{\ell-2} }{v_{\ell-1}}\Big)\frac{ n}{v_{\ell-1}^2}\Big|\ll
    \sum_{\ell=1}^{r} \sum_{m=0}^{\ell-2} \frac{v_m}{v_{\ell-1}}\log(v_{m+1}/v_{m})+\sum_{\ell=1}^{r}1/v_{\ell-1},
  
\end{aligned}$$ since $\tfrac{\overline v_{\ell-2} }{v_{\ell-1}}=(-1)^{\ell}\tfrac{u_{\ell-1} }{v_{\ell-1}}~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~1\aftergroup\egroup\originalright)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}$ and so its partial quotients are $v_0\dots,v_{\ell-1}$. The second sum is $O(1)$, whereas changing the order of summation and using $v_{\ell-1-n}\ll  v_{\ell-1}2^{-n/2}$, for $n\geq0$, we obtain $$\begin{aligned}
    \sum_{\ell=1}^{r} \sum_{m=0}^{\ell-2} \frac{v_m}{v_{\ell-1}}\log(v_{m+1}/v_{m})\ll  \sum_{m=0}^{r-2} \sum_{\ell=m+2}^{r}  2^{(m-\ell)/2}\log(v_{m+1}/v_{m})\ll\sum_{m=0}^{r-2} \log(v_{m+1}/v_{m}).
  
\end{aligned}$$ Now, we fix an $\varepsilon>1/k$ and we take $s$ to be the least integer in $\{1,\dots,r\}$ such that $v_{s}\geq1/\varepsilon$ and notice that, since $v_m\gg 2^{m/2}$, we have $s=O_\varepsilon(1)$. Then, the above computations and [\[eq:ber\]](#eq:ber){reference-type="eqref" reference="eq:ber"} give $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ { h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   { h}/k\aftergroup\egroup\originalright)}{(  { h}/k)}{(  { h}/k)}{(  { h}/k)}})= \sum_{\ell=s+1}^{r}\frac{v_{\ell}}{v_{\ell-1}}(C+O(\sqrt{\varepsilon}))+\sum_{\ell=1}^{r} O(\log(v_{\ell}/v_{\ell-1}))+    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{\pm{ u_{s}}/v_{s}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \pm{ u_{s}}/v_{s}\aftergroup\egroup\originalright)}{( \pm{ u_{s}}/v_{s})}{( \pm{ u_{s}}/v_{s})}{( \pm{ u_{s}}/v_{s})}}).
  
\end{aligned}$$ since $\tfrac{\overline v_{s-1} }{v_{s}}=\pm\tfrac{u_{s} }{v_{s}}~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~1\aftergroup\egroup\originalright)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}$ for $\pm1:=(-1)^{s-1}$. Now, if $s\geq1$, we have $\pm u_s/v_s=\gamma (b_s)$, where $\gamma:=(\begin{smallmatrix}\pm u_{s-1} & u_{s-2}\\ \pm v_{s-1} & v_{s-2}\end{smallmatrix})\in\textnormal{SL}(2,\mathbb{Z})$. Notice that by definition of $s$ all entries of $\gamma$ are bounded by $1/\varepsilon$. Thus, by Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"}, we have $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{\pm{ u_{s}}/v_{s}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \pm{ u_{s}}/v_{s}\aftergroup\egroup\originalright)}{( \pm{ u_{s}}/v_{s})}{( \pm{ u_{s}}/v_{s})}{( \pm{ u_{s}}/v_{s})}}) = Cb_s+O(\log b_s)+O_\varepsilon(1)=C\sum_{\ell=1}^s b_\ell+O(\log b_s)+O_\varepsilon(1),
  
\end{aligned}$$ since $s,v_{\ell-1}=O_\varepsilon(1)$ and so also $b_\ell=O_{\varepsilon}(1)$ for all $\ell\leq s-1$. Then, since $v_{\ell}/v_{\ell-1}=b_\ell+O(1)$ we find $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ { h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   { h}/k\aftergroup\egroup\originalright)}{(  { h}/k)}{(  { h}/k)}{(  { h}/k)}})=(C+O(\sqrt\varepsilon)) \sum_{\ell=1}^{r}(b_\ell+ O(\log b_\ell))+O(r)+O_\varepsilon(1).
  
\end{aligned}$$ Finally, we observe that $b_\ell+ O(\log b_\ell)=b_\ell(1+O(\sqrt\varepsilon))+O(1/\varepsilon)$. Thus, $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ { h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   { h}/k\aftergroup\egroup\originalright)}{(  { h}/k)}{(  { h}/k)}{(  { h}/k)}})=(C+O(\sqrt\varepsilon)) \sum_{\ell=1}^{r}b_\ell+O_\varepsilon(r)= \Sigma(h/k) \bigg(C +O(\sqrt\varepsilon)+O_\varepsilon\bigg(\frac{r(h/k)}{\Sigma(h/k)}\bigg)\bigg).
  
\end{aligned}$$ By hypothesis $r(h/k)/\Sigma(h/k)\to0$ and so [\[eq:cfef\]](#eq:cfef){reference-type="eqref" reference="eq:cfef"} follows by letting $\varepsilon\to0^+$ sufficiently slowly. Equation [\[eq:asy\]](#eq:asy){reference-type="eqref" reference="eq:asy"} then follows immediately from [@BettinDrappeau Corollary 1.4]. ◻
:::

::: proof
*Proof of Theorem [\[th:pz\]](#th:pz){reference-type="ref" reference="th:pz"}.* We extend $H_{K}$ to a function on $\mathbb{R}_{>0}$ by setting $H_{K}(x):=\lim_{y\to x, y\in\mathbb{Q}}H_{K}(y)$ for all $x\not\in\mathbb{R}_{>0}\setminus \mathbb{Q}$. By hypothesis $H_{K}(x)$ is well defined and it is easy to prove that $H_{K}$ is continuous on $\mathbb{R}\setminus\mathbb{Q}$. Then, setting $\psi(x):=H_{K}(x)-\frac{\textnormal{Vol} (K)}{2\pi}\frac{1}x-\frac{3}2\log (1/x)$, for $x>0$, and $\psi(0)=0$, we have that $\psi(x)$ is bounded and continuous almost everywhere on $[0,1]$. Thus, by Lebesgue's integrability condition, $\psi$ is Riemann-integrable on $[0,1]$. In particular, for all $\varepsilon>0$ there exist a differentiable function $\psi_\varepsilon:[0,1]\to\mathbb{R}$ such that $\|\psi-\psi_\varepsilon\|_{\infty,[0,1]}\leq\varepsilon$.

By definition $\log \mathcal{J}_{K,0}(\ifthenelse{\equal{h/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  h/k\aftergroup\egroup\originalright)}{( h/k)}{( h/k)}{( h/k)}})-\log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{k/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  k/h\aftergroup\egroup\originalright)}{( k/h)}{( k/h)}{( k/h)}})=\psi(h/k)+\frac{\textnormal{Vol} (K)}{2\pi}\frac{k}h+\frac{3}2\log (k/h)$. Thus, proceeding as in the proof of Theorem [\[theo:cfep\]](#theo:cfep){reference-type="ref" reference="theo:cfep"} using this formula instead of Theorem [\[th:2\]](#th:2){reference-type="ref" reference="th:2"}, we obtain $$\begin{aligned}
    \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{ {\overline h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   {\overline h}/k\aftergroup\egroup\originalright)}{(  {\overline h}/k)}{(  {\overline h}/k)}{(  {\overline h}/k)}}) 
    &    = \sum_{\ell=1}^{r}\bigg(\frac{\textnormal{Vol} (K)}{2\pi}\frac{v_{\ell}}{v_{\ell-1}}+\frac{3}2\log ({v_{\ell}}/{v_{\ell-1}}) +
    \psi({v_{\ell-1}}/{v_{\ell}})\bigg)=\phi_\varepsilon(h/k)+O(\varepsilon\log k),\\
  
\end{aligned}$$ where $$\begin{aligned}
    \phi_\varepsilon(h/k) &  :  = \sum_{\ell=1}^{r}\bigg(\frac{\textnormal{Vol} (K)}{2\pi}\frac{v_{\ell}}{v_{\ell-1}}+\frac{3}2\log ({v_{\ell}}/{v_{\ell-1}}) +
    \psi_\varepsilon({v_{\ell-1}}/{v_{\ell}})\bigg).
  
\end{aligned}$$ Letting $T(x) = \{1/x\}$ for $x\in(0, 1]$, we note that for $2\leq s \leq r$, we have $\frac{v_{s-1}}{{v_s}} = T^{r-s}(h'/k)$, whereas $\frac{v_{0}}{{v_1}} = T^{r-1}(h'/k)+{\mathbf 1}_{b_1=1}$ (the contribution of ${\mathbf 1}_{b_1=1}$ being negligible). We apply [@BettinDrappeau] (Theorem 1.3 with $\lambda=1$, complemented by Theorem 1.2 with $\gamma(x) = \{1/x\}$), and obtain that the estimate [\[eq:conj\]](#eq:conj){reference-type="eqref" reference="eq:conj"} holds with $\log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{{ h}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  { h}/k\aftergroup\egroup\originalright)}{( { h}/k)}{( { h}/k)}{( { h}/k)}})$ replaced by $\phi_\varepsilon(h/k)$ and $$D_K = \frac{1-\gamma_0 - \log 2}{12/\pi^2} + \frac{3\pi}{\textnormal{Vol}(K)} + \frac{24}{\pi\textnormal{Vol}(K)}\int_0^1 \frac{\psi_\varepsilon(1/x)\mathrm{d}x}{1+x},$$ and with an error term $o_\varepsilon(N^2)$. The result then follows by letting $\varepsilon\to0^+$ sufficiently slowly with respect to $N$, and making the change of variables $h/k\to h'/k$ on the left hand side of [\[eq:conj\]](#eq:conj){reference-type="eqref" reference="eq:conj"}. ◻
:::

::: proof
*Proof of Corollary [\[concor\]](#concor){reference-type="ref" reference="concor"}.* We prove the result in the case where $x\in[0,1]\setminus\mathbb{Q}$ and for $y\to x^-$, the other cases being analogous. Let $x=[0;b_1,b_2,\dots]$ and let $h/k=[0;b_1,b_2,\dots,b_{2n},X,Y]$ for some $X,Y\in\mathbb{N}_{>0}$. Then, $h/k\to x^{-}$ as $n\to\infty$, uniformly in $X>b_{2n+1}$ and $Y$. We have $k/h\equiv [0;b_2,\dots,b_{2n},X,Y]~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~1\aftergroup\egroup\originalright)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}{(\textnormal{mod}~1)}$ and so by [@Bettin2015 (1.2)-(1.3) and Lemma 4] $$\frac1h\mathop{\mathrm{c_0}}(\overline k/h)=\frac{1}{\pi}\sum_{\ell=1}^{2n+1}\frac{(-1)^\ell\log(v_{\ell-1}/v_{\ell})}{v_{\ell-1}}+O(n)$$ uniformly in $X,Y$, where $v_{i}$ denotes the partial quotient of $[0;b_2,\dots,b_{2n},X,Y]$. Now, let $B=2+\max_{1\leq i\leq 2n}b_i$. Then, for $\ell<2n$, we have $v_{\ell}/v_{\ell-1}<B$, whereas $v_{2n}/v_{2n-1}=X+O(1)$ and $v_{2n+1}/v_{2n}=Y+O(1)$. Also, $v_{2n}=X{v_{2n-1}}+{v_{2n-2}}$ and $v_{2n-2}\leq v_{2n-1}\leq B^{2n-1}$. It follows, that $$\frac\pi h\mathop{\mathrm{c_0}}(\overline k/h)=\frac{\log Y}{X{v_{2n-1}}+{v_{2n-2}}}-\frac{\log X}{v_{2n-1}}+O(n\log B)=-\frac{\log X}{v_{2n-1}}(1+o(1))$$ as $n, X, Y\to\infty$ under the constraint $Y n B^{2n}=o(\log X)$. By [\[eq:srf\]](#eq:srf){reference-type="eqref" reference="eq:srf"} and [@BettinDrappeaub Theorem 1] we then have $$H_{4_1}^*(h/k)=-\frac{\log X}{v_{2n-1}}(1+o(1))(1+O(1/Y))+O\Big(Y+\frac{\log X}{Y v_{2n-1}}\Big)$$ and this goes to $-\infty$ as $n,X,Y\to\infty$ with $Y n B^{2n}=o(\log X)$. ◻
:::
