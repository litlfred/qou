---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-002-3-a-complex-double-contour-integral-formula-for
section_title: "A complex double contour integral formula for $\tau_{r}(M_{p/q})$"
section_number: 3
pages: 12-15
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.969
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent In this section we derive a complex double contour
integral formula for the RT--invariants $\tau_{r}(M_{p/q})$ by
using methods similar to Kashaev \cite{[14]}. When we consider
the expression for the summand in the multi sum
(\ref{eq:inv2}), we see that the expression as it stands only
makes sense for non-negative integers $m$. In order to make
sense of this expression for arbitrary complex values for $m$,
let us consider the quantum dilogarithm of Faddeev
$$
S_{\gamma}(\zeta) = \exp \left( \frac{1}{4} \int_{C_{R}}
\frac{e^{\zeta z}}{\sinh(\pi z)\sinh(\gamma z)z} \dte z\right)
$$
defined on
$\Delta_{\gamma} = \{ \zeta \in \C \; | \;
|\rea(\zeta)| < \pi +\gamma \; \}$,
where $\gamma \in ]0,1[$ and $C_{R}$ is the contour
$]-\infty,-R] + \Upsilon_{R} + [R,\infty[$, where
$\Upsilon_{R}(t)=R e^{\sqrt{-1}(\pi-t)}$, $t \in [0,\pi]$ and
$R \in ]0,1[$.

The function $S_{\gamma} : \Delta_{\gamma} \to \C$ is
holomorphic and it satisfies the following well-known
functional equation (see \cite{[7]} or \cite{[14]}).


\begin{lemma}\label{lem:functional}
For $\zeta \in \C$ with $|\rea (\zeta) | < \pi$ we have
$$
(1+e^{\I \zeta})S_{\gamma}(\zeta+\gamma) =
S_{\gamma}(\zeta-\gamma).
$$
\end{lemma}


For the sake of completeness we have given a proof in Appendix
A. We use \reflem{lem:functional} to extend $S_{\gamma}$ to a
meromorphic function on the complex plane $\C$.

From now on we fix $\gamma=\pi/r$ (so $r>3$).
By \reflem{lem:functional} we get that
$$
S_{\gamma}(\zeta) = S_{\gamma}(\zeta+2\pi)
\prod_{j=0}^{r-1} \left( 1 + e^{\I(\zeta+(2j+1)\pi/r)} \right).
$$
If we write $\zeta =-\pi+2\pi x$ we get that
$$
\prod_{j=0}^{r-1} \left( 1+e^{\I(\zeta +(2j+1)\pi/r)} \right)
= \prod_{j=0}^{r-1} \left( 1-w^{j}e^{2\pi\I (x+\frac{1}{2r})}
\right),
$$
where $w=e^{2\pi\I/r}$. Using
$1 - z^{r} = \prod_{j=0}^{r-1} (1-w^{j}z)$ we get that
\begin{equation}\label{eq:functional}
S_{\gamma}(-\pi+2\pi x) = \left(1+e^{2\pi \I xr} \right)
S_{\gamma}(-\pi+2\pi(x+1))
\end{equation}
for $x \in \C$. Let
$$
x_{n} = \frac{n}{r} + \frac{1}{2r}, \hspace{.2in} n \in \Z.
$$
Then $x \mapsto S_{\gamma}(-\pi+2\pi x)$ is analytic on
$\C \sm \{ x_{n} | n =r,r+1,\ldots \,\}$. If $m$ is a positive
integer then $\{ x_{n} | n = mr, mr+1,\ldots, (m+1)r-1 \,\}$
are poles of order $m$, while the points
$\{ x_{n} | n = -mr, -mr+1,\ldots, -mr+r-1 \,\}$ are zeros of
order $m$.

Let us use the function $S_{\gamma}$ to give another expression
for $\tau_{r}(M_{p/q})$. By \reflem{lem:functional} we have
that
$$
\prod_{l=0}^{m} (1-\xi^{k \pm l}) = \prod_{l=0}^{m}
\frac{S_{\gamma}(-\pi+2\gamma(k\pm l) -\gamma)}
     {S_{\gamma}(-\pi+2\gamma(k\pm l) +\gamma)}.
$$
Therefore
\begin{eqnarray*}
\prod_{l=0}^{m} (1-\xi^{k - l}) &=&
\frac{S_{\gamma}(-\pi+2\gamma(k - m) - \gamma)}
     {S_{\gamma}(-\pi+2\gamma k +\gamma)}, \\
\prod_{l=0}^{m} (1-\xi^{k + l}) &=&
\frac{S_{\gamma}(-\pi+2\gamma k -\gamma)}
     {S_{\gamma}(-\pi+2\gamma(k + m) +\gamma)}.
\end{eqnarray*}
So
$$
\prod_{l=0}^{m} (1-\xi^{k - l})(1-\xi^{k + l}) =
(1-\xi^{k})\frac{S_{\gamma}(-\pi+2\gamma(k - m) -\gamma)}
                {S_{\gamma}(-\pi+2\gamma(k + m) +\gamma)},
$$
and then by (\ref{eq:inv2})
$$
\tau_{r}(M_{p/q}) = \beta(r)\qsum \sum_{k=1}^{r-1}
\sum_{m=0}^{r-1} f_{n,r}\left( \frac{k}{r},\frac{m+1/2}{r}
\right),
$$
where
$$
f_{n,r}(x,y) = \sin\left(\frac{\pi}{q}(x-2nd)\right)
e^{2\pi i r \left( \frac{dn^{2}}{q} + \frac{p}{4q} x^{2}
                    -\frac{n}{q}x-xy\right)}
\frac{S_{\gamma}(-\pi+2\pi(x - y))}
     {S_{\gamma}(-\pi+2\pi(x + y))}
$$
and
\begin{eqnarray}\label{eq:betaconstant}
\beta(r) &=& -\frac{ia(r)}{2\sin(\pi/r)} \nonumber \\*
&=& \frac{i\sign(q)}{r\sqrt{|q|}}
    e^{-\frac{3\pi i}{4}\sign(pq)}
\exp\left(\frac{\pi i}{2r}\left[3\sign(pq)
   -\frac{p}{q}+\dS \left(\frac{p}{q}\right)\right]\right).
\end{eqnarray}
Note that $d$ is equal to the inverse of $p \bmod{q}$ and that
the functions $f_{n,r}$ are independent of the choice of this
inverse. By the remarks following \reflem{lem:functional} the
functions $f_{n,r}$ are holomorphic on
$\Omega_{r} \times \Omega_{r}$, where
\begin{equation}\label{eq:typicaldomain}
\Omega_{s} = \left\{ w \in \C \mid -\frac{1}{4s}
< \rea(w) < 1 + \frac{1}{4s} \; \right\}
\end{equation}
for $s \in ]0,\infty]$. By the residue theorem we therefore
end up with


\begin{lemma}\label{lem:contour}
The quantum invariants of $M_{p/q}$ are given by
$$
\tau_{r}(M_{p/q}) = \frac{\beta(r) r^{2}}{4} \qsum
  \int_{C_{r}^{1}} \cot(\pi r x)
   \left( \int_{C_{r}^{2}} \tan(\pi ry)
            f_{n,r}( x,y) \dte y \right) \dte x,
$$
where $\beta(r)$ is given by (\ref{eq:betaconstant}) and
$$
f_{n,r}(x,y) = \sin\left(\frac{\pi}{q}(x-2nd)\right)
e^{2\pi i r \left( \frac{dn^{2}}{q} + \frac{p}{4q} x^{2}
            -\frac{n}{q}x-xy\right)}
\frac{S_{\gamma}(-\pi+2\pi(x - y))}
{S_{\gamma}(-\pi+2\pi(x + y))},
$$
and where $C_{r}^{1}$ is a closed curve in $\Omega_{r}$ such
that the poles $\{ k/r \; | \; k = 1,2,\ldots,r-1 \; \}$ for
$x \mapsto \cot(\pi r x)$ lies inside $C_{r}^{1}$ and the poles
$0$ and $1$ lies outside $C_{r}^{1}$, and $C_{r}^{2}$ is a
closed curve in $\Omega_{r}$ such that the poles
$\{ (m+1/2)/r \; | \; m=0,1,\ldots,r-1 \; \}$ for
$y \mapsto \tan(\pi r y)$ lies inside $C_{r}^{2}$. Both curves
are oriented in the anti-clockwise direction.
\end{lemma}


Using the function $S_{\gamma}$ we can also express $J_{K}'(r)$
as a contour integral. By \reflem{lem:functional} we get that
$$
J_{K}'(r) = r \sum_{m=0}^{r-1}
\frac{S_{\gamma}(\pi-(2m+1)\gamma)}
     {S_{\gamma}(-\pi+(2m+1)\gamma)}.
$$
We have here used that
$$
\frac{S_{\gamma}(-\pi+\gamma)}{S_{\gamma}(\pi-\gamma)} =
\prod_{j=1}^{r-1}\frac{S_{\gamma}(\pi-(2j+1)\gamma)}
                      {S_{\gamma}(-\pi+(2j+1)\gamma)} =
\prod_{j=1}^{r-1}\left(1-e^{-2\pi\I\frac{j}{r}}\right) = r.
$$
If we put
$$
g_{r}(x) = \frac{S_{\gamma}(\pi-2\pi x)}
                {S_{\gamma}(-\pi + 2\pi x)}
$$
for $x \in \Omega_{\frac{1}{2}r}$ (see
(\ref{eq:typicaldomain})) we get
$$
J_{K}'(r) = r \sum_{m=0}^{r-1} g_{r}
\left(\frac{m+1/2}{r}\right),
$$
and we can write this sum as the single contour integral
\begin{equation}\label{eq:contourfigure8}
J_{K}'(r) = \frac{\I r^{2}}{2} \int_{C_{r}^{2}}
                        \tan(\pi rx) g_{r}( x) \dte x,
\end{equation}
where $C_{r}^{2}$ is given as in \reflem{lem:contour}.
