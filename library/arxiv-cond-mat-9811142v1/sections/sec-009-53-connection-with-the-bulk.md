---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-009-53-connection-with-the-bulk
section_title: "Connection with the bulk"
section_number: 5.3
pages: 27-32
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.975
---
It is known \cite{Fo93} 
that after appropriate scaling of the variables, the static
distributions at the 
hard and soft edges tend to the bulk distributions at large
distances from the edge of the system. The required scaling is
\beqa
X \mapsto \alpha + 2\pi \sqrt{\alpha}\, \rho x\,  , \quad \quad
X \mapsto  -\left(\alpha + \pi \rho x /\sqrt{\alpha} \right) \,  ,
\label{5.15}
\eeqa
with 
$\alpha \rightarrow \infty$, for the hard and soft edges respectively. Here we
will show that this feature persists for the dynamical distributions.

Consider 
first the hard edge with $\beta =2$ initial conditions.  Changing variables
$u \mapsto  u^{2}$ and making use of the asymptotic expansion
\beqa
J_{a}(x) \mathop{\sim}\limits_{x \to \infty}
\left(\frac{2}{\pi x}\right)^{1/2} \cos(x - \pi a/2 - \pi /4)
\label{5.16}
\eeqa
in the formulas (\ref{5.1}) and (\ref{5.2}), we see that
\beqa
\lefteqn{\lim_{\alpha \rightarrow \infty} 
2\pi \sqrt{\alpha}\, \rho \, S_{2}^{\rm
 hard}
\left(\alpha + 2\pi \sqrt{\alpha}\, 
\rho x, \alpha + 2\pi \sqrt{\alpha}\, \rho y
; t_{x}, t_{y}
\right)} \quad \quad \quad \quad \quad
\nonumber \\
& \sim & \rho \int_{0}^{1}\cos(\pi u \rho (x-y))\, e^{-u^{2}(t_{x}-t_{y})}\, du
\, ,
\label{5.17} \\
\lefteqn{\lim_{\alpha \rightarrow \infty} 2\pi \sqrt{\alpha}\, \rho
\, \tilde{S}_{2}^{\rm hard} 
\left(\alpha + 2\pi \sqrt{\alpha}\, \rho x, \alpha +
 2\pi
\sqrt{\alpha}\, \rho y; t_{x}, t_{y}\right) }
\quad \quad \quad \quad \quad \nonumber \\
& = & -\rho \int_{1}^{\infty}\cos(\pi u \rho (x-y))\, e^{-u^{2}(t_{x}-t_{y})}\,
du \, .
\label{5.18}
\eeqa
Substituting these 
formulas in (\ref{5.5}) and (\ref{5.6}) and also making the 
change of
scale $t \mapsto (\pi \rho)^{2}t/2$ reclaims the known formula for the bulk
dynamical distributions \cite{NF98b}.

In fact the asymptotic behaviour 
(\ref{5.17}) and (\ref{5.18}) of $S_{\beta}^{\rm
 hard}$
and $\tilde{S}_{\beta}^{\rm hard}$ for $\beta = 2$ 
initial conditions persists for
$\beta
= 1$ and $\beta = 4$ 
initial conditions. This follows from application of (\ref{5.26})
in the exact results 
(\ref{3.20'}), (\ref{m.2}) and (\ref{m.3}), (\ref{m.4}). It
 remains
to consider 
$\tilde{I}_{\beta}$ and $D_{\beta}$. For $\beta = 1$ initial conditions
application of (\ref{5.16}) in (\ref{3.22}) and (\ref{3.23}) shows
\beqa
\lefteqn{\lim_{\alpha \rightarrow \infty} 2\pi \rho \, \tilde{I}_{1}^{\rm hard}
\left(\alpha + 2\pi \sqrt{\alpha}\, \rho x, \alpha + 2\pi \sqrt{\alpha}\,
\rho y; t_{x}, t_{y}\right)} \quad \quad \quad \quad \quad
\nonumber \\
& = & \rho \int_{1}^{\infty}du \,
\frac{e^{-u^{2}(t_{x}+t_{y})}}{u}\sin(\pi u \rho (y-x)) \, ,
\label{5.19} \\
\lefteqn{\lim_{\alpha \rightarrow \infty} 2\pi \rho \alpha \, D_{1}^{\rm hard}
\left(\alpha + 2\pi \sqrt{\alpha}\, 
\rho x, \alpha + 2\pi \sqrt{\alpha}\, \rho y
;
t_{x}, t_{y}\right)} \quad \quad \quad \quad \quad
\nonumber \\
& = & \rho \int_{0}^{1}du \,
u\, e^{u^{2}(t_{x}+t_{y})}\sin(\pi u \rho (y-x)) \, ,
\label{5.20}
\eeqa
while for $\beta = 4$ 
initial conditions application of (\ref{5.16}) in (\ref{3.35}) and
(\ref{3.38}) shows
\beqa
\lefteqn{\lim_{\alpha 
\rightarrow \infty} 2\pi \rho \alpha \, \tilde{I}_{4}^{\rm
 hard}
\left(\alpha + 2\pi 
\sqrt{\alpha}\, \rho x, \alpha + 2\pi \sqrt{\alpha}\, \rho y
;
t_{x}, t_{y}\right) } \quad \quad \quad \quad \quad
\nonumber \\
& = & \rho \int_{1}^{\infty}du \,
u\, e^{-u^{2}(t_{x}+t_{y})}\sin(\pi u \rho (y-x))  \, ,
\label{5.21} \\
\lefteqn{\lim_{\alpha \rightarrow \infty} 2\pi \rho \, D_{4}^{\rm hard}
\left(\alpha + 2\pi 
\sqrt{\alpha}\, \rho x, \alpha + 2\pi \sqrt{\alpha}\, \rho y
;
t_{x}, t_{y}\right) } \quad \quad \quad \quad \quad
\nonumber \\
& = & \rho \int_{0}^{1}du \,
\frac{e^{u^{2}(t_{x}+t_{y})}}{u}\sin(\pi u \rho (y-x))  \, .
\label{5.22}
\eeqa
After scaling $t \mapsto (\pi \rho)^{2}t/2$, the known formulas for
$\rho_{(1+1)}(x, y; t_{x}, t_{y})$ with 
$\beta = 1$ and $\beta = 4$ initial conditions
\cite{Fo96,FN97} are reproduced by these results.

In the case of the soft edge connecting to the bulk, similar formulas are found
to
hold. These formulas are derived from the asymptotic expansion
\beqa
{\rm Ai}(-x) \mathop{\sim}\limits_{x \to \infty}
\frac{1}{\pi^{1/2}x^{1/4}} \cos(2x^{3/2}/3 - \pi/4) \,  .
\label{5.23}
\eeqa
Consider for example $S_{2}^{\rm soft}$ as specified by (\ref{5.7}).  We first
change variables 
$v \mapsto \alpha(1-u)$ for $0 < v < \alpha$, and replace the Airy
functions in the integrand according to (\ref{5.23}). Noting that
\beqa
\frac{2}{3}\left\{
(\alpha + \pi \rho x /\sqrt{\alpha} - v)^{3/2} -
(\alpha + \pi 
\rho y /\sqrt{\alpha} - v)^{3/2}\right\} \sim \pi \rho u^{1/2}(x-y)\, ,
\nonumber
\eeqa
we see that if we also scale $t$ according to
\beqa
t \mapsto t/\alpha
\label{5.24}
\eeqa
then $S_{2}^{\rm soft}$ has the asymptotic form
\beqa
\lefteqn{\lim_{\alpha \rightarrow \infty} (-\pi \rho /\sqrt{\alpha})\,  
S_{2}^{\rm soft}
(-(\alpha + \pi \rho x /\sqrt{\alpha}), -(\alpha + \pi \rho y/\sqrt{\alpha});
t_{x}/\alpha , t_{y}/\alpha )} \quad \quad \quad \quad
\nonumber \\
& \sim & e^{-(t_{x}-t_{y})}
\rho \int_{0}^{1}\cos(\pi u \rho (x-y))\, e^{-u^{2}(t_{x}-t_{y})}\, du \, .
\label{5.25}
\eeqa
Apart from the factor of $e^{-(t_{x} - t_{y})}$ this is the same result as (\ref
{5.17}).
A similar calculation 
shows the asymptotic form of $\tilde{S}_{2}^{\rm soft}$ is
given by (\ref{5.18}) except for an additional factor of $e^{-(t_{x} -t_{y})}$.
This shows
that this additional factor cancels from the formula (\ref{2.s}) for the
distribution functions. 
The final result is that the bulk dynamical distributions
 are
reclaimed from the soft edge results for each of the three distinct initial
conditions. (As in the hard edge case a final rescaling $t \mapsto (\pi \rho)^{2
}t/2$
is required).


\subsection{Asymptotic  form of $\rho_{(1+1)}^{T}(X, Y; t)$}

The dynamical density-density correlation function between an eigenvalue  with
value $X$ initially, and an eigenvalue with value $Y$ and parameter $\tau$ is
defined in terms of the distribution function (\ref{2.c}) by
\beqa
\rho_{(1+1)}^{T}(x, y; \tau) = \rho_{(1+1)}(x; 0; y; \tau)
- \rho_{(1)}(x; 0) \, \rho_{(1)}(y; \tau) \,   .
\label{5.26}
\eeqa
According to (\ref{2.s}) and (\ref{2.1b}) we have that in the finite system
\beqa
\rho_{(1+1)}^{T}(x, y; \tau) = - \left( S(x, y; 0, \tau) \,
\tilde{S}(y, x; \tau, 0) - \tilde{I}(x, y; 0, \tau) \, D(x, y; 0, \tau) \right)
\,  .
\label{5.27}
\eeqa
For the Laguerre ensemble at the hard edge we define the corresponding scaled
correlation $\rho_{(1+1)}^{T \, \rm{hard}}$ by
\beqa\lefteqn{
\rho_{(1+1)}^{T \, \rm{hard}}(X, Y; t) =
\lim_{N \rightarrow \infty} \left( \frac{1}{4N}\right)^{2}  
\rho_{(1+1)}^{T}\left( \frac{X}{4N},  \frac{Y}{4N}; \frac{t}{2N} \right) }
\nonumber \\
&  & = - \left( S^{\rm hard}_{\beta}(X, Y; 0, t) \,
\tilde{S}_{\beta}^{\rm hard}(Y, X; t, 0)  
 - \tilde{I}_{\beta}^{\rm hard}(X, Y; 0, t) \,
D_{\beta}^{\rm hard}(X, Y; 0, t) \right) \,  ,
\label{5.28}
\eeqa
where $\beta = 1, 2$ or 4 depending on the initial conditions, while for the
Gaussian ensemble at the soft edge the scaled correlation
$\rho_{(1+1)}^{T \, \rm{soft}}$ is defined by
\beqa
\rho_{(1+1)}^{T \, \rm{soft}}(X, Y; t) & = &
\lim_{N \rightarrow \infty} \left( \frac{1}{2^{1/2}N^{1/6}}\right)^{2}
\rho_{(1+1)}^{T}\left( \sqrt{2N} + \frac{X}{2^{1/2}N^{1/6}},
\sqrt{2N} + \frac{Y}{2^{1/2}N^{1/6}}; \frac{t}{N^{1/3}} \right)
\nonumber \\
& = & - \left( S^{\rm soft}_{\beta}(X, Y; 0, t) \,
\tilde{S}_{\beta}^{\rm soft}(Y, X; t, 0) -
\tilde{I}_{\beta}^{\rm soft}(X, Y; 0, t) \,
D_{\beta}^{\rm soft}(X, Y; 0, t) \right)   .
\nonumber \\
\label{5.29}
\eeqa
The asymptotic 
form of $\rho_{(1+1)}^{\rm{hard}}(X, Y; t)$ for large $|X - Y|$ and $t$
is of interest in applications of the parameter dependent Laguerre ensemble to
transport in mesoscopic systems \cite{Ma296}.  To deduce this asymptotic form, a
hydrodynamical approximation to the corresponding Fokker-Planck equation was
made which implied
\beqa
\int_{0}^{\infty} \int_{0}^{\infty} (4XY) \,
\rho_{(1+1)}^{T \, {\rm hard}}\left( X^{2}, Y^{2}; t \right) \,
\cos(kX) \, \cos(kY) \, dX \, dY
\mathop{\sim} \limits_{k \to 0 \atop t \to \infty}
\frac{|k|}{2\beta}\, e^{-2t|k|}
\label{5.30}
\eeqa
(eq.\ (80) of \cite{Ma296} with $\pi \rho \delta u^{2}/\gamma = 2t$).
On the other hand we can easily check that
\beqa
{\rm Re}\left( \frac{1}{(v + u + 2it)^{2}} + \frac{1}{(v - u - 2it)^{2}} \right)
= -2 \int_{0}^{\infty} dk \, ke^{-2kt} \cos(kv) \cos(ku) \,  .
\label{5.30'}
\eeqa
Taking the inverse transform of this result and comparing with (\ref{5.30})
shows that the latter formula is equivalent to
\beqa
(4XY) \rho_{(1+1)}^{T \, {\rm hard}} \left(X^{2}, Y^{2}; t \right)
\mathop{\sim}\limits_{X,Y,t \to \infty}
-\frac{1}{\pi^{2} \beta}
{\rm Re}\left( \frac{1}{(X + Y + 2it)^{2}} + \frac{1}{(X - Y + 2it)^{2}} \right)
\label{5.31}
\eeqa
for the leading non-oscillatory behaviour.

The prediction 
(\ref{5.1}) can readily be checked on the exact formula (\ref{5.28})
with $\beta = 1, 2$ and 4 initial conditions.  The simplest case is $\beta = 2$
initial conditions, when the product
$\tilde{I}_{\beta}^{\rm hard}\tilde{D}_{\beta}^{\rm hard}$ 
in (\ref{5.28}) vanishes.
To analyze $S_{2}^{\rm hard}$  and
$\tilde{S}_{2}^{\rm hard}$ 
we make use of the asymptotic expansion (\ref{5.16}),
and furthermore expand the integrands about their endpoint $u = 1$. Integration
by
parts then gives
\beqa
S_{2}^{\rm hard}\left(X^{2}, Y^{2}; 0, t \right)
& \sim & \frac{e^{t}}{2\pi (XY)^{1/2}} \, {\rm Re}
\left(\frac{e^{i(X-Y)}}{-i(X-Y) - 2t} +
\frac{e^{i((X+Y) - \pi \alpha /2 - \pi/2)}}{-i(X+Y) - 2t} \right) \, ,
\nonumber \\
\label{5.32} \\
\tilde{S}_{2}^{\rm hard}\left(Y^{2}, X^{2}; t, 0 \right)
& \sim & \frac{e^{-t}}{2\pi (XY)^{1/2}} \, {\rm Re}
\left(\frac{e^{i(X-Y)}}{i(X-Y) - 2t} +
\frac{e^{i((X+Y) - \pi \alpha /2 - \pi/2)}}{i(X+Y) - 2t} \right) \, ,
\nonumber \\
\label{5.33}
\eeqa
and these formulas when substituted in (\ref{5.28}) imply the result (\ref{5.31}
)
with $\beta = 2$. 
In the case of $\beta = 1$ and $\beta = 4$ initial conditions,
similar analysis shows
\beqa
\lefteqn{\tilde{I}_{\beta}^{\rm hard}\left(X^{2}, Y^{2}; 0, t \right)
D_{\beta}^{\rm hard}\left(X^{2}, Y^{2}; 0, t \right)} \quad \quad \quad \quad
\nonumber \\
& \sim & \chi_{\beta} \tilde{S}_{\beta}^{\rm hard}\left(X, Y; 0, t \right)
\tilde{S}_{\beta}^{\rm hard}\left(Y, X; t, 0 \right)
\nonumber \\
& \sim &  \chi_{\beta}\frac{1}{4XY}\, \frac{1}{2\pi^{2}}
{\rm Re}
\left( \frac{1}{(X + Y + 2it)^{2}} + \frac{1}{(X - Y + 2it)^{2}} \right),
\label{5.34}
\eeqa
where 
$\chi_{\beta} = -1$ for $\beta = 1$ and 
$\chi_{\beta} = 1/2$ for $\beta = 4$,  and
the asymptotics 
refer to the leading non-oscillatory term. Thus (\ref{5.31}) again
remains valid.

Let us now turn our 
attention to the same asymptotic limit for the soft edge. There
it is known that the asymptotic form (\ref{5.31}) for $X, Y \rightarrow \infty$
is
valid in 
the static theory ($t = 0$) \cite{JF94}. It turns out that the exact results
for (\ref{5.29}) satisfy (\ref{5.31}) for $X, Y \rightarrow \infty$ and $t
\rightarrow \infty$, as just demonstrated for the hard edge correlations. Thus,
for
$\beta = 2$ initial conditions, 
use of the asymptotic expansion  (\ref{5.23}) in
(\ref{5.7}) and (\ref{5.8}) shows
\beqa
\lefteqn{S_{2}^{\rm soft}\left(-X^{2}, -Y^{2}; 0, t \right) } \quad \quad \quad
\nonumber \\
& \sim & \frac{1}{2 \pi (XY)^{1/2}} \, {\rm Re}
\left(\frac{e^{2i(X^{3}+Y^{3})/3 - iv(X+Y) - \pi i/2}}{i(X+Y) + t} +
\frac{e^{2i(X^{3}-Y^{3})/3 - iv(X-Y)}}{i(X-Y) + t}\right) \, ,
\nonumber \\
\lefteqn{\tilde{S}_{2}^{\rm soft}\left(-Y^{2}, -X^{2}; t, 0 \right)} 
\quad \quad
\quad
\nonumber \\
& \sim & \frac{1}{2 \pi (XY)^{1/2}} \, {\rm Re}
\left(\frac{e^{2i(X^{3}+Y^{3})/3 - iv(X+Y) - \pi  i/2}}{i(X+Y) - t} +
\frac{e^{2i(X^{3}-Y^{3})/3 - iv(X-Y)}}{i(X-Y) - t}\right) \, ,
\nonumber
\eeqa
and these formulas when substituted in (\ref{5.29}) (with
$\tilde{I}_{2}^{\rm soft}  D_{2}^{\rm soft} = 0$) gives the asymptotic form
(\ref{5.31}) (although $t$ therein must be rescaled by replacing $2t$ with $t$).
The same conclusion is reached for $\beta = 1$ and 4 initial conditions, where
we find the analogue of the formula (\ref{5.34}).

As pointed out 
in \cite{Ma296}, a consequence of the asymptotic form (\ref{5.31})
is a universal formula 
for the time displaced covariance of two linear statistics
\beqa
A_{t} = \sum_{j=1}^{N} a\left( x_{j}^{2}(t)\right) \, , \quad \quad
B_{t} = \sum_{j=1}^{N} b\left( x_{j}^{2}(t)\right) \,  .
\nonumber
\eeqa
Thus, if in the general formula
\beqa
{\rm Cov}(A_{0}, B_{t}) = \int_{0}^{\infty}dx \, a(x^{2}) \,
\int_{0}^{\infty}dy \, b(y^{2}) (4xy) \rho_{(1+1)}^{T}(x^{2}, y^{2}; t)
\nonumber
\eeqa
we suppose $a(x^{2})$ and $b(x^{2})$ are made slowly varying by writing
\beqa
a(x^{2}) \mapsto a((x/\alpha)^{2}) \, , \quad \quad
b(x^{2}) \mapsto b((x/\alpha)^{2}) \, ,
\nonumber
\eeqa
where $\alpha \gg 1$, and if we scale $t$ according to
\beqa
t \mapsto \alpha \, t \,   ,
\nonumber
\eeqa
then a simple change of variables and use of (\ref{5.31}) shows that for
$\alpha \rightarrow \infty$
\beqa
{\rm Cov}(A_{0}, B_{t}) & \sim & -\frac{1}{\pi^{2}\beta}
\int_{0}^{\infty} dx \, a(x^{2}) \int_{0}^{\infty} dy \, b(y^{2})
{\rm Re} \left( \frac{1}{(X+Y+2it)^{2}} + \frac{1}{(X-Y+2it)^{2}}\right)
\nonumber \\
& = & \frac{2}{\pi^{2} \beta} \int_{0}^{\infty} dk \, k \,
\tilde{a} (k) \,  \tilde{b} (k) \,  e^{-2kt} \,  ,
\label{5.35}
\eeqa
where the equality follows from (\ref{5.30'}), and
\beqa
\tilde{a} (k) := \int_{0}^{\infty} a(x^{2}) \cos(kx)\, dx
\nonumber
\eeqa
and similarly the meaning of $\tilde{b} (k)$.
