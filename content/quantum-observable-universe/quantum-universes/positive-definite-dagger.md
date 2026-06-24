Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with
[Frobenius pairing](#def:frobenius-pairing)
$\langle a, b \rangle = \int_A(\mu(a \otimes b))$ and antipode $S$.
Define the *Frobenius dagger* on morphisms by

$$
  f^{\dagger} =  \int_A \circ \mu(S(f) \otimes -).
$$

Then $\dagger$ is a positive-definite involutive structure on
$\mathbf{C}$: for every non-zero morphism
$f \colon \mathbf{1} \to X$, the composite
$f^{\dagger} \circ f$ is a positive element of
$\mathrm{End}(\mathbf{1}) \cong R$.

## Proof (sketch)

Write $\langle a, b\rangle = \int_A \mu(a \otimes b)$ for the Frobenius
pairing, non-degenerate by
[Frobenius pairing exists](#prop:frobenius-pairing-exists).

1. **$\dagger$ is involutive.** Expanding
   $(f^{\dagger})^{\dagger} = \int_A \mu(S(f^{\dagger}) \otimes -)$ and
   using the antipode condition $S^2 = \mathrm{id}$ together with
   Frobenius associativity
   $\int_A \mu(\mu \otimes \mathrm{id}) = \int_A \mu(\mathrm{id} \otimes \mu)$
   gives $(f^{\dagger})^{\dagger} = f$.

2. **Positive-definiteness.** For non-zero $f \colon \mathbf{1} \to X$,
   $f^{\dagger} \circ f = \int_A \mu(S(f) \otimes f) = \langle f, f\rangle
   \in \mathrm{End}(\mathbf{1}) \cong R$
   is the Frobenius norm of $f$. Non-degeneracy of the pairing forces
   $\langle f, f\rangle \neq 0$; in the rigid pivotal (self-dual)
   structure it is a square in $R$, hence a positive element. So
   $\dagger$ is a positive-definite involutive structure on $\mathbf{C}$.

This is the categorical analogue of the Frobenius-norm / GNS positivity
construction (\cite{kock2004}, Ch. 2). The Lean sibling states existence of a
`PositiveDefiniteStructure` and defers the construction via `sorry`
(`-- Ref: [manuscript]`). $\square$
