**Definition.**
*The **confinement category** $\mathbf{Conf}$ has:*

- ***Objects:** confined particles $P$ at every level $\ell \ge 0$.*
- ***Morphisms:** structure-preserving maps organised into three families:*

| *Family* | *Symbol* | *Action* |
|---|---|---|
| *Unfolding* | $\uparrow_\ell$ | *Replace each level-$\ell$ strand by its level-$(\ell-1)$ constituent braid* |
| *Folding* | $\downarrow_\ell$ | *Quotient a subbraid at level $\ell-1$ to a single level-$\ell$ strand* |
| *Dressing* | $\mathrm{dress}$ | *Extend $H_n(R, q) \hookrightarrow H_{n+m}(q)$ and attach $m$ additional strands via an SDP-feasible binding subword* |

- ***Composition:** concatenation of Hecke-algebra embeddings. We right-compose $\mathrm{dress}$ with $\uparrow_\ell$ and $\downarrow_\ell$.*
- ***Identity:** the identity embedding $\mathrm{id}_P: H_{n_0}(q) \hookrightarrow H_{n_0}(q)$.*

*Unfolding and folding are mutually inverse when restricted to particles whose coarse representation captures the full partition content. The morphism $\mathrm{dress}$ is generally not invertible because the binding subword may not be uniquely reversible.*

**Functoriality of the Markov trace.**
*The Markov trace $\mathrm{tr}_M$ extends to a functor*

$$
  \mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)
$$

*sending every confined particle to its trace value and every morphism to the induced trace transformation. The trace $\mathrm{tr}_M$ is invariant under $\uparrow_\ell$ and $\downarrow_\ell$. Under $\mathrm{dress}$, it multiplies by the binding weight determined by the active support.*

**Example: The atomic chain.**
*The chain $\mathrm{quark} \xrightarrow{\downarrow_1} \mathrm{nucleon} \xrightarrow{\downarrow_2} \mathrm{atom} \xrightarrow{\mathrm{dress}} \mathrm{neutral\ atom} \xrightarrow{\downarrow_3} \mathrm{molecule}$ is a composite morphism in $\mathbf{Conf}$ taking free quarks to a bonded molecule by successive foldings and one dressing. Each arrow preserves or extends the Markov trace.*
