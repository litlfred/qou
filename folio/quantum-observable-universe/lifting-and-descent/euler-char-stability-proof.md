*Proof of (1).* The categorical trace $\mathrm{tr}(\mathrm{id}_{A_n}) = \mathrm{ev}_n \circ \mathrm{coev}_n$ is the rigidity trace of the identity, the composition $\mathbf{1} \xrightarrow{\mathrm{coev}_n} A_n \otimes A_n^{\vee} \xrightarrow{\mathrm{ev}_n} \mathbf{1}$; in a pivotal category this is the quantum dimension $\dim_q(A_n)$.

Jet prolongation is a functor on $\mathbf{C}$ that preserves the Frobenius–Hopf structure ([jet prolongation](#prop:jet-prolongation)): the prolonged object $A_{n+1}$ inherits its rigidity data from $A_n$. Specifically, the unit $\eta_{n+1}$ and counit $\varepsilon_{n+1}$ of $A_{n+1}$ are the images of $\eta_n$ and $\varepsilon_n$ under the prolongation functor, and likewise for the evaluation and coevaluation morphisms: $\mathrm{ev}_{n+1} = \mathrm{ev}_n$ and $\mathrm{coev}_{n+1} = \mathrm{coev}_n$ as elements of $\mathrm{Hom}(\mathbf{1}, \mathbf{1}) \cong R$.

Therefore

$$
  \mathrm{tr}(\mathrm{id}_{A_{n+1}})
  =
  \mathrm{ev}_{n+1} \circ \mathrm{coev}_{n+1}
  =
  \mathrm{ev}_n \circ \mathrm{coev}_n
  =
  \mathrm{tr}(\mathrm{id}_{A_n}),
$$

and by induction $\mathrm{tr}(\mathrm{id}_{A_n}) = \mathrm{tr}(\mathrm{id}_{A_0})$ for all $n \geq 0$. The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ensures that the prolongation functor cannot introduce non-trivial twisting of the trace: there are no non-scalar $G_q$-invariant endomorphisms that could modify the rigidity pairing at each level. This proves the stability of the categorical trace; it says nothing about the base. $\square$
