---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-011-56-distribution-functions-in-the-initial-state
section_title: "Distribution functions in the initial state"
section_number: 5.6
pages: 33-34
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
---
With $m=0$ and $\tau_1 \to 0$ the dynamical distribution ([\[1.7\'\]](#1.7'){reference-type="ref" reference="1.7'"}) reduces to the $n$-point distribution function in the initial state. At $\beta = 1$ the formulas ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}), ([\[2.1f\]](#2.1f){reference-type="ref" reference="2.1f"}), ([\[2.1g\]](#2.1g){reference-type="ref" reference="2.1g"}) and ([\[2.1h\]](#2.1h){reference-type="ref" reference="2.1h"}) reclaim the well known [@MM91; @FP95; @NF95; @TW98] general formula $$\label{5.in}
\rho_{(n)}(x_1,\dots,x_n) =
{\rm Tdet} \left [ \begin{array}{cc}
S_1(x_j,x_k) & {1 \over 2} \int {\rm sgn}(x_k - y) S_1(x_j,y) \, dy -
{1 \over 2} {\rm sgn}(x_k - x_j) \\[.2cm]
{\partial \over \partial x_j} S_1(x_j,x_k) &
S_1(x_k,x_j) \end{array} \right ],$$ where $S_1(x_j,x_k) := S(x_j,x_k;0,0)$ as specified by ([\[2.o\]](#2.o){reference-type="ref" reference="2.o"}) with $\{R_j\}$ corresponding to the $\beta = 1$ initial condition. We remark that the integral in ([\[5.in\]](#5.in){reference-type="ref" reference="5.in"}) can be rewritten according to $${1 \over 2} \int {\rm sgn}(x_k - y) S_1(x_j,y) \, dy =
- \int_{x_j}^{x_k} S_1(x_j,y) \, dy.$$ At $\beta = 4$ these same formulas (with ([\[2.1h\]](#2.1h){reference-type="ref" reference="2.1h"}) replaced by ([\[2.1i\]](#2.1i){reference-type="ref" reference="2.1i"})) give that $$\label{5.in1}
\rho_{(n)}(x_1,\dots,x_n) =
{\rm Tdet} \left [ \begin{array}{cc}
S_4(x_j,x_k) & 
{\partial \over \partial x_k} S_1(x_k,x_j) \\[.2cm]
- \int_{x_k}^{x_j} S_4(y,x_k) \, dy &
S_4(x_k,x_j) \end{array} \right ],$$ where $S_4(x,y) := S(x,y;0,0)$ as specified by ([\[2.o\]](#2.o){reference-type="ref" reference="2.o"}) with $\{R_j\}$ therein corresponding to the $\beta = 4$ initial condition, again in accordance with the known result. In deriving ([\[5.in1\]](#5.in1){reference-type="ref" reference="5.in1"}) from ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) we assumed that none of the points $x_1,\dots,x_n$ are coincident; this is necessary because of the delta functions in ([\[2.b\]](#2.b){reference-type="ref" reference="2.b"}) with $\beta = 4$.

We can take the limit $t_X,t_Y \to 0$ in the formulas obtained for $S_1^{\rm edge}(X,Y;t_X,t_Y)$ (here edge denotes hard or soft) obtained in Section 3 and 4 to obtain the explicit form of $S_1^{\rm edge}(X,Y)$ in the scaled limit at the hard and soft edges. Thus from ([\[3.20\'\]](#3.20'){reference-type="ref" reference="3.20'"}), ([\[m.3\]](#m.3){reference-type="ref" reference="m.3"}), ([\[4.13\'\]](#4.13'){reference-type="ref" reference="4.13'"}) and ([\[ls4\]](#ls4){reference-type="ref" reference="ls4"}) we find $$\begin{aligned}
S_1^{\rm hard}(X,Y) & =  & K^{\rm hard}(X,Y) -
{J_{a+1}(\sqrt{Y}) \over 4 \sqrt{Y}} \Big (
\int_0^{\sqrt{X}} J_{a+1}(u) \, du - 1 \Big ) \label{te1}\\
S_4^{\rm hard}(X,Y) & =  & K^{\rm hard}(X,Y) -
{1 \over 4 X^{1/2}} J_{a-1}(X^{1/2}) \int_0^{Y^{1/2}} J_{a+1}(s) \, ds
\label{te2} \\
S_1^{\rm soft}(X,Y)  & =  & K^{\rm soft}(X,Y)
+ {1 \over 2} {\rm Ai}(Y) \Big ( 1 - \int_X^\infty {\rm Ai}(t) \, dt \Big )
\label{te3} \\
S_4^{\rm soft}(X,Y)  & =  & K^{\rm soft}(X,Y) -
{1 \over 2} {\rm Ai}(X) \int_Y^\infty {\rm Ai}(s) \, ds \label{te4}
\end{aligned}$$ where $$\begin{aligned}
K^{\rm hard}(X,Y) & := & {X^{1/2} J_{a+1}(X^{1/2}) J_a(Y^{1/2}) -
Y^{1/2} J_{a+1}(Y^{1/2}) J_a(X^{1/2}) \over 2 (X - Y) } \nonumber \\
 K^{\rm soft}(X,Y)  & := & { {\rm Ai}(X) {\rm Ai}'(Y) -
{\rm Ai}(Y) {\rm Ai}'(X) \over X - Y}.
\end{aligned}$$ In obtaining these formulas we have used ([\[5.2\]](#5.2){reference-type="ref" reference="5.2"}) and ([\[5.7\]](#5.7){reference-type="ref" reference="5.7"}) together with the known facts that [@Fo93] $$S_2^{\rm hard}(X,Y) = K^{\rm hard}(X,Y), \quad
S_2^{\rm soft}(X,Y) =  K^{\rm soft}(X,Y)$$ to rewrite the first of the integrals in the expressions ([\[3.20\'\]](#3.20'){reference-type="ref" reference="3.20'"}), ([\[m.3\]](#m.3){reference-type="ref" reference="m.3"}), ([\[4.13\'\]](#4.13'){reference-type="ref" reference="4.13'"}) and ([\[ls4\]](#ls4){reference-type="ref" reference="ls4"}). Also, Bessel function identities have been used in obtaining the second term in ([\[te1\]](#te1){reference-type="ref" reference="te1"}) and ([\[te2\]](#te2){reference-type="ref" reference="te2"}), while in the second term of ([\[te3\]](#te3){reference-type="ref" reference="te3"}) use has been made of the definite integral $$\int_{-\infty}^\infty {\rm Ai}(x) \, dx = 1.$$ We remark that in previous studies [@NF95; @Ve94] expression have been obtained for ([\[te1\]](#te1){reference-type="ref" reference="te1"}) and ([\[te2\]](#te2){reference-type="ref" reference="te2"}) which are of a more complicated structure. Also the expressions obtained in [@Fo93] for ([\[te3\]](#te3){reference-type="ref" reference="te3"}) and ([\[te4\]](#te4){reference-type="ref" reference="te4"}) are now seen to be in error.

Some caution must be exercised in applying these results at $\beta = 4$. In particular, the one body weight function used in ([\[2.b\]](#2.b){reference-type="ref" reference="2.b"}) at $\beta = 4$ is that corresponding to $\beta = 2$ in ([\[1.1\]](#1.1){reference-type="ref" reference="1.1"}) and ([\[1.2\]](#1.2){reference-type="ref" reference="1.2"}). To obtain from the above results expressions corresponding to the weight functions as written in ([\[1.1\]](#1.1){reference-type="ref" reference="1.1"}) and ([\[1.2\]](#1.2){reference-type="ref" reference="1.2"}) we must make the replacements $$S_4^{\rm hard}(X,Y) \mapsto 2  S_4^{\rm hard}(4X,4Y) \Big |_{a \to
2 a} , \quad S_4^{\rm soft}(X,Y) \mapsto {1 \over 2^{1/3}}
S_4^{\rm soft}(2^{2/3} X, 2^{2/3} Y).$$
