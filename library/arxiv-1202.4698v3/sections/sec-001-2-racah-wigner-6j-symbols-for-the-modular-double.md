---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-001-2-racah-wigner-6j-symbols-for-the-modular-double
section_title: "Racah-Wigner 6j symbols for the modular double"
section_number: 2
pages: 2-5
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
text_source: latex
latex_prose_ratio: 0.692
latex_coverage_ratio: 0.963
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
\setcounter{equation}{0}

\subsection{Self-dual representations of $\CU_q(\fsl(2,\BR))$ and the modular
double}

We will be considering the Hopf-algebra $\CU_q(\fsl(2,\BR))$
which has generators $E$, $F$ and $K$ subject to the usual 
relations. This algebra has a one-parameter
family of representations $\CP_{\al}$
\begin{equation}\label{Paldef}
\begin{aligned}
 \SE_\al
\equiv\pi_{\al}(E):=e^{+\pi b\sx}\frac{\cosh\pi b (\spp-s)}{\sin\pi b^2}
e^{+\pi b\sx}\,,\\
\SF_\al\equiv\pi_{\al}(F):=e^{-\pi b\sx}\frac{\cosh\pi b (\spp+s)}{\sin\pi b^2}
e^{-\pi b\sx}\,,
\end{aligned}
\qquad \SK_\al\equiv\pi_\al(K):=e^{-\pi b\spp}\,,
\end{equation}
where $\spp$ and $\sx$ are operators acting on functions $f(x)$ as
$\spp f(x)=(2\pi i)^{-1}\frac{\pa}{\pa x}f(x)$ and $\sx f(x)=xf(x)$,
respectively.
In the definitions \rf{Paldef} we are parameterizing $q$ as
$q=e^{\pi \textup{i} b^2}$, and write the parameter $\al$ as 
$\al=Q/2+\textup{i}s$. There is a maximal dense 
subspace $\CP_{\al}\subset L^2(\BR)$ on which all polynomials formed out of 
$\SE_\al$, $\SF_\al$ and $\SK_\al$ are well-defined 
\cite[Appendix B]{Bytsko:2006ut}.


These representations are distinguished by
a remarkable self-duality property: They are automatically 
representations of the quantum group 
$\CU_{\tilde{q}}(\fsl(2,\BR))$, where 
$\tilde{q}=e^{\pi \textup{i}/b^2}$ if $q=e^{\pi \textup{i} b^2}$. 
These representations are generated from operators 
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$ 
which are defined by formulae obtained from 
those in \rf{Paldef} by replacing $b\ra b^{-1}$.
The subspace $\CP_\al$ is simultaneously 
a maximal domain for the polynomial functions of 
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$ 
\cite[Appendix B]{Bytsko:2006ut}.

This phenomenon was observed independently in \cite{PT1} and in 
\cite{FMD}. 
It is closely related to the fact that  $\SE_\al$, $\SF_\al$ and $\SK_\al$
are  {\it positive} 
self-adjoint generators which allows one to construct
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$
as $\SE^{1/b^2}_\al$
$\SF^{1/b^2}_\al$, $\SK^{{1}/{b^2}}_\al$ \cite{BT1}. 

It was proposed in \cite{PT1,BT1} to construct a
noncompact quantum group which has as {\it complete} set 
of tempered representations the self-dual representations
$\CP_{\al}$. 
It's gradually becoming clear how to realize this suggestion
precisely. 
Relevant steps in this direction were taken in \cite{BT1} by 
defining co-product, R-operator and Haar-measure of such a 
quantum group. Further important progress in this direction was
recently made in \cite{Ip}. 
Following \cite{FMD}, we will in the following call 
this noncompact quantum 
group the modular double of $\CU_q(\fsl(2,\BR))$.


\subsection{Normalized Clebsch-Gordan coefficients for the modular double}

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

\subsection{Normalized b-6j symbols for the modular double}

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


\subsection{3j symbols for the modular double}

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








\subsection{A new integral formula for the b-6j symbols}













One of our main results will be the following formula 
for the b-$6j$ symbols:
\begin{align}\label{6j3}


\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b^{}
&=\Delta(\al_s,\al_2,\al_1)\Delta(\al_4,\al_3,\al_s)\Delta(\al_t,\al_3,\al_2)
\Delta(\al_4,\al_t,\al_1)\\
&\qquad \times\int\limits_{\CC}du\;
S_b(u-\alpha_{12s}) S_b(u-\al_{s34}) S_b(u -\alpha_{23t}) 
S_b(u-\alpha_{1t4})
\notag \\[-1.5ex] & \hspace{2cm}\times 
S_b( \alpha_{1234}-u) S_b(\alpha_{st13}-u) 
S_b(\alpha_{st24}-u) S_b(2Q-u)\,.
\notag\end{align}
The expression involves the following ingredients:
\begin{itemize}
\item We have used the notations $\al_{ijk}=\al_i+\al_j+\al_k$,
$\al_{ijkl}=\al_i+\al_j+\al_k+\al_l$. 
\item $\Delta(\al_3,\al_2,\al_1)$ is defined as 
\begin{align}
&\Delta(\al_3,\al_2,\al_1)=\bigg(\frac{S_b(\alpha_1+\alpha_2+\alpha_s-Q)}{S_b(\alpha_1+\alpha_2-\alpha_s) 
S_b(\alpha_1+\alpha_s-\alpha_2) S_b(\alpha_2+\alpha_s-\alpha_1)} 
\bigg)^{\frac{1}{2}}\,.
\notag\end{align}
\item The integral is defined in the cases
that $\al_k\in Q/2+\textup{i}\BR$ by a contour $\CC$ which 
approaches $2Q+\textup{i}\BR$ near infinity,
and passes the real axis in the interval $(3Q/2,2Q)$.
For other values of the variables $\al_k$ it is defined by analytic 
continuation.
\end{itemize}
The reader may notice how closely the structure of the expression 
in \rf{6j3} resembles the well-known formulae for the classical 
$6j$ symbols. 

For establishing this relation, the
main step is contained in the following integral identity:
\begin{align}\label{6j2}


\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\bar\al_4}\,|\,
{}^{\al_s}_{\al_t}\big\}_b^{\rm an}=\mathcal{C}(\underline{\alpha}) 
\int_{\CC'} du\;& 
S_b(u-\alpha_{12s}) S_b(u-\al_{s34}) S_b(u -\alpha_{23t}) 
S_b(u-\alpha_{1t4})
\\ \times & 
S_b( \alpha_{1234}-u) S_b(\alpha_{st13}-u) 
S_b(\alpha_{st24}-u) S_b(2Q-u),
\notag\end{align}
where the contour $\CC'$ in \rf{6j2} runs between $2Q-\textup{i}\infty$
and $2Q+\textup{i}\infty$,
and $\underline{\alpha}$ is shorthand notation for the tuple 
$(\al_1,\al_2,\al_3,\al_4,\al_s,\al_t)$. The prefactor 
$\CC(\underline{\alpha})$ is explicitly given by the expression
\begin{align}
\mathcal{C}(\underline{\alpha}) =& 
\,S_b(-Q+\alpha_1+\alpha_4+\alpha_t) S_b(Q-\alpha_1-\alpha_2+\alpha_s) \nonumber \\ \times & \,S_b(-Q+\alpha_2+\alpha_3+\alpha_t) S_b(Q-\alpha_2+\alpha_3-\alpha_t) S_b(Q+\alpha_2-\alpha_3-\alpha_t) \\ 
\times & \,S_b(Q-\alpha_3+\alpha_4-\alpha_s) S_b(Q-\alpha_3-\alpha_4+\alpha_s) S_b(Q+\alpha_3-\alpha_4-\alpha_s). 
\notag\end{align}
The proof of identity \rf{6j2} is nontrivial. It is described in 
Appendix \ref{idproof}, based on recent advances in the theory
of elliptic generalizations of the 
hypergeometric functions \cite{S1,S2,S3}.
