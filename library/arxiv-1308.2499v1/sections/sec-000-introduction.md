---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-11
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.759
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
\addcontentsline{toc}{section}{Introduction}

\emph{Imagine a closed curve in the Euclidean space.
Each triple of distinct points on the curve uniquely defines
its {circumcircle} that passes through these three points.
It degenerates to a line if and only if the points are collinear.
The reciprocal of the circumcircle radius can be seen
as some kind of approximate curvature.
How much information on shape and regularity of the curve
can be drawn from the $L^{p}$-norm
of the latter quantity?}

Motivated from applications in microbiology,
Gonzalez and Maddocks~\cite{gonz-madd} investigated
this question for the case $p=\infty$.
They were in search of a notion for the \emph{thickness}
of an embedded curve that, in contrast to
other approaches, e.g.\@ Litherland et al.~\cite{lsdr}, does not require
initial regularity of the respective curves.

Thickness is influenced by both local and global properties of
a curve and is additionally related to the regularity of the curve.
In fact, the thickness of an arc-length parametrized curve
is finite if and only if it is embedded and
has a Lipschitz continuous tangent, i.e., it is $C^{1,1}$,
see Gonzalez et al.~\cite{gmsm}.
Consequently, any curve of finite thickness
parametrized by arc-length
is bi-Lipschitz continuous with a bi-Lipschitz
constant only depending on its thickness.

The latter is particularly interesting in the
context of applications. Instead of
trying to immediately determine the knot type
of a given possibly quite entangled curve, one could first ``simplify'' it
in order to obtain a nicely shaped curve,
having large distances between distant strands.
Such a deformation process could be defined by the gradient flow of a
suitable functional which should prevent the curve
from leaving the ambient knot class,
preserving the bi-Lipschitz property.

This idea was formalized into the concept of
\emph{knot energies} by O'Hara~\cite[Def.~1.1]{oha:en-kn}.
A functional on a given space of knots is
called a {knot energy} if
it is bounded below and self-repulsive,
i.e., it blows up on sequences of embedded curves converging to
a non-embedded limit curve.

Among other functionals Gonzalez and Maddocks~\cite{gonz-madd} also proposed
to investigate the functional
\[ \mathscr M_{p}(\g) := \iiint\limits_{(\R/\Z)^{3}}
 \frac{\abs{\dg(u_{1})}\abs{\dg(u_{2})}\abs{\dg(u_{3})}}{R(\g(u_{1}),\g(u_{2}),\g(u_{3}))^{p}} \d u_{1}\d u_{2}\d u_{3}, \qquad p\in(0,\infty), \]
which is called \emph{integral Menger\footnote{
Named after \textsc{Karl Menger}, 1902 -- 1985, US-Austrian mathematician,
who used the circumcircle for generalizing geometric concepts
to general metric spaces~\cite{menger}.
He worked on many fields including
distance geometry, dimension theory, graph theory.
Menger was a student of Hahn in Vienna
where he received a professorship in 1927.
Being member of the Vienna Circle, he was also
interested in philosophy and social science.
After emigrating to the USA in 1937,
he obtained a position at Notre Dame, later at Chicago.
See Kass~\cite{kass:menger} for further reading.
}
curvature}.
Here $\g:\R/\Z\to\R^{n}$ is an absolutely continuous curve and
$R(x,y,z)$ denotes the circumcircle 
of the three points $x,y,z\in\R^{n}$ given by 
\begin{equation}
 R(x,y,z):= \frac{{\abs{y-z}\abs{y-x}\abs{z-x}}}{2\abs{\br{y-x}\wedge\br{z-x}}}=\frac{\abs{y-z}}{2\sin\angle\br{y-x,z-x}}.
\end{equation}




The functionals $\mathscr M_{p}$ have been investigated by
Strzelecki, Szuma\'nska and von der Mosel in~\cite{SM5}
wherein further references can be found.
Their results cover the case $p>3$ where $\mathscr M_{p}$
is known to be a knot energy.
Especially they have been able to show that
finite energy of an arc-length parametrized curve
implies $C^{1,1-3/p}$-regularity
and its image is $C^{1}$-homeomorphic to the circle.
The regularity statement has been sharpened in~\cite{blatt:imcc}.

The element $\mathscr M_{2}$ is referred to as \emph{total Menger curvature}.
Interestingly, it plays an important r\^ole in complex analysis,
more precisely in the proof of
\emph{Vitushkin’s conjecture},
a partial solution to \emph{Painlev\'e's problem}
which asks to determine \emph{removable} sets.
These are compact sets $K\subset\C$
such that for any open $U\subset\C$ containing $K$
and for any bounded analytic function $U\setminus K\to\C$,
the latter can be extended to an analytic function on $U$.
Vitushkin conjectured that a compact set $K$ with positive finite
one-dimensional Hausdorff measure is
removable if and only if it is \emph{purely unrectifiable},
i.e.\@ it intersects every rectifiable curve in a set of measure zero.

A central result in this context is the
the curvature theorem of David and
L\'eger~\cite{leger} stating that one-dimensional Borel sets in $\C$
with finite total Menger curvature are 1-rectifiable.

Mel{$'$}nikov and Verdera~\cite{melnikov,melnikov-verdera,verdera}
discovered a connection between
$L^{2}$-boundedness of the Cauchy integral operator on
Lipschitz graphs and the Menger curvature.




For further details regarding
Vitushkin’s conjecture for removable sets
we refer to
Dudziak's monography~\cite{dudziak} and references therein.

Menger curvature for higher-dimensional objects has been discussed
in~\cite{kola1,kolaSM,kolaSz,Bkola,kola2,scholtes}.
Further information on the context of the integral Menger curvature
within the field of geometric knot theory and geometric curvature energies
can be found in the recent surveys by Strzelecki and von der Mosel~\cite{SM10,SM11}.

In this article we make a first step towards the
regularity theory of stationary points of {integral Menger curvature}.
Regularity theory for minimizers of certain knot energies
has been developed in~\cite{oha:fam-en,fhw,he:elghf,reiter:rkepdc,reiter:rtme,blatt-reiter2,blatt-reiter3}.
A summary is given in~\cite{blatt-reiter:proc,blatt-reiter:mbmb}.




Unfortunately
the Euler-Lagrange operator of $\mathscr M_{p}$ is not only non-local
but also degenerate.
In order to produce non-degenerate energies,
we embed this family into the two-parameter family of generalized integral Menger curvature
\begin{equation}\label{eq:intM}
 \E(\g):=\iiint\limits_{(\R/\Z)^{3}}
 \frac{\abs{\dg(u_{1})}\abs{\dg(u_{2})}\abs{\dg(u_{3})}}{\RR(\g(u_{1}),\g(u_{2}),\g(u_{3}))}
 {\d u_{1}\d u_{2}\d u_{3}}, \qquad p,q>0,
\end{equation}
where
\begin{equation}
 \RR(x,y,z) :=
 \frac{\br{\abs{y-z}\abs{y-x}\abs{z-x}}^{p}}{\abs{\br{y-x}\wedge\br{z-x}}^{q}}
 = \frac{\abs{y-z}^{p}\abs{y-x}^{p-q}\abs{z-x}^{p-q}}{\sin\angle\br{y-x,z-x}^{q}},
 \qquad x,y,z\in\R^{n}.
\end{equation}
Note that the function $\RR$ is symmetric in all components.
Of course, $\mathscr M_{p} = 2^{p}\E[p,p]$.

The elements of this family are
knot energies 
under certain conditions only. More precisely, we will see
in Remark~\ref{rem:non-rep} that
they are punishing self-intersections if and only if
\begin{equation}\label{eq:self-avoiding}
 p\ge\tfrac23q+1.
\end{equation}
On the other hand, these energies can only be finite on closed curves iff
\begin{equation}\label{eq:singular}
 p<q+\tfrac23,
\end{equation}
see Remark~\ref{rem:singular}.
The \emph{sub-critical range},
i.e.\@ the range of parameters that lead to a {sub}-critical Euler-Lagrange equation,\footnote{In contrast, the corresponding range is called \emph{super}-critical by Strzelecki et al.~\cite{SM9}
as it lies above the respective critical value for which the
energy is scale-invariant.}
is given by
\begin{equation}\label{eq:sub-critical}
 p\in\br{\tfrac23q+1,q+\tfrac23} \qquad (q>1),
\end{equation}
and its non-degenerate part (leading to a non-degenerate equation) is
\begin{equation}\label{eq:non-degenerate-sub-critical}
 p\in\br{\tfrac73,\tfrac83}, \qquad q=2.
\end{equation}
These areas are visualized in Figure~\ref{fig:range}.

\begin{figure}[h]
 \centering
 \includegraphics{fig-1.pdf}
 \caption{The range of $\E$.
 Above the green line, the integrand is not sufficiently singular to
penalize self-intersections, thus $\E$ is not a knot energy.
On the other hand, below the red line, for $q>1$, the integrand is so singular, that the integral is
either equal to zero or infinite, so
 there are no finite-energy $C^{1}$-knots at all.
The hatched area reveals the strange behavior that there are no finite-energy
$C^{3}$-knots while it takes finite values on polygons.}
 \label{fig:range}
\end{figure}

In~\cite{blatt:imcc}, a characterization of curves with finite $\mathscr M_{p}$ energy was given in terms of function spaces. Using this technique we infer

\begin{theorem}[\secA]\label{thm:energy-space}\hfill\\
 Consider the sub-critical case~\eqref{eq:sub-critical} and
 let $\g \in C^1(\R/\Z,\R^{n})$ be an injective curve parametrized by 
 arc-length.
 Then $\E(\g)<\infty$ if and only if~$\g \in\W$. Moreover,
 one then has, for constants $C,\beta>0$ depending on $p,q$ only,
 \begin{equation}\label{eq:energy-space}
  \norm\g_{\W} \leq C\br{\E(\g) + \E(\g)^\beta}.
 \end{equation}
\end{theorem}

We will use the last theorem to show

\begin{theorem}[\secB]\label{thm:existence}\hfill\\
 In the sub-critical case~\eqref{eq:sub-critical},
 there is a minimizer of 
 $\E$ among all injective, regular curves 
 $\g \in C^1(\R / \Z, \R^n)$ in any knot class.
\end{theorem}

To shorten notation we use the abbreviation
\begin{equation}\label{eq:short-notation}
 \T[\bullet]{v}{w}:=\D[\bullet]vw
\end{equation}
throughout this paper.
Furthermore, we sometimes omit the argument of a function if it is precisely the variable $u$, i.e.\@
$\g=\g(u)$ etc.








The first variation of $\mathscr M_{p}$, $p\ge2$,
has been derived by Hermes~\cite[Thm.~2.33, Rem.~2.35]{hermes}.
Here we use a different approach to prove

\begin{theorem}[\secC]\label{thm:first-var}
 In the sub-critical case~\eqref{eq:sub-critical}
 the functional $\E$ is $C^1$ on the subspace of all regular embedded
 $\W$-curves.

 For any arc-length parameterized embedded $\g\in\W\rzd$
 and $h\in\W\rzd$, the first variation of~$\E$ at~$\g$ in direction~$h$
 amounts to
 \begin{equation}\label{eq:dE-intro}
 \begin{split}
   &\delta\E(\g,h) \\
   &= \iiint\limits_{(\mathbb R / \mathbb Z)^3} \Bigg\{
 2q\frac{\abs{\T v0\wedge\T w0}^{q-2}}{\br{\abs{\T vw}\abs{\T v0}\abs{\T w0}}^p}
 \cdot{\sp{\T v0\wedge\T w0,\T v0\wedge\T[h] w0}} \\

 &\qquad\qquad\qquad{}-3p\frac{\abs{\T v0\wedge\T w0}^{q}}{\br{\abs{\T vw}\abs{\T v0}\abs{\T w0}}^p}\cdot\frac{\sp{\T vw,\T[h] vw}}{\abs{\T vw}^{2}}\\
 &\qquad\qquad\qquad{}+3\frac{\abs{\T v0\wedge\T w0}^{q}}{\br{\abs{\T vw}\abs{\T v0}\abs{\T w0}}^p}\cdot\sp{\dg,\dh}
\Bigg\}\d w\d v\d u.
 \end{split}
 \end{equation}
\end{theorem}






































































Using this formula, we will see that stationary points of 
the energies $\E [p,2]$ restricted to fixed length satisfy some kind of non-local uniformly elliptic 
pseudo-differential equation. If furthermore  $p \in\br{\tfrac73,\tfrac83}$,
the non-linearity turns out to be sub-critical and  we can finally use the Euler-Lagrange equation
to prove the following main result of this article:

\begin{theorem}[\secD]\label{thm:smooth}\hfill\\
 For $p\in(\tfrac73,\tfrac83)$, let $\g\in\W[3p/2-2,2]\rzd$ be a stationary point of $\E[p,2]$ with respect to fixed length, injective and parametrized by arc-length.
 Then $\g\in C^{\infty}$.
\end{theorem}

In a sense this concludes our study of the non-degenerate, 
subcritical cases of the most prominent knot energies
for curves. Regularity theory for the non-degenerate sub-critical case
has already been performed for O'Hara's energies~\cite{blatt-reiter2}
and for the generalized tangent-point energies~\cite{blatt-reiter3}.
The treatment of the critical case however
turns out to be far more involved and has yet only be done for 
O'Hara's knot energies~\cite{blatt-reiter-schikorra}.

We briefly introduce \emph{Sobolev-Slobodecki{\u\i} spaces} in the form
we will use them in this text.
Let $f\in W^{1,1}\rzd$. For $s\in(0,1)$ and $\rho\in[1,\infty)$ we define the seminorm
\begin{equation}\label{eq:Wsemi}
 \seminorm{f}_{\W[1+s,\rho]} := \br{\int_{{\R/\Z}}\int_{-1/2}^{1/2}
 \frac{\abs{f'(u+w)-f'(u)}^\rho}{\abs w^{1+\rho s}} \d w\d u}^{1/\rho}.
\end{equation}
On $W^{1,\rho}$ this seminorm is equivalent to
\begin{equation}\label{eq:Wsemi'}
 \seminormv{f}_{\W[1+s,\rho]} := \br{\int_{{\R/\Z}}\int_{-1/4}^{1/4}
 \frac{\abs{f(u+w)-2f(u)+f(u-w)}^\rho}{\abs w^{1+\rho(1+s)}} \d w\d u}^{1/\rho},
\end{equation}
see Appendix~\ref{sect:equiv}.

Now let $W^{k,\rho}\rzd$, $k\in\N$, denote the usual Sobolev space
(recall $W^{0,\rho}:=L^\rho$) and
\[ W^{k+s,\rho}\rzd := \sett{f\in W^{k,\rho}\rzd}{\norm f_{\W[k+s,\rho]}<\infty} \]
which we equip, depending on the situation, either with the norm

$\norm f_{\W[k,\rho]} + \seminorm{f^{(k-1)}}_{\W[1+s,\rho]}$
or with $\norm f_{\W[k,\rho]} + \seminormv{f^{(k-1)}}_{\W[1+s,\rho]}$
respectively.

Without further notice we will frequently use the embedding
\begin{equation}\label{eq:Wembed}
 \W[k+s,\rho]\rzd\hookrightarrow C^{k,s-1/\rho}\rzd,
 \qquad \rho\in(1,\infty), \quad s\in(\rho^{-1},1).
\end{equation}
We will denote by $\Cia[]$ resp.\@ $\Wia[]$
\underline injective (embedded) curves parametrized by \underline arc-length.


As usual, a curve is said to be \emph{regular} if there is some $c>0$ such that $\abs\dg\ge c$ a.e.
Constants may change from line to line.
