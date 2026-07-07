<!-- FILE_START: dq-squared-intro.md -->
Self-duality controlled the gauge sector; we now ask
how the deformed differential $d_q$ behaves under iteration.
The answer is that $d_q^2$ does not vanish in general, and the
obstruction is concentrated on non-Reeb-invariant forms. The
$q$-connection introduced here is the structural object whose
curvature absorbs that obstruction.

Proposition: $d_q^2$ does not vanish, with its proof, computes
the composition explicitly: $d_q^2 \alpha = q^{-1}(1 - q^{-1})
\omega_V \wedge_q [\xi, \alpha]$, where $\omega_V \in
\Omega^2(A)$ is the curvature of the weight decomposition.
The composition vanishes if and only if $q = 1$ or
$[\xi, \alpha] = 0$ — so on Reeb-invariant horizontal forms,
$d_q^2 = 0$ and the deformed complex behaves as a cochain
complex; everywhere else, the categorical de Rham complex fails
to be a complex. Definition: Categorical $q$-deformed Lie bracket records the parallel deformation on derivations: $[X, Y]_q
= q^{-1}[X, Y] + (1 - q^{-1})(\varTheta_A(X)[\xi, Y] -
\varTheta_A(Y)[\xi, X])$.

Definition: $q$-deformed connection introduces $\nabla_q =
q^{-1}\nabla + (1 - q^{-1})(\iota_\xi \nabla) \varTheta_A$,
the $q$-deformation of the categorical connection.
Proposition: Existence of the categorical $q$-connection and
Proposition: uniqueness of the categorical $q$-connection, each
with its proof block, fix $\nabla_q$ once $\nabla$ and the QOU
data are chosen. The next section, **$q$-Deformed operators**,
specialises this whole package to a concrete manifold $M$ and
writes the deformed operators in coordinate form.

_(draft.)_
<!-- FILE_END: dq-squared-intro.md -->

<!-- FILE_START: categorical-dq-squared.md -->
Let $d_q$ be the categorical $q$-deformed exterior derivative
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)).  The composition
$d_q^2 = d_q \circ d_q \colon \Omega^k(A) \to \Omega^{k+2}(A)$ is
given by

$$
  d_q^2\alpha
  =  q^{-1}(1 - q^{-1})\omega_V \wedge_q [\xi, \alpha],
$$

where $\omega_V \in \Omega^2(A)$ is the curvature of the weight
decomposition (the image of the unit $1_A$ under
$\pi_V \circ d \circ d$) and $[\xi, \alpha]$ is the Lie derivative
along the generator $\xi$ of the $T$-action
([weight decomposition](#def:weight-decomposition)).  The following diagram
displays the obstruction to nilpotence:

```tex
\begin{equation}\label{eq:dq-squared-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k(A) \ar[r, "d_q"] \ar[dr, "d_q^2"']
  & \Omega^{k+1}(A) \ar[d, "d_q"] \\
  & \Omega^{k+2}(A)
\end{tikzcd}
\qquad
d_q^2 = 0 \Longleftrightarrow
q = 1  \text{ or } [\xi, \alpha] = 0.
\end{equation}
```

In particular, $d_q^2 \neq 0$ for generic $\alpha$ whenever
$q \neq 1$: the $q$-deformed de Rham complex is *not* a cochain
complex.  On $\xi$-invariant forms (the horizontal subcomplex
$\Omega^k_H(A)$), $d_q$ does reduce to $q^{-1} d$ and $d_q^2 = 0$.

While the case analysis resolving the vanishing conditions of $d_q^2$ relies on standard algebraic properties, identifying this specific $q$-curvature obstruction and demonstrating its explicit role in breaking the cochain property for generic non-invariant forms represents a mathematically novel application within the framework of categorical $q$-deformations.
<!-- FILE_END: categorical-dq-squared.md -->

<!-- FILE_START: categorical-q-lie-bracket.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)) and
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)).
The **$q$-deformed Lie bracket** on derivations of $A$ is

$$
  [X, Y]_q =  q^{-1}[X, Y]
  + (1 - q^{-1})\bigl(\varTheta_A(X)[\xi, Y]
                        - \varTheta_A(Y)[\xi, X]\bigr),
$$

where $\varTheta_A$ is the canonical $1$-form dual to $\xi$ and
$[X, Y]$ is the commutator of derivations in $\mathbf{C}$.

```tex
\begin{equation}\label{eq:q-lie-bracket-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathrm{Der}(A) \otimes \mathrm{Der}(A)
    \ar[r, "{[\cdot,\cdot]}"]
    \ar[d, "{[\cdot,\cdot]_q}"']
  & \mathrm{Der}(A) \\
  \mathrm{Der}(A)
    \ar[ur, equal, "q{=}1"']
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: categorical-q-lie-bracket.md -->

<!-- FILE_START: categorical-q-connection.md -->
Let $\nabla$ be a connection on $A$
([categorical connection](#def:categorical-connection)) and $\xi$ the Reeb
derivation ([categorical Reeb derivation](#def:categorical-reeb)).  The
**$q$-deformed connection** is

$$
  \nabla_q =  q^{-1}\nabla
  + (1 - q^{-1})(\iota_\xi \nabla)\varTheta_A.
$$

```tex
\begin{equation}\label{eq:q-connection-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\nabla"] \ar[dr, "\nabla_q"']
  & \Omega^1(A) \otimes A
    \ar[d, "q^{-1}\mathrm{id} + (1 - q^{-1})\varTheta_A \circ \iota_\xi"] \\
  & \Omega^1(A) \otimes A
\end{tikzcd}
\qquad\text{($q$-connection)}
\end{equation}
```

At $q = 1$, $\nabla_q = \nabla$.
<!-- FILE_END: categorical-q-connection.md -->

<!-- FILE_START: categorical-q-connection-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
categorical connection $\nabla$, substrate parameter $q$, and Reeb
derivation $\xi$.  Then the
[categorical $q$-connection](#def:categorical-q-connection)
$\nabla_q = q^{-1} \nabla + (1 - q^{-1}) \iota_\xi \nabla \circ \varTheta$
exists as a morphism $A \to \Omega^1(A)$.

Uniqueness is
([uniqueness of categorical $q$-connection](#prop:categorical-q-connection-unique)).


**Strategy.** We constructively define $\nabla_q$ as an explicit linear combination: $q^{-1} \nabla + (1 - q^{-1}) \iota_\xi \nabla \circ \varTheta$. Since the underlying categories are $R$-linear, and all composing terms exist by our hypotheses, this algebraic formulation immediately furnishes the required connection.
<!-- FILE_END: categorical-q-connection-exists.md -->

<!-- FILE_START: categorical-q-connection-unique.md -->
For fixed $\nabla$, $\xi$, $\varTheta$, and $q$, the
[categorical $q$-connection](#def:categorical-q-connection) is
uniquely determined by its defining formula.  Up to gauge (which
acts on $\nabla$), the $q$-connection inherits the gauge freedom
of its base connection.


**Strategy.** Because the $q$-deformed connection $\nabla_q$ is defined as a fixed algebraic deformation of $\nabla$, any distinct choice for $\nabla_q$ would require a distinct $\nabla$. Consequently, $\nabla_q$ inherits precisely the gauge freedom of $\nabla$, without introducing new degrees of freedom.
<!-- FILE_END: categorical-q-connection-unique.md -->

