---
doc_id: arxiv-2304.12545v1
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN"
section_id: sec-001-2-volumes-and-dehn-surgeries
section_title: "Volumes and Dehn surgeries"
section_number: 2
pages: 3-7
source_pdf: 2304.12545v1.pdf
source_sha256: bfc3c2be395b1b2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.983
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
---
\label{sec.3}
 
As already stated, the original main purpose of~\cite{NZ} was to study the arithmetic of 
the set of volumes of all hyperbolic 3-manifolds. It had been observed by Thurston, using
earlier work of J\o rgensen, that this volume spectrum is a well-ordered subset of the
positive reals.
In other words, there is a smallest volume (which is known), a second smallest, a third 
smallest, \dots, then a smallest limit point, a second smallest limit point, \dots, then
limits of 
these, and so on.  The proof of well-orderedness shows that these simple and higher-order
limit
points arise by ``closing up''  one or more of the cusps of a non-compact hyperbolic
3-manifold~$M$ by Dehn surgeries to obtain
a countable collection of manifolds with fewer cusps whose volumes tend from below to 
that of~$M$.  The object of~\cite{NZ} was to study the speed with which these volumes converge.

Before studying the effect of surgeries, we must understand the volume of a single hyperbolic 
3-manifold~$M$.  Clearly it can be given as the sum of the volumes of the tetrahedra of any
ideal triangulation, so the
first step is to understand these.  An (oriented and non-degenerate) ideal tetrahedron can be 
parametrized either by a shape parameter~$z$ in the complex upper half-plane, as explained in
the preceding section, or, in case~$z$ is in the upper half plane,
by the three angles $\a,\,\b,\,\g$ (positive and
with~$\a+\b+\g=\pi$) of the Euclidean triangle that one ``sees'' by looking at the
tetrahedron from any of its four cusps. When $\Im(z)>0$, the angles and the shapes are
related by $(\a,\b,\g)=(\arg(z),\arg(z'),\arg(z''))$ with $z'$ and~$z''$ as above.


According to Chapter~7 of Thurston's notes, written by Milnor, the volume of this
tetrahedron when $\Im(z)>0$ is given in terms of these two parametrizations by the two formulas
\be
\label{Kummer}
\Vol(\D(z)) \=  D(z) \;=\; \Lob(\a)+\Lob(\b)+\Lob(\g)\,,
\ee
the equality of the two being an identity due to Kummer.  (Both formulas are actually true
for all $z\ne0,\,1$, but the sum of $\a$, $\b$ and~$\g$ is $-\pi$ if $z$ is in the lower half-plane.)
Here $D(z)$ and $\Lob(\th)$ are the Bloch-Wigner dilogarithm (cf.~Section~\ref{sec.4}) and the 
Lobachevsky function, defined respectively by 
\be
\label{defD}
\begin{aligned}  D(z) &\=\Im\bigl(\Li_2(z)+\log|z|\log(1-z)\bigr)\,, \\
  \Lob(\th) &\= -\int_0^{\th} \log|2\,\sin t|\,dt
  \=\frac12\,\sum_{n=1}^\infty\frac{\sin(2n\th)}{n^2}
 \= \frac12\,D\bigl(e^{2i\th}\bigr)\;.
\end{aligned}
\ee
Thus the volume of a hyperbolic manifold $M$ triangulated by $N$ ideal tetrahedra with shape 
parameters~$z_i$ is given in terms of the dilogarithm function by
\be
\label{volM}  \Vol(M) \= \sum_{j=1}^N D(z_j)\;.
\ee

Now let $M$ be a 3-manifold with $h$ cusps.  It has a unique complete hyperbolic structure as
a quotient $\BH^3/\G$ for some lattice $\G\subset\PSL_2(\C)$ isomorphic to~$\pi_1(M)$, the
corresponding shape parameters $z^0=(z^0_1,\dots,z^0_N)$ being a solution of all $N+2h$
equations~\eqref{edge} and~\eqref{ML}. A small deformation of this hyperbolic structure
will have a nearby shape parameter vector $z=(z_1,\dots,z_N)$ satisfying only~\eqref{edge}.
By the result of Thurston mentioned earlier, the space of all such deformations has the
structure of a smooth complex manifold of dimension~$h$, so is isomorphic to a small
neighborhood $\fU$ of~0 in~$\C^h$. Thus each $z_i$ depends holomorphically on $\fu\in\fU$
and~$z_i(0)=z_i^0$.  To make this more visible, and to choose nice coordinates $\fu_i$
on~$\fU$, we have to look more closely at the structure of the cusps on~$M$ and at Dehn
surgeries.

Each cusp has the structure $[0,\infty)\times T^2$, where $T^2$ is a totally geodesically
embedded torus in~$M$ and has a flat Euclidean metric, unique up to homothety, induced by
the hyperbolic metric on~$M$.
More concretely, the cusps of~$M=\BH^3/\G$ are indexed by $P\in\BP^1(\C)$ whose
stabilizer~$\G_P$ is free
abelian of rank~2.  After conjugation we can place $P$ at~$\infty$, in which case 
$\G_\infty$ has the form
$\pm\Bigl(\begin{matrix} 1&\L\\0&1\end{matrix}\Bigr)$ for some lattice~$\L\subset\C$, 
unique up to homothety, and then we can identify~$\L$ with $H_1(T^2)$ and $T^2$ with~$\C/\L$. 
There is a canonical quadratic form on~$\L$ defined as the square of the length of a 
vector divided by the volume of~$T^2$.  If we choose an oriented basis $(\mu,\l)$ of 
$H_1(T^2)$ (``meridian'' and ``longitude'') to identify $\L$ with~$\Z^2$, then this quadratic 
form is given by $Q(p,q)=|p\tau+q|^2/\Im(\tau)$ if we rescale~$\L$ after homothety to 
be~$\Z\tau+\Z$ for some~$\tau$ in the complex upper half-plane.  

On the other hand, each element of $\L=H_1(T^2)$ can be identified with an isotopy class of
closed curves on~$T^2$. Doing a $(p,q)$ Dehn surgery at a cusp, once the basis of~$H_1(T^2)$ 
has been chosen, means removing $T^2\times[0,\infty)$ from~$M$ and replacing it by a solid 
torus in such way that the curve on~$T^2$ corresponding to the class $p\mu+q\l$ bounds 
in the solid torus. Here we assume that the integers $p$ and~$q$ are coprime, but we also 
allow~``$\infty$'' as a value for~$(p,q)$, meaning that we leave this cusp untouched.  The 
Dehn surgeries on~$M$ are then described by tuples 
$\k=((p_1,q_1),\dots,(p_h,q_h))\in(\Z^2\cup\{\infty\})^h$.  Thurston's theorem~\cite{Thurston}
tells us that if all $(p_i,q_i)$ are near enough to~$\infty$ (meaning that $(p_i,q_i)=\infty$ or 
$p_i^2+q_i^2$ is large), the surgered manifold~$M_\k$ is hyperbolic, in which case 
both the shape parameters $z_1,\dots,z_N$ and the volume~$\Vol(M_\k)$ become functions 
of~$\k$.  Explicitly, the deformed shape parameters 

$\bz(\k)=\bz(\bp,\bq)$ that tend to~$\bz^0$ as all the pairs $(p_i,q_i)$ tend to infinity 
are given by adding to the original gluing equations~\eqref{edge} the $h$ new equations given
by the product of the $p_i$-th power of the first expression by the $q_i$-th power of the 
second one in~\eqref{ML}, and then $\Vol(M_\k)$ is given by~\eqref{volM} with $z_j$
replaced by~$z_j(\k)$.

We now get two real numbers at each cusp: the value $Q_i(p_i,q_i)$ of the quadratic form
corresponding to that cusp at the pair $(p_i,q_i)$ (with the
convention~$Q_i(\infty)=\infty$) and the length
$L_i=L_i(\k)$ of the short geodesic on~$M_\k$ which is the core of the solid torus added
by the Dehn surgery
(or~0 if the $i$th cusp has not been surgered). They are related by
\be
\label{systole}
L_i \= \frac{2\pi}{Q_i(p_i,q_i)} \+ \O\biggl(\sum_{i=1}^h\frac1{p_i^4+q_i^4}\biggr)
\ee
(\cite{NZ}, Prop.~4.3) as all~$\k_i=(p_i,q_i)$ tend to infinity.  The main volume result
of~\cite{NZ}, proved by using~\eqref{volM} and analyzing the changes of the dilogarithms
under small changes of the~$z$'s, is then given by the pair of asymptotic formulas 
\begin{subequations}
  \label{XXX}
  \begin{align}\label{VolDehn1}
\Vol(M_\k) 
&\= \Vol(M) \;-\;\sum_{i=1}^h\biggl(\frac{\pi^2}{Q_i(p_i,q_i)}
\+ \O\Bigl(\frac1{p_i^4+q_i^4}\Bigr)\biggr) \\
\label{VolDehn2}  
&\= \Vol(M) \;-\;\sum_{i=1}^h\Bigl(\frac{\pi L_i}2 \+ \O\bigl(L_i^2\bigr)\Bigr)
\end{align} \end{subequations}
(Theorems 1A and~1B in~\cite{NZ}), which are equivalent to one another by virtue
of~\eqref{systole}. These volumes, as $\k=(\bp,\bq)$ ranges over all $h$-tuples of
sufficiently large pairs of coprime integers or the symbol~$\infty$ meaning unsurgered,
all belong to the hyperbolic volume spectrum, and equation~\eqref{VolDehn1} has as an
immediate corollary a description of the local structure of this volume spectrum near its
limit point, because the asymptotics of the number of lattice points, or of primitive
lattice points, in a large ellipse, is well-known.  The precise asymptotic statement, 
which we will not repeat here, is formulated explicitly as a Corollary to Theorem~1A
in~\cite{NZ}.

All of this is only for integral (and coprime) values of~$p_i$ and~$q_i$.  However, as is 
explained in~\cite{NZ} in detail, the shape parameters $z_j(\k)$ and the lengths $L_i(\k)$ 
are defined for $p$ and~$q$ real rather than just integral and coprime in pairs, and
equations~\eqref{systole} and~\eqref{XXX} still remains true.  The only point is that in
the definition of the $z_j$'s we had to take the $p_i$th and $q_i$th powers of the
equations in~\eqref{ML}, and one cannot in general take real powers of complex numbers
in a well-defined way, but since the left-hand sides of the expressions in~\eqref{ML}
are near to~1 for small deformations of the original value $\bz=\bz^0$ and since a
complex number near~1 has a well-defined logarithm near~0, there is no problem.  When the
$p_i$ and~$q_i$ are not integral, we are no longer ``filling in'' the cusp by gluing on
a solid torus, but are simply changing the hyperbolic structure on the original
open topological manifold~$M$, with the new  hyperbolic structures in general being
incomplete. 
If we now define $2h$ complex numbers $\fu=(\fu_1,\dots,\fu_h)$ and
$\fv=(\fv_1,\dots,\fv_h)$ by
$$ 
\fu_i\,=\,\sum_{j=1}^N\biggl(M'_{ij}\,\log\frac{z_j}{z_j^0}
\+M''_{ij}\,\log\frac{1-z_j}{1-z_j^0}\biggr),\quad
\fv_i\,=\,\sum_{j=1}^N\biggl(L'_{ij}\,
\log\frac{z_j}{z_j^0}\+L''_{ij}\,\log\frac{1-z_j}{1-z_j^0}\biggr),
$$
then from the symplectic properties of the gluing equations it follows
that~\cite[Lem.4.1]{N:combinatorics} 
$$ 
p_i\fu_i \+ q_i\fv_i\= 2\pi i\qquad(i=1,\dots,h)\,, 
$$
and we can take $\fu$ as canonical coordinates for the above-mentioned neighborhood $\fU$ 
of $0\in\C^h$, 
in which case each $\fv_i$ becomes an odd power series in the $\fu$'s with linear term 
$\tau_i\fu_i$
and we can write $L_i(\fu)$ and $\Vol(\fu)$ instead of $L_i(\k)$ and~$\Vol(M_\k)$.  
We should mention
that $\fu$ and~$\fv$ can be defined invariantly, without using any triangulation, 
as follows: the deformed
hyperbolic structure on~$M$ corresponds to a homomorphism $\rho:\G\to\PSL_2(\C)$ near to 
the inclusion
map, and then $\fu$ and~$\fv$ are simply the logarithms of the ratios of the eigenvalues of 
the images under~$\rho$ of the meridians and longitudes, respectively.

In terms of the new coordinates, equation~\eqref{VolDehn2} becomes
\be
\label{VolDehn3} 
\Vol(\fu) \= \Vol(M) \;-\;\frac\pi 2\,\sum_{i=1}^h L_i(\fu) \+ \ve(\fu),  
\ee
with $\ve(\fu)=\O(||\fu||^4)$ as $\fu$ tends to~0 in~$\C^h$. 
Theorem~2 of~\cite{NZ} was the statement that the function $\ve(\fu)$ defined 
by~\eqref{VolDehn3}
is harmonic, and hence is the real part of a holomorphic function $f(\fu)$ near~0 (uniquely
determined if we fix~$f(0)=0$).  
Theeorem~3, proved using equation~\eqref{Th2.2}, said that $\partial\fv_i/\partial\fu_j$ 
is symmetric in~$i$ and $j$, which implies that there is a single function $\Phi(\fu)$ with
$\partial\Phi/\partial\fu_i=2\fv_i$ for all~$i$, and that $f$ is given in terms of $\Phi$ by 
$4f=\Phi-\fu\cdot\fv$ (or equivalently by $-8f=(E-2)\Phi$, where
$E=\sum\fu_i\,\partial/\partial\fu_i$
is the Euler operator), so that the volume correction~$\ve(\fu)$ in~\eqref{VolDehn3} is
given by
\be
\label{VolDehn4}
\ve(\fu) \= \Im\bigl(f(\fu)\bigr),
\qquad f(\fu)\,:=\,\frac14\,\int_0^\fu
\biggl(\,\sum_{i=1}^h(\fv_i\,d\fu_i\,-\,\fu_i\,d\fv_i)\biggr)\,.
\ee
The function $f$ is now often called the Neumann-Zagier potential function, although
this name was used in the original paper for~$\Phi$ instead.  It should perhaps also be
mentioned that simpler proofs of the last results described could probably have been
obtained by using the second rather than the first volume formula in~\eqref{Kummer}.

There is one more important point about volumes. Another insight by Thurston was that the
volume of a hyperbolic 3-manifold, which is a positive real number, is  actually in a
natural way the imaginary part of a {\it complexified volume} whose real part is the
Chern-Simons invariant, an important topological 
invariant taking values in~$\R/4\pi^2\Z$ whose definition we omit here.
It was  conjectured in~\cite{NZ}, and proved soon afterwards by Yoshida~\cite{Yosh},
that the above formulas remain true with the volumes replaced by their complexified 
versions, the functions~$L_i(\fu)$ also lifted suitably from~$\R$ to~$\C$, and $\ve(\fu)$
replaced by~$f(\fu)$.  Later, in~\cite{N:combinatorics}, Walter showed how to
lift~\eqref{volM} to an explicit and computable expression for the complexified volume
of~$M_{\bp,\bq}$ in terms of the complex dilogarithm.
