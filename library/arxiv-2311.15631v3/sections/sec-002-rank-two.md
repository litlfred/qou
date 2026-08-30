---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI"
section_id: sec-002-rank-two
section_title: "Rank two"
section_number: null
pages: 6-11
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI — We classify connected ´ etale algebras A’s in pre-modular fusion categories B with rank(B) ≤"
---
A rank two pre-MFC has two simple objects {1, X}. There are two fusion rings, Z/2Z and
K(Fib). We start from the Z/2Z case.
2.2.1 B ≃ Vecα
Z/ 2Z
The pre-MFCs B’s have two simple objects {1, Xh}. They obey the Z/2Z fusion ring
∀b ∈ B , 1 ⊗ b ∼= b ∼= b ⊗ 1, X ⊗ X ∼= 1,
and have
FPdimB(1) = 1 = FPdim B(X).
Accordingly, the pre-MFCs have
FPdim(B) = 2 .
The quantum dimension dX is a solution of d2
X = 1, and there are two possible values
dX = ±1.
They both have the same categorical dimension
D2(B) = 2 .
The Z/2Z object X can have conformal dimensions
h = 0, 1
4 , 1
2 , 3
4 (mod 1) .
Those with h = 0 , 1/2 mod 1 are anomaly-free ( α = 1), and the others h = 1 /4, 3/4 mod 1
are anomalous ( α = −1). Therefore, for the Z/2Z fusion ring, we have
4(conformal dimension h)×2(quantum dimension dX)×2(categorical dimension D = ±
√
2) = 16
6
pre-MFCs. For a pre-MFC to be unitary, we need dX = 1. Furthermore, for such pre-MFCs
to be modular, we need h = 1
4, 3
4.5 Therefore, there are
2(conformal dimension h) × 1(dX = 1) × 2(categorical dimension D) = 4
unitary MFCs, consistent with [9]. However, we do not assume non-d egeneracy nor (pseudo-
)unitarity. Rather, we search for connected ´ etale algebras in all 16 pre-MFCs simultaneously.
First, since FPdim( B) = 2, an upper bound on ranks of BA’s is
rmax = 2. (2.2)
Fusion categories up to rank two are completely classiﬁed [10], and th ere are only three
fusion categories, Vect C, Vec α
Z/ 2Z, and Fib. The Fibonacci fusion ring has FPdim = 5+
√
5
2 >
FPdim(B), and is ruled out. The other two satisfy three conditions, and rem ain as candidates.
As the third step, we check which fusion categories satisfy axioms. We start from the
candidate Vecα
Z/ 2Z. The fusion category has FPdim = 2, and (1.5) demands FPdim B(A) = 1.
For such an object to be connected, the only candidate is
A ∼= 1. (2.3)
This is the trivial connected ´ etale algebra giving BA ≃ B . Next, we study the rank one
candidate Vect C. The fusion category has FPdim = 1, and (1.5) demands FPdim B(A) = 2.
For such an object to be connected, the only candidate is
A ∼= 1 ⊕ X. (2.4)
The candidate is connected, however, fails to be commutative depe nding on conformal di-
mensions. Let us study when the candidate is commutative. Since X ∗ ∼= X is invertible, we
have [6]
α = F XXX
X = ν2(X)
dX
. (2.5)
The formula (1.16) gives
cX,X ∼= e−2πih X αdXid1 ∼=



id1 (dX, h) = (1 , 0), (−1, 1
2),
−id1 (dX, h) = (1 , 1
2), (−1, 0),
+i · id1 (dX, h) = (1 , 1
4), (−1, 3
4),
−i · id1 (dX, h) = (1 , 3
4), (−1, 1
4).
5A pre-MFC with Xh has S-matrix (in the basis {1, X })
~S =
( 1 dX
dX e−4πih
)
.
7
Therefore, the candidate (2.4) is commutative iﬀ ( dX, h) = (1 , 0), (−1, 1
2) mod 1 for h. In
other words, our pre-MFC B ≃ Vecα
Z/ 2Z can admit nontrivial connected ´ etale algebra if it
is anomaly-free α = 1, and anomalous α = −1 ones are completely anisotropic. The result
has a simple (partial) physical explanation. When the symmetry Z/2Z is anomaly-free, we
can gauge it. Thus, it is expected that there are more algebra obje cts. On the other hand,
if the symmetry is anomalous, it cannot be gauged and there cannot exist a Z/2Z algebra
object. (This is the reason why there are fewer possible values of g round state degeneracies
in anomalous theories compared to anomaly-free theories.)
Note that not all commutative algebras are separable. For A ∼= 1 ⊕ X to be separable, it
should have quantum dimension one. In BA, we have [5]
dBA(c) = dB(c)
dB(A) ,
where dC(c) is the quantum dimension of c as an object of C. When dX = −1, this cannot
be one. Therefore, we conclude
A ∼= 1 ⊕ X (dX, hX) = (1 , 0). (mod 1 for h) (2.6)
To summarize, we arrive
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 2 No
1 ⊕ X for (2.6) VectC 1 No
,
T able 3: Connected ´ etale algebra in rank two pre-MFC B ≃ Vec1
Z/ 2Z
and
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 2 No .
T able 4: Connected ´ etale algebra in rank two pre-MFC B ≃ Vec−1
Z/ 2Z
2.2.2 B ≃ Fib
The pre-MFCs B’s have two simple objects {1, Xh} obeying the Fibonacci fusion ring
∀b ∈ B , 1 ⊗ b ∼= b ∼= b ⊗ 1, X ⊗ X ∼= 1 ⊕ X.
They thus have
FPdimB(1) = 1 , FPdimB(X) = ζ := 1 +
√
5
2 ,
8
and
FPdim(B) = 5 +
√
5
2 ≈ 3.6.
The quantum dimension dX is a solution of d2
X − dX − 1 = 0, and it can take two values
dX = ζ, −ζ −1.
Accordingly, they have categorical dimensions
D2(B) = 5 +
√
5
2 , 5 −
√
5
2 ,
respectively, and modular matrices
~S =
(
1 ζ
ζ −1
)
, T =
(
1
e2πih
)
(dX = ζ),
or
~S =
(
1 −ζ −1
−ζ −1 −1
)
, T =
(
1
e2πih
)
(dX = −ζ −1).
The former has
h = 2
5 , 3
5 (mod 1) ,
and the latter has
h = 1
5 , 4
5 (mod 1) .
Therefore, we have
2(quantum dimension dX) × 2(conformal dimension h) × 2(categorical dimension D(B)) = 8
pre-MFCs. Those with dX = ζ are unitary, and there are four unitary MFCs, consistent with
[9]. We study connected ´ etale algebras in all eight pre-MFCs simultan eously.
First, since FPdim( B) ≈ 3.6, an upper bound on ranks of BA’s is
rmax = 3. (2.7)
Fusion categories up to rank three have been classiﬁed in [10, 11] as suming an existence of
pivotal structure for rank three. There are
1(rank = 1) + 2(rank = 2) + 5(rank = 3) = 8
fusion rings. All but one are free of multiplicity, and they are summar ized in AnyonWiki [12]
based on [13, 14]. The one with multiplicity has fusion ring K(1, 0, 2, 0) in the notation of [11],
9
however, it has Frobenius-Perron dimension 6 FPdim(C) = 6 + 2
√
3 ≈ 9.4, and we can rule
it out at the outset. As in [3], one can easily check there are no one- a nd three-dimensional
NIM-reps. Hence, we are left with rank two BA’s. They have fusion rings 7
FR2, 0
1 , FR2, 0
2 .
In order to search for all rank two BA’s, we solve two-dimensional NIM-reps. We ﬁnd a
unique (up to basis transformations) solution
n1 = 1 2, n X =
(
0 1
1 1
)
.
Let m1, m2 ∈ M be basis. The NIM-rep gives actions
1 ⊲ mj ∼= mj,
X ⊲ m 1 ∼= m2,
X ⊲ m 2 ∼= m1 ⊕ m2,
or monoidal products
F (mj) ∼= F (1 ⊲ mj) ≡ Hom(m, 1 ⊲ mj) ∼= Hom(m, mj),
F (m2) ∼= F (X ⊲ m 1) ≡ Hom(m, X ⊲ m 1) ∼= X ⊗ Hom(m, m1),
F (m1) ⊕ F (m2) ∼= F (X ⊲ m 2) ≡ Hom(m, X ⊲ m 2) ∼= X ⊗ Hom(m, m2).
In order to ﬁnd forms of algebras, we set an ansatz
A ∼= F (m) ∼= a1 ⊕ bX,
with a, b ∈ N. If m ∼= m1, the second monoidal product yields
F (m2) ∼= b1 ⊕ (a + b)X.
6Simple objects {1, X, Y } obey fusion rules
⊗ 1 X Y
1 1 X Y
X 1 ⊕ 2X ⊕ Y X
Y 1
,
and have
FPdimC(1) = 1 = FPdim C(Y ), FPdimC(X) = 1 +
√
3.
7The notation in [12] is the following. A rank r fusion ring with n non-self-dual simple objects is denoted
by FR r,n
i . The subscript i = 1, . . . labels diﬀerent fusion rings with the same r and n.
10
The third monoidal product is automatically satisﬁed. For the candid ate to be connected,
we need a = 1, or A ∼= F (m1) ∼= 1 ⊕ bX. It has FPdim B(A) = 1 + bζ. For this to solve (1.5),
we need b = 0 and fusion ring FR 2, 0
2 . Namely, we only get the trivial connected ´ etale algebra
A ∼= 1 giving BA ≃ B . The other case m ∼= m2 gives the same result.
In conclusion, we arrive
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 2 No .
T able 5: Connected ´ etale algebra in rank two pre-MFC B ≃ Fib
