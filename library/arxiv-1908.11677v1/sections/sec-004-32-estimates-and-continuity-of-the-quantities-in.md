---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-004-32-estimates-and-continuity-of-the-quantities-in
section_title: "Estimates and continuity of the quantities in (??)"
section_number: 3.2
pages: 12-15
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.624
latex_coverage_ratio: 0.93
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposed to answer the question of what is the canonical shape in a given knot type"
---
As we can see from Lemma \ref{variation N},
$\delta \scrN(\vectau)[\vecphi]$
and
$\delta \scrN(\vectau)[\vecphi,\vecpsi]$
may be expressed in terms of
$\scrN(\vecu,\vecv)$
and
$\scrK(\vecu,\vecv)$.
First,
we discuss
$\scrN(\vecu,\vecv)$.

\begin{lemma}\label{estimates N}
Assume that
$\vecf$
is bi-Lipschitz.
Then,
the following properties hold.
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
Let
$\alpha \in (0,\infty)$
and
$p \in [1,\infty)$
satisfy
$2 \leq \alpha p < 2p+1$.
If
$\vecu$,
$\vecv \in W^{\sigma,2p}(\R/\calL\Z , \R^d)$,
then there exists
$C=C(\vecf)>0$
such that
\[
	\left\|
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}
	\leq
	C [\vecu]_{W^{\sigma,2p}} [\vecv]_{W^{\sigma,2p}}.
\]
\item
Let
$0 < \beta \leq 1$.
If
$\vecu$,
$\vecv \in C^{0,\beta}(\R/\calL\Z , \R^d)$,
then there exists
$C=C(\vecf)>0$
such that
\[
	\left\|
	\scrD(\vecf)^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^\infty}
	\leq
	C [\vecu]_{C^{0,\beta}} [\vecv]_{C^{0,\beta}}.
\]
\item
Let
$0 < \beta \leq 1$.
If
$\vecu$,
$\vecv \in X^\beta(\R/\calL\Z , \R^d)$,
then for
$s \in \R/\calL\Z$,
\[
	\lim_{(s_1,s_2) \to (s,s)}
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	=
	\left\{
	\begin{array}{ll}
		0 & (0<\beta<1),
	\vspace{5pt}\\
		\displaystyle \frac 1 {12} \vecu^\prime(s) \cdot \vecv^\prime(s) & (\beta=1)
	\end{array}
	\right.
\]
holds.
\end{enumerate}
\end{lemma}

\begin{proof}
\begin{enumerate}
\item
By H\"{o}lder's inequality and the bi-Lipschitz continuity of
$\vecf$,
we have
\begin{align*}
	\left\|
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}^p
	&=
	\frac 1 {2^p}
	\int_{\R/\calL\Z} \int_{s_2-\frac \calL 2}^{s_2+\frac \calL 2}
	\frac 1 { \| \Delta \vecf \|_{\R^n}^{\alpha p+2p} }
	\left|
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\Delta_4^3 \vecu \cdot \Delta_4^3 \vecv
	ds_3ds_4
	\right|^p
	ds_1ds_2
\\
	&\leq
	C
	\int_{\R/\calL\Z} \int_{s_2-\frac \calL 2}^{s_2+\frac \calL 2}
	\frac 1 { |\Delta s|^{\alpha p+2} }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\| \Delta_4^3 \vecu \|_{\R^d}^p \| \Delta_4^3 \vecv \|_{\R^d}^p
	ds_3ds_4ds_1ds_2
\\
	&=
	(\dagger).
\end{align*}
We change variables
\[
	t_1=s_1-s_2,
	\quad
	t_2=s_2,
	\quad
	s_3=t_2+t_1t_3,
	\quad
	s_4=t_2+t_1t_4
\]
in
$(\dagger)$.
Then,
we obtain
\begin{multline*}
	(\dagger)
	=
	C
	\int_{\R/\calL\Z} \int_{-\frac \calL 2}^{\frac \calL 2}
	\frac 1 { |t_1|^{\alpha p} }
\\
	\times
	\int_0^1 \int_0^1
	\| \vecu(t_2+t_1t_3) - \vecu(t_2+t_1t_4) \|_{\R^d}^p
	\| \vecv(t_2+t_1t_3) - \vecv(t_2+t_1t_4) \|_{\R^d}^p
	dt_3dt_4dt_1dt_2
\\
	=
	(\ddagger).
\end{multline*}
We use Fubini's theorem and change variables
\[
	w_1 = (t_3-t_4) t_1,
	\quad
	w_2 = t_2+t_1t_4
\]
in
$(\ddagger)$.
Then,
we obtain
\begin{align*}
	(\ddagger)
	&=
	C
	\int_0^1 \int_0^1
	\int_{-\frac \calL 2}^{\frac \calL 2} \int_{\R/\calL\Z}
	\frac 1 { |t_1|^{\alpha p} }
\\
	&\qquad
	\times
	\| \vecu(t_2+t_1t_3) - \vecu(t_2+t_1t_4) \|_{\R^d}^p
	\| \vecv(t_2+t_1t_3) - \vecv(t_2+t_1t_4) \|_{\R^d}^p
	dt_2dt_1dt_3dt_4
\\
	&=
	C
	\int_0^1 \int_0^1
	\int_{-\frac \calL 2 |t_3-t_4|}^{\frac \calL 2 |t_3-t_4|} \int_{\R/\calL\Z}
	\frac 1 { |w_1|^{\alpha p} }
	|t_3-t_4|^{\alpha p-1}
\\
	&\qquad
	\times
	\| \vecu(w_1+w_2) - \vecu(w_2) \|_{\R^d}^p
	\| \vecv(w_1+w_2) - \vecv(w_2) \|_{\R^d}^p
	dw_1dw_2dt_3dt_4
\\
	&\leq
	C
	\int_{\R/\calL\Z} \int_{-\frac \calL 2}^{\frac \calL 2}
	\frac{ \| \vecu(w_1+w_2) - \vecu(w_2) \|_{\R^d}^p }{ |w_1|^{\frac{\alpha p} 2} }
	\frac{ \| \vecv(w_1+w_2) - \vecv(w_2) \|_{\R^d}^p }{ |w_1|^{\frac{\alpha p} 2} }
	dw_1dw_2
\\
	&\leq
	C [\vecu]_{W^{\sigma,2p}}^p [\vecv]_{W^{\sigma,2p}}^p,
\end{align*}
by H\"{o}lder's inequality,
and the claim holds.
\item
Without loss of generality,
we assume that
$s_1$,
$s_2 \in \R/\calL\Z$
satisfy
$\displaystyle 0 < |\Delta s| < \calL/2$.
Then,
we have
\begin{align*}
	\left|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right|
	&\leq
	C
	|\Delta s|^{-2\beta-2}
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\| \Delta_4^3 \vecu \|_{\R^d} \| \Delta_4^3 \vecv \|_{\R^d}
	ds_3ds_4
\\
	&\leq
	C
	|\Delta s|^{-2}
	\int_{s_2}^{s_1} \int_{s_2}^{s_1}
	\frac{ \| \Delta_4^3 \vecu \|_{\R^d} }{ |\Delta_4^3 s|^\beta }
	\frac{ \| \Delta_4^3 \vecv \|_{\R^d} }{ |\Delta_4^3 s|^\beta }
	ds_3ds_4
\\
	&\leq
	C [\vecu^\prime]_{C^{0,\beta}} [\vecv^\prime]_{C^{0,\beta}}.
\end{align*}
\item
First,
we consider the case where
$0<\beta<1$,
i.e.\ $\vecu$,
$\vecv \in h^{0,\beta}(\R/\calL\Z , \R^d)$.
As is well known,
the little H\"{o}lder space
$h^{0,\beta}$
is characterized as
\[
	h^{0,\beta}(\R/\calL\Z , \R^d)
	=
	\left\{
	\vecu \in C^{0,\beta}(\R/\calL\Z , \R^d)
	\,\left|\,
	\lim_{R \to +0} [\vecu]_{C^{0,\beta},R} = 0
	\right.
	\right\},
\]
where
\[
	[\vecu]_{C^{0,\beta},R}
	=
	\sup_{\substack{s_1,s_2 \in \R/\calL\Z\\0<|\Delta s|<R}}
	\frac{ \| \Delta \vecu \|_{\R^d} }{ |\Delta s|^\beta }.
\]
For
$R>0$,
let
$s_1$,
$s_2 \in \R/\calL\Z$
satisfy
$0<|\Delta s|<R$.
Then,
we have
\begin{equation}\label{Req}
	\left|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right|
	\leq
	C [\vecu]_{C^{0,\beta},R} [\vecv]_{C^{0,\beta},R}.
\end{equation}
Taking
$\limsup$
on left-hand side in \eqref{Req},
we have
\[
	\limsup_{(s_1,s_2) \to (s,s)}
	\left|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right|
	\leq
	C [\vecu]_{C^{0,\beta},R} [\vecv]_{C^{0,\beta},R}.
\]
Taking
$R \to +0$
on right-hand side,
we obtain
\[
	\lim_{(s_1,s_2) \to (s,s)}
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	= 0.
\]
Next,
we assume
$\vecu$,
$\vecv \in C^1$.
If
$s_5$,
$s_6 \in \R/\calL\Z$
are such that
$\| (s_5,s_6) - (s,s) \|_{\R^2}$
is sufficiently small,
we can take
$\epsi>0$
arbitrarily such that
\[
	\| \vecu^\prime(s_5) - \vecu^\prime(s) \|_{\R^d}
	\leq
	\frac \epsi { 2( \| \vecv^\prime \|_{L^\infty} + 1) },
	\quad
	\| \vecv^\prime(s_6) - \vecv^\prime(s) \|_{\R^d}
	\leq
	\frac \epsi { 2( \| \vecu^\prime \|_{L^\infty} + 1) }.
\]
Then,
using the fact that
\[
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3} ds_5ds_6ds_3ds_4 = \frac 1 6 |\Delta s|^2,
\]
we have
\begin{align*}
	&
	\left|
	\frac 1 { |\Delta s|^4 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3}
	\vecu^\prime(s_5) \cdot \vecv^\prime(s_6)
	ds_5ds_6ds_3ds_4
	-
	\frac 1 6 \vecu^\prime(s) \cdot \vecv^\prime(s)
	\right|
\\
	&\leq
	\frac 1 { |\Delta s|^4 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3}
	| \vecu^\prime(s_5) \cdot \vecv^\prime(s_6) - \vecu^\prime(s) \cdot \vecv^\prime(s) |
	ds_5ds_6ds_3ds_4
\\
	&\leq
	\frac 1 { |\Delta s|^4 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3}
	( \| \vecu^\prime(s_5) \|_{\R^d} \| \vecv^\prime(s_6) - \vecv^\prime(s) \|_{\R^d}
\\
	&\qquad
	+
	\| \vecv^\prime(s) \|_{\R^d} \| \vecu^\prime(s_5) - \vecu^\prime(s) \|_{\R^d} )
	ds_5ds_6ds_3ds_4
\\
	&\leq
	\epsi.
\end{align*}
Hence,
we have
\begin{multline*}
	\lim_{(s_1,s_2) \to (s,s)}
	\frac 1 { |\Delta s|^4 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3}
	\vecu^\prime(s_5) \cdot \vecv^\prime(s_6)
	ds_5ds_6ds_3ds_4
\\
	=
	\frac 1 6 \vecu^\prime(s) \cdot \vecv^\prime(s).
\end{multline*}
Using this and
\[
	\lim_{(s_1,s_2) \to (s,s)}
	\frac{ |\Delta s| }{ \| \Delta \vecf \|_{\R^n} }
	=
	\frac 1 { \| \vectau(s) \|_{\R^n} }
	= 1,
\]
we obtain
\begin{align*}
	&
	|\Delta s|^{\alpha-2} \frac{ \scrN(\vecu,\vecv) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
\\
	&=
	\frac 1 2
	\frac{ |\Delta s|^{\alpha+2} }{ \| \Delta \vecf \|_{\R^n}^{\alpha+2} }
	\frac 1 { |\Delta s|^4 }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \int_{s_4}^{s_3} \int_{s_4}^{s_3}
	\vecu^\prime(s_5) \cdot \vecv^\prime(s_6)
	ds_5ds_6ds_3ds_4
\\
	&\to
	\frac 1 {12} \vecu^\prime(s) \cdot \vecv^\prime(s)
	\quad
	\text{as}\ (s_1,s_2) \to (s,s).
\end{align*}
\end{enumerate}
\end{proof}

Since the function
$\scrK(\vecu,\vecv)$
fulfills
\[
	| \scrK(\vecu,\vecv) | \leq C \| \vecu^\prime \|_{L^\infty} \| \vecv^\prime \|_{L^\infty},
	\quad
	\lim_{(s_1,s_2) \to (s,s)} \scrK(\vecu,\vecv)
	=
	\vecu^\prime(s) \cdot \vecv^\prime(s),
\]
we obtain estimates and continuity of
$\displaystyle \frac{ \delta \| \Delta \vecf \|_{\R^n}^2 [\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 }$
and
$\displaystyle \frac{ \delta^2 \| \Delta \vecf \|_{\R^n}^2 [\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }$
from Lemma \ref{variation lemma} as follows.

\begin{lemma}\label{estimates deltaDelta}
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
Assume that
$\vecf$,
$\vecphi$,
$\vecpsi \in W^{1,\infty}(\R/\calL\Z,\R^n)$
and
$\vecf$
is bi-Lipschitz.
Then,
there exists
$C=C(\vecf)>0$
such that
\[
	\left\| \frac{ \delta \| \Delta \vecf \|_{\R^n}^2[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 } \right\|_{L^\infty}
	\leq
	C \| \vecphi^\prime \|_{L^\infty},
	\quad
	\left\|
	\frac{ \delta^2 \| \Delta \vecf \|_{\R^n}^2[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	\right\|_{L^\infty}
	\leq
	C \| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty}.
\]
\item
If
$\vecf$,
$\vecphi$,
$\vecpsi \in C^1(\R/\calL\Z,\R^n)$,
then it follows that
\begin{align*}
	\lim_{(s_1,s_2) \to (s,s)}
	\frac{ \delta \| \Delta \vecf \|_{\R^n}^2[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	&=
	\vectau(s) \cdot \vecphi^\prime(s),
\\
	\lim_{(s_1,s_2) \to (s,s)}
	\frac{ \delta^2 \| \Delta \vecf \|_{\R^n}^2[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	&=
	\vecphi^\prime(s) \cdot \vecpsi^\prime(s)
\end{align*}
for
$s \in \R/\calL\Z$.
\end{enumerate}
\end{lemma}

To deal with
$\scrS_5(\vecf)$,
we need estimates for
$\vectau \cdot \vecphi^\prime$.
The proof is easy,
therefore we omit the details.

\begin{lemma}\label{estimates inner product}
Assume that
$\vecf$
is bi-Lipschitz.
Then,
the following properties hold.
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
Let
$\alpha \in (0,\infty)$
and
$p \in [1,\infty)$
satisfy
$2 \leq \alpha p < 2p+1$.
If
$\vecf$,
$\vecphi \in W^{1+\sigma,2p}(\R/\calL\Z , \R^n) \cap W^{1,\infty}(\R/\calL\Z , \R^d)$,
then there exists
$C=C(\vecf)>0$
such that
\[
	[(\vectau \cdot \vecphi^\prime)]_{W^{\sigma,2p}}
	\leq
	C
	( \| \vectau \|_{L^\infty} [\vecphi^\prime]_{W^{\sigma,2p}}
	+ [\vectau]_{W^{\sigma,2p}} \| \vecphi^\prime \|_{L^\infty} ).
\]
\item
Let
$0 < \beta \leq 1$.
If
$\vecf$,
$\vecphi \in C^{1,\beta}(\R/\calL\Z , \R^n)$,
then it holds that
\[
	[(\vectau \cdot \vecphi^\prime)]_{C^{0,\beta}}
	\leq
	\| \vectau \|_{L^\infty} [\vecphi^\prime]_{C^{0,\beta}} + [\vectau]_{C^{0,\beta}} \| \vecphi^\prime \|_{L^\infty}.
\]
\item
Let
$0 < \beta \leq 1$.
If
$\vectau$,
$\vecphi^\prime \in X^\beta(\R/\calL\Z , \R^n)$,
then
$(\vectau \cdot \vecphi^\prime) \in X^\beta(\R/\calL\Z , \R)$.
Moreover,
if
$\vecf$,
$\vecphi \in C^2(\R/\calL\Z , \R^n)$,
then it holds that
\[
	\frac d {ds} (\vectau(s) \cdot \vecphi^\prime(s))
	=
	\veckappa(s) \cdot \vecphi^\prime(s) + \vectau(s) \cdot \vecphi^{\prime\prime}(s)
\]
for
$s \in \R/\calL\Z$.
\end{enumerate}
\end{lemma}


\subsection{Proof of Theorem \ref{mainthm}}

In this subsection we complete the proof of Theorem \ref{mainthm} combining the facts in previous subsection.
First,
we show the
$L^1$-estimates of the first and second variational formulae for
$\scrM_{(\alpha,p)}(\vecf)$.
Using the expression of the first and second variational formulae for
$\scrN(\vectau)$
in Lemma \ref{variation N},
it follows that
\begin{align*}
	\left\| \frac{ \scrR_1(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty},
\\
	\left\| \frac{ \scrR_2(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C [ \vecphi^\prime ]_{W^{\sigma,2p}},
\\
	\left\| \frac{ \scrS_1(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty},
\\
	\left\| \frac{ \scrS_2(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C
	\{
	\| \vecphi^\prime \|_{L^\infty}
	( \| \vecpsi^\prime \|_{L^\infty} + [\vecpsi^\prime]_{W^{\sigma,2p}} )
	+
	\| \vecpsi^\prime \|_{L^\infty}
	( \| \vecphi^\prime \|_{L^\infty} + [\vecphi^\prime]_{W^{\sigma,2p}} )
	\},
\\
	\left\| \frac{ \scrS_3(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C ( \| \vecpsi^\prime \|_{L^\infty} [ \vecphi^\prime ]_{W^{\sigma,2p}}
	+
	\| \vecphi^\prime \|_{L^\infty} [ \vecpsi^\prime ]_{W^{\sigma,2p}} ),
\\
	\left\| \frac{ \scrS_4(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C [\vecphi^\prime]_{W^{\sigma,2p}} [\vecpsi^\prime]_{W^{\sigma,2p}},
\\
	\left\| \frac{ \scrS_5(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^p}
	&\leq
	C ( [\vecphi^\prime]_{W^{\sigma,2p}} + \| \vecphi^\prime \|_{L^\infty} )
	( [\vecpsi^\prime]_{W^{\sigma,2p}} + \| \vecpsi^\prime \|_{L^\infty} )
\end{align*}
by Lemmas \ref{estimates N} and \ref{estimates inner product}.
Hence,
from these estimates and Lemma \ref{estimates deltaDelta},
we obtain
\begin{align*}
	\left\|
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty}
\\
	\left\|
	\frac{ \delta \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty}
	\| \vecpsi^\prime \|_{W^{\sigma,2p} \cap L^\infty},
\end{align*}
and
$L^1$-estimates for
$\scrG_{(\alpha,p)}(\vecf)$
and
$\scrH_{(\alpha,p)}(\vecf)$.

Next,
we consider
$L^\infty$-estimates of
$\scrM_{(\alpha,p)}(\vecf)$,
$\scrG_{(\alpha,p)}(\vecf)$,
and
$\scrH_{(\alpha,p)}(\vecf)$
with the weight
$|\Delta s|^{\alpha-2\beta}$.
We assume that
$\vecf$,
$\vecphi$,
$\vecpsi \in C^{1,\beta}$
and
$s_1$,
$s_2 \in \R/\calL\Z$
satisfy
$\displaystyle 0<|\Delta s|<\calL/2$.
Because we have
\[
	1-x^\alpha \leq \left( \frac \alpha 2 +1 \right) (1-x^2)
\]
for all
$x \in [0,1]$,
it follows that
\begin{align}
	|\Delta s|^{\alpha-2\beta} \scrM_\alpha(\vecf)
	&\leq
	C \frac 1 { |\Delta s|^{2\beta} }
	\left( 1-\frac{ \| \Delta \vecf \|_{\R^n}^\alpha }{ |\Delta s|^\alpha } \right)
\nonumber\\
	&\leq
	C \frac 1 { |\Delta s|^{2\beta} }
	\left( 1-\frac{ \| \Delta \vecf \|_{\R^n}^2 }{ |\Delta s|^2 } \right)
\nonumber\\
	&\leq
	C \frac 1 { |\Delta s|^{2\beta+2} }
	\int_{s_2}^{s_1} \int_{s_2}^{s_1} \| \Delta_4^3 \vectau \|_{\R^n}^2 ds_3ds_4
\nonumber\\
	&\leq
	C.
\label{estimate D Malpha}
\end{align}
Moreover,
by Lemmas \ref{estimates N}--\ref{estimates inner product},
we have
\begin{align*}
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrR_1(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty},
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrR_2(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C [\vecphi^\prime]_{C^{0,\beta}},
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrS_1(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty},
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrS_2(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C \{
	\| \vecphi^\prime \|_{L^\infty}
	( \| \vecpsi^\prime \|_{L^\infty} + [\vecpsi^\prime]_{C^{0,\beta}} )
	+
	\| \vecpsi^\prime \|_{L^\infty}
	( \| \vecphi^\prime \|_{L^\infty} + [\vecphi^\prime]_{C^{0,\beta}} )
	\},
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrS_3(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C ( \| \vecpsi^\prime \|_{L^\infty} [\vecphi^\prime]_{C^{0,\beta}}
	+
	\| \vecphi^\prime \|_{L^\infty} [\vecpsi^\prime]_{C^{0,\beta}} ),
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrS_4(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C [\vecphi^\prime]_{C^{0,\beta}} [\vecpsi^\prime]_{C^{0,\beta}},
\\
	\left\| |\Delta s|^{\alpha-2\beta} \frac{ \scrS_5(\vecf)[\vecphi,\vecpsi] }
	{ \| \Delta \vecf \|_{\R^n}^\alpha } \right\|_{L^\infty}
	&\leq
	C ( [\vecphi^\prime]_{C^{0,\beta}} + \| \vecphi^\prime \|_{L^\infty} )
	( [\vecpsi^\prime]_{C^{0,\beta}} + \| \vecpsi^\prime \|_{L^\infty} ).
\end{align*}
Therefore,
we obtain
\begin{align*}
	\left\|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{C^{0,\beta}}
\\
	\left\|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \delta^2 \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{C^{0,\beta}}
	\| \vecpsi^\prime \|_{C^{0,\beta}},
\end{align*}
and the
$L^\infty$-estimates for
$\scrM_{(\alpha,p)}(\vecf)$,
$\scrG_{(\alpha,p)}(\vecf)$,
and
$\scrH_{(\alpha,p)}(\vecf)$
with the weight
$|\Delta s|^{\alpha-2\beta}$.

Lastly,
we consider the continuity.
Because continuity on the outside of the diagonal set is clear,
we consider the property on the diagonal set.
First,
we assume
$\vecf$,
$\vecphi$,
$\vecpsi \in h^{1,\beta}$
with
$0 < \beta < 1$,
and
$\vecf$
is bi-Lipschitz.
Let
$R>0$
be sufficiently small.
In a similar manner to the proof of \eqref{estimate D Malpha},
it holds that
\[
	|\Delta s|^{\alpha-2\beta} \scrM_\alpha(\vecf)
	\leq
	\tilde{C} [\vectau]_{C^{0,\beta},R}
\]
for
$0<|\Delta s|<R$,
and therefore
\[
	\lim_{(s_1,s_2) \to (s,s)}
	|\Delta s|^{\alpha-2\beta} \scrM_\alpha(\vecf)
	= 0,
\]
where
$\tilde{C}$
is a positive constant depending only on
$\alpha$,
$p$,
and
$C_{\text b}$.
Moreover,
by Lemma \ref{estimates N},
we have
\begin{align*}
	\lim_{(s_1,s_2) \to (s,s)}
	\left|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrR_i(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right|
	&=
	0,
	\quad
	(i=1,2),
\\
	\lim_{(s_1,s_2) \to (s,s)}
	\left|
	|\Delta s|^{\alpha-2\beta}
	\frac{ \scrS_i(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right|
	&=
	0,
	\quad
	(i=1,\ldots,5).
\end{align*}
Considering Lemma \ref{estimates deltaDelta},
we obtain the desired continuity when
$\vecf$,
$\vecphi$,
$\vecpsi \in h^{1,\beta}$
with
$0<\beta<1$.

Next,
we consider the case where
$\beta=1$.
We denote the curvature vector of
$\vecf$
by
$\veckappa$,
i.e.\ $\veckappa = \vecf^{\prime\prime}$.
Using Lemma \ref{estimates N} and L'Hospital's theorem,
we have
\begin{align*}
	|\Delta s|^{\alpha-2} \scrM_\alpha(\vecf)
	&=
	|\Delta s|^{\alpha-2} \frac{ \vphi_\alpha(\scrN(\vectau)) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
\\
	&=
	|\Delta s|^{\alpha-2} \frac{ \vphi_2(\scrN(\vectau)) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\frac{ \vphi_\alpha(\scrN(\vectau)) }{ \vphi_2(\scrN(\vectau)) }
\\
	&=
	|\Delta s|^{\alpha-2} \frac{ \scrN(\vectau) }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\frac 1 { 1+\scrN(\vectau) }
	\frac{ \vphi_\alpha(\scrN(\vectau)) }{ \vphi_2(\scrN(\vectau)) }
\\
	&\to
	\frac \alpha {24} \| \veckappa(s) \|_{\R^n}^2
	\quad
	\text{as}\ (s_1,s_2) \to (s,s).
\end{align*}
Similarly,
it follows that
\begin{align*}
	|\Delta s|^{\alpha-2}
	\frac{ \scrR_1(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	-\frac 1 6 \vectau(s) \cdot \vecphi^\prime(s) \| \veckappa(s) \|_{\R^n}^2,
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrR_2(\vecf)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	\frac 1 6 \veckappa(s) \cdot \vecphi^{\prime\prime}(s),
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrS_1(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	-\frac 1 6
	\{
	\vecphi^\prime(s) \cdot \vecpsi^\prime(s)
	-
	(\vectau(s) \cdot \vecphi^\prime(s)) (\vectau(s) \cdot \vecpsi^\prime(s))
	\}
	\| \veckappa(s) \|_{\R^n}^2,
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrS_2(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	\frac 1 6 ( \vectau(s) \cdot \vecphi^\prime(s) )
	( \veckappa(s) \cdot \vecpsi^{\prime\prime}(s)
	- \vectau(s) \cdot \vecpsi^\prime(s) \| \veckappa(s) \|_{\R^n}^2)
\\
	&\quad
	+
	\frac 1 6 ( \vectau(s) \cdot \vecpsi^\prime(s) )
	( \veckappa(s) \cdot \vecphi^{\prime\prime}(s)
	- \vectau(s) \cdot \vecphi^\prime(s) \| \veckappa(s) \|_{\R^n}^2),
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrS_3(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	- \frac 1 6
	(\vectau(s) \cdot \vecpsi^\prime(s)) (\veckappa(s) \cdot \vecphi^{\prime\prime}(s))
	- \frac 1 6
	(\vectau(s) \cdot \vecphi^\prime(s)) (\veckappa(s) \cdot \vecpsi^{\prime\prime}(s)),
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrS_4(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	\frac 1 6 \vecphi^{\prime\prime}(s) \cdot \vecpsi^{\prime\prime}(s),
\\
	|\Delta s|^{\alpha-2}
	\frac{ \scrS_5(\vecf)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	&\to
	- \frac 1 6
	\{ (\vectau(s) \cdot \vecphi^{\prime\prime}(s)) + (\vecphi^\prime(s) \cdot \veckappa(s)) \}
	\{ (\vectau(s) \cdot \vecpsi^{\prime\prime}(s)) + (\vecpsi^\prime(s) \cdot \veckappa(s)) \}
\end{align*}
as
$(s_1,s_2) \to (s,s)$.
Hence,
the desired continuity holds when
$\vecf$,
$\vecphi$,
$\vecpsi \in C^2$.

This completes
the proof of Theorem \ref{mainthm}.
\hfill
$\square$
