---
doc_id: arxiv-cond-mat-0112325v6
doc_title: "Knots in Condensed Matters"
section_id: sec-001-2-knot-in-skyrme-theory
section_title: "Knot in Skyrme theory"
section_number: 2
pages: 1-3
source_pdf: 0112325v6.pdf
source_sha256: f09f5047bd12651c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.802
doc_brief: "Knots in Condensed Matters — 6 sections: Front matter; Introduction; Knot in Skyrme theory"
---
The Skyrme theory has a rich topological structure.
It has skyrmion and baby skyrmion \cite{skyrme,piet}.
But recently it has been shown that the theory allows
a knotted soliton identical to
the Faddeev-Niemi knot in Skyrme-Faddeev
non-linear sigma model, which can be identified as a twisted 
vortex ring made of helical baby skyrmion \cite{prl01,plb04}. 
To see this, we review the knot in Skyrme theory first. 

Let $\omega$ and $\hn$ be the scalar field and 
the non-linear sigma field in Skyrme theory. With
\bea
&U = \exp (\omega \dfrac{\vec \sigma}{2i} \cdot \hat n)
= \cos \dfrac{\omega}{2} - i (\vec \sigma \cdot \hat n) 
\sin \dfrac{\omega}{2}, \nn\\
&L_\mu = U\partial_\mu U^{\dagger}, ~~~~~({\hat n}^2 = 1)
\eea
the Skyrme Lagrangian is expressed as
\bea
&{\cal L} = \dfrac{\mu^2}{4} {\rm tr} ~L_\mu^2 + \dfrac{\alpha}{32}
{\rm tr} \left( \left[ L_\mu, L_\nu \right] \right)^2  \nn \\
&= - \dfrac{\mu^2}{4} \Big[ \dfrac{1}{2} (\partial_\mu \omega)^2
+(1-\cos\omega)(\partial_\mu \hat n)^2 \Big]  \nn \\
& -\dfrac{\alpha}{16} \Big[ \dfrac{1-\cos\omega}{2} (\partial_\mu
\omega \partial_\nu \hat n - \partial_\nu \omega \partial_\mu \hat n)^2  \nn\\
& + (1-\cos\omega)^2 (\partial_\mu \hat n \times \partial_\nu \hat
n)^2 \Big].
\label{slag}
\eea
The equation of motion is given by
\bea
&\dfrac{\mu^2}{4} \left[ \partial^2 \omega -\sin\omega 
(\partial_\mu \hat n)^2 \right] \nn\\
&+\dfrac{\alpha}{32} \sin\omega (\partial_\mu
\omega \partial_\nu \hat n  -\partial_\nu \omega \partial_\mu \hat n)^2 \nn\\
&+\dfrac{\alpha}{8} (1-\cos\omega)
\partial_\mu \big[ (\partial_\mu
\omega \partial_\nu \hat n  -\partial_\nu \omega \partial_\mu \hat
n) \cdot \partial_\nu \hat n \big] \nn\\
& - \dfrac{\alpha}{8} (1-\cos\omega) \sin\omega (\partial_\mu \hat n \times
\partial_\nu \hat n)^2 =0, \nn \\
&\partial_\mu \Big\{ \dfrac{\mu^2}{4} (1-\cos\omega) \hat n \times
\partial_\mu \hat n \nn\\
& + \dfrac{\alpha}{16} (1-\cos\omega)
\big[ (\partial_\nu \omega)^2
\hat n \times \partial_\mu \hat n
-(\partial_\mu \omega \partial_\nu \omega) \hat n \times
\partial_\nu \hat n \big] \nn\\
&+\dfrac{\alpha}{8} (1-\cos\omega)^2
(\hat n \cdot \partial_\mu \hat n \times
\partial_\nu \hat n) \partial_\nu \hat n \Big\}=0.
\label{seq}
\eea
With the spherically symmetric ansatz
\bea
\omega = \omega (r),~~~~~\hat n = \hat r,
\eea
(3) is reduced to
\bea
&\dfrac{d^2 \omega}{dr^2} +\dfrac{2}{r} \dfrac{d\omega}{dr} -\dfrac{2
\sin\omega}{r^2}
-\dfrac{\alpha}{\mu^2} \Big[ \dfrac{\sin^2 (\omega /2)}{r^2}
\dfrac{d^2 \omega}{dr^2} \nn\\
&+\dfrac{\sin\omega}{2 r^2} (\dfrac{d\omega}{dr})^2
-\dfrac{2 \sin\omega \sin^2 (\omega /2)}{r^4} \Big] =0.
\eea
Imposing the boundary condition $\omega(0)= 2\pi$ and $\omega(\infty)= 0$,
one has the well-known skyrmion \cite{skyrme}.

A remarkable point of Skyrme theory is that $\omega=\pi$,
independent of $\hn$, becomes a classical solution \cite{prl01}.
So restricting $\omega$ to $\pi$, one can reduce the Lagrangian 
(\ref{slag}) to the Skyrme-Faddeev Lagrangian
\bea
{\cal L} \rightarrow -\dfrac{\mu^2}{2} (\partial_\mu
\hat n)^2-\dfrac{\alpha}{4}(\partial_\mu \hat n \times
\partial_\nu \hat n)^2,
\label{sflag}
\eea
in which case the equation of motion (\ref{seq}) is reduced to
\bea
&\hn \times
\partial^2 \hn + \dfrac{\alpha}{\mu^2} ( \partial_\mu N_{\mu\nu} )
\partial_\nu \hn = 0, \nn\\
&N_{\mu\nu} = \hn \cdot (\partial_\mu \hn \times \partial_\nu \hn)
=\pro_\mu C_\nu - \pro_\nu C_\mu.
\label{sfeq}
\eea
Notice that since $N_{\mu\nu}$ forms a closed two-form, 
it always admits a $U(1)$ potential $C_\mu$.

The equation (\ref{sfeq}) allows non-Abelian monopole,
baby skyrmion, helical baby skyrmion, and Faddeev-Niemi
knot as its solutions \cite{prl01,plb04}. But for our purpose it is 
important to understand the helical baby skyrmion, because this 
plays a crucial role for us to construct the knot. 
So we review the helical baby skyrmion.

To construct the desired helical baby skyrmion
let $(\varrho,\varphi,z)$ the cylindrical coodinates,
and choose the ansatz
\bea
&\n= \Bigg(\matrix{\sin{f(\varrho)}\cos{(mkz+n\varphi)} \cr
\sin{f(\varrho)}\sin{(mkz+n\varphi)} \cr \cos{f(\varrho)}}\Bigg).
\label{hvans}
\eea
With this the equation (\ref{sfeq}) is reduced to
\bea
&\Big(1+(m^2 k^2+\dfrac{n^2}{\varrho^2})
\dfrac{\sin^2{f}}{g^2 \rho^2}\Big) \ddot{f}
+ \Big( \dfrac{1}{\varrho}+ 2\dfrac{\dot{\rho}}{\rho} \nn\\
&+(m^2 k^2+\dfrac{n^2}{\varrho^2})
\dfrac{\sin{f}\cos{f}}{g^2 \rho^2} \dot{f}
+ \dfrac{1}{\varrho} (m^2 k^2-\dfrac{n^2}{\varrho^2})
\dfrac{\sin^2{f}}{g^2 \rho^2} \Big) \dot{f} \nn\\
&- (m^2 k^2+\dfrac{n^2}{\varrho^2}) \sin{f}\cos{f}=0.
\label{hveq}
\eea
So with the boundary condition
\bea
f(0)=\pi,~~f(\infty)=0,
\label{bc}
\eea
we obtain the non-Abelian vortex solutions shown in Fig.\ref{hbs}.
Notice that, when $m=0$, the solution describes
the well-known baby skyrmion \cite{piet}. But when $m$ is not zero,
it describes a helical baby skyrmion, a twisted magnetic vortex 
which is periodic in $z$-coodinate \cite{plb04}.
In this case, the vortex has a quantized magnetic flux
not only along the $z$-axis but also around the $z$-axis.

\begin{figure}[t]
\includegraphics[scale=0.5]{hbs.eps}
\caption{The baby skyrmion (dashed line) with $m=0,n=1$
and the helical baby skyrmion (solid line) with $m=n=1$ in Skyrme
theory. Here $\varrho$ is in the unit ${\sqrt \alpha}/\mu$
and $k=0.8~\mu/{\sqrt \alpha}$.}
\label{hbs}
\end{figure}

The helical baby skyrmion will become
unstable unless the periodicity condition is enforced by
hand. But it plays a very important role
because one can make it a vortex ring by smoothly connecting
two periodic ends. In this case the vortex ring 
acquires the topology of a knot, and thus becomes a knot 
itself \cite{prl01,plb04}. In fact it becomes a knot made of two
magnetic fluxes linked together, whose knot topology is described by
the Chern-Simon index of the potential $C_\mu$,
\bea
&Q = \dfrac{1}{32\pi^2} \int \epsilon_{ijk} C_i N_{jk} d^3x = mn,
\label{kqn}
\eea
which describes the Hopf mapping $\pi_3(S^2)$ defined by $\hn$.

Clearly the knot has a topological stability, because two
flux rings linked together can not be disjointed by a smooth
deformation of the field configuration.
Moreover the topological stability is 
backed up by a dynamical stability. This is because
the knot can be viewed as two magnetic fluxes linked together,
and the magnetic flux trapped in the knot disk
can not be squeezed out. This provides
a stablizing repulsive force which prevent the collapse 
of the knot \cite{plb04}.

From our discussion it becomes clear that the existence of 
the helical baby skyrmion is crucial for the existence of a topologically
stable knot. In the following we show that an identical mechanism 
works in two-component BEC and two-gap superconductor 
which guarantees the existence of a stable knot.
