Self-duality controlled the gauge sector; we now ask
how the deformed differential $d_q$ behaves under iteration.
The answer is that $d_q^2$ does not vanish in general, and the
obstruction is concentrated on non-Reeb-invariant forms. The
$q$-connection introduced here is the structural object whose
curvature absorbs that obstruction.

**$d_q^2$ does not vanish** (prop), with its proof, computes
the composition explicitly: $d_q^2 \alpha = q^{-1}(1 - q^{-1})
\omega_V \wedge_q [\xi, \alpha]$, where $\omega_V \in
\Omega^2(A)$ is the curvature of the weight decomposition.
The composition vanishes if and only if $q = 1$ or
$[\xi, \alpha] = 0$ — so on Reeb-invariant horizontal forms,
$d_q^2 = 0$ and the deformed complex behaves as a cochain
complex; everywhere else, the categorical de Rham complex fails
to be a complex. **Categorical $q$-deformed Lie bracket**
(def) records the parallel deformation on derivations: $[X, Y]_q
= q^{-1}[X, Y] + (1 - q^{-1})(\varTheta_A(X)[\xi, Y] -
\varTheta_A(Y)[\xi, X])$.

**$q$-deformed connection** (def) introduces $\nabla_q =
q^{-1}\nabla + (1 - q^{-1})(\iota_\xi \nabla) \varTheta_A$,
the $q$-deformation of the categorical connection.
**Existence of the categorical $q$-connection** (prop) and
**uniqueness of the categorical $q$-connection** (prop), each
with its proof block, fix $\nabla_q$ once $\nabla$ and the QOU
data are chosen. The next section, **$q$-Deformed operators**,
specialises this whole package to a concrete manifold $M$ and
writes the deformed operators in coordinate form.

_(draft.)_
