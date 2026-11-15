---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-006-43-the-large-r-asymptotics-of-tau-rm-pq
section_title: "The large $r$ asymptotics of $\tau_{r}(M_{p/q})$"
section_number: 4.3
pages: 19-29
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.803
latex_coverage_ratio: 0.982
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent We calculate the leading term of the large $r$
asymptotics of $J_{K}'(r)$, using the saddle point
method like Kashaev \cite{[14]}. Our calculation supplements
the calculation of Kashaev with the required analytic error
estimates. Let
\begin{eqnarray*}
C_{r}^{2} = C(\vep) &=& [\I+\vep,-\I+\vep]
+ [-\I+\vep,1-\vep-\I] \\
&& + [1-\vep-\I,1-\vep+\I] + [1-\vep+\I,\vep+\I],
\end{eqnarray*}
where $\vep \in ]0, \frac{1}{4r}[$. We let $C_{+}(\vep)$ be the
part of the contour $C(\vep)$ above the real axes and
$C_{-}(\vep)$ the part below the real axes. By
(\ref{eq:contourfigure8}) we have
$$
J_{K}'(r) = \frac{\I r^{2}}{2}
\left( J_{+}(r,\vep) + J_{-}(r,\vep) \right),
$$
where
$$
J_{\pm}(r,\vep) =  \int_{C_{\pm}(\vep)} \tan(\pi r x)g_{r}(x)
\dte x.
$$
Away from the real axis, the factor $\tan(\pi r x)$ can be
approximated by $\pm \I$ depending on whether we are in the
upper or lower half-plane. In fact we have
\begin{equation}\label{eq:tan+}
|\tan(\pi r x) - \I| \leq \left\{ \begin{array}{ll}
   4e^{-2\pi r \ima(x)}, & \ima(x) \geq \frac{1}{\pi r}, \\
   2e^{-2\pi r \ima(x)}, & r\rea(x) \in \Z, \ima(x) \geq 0
     \end{array}\right.
\end{equation}
and
\begin{equation}\label{eq:tan-}
|\tan(\pi r x) + \I| \leq \left\{ \begin{array}{ll}
  4e^{2\pi r \ima(x)}, & \ima(x) \leq -\frac{1}{\pi r}, \\
  2e^{2\pi r \ima(x)}, & r\rea(x) \in \Z, \ima(x) \leq 0.
    \end{array}\right.
\end{equation}
Therefore we write
$$
J_\pm(r,\vep) = \pm\I \int_{C_\pm(\vep)}g_r(x) \dte x +
\int_{C_\pm(\vep)}(\tan(\pi r x) \mp \I)g_r(x) \dte x.
$$
The estimates on $\tan(\pi r x)\pm \I$ can be used (see
Appendix B) to prove that
\begin{equation}\label{eq:figure8estimate1}
\left| \sum_{\mu =\pm 1}
    \int_{C_{\mu}(\vep)}(\tan(\pi r x) -\mu \I)g_r(x) \dte
       x\right| \leq K_{1} \frac{1}{r},
\end{equation}
where $K_{1}$ is a constant independent of $r$ and $\vep$.
Let now
\begin{equation}\label{eq:figure8Phase}
\Phi(x) = \frac{1}{2\pi\I}
\left( \Li_{2}(e^{-2\pi\I x}) - \Li_{2}(e^{2\pi\I x})\right).
\end{equation}
Note that $\Phi$ is analytic on
$D=\C \sm \{ \, x \in \C \, |\, \rea(x) \in \Z \,\}$ but not in
the points $\Z$, so here we see the reason for using the small
deformation parameter $\vep$. We have
\begin{eqnarray*}
\int_{C_\pm(\vep)}g_r(x) \dte x &=&
\int_{C_\pm(\vep)} e^{r\Phi(x)} \dte x \\
&& + \int_{C_\pm(\vep)}
\left(\exp\left( I_{\gamma}(\pi-2\pi x)
  - I_{\gamma}(-\pi + 2\pi x)\right) -1 \right)
e^{r\Phi(x)} \dte x.
\end{eqnarray*}
However, as we will see in Appendix B, the estimate in
\reflem{lem:Sapproximation} implies that
\begin{equation}\label{eq:figure8estimate2}
\left| \int_{C_{\mu}(\vep)}
   \left(\exp\left( I_{\gamma}(\pi-2\pi x)
           - I_{\gamma}(-\pi + 2\pi x)\right) -1\right)
   e^{r\Phi(x)} \dte x\right| \leq \frac{K_{2}\Log(r)}{r}
   e^{\frac{r}{2\pi}\Vol (K)}
\end{equation}
for $\mu =\pm 1$, where $K_{2}$ is a constant independent of
$r$ and $\vep$. We will see below that the estimates
(\ref{eq:figure8estimate1}) and (\ref{eq:figure8estimate2})
imply that the leading order large $r$ asymptotics of $J'_K(r)$
is given by
\begin{equation}\label{eq:Asymf8}
J'_K(r) \sim \frac{r^{2}}{2}
  \left( \int_{C_-(\vep)} e^{r\Phi(x)} \dte x
       - \int_{C_+(\vep)} e^{r\Phi(x)} \dte x \right),
\end{equation}
to which we can apply the saddle point method, see e.g.\
\cite[Chap.~5]{[6]}. First we determine the stationary points
of the phase function $\Phi$. On $D$ we have
$$
\Phi'(x) = \Log\left(1-e^{2\pi\I x}\right) +
           \Log\left(1-e^{-2\pi\I x}\right).
$$
If we put $z=e^{2\pi\I x}$, then $\Phi'(x)=0$ implies that
\begin{equation}\label{eq:hyp}
z^{2}-z+1=0.
\end{equation}
The equation (\ref{eq:hyp}) has the solutions
$z_{\pm}=e^{\pm \I\pi/3}$. We have
$1 - z_{\pm} = 1/2 \mp i\sqrt{3}/2$
which both have norm $1$ and are each others conjugate, so
$$
\Log\left(1-z_{+} \right) + \Log\left(1-z_{-}\right) = 0.
$$
We note that $z_{\pm}=e^{\pm2\pi \I \frac{1}{6}}$ correspond to
the $x$--points $\pm 1/6 +\Z$. These points are non-degenerate
critical points. In fact,
$$
\Phi''(x) = 2\pi\I\frac{e^{2\pi\I x} + 1}{e^{2\pi\I x} - 1}
$$
on $D$, so in particular $\Phi''(x_{\pm})=\pm 2\pi \sqrt{3}$
for $x_{\pm} \in \pm 1/6 +\Z$. The imaginary part of $\Phi(x)$
is zero for $x \in \R$ and
$$
\Phi(x) = \frac{1}{2\pi}
\ima \left( \Li_{2}(e^{-2\pi\I x}) - \Li_{2}(e^{2\pi\I x})
\right) = -\frac{1}{\pi}\Cl_{2}(2\pi x),
$$
by (\ref{eq:dilogimacircle}). Let $x_{\pm} \in \pm 1/6 +\Z$.
By (\ref{eq:volume}) we have
$\Cl_{2}(2\pi x_{-})=-\Cl_{2}(2\pi x_{+})
= -\Cl_{2}(\pi/3)=-\Vol(K)/2$, i.e.\
$$
\Phi(x_{\pm}) = \mp \frac{1}{2\pi}\Vol(K).
$$
By Cauchy's theorem we have
$$
\int_{C_-(\vep)} e^{r\Phi(x)} \dte x
          - \int_{C_+(\vep)} e^{r\Phi(x)} \dte x
= 2\int_{C_-(\vep)} e^{r\Phi(x)} \dte x
= -2 \int_{C_+(\vep)} e^{r\Phi(x)} \dte x.
$$
Deform $C_{-}(\vep)$ to $[\vep,1-\vep]$ keeping the end points
fixed. This does not change the integral
$\int_{C_{-}(\vep)} e^{r\Phi(x)} \dte x$. Let $x_{0}=5/6$. By
terminology borrowed from \cite[Sec.~5.4]{[6]} the axis of the
saddle point $x_{0}$ is the real axis (i.e.\ the directions of
steepest descent are along the real axis). From the analysis of
\cite[Sec.~5.7]{[6]} it follows that we can find a $\delta>0$
(independent of $r$ and $\vep$) such that
$[x_{0}-\delta,x_{0}+\delta] \subseteq [1/(4r),1-1/(4r)]$ and
such that we have an asymptotic expansion
$$
\int_{-\delta}^{\delta} e^{r\Phi(x_{0} + t)} \dte t
   \sim \frac{1}{3^{1/4}\sqrt{r}} e^{\frac{r}{2\pi}\Vol(K)}
   \left(1+\sum_{n=1}^{\infty} d_{n} r^{-n} \right)
$$
in the limit $r \ria \infty$, where the $d_{n}$'s are certain
complex numbers. Finally we note that
$$
\left|\int_{\vep}^{x_{0}-\delta} e^{r\Phi(t)}\dte t +
\int_{x_{0}+\delta}^{1-\vep} e^{r\Phi(t)}\dte t \right|
\leq e^{rc},
$$
where
$c = \max \{ -\Cl_{2}(2\pi(x_{0}-\delta))/\pi,
                 -Cl_{2}(2\pi(x_{0}+\delta))/\pi \}
   < \Vol(K)/2\pi$,
see above (\ref{eq:volume}). We have shown


\begin{lemma}\label{volume}
The leading order large $r$ asymptotics of $J_{K}'(r)$ is given
by
\begin{equation}\label{eq:asymptoticsK}
J_{K}'(r) \sim 3^{-1/4} r^{3/2}
       \exp\left(\frac{r}{2\pi}\Vol(K)\right).
\end{equation}
In fact
$$
J_{K}'(r) = 3^{-1/4} r^{3/2}
    \exp\left(\frac{r}{2\pi}\Vol(K)\right)
 + \Os \left( r\Log(r)
         \exp\left(\frac{r}{2\pi}\Vol(K)\right)\right)
$$
in the limit $r \ria \infty$.\HS
\end{lemma}


In particular
$$
\lim_{r \ria \infty} \frac{2\pi\Log(J_{K}'(r))}{r}
= \Vol(K)
$$
as predicted by the volume conjecture of Kashaev \cite{[14]}
and Murakami, Murakami \cite{[24]} and as proven by Ekholm and
others, see \cite{[22]}. However, the arguments of Ekholm and
others can't see the finer details of the asymptotic behaviour
(\ref{eq:asymptoticsK}), namely the polynomial part
$3^{-1/4} r^{3/2}$.


\begin{remark}\label{rem:hyperbolicity}
The complement $S^{3} \sm K$ of the figure $8$ knot can be
decomposed into two ideal hyperbolic tetrahedra each
parametrized by a certain complex number. This decomposition
then defines a hyperbolic  structure on this complement if and
only if a certain set of conditions is satisfied. In fact, if
the complex parameters for the two tetrahedra are respectively
$a$ and $b$, then these conditions are equivalent to $a=b$ and
$b^{2}-b+1=0$, which is equation (\ref{eq:hyp}) after
substituting $b$ for $z$. We refer to \cite[Sec.~3]{[23]} for
more details. This phenomenon, that one finds the hyperbolicity
equation for the knot complement as the equation for the
stationary points of the phase function, seems to be a
general principal for hyperbolic knots as argued by Thurston
and Yokota, cf.\ \cite{[32]}, \cite{[35]}. However, there are
major unsolved analytic difficulties in their approach.
Basically they conjecture that one can carry out an asymptotic
analysis similar to the one we carried out above for the figure
$8$ knot. To prove their conjecture one first has to show how
to give an exact (multi-dimensional) contour integral formula
for the Jones polynomial of a hyperbolic knot like our
(\ref{eq:contourfigure8}). A main part consists of choosing a
correct (multi-dimensional) contour. Secondly, one has to carry
out an asymptotic analysis similar to the one leading to
(\ref{eq:Asymf8}). This analysis is relatively simple for the
figure $8$ knot due to the fact that we have a single
(one-dimensional) contour in this case. In general one gets a
contour of dimension $>1$ and the asymptotic analysis is
expected to be harder (as also illustrated by the asymptotic
analysis of the double-contour integral expression for the
invariant $\bar{\tau}_{r}(M_{p/q})$ in
\reflem{lem:contour}, see next section.)
\end{remark}




\subsection{The large $r$ asymptotics of $\tau_{r}(M_{p/q})$}



\noindent In Sec.~5 we will see that the signs of the phases
in the asymptotics of
$\bar{\tau}_{r}(M_{p/q}) = \overline{\tau_{r}(M_{p/q})}$
agrees with the Chern--Simons values, hence we work with
this conjugate invariant. Because of (\ref{eq:mirror2})
we can always obtain the asymptotic expansion of
$\tau_{r}(M_{p/q})$ by complex conjugation or by replacing
either $p$ by $-p$ or $q$ by $-q$. By \reflem{lem:contour} we
have
\begin{equation}\label{eq:barinvariant}
\bar{\tau}_{r}(M_{p/q}) = \beta_{1}(r) \qsum
  \int_{C_{r}^{1}\times C_r^2} \cot(\pi r x) \tan(\pi ry)
        \bar{f}_{n,r}(x,y) \dte x  \dte y,
\end{equation}
where
\begin{equation}\label{eq:beta1constant}
\beta_{1}(r) = \frac{i\sign(q)r}{4\sqrt{|q|}}
         e^{\frac{3\pi i}{4}\sign(pq)}
         \exp\left(-\frac{\pi i}{2r}\left[3\sign(pq)
      -\frac{p}{q}+\dS\left(\frac{p}{q}\right)\right]\right)
\end{equation}
and
$$
\bar{f}_{n,r}(x,y)=\sin\left(\frac{\pi}{q}(x-2nd)\right)
      e^{2\pi i r \left( -\frac{dn^{2}}{q}-\frac{p}{4q} x^{2}
             + \frac{n}{q}x-xy\right)}
\frac{S_{\gamma}(-\pi+2\pi(x - y))}
     {S_{\gamma}(-\pi+2\pi(x + y))},
$$
where $\gamma=\pi/r$ as usual. Let for $k,l \in \Z$
$$
\Omega_{k,l} = \{ \; (x,y) \in \C^{2} \mid
   \rea(x)+\rea(y) \in [k,k+1],
   \hspace{.1in}\rea(x)-\rea(y) \in [-l,-l+1]\;\}.
$$
For $(x,y)\in \Omega_{k,l}$, we have by (\ref{eq:functional})
and (\ref{eq:Sgdilog}) that
\begin{eqnarray*}
\bar{f}_{n,r}(x,y) &=& \sin\left(\frac{\pi}{q}( x-2nd)\right)
  \left( 1+e^{2\pi i(x-y)r} \right)^{l}
  \left( 1+e^{2\pi i(x+y)r} \right)^{k}
e^{2\pi ir\Phi_{n}(x,y)} \\*
&& \hspace{.2in} \times \exp\left(I_{\gamma}(-\pi+2\pi(x-y+l))
                          -I_{\gamma}(-\pi+2\pi(x+y-k))\right),
\end{eqnarray*}
where
$$
\Phi_{n}(x,y) = -\frac{dn^{2}}{q} - \frac{p}{4q} x^{2}
+ \frac{n}{q}x - xy + \frac{1}{4\pi^{2}}
\left( \Li_{2}(e^{2\pi i(x+y)}) - \Li_{2}(e^{2\pi i (x-y)})
\right).
$$
We note that this expression and the above expression for
$\bar{f}_{n,r}$ are only valid for $(x,y) \in \C^{2}$
satisfying the two conditions
\begin{eqnarray*}
\mbox{\rm (i)}&& \rea(x) + \rea(y) \notin \Z \vee
       \ima(x)+\ima(y) \geq 0, \\*
\mbox{\rm (ii)}&& \rea(x) - \rea(y) \notin \Z \vee
       \ima(x)-\ima(y) \geq 0.
\end{eqnarray*}

Observe that for $k,l \in \{0,1\},$ which corresponds to the
four different $\Omega_{k,l}$ intersecting
$C_r^1\times C_r^2$, we have that
$$
\left( 1+e^{2\pi i(x-y)r} \right)^{l}
\left( 1+e^{2\pi i(x+y)r} \right)^{k}
 = \sum_{(a,b)\in F_{k,l}} e^{2\pi i(a(x+y)+b(x-y))r},
$$
where
$F_{k,l}= \{(a,b)\in \{0,1\}^{2} \mid a \leq k,
\quad b \leq l\}$.
Hence, for such $k,l$ we have
\begin{eqnarray*}
\bar{f}_{n,r}(x,y) &=& \sum_{(a,b)\in F_{k,l}}
           \sin\left(\frac{\pi}{q}( x-2nd)\right)
           e^{2\pi ir\Phi^{a,b}_{n}(x,y)} \\*
&& \times \exp\left(I_{\gamma}(-\pi+2\pi(x-y+l)) -
                    I_{\gamma}(-\pi+2\pi(x+y-k))\right)
\end{eqnarray*}
for $(x,y) \in \Omega_{k,l}$, where
\begin{equation}\label{eq:Phasefunctiontypical}
\Phi_{n}^{a,b}(x,y)= a(x+y) + b(x-y) + \Phi_{n}(x,y).
\end{equation}
Let
$$
\Omega_{k,l}^{\mu,\nu} = \{ (x,y) \in \Omega_{k,l} \mid
\mu \ima(x) \geq 0, \quad \nu \ima(y) \geq 0\}.
$$


\begin{conjecture}\label{conj:mainconj}
There exists surfaces
$\Sigma_{k,l,a,b}^{\mu,\nu,n} \subset \Omega_{k,l}^{\mu,\nu}$
for $(k,l) \in \{0,1\}^{2}$, $(a,b) \in F_{k,l}$,
$(\mu,\nu) \in \{ \pm 1 \}^{2}$ and $n \in \Z / |q|\Z$ such
that the leading order large $r$ asymptotics of the quantum
invariant is given by
\begin{eqnarray}\label{asympconjf}
\bar{\tau}_{r}(M_{p/q}) &\sim&
\frac{i\sign(q)r}{4\sqrt{|q|}}e^{\frac{3\pi i}{4}\sign(pq)}
\qsum \sum_{(k,l) \in \{0,1\}^{2}} \sum_{(a,b)\in F_{k,l}}
\sum_{(\mu,\nu)\in \{\pm 1\}^{2}} \mu\nu \nonumber \\*
&& \times \int_{\Sigma_{k,l,a,b}^{\mu,\nu,n}}
          \sin\left(\frac{\pi}{q}( x-2nd)\right)
          e^{2\pi ir\Phi_{n}^{a,b}(x,y)} \dte x \dte y.
\end{eqnarray}
Moreover, if $p/q \neq 0$ the surfaces
$\Sigma_{k,l,a,b}^{\mu,\nu,n} \subset \Omega_{k,l}^{\mu,\nu}$
can be chosen such that any critical point of $\Phi_{n}^{a,b}$
belonging to $\Sigma_{k,l,a,b}^{\mu,\nu,n}$ also belongs to the
set $\mS$ in (\ref{eq:SUcriticalpoint}).
\end{conjecture}


The rational behind this conjecture is that we anticipate an
analysis of the expression (\ref{eq:barinvariant}) paralleling
our analysis of $J'_K(r)$ should be applicable. I.e.\ $\tan$
and $\cot$ should be approximated by $\pm \I$ depending on the
signs of $\ima(y)$ and $\ima(x)$ and $\bar{f}_{n,r}(x,y)$ by
$\sum_{(a,b) \in F_{k,l}}
\sin\left(\frac{\pi}{q}( x-2nd)\right)
e^{2\pi ir\Phi_{n}^{a,b}(x,y)}$
for some deformation of the part of $C_r^1\times C_r^2$ which
is contained in $\Omega_{k,l}$. We have partial analytic
results supporting this conjecture. The factor in front of the
sum is simply the leading term in the large $r$ asymptotics of
$\beta_{1}(r)$, see (\ref{eq:beta1constant}). In case $p/q = 0$
our results in Appendix C show that we have to include critical
points not belonging to $\mS$ in our surfaces
$\Sigma_{k,l,a,b}^{\mu,\nu,n}$.

In the remaining part of this section we will compute the
large $r$ asymptotics of the right-hand side of
(\ref{asympconjf}). The only task left is to calculate the
leading term in the large $r$ asymptotic of the integrals
\begin{equation}\label{eq:integraltypical}
I = \int_{ \Sigma_{k,l,a,b}^{\mu,\nu,n} }
   \sin\left(\frac{\pi}{q}( x-2nd)\right)
       e^{2\pi ir\Phi_{n}^{a,b}(x,y)} \dte x \dte y,
\end{equation}
where $k,l \in \{0,1\}$, $(a,b) \in F_{k,l}$,
$\mu,\nu \in \{ \pm 1 \}$ and $n \in \Z$. By the properties of
the surfaces $\Sigma_{k,l,a,b}^{\mu,\nu,n}$ postulated in
\refconj{conj:mainconj} this leading asymptotics should be
calculable by the saddle point method. Let us give some
details. Assume that $(x_0,y_0)$ is a critical point of
$\Phi=\Phi_{n}^{a,b}$ belonging to the surface
$\Sigma=\Sigma_{k,l,a,b}^{\mu,\nu,n}$ and assume that
$$
\ima\left( (\Phi(x,y) - \Phi(x_{0},y_{0}))\right) \geq 0
$$
for all $(x,y)$ in a small neighborhood of $(x_0,y_0)$ in
$\Sigma$ with equality only in $(x_0,y_0)$. In this case we say
that $\Sigma$ pass through the critical point $(x_0,y_0)$ in
the directions of steepest descent. Moreover, assume this is
satisfied for all critical points of $\Phi$ inside $\Sigma$.
Then the main contribution to the integral $I$ in the large $r$
limit is given by integrating over small neighborhoods of the
critical points in $\Sigma$.

Let us therefore begin by computing the stationary points of
$\Phi_{n}^{a,b}$. To this end, it is more convenient to work
with the functions
\begin{equation}\label{eq:Phasefunctiontypical1}
\Psi^{a,b}_{n}(x,y) = ax + by + \Phi_{n}(x,y),
\end{equation}
$a,b,n \in \Z$, so $\Phi_{n}^{a,b}=\Psi_{n}^{a+b,a-b}$.

Let $a,b,n \in \Z$ and put $\Psi=\Psi_{n}^{a,b}$. Let
$z=e^{2\pi i x}$ and $w=e^{2\pi iy}$. Then
\begin{eqnarray}\label{eq:critical}
&&2\pi i\frac{\partial \Psi}{\partial x}(x,y)
= 2\pi i(a-y) - \frac{p}{2q} 2\pi i x
+ \frac{2\pi i n}{q} + \Log(1-zw)- \Log(1-zw^{-1}),
\nonumber \\*
&&2\pi i\frac{\partial \Psi}{\partial y}(x,y)
= 2\pi i (b-x)  + \Log(1-zw) + \Log(1-zw^{-1}),
\end{eqnarray}
where we have to assume (which we will also assume in what
follows) that both $zw$ and $zw^{-1}$ are different from $1$.

We will need to specify a certain square root of $z$, namely
let $v=e^{\pi ix}$. Then
$\frac{\partial \Psi}{\partial x}(x,y)=0$ implies that
\begin{equation}\label{eq:stationary1}
v^{-p} = \left(\frac{w-v^{2}}{1-v^{2}w}\right)^{q},
\end{equation}
and
$\frac{\partial \Psi}{\partial y}(x,y) = 0$ implies that
\begin{equation}\label{eq:stationary2}
(1-v^{2}w)(w-v^{2}) = v^{2}w.
\end{equation}
Both equations (\ref{eq:stationary1}) and
(\ref{eq:stationary2}) are independent of $a$, $b$, and $n$.
We note that $(v,w)=(0,0)$ is the only solution to
(\ref{eq:stationary2}) with $v$ or $w$ equal to zero. Note,
moreover, that $(v,w)$ is a common solution to
(\ref{eq:stationary1}) and (\ref{eq:stationary2}) if and only
if $(\bar{v},\bar{w})$ is a common solution to these two
equations. By writing (\ref{eq:stationary1}) as
$$
(-1)^{q}v^{p+2q} =
\left( \frac{1-v^{2}w}{1-v^{-2}w} \right)^{q}
$$
and (\ref{eq:stationary2}) as
$$
(1-v^{2}w)(1-v^{-2}w) = -w
$$
we see that $(v,w)$ is a nonzero solution to
(\ref{eq:stationary1}) and (\ref{eq:stationary2}) if and only
if $(v^{-1},w)$ is such a solution. If $p$ is even, then
$(v,w)$ is a solution to (\ref{eq:stationary1}) and
(\ref{eq:stationary2}) if and only if $(-v,w)$ is such a
solution.

Let us oppositely begin with a common solution
$(v,w) \in \C^{*} \times \C^{*}$ to (\ref{eq:stationary1}) and
(\ref{eq:stationary2}), where, as usual,
$\C^{*} = \C \sm \{0\}$. Write $v = e^{\pi i x}$ and
$w = e^{2\pi iy}$ with $\rea(x) \in ]-1,1]$ and
$\rea(y) \in ]-1/2,1/2]$, i.e.\ $x = \frac{1}{\pi i}\Log(v)$
and $y = \frac{1}{2\pi i}\Log(w)$. One now easily deduce from
(\ref{eq:stationary2}) that there exists a unique $b \in \Z$
such that
\begin{equation}\label{eq:critical2}
0 = 2\pi i (b-x)  + \Log\left(1-e^{2\pi i(x+y)}\right)
                  + \Log\left(1-e^{2\pi i(x-y)}\right),
\end{equation}
and from (\ref{eq:stationary1}) we deduce that there exists a
unique $n \in \Z$ such that
\begin{equation}\label{eq:critical1}
0 = -2\pi iy - \frac{p}{q} \pi i x + \frac{2\pi i n}{q}
    + \Log\left(1-e^{2\pi i(x+y)}\right)
    - \Log\left(1-e^{2\pi i(x-y)}\right).
\end{equation}
That is, there exists a unique pair of integers $b,n$ such
that $(x,y)$ is a stationary point of $\Psi_{n}^{0,b}$.


\begin{remark}
Let us make a slight digression by giving some general remarks
about the set of solutions to (\ref{eq:stationary2}). Assume
that $v,w \in \C^{*}$ and let $z=v^{2}$. Then
(\ref{eq:stationary2}) can be written in the following two
ways
\begin{eqnarray}\label{eq:stationary2no2}
&& z^{2} - \left( w + \frac{1}{w} + 1 \right)z + 1 = 0,
\nonumber \\*
&& w^{2} - \left( z + \frac{1}{z} - 1 \right)w + 1 = 0.
\end{eqnarray}
It is straightforward to see that if $(z,w)$ is a solution to
(\ref{eq:stationary2no2}) with $w \in \R \sm \{0\}$, then
$z$ is real and positive if $w>0$, $z$ is real and negative if
$w \in ]-\infty,-(3+\sqrt{5})/2] \cup [-(3-\sqrt{5})/2,0[$,
and $z \in S^{1}$ if
$$
-(3 + \sqrt{5})/2 \leq  w \leq - (3 - \sqrt{5})/2.
$$
If $(z,w)$ is a solution to (\ref{eq:stationary2no2}) with
$z \in \R \sm \{0\}$, then $w$ is real and negative if $z<0$,
$w$ is real and positive if
$z \in ]0,(3-\sqrt{5})/2] \cup [(3+\sqrt{5})/2,\infty[$,
and $w \in S^{1}$ if $z \in [(3-\sqrt{5})/2,(3+\sqrt{5})/2]$.

Later on we will be particularly interested in common
solutions to (\ref{eq:stationary1}) and (\ref{eq:stationary2})
with $v \in S^{1}$ and $w \in \R \sm \{0\}$. Assume that
$(v,w)$ is such a solution, and write $v=e^{\pi i x}$,
$x \in ]-1,1]$. In that case the 2nd of the equations in
(\ref{eq:stationary2no2}) is
\begin{equation}\label{eq:wrealzcircle}
w^{2} + (1-2\rea(z))w + 1 = 0.
\end{equation}
Since $z \in S^{1}$ we have $1-2\rea(z) \in [-1,3]$ and since
$w$ is real we also have $|1-2\rea(z)| \geq 2$, so
$1-2\rea(z) \in [2,3]$ or $\cos(2\pi x)=\rea(z) \in [-1,-1/2]$.
By (\ref{eq:wrealzcircle}) we find that
\begin{equation}\label{eq:wrealcircle2}
w = w_{\pm}(x) = \cos(2\pi x) - \frac{1}{2} \pm
             \sqrt{\cos^{2}(2\pi x)-\cos(2\pi x)-\frac{3}{4}}.
\end{equation}
If $w>0$ we have already seen that $z \in ]0,\infty[$. But
then $z=1$ so $w^{2} - w + 1 = 0$ by (\ref{eq:stationary2no2})
contradicting the fact that $w$ is real.

Taking absolute values we get from
(\ref{eq:stationary1}) that $|1 - zw|=|w - z|$ and then from
(\ref{eq:stationary2}) that
$|w|=|w-z|^{2}=(w-z)(w-\bar{z})=w^{2}-2\rea(z)w+1$ (still
assuming that $(v,w) \in S^1 \times \R$). Since $w<0$
this equation is equivalent to (\ref{eq:wrealzcircle}). In
other words we have to consider the argument equation following
from (\ref{eq:stationary1}) to obtain information from that
equation not obtainable from (\ref{eq:stationary2}).
\end{remark}


Let us now turn to the second derivative of $\Psi$ in a
critical point $(x_{0},y_{0})$, i.e.\ the Hessian
$H=H(x_{0},y_{0})$ of $\Psi$ in $(x_{0},y_{0})$ (which is
equal to the Hessian of $\Phi_{n}$ in $(x_{0},y_{0})$). Put
$(v_{0},w_{0})=(e^{\pi ix_{0}},e^{2\pi iy_{0}})$ and
$z_{0}=v_{0}^{2}$. By a small computation, using the fact that
$(v_{0},w_{0})$ is a solution to (\ref{eq:stationary2}), we
find that
\begin{eqnarray}\label{eq:Hessian}
H_{11} &=& \frac{\partial^{2}\Psi}{\partial x^{2}}(x_{0},y_{0})
= \frac{1}{w_{0}}-w_{0}-\frac{p}{2q}, \nonumber \\*
H_{12} = H_{21} &=&
\frac{\partial^{2}\Psi}{\partial x\partial y}(x_{0},y_{0})
= z_{0}-\frac{1}{z_{0}}, \nonumber \\*
H_{22} &=& \frac{\partial^{2}\Psi}{\partial y^{2}}(x_{0},y_{0})
= \frac{1}{w_{0}}-w_{0}.
\end{eqnarray}
Let us begin by establishing under which circumstances the
critical point $(x_{0},y_{0})$ is non-degenerate. By
(\ref{eq:Hessian})
$$
\det(H) = \left(w_{0} + \frac{1}{w_{0}}\right)^{2}
        - \left( z_{0}+\frac{1}{z_{0}} \right)^{2}
        + \frac{p}{2q}\left(w_{0} -\frac{1}{w_{0}}\right).
$$
By (\ref{eq:stationary2no2}) we have
$w_{0} + \frac{1}{w_{0}} = z_{0} + \frac{1}{z_{0}} - 1$ so
\begin{equation}\label{eq:detHessian3}
\det(H) = 1 - 2\left( z_{0} + \frac{1}{z_{0}} \right)
          + \frac{p}{2q}\left( w_{0} - \frac{1}{w_{0}} \right).
\end{equation}
If we introduce $y'_0 = iy_0$ we get the formula
\begin{equation}\label{eq:detHessian2}
\det(H) = 1 - 4\cos(2\pi x_0) + \frac{p}{2q} \sinh(2 \pi y_0').
\end{equation}
We are particularly interested in critical points where
$w_{0} < 0$ and $z_{0} \in S^{1}$ (or equivalently
$(x_0,y_0) \in \mS$, see (\ref{eq:SUcriticalpoint})). By
definition of $z_0$ we have
$z_{0} - 1/z_{0} = 2i\sin(2\pi x_0)$ and by (\ref{eq:Hessian})
we then get
\begin{equation}\label{eq:detHessian1}
\det(H) = \left( \frac{1-w_{0}^{2}}{w_{0}}
- \frac{p}{2q} \right)\left( \frac{1-w_{0}^{2}}{w_{0}}\right)
+ 4\sin^{2}(2\pi x_0).
\end{equation}
Thus if $w_{0} \in ]-1,0[$ and
$p/q \geq 0$ or if $w_{0} \in ]-\infty,-1[$ and
$p/q \leq 0$ we have $\det(H)>0$. If $w_{0}=-1$ we
also have $\det(H) >0$ by (\ref{eq:wrealcircle2}).
Since $\rea(y_0) \in \frac{1}{2} + \Z$ we get by
(\ref{eq:detHessian3}) the alternative formula
\begin{equation}\label{eq:detHessian5}
\det(H) = 1 - 4\cos(2\pi x_0)
+ \frac{p}{2q} \sinh\left(2 \pi \ima(y_0)\right).
\end{equation}
Finally we get by (\ref{eq:wrealcircle2}) and
(\ref{eq:detHessian3}) that
\begin{equation}\label{eq:detHessian4}
\det(H) = 1 - 4\cos(2\pi x_0) \pm \frac{p}{q}
\sqrt{\cos^2(2\pi x_0)-\cos(2\pi x_0)-\frac{3}{4}}.
\end{equation}
for $w=w_{\pm}(x_0)$.


\begin{proposition}\label{prop:Nondeg}
Let the situation be as above and assume that $(x_0,y_0)$ is
a critical point of $\Psi$ belonging to the
set $\mS$ in (\ref{eq:SUcriticalpoint}). If $|p/q| < \sqrt{20}$
then $(x_0,y_0)$ is non-degenerate. If $|p/q| > \sqrt{20}$ then
$(x_0,y_0)$ is non-degenerate except if
$$
\rea(z_0) = \cos(2\pi x_0) = \frac{1}{2}
+ \frac{4 - \left| \frac{p}{q} \right|
\sqrt{\frac{p^2}{q^2} - 15}}{\frac{p^2}{q^2} - 16}
$$
and $w_0 = w_+(x_0)$ if $p/q < 0$ and $w_0 = w_-(x_0)$ if
$p/q > 0$.
\end{proposition}


\begin{proof}
Let $z_0=e^{2\pi ix_0}$ and $w_0=e^{2\pi iy_0}$ as above and
put $c=\cos(2\pi x_0)$. Assume that $(x_0,y_0)$ is degenerate,
i.e.\ that $\det(H) = 0$. Then
$$
\left( 16 - \frac{p^2}{q^2} \right) c^{2}
+ \left( \frac{p^2}{q^2} - 8 \right) c
+ 1 + \frac{3}{4}\frac{p^2}{q^2} = 0
$$
by (\ref{eq:detHessian4}). If $p^2/q^2 < 15$ this equation does
not have real solutions, so $p^2/q^2 \geq 15$. If $p^2/q^2=16$
we find that $c=-13/8$ giving a contradiction.
Thus $p^2/q^2 \in [15,16[ \cup ]16,\infty[$ and
\begin{equation}\label{eq:c}
c = \frac{8 - \frac{p^2}{q^2} \pm 2\left| \frac{p}{q} \right|
                 \sqrt{ \frac{p^2}{q^2} - 15 } }
         {2 \left( 16 - \frac{p^2}{q^2} \right)}.
\end{equation}
By this and $c \in [-1,-1/2]$, see below
(\ref{eq:wrealzcircle}), we get that
\begin{equation}\label{eq:inequalities}
\frac{3}{2}\frac{p^2}{q^2} - 20 \leq
\pm \left| \frac{p}{q} \right|\sqrt{\frac{p^2}{q^2} - 15}
\leq \frac{p^2}{q^2} - 12
\end{equation}
for $p^2/q^2 \in [15,16[$ with the opposite inequalities
for $p^2/q^2 \in ]16,\infty[$.
For $p^2/q^2 \in [15,16[$ we have
$\frac{3}{2}\frac{p^2}{q^2} - 20 >0$ so we have a plus in
front of
$\left| \frac{p}{q} \right|\sqrt{\frac{p^2}{q^2} - 15}$
in (\ref{eq:inequalities}) and in that case the first
inequality in (\ref{eq:inequalities}) is equivalent to
\begin{equation}\label{eq:inequalities2}
\frac{5}{4} \left( \frac{p}{q} \right)^{4}
- 45\left( \frac{p}{q} \right)^{2} + 400 \leq 0,
\end{equation}
which forces $p^2/q^2 \in [16,20]$ giving a contradiction.

Therefore $p^2/q^2 >16$ and (\ref{eq:c}) and $c \in [-1,-1/2]$
leads, as already stated, to (\ref{eq:inequalities}) with the
opposite inequalities. Since $p^2/q^2 - 12 >0$ we again have
a plus in front of
$\left| \frac{p}{q} \right|\sqrt{\frac{p^2}{q^2} - 15}$, and
the second inequality is automatically satisfied for all
$p^2/q^2 \geq 16$. This time the first inequality leads to
(\ref{eq:inequalities2}) with the opposite inequalities, so
we can conclude that $p^2/q^2 \geq 20$ and in fact therefore
$|p/q| > \sqrt{20}$. The formula for $\cos(2\pi x_0)$
is just (\ref{eq:c}) with the plus sign in front of
$\left| \frac{p}{q} \right|\sqrt{ \frac{p^2}{q^2} - 15 }$.
\end{proof}


We note that the only other solutions
$(z,w) \in S^{1} \times ]-\infty,0[$ to (\ref{eq:wrealzcircle})
satisfying that $\rea(z)$ is equal to the right-hand side
of (\ref{eq:c}) are $(z_{0},1/w_{0})$, $(\bar{z_{0}},w_{0})$
and $(\bar{z_{0}},1/w_{0})$. By the remarks following
(\ref{eq:detHessian1}) we get that among these three points
only the point $(\bar{z_{0}},w_{0})$ can actually satisfy, that
the right-hand side of (\ref{eq:detHessian1}) is zero.
We conjecture that also in the case $|p/q|>\sqrt{20}$ all
critical points of $\Psi$ which belong to the set $\mS$ are
non-degenerate. To confirm this one has probably to use the
argument equation following from (\ref{eq:stationary1}). By a
direct check we have confirmed this conjecture in
the cases
$|p/q| \in \{14/3,5,16/3,6,20/3,22/3,8,26/3,28/3,10,32/3\}$.

We are now ready to calculate the contribution to the leading
order large $r$ asymptotics of the integral
(\ref{eq:integraltypical}) coming from a critical point $(x,y)$
of the phase function $\Phi_{n}^{a,b}$ belonging to
$\mS \cap \Sigma_{k,l,a,b}^{\mu,\nu,n}$.

The integral $I$ in (\ref{eq:integraltypical}) is a double
contour integral and as such is calcalculated by choosing a
contour for each variable $x$ and $y$. We thus have an
``inner'' integral and an ``outer'' integral and in general the
contour for the inner integral can depend on where we are on
the outer contour. Here we will, however, only consider the
very simple case where these two contours are independent of
each other.

Therefore let $\alpha,\beta \in S^{1}$ and let
$\gamma_{\alpha}, \gamma_{\beta} : I_{\delta} \to \C$ be given
by $\gamma_{\alpha}(s) = x_{0} + \alpha s$,
$\gamma_{\beta}(s) = y_{0}+\beta s$, where
$I_{\delta} = [-\delta,\delta]$ for a sufficiently small
$\delta>0$. According to the saddle point method the main
contributions to the integral (\ref{eq:integraltypical}) comes
from integrating over a small neighborhood of
$\mS \cap \Sigma$ in $\Sigma=\Sigma_{k,l,a,b}^{\mu,\nu,n}$.
We are therefore lead to consider an integral of the form
\begin{eqnarray*}
K(x_{0},y_{0}) &=& \int_{\gamma_{\alpha}}
    \left( \int_{\gamma_{\beta}}
    \sin\left(\frac{\pi}{q}(x-2nd)\right)
    e^{2\pi ir\Psi(x,y)} \dte y \right)\dte x \\*
&=& \alpha\beta\int_{-\delta}^{\delta}
    \left( \int_{-\delta}^{\delta}
    \sin\left(\frac{\pi}{q}(x_{0}+\alpha s-2nd)\right)
    e^{2\pi ir\Psi(x_{0}+\alpha s,y_{0}+\beta t)}
    \dte t \right)\dte s,
\end{eqnarray*}
where $\Psi=\Psi_{n}^{a,b}$ as above. (If $(x_{0},y_{0})$ is a
non-degenerate critical point on the boundary of $\Sigma$, then
one or both or the integrals $\int_{-\delta}^{\delta}$ should
be replaced by $\int_{0}^{\delta}$ (or $\int_{-\delta}^{0}$)
and the contribution coming from that point in
\refthm{thm:asymptotics} should be multiplied by $\frac{1}{2}$
or $\frac{1}{4}$.) By a Taylor expansion we find that
$$
\Psi(x_{0} + \alpha s,y_{0} + \beta t) = \Psi(x_{0},y_{0})
+ \frac{1}{2}\la A\left(\begin{array}{c} s\\t\end{array}
\right),
\left(\begin{array}{c} s\\t\end{array}\right) \ra + h(s,t),
$$
where $A = \diag(\alpha,\beta) H \diag(\alpha,\beta)$ and
$$
\la \left(\begin{array}{c} x_{1}\\y_{1}\end{array}\right),
    \left(\begin{array}{c} x_{2}\\y_{2}\end{array}\right)\ra
= x_{1}x_{2} + y_{1}y_{2}
$$
for $(x_{1},y_{1}),(x_{2},y_{2}) \in \C^{2}$, and where
$h(s,t)$ is a remainder term being a sum of terms of the
form $c_{m,n}s^{m}t^{n}$, $m,n \in \{0,1,2,\ldots,...\}$,
$m+n \geq 3$, $c_{m,n} \in \C$. We search for $\alpha$ and
$\beta$ such that there exists a $\delta > 0$ satisfying
$$
\rea\left( 2\pi i (\Psi(x_{0} + \alpha s,y_{0} + \beta t)
             - \Psi(x_{0},y_{0}))\right) < 0
$$
for all
$(s,t) \in I_{\delta} \times I_{\delta} \sm \{ (0,0) \}$.
This amounts to finding $\alpha$ and $\beta$ such that
$$
\ima\left(\la A\left(\begin{array}{c} s\\t\end{array}\right),
\left(\begin{array}{c} s\\t\end{array}\right)\ra \right) > 0
$$
for all $(s,t) \in \R^{2} \sm \{ (0,0)\}$. Since
$$
\ima\left(\la A\left(\begin{array}{c} s\\t\end{array}\right),
    \left(\begin{array}{c} s\\t\end{array}\right)\ra \right)
= \la \ima(A) \left(\begin{array}{c} s\\t\end{array}\right),
              \left(\begin{array}{c} s\\t\end{array}\right) \ra
$$
this corresponds to finding $\alpha$ and $\beta$ such that
$\ima(A)$ is positive definite. It is essential for the method
that such $\alpha$ and $\beta$ exist. (If not, the analysis
becomes more difficult since higher order terms in the Taylor
expansion of $\Psi(x_0 +\alpha s,y_0 +\beta t)$ need to be
involved, and it is likely that the analysis can not be carried
through in this case.)
For that reason we make the following definition.


\begin{definition}\label{defi:posdefinite}
A critical point $(x,y)$ of the phase function $\Psi$ is called
positive definite if $(x,y)$ is non-degenerate and there exists
$(\alpha,\beta) \in S^1 \times S^1$ such that $\ima(A)$ is
positive definite, where
$$
A = \diag(\alpha,\beta) H \diag(\alpha,\beta),
$$
where $H$ is the Hessian of $\Psi$ in $(x,y)$.
\end{definition}


Assume that $(x_0,y_0)$ is positive definite and let
$(\alpha,\beta) \in S^1 \times S^1$ such that $\ima(A)$ is
positive definite. Then the main contribution to the integral
$K(x_{0},y_{0})$ in the limit of large $r$ is given by
$$
K_{\main}(x_{0},y_{0}) = \alpha\beta
 \sin\left(\frac{\pi}{q}(x_{0}-2nd)\right)
 e^{2\pi ir\Psi(x_{0},y_{0})} \int_{\R^{2}}
 e^{\pi ir\la A\left(\begin{array}{c} s\\t\end{array}\right),
 \left(\begin{array}{c} s\\t\end{array}\right)\ra}
 \dte s \dte t,
$$
and this integral can be evaluated using the results of
\cite[Sec.~3.4]{[12]}. In fact,
$$
\int_{\R^{2}} e^{\pi ir\la A
\left(\begin{array}{c} s\\t\end{array}\right),
\left(\begin{array}{c} s\\t\end{array}\right)\ra} \dte s \dte t
= \frac{1}{r} \left(\det(-iA)\right)^{-1/2},
$$
where $A$ is independent of $r$. Note here that the set $S$ of
complex symmetric $2 \times 2$--matrices $B$ with $\rea(B)$
positive definite is an open convex set in the $3$--dimensional
complex vector space of symmetric $2 \times 2$--matrices. It
follows that their is a unique analytic branch of
$B \mapsto \left( \det(B) \right)^{1/2}$ on $S$ such that
$\left( \det(B) \right)^{1/2} >0$ for $B$ real. We have used
that branch in the above result.
We note that $\det(-iA)=-(\alpha\beta)^2\det(H)$.
In conclusion we can state the
following result.


\begin{theorem}\label{thm:asymptotics}
Let $\mS_{k,l,a,b}^{\mu,\nu,n}$ be the set of critical points
of $\Phi_n^{a,b}$ in $\Sigma_{k,l,a,b}^{\mu,\nu,n}$. IF
\refconj{conj:mainconj} is true and if all the critical points
of $\Phi_n^{a,b}$ in $\Sigma_{k,l,a,b}^{\mu,\nu,n}$ are
positive definite, $k,l =0,1$, $(a,b) \in F_{k,l}$,
$\mu,\nu \in \{\pm 1 \}$, $n \in \Z/|q|\Z$, then the leading
order large $r$ asymptotics of the quantum invariant is given
by
\begin{eqnarray*}
\bar{\tau}_{r}(M_{p/q}) &\sim&
\frac{i\sign(q)}{4\sqrt{|q|}} e^{\frac{3\pi i}{4}\sign(pq)}
\qsum \sum_{(k,l)\in \{0,1\}^{2}} \sum_{(a,b)\in F_{k,l}}
\sum_{(\mu,\nu)\in \{\pm 1\}^{2}} \mu\nu \\
&& \times
\sum_{(x,y) \in \mS_{k,l,a,b}^{\mu,\nu,n}}
\left( -\det(H_{(x,y)}\Phi_{n}^{a,b})\right)^{-1/2} \\
&& \times \sin\left(\frac{\pi}{q}( x-2nd)\right)
         e^{2\pi ir\Phi_{n}^{a,b}(x,y)},
\end{eqnarray*}
where $H_{(x,y)}\Phi_{n}^{a,b}$ is the Hessian of
$\Phi_{n}^{a,b}$ in $(x,y)$.
\end{theorem}


According to the above theorem the growth rate of the quantum
invariants of $M_{p/q}$ is $r^{0}$ if we can prove that the
values of the phase functions $\Phi_n^{a,b}$ in the points
$S_{k,l,a,b}^{\mu,\nu,n}$ are real. This we do in Sec.~5.3,
see \refcor{cor:imaPsi}. This is in agreement with our computer
studies of the quantum invariants of $M_{p/q}$. To obtain
\refthm{thm:MT} from \refthm{thm:asymptotics}, hence a leading
asymptotics as predicted by the AEC, we have to prove i) that
the union of the sets of critical points
$\mS_{k,l,a,b}^{\mu,\nu,n}$ corresponds to the flat
(irreducible) $\SU(2)$--connections on $M_{p/q}$ and ii) that
the values of the relevant phase functions $\Phi_{n}^{a,b}$ in
these critical points are equal to the Chern--Simons invariants
of these flat connections. This we also do in Sec.~5.3. Note
that we have used the expression (\ref{eq:detHessian5}) for the
determinant of the Hessian $H_{(x,y)}\Phi_{n}^{a,b}$ in
\refthm{thm:MT}.


\begin{remark}\label{rem:Remark4}
The manifolds $M_{p/q}$, $|p/q| \in \{1,2,3\}$, are Seifert
manifolds and by \cite{[10]} (\ref{eq:asympqi}) holds for
these manifolds if we put $m_{\bar \rho}=4$ for all
$\bar \rho \in \mM_{p/q}'$.
Moreover, the results in
Appendix C show that the part of the leading order large $r$
asymptotics of $\tau_r(M_0)$ associated to the irreducible
$\SU(2)$--connections on $M_0$ is equal to the right-hand side
of (\ref{eq:asympqi}) if we put $m_{\bar \rho}=4$ for both
points $\bar \rho$ in $\mM_{0}'$. We actually expect that
$m_{\bar \rho}=4$ for all $\bar \rho \in \mM_{p/q}'$ for all
rational $p/q$. Recall here that when we calculated the leading
order large $r$ asymptotics of $J_{K}'(r)$ in Sec.~4.2 we had
to part the contour $C(\vep)$ into two parts $C_{\pm}(\vep)$
because of the tangent factor in the contour integral
(\ref{eq:contourfigure8}). The relevant stationary point was in
that case on the real axes, namely it was $x_0=5/6$, and to
obtain a contour passing through that point we had to deform
$C_{-}(\vep)$ to $[\vep,1-\vep]$ and $C_{+}(\vep)$ to
$[1-\vep,\vep]$. In that way the stationary point $x_0$
gave two equal contributions. (In fact we used Cauchy's
theorem so that we only had to work with either $C_{-}(\vep)$
or $C_{+}(\vep)$, but that of course also produced the factor
$2$.) In the case with the quantum invariants
$\bar \tau _r(M_{p/q})$ we expect a similar phenomenon with
the difference that each relevant stationary point contribute
with $4$ instead of $2$ equal contributions.
We expect that the relevant critical points $(x,y)$
belong to $[1/3,2/3] \times \{ y \in \C | \rea(y)=1/2\}$.
Because of the cotangent and tangent factors we had to
separate our double contour integral expression
for $\bar \tau _r(M_{p/q})$ in (\ref{eq:barinvariant}) into $4$
parts causing the sum
$\sum_{(\mu,\nu) \in \{\pm 1\}^2} \mu\nu$
in the asymptotic formula for $\bar{\tau}_r(M_{p/q})$. The
contour $C_{r}^1$ was thus separated into the part with
$\ima(x) \leq 0$ and the part with $\ima(x) \geq 0$. The first
of these parts can be deformed to $[0,1]$ while the second can
be deformed to $[1,0]$. The contour $C_{r}^2$ was separated
into the part with $\ima(y) \geq 0$ and the part with
$\ima(y) \leq 0$. Both
parts can be deformed to a contour containing the part of the
line $\rea(y)=1/2$ containing the $y$'s in the relevant
stationary points. In this way we obtain as claimed that each
relevant critical point contribute $4$ times. Like in the case
of the the knot invariant $J_{K}'(r)$ we find that the signs
$\mu$ and $\nu$ are cancelled by taking care of the
orientations of the different involved contours.
\end{remark}


Let us end this section by examine to what extend the critical
points $S_{k,l,a,b}^{\mu,\nu,n}$ are positive definite, see
\refdefi{defi:posdefinite}. Since $A$ is symmetric we have
$\ima(A)_{ij}=\ima(A_{ij})$.
Here
\begin{eqnarray*}
A_{11} &=& \alpha^{2}H_{11}, \\
A_{12} = A_{21} &=& \alpha\beta H_{12}, \\
A_{22} &=& \beta^{2}H_{22},
\end{eqnarray*}
where $H$ is the Hessian in (\ref{eq:Hessian}).
We have $z_0=e^{2\pi ix_0}$ and therefore
$H_{12}=H_{21}=2i\sin(2\pi x_0)$. Moreover,
$w_0 \in \{w_{\pm}(x_0)\}$ using notation from
(\ref{eq:wrealcircle2}) and $H_{11}=H_{22}-\frac{p}{2q}$, where
$$
H_{22}=\frac{1}{w_{\pm}(x_0)} - w_{\pm}(x_0) = \mp
2\sqrt{\cos^2(2\pi x_0) - \cos(2\pi x_0) - \frac{3}{4}}.
$$
If
$M=\left( \begin{array}{cc} a & c \\ c & b \end{array}\right)$
is a real symmetric matrix, then $M$ has real eigenvalues, and
$M$ is positive definite if and only if both of these
eigenvalues are positive, i.e.\ if and only if $a$ and $b$ are
both positive and $ab>c^{2}$. Now assume that $M=\ima(A)$.
Since $\rea(z_0) \in [-1,-1/2]$ we have that $H_{12}$ is zero
if and only if $z_0=-1$. In that case $H_{22} = \mp \sqrt{5}$
which is irrational. Therefore $H_{11} \neq 0$ and we can
always choose $\alpha$ and $\beta$ so $a>0$ and $b>0$ and hence
$ab>0=c^{2}$. Therefore assume in what follows that
$H_{12} \neq 0$. If $H_{11}$ and $H_{22}$ are both positive
(meaning that $w_0=w_{-}(x_0)$) we can let
$\alpha=\beta=e^{i\pi/4}$ giving $a=H_{11}$, $b=H_{22}$ and
$c=0$. If $H_{11}$ and $H_{22}$ are both negative (meaning that
$w_0=w_{+}(x_0)$) then we can let $\alpha=\beta=e^{-i\pi/4}$
giving $a=-H_{11}$, $b=-H_{22}$ and $c=0$.
If $\mu=\sign(H_{11}) \neq \sign(H_{22})$ we can let
$\alpha=e^{\mu i\pi/4}$ and $\beta=e^{-\mu i\pi/4}$ giving
$a=|H_{11}|$, $b=|H_{22}|$ and $c=D$, writing $H_{12}=iD$,
$D \in \R$. Thus $\det(M)=-\det(H)$, so if $\det(H)<0$ this
choice of $\alpha$ and $\beta$ works. The case
$\sign(H_{11}) \neq \sign(H_{22})$ and $\det(H)>0$ is more
problematic, and the above analysis is actually too simplified
as the examples $|p/q| \in \{4/3,10/3,16/3,22/3\}$ show.

One can in an even simpler way see that the above approach
is too simplified, namely by considering the cases where
$H_{11}=0$ or $H_{22}=0$. In that case $a=0$ or $b=0$ so
$\ima(A)$ is not positive definite. We have $H_{22}=0$ if and
only if $\cos(2\pi x_0)=-1/2$ and that case occurs if and only
if $p=6m+3$ for some integer $m$.

Since $\cos(2\pi x_0) \in [-1,-1/2]$ the entry $H_{11}$ can
not be zero if $|p/q|>\sqrt{20}$.
For $|p/q| < \sqrt{20}$, $H_{11}=0$ implies that
$\cos(2\pi x_0) = \frac{1}{2} - \sqrt{1+\frac{p^2}{16q^2}}$.
Finally note that if $H_{11}=H_{22}=0$ then
$p/q=0$, but in that case $H_{22} \neq 0$ for critical points
$(x_0,y_0) \in \mS$, see Appendix C.

The solution to these problems is to let the contour for the
``inner'' integral depend on the contour for the ``outer''
integral. We will not give more details here, but refer to
a later paper. Note that the expression for the matrix $A$ in
\refdefi{defi:posdefinite} in this more general approach is
different from the one stated in that definition.
