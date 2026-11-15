---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-008-3-proof-of-theorem
section_title: "Proof of Theorem ??"
section_number: 3
pages: 21-31
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.776
latex_coverage_ratio: 0.986
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
[]{#pmt1 label="pmt1"}

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

We postpone the proof of Lemma [\[extra_terms\]](#extra_terms){reference-type="ref" reference="extra_terms"} to Section [0.1](#prolex){reference-type="ref" reference="prolex"}. Since $[x]_{r}\asymp 1$ for $0\leq r<d$, applying [\[bdfg\]](#bdfg){reference-type="eqref" reference="bdfg"} and the above lemma we obtain $$\begin{split}\label{reme}
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

The following lemma will be proven in Section [0.2](#prolem){reference-type="ref" reference="prolem"}.

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
