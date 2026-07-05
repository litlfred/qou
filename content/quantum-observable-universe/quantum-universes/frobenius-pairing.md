The structure that makes $A$ self-dual and equips it with a
categorical trace is a pairing $A \otimes A \to \mathbf{1}$ built from
its multiplication and Frobenius form; we record it here before using
it. The motivating instance is the quantum-dimension pairing of
$\mathbf{Rep}(\mathrm{SU}_q(2))$ (see
[example](#ex:frobenius-pairing-su2)); the general definition abstracts
it as follows. Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with multiplication
$\mu \colon A \otimes A \to A$ and Frobenius form
$\int_A \colon A \to \mathbf{1}$. The **Frobenius pairing** is the
composite

```tex
\begin{equation}\label{eq:frobenius-pairing}
\begin{tikzcd}[column sep=2.5em]
  A \otimes A \ar[r, "\mu"]
  & A \ar[r, "\int_A"]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

We say the Frobenius pairing is *non-degenerate* when this composite
induces an isomorphism $A \xrightarrow{ \sim } A^{\vee}$ to the
dual object. Equivalently, the standard snake identities hold: there exists a
coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ such
that the two composites (where $\alpha$ is the associator and
$\rho$, $\lambda_A$ are the right and left unitors of $\mathbf{C}$)

$$
A \xrightarrow{\rho^{-1}} A \otimes \mathbf{1}
  \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A
  \xrightarrow{\alpha^{-1}} (A \otimes A) \otimes A
  \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} \mathbf{1} \otimes A
  \xrightarrow{\lambda_A} A
$$

and its mirror are both equal to $\mathrm{id}_A$. For
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ this recovers the
quantum-dimension pairing (see [example](#ex:frobenius-pairing-su2)).
