---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-001-11-state-integrals-and-their-q-series
section_title: "State-integrals and their q-series"
section_number: 1.1
pages: 1-3
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.862
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.intro label="sub.intro"}

State-integrals are multi-dimensional integrals of products of Faddeev's quantum dilogarithms. They appear in abundance in Quantum Topology, quantum Teichmüller theory and in complex Chern--Simons theory. State integrals were studied among others by Hikami [@Hi], Dimofte--Gukov--Lennels--Zagier [@DGLZ], Andersen--Kashaev [@AK; @AK:complex], Kashaev--Luo--Vartanov [@KLV], Dimofte [@Dimofte:complex] and Dimofte--Garoufalidis [@DG2].

In our previous paper [@state-integrals], we showed how to express 1-dimensional state-integrals as a finite sum of products of $q$-series and $\tilde{q}$-series with integer coefficients, where the variables $q$ and $\tilde{q}$ are related by the modular transformation: $q=e^{2\pi\mathsf{i}\tau}$ and $\tilde{q}=e^{-2\pi\mathsf{i}/\tau}$.

In this paper we evaluate 1-dimensional state-integrals at rational points in terms of the Rogers dilogarithm, the cyclic (quantum) dilogarithm and truncated state-sums at roots of unity. Our formulas are syntactically similar with

-   the constant terms of the power series that appear in the Quantum Modularity Conjecture of Zagier [@Za:QMF; @GZ1],

-   the $1$-loop terms of the perturbation expansion of complex Chern--Simons theory [@DG2],

-   the state-sums of quantum Teichmüller theory [@Kashaev:6j; @K95; @K97] and also [@BB Sec.6].

This is not a coincidence; it is one part of a story discussed in detail in [@GZ2].

In order to keep our principle clear, we focus exclusively on 1-dimensional state-integrals, and we illustrate our results for the state-integrals of $4_1$, $5_2$ and $(-2,3,7)$ pretzel knots. In a separate publication we will discuss the evaluation of multi-dimensional state-integrals.

A 1-dimensional state-integral is an absolutely convergent integral of the form $$\label{eq.IAB}
\mathcal I_{A,B}(\mathsf{b})=
\int_{\mathbbm R+ \mathsf{i}\epsilon} \operatorname{\Phi}_{\mathsf{b}}(x)^B e^{-A \pi \mathsf{i}x^2} dx$$ for a complex number $\mathsf{b}$ with $\mathsf{b}^2 \not\in \mathbbm R_{\leq 0}$. Here $A, B$ are natural numbers satisfying $B > A > 0$ and $\operatorname{\Phi}_{\mathsf{b}}(x)$ is Faddeev's quantum dilogarithm function [@Faddeev; @FK-QDL]. Few properties of this special function are reviewed in Appendix [\[sec.QDL\]](#sec.QDL){reference-type="ref" reference="sec.QDL"}.

A numerical computation by the first author and Zagier [@GZ2] suggested the following formula for $\mathcal I_{1,2}(1)$: $$\label{eq.I211}
\mathcal I_{1,2}(1)= \frac{e^{\pi\mathsf{i}/6}}{\sqrt{3}}
\left(e^{\frac{V}{2\pi}}-e^{-\frac{V}{2\pi}}\right)$$ (and more generally for the Taylor coefficients of the analytic function $\mathcal I_{1,2}(\mathsf{b})$ at $\mathsf{b}=1$), where $V=2\,\mathrm{Im}(\mathrm{Li}_2(e^{\pi \mathsf{i}/3}))=2.0298832\ldots$ is the volume of the $4_1$ knot. Understanding and proving the above identity led to the results of our paper.

Our aim is to evaluate $\mathcal I_{A,B}(\mathsf{b})$ when $\mathsf{b}^2=M/N$ for a pair of coprime natural numbers $M,N$. The content of our paper can be summarized in a diagram

$$\begin{CD}
\{\text{state-integrals}\} @>>> \{\text{Nahm series}\} \\
@VVV                              @VVV   \\
\{\text{evaluations}\} @<<< \{\text{truncated Nahm series}\}
\end{CD}$$ The top arrow was the content of our previous article [@state-integrals]. To recall the connection between state-integrals and $q$-series, consider the integrand of the state-integral $\mathcal I_{A,B}(\mathsf{b})$, shifted by $c_{\mathsf{b}}=\mathsf{i}(\mathsf{b}+\mathsf{b}^{-1})/2$: $$\label{eq.fc}
\operatorname{f}(x-c_{\mathsf{b}})= \operatorname{\Phi}_{\mathsf{b}}(x)^B e^{-A \pi \mathsf{i}x^2} \,.$$ The quasi-periodicity of the quantum dilogarithm (see Equations [\[eq.bshift\]](#eq.bshift){reference-type="eqref" reference="eq.bshift"}--[\[eq.tbshift\]](#eq.tbshift){reference-type="eqref" reference="eq.tbshift"}) implies that $$\operatorname{f}(x+ \mathsf{i}m \mathsf{b} + \mathsf{i}n \mathsf{b}^{-1})=
\operatorname{f}(x) \operatorname{g}^+_m(e^{2 \pi \mathsf{b} x},q_+) 
\operatorname{g}^-_n(e^{2 \pi \mathsf{b}^{-1} x},q_-)$$ where $q_\pm=e^{2 \pi \mathsf{i}\mathsf{b}^{\pm 2}}$ and $$\label{eq.gpm}
\operatorname{g}^\pm_k(x,q)= (-x)^{A k}\frac{q^{\frac{A}{2}k(k+1)}}{(qx;q)_k^B} \,.$$ This gives rise to the series $G^\pm(x,q) \in \mathbbm Z[\![x,q]\!]$

defined by $$\begin{aligned}
G^\pm(x,q)&=\sum_{k=0}^\infty \operatorname{g}^\pm_k(x,q) 
\end{aligned}$$ The $q$-series $G^{\pm}(1,q) \in \mathbbm Z[\![q]\!]$ are special $q$-hypergeometric series of Nahm type and appear in the expression of the state-integral $\mathcal I_{A,B}(b)$ as a sum of products of $q$-series and $\tilde{q}$-series, where $\tilde{q}=1/q_-$, see [@state-integrals Thm.1.1].

Throughout the paper, $(M,N)$ will denote an *admissible* pair, i.e., a pair of coprime positive integers. Consider the state-sum defined by $$\begin{aligned}



G_{M,N}(x_+,x_-)&=\sum_{k=0}^{MN-1} \operatorname{g}^+_{kP}(x_+,\zeta_N^M)
\operatorname{g}^-_{kQ}(x_-,\zeta_M^N)
\end{aligned}$$ where $P,Q$ are integers that satisfy the equation $MP+NQ=1$ and $\zeta_N=e^{2 \pi i/N}$. When $x_+^N=x_-^M$, it follows from Lemma [\[lem.gg\]](#lem.gg){reference-type="ref" reference="lem.gg"} that $G_{M,N}(x_+,x_-)$ is independent of the choice of $P$ and $Q$. Observe that $$G_{1,N}(x_+,x_-)=G^+_N(x_+), \qquad G_{M,1}(x_+,x_-)=G^-_M(x_-)$$ where $$\begin{aligned}
\label{eq.GN}
G^\pm_N(x)&=\sum_{k=0}^{N-1} \operatorname{g}^\pm_k(x,\zeta_N) \,.
\end{aligned}$$
