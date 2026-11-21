---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-006-31-limit-of-the-connection-formula
section_title: "Limit of the connection formula"
section_number: 3.1
pages: 7-11
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.953
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
[]{#section3.1 label="section3.1"}

We rewrite the connection formula in Theorem [\[theorem1\]](#theorem1){reference-type="ref" reference="theorem1"} in order to take a limit $p\to 1^-$. We set new functions $h_\nu (t;p)$ and $J_\nu^{\pm}(x;p)$. We set $h_\nu (t;p):=(p^{1/2},p^{1/2};p)_\infty z(t)$. For any $x\in\mathbb{C}^*\setminus [-\lambda ;p]$ and $\lambda\in\mathbb{C}^*$, $J_{\nu ,\lambda}^{+}(x;p)$ is $$J_{\nu ,\lambda}^{+}(x;p):=\frac{(p^{\nu +1};p)_\infty}{(p;p)_\infty}\frac{\theta_p\left(\frac{\lambda p^{\nu}}{x}\right)}{\theta_p\left(\frac{\lambda}{x}\right)}{}_1\varphi_1\left(0;p^{1+2\nu};p,x\right).$$ Similarly, $J_{\nu ,\lambda}^{-}(x;p)$ is $$J_{\nu ,\lambda}^{-}(x;p):=\frac{(p^{\nu +1};p)_\infty}{(p;p)_\infty}\frac{\theta_p\left(\frac{\lambda p^{\nu}}{x}\right)}{\theta_p\left(\frac{\lambda}{x}\right)}{}_1\varphi_1\left(0;p^{1+2\nu};p,p^{2\nu }x\right).$$ We remark that the function $\theta_p(\lambda p^\nu /x)/\theta_p(\lambda /x)$ satisfies the following $q$-difference equation $$u(px)=p^\nu u(x),$$ which is also satisfied by the function $u(x)=x^\nu$. We remark that the pair $(J_{\nu,\lambda}^{+}(x;p),J_{-\nu,\lambda}^{-}(x;p))$ gives a fundamental system of solutions of equation ([\[b3\]](#b3){reference-type="ref" reference="b3"}) if $\nu\not\in\mathbb{Z}$. We set the function $C^+_\nu (\lambda ,t;p)$ and $C^-_\nu (\lambda ,t;p)$ as follow:

::: definition
For any $\lambda\in\mathbb{C}^*$, $C^+_\nu (\lambda ,t;p)$ is $$C^+_\nu (\lambda ,t;p):=
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{\nu +1},p^{-2\nu};p)_\infty}\frac{\theta_p(-p^{2\nu +2}t)}{\theta_p(-p^{\nu +2}t)}\frac{\theta_p(\lambda t)}{\theta_p(\lambda p^\nu t)}.$$ Similarly, the function $C^-_\nu (\lambda ,t;p)$ is $$C^-_\nu (\lambda ,t;p):=
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{-\nu +1},p^{2\nu};p)_\infty}\frac{\theta_p(-p^2t)}{\theta_p(-p^{\nu +2}t)}\frac{\theta_p(\lambda t)}{\theta_p(\lambda p^{-\nu }t)}.$$
:::

Then, $C^+_\nu (\lambda ,t;p)$ and $C^-_\nu (\lambda ,t;p)$ are single valued as a function of $t$. The function $C^+_\nu (\lambda ,t;p)$ and $C^-_\nu (\lambda ,t;p)$ are the $p$-elliptic functions. By using these new functions, our connection formula is rewritten by $$h_\nu\left(\frac{1}{x};p\right)=C_{\nu}^+\left(\lambda ,\frac{1}{x};p\right)J_{\nu}^{+}(x;p)
+C_\nu^-\left(\lambda ,\frac{1}{x};p\right)J_{-\nu ,\lambda}^{-}(x;p).$$

::: theorem
[]{#limitbessel label="limitbessel"}For any $x\in \mathbb{C}^*\setminus (-\infty ,0]$ where $\arg x\in (-\pi ,\pi )$, we have $$\lim_{p\to 1^-}h_\nu \left(\frac{1}{(1-p)^2x};p\right)
=-ie^{-\nu\pi i}H_{2\nu}^{(2)}(2\sqrt{x}).$$ Here, $H_{2\nu}^{(2)}(\cdot )$ is the Hankel function of the second kind.
:::

The aim of this section is to give a proof of the theorem above.

By the definition, $h_\nu \left(1/\{(1-p)^2x\};p\right)$ can be described as follows $$\begin{gathered}
 h_\nu\left(\frac{1}{(1-p)^2x};p\right)
 =\left\{\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{-2\nu},p;p)_\infty}(1-p)^{2\nu}\right\}
\left\{\frac{\theta_p\left(-\frac{p^{2\nu +2}}{x(1-p)^2}\right)}{\theta_p\left(-\frac{p^{\nu +2}}{x(1-p)^2}\right)}(1-p)^{-2\nu}\right\} \notag.\\
 \hphantom{h_\nu\left(\frac{1}{(1-p)^2x};p\right) =}{}
  \times\left\{{}_1\varphi_1\left(0;p^{1+2\nu};p,(1-p)^2x\right)\right\}\notag\\
\hphantom{h_\nu\left(\frac{1}{(1-p)^2x};p\right) =}{}  +
\left\{\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{2\nu},p;p)_\infty}(1-p)^{-2\nu}\right\}
\left\{\frac{\theta_p\left(-\frac{p^2}{x(1-p)^2}\right)}{\theta_p\left(-\frac{p^{\nu +2}}{x(1-p)^2}\right)}(1-p)^{2\nu}\right\} \notag\\
\hphantom{h_\nu\left(\frac{1}{(1-p)^2x};p\right) =}{} \times
\left\{{}_1\varphi_1\left(0;p^{1-2\nu};p,p^{-2\nu}(1-p)^2x\right)\right\}.\label{limit}
\end{gathered}$$ We consider the limit of each part $\{\cdot \}$.

::: lemma
[]{#limgam label="limgam"}For any $\nu \in\mathbb{C}^*\setminus \mathbb{Z}$, we have $$\lim_{p\to 1^-}
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{-2\nu},p;p)_\infty}(1-p)^{2\nu}
=-\frac{1}{\sin (2\nu\pi )\Gamma (2\nu +1)}.$$
:::

::: proof
*Proof.* We can check out as follows $$\begin{gathered}
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{-2\nu},p;p)_\infty}(1-p)^{2\nu} =\frac{\frac{(p;p)_\infty}{(p^{-2\nu};p)_\infty}(1-p)^{1+2\nu}}
{\left\{\frac{(p;p)_\infty}{(p^{\frac{1}{2}};p)_\infty}(1-p)^{\frac{1}{2}}\right\}
\left\{\frac{(p;p)_\infty}{(p^{\frac{1}{2}};p)_\infty}(1-p)^{\frac{1}{2}}\right\}
} =\frac{\Gamma_p(-2\nu )}{\Gamma_p\left(\frac{1}{2}\right)\Gamma_p\left(\frac{1}{2}\right)}.
\end{gathered}$$ Here, $\Gamma_q(\cdot )$ is Jackson's $q$-gamma function which is defined by $$\Gamma_q(x):=\frac{(q;q)_\infty}{(q^x;q)_\infty}(1-q)^{1-x},\qquad 0<q<1.$$ This function satisfies $\lim\limits_{q\to 1^-}\Gamma_q(x)=\Gamma (x)$ [@GR]. Therefore, $$\lim_{p\to 1^-}
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{-2\nu},p;p)_\infty}(1-p)^{2\nu}
=\frac{\Gamma (-2\nu )}{\Gamma \left(\frac{1}{2}\right)\Gamma \left(\frac{1}{2}\right)}.$$ By Euler's reflection formula of the gamma function, we get $$\frac{\Gamma (-2\nu )}{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{1}{2}\right)}=
-\frac{1}{\sin (2\nu\pi )\Gamma (2\nu +1)}.$$ Therefore, we get the conclusion. ◻
:::

If we replace $\nu$ by $-\nu$, we get the limit $$\lim_{p\to 1^-}
\frac{(p^{\frac{1}{2}},p^{\frac{1}{2}};p)_\infty}{(p^{2\nu},p;p)_\infty}(1-p)^{-2\nu}=\frac{1}{\sin (2\nu\pi )\Gamma (1-2\nu )}.$$ In [@Z1], the following proposition can be found:

::: proposition
[]{#propo1 label="propo1"} For any $x\in\mathbb{C}^*$ $(-\pi <\arg x<\pi )$, we have $$\lim_{p\to 1^-}\frac{\theta_p\left(\frac{p^{\nu_1}}{(1-p^2)x}\right)}{\theta_p\left(\frac{p^{\nu_2}}{(1-p^2)x}\right)}\left(1-p^2\right)^{\nu_2-\nu_1}=x^{\nu_1-\nu_2},$$and $$\lim_{p\to 1^-}\frac{\theta_p\left(-\frac{p^{\nu_1}}{(1-p^2)x}\right)}{\theta_p\left(-\frac{p^{\nu_2}}{(1-p^2)x}\right)}\left(1-p^2\right)^{\nu_2-\nu_1}=(-x)^{\nu_1-\nu_2}.$$
:::

::: lemma
For any $x\in\mathbb{C}^*$ $(-\pi <\arg x\leq\pi )$ and fixed constant $K$, we have $$\theta_p(-\sqrt{p})\theta_p\left(-\frac{K}{x}\right)
=\theta_{\sqrt{p}}\left(\sqrt{\frac{K}{x}}\right)\theta_{\sqrt{p}}\left(-\sqrt{\frac{K}{x}}\right).$$
:::

::: proof
*Proof.* From Jacobi's triple product identity and $(a^2;q^2)_n=(a,-a;q)_n$, we obtain $$\frac{(\sqrt{p};\sqrt{p})_\infty}{(-\sqrt{p};\sqrt{p})_\infty}\theta_p\left(-\frac{K}{x}\right)
=\theta_{\sqrt{p}}\left(\sqrt{\frac{K}{x}}\right)\theta_{\sqrt{p}}\left(-\sqrt{\frac{K}{x}}\right).$$ We remark that $(\sqrt{p};\sqrt{p})_\infty /(-\sqrt{p};\sqrt{p})_\infty$ can be rewritten as follows [@GR]: $$\frac{(\sqrt{p};\sqrt{p})_\infty}{(-\sqrt{p};\sqrt{p})_\infty}
=\sum_{n\in\mathbb{Z}}(-1)^n(\sqrt{p})^{n^2}=\theta_p(-\sqrt{p}).$$ We obtain the conclusion. ◻
:::

Therefore, we obtain the following relation.

::: corollary
[]{#kei2 label="kei2"}For any $x\in\mathbb{C}^*$ $(-\pi <\arg x\leq\pi )$, we have $$\begin{gathered}
\frac{\theta_p\left(p^{2\nu +2}\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}
=\frac{\theta_{\sqrt{p}}\left(p^{\nu +1}\frac{1}{(1-p)\sqrt{x}}\right) \theta_{\sqrt{p}}\left(p^{\nu +1}\frac{-1}{(1-p)\sqrt{x}}\right)}
{\theta_{\sqrt{p}}\left(p^{\frac{\nu}{2}+1}\frac{1}{(1-p)\sqrt{x}}\right)\theta_{\sqrt{p}}
\left(p^{\frac{\nu}{2}+1}\frac{-1}{(1-p)\sqrt{x}}\right)}\label{th1}
\end{gathered}$$ and $$\begin{gathered}
\frac{\theta_p\left(p^2\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}
=\frac{\theta_{\sqrt{p}}\left(p\frac{1}{(1-p)\sqrt{x}}\right)\theta_{\sqrt{p}}\left(p\frac{-1}{(1-p)\sqrt{x}}\right)}
{\theta_{\sqrt{p}}\left(p^{\frac{\nu}{2}+1}\frac{1}{(1-p)\sqrt{x}}\right)\theta_{\sqrt{p}}\left(p^{\frac{\nu}{2}+1}\frac{-1}{(1-p)\sqrt{x}}\right)}.\label{th2}
\end{gathered}$$
:::

We consider the limit $p\to 1^-$ (i.e., $\sqrt{p}\to 1^-$) of [\[th1\]](#th1){reference-type="eqref" reference="th1"} and [\[th2\]](#th2){reference-type="eqref" reference="th2"}.

::: lemma
For any $x\in\mathbb{C}^*\setminus (-\infty ,0]$ $(-\pi <\arg x\leq\pi )$, we have []{#limthe label="limthe"}

1.  $\displaystyle{\lim_{p\to 1^-}\frac{\theta_p\left(-\frac{p^{2\nu +2}}{x(1-p)^2}\right)}
    {\theta_p\left(-\frac{p^{\nu +2}}{x(1-p)^2}\right)}(1-p)^{-2\nu}=e^{\nu \pi i}x^\nu}$  and

2.  []{#limtheta label="limtheta"}$\displaystyle{\lim_{p\to 1^-}\frac{\theta_p\left(-\frac{p^{2}}{x(1-p)^2}\right)}
    {\theta_p\left(-\frac{p^{\nu +2}}{x(1-p)^2}\right)}(1-p)^{2\nu}=e^{-\nu \pi i}x^{-\nu}}$.
:::

::: proof
*Proof.* Combining Proposition [\[propo1\]](#propo1){reference-type="ref" reference="propo1"} and Corollary [\[kei2\]](#kei2){reference-type="ref" reference="kei2"}, we consider the limit $\sqrt{p}\to 1^-$ as follows: $$\begin{gathered}
 \frac{\theta_p\left(p^{2\nu +2}\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}(1-p)^{-2\nu}
=\frac{\theta_{\sqrt{p}}\left(p^{\nu +1}\frac{1}{(1-p)\sqrt{x}}\right) \theta_{\sqrt{p}}\left(p^{\nu +1}\frac{-1}{(1-p)\sqrt{x}}\right)}
{\theta_{\sqrt{p}}\left(p^{\frac{\nu}{2}+1}\frac{1}{(1-p)\sqrt{x}}\right)\theta_{\sqrt{p}}\left(p^{\frac{\nu}{2}+1}\frac{-1}{(1-p)\sqrt{x}}\right)}
(1-p)^{-2\nu}\\
 \hphantom{\frac{\theta_p\left(p^{2\nu +2}\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}(1-p)^{-2\nu}}{}
 =\left\{\frac{\theta_{\sqrt{p}}\left((\sqrt{p})^{2\nu +2}\frac{1}{(1-(\sqrt{p})^2)\sqrt{x}}\right) }{\theta_{\sqrt{p}}\left((\sqrt{p})^{\nu +2}\frac{1}{(1-\{\sqrt{p})^2)\sqrt{x}}\right)}\left\{1-(\sqrt{p})^2\right\}^{-\nu}\right\}\\
\hphantom{\frac{\theta_p\left(p^{2\nu +2}\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}(1-p)^{-2\nu}=}{}
\times
\left\{\frac{\theta_{\sqrt{p}}\left(-(\sqrt{p})^{2\nu +2}\frac{1}{(1-(\sqrt{p})^2)\sqrt{x}}\right) }{\theta_{\sqrt{p}}\left(-(\sqrt{p})^{\nu +2}\frac{1}{(1-\{\sqrt{p})^2)\sqrt{x}}\right)}\left\{1-(\sqrt{p})^2\right\}^{-\nu}\right\}\\
\hphantom{\frac{\theta_p\left(p^{2\nu +2}\frac{-1}{(1-p)^2x}\right)}{\theta_p\left(p^{\nu +2}\frac{-1}{(1-p)^2x}\right)}(1-p)^{-2\nu}}{}
 \to (\sqrt{x})^\nu\cdot (-\sqrt{x})^\nu=(-x)^\nu
=e^{\nu\pi i}x^\nu , \qquad \sqrt{p}\to 1^-.
\end{gathered}$$ Similarly, we can prove the latter one. We obtain the conclusion. ◻
:::

We consider the last part.

::: lemma
[]{#limbas label="limbas"}For any $x\in\mathbb{C}^*$, we have $$\lim_{p\to 1^-}{}_1\varphi_1\left(0;p^{1+2\nu};p,(1-p)^2x\right)={}_0F_1\left(-,1+2\nu ;-x\right)$$ and $$\lim_{p\to 1^-}{}_1\varphi_1\left(0;p^{1-2\nu};p,p^{-2\nu }(1-p)^2x\right)={}_0F_1\left(-,1-2\nu ;-x\right).$$
:::

::: proof
*Proof.* We check each of the term of $${}_1\varphi_1\left(0;p^{1+2\nu};p,(1-p)^2x\right)
=\sum_{n\ge 0}\frac{1}{(p^{1+2\nu},p;p)_n}(-1)^np^{\frac{n(n-1)}{2}}\left\{(1-p)^2x\right\}^n.$$ For any $n\ge 0$, $$\begin{gathered}
\frac{1}{(p^{1+2\nu},p;p)_n}(-1)^np^{\frac{n(n-1)}{2}}
\left\{(1-p)^2x\right\}^n \\
\qquad {}=\frac{(1-p)^n(1-p)^n}{(p^{1+2\nu};p)_n(p;p)_n}p^{\frac{n(n-1)}{2}}\left(-x\right)^n
 \to \frac{1}{(1+2\nu )_n\cdot n!}\left(-x\right)^n, \qquad p\to 1^-.
\end{gathered}$$ Summing up all terms, we get $$\sum_{n\ge 0}\frac{1}{(1+2\nu )_n\cdot n!}\left(-x\right)^n
={}_0F_1\left(-,1+2\nu ;-x\right).$$ Therefore, we obtain the conclusion. Similarly, we can prove the latter. ◻
:::

We give the proof of Theorem [\[limitbessel\]](#limitbessel){reference-type="ref" reference="limitbessel"}.

::: proof
*Proof.* Apply Lemma [\[limgam\]](#limgam){reference-type="ref" reference="limgam"}, Lemma [\[limthe\]](#limthe){reference-type="ref" reference="limthe"} and Lemma [\[limbas\]](#limbas){reference-type="ref" reference="limbas"} to ([\[limit\]](#limit){reference-type="ref" reference="limit"}), we obtain $$\begin{gathered}
h_\nu \left(\frac{1}{(1-p)^2x};p\right)\to  \left\{-\frac{1}{\sin (2\nu\pi )\Gamma (1+2\nu )}\right\}e^{\nu\pi i}x^{\nu}{}_0F_1\left(-,1+2\nu ;-x\right)\\
\hphantom{h_\nu \left(\frac{1}{(1-p)^2x};p\right)\to}{}
+\left\{\frac{1}{\sin (2\nu\pi )\Gamma (1-2\nu )}\right\}e^{-\nu\pi i}x^{-\nu}{}_0F_1\left(-,1-2\nu ;-x\right)\\
\hphantom{h_\nu \left(\frac{1}{(1-p)^2x};p\right)}{}
=\frac{-e^{\nu\pi i}J_{2\nu}\left(2\sqrt{x}\right)+
e^{-\nu\pi i}J_{-2\nu}\left(2\sqrt{x}\right)}{\sin (2\nu\pi )}\\
\hphantom{h_\nu \left(\frac{1}{(1-p)^2x};p\right)}{}
=\frac{e^{-\nu\pi i}}{i}H_{2\nu}^{(2)}\left(2\sqrt{x}\right)
,\qquad p\to 1^-.
\end{gathered}$$ Therefore, we acquire the conclusion. ◻
:::

## Acknowledgements

The author would like to express his deepest gratitude to Professor Yousuke Ohyama for many valuable comments. The author also expresses his thanks to Professor Lucia Di Vizio for fruitful discussions when she was invited to the University of Tokyo in the winter 2011. The author would like to give thanks to the referee for some useful comments.
