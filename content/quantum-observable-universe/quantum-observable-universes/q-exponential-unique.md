Any two grouplikes $e_1, e_2 \in G(H_q)$ satisfying the flow equation
$D_q e_i = e_i$ and the counit normalisation $\epsilon(e_i) = 1$
coincide:

$$
  e_1 \;=\; e_2.
$$

**Proof sketch.**  The difference $e_1 - e_2$ is primitive (a
consequence of $\Delta_q e_i = e_i \otimes e_i$ minus itself in the
linearisation) and satisfies $D_q (e_1 - e_2) = e_1 - e_2$.  The flow
equation on primitives has only the trivial solution: iterating
$D_q$ on a primitive with bounded degree forces all coefficients to
vanish except the leading one, and the counit condition kills the
constant term.  Hence $e_1 - e_2 = 0$.

Equivalently, $\exp_q$ is the *unique* fixed point of the linear
endomorphism $D_q$ on the group of grouplikes with trivial counit —
a categorical fact that holds over any base ring $R$ in which the
flow equation has at least one solution
([existence of $\exp_q$](#prop:q-exponential-exists)).
