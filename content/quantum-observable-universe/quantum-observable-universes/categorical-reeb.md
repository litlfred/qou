Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
maximal torus $T$ ([maximal torus](#def:maximal-torus)) and weight
decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)). The *categorical
Reeb derivation* is the endomorphism $\xi \colon A \to A$ that
generates the $T$-action: $\xi$ is the infinitesimal generator of the
one-parameter subgroup $T \cong \mathrm{U}(1) \subset G$, acting on
the Frobenius--Hopf object $A$ via the adjoint coaction. It satisfies:

1. **Vertical generator:**
   $\pi_V \circ d = \iota_\xi d\varTheta_A$, where
   $\iota_\xi$ denotes the interior product (contraction with $\xi$)
   and $\varTheta_A \in \Omega^1(A)$ is the canonical $1$-form dual to
   $\xi$.
2. **Normalisation:**
   $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$.
3. **Kernel:**
   $\Omega^k_H(A) = \ker(\iota_\xi)$ (horizontal forms are
   precisely those annihilated by contraction with $\xi$).

```tex
\begin{equation}\label{eq:reeb-decomposition-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_H"] \ar[d, "\pi_V"']
  & \Omega^k_H(A) \ar[d, hook] \\
  \varTheta_A \wedge \Omega^{k-1}_H(A) \ar[r, hook]
  & \Omega^k(A)
\end{tikzcd}
\qquad (\pi_H + \pi_V = \mathrm{id})
\end{equation}
```
