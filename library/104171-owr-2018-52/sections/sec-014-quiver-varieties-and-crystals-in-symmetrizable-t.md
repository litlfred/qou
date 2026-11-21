---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-014-quiver-varieties-and-crystals-in-symmetrizable-t
section_title: "Quiver varieties and crystals in symmetrizable type via modulated graphs"
section_number: null
pages: 44-46
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
graphs
Peter Tingley
(joint work with Vinoth Nandakumar)
Kashiwara and Saito [2] gave a geometric construction of the inﬁnity crystal for
any symmetric Kac-Moody algebra. The underlying set consists of the irreducible
components of the nilpotent representation varieties of Lusztig’s preprojective al-
gebra from [3]. We generalize this to symmetrizable types by replacing Lusztig’s
preprojective algebra with a more general one due to Dlab and Ringel [1]. We also
discuss extensions and relationships to other recent constructions. Much of this
can be found in more detail in [5].
1.1. Crystals. The inﬁnity crystal B(∞) is a combinatorial object which, among
other things, parameterizes a basis for U −
q (g), the lower triangular part of a quan-
tized universal enveloping algebra. It consists of a set along with some partial
permutations fi, and is usually deﬁned algebraically using Kashiwara’s modiﬁca-
tion eFi of the Chevalley generators. One can also realize the same combinatorics
in other ways. For example, for sln, the inﬁnity crystal is realized using multi-
segments, and the related ﬁnite crystals are realized using Young-tableaux. These
realizations can shed light on the underlying representation theory. For instance,
the connection with Young tableaux gives a way to see how Littlewood-Richardson
coeﬃcients are given by counting Littlewood-Richardson tableaux (which was
known before crystals were around, but it is still a nice example!)
1.2. Kashiwara and Saito’s construction. We will mostly review this using
the example of A3 (so sl4). This has Dynkin diagram
✈
✈
✈
1
2
3
The path algebra has a basis consisting of paths, and multiplication is concatenation
if possible, and 0 otherwise. The preprojective algebra Λ is the quotient by a generic
relation between 2-step paths starting and ending at each vertex.
For v ∈NI (I indexes nodes of the diagram), let Λ(v) be the variety of nilpotent
representations of Λ on ⊕ICvi, where each lazy path ei projects onto the corre-
sponding subspace. Kashiwara and Saito showed that ⊔vIrrΛ(v) realizes B(∞)
with the crystal operators fi acting as follows: Fix X ∈IrrΛ(v). Let Si be the
simple one-dimensional module over i. For generic x ∈X and a generic extension
0 →Si →(V ′, x′) →(V, x) →0,
(V ′, x′) is in a single irreducible component Y ∈IrrΛ(V ′). Then Y = fiX.
Proving this is not particularly hard! There is a second set of operators, f ∗
i , de-
ﬁned in the same way, but adding Si to the head instead of the socle. B(∞) also has
a second set of operators, those twisted by Kashiwara’s involution. In fact B(∞)
can be characterized as a set with operators fi and f ∗
i satisfying some straightfor-
ward conditions, including that fi, f ∗
j commute except occasionally when i = j.
Now it is just a matter of checking the conditions match exactly, which they do.
Enveloping Algebras and Geometric Representation Theory
3125
1.3. Punch line. About 8 years ago, two things bothered me about this:
• Every proof using this realization was only valid in symmetric type, even
though most of the combinatorial results could be extended to symmetric
type by “folding.” It was annoying to have this extra step!
• The name preprojective algebra. It seemed like it should mean something,
but the people I asked didn’t know where it came from (other than that
it is the term Lusztig used).
Then, at the 2010 Auslander Lectures, several talks mentioned “preprojective
modules,” and even a preprojective algebra! A mystery was about to be resolved!
Next, Hugh Thomas pointed me to a paper of Dlab and Ringel [1] studying prepro-
jective algebras in symmetrizable types...which actually dates to before Lusztig’s
work! Now for my punchline: Dlab and Ringel’s preprojective algebra (over inﬁ-
nite ﬁelds) can be used to realize B(∞) for any symmetrizable Kac-Moody algebra,
with everything analogous to Kashiwara-Saito’s work. Let me explain a bit more.
1.4. Symmetrizable quiver varieties. Consider e.g. B2, with Dynkin diagram
✈
✈
<
1
2
We need a ﬁeld extension of degree 2 to handle the diﬀerent length roots, so we use
R ⊂C. We also need a pair of bimodules for each edge, one for each orientation.
We use CMR and RM C, where both M and M are copies of C, and all actions are
just multiplication. Here M corresponds to orienting the edge left to right.
The path algebra is replaced by the tensor algebra: a copy of R at vertex 1, a
copy of C at 2, M, M, M ⊗C M, M ⊗R M, M ⊗C M ⊗R M, etc. Multiplication is
tensor product, or 0 if the ends don’t match up. The preprojective algebra is the
quotient by a degree 2 element starting and ending at each vertex. Here we use
τ1 = 1 ⊗1 ∈M ⊗C M
and
τ2 = 1 ⊗i + i ⊗1 ∈M ⊗R M.
We need these to satisfy the condition that zτ2 = τ2z for any z ∈C, which is
clearly true above. Dlab and Ringel use the canonical elements for non-degenerate
bilinear forms, which implies the necessary condition in general.
The variety Λ(v) (over R) consists of representations of this algebra on Rv1⊕Cv2.
IrrΛ(V ) is the set of irreducible components of Λ(V ), considered as a subset of
HomC(M ⊗R Rv1, Cv2) ⊕HomR(M ⊗C Cv2, Rv1).
We mean this in a naive sense, not considering components of the abstract variety
that do not have suﬃcient R points to appear. Now the deﬁnition of the crystal
operators is like in the symmetric case, and so is the proof that this realizes B(∞)!
1.5. Aﬃne sl2. This case is symmetric, but we have more freedom to choose the
relations in the preprojective algebra than usual, and this gives non-isomorphic
algebras that can still realize B(∞). Studying those may be interesting.
3126
Oberwolfach Report 52/2018
1.6. Relation with folding. Our construction is related to the method of folding
by a diagram automorphism to realize symmetrizable types: Taking the ﬁxed
points of the composition of a diagram automorphism and a Galois automorphism
of the same order acting on the symmetric quiver variety gives an instance of our
construction. Well, conjecture I guess, this certainly hasn’t been written up.
1.7. Relation to work of Geiss, Leclerc and Schroer. In [4] they consider
a similar construction, but using nilpotent polynomial rings in place of our ﬁelds.
They can then work over an algebraically closed ﬁeld, a clear advantage. But
there are disadvantages as well. For instance, they must restrict to only consider
representations that admit a ﬁltration of a ﬁxed form. They also ﬁnd irreducible
components of lower dimension which they must ignore.
Anyway, they use C and C[ǫ]/ǫ2 where we use R and C above. It seems there
should be a direct relationship with our construction, roughly as follows:
• Our construction works ﬁne using the ﬁeld extension C((ǫ2)) ⊂C((ǫ)).
• One would look for an “integral” part, deﬁned over C[[ǫ2]] ⊂C[[ǫ]].
• One would then set ǫ2 = 0, and hope nothing important collapses...
Much needs to be checked, and it is probably more complicated than this. Christof
Geiss will discuss something kind of like this in his talk.
References
[1] V. Dlab, C. M. Ringel, The preprojective algebra of a modulated graph, Representation
theory II, Lecture Notes in Math 832, Springer, Berlin 1980, 216-231.
[2] M. Kashiwara and Y. Saito, Geometric construction of crystal bases. Duke Math. J. 89
(1997), 9-36.
[3] G. Lusztig. Quivers, perverse sheaves, and quantized enveloping algebras. J. Amer. Math.
Soc., 4 (2):365–421, 1991.
[4] C. Geiss, B. Leclerc, J. Schroer. Quivers with relations for symmetrizable Cartan matrices
IV: Crystal graphs and semicanonical functions. Selecta Math. (N.S.) 24 (2018) no. 4, 3283–
3348.
[5] V. Nandakumar and P. Tingley. Quiver varieties and crystals in symmetrizable type via
modulated graphs. Math. Res. Lett. 25 No. 1 (2018) pp 159–180.
Drinfeld-Gaitsgory-Vinberg interpolation Grassmannian and
