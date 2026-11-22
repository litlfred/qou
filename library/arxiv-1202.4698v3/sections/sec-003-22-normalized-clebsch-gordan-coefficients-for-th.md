---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-003-22-normalized-clebsch-gordan-coefficients-for-th
section_title: "Normalized Clebsch-Gordan coefficients for the modular double"
section_number: 2.2
pages: 3-5
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 1.0
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The Clebsch-Gordan maps $\SC^{\al_3}_{\al_2,\al_1}:
\CP_{\al_2}\ot\CP_{\al_1}\ra\CP_{\al_3}$ were constructed in \cite{PT2}.
The defining intertwining property is
\begin{equation}\label{inter}
\SC^{\al_3}_{\al_2,\al_1}\cdot(\pi_{\al_2}\ot\pi_{\al_1})(\De(X))=
\pi_{\al_3}\cdot\SC^{\al_3}_{\al_2,\al_1}\,.
\end{equation}
In \cite{PT2} it was found that the $\SC^{\al_3}_{\al_2,\al_1}$
can be represented as integral operators
of the form
\begin{equation}\label{CGdef}
(\SC^{\al_3}_{\al_2,\al_1}\psi)(x_3)\,=\,
\int_{\BR^2}dx_1dx_2\;



\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)_b
\,\psi(x_2,x_1)\,,
\end{equation}
The intertwining property \rf{inter} will be satisfied 
if we take 
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)=
\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{\rm an}$, with 
\begin{align} \label{b-3j}
\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)_b^{\rm an} &
 = e^{-\pi \textup{i}(\Delta_{\alpha_3}-\Delta_{\alpha_1}-\Delta_{\alpha_2})/2} D_{-\frac{\textup{i}}{2} (\alpha_1+\alpha_2+\alpha_3-Q)}
\big(x_2-x_1-\textup{i} \fr{\alpha_3}{2}\big)
 \\ 
& \quad\times D_{-\frac{\textup{i}}{2}(Q+\alpha_2-\alpha_3-\alpha_1)}^{}
\big(x_2-x_3-\textup{i} \fr{\alpha_1}{2}\big)
D_{-\frac{\textup{i}}{2}(Q+\alpha_1-\alpha_3-\alpha_2)}^{}
\big(x_3-x_1-\textup{i} \fr{\alpha_2}{2}\big)\,. 
\notag\end{align}
In \rf{b-3j} we are using the notations 
$\Delta_{\alpha} = \alpha (Q-\alpha)$ with $Q=b+b^{-1}$ and
\begin{equation}
D_{\textup{i} \alpha}(x) = \frac{S_b(Q/2 - \textup{i} x + \alpha)}{S_b(Q/2 - \textup{i} x - \alpha)}.
\end{equation}
$S_b(x)$ is the so-called double Sine-function which is closely 
related to the functions called quantum dilogarithm in \cite{FK2}
hyperbolic gamma function in \cite{Ru},
and quantum exponential function in \cite{Wo}. 
Definition and relevant properties 
are recalled in Appendix \ref{Qdil}.

One should note, however, that our definition of 
the $3j$ coefficients \rf{b-3j} is not canonical,  we might equally
well use
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)_b'$ 
in \rf{CGdef},  with
\begin{equation} \label{3jrenorm}
\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,{}^{\al_1}_{x_1}\big)_{b}':=
M(\al_3,\al_2,\al_1)
\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{\rm an}\,.
\end{equation} 
This will satisfy \rf{inter} for arbitrary functions $M(\al_3,\al_2,\al_1)$.
A natural choice for $M(\al_3,\al_2,\al_1)$ can be determined by
requiring the Weyl-invariance of the Clebsch-Gordan maps.
In order to formulate this requirement, we will need the 
intertwining operator $\SR_{\al}:\CP_{\al}\ra\CP_{Q-\al}$
which can be represented explicitly as integral operator \cite{PT2}
\begin{equation}
(\SR_{\al}f)(x):=S_b(2\al)
\int_\BR dx'\;D_{-\textup{i}\al}(x-x')f(x)\,.
\end{equation}
We may now require that
\begin{equation}\label{Weyl}
\begin{aligned}
&
\SC^{\al_3}_{\al_2,\al_1}\cdot (1\ot\SR_{Q-\al_1})=
\SC^{\al_3}_{\al_2,Q-\al_1}\,,
\\
&\SC^{\al_3}_{\al_2,\al_1}\cdot (\SR_{Q-\al_2}\ot 1)
=\SC^{\al_3}_{Q-\al_2,\al_1}\,,
\end{aligned}\qquad
\SR_{\al_3}\cdot \SC^{\al_3}_{\al_2,\al_1}=\SC^{Q-\al_3}_{\al_2,\al_1}\,.
\end{equation}
We claim that \rf{Weyl} is satisfied if
we choose $M(\al_3,\al_2,\al_1)$ as 
\begin{align} \label{normcoef}
& M(\alpha_3,\alpha_2,\alpha_1)= \\ \nonumber & = 
\big(S_b(2Q-\alpha_1-\alpha_2-\alpha_3) S_b(Q-\alpha_1-\alpha_2+\alpha_3) 
S_b(\alpha_1+\alpha_3-\alpha_2) 
S_b(\alpha_2+\alpha_3-\alpha_1)\big)^{-\frac{1}{2}}.
\end{align}

To prove this claim let us consider, for example, 
the first of the equations in
\rf{Weyl}, which would follow from the identity 
\beq \label{intertw}
S_b(2\bar{\al}_1)
\int_{\BR}dx_1' \;
\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1'}\big)_b^{\rm an}
D_{-\textup{i} \bar{\al}_1}(x_1'-x_1)   =
\xi\, \big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\bar{\al}_1}_{x_1}\big)_b^{\rm an}\,,  
\eeq
where we use abbreviation $\bar{\alpha}=Q-\alpha$ and
$
\xi 
= S_b(\alpha_2+\al_3-\alpha_1) S_b(2Q-\alpha_1-\alpha_2-\alpha_3).
$
This identity can easily be rewritten in the form \cite[Equation (A.34)]{BT1}










in which it is recognized 
as the famous star-triangle relation, 
see e.g. \cite{BMS}. Proofs can be found in 
\cite{K2,V}.
It can also be derived easily
from the so-called elliptic beta-integral \cite{S1} 
following the strategy discussed in Appendix \ref{idproof}.

We will denote the Clebsch-Gordan coefficients
defined by  \rf{3jrenorm} with function $M(\al_3,\al_2,\al_1)$ 
given in \rf{normcoef} 
as $\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{}$. We would like to stress that 
both $\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{\rm an}$ and 
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{}$ have their virtues. 
While $\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{}$ has more natural symmetry
properties, the virtue of 
$\big(\,{}^{\al_3}_{x_3}\,|\,{}^{\al_2}_{x_2}\,
{}^{\al_1}_{x_1}\big)_b^{\rm an}$ is to have nice
analytic properties in all of its variables.
