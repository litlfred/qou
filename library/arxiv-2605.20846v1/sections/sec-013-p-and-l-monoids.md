---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-013-p-and-l-monoids
section_title: "P and L Monoids"
section_number: null
pages: 70-74
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Inspired by the list of relations which define theG 1 andG 2 presentations of Cob(3)S2,
we define the following monoids in symmetric monoidal categories, in anticipation that
they will come from a 3d TFT.
Definition 5.1.1.(Sketch, P/L monoids) Let (A,1,m,tr,m ∨) be a commutative
Frobenius monoid in a symmetric monoidal category (C,⊗,1 ⊗). We say thatAis
a P-monoid if there exist endomorphismse p∈EndC(A) wherepis a diffeomorphism
class of oriented irreducible prime 3 manifolds, satisfying
1. (Prime commutativity)e p◦ep′ =e p′◦ep
2. (Legs and waist relations)e p◦m=m◦(e p⊗idA) =m◦(id A⊗ep)
3. (Colegs and cowaist relations)m ∨◦ep = (ep⊗idA)◦m ∨ = (idA⊗ep)◦m ∨.
We say thatAis aL-monoid if there exist morphisms 1 p∈HomC(1⊗,A) wherep
is a diffeomorphism class of irreducible oriented prime 3 manifolds, satisfying
1. (Legs relations)m◦(1 p⊗idA) =m◦(id A⊗1p).
The sketch definition has an immediate consequence:
Lemma 5.1.2.There is a bijection ofPmonoids andLmonoids.
Proof.Let (A,1,m,tr,m ∨) be aPmonoid, withe p a prime endomorphism. We may
define the corresponding prime unit as 1 p =e p◦1.
Similarly ifAis anLmonoid with 1 p a prime unit, we may define the corresponding
prime endomorphisme p ase p =m◦(1 p⊗idA) =m◦(id A⊗1p).
It is easy to check that the proposed prime units and prime endomorphisms satisfy
the desired conditions.
Remark5.1.3.By essentially the same proofs of propositions 4.4.6 - 4.4.10, not all of
the conditions above are necessary. Proposition 4.2.9 shows that the legs relations for
Ato be anL-monoid is induced by commutativity ofAbeing a commutative Frobe-
nius algebra. Hence all commutative Frobenius monoids equipped with morphisms
1p∈HomC(1⊗,A), wherepis a diffeomorphism class of irreducible oriented prime 3
manifold, is anL-monoid. Similarly, proposition 4.4.7, 4.4.6, 4.4.10, and 4.4.8 shows
70
that prime commutativity, waist relations, colegs and cowaist relations are implied
by commutative Frobenius relations and legs relations. Therefore any commutative
Frobenius monoid equipped with prime endomorphismse p∈HomC(A) satisfying the
legs relationsm◦(e p⊗idA) =m◦(id A⊗ep) is aP-monoid.
Comment5.1.4.In light of lemma 5.1.2 and the previous remark, one may wonder why
there is a slight asymmetry betweenPmonoids andLmonoids. Both are commutative
Frobenius algebras, both come equipped with maps labelled by diffeomorphism classes
of oriented prime 3 manifolds, yetPmonoids require that the maps satisfy some
relations whileLmonoids don’t. This is because for any commutative Frobenius object
Xthere is a canonical injection
HomC(1⊗,X),→End C(X).
sendingf: 1 ⊗→Xtom◦(f⊗id X)◦λ −1
X :X ∼= 1⊗⊗X→X⊗X→X.
Hence, heuristically speaking, one may find that there are more endomorphisms.
The legs relations say that only those induced by a prime unit are prime endomorphisms
in aP-monoid. This is best illustrated in the following two examples.
Proposition 5.1.5.If(C,⊗,1 ⊗)is the category(Sets,×,{∗}), then a prime endo-
morphisme p of aPmonoid ofCacts by multiplication by the element1 p(∗) =e p(1A),
where1 p is the prime unit of the correspondingLmonoid.
Proof.LetAbe aPmonoid ande p :A→Abe a prime endomorphism. Then it
satisfy the legs and waist relatione p◦m=m◦(e p⊗idA) =m◦(id A⊗ep) :A⊗A→A.
Meaning that
ep(a·b) =e p(a)·b=a·e p(b).
Let 1A∈Abe the multiplicative unit with respect tom. Then
ep(a) =e p(a·1 A) =e p(a)·1 A =a·e p(1A).
for alla∈A. Thereforee p acts by multiplication by the elemente p(1A).
Since 1A∈Ais the image of the unit map 1 :{∗}→A, we may identifye p(1A) =
ep(1(∗)) with the compositione p◦1. By lemma 5.1.2, the composition 1 p =e p◦1 is
the prime unit in the correspondingLmonoid.
Remark5.1.6.The same proof establishes that in the category (Veck k,⊗,k) a prime
endomorphisme p acts by multiplication by the element 1 p :k→A, or equivalently
ep◦1 where 1 :k→Ais the unit. Note that there are more linear endomorphisms of a
vector space than linear maps of the formk→A. IfAis finite dimensional, the former
is given byn×nmatrices while the latter byn×1. Hence for there to be a bijection
betweenPandLmonoids (algebras), it is necessary to impose the legs relations on
the prime endomorphisms to rule out the endomorphisms not induced by prime units.
We are now finally ready to give the most compact definition forPandLmonoids.
Definition 5.1.7.(P/L monoids) Let (A,1,m,tr,m ∨) be a commutative Frobenius
monoid in a symmetric monoidal category (C,⊗,1⊗). Then the following are equivalent,
1. There exist morphisms 1 p∈HomC(1⊗,A), wherepis a diffeomorphism class of
oriented irreducible prime 3 manifolds. We sayAis aL-monoid.
71
2. There exist endomorphismse p∈End(A) that satisfiesm◦(e p⊗idA) =m◦(id A⊗
ep), wherepis a diffeomorphism class of oriented irreducible prime 3 manifolds.
We sayAis aP-monoid.
The equivalence is exhibited by 1p =e p◦1 ande p =m◦(1 p⊗idA) =m◦(id A⊗1p).
Restricting ourselves to the setting of (Vect k,⊗,k), we can say a bit more about
the prime units and prime endomorphisms:
Definition 5.1.8.(P/L algebras) Let (A,1,m,tr,m ∨) be a commutative Frobenius
algebra overk. We sayAis aLalgebra if there are elements{1 p∈A}for allp
diffeomorphism classes of oriented irreducible prime 3 manifold. Equivalently, we say
Ais aPalgebra if there are linear endomorphisms{e p}that acts by multiplications by
the element 1p. The equivalence is exhibited by 1 p =e p(1) ande p =m◦(1 p⊗idA) =
m◦(id A⊗ep).
Theorem 5.1.9.LetZ: Cob(3) S2→Cbe a symmetric monoidal functor. ThenZ(S 2)
is aP/L- monoid. In the caseC= Vect k,Z(S 2)is aP/L-algebra.
Proof.By proposition 3.2.2 and corollary 3.5.4, (Z(S 2),Z(1),Z(m),Z(tr),Z(m ∨)) is
a commutative Frobenius algebra. The prime units 1 p∈HomC(1⊗,Z(S 2)) are given
byZ([p\D 3]).
Theorem 5.1.10.LetZ: Cob(3)→Cbe an oriented 3-dimensional topological field
theory. ThenZ(S 2)is aP/L-monoid. In the caseC= Vect k,Z(S 2)is aP/L-algebra.
Proof.This is a corollary to the previous theorem 5.1.9: every 3-dimensional TFT
induces a symmetric monoidal functor
Cob(3)S2 ,→Cob(3) Z→C.
sendingS 2 toZ(S 2). Therefore the imageZ(S 2) is aP/L-monoid/algebra.
Comment5.1.11.What is surprising aboutP/Lalgebras and their existence through
theorem 5.1.9 and 5.1.10 is their simplicity. The only novel structures on anLalgebra,
besides the commutative Frobenius structures, are the existence of distinguished ele-
ments 1p labelled by diffeomorphism classes of oriented irreducible prime 3 manifolds.
There are no relations among them. This is a feature imposed by geometry, not a
bug. The only novel structures on aPalgebra besides the commutative Frobenius
structures are the distinguished endomorphismse p. Geometry forces these to act by
multiplication by 1p, and there are no additional relations. Hence definition 5.1.8 and
theorem 5.1.10 together can be thought of as a statement of the “structural collapse”
on the algebraic structures ofZ(S 2).
Remark5.1.12.We make the following observations. LetZ: Cob(3)→ Cbe an
oriented 3-dimensional topological field theory. Denote bye M :Z(S 2)→Z(S 2) the
imageZ([M\(D 3⊔D 3)]) whereMis a closed oriented 3 manifold. Then
eM#N =e M◦eN =e N◦eM.
In particular, ifP,Qwere oriented prime 3 manifolds, we recover the commutativity
of prime endomorphisms
eP#Q =e P◦eQ =e Q◦eP.
72
This means that the assignmentM7→e M is a monoid map
({Closed oriented 3 manifolds}/ ∼=,#)→End C(Z(S 2)).
In particular, this map sendsS 3 to the identityid Z(S2).
Example 8.ForZ: Cob(3)→Vect k, wherekis algebraically closed, since the prime
endomorphisms{e p}are pairwise commuting, there exists a basis onZ(S 2) such that
all thee p are simultaneously upper-triangular. Equivalently, there exists a flag
0 =V 0⊂V 1⊂···⊂V n =Z(S 2),dimV i =i.
such that everye M preserves everyV i. Since each quotientV i/Vi−1 is one-dimensional,
eM acts on the quotient by scalar multiplications. Call this scalarχ i(M)∈k. Since
eM#N =e M◦eN, their actions on the quotientV i/Vi−1 must satisfy
χi(M#N) =χ i(M)χi(N).
Therefore this “character theory” of closed oriented 3 manifolds is completely deter-
mined by the character theory of oriented irreducible prime 3 manifolds.
Example 9.In fact, we can say more in some special cases. Consider the same setup
as above. LetMbe the set of diffeomorphism classes of oriented irreducible prime 3
manifolds. Consider
A=k[{e p|p∈M}].
This is a commutative subalgebra of End C(Z(S 2)). SinceZ(S 2) is finite dimensional,
so isA.
IfZ(S 2) happens to be semisimple as anA-module, thenZ(S 2) is a direct sum
of simpleA-modules. ButAis commutative, so all its simple modules are one-
dimensional. Therefore
Z(S 2)∼=
M
λ
kλ.
Over any linek λ, everya∈Aacts by some scalar. Denote this scalar asλ(a) or, if
a=e M for some closed 3 manifoldM, byχ λ(M). Then we still have
χλ(M#N) =χ λ(M)χλ(N).
The mapa7→λ(a) definesλ:A→kfor eachλ. We may group the same 1 kλ’s
together and obtain the direct sum decomposition ofZ(S 2) into spaces with the same
character
Z(S 2) =
M
λ
Vλ.
Then eache M acts by
eM|Vλ =χ λ(M)idVλ.
or equivalently
eM =
X
λ
χλ(M)πλ.(5.1)
1We consider two linesk λ1,kλ2 the same ofλ 1 =λ 2 as mapsA→k.
73
whereπ λ :Z(S 2)→V λ are the projection maps.
The prime endomorphisms are thosee M whereMis an oriented irreducible prime
3 manifoldP. So these act by
eP =
X
λ
χλ(P)πλ.(5.2)
Example 10.The example above provides a simple way of computing the invariants
Z(M) for any closed 3 manifoldM. LetZ: Cob(3)→Vect k wherekis algebraically
closed. IfZ(S 2) is semisimple as anA-module whereAis the commutative subalgebra
A=k[{e p|p∈M}]⊂End Vectk(Z(S 2)), then the example above shows thate P acts by
equation 5.2. If 1 :k→Z(S 2) is the unit map andtr:Z(S 2)→kthe trace map, then
for any closed 3 manifoldM ∼=P1#...#P m, we have
Z(M) =tr◦e M◦1 =
X
λ
(tr◦π λ◦1)χλ(M) =
X
λ
(tr◦π λ◦1)
mY
i=1
χλ(Pi).
Note however that the simplicity of this formula comes at the cost of needing to compute
the charactersχ λ(Pi) which may be equally challenging as computingZ(M) via other
methods.
