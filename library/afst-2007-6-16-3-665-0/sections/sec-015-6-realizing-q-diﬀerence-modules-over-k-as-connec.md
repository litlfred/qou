---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-015-6-realizing-q-diﬀerence-modules-over-k-as-connec
section_title: "Realizing q-diﬀerence modules over K as connections on the elliptic curve E = C∗/qZ"
section_number: 6
pages: 39-47
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
on the elliptic curve E = C∗/qZ
As in section 2 we associate to any diﬀerence module M over K a vector
bundle v(M) on the elliptic curve Eq. The aim is to provide v(M) with
a suitable connection. The following theorem gives an explicit version of
Corollary 5.4.
Theorem 6.1 (Regular singular q-difference modules). — Let
a, b denote the generators of π1(Eq), corresponding to the shifts u →u +
1, u →u + τ on the universal covering Cu of Eq. Let i :< Γrs, ∆rs >→
π1(Eq) denote the isomorphism given by Γrs →a, ∆rs →b.
For every regular singular diﬀerence module M over K, corresponding
to a representation ρ of < Γrs, ∆rs >, there exists a unique ‘unit circle’
connection ∇M on v(M), corresponding to a representation ρ′ of π1(Eq),
such that ρ = i ◦ρ′.
This induces a Tannakian equivalence between the category of the regular
singular diﬀerence modules over K and a full subcategory of the category of
all ‘unit circle’ connections on Eq.
Proof. — We recall that a connection ∇: M →ΩEq ⊗M is called unit
circle if the corresponding representation ρ′ : π1(Eq) →GL(V ) has the
property that every eigenvalue of every ρ′(α) has absolute value 1.
– 702 –
Galois theory of q-diﬀerence equations
(1) We start by giving an explicit construction for rank one diﬀerence mod-
ules M over K. Write M = Ke with Φe = ce and c ∈C∗. A connection
∇M on v(M) is equivalent with a connection ∇: Oe →dz
z ⊗Oe commuting
with Φ (we recall that O is the algebra of holomorphic functions on C∗).
One concludes that ∇(e) = a(c) dz
z ⊗e, where a : C∗→C is a homomor-
phism. The diﬀerential equation ∇e = a(c) dz
z ⊗e, considered on C, reads
∇e = 2πia(c)du⊗e where u is the variable of C and z = e2πiu. The basic so-
lution of this equation is e−2πia(c)ue and e can be interpreted as θc−1(e2πiu).
The shifts u →u + 1 and u →u + τ multiply this equation with e−2πia(c)
and e−2πia(c)τc. Write c = e2πi(a0+a1τ) with a0 = a0(c), a1 = a1(c) ∈R.
The ‘unit circle’ condition implies that a(c) = a1(c) and the basic solution
is multiplied by e−2πia1 and e2πia0. Thus we found a unique unit circle con-
nection on v(Ke) and moreover the actions of Γrs, ∆rs coincide with the
action of the fundamental group π1(Eq).
(2) The next case to consider is M = K ⊗W with Φ(f ⊗w) = φ(f) ⊗
A(w) and A ∈GL(W) is unipotent. Deﬁne ∇: O ⊗W →O dz
z ⊗W by
∇(1 ⊗w) =
1
2πiτ
dz
z ⊗(1 ⊗log(A)(w)). Clearly ∇commutes with Φ. One
can verify that this deﬁnition of ∇induces a regular connection on v(M).
The pullback of this connection to C has the fundamental matrix Au/τ.
The shifts u →u + 1, u →u + τ multiply this matrix with A1/τ and A, in
accordance with the actions of Γrs and ∆rs.
The general case is obtained from these two special cases by taking tensor
products and direct sums.
(3) The map Hom(M, N) →Hom((v(M), ∇M), (v(N), ∇N)) is a bijec-
tion since both groups translate into homomorphisms between represen-
tations.
□
Remarks 6.2. — (1) We note that not every unit circle connection on E is
isomorphic to some (v(M), ∇M). E.g., the free vector bundle OEe1 ⊕OEe2,
provided with the unit circle connection ∇given by ∇e1 = 0, ∇e2 = dz
z ⊗e1,
is not isomorphic to some (v(M), ∇M).
(2) Our aim is to extend Theorem 6.1 to the category of all diﬀerence
modules over K. The ﬁrst step is to extend Theorem 6.1 to the category of
the split diﬀerence modules. Explicitly, one wants to construct for every split
diﬀerence module M a connection ∇M on v(M) such that ∇M : v(M) →
Ω([1]) ⊗v(M) (i.e., ∇M has a regular singularity at 1 ∈Eq). Moreover, one
requires that M →∇M is functorial, commutes with direct sums and tensor
products, and extends the construction in Theorem 6.1 of ∇M for regular
singular diﬀerence modules.
– 703 –
Marius van der Put, Marc Reversat
(3) The pure module M = Ke with Φe = (−z)e is the ﬁrst candidate for
a construction of ∇M : v(M) →Ω([1]) ⊗v(M). We note that v(M) =
OEq([1])e. Any connection ∇on this line bundle with at most a regular
singularity at 1 is given by ∇e = a dz
z ⊗e for some constant a. The assumption
a = 0 is the natural choice for ∇M. Thus ∇M is the unique extension of the
trivial connection on OEqe, given by ∇e = 0 to a connection ∇M : v(M) →
Ω([1]) ⊗v(M). One can describe this connection on Oe by ∇e = −dΘ
Θ ⊗e.
This leads to a formula for ∇M for the diﬀerence modules M = Ke with
Φe = c(−z)te, namely
∇e = (−tdΘ
Θ + a1
dz
z ) ⊗e where c = e2πi(a0+a1τ) and a0, a1 ∈R .
One observes that for diﬀerence modules of rank one , the map M →
(v(M), ∇M) respects tensor products.
(4) Instead of continuing the method of (3), we will use subsubsection 1.4.1
to give a general construction of ∇M for split diﬀerence modules over K.
Theorem 6.3. — There exists a functor N →(v(N), ∇N) from the cat-
egory of the split diﬀerence modules over K to the category of the con-
nections on Eq with at most a regular singularity at 1 ∈Eq. This func-
tor extends the one deﬁned in Theorem 6.1. Moreover, the functor N →
(v(N), ∇N) commutes with tensor products and is faithful.
Proof. — We use the notation and the results of subsubsection 1.4.1.
(1) Construction of ∇M for pure diﬀerence modules M over K∞.
Consider a pure diﬀerence module M over K∞with slope λ. Then M =
K∞⊗C V with Φ given by Φ(f ⊗v) = zλφ(f) ⊗A(v) where A ∈GL(V ) has
the property that every eigenvalue c of A has the form c = e2πi(a0(c)+a1(c)τ)
with a0(c) ∈R and a1(c) ∈L ⊂R. Let a1(Ass) ∈End(V ) be obtained
from Ass by replacing every eigenvalue c of Ass by a1(c). We introduce the
notation: On is the algebra of the convergent Laurent series in the variable
z1/n and O∞=  On. With these notation one deﬁnes the connection
∇M : O∞⊗C V →1
ΘO∞
dz
z ⊗V by
∇M(v) = −λdΘ
Θ ⊗v + dz
z ⊗( a1(Ass) +
1
2πiτ log(Au) )(v) .
The last formula is extended by ∇M(f ⊗v) = df ⊗v + f∇M(v) and by
additivity to a ∇M deﬁned on O∞⊗C V . By construction, ∇M commutes
with the action of Φ.
– 704 –
Galois theory of q-diﬀerence equations
For two pure diﬀerence modules Mi = K∞⊗C Vi, i = 1, 2 over K∞
with Φ-actions given by the slopes λ1, λ2 and Ai ∈GL(Vi), i = 1, 2, the
pure module M3 = M1 ⊗K∞M2 has the form K∞⊗C (V1 ⊗V2) with Φ-
action given by the slope λ1 + λ2 and A3 := A1 ⊗A2 ∈GL(V1 ⊗V2). One
observes that the eigenvalues c of A3 satisfy again a1(c) ∈L ⊂R. Further
(A3)ss = (A1)ss ⊗(A2)ss and a1((A1)ss ⊗(A2)ss) is equal to (a1((A1)ss) ⊗
id) + (id ⊗a1((A2)ss)). There is a similar formula for
1
2πiτ log(A3)u.
One concludes that ∇M3 is the tensor product ∇= ∇M1 ⊗∇M2. The
latter is deﬁned by ∇(m1 ⊗m2) = (∇M1(m1) ⊗m2) + (m1 ⊗∇M2m2) (for
mi ∈O∞⊗Vi, i = 1, 2).
A morphism f : M1 →M2 between two diﬀerence modules Mi = K∞⊗C
Vi, i = 1, 2 with the same slope λ and Φ given by Ai ∈GL(Vi), i = 1, 2
is induced by a C-linear map F : V1 →V2 satisfying F ◦A1 = A2 ◦F.
Therefore f induces a morphism between the two connections ∇Mi.
(2) Construction of (v(N), ∇N) for a pure diﬀerence module N over K.
The connection ∇N : v(N) →ΩEq([1]) ⊗v(N), that we want to construct,
translates into a connection with the same name
∇N : O ⊗C[z,z−1] Nglobal →1
ΘOdz
z ⊗C[z,z−1] Nglobal ,
which commutes with the action of Φ.
Put M = K∞⊗K N. This diﬀerence module is equipped with the data of
N, i.e., data(N) = (λ, V, A, {D(σ)}). We note that O∞⊗CV = O∞⊗C[z,z−1]
Nglobal and that (O∞⊗C V )Gal is equal to O ⊗C[z,z−1] Nglobal. The ∇M,
constructed above, descends to a ∇N for N if and only if ∇M commutes
with the {D(σ)}.
The formula D(σ)−1AD(σ) = e2πiλσA implies that D(σ)−1AuD(σ) =
Au and D(σ)−1AssD(σ) = e2πiλσAss. The eigenspace of Ass for the eigen-
value c is mapped by D(σ) to the eigenspace for the eigenvalue ce2πiλσ. From
a1(ce2πiλσ) = a1(c) it follows that D(σ) leaves every eigenspace invariant of
a1(Ass) for the eigenvalues of this map. Thus D(σ) commutes with a1(Ass)
and with Au, too. This implies that ∇M commutes the {D(σ)}.
(3) (v(N), ∇N) for a split diﬀerence module N over K.
For N = N1 ⊕· · · ⊕Nr with all Ni pure of slopes λ1 < · · · < λr one deﬁnes
(v(N), ∇N) := ⊕r
i=1(v(Ni), ∇Ni).
A morphism between split modules over K is the sum of morphisms
between pure modules with the same slope. The latter induces a mor-
phism between the corresponding connections, according to (1). Thus N →
– 705 –
Marius van der Put, Marc Reversat
(v(N), ∇N) is a functor. According to (1) and 1.4.1, this functor preserves
tensor products.
For proving ‘faithful’ it suﬃces to show that, for a pure module N, the
map ker(Φ−1, N) →{ξ ∈H0(Eq, v(N))| ∇Nξ = 0} is injective. If the slope
of N is not 0, then the left hand side is 0. If the slope is 0, then by Theorem
6.1, the above map is bijective.
□
Remark. — The following example shows that the functor of Theorem
6.3 is not fully faithful. Put N = Ke with Φ(e) = (−z)te and t > 0.
Then v(N) = OEq(t · [1]) and ∇N is induced by d : OEq →ΩEq, using
the inclusion OEq ⊂OEq(t · [1]). In this case, ker(Φ −1, N) = 0 and {ξ ∈
H0(Eq, v(N))| ∇Nξ = 0} has dimension 1.
We want to extend the functor of Theorem 6.3 to the category of all
diﬀerence modules over K. We start with an example.
Example 6.4. — N = Ke1 + Ke2 with Φe1 = (−z)te1, Φe2 = e2 + pe1,
t ∈Z, t > 0 and p ∈K.
We may suppose p ∈C[z, z−1]. The aim is to produce a connection
∇: Oe1 + Oe2 →1
Θt Odz
z ⊗O (Oe1 + Oe2) ,
such that ∇commutes with Φ and ∇induces for the pure module Ke1 and
Ke2 the connections of Theorem 6.3.
Consider the inclusion Oe1+Oe2 ⊂Of1+Of2 with f1 = Θ−te1, f2 = e2.
Then Φf1 = f1 and Φf2 = f2+pΘtf1. We propose ∇f1 = 0 and ∇f2 = ω⊗f1
with ω ∈O dz
z . The condition Φ∇= ∇Φ is equivalent to (φ−1)(ω) = d(pΘt).
The equation is solved as follows. There exists f ∈O with (φ −1)(f) =
pΘt −c where c is the constant term of pΘt. This f is unique up to its
constant term. Now ω := d(f) satisﬁes (φ−1)(df) = d((φ−1)(f)) = d(pΘt).
Thus ∇e1 = t dΘ
Θ ⊗e1 and ∇e2 = Θ−tω ⊗e1. Since ∇commutes with
Φ this induces a connection ∇: v(N) →ΩEq(t[1]) ⊗v(N) with a pole at
1 ∈Eq of order at most t. Moreover ∇induces on v(Ke1) and v(Ke2) the
connections of Theorem 6.3.
In the next example we give a construction of ∇N for diﬀerence modules
N over K with two integer slopes.
– 706 –
Galois theory of q-diﬀerence equations
Example 6.5. — N = P1 ⊕P2 with P1, P2 global modules with slopes
t1 < t2, t = t2 −t1 ∈Z and Φ given by Φ(p1 + p2) = Φ1p1 + ℓ(Φ2p2) + Φ2p2
for some C[z, z−1]-linear map ℓ: P2 →P1.
Put Q1 = C[z, z−1]e ⊗P1 with Φ(e) = (−z)te and t = t2 −t1 and put
Q2 = P2. Then O ⊗P1 is embedded into O ⊗Q1 by p →Θte ⊗p. Now Φ
on O ⊗Q1 + O ⊗Q2 is given by
Φ(e ⊗p1 + p2) = (−z)te ⊗Φ1(p1) + Θte ⊗ℓ(Φ2p2) + Φ2(p2) .
∇on O ⊗Q1 + O ⊗Q2 will be given by a formula of the type: ∇(e ⊗p1) =
−t dΘ
Θ e ⊗p1 + e ⊗∇1p1, where ∇i are the connections for Pi imposed by
Theorem 6.3. Further ∇p2 = ∇2p2 + m(p2) where m : O ⊗P2 →O dz
z ⊗Q1
is a yet unknown O-linear map. Thus m is an element of O dz
z ⊗O T with
T = O ⊗C[z,z−1] (P ∗
2 ⊗Q1). We note that P ∗
2 ⊗Q1 is a pure global module
of slope 0.
Write ˜ℓ: O ⊗P2
ℓ→O ⊗P1 ⊂O ⊗Q1. Thus ˜l is an element of T. The
condition Φ∇= ∇Φ is equivalent to ΦT (m) −m = ∇T (˜ℓ), where ΦT and
∇T denote the Φ-action and the connection for T.
According to Lemma 6.6, there is a canonical solution m for this equa-
tion. The corresponding ∇induces a connection ∇N : v(N) →ΩEq(t[1]) ⊗
v(N) with a pole at 1 ∈Eq of order at most t. Further ∇N induces the
connections on v(P1) and v(P2) prescribed by Theorem 6.3.
The action of Φ on O ⊗Q1 + O ⊗Q2 can be changed into an equivalent
one by adding to ˜ℓan expression (Φ −1)(ξ) with ξ ∈T. This is compatible
with the construction of ∇N, according to part (1) of Lemma 6.6. After
such a change, one may suppose that ˜ℓmaps Q2 into Q1. In this situation
the connection on Q1 ⊕Q2 is the one prescribed by Theorem 6.3, according
to part (2) of Lemma 6.6
Lemma 6.6. — (1) Let P be a pure global module of slope 0. There is
a canonical C-linear map f ∈O ⊗P →ω(f) ∈O dz
z ⊗P satisfying (Φ −
1)ω(f) = ∇f. Further ω(Φ(f)) = Φ(ω(f)).
(2) Let (Q1, Φ1), (Q2, Φ2) denote two pure global modules of the same slope
and let ℓ: Q2 →Q1 be a C[z, z−1]-linear map. Deﬁne the pure module
N = Q1 ⊕Q2 by Φ(q1 + q2) = Φ1(q1) + Φ2(q2) + ℓ(Φ2(q2)).
The connection on O ⊗N, deﬁned by Theorem 6.3 coincides with the
connection ∇given by the formula ∇(q1 +q2) = ∇1(q1)+∇2(q2)+ω(ℓ)(q2).
Proof. — Write P = C[z, z−1] ⊗C W with Φ deﬁned by Φ(w) = A(w)
and ∇(w) = dz
z ⊗(a1(Ass) +
1
2πiτ log(Au))(w). For convenience we suppose
– 707 –
Marius van der Put, Marc Reversat
that the eigenvalues c of A satisfy |q| < |c| ⩽1. Write f = 
n∈Z zn ⊗fn
and ω(f) = 
n∈Z zn dz
z ⊗ωn with all fn, ωn ∈W.
Then f =

n
zn dz
z ⊗{(n + a1(Ass) +
1
2πiτ log Au)(fn)}
and (Φ −1)ω(f) =

n
zn dz
z ⊗(qnA −1)(ωn) .
This produces the equations (qnA −1)ωn = (n + a1(Ass) +
1
2πiτ log Au)fn.
For n̸ = 0, the map qnA −1 is invertible and there is a unique solution
ωn. For the equation (A −1)ω0 = (a1(Ass) +
1
2πiτ log Au)f0 we write W as
a direct sum ⊕Wc, where Wc is the generalized eigenspace for A and the
eigenvalue c. For c̸ = 1, the restriction of the equation to Wc has a unique
solution since A −1 is invertible on Wc. On the space W1, the equation
reads (A −1)ω1
0 = (
1
2πiτ log Au)f 1
0 , where ω1
0, f 1
0 denote the components in
W1 of ω0 and f0. On W1 we have A = Au. The canonical solution, that we
propose, is given by ω1
0 = ∞
j=0(−1)j (Au−1)j
2πiτ(j+1)(f 1
0 ).
It is clear that f →ω(f) is C-linear. The formula Φ(ω(f)) = ω(Φf)
follows from the explicit deﬁnition of ω(f). The expression ‘canonical’ means
the following. Let α : P1 →P2 be a morphism between global modules of
slope 0 and let f ∈O ⊗P1. Then α applied to ω(f) is equal to ω(α(f)).
A straightforward calculation shows (2).
□
Theorem 6.7. — There exists a C-linear functor N →(v(N), ∇N) from
the category of the diﬀerence modules N over K with integer slopes to the
category of the connections on Eq with at most a pole at the point 1 ∈Eq.
This functor extends the one of Theorem 6.3, is faithful and commutes with
tensor products.
Proof. — Consider pure global modules Pj, j = 1, . . . , r with integer
slopes λ1 < · · · < λr. Let Φj denote the action of Φ on Pj. Let C[z, z−1]-
linear maps ℓi,j : Pj →Pi for i < j, be given. Deﬁne the global module
N with ascending slope ﬁltration by N = P1 ⊕· · · ⊕Pr and Φ(p1 + · · · +
pr) = r
j=1(Φj(pj) + 
i<j ℓi,jΦj(pj)). We want to construct a canonical
connection on O ⊗N commuting with Φ.
Deﬁne Qj := C[z, z−1]ej ⊗Pj with Φej = (−z)λr−λjej for j = 1, . . . , r.
Let Φ∗
j be the action of Φ on Qj. One embeds O ⊗Pj into O ⊗Qj by
pj →Θλr−λjej ⊗pj. Then O ⊗N = ⊕O ⊗Pj embeds into O ⊗Q with
– 708 –
Galois theory of q-diﬀerence equations
Q = ⊕r
j=1Qj. Let ˜ℓi,j : O ⊗Qj →O ⊗Qi be the map derived from ℓi,j.
Then Φ on O ⊗Q is given by
Φ(q1 + · · · + qr) =
r

j=1
(Φ∗
j(qj) +

i<j
˜ℓi,jΦ∗
j(qj)) .
With this formula the embedding is Φ-equivariant. On O ⊗Q one wants to
deﬁne a connection ∇of the form
∇(q1 + · · · + qr) =
r

j=1
∇j(qj) +
r

j=1

i<j
mi,j(qj) ,
with O-linear maps mi,j : O ⊗Qj →O dz
z ⊗O (O ⊗Qi). The condition
Φ∇= ∇Φ translates into (Φ−1)mi,j = ∇(˜ℓi,j) for all i < j. These equations
are solved in the canonical way of Lemma 6.6. The restriction of this ∇to
O ⊗N induce a connection ∇N : v(N) →ΩEq((λr −λ1)[1]) ⊗v(N).
The maps ℓi,j in the deﬁnition of N are not unique. They can be changed
by adding maps (Φ −1)ri,j with ri,j : Pj →Pi. It is easily seen that ∇N
only depends on the equivalence classes of the ℓi,j. Using Lemma 6.6, one
shows that the above deﬁnes a C-linear functor.
Let N1, N2 denote two global diﬀerence modules with ascending slope
ﬁltration and with integer slopes. The above constuction embeds O ⊗Ni
into O⊗Mi (for i = 1, 2) where O⊗Mi has only one slope. The connections
on N1, N2 are the restrictions of the connections on O ⊗Mi prescribed by
Theorem 6.3. The above construction applied to N3 = N1 ⊗N2 embeds
O ⊗N3 into the tensor product of the pure modules O ⊗Mi. According to
Theorem 6.3, the connection on this tensor product is the tensor product of
the connections on the O ⊗Mi. We conclude that the functor, construction
above, respects tensor products.
□
Remarks 6.8. — (1) For general diﬀerence modules M over K it is also
possible to deﬁne a connection ∇N on v(N) with at most a pole at 1 ∈Eq.
However for non integer slopes there seems not be a canonical choice for
∇N.
(2) In the situation of Example 6.5, the map ℓ: P2 →P1 is responsible for
divergence, ‘Stokes matrices’ and the unipotent part of the diﬀerence Galois
group of N. In general, the connection ∇N : v(N) →ΩEq(t[1])⊗v(N) has a
pole of order t. The irregularity of the connection ∇N locally at 1 ∈Eq will
produce Stokes matrices (in the classical sense) and unipotent elements of
the local analytic diﬀerential Galois group which depend on ℓ. The precise
relation remains to be investigated.
– 709 –
Marius van der Put, Marc Reversat
(3) It is interesting to apply another method to Example 6.4. For any in-
teger t > 0 one deﬁnes Gt = 
n∈Z(qt)n(n−1)/2(−zt)n. One observes that
(−zt)Gt(qz) = Gt(z) and that the set of the zeros of Gt is µt × qZ, where
µt is the group of the t-th roots of unity.
Let again N = Ke1 + Ke2 with Φ(e1) = (−z)te1, Φ(e2) = e2 + pe1
with p ∈C[z, z−1]. Deﬁne now f1 = G−1
t e1 and f2 = e2. Then Oe1 + Oe2
embeds into Of1 + Of2 and Φ(f1) = (−1)t−1f1 and Φ(f2) = f2 + pGtf1.
The connection ∇is deﬁned by ∇f1 = 0, ∇f2 = ω ⊗f2 where ω is the
canonical solution of (Φ −1)ω = (−1)t−1d(pGt). The resulting connection
∇N has at most simple poles at the image points of µt in Eq.
(4) The variation in (3) on Example 6.4 extends to a functor on the category
of the diﬀerence modules over K with integer slopes to the category of the
connections on Eq having at most simple poles in the images of 
t⩾1 µt in
Eq. This functor is constructed as in the proof of Theorem 6.7 and it has
again the properties: C-linear, faithful and commuting with tensor products.
For this variation on Theorem 6.7 and in connection with Example 6.5,
one observes that ℓ: P2 →P1 contributes to the poles of ∇N on the image
points of µt in Eq. Thus ℓcontributes to the monodromy group for the
connection ∇N.
