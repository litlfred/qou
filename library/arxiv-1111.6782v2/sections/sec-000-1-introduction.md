---
doc_id: arxiv-1111.6782v2
doc_title: "Stationary Points of O’Hara’s Knot Energies"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1111.6782v2.pdf
source_sha256: 5acfde49432e59e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.935
doc_brief: "Stationary Points of O’Hara’s Knot Energies — In this article we study the regularity of stationary points of the knot ener- gies E(α) introduced by O’Hara in [14, 15, 16] in the range α ∈(2, 3)."
---
The motion of a knotted charged fiber within a viscous liquid
served as model for the definition of so-called \emph{knot energies}
introduced by Fukuhara~\cite{fete}.
One hopes that it will reach a stationary point minimizing its electrostatic energy
and that the resulting shape will help to determine its knot type.
The general idea is that this procedure leads to
a ``nicer shape'' for a given knot in the same knot class, i.~e.\@ a
representative that is as little entangled as possible with preferably large distances between
different strands.

For a general definition and
an outline of different knot energies we refer the reader to O'Hara~\cite{oha:en-kn}.
Recent developements include the investigation of geometric curvature energies such as the integral Menger curvature,
see Strzelecki, Szuma{\'n}ska, and von der Mosel~\cite{SM4,SM5},
which also extends to surfaces~\cite{SM6},
or tangent-point energies~\cite{SM7}
whose domains can be characterized via Sobolev-Slobodeckij spaces~\cite{blatt:tpe}.
Attraction phenomena may also be modeled by a corresponding ``inverse
knot energy'', see Alt et~al.~\cite{alt-felix}
for an example from mathematical biology discussing interaction between pairs of
filaments via cross-linkers.


In this paper, we investigate stationary points of the most prominent family of knot energies $\E:C^{0,1}\rzd\to[0,\infty]$,
\begin{equation*}
  \g \longmapsto
  \int_{\R/\Z}\int_{-1/2}^{1/2}
  \br{\frac{1}{\abs{\g(u+w)-\g(u)}^\a} - \frac{1}{d_\g(u+w,u)^\a}}
  \abs{\dg(u+w)}\abs{\dg(u)} \d w\d u, \label{eq:a}
\end{equation*}
where $\a\in[2,3)$, which goes back to O'Hara~\cite{oha:en,oha:fam-en,oha:en-func}.
Here $d_\g(u+w,u)$ denotes the intrinsic distance between $\g(u+w)$ and $\g(u)$ on the curve~$\g$.
More precisely,
$d_\g(u+w,u):= \min\big(\length(\g|_{[u,u+w]}),\length(\g)-\length(\g|_{[u,u+w]})\big)$
provided $\abs w\le\tfrac12$ where
$\length(\g) := \int_0^1 \abs{\dg(\theta)}\d\theta$
is the length of~$\g$.

The energy $E^{(2)}$ was thoroughly studied by Freedman, He, and Wang~\cite{fhw}
who coined the name ``M\"obius energy'' due to the M\"obius invariance of this energy.
While the \emph{existence of mimizers} of the M\"obuis energy is ensured in prime knot classes only,
O'Hara~\cite{oha:fam-en,oha:en-func} proved the existence of minimizers within
\emph{any} knot class if $\a\in(2,3)$.
Abrams et~al.~\cite{acfgh} proved that circles are the global minimizers of all these energies 
among all curves.

As to the \emph{regularity of stationary points}, the first result was obtained by He~\cite{he:elghf} for $\a=2$
who initially assuming $H^{2,3}$-regularity obtained $C^\infty$ by a bootstrapping argument.
Together with a purely geometric result by Freedman, He, and Wang~\cite{fhw} heavily relying on the M\"obius invariance, this gives
$C^\infty$-regularity for \emph{all} local $E^{(2)}$-\emph{minimizers} (which exist at least in prime knot classes).
An outline is given in~\cite{reiter:rtm}.
Moreover, He was able to show that under suitable conditions any
planar (i.~e.\@ $n=2$) stationary point of $E^{(2)}$ is a circle
\cite[Thm.~6.3]{he:elghf}. The argument highly relies on the M\"obius
invariance of $E^{(2)}$."

In~\cite{reiter:rkepdc}, parts of these results were carried over to the energies $\E$ for $\alpha \in [2,3)$.
It was shown that stationary points in $H^{\a,2}\cap H^{2,3}$ 
of the energy $\E + \lambda \mathscr L$, where $\mathscr L$ denotes the length functional and $\lambda>0$ is
a constant, are smooth. Here $H^{s,p}$ denote the \emph{Bessel potential spaces}.
Unfortunately, one does not know whether local minimizers
of $\E$ belong to $H^{\a,2}\cap H^{2,3}$ since the techniques used 
by Freedman, He, and Wang~\cite{fhw} to show the 
regularity of local minimizers completely break down in these cases.

In this article we will close this gap by proving a much stronger
result. We will extend the results in~\cite{reiter:rkepdc} and~\cite{oha:en-func}
and prove smoothness of stationary points of the 
functionals $\E + \lambda\mathscr L$ under very natural conditions: We 
will only assume that the curve $\gamma$ we are looking at is parametrized by arc-length
(which means no loss of generality as $\E$ is invariant of parametrization)
and satisfies $\E(\gamma)<\infty$.

The first step to show this result is to extract as much information regarding the regularity of
$\gamma$ out of the finiteness
of the energy $\E$ as possible.
After some partial result~\cite{blatt-reiter} in this
direction, in~\cite{blatt:bre} a classification of all curves with finite energy was given:
An embedded curve parametrized by arc-length
has finite energy $\E$ if and only if it belongs to the fractional Sobolev space $\W$.

Since formulas for the first variation of $\E$ are only known 
under the assumption that $\gamma \in H^2$, we then have to extend these
to injective curves in $H^{(1+\alpha)/2}$ parametrized by arc-length. In fact our 
method even allows us to show that $\E$ is continuously differentiable on this space.
To state the result,
let
\begin{equation*}
 \textstyle U_\eps := \R/\Z \times \br{[-\frac12,-\eps]\cup[\eps,\frac12]}.
\end{equation*}

\begin{theorem} \label{thm:FrechetDifferential}
  Let $\alpha \in (2,3)$. The energies $\E$ are $C^1$-differentiable on the space of all
  injective regular curves $\gamma \in H^{(1+\alpha)/2}$. Furthermore, if $\gamma$
  is parametrized by arc-length, the derivative 
  at $\gamma$ in direction $h$ is given by\footnote{
  If $\gamma$ belongs to $ H^{\alpha +1}$ one can use partial
  integration to obtain a formula for the $L^2$ gradient like in~\cite[Thm.~2.24]{reiter:rkepdc}.}
  \begin{align*}
   \delta\E(\gamma;h) = \lim_{\varepsilon \searrow 0}  \iint_{U_\eps} \Bigg( &
    (\a-2) \frac{\sp{\dg(u),\dh(u)}}{\abs w^\a}
    + 2 \frac{\sp{\dg(u),\dh(u)}}{\abs{\D\g}^\a} \\
    &{}-\a \frac{\sp{\D\g,\D h}}{\abs{\D\g}^{\a+2}}
    \Bigg) \d w\d u.
  \end{align*}
\end{theorem}

Note that this is a principle value integral, i.~e.\@ we may not replace $U_\eps$ by $U_0$.

Now we are in the position to state the main result of this article.

\begin{theorem} \label{thm:rsp}
 Let $\alpha \in (2,3)$  and $\gamma\in C^{0,1}(\mathbb R / \mathbb Z, \mathbb R^n)$ be a curve
 parametrized by arc-length with $\E(\gamma)< \infty$. If $\gamma$ is furthermore a stationary
 point of $\E + \lambda \mathscr L$, i.~e.\@ if
 \begin{equation*}
  \delta \E(\gamma;h) + \lambda \int_{\mathbb R / \mathbb Z} \sp{\gamma',h'} =0 \quad \forall h \in \W[(1+\alpha)/2]
  (\mathbb R / \mathbb Z, \mathbb R^n),
 \end{equation*}
 then $\gamma \in C^\infty(\mathbb R / \mathbb Z, \mathbb R^n)$.
\end{theorem}

The gradient flow of the M\"obius energy $E^{(2)}$ was first discussed by He~\cite{he:elghf} where 
he states short time existence results for smooth initial data.
In~\cite{blatt:gfm}, the short time existence was proven for all intial data in $C^{2,\beta}$,
$\beta >0$, and first long time existence results for this gradient flow near local minimizers
were derived. 
For a discussion of gradient flow for  $\E+ \lambda\mathscr L$ for positive $\lambda$ and $\a\in(2,3)$
or the gradient flow of $\E$ with respect to fixed length we refer the reader to~\cite{blatt:gfoh}.

The energies $\E$ represent only the one-parameter range $p=1$ of the larger family of knot energies
\begin{equation*}
  E^{\a,p}(\g) :=
  \int_{\R/\Z}\int_{-1/2}^{1/2}
  \br{\frac{1}{\abs{\g(u+w)-\g(u)}^\a} - \frac{1}{d_\g(u+w,u)^\a}}^p
  \abs{\dg(u+w)}\abs{\dg(u)} \d w\d u, \label{eq:a-p}
\end{equation*}
where $\a p\ge2$ and $(\a-2)p<1$, see O'Hara~\cite{oha:fam-en,oha:en-func} and~\cite{blatt:bre,blatt-reiter}.
We do \emph{not} expect that our results or the results for the gradient flow of the energies
carry over to $p>1$ as we expect the 
first variation to be a degenerate elliptic operator in this case.

Let us close this introduction by briefly introducing some notation and the
\emph{Sobolev spaces of fractional order} which are also referred to as \emph{Bessel potential spaces}.
For $s\in\R$ and $p\in[1,\infty]$ let
$H^{s,p} := (\mathrm{id}-\Delta)^{-s/2} L^p$ where $\Delta$ denotes the Laplacian.
There are several equivalent definitions, e.~g.\@ by
interpolation. In case $p=2$, which mainly applies to our situation,
the Bessel potential spaces coincide with the Slobodeckij spaces.
This gives rise to the following fundamental characterization of $H^{s,2}$, $s\in(0,\infty)\setminus\N$.

Let $f\in L^2\rzd$. For $s\in(0,1)$ we define the seminorm
\[ \seminorm{f}_{H^{s,2}} := \br{\int_{\R/\Z}\int_{-1/2}^{1/2} \frac{\abs{f(u+w)-f(u)}^2}{\abs w^{1+2s}} \d w\d u}^{1/2}. \]
Then the Sobolev space $H^{k+s,2}\rzd$, $k\in\N\cup\set0$,
is the set of all functions $H^{k,2}\rzd$ for which the norm
\[ \norm f_{H^{s+k,2}} := \norm f_{H^{k,2}} + \seminorm{f^{(k)}}_{H^{s,2}} \]
is finite.
We will frequently use the embedding
\begin{equation}\label{eq:embedding}
 H^{k+s,2}\rzd\hookrightarrow C^{k+s-1/2}\rzd, \qquad s\in(\tfrac12,1),
\end{equation}
see, e.~g., Taylor~\cite[Chap.~4, Prop.~1.5]{taylor}.
For further information on Sobolev spaces we refer to the books by Grafakos~\cite[Chap.~6]{grafakos:modern},
Runst and Sickel~\cite[Chap.~2]{RS},
and Taylor~\cite[Chap.~4 and~13]{taylor}.

For some space $X\subset C^{1}\rzd$ we will denote by $X_\mathrm{ir}$ the (open) subspace consisting of all
\underline injective (embedded) and \underline regular curves in~$X$.

The standard scalar product in~$\R^n$ is denoted by $\sp{\cdot,\cdot}$, for complex vectors $a,b\in\C^n$ we define
$\sp{a,b}_{\C^n}:=\sum_{k=1}^da_k\overline{b_k}$. The $L^2$-scalar product is, as usual, given by
$\sp{f,g}_{L^2}:=\int_0^1\sp{f(u),g(u)}\d u$.

Unless stated otherwise, we will assume
\[ \a\in(2,3) \]
throughout this paper.

\paragraph{Acknowledgements.}
The first author was supported by the Swiss National Science Foundation Grant Nr.~200020\_125127 and
the Leverhulm trust.
The second author was supported by DFG Transregional Collaborative Research Centre SFB~TR~71.
