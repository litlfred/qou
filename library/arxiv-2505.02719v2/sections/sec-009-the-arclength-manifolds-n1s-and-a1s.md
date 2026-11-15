---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-009-the-arclength-manifolds-n1s-and-a1s
section_title: "The arclength manifolds N1+s and A1+s"
section_number: null
pages: 17-20
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.99
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:AL}

To identify the subset 
\begin{equation}\label{eq:arclenth-set}
H^{1+s}_\unitspeed(\R/\Z,\R^n)=\{\g\in H^{1+s}(\R/\Z,\R^n):|\g'|=1\,
\textnormal{
on $\R/\Z$}\}
\end{equation}
of arclength parametrized curves as a submanifold of the open set
$H^{1+s}_\reg(\R/\Z,\R^n)$ we follow the idea of 
\cite[Section 2]{scholtes-etal_2022} and
\cite{knappmann-etal_2023} and introduce
the scalar-valued \emph{logarithmic strain}
$\varSigma:H^{1+s}_\reg(\R/\Z,\R^n)\to H^s(\R/\Z)$ defined as
\begin{equation}\label{eq:logarithmic-strain}
	\varSigma(\g) \ceq \log\big( |\g'|\big)  \in H^s(\R/\Z) \quad\Fo \g\in H^{1+s}_\reg(\R/\Z,\R^n),
\end{equation}
which is a smooth function on the set $H^{1+s}_\reg(\R/\Z,\R^n)$ of
regular curves. It follows from \cite[Proposition 5.1]{knappmann-etal_2023}
for $s\in (\frac{1}{2},1)$
that the differential $\D\varSigma_\g:T_\g H^{1+s}_\reg(\R/\Z,\R^n)
\simeq H^{1+s}(\R/\Z,\R^n)\to T_{\varSigma(\g)}H^s(\R/\Z,\R^n)\simeq
H^s(\R/\Z,\R^n)$ has the form
\begin{equation}\label{eq:log-strain-differential}
	\D\varSigma_\g h=\langle\g',h'\rangle \quad\Fo
	\g\in H^{1+s}_\unitspeed(\R/\Z,\R^n),\, h\in H^{1+s}(\R/\Z,\R^n),
\end{equation}
and is bounded, i.e. has operator norm
\begin{equation}\label{eq:log-strain-bounded-differential}
\|\D\varSigma_\g\|_{\LL(H^{1+s},H^s)}\le C_\varSigma,
\end{equation}
where the constant  $C_\varSigma=C_\varSigma(n,s,\|\g'\|_{H^s})$
depends 
non-decreasingly on the norm $\|\g'\|_{H^s}$
of the unit tangent $\g'$. In view of the explicit
formula \cref{eq:log-strain-differential}
for $\D\varSigma_\g$ it can easily be checked that
the same holds true for $s=1$.
Moreover, \cite[Lemma 5.2]{knappmann-etal_2023}
yields for $s\in (\frac{1}{2},1)$
the existence of a bounded right inverse $Y_\g\in
\LL(H^s(\R/\Z),H^{1+s}(\R/\Z,\R^n))$ of the differential $\D\varSigma_\g$ 
satisfying
$\D\varSigma_\g(Y_\g(f))=f$ for all $f\in H^s(\R/\Z)$,
so that $\D\varSigma_\g$ is surjective for any
$\g\in H^{1+s}_\unitspeed(\R/\Z,\R^n)$. Again, as before, 
the same formula\footnote{Explicitly given in \cref{eq:right-inverse-Y}
in our proof
of \cref{prop:projection-ALs} below.}
for $Y_\g$ given in the proof of \cite[Lemma 5.2]{knappmann-etal_2023}
yields a right inverse of $\D\varSigma_\g$
also in the case $s=1$.
Therefore, we can apply the
preimage theorem\footnote{Notice that the nullspace $\ker(\D\varSigma_\g)$
splits $H^{1+s}(\R/\Z,\R^n)$ because the latter is a Hilbert space.}
(see, e.g., \cite[Theorem 4.J]{zeidler_1993}) 
to
\begin{equation}
\begin{aligned}
	\label{eq:arclength-manifold}
&\NL^{1+s}\ceq H^{1+s}_\unitspeed(\R/\Z,\R^n)=\big(\varSigma|_{H^{1+s}_\reg(\R/\Z,\R^n)}
\big)^{-1}(0),\hspace{5pt}\text{ and }\\
&\AL^{1+s} \ceq H^{1+s}_\injunitspeed(\R/\Z,\R^n)=\big(\varSigma|_{H^{1+s}_\injreg(\R/\Z,\R^n)}\big)^{-1}(0)=\NL^{1+s}\cap H^{1+s}_\inj\left( \R/\Z,\R^n \right).
\end{aligned}
\end{equation}

\begin{theorem}[Arclength manifolds]
\label{thm:arclength-manifold}
Let $s\in (\frac{1}{2},1]$.
The sets $\NL^{1+s}$ of arclength para\-met\-rized curves, and $\AL^{1+s}$ of arclength para\-met\-rized knots are smooth submanifolds
of the open subsets $H^{1+s}_\reg(\R/\Z,\R^n)$ and $ H^{1+s}_\injreg(\R/\Z,\R^n) $, respectively. 
\end{theorem}
To secure compactness of (PS)-sequences  later,
we can fix an arbitrary 
point $\bz\in\R^n$ and
consider the subsets
\begin{equation}\label{eq:arclenth-point}
\NL^{1+s}_\bz\ceq\{\g\in\NL^{1+s}:\g(0)=\bz\},\, \text{ and }\,\AL^{1+s}_\bz\ceq\{\g\in\AL^{1+s}:\g(0)=\bz\}.
\end{equation}
The corresponding ambient space $H^{1+s}_\bz(\R/\Z,\R^n)\ceq\{\g\in
H^{1+s}(\R/\Z,\R^n):\g(0)=\bz\}$ is an affine subspace
and therefore also a smooth submanifold of $H^{1+s}(\R/\Z,\R^n)$, but in order
to come up with a suitable projection later, we express $\NL^{1+s}_\bz$ as
preimage of $(0,\bz)\in H^s(\R/\Z)\times\R^n$, i.e., 
\begin{align*}\label{eq:NL_z-preimage}
	\NL^{1+s}_\bz=\big(
\varSigma|_{H^{1+s}_\reg(\R/\Z,\R^n)}\times P_0\big)^{-1}(0,\bz),
\end{align*}
where the point evaluation $P_0:H^{1+s}_\reg(\R/\Z,\R^n)\to\R^n$ is 
defined by
\begin{equation}\label{eq:point-evaluation}
P_0(\g)\ceq\g(0).
\end{equation}
This linear map is a smooth submersion at every $\g\in H^{1+s}_\reg(\R/\Z,\R^n)$
with differential $\D(P_0)_\g:T_\g H^{1+s}_\reg(\R/\Z,\R^n)\simeq
H^{1+s}(\R/\Z,\R^n)\to T_{P_0(\g)}\R ^n\simeq \R^n$  given by
\begin{equation}\label{eq:P0-differential}
\D(P_0)_\g h=P_0 h=h(0)\quad\Foa h\in H^{1+s}(\R/\Z,\R^n).
\end{equation}
The differential of the product map $\varSigma\times P_0:
H^{1+s}_\reg(\R/\Z,\R^n)\to H^s(\R/\Z)\times\R^n$ is
$$
\D(\varSigma,P_0)_\g=(\D\varSigma_\g,\D(P_0)_\g)
\overset{\cref{eq:P0-differential}}{=}(\D\varSigma_\g,P_0),
$$
 and it possesses as bounded right
inverse the map $Z_\g:H^s(\R/\Z)\times\R^n\to H^{1+s}(\R/\Z,\R^n)$
defined via the right inverse $Y_\g$ of $\D\varSigma_\g$ (see the arguments that lead to
\cref{thm:arclength-manifold}) as
\begin{align*}
	Z_\g(f,\by) \ceq Y_\g(f)+\by-Y_\g(f)(0)\quad\Fo (f,\by)\in
H^s(\R/\Z)\times\R^n.
\end{align*}
Indeed, one computes with the help of \cref{eq:P0-differential}, 
\cref{eq:point-evaluation} and
\cref{eq:log-strain-differential}
\begin{align*}
	\D(\varSigma,P_0)_\g & \big(Z_\g(f,\by)\big)
	\overset{\cref{eq:P0-differential}}{=}
	\big(\D\varSigma_\g
	\big(Y_\g(f)+\by-Y_\g(f)(0)\big),P_0\big(Y_\g(f)+\by-
	Y_\g(f)(0)\big)\big)\\
	&\overset{\cref{eq:log-strain-differential},\cref{eq:point-evaluation}}{=}
	\big(\D\varSigma_\g(Y_\g(f)),\by\big)=(f,\by)\quad\Foa (f,\by)
	\in H^s(\R/\Z)\times\R^n.
\end{align*}
We have thus shown that the differential $\D(\varSigma,P_0)_\g$ is surjective
for any curve $\g\in H^{1+s}_\reg(\R/\Z,\R^n)$, so that we may apply the
preimage theorem as in the proof of \cref{thm:arclength-manifold}.
Including injectivity, we get 
\begin{equation}\label{eq:AL_z-preimage}
	\AL^{1+s}_\bz=\big(
	\varSigma|_{H^{1+s}_\injreg(\R/\Z,\R^n)}\times P_0\big)^{-1}(0,\bz)=\NL^{1+s}_{\bz}\cap H^{1+s}_{\inj}.
\end{equation}

\begin{theorem}[Arclength manifolds with fixed initial point]
\label{thm:arclength-manifold-point}
Let $s\in (\frac{1}{2},1]$ and $\bz\in\R^n$, then the sets $\NL^{1+s}_\bz$ and 
$\AL^{1+s}_\bz$
of arclength parametrized curves and knots $\g$ with fixed initial point $\g(0)=\bz$ are
smooth submanifolds of the open subsets $H^{1+s}_\reg(\R/\Z,\R^n)$ and $ H^{1+s}_{\injreg}(\R/\Z,\R^n) $, respectively. 
\end{theorem}

The tangent space of the arclength manifold $\NL^{1+s}$ at a curve $\g\in
\NL^{1+s}$
is given by
\begin{equation}\label{eq:tangent-space-AL}
	T_\g\NL^{1+s} 
	=
	\ker (\D\varSigma_\g)
	=
	\braces[\big]{ 
		h\in H^{1+s}(\R/\Z,\R^n) : \inner{\g',h'}=0
	},
\end{equation}
whereas for $\NL_\bz^{1+s}$ we have
\begin{equation}\label{eq:tangent-space-ALz}
	T_\g\NL^{1+s}_\bz 
	=
	\ker(\D(\varSigma,P_0)_\g)
	=
	\braces[\big]{ 
		h\in H^{1+s}(\R/\Z,\R^n) : \inner{\g',h'}=0,\,h(0)=0
	}.
\end{equation}
Analogously, one finds $ T_{\g}\AL^{1+s}=T_\g\NL^{1+s} $ for $ \gamma\in \AL^{1+s} $ and $ T_\g\AL^{1+s}_{\bz}=T_\g\NL^{1+s}_{\bz} $ if $ \gamma\in\AL^{1+s}_{\bz} $. 
\begin{proposition}[Bounded linear projection onto the tangent space]
\label{prop:projection-ALs}
Let $s\in (\frac{1}{2},1]$, $ \ML\in \left\{\AL^{1+s},\NL^{1+s}\right\}$, and $\g\in\ML$. Then the mapping
$\pr_\g^{\ML}:H^{1+s}(\R/\Z,\R^n)\to H^{1+s}(\R/\Z,\R^n)$ given by
\begin{equation}\label{eq:projection-ALs}
\pr_\g^{\ML}h\ceq(\Id-Y_\g \D\varSigma_\g)h
\end{equation}
is a linear and bounded projection onto the tangent space $T_\g\ML$
of $\ML$ at $\g$.
\end{proposition}
\begin{proof}
We need the explicit formula for 
the right inverse $Y_\g$ of $\D\varSigma_\g$
as provided in \cite[Lemma 5.2]{knappmann-etal_2023}:
\begin{equation}\label{eq:right-inverse-Y}
	\textstyle
	Y_\g f(t)
	=
	\int_0^t \big( f(u) \, \g'(u) + \P_{\g'(u)}^\perp V_{\gamma}f\big) \d u,
	\;\;
	\text{with}
	\;\;
	V_{\gamma}f=-\varTheta_\g^{-1}\int_0^1 f(u) \, \g'(u)\d u\in\R^n
	,
\end{equation}
where $\varTheta_\g:\R^n\to\R^n$ is 
the bounded invertible linear operator
given by
$\varTheta_\g\ceq\int_0^1\P_{\g'(u)}^\perp \d u$. Note that $ \varTheta_{\gamma}^{-1} $ is indeed bounded because of \cite[Lemma 5.3]{knappmann-etal_2023}, since $ \gamma'\in C^{0,s-\frac{1}{2}}\left( \R/\Z,\R^n \right) $ by Morrey's embedding. 
The vector $V_{\gamma}f$ guarantees that $Y_\g(f)$ is $1$-periodic. 
It depends linearly  on $f$ and satisfies the estimate
\begin{equation}\label{eq:V-h-est}
 |V_{\gamma}f|\le C\|f\|_{C^0}\le C_EC\|f\|_{H^s}\quad\Foa f\in H^s(\R/\Z),
\end{equation}
where the constant $C=C(s,\|\g'\|_{H^s})$ depends non-de\-creas\-ingly on
the norm $\|\g'\|_{H^s}$ and $C_E=C_E(s)$ is the embedding constant from
the compact Morrey embedding $H^s(\R/\Z)\hookrightarrow
 C^0(\R/\Z)$, which is standard for $s=1$; for
 $s\in (\frac{1}{2},1)$ 
 see, e.g., \cite[Theorem A.2]{knappmann-etal_2023}. 
So, we compute
\begin{equation}\label{eq:derivative-right-inverse}
	\pars{Y_\g \, f}'(t) = f(t) \, \g'(t)+\P_{\g'(t)}^\perp V_{\gamma}f;
\end{equation}
$
	\inner{ \pars{Y_\g f}'(t),\g'(t) }=f(t)$ for all $t\in\R/\Z$ and 
$f\in H^s(\R/\Z),
$
and therefore, by \cref{eq:log-strain-differential}
\begin{align}
	\inner{ (\pr_\g^{\ML}h)'(t),\g'(t) }&
	\overset{\cref{eq:log-strain-differential}}{=}
	\inner[\big]{ 
		h'(t) - \pars[\big]{Y_\g \inner{\g', h'}}'(t)
		,
		\g'(t)
	}=0\label{eq:tangent-orthogonal}
\end{align}
for all $h\in H^{1+s}(\R/\Z,\R^n).$
This 
shows that $\pr_\g^{\ML}h\in T_\g\ML$ for all $h\in H^{1+s}(\R/\Z,\R^n).$
Obviously, $\pr_\g^{\ML}$ is linear, so that it is a projection as desired if
we can show that its restriction to $T_\g\ML$ equals the identity (see, e.g., \cite[9.13(1)]{alt_2016}). But linearity of $f\mapsto Y_\g f$ 
indeed yields for $h\in
T_\g\ML$  by means of \cref{eq:tangent-space-AL}
\begin{equation}\label{eq:proj-id}
	\pr_\g^{\ML}h
	=
	h-Y_\g \inner{ \g',h'} 
	\overset{\cref{eq:tangent-space-AL}}{=}h-Y_\g(0)
	=
	h.
\end{equation}
Combining the explicit formulas \cref{eq:right-inverse-Y}
and \cref{eq:derivative-right-inverse} with the estimates
\cref{eq:V-h-est}, \cref{eq:log-strain-bounded-differential} 
and the product rule 
(see, e.g., \cite[Proposition A.5]{knappmann-etal_2023}),     we obtain
\begin{equation}\label{eq:projection-bound}
\|\pr_\g^{\ML}h\|_{H^{1+s}}\le (1+\tilde C C_\varSigma)\|h\|_{H^{1+s}}=:C_\g\|h\|_{H^{1+s}}\quad\Foa 
h\in H^{1+s}(\R/\Z,\R^n),
\end{equation}
where the constant $\tilde C=\tilde C(n,s,\|\g\|_{H^{1+s}})$ and therefore also $C_\g$
depends non-de\-creas\-ingly on
the norm $\|\g\|_{H^{1+s}}.$
\end{proof}
\begin{corollary}[Bounded linear projection onto $T_\g\NL^{1+s}_\bz$]
\label{cor:projection-ALsz}
For $s\in (\frac{1}{2},1]$, $\bz\in\R^n$, $ \ML\in \left\{\NL^{1+s},\AL^{1+s}\right\} $, and $\g\in\ML_\bz\ceq\{\eta\in \ML: \eta(0)=\bz\}$, the
mapping $\pr_\g^{\ML_\bz}:H^{1+s}(\R/\Z,\R^n)\to 
H^{1+s}(\R/\Z,\R^n)$
defined by
\begin{equation}\label{eq:projection-ALsz}
\pr_\g^{\ML_\bz}h\ceq\pr_\g^{\ML}h-
\pr_\g^{\ML}h(0)
\end{equation}
is a linear and bounded projection onto the tangent space
$T_\g\ML_\bz$ of $\ML_\bz$ at $\g$. 
Here, $\pr_\g^{\ML}$ is the projection provided by \cref{prop:projection-ALs}.
\end{corollary}
\begin{proof}
Notice that the
linearity and boundedness of $\pr_\g^{\ML}$ 
transfers to $\pr_\g^{\ML_\bz}$, and with 
$(\pr_\g^{\ML_\bz}h)'
=
(\pr_\g^{\ML}h)'$ and $\pr_\g^{\ML_\bz}h(0)=0$ we find
by \cref{eq:tangent-orthogonal} and
\cref{eq:tangent-space-ALz} that $\pr_\g^{\ML_\bz}h
\in T_\g\ML_\bz$. Finally, for $h\in T_\g\ML_\bz
\subset T_\g\ML$ we have $h(0)=0$ and therefore, due to \cref{eq:proj-id}, 
\begin{align*}
	\pr_\g^{\ML_\bz}h=
	\pr_\g^{\ML}h\overset{\cref{eq:proj-id}}{=}h.
\end{align*}
\end{proof}

Now \cref{thm:arclength-manifold,thm:arclength-manifold-point},
\cref{prop:projection-ALs}, and \cref{cor:projection-ALsz} 
together with the estimate \cref{eq:projection-bound}
verify the basic abstract conditions
\ref{condE} and \ref{condP} for the arclength manifolds $\AL^{1+s}$ 
and
$\AL^{1+s}_\bz$.
\begin{corollary}[\ref{condE} and \ref{condP} for arclength manifolds]
\label{cor:basic-assumptions}
Let $s\in (\frac{1}{2},1]$ and $\bz\in\R^n$ be fixed. Then condition \ref{condE}
holds true for $\ML\in \left\{\AL^{1+s},\AL_{\bz}^{1+s},\NL^{1+s},\NL_{\bz}^{1+s}\right\}$, if we choose 
$\OL \ceq H^{1+s}_\reg(\R/\Z,\R^n)$, or $ \OL\ceq H^{1+s}_\injreg(\R/\Z,\R^n)$ respectively, as an open subset of the Hilbert space
$\HL \ceq H^{1+s}(\R/\Z,\R^n)$, which embeds compactly into
the Banach space $\BL \ceq C^1(\R/\Z,\R^n)$. 
Moreover, the linear projections $\pr_\g^{\ML}:
T_\g\OL\to T_\g\ML$ for $\g\in\ML$ have property \ref{condP}.
\end{corollary}

\begin{remark}[Explicit Lagrange multiplier]\label{rem:explicit-lagrange-multiplier}
	The concrete formulas for the right inverse $ Y_{\gamma} $ in \cref{eq:right-inverse-Y} and for the projection $ \pr^{\ML}_{\gamma} $ in \cref{eq:projection-ALs} for $ \ML\in \{\AL^{1+s},\NL^{1+s}\} $ allow us to derive an explicit expression for the Lagrange multiplier arising from the arclength constraint. This turns out to be extremely useful in the regularity theory in \cref{sec:Smoothness}. 

	Suppose $ \gamma\in \ML $ is critical for the restricted energy $ \widetilde{\EL}\ceq\EL\vert_{\ML} $, where $ \EL \in C^1(\OL)$ for an open subset of the Hilbert space $ \HL=H^{1+s}\left( \R/\Z,\R^n \right) $ with $ \ML\subset\OL $. Then $ \D \EL_{\gamma}h=\D \widetilde{\EL}_{\gamma}h =0$ for all $h\in \T_{\gamma}\ML $, which is equivalent to 
	\begin{equation}\label{eq:Lagra_Mult}
	\begin{aligned}
		0=\D\EL_{\gamma} \pr^{\ML}_{\gamma}\overset{\cref{eq:projection-ALs}}{=} \D\EL_{\gamma}\left( \Id_{\HL}-Y_{\gamma}\D\Sigma_{\gamma} \right).
	\end{aligned}
	\end{equation}
	By the Lagrange multiplier theorem, see \cite[Corollary 3.5.29]{abraham-etal_1988}, there exists $ \Lambda\in \left( H^{s}(\R/\Z) \right)^* $ such that $ \D\EL_{\gamma}-\Lambda\D\Sigma_{\gamma}=0 $. This in combination with \cref{eq:Lagra_Mult} yields the formula 
	\[\Lambda=\D\EL_{\gamma}Y_{\gamma}.\]
\end{remark}
