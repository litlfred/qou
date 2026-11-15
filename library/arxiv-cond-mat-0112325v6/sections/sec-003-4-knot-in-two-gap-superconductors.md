---
doc_id: arxiv-cond-mat-0112325v6
doc_title: "Knots in Condensed Matters"
section_id: sec-003-4-knot-in-two-gap-superconductors
section_title: "Knot in Two-gap Superconductors"
section_number: 4
pages: 6-8
source_pdf: 0112325v6.pdf
source_sha256: f09f5047bd12651c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.993
doc_brief: "Knots in Condensed Matters — 6 sections: Front matter; Introduction; Knot in Skyrme theory"
---
In the above gauge theory of spin-1/2   
condensates the gauge interaction was a  
self-induced interaction. But when the doublet is charged,
the gauge interaction can be treated as independent.
In this case the theory can describe a two-gap superconductor.
But even in this case the knot topology and thus the knot itself
should survive. This implies that two-gap 
superconductor should also have
a topological knot.

The knot in two-gap superconductor could be either relativistic
or non-relativistic, and appear in both Abelian and non-Abelian
setting \cite{cm2}. In this paper we will discuss the relativistic 
knot in the Abelian setting (a non-relativistic
Gross-Pitaevskii type theory gives an identical result).
Consider a charged doublet scalar field $\phi$ coupled to
the real electromagnetic field,
\bea
&{\cal L} = - |D_\mu \phi|^2 + \mu^2 \phi^{\dagger}\phi 
- \dfrac{\lambda}{2} (\phi^{\dagger} \phi)^2
- \dfrac{1}{4} F_{\mu \nu}^2 , \nn\\
&D_\mu \phi = (\partial_\mu - ig A_\mu) \phi.
\label{sclag}
\eea
The Lagrangian has the equation of motion
\bea
&D^2\phi =\lambda(\phi^{\dagger} \phi
-\dfrac{\mu^2}{\lambda})\phi, \nn\\
&\partial_\mu F_{\mu \nu} = j_\nu =  i g \Big[(D_\nu
\phi)^{\dagger}\phi - \phi ^{\dagger}(D_\nu \phi) \Big].
\label{sceq1}
\eea
Now, with
\bea
\phi =\dfrac{1}{\sqrt 2} \rho \xi,~~~~~{\xi}^{\dagger}\xi = 1,
~~~~~\hat n = \xi^{\dagger} \vec \sigma \xi,
\eea
we can reduce (\ref{sceq1}) to \cite{cm2}
\bea
&\partial ^2 \rho - \Big(
\dfrac{1}{4} (\partial _\mu \hat n)^2+ g^2
(A_\mu + \tilde A_\mu)^2 \Big) \rho
= \dfrac{\lambda}{2} (\rho^2-\rho_0^2)\rho, \nn\\
&\hat n \times \partial ^2 \hat n + 2 \dfrac{\partial_\mu \rho}{
\rho} \hat n \times \partial_\mu \hat n
+ \dfrac{2}{g\rho^2} \partial_\mu F_{\mu\nu} \partial_\nu \hat n =0, \nn\\
&\partial_\mu F_{\mu\nu} = j_\mu
=g^2 \rho^2 (A_\mu + \tilde A_\mu), \nn\\
&\tilde A_\mu=-\dfrac{i}{g} \xi^{\dagger}\partial_\mu \xi,
~~~~~\rho_0=\dfrac{2\mu^2}{\lambda}.
\label{sceq2}
\eea
This is the equation for two-gap superconductor.
Notice that with $A_\mu=-\tilde A_\mu$ the first two equations
reduce to (\ref{beckeq2}). This tells that the gauge theory of 
two-component BEC and the above theory of two-gap superconductor
are closely related.

To obtain the desired knot we first construct a superconducting
helical magnetic vortex. Let 
\bea
&\rho=\rho(\varrho), 
~~~~~\xi = \Bigg( \matrix{\cos \dfrac{f(\varrho)}{2} \exp (-in\varphi) \cr
\sin \dfrac{f(\varrho)}{2} \exp (imkz)} \Bigg), \nn\\
&A_\mu= \dfrac{1}{g} \big(n A_1(\varrho) \partial_\mu\varphi
+ mk A_2(\varrho) \partial_\mu z \big), \nn\\
&\n= \xi^\dag \vec \sigma \xi
= \Bigg(\matrix{\sin{f(\varrho)}\cos{(n\varphi+mkz)} \cr
\sin{f(\varrho)}\sin{(n\varphi+mkz)} \cr \cos{f(\varrho)}}\Bigg), \nn\\
&\tilde A_\mu=-\dfrac{n}{2g} \big(\cos{f(\varrho)}+1\big)
\partial_\mu \varphi \nn\\
&- \dfrac{mk}{2g} \big(\cos{f(\varrho)}-1\big) \partial_\mu z.
\label{scans}
\eea
With this we have
\bea
&j_\mu = g\rho^2 \Big(n \big(A_1-\dfrac{\cos{f}+1}{2}\big)
\partial_\mu \varphi \nn\\
&+ mk\big(A_2-\dfrac{\cos{f}-1}{2}\big)
\partial_\mu z \Big),
\label{sc}
\eea
and (\ref{sceq2}) becomes
\bea
&\ddot{\rho}+\dfrac{1}{\varrho}\dot\rho
- \Big[\dfrac{1}{4} \Big(\dot{f}^2
+\big(\dfrac{n^2}{\varrho^2} + m^2 k^2 \big) \sin^2{f}\Big) \nn\\
&+\dfrac{n^2}{\varrho^2} \Big(A_1-\dfrac{\cos{f}+1}{2}\Big)^2
+ m^2 k^2 \Big(A_2-\dfrac{\cos{f}-1}{2}\Big)^2 \Big]\rho \nn\\
&= \dfrac{\lambda}{2}(\rho^2-\rho_0^2)\rho, \nn\\
&\ddot{f} + \big(\dfrac{1}{\varrho}
+2\dfrac{\dot{\rho}}{\rho} \big)\dot{f}
-2 \Big(\dfrac{n^2}{\varrho^2}\big(A_1-\dfrac{1}{2}\big) \nn\\
&+ m^2 k^2 \big(A_2+\dfrac{1}{2}\big) \Big)\sin{f} = 0, \nn\\
&\ddot{A}_1-\dfrac{1}{\varrho}\dot{A}_1 -g^2 \rho^2
\Big(A_1-\dfrac{\cos{f}+1}{2}\Big) = 0, \nn\\
&\ddot{A}_2+\dfrac{1}{\varrho}\dot{A}_2 -g^2 \rho^2
\Big(A_2-\dfrac{\cos{f}-1}{2}\Big) = 0.
\label{sceq3}
\eea
Now, we impose the following boundary condition for the non-Abelian
vortices \cite{cm2},
\bea
&\rho (0) = 0,~~~\rho(\infty) = \rho_0, 
~~~f (0) = \pi,~~~f (\infty) = 0, \nn\\
& A_1 (0) = -1,~~~A_1 (\infty) =1.
\label{scbc}
\eea
This need some explanation, because the boundary
value $A_1(0)$ is chosen to be $-1$, not $0$. This is to
assure the smoothness of $\rho(\varrho)$ and $f(\varrho)$
at the origin. Only with this boundary value they
become analytic at the origin.
At this point one might object the boundary condition, because it creates
an apparent singularity in the gauge potential at the origin.
But notice that this singularity is an unphysical
(coordinate) singularity which can easily be removed by a gauge transformation.
In fact the singularity disappears with the gauge transformation
\bea
\phi \rightarrow \phi \exp(in\varphi),
~~~~A_\mu \rightarrow A_\mu + \dfrac{n}{g} \partial_\mu \varphi,
\eea
which changes the boundary condition $A_1(0)=-1$ and 
$A_1(\infty)=1$ to $A_1(0)=0$ and $A_1(\infty) =2$.
Mathematically this boundary condition
has a deep origin, which has to do with the fact
that the Abelian $U(1)$ runs from $0$ to $2\pi$, but the $S^1$
fiber of $SU(2)$ runs from $0$ to $4\pi$ \cite{cm2}.
As for $A_2(\varrho)$, we choose $A_2(\infty)=0$ 
to make the supercurrent vanishing at infinity
and require the vortex superconducting. As we will see,
this requires a logarithmic divergence for $A_2(0)$.
The boundary condition will
have an important consequence in the following.

\begin{figure}
\includegraphics[scale=0.7]{nascknot.eps}
\caption{The non-Abelian vortex (dashed line) with
$m=0,n=1$ and the helical vortex (solid line) with $m=n=1$ in
two-gap superconductor. Here we have put $g=1,~\lambda=2$,
$k=\rho_0/10$, and $\varrho$ is in the unit of $1/\rho_0$.
Notice that $A_2$ has a logarithmic singularity at the origin.}
\label{heli-sc}
\end{figure}

With the boundary condition we can integrate (\ref{sceq3})
and obtain the non-Abelian vortex solution
of the two-gap superconductor, which is shown in Fig.\ref{heli-sc}.
The solution is very similar to the one we have in 
two-component BEC. When $m=0$, the solution (with $A_2=0$) 
describes an untwisted non-Abelian vortex \cite{cm2}. 
But when $m$ is not zero, it describes a helical magnetic vortex 
which is periodic in $z$-coordinate.
Moreover, the vortex starts from
the second component at the core,
but the first component takes over completely at the infinity.
This is due to the boundary condition $f(0)=\pi$ and $f(\infty)=0$,
which assures that our solution describes a genuine
non-Abelian vortex. This is true even when $m=0$. Only when 
$f=0$ (or $f=\pi$) the doublet effectively becomes
a singlet, and (\ref{sceq3}) describes the Abelian
Abrikosov vortex of one-gap superconductor.

There are important differences between the non-Abelian vortex 
and the Abrikosov vortex. First the non-Abelian vortex
has a non-Abelian magnetic flux quantization \cite{cm2}. 
Indeed the quantized magnetic flux $\hat \phi_z$ 
of the non-Abelian vortex along the $z$-axis is given by 
\bea
&H_z= \dfrac{n}{g} \dfrac{\dot A_1}{\varrho}, \nn\\
&\hat \phi_z = \dfrac{}{} \int H_z d^2x
= \dfrac{2\pi n}{g} \big[A_1(\infty) - A_1(0)\big] \nn\\
&= \dfrac{4\pi n}{g}.
\label{zflux}
\eea
Notice that the unit of the non-Abelian flux is $4\pi/g$,
not $2\pi/g$. This is a direct
consequence of the boundary condition (\ref{scbc}).
This non-Abelian quantization of magnetic flux comes
from the non-Abelian topology $\pi_2(S^2)$ of the doublet $\xi$,
or equivalently the triplet $\hn$, whose topological
quantum number is given by \cite{cm2}
\bea
&q = \dfrac {g}{4\pi } \int H_z d^2 x
= - \dfrac {1}{4\pi} \int \epsilon_{ij} \partial_i \xi^{\dagger}
\partial_j \xi d^2 x \nn\\
&= \dfrac {1}{8\pi} \int \epsilon_{ij} \hn \cdot (\partial_i \hn
\times \partial_j \hn) d^2 x = n.
\label{scqn}
\eea
This distinguishes our non-Abelian vortex from
the Abelian vortex whose topology is fixed by $\pi_1(S^1)$.

Another important feature of the non-Abelian vortex 
is that it carries a non-vanishing supercurrent
along the $z$-axis,
\bea
&i_z = mkg \dfrac{}{} \int \rho^2 \big(A_2
-\dfrac{\cos f +1}{2}\big)\varrho d\varrho d\varphi \nn\\
&= \dfrac{2\pi mk}{g} \int \big(\ddot A_2
+\dfrac{1}{\varrho} \dot A_2 \big) \varrho d\varrho \nn\\
&= \dfrac{2\pi mk}{g} (\varrho \dot A_2) \Big|_{\varrho=0}^{\varrho=\infty}
=-\dfrac{2\pi mk}{g} (\varrho \dot A_2) \Big|_{\varrho=0}.
\label{scz}
\eea
This is due to the logarithmic divergence of $A_2$ at the origin.

Notice that the superconducting helical vortex
has only a heuristic value, because one needs
an infinite energy to create it (since the magnetic flux
around the vortex becomes divergent because of the singularity
of $A_2$ at the origin).
With the helical vortex, however, one can make
a vortex ring by smoothly bending and connecting
two periodic ends. In the vortex ring the infinite magnetic
flux of $A_2$ can be made finite making the finite supercurrent
(\ref{scz}) of the vortex ring produce a finite flux,
and we can fix the flux to have the value $4\pi m/g$
by adjusting the current with
$k$. With this the vortex ring now
becomes a topologically stable knot.

To see this notice that the doublet $\xi$, after forming a knot,
acquires a non-trivial topology $\pi_3(S^2)$ which provides
the knot quantum number,
\bea
&Q = - \dfrac {1}{4\pi^2} \int \epsilon_{ijk} \xi^{\dagger}
\partial_i \xi ( \partial_j \xi^{\dagger}
\partial_k \xi ) d^3 x \nn\\
&= \dfrac{g^2}{32\pi^2} \int \epsilon_{ijk} C_i
(\partial_j C_k - \partial_k C_j) d^3x
=mn.
\label{bkqn}
\eea
This is nothing but the Chern-Simon index of the potential
$C_\mu$, which is mathematically identical to
the quantum number of the knots we discussed before. 
This tells that our
knot is also made of two quantized magnetic flux rings
linked together whose knot quantum number is fixed by
the linking number $mn$. Obviously two flux rings linked together
can not be separated by any continuous deformation of
the field configuration. This provides the topological stability
of the knot.

Again this topological stability is backed up
by a dynamical stability. To see this notice that the supercurrent
of the knot has two components, the one around
the knot tube which confines the magnetic flux along the knot,
but more importantly the other along the knot
which creates a magnetic flux
passing through the knot disk. This component of supercurrent
along the knot now generates a net
angular momentum which provides
the centrifugal repulsive force preventing the knot to collapse.
This makes the knot dynamically stable.

To compare our knot with the Abrikosov vortex ring (made of the
Abrikosov vortex in conventional superconductor),
notice that the Abrikosov knot is empty (i.e.,
does not carry a net supercurrent).
As importantly it is unstable, and collapses immediately.
In contrast our knot has a helical supercurrent, and is stable. 
Furthermore these two features are deeply related. 
The helical supercurrent plays a crucial role to stablize the vortex
ring by providing the net angular momentum, which prevents the
collapse of the vortex ring. And this helical supercurrent 
originates from the knot topology. This remarkable
interplay between topology and dynamics is what provides
the stability of the knot. The nontrivial topology expresses 
itself in the form of the helical supercurrent, which in turn
provides the dynamical stability of the knot. We emphasize that
this supercurrent is what distinguishes our knot from
the Abrikosov vortex ring, which has neither topological
nor dynamical stability.
