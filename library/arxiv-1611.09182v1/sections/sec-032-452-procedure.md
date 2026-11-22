---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-032-452-procedure
section_title: "Procedure"
section_number: 4.5.2
pages: 32-33
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
Procedure
With these deﬁnitions in hand, the procedure for constructing minimal left ideals is
straightforward:
1.
First identify a quadratic vector space (V, Q) . In particular, we will take V to be
the generating space of a given Cliﬀord algebra, spanned by the generators {ej}
over C, where j = 1 . . . n. We will take our quadratic form to be Q(v) = {v, v}.
2.
Identify an MTIS (maximal totally isotropic subspace) U of V as the largest possible
subspace of V such that {αi, αj} = 0 ∀αi, αj ∈U.
3.
Deﬁne the nilpotent object Ω≡α1α2 · · · αn/2, where the αi are linearly independent
basis vectors of U.
4.
Construct the projector, ΩΩ†, where † takes i 7→−i, ej 7→−ej, and reverses the order
of multiplication.
5.
Left multiply the entire Cliﬀord algebra onto ΩΩ† to arrive at a minimal left ideal:
Cl(n)ΩΩ†.
24
It should be noted that the above is not the only way in which minimal left ideals may
be constructed; for details, please see [1].
The projector, ΩΩ†, is an example of a primitive idempotent. A primitive idempotent,
P, is deﬁned in [51] to be an idempotent (P 2 = P), which is not the sum of two annihilating
idempotents, P̸ = P1 + P2, where P1P2 = P2P1 = 0.
4.6
