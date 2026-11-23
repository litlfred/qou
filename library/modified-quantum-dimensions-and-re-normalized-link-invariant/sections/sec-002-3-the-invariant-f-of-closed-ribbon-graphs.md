---
doc_id: modified-quantum-dimensions-and-re-normalized-link-invariant
doc_title: "Modified quantum dimensions and re-normalized link invariants"
section_id: sec-002-3-the-invariant-f-of-closed-ribbon-graphs
section_title: "The invariant F' of closed ribbon graphs"
section_number: 3
pages: 4-6
source_pdf: modified-quantum-dimensions-and-re-normalized-link-invariants.pdf
source_sha256: 5447f6d5f5d6c8d7
toc_source: outline
doc_brief: "Modified quantum dimensions and re-normalized link invariants — 8 sections: Front matter; Introduction; Ribbon Ab-categories"
---
Let C be a strict ribbon Ab-category with ground ring K and the set of objects Ob(C). We
assume everywhere that K is an integral domain with ﬁeld of fractions F.
For any object V of C and any endomorphism f of V ⊗V , set
trL(f) = (dV ⊗IdV ) ◦(IdV ∗⊗f) ◦(b′
V ⊗IdV ) ∈End(V ),
trR(f) = (IdV ⊗d′
V ) ◦(f ⊗IdV ∗) ◦(IdV ⊗bV ) ∈End(V ).
An object V of C is called ambidextrous if trL(f) = trR(f) for all f ∈End(V ⊗V ).
The following lemma gives examples of ambidextrous elements.
Lemma 1. We have two examples of ambidextrous elements.
(1) If J is an object of C such that the braiding cJ,J commutes with any element of End(J ⊗J),
then J is ambidextrous.
(2) If J is a simple object of C such that dimC(J)̸ = 0, then J is ambidextrous.
Proof. (1) Let f ∈End(J ⊗J). We have trR(f) = trL(c−1
J,J ◦f ◦cJ,J). However, cJ,J commutes
with End(J ⊗J) and so c−1
J,J ◦f ◦cJ,J = f.
(2) Let f ∈End(J ⊗J). We have
trL(f) =
trC(f)
dimC(J) IdJ = trR(f).
2
Next we recall the category of C-colored ribbon graphs RibC (for more details see
[Tur94, ch. I]). A morphism f : V1 ⊗· · · ⊗Vn →W1 ⊗· · · ⊗Wm in the category C can be
represented by the following box and arrows:
Wm
...

W1 
f
Vn
...

V1

Such boxes are called coupons. A ribbon graph is formed from several oriented framed edges
colored by objects of C and several coupons colored with morphisms of C. The objects of RibC
are sequences of pairs (V, ϵ), where V ∈Ob(C) and ϵ = ± determines the orientation of the
corresponding edge. The morphism of RibC are isotopy classes of C-colored ribbon graphs and
their formal linear combinations with coeﬃcients in K. From now on we write V for (V, +).
Let F be the usual ribbon functor from RibC to C (see [Tur94]). Let TV (T −
V ) be a C-
colored (1, 1)-ribbon graph whose open string is oriented downward (respectively upward) and
colored with a simple object V of C. Then F(TV ) ∈EndC(V ) = K IdV . Let ⟨TV ⟩∈K be such
that F(TV ) = ⟨TV ⟩IdV .
Modified quantum dimensions and re-normalized link invariants
Let V and V ′ be objects of C such that V ′ is simple and deﬁne the following diagram.
Lemma 2. For all simple objects U, V , W of C such that W is ambidextrous and for any
C-colored ribbon graph T with two inputs and two outputs colored by U, V ,
Proof. Recall that trL(f) = trR(f) for all f ∈End(W ⊗W). This implies that:
(1)
for all C-colored ribbon graphs T ′ with two inputs and two outputs all colored by W.
By deﬁnition we have
(2)
Similarly,
(3)
Then (1) implies that the left-hand sides of the above equations are equal and so the lemma
follows.
2
Applying this lemma to U = V , we obtain that if U, W are simple objects of C such that W
is ambidextrous and S′(U, W)S′(W, U)̸ = 0, then U is also ambidextrous.
If A is a subset of Ob(C), then let LA be the set of closed C-colored ribbon graphs, such that
at least one of the colors of the edges is in A. For a simple ambidextrous object J of C, set
A(J) = {V ∈Ob(C) | V simple and S′(J, V )̸ = 0}.
Fix a non-zero d0 ∈F. For V ∈A(J) deﬁne
dJ(V ) = d0
S′(V, J)
S′(J, V ) ∈F.
N. Geer, B. Patureau-Mirand and V. Turaev
We view dJ(V ) as a modiﬁed quantum dimension of V determined by J. For any U, V ∈A(J),
Lemma 2 implies that
for any T. In particular, when T consists of two vertical intervals colored by U, V ∈A(J),
dJ(U) dimC(V ) = dJ(V ) dimC(U).
This shows that the functions dJ and dimC are proportional to each other. This is especially
interesting when dimC = 0 and dJ̸ = 0, see the examples below.
Theorem 3. Let L ∈LA(J) and V be the color of an edge of L belonging to A(J). Cutting this
edge, we obtain a colored (1, 1)-ribbon graph TV whose closure is L. Then
F ′(L) = dJ(V )⟨TV ⟩∈F
is independent of the choice of the edge to be cut and yields a well-deﬁned invariant of L.
Proof. The theorem follows from Lemma 2 and the deﬁnition of dJ.
2
We call the invariant F ′ the re-normalized Reshetikhin–Turaev link invariant.
Let A = A(J) be the set of objects W of C such that there exists a ﬁnite family of tuples
(Ui, Vi, fi, gi), where Ui ∈A(J), Vi ∈Ob(C) and gi : Ui ⊗Vi →W, fi : W →Ui ⊗Vi satisfying
IdW = P gi ◦fi. Note that A has the property that W ⊗V ∈A for all V ∈Ob(C) and W ∈A.
The map LA →F, L 7→F ′(L) extends to a map LA →F as follows. Let L be a closed C-colored
ribbon graph with one edge colored by W ∈A. Pick a decomposition IdW = P gi ◦fi as above.
Then
IdW = F















X
i
W
gi
Vi

Ui 
fi
W
















.
We deﬁne F ′(L) applying this expansion to the edge of L colored by W and then cutting as
above the edge of the resulting graph labeled by Ui. It is easy to show using Theorem 3 that this
extension is independent of the decomposition of IdW .
