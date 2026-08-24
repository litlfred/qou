---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem Paolo Dolce Francesco Zucconi 0 Introduction 1 0.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
section_id: sec-003-1-adelic-curves
section_title: "Adelic curves"
section_number: 1
pages: 3-7
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmi"
---
this product formula are called proper. The ﬁelds with a product formula of [ Cor97] are trivially
proper adelic curves when the set of places is endowed with th e counting measure. Moreover in
[Voj21, Section 3] it is shown that arithmetic function ﬁelds can be endowed with a structure of
proper adelic curve.
In this paper we prove two generalisations of Roth’s theorem for proper adelic curves. The main
results will be stated in terms of some inequalities involvi ng the integral of the measurable functions
ω ↦→log− |β −αi|ω where α1, . . . , αn ∈ K are the elements we want to approximate by an approximant
β ∈ K. Unfortunately, the bare deﬁnition of proper adelic curves is too general to give any meaningful
result in the direction of Roth’s approximation theorem, si nce the functions log − |β − αi| can be in
principle very “wild”. Therefore, we have to impose some ana lytic conditions on such functions in
order to get the desired Roth’s theorems. We will see that the se assumptions are not too artiﬁcial,
in fact we recover Theorems 0.2 and 0.3 as special cases.
The ﬁrst condition we impose on our adelic curves is the strong µ-equicontinuity (see deﬁnition
4.1): roughly speaking it means that for any set of ﬁnite measure S ⊂ Ω one requires for the functions
ω ↦→log |β|ω, to be “equicontinuous” almost everywhere on S. Under such hypothesis we prove the
following theorem:
Theorem (A). Let X = ( K, Ω , φ) be a proper adelic curve satisfying the strong µ-equicontinuity
condition. Let S = S1 ⊔ S2 ⊔ . . . ⊔ Sn ⊆ Ω be the disjoint union of subsets of ﬁnite measure. Fix some
distinct elements α1, . . . , αn ∈ K, then for any ε > 0 there exists a real constant C > 0 (depending
on the ﬁxed data) such that for any β ∈ K with hX(β) > C it holds that:
n∑
i=1
∫
Si
log− |β − αi|ωdµ(ω) > −(2 + ε)hX(β) . (2)
We will show that Theorem 0.2 is a consequence of Theorem (A), but on the other hand Vojta’s
inequality is stronger and moreover it doesn’t depend on the ﬁxed partition of S. Nevertheless, we
get a generalisation of Theorem 0.3 under the following hypotheses:
• We slightly relax the strong µ-equicontinuity condition and we allow the existence of arb itrary
small sets where the equicontinuity fails (see Deﬁnition 5.1).
• We assume that the functions ω → log− |β|ω are uniformly integrable while β varies (see deﬁni-
tion 5.2)
Our second main theorem is then the following:
Theorem (B). Let X = ( K, Ω , φ) be a proper adelic curve satisfying the µ-equicontinuity condition
and the uniform integrability condition. Fix some distinct elements α1, . . . , αn ∈ K. Let S be a
measurable subset of Ω of ﬁnite measure. Then for any ε > 0 and any c ∈ R there exists a real
constant C > 0 (depending on the ﬁxed data) such that for any β ∈ K with hX(β) > C it holds that:
∫
S
min
1≤i≤n
(
log− |β − αi|ω
)
dµ(ω) > −(2 + ε)hX(β) + c (3)
Finally, in Example 5.4 we show that the µ-equicontinuity condition doesn’t hold for all proper
adelic curves; in our example we consider Q endowed with a natural structure of adelic curve naturally
inherited from Q.
Our strategy consists in weaving together the ideas of Corva ja and Vojta to get rather elementary
proofs which are independent from Arakelov geometry. On the other hand we don’t have, at the
moment, any examples of interesting proper adelic curve diﬀ erent from the ones already known. It is
a much harder problem to ﬁnd new concrete cases in which Roth’ s theorem holds. After all, a highly
nontrivial achievement of Vojta’s work consists in showing that the µ-equicontinuity and the uniform
integrability hold for arithmetic function ﬁelds. He does t his by using the geometry of complex ﬁbres
at inﬁnity appearing in Arakelov geometry.
The very coarse overview of the proofs is the following: Roth ’s theorem is about the simultaneous
approximation of some distinct elements α1, . . . , αn that by simplicity (in fact it will be enough
to consider this case) can be ﬁxed in K, with an element β ∈ K. The existence of a very special
“interpolating polynomial” δ for such elements (section 2) allows us to write some integral estimates
for measurable functions on Ω satisfying some technical pro perties related to the heights of the
αi’s and β (section 3). Then, assuming that Roth’s theorem is false leads to the co nstruction of
a measurable function θ : S → R≥0 that gives the desired contradiction on the integral estima tes
previously found. The crucial point of the proof consists in the construction of θ, and this is exactly
where we need the additional technical conditions on the ade lic curve.
We ﬁnally mention that section 1 is a brief review of the theory of adelic curves introduced in
[CM20], and moreover that Appendix A sketches the construction of the interpolating polynomial
employed in [ Cor97].
3
Acknowledgements. Both the authors want to express their gratitude to Pietro Corvaja for
introducing them to the subject and for his enlightening exp lanations. They also want to thank
Lorenzo Freddi and Huyai Chen for replying to several questions.
A special mention goes to the anonymous referee for their inc redible peer-reviewing work with
this article. Their deep understanding of the topic and thei r compelling comments were extremely
useful to ﬁx some mistakes.
The ﬁrst author was partially supported by the EPSRC grant EP /M024830/1 “Symmetries and
correspondences: intra-disciplinary developments and ap plications”, partially by the research grant
“Higher Arakelov geometry, Cryptography and Isogenies of E lliptic Curves” conferred by the Univer-
sity of Udine, and partially by the Ben-Gurion university of the Negev.
The second author wants to thank his wife Elena.
1 Adelic curves
We will use the following notations throughout the whole pap er:
log+ x := max{0, log x} , log− x := min{0, log x} ; ∀x ∈ R>0
In this section we closely follow [ CM20, Chapter 3]. For simplicity we restrict to the characterist ic
0 case, but all the deﬁnitions work also in positive characte ristic.
Deﬁnition 1.1. Let K be a ﬁeld of characteristic 0, let MK be the set of all absolute values of K and
let Ω = (Ω , A, µ) be a measure space endowed with a map
φ : Ω → MK
ω ↦→ | · | ω := φ(ω) .
such that for any a ∈ K×, the real valued function ω ↦→log |a|ω lies in L1(Ω , µ). The triple
X = ( K, Ω , φ) is called an adelic curve ; Ω and φ are respectively the parameter space and the
parametrization. We denote with Ω ∞ the subset of Ω made of all elements ω such that | · | ω is
archimedean. We set Ω 0 := Ω \ Ω ∞.
Remark 1.2. We also recall that a more general notion of adelic curve, wit h the requirement that
| · |ω is an absolute value only almost everywhere for ω ∈ Ω, had been already given in [ Gub97] under
the name of M -ﬁeld.
It is easy to show that the set Ω ∞ is always measurable [ CM20, Proposition 3.1.1].
Deﬁnition 1.3. An adelic curve X = (K, Ω , φ) is said to be proper if for any a ∈ K×:
∫
Ω
log |a|ω dµ(ω) = 0 . (4)
Let’s see examples of adelic curves:
Example 1.4. Any ﬁeld ( k, Vk) satisfying the product formula in the sense of [ Cor97] is a proper
adelic curve. In fact in this case Ω = Vk, φ is the identity and µ is the counting measure.
Example 1.5. An arithmetic function ﬁeld K with a big polarisation is a proper adelic curve. A
quick description of this has been already given in section 0.1. For details see [ Voj21, Section 3].
Example 1.6. A polarised algebraic function ﬁeld (in d ≥ 1 variables) over a ﬁeld of characteristic
0 can be endowed with a structure of proper adelic curve. For d etails see [ CM20, 3.2.4].
In the remaining part of this section we study the behaviour o f adelic curves with respect to ﬁeld
extensions. In particular let’s ﬁx an adelic curve X = (K, Ω K, φK), and let L be a ﬁnite extension of K,
our goal is to endow it with a canonical structure of adelic cu rve “coming from K”. In other words,
we have to deﬁne a parameter space Ω L and a parametrization φL in a canonical way by starting from
Ω K and φK. For any ω ∈ Ω K we denote with ML,ω the set of absolute values of L extending | · | ω, so
we put:
Ω L :=
⨆
ω∈Ω K
ML,ω
and we have a natural projection map πL|K : Ω L → Ω K whose ﬁbres are ML,ω, for any ω. The inclusion
ML,ω ⊂ ML clearly induces a parametrization φL : Ω L → ML and for any ν ∈ Ω L we put | · |ν := φL(ν).
We obtain the following commutative diagram:
Ω L Ω K
ML MK
πL|K
φL φK (5)
4
where the bottom map is the restriction function. Note that Ω L can be abstractly deﬁned as the
ﬁbered product in the category of sets. Now on Ω L we put the σ-algebra B generated by πL|K and
all the real maps Ω L ∋ ν ↦→ |a|ν , for any a ∈ L× (on R we put the standard Lebesgue measure). We
want to deﬁne a suitable measure η on the measurable space (Ω L, B). This requires a bit of work,
since in general there is no straightforward deﬁnition of pu llback measure through a measurable map.
Nevertheless, in the case of our πL|K we explain how it is possible to deﬁne the pullback η = π∗
L|Kµ
(actually this is a construction from measure theory which w orks in full generality any time we have
a measure ﬁberwise). Consider a ﬁber ML,ω ⊂ Ω L, then for any ν ∈ ML,ω we can put
Pω(ν) := [Lν : Kω]
[L : K] (6)
where Lν and Kω denote the completions with respect to | · | ν and | · | ω respectively. Thanks to the
well known equality ∑
ν∈ML,ω
[Lν : Kω] = [ L : K] (See [ Neu99, Ch. II, Corollary 8.4]), we conclude
that equation ( 6) induces a probability measure on the ﬁbre ML,ω, with respect to the power set.
Now, for any function f : Ω L → R, by using the ﬁberwise integral along each probabilised ﬁbe r ML,ω,
we deﬁne the map IL|K(f ) : Ω K → R as:
IL|K(f ) : ω ↦→
∫
ML,ω
f dP ω =
∑
ν∈ML,ω
Pω(ν)f (ν)
Proposition 1.7. The linear operator IL|K sends B-measurable functions to A-measurable functions.
Proof. See [ CM20, Theorem 3.3.4].
At this point we are ready to deﬁne the measure η. For any E ∈ B we put:
η(E) :=
∫
Ω K
IL|K(χE) dµ (7)
where χE is the characteristic function of E. Note that the integral of equation ( 7) makes sense
because of Proposition 1.7.
Theorem 1.8. The following statements hold:
(1) The map η deﬁned above is a measure on (Ω L, B) such that for any B-measurable function f we
have ∫
Ω L
f d η =
∫
Ω K
IL|K(f ) dµ .
(2) f ∈ L1(η) if and only if IL|K(|f |) ∈ L1(µ).
(3) The pushforward measure of η through πL|K is µ.
(4) With the above constructions the triple Y = ( L, Ω L, φL) is an adelic curve. Moreover for any
b ∈ L×
[L : K]
∫
Ω L
log |b|ν dη(ν) =
∫
Ω K
log |NL|K(b)|ωdµ(ω) (8)
and in particular if X is proper, then also Y is proper.
Proof. See [ CM20, Theorem 3.3.7].
At this point we study algebraic extensions of adelic curves. Let’s ﬁx the adelic curve X =
(K, Ω K , φK) and let L an algebraic extension of K. We denote with FL|K the family of ﬁnite ﬁeld
extensions on K contained in L. Clearly FL|K is a directed set with respect to the inclusion, and for
any K′, K′′ ∈ F L|K such that K′ ⊆ K′′ we have a morphism of measurable spaces
πK′′|K′ : (Ω K′′ , B′′) → (Ω K′ , B′)
and an operator IK′′|K′ sending integrable functions to integrable functions as de scribed above in the
case of ﬁnite extensions. In other words we obtain an inverse system of measure spaces, and we
would like to deﬁne the adelic structure on L as “a projective limit”. Unfortunately, in the category
of measure spaces we don’t have a straightforward notion of p rojective limit, therefore we need again
a bit of extra work. We can deﬁne respectively ML,ω, Ω L and φL : Ω L → ML exactly as we did before
in the case of ﬁnite extensions, but we need to construct an ad equate structure of measure space on
Ω L. For any K ′ ∈ F L|K we have a map πL|K′ : Ω L → Ω K′ and a square diagram like ( 5). It turns out
that πL|K′ is surjective [ CM20, Proposition 3.4.5]. We endow Ω L with the σ-algebra Σ generated by
the maps {πL|K′ }K′∈FL|K , and it can be shown that (Ω L, Σ) is the projective limit of the inverse system
{(Ω K′ , B′)}K′∈FL|K in the category of measurable spaces. It remains the issue of putting a canonical
5
measure λ on (Ω L, Σ). This process is quite technical, but similarly to the cas e of ﬁnite extensions, it
can be done by using a ﬁberwise integration on each ML,ω; all the details are given in [ CM20, 3.4.2].
What we really need is the fact that we can construct an adelic curve ( L, Ω L, λ) which is proper if X
is proper and such that for any f ∈ L1(µ) we have that f ◦ πL|K ∈ L1(λ) with
∫
Ω L
(f ◦ πL|K)dλ =
∫
Ω K
f dµ . (9)
Below we give the notion of height for proper adelic curves:
Deﬁnition 1.9. Let X = ( K, Ω , φ) be a proper adelic curve and let K be an algebraic closure of K.
Then we have a proper adelic curve X = ( K, Ω , φ) and the (naive) height of an element a ∈ K
×
is
deﬁned as:
hX(a) :=
∫
Ω
log+ |a|ν dχ(ν) .
where ν denotes a generic element of Ω and χ is the measure on Ω. Moreover we set HX := ehX .
From now on we always assume that for an adelic curve X = ( K, Ω , φ) we have ﬁxed algebraic
closure of K, therefore also X is ﬁxed and we use the same notations of Deﬁnition 1.9. If for ν ∈ Ω,
| · |ν is an archimedean absolute value, then by Ostrowski’s theor em we know that there exists a real
number ε(ν) ∈ ]0, 1] such that | · | ν = | · | ε(ν) where on the right we mean the standard euclidean
absolute value on R or C. Thus we have a map ε : Ω ∞ →]0, 1] which can be extended to ε : Ω → [0, 1]
by putting ε|Ω 0 := 0. For instance, for an archimedean | · | ν we have log |2|ν = ε(ν) log 2, therefore
we obtain the explicit expression of the function ε on the whole Ω:
ε(ν) = log+ |2|ν
log 2 .
Clearly ε(ν) is a measurable function. We can always take a scaling µ′ of the measure µ on Ω so that
get a new height h′
X that satisﬁes h′
X(2) ≤ log 2. Notice that if X is proper, then it remains proper
after any scaling of the measure µ. From now on, when we are given an adelic curve X = ( K, Ω , φ),
we can always assume that we have performed the above mention ed scaling of the measure µ on Ω
so that hX(2) ≤ log 2.
Deﬁnition 1.10. Let P (X1, · · · , XN ) be a polynomial over K, α ∈ K
N
and i = ( i1, · · · , iN ) ∈ NN .
We set:
∆ iP (α ) := 1
i1!i2! · · · iN !
∂i1+i2+...+iN P
∂X i1
1 ∂X i2
2 . . . ∂XiN
N
(α ).
We can deﬁne the local height of P at ν ∈ Ω in the following way:
hν (P ) := log
(
max
i∈NN
{⏐⏐⏐∆ iP (0, . . . ,0)
⏐⏐⏐
ν
})
and then we have also the notion of global height of P :
hX(P ) :=
∫
Ω
hν (P )dχ(ν)
We put HX(P ) := ehX(P ).
The following estimates of log |∆ iP (α)|ω in terms of the local height of P will be very useful later:
Lemma 1.11. Let (K, |·| ω) be a ﬁeld with an absolute value. Let P ∈ K[X1, . . . XN ] such that N ≥ 1.
Then for every α ∈ KN
log|∆ iP (α )|ω ≤ hω(P ) + log +
⏐⏐⏐⏐
N∏
j=1
(
1 + deg Xj P
)⏐⏐⏐⏐
ω
+
N∑
j=1
(log+ |2|ω + log+|α(j)|ω)degXj P
Proof. See [ Cor97, Lemme, page 166].
We conclude the section with some rather straightforward re sults about heights. First of all when
we want to calculate the heights of elements lying in K×, we don’t need to involve the algebraic
closure K in the integrals:
Proposition 1.12. Let X = (K, Ω , φ) be an adelic curve. If a ∈ K×, then:
hX(a) =
∫
Ω K
log+ |a|ωdµ(ω) .
Moreover, the same result holds for the heights of polynomia ls in K[X1, . . . , XN ].
6
Proof. It is an immediate consequence of equation ( 9).
In order to simplify the notations, we often omit the subscri pt X attached to the heights when
the adelic curve is ﬁxed and there is no confusion.
Proposition 1.13. The height function of a proper adelic curve (X, Ω , φ) satisﬁes the following
properties for any a, b, a1, . . . , am ∈ K and any measurable set S ⊆ Ω
(1) h(a) = h(a−1)
(2) −h(a) ≤
∫
S log |a|ωdµ(ω) ≤ h(a)
(3)
∫
S log− |a|ωdµ(ω) ≥ −h(a)
(4) h(a1 + . . . + am) ≤ h(m) + h(a1) + . . . + h(am)
(5)
∫
S log |a − b|ωdµ(ω) ≥ − log 2 − h(a) − h(b)
(6)
∫
S log− |a − b|ωdµ(ω) ≥ − log 2 − h(a) − h(b)
Proof. (1) It follows from the product formula and from the fact that log |a|ω = log + |a|ω − log+ | 1
a |ω.
(2) By deﬁnition
∫
S log |a|ωdµ(ω) ≤ h(a), so for the other inequality it is enough to use (1).
(3) We use the equality log − |a|ω = − log+ |a−1|ω and we obtain:
∫
S
log− |a|ωdµ(ω) = −
∫
S
log+ |a−1|ωdµ(ω) ≥ −h(a−1) = −h(a)
(4) It follows from |a1 + . . . + am|ω ≤ m maxi |ai|ω.
(5) and (6) are direct consequences of (2)-(4) and the fact th at h(2) ≤ log(2).
Here we stress that the entries (5)-(6) of Proposition 1.13 replace the classical Liouville inequality
for heights. Finally we recall an important property of heig hts:
Deﬁnition 1.14. A proper adelic curve X = ( K, Ω , µ) satisﬁes the Northcott property if for any
C ∈ R the set {α ∈ K : hX(a)} ≤ C is ﬁnite.
Arithmetic function ﬁelds satisfy Northcott properties th anks to [ Mor00, Theorem 4.3].
