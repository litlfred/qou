---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-011-5-derivations-and-the-akemann-ostrand-property
section_title: "Derivations and the Akemann-Ostrand property"
section_number: 5
pages: 17-18
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
In this section we show that quantum Markov semi-groups may b e used to prove the Akemann-
Ostrand property AO + of a von Neumann algebra. In particular we ﬁnd a new range of q for which
q-Gaussians have AO +. Let us ﬁrst recall the deﬁnition of the Akemann-Ostrand pro perty that is
most suitable for us, see [Iso15].
Deﬁnition 5.1. A ﬁnite von Neumann algebra M has condition AO + if there exists a σ-weakly
dense unital C ∗-subalgebra A⊆ M such that:
(1) A is locally reﬂexive [BrOz08, Section 9];
(2) There exists a ucp map θ : A⊗min Aop→ B(L2(M )) such that θ(a⊗ bop)− abop is compact
for all a, b∈ A.
Let M be a ﬁnite von Neumann algebra with faithful normal trace τ . Let A be a ∗-subalgebra
that is σ-weakly dense in M with C ∗-closure A. Let ∂ :A→ H be a closable derivation to an
A-A bimodule H. Assume that A has some linear basis ei, i∈ I with I countable that is moreover
orthonormal in L2(M ). Deﬁne the linear map,
(5.1) S :A→ H : ei↦→ ∂(ei)
‖∂(ei)‖ ,
where we put any unit vector in H as S(ei) if ∂(ei) = 0. Then the map S is not necessarily bounded
on L2(M ) and therefore we state the following assumption.
Assumption 2. Assume that S is a bounded map L2(M )→ H. Further, we assume that S∗S is
a Fredholm operator on L2(M ).
Next, for every x, y∈A we introduce a bounded linear map
(5.2) Tx,y : L2(M )→ H : ξ↦→xS(ξ)y− S(xξy).
Let S = V|S| be the polar decomposition of S and note that 1 − V ∗V is a ﬁnite rank projection.
Denote by K(L2(M )) the compact operators .
Proposition 5.2. Assume that H is weakly contained in the coarse bimodule of M asA-A bimod-
ules (namely, the assignment x⊗ yop∈ B(L2(M )⊗ L2(M ))↦→xyop∈ B(H) for x, y∈A extends
to a bounded ∗-homomorphism). Suppose that Assumption 2 holds and that Tx,y is compact for all
x, y∈A . Then there is a ucp map
θ : A⊗min Aop→ B(L2(M )),
such that θ(a⊗ bop)− abop is compact for all a, b∈ A.
18 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
Proof. Observe that one can write Tx,y = xyopS− Sxy op for all x, y∈A , where x and yop mean
the corresponding left and right actions. Let Π be the quotie nt map on B(L2(M )) onto the Calkin
algebra. Then by the assumption, for x, y∈A ,
0 = Π( S∗Tx,y ) = Π( S∗xyopS)− Π( S∗Sxy op)
= Π(|S|)Π( V ∗xyopV )Π(|S|)− Π(|S|2)Π( xyop).
It holds that
(5.3) Π( |S|2)Π( xyop) = Π(|S|)Π( V ∗xyopV )Π(|S|).
By taking the adjoint of this equation and by exchanging x, y by x∗, y∗, we get that
Π(|S|2)Π( xyop) = Π( xyop)Π(|S|2), for all x, y∈A ,
so that Π( |S|) commutes with Π( xyop) for all x, y∈A . Since Π( |S|) is invertible by assumption,
by applying Π(|S|)−1 to (5.3) from left and right, we get
Π( xyop) = Π( V ∗xyopV ), for all x, y∈A .
We conclude that V ∗xyopV− xyop is compact for all x, y∈A .
Finally by the weak containment assumption, there is a bound ed∗-homomorphism
ϕ :A⊗A op→ C∗{xyop∈ B(H)| x, y∈A} ; ϕ(x⊗ yop) = xyop.
Then if P := V ∗V = 1, the composition Ad( V ∗)◦ ϕ works as a desired ucp map θ. For the general
case, Ad( V ∗)◦ ϕ is a ucp map into P B(L2(M ))P . Since 1 − P is compact, by using a ﬁxed state
φ on A⊗min Aop, we can consider φ(·)(1− P ) + Ad(V ∗)◦ ϕ as a desired ucp map. □
We now investigate suﬃcient conditions such that the assump tions of Proposition 5.2 are satisﬁed.
