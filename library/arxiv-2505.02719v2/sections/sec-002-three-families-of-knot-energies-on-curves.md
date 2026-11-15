---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-002-three-families-of-knot-energies-on-curves
section_title: "Three families of knot energies on curves"
section_number: null
pages: 2-4
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:knot-energies}
O'Hara introduced and investigated
in \cite{ohara_1991a,ohara_1992a,ohara_1992b,ohara_1994}
\emph{repulsive potentials} of the form
\begin{equation}\label{eq:E-alpha-p}
E^{\alpha,p}\ceq\int_{\R/\Z}\int_{\R/\Z}\left(\frac1{|\g(u)-\g(v)|^\alpha}-\frac1{d_\g(s,t)^\alpha}\right)^p|\g'(u)||\g'(v)|\d u\d v,
\end{equation}
where $d_\g(u,v)$ denotes the intrinsic distance between the points $\g(u)$
and $\g(v)$ along the curve, regularizing the singularity of the first
summand. The most prominent example is the M\"obius energy
$E^{2,1}$, which  is not only scale-invariant but also invariant under
M\"obius transformations \cite[Theorem 2.1]{freedman-etal_1994}.

In contrast to O'Hara's energies \cref{eq:E-alpha-p} the \emph{(generalized)
tangent-point energies}
\begin{equation}\label{eq:TP}
 \TP^{(p,q)}(\gamma)= \int_{\R/\Z}\int_{-\frac{1}{2}}^\frac{1}{2}
\frac{\big|\P_{\gamma'(u)}^{\perp}(\gamma(u+w)-\gamma(u)) \big|^q}{|
\gamma(u+w)-\gamma(u)|^{p}}|\g'(u)||\g'(u+w)|\d w\d u
\end{equation}
have integrands that are finite for smooth embedded curves $\g \colon \R/\Z \to \R^n$
for a reasonable\footnote{The relevant ranges for the parameters of all
three energy families will be discussed below, in connection with
their respective energy spaces.}
parameter range for $p$ and $q$.
So, there is no need for a regularizing term. Here, $P_v^\perp$ means the
orthogonal projection onto the $(n-1)$-dimensional
linear subspace $v^\perp\subset\R^n$ for a vector $v\in\R^n\setminus\{0\}$.
The energies' name originates in the
geometric classic tangent-point energy $\TP_q\ceq2^q\TP^{(2q,q)}$ whose
integrand equals the $q$-th power of the inverse
tangent-point radius, i.e., the
radius of the unique circle through the points
$\g(u)$ and $\g(u+w)$ that is in addition tangent to the curve
$\g$ in $\g(u)$. 
This energy was suggested by Gonzalez and Maddocks in 
\cite[p. 4773]{gonzalez-maddocks_1999} as an alternative to self-repulsive
potentials, and was first investigated analytically in
\cite{strzelecki-vdm_2012}.

In addition to the tangent-point radius that defines $\TP_q$,
Gonzalez
and Maddocks suggested to also
consider the unique circle through three given curve points, which
leads to integral Menger curvature $\ML_p\ceq2^p\intM^{(p,p)}$
as a specific member of the family of
\emph{(generalized) integral Menger curvatures}
\begin{equation}\label{eq:intM}
\Mpq=\iiintRZ\frac{\left|\gamma'(u) \right|\left|\gamma'(v) \right|\left|\gamma'(w) \right|}{R^{(p,q)}(\gamma(u),\gamma(v),\gamma(w))}\d u \d w \d v,
\end{equation}
where
\begin{equation}\label{eq:integrand-intM}
R^{(p,q)}(x,y,z)\ceq\frac{\left( \left|y-z \right|\left|y-x \right|\left|z-x \right| \right)^p}{\left|(y-x)\wedge(z-x) \right|^q}\, \text{ for }x,y,z\in\R^n;
\end{equation}
see \cite{strzelecki-etal_2010} for first analytical
results on $\ML_p$ and \cite{strzelecki-etal_2013a} for its
impact on knot theory. 

Crucial for our investigations is the knowledge of the
exact \emph{energy spaces} for these families of knot energies.
By this we mean specific Banach spaces $\CL$ such that any arclength
parametrized closed curve has finite energy if and only if
it is embedded and contained in $\CL$.
For each of these energies the underlying energy space\footnote{For $\TP^{(p,q)}$
this was shown in \cite[Theorem 1.1]{blatt-reiter_2015a}, for $\intM^{(p,q)}$
see \cite[Theorem 1]{blatt-reiter_2015b}, and for $E^{\alpha,p}$ we 
refer to \cite[Theorem 1.1]{blatt_2012a}.}
 is a fractional
Sobolev space $W^{1+s,\rho}(\R/\Z,\R^n)$, where
\begin{equation}\label{eq:individual-energy-spaces}
\textstyle
(s,\rho)\ceq\begin{cases}
\big(\frac{\alpha p-1}{2p},2p\big) & \Fo \FL=E^{\alpha,p},\,
\alpha>0,p\ge 1,2<\alpha p < 2p+1.\\
\big(\frac{p-1-q}{q},q\big) & \textstyle
\Fo \FL=\TP^{(p,q)},\,p\in (q+2,2q+1),q>1,\\ 
\big(\frac{3p-2q-2}q,q\big) & \textstyle
\Fo \FL=\intM^{(p,q)},\,
p\in(\frac23 q+1,q+\frac23), q>1.
\end{cases}
\end{equation}
Note that in all these cases, $s\in (0,1)$.
If $\rho=2$ these fractional Sobolev spaces are Hilbert spaces, and we write
$W^{1+s,2}=H^{1+s}$, where we also admit
the case $s=1$ to include the bending energy \cref{eq:bending-energy},
whose energy space equals $H^2(\R/\Z,\R^n)$. In fact, in the present
paper we focus on the case when the energy space of the
leading order energy is a Hilbert space, allowing, e.g., for
the tangent-point energies $\TP^{(p,2)}$ for $p\in (4,5)$,
and integral Menger curvature $\intM^{(p,2)}$ for $p\in (\frac73,\frac83)$,
as well as total energies of the form $\TL \ceq \BendingEnergy + \theta \, \FL$ for some
$\theta>0$, where $\FL$ is any of the energies in
\cref{eq:individual-energy-spaces}.

Since the knot energies and the bending energy are invariant under the
action of the non-compact group of reparametrizations of the domain $\R/\Z$,
we restrict 
them to the set of injective, arclength 
parametrized curves,
\begin{equation}\label{eq:ALs}
        \AL^{1+s}
        \ceq
        \braces[\big]{
                \g\in H^{1+s}(\R/\Z,\R^n):\g_{[0,1)}\,\,\textnormal{injective}, \,|\g'|=1
        }
        ,
\end{equation}
and show in \Cref{thm:arclength-manifold} that $\AL^{1+s}$ is
a smooth submanifold of  $H^{1+s}(\R/\Z,\R^n)$ for any $s\in (\frac{1}{2},1]$.
It contains another smooth submanifold 
\begin{equation}\label{eq:ALsz}
        \textstyle
        \AL^{1+s}_\bz
        \ceq
        \braces[\big]{\g\in\AL^{1+s}:\g(0)=\bz},\quad s\in (\frac{1}{2},1],
\end{equation}
where $\bz\in\R^n$ is an arbitrary fixed point;
see \Cref{thm:arclength-manifold-point}. 
When restricting the energies
to these submanifolds we do not lose any topological information, since
we prove in \Cref{thm:strong-deformation-ALs} that the open subset of all
regular knots in $H^{1+s}(\R/\Z,\R^n)$ strongly deformation retracts
onto the submanifolds $\AL^{1+s}$ and $\AL^{1+s}_\bz$ 
for every $s\in (\frac{1}{2},1]$
and $\bz\in\R^n$. 
In addition, if two knots $\g_0$ and $\g_1$ lie in
the same connected component of $\AL^{1+s}$ then they are ambiently isotopic,
i.e., in the same knot class,
as shown in \Cref{thm:components-knot-classes}.
