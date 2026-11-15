---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-012-invariance-under-choice-of-representatives
section_title: "Invariance under Choice of Representatives"
section_number: null
pages: 62-67
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
Invariance under Choice of Representatives
To deﬁne the partition function ZD(M; T ), for each coloring F = (g, f), we chose
arbitrarily a representative fβ for the triangle color f(β), β ∈T 2. In the following,
we show that Tr( N
σ∈T 4 Zϵ(σ)
F
(σ)) is independent on the choice of representatives, and thus
ZD(M; T ) is also independent on the choice of representatives by Deﬁnition 3.1.3.
Let φA : A
∼
−→A′, φB : B
∼
−→B′ be isomorphisms in D.
Denote by T φB
φA the
following linear isomorphism:
T φB
φA : Hom(A, B)
∼
−→Hom(A′, B′)
φB
A 7−→φB ◦φB
A ◦φA.
53
Section 4.1
Invariance under Choice of Representatives
That is, the diagram in Diagram 4.1 commutes.
B
B′
A
A′
φB
φB
A
φA
T φB
φA (φB
A)
(4.1)
The isomorphism T φB
φA satisﬁes functorial properties, namely,
1. If φC : C
∼
−→C′, then T φC
φB (φC
B) ◦T φB
φA (φB
A) = T φC
φA (φC
B ◦φB
A).
2. T φA
φA (IdA) = IdA′.
Lemma 4.1.1 The isomorphism T φB
φA preserves the pairing, i.e.,
⟨φA
B, φB
A⟩= ⟨T φA
φB (φA
B), T φB
φA (φB
A)⟩.
For the rest of the section, we ﬁx a coloring F = (g, f). For each 2-simplex (ijk) ∈T 2,
assume we have arbitrarily chosen two representatives of f(ijk) denoted by ijk and ijk′,
respectively. To distinguish these two choices, we attach an apostrophe to all quantities
related to the second the choice, e.g., V +
F (0123)′, Z−
F (01234)′, etc.
For each β = (ijk) ∈T 2, choose any isomorphism φijk : ijk −→ijk′. If τ = (0123) ∈
T 3, let φ−τ, φ+τ be the isomorphisms deﬁned below.
φ−τ := φ023 ⊗
(φ012)
23
: 023 ⊗
012
23
∼
−→023′ ⊗
012′
23
φ+τ := φ013 ⊗φ123 : 013 ⊗123
∼
−→013′ ⊗123′
Then we have the isomorphisms T φ+τ
φ−τ
: V +
F (τ) −→V +
F (τ)′, T φ−τ
φ+τ
: V −
F (τ) −→
V −
F (τ)′. See Diagram 4.2. When it is clear from the context, we will drop the sub-
54
Section 4.1
Invariance under Choice of Representatives
script/superscript, and simply write T φ+τ
φ−τ as T.
013 ⊗123
013′ ⊗123′
023 ⊗
012
23
023′ ⊗
012′
23
φ+τ
φ
φ−τ
T
φ+τ
φ−τ (φ)
(4.2)
Lemma 4.1.2 For any 4-simplex σ = (01234) ∈T 4, Diagram 4.3 and 4.4 both commute.
V +
F (0234) ⊗V +
F (0124) ⊗V −
F (1234) ⊗V −
F (0134) ⊗V −
F (0123)
C
V +
F (0234)′ ⊗V +
F (0124)′ ⊗V −
F (1234)′ ⊗V −
F (0134)′ ⊗V −
F (0123)′
˜Z+
F (01234)
T⊗T⊗T⊗T⊗T
˜Z+
F (01234)
(4.3)
V −
F (0234) ⊗V −
F (0124) ⊗V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123)
C
V −
F (0234)′ ⊗V −
F (0124)′ ⊗V +
F (1234)′ ⊗V +
F (0134)′ ⊗V +
F (0123)′
˜Z−
F (01234)
T⊗T⊗T⊗T⊗T
˜Z−
F (01234)′
(4.4)
Proof:
We only prove the case for Diagram 4.3. The other case can be proved in
the same way. Let φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4 be in the domain of ˜Z+
F (01234). Consider the
following diagram, where it is not hard to see that the the two maps on the sides of the
55
Section 4.1
Invariance under Choice of Representatives
horizontal arrows represent identical maps.
034 ⊗
023
34
⊗
012
34.23
034′ ⊗
023′
34
⊗
012′
34.23
034 ⊗
013
34
⊗
123
34
034′ ⊗
013′
34
⊗
123′
34
014 ⊗134 ⊗
123
34
014′ ⊗134′ ⊗
123′
34
014 ⊗124 ⊗234
014′ ⊗124′ ⊗234′
024 ⊗
012
24
⊗234
024′ ⊗
012′
24
⊗234′
024 ⊗234 ⊗
012
34.23
024′ ⊗234′ ⊗
012′
34.23
034 ⊗
023
34
⊗
012
34.23
034′ ⊗
023′
34
⊗
012′
34.23
φ−0234⊗
(φ012)
34.23
φ034⊗
(φ−0123)
34
φ−0134⊗
(φ123)
34
φ034⊗
(φ+0123)
34
Id⊗
φ4
34
Id⊗
T(φ4)
34
φ014⊗φ−1234
φ+0134⊗
(φ123)
34
φ3⊗Id
T(φ3)⊗Id
φ+0124⊗φ234
φ014⊗φ+1234
Id⊗φ2
Id⊗T(φ2)
φ−0124⊗φ234
φ024⊗
(
(φ012)
34.23
)
24.23.34
⊗φ234
φ1⊗Id
T(φ1)⊗Id
φ+0234⊗
(φ012)
34.23
φ024⊗φ234⊗
(φ012)
34.23
Id⊗c234,
012
34.23
Id⊗c
234′,
012′
34.23
φ−0234⊗
(φ012)
34.23
φ0⊗Id
T(φ0)⊗Id
(4.5)
The second square diagram commutes by the naturality of the G-crossed braiding. All
other square diagrams commute by Diagram 4.2. Thus, the whole diagram commutes.
Denote the composition of the vertical maps on the left (resp. right) side by L (resp.
R), then ˜Z+
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4) = Tr(L),
˜Z+
F (01234)′(T(φ0) ⊗T(φ1) ⊗
T(φ2) ⊗T(φ3) ⊗T(φ4)) = Tr(R). Since L, R are conjugate by the above diagram, thus
Tr(L) = Tr(R) and we have ˜Z+
F (01234) = ˜Z+
F (01234)′(T ⊗5).
Proposition 4.1.3 For any σ = (01234) ∈T 4, Zϵ(σ)
F
(σ) commutes with T. More pre-
56
Section 4.1
Invariance under Choice of Representatives
cisely, the following diagrams commute.
V +
F (0234) ⊗V +
F (0124)
V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123)
V +
F (0234)′ ⊗V +
F (0124)′
V +
F (1234)′ ⊗V +
F (0134)′ ⊗V +
F (0123)′
Z+
F (01234)
T⊗T
T⊗T⊗T
Z+
F (01234)′
(4.6)
V +
F (0234) ⊗V +
F (0124)
V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123)
V +
F (0234)′ ⊗V +
F (0124)′
V +
F (1234)′ ⊗V +
F (0134)′ ⊗V +
F (0123)′
T⊗T
T⊗T⊗T
Z−
F (01234)
Z−
F (01234)′
(4.7)
Proof:
Again we only prove the case of Diagram 4.6.
Let φ0⊗φ1 ∈V +
F (0234)⊗V +
F (0124), φ2⊗φ3⊗φ4 ∈V +
F (1234)⊗V +
F (0134)⊗V +
F (0123),
then
⟨(T ⊗T ⊗T) ◦Z+
F (01234)(φ0 ⊗φ1), (T ⊗T ⊗T)(φ2 ⊗φ3 ⊗φ4)⟩
=⟨Z+
F (01234)(φ0 ⊗φ1), φ2 ⊗φ3 ⊗φ4⟩
= ˜Z+
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4)
(4.8)
⟨Z+
F (01234)′ ◦(T ⊗T)(φ0 ⊗φ1), (T ⊗T ⊗T)(φ2 ⊗φ3 ⊗φ4)⟩
= ˜Z+
F (01234)′(T(φ0) ⊗T(φ1) ⊗T(φ2) ⊗T(φ3) ⊗T(φ4))
= ˜Z+
F (01234)′ ◦(T ⊗T ⊗T ⊗T ⊗T)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4)
= ˜Z+
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4)
(4.9)
The ﬁrst “= ” in Equation 4.8 is by Lemma 4.1.1, and the third “= ” in Equation 4.9 is
by Lemma 4.1.2.
Since the equalities in Equation 4.8 and 4.9 hold for any φi, i = 0, 1, 2, 3, 4.
this
57
Section 4.2
