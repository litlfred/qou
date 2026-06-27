Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
and weight decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)).  The **$q$-deformed
exterior derivative** $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is

$$
  d_q =  q^{-1}d + (1 - q^{-1})\pi_V \circ d,
$$

where $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is the differential
of the non-commutative de Rham complex.  Equivalently, $d_q$ acts as
$q^{-1}d$ on horizontal forms and as $d$ on vertical forms:

```tex
\begin{equation}\label{eq:categorical-dq-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k_H(A) \ar[r, "d"] \ar[d, hook]
  & \Omega^{k+1}(A) \ar[r, "q^{-1}"]
  & \Omega^{k+1}(A) \\
  \Omega^k(A) \ar[rru, "d_q"']
\end{tikzcd}
\end{equation}
```

The *$q$-adjoint* $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$
is the adjoint of $d_q$ with respect to the dagger structure
([positive definite dagger](#prop:positive-definite-dagger)).
