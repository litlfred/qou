---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-003-13-affine-hecke-algebras
section_title: "Affine Hecke algebras"
section_number: 1.3
pages: 4-5
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.966
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
Standard references for affine Hecke algebras include [@lusztig], [@macblue] and [@ram1]. With the above notation, the *affine Hecke algebra* $\mathscr{H}_L$ with *parameters* $q_0,\ldots,q_n$ is the algebra over $\mathbb{C}$ with vector space basis $\{T_w\mid w\in W_L\}$ and relations $$\begin{aligned}
T_uT_v&=T_{uv}&&\textrm{if $\ell(uv)=\ell(u)+\ell(v)$}\\
T_{i}^2&=1+(q_i^{\frac{1}{2}}-q_i^{-\frac{1}{2}})T_i&&\textrm{for all $i=0,1,\ldots,n$},
\end{aligned}$$ where we write $T_i=T_{s_i}$.

The above presentation is the *Coxeter* presentation of $\mathscr{H}_L$. There is a second important presentation which exploits the semidirect product structure $W_L=L\rtimes W_0$. This is the *Bernstein presentation*, given by ([\[eq:rel1\]](#eq:rel1){reference-type="ref" reference="eq:rel1"})--([\[eq:rel4\]](#eq:rel4){reference-type="ref" reference="eq:rel4"}) below. Each $\lambda\in L$ can be written as $\lambda=\mu-\nu$ with $\mu,\nu\in L\cap P^+$, and we define $$x^{\lambda}=T_{t_{\mu}}T_{t_{\nu}}^{-1}.$$ It is not hard to see that this is well defined, and in particular $x^{\lambda}=T_{t_{\lambda}}$ if $\lambda$ is dominant.

It can be shown [@macblue] that $\mathscr{H}_L$ has vector space basis $\{T_wx^{\lambda}\mid \lambda\in L,w\in W_0\}$ and relations $$\begin{aligned}
\label{eq:rel1}T_i^2&=1+(q_i^{\frac{1}{2}}-q_i^{-\frac{1}{2}})T_i&&\textrm{for $i=1,\ldots,n$}\\
\label{eq:rel2}T_iT_jT_i\cdots&=T_jT_iT_j\cdots\quad\textrm{($m_{ij}$ factors)}&&\textrm{for $1\leq i<j\leq n$}\\
\label{eq:rel3}x^{\lambda}x^{\mu}&=x^{\lambda+\mu}&&\textrm{for all $\lambda,\mu\in L$}\\
\label{eq:rel4}T_ix^{\lambda}-x^{s_i\lambda}T_i&=q_i^{\frac{1}{2}}c_i'(x)(x^{\lambda}-x^{s_i\lambda})&&\textrm{for $1\leq i\leq n$ and $\lambda\in L$.}
\end{aligned}$$ Thus we see a copy of the group algebra $\mathbb{C}[L]$ of the lattice $L$ inside of $\mathscr{H}_L$. The relation ([\[eq:rel4\]](#eq:rel4){reference-type="ref" reference="eq:rel4"}) is the *Bernstein relation*. Since $s_i\lambda=\lambda-\langle \lambda,\alpha_i\rangle\alpha_i^{\vee}$ and $\langle\lambda,\alpha_i\rangle\in\mathbb{Z}$ the "fraction" $c_i'(x)(x^{\lambda}-x^{s_i\lambda})$ that appears in the Bernstein relation is actually an element of $\mathbb{C}[L]$.

It is well known (see, for example, [@macblue (4.2.10)]) that the centre of $\mathscr{H}_L$ is $$\mathbb{C}[L]^{W_0}=\{f\in\mathbb{C}[L]\mid w\cdot f=f\textrm{ for all $w\in W_0$}\}.$$ This has powerful implications for the representation theory of $\mathscr{H}_L$. For example it forces the irreducible representations to be finite dimensional (since the centre acts on irreducible representations by scalars, and it is evident that $\mathscr{H}_L$ is finite dimensional over $\mathbb{C}[L]^{W_0}$).

It is natural to seek modifications $\tau_w$ of $T_w$ which satisfy a "simplified Bernstein relation" $$\begin{aligned}
\label{eq:simpbernstein}
\tau_w x^{\lambda}=x^{w\lambda}\tau_w\qquad\textrm{for all $w\in W_0$ and $\lambda\in L$}.
\end{aligned}$$ Define elements $\tau_1,\ldots,\tau_n\in\mathscr{H}_L$ by $$\tau_i=d_i(x)T_i-q_i^{\frac{1}{2}}n_i'(x).$$ The Bernstein relation gives $\tau_ix^{\lambda}=x^{s_i\lambda}\tau_i$, and it can be shown (see [@ramcalib Proposition 2.7] for example) that for $w\in W_0$ the product $$\tau_w=\tau_{i_1}\cdots \tau_{i_{\ell}}\quad\textrm{is independent of the choice of reduced expression $w=s_{i_1}\cdots s_{i_{\ell}}$.}$$ Thus the elements $\tau_w$, $w\in W_0$, satisfy ([\[eq:simpbernstein\]](#eq:simpbernstein){reference-type="ref" reference="eq:simpbernstein"}), and a direct calculation gives the useful formula $$\begin{aligned}
\label{eq:tausquared}
\tau_i^2=q_i\,n_i(x)n_i(x^{-1})\in\mathbb{C}[L].
\end{aligned}$$
