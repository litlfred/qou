---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-029-motivic-weights-and-stability-data-on-motivic-qu
section_title: "Motivic weights and stability data on motivic quantum tori"
section_number: null
pages: 92-95
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
tum tori
LetC be a 3-dimensional ind-constructible Calabi-Yau category over a ﬁeld
of characteristic zero (see Section 3.3). In this section we are going to de-
ﬁne motivic Donaldson-Thomas invariants associated with a constructible
stability condition and an orientation data on C.
Step 1 .
Let us deﬁne the ring
Dµ =Mµ(Spec(k))[L−1, L1/2, ([GL(n)]−1)n/greaterorequalslant1] ,
where the ring Mµ(Spec(k)) was deﬁned in 4.3, and L = [A1
k] is the motive
of the aﬃne line. The element L1/2 is a formal symbol satisfying the equation
(L1/2)2 = L. Instead of inverting motives
[GL(n)] = ( Ln− 1)(Ln− L)... (Ln− Ln−1)
of all general linear groups we can invert motives of all proj ective spaces
[Pn] = Ln+1− 1
L− 1 .
We also will consider the ring Dµ of equivalence classes of functions from
Dµ by the equivalence relation deﬁned in Section 4.5. The ring Dµ will play
the role of the universal coeﬃcient ring where motivic Donal dson-Thomas
invariants take value.
Step 2 .
We deﬁne an algebra Mµ(Ob(C)) associated with C which will contain
certain canonical element called the motivic weight. First , we deﬁne
Mµ(Ob(C)) :=
∏
i
MGL(Ni),µ(Yi)[L−1, L1/2] ,
where (Yi,GL (Ni))i∈I is a decomposition of the stack of objects of C as at
the end of 3.2. Algebra Mµ(Ob(C)) is obtained from it by passing to the
equivalence classes in the sense of Section 4.5.
For any GL(Ni)-invariant constructible set Z⊂ Yi for some i∈ I, we
have aMµ(Spec(k))[L−1, L1/2]-linear map
∫
Z
:Mµ(Ob(C))→Dµ
92
which is the µ-equivariant version of integral over stack ( Z,GL (Ni)) (see
4.2) of the restriction to Z. Explicitly, if f|Yi is represented by a µ×GL(Ni)-
equivariant map X→Yi then
∫
Z
f = [X×YiZ]/[GL(Ni)]∈Dµ
where [X×YiZ] is interpreted a constructible set with µ-action. By additivity
we extend the integral to the case whenZ is a ﬁnite union of GL(Ni)-invariant
constructible set Zi⊂Yi for diﬀerent i∈I.
Step 3 .
Now we are going to deﬁne the motivic weight. Recall that for a nyE∈
Ob(C)(k) we have deﬁned the potential Wmin
E which is a formal power series
in α∈ Ext1(E,E ) which starts with cubic terms. We denote by
MF (E) := MF 0(Wmin
E )
the motivic Milnor ﬁber of Wmin
E at 0 ∈ Ext1(E,E ). Then the assign-
mentE↦→MF (E) can be interpreted as the value of some function MF ∈
Mµ(Ob(C)).
Let us choose an orientation data
√
D forC. Recall that in Section 5.2
we deﬁned the element h∈ J2(C) represented by the equivariant super line
bundle
√
D⊗D −1
≤1 with trivialized tensor square. For a representative of h
given by a pair ( V,Q ) we have I(h) = (1−MF 0(Q))L− 1
2 rkQ. Let us choose
such a representative.
Deﬁnition 17 The motivic weight w∈M µ(Ob(C)) is the function deﬁned
on objects by the formula
w(E) = L
1
2
P
i≤1(−1)i dim Exti(E,E )(1−MF (E))(1−MF 0(QE))L− 1
2 rkQE .
The image w∈Mµ(Ob(C)) does not depend on the choice of a represen-
tative of h and is equal to
w(E) = L
1
2
P
i≤1(−1)i dim Exti(E,E )(1−MF (E))I(h(E)) ,
where h(E) is the value of the obstruction h at the point E.
Step 4 .
Let us now ﬁx the following data:
93
• a triple (Γ ,⟨•,•⟩,Q ) consisting of a free abelian group Γ of ﬁnite rank
endowed with a skew-symmetric bilinear form ⟨•,•⟩: Γ ⊗ Γ → Z, and
a quadratic form Q on Γ R = Γ ⊗ R;
• an ind-constructible, Gal( k/k)-equivariant homomorphism
clk :K0(C(k))→ Γ
compatible with the Euler form and the skew-symmetric bilin ear form;
• a constructible stability structure σ∈Stab(C, cl) compatible with the
quadratic form Q in the sense that Q| KerZ < 0 and Q(clk(E)) /greaterorequalslant0 for
E∈C ss(k).
In the next section we are going to deﬁne a homomorphism from t he
motivic Hall algebra to the associative unital algebra call ed motivic quantum
torus. The latter is deﬁned in the following way.
For any commutative unital ring C which contains an invertible symbol
L1/2 we introduce a C-linear associative algebra
RΓ,C :=⊕γ∈ΓC· ˆeγ
where the generators ˆeγ,γ ∈ Γ satisfy the relations
ˆeγ1 ˆeγ2 = L
1
2⟨γ1,γ2⟩ˆeγ1+γ2, ˆe0 = 1 .
We will call it the quantum torus associated with Γ and C.
For any strict sector V⊂ R2 we deﬁne
RV,C :=
∏
γ∈Γ∩C0(V,Z,Q)
C· ˆeγ
and call it the quantum torus associated with V . Here we introduce a nota-
tion which will be used later:
C0(V,Z,Q ) := C(V,Z,Q )∪{ 0}
where the cone C(V,Z,Q ) was deﬁned in 2.2. Algebra RV,C is the natural
completion of the subalgebra RV,C∩R Γ,C⊂R Γ,C.
Let us choose as C the ring Dµ. We denote RΓ :=RΓ,Dµ the correspond-
ing quantum torus and call it the motivic quantum torus associated with Γ.
Similarly, we have motivic quantum tori RV associated with strict sectors V .
94
Step 5 .
We deﬁne an element Amot
V ∈R V :=RV,
Dµ in the following way. First,
we ﬁx a branch of the function Log z, where z ∈ V (the result will not
depend on the choice of the branch). Recall the category CV,Log⊂C (see
Section 3.4). It follows from our assumptions that for any γ ∈ Γ the set
CV,γ ={E∈Ob(CV,Log)| cl(E) = γ} is constructible.
Finally, we deﬁne the desired element
Amot
V =
∑
γ
(∫
CV,γ
w
)
· ˆeγ .
The element Amot
V in fact depends only on
w.
Informally, one can write
Amot
V =
∑
E∈Iso(CV, Log)
w(E)
[Aut(E)] ˆecl(E) = 1 +···∈R V,
where Iso(CV,Log) denotes the set of isomorphism classes of objects of the
categoryCV,Log.
Theorem 7 Assuming the integral identity, the collection of elements (Amot
V )
satisﬁes the Factorization Property: if a strict sector V is decomposed into a
disjoint union V =V1⊔V2 (in the clockwise order) then
Amot
V =Amot
V1 Amot
V2 .
Moreover we have a local homeomorphism Stab(C)→Stab
(
RΓ,
Dµ
)
.
This theorem follows immediately from the statement of Prop osition 11
(see 6.1) about the elements AHall
V , and the Theorem 8 from the next section.
