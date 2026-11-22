---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-003-22-the-hahn-exton-q-bessel-function
section_title: "The Hahn-Exton q-Bessel function"
section_number: 2.2
pages: 4-4
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.839
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
[]{#section2.2 label="section2.2"}

The Hahn--Exton $q$-Bessel function is defined by $$J_\nu^{(3)}(x;q):=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}x^\nu\sum_{n\ge 0}\frac{(-1)^nq^{\frac{n(n-1)}{2}}}{(q^{\nu +1},q;q)_n}\left(qx^2\right)^n.$$ The function $J_\nu^{(3)}(x;q)$ satisfies the $q$-difference equation $$\begin{gathered}
\label{heqb}
\left[\sigma_p^2- \left\{(p^\nu +p^{-\nu })-x^2p^{2-\nu}\right\}\sigma_p +1\right]y(x)=0.
\end{gathered}$$ If we replace $\nu$ by $-\nu$ and $x$ by $xp^{-\nu}$, we obtain $J_{-\nu}^{(3)}(xp^{-\nu};q)$ which is another solution of ([\[heqb\]](#heqb){reference-type="ref" reference="heqb"}) around the origin. This solution corresponds to the classical Neumann function $Y_\nu (x)$ [@Z3]. We consider the behavior of equation ([\[heqb\]](#heqb){reference-type="ref" reference="heqb"}) around the infinity. We set $1/t$, formally $t^2\mapsto t$ and $z(t)=y(1/t)$. Then $z(t)$ satisfies $$\begin{gathered}
\left[\sigma_p^2-\left\{(p^\nu +p^{-\nu})-\frac{p^{-2-\nu }}{t}\right\}\sigma_p+1\right]z\left(t\right)=0.
\label{b3}
\end{gathered}$$

We set $\mathcal{E}(t)=1/\theta_p(-p^{\nu +2}t)$ and $f(t)=\sum\limits_{n\ge 0}a_nt^n$, $a_0=1$. We assume that $z(t)$ can be described as $$z(t)=\mathcal{E}(t)f(t)=\frac{1}{\theta_p(-p^{\nu +2}t)}\left(\sum_{n\ge 0}a_nt^n\right).$$ Since $\mathcal{E}(t)$ satisfies the following $q$-difference equation $$\sigma_p\mathcal{E}(t)=-p^{\nu +2}t\mathcal{E}(t),\qquad
\sigma_p^2\mathcal{E}(t)=p^{2\nu +5}t^2\mathcal{E}(t),$$ we can check out that the function $f(t)$ satisfies the equation $$\begin{gathered}
\left\{p^{2\nu +5}t^2\sigma_p^2 +p^{\nu +2} (p^\nu +p^{-\nu})t\sigma_p-\sigma_p +1\right\}f(t)=0.
\label{b4}
\end{gathered}$$
