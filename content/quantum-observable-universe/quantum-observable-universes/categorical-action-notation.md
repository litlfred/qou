Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)),
a connection $\nabla$ ([categorical connection](#def:categorical-connection)),
and a section $\psi \colon \mathbf{1} \to A$ (a "state").
The following notation is used in
[categorical action](#def:categorical-action):

- $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ is the
  *categorical trace* (the composition
  $\mathrm{coev} \to \mathrm{id} \to \mathrm{ev}$ via the rigid
  structure).
- $R_{\int} \in \mathrm{End}_{\mathbf{C}}(A)$ is the
  *Frobenius--Ricci endomorphism*: the curvature of the
  Frobenius form $\int_A$ itself, defined by
  $R_{\int} = (\mathrm{id}_A \otimes \int_A) \circ F_{\nabla_{\int}}$,
  where $\nabla_{\int}$ is the canonical connection on $A$ induced
  by $\int_A$ via $\nabla_{\int}(a) = \int_A(a_{(1)}) \otimes a_{(2)} - a \otimes 1$
  (Sweedler notation: $\Delta(a) = a_{(1)} \otimes a_{(2)}$,
  summation suppressed).
- $\mathrm{tr}_A \colon \mathrm{End}_{\mathbf{C}}(A \otimes \Omega^{\bullet}(A)) \to \mathrm{End}_{\mathbf{C}}(\Omega^{\bullet}(A))$ is the
  *partial trace* over the $A$ factor.
- $\psi^* = \int_A \circ S(\psi) \colon A \to \mathbf{1}$ is the
  *adjoint section* (antipode composed with the Frobenius form).
- $D_\nabla = q^{-1}\,\nabla + (1 - q^{-1})\,\iota_\xi\,\nabla$ is
  the *$q$-deformed covariant derivative*, where $\xi$ is the
  Reeb derivation of $A$
  ([Reeb decomposition](#ex:reeb-decomposition)).
