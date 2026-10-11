---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-002-21-alternative-formulas-and-inter-relationships
section_title: "Alternative formulas and inter-relationships"
section_number: 2.1
pages: 7-8
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
---
As first noted in [@NF98], substitution of ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) in ([\[2.o\]](#2.o){reference-type="ref" reference="2.o"}) and use of ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) implies the decomposition $$\begin{aligned}
\label{2.1c}
S(x,y;\tau_x,\tau_y) = S_1(x,y;\tau_x,\tau_y) +  S_2(x,y;\tau_x,\tau_y)
\end{aligned}$$ where $$\begin{aligned}
\label{2.1d} 
 S_1(x,y;\tau_x,\tau_y) & = &
 \sqrt{w(x) w(y)} \sum_{\nu = 0}^{N-1}
  \frac{C_{\nu}(x) C_{\nu}(y)e^{-\gamma_\nu(\tau_x-\tau_y)}}{h_{\nu}}
\\
\label{2.1e}
S_2(x,y;\tau_x,\tau_y) & = &  \sqrt{w(x) w(y)}
\sum_{\nu = N}^{\infty} \sum_{k=0}^{N-1}
\frac{C_{\nu}(x)  e^{-\gamma_{\nu} \tau_x}}{h_{\nu}} 
\beta_{\nu k}
R_k(y;\tau_y
)
{\rm e}^{\gamma_k \tau_y}
\end{aligned}$$

Since $0 \leq \gamma_{1} < \gamma_{2} < \cdots$ (recall ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) and ([\[2.5\]](#2.5){reference-type="ref" reference="2.5"})) we see that for $N \rightarrow \infty$ and with all other parameters fixed, $S_{2} \rightarrow 0$ while $$\begin{aligned}
S_{1}\left(x, y; \tau_{x}, \tau_{y}\right) \rightarrow 
g\left(x, y; \tau_{x}-\tau_{y}\right) \, ,
\nonumber
\end{aligned}$$ assuming $\tau_{x} - \tau_{y} > 0$. The use of this result is that it shows $$\begin{aligned}
\label{2.1f}
\tilde{I}(x,y;\tau_x,\tau_y) = \int F(y',y;\tau_y) \Big (
g(x,y';\tau_x - \tau_y) - S(x,y';\tau_x,\tau_y) \Big ) \, dy'
\end{aligned}$$ valid for $\tau_{x} - \tau_{y} > 0$ (for $\tau_{x} - \tau_{y} < 0$ we can first use the first equation in ([\[2.1a\]](#2.1a){reference-type="ref" reference="2.1a"}), then apply ([\[2.1f\]](#2.1f){reference-type="ref" reference="2.1f"})).

We would also like to relate $D$ to $S$. Apparently this can be done naturally only when $\tau_{x} = 0$. Using the fact that $g(x, y; 0) = \delta(x - y)$ we see from ([\[2.d\]](#2.d){reference-type="ref" reference="2.d"}) and ([\[2.e\]](#2.e){reference-type="ref" reference="2.e"}) that $$\begin{aligned}
\label{2.1g}
F(x,y;0) = \left \{ \begin{array}{ll} {\rm sgn}(y-x), & \beta = 1 \\
2 {\partial \over \partial x} \delta (y-x), & \beta = 4. \end{array}
\right.
\end{aligned}$$ Recalling ([\[2.k\]](#2.k){reference-type="ref" reference="2.k"}), these formulas show $$\begin{aligned}
\nonumber
{d \over dx} \Phi_l(x;0) & = & 2 \sqrt{w(x)} R_k(x;0) \\
 \Phi_l(x;0) & = & - 2 {d \over dx} \Big (
\sqrt{w(x)} R_k(x;0) \Big ) \label{2.1g'}
\end{aligned}$$ in the two cases respectively. Thus for $\beta = 1$ initial conditions $$\begin{aligned}
\label{2.1h}
{d \over dx} S(x,y;0,\tau_y) = -2 D(x,y;0,\tau_y)
\end{aligned}$$ while for $\beta = 4$ initial conditions $$\begin{aligned}
\label{2.1i}
\int_y^x S(x',y;0,\tau_y) \, dx' = 2 D(x,y;0,\tau_y).
\end{aligned}$$
