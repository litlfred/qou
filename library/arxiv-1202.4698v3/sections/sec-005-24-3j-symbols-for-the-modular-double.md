---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-005-24-3j-symbols-for-the-modular-double
section_title: "3j symbols for the modular double"
section_number: 2.4
pages: 6-7
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.957
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
$3j$ coefficients describe invariants in tensor products of three 
representations. Such invariants may be constructed from 
the Clebsch-Gordon maps and the invariant bilinear form
$\CB:\CP_{\al}\ot\CP_{Q-\al}\ra \BC$ defined by \cite{PT2}
\begin{equation}
\CB(f,g):=\,\int_\BR dx\; f(x)g(x-\textup{i}Q/2)\,.
\end{equation}
We may thereby construct an invariant trilinear form 
$\CC_{\al_3,\al_2,\al_1}:\CP_{\al_3}\ot\CP_{\al_2}\ot\CP_{\al_1}\ra \BC$ as
\begin{equation}
\CC_{\al_3,\al_2,\al_1}(f_3,f_2,f_1):=\CB\big(\,f_3\,,\,
\SC^{Q-\al_3}_{\al_2,\al_1}\cdot f_2\ot f_1\,\big)\,.
\end{equation}
The form $\CC_{\al_3,\al_2,\al_1}$ can be represented as
\begin{equation}
\CC_{\al_3,\al_2,\al_1}(f_3,f_2,f_1)\,=\,
\int_{\BR^3}dx_3dx_2dx_1\;
\big(\,{}^{\al_3}_{x_3}\;{}^{\al_2}_{x_2}\;{}^{\al_1}_{x_1}\big)\,
f_3(x_3)f_2(x_2)f_1(x_1)
\end{equation}
with $3j$-symbols $\big(\,{}^{\al_3}_{x_3}\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)$
given in terms of the Clebsch-Gordan coefficients
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)$
as
\begin{equation}
\big(\,{}^{\al_3}_{x_3}\;{}^{\al_2}_{x_2}\;{}^{\al_1}_{x_1}\big)=
\big(\,{}^{Q-\al_3}_{x_3-\textup{i}Q/2}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)\,.
\end{equation}

We may similarly define 
\begin{equation}
\begin{aligned}
{}_{}^s\CC_{\al_4,\al_3,\al_2,\al_1}^{\al_s}(f_4,f_3,f_2,f_1):=
\CB\big(\,f_4\,,\,
{}_{}^s\SC^{Q-\al_4}_{\al_3,\al_2,\al_1}(\al_s)\cdot 
f_3\ot f_2\ot f_1\,\big)\,,\\
{}_{}^t\CC_{\al_4,\al_3,\al_2,\al_1}^{\al_t}(f_4,f_3,f_2,f_1):=
\CB\big(\,f_4\,,\,
{}_{}^t\SC^{Q-\al_4}_{\al_3,\al_2,\al_1}(\al_t)\cdot 
f_3\ot f_2\ot f_1\,\big)\,.
\end{aligned}
\end{equation}
The b-$6j$ symbols $\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}$ are then defined by the relation
\begin{equation}\label{6j-def}
{}_{}^s\CC_{\al_4,\al_3,\al_2,\al_1}^{\al_s}
\,=\,\int_{{Q/2}+\textup{i}\BR} d\mu(\al_t)\;
\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b\,
{}_{}^t\CC_{\al_4,\al_3,\al_2,\al_1}^{\al_t}\,.
\end{equation}
It follows that
\begin{equation}\label{6j-moddef}
\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b
=
\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\bar\al_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b\,,
\qquad
\bar\al_4:=Q-\al_4.




\end{equation}
The b-$6j$ symbols satisfy
the following identities \cite{PT1}
\begin{equation}\begin{aligned}
& \int_{Q/2+\textup{i}\BR^+}d\mu(\delta_{1})\; 
\fus{\al_1}{\al_2}{\al_3}{\beta_{2}}{\beta_{1}}{\delta_{1}}
\fus{\al_1}{\delta_1}{\al_4}{\al_5}{\beta_{2}}{\gamma_{2}}
\fus{\al_2}{\al_3}{\al_4}{\gamma_{2}}{\delta_{1}}{\gamma_{1}} 

=\fus{\beta_1}{\al_3}{\al_4}{\al_5}{\beta_{2}}{\gamma_{1}}
\fus{\al_1}{\al_2}{\gamma_1}{\al_{5}}{\beta_{1}}{\gamma_{2}}\,,\\
& \int_{Q/2+\textup{i}\BR^+}d\mu(\al_s)\;
\fus{\al_1}{\al_2}{\al_3}{\al_4}{\al_s}{\al_t}^*\,
\fus{\al_1}{\al_2}{\al_3}{\al_4}{\al_s}{\al_t'}
\,=\,(M(\al_t))^{-1}\de(\al_t-\al_t')\,.
\end{aligned}
\end{equation}
The explicit expression will again depend on the chosen normalization
of the Clebsch-Gordan maps, giving us two versions,
$\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b^{}$
and
$\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b^{\rm an}$,
respectively.
