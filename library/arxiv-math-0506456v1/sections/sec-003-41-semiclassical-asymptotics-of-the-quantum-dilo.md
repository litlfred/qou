---
doc_id: arxiv-math-0506456v1
doc_title: "arXiv:math/0506456v1 [math.QA] 22 Jun 2005"
section_id: sec-003-41-semiclassical-asymptotics-of-the-quantum-dilo
section_title: "Semiclassical asymptotics of the quantum dilogarithm"
section_number: 4.1
pages: 15-70
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.797
---
\noindent It is well-known that the semiclassical asymptotics,
i.e.\ the small $\gamma$ asymptotics of the quantum dilogarithm
$S_\gamma$, is given by Euler's dilogarithm
\begin{equation}\label{eq:dilog}
\Li_{2}(z) = -\int_{0}^{z} \frac{\Log (1-w)}{w} \dte w
\end{equation}
for $z \in \C \sm ]1,\infty[$. Here and elsewhere $\Log$
denotes the principal logarithm. For $\zeta \in \C$ satisfying
either $\rea(\zeta) = \pm \pi$ and $\ima(\zeta) \geq 0$ or
$|\rea(\zeta)| < \pi$ one can check (see Appendix A) that
$$
\frac{1}{2\I \gamma} \Li _{2} (-e^{\I \zeta} ) =
\frac{1}{4} \int_{C_{R}}
\frac{e^{\zeta z}}{\sinh(\pi z) \gamma z^{2}} \dte z,
$$
hence we have that
\begin{equation}\label{eq:Sgdilog}
S_\gamma(\zeta) = \exp\left( \frac{1}{2\I \gamma}
      \Li _{2} (-e^{\I \zeta} ) + I_\gamma(\zeta)\right)
\end{equation}
for such $\zeta$, where
$$
I_{\gamma}(\zeta) = \frac{1}{4} \int_{C_{R}}
      \frac{e^{\zeta z}}{z\sinh(\pi z)}
      \left( \frac{1}{\sinh(\gamma z)}
              - \frac{1}{\gamma z}\right) \dte z.
$$


\begin{lemma}\label{lem:Sapproximation}
 If $|\rea(\zeta)| < \pi$ then
$$
|I_{\gamma}(\zeta)| \leq A \left( \frac{1}{\pi -\rea(\zeta)}
          + \frac{1}{\pi + \rea(\zeta)} \right) \gamma
          + B\left(1+e^{-\ima(\zeta) R} \right)\gamma,
$$
and for $|\rea(\zeta)| \leq \pi$ we have
$$
|I_{\gamma}(\zeta)| \leq 2A +
          B \left(1+e^{-\ima(\zeta) R} \right)\gamma,
$$
where $A$ and $B$ are positive constants only depending on $R$.
\end{lemma}


A proof is given in Appendix A. On the unit circle the
imaginary part of the dilogarithm is given by Clausen's
function $\Cl_{2}$, i.e.\
\begin{equation}\label{eq:dilogimacircle}
\ima\left( \Li_{2}( e^{i\theta})\right) = \Cl_{2}(\theta)
   = \sum_{n=1}^{\infty} \frac{\sin(n\theta)}{n^{2}}
   = -\int_{0}^{\theta}
         \Log\left|2\sin\left(\frac{t}{2}\right)\right|\dte t
\end{equation}
for $\theta \in \R$. One sees that $\Cl_{2}$ is increasing on
$[0,\pi/3] \cup [5\pi/3,2\pi]$ and decreasing on
$[\pi/3,5\pi/3]$. In particular, $\Cl_{2}$ attains its maximum
value at $\pi/3$ and its minimum value at $5\pi/3$. Moreover
\begin{equation}\label{eq:volume}
-\Cl_{2} \left( \frac{5\pi}{3}\right) =
                    \Cl_{2}\left(\frac{\pi}{3}\right)
  = -2\int_{0}^{\pi/6} \Log|2\sin(\phi)|\dte \phi
  = 2\J \left(\frac{\pi}{6}\right) = \frac{1}{2}\Vol(K),
\end{equation}
where $\J$ is Lobachevsky's function and $\Vol(K)$ is the
hyperbolic volume of the complement of the figure $8$ knot,
see e.g.\ \cite[Sec.~10.4]{[25]}.




\subsection{The large $r$ asymptotics of $J_{K}'(r)$}



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




\section{Classical Chern--Simons theory on $M_{p/q}$}



\noindent In this section we will describe the classical
theory, that is the classical Chern--Simons theory on the
manifolds $M_{p/q}$. The $\SU(2)$ Chern--Simons functional is
a map with values in $\R/\Z$ defined on the set $\mA$ of gauge
equivalence classes of connections in a principal $\SU(2)$
bundle on $M_{p/q}$ (all such bundles being trivializable).
Inside $\mA$ sits the moduli space $\mM_{p/q}$ of flat
$\SU(2)$--connections on $M_{p/q}$, that is the set of
classical solutions to the $\SU(2)$ Chern--Simons field theory.
Recall that
\[\mM_{p/q} = \Hom(\pi_{1}(M_{p/q}),\SU(2))/\SU(2) \]
from which it is clear that  $\mM_{p/q}$ is a compact space.
The Chern--Simons functional is constant on the connected
components of $\mM_{p/q}$, thus there are only finitely many
different values on flat connections. Let $\mM_{p/q}'$ be the
subset of $\mM_{p/q}$ consisting of nonabelian representations.
Recall that these representations correspond to the irreducible
connections, while the abelian representations correspond to
the reducible connections.

The main results in this section are \refthm{thm:comparison}
and \refthm{thm:main} which tie up the Chern--Simons theory
to the large $r$ asymptotics of $\bar{\tau}_{r}(M_{p/q})$ by
showing that a certain subset of the critical points of the
phase functions $\Phi_{n}^{a,b}$ corresponds to $\mM_{p/q}'$.
Under this correspondence, the Chern--Simons functional is
taken to the phase functions $\Phi_{n}^{a,b}$.

We begin by giving a description of $\mM_{p/q}$ following
Riley \cite{[28]}, \cite{[29]} and Kirk \& Klassen \cite{[18]}.




\subsection{The moduli space of flat $\SU(2)$--connections on
$M_{p/q}$}



\noindent In the following
$\pi=\pi_{1}\left( S^{3} \sm \nbd (K) \right)$ denotes the knot
group of the figure $8$ knot. We have a presentation
\begin{equation}\label{eq:pi}
\pi = \la \, x,y\, | wx=yw \,\ra,
\end{equation}
where $w=[x^{-1},y]$, and where $\mu=x$ and
$\lambda=yx^{-1}y^{-1}x^{2}y^{-1}x^{-1}y$ are the elements of
$\pi$ corresponding to the meridian and the preferred longitude
of $K$. The $\SL(2,\C)$ representation variety of $\pi$ was
analyzed by Riley \cite{[28]}, \cite{[29]} relevant to our
work. Consider a group $G$ given by a presentation
$$
G = \la \, x,y\, | wx=yw \,\ra,
$$
where
$w=x^{\vep_{1}}y^{\vep_{2}}x^{\vep_{3}}\cdots
y^{\vep_{\alpha-1}}$,
where $\alpha$ is odd and $\vep_{j} = \vep_{\alpha-j} = \pm 1$,
$j=1,2,\ldots,\alpha-1$. Such groups are denoted $2$--bridge
kmot groups by Riley since they generalize the $2$--bridge knot
groups. Following Riley we say that a representation
$\psi : G \to \SL(2,\C)$ is affine when the image of $\psi$
fixes exactly one point in $\C\Pro^{1}$ and not affine when
this image has no fixed points. We note that if $\psi$ is
nonabelian then $\psi$ is affine if and only if $\psi(x)$
and $\psi(y)$ have a common eigenvector, and $\psi$ is not
affine if these two matrices have no common eigenvector.
Let $H$ be some subgroup of $\SL(2,\C)$. Then we will say
that two representations $\psi_{1},\psi_{2} : G \to \SL(2,\C)$
are $H$--equivalent if they are conjugate to each other by a
matrix in $H$, i.e.\ if there exists a matrix $U \in H$ such
that $\psi_{2}(\gamma)=U\psi_{1}(\gamma)U^{-1}$ for all
$\gamma \in G$. In particular, we will say that $\psi_{1}$ and
$\psi_{2}$ are equivalent if they are  $\SL(2,\C)$--equivalent.
For $(t,u) \in \C^{*} \times \C$ we put
\begin{eqnarray*}
C_{0}(t) &=& \left( \begin{array}{cc} t & 1 \\
                0 & 1 \end{array}\right), \hspace{.2in}
D_{0}(t,u) = \left( \begin{array}{cc} t & 0 \\
                         -tu & 1 \end{array}\right), \\
C_{1}(t) &=& \left( \begin{array}{cc} t & 1 \\
                0 & t^{-1} \end{array}\right), \hspace{.2in}
D_{1}(t,u) = \left( \begin{array}{cc} t & 0 \\
                     -u & t^{-1} \end{array}\right), \\
C_{2}(t) &=& \left( \begin{array}{cc} t & t^{-1} \\
                0 & t^{-1} \end{array}\right), \hspace{.2in}
D_{2}(t,u) = \left( \begin{array}{cc} t & 0 \\
                     -tu & t^{-1} \end{array}\right).
\end{eqnarray*}
We note that $C_{\nu}(t)$ and $D_{\nu}(t,u)$ are elements of
$\SL(2,\C)$, $\nu=1,2$. If $s$ is a square root of $t$ and
$V(s)=\diag(s,s^{-1})$ then
\begin{equation}\label{eq:konjugering}
V(s)C_{2}(t)V(s)^{-1} = C_{1}(t), \hspace{.2in}
V(s)D_{2}(t,u)V(s)^{-1} = D_{1}(t,u),
\end{equation}
and
\begin{equation}\label{eq:C0C2}
C_{0}(t) = sC_{2}(s), \hspace{.2in} D_{0}(t,u) = sD_{2}(s,u).
\end{equation}
Let $W_{\nu}(t,u)$ denote the matrix obtained by replacing
$x$ and $y$ by respectively $C_{\nu}(t)$ and $D_{\nu}(t,u)$
in the expression for $w$, and let
$$
\phi(t,u) = W_{11} + (1-t)W_{12},
$$
where $W=W(t,u)=W_{0}(t,u)$. We let $\rho_{(t,u)}$ be the
assignment $x \mapsto C_{2}(t)$, $y \mapsto D_{2}(t,u)$. We
have the following $\SL(2,\C)$ version of
\cite[Theorem 1]{[28]}.


\begin{theorem}\label{thm:SL(2,C)}
Let $(s,u) \in \C^{*} \times \C$. None of the assignments
$\rho_{(s,u)}$ extend to an abelian
$\SL(2,\C)$--representation of $G$. The assignment
$\rho_{(s,u)}$ extends to a nonabelian representation
$\rho_{(s,u)} : G \to \SL(2,\C)$ if and only if
\begin{equation}\label{eq:phizero}
\phi(s^{2},u) = 0.
\end{equation}
Conversely, if $\psi : G \to \SL(2,\C)$ is a nonabelian
representation, then there exists a pair
$(s,u) \in \C^{*} \times \C$ satisfying
(\ref{eq:phizero}) such that $\psi$ and $\rho_{(s,u)}$
are equivalent. When $\psi$ is affine this pair is unique,
and when $\psi$ is not affine the pair $(s,u)$ can only be
replaced by $(s^{-1},u)$.
\end{theorem}


\begin{proof}
The theorem follows by results of \cite{[28]}, \cite{[29]}.
The assignment $\rho_{(s,u)}$ extends to a
$\SL(2,\C)$--representation of $G$ if and only if
$W_{2}(s,u)C_{2}(s,u) = D_{2}(s,u)W_{2}(s,u)$.
The matrices $C_{2}(s)$ and $D_{2}(s,u)$ commute if and only
if $s = \pm 1$ and $u=0$, and since $C_{2}(\pm 1)=\pm C_{2}(1)$
is different from $D_{2}(\pm 1,0)=\pm D_{2}(1,0)$ we have that
the assignment $\rho_{(\pm 1,0)}$ does not extend to a
$\SL(2,\C)$--representation of $G$. (We note that if $W=W(1,0)$
then $W_{21}=0$ since the matrices $C_{0}(1), D_{0}(1,0)=I$ and
their inverses are upper triangular. But we also have that
$\phi(1,0)=0$ would imply that $W_{11}=0$ contradicting the
fact that $W$ is invertible. Therefore $\phi(1,0) \neq 0$.)

Let $\sigma=\sum_{j=1}^{\alpha-1} \vep_{j}$. Then
$s^{\sigma}W_{2}(s,u)=W(s^{2},u)$. By (the proof of)
\cite[Theorem 1]{[28]} we have
$W(s^{2},u)C_{0}(s^{2}) = D_{0}(s^{2},u)W(s^{2},u)$
if and only if $\phi(s^{2},u)=0$, so by (\ref{eq:C0C2}) we
find that $\rho_{(s,u)}$ extends to a (necessarily nonabelian)
$\SL(2,\C)$--representation of $G$ if and only if
$\phi(s^{2},u)=0$.

If $\psi : G \to \SL(2,\C)$ is an arbitrary nonabelian
representation it follows by \cite[Lemma 7]{[29]} and
(\ref{eq:konjugering}) that there exists a pair
$(s,u) \in \C^{*} \times \C$ (necessarily satisfying
(\ref{eq:phizero})) such that $\psi$ and $\rho_{(s,u)}$
are equivalent. By the above any such pair is different from
$(\pm 1,0)$ and by \cite[Lemma 8]{[29]} and
(\ref{eq:konjugering}) we then get the final statement of
the theorem.
\end{proof}


If $(s,u) \in \C^{*} \times \C$ with $\phi(s^{2},u)=0$ then
$\rho_{(s,u)}$ is affine if and only if $C_{2}(s)$ and
$D_{2}(s,u)$ have a common eigenvector. But this happens
exactly when $u=0$ or $u=(s-s^{-1})^{2}$.

Let us now restrict to the case where $G$ is the figure $8$
knot group $\pi$. Then
\begin{equation}\label{eq:phifunction}
\phi(t,u)=u^{2}+\left(3-(t+t^{-1})\right)(u+1)
\end{equation}
so in particular $\phi(s^{2},0)=3-s^{2}-s^{-2}=0$ if and only
if $s^{4}-3s^{2}+1=0$ i.e.\ if and only if
$s=\mu_{1}\sqrt{(3+\mu_{2}\sqrt{5})/2}$ for some
$\mu_{1},\mu_{2} \in \{ \pm 1 \}$. If
$u=(s-s^{-1})^{2}=s^{2}+s^{-2}-2$ then
$\phi(s^{2},u) = u^{2} + (3-u-2)(u+1) = u^{2} + 1 - u^{2} = 1$,
so we conclude that $\rho_{(s,u)}$ is affine if and only if
$u=0$ and $s^{4}-3s^{2}+1=0$. Let
$$
\mN = \Hom(\pi,\SL(2,\C))/\SL(2,\C)
$$
be the space of conjugacy classes of
$\SL(2,\C)$--representations of $\pi$ and let $\mN_{\nab}$ be
the subset consisting of classes represented by nonabelian
$\SL(2,\C)$--representations. Moreover, let
\begin{equation}\label{eq:Ntilde}
\tilde{\mN} = \{\, (s,u) \in
        \C^{*} \times \C \, | \, \phi(s^{2},u)=0 \,\},
\end{equation}
and let $\Phi : \tilde{\mN} \to \mN$ be the map which maps
$(s,u)$ to the class represented by $\rho_{(s,u)}$. We have
shown


\begin{corollary}\label{cor:SL(2,C)}
The image of $\Phi$ is $\mN_{\nab}$. If we let
$$
\tilde{\mN}_{0} = \{ \,(\mu_{1}\sqrt{(3+\mu_{2}\sqrt{5})/2},0)
         \,|\,\mu_{1},\mu_{2} \in \{\pm 1\}\,\}
$$
then $\Phi|_{\tilde{\mN}_{0}} : \tilde{\mN}_{0} \to \mN$ is
injective and $\Phi^{-1}(\Phi(s,u))=\{(s,u),(s^{-1},u)\}$
for any $(s,u) \in \tilde{\mN} \sm \tilde{\mN}_{0}$.\HS
\end{corollary}


Recall that $M_{p/q}$ denotes the closed oriented $3$--manifold
obtained by surgery on $S^{3}$ along the figure $8$ knot with
rational surgery coefficient $p/q$. The representation
$\rho_{(s,u)}$, $(s,u) \in \tilde{\mN}$, extends to a
$\SL(2,\C)$--representation of $\pi_{1}(M_{p/q})$ if and only
if
$$
\rho_{(s,u)}(\mu)^{p}\rho_{(s,u)}(\lambda)^{q} = 1.
$$
To analyze this criterion it is an advantage to diagonalize
$\rho_{(s,u)}(\lambda)$. Assume in the following that
$(s,u) \in \tilde{\mN}$. By a rather long but completely
elementary and straightforward calculation we find that
$$
\rho_{(s,u)}(\lambda) = \left(
  \begin{array}{cc} \lambda_{11}(s,u) & \lambda_{12}(s,u) \\
            0 & \lambda_{11}(s^{-1},u) \end{array} \right),
$$
where
$$
\lambda_{11}(s,u) =
-1 + s^{-2} - 2s^{2} + s^{4} + u(s^{-2}-s^{2})
$$
and $\lambda_{12}(s,u) = 2u(1-u)$ if $s^{2}=1$ and
$$
\lambda_{12}(s,u) = \frac{\lambda_{11}(s,u)
              - \lambda_{11}(s^{-1},u)}{s^{2}-1}
$$
for $s^{2} \neq 1$. We note that
$\lambda_{11}(s^{-1},u) = \lambda_{11}(s,u)^{-1}$.

In general, if
$A = \left(\begin{array}{cc} \alpha & \beta \\
       0 & \alpha^{-1} \end{array}\right) \in \SL(2,\C)$,
then $A$ can be diagonalized if and only if $A$ is not
parabolic, i.e.\ if and only if $\tr(A) \neq \pm 2$ or
equivalently if and only if $\alpha \neq \pm 1$ (except, of
course, if $\beta=0$). If $\alpha \neq \pm 1$ then $(1,0)$ is
an eigenvector with eigenvalue $\alpha$ and
$(-\beta/(\alpha-\alpha^{-1}),1)$ is an eigenvector with
eigenvalue $\alpha^{-1}$. If $s^{2}=1$ then
$\lambda_{11}(s,u)=-1$ and $\lambda_{12}(s,u)=\pm i2\sqrt{3}$.
If $s^{2} \neq 1$ then $\lambda_{11}(s,u) = \pm 1$ if and only
if $\lambda_{12}(s,u)=0$. Therefore $\rho_{(s,u)}(\lambda)$ is
diagonalizable (or diagonal) if and only if $s^{2} \neq 1$. In
case $s^{2} \neq 1$ and $\lambda_{12}(s,u) \neq 0$ we have
$$
\frac{\lambda_{12}(s,u)}{\lambda_{11}(s,u)
         -\lambda_{11}(s,u)^{-1}}
= \frac{1}{s^{2}-1} = \frac{s^{-1}}{s-s^{-1}}.
$$
We conclude that if $s^{2} \neq 1$, then $\C^{2}$ has a basis
consisting of a set of common eigenvectors for the matrices
$\rho_{(s,u)}(\mu)$ and $\rho_{(s,u)}(\lambda)$, namely
$u_{1}=(1,0)$ and $u_{2}=(-1/(s^{2}-1),1)$. If we let
$\tilde{\rho}_{(s,u)} : \pi \to \SL(2,\C)$ be the
representation
$\tilde{\rho}_{(s,u)}(\gamma)=U^{-1}\rho_{(s,u)}(\gamma)U$,
where $U \in \SL(2,\C)$ with $j$th column $u_{j}$, we
therefore have
\begin{equation}\label{eq:rhoa1}
\tilde{\rho}_{(s,u)}(x) = \diag\left(s,s^{-1}\right), \qquad
\tilde{\rho}_{(s,u)}(\lambda) =
   \diag\left(\lambda_{11}(s,u),\lambda_{11}(s,u)^{-1}\right).
\end{equation}
In particular, $\rho_{(s,u)} : \pi \to \SL(2,\C)$,
$s^{2} \neq 1$, extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if
\begin{equation}\label{eq:rhosurgery}
s^{-p} = \lambda_{11}(s,u)^{q}.
\end{equation}
Recall here that $\rho_{(s,u)}$ and $\rho_{(s^{-1},u)}$
are equivalent for $(s,u) \in \tilde{\mN} \sm \tilde{\mN}_{0}$,
cf.\ \refcor{cor:SL(2,C)}. But as noted above
$\lambda_{11}(s^{-1},u) = \lambda_{11}(s,u)^{-1}$ in accordance
with (\ref{eq:rhosurgery}). For $(s,u) \in \tilde{\mN}_{0}$
we have $\lambda_{11}(s,u)=1$ and $|s| \neq 1$, so
$\rho_{(s,u)}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if $p=0$.

A direct check shows that if $s^{2}=1$ then $\rho_{(s,u)}$
does not extend to a representation of $\pi_{1}(M_{p/q})$ for
any rational number $p/q$. In fact, if $s = \pm 1$, then
$$
\rho_{(s,u)}(\mu)^{p} = (\pm 1)^{|p|}
  \left(\begin{array}{cc} 1 & p \\ 0 & 1 \end{array}\right)
$$
and
$$
\rho_{(s,u)}(\lambda)^{q} =
       \left(-\left(\begin{array}{cc} 1 & \vep i2\sqrt{3} \\
            0 & 1 \end{array}\right)\right)^{q}
= (-1)^{|q|}\left(\begin{array}{cc} 1 & \vep i2q\sqrt{3} \\
          0 & 1 \end{array}\right)
$$
for a $\vep \in \{-1,1\}$. On the other hand, since
$\lambda_{11}(s,u) = -1$, we have that (\ref{eq:rhosurgery})
is satisfied if $s=1$ and $q$ is even or $s=-1$ and both $p$
and $q$ are odd. For the following we note that if $s^{2}=1$
then $u^{2} + u + 1 = \phi(1,u) = 0$ so $u$ is not real.

We are mostly interested in the $\SU(2)$--representations of
$\pi$. Let in the following $\mM_{\nab}$ be the set of
conjugacy classes of nonabelian $\SU(2)$--representations of
$\pi$.


\begin{proposition}\label{prop:SU(2)}
Let $(s,u) \in \tilde{\mN}$. The representation
$\rho_{(s,u)} : \pi \to \SL(2,\C)$ is $\SL(2,\C)$--equivalent
to a representation  $\pi \to \SU(2)$ if and only if $|s|=1$
and $u$ is real. If we write $s=e^{2\pi i\theta}$,
$\theta \in ]-1/2,1/2]$, then $u \in \{ u_{\pm} \}$, where
$u_{\pm} = u_{\pm}(\theta)$ are the two solutions to
$\phi(e^{4\pi i\theta},u) = 0$, i.e.\
$$
u_{\pm}(\theta) = \cos(4\pi\theta)-\frac{3}{2}
\pm \sqrt{\cos^{2}(4\pi\theta)-\cos(4\pi\theta)-\frac{3}{4}}.
$$
Since $u$ is real we have
$\theta \in [-1/3,-1/6] \cup [1/6,1/3]$.
The representation $\rho_{(e^{2\pi i \theta},u_{\vep})}$,
$\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$\vep \in \{\pm \}$, is $\SL(2,\C)$--equivalent to a
$\SU(2)$--representation $\bar{\rho}_{\theta,\vep}$ which
satisfies
$$
\bar{\rho}_{\theta,\vep}(\mu) = \diag\left(e^{2\pi i \theta},
         e^{-2\pi i\theta}\right),\hspace{.2in}
\bar{\rho}_{\theta,\vep}(\lambda) =
\diag(L_{\vep},L_{\vep}^{-1}),
$$
where $\mu$ and $\lambda$ are the elements of $\pi$
corresponding to the meridian and the preferred longitude of
$K$, and
$$
L_{\pm} = L_{\pm}(\theta) =
   \lambda_{11}\left(e^{2\pi i\theta},u_{\pm}\right)
= - 1 + e^{-4\pi i\theta} - 2e^{4\pi i\theta}
+ e^{8\pi i \theta}
+ u_{\pm}\left(e^{-4\pi i\theta} - e^{4\pi i\theta}\right).
$$
We note that $\bar{\rho}_{-\theta,\vep}$ and
$\bar{\rho}_{\theta,\vep}$ are $\SU(2)$--equivalent. In
particular, the space $\mM_{\nab}$ can be parametrized by the
two arcs
$(e^{2\pi i\theta},u_{+}(\theta))$, $\theta \in [1/6,1/3]$, and
$(e^{2\pi i\theta},u_{-}(\theta))$, $\theta \in [1/6,1/3]$.
These two arcs only coincide at the endpoints, so
topologically $\mM_{\nab}$ is a circle.
\end{proposition}


This proposition follows from \cite[Proposition 4]{[28]}, see
also \cite[Proposition 5.4]{[18]}. For a more geometric
argument determining the topological type of $\mM_{\nab}$,
see \cite{[19]}.

For $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$\vep \in \{\pm\}$, the representation
$\bar{\rho}_{\theta,\vep}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if
$$
\bar{\rho}_{\theta,\vep}(\mu)^{p}
\bar{\rho}_{\theta,\vep}(\lambda)^{q} = 1,
$$
i.e.\ if and only if
\begin{equation}\label{eq:p/q}
e^{-2\pi ip\theta} = L_{\vep}(\theta)^{q}.
\end{equation}
From this (use e.g.\ (\ref{eq:Lreaima})) we see that


\begin{corollary}
Let $p/q \in \Q$ be arbitrary. The moduli space of irreducible
flat $\SU(2)$--connections on $M_{p/q}$ is a finite set.\HS
\end{corollary}


Let us end this section by finding the abelian
$\SU(2)$--representations of $\pi_{1}(M_{p/q})$ (up to
equivalence). Therefore, let $\theta \in ]-1/2,1/2]$
and let $\rho_{\theta}$ be the assignment
$$
\rho_{\theta}(\mu) =
\diag (e^{2\pi i \theta},e^{-2\pi i \theta}).
$$
By (\ref{eq:pi}) this assignment extends to an abelian
$\SU(2)$--representation of $\pi$ for any
$\theta \in ]-1/2,1/2]$ by letting
$\rho_{\theta}(y) = \rho_{\theta}(x)$. Moreover, any abelian
$\SU(2)$--representation of $\pi$ is $\SU(2)$--equivalent to
$\rho_{\theta}$ for some $\theta \in ]-1/2,1/2]$. For any
$\theta \in ]-1/2,1/2]$ we have $\rho_{\theta}(\lambda)=1$, and
$\rho_{\theta}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if $\rho_{\theta}(\mu)^{p} = 1$,
i.e.\ if and only if $p\theta \in \Z$. If
$A = \left(\begin{array}{cc} 0 & -1 \\
1 & 0 \end{array} \right)$
then $A\rho_{\theta}(\mu)A^{-1} = \rho_{-\theta}(\mu)$ so we
can assume that $\theta \in [0,1/2]$. Note, moreover, that two
matrices $\diag (e^{i \phi},e^{-i \phi})$ and
$\diag (e^{i \psi},e^{-i \psi})$, $\phi,\psi \in ]-\pi,\pi]$,
are conjugate in $\SU(2)$ if and only if $\phi=\psi$ or
$\phi =-\psi$. We conclude


\begin{proposition}\label{prop:SU(2)abelian}
For $p \neq 0$ the set of conjugacy classes of abelian
$\SU(2)$--represen-tations of $\pi_{1}(M_{p/q})$ is given by
$$
\left\{ \; [\rho_{j/|p|}] \; \left| \; j=0,1,\ldots,
    \left[\frac{|p|}{2}\right] \; \right. \right\},
$$
where $[|p|/2]$ is the integer part of $|p|/2$. For $p=0$
the set of conjugacy classes of abelian $\SU(2)$--representations
of $\pi_{1}(M_{p/q})$ is given by
$$
\left\{ \; [\rho_{\theta}] \; \left| \; \theta \in
           [0,\frac{1}{2}] \; \right. \right\},
$$
so topologically this set is a closed interval.\HS
\end{proposition}




\subsection{Chern--Simons invariants}



\noindent We begin by recalling formulas from \cite{[18]} for
the Chern--Simons invariants of the flat $\SU(2)$--connections
on $M_{p/q}$. The basic tool will be \refthm{thm:KK} below due
to P.\ A.\ Kirk and E.\ P.\ Klassen.

Let $M$ be a closed oriented $3$--manifold with a knot $K$ in
its interior and let $X$ be the complement of a tubular
neighborhood of $K$ in $M$. Moreover, let $\mu$ be a meridian
of $K$ and $\lambda$ a longitude, both in $\partial X$. Let $G$
be $\SU(2)$ or $\SL(2,\C)$. If $\rho : \pi_{1}(X) \to G$ is a
representation, then $\rho$ extends to a $G$--representation of
$\pi_{1}(M)$ if and only if $\rho(\mu)=1$. Now assume that
$\rho_{t} : \pi_{1}(X) \to G$ is a piecewise smooth path of
representations, $t \in I=[0,1]$. Choose a piecewise smooth
path $g : I \to G$ such that
\begin{eqnarray}\label{eq:pathkonjugering}
g_{t} \rho_{t}(\mu) g_{t}^{-1} &=&
\diag \left( e^{2\pi i \alpha(t)},e^{-2\pi i \alpha(t)}
\right), \nonumber \\*
g_{t} \rho_{t}(\lambda) g_{t}^{-1} &=&
\diag \left( e^{2\pi i \beta(t)},e^{-2\pi i \beta(t)} \right)
\end{eqnarray}
for some piecewise smooth curves $\alpha,\beta$. If $G=\SU(2)$
this is always possible by \cite[Lemma 3.1]{[18]}, and in that
case $\alpha$ and $\beta$ are real-valued. If $G=\SL(2,\C)$ the
above is possible if the path $\rho$ avoids the parabolic
representations (i.e.\ upper triangular with $1$s or $-1$s on
the diagonal), cf.\ \cite[Remark p.~354]{[18]}. (See the text
in connection to (\ref{eq:rhoa1}) for the case of the figure
$8$ knot.) In that case the curves $\alpha$ and $\beta$ are
complex-valued. We then have


\begin{theorem}[ {\cite[Theorem 4.2]{[18]}} ]\label{thm:KK}
Assume that $\rho_{0}(\mu)=\rho_{1}(\mu)=1$. Thinking of
$\rho_{0}$ and $\rho_{1}$ as flat $G$--connections on $M$, we
have
$$
\CS(\rho_{1})-\CS(\rho_{0})
= -2\int_{0}^{1} \beta(t)\alpha'(t) \dte t \pmod{\Z},
$$
where $\CS$ is the Chern--Simons functional associated to
$G$.\HS
\end{theorem}


We note that in case $G=\SL(2,\C)$ the Chern--Simons functional
takes values in $\C/\Z$.

Next consider a knot $K$ in $S^{3}$ and let $X$ be the knot
complement. Let $p/q$ be a rational number and let $N_{p/q}$ be
the closed oriented $3$--manifold obtained by $p/q$ surgery on
$S^{3}$ along $K$. Let $\mu$ and $\lambda$ be classes in
$\pi_{1}(\partial X)$ represented by respectively a meridian
and the preferred longitude of $K$. Choose integers
$c,d \in \Z$ such that $pd-qc=1$. Let $V$ be a tubular
neighborhood of $K$ considered as a subspace of $N_{p/q}$. We
note that $\mu'=p\mu+q\lambda$ and $\lambda'=c\mu+d\lambda$ are
represented by respectively a meridian of $V$ and a longitude
of $V$. Assume that $\rho_t : \pi_{1}(X) \to G$, $t \in I$, is
a piecewise smooth curve of representations from the trivial
representation to a representation, which extends to a
representation of $\pi_{1}(N_{p/q})$, i.e.\ $\rho_1(\mu')=1$.
Assume, moreover, that $\rho_t$ avoids the parabolic
representations in case $G=\SL(2,\C)$, and choose curves
$\alpha,\beta$ as in (\ref{eq:pathkonjugering}) with
$\alpha(0)=\beta(0)=0$. By \refthm{thm:KK} we have
\begin{eqnarray}\label{eq:CSsurgery}
\CS(\rho_1) &=& -2\int_{0}^{1}
(c\alpha(t)+d\beta(t))(p\alpha'(t)+q\beta'(t))\dte t \\*
&=& -2\int_{0}^{1} \beta(t)\alpha'(t)\dte t
    -cp\alpha^{2}(1) - dq\beta^{2}(1) - 2cq\alpha(1)\beta(1)
            \pmod{\Z}.\nonumber
\end{eqnarray}
(We have corrected a sign error in
\cite[Formula (*) p.~361]{[18]}.) We note that this expression
is independent of the choice of $c,d$. The condition
$\rho_1(\mu')=1$ is equivalent to
\begin{equation}\label{eq:p/q1}
p\alpha(1) + q\beta(1) \in \Z.
\end{equation}
Now let $K$ be the figure $8$ knot and let
$\bar{\rho}_{\theta,\vep}$ be a $\SU(2)$--representation of
$\pi_{1}(M_{p/q})$, i.e.\ (\ref{eq:p/q}) is satisfied.
Following \cite{[18]} we determine a formula for
$\CS(\bar{\rho}_{\theta,\vep})$. For later we will here pay
special attention to the branches of the logarithm. By
\refprop{prop:SU(2)} we have
\begin{eqnarray}\label{eq:Lreaima}
\rea\left(L_{-}(\theta)\right) &=&
\rea\left(L_{+}(\theta)\right)
= 2\cos^{2}(4\pi\theta) - \cos(4\pi\theta)-2, \nonumber \\*
\ima\left(L_{\pm}(\theta)\right) &=&
\mp 2\sin(4\pi\theta)\sqrt{\cos^{2}(4\pi\theta)
         - \cos(4\pi\theta) - \frac{3}{4}}
\end{eqnarray}
for all $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$. From these
identities we see that
\begin{equation}\label{eq:Lspecialvalues}
L_{\pm}(1/3) = L_{\pm}(1/6) = -1, \hspace{.2in}
L_{\pm}(1/4) = 1,
\end{equation}
and that $\ima(L_{+})<0$ and $\ima(L_{-})>0$ on $]1/6,1/4[$
with the opposite signs on $]1/4,1/3[$. We conclude that
$L_{+}(\theta)$ and $L_{-}(\theta)$ run through $S^{1}$ both
beginning and ending in $-1$, $L_{+}$ in the anti-clockwise and
$L_{-}$ in the clockwise direction, as $\theta$ runs through
$[1/6,1/3]$. We can therefore use the principal logarithm
$\Log$ to define continuous curves
$\beta_{\pm} : [1/6,1/3] \to \R$ by
\begin{equation}\label{eq:beta}
\beta_{\pm}(\theta) = \frac{1}{2\pi i} \Log(L_{\pm}(\theta))
                      + f_{\pm}(\theta),
\end{equation}
where
\begin{equation}\label{eq:f+}
f_{+}(\theta) = \left\{
\begin{array}{cl} 0,& \theta = \frac{1}{6}, \\
1,& \theta \in ]\frac{1}{6},\frac{1}{3}],\end{array}\right.
\end{equation}
and
\begin{equation}\label{eq:f-}
f_{-}(\theta) = \left\{
\begin{array}{cl} 0,& \theta \in [\frac{1}{6},\frac{1}{3}[, \\
-1,& \theta = \frac{1}{3}.\end{array}\right.
\end{equation}
By (\ref{eq:p/q}) and the definition of $\beta_{\pm}$ the
representation $\bar \rho _{\theta,\vep}$ extends to a
representation of $\pi_1(M_{p/q})$ if and only if
\begin{equation}\label{eq:p/q'}
p\theta+q\beta_{\vep}(\theta) \in \Z
\end{equation}
which is nothing but (\ref{eq:p/q1}) (reparametrized).
We note that $\beta_{\pm}$ are smooth on
$]\frac{1}{6},\frac{1}{3}[$ but not in the end points $1/6$ and
$1/3$. The terms $f_{\pm}$ have been chosen so that
$\beta_{\pm}(1/6)= 1/2$. This is needed for the proof of


\begin{proposition}[ {\cite[p.~362]{[18]}} ]\label{prop:CS1}
Let $\theta \in [1/6,1/3]$ and let $\bar{\rho}_{\theta,\pm}$
be as in \refprop{prop:SU(2)}. If $\bar{\rho}_{\theta,\vep}$
extends to a representation of $\pi_{1}(M_{p/q})$ for a
$\vep \in \{\pm 1\}$ then
$$
\CS(\bar{\rho}_{\theta,\vep}) = -\frac{1}{6} - cp\theta^{2}
- dq\beta_{\vep}^{2}(\theta) - 2cq\theta\beta_{\vep}(\theta)
- 2\int_{1/6}^{\theta}\beta_{\vep}(t)\dte t \pmod{\Z},
$$
where $\beta_{\pm}$ are the curves defined by
(\ref{eq:beta}).\HS
\end{proposition}


Kirk and Klassen prove the above result by explicitly
constructing a piecewise smooth path
$\rho : [0,1] \to \Hom(\pi,\SL(2,\C))$ from the trivial
representation to
$\bar{\rho}_{\frac{1}{6},+} = \bar{\rho}_{\frac{1}{6},-}$ with
piecewise smooth curves $\alpha,\beta:[0,1] \to \C$ as in
(\ref{eq:pathkonjugering}) satisfying $\alpha(1)=\frac{1}{6}$
and $\beta(1)=\frac{1}{2}$. Moreover, they use that
$\int_{0}^{1} \beta(t)\alpha'(t) \dte t=\frac{1}{12}$ and the
fact that $y \mapsto \bar{\rho}_{y,\vep}$,
$[1/6,\theta] \to \Hom(\pi,\SU(2))$ is a path from
$\bar{\rho}_{\frac{1}{6},\vep}$ to $\bar{\rho}_{\theta,\vep}$
with associated functions $\alpha(y)=y$ and
$\beta(y)=\beta_{\vep}(y)$. By the choice of the functions
$f_{\pm}$, these $\alpha$-- and $\beta$--functions are
continuations of the ones used for the path $\rho$ from the
trivial representation to $\bar{\rho}_{\frac{1}{6},\pm}$.

Kirk and Klassen argue that
$\int_{0}^{1} \beta(t)\alpha'(t) \dte t = \frac{1}{12}$ using a
comparison between a computer calculation and the Chern--Simons
invariants of flat $\SU(2)$--connection on the Seifert manifold
$M_{-3}$. By following Kirk and Klassen's argument
\cite[pp.~361--362]{[18]} it is actually not hard to give an
explicit calculation of this integral. Let us give some
details. The path $\rho$ from the trivial connection to
$\bar{\rho}_{\frac{1}{6},\pm}$ consists of three parts, where
$\beta$ is identically zero along the first two parts. We can
therefore concentrate on the third part. Let
$a=(3+\sqrt{5})/2$, and let $\alpha : [0,1] \to \C$ be a
piecewise smooth curve from $\frac{1}{2\pi i} \Log(\sqrt{a})$
to $1/6$. Let $t(s)=e^{4\pi i \alpha(s)}$ and choose a
piecewise smooth solution $u(s)$ to $\phi(t(s),u(s))=0$, where
$\phi$ is given by (\ref{eq:phifunction}). Then
$s \mapsto \rho_{(e^{2\pi i\alpha(s)},u(s))} =: \eta_{s}$
is the third piece of our curve $\rho$ (reparametrized).
Assuming $\alpha(s) \notin \frac{1}{2}\Z$ (so as to avoid the
parabolic representations) we can diagonalize exactly as
demonstrated after \refcor{cor:SL(2,C)} and get
$$
\tilde{\eta}_{s}(\mu) = \diag(T,T^{-1}),\qquad
\tilde{\eta}_{s}(\lambda) =
\diag\left( \lambda_{11}(T,u),\lambda_{11}(T,u)^{-1}\right),
$$
where $T=T(s)=e^{2\pi i\alpha(s)}$, $u=u(s)$, $\lambda_{11}$
is as below \refcor{cor:SL(2,C)}, and where
$\tilde{\eta}_{s}(\gamma) = U^{-1}\eta_{s}(\gamma)U$ for
$\gamma \in \pi$, where
$U=U(s)=\left( \begin{array}{cc}
                1 & -1/(T^{2}-1) \\
                0 & 1
                \end{array}
\right)$.
This shows that $\alpha(s)$ indeed plays the role as the
$\alpha$--curve for our path $\eta_{s}$. The $\beta$--curve
should be a piecewise smooth curve $\beta(s)$ starting at zero
such that
\begin{equation}\label{eq:betany}
e^{2\pi i\beta(s)} = \lambda_{11}(e^{2\pi i\alpha(s)},u(s))
\end{equation}
for $s \in [0,1]$. We note that
$\lambda_{11}(e^{2\pi i\alpha(1)},u(1))=-1$ so we must have
$\beta(1) \in \frac{1}{2} + \Z$. Since $\bar{\rho}_{1/6,\pm}$
extends to a $\SU(2)$--representation of $\pi_{1}(M_{-3})$ we
get from (\ref{eq:CSsurgery}) that
$$
- 2\int_{0}^{1} \beta(s) \alpha'(s) \dte s - \frac{1}{12}
+ \frac{1}{3}\beta(1) \pmod{\Z}
$$
is a Chern--Simons value of a flat $\SU(2)$--connection on
$M_{-3}$, so $\int_{0}^{1} \beta(s) \alpha'(s) \dte s$ is real.

We now only have to choose a nice $\alpha$--curve. Let $\delta$
be a small positive parameter less than $|\alpha(0)| < 1/6$,
and let $\alpha = \alpha_{1} + \alpha_{2} + \alpha_{3}$, where
$\alpha_{1}$ is the line segment $[\alpha(0), -i\delta]$,
$\alpha_{2}$ is the part of the circle with centre zero and
radius $\delta$ running from $-i\delta$ to $\delta$, and
$\alpha_{3} = [\delta,1/6]$. Here the parameter $\delta$ is
introduced to avoid passing through zero (so as to avoid
parabolic representations). With this choice it is not hard to
show that there is a unique continuous solution
$(u(s),\beta(s))$ to $\phi(t(s),u(s))=0$ and (\ref{eq:betany})
with $\beta(0)=0$ and $\beta(1)=\frac{1}{2}$ and to show that
$\int_{0}^{1} \beta(s) \alpha'(s)\dte s = \frac{1}{12}$ for
this solution. (Use that the integral is real and independent
of $\delta$ and calculate its $\delta \ria 0_{+}$ limit).

\refprop{prop:CS1} gives a formula for the Chern--Simons
invariants of the irreducible flat $\SU(2)$--connections on
$M_{p/q}$. Let us also determine the Chern--Simons invariants
of the reducible flat $\SU(2)$--connections on $M_{p/q}$.
Therefore let $\rho_{j/|p|}$ be as in
\refprop{prop:SU(2)abelian}, $p \neq 0$, and let
$\alpha(t)=jt/|p|$ and $\beta(t)=0$, $t \in [0,1]$, and get by
(\ref{eq:CSsurgery}) that
\begin{equation}\label{eq:CSabelianpnot0}
\CS(\rho_{j/|p|}) = -cpj^{2}/p^{2} = -cj^{2}/p \pmod{\Z},
\end{equation}
where $c$ is the inverse of $-q \bmod{p}$.

In case $p=0$ the moduli space of flat reducible
$\SU(2)$--connections on $M_{0}$ can be identified with a
closed interval, cf.\ \refprop{prop:SU(2)abelian}. Since the
Chern--Simons functional is constant on each of the connected
components of the moduli space of flat connections, we conclude
that the Chern--Simons invariant of any of the reducible
$\SU(2)$--connections is equal to the Chern--Simons invariant
of the trivial connection, i.e.\ it is equal to zero. This of
course also follows from Kirk and Klassen's result. In fact,
if $\rho_{\theta}$ denotes the abelian representation from
\refprop{prop:SU(2)abelian}, then we can put
$\alpha(t)=\theta t$ and $\beta(t) =0$, $t \in [0,1]$, and get
by (\ref{eq:CSsurgery}) that
\begin{equation}\label{eq:CSabelianp0}
\CS(\rho_{\theta}) = 0 \pmod{\Z}.
\end{equation}


\newpage


\subsection{A comparison between Chern--Simons invariants and
critical values of the phase functions $\Phi_{n}^{a,b}$}



\noindent The purpose of this section is to combine the
Chern--Simons theory described in the previous two sections
with the asymptotic analysis in Sec.~4.3. First we will
describe a correspondence between the critical points of the
phase functions $\Phi_{n}^{a,b}$ in
(\ref{eq:Phasefunctiontypical}) and the nonabelian
$\SL(2,\C)$--representations of $\pi_{1}(M_{p/q})$. Thereafter
we will show that the set of Chern--Simons invariants of flat
irreducible $\SU(2)$--connections on $M_{p/q}$ is a certain
subset of the critical values of the functions
$\Phi_{n}^{a,b}$. Like in Sec.~4.3 we will most of the time
work with the shifted phase functions $\Psi_{n}^{a,b}$ in
(\ref{eq:Phasefunctiontypical1}). We refer to
\refrem{rem:PhiPsi} below for a comparison between the phase
functions $\Phi_{n}^{a,b}$ and $\Psi_{n}^{a,b}$. Recall the set
$\tilde{\mN}$ given by (\ref{eq:Ntilde}).


\begin{theorem}\label{thm:comparison}
The map $(x,y) \mapsto \rho_{(e^{\pi ix},e^{2\pi iy} -1)}$
gives a surjection $\varphi$ from the set of critical points
$(x,y)$ of the functions $\Psi^{a,b}_{n}$, $a,b,n \in \Z$, with
$x \notin \Z$ onto the set of representations
$\rho_{(s,u)} : \pi \to \SL(2,\C)$, $(s,u) \in \tilde{\mN}$,
which extend to $\SL(2,\C)$--representations of
$\pi_{1}(M_{p/q})$.

If $(x,y)$ is a critical point, let us say of $\Psi_{n}^{a,b}$,
then $(x+2k,y+l)$ is a critical point of
$\Psi_{n+pk}^{a+l,b+2k}$ for any $k,l \in \Z$, so
$\varphi^{-1}(\varphi(x,y))=\{\;(x+2k,y+l)\;|\;k,l \in \Z\;\}$
if $x \notin \Z$.
\end{theorem}


\begin{proof}
The last statement follows immediately from
(\ref{eq:critical}), so let us concentrate on the first part.
Let $\psi : \C^{2} \to \C$ be given by
$$
\psi(z,w) = (1-zw)(w-z) - zw,
$$
so $\psi(v^{2},w)=0$ if and only if $(v,w)$ is a solution to
(\ref{eq:stationary2}). Then
$$
\psi(z,u+1) = -z\phi(z,u)
$$
for $(z,u) \in \C^{*} \times \C$, where $\phi$ is the function
(\ref{eq:phifunction}). It follows that $(v,w)$ is a solution
to (\ref{eq:stationary2}) if and only if either $(v,w)=(0,0)$
or $(v,w-1) \in \tilde{\mN}$.

Next assume that $(v,u) \in \tilde{\mN}$ and put
$(z,w)=(v^{2},u+1)$. Since $\psi(z,w)=0$ and $z \neq 0$ we have
that $w \neq 0$ and $w-z \neq 0$. Therefore $1-zw = wz/(w-z)$
and $(v,w)$ is a solution to (\ref{eq:stationary1}) if and only
if
\begin{eqnarray*}
v^{-p} &=& \left(\frac{(w-z)^{2}}{wz}\right)^{q}
    = \left( wz^{-1} - 2 + zw^{-1} \right)^{q} \\*
&=& \left( \lambda_{11}(v,w-1) - 1 - z^{2}
               + zw^{-1} + wz + z \right)^{q}.
\end{eqnarray*}
But $\psi(z,w)=0$ and $w \neq 0$ implies that
$-1-z^{2}+zw^{-1}+wz+z=0$. Thus $(v,w)$ is a solution to
(\ref{eq:stationary1}) if and only if $(s,u)=(v,u)$ is a
solution to (\ref{eq:rhosurgery}).

The above shows together with the discussion around
(\ref{eq:rhosurgery}) that there is a one to one correspondence
between common nonzero solutions $(v,w)$ to
(\ref{eq:stationary1}), (\ref{eq:stationary2}) with
$v^{2} \neq 1$ and representations
$\rho_{(v,w-1)} : \pi \to \SL(2,\C)$,
$(v,w-1) \in \tilde{\mN}$, which extend to
$\SL(2,\C)$--representations of $\pi_{1}(M_{p/q})$. By the
remarks following (\ref{eq:critical}) this proves the theorem.
\end{proof}


Recall the set $\mS$ in (\ref{eq:SUcriticalpoint}). Moreover,
recall that if $(x,y)$ is a critical point of $\Psi_n^{a,b}$,
$a,b,n \in \Z$, with $(x,y) \in \mS$ then $x \notin \Z$ is
automatically satisfied. By \refprop{prop:SU(2)} and the above
theorem we therefore have


\begin{corollary}
The surjection $\varphi$ in \refthm{thm:comparison} restricts
to a surjection from the set of critical points $(x,y)$ of
$\Psi_n^{a,b}$, $a,b,n \in \Z$, with $(x,y) \in \mS$ onto the
set of representations
$\rho_{(s,u)} : \pi_1(M_{p/q}) \to \SL(2,\C)$,
$(s,u) \in \tilde{\mN}$, which are equivalent to
$\SU(2)$--representations of $\pi_{1}(M_{p/q})$.
\end{corollary}


\begin{theorem}\label{thm:main}
Let $(x,y) \in \C^{2}$ such that
$\rho_{(e^{\pi ix},e^{2\pi iy} -1)}$
is equivalent to a nonabelian $\SU(2)$--representation of
$\pi_{1}(M_{p/q})$ and choose in accordance with
\refthm{thm:comparison} integers $a,b,n$ such that $(x,y)$ is a
critical point of $\Psi_{n}^{a,b}$. If $a',b',n'$ is another
such set of integers, then $b'=b$ and $a'+n'/q=a+n/q$. In fact
we have
\begin{eqnarray*}
a + \frac{n}{q} &=& y + \frac{p}{2q}x
+ \frac{i}{2\pi} \left(\Log\left(1-e^{2\pi i(x+y)}\right)
- \Log\left(1-e^{2\pi i(x-y)}\right)\right), \\*
b &=& x
+ \frac{i}{2\pi} \left(\Log\left(1-e^{2\pi i(x+y)}\right)
+ \Log\left(1-e^{2\pi i(x-y)}\right)\right).
\end{eqnarray*}
Moreover, for any such set of integers $a,b,n$ we have
$$
\CS(\bar{\rho}_{\theta,\vep}) = \Psi_{n}^{a,b}(x,y) \pmod{\Z},
$$
where $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$\vep \in \{ \pm \}$ with $e^{2\pi i\theta}=e^{\pi ix}$ and
$1+u_{\vep}(\theta) = e^{2\pi iy}$, and
$\bar{\rho}_{\theta,\vep}$ is a $\SU(2)$--representation of
$\pi_{1}(M_{p/q})$ equivalent to
$\rho_{(e^{\pi ix},e^{2\pi iy} -1)}$ and given by
\refprop{prop:SU(2)}.
\end{theorem}


\begin{remark}\label{rem:PhiPsi}
i) In general we have $\Phi_{n}^{a,b} = \Psi_{n}^{a+b,a-b}$,
so there is a ono to one correspondence between the phase
functions $\Phi_{n}^{a,b}$ and the phase functions
$\Psi_{n}^{a',b'}$ with $a'+b'$ even.
If $(x,y)$ is a critical point
of $\Psi_{n}^{a',b'}$ with $a'+b'$ odd, then $(x,y)$ is also a
critical point of $\Psi_{n-q}^{a'+1,b'}$ by \refthm{thm:main}.
In that way we see that any critical point of one of the
functions $\Psi_{n}^{a',b'}$ is also a critical point of one
of the functions $\Phi_{n}^{a,b}$.

\noindent ii) Assume that $|p/q| > \sqrt{20}$ and assume that
$(x_j,y_j)$, $j=1,2$, are degenerate critical points of phase
functions $\Phi_n^{a,b}$ belonging to $\mS$. Let
$v_j=e^{\pi ix_j}$ and $w_j=e^{2\pi iy_j}$. By
\refprop{prop:Nondeg} we have
$\cos(2\pi x_1) = \cos(2\pi x_2)$ and $w_j=w_{-\vep}(x_j)$,
where $\vep=\sign(p/q)$, so $w_1=w_2$. Moreover,
$x_1, x_2 \in [-2/3,-1/3] \cup [1/3,2/3] + 2\Z$. We are
interested in
comparing the equivalence classes of the representations
$\rho_j=\rho_{(v_j,w_j - 1)}$. For that purpose we can without
loss of generality assume that $x_1,x_2 \in [1/3,2/3]$. Then
$x_2=x_1$ or $x_2=1-x_1$. In the second case $v_2 = - v_1$.
Note here that $-v_1 = v_1^{-1}$ if and only if
$v_1 \in \{ \pm i \}$. But in that case $\cos(2\pi x_1)=-1$ and
by (\ref{eq:detHessian4}) we get that
$p/q \in \{ \pm 2/\sqrt{5} \}$ which is impossible. Thus
$\rho_1$ and $\rho_2$ are not equivalent. If $p$ is odd we
must have $x_2=x_1$ since only one of the points
$(v_1,w_1)$, $(-v_1,w_1)$ can be a solution to
(\ref{eq:stationary1}). If $p$ is even both $(v_1,w_1)$ and
$(-v_1,w_1)$ are solutions to both of the equations
(\ref{eq:stationary1}) and (\ref{eq:stationary2}). Thus
\refprop{prop:Nondeg} shows that the set of degenerate critical
points in $\mS$ of the phase functions $\Phi_n^{a,b}$,
$a,b,n \in \Z$, is either empty or corresponds under the
surjection in \refthm{thm:comparison} to one point in
$\mM_{p/q}$ in case $p$ is odd and to two points in the moduli
space in case $p$ is even.
\end{remark}


The phase functions $\Psi_{n}^{0,0}$, $\Psi_{n}^{1,-1}$,
$\Psi_{n}^{1,1}$ and $\Psi_{n}^{2,0}$ are the ones entering
\refconj{conj:mainconj}. By \refthm{thm:main} the parameter
$b$ is fixed by a critical point of $\Psi_{n}^{a,b}$, while
$a$ and $n$ can be varied as long as we keep fixed $a+n/q$.
Because of this (see also \reflem{lem:Phivaluesym} below) we
only need to consider $\Psi_{n}^{0,0}$, $\Psi_{n}^{0,-1}$, and
$\Psi_{n}^{0,1}$. By \refthm{thm:main} (and also the proof of
this theorem and \refprop{prop:SU(2)}) we get


\begin{corollary}
Let $(x,y) \in \C^{2}$ such that
$\rho_{(e^{\pi ix},e^{2\pi iy} -1)}$
is equivalent to a nonabelian $\SU(2)$--representation of
$\pi_{1}(M_{p/q})$. Let $(x',y') \in \C^{2}$ such that
$(e^{\pi ix'},e^{2\pi iy'})=(e^{\pi ix},e^{2\pi iy})$ and
$\rea(x') \in ]-1,1]$ and $\rea(y') \in ]-1/2,1/2]$. Moreover,
let
\begin{eqnarray*}
n &=& q\left(y'+\frac{p}{2q}x'
+ \frac{i}{2\pi} \left(\Log\left(1-e^{2\pi i(x+y)}\right)
- \Log\left(1-e^{2\pi i(x-y)}\right)\right)\right), \\
b &=& x'
+ \frac{i}{2\pi} \left(\Log\left(1-e^{2\pi i(x+y)}\right)
+ \Log\left(1-e^{2\pi i(x-y)}\right)\right).
\end{eqnarray*}
Then $\theta:= x'/2 \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$$
b = \left\{ \begin{array}{rl} -1,& \theta \in [-1/3,-1/4] \\
0, & \theta \in ]-1/4,-1/6] \cup [1/6,1/4] \\
1, & \theta \in ]1/4,1/3].
\end{array}\right.
$$
Moreover, $n \in \Z$ and $(x',y')$ is a critical point of
$\Psi_{n}^{0,b}$ and
$$
\CS(\bar{\rho}_{\theta,\vep}) =
\Psi_{n}^{0,b}(x',y') \pmod{\Z},
$$
where $\vep \in \{ \pm \}$ with
$1+u_{\vep}(\theta) = e^{2\pi iy}$, and
$\bar{\rho}_{\theta,\vep}$ is a $\SU(2)$--representation
of $\pi_{1}(M_{p/q})$ equivalent to
$\rho_{(e^{\pi ix},e^{2\pi iy} -1)}$ and given by
\refprop{prop:SU(2)}.
\end{corollary}


We note that the first part of \refthm{thm:main} is an
immediate consequence of (\ref{eq:critical}). To prove the
second part we start by observing that if $a,a',n,n',b$ are
integers such that $a'+n'/q=a+n/q$ then
$\Psi_{n}^{a,b}(x,y)-\Psi_{n'}^{a',b}(x,y)$ is an integer
independent of $(x,y) \in \C^{2}$. The remaining part of the
proof will consists of a series of lemmas. We start by


\begin{lemma}\label{lem:Phivaluesym}
Let $a,b,n \in \Z$ and assume that $(x,y)$ is a critical point
of $\Psi_{n}^{a,b}$. Let $l,k \in \Z$ and put $a'=a+l$,
$b'=b+2k$, and $n'=n+pk$. Then $(x+2k,y+l)$ is a critical point
of $\Psi_{n'}^{a',b'}$ and
$$
\Psi_{n'}^{a',b'} (x+2k,y+l) - \Psi_{n}^{a,b}(x,y) \equiv
0 \pmod{\Z}.
$$
\end{lemma}


\begin{proof}
That $(x+2k,y+l)$ is a critical point of $\Psi_{n'}^{a',b'}$ is
an immediate consequence of (\ref{eq:critical}) and was already
observed in \refthm{thm:comparison}. Put $x'=x+2k$ and
$y'=y+l$. Since $e^{2\pi i x'}=e^{2\pi ix}$ and
$e^{2\pi iy'}=e^{2\pi iy}$ we get
\begin{eqnarray*}
\Psi_{n'}^{a',b'} (x',y') - \Psi_{n}^{a,b}(x,y) &=&
a'x' + b'y' -x'y' + \frac{n'}{q}x' -\frac{p}{4q}{x'}^{2}
     - \frac{d}{q}{n'}^{2} \\
&& - ax - by + xy - \frac{n}{q}x + \frac{p}{4q}x^{2}
   + \frac{d}{q}n^{2} \\
&=& 2(a+l)k  + 2\frac{n}{q}(1-pd)k + \frac{p}{q} (1-pd) k^{2}.
\end{eqnarray*}
Here $pd-cq =1$ for an integer $c$ so
$$
\Psi_{n'}^{a',b'} (x',y') - \Psi_{n}^{a,b}(x,y)
= 2(a+l-nc)k - pck^{2}.
$$
\end{proof}


By \refprop{prop:SU(2)} and the above lemma we are thus left
with the following to prove: Let
$\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and assume that
$\bar{\rho}_{\theta,\vep}$ extends to a representation of
$\pi_{1}(M_{p/q})$ for $\vep \in \{\pm\}$. Let $b=b(\theta)$
and $n=n(\theta)$ be the unique integers such that
$(2\theta,y)$ is a stationary point of $\Psi_{n}^{0,b}$, where
$y=\frac{1}{2\pi i} \Log(1+u_{\vep}(\theta))$ (so
$\rea(y) = \frac{1}{2}$) (see around (\ref{eq:critical2}) and
(\ref{eq:critical1})). Then
\begin{equation}\label{eq:mainstatement}
\CS(\bar{\rho}_{\theta,\rho}) = \Psi_{n}^{0,b}(2\theta,y) \pmod{\Z}.
\end{equation}
In the course of the proof of this identity we will prove that
\begin{equation}\label{eq:CS2}
\CS(\bar{\rho}_{\theta,\vep}) = -\frac{1}{6}
- \frac{p}{q}\theta^{2} + \frac{m}{q}2\theta - \frac{d}{q}m^{2}
- 2\int_{1/6}^{\theta}\beta_{\vep}(t) \dte t \pmod{\Z},
\end{equation}
for $\theta \in [1/6,1/3]$, where
$m= p\theta + q\beta_{\vep}(\theta) \in \Z$ by (\ref{eq:p/q'}).
Unfortunately the proof of (\ref{eq:mainstatement}) is rather
technical, but we have tried to emphasize the main ideas of the
proof here and defer many technicalities to the appendices C
and D.

The Chern--Simons invariants of $\SU(2)$--connections are real,
so we begin by investigating to what extent a general phase
function $\Psi_{n}^{a,b}$, $a,b,n \in \Z$, is real in its
critical points. Assume that $(x,y)$ is such a critical point
and write $z=e^{2\pi i x}$ and $w=e^{2\pi i y}$ as usual. From
(\ref{eq:critical}) we find that
$$
a - \rea(y) = \frac{p}{2q}\rea(x) - \frac{n}{q}
- \frac{1}{2\pi} \ima \left(\Log(1-zw)-\Log(1-zw^{-1})\right),
$$
and
$$
b - \rea(x) =
- \frac{1}{2\pi} \ima\left(\Log(1-zw)+\Log(1-zw^{-1})\right).
$$
Moreover, we have $\ima(x) = -\frac{1}{2\pi}\Log|z|$ and
$\ima(y)=-\frac{1}{2\pi}\Log|w|$. By
(\ref{eq:Phasefunctiontypical1}) we therefore get
\begin{eqnarray*}
\ima\left(\Psi_{n}^{a,b}(x,y)\right) &=& (a-\rea(y))\ima(x)
+ (b-\rea(x))\ima(y) - \frac{p}{2q}\ima(x)\rea(x) \\
&& + \frac{n}{q}\ima(x) + \frac{1}{4\pi^{2}}
\ima\left( \Li_{2}(zw)-\Li_{2}(zw^{-1})\right).
\end{eqnarray*}
This together with the above expressions for $a-\rea(y)$ and
$b-\rea(x)$ leads to the formula
\begin{eqnarray*}
\ima\left(\Psi_{n}^{a,b}(x,y)\right) &=& \frac{1}{4\pi^{2}}
\left( \ima(\Log(1-zw)-\Log(1-zw^{-1}))\Log|z| \right. \\
&& + \ima(\Log(1-zw) + \Log(1-zw^{-1}))\Log|w| \\
&& + \left.
\ima\left( \Li_{2}(zw)-\Li_{2}(zw^{-1})\right) \right).
\end{eqnarray*}
By introducing the Bloch--Wigner dilogarithm function
$$
D(z) = \ima\left( \Li_{2}(z) \right) + \Arg(1-z) \Log|z|
$$
we obtain


\begin{lemma}\label{lem:imaPsi}
Let $a,b,n \in \Z$ and let $(x,y)$ be a critical point of
$\Psi_{n}^{a,b}$. Then
$$
\ima\left(\Psi_{n}^{a,b}(x,y)\right)
= \frac{1}{4\pi^{2}} \left( D\left(e^{2\pi i(x+y)}\right)
  - D\left(e^{2\pi i(x-y)}\right)\right).
$$\HS
\end{lemma}


We note that $D$ is analytic on $\C \sm \{ 0,1\}$ and
continuous on $\C$. Moreover, $D$ satisfies the identities
\begin{equation}\label{eq:WienerBlochidentities}
D(z) + D(\bar{z}) = 0, \hspace{.2in} D(z) + D(1/z) = 0
\end{equation}
for all $z \in \C \sm \{0\}$. From this we have


\begin{corollary}\label{cor:imaPsi}
Let $a,b,n \in \Z$ and let $(x,y)$ be a critical point of
$\Psi_{n}^{a,b}$ with $e^{2\pi ix} \in S^{1}$ and
$e^{2\pi i y } \in \R$. Then
$$
\ima\left(\Psi_{n}^{a,b}(x,y)\right) = 0.
$$\HS
\end{corollary}


\begin{remark}
Let $(v,w)$ be a non-zero solution to (\ref{eq:stationary1})
and (\ref{eq:stationary2}). Then $(\bar{v},\bar{w})$ is also
a solution to these two equations as already observed. Let
$z=v^{2}$ and write $(z,w)=(e^{2\pi ix},e^{2\pi iy})$. Then
$(\bar{z},\bar{w})=(e^{-2\pi i\bar{x}},e^{-2\pi i\bar{y}})$.
If $(x,y)$ is a critical point of $\Psi_{n}^{a,b}$, then
$(-\bar{x},-\bar{y})$ is a critical point of
$\Psi_{-n}^{-a,-b}$. By \reflem{lem:imaPsi} and
(\ref{eq:WienerBlochidentities}) we have
$$
\ima\left(\Psi_{n}^{a,b}(x,y)\right) =
    -\ima\left(\Psi_{-n}^{-a,-b}(-\bar{x},-\bar{y})\right).
$$
Hence, if this value is different from zero, then either
$\exp(2\pi ir\Psi_{-n}^{-a,-b}(-\bar{x},-\bar{y}))$ or
$\exp(2\pi ir\Psi_{n}^{a,b}(x,y))$ grows exponentially. We
note that by \refconj{conj:mainconj} and
\refcor{cor:imaPsi} stationary points leading to such
exponential growth do not contribute to the large $r$
asymptotics of $\bar{\tau}_{r}(M_{p/q})$, see also
\refthm{thm:asymptotics}.
\end{remark}


We now embark upon proving (\ref{eq:mainstatement}). We start
by reducing to the case $\theta \in [1/6,1/3]$. By
\refprop{prop:SU(2)} we know that the representations
$\bar{\rho}_{\theta,\vep}$ and $\bar{\rho}_{-\theta,\vep}$ are
$\SU(2)$--equivalent, so in particular they have the same
Chern--Simons invariant.


\begin{lemma}\label{lem:symmetry}
Let the situation be as in (\ref{eq:mainstatement}). Then
$$
\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)
- \Psi_{n(-\theta)}^{0,b(-\theta)}(-2\theta,y) \equiv
0 \pmod{\Z}.
$$
\end{lemma}


To prove this and (\ref{eq:mainstatement}) we need the
technical \reflem{lem:Qfunctions} below keeping track of
branches of the logarithm in certain expressions. Let
$I=[-1/3,-1/6] \cup [1/6,1/3]$ and put
\begin{eqnarray}\label{eq:Q}
Q_{1}^{\pm}(\theta) &=& 1
- \left( 1+u_{\pm}(\theta) \right)^{-1}
e^{4\pi i\theta}, \nonumber \\
Q_{2}^{\pm}(\theta) &=& 1
- \left(1+u_{\pm}(\theta)\right) e^{4\pi i\theta}
\end{eqnarray}
for $\theta \in I$, where $u_{\pm}$ are defined in
\refprop{prop:SU(2)}. We also put
$Q_{3}^{\pm}(\theta)=1+u_{\pm}(\theta)$.


\begin{lemma}\label{lem:Qfunctions}
We have
\begin{equation}\label{eq:Qlog1}
\Log\left(Q_{1}^{\pm}(\theta)\right)
+ \Log\left(Q_{2}^{\pm}(\theta)\right)
= \Log\left(Q_{1}^{\pm}(\theta)Q_{2}^{\pm}(\theta)\right)
\end{equation}
and
\begin{equation}\label{eq:Qidentity1}
Q_{1}^{\pm}(\theta)Q_{2}^{\pm}(\theta) = e^{4\pi i\theta}
\end{equation}
for all $\theta \in I$. Moreover
\begin{equation}\label{eq:Qlog2}
\Log\left(Q_{1}^{\pm}(\theta)\right)
+ \Log\left(Q_{3}^{\pm}(\theta)\right)
- \Log\left(Q_{2}^{\pm}(\theta)\right)
= \Log\left(\frac{Q_{1}^{\pm}(\theta)Q_{3}^{\pm}(\theta)}
                 {Q_{2}^{\pm}(\theta)}\right)
+ e_{\pm}(\theta)2\pi i
\end{equation}
for all $\theta \in I$, where
$$
e_{+}(\theta) = \left\{
\begin{array}{cc} 1, & \theta \in ]1/6,1/4],\\
0, & \theta \in ]1/4,1/3[,\end{array}\right.
$$
and
$e_{-}(\theta) = 1 - e_{+}(\theta)$ for $\theta \in ]1/6,1/3[$,
$e_{\pm}(-1/4) = e_{\pm}(1/4)$,
$e_{\pm}(\theta) = 1 - e_{\pm}(-\theta)$ for
$\theta \in I \sm \{ \pm 1/6,\pm 1/4,\pm 1/3\}$, and
$e_{\pm}(\theta)=0$ for $\theta \in \{ \pm 1/6,\pm 1/3\}$.
Finally
\begin{equation}\label{eq:Qidentity2}
\frac{Q_{1}^{\pm}(\theta)Q_{3}^{\pm}(\theta)}
     {Q_{2}^{\pm}(\theta)}
= L_{\pm}(\theta)
\end{equation}
for all $\theta \in I$, where $L_{\pm}$ are given by
\refprop{prop:SU(2)}.
\end{lemma}


The proof of this lemma is given in Appendix D.


\begin{proofa}{\it of\,} \reflem{lem:symmetry}\,\,
By (\ref{eq:critical2}) and (\ref{eq:critical1}) we have
$$
b(\theta) = 2\theta - \frac{1}{2\pi i}
\left( \Log\left(Q_{1}^{\vep}(\theta)\right)
+ \Log\left(Q_{2}^{\vep}(\theta)\right)\right)
$$
and
$$
n(\theta) = p\theta + qy + q\frac{1}{2\pi i}
\left( \Log\left(Q_{1}^{\vep}(\theta)\right)
- \Log\left(Q_{2}^{\vep}(\theta)\right)\right).
$$
By \reflem{lem:Qfunctions}
\begin{equation}\label{eq:b}
b(\theta) = 2\theta
- \frac{1}{2\pi i} \Log\left( e^{4\pi i\theta} \right).
\end{equation}
Taking the real part of the expression for $n(\theta)$ we get
\begin{equation}\label{eq:n1}
n(\theta) = p\theta + \frac{1}{2}q
+ \frac{q}{2\pi} \left( \Arg\left(Q_{1}^{\vep}(\theta)\right)
- \Arg\left(Q_{2}^{\vep}(\theta)\right)\right).
\end{equation}
By (\ref{eq:b}) we get that
$$
b(-\theta) = - b(\theta), \hspace{.2in}
\theta \in [-1/3,-1/6] \cup [1/6,1/3] \sm \{ \pm 1/4\},
$$
and
$$
b(-1/4)=-1, \hspace{.2in} b(1/4)=0.
$$
By (\ref{eq:n1}), (\ref{eq:Qsym1}), and (\ref{eq:Qsym2}) we get
$$
n(-\theta) = q - n(\theta), \hspace{.2in}
\theta \in [-1/3,-1/6] \cup [1/6,1/3]\sm \{ \pm 1/4\},
$$
and
$$
n(-1/4) = n(1/4) - \frac{p}{2}.
$$
Let $b=b(\theta)$ and $n=n(\theta)$. Since
$\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)$ is real by
\refcor{cor:imaPsi} and since
$\rea\left( \Li_{2}(\bar{z})\right) =
\rea\left( \Li_{2}(z)\right)$
for $z \in \C \sm ]1,\infty[$ we find that
\begin{eqnarray*}
\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)
- \Psi_{n(-\theta)}^{0,b(-\theta)}(-2\theta,y)
&=& (b-b(-\theta))\rea(y) -4\theta\rea(y) \\
&& + \frac{(n+n(-\theta)}{q}2\theta
   - \frac{d(n^{2}-n(-\theta)^{2})}{q}.
\end{eqnarray*}
(If $\theta \in \{\pm 1/4\}$, use that
$\Li_{2}(e^{2\pi i(2\theta +y)})
- \Li_{2}(e^{2\pi i(2\theta-y)})$
is the same for $\theta =1/4$ and $\theta=-1/4$.) Assume first
that $\theta \neq \pm 1/4$. Then, since $\rea(y)=1/2$, we get
$$
\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)
- \Psi_{n(-\theta)}^{0,b(-\theta)}(-2\theta,y)
= b + dq -2dn \in \Z.
$$
Next assume that $\theta = 1/4$. Then one finds
$$
\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)
- \Psi_{n(-\theta)}^{0,b(-\theta)}(-2\theta,y)
= \frac{n}{q}(1-pd) - \frac{p}{4q}(1 - pd).
$$
But $1-pd=-qc$ for an integer $c$ so
$$
\Psi_{n(\theta)}^{0,b(\theta)}(2\theta,y)
- \Psi_{n(-\theta)}^{0,b(-\theta)}(-2\theta,y)
= \left(\frac{p}{4} -n \right)c.
$$
By (\ref{eq:p/q'}) $p/4 + q\beta_{\vep}(1/4) \in \Z$. But
$L_{\pm}(1/4)=1$ so $\beta_{\vep}(1/4) = f_{\vep}(1/4) \in \Z$,
so $p$ is divisible by $4$.
\end{proofa}


By using that
$y=\frac{1}{2\pi i} \Log\left(Q_{3}^{\vep}(\theta)\right)$
together with \reflem{lem:Qfunctions} we obtain the alternative
formula
$$
n(\theta) = p\theta + qe_{\vep}(\theta)
+ \frac{q}{2\pi i} \Log\left(L_{\vep}(\theta)\right).
$$
This and (\ref{eq:beta}) immediately leads to
\begin{equation}\label{eq:n3}
n(\theta) = p\theta + q\beta_{\vep}(\theta)
+ q(e_{\vep}(\theta)-f_{\vep}(\theta))
\end{equation}
for $\theta \in [1/6,1/3]$.
In the proof of (\ref{eq:mainstatement}) we need certain
symmetries for the functions $L_{\pm}$.
First we note that
\begin{equation}\label{eq:Lsym2}
L_{\pm}\left(\frac{1}{2} -\theta\right) = L_{\mp}(\theta)
\end{equation}
for $\theta \in [1/6,1/3]$ by (\ref{eq:Lreaima}).
Second, by the next lemma and \refprop{prop:SU(2)}, we have
\begin{equation}\label{eq:Lsym1}
L_{\mp}(\theta) = L_{\pm}(\theta)^{-1}
\end{equation}
for $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$. (In particular,
$\bar{\rho}_{\theta,\pm}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if $\bar{\rho}_{\theta,\mp}$
extends to a representation of $\pi_{1}(M_{-p/q})$.)


\begin{lemma}\label{lem:lambdasymmetry}
Let $s \in \C^{*}$ and let $u_{\pm}$ be the two solutions to
$\phi(s^{2},u)=0$. Then
$$
(1+u_{+})(1+u_{-}) = 1,
$$
and
$$
\lambda_{11}(s,u_{+})\lambda_{11}(s,u_{-}) = 1.
$$
\end{lemma}


\begin{proof}
We have
$$
1 + u_{\pm} = \frac{1}{2}(s^{2}+s^{-2}-1)
\pm \frac{1}{2}\sqrt{s^{4}+s^{-4}-2(s^{2}+s^{-2})-1}
$$
so
$$
(1 + u_{+})(1 + u_{-}) = \frac{1}{4}(s^{2} + s^{-2} -1)^{2}
- \frac{1}{4}(s^{4} + s^{-4} - 2(s^{2} + s^{-2}) - 1) = 1.
$$
Moreover,
\begin{eqnarray*}
\lambda_{11}(s,u_{\pm}) &=& \frac{1}{2}(s^{4} + s^{-4})
- \frac{1}{2}(s^{2} + s^{-2}) - 1 \\*
&& \pm \frac{1}{2}(s^{-2} - s^{2})\sqrt{s^{4} + s^{-4}
- 2(s^{2} + s^{-2}) -1}
\end{eqnarray*}
so
\begin{eqnarray*}
\lambda_{11}(s,u_{+})\lambda_{11}(s,u_{-}) &=&
\left(\frac{1}{2}(s^{4} + s^{-4})
- \frac{1}{2}(s^{2} + s^{-2}) - 1 \right)^{2} \\*
&& - \frac{1}{4}(s^{2} - s^{-2})^{2}
\left(s^{4} + s^{-4} - 2(s^{2} + s^{-2}) - 1 \right).
\end{eqnarray*}
By simple reductions one gets the result.
\end{proof}


We are now ready to finalize the proof of
(\ref{eq:mainstatement}) and thereby the proof of
\refthm{thm:main}.


\begin{proofa}{\it of\,} (\ref{eq:mainstatement})\,\,
By \reflem{lem:symmetry} we can assume that
$\theta \in [1/6,1/3]$. Write $\theta_{0}$ for $\theta$ in the
following. Let us first observe that formula (\ref{eq:CS2}) is
an immediate consequence of \refprop{prop:CS1}. In fact, by
letting $c,d$ be integers as in \refprop{prop:CS1} we get
\begin{eqnarray*}
&& -2cq\theta_{0}\beta_{\vep}(\theta_{0}) = 2cp\theta_{0}^{2}
- 2cm\theta_{0}, \\
&& -dq\beta_{\vep}^{2}(\theta_{0}) = -\frac{d}{q}\left(m^{2}
- 2pm\theta_{0}+p^{2}\theta_{0}^{2}\right),
\end{eqnarray*}
and therefore
$$
- cp\theta_{0}^{2} - dq\beta_{\vep}^{2}(\theta_{0})
- 2cq\theta_{0}\beta_{\vep}(\theta_{0})
= \left(c - \frac{dp}{q}\right)p\theta_{0}^{2}
- 2\left(c - \frac{dp}{q}\right)m\theta_{0} - \frac{d}{q}m^{2}.
$$
But $c-dp/q=-1/q$, hence (\ref{eq:CS2}) follows. On the other
hand we have
$$
\Psi_{n}^{0,b}(2\theta_{0},y) = (b-2\theta_{0})y
+ \frac{n}{q}2\theta_{0} -\frac{p}{q}\theta_{0}^{2}
- \frac{d}{q} n^{2} + \frac{1}{4\pi^{2}}
\left( \Li_{2}(z_{0}w_{\vep})
- \Li_{2}(z_{0}w_{\vep}^{-1}) \right),
$$
where $z_{0}=e^{4\pi i\theta_{0}}$ and
$w_{\vep}=1+u_{\vep}(\theta_{0})$. By (\ref{eq:b}) and
(\ref{eq:n3}) we have $b-2\theta_{0}=-\frac{1}{2\pi i}\Log(z_{0})$
and $n=m+q\left(e_{\vep}(\theta_{0})-f_{\vep}(\theta_{0})\right)$
so
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y) &=& -\frac{p}{q}\theta_{0}^{2}
+ \frac{m}{q}2\theta_{0} - \frac{d}{q} m^{2}
+ 2\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right)\theta_{0}
- l_{\vep}(\theta_{0}) \\*
&& + \frac{1}{4\pi^{2}}
\left(\Log(z_{0})\Log(w_{\vep})+ \Li_{2}(z_{0}w_{\vep})
- \Li_{2}(z_{0}w_{\vep}^{-1}) \right),
\end{eqnarray*}
where
$l_{\vep}(\theta_{0}) = 2dm\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right) + dq\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right)^{2} \in \Z$.
We therefore get that
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep}) &=& \frac{1}{6}
+ 2\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right)\theta_{0} \\*
&& + \frac{1}{4\pi^{2}} \left(\Log(z_{0})\Log(w_{\vep})
+ \Li_{2}(z_{0}w_{\vep})
- \Li_{2}(z_{0}w_{\vep}^{-1}) \right) \\*
&& + 2\int_{1/6}^{\theta_{0}}\beta_{\vep}(t) \dte t \pmod{\Z}.
\end{eqnarray*}
For $\theta_{0} \in [1/6,1/4]$ we note that
$e_{\vep}(\theta_{0}) = f_{\vep}(\theta_{0})$. We will consider
the special cases $\theta_{0} \in \{1/6,1/4,1/3\}$ first and
then handle the other cases afterwards.\newline
{\bf The cases $\theta_{0} \in \{1/6,1/3\}$.} In these
cases we have $w_{\vep}=-1$ so
\begin{eqnarray*}
&& \Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep}) \\*
&& \hspace{.3in} = \frac{1}{6}+\frac{i}{4\pi} \Log(z_{0})
+ 2\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right)\theta_{0}
+ 2\int_{1/6}^{\theta_{0}}\beta_{\vep}(t) \dte t \pmod{\Z}.
\end{eqnarray*}
If $\theta_{0}=1/6$ we immmediately get that this is zero. If
$\theta_{0}=1/3$ we get
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{6}+\frac{i}{4\pi} (4\pi i/3-2\pi i)
+ \frac{2}{3}\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right) \\*
&& + 2f_{\vep}(1/4)(1/3-1/6) \\*
&& + \frac{1}{\pi i}
\int_{1/6}^{1/3}\Log(L_{\vep}(t)) \dte t \pmod{\Z}.
\end{eqnarray*}
But if $\theta_0 \in [1/4,1/3]$ then
$$
\int_{1/4}^{\theta_{0}} \Log(L_{\pm}(\theta)\dte \theta
= -\int_{1/4}^{1/2-\theta_{0}}\Log(L_{\mp}(t))\dte t
= - \int_{1/2-\theta_{0}}^{1/4}\Log(L_{\pm}(t))\dte t,
$$
by (\ref{eq:Lsym2}) and (\ref{eq:Lsym1}) so
\begin{equation}\label{eq:Lintegral}
\int_{1/2-\theta_{0}}^{\theta_{0}}
\Log(L_{\pm}(\theta)\dte \theta = 0.
\end{equation}
In particular,
$$
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
= \frac{1}{3} - \frac{2}{3}f_{\vep}(1/3)
+ \frac{1}{3}f_{\vep}(1/4) \pmod{\Z},
$$
where we also use that $e_{\pm}(1/3)=0$ by
\reflem{lem:Qfunctions}. By (\ref{eq:f+}) and (\ref{eq:f-})
this is zero.\newline
{\bf The case $\theta_{0} = 1/4$.} In this case we have
$z_{0}=-1$ so
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{6}
+ \frac{1}{4\pi^{2}} \left(i\pi\Log(w_{\vep})
+ \Li_{2}(|w_{\vep}|) - \Li_{2}(|w_{\vep}|^{-1}) \right) \\*
&& + 2\int_{1/6}^{1/4}\beta_{\vep}(t) \dte t \pmod{\Z}.
\end{eqnarray*}
Since $(v_{0},w_{\vep})=(e^{2\pi i\theta_{0}},w_{\vep})$ is a
solution to (\ref{eq:stationary2}) we have
$w_{\vep} \in \{ (-3-\sqrt{5})/2,(-3+\sqrt{5})/2\}$, and by
(\ref{eq:1+u}) we then conclude that
$w_{\vep} = \frac{-3-\sqrt{5}}{2}$ if $\vep=-$ and
$w_{\vep} = \frac{-3+\sqrt{5}}{2}$ if $\vep=+$. By
(\ref{eq:dilog1/4}) we then get
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{6} + \frac{1}{4\pi^{2}}\left(-\pi^{2}
- \vep \frac{\pi^{2}}{5}\right)
+ 2\int_{1/6}^{1/4}\beta_{\vep}(t) \dte t \\*
&=& \frac{1}{6}
+ \frac{1}{4}\left(-1 - \vep\frac{1}{5}\right)
+ \frac{1}{6}f_{\vep}(1/4) \\*
&& + \frac{1}{\pi} \int_{1/6}^{1/4}\Arg(L_{\vep}(t)) \dte t
\pmod{\Z},
\end{eqnarray*}
and this is zero by (\ref{eq:f+}), (\ref{eq:f-}), and
(\ref{eq:Specialintegral1/4}).\newline
{\bf The case $\theta \in ]1/6,1/3[ \sm \{1/4\}$.}
We have
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{6}+\frac{1}{4\pi^{2}} \Log(z_{0})\Log(w_{\vep})
+ 2\left(e_{\vep}(\theta_{0})
- f_{\vep}(\theta_{0})\right)\theta_{0} \\*
&& + 2\int_{1/6}^{\theta_{0}}\beta_{\vep}(t) \dte t
+ R(2\theta_{0},y) \pmod{\Z},
\end{eqnarray*}
where
$$
R(x,y) = \frac{1}{4\pi^{2}}\left( \Li_{2}(e^{2\pi i(x+y)})
- \Li_{2}(e^{2\pi i(x-y)}) \right).
$$
Let us write $u$ for $u_{\vep}$ in the following. By definition
of the dilogarithm we have
$$
4\pi^{2}R(2\theta_{0},y) =
\int_{0}^{(1+u)^{-1}e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t
- \int_{0}^{(1+u)e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t.
$$
By (\ref{eq:1+u}) we have
$1+u_{-}(\theta) \leq -1 \leq 1+u_{+}(\theta) <0$ for all
$\theta \in [1/6,1/3]$ and $1+u_{\pm}(\theta)=-1$ if and only
if $\theta \in \{1/6,1/3\}$. Let $\theta_{1}=1/6$ if
$\theta_{0} \in [1/6,1/4[$ and $\theta_{1}=1/3$ if
$\theta_{0} \in ]1/4,1/3[$. We note that
$z \mapsto \Log(1-z)/z$ is analytic on $\C \sm [1,\infty[$ so
by Cauchy's theorem
\begin{eqnarray*}
4\pi^{2}R(2\theta_{0},y) &=& \int_{0}^{-e^{4\pi i \theta_{1}}}
\frac{\Log(1-t)}{t} \dte t +
\int_{-e^{4\pi i \theta_{1}}}^{(1+u)^{-1}e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t \\*
&& - \int_{0}^{-e^{4\pi i \theta_{1}}}
\frac{\Log(1-t)}{t} \dte t
- \int_{-e^{4\pi i \theta_{1}}}^{(1+u)e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t \\*
&=&
\int_{-e^{4\pi i \theta_{1}}}^{(1+u)^{-1}e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t
- \int_{-e^{4\pi i \theta_{1}}}^{(1+u)e^{4\pi i \theta_{0}}}
\frac{\Log(1-t)}{t} \dte t .
\end{eqnarray*}
The curves
$\gamma_{\pm}(\theta)=(1+u(\theta))^{\pm 1} e^{4\pi i \theta}$
are smooth on $]1/6,1/3[$ so
\begin{eqnarray*}
4\pi^{2}R(2\theta_{0},y) &=&
\lieta \left( \int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log(1-\gamma_{-}(\theta))\frac{\gamma_{-}'(\theta)}
{\gamma_{-}(\theta)} \dte \theta \right.\\*
&& \left. \hspace{.5in}
- \int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log(1-\gamma_{+}(\theta))\frac{\gamma_{+}'(\theta)}
{\gamma_{+}(\theta)} \dte \theta \right),
\end{eqnarray*}
where $\mu =1$ if $\theta_{1}=1/6$ and $\mu=-1$ if
$\theta_{1}=1/3$. (The parameter $\eta$ is necessary because
$u$ is not differentiable in $1/6$ and $1/3$.) It follows that
$$
4\pi^{2}R(2\theta_{0},y) = \lieta \left(
4\pi i R_{1}(\theta_{0},\eta) - R_{2}(\theta_{0},\eta)\right),
$$
where
\begin{eqnarray*}
R_{1}(\theta_{0},\eta) &=&
\int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(Q_{1}^{\vep}(\theta)\right)
- \Log\left(Q_{2}^{\vep}(\theta)\right) \dte \theta, \\
R_{2}(\theta_{0},\eta) &=&
\int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\left\{ \Log\left(Q_{1}^{\vep}(\theta)\right)
+ \Log\left(Q_{2}^{\vep}(\theta)\right) \right\}
\frac{u'(\theta)}{1+u(\theta)} \dte \theta,
\end{eqnarray*}
where the functions $Q_{i}^{\pm}$ are defined above
\reflem{lem:Qfunctions}. By \reflem{lem:Qfunctions}
\begin{eqnarray*}
R_{2}(\theta_{0},\eta) &=&
\int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(e^{4\pi i\theta}\right)
\frac{u'}{1+u} \dte \theta \\*
&=& 4\pi i \int_{\theta_{1}+\mu\eta}^{\theta_{0}} \theta
\frac{u'(\theta)}{1+u(\theta)} \dte \theta
- 2\pi ib(\theta_{0}) \int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\frac{u'(\theta)}{1+u(\theta)} \dte \theta.
\end{eqnarray*}
Since
$u'(\theta)/(1+u(\theta))
= \frac{\dte}{\dte \theta} \log(1+u(\theta))$
for any branch $\log$ of the logarithm defined on an open
section of $\C^{*}$ containing $]-\infty,0[$ we have
$$
\int_{\theta_{1}+\mu\eta}^{\theta_{0}} \theta
\frac{u'(\theta)}{1+u(\theta)} \dte \theta =
\left[ \theta\Log(1+u(\theta))
\right]_{\theta_{1}+\mu\eta}^{\theta_{0}}
- \int_{\theta_{1}+\mu\eta}^{\theta_{0}}
\Log(1+u(\theta)) \dte \theta,
$$
and
$$
\int_{\theta_{1}+\mu\eta}^{\theta_{0}}
\frac{u'(\theta)}{1+u(\theta)} \dte \theta
= \left[ \Log(1+u(\theta))
\right]_{\theta_{1}+\mu\eta}^{\theta_{0}}.
$$
We therefore get
\begin{eqnarray*}
R(2\theta_{0},y) &=& \frac{1}{4\pi^{2}}\lieta \left(
    4\pi i R_{1}(\theta_{0},\eta) - R_{2}(\theta_{0},\eta)
\right) \\*
&=& \frac{b(\theta_{0})}{2} - \theta_{1}
-\frac{1}{4\pi^{2}} \Log(z_{0})\Log(w_{\vep}) \\*
&& + \frac{i}{\pi}\lieta \left( R_{1}(\theta_{0},\eta)
+ \int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(Q_{3}^{\vep}(\theta)\right)\dte \theta \right),
\end{eqnarray*}
where we use that
$1 + u_{\vep}(\theta) = Q_{3}^{\vep}(\theta) = w_{\vep}$ and
(\ref{eq:b}). By \reflem{lem:Qfunctions} we get
$$
R_{1}(\theta_{0},\eta) +
\int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(Q_{3}^{\vep}(\theta)\right)\dte \theta
=  \int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(L_{\vep}(\theta)\right)
+ 2\pi i e_{\vep}(\theta)\dte \theta,
$$
so
$$
\lieta\left(R_{1}(\theta_{0},\eta) +
\int_{\theta_{1} + \mu\eta}^{\theta_{0}}
\Log\left(Q_{3}^{\vep}(\theta)\right)\dte \theta\right)
= e_{\vep}(\theta_{0}) 2\pi i(\theta_{0} - \theta_{1})
+ \int_{\theta_{1}}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta.
$$
But then
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{6} + 2e_{\vep}(\theta_{0})\theta_{1}
- 2f_{\vep}(\theta_{0})\theta_{0}
+ \frac{b(\theta_{0})}{2} - \theta_{1} \\*
&& + 2\int_{1/6}^{\theta_{0}}\beta_{\vep}(t) \dte t
- \frac{1}{\pi i} \int_{\theta_{1}}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta \pmod{\Z}.
\end{eqnarray*}
Here
$$
2\int_{1/6}^{\theta_{0}}\beta_{\vep}(t) \dte t =
2f_{\vep}(\theta_{0})\left(\theta_{0}-\frac{1}{6}\right)
+ \frac{1}{\pi i} \int_{\theta_{1}}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta,
$$
so
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{\pi i} \left(\int_{1/6}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta
- \int_{\theta_{1}}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta\right) \\*
&& + \frac{1}{6} + 2e_{\vep}(\theta_{0})\theta_{1}
- \frac{1}{3}f_{\vep}(\theta_{0})
+ \frac{b(\theta_{0})}{2} - \theta_{1} \pmod{\Z}.
\end{eqnarray*}
{\bf The subcase $\theta_{0} \in ]1/6,1/4[$.} Here we have
$\theta_{1}=1/6$ and $b(\theta_{0})=0$ so the result follows by
the fact that $e_{\vep}(\theta)=f_{\vep}(\theta)$ for
$\theta \in ]1/6,1/4[$.\newline
{\bf The subcase $\theta_{0} \in ]1/4,1/3[$.} In this case we
have $b(\theta_{0})=1$ and $\theta_{1}=1/3$ so
\begin{eqnarray*}
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
&=& \frac{1}{\pi i} \left( \int_{1/6}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta - \int_{1/3}^{\theta_{0}}
\Log(L_{\vep}(\theta))\dte \theta \right) \\*
&& + \frac{1}{3} + \frac{2}{3}e_{\vep}(\theta_{0})
- \frac{1}{3}f_{\vep}(\theta_{0})  \pmod{\Z}.
\end{eqnarray*}
By (\ref{eq:Lintegral}) we get
$$
\int_{1/3}^{\theta_{0}} \Log(L_{\pm}(t))\dte t =
\int_{1/3}^{\frac{1}{2}-\theta_{0}} \Log(L_{\pm}(t))\dte t
= -\int_{1/6}^{\theta_{0}}
\Log(L_{\pm}\left(\frac{1}{2}-t\right))\dte t.
$$
By (\ref{eq:Lsym2}) and (\ref{eq:Lsym1}) we then have
$$
\int_{1/3}^{\theta_{0}} \Log(L_{\pm}(t))\dte t =
\int_{1/6}^{\theta_{0}} \Log(L_{\pm}(t))\dte t,
$$
so
$$
\Psi_{n}^{0,b}(2\theta_{0},y)
- \CS(\bar{\rho}_{\theta_{0},\vep})
= \frac{1}{3} + \frac{2}{3}e_{\vep}(\theta_{0})
- \frac{1}{3}f_{\vep}(\theta_{0}) \pmod{\Z},
$$
and this is zero by \reflem{lem:Qfunctions}, (\ref{eq:f+}) and
(\ref{eq:f-}).
\end{proofa}


\begin{remark}\label{rem:whybar}
If $u_{\pm}=u_{\pm}(v)$ are the two solutions to
$\phi(v^{2},u)=0$ for $v \in \C^{*}$ fixed, then
$\lambda_{11}(v,u_{-})=\lambda_{11}(v,u_{+})^{-1}$ by
\reflem{lem:lambdasymmetry}. By the proof of
\refthm{thm:comparison} we therefore conclude that
$(v,1+u_{\vep})$, $\vep \in \{\pm\}$, is a solution to
(\ref{eq:stationary1}) and (\ref{eq:stationary2}) if and only
if $(v,1+u_{-\vep})$ is a solution to (\ref{eq:stationary2})
and
\begin{equation}\label{eq:stationary1-}
v^{p} = \left(\frac{w-v^{2}}{1-v^{2}w} \right)^{q}.
\end{equation}
If we work with the invariants $\tau_{r}$ instead of the
invariants $\bar{\tau}_{r}$, then by (\ref{eq:mirror2}) we have
to change $p/q$ to $-p/q$ everywhere in the above. The equation
(\ref{eq:stationary2}) will be the same but
(\ref{eq:stationary1}) will change to (\ref{eq:stationary1-}).
If $(v,u) \in \tilde{\mN}$ then we find as in the proof of
\refthm{thm:comparison} that $(v,w)=(v,u+1)$ is a solution to
(\ref{eq:stationary1-}) if and only if $(v,u)$ is a solution to
$$
v^{p}=\lambda_{11}(v,u)^{q},
$$
which is the ``wrong'' equation. This is one of the main
reasons for working with $\bar{\tau}_{r}$ instead of
$\tau_{r}$. Another reason is that one would get a minus sign
in (\ref{eq:mainstatement}).
\end{remark}


Let us end this section by some futher results on the
Chern--Simons invariants of flat irreducible
$\SU(2)$--connections on $M_{p/q}$.
By (\ref{eq:Lsym1}) $\bar \rho _{\theta,\vep}$ extends to
a $\SU(2)$--representation of $\pi_1(M_{p/q})$ if and only if
$\bar \rho _{\theta,-\vep}$ extends to
a $\SU(2)$--representation of $\pi_1(M_{-p/q})$. In that case
we find that
$$
\CS(\bar \rho _{\theta,-\vep}) =
- \CS(\bar \rho _{\theta,\vep})
$$
by using (\ref{eq:p/q'}).

If $p$ is even then
$e^{2\pi ip(1/2-\theta)}=e^{2\pi ip\theta}$. Since
$L_{\vep}(1/2-\theta)=L_{\vep}(\theta)^{-1}$ by
(\ref{eq:Lsym2}) and (\ref{eq:Lsym1}) and since $q$ is odd it
follows that $\bar \rho _{\theta,\vep}$ extends to a
$\SU(2)$--representation of $\pi_1(M_{p/q})$ if and only if
$\bar \rho _{1/2-\theta,\vep}$ extends to such a
representation, see (\ref{eq:p/q}). Assuming that
$\bar \rho _{\theta,\vep}$ extends to such a representation
we get
$$
\CS(\bar \rho _{\frac{1}{2}-\theta,\vep})
= \CS(\bar \rho _{\theta,\vep})
- \frac{1}{2} \frac{p}{2} \pmod{\Z}
$$
by using (\ref{eq:Lintegral}) and (\ref{eq:p/q'}).

By (\ref{eq:Lspecialvalues}) and (\ref{eq:p/q}) we find that
$\bar \rho _{1/6,-}=\bar \rho _{1/6,+}$ is a
$\SU(2)$--representation of $\pi_1(M_{p/q})$ if and only if
$p=6m+3$, $m \in \Z$, and q is odd. In that case
$$
\CS(\bar \rho _{1/6,\vep}) = - \frac{cp}{36} - \frac{dq}{4}
- \frac{1}{2}d \pmod{\Z}.
$$
By (\ref{eq:Lspecialvalues}) and (\ref{eq:p/q}) we also have
that $\bar \rho _{1/3,-}=\bar \rho _{1/3,+}$ is a
$\SU(2)$--representation of $\pi_1(M_{p/q})$ if and only if
$p=6m+3$, $m \in \Z$, and q is even. In that case
$$
\CS(\bar \rho _{1/3,\vep}) = \frac{1}{2} - \frac{cp}{9}
- \frac{dq}{4} \pmod{\Z}.
$$

Finally, by (\ref{eq:Lspecialvalues}) and (\ref{eq:p/q}),
$\rho_{1/4,-}$ and $\rho_{1/4,+}$ are
$\SU(2)$--representations of $\pi_1(M_{p/q})$ if and only if
$4$ divides $p$. In that case we find that
\begin{eqnarray*}
\CS(\bar \rho _{1/4,+}) &=& \frac{1}{5}
- \frac{cp}{16} \pmod{\Z}, \\
\CS(\bar \rho _{1/4,-}) &=& - \frac{1}{5}
- \frac{cp}{16} \pmod{\Z}.
\end{eqnarray*}
This follows by using (\ref{eq:Specialintegral1/4}).


\renewcommand{\theequation}{\Alph{appendixc}.\arabic{equation}}


\noindent We have in the following appendices collected
material of a technical nature.
