**Definition.**
*The **confinement category** $\mathbf{Conf}$ has:*

- ***Objects:** [confined particles](#def:confined-particle) $P$ at
  every level $\ell \ge 0$ (quark, nucleon, atom, compound).*
- ***Morphisms:** structure-preserving maps organised into three
  families:*

| *Family* | *Symbol* | *Action* |
|---|---|---|
| *Unfolding* | $\uparrow_\ell$ | *Replace each level-$\ell$ strand by its level-$(\ell-1)$ constituent braid* |
| *Folding* | $\downarrow_\ell$ | *Quotient a subbraid at level $\ell-1$ to a single level-$\ell$ strand* |
| *Dressing* | $\mathrm{dress}$ | *Extend $H_n(R, q) \hookrightarrow H_{n+m}(q)$ and attach $m$ additional strands via an SDP-feasible binding subword* |

- ***Composition:** concatenation of Hecke-algebra embeddings;
  $\mathrm{dress}$ is right-composable with $\uparrow_\ell$ and
  $\downarrow_\ell$.*
- ***Identity:** the identity embedding
  $\mathrm{id}_P: H_{n_0}(q) \hookrightarrow H_{n_0}(q)$.*

*Unfolding and folding are mutually inverse when restricted to
particles whose coarse representation captures the full partition
content ([level sufficiency](#prop:level-sufficiency));
$\mathrm{dress}$ is in general not invertible because the binding
subword may not be uniquely reversible.*

**Functoriality of the Markov trace.**
*The Markov trace $\mathrm{tr}_M$ extends to a functor*

$$
  \mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)
$$

*sending every confined particle to its trace value and every
morphism to the induced trace transformation.  By
[level sufficiency](#prop:level-sufficiency), $\mathrm{tr}_M$ is
invariant under $\uparrow_\ell$ and $\downarrow_\ell$; under
$\mathrm{dress}$ it multiplies by the binding weight determined by
the [confinement SDP](#prop:confinement-sdp) active support.*

**Example — the atomic chain.**
*The chain $\mathrm{quark} \xrightarrow{\downarrow_1} \mathrm{nucleon}
\xrightarrow{\downarrow_2} \mathrm{atom} \xrightarrow{\mathrm{dress}}
\mathrm{neutral\ atom} \xrightarrow{\downarrow_3} \mathrm{molecule}$
is a composite morphism in $\mathbf{Conf}$ that takes free quarks to
a bonded molecule by successive foldings and one dressing (the
electron shell).  Each arrow preserves or extends the Markov trace
according to the functoriality rule above.*
