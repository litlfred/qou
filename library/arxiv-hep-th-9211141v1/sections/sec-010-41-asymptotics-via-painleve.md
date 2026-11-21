---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-010-41-asymptotics-via-painleve
section_title: "Asymptotics via Painlev'e"
section_number: 4.1
pages: 17-19
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsec:asy_painleve label="subsec:asy_painleve"} Hastings and McLeod [@hastings_mcleod] (see also [@clarkson_mcleod1; @clarkson_mcleod2]) have shown that $q(s;1)$, the unique solution to equation ([\[p2\]](#p2){reference-type="ref" reference="p2"}) which is asymptotic to ${\rm Ai}(s)$ as $s\rightarrow +\infty$, is asymptotically equal to $\sqrt{-s/2}$ as $s\rightarrow -\infty$. In fact there is a complete asymptotic expansion in decreasing powers of $-s$, beginnning with this term [@mcleod_private]. Successive terms are easily computed. This result and later ones, become a little easier to state if we write $s=-t/2$: $$q(-t/2;1)={1\over 2}\sqrt{t}\left( 1 - {1\over t^3} - {73\over 2t^6}
-{10657\over 2 t^9} - {13912277\over 8 t^{12}}
+{\rm O}({1\over t^{15}})\right) \ \ \
(t\rightarrow +\infty)
\label{p2_asy}$$ Squaring and integrating and using ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}) we deduce $$R(s) = {1\over 4} s^2 + c - {1\over 8\, s} + {9\over 64\,  s^4} -
{189\over 128 \, s^7} + {21663\over 512\,  s^{10}} + {\rm O}({1\over s^{13}})
\ \ \ (s\rightarrow -\infty)$$ where $c$ is a constant. Substituting this into ([\[rDE\]](#rDE){reference-type="ref" reference="rDE"}) shows that $c=0$. Thus we obtain ([\[R_exp\]](#R_exp){reference-type="ref" reference="R_exp"}) and then, after integrating and exponentiating, ([\[E0_exp\]](#E0_exp){reference-type="ref" reference="E0_exp"}).

To obtain the asymptotic expansions of $q_n(s)$ in ([\[qn_defn\]](#qn_defn){reference-type="ref" reference="qn_defn"}), we differentiate ([\[p2\]](#p2){reference-type="ref" reference="p2"}) with respect to $\lambda$ and set $\lambda=1$. We obtain $$q_1^{\prime\prime}-\left(s+6q_0^2\right) q_1=0$$ (where $q_0(s)=q(s;1)$). Using ([\[p2_asy\]](#p2_asy){reference-type="ref" reference="p2_asy"}) we find two linearly independent solutions of this equation, one exponentially large at $-\infty$ and one exponentially small. Assuming the exponentially large one actually appears with a nonzero factor we obtain the asymptotic expansion $$q_1(-t/2)=c_1 {\exp({1\over 3} t^{3/2})\over t^{1/4}}
\left( 1 + {17\over 24\,  t^{3/2}} +{1513\over 2^7 3^2\,  t^3} +
{850193\over 2^{10} 3^4\,  t^{9/2}}+{407117521\over 2^{15} 3^5\,  t^{6}}
 + \cdots
\right)
\label{q1_asy}$$ where $c_1$ is a constant factor to be determined.

Successive differentiations of ([\[p2\]](#p2){reference-type="ref" reference="p2"}) with respect to $\lambda$, followed by setting $\lambda=1$, yields a sequence of linear differential equations for the $q_n$, $$q_n^{\prime\prime}-\left(s+6q_0^2\right) q_n= \varphi_n(q_0,\cdots,
q_{n-1}),$$ where $\varphi_n$ is a polynomial in the $q_m$ with $m<n$. For $n>1$ a particular solution dominates all solutions of the homogeneous equation. Therefore, in the asymptotics, no new unknown constant factors are introduced (unless we want to go "beyond all orders").

To deduce expansions for the $r(n;s)$ we must differentiate ([\[det_p2\]](#det_p2){reference-type="ref" reference="det_p2"}) $n$ times with respect to $\lambda$ and set $\lambda=1$. We find expressions of the form $$r(n;s)=\int_s^\infty (x-s) \psi(q_0,\cdots,q_n)\, dx
\label{r_integral}$$ where $\psi_n$ is a polynomial in $q_0, \cdots, q_n$. In particular we obtain (after setting $s=-t/2$) $$r(1;-t/2)={1\over 2}\int_{-\infty}^t (t-x) q_0(-x/2) q_1(-x/2)\, dx\, .$$ Substituting ([\[p2_asy\]](#p2_asy){reference-type="ref" reference="p2_asy"}) and ([\[q1_asy\]](#q1_asy){reference-type="ref" reference="q1_asy"}) into this integral gives the asymptotic expansion for $r(1;-t/2)$. The first order result is $$r(1;-t/2) \sim c_1 {\exp(t^{3/2}/3)\over t^{3/4}}$$ and comparing this with ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}) reveals that $$c_1={1\over 2\sqrt{2\pi}}\, .$$

We now state the expansions we have obtained in this way with the help of Mathematica. For $q_n$ with $n>2$, as $t\rightarrow +\infty$ $$\begin{aligned}
q_n(-t/2)&=& {n!\over 2^{3n/2}\, \pi^{n/2}}\,
{ \exp({n\over 3} t^{3/2}) \over
t^{3n/4-1/2}}
\Biggl( 1 +{59n-36\over 24}\>  t^{-3/2} + \nonumber \\
&& \quad {3481 n^2+8244 n -8496\over 1152 }\>  t^{-3} +
 {\rm O}(t^{-9/2})\Biggr).
\label{qn_asy}
\end{aligned}$$ For $n=1, 2$ the leading order term is as above. For $n=1$ the correction terms are given above in ([\[q1_asy\]](#q1_asy){reference-type="ref" reference="q1_asy"}). For $n=2$ the coefficient of $t^{-3/2}$ is as given above but the coefficient of $t^{-3}$ is ${5461/ 288}$. (Similar exceptional values of $n$ occurred in analogous expansions for the sine kernel [@btw].)  These expansions have been computed for $n\leq 10$ and are undoubtedly correct for all $n$. (In [@btw] the analogous expansions were proved for all $n$ by a backwards induction argument---such arguments should extend to the present case of $q_n$.)

For $r(n;s)$ we have obtained the following sharpening of ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}): as $t\rightarrow +\infty$ $$\begin{aligned}
r(n;-t/2)& =& {1! 2! \cdots (n-1)!\over 2^{n^2+n/2} \pi^{n/2} } \,
{\exp({n\over 3} t^{3/2})\over t^{3n^2/4}}
 \Biggl(
1+
{n(34 n^2 +31)\over 24}\>  t^{-3/2} + \nonumber \\
&& \quad {n^2(1156 n^4+6608 n^2 +11509)\over 1152 }\>  t^{-3}+
{\rm O}(t^{-9/2}) \Biggr).
\label{r_asy2}
\end{aligned}$$ This was established for $n\leq 6$. As was mentioned in the Introduction, when we substitute expansions ([\[qn_asy\]](#qn_asy){reference-type="ref" reference="qn_asy"}) into ([\[r_integral\]](#r_integral){reference-type="ref" reference="r_integral"}) a large amount of cancellation takes place, so that $r(n;s)$ is much smaller than might be anticipated. This also means that to deduce even the first-order asymptotics in ([\[r_asy2\]](#r_asy2){reference-type="ref" reference="r_asy2"}) for moderate values of $n$ one has to go very far out in the expansions ([\[qn_asy\]](#qn_asy){reference-type="ref" reference="qn_asy"}). Thus it is important that we have an alternative approach which yields asymptotic results for all values of $n$.
