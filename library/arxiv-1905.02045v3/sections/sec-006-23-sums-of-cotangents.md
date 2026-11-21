---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-006-23-sums-of-cotangents
section_title: "Sums of cotangents"
section_number: 2.3
pages: 14-19
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.968
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
In this section and the next, we introduce the following extension of the Landau $O$-symbol. Let $D_1\subset D_2\subset \mathbb{C}$ be two sets given by the context, and $g: D_2 \to \mathbb{R}_+$. We will write $$f(z) = \mathcal{O}_{(p_1, p_2, \dotsc)}^z(g(z)) \qquad (z\in D_1)\label{eq:def-Oh}$$ whenever, for any fixed choice of the parameters $p_1, p_2, \dotsc$, there exists a function $\varphi$ holomorphic on $D_2$, which satisfies $\varphi(z) = f(z)$ for $z\in D_1$, and $\mathopen{}\mathclose\bgroup\originalleft|\varphi(z)\aftergroup\egroup\originalright|\ll g(z)$ for $z\in D_2$, the implied constant being *uniform* in the parameters $p_1, p_2, \dotsc$. The additional information is the holomorphic behaviour in $z$, which may become useful when studying knots other than $4_1$. However we stress that, in the present work, a later obstacle (possible cancellation of main terms) imposes the restriction $K = 4_1$, and in this case, we do not require holomorphicity of error terms.

::: lemma
[]{#tan_ineq label="tan_ineq"} For $0<\alpha<\frac12$, we have $$\begin{aligned}
    \cot(\pi\alpha) \tan(\pi\alpha x) & {} \leq x & \hspace{8em} (0<x\leq 1), \label{eq:tanineq-1} \\
    x(1-(2\alpha)^2)< \cot(\pi\alpha) \tan(\pi\alpha x) &{} \leq O_\varepsilon(x) &\hfill (0<x\leq \tfrac1\alpha(\tfrac12-\varepsilon)). \label{eq:tanineq-2}
  
\end{aligned}$$
:::

::: proof
*Proof.* Assume $0<x \leq \frac1\alpha(\frac12-\varepsilon)$. The function $x\mapsto \frac{\tan(x\lambda)}{x}$ is increasing on $(0, \frac{\pi}{2\lambda})$ for all $\lambda>0$. It follows that $\pi\alpha\leq \tan(\pi\alpha x)/x \leq O_\varepsilon(\alpha)$, while $\tan(\pi\alpha x)/x \leq \tan(\pi\alpha)$ if $x\leq 1$. Thus, it suffices to show the bounds $$1-(2\alpha)^2 < \pi \alpha \cot(\pi \alpha), \qquad \tan(\pi\alpha ) \cot(\pi \alpha)\leq 1, \qquad \alpha \cot(\pi \alpha) \ll 1.$$ The second is trivial, while the third follows from elementary properties of $\cot$. For the first, we note that by the Taylor expansion of $\cot$ [@GZ 1.411.7], we have $\phi(\alpha) := \frac{1-\pi\alpha \cot(\pi \alpha)}{\alpha^2} = \sum_{j\geq 0} c_j \alpha^{2j}$ for $\alpha\in(0, 1)$, where $c_j>0$. In particular $\phi$ is increasing, and we conclude by $\phi(\frac12)=4$. ◻
:::

::: lemma
[]{#tan_ineq2 label="tan_ineq2"} Let $\varepsilon>0$. For $0<\alpha\leq \frac12-\varepsilon$ and $|\operatorname{Re}(\alpha z)|\leq \frac12-\varepsilon$ we have $$\begin{aligned}
    1-\cot(\pi\alpha)\tan(\pi\alpha z)=(1-z)\big(1+O_\varepsilon(\alpha^2(|z|^2+|z|))\big).
  
\end{aligned}$$
:::

::: proof
*Proof.* If $|z|\leq 1/2$, expanding in Taylor series we obtain $$\begin{aligned}
    \cot(\pi\alpha)\tan(\pi\alpha z)=    \cot(\pi\alpha)\pi\alpha z(1+O(\alpha^2|z|^2))= z(1+O(\alpha^2))(1+O(\alpha^2|z|^2))
  
\end{aligned}$$ and the claimed result follows. If $|z|\geq1/2$, we observe that the left hand side is equal to $\cot(\pi\alpha)(\tan(\pi\alpha )-\tan(\pi\alpha z))$ and so, since $\cot(\pi\alpha)\pi\alpha=1+O_\varepsilon(\alpha^2)$, we are required to show that $$\frac{\tan(\pi \alpha z)-\tan(\pi \alpha)}{\pi \alpha(z-1)}
  = \frac1{\alpha z-\alpha}\int_\alpha^{\alpha z} \frac{\mathrm{d}v}{\cos(\pi v)^2} =  1 + O_\varepsilon( \mathopen{}\mathclose\bgroup\originalleft|\alpha z\aftergroup\egroup\originalright|^2).\label{eq:lemmatan-integ}$$ This follows for $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Im}(\alpha z)\aftergroup\egroup\originalright|\leq 1$ by the estimate  $\cos(\pi v)^2 = \exp\{O_\varepsilon(\mathopen{}\mathclose\bgroup\originalleft|v\aftergroup\egroup\originalright|^2)\}$ for $|\operatorname{Re}(v)|\leq\frac12-\varepsilon$ and $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Im}(v)\aftergroup\egroup\originalright|\leq 1$. If $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Im}(\alpha z)\aftergroup\egroup\originalright|>1$, then both the ratio $\frac1{\alpha z-\alpha}$ and the integral are bounded, since $\mathopen{}\mathclose\bgroup\originalleft|\cos(\pi v)\aftergroup\egroup\originalright| \gg \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{\pi|\operatorname{Im}(v)|}$, so that [\[eq:lemmatan-integ\]](#eq:lemmatan-integ){reference-type="eqref" reference="eq:lemmatan-integ"} holds in this case as well. ◻
:::

::: lemma
[]{#mlftt label="mlftt"} Let $\alpha\in\mathbb{R}$ with $0<|\alpha|<1/2$, and $$D_\alpha := \{z\in\mathbb{C}\mid \tfrac{-1}{{3}|\alpha|} < \operatorname{Re}(z)<1\}.$$ Then, taking the determination of the logarithm which is real on the real axis, the function given by $$\begin{aligned}
\label{dfps}
    \psi_\alpha(z):=\log(1-\cot(\pi \alpha)\tan(\pi \alpha z))+\cot(\pi \alpha)\tan(\pi \alpha z)
  
\end{aligned}$$ is holomorphic on $D_\alpha$, where it satisfies $$\begin{aligned}
    &\psi_\alpha(z)\ll |z|^2+|z||\log(1-z)|, \qquad \operatorname{Im}(\psi_\alpha(z))\ll |z|^2,\label{dfps1}\\
    &\psi_\alpha(z)=\log(1-z)+z+O_\varepsilon((|z|^2+|z|^3)|\alpha|^2) \quad \text{if $\mathopen{}\mathclose\bgroup\originalleft|\alpha\aftergroup\egroup\originalright|\leq\tfrac{1}{2}-\varepsilon$.}\label{dfps2}
  
\end{aligned}$$
:::

::: proof
*Proof.* We can assume $\alpha\in(0,1/2)$, since $\psi_\alpha$ is even in $\alpha$. For $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Re}(z)\aftergroup\egroup\originalright|<\frac1{2\alpha}$, let $g_\alpha(z) := \cot(\pi \alpha) \tan(\pi \alpha z)$. Since, for $z=x+iy$, we have $$\begin{aligned}
\label{tsum}
    \tan(\pi \alpha z)=\frac{\tan(\pi \alpha x)(1-\tanh^2 (\pi \alpha y))+i\tanh(\pi\alpha y)(1+\tan^2 (\pi\alpha  x))}{1+\tan^2(\pi\alpha  x)\tanh^2(\pi\alpha y)},
  
\end{aligned}$$ we deduce, for $x, y$ real and $\mathopen{}\mathclose\bgroup\originalleft|x\aftergroup\egroup\originalright|\leq 1$, $$\begin{aligned}
    \mathopen{}\mathclose\bgroup\originalleft|\operatorname{Re}(g_\alpha(z))\aftergroup\egroup\originalright| \leq \mathopen{}\mathclose\bgroup\originalleft|\cot(\pi\alpha)\tan(\pi \alpha x)\aftergroup\egroup\originalright| \leq \mathopen{}\mathclose\bgroup\originalleft|x\aftergroup\egroup\originalright|\label{bfrg}.
  
\end{aligned}$$ by Lemma [\[tan_ineq\]](#tan_ineq){reference-type="ref" reference="tan_ineq"}. Moreover, if $x\leq 0$, then $\operatorname{Re}(g_\alpha(z))\leq 0$. Using [\[tsum\]](#tsum){reference-type="eqref" reference="tsum"} and the lower bound [\[eq:tanineq-2\]](#eq:tanineq-2){reference-type="eqref" reference="eq:tanineq-2"}, we obtain $\mathopen{}\mathclose\bgroup\originalleft|\operatorname{Re}(g_\alpha(z))\aftergroup\egroup\originalright| \gg \cot(\pi \alpha) \tan(\pi \alpha \mathopen{}\mathclose\bgroup\originalleft|x\aftergroup\egroup\originalright|) \gg_\varepsilon\mathopen{}\mathclose\bgroup\originalleft|x\aftergroup\egroup\originalright|$. Thus, there exists $c_\varepsilon>0$ such that $$\operatorname{Re}(1-g_\alpha(z)) \geq \min(1-x, 1-c_\varepsilon x). \label{eq:bfrg2}$$ In particular, the function $z\mapsto \psi_\alpha(z) = \log(1-g_\alpha(z)) + g_\alpha(z)$ is well-defined and holomorphic in $D_\alpha$, and moreover $\operatorname{Im}(\log(1-g_\alpha(z))) < \pi / 2$.

We observe that if $\alpha y\to\pm \infty$ (and so $z\to\infty$), then $g_{\alpha}(z)\sim\pm i\cot(\pi\alpha)$ uniformly in $x$, so that $\psi_\alpha (z)\ll 1/\alpha\ll |z|$ and [\[dfps1\]](#dfps1){reference-type="eqref" reference="dfps1"}-[\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} follow trivially. Thus, we can assume $\alpha y\ll1$. Also, by [\[tsum\]](#tsum){reference-type="eqref" reference="tsum"} and Lemma [\[tan_ineq\]](#tan_ineq){reference-type="ref" reference="tan_ineq"} we obtain $$\begin{aligned}
    |\operatorname{Im}(g_\alpha(z))| &\ll |\cot(\pi\alpha)|\big(|\tan (\pi x\alpha)|+|\tanh (\pi \alpha y)|)\ll |x|+|y|\ll |z|.\label{bfig}
  
\end{aligned}$$

In particular, recalling [\[bfrg\]](#bfrg){reference-type="eqref" reference="bfrg"}, we have $g_\alpha(z)\ll |z|$.

Now, assume $\alpha \leq \frac12 - \varepsilon$. By [\[tsum\]](#tsum){reference-type="eqref" reference="tsum"}, and since $\alpha y\ll1$, we have $$|\operatorname{Im}(g_{\alpha}(z))|\geq |\cot(\pi\alpha)\tanh(\pi \alpha y)|\gg_\varepsilon|y| .$$ By [\[eq:bfrg2\]](#eq:bfrg2){reference-type="eqref" reference="eq:bfrg2"}, it then follows that $|1-g_{\alpha}(z)|\gg_\varepsilon\min(1-x, 1-c_\varepsilon x)+|y|\gg_\varepsilon|1-z|$, and so $\mathopen{}\mathclose\bgroup\originalleft|u_\alpha(z)\aftergroup\egroup\originalright|\gg_\varepsilon 1$ for $u_\alpha(z):=\frac{1-g_\alpha(z)}{1-z}$. Thus, $$\begin{aligned}
    \log(u_\alpha(z))=u_\alpha(z)-1+O_\varepsilon(|u_\alpha(z)-1|^2)=z-g_\alpha(z)+z (u_\alpha(z)-1)+O_\varepsilon(|u_\alpha(z)-1|^2)
  
\end{aligned}$$ and so [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} follows since $u_\alpha(z)-1=O_\varepsilon(\alpha^2(|z|^2+|z|))$ by Lemma [\[tan_ineq2\]](#tan_ineq2){reference-type="ref" reference="tan_ineq2"} (and since $\alpha z\ll1$).

We now move to [\[dfps1\]](#dfps1){reference-type="eqref" reference="dfps1"}. Since $g_\alpha(z)\ll |z|$, then if $|z|<\delta$ with $\delta>0$ sufficiently small, then by Taylor expansion one trivially has that [\[dfps1\]](#dfps1){reference-type="eqref" reference="dfps1"} holds for $|z|<\delta$. By the assumption $|\alpha y|\ll1$ we have that [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} implies [\[dfps1\]](#dfps1){reference-type="eqref" reference="dfps1"} for $|z|\geq \delta$ and $\alpha \leq \frac12 - \varepsilon$. It follows that we can also assume $\alpha\gg1$ (and so also $\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|\ll \alpha \mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|\ll1$).

Finally, we observe that under the above assumptions we have that [\[tsum\]](#tsum){reference-type="eqref" reference="tsum"} implies also $$\operatorname{Re}(1-g_\alpha(z)) \geq  1-x (1-\tanh^2(\pi\alpha y))\gg 1-x+ y^2\gg |1-z|^2 \qquad (x \geq 0),$$ which inequality $\operatorname{Re}(1-g_\alpha(z)) \gg \mathopen{}\mathclose\bgroup\originalleft|1-z\aftergroup\egroup\originalright|^2$ is also trivially true if $x<0$. The bound [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} follows since $g_\alpha(z)\ll \mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|$, $\operatorname{Im}(\log(1-g_\alpha(z))) < \pi / 2$, and $\log(1-w)+w \ll \min\{\mathopen{}\mathclose\bgroup\originalleft|w\aftergroup\egroup\originalright|^2, \mathopen{}\mathclose\bgroup\originalleft|w\aftergroup\egroup\originalright|+\log\mathopen{}\mathclose\bgroup\originalleft|1-w\aftergroup\egroup\originalright|\}$ for $w\in\mathbb{C}\smallsetminus[1, \infty)$. ◻
:::

::: lemma
[]{#triab label="triab"} Let $\gamma\leq \delta$ and let $a\in\mathbb{N}$ with $\gamma\leq a-\frac12\leq \delta$. Let $g(z)$ be holomorphic on a neighborhood of $\gamma\leq \operatorname{Re}(z)\leq \delta$, where it satisfies $|g(z)|\leq C_1 |z|^m+C_2$ for some $m,C_1,C_2\geq0$. Then, with $z=r$, we have $$\begin{aligned}
    \sum_{n=a}^r g(n) = \mathcal{O}_{(g,a)}^r(C_1((\mathopen{}\mathclose\bgroup\originalleft|a\aftergroup\egroup\originalright|+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|)^{m+1}+1)+C_2(\mathopen{}\mathclose\bgroup\originalleft|a\aftergroup\egroup\originalright|+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|+1)), && (r\in\mathbb{Z}\cap [a, \delta])
  
\end{aligned}$$ using the notation [\[eq:def-Oh\]](#eq:def-Oh){reference-type="eqref" reference="eq:def-Oh"} with $D_2 = \{z,\ \gamma+\frac12 \leq \operatorname{Re}(z)\leq \delta\}$.
:::

::: proof
*Proof.* We apply Lemma [\[lem:abelplana\]](#lem:abelplana){reference-type="ref" reference="lem:abelplana"} with $\alpha=a-\frac12$, $\beta=r-\frac12$, we find $$\begin{aligned}
    \sum_{n=a}^{r-1} g(n)=\int_{a-\frac12}^{r-\frac12}g(z)\mathrm{d}z- i \int_{0}^\infty  \frac{g(a-\frac12 + it)-g(a-\frac12 - it)-g(r-\frac12+ it)+g(r-\frac12 - it)}{\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}+1}\mathrm{d}{t},
  
\end{aligned}$$ Denoting by $\varphi(r)-g(r)$ the right hand side, we immediately see that $\varphi$ extend to a holomorphic function in $\gamma+\frac12 \leq \operatorname{Re}(z)\leq \delta$ and that $\varphi(z)\ll C_1((\mathopen{}\mathclose\bgroup\originalleft|a\aftergroup\egroup\originalright|+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|)^{m+1}+1)+C_2(\mathopen{}\mathclose\bgroup\originalleft|a\aftergroup\egroup\originalright|+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|+1)$ in this strip. ◻
:::

::: lemma
[]{#madc label="madc"} Let $(h,k)=1$, $3\leq h<k$ and $r_0\in\mathbb{Z}/h\mathbb{Z}$. Then for all $0\leq r<k$ with $r\equiv r_0~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$, writing $z=r/k$, we have $$\begin{aligned}
    \sum_{\substack{0\leq n\leq r\\ h\nmid n}}\bigg(\log \bigg(1&-\cot\Big( \frac{\pi n\overline k }{h} \Big)\tan\Big( \frac { \pi n}{hk} \Big)\bigg)+\cot\Big( \frac{\pi n\overline k }{h} \Big)\tan\Big( \frac { \pi n}{hk}\Big)\bigg)\\[-1em]
    {}& =\frac kh\Big(\frac{\pi i (z^2-z)}{2}+\mathop{\mathrm{{\mathfrak L}}}(z)+\frac{\pi i }{12}+z \log(2 \pi z/e)\Big) \\
    {}& \qquad\qquad +\mathcal{O}_{(h,k,r_0)}^{z}((1+\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright| + |z|^4)(1+k/h^2 + \log(k/h))),
  
\end{aligned}$$ using the notation [\[eq:def-Oh\]](#eq:def-Oh){reference-type="eqref" reference="eq:def-Oh"} with $D_2 = \{z\in\mathbb{C}, 0\leq \operatorname{Re}(z) < 1\}$. Moreover, the error term $\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|$ can be omitted if $z \in [0, 1 - \frac hk(1-\{\frac{r_0-k}h\})]$.
:::

::: proof
*Proof.* In this proof, the notation $\mathcal{O}$ will stand for $\mathcal{O}_{(k,h,r_0)}^z$ relative to the set $D_2 = \{z, \operatorname{Re}(z)\in[0, 1)\}$. We divide the sum into congruence classes $n\equiv \ell k~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$, $|\ell|<h/2$, where the possible term $\ell=h/2$ is excluded since the summand is zero in this case. With the notation [\[dfps\]](#dfps){reference-type="eqref" reference="dfps"}, we write the sum to be computed as $$\sum_{0 < \mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright| < h/2} S(\ell), \qquad S(\ell) := \sum_{\substack{0<n\leq r \\ n\equiv \ell k ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}} \psi_{\ell/h}\Big(\frac{n}{k\ell}\Big).$$ We consider each $\ell$ separately. We first consider $\ell \neq 1$. Let $\delta_\ell := \{\frac{r_0-k\ell}{h}\}$, and $$\alpha_\ell = \mathopen{}\mathclose\bgroup\originalleft\lceil\frac{-k\ell}h\aftergroup\egroup\originalright\rceil - \frac12, \qquad \beta_\ell(r) := {\mathopen{}\mathclose\bgroup\originalleft\lfloor {\frac{r-k\ell}{h}} \aftergroup\egroup\originalright\rfloor} + \frac12 = \frac{r-k\ell}{h} + \frac12 - \delta_{\ell}.$$ Then by Lemma [\[lem:abelplana\]](#lem:abelplana){reference-type="ref" reference="lem:abelplana"}, we have $$S(\ell) = \sum_{\alpha_\ell < m \leq \beta_\ell(r)} \psi_{\ell/h}(1 + \tfrac{hm}{k\ell}) = I + C(\alpha_\ell) - C(\beta_\ell(r)),$$ where $$\begin{aligned}
    I := \int_{\alpha_\ell}^{\beta_\ell(r)} \psi_{\ell/h}(1 + \tfrac{ht}{k\ell})\mathrm{d}t, \qquad  C(\gamma) := 2 \int_0^\infty \frac{\operatorname{Im}(\psi_{\ell/h}(1+\frac{h}{k\ell}(\gamma + it)))\mathrm{d}t}{\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t} + 1}.
  
\end{aligned}$$ Note that $\beta_\ell(r) = \frac{r-r_0}h + \beta_\ell(r_0)$, the right-hand side of which depends holomorphically on $r$. Splitting the integral as $\int_{- {k\ell}/h}^{(z-\ell) k/h}+\int_{\alpha_\ell}^{- {k\ell}/h}+\int_{(z-\ell) k/h}^{\beta_\ell(r)}$ with $z = r/k$, we get $$\begin{aligned}
    I &{} =
        \frac{k}h \int_0^{z} \psi_{\ell/h}(t/\ell)\mathrm{d}t + \int_{\alpha_\ell+\frac{k\ell}h}^{0}\psi_{\ell/h}(\tfrac{ht}{k\ell})\mathrm{d}t + \int_0^{\frac12-\delta_\ell} \psi_{\ell/h}(\tfrac z\ell+\tfrac{ht}{k\ell})\mathrm{d}t \\
    &{} =  \frac{k}h \int_0^{z} \psi_{\ell/h}(t/\ell)\mathrm{d}t + \mathcal{O}\big(\tfrac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2}{\ell^2}\big),
  
\end{aligned}$$ by Lemma [\[mlftt\]](#mlftt){reference-type="ref" reference="mlftt"}.

Next, we have $$C(\beta_\ell(r)) = \frac1{2i}\sum_\pm \pm \int_0^\infty \psi_{\ell/h}\Big(\frac z\ell + \frac{h}{k\ell}\Big(\frac12-\delta_\ell\Big) \pm i\frac{t h}{k\ell}\Big)\frac{\mathrm{d}t}{\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}+1}.$$ This also defines a holomorphic function of $z$ for $\operatorname{Re}(z) \in [0, 1)$, by Lemma [\[mlftt\]](#mlftt){reference-type="ref" reference="mlftt"}. Since $\ell \neq 1$, it is bounded by $\mathcal{O}(\frac{\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2+1}{\ell^2})$.

Grouping the above discussion, we deduce for $\ell\neq 1$ the estimate $$S(\ell) = \frac{k}{h} \int_0^z \psi_{\ell/h}(t/\ell)\mathrm{d}t + \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^2}{\ell^2}\Big).\label{eq:estim-Sell-neq1}$$

Consider now the case $\ell = 1$. We recall the notation $\delta_\ell$ from above. Since $h\geq 3$, by [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} and Lemma [\[triab\]](#triab){reference-type="ref" reference="triab"} we have $$S(1) = \mathcal{O}(\tfrac{k}{h^3}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4+1)) + \sum_{\substack{0<n\leq r \\ n\equiv k ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}} \Big( \frac nk + \log\Big(1 - \frac nk\Big)\Big).\label{eq:sumcotan-ell-1}$$ Let $a\in\{1, \dotsc, h\}$ satisfy $a\equiv k~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}$, $q = \frac{k-a}h$ and $g = {\mathopen{}\mathclose\bgroup\originalleft\lfloor {\frac{r-a}h} \aftergroup\egroup\originalright\rfloor} = \frac{r-a}h - \delta_1$. In the sum, the integer $m = \frac{k-n}{h}$ runs through $\mathbb{Z}\cap[q-g, q]$, so that $$\begin{aligned}
    \sum_{\substack{0<n\leq r \\ n\equiv k ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}} \log\Big(1 - \frac nk\Big) = {}& (g+1)\log\Big(\frac hk\Big) + \log\frac{\Gamma(q+1)}{\Gamma(q-g)} \\[-1em]
    = {}& \int_0^{g+1}\Big(\log\Big(\frac hk\Big) + \frac{\Gamma'}{\Gamma}(q+1-v)\Big)\mathrm{d}v \\
    = {}& \int_0^{g+1}\Big(\log\Big(\frac hk(q+1-v)\Big) - \frac1{q+1-v} - \int_0^\infty \frac{\{s\}\mathrm{d}s}{(s+q+1-v)^2}\Big)\mathrm{d}v
  
\end{aligned}$$ by Stirling's formula [@Tenenbaum2015a Theorem II.0.12]. First, setting $t = \frac{(v-1)h+a}k$, we have $$\begin{aligned}
    \int_0^{g+1}\log\Big(\frac hk(q+1-v)\Big)\mathrm{d}v = {}& \frac kh\int_0^z \log(1-t)\mathrm{d}t + \frac kh\Big[\int_{\frac{a-h}{k}}^0 + \int^{z-\frac hk \delta_1}_z\Big] \log(1-t)\mathrm{d}t \\
    = {}& \frac kh\int_0^z \log(1-t)\mathrm{d}t + \mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright| + \log(1+k/h)).
  
\end{aligned}$$ Secondly, we have $$\begin{aligned}
    \int_0^{g+1} \frac{\mathrm{d}v}{q+1-v} = \log\Big(1-z+\frac{h}k\delta_1\Big) - \log\Big( 1 + \frac{h-a}k\Big) = \mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright| + \log(1+k/h)).
  
\end{aligned}$$ Note that in both cases, as well as in the following computations, the error term $\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|$ can be omitted if $z \in [0, 1 - \frac hk(1-\delta_1)]$ (which is the case when $z=r/k$). Finally, $$\begin{aligned}
    \int_0^{g+1}\int_0^\infty \frac{\{s\}\mathrm{d}s}{(s+q+1-v)^2}\mathrm{d}v = {}& \int_0^\infty \frac{\{s\}(g+1)\mathrm{d}s}{(s+q-g)(s+q+1)} \\
    = {}& \int_0^\infty \{s\}\frac{1 + \frac kh z - \frac ah - \delta_1}{(s+\frac kh(1-z) + \delta_1)(s+\frac{k-a}h+1)}\mathrm{d}s \\
    = {}& \mathcal{O}(\log (1+k/h)+\log(1+|z|) ).
  
\end{aligned}$$ We turn to the contribution of the term $n/k$ in [\[eq:sumcotan-ell-1\]](#eq:sumcotan-ell-1){reference-type="eqref" reference="eq:sumcotan-ell-1"}. By a direct computation, we find $$\begin{aligned}
    \sum_{\substack{0<n\leq r \\ n\equiv k ~\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \textnormal{mod}~h\aftergroup\egroup\originalright)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}{(\textnormal{mod}~h)}}} \frac nk - \frac kh \int_0^z t\mathrm{d}t =
    {}& z(\tfrac12-\delta_1) + 1 - \tfrac{h}{2k}(\tfrac ah + \delta_1)(\tfrac ah + 1 - \delta_1) = \mathcal{O}(\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|+1).
  
\end{aligned}$$ On the other hand, we note that by [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"}, $$\int_0^z (t + \log(1-t))\mathrm{d}t = \int_0^z \psi_{1/h}(t)\mathrm{d}t + \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4}{h^2}\Big).$$ Grouping the above estimates, we deduce $$S(1) = \frac kh\int_0^z \psi_{1/h}(t)\mathrm{d}t + \mathcal{O}\big((1 + \tfrac{k}{h^3} + \log(k/h))(1 + \mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4 + \mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|)\big).\label{eq:estim-S1}$$

We now sum the estimates [\[eq:estim-Sell-neq1\]](#eq:estim-Sell-neq1){reference-type="eqref" reference="eq:estim-Sell-neq1"}, [\[eq:estim-S1\]](#eq:estim-S1){reference-type="eqref" reference="eq:estim-S1"} over $\ell$, getting $$\sum_{0<\mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright|<h/2} S(\ell) = \frac{k}{h} \int_0^z \sum_{0<\mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright|<h^{2/3}} \psi_{\ell/h}(t/\ell)\mathrm{d}t +
  \mathcal{O}((1 + \tfrac{k}{h^{3}} + \log(k/h))(1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4+\mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|)).$$ The main term is evaluated by [\[dfps2\]](#dfps2){reference-type="eqref" reference="dfps2"} (for $\mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright|\leq h/3$) and [\[dfps1\]](#dfps1){reference-type="eqref" reference="dfps1"} (for $h/3<\mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright|<h/2$) as $$\begin{aligned}
    \sum_{ 0<|\ell|\leq h/2}\int_0^z \psi_{\ell/h}(t/\ell)\mathrm{d}t&=  \sum_{ 0<|\ell|\leq h/3}\bigg(\int_0^z(\log(1-t/\ell)+t/\ell)\mathrm{d}t+ \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4}{h^2}\Big)\bigg) + \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^3}{h}\Big) \\
    & =  \sum_{0<\ell<h/3}\int_0^z \log(1-t^2/\ell^2)\mathrm{d}t+ \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4}{h}\Big) \\
    & =  \sum_{\ell>0}\int_0^z\log(1-t^2/\ell^2)\mathrm{d}t + \mathcal{O}\Big(\frac{1+\mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4}{h}\Big).
  
\end{aligned}$$ For $-1\leq t\leq1$ we have $\prod_{\ell=1}^\infty (1-t^2/\ell^2)=\frac{\sin (\pi t)}{\pi t}$. Moreover, for $0\leq z<1$ we have $$\begin{aligned}
    \int_{0}^{z}\log(2\sin(\pi t))\mathrm{d}t&=\int_{0}^{z}\log(-i\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{\pi i t}(1-\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{-2\pi i t}))\mathrm{d}t=\frac{\pi i (z^2-z)}{2}+\int_{0}^{z}\log(1-\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{-2\pi i t})\mathrm{d}t\\
    &=\frac{\pi i (z^2-z)}{2}+\mathop{\mathrm{{\mathfrak L}}}(z)+\frac{\pi i }{12},
  
\end{aligned}$$ by [\[dig\]](#dig){reference-type="eqref" reference="dig"}. Collecting the previous estimates, we conclude that $$\begin{aligned}
    \sum_{0 < \mathopen{}\mathclose\bgroup\originalleft|\ell\aftergroup\egroup\originalright| < h/2} S(\ell) = {}& \frac kh\Big(\frac{\pi i (z^2-z)}{2}+\mathop{\mathrm{{\mathfrak L}}}(z)+\frac{\pi i }{12}+z \log(2 \pi z/\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}})\Big) \\
    \qquad & + \mathcal{O}\Big(\Big(1 + \frac k{h^2} + \log(k/h)\Big)(1 + \mathopen{}\mathclose\bgroup\originalleft|z\aftergroup\egroup\originalright|^4 + \mathopen{}\mathclose\bgroup\originalleft|\log(1-z)\aftergroup\egroup\originalright|) \Big),
  
\end{aligned}$$ as claimed. ◻
:::
