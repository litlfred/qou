---
doc_id: arxiv-1011.4891v1
doc_title: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold"
section_id: sec-005-6-flat-knots
section_title: "§6. Flat knots"
section_number: null
pages: 13-16
source_pdf: 1011.4891.pdf
source_sha256: c3529df5dd909b5e
toc_source: inferred
doc_brief: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold — A new type of knot"
---
§6. Flat knots
Flat mechanical knots were described in the previous section. Numerous
experiments of the following type were performed with them: the device
was knotted (i.e., given the shape of some planar knot diagram and pressed
against the table top by a pane of glass) and then the glass pane was raised
to the height of approximately 7mm above the table. The device would then
move very rapidly on the surface of the table, with some of its branches sliding
along other ones, almost instantly acquiring what we call its ﬂat mechanical
normal form.
Observation 3. For a small number of crossings in its original position,
the ﬂat mechanical knot acquires a unique ﬂat normal form.
Some such normal forms are shown in Figure 9. The “small number”
here is at least 5. There are reasons to believe that it is at least ten or even
more, but experiments were carried out systematically only for ﬁve crossings
or less, and the total number of experiments was several hundred (rather
than many thousands for spacial mechanical knots).
Figure 9. Some ﬂat normal forms
Note that if the initial position of the ﬂat knot has little loops, then these
14
loops sometimes become incorporated into the normal form (increasing in
size, as for the second normal form in Figure 8), sometimes mutually cancel
each other as in the Whitney trick (see Figure 7).
The physical notion of ﬂat mechanical knot has a mathematical counter-
part: a ﬂat (mathematical ) knot can be deﬁned as the equivalence class of
all knot diagrams under the Reidemeister moves Ω2 and Ω3 (the destruction
and creation of little loops, Ω1, is not allowed). When two knot diagrams are
equivalent in this sense, we will say that they are ﬂat isotopic. Flat isotopy
is a stronger equivalence relation than the usual ambient isotopy relation,
nevertheless we have the following theorem.
Theorem 1. If two ambient isotopic knot diagrams K1 and K2 have the
same Whitney index, then they are ﬂat isotopic.
Proof . By the Reidemeister lemma, there exists a sequence of Reide-
meister moves taking K1 to K2. We will replace this sequence by another
sequence, not involving any Ω1 moves, that nevertheless takes K1 to K2, in
the following way.
If an Ω1 move that destroys a little loop is performed at some point,
we do not perform it, but, instead, tighten the little loop until it becomes
tiny (we call it a kink) and “freeze” it to the part of the diagram where it
is located. During further moves of the diagram, the kink stays frozen to
the diagram and moves rigidly with it as if it were simply a marked point
on the diagram. (Actually, when that part of the diagram participates in
moves where it crosses other parts of the diagram, the kink moves along with
it without changing its shape, but as it does this, tiny Ω2 and Ω3 moves
involving it occur.)
If an Ω1 move that creates a little loop is performed at some point, we do
not perform this move, but carry out the Whitney trick (which only uses Ω2
and Ω3 moves) to create two opposite little loops; one of them plays the role
of the loop created by the Ω1 move, while the other is tightened and becomes
a frozen kink (and we forget about it until the end of the construction).
Proceeding in this way, after a ﬁnite number of Ω2 and Ω3 moves (the old
ones from the original sequence and the new ones – those used to mimic the
Ω1 moves that create new loops and those appearing when the kinks cross
other parts of the knot diagram), we will obtain a knot diagram K′
2 which
is exactly like K3 except that it has a certain number of kinks (little loops)
on it. The knot diagram K′
2 has the same Whitney index as K1 (because
Ω2 and Ω3 moves do not change the Whitney index) and so, by assumption,
15
has the same Whitney index as K2. Thus the little loops on K′
2 destroy each
other and we obtain K2 without doing any Ω1 moves, i.e., by means of a ﬂat
isotopy.
□
Flat knots K have two well-known invariants, the Kauﬀman bracket ⟨K⟩
(see, e.g., [5, p.23-24]) and the Whitney index or winding number w(K) (see
Sec.3 above).
To each ﬂat knot K, one can assign another integer invariant, its twisting
number τ(K), deﬁned as shown in Figure 10: given a knot diagram K, we
ﬁrst transform it into an unknot by appropriate crossing changes (see, e.g.,
[5], Chapter 1), then replace that unknot by a ﬂat ribbon, cut the ribbon and
pull it taut (this is the well known belt trick, see, e.g., [5]); then the number of
twists obtained (with sign speciﬁed via the “left-hand rule”) is, by deﬁnition,
τ(K). As far as I know, this deﬁnition ﬁrst appeared in S.Matveev’s article
[12] (see also [13]) for the particular case of the ﬂat unknot.
Figure 10. Deﬁnition of the twisting number
Theorem 2. Flat knots possess the following three invariants: the Kauﬀ-
man bracket ⟨K⟩, the Whitney index w(K), and the twisting number τ(K).
Together, w(K) and τ(K) constitute a complete system of invariants for ﬂat
unknots.
Proof. The invariance of the Kauﬀman bracket is a classical lemma due
to Kauﬀman (see, e.g., [5], pp.24-25). To prove the invariance of the twisting
number, it suﬃces to check that it does not change under Ω2 and Ω3, but
this is a straightforward veriﬁcation. The invariance of the Whitney index,
16
as well as the fact that together with the twisting number it constitutes a
complete system of invariants for ﬂat unknots, was proved by Matveev in
[12] by an elementary but tedious argument (see also [13]).
□
Of course the algebraic classiﬁcation problem for all ﬂat knots is more
diﬃcult than the same problem for classical (spacial) knots and would require
much stronger invariants (of Vassiliev type?).
