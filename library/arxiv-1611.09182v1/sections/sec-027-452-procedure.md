---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-027-452-procedure
section_title: "Procedure"
section_number: 4.5.2
pages: 31-33
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
plex Cliﬀord algebras, where n is even. This procedure is described in [1], which also
accommodates other types of Cliﬀord algebra.
In the special case of C⊗ H, this procedure will allow us to recover the Weyl spinors
ΨL or ΨR, which we found earlier via the complex multiplicative action, mc. We will then
move on to the algebra of C⊗ O, which can be seen to generate Cl(6). This leads us to
minimal left ideals behaving as a full generation of quarks and leptons.
4.5.1 Some deﬁnitions
Let V be the vector space over a ﬁeld F. A quadratic form, Q, is a map Q :V → F such
that∀v,w ∈V and λ∈ F,
Q(λv) =λ2Q(v) (4.4)
and such that the map B :V×V→ F,
B : (v,w )↦→Q(v +w)−Q(v)−Q(w) (4.5)
is linear in both v and w. This V, together with its quadratic form, is called a quadratic
vector space.
23
We will be especially interested in the quadratic vector space given by V andQ, where
V is the n-dimensional vector space spanned by the generating elements ej of deﬁnition
(4.1). Here, the quadratic form will be given by Q(v) = {v,v}, and the corresponding
bilinear form is then B(v,w ) = 2{v,w}. Note that V here is only the generating subspace
of our Cliﬀord algebra, it does not represent the entire Cliﬀord algebra.
A subspace U of V is said to be totally isotropic if B(αi,αj) = 0 ∀ αi,αj ∈ U. In
the following construction, we will be interested in maximal totally isotropic subspaces of
V , which are deﬁned to be totally isotropic subspaces of V with maximal dimension. As
explained in [1], for Cliﬀord algebras over C with n even, the dimension of any maximal
totally isotropic subspace will be n/2. In fact, we ﬁnd that the generating space splits into
exactly two maximal totally isotropic subspaces, each with the dimension n/2.
It is interesting to note that our maximal totally isotropic subspace, U of V, generates
a Grassmann algebra, seeing as how B(αi,αj) = 2{αi,αj} = 0 ∀ αi,αj∈ U. This fact
merits notice, especially in consideration of recent work by L´ aszl´ o, [49].
4.5.2 Procedure
With these deﬁnitions in hand, the procedure for constructing minimal left ideals is
straightforward:
1. First identify a quadratic vector space ( V,Q ). In particular, we will take V to be
the generating space of a given Cliﬀord algebra, spanned by the generators {ej}
over C, wherej = 1...n. We will take our quadratic form to be Q(v) ={v,v}.
2. Identify an MTIS (maximal totally isotropic subspace) U of V as the largest possible
subspace of V such that{αi,αj} = 0∀αi,αj∈U.
3. Deﬁne the nilpotent object Ω ≡α1α2··· αn/2, where the αi are linearly independent
basis vectors of U.
4. Construct the projector, ΩΩ†, where† takesi↦→−i, ej↦→−ej, and reverses the order
of multiplication.
5. Left multiply the entire Cliﬀord algebra onto ΩΩ† to arrive at a minimal left ideal:
Cl(n)ΩΩ†.
24
It should be noted that the above is not the only way in which minimal left ideals may
be constructed; for details, please see [1].
The projector, ΩΩ†, is an example of a primitive idempotent. A primitive idempotent,
P , is deﬁned in [51] to be an idempotent (P 2 =P ), which is not the sum of two annihilating
idempotents, P⁄=P1 +P2, where P1P2 =P2P1 = 0.
4.6 Minimal left ideals in C⊗ H
As a speciﬁc example, let us now build a minimal left ideal in C⊗ H≃ Cl(2), as per Figure
(4.2). Following the procedure from Section (4.5.2),
1. Our vector space, V, is spanned by the elements iϵx and iϵy over C. The quadratic form is
given by Q(v) ={v,v}.
2. An MTIS of V is just one-complex-dimensional in this case, and can be spanned
byα1 =ϵ↓↑ = 1
2 (ϵy +iϵx). (Another option would be ϵ↑↓ = 1
2 (−ϵy +iϵx)).
3. Since U is only one-dimensional here, the nilpotent object Ω is given simply by
Ω =α1 =ϵ↓↑.
4. The primitive idempotent, ΩΩ†, is then ΩΩ† =ϵ↓↑ϵ↓↑† =ϵ↓↓.
5. Our minimal left ideal is ﬁnally given by Ψ R = C⊗ H ΩΩ† =ψ↑
Rϵ↑↓ +ψ↓
Rϵ↓↓.
Readers will notice that this minimal left ideal matches Ψ R, found as a generalized ideal in
Section (3.5). Furthermore, redoing this procedure by taking the maximal totally isotropic
subspace to be instead spanned by ϵ↑↓ yields the familiar ΨL =ψ↑
Lϵ↑↑ +ψ↓
Lϵ↓↑ from before.
So, we have just shown that we can use this procedure to build a left- or right-handed
Weyl spinor from the left action of C⊗ H on itself.
