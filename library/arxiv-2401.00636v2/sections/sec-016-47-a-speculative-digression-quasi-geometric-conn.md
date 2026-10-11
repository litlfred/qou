---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-016-47-a-speculative-digression-quasi-geometric-conn
section_title: "A speculative digression: quasi-geometric connections"
section_number: 4.7
pages: 14-17
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
4.7.1. Quasi-geometric connections.
Deﬁnition 4.18. Let X be a smooth irreducible complex algebraic variety deﬁned over
Q. Let ∇be a ﬂat connection on a vector bundle V on X with regular singularities. We
say that ∇is quasi-geometric if the monodromy representation of the corresponding ﬂat
holomorphic connection ∇C on X viewed as a complex manifold is also deﬁned over Q.
In other words, a quasi-geometric connection is a ﬂat connection with regular singularities
deﬁned over Q both in the de Rham and the Betti realization.
Note that if X◦⊂X is a non-empty Zariski open subset and x0 ∈X◦then the map
π1(X◦, x0) →π1(X, x0) is surjective, so ∇is quasi-geometric on X if and only if it is quasi-
geometric on X◦.
Example 4.19. 1. A geometric connection (Subsection 2.5) is quasi-geometric.
2. The category of quasi-geometric connections is invariant under pullbacks, external prod-
ucts (hence tensor products), and duals. Thus for every X, we have a Q-linear Tannakian
category QG(X) of quasi-geometric connections on X.
3. If π : Y →X is a smooth morphism and ∇is a quasi-geometric connection on Y then
for all i the i-th cohomology of π∗∇is quasi-geometric on its smooth locus X◦⊂X, since
the direct image can be computed over Q both in the de Rham and the Betti realization.
4. A simple composition factor of a quasi-geometric connection is quasi-geometric.
5.
An irreducible rigid connection (i.e., one determined up to ﬁnitely many choices
by conjugacy classes of its local monodromies) is quasi-geometric, since it is deformation-
theoretically rigid both in the de Rham and the Betti realization. Note that for X = P1 \ S
where S ⊂Q is a ﬁnite set, N. Katz showed that rigid connections are geometric by using
the method of middle convolution ([K]).
The relevance of the notion of a quasi-geometric connection to this paper is exhibited by
the following proposition, whose proof is straightforward.
Proposition 4.20. If ∇is a quasi-motivic family of ﬂat connections on X deﬁned over Q
with algebraic monodromy, then for s ∈Qn, ∇(s) is quasi-geometric.
In particular, this means that the examples of Section 5 are quasi-geometric (we will see
that they have algebraic monodromy).
An important property of quasi-geometric connections is quasiunipotent monodromy at
inﬁnity.
Proposition 4.21. Let X be a smooth compactiﬁcation of X such that X \ X is a normal
crossing divisor. If ∇is a quasi-geometric connection on X, then its monodromy around
every component D of X \ X is quasiunipotent.
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
15
Proof. Let us extend the underlying vector bundle of ∇over D so that ∇has a ﬁrst order
pole there (this is possible since ∇has regular singularities, [De2]). Then the eigenvalues of
the monodromy of ∇around D are of the form e2πis, where s runs through the eigenvalues
of the residue of ∇at D. Thus both s and e2πis are algebraic numbers. Hence it follows from
the theorem of Gelfond and Schneider in transcendental number theory ([Ge]) that s ∈Q,
i.e., e2πis is a root of unity, as desired.
□
Remark 4.22. Since every geometric connection is quasi-geometric, Proposition 4.21 is a
generalization of the Local Monodromy Theorem in Hodge theory: monodromy at inﬁnity
of a Gauss-Manin connection is quasiunipotent. In fact, our proof of Proposition 4.21 is the
same as Brieskorn’s proof of this theorem given at the end of [De2].
Remark 4.23. There are many examples of irreducible quasi-geometric connections without
a known geometric construction, even on X = P1\S. E.g., we can take the Dunkl connection
5.2.1 for exceptional Coxeter groups at a rational parameter c, restricted to a generic line
in h (not passing through 0). However, we do not know an example of an irreducible quasi-
geometric connection which is provably non-geometric. For instance, Proposition 4.21 implies
that a 1-dimensional connection on P1 \ S which is quasi-geometric is actually geometric.
Let ∇be a connection on X := P1 \ S with regular singularities deﬁned over Q whose
monodromies around points of S are quasiunipotent (i.e., the eigenvalues of the residues are
rational). In this case it is usually diﬃcult to show that ∇is not quasi-geometric, because
this entails establishing transcendence of certain numbers (such as traces of monodromy
operators). Yet we expect that the quasi-geometric property is quite rare. Namely, we make
the following conjecture.
Conjecture 4.24. Fix a quasiunipotent Riemann symbol P for S (i.e., the list of eigen-
values of monodromies around points of S). Then there are ﬁnitely many quasi-geometric
connections on P1 \ S with Riemann symbol P.
In particular, this would mean that already for rank 2 and |S| = 4, most connections
with a given P are not quasi-geometric, since such connections are parametrized by two
parameters in Q.
Remark 4.25. Conjecture 4.24 holds for geometric connections by a result of Deligne [De1],
which provides motivation and supporting evidence for this conjecture.
4.7.2. Quasi-geometric connections and braided fusion categories. In spite of likely being rare
among general regular connections with quasiunipotent local monodromies, quasi-geometric
connections are ubiquitous in diﬀerent areas of mathematics. In particular, we would like
to propose the following conjecture, stating that connections arising from braided fusion
categories are always quasi-geometric.
Let C be a braided fusion category over C ([EGNO], Deﬁnitions 4.1.1, 8.1.1). By the
Ocneanu rigidity theorem, C is deﬁned over Q ([EGNO], Corollary 9.1.8). Thus for any
objects X1, ..., Xn, Y ∈C, the space Hom(Y, X1 ⊗... ⊗Xn) carries an action of the pure
braid group PBn, which deﬁnes a Betti local system LX1,...,Xn,Y on the conﬁguration space
Xn := Cn \ diagonals deﬁned over Q. By the Riemann-Hilbert correspondence ([De2]), there
is a unique up to isomorphism ﬂat connection ∇X1,...,Xn,Y on Xn with regular singularities
whose monodromy is LX1,...,Xn,Y .
16
PAVEL ETINGOF AND ALEXANDER VARCHENKO
Conjecture 4.26. The connection ∇X1,...,Xn,Y is deﬁned over Q. In other words, it is a
quasi-geometric connection.
If C is a modular category ([EGNO], Subsection 8.14) then Conjecture 4.26 can be strength-
ened to say that the ﬂat connections with regular singularities on the moduli space of curves
of any genus g with n punctures attached to mapping class group representations on spaces
of conformal blocks of the category C are deﬁned over Q (equivalently, are quasi-geometric).
In genus 0 this is actually equivalent to Conjecture 4.26, since the category C can be as-
sumed modular by pivotalization ([EGNO], p.180) and taking the Drinfeld center ([EGNO],
Subsection 7.13).
A possible approach to proof of Conjecture 4.26 would be to establish a de Rham analog of
Ocneanu rigidity, using the de Rham description of the notion of a modular fusion category
and modular functor in terms of the Teichm¨uller tower, due to Deligne and Beilinson-Feigin-
Mazur (see [BK], Chapter 6 and references therein).
Some evidence for Conjecture 4.26 is provided by the following proposition.
Proposition 4.27. If C is the category of representations of a strongly rational vertex algebra
V (in the sense of [M], p.1) deﬁned over Q then Conjecture 4.26 holds for C (in the generalized
form for any genus).
Proof. By Huang’s theorem ([H]), C is a modular category.
Since V is deﬁned over Q,
so are the KZ type connections on genus 0 conformal blocks for V. On the other hand,
the monodromy of these connections is also deﬁned over Q by Ocneanu rigidity ([EGNO],
Corollary 9.1.8), as already mentioned above. This proves the proposition.
□
Note that it is conjectured (see e.g. [GJ], p.2) that any modular category C is the category
of representations of a (strongly) rational vertex algebra V. If so, and V is deﬁned over Q,
then Conjecture 4.26 would follow from Proposition 4.27.
We do not know if any rational vertex algebra is deﬁned over Q (although this seems to
be true in all known examples). But we hope that this can be proved (maybe under mild
assumptions) if V is deformation-theoretically rigid (has no non-trivial formal deformations),
which could presumably be deduced from vanishing of a suitable second cohomology group.
We do not know, however, how to prove such rigidity.
Also, in all examples of vertex algebras we know, the KZ type connections on genus 0
conformal blocks are Gauss-Manin connections (i.e., their local ﬂat sections have integral
representations). For instance, if V is the simple vertex algebra attached to the aﬃne Kac-
Moody algebra bg at level k then these connections are literally the KZ connections, whose
Gauss-Manin realization (i.e., integral form of solutions) is given in [SV]. In such cases, one
may say that the quasi-geometric nature of the corresponding ﬂat connections is explained
by the fact that they are Gauss-Manin connections (i.e., geometric).
Finally, we note that there are concrete examples of modular fusion categories (coming
from subfactors) for which the ﬂat KZ-type connections attached via the Riemann-Hilbert
correspondence to their braid group representations are not known explicitly (the problem of
computing a regular connection with given monodromy is, in general, highly transcendental,
even on X = P1 \ S). In particular, they are not known to be Gauss-Manin connections, not
even quasi-geometric ones, so Conjecture 4.26 is open for them. The simplest such example
is perhaps the Drinfeld center of the Haagerup fusion category, see [GI]. This category is
not known to be the representation category of a rational vertex algebra.
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
17
Remark 4.28. If a braided fusion category C is unitary ([Tu]) then the representations of
the pure braid group PBn on its multiplicity spaces are also unitary, thus semisimple. Hence
they are also semisimple if C is Galois conjugate to a unitary category. We do not know,
however, whether representations of PBn coming from braided fusion categories must be
semisimple in general. This is true in the abelian case n = 2 by the Anderson-Moore-Vafa
theorem ([EGNO], 8.18), but nothing is known for n > 2.
