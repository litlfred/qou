---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-032-62-dynamical-twists-of-hopf-algebras-we-describe
section_title: "Dynamical twists of Hopf algebras. We describe a method of construct-"
section_number: 6.2
pages: 24-25
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
ing twists of quantum groupoids, which is a ﬁnite-dimensional modiﬁca tion of the
construction proposed in [Xu] and is dual to that of [EV], cf. [EN].
Dynamical twists ﬁrst appeared in the work of Babelon [Ba], see also [B BB].
Let U be a Hopf algebra and A = Map( T, k) be a commutative and cocom-
mutative Hopf algebra of functions on a ﬁnite Abelian group T which is a Hopf
subalgebra of U . Let Pµ, µ∈ T be the minimal idempotents in A.
Deﬁnition 6.2.1. We say that an element x in U ⊗n, n ≥ 1 has zero weight if
x commutes with ∆ n(a) for all a ∈ A, where ∆ n : A → A⊗n is the iterated
comultiplication.
Deﬁnition 6.2.2. An invertible, zero-weight U ⊗2-valued function J(λ) on T is
called a dynamical twist for U if it satisﬁes the following functional equations :
(∆ ⊗ id)J(λ)(J(λ +h(3)) ⊗ 1) = (id ⊗ ∆) J(λ)(1 ⊗J(λ)),(55)
(ε ⊗ id)J(λ) = (id ⊗ε)J(λ) = 1 .(56)
Here an in what follows the notation λ+h(i) means that the argument λ is shifted by
the weight of the i-th component, e.g., J(λ+h(3)) = ∑
µ J(λ+µ)⊗Pµ ∈U ⊗2 ⊗kA.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 25
Note that for every ﬁxed λ ∈ T the element J(λ) ∈U ⊗U does not have to be
a twist for U in the sense of Drinfeld. It turns out that an appropriate object f or
whichJ deﬁnes a twisting is a certain quantum groupoid that we describe nex t.
Observe that the simple algebra End k(A) has a natural structure of a cocommu-
tative quantum groupoid given as follows (cf. Section 2.5) :
Let {Eλµ}λ,µ∈T be a basis of End k(A) such that
(Eλµf )(ν) = δµνf (λ), f ∈A, λ,µ,ν ∈ T,(57)
then the comultiplication, counit, and antipode of End k(A) are given by
∆( Eλµ) = Eλµ ⊗Eλµ, ε (Eλµ) = 1, S (Eλµ) = Eµλ.(58)
Deﬁne the tensor product quantum groupoid H = End k(A) ⊗kU and observe
that the elements
Θ =
∑
λµ
Eλλ+µ ⊗EλλPµ and ¯Θ =
∑
λµ
Eλ+µλ ⊗EλλPµ(59)
deﬁne a twist for H. Thus, according to Proposition 6.1.2, HΘ = (End k(A) ⊗kU )Θ
becomes a quantum groupoid . It is non-commutative, non-cocomm utative, and
not a Hopf algebra if |T|> 1.
It was shown in [EN], following [Xu], that HΘ can be further twisted by means of
a dynamical twist J(λ) on U . Namely, if J(λ) is a dynamical twists on U embedded
inH ⊗kH as
J(λ) =
∑
λ
EλλJ (1)(λ) ⊗EλλJ (2)(λ),(60)
then the pair ( F (λ), ¯F (λ)), where
F (λ) = J(λ)Θ and ¯F (λ) = ¯ΘJ −1(λ)
deﬁnes a twist for H = End k(A) ⊗k U . Thus, every dynamical twist J(λ) for a
Hopf algebra U gives rise to a quantum groupoid HJ =HJ(λ)Θ .
Remark 6.2.3. According to Proposition 6.1.2, the antipode SJ of HJ is given by
SJ (h) = v−1S(h)v for all h ∈HJ , where S is the antipode of H and
v =
∑
λµ
Eλ+µλ(S(J (1))J (2))(λ)Pµ.
Remark 6.2.4. There is a procedure dual to the one described above. It was show n
in [EV] that given a dynamical twist J(λ) it is possible to deform the multiplication
on the vector space D = Map( T × T, k) ⊗kU ∗ and obtain a dynamical quantum
group DJ . The relation between HJ and DJ in the case when dim U < ∞ was
established in [EN], where it was proven that DJ is isomorphic to H ∗op
J .
