---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-002-21-mellin-transform
section_title: "Mellin transform"
section_number: 2.1
pages: 8-13
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
8
algebra in Section 4. Then we describe the details of weights and multip lier algebra
of a C∗-algebra, and its GNS construction and modular theory in the von Ne umann
setting. Next we explain the signiﬁcance of the multiplicative unitary t hat is im-
portant in the study of locally compact quantum groups. Finally we co llect several
technical results concerning the calculations involving q-commuting variables.
2.1 Mellin transform
In this subsection, let us recall the Mellin transform of a function an d its properties.
Theorem 2.1. Let f (x) be a continuous function on the half line 0 < x <∞.
Then its Mellin transform is deﬁned by
φ(s) := (Mf )(s) =
∫ ∞
0
xs−1f (x)dx, (2.1)
whenever the integration is absolutely convergent for a<Re (s)<b . By the Mellin
inversion theorem, f (x) is recovered from φ(s) by
f (x) := (M−1φ)(x) = 1
2π
∫ c+i∞
c−i∞
x−sφ(s)ds, (2.2)
wherec∈ R is any values in between a and b.
We have the following analyticity theorem [29]:
Theorem 2.2. (Strip of analyticity) If f (x) is a locally integrable function on
(0,∞) such that it has decay property:
f (x) =
{ O(x−a−ǫ) x−→ 0+
O(x−b+ǫ) x−→ +∞ (2.3)
for every ǫ > 0 and some a < b, then the Mellin transform deﬁnes an analytic
function (Mf )(s) in the strip
a<Re (s)<b.
(Analytic continuation) Assume f (x) behaves algebraically for x−→ 0+, i.e.
f (x)∼
∞∑
k=0
Akxak, (2.4)
whereRe(ak) increases monotonically to∞ ask−→∞ . Then the Mellin transform
(Mf )(s) can be analytically continued into Re(s)≤a =−Re(a0) as a meromorphic
function with simple poles at the points s =−ak with residue Ak.
A similar analytic property holds for the continuation to th e right half plane.
(Growth) If f (x) is a holomorphic function of the complex variable x in the
sector−α< argx<β where 0<α,β ≤π, and satisﬁes the growth property (2.3)
9
uniformly in any sector interior to the above sector, then (Mf )(s) has exponential
decay in a<Re (s)<b with
(Mf )(s) =
{ O(e−(β−ǫ)t) t−→ +∞
O(e(α−ǫ)t) t−→−∞ (2.5)
for any ǫ> 0 uniformly in any strip interior to a<Re (s)<b , where s =σ +it.
(Parseval’s Formula)
∫ ∞
0
f (x)g(x)xz−1dx = 1
2πi
∫ c+i∞
c−i∞
(Mf )(s)(Mg)(z−s)ds, (2.6)
whereRe(s) = c lies in the common strip for Mf andMg. In particular we have
∫ ∞
0
|f (x)|2dx = 1
2π
∫ ∞
−∞
|(Mf )( 1
2 +it)|2dt. (2.7)
2.2 Weight and multiplier algebra of a C ∗-algebra
In this subsection, we recall the deﬁnition of weights on a C∗-algebra, and the
language of multiplier algebra. Most of the notions are adopted from [24, 40]. Let
A be a C∗-algebra andA+ its positive self-adjoint elements.
Deﬁnition 2.3. A weight on a C∗-algebraA is a function φ :A+−→ [0,∞] such
that
φ(x +y) = φ(x) +φ(y), (2.8)
φ(rx) = rφ(x), (2.9)
for x,y∈A +,r∈ R>0.
Deﬁnition 2.4. Given a weight φ onA, we deﬁne
M+
φ = {a∈A + :φ(a)<∞}, (2.10)
Nφ = {a∈A :φ(a∗a)<∞}, (2.11)
Mφ = span{y∗x :x,y∈N φ}. (2.12)
Then it is known that M+
φ =Mφ∩A +, and that φ extends uniquely to a map
Mφ−→ C. A weight is called faithful iﬀ φ(a) = 0 =⇒a = 0 for every a∈A +.
Next we recall a useful notion of a multiplier algebra. Let B(H) be the algebra
of bounded linear operators on a Hilbert space H.
Deﬁnition 2.5. IfA⊂B (H) as operators, then the multiplier algebra M (A) ofA
is the C∗-algebra of operators
M (A) ={b∈B (H) : bA⊂A ,Ab⊂A}. (2.13)
In particular,A is an ideal of M (A).
10
Example 2.6. Important examples include
M (K(H)) =B(H), (2.14)
whereK(H) are compact operators on H, and
M (C0(X)) = Cb(X), (2.15)
where X is a locally compact Hausdorﬀ space, C0(X) is the algebra of C-valued
functions on X vanishing at inﬁnity equipped with the sup-norm, and Cb(X) is the
C∗-algebra of all bounded continuous functions on X.
Proposition 2.7. LetA andB beC∗-algebras. A homomorphism φ :A−→ M (B)
is called non-degenerate if the linear span of φ(A)B and ofBφ(A) are both equal to
B. Then φ extends uniquely to a homomorphism M (A)−→M (B). In particular,
by taking B = C, every weight ω onA has a unique extension to M (A).
Using the notion of a multiplier algebra, the concept of a multiplier Hopf algebra
is introduced in [41] (see also [40]). In particular, the coproduct ∆ of A will be
a non-degenerate homomorphism ∆ : A−→ M (A⊗A ). The coassociativity is
well-deﬁned from the proposition above.
Given a multiplier Hopf * algebra A with coproduct ∆, we can deﬁne left and
right invariance of a functional.
Deﬁnition 2.8. A linear functional h onA is called a left invariant Haar functional
if it satisﬁes
(1⊗h)(∆ x) = h(x)· 1M(A), (2.16)
where 1M(A) is the unital element in M (A).
Similarly, a right invariant Haar functional satisﬁes
(h⊗ 1)(∆ x) = h(x)· 1M(A). (2.17)
2.3 GNS representation and Tomita-Takesaki’s theory
Let us recall the main objects in the study of GNS representation o f a C∗-algebra
(see e.g. [24]).
Deﬁnition 2.9. A Gelfand-Naimark-Segal (GNS) representation of a C∗-algebra
A with a weight φ is a triple
(H,π, Λ),
whereH is a Hilbert space, Λ : A−→H is a linear map, and π :A−→B (H) is a
representation ofA onH such that Λ(N ) is dense in H, and
π(a)Λ(b) = Λ( ab) ∀a∈A,b∈N , (2.18)
⟨Λ(a), Λ(b)⟩ = φ(b∗a) ∀a,b∈N , (2.19)
whereN ={a∈A :φ(a∗a)<∞}.
11
The Tomita-Takesaki’s Theory [39, 40] provides a detailed descriptio n of the
GNS-construction in the von Neumann algebraic setting:
Deﬁnition 2.10. Giving a weight φ that determines the Hilbert space structure by
the GNS construction, the operator
T :x−→x∗ (2.20)
is closable and has a polar decomposition as
T =J∇
1
2, (2.21)
whereJ is called the modular conjugation, and ∇ is called the modular operator.
A very important property of J is the following
Theorem 2.11 (Murray-von Neumann) . Let M be the completion of A⊂B (H)
in the weak operator topology as a von Neumann algebra. Then c onsidering M⊂
B(H), we have
JMJ =M ′, (2.22)
whereM ′ is the commutant of M .
Deﬁnition 2.12. Forx∈A , the operator
σφ
t (x) :=∇itx∇−it (2.23)
is called the modular automorphism group.
We have φ(a∗b) = φ(bσφ
0 (a∗))
On the Hopf * algebra level, we have the following properties:
Proposition 2.13. The antipode S has a polar decomposition
S =τ−i/2◦R, (2.24)
whereτ−i/2 denotes the analytic generator of (τt)t∈R, called the scaling group, which
is a group of automorphisms of M , and R, called the unitary antipode , is an anti-
automorphism of M .
We have R2 = 1 and S2 =τ−i.
Finally some properties concerning the left and right invariant Haar f unctional:
Proposition 2.14. The left invariant Haar functional φ and right invariant Haar
functional ψ are related by ψ =φ◦R.
We have
φ◦τt =ν−tφ, ψ ◦σφ
t =ν−tψ, (2.25)
whereν >0 is called the scaling constant.
Furthermore there exists an element δ∈A such that
σφ
t (δ) = νtδ,
whereδ∈A is called the modular element.
12
Proposition 2.15. The map Λ R :A−→H deﬁned by
Λ R(a) := Λ L(aδ− 1
2 ), (2.26)
gives the GNS representation of A with the right Haar functional on the same space
H, where δ is the modular element deﬁned above.
