---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-003-main-results
section_title: "Main results"
section_number: null
pages: 4-7
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.993
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
We start with the Palais--Smale condition for linear combinations of the
bending energy \cref{eq:bending-energy} with any energy contained in
one of the
three families \cref{eq:E-alpha-p}, \cref{eq:TP}, or \cref{eq:intM}. But we
have to shrink slightly\footnote{This does \emph{not} change the 
respective parameter range
for $E^{\alpha,1}$, or for $\TP^{(p,q)}$ and $\intM^{(p,q)}$ if $q\in (1,2]$.}
the range of parameters by requiring in addition to
\cref{eq:individual-energy-spaces} that
\begin{equation}\label{eq:shrink-range}
\textstyle
\alpha p<p+2\Fo E^{\alpha,p},\,\, p<\frac{3}{2} q +2\Fo
\TP^{(p,q)},\AND p<\frac{5}{6} q+1\Fo \intM^{(p,q)}
\end{equation}
to allow for the compact embedding $H^2\hookrightarrow W^{1+s,\rho}$ for 
each knot energy. 
\begin{theorem}[Bending energy plus knot energy above scale-invariance]
\label[theorem]{thm:bending-knot-energy}
Let $\theta>0$,  $\bz\in\R^n$, and $\FL\in\{E^{\alpha,p},\TP^{(p,q)},
\intM^{(p,q)}\}$, where the respective combinations of
parameters $\alpha$, $p$, and $q$ are chosen
as in \cref{eq:individual-energy-spaces} and \cref{eq:shrink-range}.
Then the total energy $\TL \ceq \BendingEnergy + \theta \, \FL$ restricted to
the arclength submanifold $\AL^2_\bz\subset H^2(\R/\Z,\R^n)$ 
defined in \cref{eq:ALsz}
satisfies the {\rm (PS)}-condition.
\end{theorem}
Notice that \cref{eq:individual-energy-spaces} excludes the respective
scale-invariant energies, whose energy spaces do \emph{not} embed compactly
into $C^1(\R/\Z,\R^n)$. For example, the energy space of the
M\"obius energy $E^{2,1}$ is the Hilbert space
$H^{\frac{3}{2}}(\R/\Z,\R^n)$. To include this energy as part of
the total energy, we
use in our proof
a slightly smaller Banach space that \emph{does} embed
into $C^1$ (similarly as in 
\cite{reiter-schumacher_2021} and \cite{matt-etal_2023}).
\begin{theorem}[Bending energy plus M\"obius energy]
\label[theorem]{thm:bending-moebius-energy}
The total energy $\TL \ceq \BendingEnergy+ \theta \, E^{2,1}$ restricted
to $\AL^2_\bz$ satisfies the {\rm (PS)}-condition for every $\theta>0$ and
$\bz\in\R^n$.
\end{theorem}
We strongly believe that the statement of \Cref{thm:bending-knot-energy}
carries over to all scale-invariant energies, i.e., to $E^{\alpha,p}$
for $\alpha p=2$, to $\TP^{(p,q)}$ for $p=q+2$, and to $\intM^{(p,q)}$
for $p=\frac23 q +1$, as well.

The case of a pure knot energy  is harder to handle, and we focus
here on the tangent-point energies $\TP^{(p,2)}$ for $p\in (4,5)$ whose
energy space $H^{1+\frac{p-3}2}(\R/\Z,\R^n)$ is a Hilbert space.
\begin{theorem}[Tangent-point energies $\TP^{(p,2)}$]
\label{thm:PS-TP}
Let $\bz\in\R^n$ and $p\in (4,5)$ be fixed and set
\begin{equation}\label{eq:s-TP}
        \textstyle
        s(p)\ceq\frac{p-3}{2}.
\end{equation}
Then the tangent-point energy $\TP^{(p,2)}$ restricted to
the arclength submanifold $\AL^{1+s(p)}_\bz\subset H^{1+s(p)}(\R/\Z,\R^n)$
satisfies the {\rm (PS)}-condition.
\end{theorem}
This result carries over to O'Hara's energies $E^{\alpha,1}$ for 
$\alpha\in (2,3)$ and to the integral Menger curvature functionals
$\intM^{(p,2)}$ for $p\in (\frac73,\frac83)$,   where
one has to replace \cref{eq:s-TP} by the respective differentiability
index $s=\frac{\alpha-1}2$ or 
$s=\frac{3}{2} p -3$ of the corresponding energy space;
see \cite{freches_2025}. At this point, it seems feasible to generalize our methods to the non-Hilbert case $ \TPpq $, with suitable restrictions on $ p $ and $ q $. This is currently work in progress (see \cite{frechesetal_2026}). 

As an immediate application of the (PS)-condition we can
prove the existence of minimizing (PS)-sequences and of
minimizing knots for the total energies
$\TL = \BendingEnergy + \theta \, \FL$ of \Cref{thm:bending-knot-energy}
in any connected component of the arclength
submanifold.

\begin{corollary}[Minimizing knots for total energies]
\label{cor:minimizing-knots-total-energy}
Fix a point \,$\bz\in\R^n$ and some $\theta>0$, and let $\TL = \BendingEnergy + \theta \, \FL$
be any of the total energies considered 
in \cref{thm:bending-knot-energy,thm:bending-moebius-energy}. 
Let $\KL$ be a connected component of the arclength submanifold $\AL^2_\bz$.
Then there are a minimizing {\rm (PS)}-sequence and
a minimizing knot for $\TL|_{\KL}$.
The same statements hold true for the whole arclength submanifold, i.e., for $\KL = \AL^2_\bz$.
\end{corollary}
This result contains the existence results in
\cite[Theorem 3.1]{vdm_1999} and \cite[Theorem 1.1]{gilsbach-etal_2023}\footnote{The additional symmetry constraint considered in \cite[Theorem 1.1]{gilsbach-etal_2023} is of lower order and can be omitted to obtain
global minimizers. This was carried
out  in \cite[Theorem 2.1]{gerlach-etal_2017} but there
for the non-smooth ropelength
functional, which  can be viewed 
as the $L^\infty$-limit of $\TP_q^{1/q}$, or of
$\ML_p^{1/p}$ as $q$ or $p$ tends to infinity.}, there
for specific
choices of knot energies
in pursuit of \emph{elastic knots} in any given knot class.  
As mentioned before,
connected components of $\AL^2_\bz$ correspond to
different knot classes as we show in \Cref{thm:components-knot-classes}.

For the pure  tangent-point energies $\TP^{(p,2)}$,
which are even
of class $C^{1,1}_\loc$ on 
 the underlying arclength submanifold of the larger Hilbert space $H^{1+s(p)}
 (\R/\Z,\R^n)$,
we obtain the analogous statement.


\begin{corollary}[Minimizing knots for $\TP^{(p,2)}$]
\label{cor:minimizing-knots-TP}
Let $\bz\in\R^n$, $p\in (4,5)$, and $s(p)$ as in \cref{eq:s-TP}.
Let $\KL$ be a connected component of the arclength submanifold $\AL^{1+s(p)}_\bz$.
Then there are a minimizing {\rm (PS)}-sequence and a minimizing knot for $\TP^{(p,2)}|_{\KL}$.
This is also true for $\KL = \AL^{1+s(p)}_\bz$.
\end{corollary}
The existence of minimizing knots in prescribed knot classes
under a fixed-length constraint
has been proven in \cite[Theorem 1.3]{blatt-reiter_2015a} for the 
more general energy family
$\TP^{(p,q)}$ with parameters $p,q$ as in \cref{eq:individual-energy-spaces}.

If the energies are of class $C^{1,1}_\loc$, then one can apply
Hilbert gradient-flow techniques on the arclength submanifold
to find critical points. This was carried out by Okabe and Schrader for
the pure bending energy $\BendingEnergy$ in \cite{okabe-schrader_2023}
 which inspired the following result.
Since at this point,  the necessary 
Lipschitz-estimates for the first
variation are not available
for \emph{every} knot energy considered above,
we restrict the following result
to the subfamilies of energy functionals $\FL$ with 
\begin{align}\label{eq:subfamilies}
\FL=E^{2,1},&\OR 
\textstyle
\FL\in 
\big\{\intM^{(p,2)} : p\in (\frac{7}{3} , \frac{8}{3}) \big\}
\cup
\big\{\intM^{(p,p)} : p\in (3,6)\big\},
\notag\\
&\OR\FL\in\big\{\TP^{(p,q)} : \textnormal{$p,q$ as in \cref{eq:individual-energy-spaces},
\cref{eq:shrink-range}, and $q\ge 2$}\big\}. 
\end{align}
\begin{theorem}[Gradient flow for total energies]
\label{thm:gradient-flow-total-energy}
        Fix $\theta >0$ and $\bz\in\R^n$, set $\ML\ceq\AL^2_\bz$,
        and consider the restriction
        $\widetilde{\TL}\ceq\TL|_{\ML}$ of the total energy
        $\TL \ceq \BendingEnergy + \theta \, \FL$ to the arclength submanifold $\ML$
        for any choice of $\FL$ in \cref{eq:subfamilies}.
        Then there is a function $\phi:[0,\infty)\times\ML\to\ML$ such
        that $\phi(\cdot,\g_0)\in C^1([0,\infty),\ML)$ for every knot
        $\g_0\in\ML$, that solves the Cauchy-Problem 
        \begin{equation}
                \label{eq:gradient-flow-total-energy}
                \begin{cases}
                        \frac{\d}{\d t}\phi(t,\g_0)& =-\nabla
                        \widetilde{\TL}(\phi(t,
                        \g_0))   
                                \Foa t\in [0,\infty),\\
                        \phi(0,\g_0)&=\g_0.  
                \end{cases}
        \end{equation}
        The function $t\mapsto\widetilde{\TL}(\phi(t,\g_0))$ 
        is strictly decreasing on $[0,\infty)$ unless
        $\g_0$ is 
        a critical knot for $\widetilde{\TL}$.
        For every $t\in [0,\infty)$ the knot $\phi(t,\g_0)$ is ambiently isotopic to $\g_0$, and as
        $t\to\infty$ the solution $\phi(t,\g_0)$ subconverges
        to a critical point $\g_\infty$ of  
        $\widetilde{\TL}$, which is ambiently isotopic
        to $\g_0$ as well. 
\end{theorem}  

This Hilbert gradient flow result is new, and it 
complements the long-time existence theorems
for the $L^2$-gradient flow of $\BendingEnergy+E^{2,1}$ in 
\cite[Theorem 1]{lin-schwetlick_2010},
as well as the arclength-constrained $L^2$-gradient flow in
\cite[Theorem 4.13]{vonbrecht-blair_2017} for total energies with a certain
family
of self-repulsive
potentials containing $E^{2,1}$.

Note, that for geometric energies, one usually investigates a natural gradient flow with respect to some geometric metric, often denoted $ L^2(\dd s) $, or $ H^2(\dd s) $. However, since we restrict the $ H^2 $-flow \cref{eq:gradient-flow-total-energy} to the arclength manifold, it coincides with the projected (i.e. intrinsic) $ H^2(\d s) $-gradient flow.

The subfamilies of energies in \cref{eq:subfamilies} contain 
the tangent-point energies $\TP^{(p,2)}$ for $p\in (4,5)$. For these
pure knot energies we can
also establish long-time existence for the Hilbert gradient flow
and its subconvergence
to critical points.
\begin{theorem}[Gradient flow for $\TP^{(p,2)}$]
\label{thm:gradient-flow-TP}
For fixed $\bz \in \R^n$, $p\in (4,5)$, and $s(p)$ as in \cref{eq:s-TP} set 
$\ML\ceq\AL^{1+s(p)}_\bz\subset H^{1+s(p)}(\R/\Z,\R^n)$. 
Then for  any given initial knot $\g_0\in\ML$
we have long-time existence for the gradient
flow \cref{eq:gradient-flow-total-energy} on $\ML$ 
within the same knot class $[\g_0]$ (with $\widetilde{\TL}$ 
replaced by the restriction $\widetilde{\TP}\ceq
\TP^{(p,2)}|_{\ML}$), along which $\widetilde{\TP}$ is strictly
decreasing unless the initial knot $\g_0$ is 
a $\widetilde{\TP}$-critical point. Moreover,
the flow subconverges to a $\widetilde{\TP}$-critical knot $\g_\infty$
of the  same
knot type as $\g_0$ as time
tends to infinity. 
\end{theorem}
This result carries over to the integral Menger curvatures
$\intM^{(p,2)}$ for $p\in (\frac{7}{3},\frac{8}{3})$ and to $ E^{\alpha,1} $ for $ \alpha \in (2,3) $, \cite{freches_2025}.
In contrast to the long-time existence result for a projected 
Hilbert-gradient
flow for $\intM^{(p,2)}$ in
\cite[Theorem 1.1]{knappmann-etal_2023} we do not need to project
the flow to control the parametrizations, and we do have subconvergence
of the flow
to a critical knot. Very recently, D\"ohrer in cooperation with the
first author proved a {\L}ojasiewicz--Simon inequality, which even leads
to full 
convergence of the flow for $\TP^{(p,2)}$ in \Cref{thm:gradient-flow-TP}; 
see \cite[Theorem 1.5]{doehrer-freches_2025}.
In addition, the gradient flows in \cref{thm:gradient-flow-total-energy,thm:gradient-flow-TP} preserve
symmetries, induced, for instance, by 
a group of isometries acting on the arclength submanifold; see 
\Cref{prop:symmetry-preserving-grad-flow} where we address such symmetries
in an abstract setting. 

In view of the existing regularity results\footnote{ 
\cite[Theorem 1.5]{blatt-reiter_2015a}, \cite[Theorem 4]{blatt-reiter_2015b}, \cite[Theorem 1.2]{blatt-reiter_2013}}
for critical points of knot energies
on the open subset of regular knots under a fixed-length
constraint 
one may ask whether also the more constrained arclength critical knots obtained in
\cref{cor:minimizing-knots-total-energy,cor:minimizing-knots-TP} and \cref{thm:gradient-flow-total-energy,thm:gradient-flow-TP} are smooth. 
We prove in \cref{thm:critical-points} in an abstract setting that
arclength constrained critical knots are actually also critical knots for the more
relaxed variational problem of fixed-length, but under the assumption of 
one more
order of differentiability of the critical knot. 
 For the concrete
energies treated above  we provide this additional regularity
by carefully analyzing the additional Lagrange parameter in the variational equation.
In fact, we prove full $C^\infty$-smoothness of critical knots
for all non-negative linear combinations
of bending energy $\BendingEnergy$ and tangent-point energies $\TP^{(p,2)}$ including
the cases when only one of these energies appears.
\begin{theorem}[Smoothness of critical points of total energies]
\label{thm:smoothness}
Let $\TL_{\nu\theta}\ceq\nu \, \BendingEnergy + \theta \, \TP^{(p,2)}$ for 
 $p\in (4,5)$, $\nu,\theta\ge 0$ with $\nu+\theta>0$,
and $\ML\in\{\AL^{1+s(\nu)},\AL^{1+s(\nu)}_\bz\}$ for a fixed point 
$\bz\in\R^n$, where $s(\nu)=1$ if $\nu >0$ and $s(\nu)=s(p)$ as in \cref{eq:s-TP} if
$\nu=0$. Then   
each critical knot $\g\in\ML$
of the restricted energy $\TL_{\nu\theta}|_{\ML}$ is of class $C^\infty(\R/\Z,\R^n)$.
\end{theorem}
If $ \nu>0 $ and $ \theta=0 $, then also $ \BendingEnergy $-critical immersions with possible self-intersections are smooth.\\
\Cref{thm:smoothness} also holds if one replaces the tangent-point energies
$\TP^{(p,2)}$ by the integral Menger curvature functionals $\intM^{(p,2)}$
for $p\in (\frac{7}{3},\frac{8}{3})$, or by O'Hara's energies
$E^{\alpha,1}$ for $\alpha\in (2,3)$; see \cite{freches_2025}. 
Critical points of these three energy families
are actually  also real-analytic, 
which follows from \Cref{thm:critical-points} and the regularity proofs
for the length-constrained critical points of  O'Hara's energies
in \cite{vorderobermeier_2020}, or of
integral Menger curvature in \cite{steenebruegge-vorderobermeier_2022}, the methods of which transfer to the tangent-point energies.
