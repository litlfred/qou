---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-006-41-normal-forms-of-involutive-r-matrices
section_title: "Normal forms of involutive R-matrices"
section_number: 4.1
pages: 15-20
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
Normal forms of involutive R-matrices
Our next aim is to prove that TYB parameterizes the set of all Yang-Baxter characters,
that is, that every (α, β) ∈TYB is realized as the Thoma parameters of some R-matrix.
We will follow a procedure which has some analogy to building general group
representations (of, say, a ﬁnite group) as direct sums of irreducibles. Yang-Baxter
representations are reducible, but decomposing them gives representations which are
no longer of Yang-Baxter form. Conversely, taking direct sums of Yang-Baxter repre-
sentations is not compatible with the Yang-Baxter equation either.
To get around these problems, we introduce a binary operation ⊞on R-matrices
that on the level of the base spaces corresponds to taking direct sums, and respects the
Yang-Baxter equation. Under various names, such operations have been considered
in the literature before [18, 2, 15]. We present here the version that is most useful for
the case at hand.
Deﬁnition 4.1. Let V, W be ﬁnite dimensional Hilbert spaces and let X ∈End(V ⊗V ),
Y ∈End(W ⊗W). We deﬁne X ⊞Y ∈End((V ⊕W) ⊗(V ⊕W)) as
X ⊞Y = X ⊕Y ⊕F
on
(4.1)
(V ⊕W) ⊗(V ⊕W) = (V ⊗V ) ⊕(W ⊗W) ⊕((V ⊗W) ⊕(W ⊗V )).
In other words, X ⊞Y acts as X on V ⊗V , as Y on W ⊗W, and as the ﬂip on the
mixed tensors involving factors from both, V and W. Note that the above deﬁnition
works in the same way for inﬁnite dimensional Hilbert spaces.
15
Before applying this operation to R-matrices, we collect its main properties. In
particular, we note that ⊞behaves well under taking the partial trace
ptr : End(U ⊗U) →End U ,
(4.2)
X 7→(idEnd U ⊗TrU)(X),
(4.3)
where U is any ﬁnite dimensional vector space.
Lemma 4.2. Let V, W be ﬁnite dimensional Hilbert spaces and X ∈End(V ⊗V ),
Y ∈End(W ⊗W).
i) ⊞is commutative and associative up to canonical isomorphism.
ii) If X and Y are unitary (respectively selfadjoint, involutive, invertible), then
X ⊞Y is unitary (respectively selfadjoint, involutive, invertible).
iii) If X commutes with the ﬂip (on V ⊗V ) and Y commutes with the ﬂip (on
W ⊗W), then X ⊞Y commutes with the ﬂip (on (V ⊕W) ⊗(V ⊕W)).
iv) ptr(X ⊞Y ) = (ptr X) ⊕(ptr Y ). In particular, Tr(X ⊞Y ) = Tr X + Tr Y . The
same formula holds for the right partial trace.
Proof. i) The deﬁnition (4.1) is invariant under exchanging (X, V ) with (Y, W), that
is X⊞Y = Y ⊞X. Associativity follows by repeatedly evaluating the deﬁnition. Given
ﬁnite dimensional vectors spaces V 1, . . . , V n and Xi ∈End(V i ⊗V i), i = 1, . . . , n,
one ﬁnds
n
⊞
i=1
Xi = X1 ⊕. . . ⊕Xn ⊕F ,
(4.4)
where on the right hand side, each Xi acts on V i ⊗V i, and F on the orthogonal
complement of L
i(V i ⊗V i) in (L
i V i)⊗2.
ii), iii) These statements follow directly from the facts that F is unitary, self-
adjoint, involutive, invertible, and the ﬂip of (V ⊕W) ⊗(V ⊕W) leaves the three
subspaces in the decomposition (4.1) invariant.
iv) Proving the claimed formula amounts to showing that the partial trace of
FQ vanishes, where Q is the orthogonal projection onto (V ⊗W) ⊕(W ⊗V ). Let
v1, v2 ∈V , and let {wk} be an orthonormal basis of W. Then the right partial trace
satisﬁes ⟨v1, ptr(FQ)v2⟩= P
k⟨v1 ⊗wk, F(v2 ⊗wk)⟩, because Q vanishes on V ⊗V .
But ⟨v1 ⊗wk, F(v2 ⊗wk)⟩= 0 because V and W lie orthogonal to each other. The
argument for the right partial trace is the same.
We now apply ⊞to R-matrices. The following result is known [18, 2, 15]. But
since no proof seems to be available in the literature, we state it here with a proof.
Proposition 4.3. Let R ∈R(V ), ˜R ∈R( ˜V ). Then R ⊞˜R ∈R(V ⊕˜V ).
Proof. Invertibility of R ⊞˜R follows from the preceding lemma and the invertibility
of R, ˜R. The main point is to check that ˆR := R ⊞˜R solves the Yang-Baxter equation
on (V ⊕˜V )⊗3.
This space is the direct sum of eight orthogonal subspaces V1 ⊗V2 ⊗V3, where
each Vi is either V or ˜V . Observe that both of the operators ˆR1 ˆR2 ˆR1 and ˆR2 ˆR1 ˆR2
decompose into direct sums of their restrictions to V ⊗3, V ⊗˜V ⊗V , (V ⊗V ⊗˜V ) ⊕
( ˜V ⊗V ⊗V ), ˜V ⊗3, ˜V ⊗V ⊗˜V and ( ˜V ⊗˜V ⊗V ) ⊕(V ⊗˜V ⊗˜V ).
16
By symmetry in V, ˜V and R, ˜R it suﬃces to show that ˆR1 ˆR2 ˆR1 and ˆR2 ˆR1 ˆR2
coincide on the ﬁrst three subspaces in the list. Since R ∈R(V ), this is true for V ⊗3.
Inserting the deﬁnition of ˆR, one ﬁnds that on V ⊗˜V ⊗V , ˆR1 ˆR2 ˆR1 acts as F1R2F1,
while ˆR2 ˆR1 ˆR2 acts as F2R1F2. These two operators coincide with the one acting as
R on the ﬁrst and third tensor factors.
Let W := (V ⊗V ⊗˜V ) ⊕( ˜V ⊗V ⊗V ). The restrictions of both sides of the Yang-
Baxter equation evaluate to ˆR1 ˆR2 ˆR1|W = (F1F2R1 ⊕R1F2F1)|W and ˆR2 ˆR1 ˆR2|W =
(R2F1F2⊕F2F1R2)|W . The operator F1F2 coincides with the tensor ﬂip on (V ⊗V )⊗˜V .
This implies F1F2R1 = R2F1F2. Likewise F2F1 is the tensor ﬂip on ˜V ⊗(V ⊗V ) and
we have F2F1R2 = R1F2F1. Therefore ˆR1 ˆR2 ˆR1|W = ˆR2 ˆR1 ˆR2|W , which ﬁnishes the
proof.
By Lemma 4.2 ii), ⊞preserves involutivity, and thus also induces a binary opera-
tion on R0 ⊂R.
It is clear that variants of this operation are possible: A trivial change would be
to use −F instead of F in the deﬁnition of ⊞, but also more substantial variations
exist [15]. However, all these variations lead to R-matrices that are equivalent in the
sense of Def. 1.1.
For characterizing equivalence classes of R-matrices, we next describe how ⊞acts
on the Yang-Baxter characters of S∞and their Thoma parameters.
Proposition 4.4. Let R, ˜R ∈R0 have dimensions d, ˜d.
i) The characters of R, ˜R, and R ⊞˜R are related by (cn an n-cycle, n ≥2)
χR⊞˜R(cn) =
dn
(d + ˜d)n χR(cn) +
˜dn
(d + ˜d)n χ ˜R(cn) .
(4.5)
ii) Let (α, β) and (˜α, ˜β) be the Thoma parameters of R and ˜R, respectively. Then
the Thoma parameters of R ⊞˜R are the non-increasing arrangements of
{ˆαi}i = {
d
d+ ˜d αk,
˜d
d+ ˜d ˜αl, : k, l ∈N} ,
{ˆβi}i = {
d
d+ ˜d βk,
˜d
d+ ˜d ˜βl, : k, l ∈N} .
(4.6)
Proof. i) We denote the base spaces of R and ˜R by V+ and V−, respectively, and write
ˆR := R ⊞˜R and ˆV := V+ ⊕V−. Noting that the dimension of ˆV is d + ˜d, equation
(4.5) is equivalent to
Tr ˆV ⊗n( ˆR1 · · · ˆRn−1) = TrV ⊗n
+ (R1 · · · Rn−1) + TrV ⊗n
−( ˜R1 · · · ˜Rn−1) .
(4.7)
The trace on the left hand side is taken over ˆV ⊗n = L
ε1,...,εn(Vε1 ⊗. . . ⊗Vεn), where
the sum runs over εi = ±, i = 1, . . . , n. We claim that
( ˆR1 · · · ˆRn−1)Vε1 ⊗. . . ⊗Vεn̸ ⊥Vε1 ⊗. . . ⊗Vεn ⇒ε1 = . . . = εn .
(4.8)
Note that (4.8) implies (4.7): If (4.8) holds, then the trace over ˆV ⊗n simpliﬁes to the
sum of the trace over V ⊗n
+
and that over V ⊗n
−. As ˆR acts as R and ˜R on V+ ⊗V+ and
V−⊗V−, respectively, (4.7) then follows.
To show (4.8), we consider the position of the image ( ˆR1 · · · ˆRn−1)Vε1 ⊗. . . ⊗Vεn
relative to Vε1 ⊗. . . ⊗Vεn for given ε1, . . . , εn = ±. Assume that εn−1̸ = εn. Then the
rightmost factor ˆRn−1, acting non-trivially only on Vεn−1 ⊗Vεn, simpliﬁes to the ﬂip by
17
deﬁnition of ˆR = R⊞˜R. As all other factors ˆR1 · · · ˆRn−2 act trivially on the last tensor
factor Vεn, this implies ( ˆR1 · · · ˆRn−1)Vε1 ⊗. . .⊗Vεn ⊂ˆV ⊗n−1 ⊗Vεn−1 ⊥Vε1 ⊗. . .⊗Vεn.
Hence the non-orthogonality assumption in (4.8) implies εn−1 = εn.
We next assume εn−2̸ = εn−1 = εn. In this situation, the rightmost factor ˆRn−1
maps the product of the last two tensor factors Vεn ⊗Vεn onto itself, so that we are left
with the same situation as before, but with the number of tensor factors reduced by
one. Inductively, we conclude that the non-orthogonality assumption in (4.8) implies
ε1 = . . . = εn.
ii) Deﬁne parameters ˆαi, ˆβj by (4.6), ordered non-increasingly. Then 0 ≤ˆαi, ˆβj ≤
1, and for any n ∈N,
X
i
ˆαn
i + (−1)n+1 X
j
ˆβn
j =

d
d + ˜d
n

X
i
αn
i + (−1)n+1 X
j
βn
j


+
 
˜d
d + ˜d
!n 
X
i
˜αn
i + (−1)n+1 X
j
˜βn
j

.
Since (α, β), (˜α, ˜β) ∈T, we have P
i αi + P
j βj ≤1 and P
i ˜αi + P
j ˜βj ≤1, and
therefore P
i ˆαi + P
j ˆβj ≤1. This shows that (ˆα, ˆβ) ∈T. In terms of characters, the
above equation reads, n ∈N,
X
i
ˆαn
i + (−1)n+1 X
j
ˆβn
j =
dn
(d + ˜d)n χR(cn) +
˜dn
(d + ˜d)n χ ˜R(cn) ,
and by part i) and the uniqueness of the Thoma parameters of an extremal character,
identiﬁes (ˆα, ˆβ) as the Thoma parameters of χ ˆR.
By construction, ⊞maps pairs of parameters in TYB into TYB, preserving the
three properties of TYB (Def. 3.6). But given d, ˜d > 0, (4.5) also makes sense as an
operation on general extremal characters of S∞. We do not investigate this observation
any further here.
After these preparations, we come to the deﬁnition of special normal form R-
matrices as ⊞-sums of identities and negative identities.
We will write 1a for the
identity on a vector space of dimension a2, i.e. 1a ∈R0(Ca).
Deﬁnition 4.5. Let n, m ∈N0 with n + m ≥1, d+ ∈Nn and d−∈Nm. The normal
form R-matrix N with dimensions d+, d−is
N := 1d+
1 ⊞. . . ⊞1d+
n ⊞(−1d−
1 ) ⊞. . . ⊞(−1d−
m) .
(4.9)
Any R-matrix of the type (4.9) will be called normal form R-matrix. Note that in
view of Prop. 4.3, N is indeed an involutive R-matrix. We emphasize that N is not
simply a multiple of the identity: For example, 11 ⊞11 = F is the ﬂip of dimension 2.
Lemma 4.6. Let N ∈R0 be the normal form R-matrix with dimensions d+ ∈
Nn, d−∈Nm. Then N has dimension d = P
i d+
i +P
j d−
j , and the Thoma parameters
of χN are
αi = d+
i
d ,
i = 1, . . . , n,
βj =
d−
j
d ,
j = 1, . . . , m.
(4.10)
18
Proof. Recall that the identity 1 ∈R0(V ) has α1 = 1 as its only non-vanishing Thoma
parameter, and the negative identity −1 ∈R0(V ) has β1 = 1 as its only non-vanishing
Thoma parameter, independently of the dimension of V . From this observation and
the fact that ⊞adds dimensions, one can easily compute dimension and the Thoma
parameters of N (4.9) by iterating Prop. 4.4 ii), with the claimed result for d and
α = d+/d and β = d−/d.
In Thm. 3.7 we had proven that the Thoma parameters of every Yang-Baxter
character lie in TYB.
Lemma 4.6 now implies the converse, ﬁnishing the proof of
Thm. III from the Introduction.
Theorem 4.7. The Yang-Baxter characters of S∞are in one to one correspondence
with TYB (Def. 3.6) via Thoma’s formula (2.6).
Proof. Let (α, β) ∈TYB. All that remains to be shown is that there is an R-matrix
with these Thoma parameters. There exists d ∈N such that all dαi, dβj are integer
because the αi, βj are rational and ﬁnite in number (Def. 3.6).
The character of
the normal form R-matrix N with dimensions d+
i = dαi, d−
j = dβj then has Thoma
parameters (α, β) by Lemma 4.6 and the fact that the Thoma parameters sum to 1
(Cor. 2.6).
This result also justiﬁes the notation TYB as the Yang-Baxter simplex, consisting
of all Thoma parameters of Yang-Baxter characters. Thoma’s simplex T, viewed as
a subset of [0, 1]∞× [0, 1]∞, where [0, 1]∞is equipped with the product topology, is
a compact metrizable space. It is noteworthy to point out that TYB ⊂T is a dense
subset, cf. [24, Ch. 3].
At this stage, we know that for every R-matrix R ∈R0, there exists a normal
form R-matrix N such that χR = χN.
Furthermore, N can be chosen in such a
way that R ∼N, i.e. such that also the dimensions of R and N coincide. To see
this, we just need to recall that the rescaled Thoma parameters dαi, dβi of R are
integers summing to d (Thm. 3.7), so that the normal form R-matrix with dimensions
d+
i = dαi, d−
i = dβi has the same character and the same dimension as R.
We brieﬂy mention further properties of normal form R-matrices: Any normal form
R-matrix N commutes with the ﬂip because of Lemma 4.2 iii). Thus any involutive
R-matrix is equivalent to an R-matrix which commutes with the ﬂip, though this need
not be true for an R-matrix not in normal form.
Furthermore, one can check that any normal form R-matrix N satisﬁes
N(1 ⊗ptr N)N = ptr N ⊗1 .
(4.11)
By Thm. 3.4, a normal form R-matrix N (of dimension d) satisﬁes, as any involu-
tive R-matrix,
χN(cn) = d−n TrV ⊗n(N1 · · · Nn−1) = d−n TrV ((ptr N)n−1),
(4.12)
where cn is an n-cycle, n ≥2.
With the exchange relation (4.11), it is a matter
of explicit calculation to prove (4.12) directly for normal form R-matrices, without
relying on subfactor theory.
19
