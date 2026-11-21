---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-007-24-second-reciprocity-formula-for-the-q-pochhamm
section_title: "Second reciprocity formula for the q-Pochhammer symbol"
section_number: 2.4
pages: 19-21
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.846
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
