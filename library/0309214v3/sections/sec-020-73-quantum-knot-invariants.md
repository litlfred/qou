---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-020-73-quantum-knot-invariants
section_title: "Quantum knot invariants"
section_number: 7.3
pages: 29-37
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
7.3.1 The quasi- R–matrix
Fix a reduced word w representing the longest element of W . For each r, 1 ≤
r ≤ t, let
Θ r :=
∑
k∈N
ck f k
r ⊗ ek
r ,
where ck = (−1)kv−k(k−1)/2
γr
(vγr − v−1
γr )k
[k]γr ! .
Geometry & Topology, Volume 9 (2005)
1282 Stavros Garoufalidis and Thang T Q Lˆ e
Here vγ = v(γ|γ)/2 , and
[k]γ! =
k∏
i=1
vi
γ − v−i
γ
vγ − v−1γ
.
The main thing to observe is that ck is q –holonomic with respect to k . Note
that although Θ r is an inﬁnite sum, for every weight λ ∈ X , the action of Θ r
on M (λ) ⊗ M (λ) is well-deﬁned. This is because the action of er is locally
nilpotent, ie, for every x ∈ M (λ), there is k such that ek
r · x = 0.
The quasi-R–matrix is:
Θ := Θ tΘ t−1 . . .Θ 1.
We will consider Θ as an operator from M (λ) ⊗ M (λ) to itself. There is a
natural basis for M (λ) ⊗ M (λ) coming from the PBW basis of M (λ).
Proposition 7.5 The matrix of Θ acting on M (λ) in a PBW basis is q –
holonomic with respect to all the coordinates of the entry an d λ.
Proof It’s enough to prove the statement for each Θ r . The result for Θ r
follows from the fact that the actions of ek
r , f k
r on M (λ), as well as ck , are
q –holonomic in k and so are all the coordinates of the matrix entries, by Propo -
sition 7.4 .
7.3.2 The R–matrix and the braiding
As usual, let us deﬁne the weight on M (λ) by declaring the weight of Fn · η to
be λ − ∑ niγi , where n = ( n1, . . . , nt). The space M (λ) is the direct sum of
its weight subspaces.
Let D : M (λ) ⊗ M (λ) → M (λ) ⊗ M (λ) be the linear operator deﬁned by
D(x ⊗ y) = v−(|x|,|y|)x ⊗ y.
Clearly D is q –holonomic; it’s called the diagonal part of the R–matrix, which
is R := Θ D.
The braiding is B := Rσ , where σ(x⊗ y) = y ⊗ x. Combining the above results,
we get the following:
Theorem 8 The entry of the matrix of the braiding acting on M (λ) is q –
holonomic with respect to all the coordinates and λ.
Remark 7.6 Technically, in order to deﬁne the diagonal part D, one needs to
extend the ground ring to include a D-th root of v , since ( λ, µ), with λ, µ ∈ X ,
is in general not an integer, but belonging to 1
D Z.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1283
7.3.3 q –holonomicity of quantum invariants of knots
First let us recall the deﬁnition of quantum knot invariant.
Using the braiding B : M (λ) → M (λ) one can deﬁne a representation of the
braid group τ : Bm → (M (λ))⊗m by putting
τ (σi) := id ⊗i−1 ⊗B ⊗ id⊗m−i−1 .
Let ρ denote the half-sum of positive roots. For an element x ∈ U and an
U –module V , the quantum trace is deﬁned as
trq(x, V ) := tr( xK−2ρ, V ).
Suppose a framed knot K is obtained by closing a braid β ∈ Bm . We would
say that the colored Jones polynomial is the quantum trace of τ (β). However,
since M (λ) is inﬁnite-dimensional, the trace may not make sense. Inst ead, we
will use a trick of breaking the knot . Let K′ denote the long knot which is the
closure of all but the ﬁrst strand of β .
Recall that τ (β) acts on ( M (λ))⊗m . Let
τ (β)(λ)n′
1,...,n′
m
n1,...,nm ∈ Z[v±1/D]
be the entries of the matrix τ (β)(λ). We will take partial trace by ﬁrst putting
n1 = n′
1 = 0 and then take the sum over all n2 = n′
2, . . . ,nm = n′
m . The
following lemma shows that the sum is actually ﬁnite.
Lemma 7.7 Suppose n1 = 0 . There are only a ﬁnite number of collections of
(n2, n3, . . . ,nm) ∈ Nt−1 such that
τ (β)(λ)n1,...,nm
n1,...,nm
is not zero.
Proof Let M ′(λ) be the maximal proper U –submodule of M (λ). Then
L(λ) = M (λ)/M′(λ) is a ﬁnite dimensional vector space. In particular it has
only a ﬁnite number of non-trivial weights. Hence, all excep t for a ﬁnite number
of fn, n ∈ Nt, are in M ′(λ).
We present the coeﬃcients B±(λ) graphically as in Figure 3.
Note that if ( B±)m1,m2
n1,n2 is not equal to 0, then fm2 can be obtained from fn1
by action of an element in U , and similarly, fm1 can be obtained from fn2 by
action of an element in U . Thus if we move upwards along a string of the braid,
Geometry & Topology, Volume 9 (2005)
1284 Stavros Garoufalidis and Thang T Q Lˆ e
Figure 3: ( B+)m1,m2
n1,n2 and ( B−)m1,m2
n1,n2
the basis element at the top can always be obtained from the on e at the bottom
by an action of U .
Because the closure of β is a knot, by moving around the braid one can get any
point from any particular point. Because the basis element f0 is not in M ′(λ),
we conclude that if
τ (β)(λ)n1,...,nm
n1,...,nm
is not 0, with n1 = 0, then all the basis vectors fn2, . . . ,fnm are not in M ′(λ),
and there are only a ﬁnite number of such collections.
R ecall that 2 ρ is the sum of all positive roots. Let us deﬁne
JK′(λ) =
∑
n2,...nm∈Nt,n1=0,
(K−2ρ τ (β)(λ))n1,...,nm
n1,...,nm.
From q –holonomicity of τ (β)(λ) it follows that JK′(λ) is q –holonomic. JK′(λ)
is a long knot invariant, and is related to the colored Jones p olynomial JK of
the knot K by
JK(λ) = JK′(λ) × dimq(L(λ)),
where L(λ) is the ﬁnite-dimensional simple U –module of highest weight λ, and
dimq(L(λ)) is its quantum dimension, and is given by the formula
dimq(L(λ)) =
∏
α>0
v(λ+ρ,α) − v−(λ+ρ,α)
v(ρ,α) − v−(ρ,α) .
Since dim q(L(λ)) is q –holonomic in λ, we see that JK(λ) is q –holonomic. This
completes the proof of Theorem 6.
Remark 7.8 The invariant JK′ of long knots is sometime more convenient.
For example, JK(λ) might contain fractional power of q , but (if K′ has framing
0,) JK′(λ) is always in Z[q±1], see [20]. Also the function JK′ can be extended
to the whole weight lattice.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1285
7.4 Proof of Theorem 7
7.4.1 rα is q –holonomic
We will need the linear maps rα, r′
α : U ± → U ± , as deﬁned in [17, Chapter 6].
Their restriction to U − is uniquely characterized by the properties:
rα(xy) = rα(x) y + v(α,|x|) x rα(y) r′
α(xy) = x r′
α(y) + v(α,|x|) r′
α(x) y (5)
and for any two fundamental roots α, β, (see [17, Eqn.(6.15.4)]) and
rα(F n
β ) = r′
α(F n
β ) = δα,β
1 − v2n
α
1 − v2α
F n−1
α , (6)
where vα := v(α,α)/2 ; see [17, Eqn.(8.26.2)].
Lemma 7.9 For a ﬁxed α ∈ {α1, . . . , αℓ}, the matrix entries of the operators
(rα)k, (r′
α)k : U − → U − are q –holonomic with respect to k and the coordinates
of the matrix entry. Similarly, (rα)k, (r′
α)k : U + → U + are q –holonomic.
Proof We give a proof for rk
α : U − → U − . The other case is similar.
There is a reduced word w′ = si1 . . . sit representing the longest element ω0
of W such that αi1 = α. Then w = si2 . . . sits ¯α is another reduced word
representing ω0 , where ¯α := −ω0(α).
For the PBW basis of U − associated with w it’s known that γt = α, and thus
ft = Fα . According to [17, 8.26.5], for every x in the algebra U −[t − 1, 1], one
has
rα(x) = 0 .
Using Equations (5) and (6) and induction, one can easily sho w that for every
x ∈ U −[t − 1, 1],
(rα)k(f nt
t x) =
k∏
i=1
1 − v2nt−2i+2
α
1 − v2α
f nt−k
t x,
This formula, applied to x = f nt−1
t−1 . . . fn1
1 , proves the statement.
7.4.2 Uq(sl2) is q –holonomic
Lemma 7.10 Theorem 7 holds true for g = sl2 .
Geometry & Topology, Volume 9 (2005)
1286 Stavros Garoufalidis and Thang T Q Lˆ e
Proof The PBW basis for U is F nK jEm , with m, n ∈ N and j ∈ Z. First of
all we know that
Em
α F n
α =
∞∑
i=0
[ m
i
]
vα
[ n
i
]
vα
F n−i
α b(Kα; 2i − n − m, i) Em−i
α ,
where b(Kα; a, i) :=
i∏
j=1
Kαva−j+1
α − K −1
α v−a+j−1
α
vα − v−1α
.
Here for any root γ , one deﬁnes vγ = v(γ,γ )/2 , and
[ m
i
]
vα
is the usual
quantum binomial coeﬃcient calculated with v replaced by vα .
Hence
(F mK kEn)(F m′
K k′
Em′
) =
∞∑
i=0
F m+m′−i a(m, k, n, m′, k′, n′, i) En+n′−i,
where
a(m, k, n, m′, k′, n′, i)
= v2k(i−m′)+2k′(i−n)
[ n
i
][ m′
i
]
[i]! b(K; 2i − n − m′, i) K k+k′
.
The value of the function a is in Z[v±1][K ±1]. Consider the coeﬃcient of K r
in a; one gets a function of m, n, k, m′, n′, k′, i, r with values in Z[v±1] which is
clearly q –holonomic with respect to all variables. The lemma follows .
7.4.3 Ek
α, F k
α : U → U are q –holonomic in k
Proposition 7.11 For a ﬁxed fundamental root α ∈ {α1, . . . , αℓ}, the opera-
tors Ek
α, F k
α : U → U of left multiplication are q –holonomic with respect to k
and all the coordinates of the matrix entry. Similarly, the r ight multiplication
by Ek
α, F k
α are q –holonomic with respect to k and all the coordinates of the
matrix entry.
Proof (a) Left multiplication by F k
α and right multiplication by Ek
α .
Choose w as in the proof of Lemma 7.9. Then ft = Fα and et = Eα , and
an element of the PBW basis has the form f nt
t xKβyemt
t . It’s clear that left
multiplication by Fα and right multiplication by Eα are q –holonomic.
(b) Left multiplication by Ek
α .
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1287
Choose a reduced word w = si1 . . . sit representing the longest element ω0 that
begins with α: αi1 = α. We have the corresponding PBW basis fi, ei, i =
1, . . . , t with f1 = Fα and e1 = Eα . Thus a typical element of the PBW basis
has the form
xF n1
α KβEm1
α y, (7)
where x = f nt
t . . . fn2
2 , y = em2
2 . . . emt
t . By [17, 8.26.6], since x ∈ U −[t, 2], one
has r′
α(x) = 0. Using formula [17, 6.17.1], one can easily prove by indu ction
that
(Eα)kx =
∞∑
i=0
vi−ik
[ k
i
]
vα
K i
α
(vα − v−1α )i (rα)i(x)Ek−i
α .
Using this formula one can move the Eα past x in the expression (7), (there
appear rα and Kα ), then one moves Eα past Fα using the sl2 case. The last
step is moving past Kβ is easy, since
EαKβ = v−(β,α)KβEα.
Using Lemmas 7.9 and 7.10, we see that each “moving step” is q –holonomic.
Hence we get the result for the left multiplication by Ek
α .
(c) Right multiplication by F k
α .
The proof is similar. We use the same basis (7) as in the case b) . For y , by
Lemma 8.26 of [17], one has rα(y) = 0. Hence using induction based on the
formula (6.17.2) of [17] one can show that
yF n
α =
∞∑
i=0
vi(n−i)
α
(v−1α − vα)i
[ n
i
]
vα
F n−i
α K −i
α (r′
α)i(y).
Using this formula, and the results for r′
α (Lemma 7.9) and sl2 (Lemma 7.10)
we can move Fα to the right.
7.4.4 Tα is q –holonomic
Proposition 7.12 For a ﬁxed fundamental root α ∈ { α1, . . . , αℓ}, the braid
operator Tα : U → U and its inverse T −1
α are q –holonomic.
Proof By Proposition 7.3 we can use any PBW basis.
Choose a reduced word w′ = si1 . . . sit representing the longest element ω0
that begins with α: αi1 = α. Then w = si2 . . . sits ¯α is another reduced word
representing ω0 , where ¯α is the dual of α: ¯α = −ω0(α).
Geometry & Topology, Volume 9 (2005)
1288 Stavros Garoufalidis and Thang T Q Lˆ e
We use fr to denote fr(w), and f ′
r to denote fr(w′). The relation between the
two PBW basis of w and w is as follows: For 1 ≤ r ≤ t − 1,
Tα(fr) = f ′
r+1, T α(er) = e′
r+1.
Besides, ft = Fα = f ′
1, et = Eα = e′
1 .
We will consider the matrix entry of Tα : U → U where the source space is
equipped with the PBW corresponding to w, while the target space with the
PBW basis corresponding to w′ .
From [17, Chapter 8], recall that:
Tα(Fα) = −K −1
α Eα, T α(Eα) = −FαKα.
Hence
Tα(F n
α ) = ( −1)nvn(n−1)
α K −n
α En
α, T α(Em
α ) = ( −1)mv−m(m−1)
α F m
α K m
α .
For a basis element xσ = f nt
t . . . fn1
1 Kβem1
1 . . . emt
t , we have
Tα(xσ) = dα(nt, mt) K −nt
α Ent
α × (f ′
t)mt−1
. . .(f ′
1)n2Ksαβ(e′
1)m2 . . .(e′
t)mt−1 × F mt
α K mt
α ,
where dα(nt, mt) := ( −1)nt+mtvnt(nt−1)−mt(m1−1)
α .
The left or right multiplication by K n
α is q –holonomic with respect to n and
all the coordinates. The left multiplication by Ent , as well as the right mul-
tiplication my F mt
α is q –holonomic with respect to nt and all coordinates, by
Proposition 7.11. One then can conclude that Tα is q –holonomic.
The proof for T −1
α : U → U is similar. One should use the PBW basis of w′ for
the source, and that of w for the target.
7.4.5 Proof of Theorem 7
It is clear that for each j ∈ Zℓ , the operator Kj : U → U of left multiplication
is q –holonomic.
Fix a reduced word w representing the longest element of W . It suﬃces to
show that for each 1 ≤ r ≤ t the operators ek
r , f k
r : U → U (left multiplication)
are q –holonomic with respect to all variables, including k .
This is true if er = Eα and fr = Fα , where α is one of the fundamental
roots, by Proposition 7.11. But any er or fr can be obtained from Eα and
Fα by actions of product of various Tαi ’s. Hence from Proposition 7.12 we get
Theorem 7.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1289
A Appendix: Proof of Proposition 7.3 for A2 and B2
In this appendix we will prove Proposition 7.3 for the rank 2 L ie algebras A2
and B2 . We will achieve this by a brute-force calculation.
First, let us discuss some simpliﬁcation, due to symmetry. T he transition ma-
trix of U leaves invariant each of U +, U −, U 0 . On U 0 the transition matrix is
identity. Hence it’s enough to consider the restriction of t he transition matrix
in U − and U + . Furthermore, the Cartan symmetry (the operator τ of [17])
reduces the case of U + to that of U − .
