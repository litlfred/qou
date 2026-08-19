---
doc_id: afst-2007-6-16-3-665-0
doc_title: "ANNALES DE LA FACULTÉ DES SCIENCES Mathématiques"
section_id: sec-019-6-realizing-q-diﬀerence-modules-overk-as-connect
section_title: "Realizing q-diﬀerence modules overK as connections"
section_number: 6
pages: 39-47
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
on the elliptic curveE = C∗/qZ
As in section 2 we associate to any diﬀerence moduleM overK a vector
bundle v(M) on the elliptic curveEq. The aim is to providev(M) with
a suitable connection. The following theorem gives an explicit version of
Corollary 5.4.
Theorem 6.1 (Regular singularq-difference modules).—L et
a,b denote the generators ofπ
1(Eq), corresponding to the shiftsu ↦→u+
1,u ↦→u+τ on the universal covering Cu of Eq.L e ti :< Γrs,∆rs >→
π1(Eq) denote the isomorphism given byΓrs ↦→a, ∆rs ↦→b.
For every regular singular diﬀerence moduleM over K, corresponding
to a representationρ of < Γrs,∆rs >, there exists a unique ‘unit circle’
connection ∇M on v(M), corresponding to a representationρ′of π1(Eq),
such thatρ=i ◦ρ′.
This induces a Tannakian equivalence between the category of the regular
singular diﬀerence modules overK and a full subcategory of the category of
all ‘unit circle’ connections onEq.
Proof.— We recall that a connection∇ : M→ ΩEq ⊗M is calledunit
circle if the corresponding representationρ′ : π1(Eq) → GL(V) has the
property that every eigenvalue of everyρ′(α) has absolute value 1.
– 702 –
Galois theory ofq-diﬀerence equations
(1) We start by giving an explicit construction for rank one diﬀerence mod-
ules M over K. WriteM = Ke with Φe = ce and c ∈ C∗. A connection
∇M onv(M) is equivalent with a connection∇ :Oe →dz
z ⊗Oe commuting
with Φ (we recall thatO is the algebra of holomorphic functions onC∗).
One concludes that∇(e)= a(c)dz
z ⊗e, wherea : C∗ → C is a homomor-
phism. The diﬀerential equation∇e = a(c)dz
z ⊗e, considered onC, reads
∇e=2πia(c)du⊗ewhereuis the variable ofCandz =e2πiu. The basic so-
lution of this equation ise−2πia(c)ueandecan be interpreted asθc−1(e2πiu).
The shiftsu ↦→u+1 and u ↦→u+τ multiply this equation withe−2πia(c)
and e−2πia(c)τc. Writec = e2πi(a0+a1τ ) with a0 = a0(c),a 1 = a1(c) ∈ R.
The ‘unit circle’ condition implies thata(c)= a1(c) and the basic solution
is multiplied bye−2πia1 ande2πia0. Thus we found a unique unit circle con-
nection onv(Ke) and moreover the actions of Γrs,∆rs coincide with the
action of the fundamental groupπ1(Eq).
(2) The next case to consider isM = K ⊗W with Φ(f ⊗w)= φ(f) ⊗
A(w) andA ∈ GL(W) is unipotent. Deﬁne∇ : O ⊗W → Odz
z ⊗W by
∇(1 ⊗w)= 1
2πiτ
dz
z ⊗(1 ⊗log(A)(w)). Clearly ∇ commutes with Φ. One
can verify that this deﬁnition of∇ induces a regular connection onv(M).
The pullback of this connection toC has the fundamental matrixAu/τ.
The shiftsu ↦→u+1,u ↦→u+τ multiply this matrix withA1/τ andA,i n
accordance with the actions of Γrs and ∆rs.
Thegeneralcaseisobtainedfromthesetwospecialcasesbytakingtensor
products and direct sums.
(3) The map Hom(M,N ) → Hom((v(M), ∇M),(v(N), ∇N)) is a bijec-
tion since both groups translate into homomorphisms between represen-
tations. □
Remarks 6.2.— (1)Wenotethatnoteveryunitcircleconnectionon E is
isomorphic to some (v(M), ∇
M). E.g., the free vector bundleOEe1 ⊕OEe2,
providedwiththeunitcircleconnection ∇givenby ∇e1 =0, ∇e2 =dz
z ⊗e1,
is not isomorphic to some (v(M), ∇M).
(2) Our aim is to extend Theorem 6.1 to the category of all diﬀerence
modules overK. The ﬁrst step is to extend Theorem 6.1 to the category of
thesplitdiﬀerencemodules.Explicitly,onewantstoconstructforeverysplit
diﬀerence moduleM a connection ∇
M on v(M) such that∇M : v(M) →
Ω([1]) ⊗v(M) (i.e.,∇M has a regular singularity at 1∈Eq). Moreover, one
requires thatM ↦→ ∇M is functorial, commutes with direct sums and tensor
products, and extends the construction in Theorem 6.1 of∇M for regular
singular diﬀerence modules.
– 703 –
Marius van der Put, Marc Reversat
(3) The pure moduleM = Ke with Φe =( −z)e is the ﬁrst candidate for
a construction of ∇M : v(M) → Ω([1]) ⊗v(M). We note thatv(M)=
OEq([1])e. Any connection ∇ on this line bundle with at most a regular
singularityat1isgivenby ∇e=adz
z ⊗eforsomeconstant a.Theassumption
a= 0 is the natural choice for∇M.T h u s∇M is the unique extension of the
trivial connection onOEqe, given by∇e= 0 to a connection∇M :v(M) →
Ω([1]) ⊗v(M). One can describe this connection onOe by ∇e = −dΘ
Θ ⊗e.
This leads to a formula for∇M for the diﬀerence modulesM = Ke with
Φe=c(−z)te, namely
∇e=( −tdΘ
Θ +a1
dz
z ) ⊗e wherec=e2πi(a0+a1τ ) anda0,a 1 ∈ R.
One observes that for diﬀerence modules of rank one , the mapM ↦→
(v(M), ∇M) respects tensor products.
(4) Instead of continuing the method of (3), we will use subsubsection 1.4.1
to give a general construction of∇M for split diﬀerence modules overK.
Theorem 6.3.— There exists a functorN ↦→(v(N), ∇N) from the cat-
egory of the split diﬀerence modules overK to the category of the con-
nections on Eq with at most a regular singularity at1 ∈ Eq. This func-
tor extends the one deﬁned in Theorem 6.1. Moreover, the functorN ↦→
(v(N), ∇N) commutes with tensor products and is faithful.
Proof.— We use the notation and the results of subsubsection 1.4.1.
(1) Construction of ∇M for pure diﬀerence modulesM over K∞.
Consider a pure diﬀerence moduleM over K∞ with slopeλ. ThenM =
K∞ ⊗CV with Φ given by Φ(f ⊗v)= zλφ(f) ⊗A(v) whereA ∈GL(V) has
the property that every eigenvaluec ofA has the formc=e2πi(a0(c)+a1(c)τ )
with a0(c) ∈ R and a1(c) ∈ L ⊂ R. Leta1(Ass) ∈ End(V) be obtained
fromAss by replacing every eigenvaluec ofAss bya1(c). We introduce the
notation:On is the algebra of the convergent Laurent series in the variable
z1/n andO∞ = ⋃On. With these notation one deﬁnes the connection
∇M :O∞ ⊗CV → 1
ΘO∞
dz
z ⊗V by
∇M(v)= −λdΘ
Θ ⊗v+ dz
z ⊗(a1(Ass)+ 1
2πiτ log(Au)) (v).
The last formula is extended by∇M(f ⊗v)= df ⊗v +f ∇M(v) and by
additivity to a∇M deﬁned onO∞ ⊗C V. By construction,∇M commutes
with the action of Φ.
– 704 –
Galois theory ofq-diﬀerence equations
For two pure diﬀerence modulesMi = K∞ ⊗C Vi,i =1 ,2 overK∞
with Φ-actions given by the slopesλ1,λ 2 and Ai ∈ GL(Vi),i =1 ,2, the
pure moduleM3 = M1 ⊗K∞ M2 has the formK∞ ⊗C (V1 ⊗V2) with Φ-
action given by the slopeλ1 +λ2 and A3 :=A1 ⊗A2 ∈ GL(V1 ⊗V2). One
observes that the eigenvaluesc of A3 satisfy againa1(c) ∈L ⊂ R. Further
(A3)ss =(A1)ss ⊗(A2)ss anda1((A1)ss ⊗(A2)ss) is equal to (a1((A1)ss) ⊗
id)+( id ⊗a1((A2)ss)). There is a similar formula for1
2πiτ log(A3)u.
One concludes that∇M3 is the tensor product∇ = ∇M1 ⊗∇M2. The
latter is deﬁned by∇(m1 ⊗m2)=( ∇M1(m1) ⊗m2)+( m1 ⊗∇M2m2) (for
mi ∈O∞ ⊗Vi,i =1,2).
Amorphism f :M1 →M2 betweentwodiﬀerencemodules Mi =K∞ ⊗C
Vi,i =1 ,2 with the same slopeλ and Φ given byAi ∈ GL(Vi),i =1 ,2
is induced by aC-linear mapF : V1 → V2 satisfying F ◦A1 = A2 ◦F.
Thereforef induces a morphism between the two connections∇Mi.
(2) Construction of(v(N), ∇N) for a pure diﬀerence moduleN over K.
The connection ∇N :v(N) → ΩEq([1]) ⊗v(N), that we want to construct,
translates into a connection with the same name
∇N :O ⊗C[z,z−1] Nglobal → 1
ΘOdz
z ⊗C[z,z−1] Nglobal ,
which commutes with the action of Φ.
PutM =K∞ ⊗KN.Thisdiﬀerencemoduleisequippedwiththedataof
N,i.e., data(N)=( λ,V,A, {D(σ)}).Wenotethat O∞ ⊗CV =O∞ ⊗C[z,z−1]
Nglobal and that (O∞ ⊗C V)Gal is equal toO ⊗C[z,z−1] Nglobal. The ∇M,
constructed above, descends to a∇N for N if and only if∇M commutes
with the {D(σ)}.
The formulaD(σ)−1AD(σ)= e2πiλσA implies thatD(σ)−1AuD(σ)=
Au and D(σ)−1AssD(σ)= e2πiλσAss. The eigenspace ofAss for the eigen-
valuecismappedby D(σ)totheeigenspacefortheeigenvalue ce2πiλσ.From
a1(ce2πiλσ)= a1(c) it follows thatD(σ) leaves every eigenspace invariant of
a1(Ass) for the eigenvalues of this map. ThusD(σ) commutes witha1(Ass)
and withAu, too. This implies that∇M commutes the{D(σ)}.
(3) (v(N), ∇N) for a split diﬀerence moduleN over K.
ForN =N1 ⊕···⊕ Nr with allNi pure of slopesλ1 < ··· <λr one deﬁnes
(v(N), ∇N): =⊕r
i=1(v(Ni), ∇Ni).
A morphism between split modules overK is the sum of morphisms
between pure modules with the same slope. The latter induces a mor-
phism between the corresponding connections, according to (1). ThusN ↦→
– 705 –
Marius van der Put, Marc Reversat
(v(N), ∇N) is a functor. According to (1) and 1.4.1, this functor preserves
tensor products.
For proving ‘faithful’ it suﬃces to show that, for a pure moduleN, the
map ker(Φ−1,N) →{ξ ∈H0(Eq,v(N))|∇Nξ =0 }is injective. If the slope
ofN is not 0, then the left hand side is 0. If the slope is 0, then by Theorem
6.1, the above map is bijective. □
Remark.— The following example shows that the functor of Theorem
6.3 is not fully faithful. PutN = Ke with Φ(e)=( −z)te and t> 0.
Then v(N)= OEq(t · [1]) and ∇N is induced byd : OEq → ΩEq, using
the inclusionOEq ⊂ OEq(t ·[1]). In this case, ker(Φ−1,N) = 0 and{ξ ∈
H0(Eq,v(N))|∇Nξ =0 } has dimension 1.
We want to extend the functor of Theorem 6.3 to the category of all
diﬀerence modules overK. We start with an example.
Example 6.4.— N =Ke1 +Ke2 with Φe1 =( −z)te1, Φe2 =e2 +pe1,
t ∈ Z,t> 0 and p ∈K.
We may supposep ∈ C[z,z −1]. The aim is to produce a connection
∇ :Oe1 +Oe2 → 1
ΘtOdz
z ⊗O (Oe1 +Oe2),
such that∇ commutes with Φ and∇ induces for the pure moduleKe1 and
Ke2 the connections of Theorem 6.3.
Considertheinclusion Oe1+Oe2 ⊂Of1+Of2 withf1 =Θ −te1,f 2 =e2.
ThenΦf1 =f1 andΦf2 =f2+pΘtf1.Wepropose ∇f1 = 0and ∇f2 =ω⊗f1
withω ∈Odz
z .TheconditionΦ ∇ = ∇Φisequivalentto( φ−1)(ω)= d(pΘt).
The equation is solved as follows. There existsf ∈O with (φ −1)(f)=
pΘt −c where c is the constant term ofpΘt. Thisf is unique up to its
constantterm.Now ω :=d(f)satisﬁes( φ−1)(df)= d((φ−1)(f)) =d(pΘt).
Thus ∇e1 = tdΘ
Θ ⊗e1 and ∇e2 =Θ −tω ⊗e1. Since ∇ commutes with
Φ this induces a connection∇ : v(N) → ΩEq(t[1]) ⊗v(N) with a pole at
1 ∈Eq of order at mostt. Moreover∇ induces onv(Ke1) andv(Ke2) the
connections of Theorem 6.3.
In the next example we give a construction of∇N for diﬀerence modules
N overK with two integer slopes.
– 706 –
Galois theory ofq-diﬀerence equations
Example 6.5.— N = P1 ⊕P2 with P1,P 2 global modules with slopes
t1 <t 2,t =t2 −t1 ∈ Z and Φ given byΦ(p1 +p2)=Φ 1p1 +𝓁(Φ2p2)+Φ 2p2
for some C[z,z −1]-linear map𝓁:P2 →P1.
Put Q1 = C[z,z −1]e ⊗P1 with Φ(e)=( −z)te and t =t2 −t1 and put
Q2 =P2. ThenO ⊗P1 is embedded intoO ⊗Q1 byp ↦→Θte ⊗p.N o wΦ
onO ⊗Q1 +O ⊗Q2 is given by
Φ(e ⊗p1 +p2)=( −z)te ⊗Φ1(p1)+Θte ⊗𝓁(Φ2p2)+Φ 2(p2).
∇ onO ⊗Q1 +O ⊗Q2 will be given by a formula of the type:∇(e ⊗p1)=
−tdΘ
Θ e ⊗p1 +e ⊗∇ 1p1, where ∇i are the connections forPi imposed by
Theorem 6.3. Further∇p2 = ∇2p2 +m(p2) wherem:O ⊗P2 →Odz
z ⊗Q1
is a yet unknownO-linear map. Thusm is an element ofOdz
z ⊗O T with
T =O ⊗C[z,z−1] (P ∗
2 ⊗Q1). We note thatP ∗
2 ⊗Q1 is a pure global module
of slope 0.
Write ˜𝓁:O ⊗P2
𝓁
→O ⊗P1 ⊂O ⊗Q1.T h u s˜l is an element ofT. The
condition Φ∇ = ∇Φ is equivalent to ΦT(m) −m = ∇T(˜𝓁), where ΦT and
∇T denote the Φ-action and the connection forT.
According to Lemma 6.6, there is a canonical solutionm for this equa-
tion. The corresponding∇ induces a connection∇N :v(N) → ΩEq(t[1]) ⊗
v(N) with a pole at 1∈ Eq of order at mostt. Further ∇N induces the
connections onv(P1) andv(P2) prescribed by Theorem 6.3.
The action of Φ onO ⊗Q1 +O ⊗Q2 can be changed into an equivalent
one by adding to˜𝓁an expression (Φ−1)(ξ) withξ ∈T. This is compatible
with the construction of∇N, according to part (1) of Lemma 6.6. After
such a change, one may suppose that˜𝓁maps Q2 intoQ1. In this situation
the connection onQ1 ⊕Q2 is the one prescribed by Theorem 6.3, according
to part (2) of Lemma 6.6
Lemma 6.6.— (1) Let P be a pure global module of slope 0. There is
a canonical C-linear mapf ∈ O ⊗P → ω(f) ∈ Odz
z ⊗P satisfying (Φ −
1)ω(f)= ∇f. Furtherω(Φ(f)) = Φ(ω(f)).
(2) Let (Q1,Φ1),(Q2,Φ2) denote two pure global modules of the same slope
and let 𝓁: Q2 → Q1 be a C[z,z −1]-linear map. Deﬁne the pure module
N =Q1 ⊕Q2 by Φ(q1 +q2)=Φ 1(q1)+Φ 2(q2)+ 𝓁(Φ2(q2)).
The connection onO ⊗N, deﬁned by Theorem 6.3 coincides with the
connection ∇ given by the formula∇(q1+q2)= ∇1(q1)+ ∇2(q2)+ω(𝓁)(q2).
Proof.— WriteP = C[z,z −1] ⊗C W with Φ deﬁned by Φ(w)= A(w)
and ∇(w)= dz
z ⊗(a1(Ass)+ 1
2πiτ log(Au))(w). For convenience we suppose
– 707 –
Marius van der Put, Marc Reversat
that the eigenvaluesc of A satisfy |q| < |c| ⩽ 1. Writef = ∑
n∈Zzn ⊗fn
andω(f)= ∑
n∈Zzndz
z ⊗ωn with allfn,ωn ∈W.
Thenf =
∑
n
zndz
z ⊗{(n+a1(Ass)+ 1
2πiτ logAu)(fn)}
and (Φ−1)ω(f)=
∑
n
zndz
z ⊗(qnA −1)(ωn).
This produces the equations (qnA −1)ωn =(n+a1(Ass)+ 1
2πiτ logAu)fn.
For n ⁄= 0, the mapqnA − 1 is invertible and there is a unique solution
ωn. For the equation (A −1)ω0 =(a1(Ass)+ 1
2πiτ logAu)f0 we writeW as
a direct sum⊕Wc, whereWc is the generalized eigenspace forA and the
eigenvaluec.F o rc ⁄= 1, the restriction of the equation toWc has a unique
solution sinceA − 1 is invertible onWc. On the spaceW1, the equation
reads (A −1)ω1
0 =( 1
2πiτ logAu)f 1
0, whereω1
0,f 1
0 denote the components in
W1 ofω0 andf0.O nW1 we haveA =Au. The canonical solution, that we
propose, is given byω1
0 = ∑ ∞
j=0(−1)j (Au−1)j
2πiτ (j+1)(f 1
0).
It is clear thatf ↦→ω(f)i s C-linear. The formula Φ(ω(f)) =ω(Φf)
followsfromtheexplicitdeﬁnitionof ω(f).Theexpression‘canonical’means
the following. Letα : P1 → P2 be a morphism between global modules of
slope 0 and letf ∈O ⊗P1. Thenα applied toω(f) is equal toω(α(f)).
A straightforward calculation shows (2). □
Theorem 6.7.— There exists aC-linear functorN ↦→(v(N), ∇N) from
the category of the diﬀerence modulesN over K with integer slopes to the
category of the connections onEq with at most a pole at the point1 ∈Eq.
This functor extends the one of Theorem 6.3, is faithful and commutes with
tensor products.
Proof.— Consider pure global modulesP
j,j =1 ,...,r with integer
slopes λ1 < ··· <λr. Let Φj denote the action of Φ onPj. Let C[z,z −1]-
linear maps𝓁i,j : Pj → Pi for i<j , be given. Deﬁne the global module
N with ascending slope ﬁltration byN = P1 ⊕···⊕ Pr and Φ(p1 + ··· +
pr)= ∑r
j=1(Φj(pj)+ ∑
i<j 𝓁i,jΦj(pj)). We want to construct a canonical
connection onO ⊗N commuting with Φ.
Deﬁne Qj := C[z,z −1]ej ⊗Pj with Φej =( −z)λr −λjej for j =1,...,r .
Let Φ∗
j be the action of Φ onQj. One embedsO ⊗Pj into O ⊗Qj by
pj ↦→Θλr −λjej ⊗pj. ThenO ⊗N = ⊕O ⊗Pj embeds intoO ⊗Q with
– 708 –
Galois theory ofq-diﬀerence equations
Q = ⊕r
j=1Qj. Let ˜𝓁i,j : O ⊗Qj → O ⊗Qi be the map derived from𝓁i,j.
Then Φ onO ⊗Q is given by
Φ(q1 + ··· +qr)=
r∑
j=1
(Φ∗
j(qj)+
∑
i<j
˜𝓁i,jΦ∗
j(qj)).
With this formula the embedding is Φ-equivariant. OnO ⊗Q one wants to
deﬁne a connection∇ of the form
∇(q1 + ··· +qr)=
r∑
j=1
∇j(qj)+
r∑
j=1
∑
i<j
mi,j(qj),
with O-linear maps mi,j : O ⊗Qj → Odz
z ⊗O (O ⊗Qi). The condition
Φ∇ = ∇Φtranslatesinto(Φ −1)mi,j = ∇(˜𝓁i,j)forall i<j .Theseequations
are solved in the canonical way of Lemma 6.6. The restriction of this∇ to
O ⊗N induce a connection∇N :v(N) →ΩEq((λr −λ1)[1]) ⊗v(N).
Themaps 𝓁i,j inthedeﬁnitionof N arenotunique.Theycanbechanged
by adding maps (Φ−1)ri,j with ri,j : Pj → Pi. It is easily seen that∇N
only depends on the equivalence classes of the𝓁i,j. Using Lemma 6.6, one
shows that the above deﬁnes aC-linear functor.
Let N1,N 2 denote two global diﬀerence modules with ascending slope
ﬁltration and with integer slopes. The above constuction embedsO ⊗Ni
intoO ⊗Mi (fori=1,2) whereO ⊗Mi has only one slope. The connections
on N1,N 2 are the restrictions of the connections onO ⊗Mi prescribed by
Theorem 6.3. The above construction applied toN3 = N1 ⊗N2 embeds
O ⊗N3 into the tensor product of the pure modulesO ⊗Mi. According to
Theorem 6.3, the connection on this tensor product is the tensor product of
the connections on theO ⊗M
i. We conclude that the functor, construction
above, respects tensor products. □
Remarks 6.8.— (1) For general diﬀerence modulesM overK it is also
possible to deﬁne a connection∇N onv(N) with at most a pole at 1∈Eq.
However for non integer slopes there seems not be a canonical choice for
∇
N.
(2) In the situation of Example 6.5, the map𝓁:P2 →P1 is responsible for
divergence, ‘Stokes matrices’ and the unipotent part of the diﬀerence Galois
group ofN. In general, the connection∇
N :v(N) →ΩEq(t[1]) ⊗v(N) has a
pole of ordert. The irregularity of the connection∇N locally at 1∈Eq will
produce Stokes matrices (in the classical sense) and unipotent elements of
the local analytic diﬀerential Galois group which depend on𝓁. The precise
relation remains to be investigated.
– 709 –
Marius van der Put, Marc Reversat
(3) It is interesting to apply another method to Example 6.4. For any in-
teger t> 0 one deﬁnesGt = ∑
n∈Z(qt)n(n−1)/2(−zt)n. One observes that
(−zt)Gt(qz)= Gt(z) and that the set of the zeros ofGt is µt ×qZ, where
µt is the group of thet-th roots of unity.
Let againN = Ke1 +Ke2 with Φ(e1)=( −z)te1, Φ(e2)= e2 +pe1
with p ∈ C[z,z −1]. Deﬁne nowf1 = G−1
t e1 and f2 = e2. ThenOe1 +Oe2
embeds intoOf1 +Of2 and Φ(f1)=( −1)t−1f1 and Φ(f2)= f2 +pGtf1.
The connection ∇ is deﬁned by ∇f1 =0 , ∇f2 = ω ⊗f2 where ω is the
canonical solution of (Φ−1)ω =( −1)t−1d(pGt). The resulting connection
∇N has at most simple poles at the image points ofµt inEq.
(4)Thevariationin(3)onExample6.4extendstoafunctoronthecategory
of the diﬀerence modules overK with integer slopes to the category of the
connections onEq having at most simple poles in the images of⋃
t/greaterorequalslant1µt in
Eq. This functor is constructed as in the proof of Theorem 6.7 and it has
againtheproperties: C-linear,faithfulandcommutingwithtensorproducts.
For this variation on Theorem 6.7 and in connection with Example 6.5,
one observes that𝓁:P2 →P1 contributes to the poles of∇N on the image
points of µt in Eq.T h u s𝓁contributes to the monodromy group for the
connection ∇N.
