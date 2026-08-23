---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-019-canonical-basic-sets-for-hecke-algebras-from-rat
section_title: "Canonical basic sets for Hecke algebras from rational Cherednik algebras"
section_number: null
pages: 41-44
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
nik algebras
Let Θ and Hk(W ) be deﬁned as above. We have a decomposition matrix Dk for the specialised Hecke
algebraHk(W ) with respect to the specialisation Θ. The rows of Dk are indexed by Irr( W ) and its
columns by Irr(Hk(W )). Following Proposition 5.9, Dk can be obtained from the decomposition matrix
D of the categoryO by removing the columns that correspond to the simple modules killed by the KZ-
functor, that is, the columns labelled by Irr( W )\ B. This implies that Dk becomes lower unitriangular
when its rows are ordered with respect to <O, in the same way that, in the cases where Θ factors
through a cyclotomic Hecke algebra, the existence of a canonical basic set implies that Dk becomes
lower unitriangular when its rows are ordered with respect to the a-function. If we could show that
the a-function deﬁnes an ordering on the category O, we would automatically obtain the existence of a
canonical basic set for Hk(W ). At the same time, we would obtain the determination of B in the cases
where canonical basic sets have already been explicitly described.
5.2.1 The (a + A)-function
Let m = (mC,j)(C∈A/W)(0⩽j⩽eC−1) be a family of integers and letϕm :vC,j↦→qmC,j be the corresponding
cyclotomic specialisation for the Hecke algebra H(W ). Let θ : q↦→ η be a specialisation such that η
is a non-zero complex number. If η is not a root of unity or η = 1, then, due to Theorem 1.7 and the
form of the Schur elements ofHϕm(W ), the specialised Hecke algebraHη(W ) is semisimple. So we may
assume from now on that η is a root of unity of order e> 1, namely η =ζr
e for some r∈ Z>0 such that
gcd(e,r ) = 1.
38
Let k = (kC,j)(C∈A/W)(0⩽j⩽eC−1) be the family of rational numbers deﬁned by
kC,j := rNW
e mC,j for all C,j.
ThenHk(W ) = Hη(W ). Following [CGG, §3.3], we obtain the following equation which relates the
functions am and Am forHϕm(W ) with the c-function for Hk(W ):
am
E +Am
E = e
rNW
cE +
∑
H∈A
eC−1∑
j=0
mC,j for all E∈ Irr(W ), (5.2)
whereC denotes the orbit of H∈A under the action of W .
Remark 5.10 The above formula was also obtained in [GGOR,§6.2] for ﬁnite Weyl groups in the equal
parameter case.
Equation (5.2) implies that am +Am yields the same ordering on Irr(W ) as the c-function (note that
in this case cE∈ Q for all E∈ Irr(W )). Thus, am +Am is also an ordering on the category O, that is,
if [∆(E) : L(E′)]⁄= 0 for some E,E′∈ Irr(W ), then either E =E′ or am
E′ + Am
E′ < am
E + Am
E . If now
the function am is compatible with am +Am, that is, for all E,E′∈ Irr(W ),
am
E′ + Am
E′ < am
E + Am
E ⇒ am
E′ < am
E, (5.3)
thenam is an ordering on the categoryO and we obtain the existence of a canonical basic set forHϕm(W )
with respect to θ by Proposition 5.9. This is true in several cases, but unfortunately not true in general.
Some exceptional complex reﬂection groups where (5.3) holds and the above argument works are:
G23 =H3, G24, G27, G29 and G30 =H4.
This yields the existence of canonical basic sets for the groups G24, G27 and G29, which was not known
before. To summarise, we have the following [Ch6, Proposition 5.11]:
Proposition 5.11 Let W = Gn, n∈{ 23, 24, 27, 29, 30}. Let m and k be deﬁned as above, and let
E, E′ ∈ Irr(W ). If [∆(E) : L( E′)]⁄= 0 , then either E = E′ or am
E′ < am
E . In particular, we have
KZ(L(E))⁄= 0 if and only if E belongs to the canonical basic set of Hϕm(W ) with respect to θ :q↦→ζr
e .
5.2.2 Canonical basic sets for Iwahori–Hecke algebras
Equation (5.2) has also allowed us to show that, in the case where W is a ﬁnite Coxeter group, and
assuming that Lusztig’s conjectures P1 – P15 hold, thec-function is compatible with the ordering⩽LR
on two-sided cells, since a andA are (see [Ge8, Remark 5.4] for the a-function, [Lu6, Corollary 21.6] and
[ChJa1, Proposition 2.8] for A). This in turn was crucial in showing [CGG, Corollary 4.7]:
Proposition 5.12 Let (W,S ) be a ﬁnite Coxeter group and let Hq(W,L ) be the Iwahori–Hecke algebra
ofW with parameterL, as deﬁned in Chapter 2. For H∈A , let sH∈W be the reﬂection with reﬂecting
hyperplaneH and letC be the orbit of H under the action of W . If H′∈C , then we have L(sH) =L(sH′)
and we can set LC :=L(sH). Let e,r∈ Z>0 such that gcd(e,r ) = 1, and take, for all C∈A /W ,
kC,0 = rLC
e and kC,1 =−rLC
e .
If E∈ Irr(W ), then KZ(L(E))⁄= 0 if and only if E belongs to the canonical basic set of Hq(W,L ) with
respect toθ :q↦→ζr
e .
The proof uses a connection, established in [CGG, Proposition 4.6], between category O and the
cellular structure of the Iwahori–Hecke algebra. More speciﬁcally, if E∈ Irr(W ), then KZ(∆(E)) is iso-
morphic to the cell module Wθ(E) deﬁned in [Ge6, Example 4.4]; we will not go into further details here.
Note though that, in Proposition 5.12, we have not included the assumption that Lusztig’s conjectures
must hold. The reason is that the only case where they are not known to hold, the case of Bn, is covered
by Corollary 5.17 below.
39
Remark 5.13 The above result can be generalised to the case where kC,0 = λLC and kC,1 =−λLC
for any complex number λ. If λ∈ Z or λ∈ C\ Q, then both category O andHexp(2πiλ)(W,L ) are
semisimple, so the statement trivially holds. If λ is a negative rational number, let us say λ =−r/e for
some e,r∈ Z>0 with gcd(e,r ) = 1, and E∈ Irr(W ), then KZ(L(E))⁄= 0 if and only if E belongs to the
canonical basic set ofHq(W,−L) with respect to θ :q↦→ζr
e. We recall now that the canonical basic sets
for ﬁnite Coxeter groups where L can take negative values are described in [ChJa1]. In fact, E belongs
to the canonical basic set of Hq(W,−L) with respect to θ : q↦→ ζr
e if and only if E⊗ε belongs to the
canonical basic set of Hq(W,L ) with respect to θ, where ε denotes the sign representation of W .
Proposition 5.12 yields the existence of canonical basic sets for all ﬁnite Coxeter groups in a uniform
way. At the same time, it yields a description of the simple modules that are not killed by the KZ-
functor, since canonical basic sets for ﬁnite Coxeter groups are explicitly known (see, for example,
[GeJa2]). However, it does not imply that the a-function is an ordering on the category O, because we
do not know what happens with the simple modules killed by the KZ-functor. We do believe though
that, for ﬁnite Coxeter groups, the a-function is an ordering on the category O.
Example 5.14 Let W be the symmetric group Sn and let l := L(s) for every transposition s∈ Sn
(there exists only one orbit C inA/W ). Let η2l :=ζr
e for some e,r∈ Z>0 with gcd(e,r ) = 1. As we saw
in Example 2.14, the canonical basic setBθ ofHq(W,l ) with respect to θ :q↦→η consists of thee-regular
partitions of n. Now take kC,0 = r/2e and kC,1 =−r/2e. Let λ be a partition of n and let Eλ be the
corresponding irreducible representation of Sn. We have KZ(L(Eλ))⁄= 0 if and only if λ is e-regular.
5.2.3 Canonical basic sets for Ariki–Koike algebras
As we have said and seen earlier, there exist several orderings on the category O. For W = G(l, 1,n ),
where the irreducible representations are parametrised by the set P(l,n ) of l-partitions of n, one com-
binatorial ordering on the category O is given by Dunkl and Griﬀeth in [DuGr]. More precisely, in this
case, there are two hyperplane orbits in A/W ; we will denote them by Cs andCt. We have eCs =l and
eCt = 2. Let (s0,...,s l−1)∈ Zl and e∈ Z>0. We deﬁne k = (kCs,0,...,k Cs,l−1,kCt,0,kCt,1) by
kCs,j = sj
e − j
l for j = 0,...,l − 1, kCt,0 = 1
e, kCt,1 = 0. (5.4)
Then the KZ-functor goes from the category O of Hk(W ) to the category of representations of the
specialised Ariki–Koike algebraHk(W ) with relations
(s−ζs0
e )(s−ζs1
e )··· (s−ζsl−1
e ) = 0, (ti−ζe)(ti + 1) = 0 for i = 1,...,n − 1,
as in (4.4).
Let λ = (λ(0),...,λ (l−1))∈P (l,n ). We will denote by Eλ the corresponding irreducible representa-
tion of G(l, 1,n ). We deﬁne the set of nodes of λ to be the set
[λ] ={(a,b,c ) : 0⩽c⩽l− 1, a> 1, 1⩽b⩽λ(c)
a }.
Let γ = (a(γ),b (γ),c (γ))∈ [λ]. We set ϑ(γ) := b(γ)−a(γ) +sc(γ). We then have the following [DuGr,
Proof of Theorem 4.1]:
Proposition 5.15 Let λ, λ′∈P (l,n ). If [∆(Eλ) : L(Eλ′
)]⁄= 0, then there exist orderings γ1,γ 2,...,γ n
and γ′
1,γ′
2,...,γ ′
n of the nodes of λ and λ′ respectively, and non-negative integers µ1,µ 2,...,µ n, such
that, for all 1⩽i⩽n,
µi≡c(γi)−c(γ′
i) modl and µi =c(γi)−c(γ′
i) + l
e(ϑ(γ′
i)−ϑ(γi)).
Now, there are several diﬀerent cyclotomic Ariki–Koike algebras that produce the specialised Ariki–
Koike algebra Hk(W ) deﬁned above and they may have distinct a-functions attached to them. Let
u = (u0,...,u l−1)∈ Ql be a list of rational numbers such that 0 < uj−ui < ewhenever i < j. Set
tj := sj−uj, for all 0 ⩽ j⩽ l− 1, and t := (t0,...,t l−1). We then use the combinatorial description
of the a-function for G(l, 1,n ) given by (4.3), taking aEλ := a(t,1)(λ) for all λ∈P (l,n ). Note that this
40
deﬁnition captures all a-functions for G(l, 1,n ) in the literature: the function am for mCs,j = sjl−ej,
j = 0,...,l − 1, given by Jacon [Ja3] and studied in the context of Uglov’s work on canonical bases
for higher level Fock spaces, and also the a-function for type Bn (l = 2) arising from the Kazhdan–
Lusztig theory for Iwahori–Hecke algebras with unequal parameters (see [GeJa2, 6.7]). We have shown
in [CGG, §5] that this a-function is compatible with the ordering on category O given by Proposition
5.15. Consequently, the a-function also deﬁnes a highest weight category structure on O, that is, we
have the following:
Proposition 5.16 Let λ, λ′∈P (l,n ). If [∆(Eλ) : L(Eλ′
)]⁄= 0, then either λ = λ′ or aEλ′ <a Eλ.
The above result, combined with Proposition 5.9, yields the following:
Corollary 5.17 Let W =G(l, 1,n ). Let (s0,...,s l−1)∈ Zl and e∈ Z>0. Let k be deﬁned as in (5.4).
If λ∈P (l,n ), then KZ(L(Eλ))⁄= 0 if and only if Eλ belongs to the canonical basic set of Hk(W ) with
respect to the a-function above.
Thus, we obtain the existence of canonical basic sets for Ariki–Koike algebras without the use of
Ariki’s Theorem. On the other hand, the description of the canonical basic sets for Ariki–Koike algebras
by [Ja3, Main Theorem] yields a description of the set B ={Eλ∈ Irr(W )| KZ(L(Eλ))⁄= 0}: we have
that Eλ∈ B if and only if λ is an Uglov l-partition.
Finally, we expect a result similar to Corollary 5.17 to hold in the case where W = G(l,p,n ) for
p> 1.
Remark 5.18 By repeating the proof of [CGG, Proposition 4.6] for W =G(l, 1,n ), we can obtain that
the images of the standard modules via the KZ-functor agree with the Specht modules deﬁned by the
cellular structure on the Ariki–Koike algebras in [DJM], provided that the parameters k are chosen to
belong to the so-called “asymptotic region” (see [Ro2, Proposition 6.4] for the explicit description of this
region).
