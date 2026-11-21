---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-016-36-q-characters
section_title: "q-characters"
section_number: 3.6
pages: 12-13
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.994
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
In this paragraph, we present a quantization of the $\varSigma$-basis of $\mathscr{O}$ corresponding to renormalized $q$-characters of the Iwahori-Hecke algebras. The theory of character of Iwahori-Hecke algebra is a little more involved than the one of symmetric groups. Indeed, given two permutations $\sigma$ and $\tau$ in the same conjugacy class of $\mathfrak{S}_n$, the $T$-basis elements $T_\sigma$ and $T_\tau$ can have different traces in a $\mathscr{H}_{n,q}$-module: for instance, $(1,2)$ and $(1,3)$ are conjugate in $\mathfrak{S}_3$, but $\chi(T_{(1,2)})=q$ and $\chi(T_{(1,3)})=q^3$ if we consider the one-dimensional index representation. However, if $\sigma$ and $\tau$ are of minimal Coxeter length in their conjugacy classes, then one has $\chi(T_{\sigma})=\chi(T_{\tau})$ for any character $\chi$. Moreover, the values of a character $\chi$ on these particular elements determine $\chi$, see [@Ram91 Propositions 5.1 and 5.2] or [@GP00 §8.2] for the general case of an Iwahori-Hecke algebra of a Coxeter group. Consequently, if $$\sigma_\rho=(1,2,\ldots,\rho_1)\,(\rho_1+1,\rho_1+2,\ldots,\rho_1+\rho_2)\,
\cdots\,(\rho_1+\cdots+\rho_{r-1}+1,\ldots,\rho_1+\cdots+\rho_r),$$ then $\varsigma^{\lambda}(q)$ is entirely determined by the values $\varsigma^{\lambda}(\rho,q)=\varsigma^{\lambda}(T_{\sigma_{\rho}},q)$, where $\rho$ runs over $\mathscr{Y}_{n}$. As in the case $q=1$, we denote by $\chi^\lambda(\rho,q)$ the rescaled character value (divided by the dimension of the module).

In [@Ram91], A. Ram uses the Schur-Weyl decomposition of $(\mathbb{C}^m)^{\otimes n}$ into irreducible $(U_q(\mathfrak{sl}(m,\mathbb{C})),\mathscr{H}_{n,q})$-bimodules to compute explicitly the characters of the Iwahori-Hecke algebra $\mathscr{H}_{n,q}$ --- the reader can also consult [@RRW96] and [@RR97]. These computations lead to a generalization of the usual Frobenius-Schur formula.

To state it, we need to introduce a few notations about symmetric functions (we try to be consistent with the one in [@Mac95]): the notations $h_\lambda$, $m_\lambda$, $s_\lambda$ and $p_\lambda$ stand respectively for the complete, monomial, Schur and power-sum basis of the symmetric function ring. We will also use the Hall scalar product, for which complete function basis is dual to the monomial one, while Schur functions are orthonormal and power sums orthogonal.

Furthermore, let us define a $q$-analog of the power sum $p_k(X)$. Let $\widetilde{q}_k(X,q)$ be the symmetric function defined by the formulas $$\begin{aligned}
\widetilde{q_k}(X,q)&=\frac{q^k}{q-1}\, h_k(X(1-q^{-1})) \quad (\lambda\text{-ring notations, }X\text{ is an alphabet and }q^{-1}\text{ is a variable}),\\
&=\frac{q^k}{q-1}\,\sum_{\mu \in \mathscr{Y}_k} (1-q^{-1})^{\ell(\mu)} \,m_\mu(X)=\frac{1}{q-1} \,\sum_{\mu \in \mathscr{Y}_k} (q^\mu-1)(z_\mu)^{-1}\,p_\mu(X),
\end{aligned}$$ where $q^\mu-1$ means $\prod_{i=1}^r \,(q^{\mu_i}-1)$, and where $z_\mu$ equals $\prod_{i \geq 1} i^{m_i}\,m_i!\,$ if $\mu$ writes multiplicatively as $1^{m_1}2^{m_2}\ldots s^{m_s}$. This is a slightly modified version of the Hall-Littlewood polynomial $P_k(X,q^{-1})$ described in [@Mac95 Chapter 3]. Let us first recall Frobenius formula for usual character values of symmetric group: $$\forall \rho \in \mathscr{Y}_n,\,\,\,p_\rho(X)=\sum_{\lambda \in \mathscr{Y}_n} \varsigma^{\lambda}(\rho)\,s_\lambda(X).$$ Here is the statement of Ram's generalization of Frobenius-Schur formula:

::: proposition
[]{#quantumcross label="quantumcross"} If $\widetilde{q}_\rho=\widetilde{q}_{\rho_1}\cdots \widetilde{q}_{\rho_r}$, then the following generalized Frobenius-Schur formula holds: $$\forall \rho \in \mathscr{Y}_n,\,\,\,\widetilde{q}_\rho(X,q)=\sum_{\lambda \in \mathscr{Y}_n} \varsigma^{\lambda}(\rho,q)\,s_\lambda(X).$$
:::

Many combinatoric rules follow from Proposition [\[quantumcross\]](#quantumcross){reference-type="ref" reference="quantumcross"}, *e.g.*, a quantization of the classical Murnaghan-Nakayama rule, see [@RR97 §2]. For the asymptotic analysis of the $q$-Plancherel measures, we shall use a triangular relation between $q$-characters and standard characters: $$\begin{aligned}
\varsigma^{\lambda}(\rho,q)&=\left\langle \widetilde{q}_\rho(X,q)\vphantom{s_\lambda(X)}\,\right |\left.s_\lambda(X) \vphantom{\widetilde{q}_\rho(X,q)}\right\rangle =\frac{q^n}{(q-1)^{\ell(\rho)}}\,\left\langle h_\rho(X-q^{-1}X)\vphantom{s_\lambda(X)}\,\right |\left.s_\lambda(X) \vphantom{h_\rho(X-q^{-1}X)}\right\rangle\\
&=\frac{q^n}{(q-1)^{\ell(\rho)}}\,\sum_{\nu\in \mathscr{Y}_n} \frac{\left\langle h_\rho(X-q^{-1}X)\vphantom{p_\nu(X-q^{-1}X)}\,\right |\left.p_\nu(X-q^{-1}X) \vphantom{h_\rho(X-q^{-1}X)}\right\rangle\,\left\langle p_\nu(X-q^{-1}X)\vphantom{s_\lambda(X)}\,\right |\left.s_\lambda(X) \vphantom{p_\nu(X-q^{-1}X)}\right\rangle}{\left\langle p_\nu\vphantom{p_\nu}\,\right |\left.p_\nu \vphantom{p_\nu}\right\rangle}\\
&=\frac{1}{(q-1)^{\ell(\rho)}}\,\sum_{\nu \in \mathscr{Y}_n}(q^\nu-1)\,\frac{\left\langle h_\rho\vphantom{p_\nu}\,\right |\left.p_\nu \vphantom{h_\rho}\right\rangle}{z_\nu}\,\left\langle p_\nu\vphantom{s_\lambda}\,\right |\left.s_\lambda \vphantom{p_\nu}\right\rangle=\frac{1}{(q-1)^{\ell(\rho)}}\,\sum_{\nu \in \mathscr{Y}_n}\frac{q^\nu-1}{z_\nu}\left\langle h_\rho\vphantom{p_\nu}\,\right |\left.p_\nu \vphantom{h_\rho}\right\rangle\,\varsigma^\lambda(\nu)
\end{aligned}$$ As for $q=1$, we define the following function on the set $\mathscr{Y}$ of all Young diagrams: $$\varSigma_{\rho,q}(\lambda)= \left\{\begin{array}{ll} |\lambda|^{\downarrow |\rho|}\,\chi^\lambda(\rho\,1^{|\lambda|-|\rho|},q) & \text{ if }|\rho| \leq |\lambda| ; \\ 0 & \text{ else.} \end{array}\right.$$ If $|\rho|=|\lambda|=n$, the previous formula can be rewritten: $$\label{eq:sigmaq_fct_sigma}
(q-1)^{\ell(\rho)}\,\varSigma_{\rho,q}(\lambda)=\sum_{\nu \in \mathscr{Y}_n} \frac{q^\nu-1}{z_\nu}\left\langle p_\nu\vphantom{h_\rho}\,\right |\left.h_\rho \vphantom{p_\nu}\right\rangle\,\varSigma_\nu(\lambda)$$ This is of course also true for $|\rho| > |\lambda|$. We will show that it still holds for $k=|\rho| < |\lambda|=n$. In this case, the scalar product $\langle h_{\rho\,1^{n-k}}| p_\nu \rangle$ in the sum above is given by: $$\begin{gathered}
\langle h_{\rho\,1^{n-k}}| p_\nu \rangle=\left\langle h_\rho(p_1)^{n-k}\vphantom{p_\nu}\,\right |\left.p_\nu \vphantom{h_\rho(p_1)^{n-k}}\right\rangle=\sum_{\pi_1\in \mathscr{Y}_{\rho_1},\ldots,\pi_m\in \mathscr{Y}_{\rho_m}} (z_{\pi_1}\cdots z_{\pi_m})^{-1} \,\left\langle p_\pi(p_1)^{n-k}\vphantom{p_\nu}\,\right |\left.p_\nu \vphantom{p_\pi(p_1)^{n-k}}\right\rangle \\
=\sum_{\pi_1,\ldots,\pi_m} z_{\pi1^{n-k}} \,(z_{\pi_1}\cdots z_{\pi_m})^{-1}\,\mathbb{1}_{(\nu=\pi1^{n-k})}
=(z_\nu\,\mathbb{1}_{(\nu=\nu_k1^{n-k})})\,\sum_{\pi_1,\ldots,\pi_m} (z_{\pi_1}\cdots z_{\pi_m})^{-1}\,\mathbb{1}_{(\nu_k=\pi)}\\
=(z_\nu /z_{\nu_k})\,\mathbb{1}_{(\nu=\nu_k1^{n-k})}\,\sum_{\pi_1,\ldots,\pi_m} (z_{\pi_1}\cdots z_{\pi_m})^{-1}\,\left\langle p_\pi\vphantom{p_{\nu_k}}\,\right |\left.p_{\nu_k} \vphantom{p_\pi}\right\rangle=(z_\nu /z_{\nu_k})\,\mathbb{1}_{(\nu=\nu_k1^{n-k})}\,\left\langle h_\rho\vphantom{p_{\nu_k}}\,\right |\left.p_{\nu_k} \vphantom{h_\rho}\right\rangle
\end{gathered}$$ As a consequence, formula ([\[eq:sigmaq_fct_sigma\]](#eq:sigmaq_fct_sigma){reference-type="ref" reference="eq:sigmaq_fct_sigma"}) can be seen as an equality of functions on $\mathscr{Y}$. Note that this relation between the symbols $\varSigma_{\rho,q}$ and $\varSigma_\nu$ is triangular, because $\left\langle p_\nu\vphantom{h_\rho}\,\right |\left.h_\rho \vphantom{p_\nu}\right\rangle=0$ unless $\nu$ is finer than $\rho$. Moreover, as $(m_\rho)_{\rho \in \mathscr{Y}}$ is the dual basis of $(h_\rho)_{\rho \in \mathscr{Y}}$, the inverse relation is easily obtained. We conclude that:

::: proposition
The symbols $(\varSigma_{\rho,q})_{\rho \in \mathscr{Y}}$ form a $\mathbb{C}(q)$-basis of $\mathscr{O}(q)=\mathscr{O}\otimes_{\mathbb{C}}\mathbb{C}(q)$ and yield a quantization of the basis $(\varSigma_\rho)_{\rho \in \mathscr{Y}}$ of $\mathscr{O}$. Moreover, the transition matrices between the $\varSigma_{\rho,q}$ and the $\varSigma_\rho$ are triangular, given by: $$\begin{aligned}
(q-1)^{\ell(\rho)}\,\varSigma_{\rho,q}(\lambda)&=\sum_{\nu \in \mathscr{Y}_k} \frac{q^\nu-1}{z_\nu}\left\langle p_\nu\vphantom{h_\rho}\,\right |\left.h_\rho \vphantom{p_\nu}\right\rangle\,\varSigma_\nu(\lambda) ;\\
(q^\rho-1)\,\varSigma_\rho(\lambda)&=\sum_{\nu \in \mathscr{Y}_k} (q-1)^{\ell(\nu)}\left\langle m_\nu\vphantom{p_\rho}\,\right |\left.p_\rho \vphantom{m_\nu}\right\rangle\,\varSigma_{\nu,q}(\lambda).
\end{aligned}$$
:::
