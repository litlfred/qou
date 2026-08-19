---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI"
section_id: sec-004-22-yangbaxter-operator
section_title: "Yang–Baxter operator"
section_number: 2.2
pages: 5-10
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
dimensional vector space V .
Deﬁnition 2.6. For an n-braid β, we deﬁne T(R,µ,a,b)(β)∈ C by the following
formula.
T(R,µ,a,b)(β) := a−w(β)b−n Tr1
(
Tr2
(
···
(
Trn
(
Φ( β)µ⊗n))
···
) )
,
where w(β) is the sum of the exponents in β. Note that Tr 1 : End( V )→ C is the
usual trace.
Example 2.7. For the braid σ1σ−1
2 σ1σ−1
2 , we have
T(R,µ,a,b)(σ1σ−1
2 σ1σ−1
2 )
= b−2 Tr1
(
Tr2(Tr3((R⊗ IdV )(IdV⊗R−1)(R⊗ IdV )(IdV⊗R−1)(µ⊗ µ⊗ µ)))
)
since w(σ1σ−1
2 σ1σ−1
2 ) = +1− 1 + 1− 1 = 0 (Figure 9).
⇒ a−w(β)b−n×
Figure 9. A braid and its invariant
We can show that T(R,µ,a,b) gives a link invariant.
Theorem 2.8 (Turaev [36]). If β and β′ present the same link, then TR,µ,a,b(β) =
TR,µ,a,b(β′).
6 HITOSHI MURAKAMI
Sketch of a proof. By Markov’s theorem (Theorem 2.2) it is suﬃcient to prove that
TR,µ,a,b is invariant under a braid relation, a conjugation and a stabilization.
The invariance under a braid relation σiσi+1σi = σi+1σiσi+1 follows from Fig-
ure 10. Note that the left hand side depicts a braid relation (2.1) and the right
hand side depicts the corresponding Yang–Baxter equation (Deﬁn ition 2.3 (1)).
=
braid relation
Φ
− →
 =
Yang–Baxter equation
Figure 10. braid relation corresponds to the Yang–Baxter equation
The invariance under a conjugation follows from Figure 11. The ﬁrst equality
follows since Trk is invariant under a conjugation. The second equality follows since
(µ⊗µ)R = R(µ⊗µ) (Deﬁnition 2.3 (2)). Note that the equality ( µ⊗µ)R = R(µ⊗µ)
means that a pair µ⊗ µ can pass through a crossing.
= =
Figure 11. invariance under a conjugation
To prove the invariance under a stabilization, we ﬁrst note that if a h omomor-
phism f : V ⊗n→ V ⊗n given by
f (ei1⊗···⊗ ein ) =
N −1∑
j1,...,jn=0
f j1,...,jn
i1,...,in (ej1⊗···⊗ ejn ),
then its n-fold trace is given by
Tr1(··· (Trn(f ))··· ) =
∑
j1,...,jn
f j1,...,jn
j1,...,jn .
AN INTRODUCTION TO THE VOLUME CONJECTURE 7
Therefore if g is a homomorphism g : V⊗ V → V⊗ V given by gk1,k2
l1,l2 , then we have
Tr1
(
···
(
Trn
(
Trn+1
(
(f⊗ IdV )(Id⊗(n−1)
V ⊗g)
) )))
=
∑
j1,...,jn,kn,kn+1
f j1,...,jn−1,kn
j1,...,jn−1,jn gjn,kn+1
kn,kn+1,
which coincides with the n-fold trace of the homomorphism f
(
Id⊗(n−1)
V ⊗ Tr2(g)
)
: V ⊗n→
V ⊗n.
Therefore for β∈ Bn we have
Tr1
(
Tr2
(
···
(
Trn
(
Trn+1
(
Φ( βσ ±1
n )µ⊗(n+1)
)))
···
) )
= Tr1
(
Tr2
(
···
(
Trn
(
Trn+1
(
(µ⊗nΦ( β)⊗ IdV )(Id⊗(n−1)
V ⊗R±1(IdV⊗µ))
)))
···
) )
= Tr1
(
Tr2
(
···
(
Trn
(
(µ⊗nΦ( β))(Id⊗(n−1)
V ⊗ Tr2(R±1(IdV⊗µ)))
))
···
) )
=a±1b Tr1
(
Tr2
(
···
(
Trn
(
(µ⊗nΦ( β))
) )
···
) )
=a±1b Tr1
(
Tr2
(
···
(
Trn
(
(Φ( β)µ⊗n)
) )
···
) )
,
since Tr 2
(
R±1(IdV⊗µ
)
= a±1b IdV (Deﬁnition 2.3 (3)) as depicted in Figure 12.
Since w(βσ ±1
n ) = w(β)± 1, the invariance under a stabilization follows. □
= a±1b
Figure 12. invariance under a stabilization
Therefore we can deﬁne a link invariant TR,µ,a,b(L) to be TR,µ,a,b(β) if L is the
closure of β.
8 HITOSHI MURAKAMI
2.4. Quantum (g, V ) invariant. One of the important ways to construct an en-
hanced Yang–Baxter operator is to use a quantum group, which is a deformation
of a Lie algebra.
Let g be a Lie algebra. Then one can deﬁne a quantum group Uq(g) as a de-
formation of g with q a complex parameter ([4], [12]). Given a representation
ρ : g→ gl(V ) of g one can construct an enhanced Yang–Baxter operator. The
corresponding invariant is called the quantum ( g, V ) invariant. For details see [36].
To deﬁne the colored Jones polynomial we need the Lie algebra sl2(C) and
its N -dimensional irreducible representation ρN : sl2(C) → gl(VN ). The quan-
tum ( sl2(C), VN ) invariant is called the N -dimensional colored Jones polynomial
JN (L; q).
A precise deﬁnition is as follows.
Put V := CN and deﬁne the R-matrix R : V⊗ V → V⊗ V by
R(ek⊗ el) :=
N −1∑
i,j=0
Rij
klei⊗ ej,
where
Rij
kl :=
min(N −1−i,j)∑
m=0
δl,i+mδk,j−m
{l}!{N− 1− k}!
{i}!{m}!{N− 1− j}!
× q
(
i−(N −1)/2
)(
j−(N −1)/2
)
−m(i−j)/2−m(m+1)/4,
(2.2)
with{e0, e1, . . . , eN −1} is the standard basis of V ,{m} := qm/2−q−m/2 and{m}! :=
{1}{2}···{ m}. Here q is a complex parameter. A homomorphism µ : V → V is
given by
µ(ej) :=
N −1∑
i=0
µi
jei
with
µi
j := δi,jq(2i−N +1)/2.
Then it can be shown that ( R, µ, q(N 2−1)/4, 1) gives an enhanced Yang–Baxter
operator.
Deﬁnition 2.9 (colored Jones polynomial) . For an integer N≥ 1, put V := CN
and deﬁne R and µ as above. The N -dimensional colored Jones polynomial JN (L; q)
for a link L is deﬁned as
JN (L; q) := T(R,µ,q(N 2 −1)/ 4,1)(β)× {1}
{N} ,
where β is a braid presenting the link L.
Remark 2.10. Note that JN (unknot; q) = 1 since
Tr1(µ) =
N −1∑
i=0
q(2i−N +1)/2 ={N}
{1} .
The two-dimensional colored Jones polynomial J2(L; q) is (a version) the original
Jones polynomial [14] as shown below.
AN INTRODUCTION TO THE VOLUME CONJECTURE 9
L+ :
,
L− :
,
L0 :
Figure 13. skein triple
Lemma 2.11. Let L+, L−, and L0 be a skein triple, that is, they are the same
links except for a small disk as shown in Figure 13. Then we hav e the following
skein relation:
qJ2(L+; q)− q−1J2(L−; q) = ( q1/2− q−1/2)J2(L0; q).
Proof. By the deﬁnition, the R-matrix is given by
R =




q1/4 0 0 0
0 q1/4− q−3/4 q−1/4 0
0 q−1/4 0 0
0 0 q1/4




with respect to the basis {e0⊗ e0, e0⊗ e1, e1⊗ e0, e1⊗ e1} of V⊗ V , and µ is given
by
µ =
( q−1/2 0
0 q1/2
)
with respect to the basis {e0, e1} of V .
Therefore we can easily see that
(2.3) q1/4R− q−1/4R−1 = (q1/2− q−1/2) IdV⊗ IdV .
Since L+, L−, and L0 can be presented by n-braids βσiβ′, βσ −1
i β′, and ββ ′
respectively, we have
(
qJ2(L+; q)− q−1J2(L−; q)
)
×{2}
{1}
=q× q−3(w(ββ ′)+1)/4 Tr1(Tr2(··· (Trn(Φ( βσiβ′)µ⊗n))))
− q−1× q−3(w(ββ ′)−1)/4 Tr1(Tr2(··· (Trn(Φ( βσ −1
i β′)µ⊗n))))
=q−3w(ββ ′)/4
×
(
q1/4 Tr1(Tr2(··· (Trn(Φ( βσiβ′)µ⊗n))))− q−1/4 Tr1(Tr2(··· (Trn(Φ( βσ −1
i β′)µ⊗n))))
)
=q−3w(ββ ′)/4
×
{
Tr1(Tr2(··· (Trn(Φ( β)(Id⊗(i−1)
V ⊗q1/4R⊗ Id⊗(n−i−1)
V )Φ( β′)µ⊗n))))
− Tr1(Tr2(··· (Trn(Φ( β)(Id⊗(i−1)
V ⊗q−1/4R−1⊗ Id⊗(n−i−1)
V )Φ( β′)µ⊗n))))
}
(from (2.3))
=q−3w(ββ ′)/4(q1/2− q−1/2) Tr1(Tr2(··· (Trn(Φ( ββ ′)µ⊗n))))
=(q1/2− q−1/2)J2(L0; q)×{2}
{1} ,
completing the proof. □
10 HITOSHI MURAKAMI
Remark 2.12. The original Jones polynomial V (L; q) satisﬁes
q−1V (L+; q)− qV (L−; q) = ( q1/2− q−1/2)V (L0; q)
[14, Theorem 12]. So we have J2(L; q) = (−1)♯(L)−1V (L; q−1), where ♯(L) denotes
the number of components of L.
