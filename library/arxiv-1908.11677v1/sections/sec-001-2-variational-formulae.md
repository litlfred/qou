---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-001-2-variational-formulae
section_title: "Variational formulae"
section_number: 2
pages: 5-11
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposed to answer the question of what is the canonical shape in a given knot type"
---
\label{Sect. variational formulae}

We begin by recalling the definition of the function
$\scrN$.
For functions
$\vecu$,
$\vecv : \R/\calL\Z \to \R^d$,
where
$d=1$
or
$n$,
we set
\[
	\scrN(\vecu,\vecv)
	=
	\frac 1 { 2 \| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\Delta_4^3 \vecu \cdot \Delta_4^3 \vecv
	ds_3ds_4.
\]
We use
$\scrN(\vecu)$
instead of
$\scrN(\vecu,\vecu)$
for simplicity.

Setting
\begin{equation}\label{def Malpha}
	\scrM_\alpha(\vecf)
	=
	\frac{ \vphi_\alpha(\scrN(\vectau)) }{ \| \Delta \vecf \|_{\R^n}^\alpha },
\end{equation}
then the energy can be written as
\[
	\calE_{(\alpha,p)}(\vecf)
	=
	\iint_{(\R/\calL\Z)^2} ( \scrM_\alpha(\vecf) )^p ds_1ds_2.
\]
The first variational formula
$\scrG_{(\alpha,p)}$
can be derived as
\[
	\scrG_{(\alpha,p)}(\vecf)[\vecphi] ds_1ds_2
	=
	\delta \{ ( \scrM_\alpha(\vecf) )^p \} [\vecphi] ds_1ds_2
	+
	\scrM_\alpha(\vecf) \delta (ds_1ds_2)[\vecphi],
\]
and
\[
	\delta \{ (\scrM_\alpha(\vecf))^p \} [\vecphi]
	=
	p (\scrM_\alpha(\vecf))^{p-1} \delta \scrM_\alpha(\vecf) [\vecphi].
\]
The second variational formula
$\scrH_{(\alpha,p)}$
is calculated similarly.
Since
$\delta(ds_j) [\vecphi] = \vectau(s_j) \cdot \vecphi^\prime(s_j) ds_j$
holds
(see,
for example,
\cite{IN15}),
we obtain the following.
\begin{theorem}\label{variation}
$\scrG_{(\alpha,p)}(\vecf)[\vecphi]$
and
$\scrH_{(\alpha,p)}(\vecf)[\vecphi,\vecpsi]$
can be written as
\[
	\scrG_{(\alpha,p)}(\vecf)[\vecphi]
	=
	\sum_{i=1}^2 \scrG_i(\vecf)[\vecphi],
	\quad
	\scrH_{(\alpha,p)}(\vecf)[\vecphi,\vecpsi]
	=
	\sum_{i=1}^6 \scrH_i(\vecf)[\vecphi,\vecpsi],
\]
where
\begin{align*}
	\scrG_1(\vecf)[\vecphi]
	&=
	p(\scrM_\alpha(\vecf))^{p-1} \delta \scrM_\alpha(\vecf)[\vecphi],
\\
	\scrG_2(\vecf)[\vecphi]
	&=
	( \scrM_\alpha(\vecf) )^p
	( \vectau(s_1) \cdot \vecphi^\prime(s_1) + \vectau(s_2) \cdot \vecphi^\prime(s_2) ),
\\
	\scrH_1(\vecf)[\vecphi,\vecpsi]
	&=
	p(\scrM_\alpha(\vecf))^{p-1} \delta^2 \scrM_\alpha(\vecf) [\vecphi,\vecpsi],
\\
	\scrH_2(\vecf)[\vecphi,\vecpsi]
	&=
	p(p-1) ( \scrM_\alpha(\vecf) )^{p-2}
	\delta \scrM_\alpha(\vecf) [\vecphi] \delta \scrM_\alpha(\vecf) [\vecpsi],
\\
	\scrH_3(\vecf)[\vecphi,\vecpsi]
	&=
	\scrG_1(\vecf) [\vecphi]
	( \vectau(s_1) \cdot \vecpsi^\prime(s_1) + \vectau(s_2) \cdot \vecpsi^\prime(s_2) ),
\\
	\scrH_4(\vecf)[\vecphi,\vecpsi]
	&=
	\scrG_1(\vecf) [\vecpsi]
	( \vectau(s_1) \cdot \vecphi^\prime(s_1) + \vectau(s_2) \cdot \vecphi^\prime(s_2) ),
\\
	\scrH_5(\vecf)[\vecphi,\vecpsi]
	&=
	( \scrM_\alpha(\vecf) )^p
	\{
	\vecphi^\prime(s_1) \cdot \vecpsi^\prime(s_1) + \vecphi^\prime(s_2) \cdot \vecpsi^\prime(s_2)
\\
	&\quad
	\left.
	-2 ( \vectau(s_1) \cdot \vecphi^\prime(s_1) )( \vectau(s_1) \cdot \vecpsi^\prime(s_1) )
	-2 ( \vectau(s_2) \cdot \vecphi^\prime(s_2) )( \vectau(s_2) \cdot \vecpsi^\prime(s_2) )
	\right\},
\\
	\scrH_6(\vecf)[\vecphi,\vecpsi]
	&=
	( \scrM_\alpha(\vecf) )^p
	( \vectau(s_1) \cdot \vecphi^\prime(s_1) + \vectau(s_2) \cdot \vecphi^\prime(s_2) )
	( \vectau(s_1) \cdot \vecpsi^\prime(s_1) + \vectau(s_2) \cdot \vecpsi^\prime(s_2) ).
\end{align*}
\end{theorem}

In the remainder of this section,
we will give the exact expression of
$\delta \scrM_\alpha(\vecf)[\vecphi]$
and
$\delta^2 \scrM_\alpha(\vecf)[\vecphi,\vecpsi]$.
First we note that,
by \eqref{def Malpha},
we have
\begin{equation}
	\delta \scrM_\alpha(\vecf)[\vecphi]
	=
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta \scrN(\vectau) [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	-
	\frac \alpha 2
	\frac{ \vphi_\alpha(\scrN(\vectau)) \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }
	{ \| \Delta \vecf \|_{\R^n}^{\alpha+2} },
\label{delta Malpha}
\end{equation}
and therefore we need variational formulae for
$\scrN(\vectau)$,
and
$\| \Delta \vecf \|_{\R^n}^2$.
It follows from the definition of
$\scrN(\vectau)$
that 
$\delta \scrN(\vectau)$
can be written in terms of
$\delta \vectau$
as well as
$\delta \| \Delta \vecf \|_{\R^n}^2$.
We can derive the second variational formula from the corresponding ingredients.

Firstly,
we show the ingredients as Lemma \ref{variation lemma}.
The variational formulae
$\delta \scrN(\vectau)$
and
$\delta^2 \scrN(\vectau)$
will be given in the forthcoming Lemma \ref{variation N}.
Also,
we give representations of
$\delta \scrM_\alpha(\vecf)$
and
$\delta^2 \scrM_\alpha(\vecf)$
in Proposition \ref{variation Malpha}.

For
$\vecu$,
$\vecv : \R/\calL\Z \to \R^n$,
let
\[
	\scrK(\vecu,\vecv)
	=
	\frac{ \Delta \vecu \cdot \Delta \vecv }{ \| \Delta \vecf \|_{\R^n}^2 }.
\]

\begin{lemma}\label{variation lemma}
The following variational formulae hold.
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
$\delta \vectau(s_j)[\vecphi] = \vecphi^\prime(s_j) - (\vectau(s_j) \cdot \vecphi^\prime(s_j)) \vectau(s_j)$.
\item
$
	\delta \| \Delta^i_j \vectau \|_{\R^n}^2[\vecphi]
	=
	2\Delta^i_j \vectau \cdot \Delta^i_j \vecphi^\prime
	-
	\| \Delta^i_j \vectau \|_{\R^n}^2
	( \vectau(s_i) \cdot \vecphi^\prime(s_i) + \vectau(s_j) \cdot \vecphi^\prime(s_j) )
$.
\item
$
	\displaystyle
	\delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi]
	=
	2 \scrK(\vecf,\vecphi) \| \Delta \vecf \|_{\R^n}^2
$.
\item
$
	\displaystyle
	\delta \left( \frac 1 { \| \Delta \vecf \|_{\R^n}^2 } \right)[\vecphi]
	=
	-2
	\frac{ \scrK(\vecf,\vecphi) }{ \| \Delta \vecf \|_{\R^n}^2 }
$.
\item
$
	\displaystyle
	\delta^2 \| \Delta \vecf \|_{\R^n}^2[\vecphi,\vecpsi]
	=
	2 \scrK(\vecphi,\vecpsi) \| \Delta \vecf \|_{\R^n}^2
$.
\end{enumerate}
\end{lemma}

\begin{proof}
See
\cite[Lemma 1]{IN15}.
\end{proof}

Before proving Lemma \ref{variation N},
we establish the following sublemma.

\begin{lemma}\label{variation N sublemma}
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
Assume that
$\vecu : \R/\calL\Z \to \R^n$
is
$\vectau$
or
$\vecphi^\prime$.
Then,
$\delta \scrN(\vectau,\vecu)[\vecpsi]$
can be written as
\begin{align*}
	\delta \scrN(\vectau,\vecu) [\vecpsi]
	&=
	-2 \scrK(\vecf,\vecpsi) \scrN(\vectau,\vecu)
\\
	&\quad
	+
	\frac 1 { 2 \| \Delta \vecf \|_{\R^n} }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\{
	\delta (\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu)[\vecpsi]
\\
	&\qquad
	+
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecu )
	( \vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4) )
	\}
	ds_3ds_4,
\end{align*}
where
\begin{multline*}
	\delta (\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu)[\vecpsi]
\\
	=
	\left\{
	\begin{array}{ll}
		2\Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime
		-
		\| \Delta_4^3 \vectau \|_{\R^n}^2
		( \vectau(s_3) \cdot \vecphi^\prime(s_3) + \vectau(s_4) \cdot \vecphi^\prime(s_4) ),
		& \vecu = \vectau,
	\vspace{5pt}\\
	\begin{aligned}
		\Delta_4^3 \vecphi^\prime \cdot \Delta_4^3 \vecpsi^\prime
		&- ( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime )
		( \vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4) )
	\\
		&- \{ \Delta_4^3 ( \vectau \cdot \vecphi^\prime ) \}
		\{ \Delta_4^3 ( \vectau \cdot \vecpsi^\prime ) \},
	\end{aligned}
		& \vecu = \vecphi^\prime.
	\end{array}
	\right.
\end{multline*}
\item
It holds that
\[
	\delta \scrK(\vecf,\vecphi)[\vecpsi]
	=
	\scrK(\vecphi,\vecpsi)
	-
	2 \scrK(\vecf,\vecphi) \scrK(\vecf,\vecpsi).
\]
\end{enumerate}
\end{lemma}

\begin{proof}
\begin{enumerate}
\item By Lemma \ref{variation lemma},
we have
\begin{align*}
	\delta \scrN(\vectau,\vecu)[\vecpsi]
	&=
	\delta
	\left(
	\frac 1 { 2\| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu ds_3ds_4
	\right) [\vecpsi]
\\
	&=
	\frac 1 2
	\delta
	\left(
	\frac 1 { \| \Delta \vecf \|_{\R^n}^2 }
	\right) [\vecpsi]
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu ds_3ds_4
\\
	&\quad
	+
	\frac 1 { 2\| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\delta (\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu) [\vecpsi] ds_3ds_4
\\
	&\quad
	+
	\frac 1 { 2\| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} ( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecu )
	\delta(ds_3ds_4)[\vecpsi]
\\
	&=
	-2\scrK(\vecf,\vecpsi) \scrN(\vectau,\vecu)
	+
	\frac 1 { 2\| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\{
	\delta (\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu) [\vecphi]
\\
	&\qquad
	+
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecu )
	(\vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4))
	\}
	ds_3ds_4.
\end{align*}
It remains to calculate
$\delta (\Delta_4^3 \vectau \cdot \Delta_4^3 \vecu) [\vecphi]$.
Since the case where
$\vecu = \vectau$
may be handled by Lemma \ref{variation lemma},
we deal with the case where
$\vecu = \vecphi^\prime$.
Then,
it follows from Lemma \ref{variation lemma} and
$\delta \vecphi^\prime(s_j)[\vecpsi] = - (\vectau(s_j) \cdot \vecpsi^\prime(s_j)) \vecphi^\prime(s_j)$
that
\begin{align*}
	&
	\delta ( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime ) [\vecpsi]
\\
	&=
	\delta ( \Delta_4^3 \vectau ) [\vecpsi] \cdot \Delta_4^3 \vecphi^\prime
	+
	\Delta_4^3 \vectau \cdot \delta ( \Delta_4^3 \vecphi^\prime ) [\vecpsi]
\\
	&=
	\Delta_4^3 \vecpsi^\prime \cdot \Delta_4^3 \vecphi^\prime
	-
	\Delta_4^3 \{ ( \vectau \cdot \vecpsi^\prime ) \vectau \} \cdot \Delta_4^3 \vecphi^\prime
	-
	\Delta_4^3 \vectau \cdot \Delta_4^3 \{ ( \vectau \cdot \vecpsi^\prime ) \vecphi^\prime \}
\\
	&=
	\Delta_4^3 \vecphi^\prime \cdot \Delta_4^3 \vecpsi^\prime
	-
	[ ( \vectau(s_3) \cdot \vecpsi^\prime(s_3) ) \Delta_4^3 \vectau
	+ \{ \Delta_4^3 ( \vectau \cdot \vecpsi^\prime) \} \vectau(s_4) ] \cdot \Delta_4^3 \vecphi^\prime
\\
	&\quad
	-
	\Delta_4^3 \vectau \cdot [ \{ \Delta_4^3 (\vectau \cdot \vecpsi^\prime ) \} \vecphi^\prime(s_3)
	+ ( \vectau(s_4) \cdot \vecpsi^\prime(s_4) ) \Delta_4^3 \vecphi^\prime ]
\\
	&=
	\Delta_4^3 \vecphi^\prime \cdot \Delta_4^3 \vecpsi^\prime
\\
	&\quad
	-
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime )
	( \vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4) )
\\
	&\quad
	- \{ \Delta_4^3 ( \vectau \cdot \vecpsi^\prime ) \}
	( \vectau(s_4) \cdot \Delta_4^3 \vecphi^\prime + \Delta_4^3 \vectau \cdot \vecphi^\prime(s_3) )
\\
	&=
	\Delta_4^3 \vecphi^\prime \cdot \Delta_4^3 \vecpsi^\prime
\\
	&\quad
	-
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime )
	( \vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4) )
\\
	&\quad
	- \{ \Delta_4^3 ( \vectau \cdot \vecphi^\prime ) \} \{ \Delta_4^3 ( \vectau \cdot \vecpsi^\prime ) \}.
\end{align*}

\item Using Lemma \ref{variation lemma},
we have
\begin{align*}
	\delta \scrK(\vecf , \vecphi)[\vecpsi]
	&=
	\frac{ \delta ( \Delta \vecf \cdot \Delta \vecphi )[\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	+
	(\Delta \vecf \cdot \Delta \vecphi)
	\delta \left( \frac 1 { \| \Delta \vecf \|_{\R^n}^2 } \right) [\vecpsi]
\\
	&=
	\frac{ \Delta \vecpsi \cdot \Delta \vecphi }{ \| \Delta \vecf \|_{\R^n}^2 }
	-
	2
	\Delta \vecf \cdot \Delta \vecphi
	\frac{ \scrK(\vecf,\vecpsi) }{ \| \Delta \vecf \|_{\R^n}^2 }
\\
	&=
	\scrK(\vecphi,\vecpsi)
	-
	2 \scrK(\vecf,\vecphi) \scrK(\vecf,\vecpsi).
\end{align*}
\end{enumerate}
\end{proof}

\begin{lemma}\label{variation N}
$\delta\scrN(\vectau)[\vecphi]$
and
$\delta^2\scrN(\vectau)[\vecphi,\vecpsi]$
can be written as
\[
	\delta\scrN(\vectau)[\vecphi]
	=
	\sum_{i=1}^2 \scrR_i(\vecf)[\vecphi],
	\quad
	\delta^2\scrN(\vectau)[\vecphi,\vecpsi]
	=
	\sum_{i=1}^5 \scrS_i(\vecf)[\vecphi,\vecpsi],
\]
where
\begin{align*}
	\scrR_1 (\vecf)[\vecphi]
	&=
	-2\scrK(\vecf,\vecphi) \scrN(\vectau),
\\
	\scrR_2 (\vecf)[\vecphi]
	&=
	2\scrN(\vectau,\vecphi^\prime),
\\
	\scrS_1(\vecf)[\vecphi,\vecpsi]
	&=
	-2
	( \scrK(\vecphi,\vecpsi) -2 \scrK(\vecf,\vecphi) \scrK(\vecf,\vecpsi) )
	\scrN(\vectau),
\\
	\scrS_2(\vecf)[\vecphi,\vecpsi]
	&=
	-
	\scrK(\vecf,\vecphi) \delta \scrN(\vectau) [\vecpsi]
	-
	\scrK(\vecf,\vecpsi) \delta \scrN(\vectau) [\vecphi],
\\
	\scrS_3(\vecf)[\vecphi,\vecpsi]
	&=
	-2
	\scrK(\vecf,\vecpsi)
	\scrN(\vectau,\vecphi^\prime)
	-2
	\scrK(\vecf,\vecphi)
	\scrN(\vectau,\vecpsi^\prime),
\\
	\scrS_4(\vecf)[\vecphi,\vecpsi]
	&=
	2\scrN(\vecphi^\prime,\vecpsi^\prime),
\\
	\scrS_5(\vecf)[\vecphi,\vecpsi]
	&=
	-
	2 \scrN( (\vectau \cdot \vecphi^\prime) , (\vectau \cdot \vecpsi^\prime) ).
\end{align*}
\end{lemma}

\begin{proof}
By Lemmas \ref{variation lemma} and \ref{variation N sublemma},
we have
\begin{align*}
	\delta \scrN(\vectau)[\vecphi]
	&=
	-2\scrK(\vecf,\vecphi) \scrN(\vectau)
\\
	&\quad
	+
	\frac 1 { 2\| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\{
	\delta \| \Delta_4^3 \vectau \|_{\R^n}^2 [\vecphi]
\\
	&\qquad
	+
	\| \Delta_4^3 \vectau \|_{\R^n}^2
	(\vectau(s_3) \cdot \vecphi^\prime(s_3) + \vectau(s_4) \cdot \vecphi^\prime(s_4))
	\}
	ds_3ds_4
\\
	&=
	-2\scrK(\vecf,\vecphi) \scrN(\vectau)
	+
	\frac 1 { \| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime ds_3ds_4
\\
	&=
	-2\scrK(\vecf,\vecphi) \scrN(\vectau)
	+
	2\scrN(\vectau,\vecphi^\prime)
\\
	&=
	\sum_{i=1}^2 \scrR_i(\vecf)[\vecphi].
\end{align*}

Next we calculate
$\delta^2 \scrN(\vectau)[\vecphi,\vecpsi]$.
Firstly,
we have
\[
	\delta^2 \scrN(\vectau)[\vecphi,\vecpsi]
	=
	\frac 1 2 \delta ( \delta \scrN(\vectau)[\vecphi] ) [\vecpsi]
	+
	\frac 1 2 \delta ( \delta \scrN(\vectau)[\vecpsi] ) [\vecphi].
\]
By the symmetry with respect to
$\vecphi$
and
$\vecpsi$,
it is sufficient to calculate
$\delta ( \delta \scrN(\vectau)[\vecphi] ) [\vecpsi]$,
for which we first note that
\[
	\delta ( \delta \scrN(\vectau)[\vecphi] ) [\vecpsi]
	=
	\sum_{i=1}^2 \delta ( \scrR_i(\vecf)[\vecphi] ) [\vecpsi].
\]
Using Lemma \ref{variation N sublemma} again,
we can show that
\begin{align*}
	\delta (\scrR_1(\vecf)[\vecphi]) [\vecpsi]
	&=
	-2 \delta \scrK(\vecf,\vecphi) [\vecpsi] \scrN(\vectau)
	-2 \scrK(\vecf,\vecphi) \delta \scrN(\vectau) [\vecpsi]
\\
	&=
	-2
	\scrK(\vecphi,\vecpsi) \scrN(\vectau)
	+
	4
	\scrK(\vecf,\vecphi) \scrK(\vecf,\vecpsi)
	\scrN(\vectau)
\\
	&\quad
	-2
	\scrK(\vecf,\vecphi)
	\delta \scrN(\vectau)[\vecpsi],
\end{align*}
and
\begin{align*}
	\delta (\scrR_2(\vecf)[\vecphi]) [\vecpsi]
	&=
	2 \delta ( \scrN(\vectau,\vecphi^\prime) )[\vecpsi]
\\
	&=
	-4\scrK(\vecf,\vecpsi) \scrN(\vectau,\vecphi^\prime)
\\
	&\quad
	+
	\frac 1 { \| \Delta \vecf \|_{\R^n}^2 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	[
	\Delta_4^3 \vecphi^\prime \cdot \Delta_4^3 \vecpsi^\prime
\\
	&\qquad
	-
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime )
	( \vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4) )
\\
	&\qquad
	- \{ \Delta_4^3 ( \vectau \cdot \vecphi^\prime ) \} \{ \Delta_4^3 ( \vectau \cdot \vecpsi^\prime ) \}
\\
	&\qquad
	+
	( \Delta_4^3 \vectau \cdot \Delta_4^3 \vecphi^\prime )
	(\vectau(s_3) \cdot \vecpsi^\prime(s_3) + \vectau(s_4) \cdot \vecpsi^\prime(s_4))
	]
	ds_3ds_4
\\
	&=
	-4\scrK(\vecf,\vecpsi)
	\scrN(\vectau,\vecphi^\prime)
	+
	2\scrN(\vecphi^\prime,\vecpsi^\prime)
	-
	2 \scrN( (\vectau \cdot \vecphi^\prime) , (\vectau \cdot \vecpsi^\prime) ),
\end{align*}
from which the claim follows.
\end{proof}

Next,
we give expressions of
$\delta \scrM_\alpha(\vecf) [\vecphi]$
and
$\delta^2 \scrM_\alpha(\vecf) [\vecphi,\vecpsi]$
in terms of
$\scrN$,
$\delta \scrN$,
and
$\delta^2 \scrN$.

\begin{proposition}\label{variation Malpha}
$\delta \scrM_\alpha(\vecf) [\vecphi]$
and
$\delta^2 \scrM_\alpha(\vecf) [\vecphi,\vecpsi]$
can be written as
\[
	\delta \scrM_\alpha(\vecf) [\vecphi]
	=
	\sum_{i=1}^2 \scrP_i(\vecf) [\vecphi],
	\quad
	\delta^2 \scrM_\alpha(\vecf) [\vecphi,\vecpsi]
	=
	\sum_{i=1}^6 \scrQ_i(\vecf)[\vecphi,\vecpsi],
\]
where
\begin{align*}
	\scrP_1(\vecf)[\vecphi]
	&=
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha },
\\
	\scrP_2(\vecf)[\vecphi]
	&=
	-
	\frac \alpha 2 
	\scrM_\alpha(\vecf)
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 },
\\
	\scrQ_1(\vecf)[\vecphi,\vecpsi]
	&=
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta^2 \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha },
\\
	\scrQ_2(\vecf)[\vecphi,\vecpsi]
	&=
	-
	\frac \alpha 2
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 },
\\
	\scrQ_3(\vecf)[\vecphi,\vecpsi]
	&=
	\vphi_\alpha^{\prime\prime}(\scrN(\vectau))
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^{\frac \alpha 2} }
	\frac{ \delta \scrN(\vectau)[\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^{\frac \alpha 2} },
\\
	\scrQ_4(\vecf)[\vecphi,\vecpsi]
	&=
	-
	\frac \alpha 2
	\delta \scrM_\alpha(\vecf)[\vecpsi]
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 },
\\
	\scrQ_5(\vecf)[\vecphi,\vecpsi]
	&=
	-
	\frac \alpha 2
	\scrM_\alpha(\vecf)
	\frac{ \delta^2 \| \Delta \vecf \|_{\R^n}^2 [\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 },
\\
	\scrQ_6(\vecf)[\vecphi,\vecpsi]
	&=
	\frac \alpha 2
	\scrM_\alpha(\vecf)
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }.
\end{align*}
\end{proposition}

\begin{proof}
The assertion for
$\delta \scrM_\alpha(\vecf)$
follows immediately from \eqref{def Malpha} and \eqref{delta Malpha}.

Regarding
$\delta^2 \scrM_\alpha(\vecf)$,
we have
\[
	\delta^2\scrM_\alpha(\vecf)[\vecphi,\vecpsi]
	=
	\delta ( \delta\scrM_\alpha(\vecf)[\vecphi] )[\vecpsi]
	=
	\sum_{i=1}^2
	\delta (\scrP_i(\vecf)[\vecphi]) [\vecpsi],
\]
and
\begin{align*}
	\delta (\scrP_1(\vecf)[\vecphi]) [\vecpsi]
	&=
	\vphi_\alpha^{\prime\prime}(\scrN(\vectau)) \delta\scrN(\vectau)[\vecpsi]
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	+
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta^2 \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
\\
	&\quad
	-
	\frac \alpha 2
	\vphi_\alpha^\prime(\scrN(\vectau))
	\frac{ \delta \scrN(\vectau)[\vecphi] \delta\| \Delta \vecf \|_{\R^n}^2[\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^{\alpha+2} }
\\
	&=
	\scrQ_3(\vecf)[\vecphi,\vecpsi] + \scrQ_1(\vecf)[\vecphi,\vecpsi] + \scrQ_2(\vecf)[\vecphi,\vecpsi],
\\
	\delta (\scrP_2(\vecf)[\vecphi]) [\vecpsi]
	&=
	-
	\frac \alpha 2
	\delta\scrM_\alpha(\vecf)[\vecpsi]
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	-
	\frac \alpha 2
	\scrM_\alpha(\vecf)
	\frac{ \delta^2 \| \Delta \vecf \|_{\R^n}^2 [\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }
\\
	&\quad
	+
	\frac \alpha 2
	\scrM_\alpha(\vecf)
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] \delta \| \Delta \vecf \|_{\R^n}^2 [\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^4 }
\\
	&=
	\scrQ_4(\vecf)[\vecphi,\vecpsi] + \scrQ_5(\vecf)[\vecphi,\vecpsi] + \scrQ_6(\vecf)[\vecphi,\vecpsi].
\end{align*}
\end{proof}

Plugging Lemma \ref{variation N} and Proposition \ref{variation Malpha} into Theorem \ref{variation},
we obtain the first and second variational formulae of the
$(\alpha,p)$-O'Hara energies.
Since the expressions are rather lengthy,
we omit their explicit formulae here.
