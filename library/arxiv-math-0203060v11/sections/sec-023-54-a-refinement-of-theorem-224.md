---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-023-54-a-refinement-of-theorem-224
section_title: "A refinement of Theorem 2.24"
section_number: 5.4
pages: 19-20
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
coconnected, semisimple weak Hopf algebra. Let πi be the primitive idempotents
in A∗
s ∩Z(A∗), and let Aij ⊂A be deﬁned by A∗
ij = πiA∗S(πj). It is easy to see
that Aij = pjApi, where pi are the primitive idempotents of As ∩At. In particular,
Aii are semisimple algebras.
In fact, for every i the algebra Aii has a natural structure of a biconnected weak
Hopf algebra, and its representation category Rep(Aii) is equivalent to Rep(A) via
the usual Morita equivalence V →piV , V ∈Rep(A). Indeed, this map is a tensor
functor since ∆(pi) = (pi ⊗pi)∆(1). To prove that it is an equivalence it suﬃces to
show that the central support ˆpi of pi equals 1. From the formula for ∆(pi) above
we have ∆(ˆpiA) ⊂ˆpiA⊗ˆpiA. But ˆpiA contains the matrix block q0A corresponding
to the trivial representation of A (which is irreducible since A is connected). Hence,
∆(q0A) ⊂ˆpiA ⊗ˆpiA and so ˆpi = 1.
Let qir be the primitive idempotents of Z(Arr). Let n2
ir = dim(qir(Arr)t). We
have the following reﬁnement of Theorem 2.24.
20
PAVEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Theorem 5.2. One has Tr(S2|qjrArsS(qis)) = dim(Rep(A))n2
jrn2
is.
Proof. The proof is completely analogous to the proof of Theorem 2.24. Namely,
let g be an element of A such that gxg−1 = S2(x). Then prgpr realizes S2 in Arr.
Hence, as was shown in the proof of Theorem 2.24 for any V ∈Rep(A), one has
Tr(prgpr|qirV ) = TrV (g)n2
ir,
and
Tr(prg−1pr|S(qir)V ) = TrV ((g−1)∗)n2
ir.
Now, Ars = ⊕V psV ⊗(prV )∗, and S2|Ars = psgps ⊗(prg−1pr)∗. Hence, taking the
sum over all V , we arrive at the result.
□
