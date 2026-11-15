---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-007-32-duality
section_title: "Duality"
section_number: 3.2
pages: 74-77
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
If P = ∪kPk is a planar algebra, the ﬁltered algebras λn(P), where
λn(P)k = Pn,n+k, for ﬁxed n, have natural planar algebra structures. For
n even, this is rather obvious — just add n straight vertical lines to the left
of a tangle. But if n is odd one must be more careful because of orientations.
In fact λ1(P) and P are not isomorphic in general, even as ﬁltered algebras,
as one can see from example 2.9. We begin by describing the planar algebra
structure on λ1(P).
If T is an unlabelled k-tangle we deﬁne the unlabelled (k + 1)-tangle ˜T
to be the tangle consisting of a vertical straight line from (1,0) to (1,1), and
the tangle T, with all its orientations reversed, shifted by 1 in the positive
74
x direction. Also in ˜T each internal p-box is replaced by a (p + 1)-box with
the ﬁrst and last distinguished boundary points connected by a short curve.
The procedure is illustrated in Figure 3.2.1.
The tangle T.
The tangle ˜T.
∗
∗
∗
∗
∗
∗
Figure 3.2.1
To each internal box B of T there corresponds in the obvious way a box ˜B
of ˜T. If T is labelled by L = `
k>0 Lk,
˜T will be given the obvious labelling
by ˜L, ˜Lk = Lk−1(˜L1 = ∅).
Proposition 3.2.2 Let P = ∪kPk be a planar algebra with parameters
δ1 = Z(
) and δ2 = Z(
). Assume P is presented on itself by Φ. Then
λ1(P) is a planar algebra with parameters δ2, δ1, presented on itself by λ1(Φ)
where λ1(Φ) is deﬁned by λ1(Φ)(T) = δ−pΦ( ˜T),
p being the number of
internal boxes in T.
Proof.
First note how the labels in a tangle of P(λ1(P)) give valid
labels for P(P) because of the inclusion λ1(P)k ⊂Pk+1. That λ1(Φ) is a
ﬁltered algebra homomorphism is obvious.
The annular invariance of ker
λ1(Φ) follows immediately from that of Φ, by representing elements of P1,1+k
as linear combinations of tangles with vertical ﬁrst string and applying ∼to
linear combinations. Thus λ1(P) is a general planar algebra.
Now λ1(P)0 = P1,1 and λ1(P)1,1 = P2,2 which has dimension 1 since P
is a planar algebra. So λ1(P) is planar. The multiplicativity property for
λ1(P) follows immediately from that of P, where orientations on networks
without boxes are reversed.
□
75
In the next two lemmas, A will be the A(∅) element
where the actual number of boundary points is as required by context.
Lemma 3.2.3 If P is a planar algebra, πA deﬁnes a linear isomorphism
between Pk and λ1(P)k, for each k > 0.
Proof. By a little isotopy and the deﬁnition of P1,k+1, πA is onto. But
provides an inverse for πA, up to a non-zero scalar. So πA is an isomorphism.
□
Lemma 3.2.4 The subset S of the planar algebra generates P as a planar
algebra iﬀπA(S) generates λ1(P) as a planar algebra.
Proof. (⇒) Given a tangle T in P1,k+1(S), it suﬃces to exhibit a tangle
TA in Pk(πA(S)) with Φ( ˜TA) being a multiple of Φ(T). We create TA from
T by eliminating the ﬁrst string, reversing all orientations and otherwise
changing only in small neighborhoods of the internal boxes of G, sending a
box labelled R ∈S in T to the box labelled πA(R) in TA as below:
· · ·
· · ·
πA(R)
R
· · ·
· · ·
76
Then by deﬁnition ˜TA will be exactly like T except near its boxes where it
will look as below:
πA(R)
· · ·
· · ·
· · ·
· · ·
R
Φ
Thus Φ( ˜TA) is a multiple of Φ(T).
(⇐) Given x ∈P, πA( x ) is in λ1(P) so by hypothesis it is the image
under λ1(Φ) of a linear combination of tangles labelled by elements of πA(S)
which are in turn images under Φ of tangles labelled by elements of S (up
to nonzero scalars). Using the tangle of Lemma 3.2.3 to invert πA, we are
done.
□
By iterating the procedure P 7→λ1(P), we see that all the λn(P) have
natural planar algebra structures, but observe that all the λ2n(P) are isomor-
phic to P as planar algebras via the endomorphism (often called “le shift de
deux”) deﬁned by adding two straight vertical strings to the left of a tangle.
We leave the details to the reader.
The planar algebra λ1(P) is said to be the dual of the planar algebra P,
and we have λ1(λ1(P)) ≃P as planar algebras.
In the case of Example 2.9, P G
2 is the group algebra CG and λ1(P G)2 is
ℓ∞(G). The tangle πA gives a linear isomorphism between the two. Thus
planar algebra duality extends the duality between a ﬁnite group and its dual
object.
