---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-021-71-picard-vessiot-theory-and-examples
section_title: "Picard-Vessiot theory and examples"
section_number: 7.1
pages: 49-53
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Consider a ﬁeldF provided with an automorphismφ of inﬁnite order.
The ﬁeld of constantsC := {f ∈ F | φ(f)= f } is supposed to be alge-
braically closed. A diﬀerence moduleM is a ﬁnite dimensional vector space
over F, provided with a bijective additive map Φ :M → M satisfying
Φ(fm)= φ(f)Φ(m). After choosing a basis ofM over F, the equation
Φ(m)= m translates into a matrix diﬀerence equationy = Aφ(y) with
A ∈GLn(F).
A Picard-Vessiot ringPV for M (or y = Aφ(y)) is a commutativeF-
algebra with unit element satisfying
1. An extension ofφ as automorphism ofPV is given.
2. PV has noφ-invariant ideals except{0} andPV .
3. There is aU ∈GLn(PV ) withU =Aφ(U).
4. PV is generated overF by the entries ofU andU −1.
With the methods of [vdP-S 1,2] one shows the existence and unicity of
PV (up toφ-isomorphisms). One observes thatPV is reduced and has in
– 712 –
Galois theory ofq-diﬀerence equations
general zero divisors. The ﬁeld of constants of the total ring of fractions of
PV is againC.
The naive deﬁnition of the diﬀerence Galois groupG of M is: G is the
‘abstract’ group of theF-automorphisms ofPV commuting withφ. This
deﬁnition is insuﬃcient in positive characteristic. A more precise deﬁnition
is the following. One deﬁnes a covariant functorG from the category of the
ﬁnitely generated commutativeC-algebras R to the category of groups by
G(R)isthegroupoftheautomorphismsof R⊗
CPV whichare R⊗CF-linear
and commute with the action ofφ. It can be shown thatG is represented
by an aﬃne group scheme of ﬁnite type overC. The diﬀerence Galois group
G is by deﬁnition this group scheme.
If the ﬁeldF has characteristic zero thenG is a reduced linear alge-
braic group. In our case, whereF has characteristicp> 0, the diﬀerence
Galois group need not be reduced. In the following examples we calculate
the Picard-Vessiot rings and their diﬀerence Galois groups for some typical
equations. For all examples we takeF = ˆK = C((z)) with C as before.
Since the examples are pure modules, one may replaceˆK by K = C({z})
everywhere. For convenience, we calculate for modulesM the ‘contravari-
ant solutions’, i.e., ker(Φ− 1,Hom
(M,PV )) , in stead of the ‘covariant
solutions’, i.e., ker(Φ−1,PV ⊗M).
Example 1.— The extension ˆK ⊂ ˆK(z1/p) is the Picard-Vessiot exten-
sion for the diﬀerence equationφ(y)= q1/py. Its diﬀerence Galois group is
the groupµp,C. More generally,ˆK(z1/n) is the Picard-Vessiot extension of
an equationφ(y)= qt/ny with (t,n) = 1 and its diﬀerence Galois group
is µn,C. We recall thatµn,C = Spec(C[t]/(tn −1)), with co-multiplication
given byt ↦→t ⊗t.
Example 2.— Equation φ(y)= cy with c ∈ C∗. Suppose that for all
n /greaterorequalslant1 the only solution ofφ(y)= cny in ˆK isy = 0, then the Picard-Vessiot
extension is ˆK[Y,Y −1] withφ(Y)= cY and the diﬀerence Galois group is
Gm,C.
Suppose that there exists a non zeroy ∈ ˆK such thatφ(y)= cay for some
a /greaterorequalslant1. Then c has the formζqt/n with ζ a primitive dth root of unity
and n /greaterorequalslant1, (t,n) = 1. We consider the two equationsφ(y)= qt/ny and
φ(y)= ζy separately. The ﬁrst equation is considered in example 1. The
second equation has Picard-Vessiot ring ˆK[y] with equationyd = 1 and
φ(y)= ζy. This ring has obviously zero divisors (ifd> 1). Its diﬀerence
Galoisgroupis µd,C ∼= Z/ZdoverCsincedisnotdivisibleby p.ThePicard-
Vessiot extension forφ(y)= cy is a subring of ˆK[z1/n][y]. The diﬀerence
Galois group is therefore a quotient of the groupµn,C × Z/Zd.
– 713 –
Marius van der Put, Marc Reversat
Example 3.— Um = ˆK ⊗V with dimV = m, Φ(1 ⊗v)=1 ⊗U(v)
and U ∈ GL(V) the indecomposable unipotent operator. There exists an
elemente ∈V such thate,(U −1)e,..., (U −1)m−1e is a basis ofV. Hence
Um ∼= ˆK[Φ,Φ−1]/ ˆK[Φ,Φ−1]((Φ −1)m). Thus we have to ﬁnd the Picard-
Vessiot ring for the equation (φ −1)m(y)=0 .
(a) Suppose that 1<m ⩽ p. The diﬀerence ringA1 := ˆK[𝓁], deﬁned
by 𝓁p −𝓁= 0 andφ(𝓁)= 𝓁+ 1, has only trivialφ-invariant ideals. The
elements
(𝓁
i
)
for i =0 ,...,m − 1 are C-linear independent solutions of
(φ −1)m(y) = 0. SinceA1 is generated over ˆK by 𝓁one ﬁnds thatA1 is
the Picard-Vessiot extension for the equation (φ −1)m(y)=0 .L e tR be a
C-algebra andσ aR⊗C automorphism ofR ⊗CK[𝓁], which commute with
φ. Thenσ is determined byσ(𝓁) andσ(𝓁)= 𝓁+a where a is any element
in R with ap =a. The diﬀerence Galois group is therefore the groupZ/Zp
over C. In view of further equations we write𝓁=𝓁1.
(b) Suppose thatp<m ⩽p2. The Picard-Vessiot ring for (φ −1)m(y)
=0i s A2 := ˆK[𝓁1,𝓁2], deﬁned by𝓁p
1 −𝓁1 =0 ,𝓁p
2 −𝓁2 =0 , φ(𝓁1)=
𝓁1 +1,φ (𝓁2)= 𝓁2 +
(𝓁1
p−1
)
. The set of maximal ideals ofA2 is {(𝓁1 −a,
𝓁2 −b)|a,b ∈ Fp} ∼= F2
p.Onecalculatesthat φactstransitivelyonthissetand
one concludes thatA2 has only trivialφ-invariant ideals. One observes that
(φ−1)p(𝓁2)=( φ−1)p−1(
( 𝓁1
p −1
)
) = 1 and (φ−1)p2−1
( 𝓁2
p −1
)( 𝓁1
p −1
)
=1 .
The conclusion is thatC[𝓁1,𝓁2] is the kernel of (φ −1)p2
, acting onA2. This
shows thatA2 is generated by the solutions of (φ −1)my = 0 and thus that
A2 is indeed the Picard-Vessiot ring.
Wehavetorepresentthefunctor G,givenby G(R)isthegroupofthedif-
ference automorphism ofR ⊗CA2 overR ⊗CK. For the calculation ofG(R)
we suppose for convenience that Spec(R) is connected. Thena ∈R, ap =a
impliesa ∈ Fp. FurtherFp[𝓁1,𝓁2]= {ξ ∈R ⊗C A2|ξp =ξ and (φ −1)p2
ξ =
0}.T h u sa n yσ ∈G (R) induces an automorphism ofFp[𝓁1,𝓁2] commuting
withφ. On the other hand, any automorphism ofFp[𝓁1,𝓁2] commuting with
φ, extends uniquely to an element ofG(R).
The algebra Fp[𝓁1,𝓁2] is seen asFp[φ]-module. The elementξ =
(𝓁2
p−1
)
·(𝓁1
p−1
)
is a generator and the module can be written asFp[t]/(tp2
), where
t = φ − 1. We recall thattp2−1ξ = 1. Thus an automorphismσ satisﬁes
σξ =aξ with a ∈ Fp[t]/(tp2
) anda ≡ 1m o d(t). On the other hand anya,
as above, produces a unique automorphism. The above group is the cyclic
group of orderp
2, generated bya =1+ t mod(tp2
). Thus the diﬀerence
Galois group is equal to the groupZ/Zp2 over C.
– 714 –
Galois theory ofq-diﬀerence equations
(c)Inasimilarwayoneobtainsthatthediﬀerencering Ak := ˆK[𝓁1, ··· ,𝓁k],
given by the equations𝓁p
i −𝓁i = 0 fori=1,...,k and
(φ −1)(𝓁i)=
(𝓁i−1
p −1
)(𝓁i−2
p −1
)
···
( 𝓁1
p −1
)
fori=2,...,k and(φ−1)𝓁1 = 1,isthePicard-Vessiotringfor( φ−1)my =0
for m such thatpk−1 <m ⩽ pk. Its diﬀerence Galois group is the group
Z/pkZ over C. As in the casek = 2, the diﬀerence Galois group is identiﬁed
with the group of the automorphisms ofZ := Fp[𝓁1,...,𝓁k] which commute
with φ.N o wZ,a sa Fp[φ]= Fp[t]-module (with t = φ − 1), has ξ =(𝓁k
p−1
)(𝓁k−1
p−1
)
···
(𝓁1
p−1
)
as cyclic element, and is isomorphic toFp[t]/(tpk
). The
automorphismsaregivenbytheelements a ∈ Fp[t]/(tpk
)with a ≡1mod( t).
This group is cyclic of orderpk and has generatora=1+ t mod(tpk
).
Example4.— M = ˆK(z1/n)e,Φe=zt/newithn /greaterorequalslant1,(t,n)=( p,n)=1 .
The corresponding scalar equation isφn(y)= qt(n−1)/2zty. By deﬁnition,
PV contains an invertible elementα satisfying the equation. Any other
solutiony has the form ˜yα withφn(˜y)=˜y. HencePV contains ˆK[y1] with
yn
1 = 1 andφ(y1)= ζny1 where ζn is a primitiventh root of unity. The
invertible elementu := φ(α)α−1 satisﬁes the equationφn(u)= qtu. All
solutions of the latter equation have the formzt/ny with φny =y.T h u sy
is an invertible element ofC[y1]. It follows thatzt/n and z1/n are inPV .
After changingα we may suppose thatu =zt/n. This leads to the assertion
that the Picard-Vessiot ring is ˆK(z1/n)[y1,α,α −1] with the rules:yn
1 =
1,φ (y1)= ζny1 (with ζn a primitiventh root of unity);α transcendental
over ˆK and φ(α)= zt/nα. The elements {yi
1α| i =0 ,...,n − 1} form a
C-basisofsolutions.Theinclusion ˆK[z1/n][y1] ⊂ ˆK[z1/n][y1,α,α −1]induces
an exact sequence for the diﬀerence Galois group, namely
1 → Gm →G →µn ×µn →1.
The termµn ×µn is the diﬀerence Galois group of the Picard-Vessiot ex-
tension ˆK(z1/n)[y1] of the equationφn(y)= qy.
Example 5. One considers the diﬀerence moduleM = ˆK(z1/p)e with Φe =
zt/pe (and 1 ⩽ t<p ), seen as diﬀerence module of dimensionp over
ˆK. A corresponding scalar equation isφp(y)= qt(n−1)/2zty. The method
of example 4 yields that the Picard-Vessiot extension forM is PV =
ˆK(z1/p)[𝓁1,α,α −1], satisfying the following rules:𝓁p
1 −𝓁1 = 0 andφ(𝓁1)=
𝓁1 +1 , α is transcendental over ˆK and φ(α)= zt/pα. The inclusion
– 715 –
Marius van der Put, Marc Reversat
ˆK(z1/p)[𝓁1] ⊂ ˆK(z1/p)[𝓁1,α,α −1], induces an exact for the diﬀerence Galois
groupG
1 → Gm →G → Z/pZ ×µp →1.
The group Z/pZ ×µp is the diﬀerence Galois group of the Picard-Vessiot
extension ˆK(z1/p)[𝓁1] of the equationφp(y)= qy.
Example 6.— M = ˆK(z1/pk
)e with Φe=zt/pk
e and (t,p) = 1. A corre-
sponding scalar equation isφpk
(y)= qt(pk −1)/2zty. The Picard-Vessiot ring
is ˆK(z1/pk
)[𝓁1,...,𝓁k,α,α −1] with φ(α)= zt/pk
α. The diﬀerence Galois
group admits an exact sequence
1 → Gm →G → Z/pkZ ×µpk →1.
