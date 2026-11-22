---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-004-41-semiclassical-asymptotics-of-the-quantum-dilo
section_title: "Semiclassical asymptotics of the quantum dilogarithm"
section_number: 4.1
pages: 15-16
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
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
