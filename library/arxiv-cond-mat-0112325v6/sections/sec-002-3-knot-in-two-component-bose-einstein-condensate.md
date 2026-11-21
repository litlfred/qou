---
doc_id: arxiv-cond-mat-0112325v6
doc_title: "Knots in Condensed Matters"
section_id: sec-002-3-knot-in-two-component-bose-einstein-condensate
section_title: "Knot in Two-component Bose-Einstein Condensates"
section_number: 3
pages: 3-6
source_pdf: 0112325v6.pdf
source_sha256: f09f5047bd12651c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.991
doc_brief: "Knots in Condensed Matters — 6 sections: Front matter; Introduction; Knot in Skyrme theory"
---
The recent advent of multi-component BEC (in particular
the spin-1/2 condensate of $^{87}{\rm Rb}$ atoms)
has widely opened a new opportunity for
us to study novel topological objects which can not be
realized in ordinary (one-component) BEC \cite{bec,ruo}.
This is because the multi-component BEC naturally allows
a non-Abelian structure which accommodates a non-trivial
topological objects, in particular a topolgical knot which is
very similar to the knot in Skyrme theory \cite{bec1,bec5}.
 
There are two competing theories of two-component BEC,
the popular Gross-Pitaevskii theory \cite{ruo} and the gauge theory
of two-component BEC proposed recently \cite{bec1}. 
Both theories predict topological knots. 
Many authors have already claimed 
the existence of a knot in Gross-Pitaevskii theory \cite{ruo}.
Moreover it has been shown that this knot can be identified 
as a vorticity knot which is made of
two vorticity fluxes linked together, whose topology $\pi_3(S^2)$
is fixed by the Chern-Simon index of the velocity potential
of the condensate \cite{bec5}.

So in this section we discuss the gauge theory of two-component BEC,
and show that this theory also has a vorticity knot very similar 
to the knot in Gross-Pitaevskii theory. 
Consider a ``charged'' two-component BEC
described by a complex doublet $\phi$ interacting
``electromagnetically'', which can be described by the following
non-relativistic gauged Gross-Pitaevskii type Lagrangian (we
will discuss the relativistic generalization later)
\bea
&{\cal L} = i \dfrac {\hbar}{2} \Big[\phi^\dag (\tilde D_t \phi)
-(\tilde D_t \phi)^\dag \phi \Big] 
-  \dfrac {\hbar^2}{2m} |\tilde D_i \phi|^2 \nn\\
& + \mu^2 \phi^\dag \phi - \dfrac {\lambda}{2}
(\phi^\dag \phi)^2 - \dfrac {1}{4} \tilde F_{\mu \nu} ^2,
\label{beclag}
\eea
where $\tilde D_\mu \phi = ( \pro_\mu - i g \tilde A_\mu ) \phi$,
and $\mu^2$ and $\lambda$ are the chemical potential 
and the quartic coupling constant.
Normalizing $\phi$ to $(\sqrt{2m}/\hbar)\phi$ and putting
\bea
\phi = \dfrac {1}{\sqrt 2} \rho \xi , ~~~~~(\xi^\dag \xi = 1)
\eea
we have the following Hamiltonian in the static limit,
\bea
&{\cal H} =  \dfrac {1}{2} (\pro_i \rho)^2
+ \dfrac {\rho^2}{2} |\tilde D_i \xi |^2 \nn \\
&- \dfrac {\mu^2}{2} \rho^2 + \dfrac{\lambda}{8} \rho^4
+ \dfrac {1}{4} \tilde F_{ij} ^2.
\label{becham}
\eea
Notice that here we have also
normalized $\mu^2$ and $\lambda$ to
$(\hbar^2/2m) \mu^2$ and $(\hbar^2/2m)^2 \lambda$.
From now on we will use the normalized Hamiltonian (\ref{becham}).

At this point it is important to realize that the ``electromagnetic''
interaction here should be self-induced, since we are dealing
with neutral condensates. So we identify
the ``electromagnetic'' potential by the velocity field of
the doublet $\xi$,
\bea
\tilde A_\mu = -\dfrac {i}{g} \xi^\dag \pro_\mu \xi.
\label{am}
\eea
A justification for this is that the $U(1)$ gauge invariance almost
dictates us to identify the velocity field as the gauge potential.
Indeed in the absence of the Maxwell term, (\ref{am}) becomes 
an equation of motion. With this identification 
the field strength becomes the vorticity field
\bea
&\tilde F_{\mu\nu} = \pro_\mu \tilde A_\nu - \pro_\nu \tilde A_\mu \nn\\
&= -\dfrac {i}{g} (\pro_\mu \xi^\dag \pro_\nu \xi
- \pro_\nu \xi^\dag \pro_\mu \xi).
\label{fmn}
\eea
One might wonder why we have included 
the vorticity interaction in the Lagrangian (\ref{beclag}), 
when this is absent in the Gross-Pitaevskii Lagrangian. 
The reason is because it costs energy to create
the vorticity in two-component BEC. In ordinary BEC one does
not have to worry about the vorticity because the vorticity is identically
zero (since the velocity is given by the gradient of the phase
of the one-component complex condensate). But a non-Abelian
(multi-component) BEC has a non-vanishing vorticity,
in which case it is natural to include
the vorticity interaction in the Lagrangian \cite{bec1,bec5}. 

With (\ref{am}) the Hamiltonian (\ref{becham}) becomes
\bea
&{\cal H} = \dfrac {1}{2} (\pro_i \rho)^2 + \dfrac {\rho^2}{2}\Big(|\pro_i
\xi |^2 - |\xi^\dag \pro_i \xi|^2 \Big) 
- \dfrac {\lambda}{8} (\rho^2 - \rho^2_0)^2 \nn\\
&- \dfrac {1}{4 g^2} (\pro_i \xi^\dag \pro_j \xi 
- \pro_j \xi^\dag \pro_i \xi)^2, \nn\\
&\rho^2_0= \dfrac{2\mu^2}{\lambda}.
\label{becham1}
\eea
Notice that now the coupling constant $g$ represents
the coupling strength of the vorticity.
Minimizing the Hamiltonian we have
the following equation of motion
\bea
& \pro^2 \rho - \Big(|\pro_i \xi |^2 - |\xi^\dag \pro_i \xi|^2 \Big)
\rho = \dfrac {\lambda}{2} (\rho^2 - \rho_0^2) \rho,\nn \\
&\Big\{(\pro^2 - \xi^\dag \pro^2 \xi) + 2 (\dfrac {\pro_i
\rho}{\rho} - \xi^\dag \pro_i\xi)(\pro_i - \xi^\dag \pro_i \xi) \nn\\
&- \dfrac {1}{g^2 \rho^2} \Big[\pro_i (\pro_i
\xi^\dag \pro_j \xi - \pro_j \xi^\dag \pro_i \xi) \Big] 
(\pro_j - \xi^\dag \pro_j \xi) \Big\} \xi \nn\\
&= 0.
\label{beckeq1}
\eea
To understand the meaning of this notice that with
\bea
\n = \xi^\dag \vec \sigma \xi,
\label{hn}
\eea
we have
\bea
& |\pro_\mu \xi|^2 - |\xi^\dag \pro_\mu \xi|^2
= \dfrac{1}{4} (\pro_\mu \hn)^2, \nn\\
&i (\pro_\mu \xi^\dag \pro_\nu \xi 
- \pro_\nu \xi^\dag \pro_\mu \xi ) 
= \dfrac{1}{2} \hn \cdot (\pro_\mu \hn \times \pro_\nu \hn) \nn\\
&= \dfrac{1}{2} N_{\mu\nu},
\label{id}
\eea
where $N_{\mu\nu}$ is mathematically identical to what we have 
in Skyrme theory in (\ref{sfeq}).
This tells that the potential $C_\mu$ for the two-form $N_{\mu\nu}$
in (\ref{sfeq}) is given by (up to a gauge transformation)
\bea
C_\mu = 2g \tilde A_\mu = -2i \xi^\dag \pro_\mu \xi. 
\label{cm}
\eea
More importantly, with (\ref{id}) the Hamiltonian (\ref{becham1}) 
can be expressed as
\bea
&{\cal H} = \dfrac{1}{2} (\pro_i \rho)^2
+ \dfrac{\rho^2}{8} (\pro_i \hn)^2 
+ \dfrac{\lambda}{8}(\rho^2-\rho^2_0)^2 \nn\\
&+ \dfrac{1}{16 g^2} (\pro_i \hn \times \pro_j \hn)^2.
\eea
So the theory becomes very similar to Skyrme-Faddeev
theory, which strongly indicates that 
the gauge theory of two-component BEC can allow a knot.
As importantly this strongly implies that the Skyrme-Faddeev theory 
could play an important role in condensed matter
physics.

To simplify the equation (\ref{beckeq1}) notice that 
from (\ref{am}) and (\ref{hn}) we have
\bea
\pro_\mu \xi = (ig \tilde A_\mu + \dfrac{1}{2} \vec \sigma
\cdot \pro_\mu \n) \xi.
\eea
With the identity the second equation of (\ref{beckeq1}) is reduced to 
\bea
&(A + \B \cdot \vec \sigma) \xi = 0, \nn\\
&A = (\pro_i \n)^2, \nn \\
&\B = \pro^2 \n + 2 \dfrac{\pro_i \rho}{\rho} \pro_i \n
- \dfrac{i}{2 g^2 \rho^2} \pro_i N_{ij} \pro_j \n, 
\eea
which can be written as
\bea
&A+ \vec B \cdot \hn=0, \nn\\
& \hn \times \vec B - i \hn \times (\hn \times \vec B) =0,
\eea
or 
\bea
\n \times (\pro^2 \n + 2 \dfrac{\pro_i \rho}{\rho} \pro_i \n) 
+ \dfrac{1}{2 g^2 \rho^2} \pro_i N_{ij} \pro_j \n = 0.
\eea
So we can put (\ref{beckeq1}) into the form
\bea
&\pro^2 \rho - \dfrac{1}{4} (\pro_i \n)^2 \rho 
= \dfrac{\lambda}{2}(\rho^2 - \rho_0^2)
\rho, \nn \\
&\n \times \pro^2 \n + 2 \dfrac{\pro_i \rho}{\rho} \n \times \pro_i
\n + \dfrac{1}{g^2\rho^2} \pro_i N_{ij} \pro_j \n = 0.
\label{beckeq2}
\eea
This is the equation of two-component BEC that we are 
looking for. The similarity between this and the equation 
(\ref{sfeq}) of Skyrme-Faddeev theory is unmistakable.

Notice that the target space of $\xi$ and $\n$ is $S^3$ and
$S^2$, but here we have transformed the equation for $\xi$
in (\ref{beckeq1}) completely into the equation
for $\n$ in (\ref{beckeq2}).
This is made possible because, with the Abelian gauge invariance of (6),
the physical target space of $\xi$ becomes the gauge orbit space
$S^2 = S^3/S^1$ which forms a $CP^1$ space.
This means that we can view the theory as a self interacting
$CP^1$ theory (coupled to a scalar field $\rho$), and replace
$\xi$ completely in terms of $\n$.

To show that the theory has a knot solution we construct 
a helical vortex solution first. To do this 
we choose the ansatz
\bea
&\rho= \rho(\varrho), 
~~~~~\xi = \Bigg( \matrix{\cos \dfrac{f(\varrho)}{2}
\exp (-in\varphi) \cr
\sin \dfrac{f(\varrho)}{2} \exp (imkz)} \Bigg), \nn\\
&\n= \xi^\dag \vec \sigma \xi
= \Bigg(\matrix{\sin{f(\varrho)}\cos{(mkz+n\varphi)} \cr
\sin{f(\varrho)}\sin{(mkz+n\varphi)} \cr \cos{f(\varrho)}}\Bigg). \nn\\
\label{bhvans}
\eea
With this (\ref{beckeq2}) is reduced to
\bea
&\ddot{\rho}+\dfrac{1}{\varrho}\dot\rho
- \dfrac{1}{4}\Big(\dot{f}^2+(m^2 k^2+\dfrac{n^2}{\varrho^2})
\sin^2{f}\Big)\rho \nn\\
&= \dfrac{\lambda}{2}(\rho^2-\rho_0^2)\rho, \nn\\
&\Big(1+(m^2 k^2+\dfrac{n^2}{\varrho^2})
\dfrac{\sin^2{f}}{g^2 \rho^2}\Big) \ddot{f}
+ \Big( \dfrac{1}{\varrho}+ 2\dfrac{\dot{\rho}}{\rho} \nn\\
&+(m^2 k^2+\dfrac{n^2}{\varrho^2})
\dfrac{\sin{f}\cos{f}}{g^2 \rho^2} \dot{f}
+ \dfrac{1}{\varrho} (m^2 k^2-\dfrac{n^2}{\varrho^2})
\dfrac{\sin^2{f}}{g^2 \rho^2} \Big) \dot{f} \nn\\
&- (m^2 k^2+\dfrac{n^2}{\varrho^2}) \sin{f}\cos{f}=0.
\label{bveq}
\eea
So with the boundary condition
\bea
&\dot \rho(0)=0,~~~~~\rho(\infty)=\rho_0, \nn\\
&f(0)=\pi,~~~~~f(\infty)=0,
\label{becbc}
\eea
we obtain the non-Abelian vortex solutions shown in Fig.\ref{becheli}.

\begin{figure}[t]
\includegraphics[scale=0.5]{becknot.eps}
\caption{The non-Abelian vortex (dashed line) with $m=0,n=1$ and
the helical vortex (solid line) with $m=n=1$ in the gauge theory
of two-component BEC. Here we have put $\lambda/g^2=1$,
$k=0.64~{\sqrt \lambda}\rho_0$, and $\varrho$ is in the unit of
$1/{\sqrt \lambda}\rho_0$.}
\label{becheli}
\end{figure}

There are three points that have to be
emphasized here. First, when $m=0$, the solution describes
the untwisted non-Abelian vortex \cite{bec1}. But when $m$ is not zero,
it describes a helical vortex which is periodic in $z$-coodinate.
In this case, the vortex has a non-vanishing velocity current
(not only around the vortex but also) along the $z$-axis.
Secondly, the doublet $\phi$ starts from
the second component at the core,
but the first component takes over completely at the infinity.
This is due to the boundary condition $f(0)=\pi$ and $f(\infty)=0$,
which assures that our solution describes a genuine
non-Abelian vortex. Thirdly, when $f=0$ (or $f=\pi$)
the doublet effectively becomes
a singlet, and (\ref{bveq}) describes the well-known
vortex in single-component BEC. Only when $f$ has a non-trivial
profile, we have a non-Abelian vortex.

In Skyrme theory the helical vortex is interpreted as
a twisted magnetic vortex whose flux is quantized \cite{prl01,plb04}
Now we show that the above vortex is a twisted vorticity flux
which is also quantized.
To see this notice that the non-Abelian structure of
the vortex is represented by the doublet $\xi$.
Moreover, the velocity field 
of the doublet is given by 
\bea
&\tilde A_\mu =-\dfrac{n}{2g}(\cos{f}+1) \pro_\mu \varphi \nn\\
&-\dfrac{mk}{2g}(\cos{f}-1) \pro_\mu z,
\label{gpvel}
\eea
which generates the vorticity
\bea
&H_{\mu\nu}= -\dfrac{i}{g}(\pro_\mu \xi^{\dagger} \pro_\nu \xi
-\pro_\nu \xi^{\dagger} \pro_\mu \xi) \nn\\
&=\dfrac{\dot{f}}{2g} \sin{f}\Big(n(\pro_\mu \varrho \pro_\nu \varphi
-\pro_\nu \varrho \pro_\mu \varphi) \nn\\
&+mk(\pro_\mu \varrho \pro_\nu z
- \pro_\nu \varrho \pro_\mu z) \Big).
\label{gpvor}
\eea
This has two vorticity fluxes, $\phi_{\hat z}$
along the $z$-axis
\bea
&\phi_{\hat z}=\dfrac{}{} \int H_{{\hat \varrho}{\hat \varphi}}
\varrho d \varrho d \varphi
= -\dfrac{2\pi n}{g},
\label{gpfluxz}
\eea
and $\phi_{\hat \varphi}$ around the the $z$-axis (in one
period section from $z=0$ to $z=2\pi/k$)
\bea
&\phi_{\hat \varphi}=\dfrac{}{} \int_{z=0}^{z=2\pi/k}
H_{{\hat z}{\hat \varrho}} d \varrho dz
= \dfrac{2\pi m}{g}.
\label{gpfluxphi}
\eea
This shows that the helical vortex is made of two quantized vorticity
fluxes, the $\phi_{\hat z}$-flux which is concentrated at the core
and the $\phi_{\hat \varphi}$-flux which surrounds it. 
This confirms that the helical vortex is a twisted vorticity
flux which is very similar to the helical vortex in Gross-Pitaevskii 
theory \cite{bec5}.

Now, with the helical vortex, one can easily make a twisted vortex ring
smoothly connecting the periodic ends together. 
And just as in Skyrme theory the twisted vortex ring
becomes a topological knot. But
here it is $\pi_3(S^3)$ of the doublet $\xi$ which provides the
non-trivial quantum number, 
\bea
q = - \dfrac {1}{4\pi^2} \int \epsilon_{ijk} \xi^{\dagger}
\partial_i \xi ( \partial_j \xi^{\dagger}
\partial_k \xi ) d^3 x.
\label{beckqn}
\eea
Of course this is identical to the expression (\ref{kqn}), due to the
Hopf fibering of $S^3$ to $S^2 \times S^1$ \cite{bec5}. This
tells that we can express the knot quantum number either
by $\pi_3(S^3)$ or by $\pi_3(S^2)$. 

Obviously this knot has a topological stability, because 
the knot topology (\ref{kqn}) can not be changed by a smooth 
deformation of the field configuration. Moreover it has 
a dynamical stability. To understand this notice that
the knot has a twisted velocity field so that it has a
non-vanishing velocity around the $z$-axis.
This means that it carries a non-vanishing angular momentum along 
the $z$-axis. And this angular momentum provides 
the dynamical stability, because it creates a centrifugal force that 
prevents the collapse of the knot. Notice that this dynamical 
stability originates from the knot topology, because 
the angular momentum comes from the twisted velocity field. 
In this sense the topological stability and the dynamical stability
have one and the same origin. It is this remarkable 
interplay between topology and dynamics which assures 
the stability of the knot. The nontrivial twisted topology of 
the knot expresses itself in the form of the angular momentum, 
which in turn provides the dynamical stability of the knot. 
This presence of the angular momnetum is 
what differentiates our
knot from the untwisted Abrikosov-type vortex ring 
which has no dynamical stability.  

There have been assertions that two-component BEC admits
a knot \cite{ruo}. But notice that this knot is based on 
Gross-Pitaevskii theory of two-component BEC, which has no
vorticity interaction. In contrast our knot is based on 
the gauge theory in which the vorticity 
interaction plays a crucial role. Nevertheless physically two knots 
are very similar \cite{bec5}. Both can be identified as 
a vorticity knot. This implies that both theories should be 
taken seriously as a theory of two-component BEC.
