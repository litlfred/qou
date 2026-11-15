---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-013-41-some-facts-about-subfactors
section_title: "Some facts about subfactors"
section_number: 4.1
pages: 81-92
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
Let N C M be I], factors with 7~! = [M : N] < co. We adopt standard
notation so that M;, i = 0,1,2,... is the tower of [J1] with Mj) =M, M, =
(M,en), Misi = (Mj, e:+1) where e; : L?(M;_1) > L?(M;_2) is orthogonal

81
projection, eN = e1. Let B = {b} be a ﬁnite subset of M (called a basis)
with
(4.1.1)
X
b∈B
be1b∗= 1 .
Then by [PP] and [Bi],
(4.1.2)
x(
X
b
be1b∗) = (
X
b
be1b∗)x = x
for x ∈M.
(4.1.3)
X
b
bb∗= τ −1
(4.1.4)
X
b
bEN(b∗x) = x =
X
b
EN(xb)b∗
for x ∈M.
(4.1.5)
For x ∈N′ (on L2(M)),
τ
X
b
bxb∗= EM′(x) .
4.1.6 Recall that the subfactor is called extremal if the normalized traces on
N′ and M coincide on N′ ∩M in which case the traces on N′ ∩Mk, realized
on L2(M), coming from Mk and N′ coincide for all k, and EM′(e1) = τ.
4.1.7 By standard convex averaging procedures on L2(Mk), given a ﬁnite
subset X = {x} of Mk and ε > 0, there is a ﬁnite set U = {u} of unitaries
in M and λu ∈R+, P
u∈U λu = 1 with
∥
X
u
λuuxu∗−EM′(x)∥2 < ε
for x ∈X.
Further averaging does not make the estimate worse, so by averaging again
with P
u λuAd u∗and gathering together repeated terms if necessary, we may
assume U∗= U and λu∗= λu.
It will be convenient to renormalize the ei’s so we set Ei = δei with
δ2τ = 1 (δ > 0). (Note that there is a very slight notational clash with §2,
but we will show it to be consistent.) We then have the formulae
(4.1.8)
E2
i = δEi ,
EiEj = EjEi
if |i −j| ≥2,
EiEi±1Ei = Ei ,
E1xE1 = δEN(a)E1 and P
b bE1e2E1b∗= 1 so that {bE1 | b∈B} is a basis for
M1 over M.
82
Deﬁnition 4.1.9. For k = 1, 2, 3, . . . let vk = EkEk−1 . . . E1 ∈N′ ∩Mk.
(Note vkxv∗
k = δEN(x)Ek for x ∈M, v∗
kvk = δE1.)
Theorem 4.1.10 If xi, i = 1, . . ., k+1 are elements of M then x1v1x2v2 . . . vkxk+1 =
x1v∗
kx2v∗
k−1 . . . v∗
1xk+1, and the map x1 ⊗x2 ⊗. . .⊗xk+1 7→x1v1x2v2 . . . vkxk+1
deﬁnes an M−M bimodule isomorphism, written θ, from M⊗NM⊗N. . .⊗NM
(with k + 1 M’s), written Nk+1
N
M, onto Mk.
Proof. See [J5], Corollary 11.
Recall that if R is a ring and B is an R −R bimodule, an element b of B
is called central if rb = br ∀r ∈R.
Corollary 4.1.11 The centralizer N′ ∩Mk is isomorphic under θ to the
vector space Vk+1 of central vectors in the N −N bimodule Nk+1
N
M.
We now deﬁne the most interesting “new” algebraic ingredient of sub-
factors seen from the planar point of view. It is the “rotation”, known to
Ocneanu and rediscovered by the author in speciﬁc models. See also [BJ1].
Deﬁnition 4.1.12. For x ∈Mk we deﬁne
ρ(x) = δ2EMk(vk+1 EM′(xvk+1))
Proposition 4.1.13 ρ(Mk) ⊆N′ ∩Mk and if B is a basis, ρ coincides on
N′ ∩Mk with r : Mk →Mk, r(x) = EMk(vk+1
P
b∈B bxvk+1b∗).
Proof. This is immediate from 4.1.5.
□
Lemma 4.1.14 With θ as above,
θ−1rθ(x1 ⊗x2 ⊗. . . ⊗xk+1) =
X
b∈B
EN(bx1)x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗b∗
83
Proof.
r(x1v1x2v2 . . . vkxk+1)
=
X
b
EMk(vk+1bx1v∗
k+1x2v∗
k . . . v∗
1b∗)
=
δ
X
b
EMk(Ek+1EN(bx1)x2v∗
k . . . v∗
1b∗)
(by(4.1.9))
=
X
b
EN(bx1)x2v∗
k . . . v∗
1b∗
=
X
b
θ(EN(bx1)x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗b∗)
□
Note that the rotation on Nk+1
C
M does not pass to the quotient Nk+1
N
M,
however we have the following.
Lemma 4.1.15 Suppose N ⊂M is extremal, then
ρ(θ(x1 ⊗x2 ⊗. . . ⊗xk+1)) = EN′(θ(x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗x1))
Proof. If x = θ(x1 ⊗x2 ⊗. . . ⊗xk+1) and y = θ(x2 ⊗x3 ⊗. . . ⊗x1), it
suﬃces to show that tr(ρ(x)a) = tr(ya) for all a in N′ ∩Mk. Let ε > 0 be
given and choose by 4.1.7 a ﬁnite set U of unitaries in M, with U = U∗, and
λu ∈R+, P
u∈U λu = 1, λu∗= λu so that
∥
X
u
λuvk+1uxvk+1u∗−vk+1EM′(xvk+1)∥2 < ε ,
and, by extremality, ∥P
u λuuE1u∗−δ−1∥2 < ε. So, if y ∈M,
(4.1.16)
|
X
u
λuuEN(u∗y) −τy∥2 < ε∥y∥
(by(4.1.8)and ∥ab∥2 ≤∥a∥∥b∥2.
So
|tr((ρ(x) −y)a|
=
|tr(δ2EMk(vk+1EM′(xvk+1)) −y)a|
<
|tr(δ2EMk(vk+1
X
u
λuuxvk+1u∗) −y)a| + δ2ε∥a∥2
=
|tr(δ2 X
u
λuEN(ux1)θ(x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗u∗) −y)a| + δ2ε∥a∥2
84
(as in the proof of 4.11)
=
|δ2((tr
X
u
λuθ(x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗u∗EN(ux1)) −θ(y))a) + δ2ε∥a∥2
(since a ∈N′)
=
|δ2tr(θ(x2 ⊗x3 ⊗. . . ⊗xk+1 ⊗(
X
u
λuuEN(u∗x1) −x1))a)∥2 + δ2ε∥a∥2
(since U = U∗,
λu = λu∗) .
For ﬁxed x1, x2, . . . , xk+1 and a, this can clearly be made as small as desired
by 4.1.16, by choosing ε small.
□
Corollary 4.1.17 If x ∈N and ξ ∈L2(Mk), ρ(xξ −ξx) = 0.
Proof. By its deﬁnition, ρ extends to a bounded linear map from L2(Mk)
to itself, so it suﬃces to show the formula for ξ of the form θ(x1 ⊗x2 ⊗. . . ⊗
xk+1). But if n ∈N,
EN′(θ(x2 ⊗. . . ⊗xk+1 ⊗nx1)) = EN′(θ(x2 ⊗. . . ⊗
xk+1n ⊗x1)), so by 4.1.15 we are done.
□
Theorem 4.1.18 If N ⊂M is extremal, ρk+1 = id on N′ ∩Mk.
Proof. Recall that if H is an N −N bimodule (correspondence as in
[Co]) then ⟨η, xξ −ξx⟩= ⟨x∗η −ηx∗, ξ⟩for x ∈N and ξ, η ∈H. So η is
central iﬀit is orthogonal to commutators.
Hence Lemma 4.1.15 reads
ρ(θ(x1 ⊗x2 ⊗. . . ⊗xk+1)) = θ(x2 ⊗x3 ⊗. . . ⊗x1) + ξ
where ξ ∈κ, which we deﬁne to be the closure of the linear span of com-
mutators in the N −N correspondence L2(Mk). Applying ρ to both sides of
this equation, and 4.1.17, we obtain
ρ(θ(x1 ⊗. . . ⊗xk+1)) −θ(x3 ⊗x4 ⊗. . . ⊗x1 ⊗x2) ∈κ
and continuing,
ρk+1(θ(x1 ⊗. . . ⊗xk+1)) −θ(x1 ⊗x2 ⊗. . . ⊗xk+1) ∈κ .
So, by linearity, if x ∈N′ ∩Mk, ρk+1(x) −x ∈κ. But both ρk+1(x) and x
are central, so orthogonal to κ and ρk+1(x) = x.
□
85
We now deﬁne ﬁve types of maps between centralizers using the isomor-
phism θ. Choose a basis B.
Deﬁnition 4.1.19. If x = x1 ⊗x2 ⊗. . . ⊗xk ∈Nk
N M,
(1) For j = 2, 3, . . ., k,
aj(x) = δ(x1 ⊗x2 ⊗. . . ⊗xj−1E(xj) ⊗. . . ⊗xk) ∈Nk−1
N
M,
and a1(x) = δE(x1)x2 ⊗. . . ⊗xk.
(2) For j = 2, 3, . . ., k,
µj(x) = x1 ⊗x2 ⊗. . . ⊗xj−1xj ⊗. . . ⊗xk) ∈Nk−1
N
M
(3) For j = 2, 3, . . ., k,
ηj(x) = x1 ⊗x2 ⊗. . . ⊗xj−1 ⊗1 ⊗xj ⊗. . . ⊗xk) ∈Nk−1
N
M,
and η1(x) = 1 ⊗x1 ⊗. . . ⊗xk.
(4) For j = 1, 2, . . ., k,
κj(x) = δ−1 P
b∈B x1⊗. . .⊗xjb⊗b∗⊗xj+1⊗. . .⊗xk) ∈Nk−1
N
M
(5) If θ(c) ∈N′ ∩Mn−1 deﬁne αj,k ⊗k
N M →⊗k+n
N
M by
αj,c(x) = x1 ⊗. . . ⊗xj−1 ⊗c ⊗xj ⊗. . . ⊗xk
(α1,c(x) = c ⊗x, αk+1,c(x) = x ⊗c. Note also αj,1 = ηj.)
Note all these maps are N middle linear (for (5) this requires b to be central;
for (4) we use 4.1.2), so they are deﬁned on the tensor product over N. They
are all N−N bimodule for maps so they preserve central vectors and are thus
deﬁned on the space Vk of N-central elements of ⊗k
NM (= θ−1(N′ ∩Mk−1)).
We will use the same notation for the restrictions of these maps to the Vk.
Note that κj does not depend on the basis, indeed κj(x) = µj+1αj+1,id(x)
where θ(id) is the identity of N′ ∩M, is a basis-independent formula for κj.
Lemma 4.1.20 If c ∈Vk and d ∈Vk′, then
(i) αd,j+kαc,i = αc,iαd,j for i ≤j.
(ii) For i < j, aj−1ai = aiaj, µj−1µi = µiµj.
For i ≤j, ηj+1ηi = ηiηj, κj+1κi = κiκj.
(iii) For i ≤j,
aj+kαc,i = αc,iaj
aj−1αc,j = αc,j−1ai−1
86
µj+k+1αc,i = αc,iµj+1
µi−1αc,j = αc,j−1µi−1
ηj+kαc,i = αc,iηj
ηi−1αc,j−1 = αc,jηi−1
κj+kαc,i = αc,iκj
κi−1αc,j = αc,j+1κi−1
(iv) For i < j,
µjai = aiµj+1
µiaj = aj−1µi
ηj−1ai = aiηj
ηi+1aj = aj+1ηi+1
κj−1ai = aiκj
κiaj = aj+1κi
ηj−1µi = µiηj
ηiµj = µj+1ηi
κj−2µi = µiκj−1
κiµj = µj+1κi
κjηi = ηiκj−1
κiηj = ηj+1κi
(v)
aiκi = id
µiηi = id
ai+1κi = id
µi+1ηi = id
(vi)
ajηj = δid
µj+1κj = δid.
(These identities hold when i, j and k are such that all the maps involved
are deﬁned by 4.1.19.)
Proof. Almost all cases of identities (i)–(iv) are trivial as they can be
written so as to involve distant tensor product indices: thus they just amount
to a renumbering. The ones that involve some interaction between the tensor
product components are
µiµi = µiµi+1 ,
κi+1κi = κiκi ,
κi−1µi = µiκi ,
κiµi+1 = µi+2κi .
87
These all follow easily from associativity of multiplication and
X
b∈B
b⊗b∗x=
X
b∈B
xb ⊗b∗for x ∈M, which is 4.1.2.
For (v): aiκi
=
id follows from
X
b∈B
EN(xb)b∗= x
(4.1.4)
µiηi
=
id follows fromx1 = x
ai+1κi
=
id follows from
X
b∈B
bE(b∗x) = x
(4.1.4)
µi+1ηi
=
id follows from x1 = x
For (vi): ajηj
=
δid follows from EN(1) = 1
µj+1κj
=
δid follows from
X
b∈B
bb∗= δ2id
(4.1.3)
□
Lemma 4.1.21
If
x ∈M,
2 ≤r ≤k, then
vkxvr = vr−2xvk (where
v0 = 1), and vkxv1 = δEN(x)vk.
Proof. Simple manipulation of 4.1.8 and 4.1.9.
□
Lemma 4.1.22 If x ∈⊗k
NM, then
(i) θ−1EMk−2θ(x) = δ−1am+1(x) if k is odd, k = 2m + 1.
(ii) θ−1EMk−2θ(x) = δ−1µm+1(x) if k is even, k = 2m.
Proof. Let x be of the form x1 ⊗x2 ⊗. . . ⊗xk. Then
EMk−2(θ(x)) = EMk−2(x1v1x2v2 . . . vk−1xk) = δ−1x1v1x2v2 . . . xk−2vk−2xk−1vk−2xk
Case (i). If k = 2m + 1 we may apply 4.1.21 m−1 times to obtain
EMk−2(θ(x))
= δ−1x1v1 . . . xmvmxm+1v1xm+2vm+1 . . . xk−1vk−2xk
= x1v1 . . . xmvmE(xm+1)xm+2vm+1 . . . xk−1vk−2xk
= δ−1θ(am+1(x))
88
Case (ii). If k = 2m we apply 4.1.21 m−1 times to obtain
EMk−2(θ(x))
= δ−1x1v1 . . . xmvmxm+1v0xm+2vm+1 . . . xk−1vk−2xk
= δ−1θ(µm+2(x))
(since v0=1).
□
Lemma 4.1.23 If y ∈⊗k
NM and x, z ∈M, then
xv∗
kθ(y)vk+1z = θ(x ⊗y ⊗z)
Proof. Simple commutation of Ei with M and Ej’s j ≤i −2.
□
In the next lemma, let χj = ajµj+1, j = 1, 2, . . .k −1.
Lemma 4.1.24 If x, y ∈⊗k
NM, then θ(x)θ(y) =
(i) θ(χm+1χm+2 . . . χk(x ⊗N y)) if k is even, k = 2m.
(ii) θ(µm+2χm+2 . . . χk(x ⊗N y)) if k is odd, k = 2m + 1.
Proof. By induction on k. Let x = x1 ⊗x2 . . . ⊗xk+1, y = y1 ⊗y2 . . . ⊗
yk+1, then
θ(x)θ(y)
=
x1v∗
kkx2v∗
k−1 . . . v∗
1xk+1y1v1y2v2 . . . ykvkyk+1
=
δx1v∗
k−1EMk−2(θ(x2 ⊗x3 ⊗. . . ⊗xk+1)θ(y1 ⊗. . . ⊗yk))vkyk+1
(i) If k is even, k = 2m, by the inductive hypothesis we have
θ(x)θ(y)
=
δx1v∗
k−1EMk−2(θ(χm+1χm+2 . . . χk(x2 ⊗. . . ⊗xk+1 ⊗y1 ⊗. . . ⊗yk)))vkyk+1
=
x1v∗
k−1θ(µm+1χm+1 . . . χk(x2 ⊗. . . ⊗yk))vkyk+1 (by Lemma 4.1.22)
=
θ(x1 ⊗(µm+1χm+1χm+2 . . . χk(x2 ⊗. . . ⊗yk) ⊗yk+1)) (by Lemma 4.1.23)
=
θ(µm+2χm+2χm+3 . . . χk+1(x1 ⊗x2 ⊗xk+1 ⊗y1 ⊗. . . ⊗yk+1))
89
(ii) If k is odd, k = 2m + 1,
θ(x)θ(y)
=
x1v∗
k−1EMk−2(θ(µm+2χm+2χm+3 . . . χk(x2 ⊗. . . xk+1 ⊗y1 ⊗. . . ⊗yk)))vkyk+1
(by the induction hypothesis)
=
x1v∗
k−1θ(am+1µm+2χm+2χm+3 . . . χk(x2 ⊗. . . ⊗yk))vkyk+1
(by Lemma 4.1.22)
=
θ(x1 ⊗χm+1χm+2 . . . χk(x2 ⊗. . . ⊗yk) ⊗yk+1))
(by Lemma 4.1.23)
=
θ(χm+2χm+3 . . . χk+1(x1 ⊗x2 . . . ⊗yk+1)) .
It only remains to check the formula for k = 1, (m = 0). Then θ(x) = x,
θ(y) = y and the formula reads
θ(x)θ(y) = xy = θ(µ2(x ⊗y)) = θ(xy) .
□
Lemma 4.1.25 For m = 1, 2, . . ., and xm+1, xm+2, . . . x2m ∈M,
vmvm+1xm+1vm+2xm+2vm+3 . . . v2mx2m = vmxm+1vm+1xm+2 . . . v2m−1x2m .
Proof. Induction on m.
For m = 1 the formula reads E1E2E1x2 = E1x2 which is correct. Now
suppose the formula holds for m, then
vm+1vm+2xm+2 = vm+1xm+2Em+2Em+1 . . . E3
(by 4.1.8)
so
vm+1vm+2xm+2vm+3xm+3 . . . v2m+2x2m+2 = (vm+1xm+2)VmVm+1ym+1Vm+2ym+2 . . . V2my2m
where Vn = En+2En+1 . . . E3 and yn = E2E1xn+2.
We may now apply the inductive hypothesis to the subfactor M1 ⊂M2
(for which the Ei’s are just those for N ⊂M, shifted by 2), to obtain
vm+1xm+2Vmym+1 . . . V2my2m = vm+1xm+2vm+2xm+3 . . . v2m+1x2m+2
□
90
Corollary 4.1.26 With notation as above, for m = 2, 3, 4, . . .,
EmEm−1 . . . E2(vm+1xm+1)(vm+2xm+2) . . . (v2m−1x2m−1)
= (vm . . . xm+1)(vm+1xm+2) . . . (v2m−2x2m−1)
Proof. Write Vn = En+1En−1 . . . E2, yn = E1xn+1 and apply the 4.1.25
to the subfactor M ⊂M1.
□
Lemma 4.1.27 For p = 1, 2, . . .,
X
b1,b2,...bp∈B
(b1v1)(b2v2) . . .(bpvp)vp+1vp+2b∗
pvp+3b∗
p−1vp+4 . . . v2p+1b∗
1 = δpE2p+1
Proof. By induction on p. For p = 1 the formula reads
X
b∈B
bE1E2E1E3E2E1b∗= E3
X
b∈B
bE1b∗= δE3 ,
which is correct. Now observe that
X
b
bvpvp+1vp+2b∗vp+3 = δEpEp−1 . . . E2Vp−1VpVp+1E2E1
where Vn = En+2En+1 . . . E3, and that
b1v1b2v2 . . . bp−1vp−1EpEp−1 . . . E2 = y1V1y2V2 . . . yp−2Vp−2yp−1
where yi = biE1E2, so that
X
b1,...,bp∈B
b1v1b2v2 . . . bpvpvp+1vp+2b∗
pvp+3b∗
p−1vp+4 . . . v2p+1b∗
1
= δ
X
y1...yp−1∈BE1E2
y1V1y2V2 . . . yp−2Vp−2yp−1Vp−1VpVp+1y∗
p−1Vp+2 . . . V2p−1y∗
1
so since {bE1E2 | b ∈B} is a basis for M2 over M1, we are through by
induction.
□
Corollary 4.1.28 For p = 1, 2, . . .,
X
b1,b2,...,bp+1∈B
(b1v1)(b2v2) . . . (bpvp)b∗
pbp+1vp+1b∗
p+1vp+2b∗
p−1 . . . v2pb∗
1 = δp+1E2p
91
Proof. Observe that
X
bp,bp+1∈B
bpvpb∗
pbp+1vp+1b∗
p+1vp+2 = δ2Vp−1VpVp+1E1 ,
where Vn = En+1En . . . E2, so the left-hand side of the equation becomes
δ2
X
y1,...,yp−1
y1V1y2V2 . . . yp−1Vp−1VpVp+1y∗
p−1Vp+2 . . . V2p−1y∗
1
where yn = bnE1, and this is δp+1E2p by 4.1.27 applied to the subfactor
M ⊂M1 with basis {bE1 | b ∈B}.
□
