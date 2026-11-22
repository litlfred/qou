---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.966
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.intro}

For a closed 3-manifold $M$, the Cheeger-Chern-Simons 
invariant~\cite{CheegerSimons,ChernSimons} of a representation 
$\rho$ of $\pi_1(M)$ in $\SL(n,\C)$ is given by the Chern-Simons integral
\begin{equation}
\lbl{ChernSimonsintegral}
\widehat c(\rho)=\frac{1}{2}\int_Ms^*
\big(\Tr(A\wedge dA+\frac{2}{3}A\wedge A\wedge A)\big)\in \C/4\pi^2\Z,
\end{equation}
where $A$ is the flat connection in the flat $\SL(n,\C)$-bundle $E_\rho$ 
with holonomy $\rho$, and $s\colon M\to E_\rho$ is a section of $E_\rho$. 
Since $\SL(n,\C)$ is $2$-connected a section always exists, and a different 
choice of section changes the value of the integral by a multiple of $4\pi^2$.

When $n=2$, the imaginary part of the Cheeger-Chern-Simons invariant equals 
the hyperbolic volume of~$\rho$. More precisely, if 
$D\colon\widetilde M\to\H^3$ is a developing map for $\rho$ and $\nu_{\H^3}$ 
is the hyperbolic volume form, $\Imag(\widehat c(\rho))$ equals the integral 
of $D^*(\nu_{\rho})$ over a fundamental domain for $M$. In particular, if 
$M=\H^3/\Gamma$ is a hyperbolic manifold, and $\rho$ is a lift to 
$\SL(2,\C)$ of 
the geometric representation $\rho_{\geo}\colon\pi_1(M)\to\PSL(2,\C)$, the 
imaginary part equals the volume of $M$.
In fact, in this case we have
\begin{equation}
\lbl{CCSeqVolC}
\widehat c(\rho)=i(\Vol(M)+i\CS(M)),
\end{equation}
where $\CS(M)$ is the Chern-Simons invariant of $M$ (with the Riemannian 
connection). Although this result is known to experts, no proof seems to be 
available (see \cite{Snapdescription,Neumann} for discussions). We give a 
proof in Section~\ref{sec.CCS}.
The invariant $\Vol(M)+i\CS(M)$ is often referred to as \emph{complex volume}. 
Motivated by this, we define the complex volume $\Vol_\C$ of a representation 
$\rho\colon\pi_1(M)\to\SL(n,\C)$ by
\begin{equation}
\widehat c(\rho)=i\Vol_\C(\rho)
\end{equation} 
and define the \emph{volume} of $\rho$ to be the real part of the complex 
volume, i.e.~the imaginary part of the Cheeger-Chern-Simons invariant. 
Surprisingly, as we shall see, the relationship to hyperbolic volume seems 
to persist even when $n>2$.

The set of $\SL(n,\C)$-representations is a complex variety with finitely 
many components, and the complex volume is constant on components. This 
follows from the fact that representations in the same component have 
cohomologous Chern-Simons forms.
Hence, for any $M$, the set of complex volumes is a finite set.

We show that the definition of the Cheeger-Chern-Simons invariant naturally 
extends to compact manifolds with boundary, and representations 
$\rho\colon \pi_1(M)\to\SL(n,\C)$ that are \emph{boundary-unipotent}, 
i.e.~take peripheral subgroups to a conjugate of the unipotent group $N$ 
of upper triangular matrices with $1$'s on the diagonal. We formulate all 
our results in this more general setup.


The main result of the paper is a concrete algorithm for computing the set 
of complex volumes. The idea is that the set of (conjugacy classes of) 
boundary-unipotent representations can be parametrized by a variety, 
called the \emph{Ptolemy variety}, which is defined by homogeneous 
polynomials of degree $2$. The Ptolemy variety depends on a choice of 
triangulation, but if the triangulation is sufficiently fine, every 
representation is detected by the Ptolemy variety. We show that a point $c$ in the 
Ptolemy variety naturally determines an element $\lambda(c)$ in Neumann's 
extended Bloch group $\widehat\B(\C)$, such that if $\rho$ is the representation 
corresponding to $c$, we have
\begin{equation}
\lbl{VolCintro}
R(\lambda(c))=i\Vol_\C(\rho),
\end{equation}
where $R\colon\widehat\B(\C)\to\C/4\pi^2\Z$ is a Rogers dilogarithm.

There is a canonical group homomorphism
$$
\phi_n\colon\SL(2,\C)\to\SL(n,\C)
$$ 
coming from the natural $\SL(2,\C)$-action on the vector space 
$\text{Sym}^{n-1}(\BC^2)$. The map $\phi_n$ preserves unipotent elements, 
and we show that composing a boundary-unipotent representation in $\SL(2,\C)$ 
with $\phi_n$ multiplies the complex volume by $\binom{n+1}{3}$. If 
$M=\H^3/\Gamma$ is a hyperbolic $3$-manifold, the geometric representation 
$\rho_{\geo}$ always lifts to a representation in $\SL(2,\C)$, but if $M$ has 
cusps, lifts are not necessarily boundary-unipotent. In fact, by a result of 
Calegari~\cite{Calegari}, if $M$ has a single cusp, any lift of the geometric representation takes a longitude to an element with 
trace $-2$.
When $n$ is even, we shall thus, more generally, be interested in 
boundary-unipotent representations in
\begin{equation}
p\SL(n,\C)=\SL(n,\C)\big/\langle \pm I\rangle.
\end{equation}
Such representations have a complex volume defined modulo $\pi^2i$, and our 
algorithm computes these as well. By studying representations in 
$p\SL(n,\C)$, we make sure that when $M$ is hyperbolic, there is always at 
least one representation with non-trivial complex volume, namely 
$\phi_n\circ \rho_{\geo}$.

Walter Neumann has conjectured that every element in the Bloch group 
$\B(\C)$ is an integral linear combination of Bloch group elements of 
hyperbolic $3$-manifolds. Since the extended Bloch group equals the Bloch 
group up to torsion, Neumann's conjecture would imply that all complex 
volumes are, up to rational multiples of $i\pi^2$, integral linear 
combinations of complex volumes of hyperbolic $3$-manifolds.
In particular, the volumes should all be integral linear combinations of 
volumes of hyperbolic manifolds.

Our algorithm has been implemented by Matthias Goerner. The algorithm uses 
Magma~\cite{Magma} to 
compute a primary decomposition of the Ptolemy variety, and then uses 
\eqref{VolCintro} 
to compute the complex volumes. 






For $n=2$, we have computed primary decompositions of the Ptolemy varieties for all census manifolds with 
$\leq 8$ simplices (these usually finish within a fraction of a second) and all link complements with $\leq 16$ simplices in the SnapPy census~\cite{SnapPy} of knots with up to 11 crossings and links with up to 10 crossings. 
When there are more than 16 simplices some of the computations don't terminate.
For $n=3$, computations are feasible for many manifolds with up to $4$ simplices, but for $n=4$ the computations run 
out of memory for all manifolds with more than $2$ simplices. It would be 
interesting to perform numerical calculations for $n \geq 4$. 
Our computations have revealed numerous (numerical) examples of linear 
combinations as predicted by Neumann's conjecture. 
To the best of our knowledge, our examples are the first concrete 
computations (the first of which were carried out in $2009$) of the Cheeger-Chern-Simons invariant (complex volume) 
for $n>2$.
