---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-009-10-quasitriangular-and-ribbon-structures
section_title: "Quasitriangular and ribbon structures"
section_number: 10
pages: 79-86
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
10. Quasitriangular and ribbon structures
The notion of quasitriangular Hopf algebra was introduced by Drinfeld in [45] and extended to the quasi-Hopf algebra case in [47]. In this section we introduce and study
quasitriangular structure for weak quasi-Hopf algebras. We shall then restrict to weak
quasi-Hopf algebras with a strong antipode and introduce the notion of ribbon structure
in this case. In particular, we develop the basic results for this special subclass. For some
results for which computational difficulties would arise, we further restrict to the special
subclass of weak Hopf algebras. In this case, we are able to present arguments extending the corresponding results for Hopf algebras. We conclude the section explaining how
later on we shall extend all the results of this section concerning weak Hopf algebras to
weak quasi-Hopf algebras with a strong antipode. This extension will be useful for the
forthcoming developments of the paper of Sect. 28 and for our applications of Sect. 32,
25.
With any weak quasi-bialgebra A, we associate the opposite algebra Aop with data given
by
ε
op = ε, ∆op(a) := σ ◦ ∆(a), Φop := Φ−1
321, (10.1)
where σ is the transposition automorphism of A ⊗ A and Φ−1
321 understood in a partial
sense. Note that Aop is a weak bialgebra if so is A.
Definition 10.1. A quasitriangular structure on A, also referred to R-matrix axioms, is
defined by a partially invertible element R ∈ A ⊗ A, (R ∈ M(A ⊗ A) if A is discrete)
satisfying the following properties,
D(R) = ∆(I), R(R) = ∆op(I) (10.2)
∆
op(a) = R∆(a)R−1
, (10.3)
∆ ⊗ 1(R) = Φ312R13Φ
−1
132R23Φ123, (10.4)
1 ⊗ ∆(R) = Φ−1
231R13Φ213R12Φ
−1
123, (10.5)
We follow the standard notation: for a simple tensor a = a1 ⊗ · · · ⊗ an ∈ A⊗n and
a permutation i ∈ Pn, ai1...inis the simple tensor having ajin the ij -th component. If
a ∈ A⊗k with k < n then we apply this definition to a tensored on the right with n − k
copies of the identity operator. Furthermore relations (10.2)–(10.5) imply the analogue of
the Yang-Baxter relation, which, taking into account (10.4) and (10.5), can be written in
the following form
Φ
−1
321 = I ⊗ R1 ⊗ ∆(R)Φ∆ ⊗ 1(R
−1
)R
−1 ⊗ I. (10.6)
Relations (10.2), (10.3), (10.6), and the following property (10.15) express the twist relation
A
op = AR. (10.7)
Given a ∗-algebra A endowed with the structure of a weak quasi-bialgebra, we can form
another weak quasi-bialgebra A˜, the adjoint algebra with the same algebra structure but
counit, coproduct, and associator given by
ε˜(a) := ε(a
∗
), ∆( ˜ a) := ∆(a
∗
)
∗
, Φ := Φ ˜ ∗−1
. (10.8)

80 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Note that if B is a ∗-algebra, and p and q are idempotents of B and if T ∈ (p, q) then
T
∗ ∈ (q∗
, p∗). Hence if T is partially invertible in (p, q), so is T
∗
in (q
∗
, p∗). We understand
Φ
∗−1
in this way. It will be useful to observe that
Proposition 10.2. If R is an R-matrix for A then
a) Rop := R21 is an R-matrix for Aop,
b) if A is a ∗-algebra, R˜ := R∗−1
is an R-matrix for A˜,
c) if F ∈ A ⊗ A is a twist, RF := F21RF −1is an R-matrix for AF ,
d) R
−1
21 is another R-matrix for A.
Definition 10.3. By a quasitriangular weak bialgebra we understand a weak bialgebra
endowed with a quasitriangular structure as a weak quasi-bialgebra.
Note that any R-matrix of a weak Hopf algebra is a 2-cocycle by (10.7). An important
property for representation theory of quasitriangular Hopf algebras is that the square of the
antipode is an inner automorphism. This was shown by Drinfeld who explicitly constructed
an implementing invertible element u ∈ A for Hopf algebras [46]. Furthermore, Reshetikhin
and Turaev introduced the notion of ribbon Hopf algebra [155]. We next show that these
developments have extensions to weak Hopf algebras, although the computations in the
proofs become more involved. We start with the following remark giving a simplification
of the axioms in the weak Hopf algebra case.
Proposition 10.4. Equations (10.4) and (10.5) for a weak Hopf algebra are equivalent to
∆ ⊗ 1(R) = Φ312R13R23Φ123, (10.9)
1 ⊗ ∆(R) = Φ−1
231R13R12Φ
−1
123. (10.10)
Proof. We prove (10.9). We have Φ123 = 1 ⊗ ∆(P)∆ ⊗ 1(P), Φ−1 = ∆ ⊗ 1(P)1 ⊗ ∆(P),
Φ312 = ∆⊗1(P
′
)a2⊗b⊗a1, and Φ−1
132 = a1⊗b⊗a21⊗∆op(P) where P = ∆(I), P
′ = ∆op(I),
and we have used the notation ∆(b) = b1 ⊗ b2 and P = a ⊗ b. By (10.3) we have
R13Φ
−1
132R23 = R13a1 ⊗ b ⊗ a21 ⊗ ∆
op(P)R23 = a2 ⊗ b ⊗ a1R13R231 ⊗ ∆(P)
and the conclusion follows. For (10.10) we similarly have Φ−1
231 = 1 ⊗ ∆(P
′
)b2 ⊗ a ⊗ b1 and
Φ213 = b1 ⊗ a ⊗ b2∆op ⊗ 1(P). □
We give a definition of ribbon weak quasi-Hopf algebra A with a strong antipode extending the corresponding notion for Hopf algebras due to Reshetikhin and Turaev [154].
Definition 10.5. Let A be a (discrete) weak quasi-bialgebra Then A is called balanced if
it is quasitriangular and is endowed with an invertible central element v ∈ A (v ∈ M(A))
such that
R21R = v ⊗ v∆(v
−1
), (10.11)
where R is the R-matrix. If in addition A has an antipode (S, α, β) such that S(v) = v,
then A is called a ribbon weak quasi-Hopf algebra, and v the ribbon element. A balanced
(ribbon) weak bialgebra is a weak bialgebra (weak Hopf algebra) is defined in the natural
way.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 81
Note that the definition does not depend on the choice of the antipode by Prop. 6.10.
We next introduce Drinfeld element u. For simplicity, we restrict to the case of a weak
quasi-Hopf algebra with strong antipode. This will suffice for our applications.
Definition 10.6. Let A be a quasitriangular weak quasi-Hopf algebra with strong antipode
S and R-matrix R. The element
u =
X
i
S(ti)ri (10.12)
where R =
P
i
ri ⊗ tiis called Drinfeld element. We also set R−1 =
P
j
rj ⊗ tj.
Proposition 10.7. Let A be a quasitriangular weak quasi-Hopf algebra with strong antipode
S and u the associated Drinfeld element. Then u is invertible, u
−1 =
P
j S
−1
(tj )rj and
S
2
(x) = uxu−1, x ∈ A. (10.13)
Proof. This proof is a generalisation of the corresponding proof for quasitriangular Hopf
algebras, see e.g. [105]. In the following computations we use the notation ∆(x) = x1 ⊗ x2
for x ∈ A, ∆(I) = a ⊗ b, R = r ⊗ t, Φ−1 = x
′ ⊗ y′ ⊗ z′
. We have
∆
op ⊗ 1(∆(x))R ⊗ IΦ−1 = R ⊗ IΦ−1
1 ⊗ ∆(∆(x))
that accordingly may be written as
x1,2rx′ ⊗ x1,1ty′ ⊗ x2z
′ = rx′x1 ⊗ ty′x2,1 ⊗ z′x2,2.
Applying 1 ⊗ S ⊗ S
2 and multiplying from right to left gives by (6.7), (6.2),
S
2
(x)w = wx, w := S
2
(z
′
)S(y
′
)ux′. (10.14)
The 3-cocycle relation Φ−1 ⊗ I = ∆ ⊗ 1 ⊗ 1(Φ−1)1 ⊗ 1 ⊗ ∆(Φ−1)I ⊗ Φ1 ⊗ ∆ ⊗ 1(Φ) leads
to w = u. The last argument extends in a straightforward way the case of quasi-Hopf
algebras, see the proof of Lemma 2.4 in [20]. The formula for u
−1
follows from Cor. 6.11
b). □
Note that this proposition does not depend on the R-matrix properties (10.4), (10.5).
But when they do hold, we obtain stronger relations for u in a way that extends the
corresponding relations for quasitriangular Hopf algebras. The following extends Lemma
2.1.1, Ch. XI, of [174], or Theorem VIII.2.4 of [105] to weak Hopf algebras.
Proposition 10.8. If A is a quasitriangular weak quasi-bialgebra algebra defined by R
then
ε ⊗ 1(R) = I, 1 ⊗ ε(R) = I. (10.15)
If A is a weak Hopf algebra,
S ⊗ S(R) = f21Rf −1, (10.16)
where f is the element defined in Prop. 6.13.

82 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proof. The proof of (10.15) goes as in the bialgebra case, it suffices to apply ε ⊗ 1 ⊗ 1 and
1 ⊗ 1 ⊗ ε to (10.4) and (10.5) respectively. To show (10.16) we tensor both sides of (10.9)
by the identity operator I on the left and multiply by I ⊗ 1 ⊗ ∆(P)∆ ⊗ ∆(P) on the right
and obtain
1 ⊗ ∆ ⊗ 1(I ⊗ R)1 ⊗ 1 ⊗ ∆(I ⊗ P)∆ ⊗ ∆(P) = XR34 (10.17)
where
X = I ⊗ Φ312R241 ⊗ 1 ⊗ σ[1 ⊗ 1 ⊗ ∆(I ⊗ P)∆ ⊗ ∆(P)],
σ : A ⊗ A → A ⊗ A is the flip automorphism and we have used the intertwining relations
(10.2), (10.3). We next recall from the first section the map V (a⊗b⊗c⊗d) = S(b)c⊗S(a)d
that we wish to apply to both sides of (10.17) and we obtain
f = V (X)R. (10.18)
To show the claim we perform computations taking into account the following facts: a)
one of the two ways the element f is defined for a weak quasi-Hopf algebra with strong
antipode is f = V (I ⊗ Φ
−11 ⊗ 1 ⊗ ∆(Φ)). For a weak Hopf algebra we have
I ⊗ Φ
−1
1 ⊗ 1 ⊗ ∆(Φ) = I ⊗ ∆ ⊗ 1(P)1 ⊗ 1 ⊗ ∆(1 ⊗ ∆(P))∆ ⊗ ∆(P) =
1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))I ⊗ 1 ⊗ ∆(P)∆ ⊗ ∆(P).
b) We have V (1⊗∆⊗1(Z)Y ) = V (Y ) as soon as m◦S⊗ε⊗1(Z) = I, where m : A⊗A → A
is the multiplication map. This holds in particular for Z = I ⊗ R and Z = 1 ⊗ ∆(P),
by (10.15) and (6.7). Hence the image of the left hand side of (10.17) under V is f. c)
V (XR34) = V (X)R. We next apply a similar procedure to relation (10.17) for the opposite
weak Hopf algebra getting the relation
1 ⊗ ∆
op ⊗ 1(I ⊗ R21)1 ⊗ 1 ⊗ ∆op(I ⊗ P21)∆op ⊗ ∆op(P21) = XopR43 (10.19)
where Xop = I ⊗ Φ
−1
213R421 ⊗ 1 ⊗ ∆(I ⊗ P21)∆op ⊗ ∆(P21) but now we apply the map
W := σ ◦ S ⊗ S ◦ V
op to both sides of (10.19), where Vop acts as V but with S−1
in
place of S. To perform these computations we remark that: d) for the left hand side
we use the identity S ⊗ S ◦ V
op = V ◦ τ , where τ is the automorphism of A⊗4
taking
a1 ⊗ a2 ⊗ a3 ⊗ a4 → a4 ⊗ a3 ⊗ a2 ⊗ a1. e) the image of the left hand side of (10.19) under
τ is
1 ⊗ ∆ ⊗ 1(R ⊗ I)∆ ⊗ 1 ⊗ 1(P ⊗ I)∆ ⊗ ∆(P)
f) the second way in which f can be computed is f = V (Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1)), and recall
that this was due to the 3-cocycle relation of Φ and the previous remark b). For a weak
Hopf algebra, computations similar to those in a) give
Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1) = 1 ⊗ ∆ ⊗ 1(∆ ⊗ 1(P))∆ ⊗ 1 ⊗ 1(P ⊗ I)∆ ⊗ ∆(P).
Hence using b) again, the image of the left hand side of (10.19) under W is f21. For the
right hand side, we write W in the form W = V ◦ σ ⊗ σ ◦ τ . Simple computations show
that if α = σ ⊗ σ ◦ τ then α(R43) = R21 and that V (Y R21) = S ⊗ S(R)V (Y ) for Y ∈ A⊗4.
Summarizing, the image of (10.19) under W is
f21 = S ⊗ S(R)V (α(X
op)). (10.20)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 83
Comparing (10.18) and (10.20), the proof of (10.16) will be complete provided V (X) =
V (α(Xop)). To show this, a computation relying on by (10.2), (10.3), (6.4) gives
I ⊗ Φ312R241 ⊗ 1 ⊗ σ[1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))] = 1 ⊗ ∆ ⊗ 1(Z)I ⊗ Φ312R24
where Z = 1 ⊗ ∆op(P). It follows, by a), and the 3-cocycle relation, and (10.2), (10.3)
again,
1 ⊗ ∆ ⊗ 1(Z)X = I ⊗ Φ312R241 ⊗ 1 ⊗ σ[I ⊗ Φ
−1
1 ⊗ 1 ⊗ ∆(Φ)] =
I ⊗ Φ312R241 ⊗ 1 ⊗ σ[1 ⊗ ∆ ⊗ 1(Φ)Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1)] =
(I ⊗ Φ1 ⊗ ∆ ⊗ 1(Φ))1423R241 ⊗ 1 ⊗ σ[Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1)].
On the other hand,
α(X
op) = Φ−1
142R241 ⊗ 1 ⊗ σ[∆ ⊗ 1(P) ⊗ I∆ ⊗ ∆(P)]
and similar computations give
a1,1 ⊗ a2 ⊗ b ⊗ a1,2α(X
op) = Φ−1
142R241 ⊗ 1 ⊗ σ[Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1
)].
Hence
1 ⊗ ∆ ⊗ 1(Z)X = (I ⊗ Φ1 ⊗ ∆ ⊗ 1(Φ)Φ ⊗ I)1423a1,1 ⊗ a2 ⊗ b ⊗ a1,2α(X
op) =
(1 ⊗ 1 ⊗ ∆(Φ)∆ ⊗ 1 ⊗ 1(Φ))1423α(X
op)
by the 3-cocycle relation again. It now suffices to apply V on both sides of this identity. □
Proposition 10.9. Drinfeld element u of a quasitriangular weak Hopf algebra satisfies
R21R∆(u) = ∆(u)R21R = f
−1S ⊗ S(f21)u ⊗ u.
Proof. The first equality follows easily from (10.3). We show the second equality. The left
hand side equals, by Prop. 6.13,
∆(u)R21R = ∆(S(t))R21R∆(r) = f
−1S ⊗ S(∆op(t))fR21R∆(r).
where notation is as before: R = r ⊗ t, ∆(I) = P = a ⊗ b, ∆(x) = x1 ⊗ x2. We are thus
reduced to show the equality
S ⊗ S(∆op(t))fR21R∆(r) = S ⊗ S(f21)u ⊗ u. (10.21)
We denote by λ and ρ the left and right hand sides of (10.21), respectively. We use again the
map V : A⊗4 → A⊗2, V (a⊗b⊗c⊗d) = S(b)c⊗S(a)d, and recall that f = V (A) = V (X),
where we have set A = I ⊗ Φ
−11 ⊗ 1 ⊗ ∆(Φ) and X = Φ ⊗ I∆ ⊗ 1 ⊗ 1(Φ−1
). We shall also
need the property
V (La ⊗ b ⊗ c ⊗ d) = S(b) ⊗ S(a)V (L)c ⊗ d. (10.22)
For example, it shows that
λ = V (A · ∆(t) ⊗ [R21R∆(r)]).
Furthermore, assuming that Y ∈ A⊗4satisfies V (Y ) = u⊗u, and writing X = x⊗y⊗w⊗z,
we have
ρ = S ⊗ S((S(y)w ⊗ S(x)z)21)u ⊗ u = S(z)S
2
(x)u ⊗ S(w)S
2
(y)u =
S(z)ux ⊗ S(w)uy = V (Y w ⊗ z ⊗ x ⊗ y) = V (Y X3412).

84 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We start computing λ. By (10.9), and (10.10),
R21R∆(r) ⊗ ∆(t) = R21R∆ ⊗ 1 ⊗ 1(Φ−1
231R13R12Φ
−1
123) =
∆ ⊗ 1 ⊗ 1(Φ−1
231)R21∆
op ⊗ 1 ⊗ 1(R13)R∆ ⊗ 1 ⊗ 1(R12)∆ ⊗ 1 ⊗ 1(Φ−1
123) =
∆ ⊗ 1 ⊗ 1(Φ−1
231)R21Φ421R24R14Φ214RΦ312R13R23Φ123∆ ⊗ 1 ⊗ 1(Φ−1123).
After applying the permutation of (13)(24) ∈ P4, and taking into account
A1 ⊗ 1 ⊗ ∆(Φ−1) = I ⊗ Φ
−1
1 ⊗ 1 ⊗ ∆(1 ⊗ ∆(P)) = 1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))I ⊗ Φ
−1
we see that λ equals
V (1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))[I ⊗ Φ
−1R43Φ243R42R32Φ432][R34Φ134R31R41Φ341]1 ⊗ 1 ⊗ ∆(Φ−1
312)).
The first bracketed element is the shift to the right of Φ−1R32Φ132R31R21Φ321, and computations similar to those of Prop. 10.4 show that the latter equals (1⊗∆(R))312R21b⊗a2 ⊗a1.
Similarly, the second bracketed element acts as identity on the second factor, and as
a ⊗ b2 ⊗ b1R23R21Φ
−1
213R31Φ231 in the remaining factors. This in turn equals a ⊗ b2 ⊗ b1(1 ⊗
∆(R))213R31Φ231 by Prop. 10.4 again and property (9.5). Hence λ equals
V (1⊗∆⊗1(1⊗∆(P))(1⊗∆(R))423R32I ⊗b⊗a2⊗a1 ·a⊗I ⊗b2⊗b1(1⊗∆(R))314R41X3412).
Taking the range of X into account, we are finally left to show that
Y := 1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))(1 ⊗ ∆(R))423R32I ⊗ b ⊗ a2 ⊗ a1·
a ⊗ I ⊗ b2 ⊗ b1(1 ⊗ ∆(R))314R41(1 ⊗ ∆ ⊗ 1(∆ ⊗ 1(P))3412.
indeed satisfies V (Y ) = u ⊗ u. To this aim, we move the two idempotents at both extremes towards the center using the commutation relations (10.3) and (9.4) and the domain
relations (9.3), we find
Y = (1 ⊗ ∆(R))423R32I ⊗ b2 ⊗ b1 ⊗ a(1 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P))1432·
(1 ⊗ ∆ ⊗ 1(∆ ⊗ 1(P))1432a1 ⊗ I ⊗ b ⊗ a2(1 ⊗ ∆(R))314R41 =
(1 ⊗ ∆(R))423R32(1 ⊗ ∆ ⊗ 1(Φ))1432(1 ⊗ ∆(R))314R41.
Now 1⊗∆⊗1(1⊗∆(P))(1⊗∆(R))423R32 and (1⊗∆(R))314R41(1⊗∆⊗1(∆⊗1(P))3412 have
(Q3)1432 and (P3)1432 as domain and range respectively, and furthermore Q31⊗∆⊗1(Φ)P3 =
Q3∆ ⊗ ∆(P)P3 by the cocycle relation, see Remark 9.3. Hence we can also write
Y = (1 ⊗ ∆(R))423R32(∆ ⊗ ∆(P))1432(1 ⊗ ∆(R))314R41.
We are now able to compute V (Y ) by means of an iterative use of (10.22):
V ((1 ⊗ ∆(R))423) = I ⊗ I,
V ((1 ⊗ ∆(R))423R32) = u ⊗ I,
V ((1 ⊗ ∆(R))423R32(∆ ⊗ ∆(P))1432) = S(b2) ⊗ S(a1) · u ⊗ I · b1 ⊗ a2 =
S(b2)ub1 ⊗ S(a1)a2 = S(S(b1)b2)u ⊗ ε(a) =
ε(b) ⊗ ε(a)u ⊗ I = u ⊗ I,
V ((1 ⊗ ∆(R))423R32(∆ ⊗ ∆(P))1432(1 ⊗ ∆(R))314) = I ⊗ S(t1) · u ⊗ I · r ⊗ t2 =
u ⊗ I1 ⊗ ε(R) = u ⊗ I,

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 85
V (Y ) = u ⊗ u,
and the proof is complete.
□
At the level of representation theory, the previous proposition establishes commutativity
of the following diagram.
ρ ⊗ σ ρ
∨∨ ⊗ σ∨∨
σ ⊗ ρ ρ ⊗ σ (ρ ⊗ σ)
∨∨
uρ⊗uσ
ε(ρ,σ)
ε(σ,ρ) uρ⊗σ
We shall go back to this in Sect. 27.
Remark 10.10. It follows from (10.11) and (10.15) that if v makes A balanced then
ε(v) = 1. Furthermore when v is a ribbon element, applying m ◦ S ⊗ 1 to both sides of
(10.11) and taking into account (10.13) also gives v
2 = uS(u), with u Drinfeld element, as
in Def. 10.6.
Corollary 10.11. The elements u and v of a ribbon weak Hopf algebra satisfy
∆(uv−1) = f
−1S ⊗ S(f21)uv−1 ⊗ uv−1
.
Thus ω = uv−1is a pivot making A into a pivotal weak Hopf algebra in the sense of
Def. 7.5.
Remark 10.12. It is shown in [154, 144] that when A is a quasi-triangular Hopf algebra
then v → ω = uv−1is a bijective correspondence between ribbon elements and invertible
elements ω ∈ A satisfying a) S
2
(a) = ωaω−1, b) S(ω) = ω
−1
, and c) S(u) = ω
−1uω−1 and
d) ∆(ω) = ω ⊗ ω (ω is group-like). Such elements ω are called charmed.
Remark 10.13. Altschuler and Coste extended ribbon structures to quasi-Hopf algebras [1], stated analogues of the lemmas of this section and outlined some of the proofs.
Complete proofs have been given in [83, 20]. In this passage, the construction of Drinfeld
element u and the notion of ribbon quasi-Hopf algebra needs to be suitaby modified. Moreover, the proof of the analogue of Prop. 10.8, Prop. 10.9 become more involved. These
works together with the results of this section lead to extensions of the main properties
of ribbon structures to the more general setting of weak quasi-Hopf algebras. Furthermore, the correspondence described in Remark 10.12 extends as well to quasi-triangular
weak quasi-Hopf algebras replacing the group-like condition d) with the pivot condition
∆(ω) = f
−1S ⊗ S(f21)ω ⊗ ω.
However, we shall refrain from doing this, and rather take an alternative categorical
approach. More in detail, motivated also by the study of quantum dimension, in Sect.
27 we shall revisit Drinfeld isomorphism and ribbon structures in the framework of tensor
categories. Moreover, we shall study more general structures (coboundary symmetries).
In particular, it will follow from the results of that section that via Tannaka-Krein duality
when A is a discrete weak quasi-Hopf algebra with a strong antipode then Drinfeld element

86 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
is still defined as in Def. 10.6. It will also follow that all the special results of this section
concerning weak Hopf algebras extend to this setting with the same statements, and this
will suffice for the forthcoming developments of our paper considered in Sect. 28, and for
our applications of Sects. 32, 25.
