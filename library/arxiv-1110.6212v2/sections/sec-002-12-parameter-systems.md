---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-002-12-parameter-systems
section_title: "Parameter systems"
section_number: 1.2
pages: 3-4
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.976
---
Let $q_0,q_1,\ldots,q_n\in\mathbb{C}^{\times}$ be such that $q_i=q_j$ whenever $s_i$ and $s_j$ are conjugate in $W_Q$. We call the sequence $(q_i)$ a *parameter system*. By [@bourbaki IV, §5, No.5, Prop 5] the product $$q_w=q_{i_1}\cdots q_{i_{\ell}}\quad\textrm{(where $w=s_{i_1}\cdots s_{i_{\ell}}\in W_Q$ is reduced)}$$ does not depend on the particular reduced expression for $w$. If $\alpha\in W_0\alpha_i\cap W_0\alpha_j$ then $s_i$ and $s_j$ are conjugate in $W_0$, and hence for $\alpha\in R_0$ we define $$q_{\alpha}=q_i\qquad\textrm{if $\alpha\in W_0 \alpha_i$}.$$

Let $\mathbb{C}[L]=\mathbb{C}\textrm{-span }\{x^{\lambda}\mid \lambda\in L\}$ be the group algebra of $L$, with the group operation written multiplicatively as $x^{\lambda}x^{\mu}=x^{\lambda+\mu}$. In the field of fractions of $\mathbb{C}[L]$ let (for $\alpha\in R_0$) $$\begin{aligned}
c_{\alpha}(x)=\begin{cases}\displaystyle{\frac{1-q_{\alpha}^{-1}x^{-\alpha^{\vee}}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_1$}\\
\displaystyle{\frac{(1-q_0^{-1/2}q_n^{-1/2}x^{-\alpha^{\vee}/2})(1+q_0^{1/2}q_n^{-1/2}x^{-\alpha^{\vee}/2})}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_2$.}
\end{cases}
\end{aligned}$$ (Note that if $\alpha\in R_2$ then $2\alpha\in R$, and so $(2\alpha)^{\vee}=\alpha^{\vee}/2$ is in $L$.) Choose relatively prime elements $n_{\alpha}(x)$ and $d_{\alpha}(x)$ in $\mathbb{C}[L]$ so that $$c_{\alpha}(x)=\frac{n_{\alpha}(x)}{d_{\alpha}(x)}.$$ For example, $\alpha\in R_2$ and $q_n^{1/2}=q_0^{1/2}$ then $n_{\alpha}(x)=1-q_n^{-1}x^{-\alpha^{\vee}/2}$ and $d_{\alpha}(x)=1-x^{-\alpha^{\vee}/2}$.

Similarly, let $$\begin{aligned}
c_{\alpha}'(x)=\begin{cases}
\displaystyle{\frac{1-q_{\alpha}^{-1}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_1$}\\
\displaystyle{\frac{1-q_n^{-1}+q_n^{-1/2}(q_0^{1/2}-q_0^{-1/2})x^{-\alpha^{\vee}/2}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_2$}.
\end{cases}
\end{aligned}$$ Then, with $d_{\alpha}(x)$ as above, $$c_{\alpha}'(x)=\frac{n_{\alpha}'(x)}{d_{\alpha}(x)}$$ for some $n_{\alpha}'(x)\in\mathbb{C}[L]$ with $n_{\alpha}'(x)$ and $d_{\alpha}(x)$ relatively prime.

Let $$\begin{aligned}
c(x)&=\prod_{\alpha\in R_0^+}c_{\alpha}(x),&n(x)&=\prod_{\alpha\in R_0^+}n_{\alpha}(x),&d(x)&=\prod_{\alpha\in R_0^+}d_{\alpha}(x).
\end{aligned}$$ The expression $c(x)=n(x)/d(x)$ is the *Macdonald $c$-function*. We write $c_i(x)$, $c_i'(x)$, $n_i(x)$, $n_i'(x)$, and $d_i(x)$ for $n_i(x)$ for $c_{\alpha_i}(x)$, $c_{\alpha_i}'(x)$, $n_{\alpha_i}(x)$, $n_{\alpha_i}'(x)$, and $d_{\alpha_i}(x)$ (respectively).
