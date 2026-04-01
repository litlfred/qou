Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([quantum observable universe](#def:quantum-observable-universe))
with Frobenius form $\lambda \colon A \to \mathbf{1}$ and substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter)).

An *observation* is an endomorphism $O \colon A \to A$ in $\mathbf{C}$
satisfying two conditions:

1. **Frobenius compatibility.**  The Frobenius form is preserved:

   ```tex
   \begin{equation}\label{eq:observation-frobenius}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A \ar[r, "O"] \ar[dr, "\lambda"']
     & A \ar[d, "\lambda"] \\
     & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   Measurement is consistent: $\lambda \circ O = \lambda$.

2. **Adjoint backreaction.**  The endomorphism $O$ induces a
   substrate shift $\delta q \colon \mathbf{1} \to \mathbf{1}$ via
   the Hopf coaction:

   ```tex
   \begin{equation}\label{eq:observation-substrate}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A \ar[r, "\Delta"] \ar[d, "O"']
     & A \otimes A \ar[r, "O \otimes S"]
     & A \otimes A \ar[d, "\mu"] \\
     A \ar[rr, "\lambda"']
     & & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   with $\delta q = \lambda\bigl(O(a_{(1)})\,S(a_{(2)})\bigr)$.
   The observation shifts $q \mapsto q + \delta q$ through the
   colour fibre.

The two conditions correspond to the two physical roles of measurement:

- **Receiving (Frobenius compatibility):** the observation reads the
  state by pairing with $\lambda$ — this is the passive aspect.
  The trace is preserved, so the measurement is self-consistent.

- **Sending back (backreaction):** the Hopf coaction carried by $O$
  conjugates the gauge degrees of freedom via the antipode $S$,
  feeding the measurement result back into the substrate parameter.
  This is the active aspect: observing the universe changes it.

A *categorical point*
([categorical point](#def:categorical-point))
$p \colon \mathbf{1} \to A$ gives the fermion or boson that is being
observed.  The composition $O \circ p \colon \mathbf{1} \to A$ is the
post-observation state.

In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)),
an observation $O \colon A \to A$ is concretely realised as a
gauge-equivariant continuous open endomorphism of the state bundle
$\mathcal{S} \to M$
([archimedean observation](#rem:observation-archimedean)).
