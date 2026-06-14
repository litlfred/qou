**Lemma (body order = jet degree).**

Let $\mathcal{B}_K$ be the canonical atomic braid of a nucleus with $A$
nucleons — each nucleon a $3$-strand block, assembled by
`atom_braid_word_3A` — and equip $H_{3A}(q)$ with the Gröbner--Shirshov
filtration by Coxeter length $\ell(w)$
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)) read off through
the jet-prefix order
([`prop:jet-prefix-gb-filtration`](#prop:jet-prefix-gb-filtration)). Then:

1. the sub-braid spanning an $n$-nucleon cluster lies in **jet vertical
   degree $n$** — its Gröbner--Shirshov normal form has filtration degree
   $n$; and
2. the associated-graded component $\mathrm{gr}_n$ of the filtration is
   exactly the **$n$-body cluster contribution**.

Consequently the body-order decomposition of the binding coincides, term by
term, with the jet-order filtration:

$$
\sum_{n} (\text{$n$-body term}) \;=\; \sum_{n}\mathrm{gr}_n .
$$

This is obligation **(C)** of
[`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration):
it identifies the two filtrations, leaving the per-term mass identity
$B_n = m_e\,a_D^{(n)}$ (the mass identity applied to each graded piece) and
the kernel of the growth recurrence
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)) as the
remaining inputs.

The grading rests on the Gröbner--Shirshov filtration (step 7, derived) read
through the jet-prefix order (step 8); the exhaustiveness of the cluster
decomposition — every contribution lives in some finite cluster degree — is
the structural property of the `atom_braid_word_3A` construction (each added
nucleon raises the normal-form length by its block, so an $n$-cluster
sub-word sits at degree $n$).

Though the proof reduces to a standard jet-degree equivalence argument, projecting the structural hypothesis onto this geometric form to explicitly equate bond order with the jet-degree of the extracted $S$ field is a mathematically novel physical framing specific to the Quantum Observable Universe.
