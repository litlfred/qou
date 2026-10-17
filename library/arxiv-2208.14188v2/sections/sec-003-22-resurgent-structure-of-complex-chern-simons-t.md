---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-003-22-resurgent-structure-of-complex-chern-simons-t
section_title: "Resurgent structure of complex Chern-Simons theory"
section_number: 2.2
pages: 10-15
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.992
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
The power series $\varphi_{\gamma}^{(k,\s_*)}(u,n;\tau)$ are
asymptotic.  To make sense of them, we need to apply the resurgence
theory \cite{Ecalle,Mitschi:2016fxp} (see reviews
\cite{Marino:2012zq,Dorigoni:2014hea,Aniceto:2018bis} by physicists).
Generically in physics perturbation series are asymptotic.  The
coefficients grow factorially due to the proliferation of Feynman
diagrams\footnote{Renormalons can also contribute to factorial growth
  of coefficients in a general QFT, but they are absent in complex
  Chern-Simons theory.},
\begin{equation}
  f(\tau) = \sum_{\ell=0}^\infty a_n\tau^n,\quad a_n\sim \cO(A^nn!).
\end{equation}
The series is divergent and it cannot be summed to an exact finite
value in the traditional sense.  Nevertheless, we can convert it into
an analytic function of $\tau$ by the means of Borel resummation.

We first construct the Borel transform of the
original series
\begin{equation}
  \mc{B}[f](t) = \sum_{\ell=0}^\infty \frac{a_n}{n!} t^n,
\end{equation}
which is now a convergent series with a finite radius of convergence
$1/A$.  The boundary of the disk of convergence is punctuated by
singular points.  If the singular points are sparse, the convergent
series can be analytically continued to the entire complex plane,
known as the Borel plane.  The Borel transform is said to be
\emph{resurgent} if its singular points are isolated and it can be
analytically continued to infinity in all directions bypassing its
singular points.  In this case, we can perform the Laplace transform
and define the Borel resummation
\begin{equation}
  s[f](\tau) = \int_0^\infty \mc{B}[f](\tau t) \re^{-t}\rd t.
\end{equation}
This definition involves integration along a ray $\rho_\theta$ of
angle $\theta =\arg\tau$.  If the Borel transform has no singular
points along the ray, the integral is well-defined and it gives us a
function of $\tau$.  If, however, the Borel transform does have a
singular point $w$ on the ray $\rho_\theta$, the integration is
obstructed, and we are missing non-perturbative corrections of the
order $\re^{-w/\tau}$ coming from another saddle point, and the action
of the new saddle point is $V_w = V_0 + w$, where $V_0$ is the action
at the original saddle point associated to the series $f$ we start
with.

We can define a pair of lateral Borel resummations
\begin{equation}
  s_{\pm}[f](\tau) = \int_0^{\re^{\pm \ri 0}\infty}
  \mc{B}[f](\tau t)\re^{-t} \rd t,
\end{equation}
and their difference, called the Stokes discontinuity
\begin{equation}
  \text{disc}_\theta[f](\tau) = s_{+}[f](\tau) - s_{-}[f](\tau),
\end{equation}
is of the order $\re^{-w/\tau}$.

The Borel transform $\mc{B}[f]$ is in addition called a \emph{simple
  resurgent function} if all its singular points are simple poles or
branch points.

In this paper, we assume there are only logarithmic branch points.
Then at the vicinity of a singular point at $w$, the resurgent
function $\mc{B}[f](t)$ has the form
\begin{equation}
  \mc{B}[f](t+w) = 
  -\frac{\mc{S}_w}{2\pi\ri} \mc{B}[g](t)\log(t) + \text{reg}(t).
\end{equation}
where both $\mc{B}[g](t)$ and $\text{reg}(t)$ are regular at $t=0$,
and the constant $\mc{S}_w$ is called the Stokes constant.  Here we
make it manifest that the regular function $\mc{B}[g](t)$ can be
regarded as the Borel transform of another asymptotic series
$g(\tau)$, which in fact is the perturbation series at the new saddle
point $w$.  Suppose no other singular points of $\mc{B}[f](t)$ share
the same argument $\theta = \arg w$, the Stokes discontinuity of the
original Borel resummation across the Stokes ray $\rho_\theta$ is
\begin{equation}
  \text{disc}_\theta[f](\tau) = \mc{S}_w\re^{-w/\tau} s_-[g](\tau).
  \label{eq:discStokes}
\end{equation}
To put it in a more democratic form, we can introduce elementary
trans-series
\begin{equation}
  F(\tau) = \re^{-V_0/\tau}f(\tau),\quad
  G(\tau) = \re^{-V_w/\tau}g(\tau).
\end{equation}
Then the formula of Stokes discontinuity reads
\begin{equation}
  \text{disc}_\theta[F](\tau) = s_+[F](\tau) - s_-[F](\tau)
  = \mc{S}_w s_-[G](\tau).
\end{equation}
Abstractly, it can also be represented as a linear transformation of
trans-series, whose coefficient is the Stokes constant,
\begin{equation}
  \mf{S}_\theta F = F+\mc{S}_w G.
\end{equation}
This is called the Stokes automorphism.

In summary, starting from a single perturbation series $\varphi_0$ in
a theory, one can find new saddle points and their actions by looking
for singular points of the Borel transform $\mc{B}[\varphi_0]$, and
furthermore explore the asymptotic series associated to the new saddle
points by computing the Stokes discontinuity (or expansion of Borel
transform at the singular point) of $\varphi_0$.  The same procedure
can be repeated on the new asymptotic series to uncover additional
saddle points. In general, all the saddle points of the theory are
interconnected in this way, which is called the resurgent structure of
the theory, cf.~Fig.\ref{fg:reg-net}. These relationships are
completely controlled by Stokes constants, which define for us new
invariants of the theory.
We note that Stokes constants are not necessarily symmetric,
i.e.~$\mc{S}_{ij}\neq \mc{S}_{ji}$.

\begin{figure}
  \centering
  \includegraphics[height=3.5cm]{resurg-net0}
  \caption{Demonstration of resurgent structure.}
  \label{fg:reg-net}
\end{figure}

In practise we usually do not have the entire asymptotic series
$f(\tau)$ but only the truncated power series up to certain
(relatively high) order.  The Borel transform of the truncated power
series is only a polynomial which has no poles.
In order to mimic the singularity structure of the Borel transform of
the full series, we
make use of the Pad\'{e} approximant to approximate
$\mc{B}[f](t)$,
\begin{equation}
  \mathcal{P}_N[f](t) = \frac{p_0 + p_1 t +\cdots+ p_{N} t^{N}}
  {1 + q_1 t + \cdots + q_{N} t^{N}}\,.
\end{equation}
$p_i$ and $q_i$ are determined by requiring that the power series
expansion of $\mc{P}_N[f](t)$ in $t$ coincides with $\mc{B}[f](t)$ up
to order $2N$.  Thus the poles of $\mc{P}_N[f](t)$ can be used to
infer the singularities of the Borel transform.  Then we numerically
Laplace transform the Pad\'{e} approximant to obtain the Borel
resummation. The precision of the Pad\'{e} approximant can be improved
by utilizing, say, the conformal mapping method. One can find more
numerical techniques in \cite{Caliceti_2007}.


Suppose that the theory in question has finitely many saddle points
$\sigma_i$, with the associated trans-series
\begin{equation}
  F_i(\tau) = \re^{-V_i/\tau} f_i(\tau),\quad i =1,\ldots, r.
\end{equation}
We represent all the trans-series at once by an $r$-dimensional vector
$F(\tau)$
\begin{equation}
  F(\tau) =
  \begin{pmatrix}
    F_1(\tau)\\
    \vdots\\
    F_r(\tau)
  \end{pmatrix}.
\end{equation}
If saddle point $j$ appears as a singular point at $V_j - V_i$ of the
Borel transform of $F_i(\tau)$ and the Stokes constant is
$\mc{S}_{ij}$, and it is the only singular point on the Stokes ray
$\rho_{\theta_{ij}}$ where $\theta_{ij} = \arg(V_j-V_i)$, then the
Borel resummation above and below $\rho_{\theta_{ij}}$ are related by
the Stokes automorphism
\begin{equation}
  s_+[F](\tau) = \mf{S}_{\theta_{ij}} s_-[F](\tau),
  \label{eq:Sthij}
\end{equation}
where $\mf{S}_{\theta_{ij}}$ is an $r\times r$ matrix called the Stokes
matrix, and it has the form
\begin{equation}
  \mf{S}_{\theta_{ij}} = I + \mc{S}_{ij} E_{ij}
\end{equation}
with $I$ the identity matrix, and $E_{i,j}$ the elementary matrix with
$(i,j)$-entry $1$ and all other entries zero.

If there are multiple singular points on the ray $\rho_{\theta}$, we
assume the \emph{locality condition}: the Stokes matrices of any two
Borel plane singular points commute if they are on the same Stokes
ray.  In this case, \eqref{eq:Sthij} should be generalised to
\begin{equation}
  s_+[F](\tau) = \mf{S}_\theta s_-[F](\tau),\quad
  \mf{S}_\theta = \prod_{\arg\iota=\theta} \mf{S}_\iota.
\end{equation}
The order of the product of the local Stokes matrices is irrelevant
due to the locality condition.  Furthermore, given two rays
$\rho_{\theta^+}$ and $\rho_{\theta^-}$ whose arguments satisfy
$0<\theta^+-\theta^- \leq \pi$, we define the \emph{global Stokes
  automorphism}
\begin{equation}
  s_{\theta^+}[F](\tau) = \mf{S}_{\theta^-\rightarrow \theta^+} s_{\theta^-}[F](\tau)
\end{equation}
where both sides should be analytically continued to the same value of
$\tau$.  The global Stokes automorphism
$\mf{S}_{\theta^-\rightarrow \theta^+}$ has the property of unique
factorisation
\begin{equation}
  \mf{S}_{\theta^-\rightarrow \theta^+} =
  \prod_{\theta^-<\theta<\theta^+}^{\leftarrow}
  \mf{S}_\theta.
  \label{eq:Sfac}
\end{equation}
The superscript $\leftarrow$ indicates that the product is ordered so
that $\theta$ increases from right to left.  




We can apply this theory to the trans-series
$\Phi_\gamma^{(k,\s_i)}(u,n;\tau)$ with $(i=1,\ldots,r)$ in
\eqref{eq:Zpert} coming from the state integral of $sl(2,\IC)$ Chern-Simons theory.
We also define the vector of trans-series
\begin{equation}
  \Phi_\gamma^{(k)}(u,n;\tau) =
  \begin{pmatrix}
    \Phi_\gamma^{(k,\s_1)}\\
    \vdots\\
    \Phi_\gamma^{(k,\s_r)}
  \end{pmatrix}(u,n;\tau).
  \label{eq:Zkgamma}
\end{equation}
We will be concerned with the regime where $|u|\ll 1$, which is
equivalent to $|x| \sim 1$.  We note that in this regime both holonomy
parameters $(u,n)$ can be read off uniquely from $x$: $u$ is given by
\begin{equation}
  u = \log(x^k),
\end{equation}
after which $n\in\IZ_k$ is chosen such that
\begin{equation}
  \zeta^n x = \re^u.
\end{equation}

The Borel transform $\mc{B}[\Phi_\gamma^{(k,\sigma_i)}](u,n;t)$ has
singularities at
\begin{equation}
  \Lambda_{i}^{(k),0} = \{\iota_{i,j}/k \;|\; j=1,\ldots,r,\; j\neq i\}
\end{equation}
where
\begin{equation}
  \iota_{i,j} = \frac{U_{0,0}(\s_i)-U_{0,0}(\s_j)}{2\pi\ri}.
\end{equation}
They correspond to the flat connections $j\neq i$ as predicted by the
resurgence theory.  Furthermore, there are additional singularities on
top of and slightly away from these singular points and on the
imaginary axis as well; the full set of singular points is
\begin{equation}
  \Lambda_{i}^{(k)} = \left\{
    \frac{\iota_{i,j}+2\pi\ri \ell + \log(x^k) m}{k}    \;\Big|\;
    j=1,\ldots,r,\;
    \ell\in\
    \begin{cases}
      \IZ\quad j\neq i\\
      \IZ_{\neq 0}\quad j=i
    \end{cases}\hspace{-2ex},\; m\in I(i,j,\ell)
  \right\}. \label{eq:Lmdu}
\end{equation}
Here $I(i,j,\ell)$ are finite and continuous sets of integers centered
on $0$.

These singularities form infinite towers in the imaginary direction
(see Figs.~\ref{fg:sing.k1.41}, \ref{fg:sing.k1.52} for
illustrations), and the Stokes rays passing through them are said to
form ``peacock patterns'' \cite{Garoufalidis:2020xec}.  This type of
distribution of Borel plane singularities is in fact quite
univeral. Similar patterns have already been seen in large $N$
expansion of Chern-Simons matrix integral
\cite{Pasquetti2010,Aniceto:2014hoa}, in closedly related topological
string free energies
\cite{Couso-Santamaria:2016vwq,Gu:2021ize,Alim:2021mhp,Grassi:2022zuk},
in earlier studies of complex Chern-Simons theory
\cite{Garoufalidis:2007wa}, and in other related works
\cite{Garoufalidis:2020pax}.

In the context of complex Chern-Simons theory, this reflects the fact
that due to ambiguity of the Chern-Simons action\footnote{For instance
  by a large gauge transformation the Chern-Simons action changes by
  $2\pi$.  This will change the complexified hyperbolic volume
  $U_{0,0}/(2\pi\ri)$ in \eqref{eq:U00k}, whose imaginary part is the
  Chern-Simons action.}, each trans-series
$\Phi_\gamma^{(k,\s_i)}(u,n;\tau)$ should be upgraded to a family of
trans-series with the same power series but with shifted instanton
action.  Recall the definition
\begin{equation}
  \tq = \exp \left(-\frac{2\pi\ri}{k\tau}- \frac{2\pi\ri}{k}\right),\quad
  \tx = \exp \left(\frac{\log (x^k)}{k\tau} + \frac{2\pi\ri n}{k}\right).
\end{equation}
It is convenient to parametrise the trans-series in each family as
\begin{equation}
  \Phi_\gamma^{(k,\s_i)_{\ell,m}}(u,n;\tau) = \tx^m\tq^\ell
  \Phi_\gamma^{(k,\s_i)}(u,n;\tau),\quad \ell,m\in\IZ.
\end{equation}
On the other hand, the Stokes constant that relates two trans-series
labelled by $(\s_i)_{\ell,m}$ and $(\s_j)_{\ell',m'}$ only depends on
$\s_i,\s_j$ and the differences $\ell-\ell'$, $m-m'$, and we denote it
by $\mc{S}_{i,j;\ell-\ell',m-m'}$. As a consequence, we only need to
study the resurgent properties of the vector of trans-series
$\Phi_\gamma^{(k)}(u,n;\tau)$ defined in \eqref{eq:Zkgamma}.  The Stokes
automorphism associated to the Borel plane singularity
$\iota_{i,j;\ell,m}/k = (\iota_{i,j}+2\pi\ri\ell+\log(x^k)m)/k$ is
given by
\begin{equation}
  s_+[\Phi_\gamma^{(k)}](u,n;\tau) = \mf{S}_{\iota_{i,j;\ell,m}/k}(\tx,\tq)
  s_-[\Phi_\gamma^{(k)}](u,n;\tau)
\end{equation}
where the Stokes matrix is
\begin{equation}
  \mf{S}_{\iota_{i,j;\ell,m}/k}(\tx,\tq) = I +
  \mc{S}_{i,j,\ell,m}\tx^m\tq^\ell E_{i,j}.
\end{equation}
Due to the factorisation property $\eqref{eq:Sfac}$, in order to
compute all the Stokes constants, it suffices to compute a suitable
choice of finite number of global Stokes automorphisms, and extract
the Stoks constants from their factorised form.  For instance we can
choose to compute
\begin{equation}
  \mf{S}^{(k)}_{+}(\tx,\tq) =
  \mf{S}^{(k)}_{0_{-}\rightarrow \pi+0_{-}}
  (\tx,\tq),\quad
  \mf{S}^{(k)}_{-}(\tx,\tq) =
  \mf{S}^{(k)}_{\pi+0_{-}\rightarrow 2\pi+0_{-}}
  (\tx,\tq).
\end{equation}
The entries of the global Stokes automorphisms are no longer
constants, but elements in $\IZ[\tx^{\pm 1}][[\tq]]$ (upper half
plane) or $\IZ[\tx^{\pm 1}][[1/\tq]]$(lower half plane).  See
\cite{Garoufalidis:2021osl,Garoufalidis:2020xec} for concrete
examples.

In the case of the two simplest hyperbolic knots
$\knot{4}_1, \knot{5}_2$, at level $k=1$ and for $|u|\ll 1$, the
global Stokes automorphisms $\mf{S}^{(1)}_{\pm}(\tx,\tq)$ have been
conjectured in \cite{Garoufalidis:2020xec,Garoufalidis:2020nut}.  In
this paper, we generalise the studies of these two knots to generic
level $k\geq 1$, and the main result of this paper is that the Stokes
automorphisms are \emph{independent} of the level $k$
\begin{equation}
  \mf{S}^{(k)}_{\pm}(\tx,\tq) = \mf{S}^{(1)}_{\pm}(\tx,\tq).
  \label{eq:Sk}
\end{equation}

This is rather surprising because the power series
$\varphi_{\gamma}^{(k,\s_*)}(u,n;\tau)$ are very different at
different levels.  We will demonstrate the complexity of power series
at higher levels and provide numerical evidence of \eqref{eq:Sk} in
Sections~\ref{sc:41}, \ref{sc:52}.  But before ending this section, we
give some philosophical argument for \eqref{eq:Sk}.  The following
subsection is more speculative.
