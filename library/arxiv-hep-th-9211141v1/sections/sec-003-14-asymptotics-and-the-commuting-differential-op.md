---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-003-14-asymptotics-and-the-commuting-differential-op
section_title: "Asymptotics and the Commuting Differential Operator"
section_number: 1.4
pages: 6-8
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsec:sum_commuting label="subsec:sum_commuting"} Again we take $J=(s,\infty)$ and consider asymptotics as $s\rightarrow
-\infty$. (Asymptotics as $s\rightarrow\infty$ can be obtained trivially from the Neumann series for $(I-K)^{-1}$.) From the random matrix point of view the interesting quantities are $$E(n;s):= {(-1)^n\over n!}\> {\partial^n\over \partial \lambda^n}
\, D(I;\lambda)\biggr\vert_{\lambda=1} \, .$$ This is the probability that exactly $n$ eigenvalues lie in $J$. Using our differential equations plus the known asymptotics of $q(s;1)$ as $s\rightarrow -\infty$ [@hastings_mcleod] we obtain the asymptotic expansions $$R(s;1)\sim  {1\over 4} s^2 -{1\over 8\, s} + {9\over 64\,  s^4}
 -{189\over 128\,  s^7}
+ {21663\over 512\, s^{10}}  +\cdots \, \ \ \ (s\rightarrow -\infty) .
\label{R_exp}$$ (where $R(s;1)$ denotes $R(s)$ corresponding to $\lambda=1$) and $$\begin{aligned}
 E(0;s)& =& D(J;1) \sim  {\tau_0\over (-s)^{1/8}}\exp\left(s^3/12\right)
\nonumber \\
&&\times\left (1 -
{3\over 2^6\,  s^3} +{2025\over 2^{13}\, s^6}
- {2470825\over 2^{19}\, s^9}  + \cdots \right)
\ \ \ (s\rightarrow -\infty)
\label{E0_exp}
\end{aligned}$$ where $\tau_0$ is an undetermined constant.

The analogue of this formula for the sine kernel was obtained by Dyson [@dyson76]. The analogue of our constant $\tau_0$ in the expansion was found to be equal to $2^{1/12} e^{3\zeta^\prime(-1)}$ ($\zeta(s)$ is the Riemann zeta function). This constant was obtained by scaling a result of the second author [@widom71] on Toeplitz matrices. Such a result is not available to us now. Using ([\[R_exp\]](#R_exp){reference-type="ref" reference="R_exp"}) and the fact that $R(s)$ is the logarithmic derivative of $E(0;s)$, it is straightforward to derive an integral representation for $\log\tau_0$. This integral can be evaluated approximately by numerically integrating ([\[p2\]](#p2){reference-type="ref" reference="p2"}) and using ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}). This leads to the value $\log\tau_0\simeq -0.136540$. We conjecture that in fact $$\tau_0 = e^{\zeta^\prime(-1)}\,  2^{1\over 24} =
 0.87237\> 14149\>  54127\, \ldots\, .$$ This agrees with the numerically computed value, up to its degree of accuracy.

For asymptotics of $E(n;s)$ for general $n$ we introduce $$r(n;s):= {E(n;s)\over E(0;s)}\, .$$ Successive differentiation of ([\[p2\]](#p2){reference-type="ref" reference="p2"}) with respect to $\lambda$, plus the known asymptotics of $q(s;1)$, allows us to find asymptotic expansions for the quantities $$q_n(s):= {\partial^n q\over \partial\lambda^n}\biggr\vert_{\lambda=1}
\label{qn_defn}$$ (for the analogue in the sine kernel case see [@btw]); and these in turn can be used to find expansions for $r(n;s)$. One drawback of this approach is that yet another undetermined constant factor enters the picture. (In [@btw; @widom92] Toeplitz and Wiener-Hopf techniques, not available for the Airy kernel, fixed this constant.)  Another drawback is that when one expresses the $r(n;s)$ in terms of the $q_n(s)$ a large amount of cancellation takes place, with the result that even the first-order asymptotics of $r(n;s)$ are out of reach by this method when $n$ is large.

There is, however, another approach (briefly indicated in [@btw], and with details in [@tw1], for the sine kernel case). We have $$r(n;s)=\sum_{i_1<\cdots<i_n} {\lambda_{i_1}\cdots \lambda_{i_n} \over
(1-\lambda_{i_1})\cdots (1-\lambda_{i_n}) }
\label{eig_repr}$$ where $\lambda_0>\lambda_1>\cdots$ are the eigenvalues of the integral operator $K$ (with $\lambda=1$). Now just as the operator with the sine kernel commutes with the differential operator for the prolate spheroidal wave functions [@ince], so does the Airy operator commutes with the differential operator $L$ given by $$Lf(x)=\left(\left(x-s\right) f^\prime(x)\right)^\prime - x(x-s) f(x)\, .
\label{L_operator}$$ An application of the WKB method, plus a trick allows us to derive the following asymptotic formula for $\lambda_i$ with $i$ fixed: $$1-\lambda_i\sim {\sqrt{\pi}\over i!}\,  2^{5i+3}\,  t^{3i/2 +3/4} \exp\left(
-{8\over 3} t^{3/2}\right) \ \ \ (s=-2t\rightarrow - \infty).
\label{eigs_asy}$$ (The analogue of this for the sine kernel is in [@fuchs64].) From this and ([\[eig_repr\]](#eig_repr){reference-type="ref" reference="eig_repr"}) we deduce $$r(n,-2t)\sim {1! 2! \cdots (n-1)!\over \pi^{n/2}\,  2^{(5n^2+n)/2}}\>
t^{-3n^2/4}\>\exp\left( {8\over 3} n t^{3/2} \right ) \, .
\label{r_asy}$$ (Note that this can be used to fix the constant mentioned in the last paragraph.)
