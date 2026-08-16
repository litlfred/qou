---
doc_id: ant-v14-n7-s-p01
doc_title: "p-adic Asai L-functions of Bianchi modular forms David Loeﬄerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the"
section_id: sec-002-3-siegel-units-and-weight-2-asaieisenstein-eleme
section_title: "Siegel units and weight 2 Asai–Eisenstein elements"
section_number: 3
pages: 14-17
source_pdf: ant-v14-n7-s-p01.pdf
source_sha256: 976199bfca4ac086
doc_brief: "p-adic Asai L-functions of Bianchi modular forms David Loefflerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the tensor induction"
---
3A. Modular units. Let U⊂ GL2(ˆZ) be an open compact subgroup, with associated symmetric space
YQ(U). In this section, we work exclusively overQ, so we shall drop the subscriptQ from the notation. As
is well known, the manifolds Y(U) are naturally the complex points of algebraic varieties deﬁned over Q.
Deﬁnition 3.1. A modular unit on Y(U) is an element of O(Y(U))×, that is, a regular function on Y(U)
with no zeros or poles. (This corresponds to a rational function on the compactiﬁcation X(U) whose
divisor is supported on the cusps).
Modular units are motivic in the sense that there arerealisations of modular units in various cohomology
theories. In particular, to a modular unit φ∈ O(Y1(N))× one can attach:
• its de Rham realisation CdR(φ)∈ H1
dR(Y1(N), Q), which is the class of the differential form
d logφ= dφ
φ ;
• its Betti realisation C(φ)∈ H1(Y1(N), Z), which is the pullback along φ: Y1(N)(C)→ C× of the
generator C of H1(C×, Z)∼= Z that pairs to 1 with the homology class of a positively oriented loop
around 0.
p-adic Asai L-functions of Bianchi modular forms 1683
These are closely related:
Proposition 3.2. The canonical comparison isomorphism
H1(Y1(N), Z)⊗Z C ∼=−→H1
dR(Y1(N), Q)⊗Q C
maps C(φ) to 1/(2πi)CdR(φ).
Proof. The comparison isomorphism identiﬁes the de Rham cohomology class of an n-formω with the
Betti cohomology class mapping an n-simplexδ to
∫
δω. By construction, this isomorphism is compatible
with the pullback maps in the two cohomology theories attached to a smooth map of manifolds.
In our case, the modular unitφ gives a map Y1(N)(C)→ C×. By deﬁnition, C(φ) is the pullback byφ
of the generator C of H1(C×, Z); and CdR(φ) is the pullback of the class of the differential dT
T , where T
is the coordinate on C. If δ denotes a positively oriented loop around 0, then
∫
δ
dT
T = 2πi. Since C pairs
to 1 withδ (by deﬁnition), the result follows. □
Remark. It is conventional to “normalise away” the factor of 2πi by deﬁning C(φ) as an element
of H1(Y1(N), Z(1)), where Z(1)= 2πi· Z⊂ C. However, this formalism does not work well when
considering the cohomology of nonalgebraic manifolds, so we shall not use it here.
3B. Eisenstein series. The de Rham realisations of modular units give rise to weight 2 Eisenstein series
in the de Rham cohomology. In the next section, we’ll exhibit a canonical system of modular units – the
Siegel units – whose de Rham realisations can be written down very explicitly in terms of the following
Eisenstein series.
Deﬁnition 3.3 (compare [Kato 2004, §3]). Let τ∈ H, k an integer> 2, and β∈ Q/Z, with β⁄= 0 if
k= 2. Deﬁne
F(k)
β (τ):= (k− 1)!
(−2πi)k
∑′
(m,n)∈Z2
e2πiβm
(mτ+ n)k,
where the prime denotes that the term (m, n)=(0, 0) is omitted. This is a modular form of weight k and
level01(N), for any N such that Nβ= 0.
(Kato deﬁnes a slightly more general class of Eisenstein series F(k)
α,β; we shall only use the case α= 0,
so we drop it from the notation.)
For the L-value calculations in the Appendix, we shall need to use the fact that this series is a
specialisation of a real-analytic family. Forℜ(s)> 1− 1
2k, we deﬁne
E(k)
β (τ, s):= 0(s+ k)
(−2πi)kπ s
∑′
(m,n)∈Z2
Im(τ) s
(mτ+ n+β)k|mτ+ n+β|2s, (3-1)
where the prime denotes that the term (m, n)=(0, 0) is omitted ifβ= 0 (but included otherwise). This
has analytic continuation to all s∈ C, and we have
F(k)
β (τ)= E(k)
β (τ, 1− k).
(See, e.g., [Lei et al. 2014, 4.2.2(iv)].)
1684 David Loeﬄer and Chris Williams
3C. Siegel units.
Deﬁnition 3.4. For N> 1, and c> 1 an integer coprime to 6 N, let
cgN∈ O(Y1(N))×
be Kato’s Siegel unit (the unit denoted by cg0,1/N in the notation of [Kato 2004, §1]).
Slightly abusively, we shall use the same symbol cgN for the pullback of this unit to Y(M, N), for any
M> 1 (we shall only need this when M| N).
As in [op. cit.] we note that if c, d are two integers that are both > 1 and coprime to 6N, then we have
the identity
(d2−⟨ d⟩)cgN=(c2−⟨ c⟩)dgN. (3-2)
It follows that the dependence on c may be removed after extending scalars to Q: there is an element
gN∈ O(Y1(N))×⊗ Q such that cgN=(c2−⟨ c⟩)· gN for any choice of c.
Proposition 3.5. (i) The Siegel units arenorm-compatible, in the sense that if N′|N and N and N′ have
the same prime divisors, then under the natural map
pr: Y(M, N)→ Y(M, N′)
we have
(pr)∗(cgN)= cgN′.
(ii) The de Rham realisation of gN is the Eisenstein series
d log(gN)(τ)=− 2πi F(2)
1/N(τ) dτ.
Proof. Part (i) is proved in [Kato 2004, Section 2.11]. Part (ii) is [op. cit., Proposition 3.11(2)]. □
One important use of Siegel units comes in the construction of Euler systems; for example, see [Kato
2004; Lei et al. 2014; Kings et al. 2017]. The basic method in each of these cases is similar; one takes
cohomology classes attached to Siegel units under the realisation maps and pushes them forward to
a different symmetric space, then exploits the norm compatibility to prove norm relations for these
cohomology classes. We will do something similar in the Betti cohomology. In particular, we make the
following deﬁnition:
Deﬁnition 3.6. Let cCN:= C(cgN)∈ H1(Y1(N), Z) be the Betti realisation of cgN .
From Proposition 3.5(i), we see that if p| N, the classes cCN pr for r> 0 are compatible under
push-forward, and deﬁne a class
cCN p∞∈ lim←−−r
H1(Y1(N pr), Z).
Lemma 3.7. If ρ denotes the involution of Y1(N) corresponding to x+ iy↦→− x+ iy on H, then
ρ∗(cCN)=− cCN .
p-adic Asai L-functions of Bianchi modular forms 1685
Proof. The variety Y1(N) has a canonical model over Q for whichρ corresponds to complex conjugation
on Y1(N)(C). Since the Siegel units are deﬁned over Q in this model, they intertwine the action of ρ on
Y1(N)(C) with complex conjugation on C×. So it sufﬁces to check that complex conjugation acts as −1
on H1(C×, Z), which is clear. □
3D. Asai–Eisenstein elements in weight 2. Now let F be an imaginary quadratic ﬁeld, and n an ideal
of OF divisible by some integer> 4. Recall that we have
Y∗
F,1(n)=0∗
F,1(n)\H3,
and that we showed in Proposition 2.5 that the natural map
ι: YQ,1(N)↪→ Y∗
F,1(n)
is a closed immersion. We also need the following map:
Deﬁnition 3.8. Let m> 1 and a∈ OF. Consider the map
κa/m: Y∗
F,1(m2n)→ Y∗
F,1(n)
given by the left action of
( 1
0
a/m
1
)
∈ SL2(F) on H3. This is well-deﬁned, since it is easy to see that
(1 a/m
0 1
)
0∗
F,1(m2n)
(1−a/m
0 1
)
⊂0∗
F,1(n),
and it depends only on the class of a modulo mOF.
Remark. Note thatκa/m is not in general well-deﬁned on YF,1(m2n), since
(1 a/m
0 1
)(−1 0
0 1
)( 1−a/m
0 1
)
=
(−1 2 a/m
0 1
)
,
which is not in0F,1(n) if 2a /∈ mOF.
The elements we care about are the following. Assume that n is divisible by some integer q> 4, as
above. Then we have maps
YQ,1(m2N) ι→ Y∗
F,1(m2n) κa/m−−→Y∗
F,1(n).
Moreover, writing HBM
∗ for Borel–Moore homology (homology with noncompact supports), there are
isomorphisms
H1(YQ,1(m2N), Z)∼= HBM
