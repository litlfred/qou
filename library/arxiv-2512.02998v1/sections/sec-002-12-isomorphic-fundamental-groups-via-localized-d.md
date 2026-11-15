---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-002-12-isomorphic-fundamental-groups-via-localized-d
section_title: "Isomorphic fundamental groups via localized distortion"
section_number: 1.2
pages: 2-3
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.913
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
In order to apply the results on knot equivalence, i.e., Theorem~\ref{thm:gordon-luecke},
under low regularity assumptions
we are going to use a localized version of Gromov's distortion \cite{gromov_1978}. 
For a closed, path-connected set $M\subset\R^n$ its \emph{distortion} is defined as
the quantity
\begin{equation}\label{eq:distortion}
\delta(M):=\sup_{x,y\in M\atop x\not= y}\frac{d_M(x,y)}{|x-y|}
\qquad\ge 1,
\end{equation}
where $d_M(x,y)$ denotes the  
\emph{intrinsic distance} between the points $x,y$, i.e.,
the length of the shortest curve  in $M$ connecting $x$ with $y$. It is well-known that
the circle $c_{2\pi}$ satisfies $\delta(c_{2\pi})=\frac{\pi}2$ uniquely minimizing 
the distortion among all closed curves (see \cite[Proposition 2.1]{kusner-sullivan_1997} 
for a nice and short proof of that fact).  
Moreover, any non-trivial tame
knot $\g\in C^0(\R/\Z,\R^3)$ has distortion at least
$\frac{5\pi}3$, which was shown by Denne and Sullivan in \cite{denne-sullivan_2009}.
So, distortion detects knottedness, but it is not useful to distinguish between different
knots. For example, distortion cannot prevent the pull-tight phenomenon 
where knotted subarcs of a curve 
can be scaled down to vanish in the limit without any effect
on the curve's distortion \cite{mullikin_2007}. In addition, O'Hara constructed infinitely many
different prime knots with a uniform upper bound on their distortion 
\cite[Theorem~3.5]{ohara_1992a}.
On the other hand, Gromov asked if there is a universal bound on the distortion 
under which \emph{every}
knot type can be represented.
This was answered to the negative by Pardon in
\cite[Theorems 1.1 \& 1.2]{pardon_2011}
who also points out~\cite[p.~638]{pardon_2011} that there are 
even wild knots with finite distortion such as \cite[Figure~5]{crowell-fox_1977}.

Nevertheless, a universal bound on a
localized version of distortion
together with a comparable $L^\infty$-distance guarantees knot equivalence as
we will see in Corollary \ref{cor:equiv-knots} below.
\begin{definition}\label{def:local-distortion}
For a nonempty closed, path-connected set $M\subset\R^n$ and $r>0$ we define
the \emph{local distortion of $M$ at scale $r$} as
\begin{equation}\label{eq:local-distortion}
\delta(M,r):=\sup_{x,y\in M\atop 0<|x-y|\le 2r}\frac{d_M(x,y)}{|x-y|}.
\end{equation}
We say that \emph{$M$ has local distortion strictly below $\varepsilon>0$}
if there is some $r_M>0$ such that $\delta(M,r_M)<\varepsilon$,
and we call any such $r_M>0$ an \emph{admissible scale}.



\end{definition}

Our first result on fundamental groups is stated for general 
subsets of $\R^n$ and might therefore
be of independent interest. Its formulation uses the
dimension-dependent constant
\begin{equation}\label{eq:dekster-jung}
g_n:=\sqrt{\frac{2n-2}n}\arcsin\sqrt{\frac{n}{2n-2}}
\quad\Fo n\ge 3,
\end{equation}
converging in a strictly decreasing manner
to $g_\infty:=\frac{\pi}{\sqrt{8}}$ as $n\to\infty$. Notice 
that
$g_3= \frac2{\sqrt{3}}\arcsin\frac{\sqrt{3}}2
= \frac{\sqrt{32}}{\sqrt{27}}g_\infty$ equals the
distortion of one third of a circle, whereas $g_\infty$
is the distortion of a quarter circle.
\begin{theorem}[Isomorphic fundamental groups]\label{thm:isomorphic}
Let $n\ge 3$.
If two nonempty closed, path-connected sets $M_i\subset\R^n$ 
with path-connected complements
$\R^n\setminus M_i$ have local distortion strictly
below $g_n$
at scales $r_{M_i}>0$ for $i=1,2$, and satisfy
\begin{equation}\label{eq:hausdorff}
\dist_\HH(M_1,M_2)<\frac14 \min\{r_{M_1},r_{M_2}\},
\end{equation}
then there exists an isomorphism $J:\pi_1(\R^n\setminus M_1)\to
\pi_1(\R^n\setminus M_2)$ such that its restriction to the peripheral
subgroup $P_{M_1}\subset \pi_1(\R^n\setminus M_1)$ maps $P_{M_1}$ isomorphically onto 
$P_{M_2}\subset \pi_1(\R^n\setminus M_2)$.
\end{theorem}
