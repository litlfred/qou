---
doc_id: 104171-rmi-1356
doc_title: "Handlebody diagram algebras"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 10.4171-rmi-1356.pdf
source_sha256: 148119374f06be9f
toc_source: outline
doc_brief: "Handlebody diagram algebras — In this paper, we study handlebody versions of some classical diagram algebras, most prominently, handlebody versions of Temperley–Lieb, blob, Brauer, BMW, Hecke and"
---
A large collection of diagram algebras, such as Temperley–Lieb or (type A) Hecke alge-
bras, are interesting from at least two perspectives: they are of fundamental importance in
low-dimensional topology and they also have a rich representation theory.
Having an eye on the study of links in 3-manifolds brings the topology of the ambient
space into play. In all the classical examples, like Temperley–Lieb or Hecke algebras, the
ambient space is the 3-ball, and these algebras are related to spherical Coxeter groups and
Artin–Tits braid groups. In the simplest case beyond the 3-ball, when one passes to links in
a solid torus, these diagram algebras get replaced by their (extended) affine versions, and
the related objects are now affine Coxeter groups and Artin–Tits braid groups. A natural
question is what kind of diagrammatics and Coxeter combinatorics one could expect for
more general 3-manifolds.
In this paper we consider (three-dimensional) handlebodies of genus g. The 3-ball and
the solid torus correspond to g D 0 (called classical in this paper) and g D 1, respectively.
As we will see, the Temperley–Lieb and Hecke algebras, their affine versions as well as
algebras along the same lines, can be seen as a low genus class of a more general, higher
genus, class of diagram algebras.
In case g D 0, these diagram algebras and their associated braid groups are around for
donkey’s years. For g D 1, there is a long history of work on this topic which goes back
to at least Brieskorn [7]. For example (with more references to come later on), see [1] for
braid pictures, [19] or [52] for connections to knot theory, [24] or [27] for affine diagram
algebras. To the best of our knowledge, the first attempts to give a description of braids
2020 Mathematics Subject Classification: Primary 16G99; Secondary 20F36, 18M30, 20C08, 57K14.
Keywords: Diagrammatic algebra, cellular algebras, braid groups, handlebodies.
D. Tubbenhauer and P. Vaz
846
in handlebodies are due to Vershinin [64] and Häring-Oldenburg–Lambropoulou [28,41],
while Lambropoulou studied links in 3-manifolds even before that [40].
From the representation theoretical point of view all these algebras share the common
feature of being cellular in a certain way that we will make precise. In a nutshell, in the
g D 0 case, these algebras are often cellular in the sense of Graham–Lehrer [21], and in
the g D 1 case, they are often affine cellular in the sense of König–Xi [34].
We see this paper as a continuation of these works, focusing on the diagrammatic, alge-
braic and representation theoretical aspects. That is, we generalize some diagram algebras
to higher genus, and we show that they are sandwich cellular. (Sandwich cellular is a
notion that generalizes cellularity. Roughly speaking it means that the original algebra
can be obtained by sandwiching smaller algebras. One of the upshots of being sandwich
cellular is that the classification of simple modules is reduced from the original algebra to
the sandwiched algebras.)
1A. What this paper does
Our starting point is a diagrammatic description of handlebody braid groups of genus g,
i.e., a diagrammatic description of the configuration space of a disk with g punctures. The
pictures hereby are, e.g.,
A handlebody braid for g D 4W
core strands
usual strands
:
This illustrates a handlebody braid of genus 4: The three strands on the right are usual
strands. The four thick and blue/grayish strands on the left are core strands and they cor-
respond to the punctures of the disk respectively the cores of the handlebody. The point is
that by an appropriate closure, i.e., merging the core strands at infinity, illustrated by
An Alexander closureW
⇝

1

1
;
the core strands correspond to cores of a handlebody as explained in e.g. [55], Section 2,
hence the name. All links in such handlebodies can be obtained by this closing proce-
dure, and there is also an associated Markov theorem. In other words, the handlebody
braid group gives an algebraic way to study links in handlebodies. The main references
here are [64] and [28]. After explaining this setup more carefully, building upon the afore-
mentioned works, in Section 3 we also study an associated handlebody Coxeter group for
which we find a basis using versions of Jucys–Murphy elements.
These handlebody braid pictures are also our starting point to define and study various
diagram algebras associated to handlebodies:
Handlebody diagram algebras
847
(1) In Section 4 we study handlebody Temperley–Lieb and blob algebras. The pictures
to keep in mind are crossingless matchings and core strands (left, Temperley–Lieb)
respectively crossingless matchings decorated with colored blobs (right, blob):
A Temperley–Lieb pictureW
:
A blob pictureW
u
u
w
v
w
v
v
u
v
u
:
Note that the blobs illustrated in the right picture come in colors, corresponding
to the various cores strands. These algebras generalize Temperley–Lieb algebras
and blob algebras: If g D 0, then these two algebras are the same as the classical
Temperley–Lieb algebra. For g  1 they are not the same anymore (at least in our
formulation), and have a long history of study starting with e.g. [45].
(2) In Section 5 we move on to handlebody versions of Brauer and BMW algebras.
These are tangle algebras with core strands and the picture is
A BMW pictureW
:
As before, the case g D 0 is classical and goes back to Brauer, while g D 1 appears
in [26]. In the same section we also study their cyclotomic quotients.
(3) Finally, Section 6 studies handlebody versions of Hecke and Ariki–Koike algebras.
The picture for handlebody Hecke algebras is the same as for handlebody braid
groups, while we choose to illustrate handlebody versions of Ariki–Koike algebras
using blobs, e.g.,
An Ariki–Koike pictureW
u
v
:
The cases g D 0 and g D 1 are, of course, well-studied and they correspond to Hecke
respectively extended affine Hecke algebras or cyclotomic quotients. We learned
about the g > 1 case from [41] and [5].
We also study a generalization of cellularity in Section 2, giving us a toolkit to param-
eterize the simples modules of the aforementioned algebras. Note hereby that this gener-
alization heavily builds on and borrows from [23], [36], [25] or [14]. Although it might be
known to experts, our exposition is new.
1B. Speculations
Let us mention a number of possible future directions.
 Quantum topology. A manifest direction which we do not explore in this work would
be to study these algebras in connections to quantum topology and its ramifications.
D. Tubbenhauer and P. Vaz
848
For example, for g D 1, [19] and [52] construct link invariants from Markov traces,
and these link invariants admit categorifications [66]. For g > 1, [55] takes a few first
steps towards categorical handlebody link invariants, but this direction appears to be
widely open otherwise.
Moreover, for g D 0 most of these diagram algebras are related to representation
theory by some form of Schur–Weyl duality. (In fact, this was the reason to define e.g.
the Temperley–Lieb algebras to begin with, see [57].) Some work for higher genus
on this representation theoretical aspect is done, e.g. in relation to Verma modules
[11, 30, 39] or complex reflection groups [48, 58]. Following this track for higher
genus seems to be a worthwhile goal.
 Diagram algebras. There are plenty of diagram algebras that we do not considered
in this paper, but for which (some version of) our discussion goes through.
Examples of such algebras that come to mind that appear in classical literature are
partition algebras [44], rook monoid algebras [60], walled Brauer algebras [35] and
alike. Other examples are related to knot theory and categorification such as (type A)
webs appearing in a version of Schur–Weyl duality [9,53,54,63].
Diagrammatic algebras are also important in categorification. After the introduction
of the diagrammatic version of the KLR algebra [33] (see also [56]) they have become
quite popular, and might admit handlebody extensions. For example, alongside with
KLR algebras Webster’s tensor product algebras [65], algebras related to Verma cat-
egorifications [38, 43, 50, 51], Soergel diagrammatics [16], potentially admit handle-
body versions, just to name a few.
We also expect these handlebody diagram algebras to have “nice” sandwich cellular
bases.
 Categories instead of algebras. All of our algebras and concepts under study also
have appropriate categorical versions.
For example, it should be fairly straightforward to generalize our discussion of Sec-
tion 2 to cellular categories [15, 67]. However, let us mention that a reason why we
have not touched upon categorical versions of our handlebody diagram algebras is
that these do not form monoidal categories for g > 0 (at least not in any reasonable
sense as far as we are aware), but rather module categories. We think this deserves a
thorough treatment, following for example [26] or [59].
1C. How to read this paper
Section 2 explains our generalization of cellularity and is independent of the rest. It can be
easily skipped during a first reading. Section 3 treats handlebody braid and Coxeter groups
and is fundamental for all sections following it. Moreover, to avoid too much repetition, we
decided to construct the remaining sections assuming the reader knows Section 4, in which
we define handlebody Temperley–Lieb and blob algebras. So this section is mandatory if
one wants to read either Section 5, the BMW part, or Section 6, the Hecke part.
Handlebody diagram algebras
