---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-004-3-the-drinfeld-kohno-theorem
section_title: "The Drinfeld-Kohno theorem"
section_number: 3
pages: 4-5
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
The Drinfeld-Kohno theorem
We give a brief discussion of the essential points only, as they pertain to the particular case examined (in particular,
we do not mention coassociativity since it is not essential to the problem at hand) - the reader is referred to [5]
for a detailed account of these matters in a general context.
Starting from the (undeformed) universal enveloping algebra U(su(2)) ≡U one can form the algebra U([[h]])
by extending the ﬁeld of coeﬃcients to the ring of formal power series in h. With the identiﬁcation h ≡ln(q),
U([[h]]) can be shown to be isomorphic to Uq. In other words, one can ﬁnd h-dependent invertible functions of
the classical su(2) generators, which obey the deformed relations (1). Applying the classical coproduct to these
functions one does not however obtain the coproduct of (2) (with H, X± in these equations considered as functions
of the classical generators). Instead, as the Drinfeld-Kohno theorem states, the following relation holds
∆(x) = F∆c(x)F−1
(13)
for x ∈Uq, where F ≡F(1) ⊗F(2) ∈U⊗2
q
is called the twist. In the above relation ∆(·) stands for the coproduct
that appears in (2) while ∆c(·) is the classical cocommutative coproduct given by ∆c(y) = y ⊗1 + 1 ⊗y where y
is any classical Lie algebra generator.
As an illustration of the content of the theorem, consider the particular case where x in (13) stands for a
classical generator (then, in the rhs, ∆c(x) does not involve q). To compute the lhs, one could express x in terms
of the quantum generators qH, X± (via the isomorphism mentioned in the theorem), then take the coproduct
using (2) and ﬁnally switch back to the classical generators using the inverse of the above isomorphism. Notice
that the q-dependence of the lhs comes, in this case, entirely from the argument of the coproduct (x being a
q-dependent function of the quantum generators) - the coproduct (2), written in terms of K ≡qH, X± does
not involve q explicitly. On the rhs, the q-dependence comes entirely through F. One way to look at (13) is to
consider it as deﬁning a second (q-dependent) coproduct for the classical algebra U via conjugation by F.
There is more to the Drinfeld-Kohno theorem though. U is a cocommutative coassociative quasitriangular
Hopf algebra and as such its universal R-matrix is trivial (i.e. equal to 1 ⊗1). It can however alternatively be
considered as a quasitriangular quasi-Hopf algebra with universal R-matrix given by Rc = qt where
t = ∆c(Cc) −Cc ⊗1 −1 ⊗Cc .
(14)
Adopting this point of view one sees the universal R-matrix of Uq to be the image, under the twist, of its classical
counterpart according to
R = F′RcF−1
where F′ ≡P(F) and P is the permutation operator in U⊗2
q
.
