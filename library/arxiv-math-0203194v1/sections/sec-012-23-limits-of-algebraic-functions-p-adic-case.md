---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-012-23-limits-of-algebraic-functions-p-adic-case
section_title: "Limits of algebraic functions; $p$-adic case."
section_number: 2.3
pages: 27-33
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.984
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{subsection-remedy}
\begin{para}
 In the $p$-adic situation, we have seen that there are ``much more''
 \'etale coverings than topological coverings. For instance, the unit disk
 $\matheur{D}=\matheur{D}(0,1^+)$ is simply-connected, but admits many
 non-trivial finite \'etale coverings, \eg the Artin-Schreier covering
 $\matheur{D}\rightarrow \matheur{D}, \;y\mapsto z=y^p-y$.
 
\propref{pro-gabber} suggests to replace, in the $p$-adic case, the ring 
 $\mathcal{O}(\til{S})$, which is often too
 small, by some kind of completion of $\mathcal{O}(S)^{\mathrm{et}}= \varinjlim
 \mathcal{O}(S'),$ where $S'$ runs over the finite \'etale
 connected coverings of $S$.
 
 Let us now assume that $S$ is an affinoid curve with good 
 reduction (hence simply connected). Then there is a
 Gauss $p$-adic norm on $\mathcal{O}(S)$, which extends uniquely to 
 $\mathcal{O}(S)^{\mathrm{et}}$.
 The completion $\widehat{\mathcal{O}(S)^{\mathrm{et}}}$ is
 however pathological in several senses: for instance, 
 it is difficult to give a function-theoretic 
 meaning to its elements, and the continuous derivations of
 $\mathcal{O}(S)$ extends to $\mathcal{O}(S)^{\mathrm{et}}$ but not to
 $\widehat{\mathcal{O}(S)^{\mathrm{et}}}$ in a natural way.
\end{para}

\begin{para}\label{para:r}
 To bypass such problems, we are going to look for some convenient {\it subring} of
 $\widehat{\OO(S)^{\mathrm{et}}}$.
 For simplicity, let us limit ourselves to the following situation:
 \begin{itemize}
  \item $K = {\widehat{\Q}}^{\mathrm{ur}}_p \subset \C_p$
	is the completion of
	the maximal unramified algebraic extension of ${\Q}_p$,
  \item $\mathfrak{v} = {\widehat{\Z}}^{\mathrm{ur}}_p$ is its ring of
	integers (the Witt ring of ${\ovl{\F}}_p$),
  \item $S_0$ is the affine line over ${\ovl{\F}}_p$, deprived from
	finitely many points ${\ovl{\zeta}}_1\ldots,{\ovl{\zeta}}_{\nu}$;
	we choose a point $s_0$ on $S_0$,
  \item $\mathcal{R}$ is the $p$-adic completion of
	$\mathfrak{v}[z, \frac{1}{(z-\zeta_1)\ldots (z-\zeta_{\nu})}]$,
	where $\zeta_1\ldots \zeta_{\nu}$ are liftings of
	${\ovl{\zeta}}_1\ldots,{\ovl{\zeta}}_{\nu}$ in $\mathfrak{v}$; its
	residue ring is $\mathcal{O}(S_0)$,
  \item $S = \matheur{M}\bigl(\mathcal{R}[\frac{1}{p}]\bigr) =
	\matheur{D}(0,1^+) \setminus \bigcup 
	\matheur{D}(\zeta_i,1^-)$, the associated affinoid domain over $K$.
	There is a natural specialization map $\sp: S \rightarrow S_0$ from
	characteristic $0$ to characteristic $p$.
 \end{itemize}

 Let us consider the integral closure ${\mathcal{R}^{\mathrm{et}}}$ of
 $\mathcal{R}$ in ${\mathcal{O}(S)^{\mathrm{et}}}$ and its $p$-adic
 completion $\widehat{\mathcal{R}^{\mathrm{et}}} \subset
 \widehat{\OO(S)^{\mathrm{et}}}$.
 It is thus endowed with (a natural extension of) the $p$-adic
 valuation, and its residue ring is
 $\mathcal{O}(S_0)^{\mathrm{et}}$. Moreover, there is a natural
 structure of ``differential ring'' (better: a connection) on
 $\widehat{\mathcal{R}^{\mathrm{et}}}$ with $\mathfrak{v}$ as ring of
 constants. The ``remarkable equivalence of categories'' of
 A. Grothendieck \cite[18.1.2]{ega44} allows to identify
 $\Aut_{\mathrm{cont}}(\widehat{\mathcal{R}^{\mathrm{et}}}/\mathcal{R})$
 with the algebraic fundamental group $\pi_1^{\mathrm{alg}}(S_0,s_0)$.
\end{para}

\begin{para}\label{para-analytic-cont}
 {\itshape ``Analytic continuation'' as specialization.\ } Let
 $\matheur{D}(s_0,1^-) = \sp^{-1}\lbrace s_0\rbrace$ be the residue
 class of $s_0$ in $S$.  The morphism $\mathcal{R}\rightarrow
 \mathcal{O}(\matheur{D}(s_0,1^-))$ extends non-canonically to a
 continuous morphism $\widehat{\mathcal{R}^{\mathrm{et}}}
 [\frac{1}{p}]\rightarrow \mathcal{O}(\matheur{D}(s_0,1^-))$, determined
 \emph{only up to the action of } $\pi_1^{\mathrm{alg}}(S_0,s_0)$. This
 allows to interpret elements of
 $\widehat{\mathcal{R}^{\mathrm{et}}}[\frac{1}{p}]$ as certain
 multivalued locally analytic functions (in the ``wobbly'' sense). 

The main difference here with Krasner's analytic continuation
 (\cf~\subsecref{subsec-limit-rational}) is the ambiguity coming from
 $\pi_1^{\mathrm{alg}}(S_0,s_0)$.  This provides a kind of multivalued
 analytic continuation, which may be interpreted as analytic
 continuation in characteristic $0$ along an ``\'etale path'' in
 characteristic $p$ (figure \ref{pic4}). 
 
\begin{center}
 \begin{figure}[h]
  \begin{picture}(200,100)(0,0)
   \put(0,100){\makebox(0,0)[l]{$\matheur{D}(s_0,1^{-})$}}
   \put(0,0){\includegraphics{fig4.eps}}
   \put(15,5){\makebox(0,0)[c]{$s_0$}}
   \put(136,5){\makebox(0,0)[c]{$s_0'$}}
   \put(25,70){\makebox(0,0)[c]{$\times$}}
   \put(135,70){\makebox(0,0)[c]{$\times$}}
   \put(36,66){\makebox(0,0)[c]{$\bbp$}}
   \put(148,66){\makebox(0,0)[c]{$\bbp$}}
  \end{picture}
  \caption{analytic continuation along an underground path}
  \label{pic4}
 \end{figure}
\end{center}

 This is very close to the Robba-Christol theory of ``algebraic
 elements'' \cite{feea}, in which the main player is the \emph{complete}
 subalgebra of $H^{\infty}(\matheur{D}_{\C_p}(0,1^-))$ (the algebra of bounded
 analytic functions) generated the algebraic functions analytic on
 $\matheur{D}_{\C_p}(0,1^-)$. Underlying this ``algebraic'' analytic
 continuation, 
 there is a combinatorics of \emph{automata} (whereas a combinatorics of
 graphs underlies the ``topological'' analytic continuation, as we have
 seen).\footnote{for these and further aspects of the Krasner, resp.
 Christol-Robba, analytic continuation, we refer to \cite{paeap} and to the mimeographed
 notes of the numerous conferences of the Groupe d'\'etude d'analyse
 ultram\'etrique, Paris, devoted to this subject (1973-1980).}
\end{para}

\begin{rem}
 The complex formula $\log z = \lim_n n\bigl(z^\frac{1}{n}-1\bigr)$ has the
 following $p$-adic analogue: $\log z = \lim_n p^{-n}(z^{p^n}-1)$ for $z
 \in \matheur{D}(1,1^-)$. However, the convergence is not uniform on
 $\matheur{D}(1,1^-)$, and the analytic function $\log z$ is not bounded
 on that disk.  Nevertheless $\log : \matheur{D}(1,1^-) \rightarrow
 {\A}^1$ defines an infinite Galois \'etale covering of the $p$-adic
 affine line (not at all a topological covering), with Galois group
 $\mu_{p^{\infty}}$, the $p$-primary torsion in $\C_p$.
\end{rem}


\subsection{$\widehat{\mathcal{R}^{\mathrm{et}}}$ and unit-root $F$-crystals.}
\label{sub-r-and-unit-root}
\begin{para}
 Let us assume for technical simplicity that $p\neq 2$. Let $\mathcal{M}$ be
 a free $\mathcal{R}$-module of finite rank $\mu$, endowed with a connection
 $\nabla: \mathcal{M} \rightarrow
 \Omega_\mathcal{R}\otimes_\mathcal{R}\mathcal{M}$, where
 $\Omega_\mathcal{R}$ is the rank-one module of continuous differentials
 (relative to $\mathfrak{v}$).

 In general, solutions make sense only very locally: typically, analytic
 solutions exist in disks of radius $p^\frac{-1}{p-1}$ (the radius of
 $p$-adic convergence of the exponential function, which is the basic
 example).  A very important criterion, due to B.~Dwork, for the
 convergence of analytic solutions in any open disk of radius $1$, is
 the existence of a so-called Frobenius structure.
\end{para}

\begin{para}\label{para:f-cris}
 {\itshape $F$-crystals.}  Let $\sigma$ be the Frobenius automorphism of
 $\mathfrak{v}$ lifting the $p$th-power map in $\ovl{\F}_p$. There
 are many $\sigma$-linear endomorphisms $\phi$ of $\mathcal{R}$ which reduce
 to the $p$th-power map of $\mathcal{O}(S_0)$ in characteristic
 $p$. For instance, we can take $\phi(z) = z^p$, so that
 $\phi\bigl((z-\zeta_1)\ldots (z-\zeta_{\nu})\bigr) =
 (z^p-\sigma(\zeta_1))\ldots
 (z^p-\sigma(\zeta_{\nu})) \equiv
 \bigl((z-\zeta_1)\ldots (z-\zeta_{\nu})\bigr)^p
 \pmod{p}$. One can show that any lifting $\phi$ extends uniquely to a 
 $\pi_1^{\mathrm{alg}}(S_0,s_0)$-equivariant endomorphism of
 $\widehat{\mathcal{R}^{\mathrm{et}}}$.

 A Frobenius structure on $(\mathcal{M},\nabla)$ is a rule $F$ which
 associates to every lifting $\phi$ a homomorphism $F(\phi):
 \phi^{\ast}\mathcal{M} \rightarrow \mathcal{M}$ (that is to say, a
 $\phi$-linear endomorphism of $\mathcal{M}$) such that:

\begin{enumerate}
 \item $F(\phi)\otimes \Q$ is an \emph{isomorphism},
 \item $F(\phi)$ is \emph{horizontal}, \ie compatible with
       the connections
       $\phi^{\ast}\nabla$ and $\nabla$ respectively,
 \item for any two liftings $\phi$ and $\phi^{\prime}$, the
       homomorphisms $F(\phi)$ and
       $F(\phi^{\prime})$ are related by $F(\phi^{\prime}) = F(\phi)\; \circ
       \;\chi(\phi^{\prime},\phi),$ where
       $\chi(\phi^{\prime},\phi): {\phi^{\prime}}^{\ast}\mathcal{M} \rightarrow
       \phi^{\ast}\mathcal{M} $ is
       the ``Taylor isomorphism'' given by the formulas
       \begin{align*}
	\chi(\phi^{\prime},\phi)({\phi^{\prime}}^{\ast}m) & =
	 \sum_{n\geq 0}{\phi}^{\ast}
	\biggl(\nabla \Bigl(\frac{d}{dz}\Bigr)^n(m)\biggr)
	 ({\phi^{\prime}}(z)-{\phi}(z))^n/n!\\
	& = \sum_{n\geq 0}{\phi}^{\ast} 
	 \biggl(\nabla \Bigl(z\frac{d}{dz}\Bigr)^n(m)\biggr)
	 \biggl(\log\frac{{\phi^{\prime}}(z)}{{\phi}(z)}\biggr)^n\big/n!.
       \end{align*}\label{item:3}
\end{enumerate} 

In virtue of (\ref{item:3}), a Frobenius structure amounts to the data of
the semi-linear horizontal endomorphism $F(\phi)$, for the standard
$\phi(z) = z^p$.

\noindent
The triple $(\mathcal{M},\nabla, F)$ is
called an $F$-{\it crystal}, \cf \cite{tdd}\footnote{the endomorphism
$F_{S_0}$ of $S_0$ given by the $p$th-power map, as well as $\sigma$, $\phi$
and $F$ are all called ``Frobenius'' in the usual jargon, without
causing too much confusion, it seems... }.  The very existence of a
horizontal isomorphism $\phi^{\ast}\mathcal{M}\otimes {\Q} \simeq
\mathcal{M} \otimes {\Q}$ implies that the radius of convergence
${\rho}$ of any local solution of $(\mathcal{M},\nabla)$ satisfies
$\min(1,{\rho})=\min(1,{\rho}^p)$, that is to say: ${\rho}\geq 1$ (since
${\rho}\neq 0$).
\end{para}

\begin{para}\label{para-unit-root}
 {\itshape Unit-root $F$-crystals.}  This is the case where $F(\phi)$
 (not only $F(\phi)\otimes {\Q}$) is an isomorphism (for one, or
 equivalently, for all $\phi$).  The name comes from their first
 appearance in Dwork's computation of the $p$-adic units among the
 reciprocal zeroes of the zeta-function of hypersurfaces in
 characteristic $p$.

 N. Katz has constructed a functor:
 \begin{equation*}
  \left(\begin{array}{l}
   \text{continuous ${\Z}_p$-representations}\\
   \text{of $\pi_1^{\mathrm{alg}}(S_0,s_0)$}
  \end{array}\right)
   \longrightarrow \text{(unit-root $F$-crystals)}
 \end{equation*}
 which associates to any free ${\Z}_p$-module $V$ of rank $r$
 with a continuous action of
 $\pi_1^{\mathrm{alg}}(S_0,s_0)$ a unit-root
 $F$-crystal $(\mathcal{U}_V,\nabla_V, F_V)$ over $\mathcal{R}$ of rank
 $r$.
 Let us recall its definition at the level of objects.
 For any $m\in \N$, we set $S_m=\Spec\;\mathcal{R}/p^m\mathcal{R}$.
 Starting from a representation $\rho$ of $\pi_1^{\mathrm{alg}}(S_0,s_0)$, let
 $G_n$ denote the image of $\rho$ in $GL(V/p^nV)$.  The homomorphism
 $\pi_1^{\mathrm{alg}}(S_0,s_0)\rightarrow G_n$ corresponds to an \'etale 
 covering $S_{n,0}\rightarrow S_0$, which has a
 unique \'etale lifting $\pi_{n,m}:\;S_{n,m}\rightarrow S_m$. The action 
 of $G_n$ on $S_{n,0}$ extends uniquely to
 $S_{n,m}$; on the other hand, the action of $\phi$ on $S_m$ extends 
 uniquely to $S_{n,m}$, and the $\phi$- and
 $G_n$-actions commute. The opposite action makes
 $\mathcal{O}_{S_{n,m}}$ into a right $G_n$-module.
 If we set $\mathcal{U}_n=
 \pi_{n,n_\ast}\mathcal{O}_{S_{n,n}}
 \otimes_{(\mathfrak{v}/p^n\mathfrak{v})[G_n]} V$, 
 we then have a compatible system of isomorphisms
 \begin{equation*}
  \Phi_n=\phi\otimes \id:\;\phi^{\ast}\mathcal{U}_n\rightarrow\mathcal{U}_n
 \end{equation*} 
 and a compatible system of connections
 \begin{equation*}
  \nabla_n=d\otimes \id:\;\mathcal{U}_n\rightarrow
 \pi_{n,n_\ast}\Omega_{S_{n,n}}\otimes_{\mathcal{R}/p^m\mathcal{R}}
 \mathcal{U}_n \simeq \Omega_\mathcal{R}\otimes_\mathcal{R} {\mathcal{U}}_n
 \end{equation*} 
 The unit-root crystal attached to $\rho$ is given 
 by $\mathcal{U}=\varprojlim_n \mathcal{U}_n,
 \nabla=\varprojlim_n \nabla_n,\Phi=\varprojlim_n \Phi_n$.

 The next statement summarizes results of Katz and R.~Crew \cite{fapr}.
\end{para}

\begin{pro}
 \begin{enumerate}
  \item The Katz functor is an equivalence of categories;
  \item any unit-root $F$-crystal $(\mathcal{U},\nabla, F)$ is
	solvable in $\widehat{\mathcal{R}^{\mathrm{et}}}$, \ie :
	$\mathcal{U}\otimes_\mathcal{R}
	\widehat{\mathcal{R}^{\mathrm{et}}}\simeq
	(\mathcal{U}\otimes_\mathcal{R}
	\widehat{\mathcal{R}^{\mathrm{et}}})^{\nabla}\otimes_{\mathfrak{v}}
	\widehat{\mathcal{R}^{\mathrm{et}}}$;
  \item the rule  $\;(\mathcal{U},\nabla, F) \mapsto
	(\mathcal{U}\otimes_\mathcal{R}
	\widehat{\mathcal{R}^{\mathrm{et}}})^{\nabla =0, F(\phi)=\id}$
	(with Galois action coming from that on
	$\widehat{\mathcal{R}^{\mathrm{et}}}$) provides an inverse of
	the Katz functor. 
  \end{enumerate}
\end{pro}
More precisely, we have the action of $\phi$ and $d/dz$ on 
$\widehat{\mathcal{R}^{\mathrm{et}}}$ commute with the action of
$\pi_1^{\mathrm{alg}}(S_0,s_0)$, and we have a canonical isomorphism
\begin{equation*}
 \mathcal{U}\otimes_\mathcal{R}\widehat{\mathcal{R}^{\mathrm{et}}}
  \simeq V\otimes_{\Z_p}\widehat{\mathcal{R}^{\mathrm{et}}}
\end{equation*}
compatible with $\phi, d/dz$ and $\pi_1^{\mathrm{alg}}(S_0,s_0)$
(diagonal action of $\phi, d/dz$ on the left hand side, diagonal action
of $\pi_1^{\mathrm{alg}}(S_0,s_0)$ on the right hand side), which allows
to reconstruct the representation $V$ from the unit-root $F$-crystal and
conversely. In fact, the connection as well as $V$ can be reconstructed
from $(\mathcal{U}, \Phi)$ alone.

This proposition may be compared with \ref{para-cauchy-monodromy}, though it
applies to a quite different type of $p$-adic connections. In
\ref{para-cauchy-monodromy} (for dimension 1), the analytic curve $S$ had
typically bad reduction and the main player was the \emph{discrete
fundamental group} $\pi_1(\Delta)$ of the dual graph of the semistable
reduction, together with the $\pi_1(\Delta)$-module
$\mathcal{O}(\til{S})$. Here the curve $S$ has good reduction
$S_0$ and the main player is the \emph{compact fundamental group}
$\pi_1^{\mathrm{alg}}(S_0)$, together with the
$\pi_1^{\mathrm{alg}}(S_0)$-module $\widehat{\mathcal{R}^{\mathrm{et}}}$.

Before presenting one of Dwork's classical unit-root $F$-crystals, let
us just mention that the above theory extends with little change to the
case when the base ring $\mathfrak{v}$ is a finite ramified extension of
${\widehat{\Z}}^{\mathrm{ur}}_p$: one has to fix an extension of $\sigma$ to
$\mathfrak{v}$, to replace ${\Z}_p$ by $\mathfrak{v}^{\sigma}$, and
to impose some mild nilpotence constraint on $\nabla$ if the
ramification index is $\geq p-1$ (also, it is customary to extend the
definition of Frobenius structure on replacing $\phi$ by some power).

\begin{exa}\label{exa-dwork-exp}
 {\itshape Dwork's exponential.} We denote by
 $\pi$ a fixed $(p-1)$th
 root of $-p$, and set $\mathfrak{v}={\widehat{\Z}}^{\mathrm{ur}}_p[\pi]$, with
 $\sigma(\pi) = \pi$. Let us
 consider the differential equation 
 \begin{equation*}\label{eq:ast}
  f^{\prime}(z)=-\pi f(z) \tag{$\ast$}
 \end{equation*}
 over $S=\matheur{D}(0,1^+)$, which has the analytic solution $f_a =
 e^{-\pi(z-a)}$ in any residue class $\matheur{D}(a,1^-)\subset
 \matheur{D}(0,1^+)$.  The change of variable $z\mapsto z^p$ leads to
 the differential equation

 \begin{equation*}\label{eq:astp}
   g'(z)=-p\pi z^{p-1}g(z) = {\pi}^p z^{p-1}g(z) \tag{$\ast_p$}
 \end{equation*} 

 \noindent
 Dwork's exponential function is 
 \begin{equation*}
  E_{\pi}(z) =
   e^{\pi(z-z^p)} \in {\Z}_p[\pi][[z]].
 \end{equation*}
 This is an invertible element of $\mathcal{R}$, the $\pi$-adic completion of
 $\mathfrak{v}[z]$. This function provides the unit-root Frobenius structure
 which relates (\ref{eq:ast}) and (\ref{eq:astp}).

 Let us reformulate this in the setting of \ref{para-unit-root}: the
 relevant $F$-crystal is $(\mathcal{R}, \nabla, F)$, with $\nabla(1) =
 \pi dz$, $F(\phi)(1) = E_{\pi}(z)$ for the standard $\phi$.  This is
 the unit-root $F$-crystal attached to the finite character of
 $\pi_1^{\mathrm{alg}}({\A}^1_{{\ovl{\F}}_p},0)$ corresponding to the
 Artin-Schreier covering $z=y^p-y.$ The solution $f_0$ of $(\ast)$
 belongs to $\widehat{\mathcal{R}^{\mathrm{et}}}$: indeed, $e^{-\pi z}=
 E_{\pi}(y) \in {\widehat{\mathfrak{v}[y]}} \subset
 \widehat{\mathcal{R}^{\mathrm{et}}}$;
 explicitly, $e^{-\pi z}=\lim_n(1-\pi p^n z)^{p^{-n}}$.

 Dwork has computed the value of his exponential for any $(p-1)$th
 root of unity $\zeta_{p-1}$ (\eg $\zeta_{p-1} =1$): this is

 \begin{equation*}
  E_{\pi}(\zeta_{p-1})=\zeta_p^{\zeta_{p-1}} 
 \end{equation*}

 where $\zeta_p$ is the unique $p$th root of unity $\equiv
 1+\pi\pmod{\pi}$ (\cf \cite[chap. 14]{cf1a2}).  In the spirit of
 \ref{para-analytic-cont}, this may be understood as follows:

 $\zeta_p^{\zeta_{p-1}}=$ \emph{the value at $(z=0)$ of the analytic
 continuation of $f_0$ along the ``wild loop''} corresponding to the
 path from $(y=0)$ to $(y=\zeta_{p-1})$ on the Artin-Schreier covering
 $z=y^p-y$ in characteristic $p$ (figure \ref{pic2}).  If one
 changes $\zeta_{p-1}$, this value $\zeta_p^{\zeta_{p-1}}$ is multiplied
 by some $p$th root of unity.

\begin{figure}[h]
 \begin{picture}(200,130)(0,0)

  \put(0,0){\includegraphics[height=4cm,clip]{fig5.eps}}
  \put(40,102){\makebox(0,0)[c]{$\scriptstyle{\zeta_{p-1}}$}}
  \put(48,99.5){$\bbp$}
  \put(43,84){\makebox(0,0)[c]{$\scriptstyle{0}$}}
  \put(48,81){$\bbp$}
  \put(40,55){\makebox(0,0)[r]{$\scriptstyle{y^p-y=x}$}}
  \put(43,23){\makebox(0,0)[c]{$\scriptstyle{0}$}}
  \put(48,20){$\bbp$}
  \put(180,90){\makebox(0,0)[c]{$y$}}


  \put(180,20){\makebox(0,0)[c]{$x$}}
 \end{picture}
 \caption{a wild underground loop}
 \label{pic2}
\end{figure}













In our special case, the discussion of \ref{para-analytic-cont} tells us
that $e^{-\pi z}$ \emph{admits an extension to any disk
$\matheur{D}(a,1^-) \subset \matheur{D}(0,1^+)$, analytic in that disk,
and well-defined up to multiplication by some $p$th root of unity}. It
is easy to find a formula for this extension: it must be proportional to
$e^{\pi (a-z) }$, and by evaluation at $a$, we find that it is $e^{\pi
(a-z)}E_{\pi}(b)$, where $b$ is any solution of the equation $b^p-b=a$.
Its $p$th power is, as expected, $e^{-p\pi z}$ itself.

Therefore, this multivalued exponential $e^{-\pi z}$ on $\matheur{D}(0,1^+)$
appears as a multivalued section of the logarithmic \'etale covering
$\frac{-1}{\pi}\log : \matheur{D}\bigl(1,p^{-\frac{1}{p-1}+}\bigr)
\rightarrow \matheur{D}(0,1^+)$.  This is just the \emph{opposite} way
from the complex situation, where the logarithm is a multivalued
section of the \'etale covering of $\C^{\times}$ given by the exponential.
\end{exa}


\subsection{$p$-adic chiaroscuro: overconvergence.}
\label{sub-chiaroscuro}
\begin{para}
 In fact, Dwork's exponential $E_{\pi}$ is more
 than just an element of the $\pi$-adic completion of $\mathfrak{v}[z]$: it
 is \emph{overconvergent}, \ie extends to an analytic function on a disk
 of radius $\rho > 1$ ($\rho = p^{(p-1)/p^2}$).

 Overconvergence is a fundamental notion in $p$-adic analysis: dimming
 the contours of an affinoid turns out to be the key to the finiteness
 properties of $p$-adic cohomology, as was recognized by Dwork, and
 subsequently developed by P. Monsky, G.  Washnitzer, P. Berthelot
 (rigid cohomology, $\mathcal{D}^{\dagger}$-modules)...
  \begin{figure}[h]
   \begin{picture}(80,80)(0,0)
    \put(0,0){\includegraphics{fig6.eps}}
    \put(35,35){$\bbp$}
   \end{picture}
   \caption{}
  \end{figure}
\end{para}

\begin{para}
 Let again $S$ be $\matheur{D}(0,1^+)
 \setminus \bigcup \matheur{D}(\zeta_i,1^-)$.  For any
 $\rho >1$, let us consider the bigger affinoids
 $S_{\rho}=\matheur{D}(0,{\rho}^+)
 \setminus \bigcup \matheur{D}(\zeta_i,\frac{1}{\rho}^-)$.  The ring of
 \emph{overconvergent analytic functions} on $S$ is
 
 \begin{equation*}
  \mathcal{H}^{\dagger}(S)= \bigcup_{\rho >1}\mathcal{O}(S_{\rho}).
 \end{equation*}
 Its relevance to the algebraic viewpoint on analytic continuation comes
 from the following result \cite{utdppdfa}:
\end{para}
\begin{pro}
  Let $f \in \mathcal{O}(S)$ satisfy a \emph{monic} polynomial equation
 with coefficients in $\mathcal{H}^{\dagger}(S)$. Then $f \in
 \mathcal{H}^{\dagger}(S)$.
\end{pro}
\begin{para}
 A $F$-crystal $(\mathcal{M},\nabla, F)$ is {\it overconvergent} if
 $(\mathcal{M},\nabla)$ as well as $F(\phi)$ extends over some
 $S_{\rho}$.  This is the case in example \examref{exa-dwork-exp}.  For
 unit-root $F$-crystals, Crew has given the following characterization:

\begin{pro}
 The unit-root $F$-crystal $(\mathcal{U}_V,\nabla_V, F_V )$
 attached to a $p$-adic representation $V$ is overconvergent if and only
 if the images in $GL(V)$ of the inertia groups at the missing points
 ${\ovl{\zeta}}_1\ldots,{\ovl{\zeta}}_{\nu},\infty$ are finite.
\end{pro}

 \end{para}
