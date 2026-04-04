Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe)
with [substrate parameter](#def:substrate-parameter) $q > 1$,
[brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$,
and [quantum characteristic classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

We say that $(\mathbf{C}, A, \tau)$ **satisfies Navier--Stokes
regularity** if the following condition holds:

For every divergence-free $v_0 \in \ker(\delta_q|_{\Omega^1(A)})$
with finite Frobenius norm, and for every sequence
$q_j \to 1^+$ with $q_j > 1$, the family of
[q-NS solutions](#def:q-navier-stokes) $\{v_{q_j}\}$ converges
(in the sense of [q-Aubin--Lions](#thm:q-aubin-lions)) to a
limit $v^*$ that extends smoothly to all $t \geq 0$.

Equivalently, defining the **boundary observability** at $q = 1$:

$$
  \mathrm{Obs}_{\partial}(A)
  \;\equiv\;
  \lim_{q \to 1^+}
  \mathrm{Hom}_{\mathbf{C}_q}\!
  \bigl(\mathbf{1},\, \mathrm{Ad}(A_q)\bigr),
$$

the QOU satisfies NS regularity if and only if

$$
  \mathrm{Obs}_{\partial}(A) \;\neq\; 0.
$$

That is: NS regularity holds precisely when the
[observability axiom](#def:quantum-observable-universe) **fails**
in the boundary limit $q \to 1$.

The four cases:

| $\mathrm{Obs}_\partial(A)$ | Observability at boundary | Contact structure | NS regularity |
|---|---|---|---|
| $= 0$ | Survives (no new gauge modes) | Non-degenerate | **Fails** (blowup) |
| $\neq 0$ | Fails (gauge mode appears) | Degenerates | **Holds** (regular) |

**Notation.** We write **NS-regular** for a QOU satisfying the
above condition, and **NS-singular** for a QOU where the
boundary observability vanishes
($\mathrm{Obs}_\partial(A) = 0$), implying finite-time blowup
of the classical NS equation.
