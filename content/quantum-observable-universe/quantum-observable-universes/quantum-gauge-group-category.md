The
([quantum gauge group](#def\:quantum-gauge-group)) is realised pointwise by
the Hopf algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ of regular
functions on $\mathrm{SU}_{q(p)}(2)$. The categorical view replaces
each fibre with its representation category
$\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$, a :refterm[braided monoidal category]{#braided-monoidal-category}.
Tannaka--Krein duality reconstructs $\mathcal{O}_{q(p)}$ from
$\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ via
$\mathrm{End}^{\otimes}(\tau)$, where $\tau$ is the forgetful
fibre functor. For any two points $p, p' \in M$ connected by a
path $\gamma$, the passage between fibres is captured by the
commutative square

```tex
\begin{equation}\label{eq:tannaka-krein-functoriality}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \mathcal{O}_{q(p)}(\mathrm{SU}(2))
    \ar[r, "\mathrm{Rep}"]
    \ar[d, "\text{transition along } \gamma"']
  & \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))
    \ar[d, "\text{monoidal functor}"]
  \\
  \mathcal{O}_{q(p')}(\mathrm{SU}(2))
    \ar[r, "\mathrm{Rep}"']
  & \mathrm{Rep}(\mathrm{SU}_{q(p')}(2))
\end{tikzcd}
\end{equation}
```

Tannaka--Krein reconstruction inverts the horizontal arrows, so the
Hopf-algebra and representation-category viewpoints are equivalent
fibrewise.
