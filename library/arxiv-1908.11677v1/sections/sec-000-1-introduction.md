---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.992
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposed to answer the question of what is the canonical shape in a given knot type"
---
In his papers \cite{O91,O92},
O'Hara proposed several energies for knots to determine the {\it canonical shape} of  a knot in a given knot class.
In order to describe these energies,
let
$\vecf : \R/\calL\Z \ni s \mapsto \vecf(s)$
be an arclength parametrization of a knot,
or more generally,
of a closed curve in
$\R^n$
without self-intersections.
For positive constants
$\alpha$
and
$p$,
the O'Hara
$(\alpha , p)$-energy is defined as
\[
	\calE_{(\alpha,p)}(\vecf)
	=
	\iint_{(\R/\calL\Z)^2}
	\scrM_{(\alpha,p)}(\vecf)(s_1,s_2) ds_1ds_2,
\]
where
\[
	\scrM_{(\alpha,p)}(\vecf)(s_1,s_2)
	=
	\left(
	\frac 1 { \| \vecf(s_1)-\vecf(s_2) \|_{\R^n}^\alpha } - \frac 1 { \scrD(\vecf(s_1) , \vecf(s_2))^\alpha }
	\right)^p .
\]
Here,
$\| \vecf(s_1)-\vecf(s_2) \|_{\R^n}$
and
$\scrD(\vecf(s_1),\vecf(s_2))$
are the extrinsic and the intrinsic distances between two points
$\vecf(s_1)$
and
$\vecf(s_2)$
on the curve,
respectively.

Amongst these energies,
the case
$p=1$
has been well-studied by many authors and here we describe several important contributions in this direction.
For example,
the first variational formula was derived in
\cite{FHW94,Rei12},
and the existence of a minimizer in a given knot class was studied in
\cite{FHW94,O94}.
In
\cite{ACFGH03},
it was shown that the right circle is the only global minimizer of the energy under length-constraint for appropriate
$\alpha$.
We also mention that there are several recent works concerning the gradient flow
\cite{B12-2,B18}
and the regularity of critical points
\cite{BRS16,BR13,BV19,FHW94,He00,Rei12}
of the
$(\alpha,1)$-energies.
The obvious difficulty in the analysis is that the energy density has a singularity on the diagonal set
$\{ (s,s) \,|\, s \in \R/\calL\Z \}$.
To avoid this,
the variational formulae were first derived using Cauchy's principal value \cite{FHW94,Rei12}.
The absolute integrability of the first and second variational formulae was shown by Ishizeki-Nagasawa \cite{IN15}
in the energy class.
They used the decomposition of the
$(2,1)$-energy
shown in
\cite{IN14},
which gives an expression of the energy density without using the intrinsic distance.
Furthermore, in
\cite{IN15},
they derived other estimates of variational formulae in several function spaces and a similar technique is applicable to other
$(\alpha,1)$-energies;
see \cite{INpre}.

By comparison,
the case
$p>1$
is rather less well studied.
Even the explicit expression of the first variational formula in the sense of Cauchy's principle value seems not to have been given.
In this paper,
the first and second variational formulae of
$(\alpha,p)$-energies will be given,
and several estimates will be shown:
absolute integrability,
uniform boundedness,
and continuity.
We,
however,
do not have a decomposition like the
$(\alpha,1)$
case,
and therefore the technique in \cite{IN15,INpre} cannot be used.
Instead,
we pay attention to the function
\[
	\scrN ( \vecu , \vecv ) =
	\frac 1 { 2 \| \vecf ( s_1 ) - \vecf ( s_2 ) \|_{ \R^n }^2 }
	\int_{ s_1 }^{ s_2 }
	\int_{ s_1 }^{ s_2 }
	( \vecu ( s_3 ) - \vecu ( s_4 ) )
	\cdot
	( \vecv ( s_3 ) - \vecv ( s_4 ) )
	ds_3 ds_4.
\]
By use of
$\scrN$,
the
$(\alpha,p)$-energy may be written as
\[
	\calE_{ ( \alpha , p ) } ( \vecf )
	=
	\iint_{ ( \R / \calL \Z )^2 }
	\left(
	\frac { \vphi_\alpha \left( \scrN ( \vecf^\prime , \vecf^\prime ) \right) }
	{ \| \vecf ( s_1 ) - \vecf ( s_2 ) \|_{ \R^n }^\alpha }
	\right)^p
	ds_1 ds_2,
\]
where
\[
	\vphi_\alpha (t)
	=
	1 - \frac 1 { ( 1 + t )^{ \frac \alpha 2 } }.
\]
Here,
we note that if
$ \calE_{ ( \alpha , p ) } ( \vecf ) < \infty $,
then
$ \vecf^\prime $
exists almost everywhere;
we refer the reader to
\cite{B12}
for this fact.
Since
$ \scrN ( \vecf^\prime , \vecf^\prime ) $
is non-negative,
and since
$ \vphi_\alpha $
is smooth for
$ t \geq 0 $,
the derivation and estimation of variational formulae mainly reduce to the study of
$ \scrN $.

We are now in a position to describe our main result of this article.
For the simplicity of notation,
we will use
$\Delta_j^i \vecu$
to mean
$\vecu(s_i)-\vecu(s_j)$
for a function
$\vecu : \R/\calL\Z \to \R^d$,
where
$d=1$
or
$n$,
and
$\Delta_j^i s$
to mean
$s_i-s_j$
for
$s_i$,
$s_j \in \R/\calL\Z$.
Furthermore,
we rewrite
$\Delta_2^1 \vecu$
and
$\scrD(\vecf(s_1),\vecf(s_2))$
as
$\Delta \vecu$
and
$\scrD(\vecf)$,
respectively.
Also,
we let
$\vectau = \vecf^\prime$
be the unit tangent vector.

For a geometric quantity
$\scrF(\vecf)$
of the closed curve
$\vecf$,
and for functions
$\vecphi$,
$\vecpsi$,
from
$\R/\calL\Z$
to
$\R^n$,
let
$\delta$
and
$\delta^2$
be given by
\begin{align*}
	\delta \scrF(\vecf) [\vecphi]
	&=
	\left. \frac d {d\epsi} \scrF(\vecf + \epsi\vecphi) \right|_{\epsi =0},
\\
	\delta^2 \scrF(\vecf) [\vecphi,\vecpsi]
	&=
	\left.
	\frac{\partial^2}{\partial\epsi_1 \partial\epsi_2} \scrF(\vecf + \epsi_1\vecphi + \epsi_2\vecpsi)
	\right|_{\epsi_1=\epsi_2=0}.
\end{align*}
The first and second variational formulae,
$\scrG_{(\alpha,p)}(\vecf)[\vecphi]$
and
$\scrH_{(\alpha,p)}(\vecf)[\vecphi,\vecpsi]$,
are given by
\begin{align*}
	\scrG_{(\alpha,p)}(\vecf)[\vecphi] \, ds_1 ds_2
	&=
	\delta ( \scrM_{(\alpha,p)}(\vecf) \, ds_1 ds_2 )[\vecphi],
\\
	\scrH_{(\alpha,p)}(\vecf)[\vecphi,\vecpsi]ds_1 ds_2
	&=
	\delta^2 ( \scrM_{(\alpha,p)}(\vecf) \, ds_1 ds_2 )[\vecphi,\vecpsi].
\end{align*}
The purpose of this article is to give certain new expressions and estimates for these variational formulae.
The expression will be given in \S~2.
In \S~3,
we prove the
$ L^1 $,
$ L^\infty $
and
$ C^0 $-estimates for them on the appropriate function spaces.
The first space is the \textit{Sobolev-Slobodeckij space}
$W^{k+\sigma,q}(\R/\calL\Z,\R^n)$
given by
\[
	W^{k+\sigma , q}(\R/\calL\Z,\R^n)
	=
	\{
	\vecf \in W^{k,q}(\R/\calL\Z,\R^n)
	\,|\,
	[\vecf^{(k)}]_{W^{\sigma,q}}
	< \infty
	\}
\]
for
$k \in \{ 0 \} \cup \N$,
$0<\sigma<1$,
and
$q \geq 1$.
We equip
$W^{k+\sigma,q}(\R/\calL\Z,\R^n)$
with the norm
\[
	\| \vecf \|_{W^{k+\sigma , q}}
	=
	\left(
	\| \vecf \|_{W^{k,q}}^q + [\vecf^{(k)}]_{W^{\sigma,q}}^q
	\right)^{\frac 1 q},
\]
where
\[
	[\vecf^{(k)}]_{W^{\sigma,q}}
	=
	\left(
	\iint_{(\R/\calL\Z)^2}
	\frac{ \| \Delta \vecf^{(k)} \|_{\R^n}^q }{ |\Delta s|^{1+\sigma q} }
	ds_1ds_2
	\right)^{\frac 1 q}.
\]
For
$\alpha \in (0,\infty)$,
$p \in [1,\infty)$
such that
$2 \leq \alpha p < 2p+1$,
and
$\sigma = (\alpha p-1)/(2p)$,
it was shown in
\cite{B12}
that
$\calE_{(\alpha,p)}(\vecf) < \infty$
if and only if
$\vecf$
belongs to
$W^{1+\sigma , 2p}(\R/\calL\Z , \R^n) \cap W^{1,\infty}(\R/\calL\Z,\R^n)$
and is bi-Lipschitz.
We will show the
$L^1$-estimate for the variational formulae on the same space.

By use of an appropriate weight,
the
$ L^\infty $-estimate holds on some H\"{o}lder or Lipschitz space
$ C^{k,\beta}(\R/\calL\Z,\R^n)$
with
$ k \in \mathbb{N} \cup \{ 0 \} $
and
$ \beta \in ( 0,1 ] $.
Here,
\[
	C^{k,\beta}(\R/\calL\Z,\R^n)
	=
	\{
	\vecf \in C^k(\R/\calL\Z,\R^n)
	\,|\,
	[\vecf^{(k)}]_{C^{0,\beta}}
	< \infty
	\}
\]
and this space is equipped with the norm
\[
	\| \vecf \|_{C^{k,\beta}}
	=
	\| \vecf \|_{C^k} + [\vecf^{(k)}]_{C^{0,\beta}},
\]
where
\[
	[\vecf^{(k)}]_{C^{0,\beta}}
	=
	\sup_{s_1,s_2 \in \R/\calL\Z}
	\frac{ \| \Delta \vecf^{(k)} \|_{\R^n} }{ |\Delta s|^\beta }.
\]
Note that we will see later that the weight is necessary.

The completion of
$ C^\infty (\R/\calL\Z,\R^n) $
in the H\"{o}lder space is known as the \textit{little H\"{o}lder space}
$h^{k,\beta}(\R/\calL\Z,\R^n)$
when
$ \beta < 1 $.
The completion of
$ C^\infty (\R/\calL\Z,\R^n) $
in
$ C^{k,1} (\R/\calL\Z,\R^n)$
is
$ C^{ k+1 } (\R/\calL\Z,\R^n) $.
We have the continuity of the energy density,
and the first and second variational formulae in the completion space.
The precise statement is as follows.
\begin{theorem}\label{mainthm}
Let
$\alpha \in (0,\infty)$,
$p \in [1,\infty)$
satisfy
$2 \leq \alpha p < 2p+1$,
and set
$\sigma = (\alpha p-1)/(2p)$.
Assume that
$\vecf$
is bi-Lipschitz,
i.e.,
there exists a positive constant
$C_{\mathrm{b}} >0$
such that
$\scrD(\vecf) \leq C_{\mathrm{b}} \| \Delta \vecf \|_{\R^n}$.
\begin{enumerate}\renewcommand{\labelenumi}{\upshape\textrm{\theenumi.}}
\item
If
$\vecf$,
$\vecphi$,
$\vecpsi \in W^{1+\sigma , 2p}(\R/\calL\Z , \R^n) \cap W^{1,\infty}(\R/\calL\Z , \R^n)$,
then
$\scrM_{(\alpha,p)} (\vecf)$,
$\scrG_{(\alpha,p)} (\vecf)[\vecphi]$,
$\scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi] \in L^1((\R/\calL\Z)^2)$.
Moreover,
there exists a positive constant
$C$
depending on
$\| \vectau \|_{W^{\sigma , 2p} \cap L^\infty}$,
$C_{\mathrm{b}}$,
$\alpha$,
and
$p$
such that
\begin{align*}
	\| \scrM_{(\alpha,p)} (\vecf) \|_{L^1((\R/\calL\Z)^2)} &\leq C,
\\
	\| \scrG_{(\alpha,p)} (\vecf)[\vecphi] \|_{L^1((\R/\calL\Z)^2)}
	&\leq C \| \vecphi^\prime \|_{W^{\sigma , 2p} \cap L^\infty},
\\
	\| \scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi] \|_{L^1((\R/\calL\Z)^2)}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma , 2p} \cap L^\infty}
	\| \vecpsi^\prime \|_{W^{\sigma , 2p} \cap L^\infty}.
\end{align*}
\item
Let
$\beta \in (0,1]$.
If
$\vecf$,
$\vecphi$,
$\vecpsi \in C^{1,\beta}(\R/\calL\Z , \R^n)$,
then
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrM_{(\alpha,p)} (\vecf)$,
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrG_{(\alpha,p)} (\vecf)[\vecphi]$,
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi] \in L^\infty((\R/\calL\Z)^2)$.
Moreover,
there exists a positive constant
$C$
depending on
$\| \vectau \|_{C^{0,\beta}}$,
$C_{\mathrm{b}}$,
$\alpha$,
and
$p$
such that
\begin{align*}
	\| \scrD(\vecf)^{(\alpha-2\beta)p} \scrM_{(\alpha,p)} (\vecf) \|_{L^\infty((\R/\calL\Z)^2)}
	&\leq C,
\\
	\| \scrD(\vecf)^{(\alpha-2\beta)p} \scrG_{(\alpha,p)} (\vecf)[\vecphi] \|_{L^\infty((\R/\calL\Z)^2)}
	&\leq C \| \vecphi^\prime \|_{C^{0,\beta}},
\\
	\| \scrD(\vecf)^{(\alpha-2\beta)p}
	\scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi] \|_{L^\infty((\R/\calL\Z)^2)}
	&\leq
	C \| \vecphi^\prime \|_{C^{0,\beta}} \| \vecpsi^\prime \|_{C^{0,\beta}}.
\end{align*}
\item
For
$\beta \in (0,1]$,
let
\[
	X^\beta(\R/\calL\Z,\R^n) = \left\{
	\begin{array}{ll}
		h^{0,\beta}(\R/\calL\Z , \R^n) & \mbox{for}\ 0<\beta<1,
	\vspace{3pt}\\
		C^1(\R/\calL\Z , \R^n) & \mbox{for}\ \beta =1.
	\end{array}
	\right.
\]
If
$\vectau$,
$\vecphi^\prime$,
$\vecpsi^\prime \in X^\beta(\R/\calL\Z , \R^n)$,
then
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrM_{(\alpha,p)} (\vecf)$,
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrG_{(\alpha,p)} (\vecf)[\vecphi]$,
$\scrD(\vecf)^{(\alpha-2\beta)p} \scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi]$
can be extended to the diagonal set
$\{ (s,s) \,|\, s \in \R/\calL\Z \}$
such that these functions are continuous everywhere on
$(\R/\calL\Z)^2$,
and they satisfy the estimates
\begin{align*}
	\| \scrD(\vecf)^{(\alpha-2\beta)p} \scrM_{(\alpha,p)} (\vecf) \|_{C^0((\R/\calL\Z)^2)}
	&\leq
	C,
\\
	\| \scrD(\vecf)^{(\alpha-2\beta)p} \scrG_{(\alpha,p)} (\vecf)[\vecphi] \|_{C^0((\R/\calL\Z)^2)}
	&\leq
	C \| \vecphi^\prime \|_{X^\beta},
\\
	\| \scrD(\vecf)^{(\alpha-2\beta)p} \scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi] \|_{C^0((\R/\calL\Z)^2)}
	&\leq
	C \| \vecphi^\prime \|_{X^\beta} \| \vecpsi^\prime \|_{X^\beta}
\end{align*}
for some positive constant
$C$
depending on
$\| \vectau \|_{X^\beta}$,
$C_{\mathrm{b}}$,
$\alpha$,
and
$p$.
The limit functions
\begin{gather*}
	\lim_{(s_1,s_2) \to (s,s)}
	\scrD(\vecf)^{(\alpha-2\beta)p} \scrM_{(\alpha,p)} (\vecf),
\\
	\lim_{(s_1,s_2) \to (s,s)}
	\scrD(\vecf)^{(\alpha-2\beta)p} \scrG_{(\alpha,p)} (\vecf)[\vecphi],
\\
	\lim_{(s_1,s_2) \to (s,s)}
	\scrD(\vecf)^{(\alpha-2\beta)p} \scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi]
\end{gather*}
exist and are finite.
These vanish everywhere on
$\R/\calL\Z$
when
$\beta \in (0,1)$.
\end{enumerate}
\end{theorem}

The second assertion gives us the
$L^\infty$-estimates for
$\scrM_{(\alpha,p)}$,
$\scrG_{(\alpha,p)}$,
and
$\scrH_{(\alpha,p)}$ without the weight,
when
$\alpha \leq 2$.

\begin{corollary}\label{mainthm coro}
Let
$\alpha \in (0,\infty)$,
$p \in [1,\infty)$
satisfy
$2/p \leq \alpha \leq 2$.
If
$\vecf$,
$\vecphi$,
$\vecpsi \in C^{1,\frac \alpha 2}(\R/\calL\Z , \R^n)$
and
$\vecf$
is bi-Lipschitz,
then
$\scrM_{(\alpha,p)} (\vecf)$,
$\scrG_{(\alpha,p)} (\vecf)[\vecphi]$,
and
$\scrH_{(\alpha,p)} (\vecf)[\vecphi,\vecpsi]$
belong to
$L^\infty((\R/\calL\Z)^2)$.
\end{corollary}

The corresponding estimates to our main result were shown for the spacial case
$ \calE_{ (2,1) } $
in
\cite{IN15},
and in this sense our result is an extension to a wider class of O'Hara's energies.
\begin{remark}
When
$\alpha >2$,
we need the weight
$ \scrD ( \vecf )^{ ( \alpha - 2 \beta ) p } $
to obtain the uniform boundedness even if
$ \vecf $
is analytic.
For example,
let us consider the right circle with the total length
$ 2 \pi $,
i.e.,
\[
	\vecf(s) = (\cos s , \sin s , 0, \ldots ,0)
	\quad
	\mbox{for}\ s \in \R/2\pi\Z.
\]
Since
$\| \Delta \vecf \|_{\R^n}^2 = 2(1-\cos \Delta s)$,
it follows that
\begin{equation}\label{eq remark}
	\scrM_{(\alpha,p)}(\vecf)
	=
	\frac 1 { \| \Delta \vecf \|_{\R^n}^{\alpha p} }
	\left[
	1-
	\left\{
	\frac{ 2(1-\cos\Delta s) }{ (\Delta s)^2 }
	\right\}^{\frac \alpha 2}
	\right]^p.
\end{equation}
Using Taylor's theorem
\[
	2(1-\cos x)
	=
	x^2 - \frac 1 {12} x^4 + \calO(x^6)
	\quad
	\text{as}\ x \to 0,
\]
and thus we have
\[
	1-
	\left\{
	\frac{ 2(1-\cos\Delta s) }{ (\Delta s)^2 }
	\right\}^{\frac \alpha 2}
	=
	\frac \alpha {24} (\Delta s)^2
	+
	\calO((\Delta s)^4)
	\quad
	\text{as}\ \Delta s \to 0.
\]
Hence,
the right-hand side of
\eqref{eq remark}
is equal to
\[
	\left(
	\frac{ |\Delta s| }{ \| \Delta \vecf \|_{\R^n} }
	\right)^{\alpha p}
	\left(
	\frac \alpha {24} |\Delta s|^{2-\alpha}
	+
	\calO(|\Delta s|^{4-\alpha})
	\right)^p
	\quad
	\text{as}\ \Delta s \to 0.
\]
Therefore,
when
$\alpha >2$,
$ \scrD ( \vecf )^\gamma \scrM_{(\alpha,p)}(\vecf) $
is uniformly bounded if and only if
$ \gamma \geq ( \alpha - 2 ) p $.
\end{remark}

\paragraph*{Acknowledgments}
The authors would like to thank Professor Richard Neal Bez for English language editing and mathematical comments.

The second author is supported by Grant-in-Aid for Scientific Research (C) (No.17K05310),
Japan Society for the Promotion of Science.
