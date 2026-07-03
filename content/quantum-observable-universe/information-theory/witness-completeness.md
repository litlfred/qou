**Conjecture (witness completeness).**
*Let $\mathcal{H} = V(\mathfrak{h})$ be a jet horizon
([jet horizon](#def:jet-horizon)) of finite lifetime.  The map sending
the trapped degree-$0$ section data to the total accumulated
degree-$\geq 1$ witness stream across $\mathcal{H}$ — all of
$\Gamma(\mathcal{H}_t, A_k/A_0)$ for $k \geq 1$, integrated over the
horizon's lifetime — is injective on the physical state space.*

Equivalently: the restriction of the evolution to exterior data
(infalling degree-$0$ identities to outgoing degree-$\geq 1$
Hawking-type record) is unitary.  The horizon ideal blocks every
degree-$0$ section at each fixed time
([Hawking radiation](#rem:hawking-radiation)), while the conjecture
asserts that no two distinct interior states produce the same
*lifetime-total* leakage.

The conjecture is the first postulate of black hole complementarity
\cite{susskind1993} in jet-horizon form: information is present in the
exterior record, and what the computational horizon obstructs is
*decoding*, not existence \cite{harlowhayden2013}.  It selects, within
the trichotomy of
[the information paradox](#rem:information-paradox-incompleteness),
the refinement in which partial witnesses accumulate toward a complete
(if never finitely derivable) determination of the interior
\cite{marolf2017}.

The statement lives at the level of the two compatible filtrations —
the jet filtration $A_0 \subset A_1 \subset \cdots$ on the bundle side
and the Gröbner–Shirshov leading-term filtration on the Hecke-algebra
side — not at the level of degree-$0$ observables.  The evolution on
the full filtered algebra is unitary; the apparent non-unitarity of the
exterior description is the compression to the degree-$0$ observable
marginal, which no framework requires to be unitary.  What the
conjecture asserts is precisely faithfulness of the associated graded
record.  It reduces to a non-degeneracy statement: if the Frobenius-type
pairing between trapped degree-$0$ sections and accumulated exterior
graded probes separates interior states, injectivity of the witness
stream follows (the sorry-free reduction
`witnessComplete_of_frobeniusSeparation` in the Lean sibling); the open
content is the persistence, on the horizon graded module, of the
non-degeneracy that is definitional for the observable subcategory away
from the horizon.
