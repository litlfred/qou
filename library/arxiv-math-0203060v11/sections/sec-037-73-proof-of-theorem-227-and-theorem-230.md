---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-037-73-proof-of-theorem-227-and-theorem-230
section_title: "Proof of Theorem 2.27 and Theorem 2.30"
section_number: 7.3
pages: 28-29
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
gories, and F : C →C′ a tensor functor between them. We can assume without loss
of generality that F is faithful and surjective. Let R be a semisimple algebra, and
ON FUSION CATEGORIES
29
let G : C′ →R−bimod be a ﬁber functor on C′ (we know by now that it necessarily
exists for a suitable R). Let B = End(G) be the corresponding weak Hopf algebra.
Let A = End(G ◦F). Then B is a weak Hopf subalgebra of A, C′ = Rep(B),
C = Rep(A), and F is the restriction functor. Thus, by Proposition 7.4, the com-
plex C•
F (C) is isomorphic to the complex C•(A, B). Now, since A is semisimple, it
is also cosemisimple by Theorem 2.26. Hence, by Theorem 6.3, C•
F (C) is acyclic in
positive degrees. Theorem 2.27 is proved.
Now let us prove Theorem 2.30. Let C be a multifusion category. By theorem
2.27, we have Hi(C) = 0, i > 0, in particular H3(C) = 0.
Now consider the set of all admissible associativity constraints for a tensor cat-
egory with the same Grothendieck ring as C. It is an aﬃne algebraic variety. This
variety is acted upon by the group of twists. By a standard argument, one ﬁnds
that the quotient of the tangent space to this variety at the point C by the tangent
space to the orbit of C is equal to H3(C). Since H3(C) = 0, the group action is
locally transitive, and hence has ﬁnitely many orbits. We are done.
In conclusion we give the formulation of Ocneanu rigidity for semisimple weak
Hopf algebras. This is a generalization to the weak case of Stefan’s rigidity theorem
for semisimple Hopf algebras [S], which was conjectured in [N, 3.9].
Theorem 7.5. A regular semisimple ﬁnite dimensional weak Hopf algebra does
not admit nontrivial deformations in the class of regular weak Hopf algebras. In
particular, there are ﬁnitely many such weak Hopf algebras in each dimension.
Proof. Let A be a regular semisimple weak Hopf algebra, Rep(A) its representation
category, R its base, and let F : Rep(A) →R −bimod be the forgetful functor.
Suppose we have a deformation of A. Then by Theorem 2.30, this deformation
produces a trivial deformation of Rep(A) as a tensor category. It is also clear that
the base R of A, being a semisimple algebra, is deformed trivially. This means
that this deformation comes from a deformation of the forgetful functor F as a
tensor functor (indeed, a regular weak Hopf algebra is completely determined by
the associated forgetful functor, since the symmetric separability idempotent is
unique). But the deformation of F must also be trivial, by Theorem 2.31. This
implies the ﬁrst statement of the theorem. The second statement follows from the
ﬁrst one as in the proof of Theorem 2.30.
□
