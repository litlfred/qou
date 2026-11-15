---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-004-23-normalized-b-6j-symbols-for-the-modular-doubl
section_title: "Normalized b-6j symbols for the modular double"
section_number: 2.3
pages: 5-6
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.955
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The composition of Clebsch-Gordan maps allows us to define two natural
families of projection operators 
\begin{align}
&({}_{}^s\SC^{\al_4}_{\al_3,\al_2,\al_1}(\al_s)\Psi)(x_4)\,=\,
\int_{\BR^3}dx_1dx_2dx_3\;
\CE_{\al_s}^{(s)}(A|X)\psi(x_3,x_2,x_1)\,,\\
&({}_{}^t\SC^{\al_4}_{\al_3,\al_2,\al_1}(\al_t)\Psi)(x_4)\,=\,
\int_{\BR^3}dx_1dx_2dx_3\;
\CE_{\al_t}^{(t)}(A|X)\psi(x_3,x_2,x_1)\,,
\end{align}
with integral kernels $\CE_{\al_s}^{(s)}(A|X)$
and $\CE_{\al_t}^{(t)}(A|X)$ given as
\begin{align}
&\CE_{\al_s}^{(s)}(A|X)\,=\,\int dx_s\;
\big(\,{}^{\al_4}_{x_4}\,|\,{}^{\al_3}_{x_3}\,{}^{\al_s}_{x_s}\big)_b
\big(\,{}^{\al_s}_{x_s}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)_b\,,\\
&\CE_{\al_t}^{(t)}(A|X)\,=\,\int dx_t\;
\big(\,{}^{\al_4}_{x_4}\,|\,{}^{\al_t}_{x_t}\,{}^{\al_1}_{x_1}\big)_b
\big(\,{}^{\al_t}_{x_t}\,|\,{}^{\al_3}_{x_3}\,{}^{\al_2}_{x_2}\big)_b\,.
\end{align}

The b-$6j$ symbols $\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b$ are then defined by the relations
\begin{equation}\label{fusion'}
\CE_{\al_s}^{(s)}(A|Z)\,=\,\int_{{Q/2}+\textup{i}\BR} d\mu(\al_t)\;
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b\,
\CE_{\al_t}^{(t)}(A|Z)\,,
\end{equation}
where the Plancherel measure $d\mu(\al)$ is explicitly given by
the expression
\begin{equation} \label{Pmeas}
d\mu(\al)\,=\,d\al\;M(\al)\,,\qquad M(\al):=|S_b(2\al)|^2\,.
\end{equation}
It is clear that the explicit expression for the b-$6j$ symbols
depends on the normalization chosen for the
Clebsch-Gordan maps. We will denote 
the $6j$ symbols corresponding to 
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{\rm an}$
and 
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{}$ by
$\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{\rm an}$
and
$\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{}$,
respectively.

The b-$6j$ symbols $\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{\rm an}$ were calculated in \cite{PT2}\footnote{The formula below coincides with equation (228) in \cite{Teschner:2001rv} after shifting $s \rightarrow u-\alpha_s-Q/2$. We have moved a factor $|S_b(2\al_t)|^2$ into the
measure of integration in \rf{fusion'}.}, 
\begin{align} \label{6j1}


\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\bar{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{\rm an}= & 
\;\frac{S_b(\alpha_2+\alpha_s-\alpha_1) S_b(\alpha_t+\alpha_1-\alpha_4)}{S_b(\alpha_2+\alpha_t-\alpha_3) S_b(\alpha_s+\alpha_3-\alpha_4)} \\
& \times  \int_{\CC}du\; 
S_b(-\alpha_2 \pm (\alpha_1-Q/2)+u) 
S_b(-\alpha_4 \pm (\alpha_3-Q/2) +u) \nonumber \\[-.5ex] &
\hspace{1.125cm}\times  
S_b(\alpha_2 + \alpha_4 \pm (\alpha_t-Q/2) - u) 
S_b(Q \pm (\alpha_s - Q/2) - u) \,.
\notag\end{align}
The following notation has been used
$
S_b(\alpha \pm u) :=
S_b(\alpha+u)
S_b(\alpha-u).
$
The integral in \rf{6j1} will be defined for $\al_k\in Q/2+\textup{i}\BR$ by
using a contour $\CC$ that approaches $Q+\textup{i}\BR$ near infinity,
and passes the real axis in $(Q/2,Q)$, and for other values 
of $\al_k$ by analytic continuation.

The b-$6j$ symbols corresponding to the 
normalization defined above are then given by the formula
\begin{equation} \label{norm}
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{}={\textstyle
\frac{M(\alpha_s,\alpha_2,\alpha_1)M(\alpha_4,\alpha_3,\alpha_s)}{M(\alpha_t,\alpha_3,\alpha_2) M(\alpha_4,\alpha_t,\alpha_1)} }
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{\rm an}\,.


\end{equation}
with $M(\al_3,\al_2,\al_1)$ being defined in \rf{normcoef}.
