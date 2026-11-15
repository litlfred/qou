---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-014-42-h-transform-convolution-and-fourier-transform
section_title: "h-transform, convolution and Fourier transform on Bk,n"
section_number: 4.2
pages: 25-28
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.908
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
As a consequence of the fact that $B_{k,n}$ is an integrable PM-graph and the expression of its eigenbasis, we can deduce several results from Section [\[sec:pm_graph\]](#sec:pm_graph){reference-type="ref" reference="sec:pm_graph"}. In order to do so, we will need several times the following inversion formula for evaluating $S_{I}(\xi_{n}(J))$ in terms of $S_{J}(\xi_{n}(I))$.

::: lemma
[]{#lem:formula_inversion_Schur label="lem:formula_inversion_Schur"} For $I,J\in  B_{k,n}$, $$S_J(\xi_{n}(I))=\frac{S_J(\xi_{n}(I_0))}{S_I(\xi_{n}(I_0))}S_I(\xi_{n}(J)).$$ Moreover, $$V(\xi_{n}(I))=\exp\left(\frac{(k-1)i\pi}{n}\left(\langle I\rangle-\langle I_0\rangle\right)\right)V(\xi_{n}(I_0))S_I(\xi_{n}(I_0)),$$ where $\langle I\rangle=\sum_{i=1}^kI_i$.
:::

::: proof
*Proof.* By definition of Schur functions as ratios of generalized Vandermonde determinants, for $I\in B_{k}$ and $\vec{u}\in \mathbb{R}^k$ we have $$S_{I}(\vec{u})=\frac{a_{I}(\vec{u})}{a_{I_0}(\vec{u})},$$ where $a_{J}(\vec{u})=\det\left(e^{iu_lJ_m}\right)_{1\leq l,m\leq k}$ for $J\in B_{k}$. For $I,J\in B_{k,n}$, $$\begin{aligned}
a_{J}(\xi_{n}(I))=&\det\left(\exp\left(\frac{2i\pi}{n}(I_l-(k-1)/2)J_m\right)\right)_{1\leq l,m,\leq k}\nonumber\\
=&\exp\left(\frac{(k-1)i\pi}{n}\left(\sum_{l=1}^kI_l-\sum_{m=1}^kJ_m\right)\right)\det\left(\exp\left(\frac{2i\pi}{n}I_l(J_m-(k-1)/2)\right)\right)_{1\leq l,m,\leq k}\nonumber\\
=&\exp\left(\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle J\rangle)\right)\det\left(\exp\left(\frac{2i\pi}{n}I_l(J_m-(k-1)/2)\right)\right)_{1\leq l,m,\leq k}\nonumber\\
=&\exp\left(\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle J\rangle)\right)a_{I}(\xi_{n}(J)).\label{eq:relation_vandermonde}
\end{aligned}$$ Applying the latter formula to the ratio $\frac{S_J(\xi_{n}(I))}{S_J(\xi_{n}(I_0))}$ yields $$\begin{aligned}
\frac{S_J(\xi_{n}(I))}{S_J(\xi_{n}(I_0))}=&\frac{a_{J}(\xi_{n}(I))}{a_{I_0}(\xi_{n}(I))}\frac{a_{I_0}(\xi_{n}(I_0))}{a_{J}(\xi_{n}(I_0))}\\
=&\frac{a_{I}(\xi_{n}(J))}{a_{I}(\xi_{n}(I_0))}\frac{a_{I_0}(\xi_{n}(I_0))}{a_{I_0}(\xi_{n}(J))}\exp\left(\frac{(k-1)i\pi}{n}\left(\langle I\rangle-\langle J\rangle+\langle I_0\rangle-\langle I\rangle+\langle J\rangle-\langle I_0\rangle\right)\right)\\
=&\frac{S_I(\xi_{n}(J))}{S_I(\xi_{n}(I_0))},
\end{aligned}$$ which proves the first statement. Then, using [\[eq:relation_vandermonde\]](#eq:relation_vandermonde){reference-type="eqref" reference="eq:relation_vandermonde"} with $J=I_0$ yields $$V(\xi_{n}(I))=a_{I_0}(\xi_{n}(I))=\exp\left(\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle I_0\rangle\right)a_{I}(\xi_{n}(I_0))),$$ and, since $S_I(\xi_{n}(I_0))=\frac{a_{I}(\xi_{n}(I_0))}{V(\xi_{n}(I_0))}$, $$V(\xi_{n}(I))=\exp\left(\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle I_0\rangle)\right)V(\xi_{n}(I_0))S_I(\xi_{n}(I_0)).$$ ◻
:::

Specializing [\[eq:def_vI\]](#eq:def_vI){reference-type="eqref" reference="eq:def_vI"} and [\[eq:def_uI_Bkn\]](#eq:def_uI_Bkn){reference-type="eqref" reference="eq:def_uI_Bkn"} to $I=I_0$ yields the following Lemma.

::: lemma
[]{#lem:Perron-Frobenius label="lem:Perron-Frobenius"} The common left and right positive eigenvectors $h^l, h^r$ of all $A_{I},\, I\in B_{k,n}$ with the normalization $h^l(I_0)=1$, $\left\langle h^l,h^r\right\rangle=1$ are $$h^l(I)=S_I(\xi_{n}(I_0)),\quad h^r(I)=\frac{\vert V(\xi_{n}(I_0))\vert}{n^k}\cdot\vert V(\xi_{n}(I))\vert,$$ and the invariant probability measure of $B_{k,n}$ is $$\mu^h(I)=\frac{1}{n^k}\left\vert V(\xi_{n}(I))\right\vert^2.$$
:::

::: proof
*Proof.* Remark that with the notation of the statement, we have $w^{(I_0)}=h^l$. By [\[eq:def_vI\]](#eq:def_vI){reference-type="eqref" reference="eq:def_vI"}, [\[eq:def_uI_Bkn\]](#eq:def_uI_Bkn){reference-type="eqref" reference="eq:def_uI_Bkn"} and Lemma [\[lem:action_s_mu\]](#lem:action_s_mu){reference-type="ref" reference="lem:action_s_mu"}, $w^{(I_0)}$ and $u^{(I_0)}$ are both left and right eigenvectors of $A_{I}$ for $I\in B_{k,n}$ with eigenvalue $S_{I}(\xi_{n}(I_0))$. To conclude, we need to prove that $w^{(I_0)}(I)>0$ for all $I\in B_{k,n}$ and $h^r=w^{(I_0)}$ and $u^{(I_0)}=h^r$. Both assumptions are deduced if we prove that $\vert V(\xi_n(I_0))\vert S_I(\xi_{n}(I_0))=\vert V(\xi_{n}(I))\vert$, since then $h^l(I)=\frac{\vert V(\xi_{n}(I))\vert}{\vert V(\xi_n(I_0))\vert}>0$ and $u^{(I_0)}(I)=\frac{\vert V(\xi_n(I_0))\vert^2}{n^k}S_{I}(\xi_{n}(I_0))=\frac{\vert V(\xi_n(I_0))\vert}{n^k}\vert V(\xi_{n}(I))\vert$.

By Lemma [\[lem:formula_inversion_Schur\]](#lem:formula_inversion_Schur){reference-type="ref" reference="lem:formula_inversion_Schur"} $$V(\xi_{n}(I_0))S_{I}(\xi_{n}(I_0))=\exp\left(-\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle I_0\rangle)\right)V(\xi_{n}(I)).$$ Then, using that $\langle I_0\rangle=\frac{k(k-1)}{2}$ $$\begin{aligned}
&\exp\left(-\frac{(k-1)i\pi}{n}(\langle I\rangle-\langle I_0\rangle)\right)V(\xi_{n}(I))\\
=&\exp\left(-\frac{(k-1)i\pi}{n}\sum_{j=1}^k(I_j-(k-1)/2)\right)\prod_{1\leq l<m\leq k}\left( e^{2i\pi (I_m-(k-1)/2)/n}-e^{2i\pi (I_l-(k-1)/2)/n}\right)\\
=&\prod_{1\leq l<m\leq k}e^{-\frac{(I_m+I_l-(k-1))i\pi}{n}}\left(e^{2i\pi (I_m-(k-1)/2)/n}-e^{2i\pi (I_l-(k-1)/2)/n}\right)\\
=&(2i)^{k(k-1)/2}\prod_{l<m}\sin(\pi(I_m-I_l)/n).
\end{aligned}$$ Since $I$ is an increasing sequence, $\prod_{l<m}\sin(\pi(I_m-I_l)/n)>0$. In particular, for $I=I_0$ we get $V(\xi_{n}(I_0))=i^{k(k-1)/2}\vert V(\xi_{n}(I_0))\vert$. We deduce that $$\label{eq:rel_S_V}
\vert V(\xi_n(I_0))\vert S_I(\xi_{n}(I_0))=\vert V(\xi_{n}(I))\vert,$$ and the lemma is deduced. ◻
:::

As a consequence of the latter lemma, the positive eigenvalue of $A_I, I\in B_{k,n}$ corresponding to the eigenvector $h^r$ is $S_{I}(\xi_n(I_0))$. In particular, Lemma [\[lem:action_s_mu\]](#lem:action_s_mu){reference-type="ref" reference="lem:action_s_mu"} yields that for all $I,J\in B_{k,n}$ $$\label{eq:inequality_Perron_Frobenius}
\left\vert S_{I}(\xi_n(J))\right\vert\leq S_{I}(\xi_n(I_0)).$$ Following notation of Section [\[sec:formal_model_pm\]](#sec:formal_model_pm){reference-type="ref" reference="sec:formal_model_pm"}, set $P^I=\frac{A_{I}^h}{S_{I}(\xi_{n}(I_0))}$. Translating Definition [\[def:convolution\]](#def:convolution){reference-type="ref" reference="def:convolution"} to $B_{k,n}$ yields the following convolution product on $L^2_h(B_{k,n})$.

::: definition
[]{#def:dft_conv label="def:dft_conv"} The convolution product on $B_{k,n}$ is the map $*:L^2(B_{k,n})\otimes L^2(B_{k,n})\rightarrow L^2(B_{k,n})$ defined by $$x\ast y=\sum_{I\in B_{k,n}}\mu^h(I) x(I)P^I(y)=\sum_{I\in B_{k,n}}\frac{\vert V(\xi_{n}(I))\vert^2}{n^k} x(I)P^I(y),$$ where $P^I(y)=\frac{1}{h^r}\cdot \frac{A_I}{S_I(\xi_{n}(I_0))}(h^r\cdot y)$ and $\cdot$ denotes the pointwise multiplication.

A $h$-probability measure $\mu$ on $B_{k,n}$ is a vector $\mu\in L^2(B_{k,n})$ such that $$\sum_{I\in B_{k,n}}\frac{\vert V(\xi_{n}(I))\vert^2}{n^k}\mu(I)=1.$$
:::

Recall that we denote then by $\mathcal{M}_1(B_{k,n})$ the set of h-probability measures on $B_{k,n}$. We also denote by $\delta_I$ the unique $h$-probability measure supported at $I$, namely $$\label{eq:definition_dirac}
\delta_I=\frac{n^k}{\vert V(\xi_{n}(I)\vert^2}e_I.$$ The results of Section [\[sec:pm_graph\]](#sec:pm_graph){reference-type="ref" reference="sec:pm_graph"} yield then directly the proof of Proposition [\[prop:result_1\]](#prop:result_1){reference-type="ref" reference="prop:result_1"}.

::: proof
*Proof of Proposition [\[prop:result_1\]](#prop:result_1){reference-type="ref" reference="prop:result_1"}.* By Proposition [\[prop:structure_conv\]](#prop:structure_conv){reference-type="ref" reference="prop:structure_conv"}, $(L^2(B_{k,n}),+,*)$ is a commutative algebra such that $\mathcal{M}_1(B_{k,n})*\mathcal{M}_1(B_{k,n})\subset \mathcal{M}_1(B_{k,n})$, which proves $(1)$ and $(2)$.

Then, applying Definition [\[def:dft_conv\]](#def:dft_conv){reference-type="ref" reference="def:dft_conv"} to $x=\frac{e_{I^1}}{\mu^h(I^1)}$ and $y\in L^2(B_{k,n})$ and using that $\mu^h(I)=\frac{\vert V(I)\vert^2}{n^k}$ for $I\in B_{k,n}$, we get $$\frac{e_{I^1}}{\mu^h(I^1)}\ast y=P_{I^1}(y)=\frac{A^h}{\lambda},$$ where the last equality is due to Proposition [\[prop:equiv_graph_qh\]](#prop:equiv_graph_qh){reference-type="ref" reference="prop:equiv_graph_qh"} which implies that $A_{I^1}=T(s_{(1)})=A$. Doing the same with $x=\frac{e_I}{\mu^h(I)}$ and $y=\frac{e_{I_0}}{\mu^h(I_0)}$ yields $$\frac{e_{I}}{\mu^h(I)}\ast \frac{e_{I_0}}{\mu^h(I_0)}=\frac{1}{\mu^h(I_0)}P^I(e_{I_0})=\frac{h^r(I_0)}{h^r(I)h^l(I_0)h^r(I_0)h^l(I)}e_I=\frac{e_I}{\mu^h(I)},$$ where we used that $A_{I}(e_{I_0})=e_{I}$ and $h^l(I_0)=1$. Thus, (3) and (4) are proven. ◻
:::

Likewise, since $B_{k,n}$ is an integrable PM-graph, we can define a Fourier transform as in Section [\[sec:integrable_graph\]](#sec:integrable_graph){reference-type="ref" reference="sec:integrable_graph"}.

::: definition
[]{#def:Fourier_Bkn label="def:Fourier_Bkn"} The discrete Fourier transform on $B_{k,n}$ is the map $\Phi_n:L^2(B_{k,n})\rightarrow L^2(B_{k,n})$ defined for $x\in L^2(B_{k,n})$ by $$\Phi_n[x](I)=\langle \tilde{w}^{(I)},x\rangle_{h}=\sum_{J\in B_{k,n}}\frac{\vert V(\xi_{n}(J))\vert\cdot\vert V(\xi_{n}(I_0))\vert}{n^k}S_{J}(\xi_{n}(I))x(J).$$
:::

Then, Proposition [\[prop:diagonalization_Fourier\]](#prop:diagonalization_Fourier){reference-type="ref" reference="prop:diagonalization_Fourier"} directly yields for $x_1,\ldots,x_m\in L^2(B_{k,n})$ $$\label{eq:relation_conv_dft}
\Phi_n[x_1*\cdots*x_m]=\Phi_n[x_1]\cdots\Phi_n[x_m].$$ Let us more specifically study the Fourier transform of a $h$-probability measure. First, for $I,J\in B_{k,n}$, we have by Definition [\[def:Fourier_Bkn\]](#def:Fourier_Bkn){reference-type="ref" reference="def:Fourier_Bkn"}, [\[eq:definition_dirac\]](#eq:definition_dirac){reference-type="eqref" reference="eq:definition_dirac"} and [\[eq:rel_S_V\]](#eq:rel_S_V){reference-type="eqref" reference="eq:rel_S_V"}, $$\Phi_n[\delta_I](J)=\frac{\vert V(\xi_{n}(I))\vert\cdot\vert V(\xi_{n}(I_0))\vert}{n^k}S_{I}(\xi_{n}(J))\cdot \frac{n^k}{\vert V(\xi_{n}(I)\vert^2}=\frac{S_{I}(\xi_{n}(J))}{S_I(\xi_{n}(I_0))}.$$

Then, by Definition [\[def:dft_conv\]](#def:dft_conv){reference-type="ref" reference="def:dft_conv"} and [\[eq:definition_dirac\]](#eq:definition_dirac){reference-type="eqref" reference="eq:definition_dirac"}, a $h$-probability measure $\mu\in L_h^2(B_{k,n})$ can be written $\mu=\sum_{I\in B_{k,n}}a_{I}\delta_I$ with $a_I\geq 0$ for $I\in B_{k,n}$ and $\sum_{I\in B_{k,n}}a_I=1$. Hence, we have $$\label{eq:Fourier_probability}
\Phi_n[\mu](J)=\sum_{I\in B_{k,n}}a_{I}\frac{S_{I}(\xi_{n}(J))}{S_I(\xi_{n}(I_0))}.$$

::: example
For $k=1$, $B_{1}=\mathbb{Z}$, and we can identify $B_{1,n}$ with $\mathbb{Z}/n\mathbb{Z}$, and $S_{J}(u)=e^{iJu}$ for $u\in \mathbb{R}, J\in \mathbb{Z}$. In particular, $I_0=0$ and $S_{I_0}(u)=1$ for $u\in \mathbb{R}$. For $I\in [0,n[\cap \mathbb{Z}$, $\vert V(\xi_{n}(I))\vert=1$, and thus $$w^{(I)}=\sum_{J\in  B_{k,n}}\exp(-2i\pi IJ/n)e_{J},\quad u^{(I)}=\frac{1}{n}\sum_{J\in  B_{k,n}}\exp(-2i\pi IJ/n)e_{J}$$ so that we recover the usual discrete Fourier vectors. For $x\in L^2(B_{k,n})$, we then have $$\Phi_{n}[x](I)=\frac{1}{n}\sum_{J\in \mathbb{Z}/n\mathbb{Z}}\exp(2i\pi IJ/n)x(J),$$ which is the usual (inverse) discrete Fourier transform. Finally, the map $P_{I}$ is the circulant operator sending $e_{J}$ to $e_{J+I}$, so that for $x,y\in L^2(B_{1,n})$, the convolution product is $$x\ast y(J)=\frac{1}{n}\sum_{I\in \mathbb{Z}/n\mathbb{Z}}x(I)y(J-I),$$ which is the classical convolution product on $\mathbb{Z}/n\mathbb{Z}$. Then, [\[eq:relation_conv_dft\]](#eq:relation_conv_dft){reference-type="eqref" reference="eq:relation_conv_dft"} recovers the fact that $$\Phi_n(x\ast y)=\Phi_n(x)\Phi_n(y).$$
:::
