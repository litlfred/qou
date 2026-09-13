---
doc_id: arxiv-1011.4891v1
doc_title: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold"
section_id: sec-004-5-nonuniqueness-of-normal-forms
section_title: "Nonuniqueness of normal forms"
section_number: 5
pages: 12-17
source_pdf: 1011.4891.pdf
source_sha256: c3529df5dd909b5e
doc_brief: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold — A new type of knot"
---
Experimenting with our mechanical device (of diameter to length ratio
s =d/L = 0.004), we were unable to ﬁnd any knots that have more than one
mechanical normal form, and we claim that no such knots (with 7 crossings
or less) exist. However, we believe that uniqueness of mechanical normal
forms holds only for a small number of crossing points (less than 30, less
than 20?). More speciﬁcally, having in mind idealized mechanical models
with tiny values of s =d/L, we conjecture the following.
Conjecture 1. For any n0 > 0, there exists a suﬃciently small s >0
such that the unknot has an s-mechanical normal form with n>n 0 crossing
points.
Recall that for M¨ obius energy, the unknot has only one normal form
(energy minimum), namely the round circle [3].
Conjecture 2. For any suﬃciently large n0 > 0, there exists a positive
s and a nontrivial knot with crossing number n greater than n0 which has
more than one s-normal form.
Examples justifying both of these two conjectures can be constructed by
the same method: it can be shown that certain diﬀerent braids have the same
closure, but the isotopy equivalence of these closures involves Markov moves
that increase as well as decrease the length of the braid, whereas our device
can only do the simplifying Markov moves.
In order to construct such examples, and verify their validity, we need
to be able to work with highly idealized mechanical models with tiny values
of the parameter s, and this can only be done by computer simulation after
an appropriate energy functional (imitating the resilience of our device) has
been found.
13
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
part: a ﬂat (mathematical) knot can be deﬁned as the equivalence class of
all knot diagrams under the Reidemeister moves Ω 2 and Ω3 (the destruction
and creation of little loops, Ω 1, is not allowed). When two knot diagrams are
equivalent in this sense, we will say that they are ﬂat isotopic. Flat isotopy
is a stronger equivalence relation than the usual ambient isotopy relation,
nevertheless we have the following theorem.
Theorem 1. If two ambient isotopic knot diagrams K1 andK2 have the
same Whitney index, then they are ﬂat isotopic.
Proof . By the Reidemeister lemma, there exists a sequence of Reide-
meister moves taking K1 to K2. We will replace this sequence by another
sequence, not involving any Ω 1 moves, that nevertheless takes K1 to K2, in
the following way.
If an Ω 1 move that destroys a little loop is performed at some point,
we do not perform it, but, instead, tighten the little loop until it becomes
tiny (we call it a kink) and “freeze” it to the part of the diagram where it
is located. During further moves of the diagram, the kink stays frozen to
the diagram and moves rigidly with it as if it were simply a marked point
on the diagram. (Actually, when that part of the diagram participates in
moves where it crosses other parts of the diagram, the kink moves along with
it without changing its shape, but as it does this, tiny Ω 2 and Ω 3 moves
involving it occur.)
If an Ω1 move that creates a little loop is performed at some point, we do
not perform this move, but carry out the Whitney trick (which only uses Ω 2
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
other and we obtain K2 without doing any Ω 1 moves, i.e., by means of a ﬂat
isotopy. □
Flat knots K have two well-known invariants, the Kauﬀman bracket⟨K⟩
(see, e.g., [5, p.23-24]) and the Whitney index or winding number w(K) (see
Sec.3 above).
To each ﬂat knotK, one can assign another integer invariant, its twisting
number τ(K), deﬁned as shown in Figure 10: given a knot diagram K, we
ﬁrst transform it into an unknot by appropriate crossing changes (see, e.g.,
[5], Chapter 1), then replace that unknot by a ﬂat ribbon, cut the ribbon and
pull it taut (this is the well known belt trick, see, e.g., [5]); then the number of
twists obtained (with sign speciﬁed via the “left-hand rule”) is, by deﬁnition,
τ(K). As far as I know, this deﬁnition ﬁrst appeared in S.Matveev’s article
[12] (see also [13]) for the particular case of the ﬂat unknot.
Figure 10. Deﬁnition of the twisting number
Theorem 2. Flat knots possess the following three invariants: the Kauﬀ-
man bracket⟨K⟩, the Whitney index w(K), and the twisting number τ(K).
Together,w(K) andτ(K) constitute a complete system of invariants for ﬂat
unknots.
Proof. The invariance of the Kauﬀman bracket is a classical lemma due
to Kauﬀman (see, e.g., [5], pp.24-25). To prove the invariance of the twisting
number, it suﬃces to check that it does not change under Ω 2 and Ω 3, but
this is a straightforward veriﬁcation. The invariance of the Whitney index,
16
as well as the fact that together with the twisting number it constitutes a
complete system of invariants for ﬂat unknots, was proved by Matveev in
[12] by an elementary but tedious argument (see also [13]). □
Of course the algebraic classiﬁcation problem for all ﬂat knots is more
diﬃcult than the same problem for classical (spacial) knots and would require
much stronger invariants (of Vassiliev type?).
§7. Perspectives: new knot energies for computer simulations
The analytical speciﬁcation of a knot energy mimicking the resilience of
our little device is ongoing joint research with Oleg Karpenkov and will be
published elsewhere.
Here we only mention that our functional is deﬁned for ﬂat knots only,
it depends on a small parameter d in the space of smooth ﬂat knots in R2;
roughly speaking, the functional is based on an “unbending force” (the larger
the curvature in the vicinity of some point, the stronger the force that tends
to straighten out the curve near that point). For ﬂat knots, unlike “fat
knots” of cross section diameter d in space, no δ-function type of repulsive
term that does not allow diﬀerent branches of the curve to be at a distance
strictly smaller than d from each other, but allows theses branches to be at
a distance exactly equal to d, is needed.
However, because of Theorem 1, an energy functional for ﬂat knots suﬃces
to determine if two knot diagrams correspond to the same knot (i.e., are
ambient isotopic in space). To do this, compute the Whitney index of the
two knot diagrams, add an appropriate number of little loops to one of them
so as to equalize their Whitney indices and then apply the energy functional;
the given knot diagrams present the same knot if and only if the two ﬂat
normal forms obtained are identical.
Of course this works only provided that the number of crossings is small
enough to ensure uniqueness of normal forms. An optimistic prediction is
that “small” means less than 30; if this were so, we would have a fast eﬀective
algorithm for comparing knot diagrams with 30 crossings or less.
To my mind, a more interesting problem is to deﬁne other energy function-
als that do not necessarily mimic our little device. Such functionals should
include not only a δ-function-like repulsive term, but other terms related to
curvature, torsion, twisting numbers, and whatnot.
More speciﬁcally, such a functional could mimic another concrete device
with which I have performed a series of similar experiments. This new de-
17
vice is made from a thin (∼ 3mm) three-strand metallic cable which resists
twisting (unlike the device described in this article, it does the “belt trick”).
The corresponding functional would involve three summands: an unbending
term (related to local curvature), a repulsive term (related to the thickness of
the device), and an untwisting term (related to torsion and/or the so called
“blackboard framing” of the initial knot diagram).
