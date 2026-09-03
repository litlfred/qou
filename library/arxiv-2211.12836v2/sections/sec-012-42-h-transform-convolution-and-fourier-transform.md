---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-012-42-h-transform-convolution-and-fourier-transform
section_title: "h-transform, convolution and Fourier transform on Bk,n"
section_number: 4.2
pages: 25-30
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
that Bk,n is an integrable PM-graph and the expression of its eigenbasis, we can deduce several
results from Section 3. In order to do so, we will need several times the following inversion formula
for evaluating SI(ξn(J)) in terms of SJ(ξn(I)).
Lemma 4.4. ForI,J ∈Bk,n,
SJ(ξn(I)) = SJ(ξn(I0))
SI(ξn(I0))SI(ξn(J)).
Moreover,
V (ξn(I)) = exp
((k− 1)iπ
n (⟨I⟩−⟨ I0⟩)
)
V (ξn(I0))SI(ξn(I0)),
where⟨I⟩ =∑k
i=1Ii.
Proof. By deﬁnition of Schur functions as ratios of generalized Vandermonde determinants, for
I∈Bk and⃗ u∈ Rk we have
SI(⃗ u) = aI(⃗ u)
aI0(⃗ u),
where aJ(⃗ u) = det
(
eiulJm
)
1≤l,m≤k for J∈Bk. For I,J ∈Bk,n,
aJ(ξn(I)) = det
(
exp
(2iπ
n (Il− (k− 1)/2)Jm
))
1≤l,m,≤k
= exp
(
(k− 1)iπ
n
( k∑
l=1
Il−
k∑
m=1
Jm
))
det
(
exp
(2iπ
n Il(Jm− (k− 1)/2)
))
1≤l,m,≤k
= exp
((k− 1)iπ
n (⟨I⟩−⟨ J⟩)
)
det
(
exp
(2iπ
n Il(Jm− (k− 1)/2)
))
1≤l,m,≤k
= exp
((k− 1)iπ
n (⟨I⟩−⟨ J⟩)
)
aI(ξn(J)).(14)
Applying the latter formula to the ratio SJ(ξn(I))
SJ(ξn(I0)) yields
SJ(ξn(I))
SJ(ξn(I0)) =aJ(ξn(I))
aI0(ξn(I))
aI0(ξn(I0))
aJ(ξn(I0))
=aI(ξn(J))
aI(ξn(I0))
aI0(ξn(I0))
aI0(ξn(J)) exp
((k− 1)iπ
n (⟨I⟩−⟨ J⟩ +⟨I0⟩−⟨ I⟩ +⟨J⟩−⟨ I0⟩)
)
=SI(ξn(J))
SI(ξn(I0)),
which proves the ﬁrst statement. Then, using (14) with J =I0 yields
V (ξn(I)) =aI0(ξn(I)) = exp
((k− 1)iπ
n (⟨I⟩−⟨ I0⟩
)
aI(ξn(I0))),
and, since SI(ξn(I0)) = aI(ξn(I0))
V (ξn(I0)) ,
V (ξn(I)) = exp
((k− 1)iπ
n (⟨I⟩−⟨ I0⟩)
)
V (ξn(I0))SI(ξn(I0)).
□
Specializing (10) and (13) to I =I0 yields the following Lemma.
26 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Lemma 4.5. The common left and right positive eigenvectors hl,hr of all AI, I∈ Bk,n with the
normalization hl(I0) = 1,
⟨
hl,hr⟩
= 1 are
hl(I) =SI(ξn(I0)), h r(I) =|V (ξn(I0))|
nk ·|V (ξn(I))|,
and the invariant probability measure of Bk,n is
µh(I) = 1
nk|V (ξn(I))|2.
Proof. Remark that with the notation of the statement, we have w(I0) = hl. By (10), (13) and
Lemma 4.3, w(I0) and u(I0) are both left and right eigenvectors of AI for I∈Bk,n with eigenvalue
SI(ξn(I0)). To conclude, we need to prove that w(I0)(I) > 0 for all I∈ Bk,n and hr = w(I0) and
u(I0) = hr. Both assumptions are deduced if we prove that |V (ξn(I0))|SI(ξn(I0)) = |V (ξn(I))|,
since then hl(I) = |V (ξn(I))|
|V (ξn(I0))| > 0 and u(I0)(I) = |V (ξn(I0))|2
nk SI(ξn(I0)) = |V (ξn(I0))|
nk |V (ξn(I))|.
By Lemma 4.4
V (ξn(I0))SI(ξn(I0)) = exp
(
−(k− 1)iπ
n (⟨I⟩−⟨ I0⟩)
)
V (ξn(I)).
Then, using that⟨I0⟩ = k(k−1)
2
exp
(
−(k− 1)iπ
n (⟨I⟩−⟨ I0⟩)
)
V (ξn(I))
= exp

−(k− 1)iπ
n
k∑
j=1
(Ij− (k− 1)/2)

 ∏
1≤l<m≤k
(
e2iπ(Im−(k−1)/2)/n−e2iπ(Il−(k−1)/2)/n
)
=
∏
1≤l<m≤k
e− (Im+Il−(k−1))iπ
n
(
e2iπ(Im−(k−1)/2)/n−e2iπ(Il−(k−1)/2)/n
)
=(2i)k(k−1)/2∏
l<m
sin(π(Im−Il)/n).
Since I is an increasing sequence, ∏
l<m sin(π(Im−Il)/n) > 0. In particular, for I = I0 we get
V (ξn(I0)) =ik(k−1)/2|V (ξn(I0))|. We deduce that
(15) |V (ξn(I0))|SI(ξn(I0)) =|V (ξn(I))|,
and the lemma is deduced. □
As a consequence of the latter lemma, the positive eigenvalue of AI,I ∈Bk,n corresponding to
the eigenvector hr is SI(ξn(I0)). In particular, Lemma 4.3 yields that for all I,J ∈Bk,n
(16) |SI(ξn(J))|≤ SI(ξn(I0)).
Following notation of Section 4, set PI = Ah
I
SI(ξn(I0)). Translating Deﬁnition 3.5 to Bk,n yields the
following convolution product on L2
h(Bk,n).
Deﬁnition 4.6. The convolution product on Bk,n is the map ∗ :L2(Bk,n)⊗L2(Bk,n)→L2(Bk,n)
deﬁned by
x∗y =
∑
I∈Bk,n
µh(I)x(I)PI(y) =
∑
I∈Bk,n
|V (ξn(I))|2
nk x(I)PI(y),
wherePI(y) = 1
hr· AI
SI(ξn(I0))(hr·y) and· denotes the pointwise multiplication.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 27
A h-probability measureµ on Bk,n is a vector µ∈L2(Bk,n) such that
∑
I∈Bk,n
|V (ξn(I))|2
nk µ(I) = 1.
Recall that we denote then by M1(Bk,n) the set of h-probability measures on Bk,n. We also
denote by δI the unique h-probability measure supported at I, namely
(17) δI = nk
|V (ξn(I)|2eI.
The results of Section 3 yield then directly the proof of Proposition 2.1.
Proof of Proposition 2.1. By Proposition 3.6, (L2(Bk,n), +,∗) is a commutative algebra such that
M1(Bk,n)∗M 1(Bk,n)⊂M 1(Bk,n), which proves (1) and (2).
Then, applying Deﬁnition 4.6 to x = eI1
µh(I 1) and y∈L2(Bk,n) and using that µh(I) = |V (I)|2
nk for
I∈Bk,n, we get
eI 1
µh(I1)∗y =PI 1(y) = Ah
λ ,
where the last equality is due to Proposition 4.2 which implies that AI 1 =T (s(1)) =A. Doing the
same with x = eI
µh(I) and y =
eI0
µh(I0) yields
eI
µh(I)∗ eI0
µh(I0) = 1
µh(I0)PI(eI0) = hr(I0)
hr(I)hl(I0)hr(I0)hl(I)eI = eI
µh(I),
where we used that AI(eI0) =eI and hl(I0) = 1. Thus, (3) and (4) are proven. □
Likewise, since Bk,n is an integrable PM-graph, we can deﬁne a Fourier transform as in Section
3.3.
Deﬁnition 4.7. The discrete Fourier transform on Bk,n is the map Φn : L2(Bk,n)→ L2(Bk,n)
deﬁned for x∈L2(Bk,n) by
Φn[x](I) =⟨ ˜w(I),x⟩h =
∑
J∈Bk,n
|V (ξn(J))|·| V (ξn(I0))|
nk SJ(ξn(I))x(J).
Then, Proposition 3.9 directly yields for x1,...,x m∈L2(Bk,n)
(18) Φ n[x1∗···∗ xm] = Φn[x1]··· Φn[xm].
Let us more speciﬁcally study the Fourier transform of a h-probability measure. First, for I,J ∈
Bk,n, we have by Deﬁnition 4.7, (17) and (15),
Φn[δI](J) =|V (ξn(I))|·| V (ξn(I0))|
nk SI(ξn(J))· nk
|V (ξn(I)|2 = SI(ξn(J))
SI(ξn(I0)).
Then, by Deﬁnition 4.6 and (17), a h-probability measure µ∈ L2
h(Bk,n) can be written µ =∑
I∈Bk,naIδI with aI≥ 0 for I∈Bk,n and∑
I∈Bk,naI = 1. Hence, we have
(19) Φ n[µ](J) =
∑
I∈Bk,n
aI
SI(ξn(J))
SI(ξn(I0)).
28 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Example 4.8. For k = 1, B1 = Z, and we can identify B1,n with Z/nZ, and SJ(u) = eiJu for
u∈ R,J ∈ Z. In particular, I0 = 0 and SI0(u) = 1 for u∈ R. For I∈ [0,n [∩Z,|V (ξn(I))| = 1,
and thus
w(I) =
∑
J∈Bk,n
exp(−2iπIJ/n )eJ, u (I) = 1
n
∑
J∈Bk,n
exp(−2iπIJ/n )eJ
so that we recover the usual discrete Fourier vectors. For x∈L2(Bk,n), we then have
Φn[x](I) = 1
n
∑
J∈Z/nZ
exp(2iπIJ/n )x(J),
which is the usual (inverse) discrete Fourier transform. Finally, the map PI is the circulant operator
sending eJ to eJ+I, so that for x,y∈L2(B1,n), the convolution product is
x∗y(J) = 1
n
∑
I∈Z/nZ
x(I)y(J−I),
which is the classical convolution product on Z/nZ. Then, (18) recovers the fact that
Φn(x∗y) = Φn(x)Φn(y).
4.3. Fourier transform on Tk. Let us turn to Tk, the continuous limit object of the sequence
{Bk,n,n≥k}. Recall that the set of continuous k-conﬁgurations on a circle Tk is the subset of Rk
consisting of vectors u = (u1,...,u k) such that
0≤uk≤uk−1≤···≤ u1< 2π.
Before describing the relation with Bk,n, let us describe the Fourier transform on Tk coming from
representations theory of U(k), the Lie group of unitary matrices of rank k. Sending U∈U(k) to
the sequence of arguments of its eigenvalues taken in [0 , 2π[) and sorted in decreasing order yields
a map p : U(k)↦→ Tk. Characters of U(k) are conjugation invariant functions {χI,I ∈ Bk} with
the formula
(20) χI(U) =SI(p(U)) = aI(u1,...,u k)
aI0(u1,...,u k),
where{u1,...,u k} are arguments of eigenvalues of U∈ U(k) and we recall that aI(u1,...,u k) =
det(eiulIm)1≤l,m≤k foru∈ Rk andI∈Bk, where we recall thatBk is the set of increasing sequences
of integers.
By Weyl integration formula, the image of the Haar measure µH on U(k) through the map
p sending a unitary matrix to the decreasing sequence of arguments of its eigenvalues yields a
probability measure on Tk which is continuous with respect to the Lebesgue measure and has
density
dp⋆µH(u1,...,u n) = 1
(2π)k
∏
l<m
⏐⏐eiul−eium
⏐⏐2
= 1
(2π)k|V (⃗ u)|2.
Reciprocally, any probability measure onTk yields a unique probability measurep⋆µ onU(k) which
is invariant by conjugation. Denote by L2
inv(U(k)) the vector space of square integrable functions
on U(k) which are invariant by conjugation. Each element f of L2
inv(U(k)) yields a function ˜f on
L2(Tk,dp⋆µH) by restricting its values to diagonal matrices, and the map f↦→ ˜f is an isomorphism
by Weyl integration formula. By Plancherel theorem, the map
Φ :



L2
inv(U(k),dµH)≃ L2(Tk,dp⋆(µH))→ 𝓁2(Bk)
f ↦→
(∫
Tk
SJ(u) ˜f(u)dp⋆µH(u)
)
J∈Bk
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 29
is an L2-isometry. For c = (c(J))∈𝓁2(Bk), the inverse of Φ at c is given by
Φ−1[c](⃗ u) =
∑
J∈Bk
dJc(J)SJ(⃗ u)
for ⃗ u∈ Tk, where the sum almost-surely converges and dJ = SJ(0,..., 0) is the dimension of the
irreducible representation of U(k) having character χJ =SJ◦p.
The map Φ extends by continuity (in the weak-topology) to a unique map, also denoted Φ and
called the Fourier transform onTk, from the setMf(Tk) of ﬁnite measures onTk to the topological
space of maps from Bk to C with the pointwise convergence. We then have for m∈M f(Tk) and
J∈Bk
(21) Φ[ m](J) = 1
(2π)k
∫
Tk
SJ(⃗ u)|V (⃗ u)|2dm(⃗ u).
As for ﬁnite measures on R or R/(2πZ), the Fourier transform characterizes ﬁnite measures and
vague convergence on Tk. Denote by M1(Tk) the subset of Mf(Tk) consisting in measures m on
Tk such that Φ[m](I0) = 1.
If ν1,ν 2∈M f(U(k)), the set of ﬁnite measures on U(k), the convolution of ν1 with ν2 is the
unique ﬁnite measure ν1∗ν2 such that
∫
U(k)fdν 1∗ν2 =
∫
U(k)×U(k)f(g1g2)dν1(g1)dν2(g2) for all
f∈C0(U(k)). If µ1,µ 2∈M f(Tk), we deﬁne
ν1∗ν2 =p⋆(p⋆(µ1)∗p⋆(µ2)).
Then, the convolution product∗ is commutative onMf(Tk), and
Φ[µ1∗µ2] = Φ[µ1]· Φ[µ2],
where the product on the right-hand side is the pointwise product on M(Bk).
Recall that Bk,n embeds in Tk through the map ξn deﬁned in Section 2.1. By linearity, this map
is extended to a map (also denoted by ξn) from L2(Bk,n) toMf(Tk) with the formula
ξn

 ∑
I∈Bk,n
µ(I)eI

 =
(2π
n
)k ∑
I∈Bk,n
µ(I)δξn(I), µ ∈L2(Bk,n).
A crucial fact for the sequel is that ξn intertwines the Fourier transforms Φn and Φ.
Proposition 4.9. For all µ∈L2(Bk,n) andJ∈Bk such that J1<J k +n. Then, with J(n)∈Bk,n
such that{J(n)
i [n]}1≤i≤k ={Ji[n]}1≤i≤k,
Φ[ξn(µ)](J) =SJ(ξn(I0))Φn[µ](J(n)).
Proof. By linearity, we only have to prove the relation on µ =δI for I∈Bk,n, where δI is deﬁned
in (17). First, (19) and Lemma 4.4 yield
Φn[δI](J(n)) = SI(ξn(J(n)))
SI(ξn(I0)) = SJ (n)(ξn(I))
SJ (n)(ξn(I0)).
On the other hand, since ξn(δI) =
( 2π
n
)k nk
|V (ξn(I))|2δξn(I) = (2π)k
|V (ξn(I))|2δξn(I),
Φ[ξn(δI)](J) = 1
(2π)k
∫
Tk
SJ(⃗ u)|V (⃗ u)|2 (2π)kdδξn(I)
|V (ξn(I))|2 (⃗ u)
=SJ(ξn(I)) =SJ (n)(ξn(I)),
30 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
The last equality is a consequence to the fact that J(n) has the form (Jr + (𝓁 + 1)n,...,J k + (𝓁 +
1)n,J 1 +𝓁n,...,J r−1 +𝓁n) for some 1≤r≤k and𝓁∈ Z and because of the determinantal formula
of SJ and SJ′. The result is then deduced. □
