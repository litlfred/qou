---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-003-2-osp12-braid-invariant
section_title: "osp(1|2) braid invariant"
section_number: 2
pages: 3-6
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
2. osp(1|2) braid invariant
In this paper, τ is an indeterminant such that τ4 = 1, and π := τ 2. We also deﬁne the rings
Rτ = R[τ]/(τ4 −1)
Rπ = R[π]/(π2 −1)
Deﬁnition 2.1. Given n ∈
N and d ∈
Zτ[q, q−1], the Temperley-Lieb algebra T Ln(d) is deﬁned as
the
Zτ[q, q−1]-algebra with generators {1, E1, . . . , En−1} with relations.
(1) EiEj = EjEi for |i −j| > 1
(2) EiEi±1Ei = Ei
(3) E2
i = dEi
We can also think of it as a purely even superalgebra.
For this section, set
d := τ −1q + τq−1 ∈
Zτ[q, q−1]
Deﬁnition 2.2. The braid group Bn on n strands is the group
Bn = ⟨σ1, . . . , σn−1 | σiσi+1σi = σi+1σiσi+1, σiσj = σjσi⟩
where |i −j| > 1.
We can represent elements of the braid group and the Tempereley Lieb algebra diagrammatically
σi =
σ−1
i
=
Id :=
Ei :=
We take braids to be oriented upwards, and so remove the arrows from now on.
Deﬁnition 2.3. Given B ∈Bn thought of as an upward oriented braid, we deﬁne the trace closure
Btr as the link formed by closing oﬀthe braid to the right.
For example,
σ =
∈B2
implies
σtr =
.
Deﬁnition 2.4. Given a braid B ∈Bn, deﬁne the bracket polynomial ⟨B⟩∈
Zτ[q, q−1] by ⟨B⟩:= ⟨Btr⟩,
where ⟨Btr⟩is characterized by the following local relations on the braid closure.

=
τ

−q

OR

=
τ 3

−q−1

(2.1)
⟨B1 ⊔B2⟩:= ⟨B1⟩⟨B2⟩

=
d
⟨∅⟩= 1
(2.2)
π
=
−τ
=
WHICH IMPLIES
=
=
(2.3)
Remark 2.5. The second relation of (2.1) follows from the ﬁrst and vice versa since the braid group
relations imply that ⟨σiσ−1
i
⟩= ⟨Id⟩. We include both here for convenience.
4
MARK EBERT
Remark 2.6. The ﬁrst relation of (2.3) clearly implies second relation, and it does hold in the repre-
sentation theoretic perspective. However, we don’t actually need it to deﬁne the bracket polynomial.
We can in fact reduce all closed loops to circles using the second relation. The second relation provides
an easy connection to the Temperley Lieb algebra.
Deﬁnition 2.7. A state z of a braid B to be a choice of resolution
or
at each crossing of B.
We call each resolution of a crossing a 0-resolution or a 1-resolution according to the ﬁgure below.
0−resolution
w♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
1−resolution
'❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
1−resolution
g❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖
0−resolution
7♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
♦
If B has m crossings (which we label), then states of B correspond to sequences z ∈{0, 1}m where
the ith element says how we resolved the ith crossing of B. We can deﬁne the cube of resolutions as
follows. Take the graph with vertices given by sequences z ∈{0, 1}m and edges z →w where w can be
obtained from z by changing exactly one 0 in z to a 1. To each vertex z, associate a diagram B′
z given
by resolving each crossing according to z (remember not to evaluate the bubbles). This is known as
the cube of resolutions, and also is deﬁned for knots and links. When we discuss categoriﬁcation later
in section 4, we will associate a saddle cobordism (B′
z)tr →(B′
w)tr to each edge z →w.
Deﬁnition 2.8. For a braid B ∈Bn and a state z, we deﬁne a polynomial fz(q, τ) ∈
Zτ[q, q−1] and
a diagram Bz ∈T Ln(d) by ﬁrst replacing each crossing of B with the term in (2.1) containing the
resolution speciﬁed by z and then evaluating each closed loop using (2.2) and (2.3). The result is an
element in T Ln(d) given by a diagram in T Ln(d) multiplied by a polynomial in
Zτ[q, q−1]. We call the
resulting diagram Bz, and the resulting polynomial fz(q, τ).
It is not diﬃcult to see that Bz is the diagram obtained by deleting all of the closed loops in B′
z.
We can write fz(q, τ) in the form
fz(q, τ) = ±τ z0qz1dk,
where z0, z1 are determined by (2.1), and k is the number of closed loops that were removed from B′
z
to get Bz.
It is evident from our construction that the following is true.
⟨B⟩=
X
z
fz(q, τ)⟨Btr
z ⟩
(2.4)
where ⟨Btr
z ⟩:= ⟨(Bz)tr⟩is evaluated using (2.2) and (2.3).
In the same way that one renormalizes the Kauﬀman bracket to get the Jones polynomial, we also
renormalize ⟨−⟩to get an invariant.
A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT AND CATEGORIFICATION
5
Deﬁnition 2.9. The writhe of a braid (or link) T is deﬁned by setting
wr


= 1
wr


= −1
wr(T ) =
X
wr(X)
where the sum is over all crossings X in T . We often write this as wr(T ) = n+ −n−, where n+ and
n−denote the number of positive and negative crossings in T respectively.
We are now ready to deﬁne the osp(1|2)-polynomial invariant on a braid T . This will turn out deﬁne
a invariant of oriented links.
Deﬁnition 2.10. The uncolored osp(1|2)-polynomial bJ is deﬁned as a renormalization of the bracket
polynomial 1 .
bJ(T ) = (τ 2q)wr(T )⟨T ⟩
To extend our discussion to oriented links, we recall Alexander’s theorem, which states any oriented
link can be obtained as the trace closure of a braid. It is possible that two diﬀerent braids can have
the same trace closure, so bJ extends to an invariant of oriented links if and only if it is well deﬁned on
isomorphism classes of closures of braids. If this is the case, then if L can be realized as T tr for some
braid T , then bJ(L) = bJ(T tr) = bJ(T ).
We say that bJ preserves the Markov moves if it satisﬁes the conditions M1 and M2 listed below.
M1 bJ(T σ±1
n ) = bJ(T ) for all T ∈Bn
M2 bJ(AB) = bJ(BA) for all A, B ∈Bn
If bJ preserves the Markov moves as above, then Markov’s theorem tells us that bJ is well deﬁned on
isomorphism classes of closures of braids, and is thus an invariant of oriented links. We will now show
that bJ preserves the Markov moves.
Lemma 2.11. bJ satisﬁes M1.
Proof. Assume for the duration of the proof that T ∈Bn. We need to show that bJ(T ) = bJ(T σ±1
n ).
We only show the proof for T σ+1
n , as the proof of the other case is essentially the same.
T σn ∈Bn+1 has the following diagram
. . .
. . .
T
Using (2.1), we see that the trace closure of this diagram is equal to the trace closure of
. . .
. . .
T
=
πqτ
. . .
. . .
T
−πq2
. . .
. . .
T
Hence, bJ(T σn) = (τ 3q(τ 3q + τq−1) −τ 2q2) bJ(T ) = bJ(T ).
□
1This new deﬁnition b
J(−) of the osp(1|2)-polynomial is designed to agree with the uncolored osp(1|2)-polynomial
Jl
−given in [10, Example 3.10]. The main diﬀerence between the two deﬁnitions is the type of skein relation used as
mentioned in the introduction. The skein relation he uses can be derived from the skein relation I use, but not the other
way around.
6
MARK EBERT
Lemma 2.12. bJ satisﬁes M2.
Proof. For A, B ∈Bn we need to show that bJ(AB) = bJ(BA) for any A, B ∈Bn.
Let x be a state of A and y be a state of B. Then we get canonical states xy and yx of AB and
BA respectively. Let ℓAB be the number of loops in AxBy. Then fxy = fxfydℓAB and ⟨(AxBy)tr⟩=
dℓAB⟨((AB)xy)tr⟩by construction. Therefore, fxy⟨((AB)xy)tr⟩= fxfy⟨(AxBy)tr⟩. Similarly, fyx⟨((BA)yx)tr⟩=
fyfx⟨(ByAx)tr⟩.
Therefore, it suﬃces to prove that ⟨(AxBy)tr⟩= ⟨(ByAx)tr⟩for an arbitrary choice of states x
of A and y of B. Since Ax, By ∈T Ln(d), we can use properties of the Temperley Lieb algebra to
prove this without much eﬀort. Let tr′ : T Ln(d) →
Zτ[q, q−1] denote the Markov trace on T Ln(d)
(see [1, Deﬁnition 2.12]). Then, ⟨(AxBy)tr⟩= dntr′(AxBy) by deﬁnition. The Markov trace satisﬁes
tr′(AB) = tr′(BA), hence we have that ⟨(AxBy)tr⟩= ⟨(ByAx)tr⟩for any states x, y. Therefore,
bJ(AB) =
X
xy
fxy⟨((AB)xy)tr⟩=
X
x,y
fxfy⟨(AxBy)tr⟩=
X
x,y
fxfy⟨(ByAx)tr⟩=
X
yx
fyx⟨((BA)yx)tr⟩= bJ(BA)
□
Hence, we have proven the following theorem.
Theorem 2.13. bJ is an invariant of oriented links.
