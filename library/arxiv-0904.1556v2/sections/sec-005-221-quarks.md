---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-005-221-quarks
section_title: "Quarks"
section_number: 2.2.1
pages: 13-17
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
In the last section, we learned how Heisenberg uniﬁed the proton an d neutron into
the nucleon, and that Yukawa proposed that nucleons interact by exchanging pions.
This viewpoint turned out to be at least approximately true, but it wa s based on
the idea that the proton, neutron and pions were all fundamental particles without
internal structure, which was not ultimately supported by the evid ence.
Protons and neutrons are not fundamental. They are made of par ticles called
quarks. There are a number of diﬀerent types of quarks, called ﬂavors. However,
it takes only two ﬂavors to make protons and neutrons: the up quark , u, and the
down quark , d. The proton consists of two up quarks and one down:
p =uud
while the neutron consists of one up quark and two down:
n =udd
Protons have an electric charge of +1, exactly opposite the electr on, while neutrons
are neutral, with 0 charge. These two conditions are enough to det ermine the charge
of their constituents, which are fundamental fermions much like th e electron:
F undamental F ermions (second try)
Name Symbol Charge
Electron e− −1
Up quark u + 2
3
Down quark d − 1
3
There are more quarks than these, but these are the lightest one s, comprising the
ﬁrst generation . They are all we need to make protons and neutrons, and so,
with the electron in tow, the above list contains all the particles we ne ed to make
atoms.
Yet quarks, fundamental as they are, are never seen in isolation. They are al-
ways bunched up into particles like the proton and neutron. This phe nomenon is
called conﬁnement . It makes the long, convoluted history of how we came to un-
derstand quarks, despite the fact that they are never seen, all the more fascinating.
Unfortunately, we do not have space for this history here, but it c an be found in
the books by Crease and Mann [8], Segr` e [33], and Pais [25].
It is especially impressive how physicists were able to discover that ea ch ﬂavor
of quark comes in three diﬀerent states, called colors: red r, green g, and blue
13
b. These ‘colors’ have nothing to do with actual colors; they are jus t cute names—
though as we shall see, the names are quite well chosen. Mathemat ically, all that
matters is that the Hilbert space for a single quark is C3; we call the standard basis
vectors r,g and b. The color symmetry group SU(3) acts on this Hilbert space
in the obvious way, via its fundamental representation.
Since both up and down quarks come in three color states, there ar e really six
kinds of quarks in the matter we see around us. Three up quarks, s panning a copy
of C3:
ur,ug,ub ∈ C3.
and three down quarks, spanning another copy of C3:
dr,dg,db ∈ C3.
The group SU(3) acts on each space. All six quarks taken togethe r span this vector
space:
C3 ⊕ C3 ∼
= C2 ⊗ C3
where C2 is spanned by the ﬂavors u and d. Put another way, a ﬁrst-generation
quark comes in one of six ﬂavor-color states.
How could physicists discover the concept of color, given that quar ks are con-
ﬁned? In fact conﬁnement was the key to this discovery! Conﬁnem ent amounts to
the following decree: all observed states must be white, i.e., invariant under the
action of SU(3). It turns out that this has many consequences.
For starters, this decree implies that we cannot see an individual qu ark, because
they all transform nontrivially under SU(3). Nor do we ever see a pa rticle built
from two quarks, since no unit vectors in C3 ⊗ C3 are ﬁxed by SU(3). But we do
see particles made of three quarks: namely, nucleons! This is becau se there are unit
vectors in
C3 ⊗ C3 ⊗ C3
ﬁxed by SU(3). Indeed, as a representation of SU(3), C3 ⊗C3 ⊗C3 contains precisely
one copy of the trivial representation: the antisymmetric rank th ree tensors, Λ 3C3 ⊆
C3 ⊗ C3 ⊗ C3. This one dimensional vector space is spanned by the wedge produc t
of all three basis vectors:
r ∧b ∧g ∈ Λ 3C3.
So, up to normalization, this must be the color state of a nucleon. And now we see
why the ‘color’ terminology is well-chosen: an equal mixture of red, g reen and blue
light is white. This is just a coincidence, but it is too cute to resist.
So: color is deeply related to conﬁnement. Flavor, on the other han d, is deeply
related to isospin. Indeed, the ﬂavor C2 is suspiciously like the isospin C2 of the
nucleon. We even call the quark ﬂavors ‘up’ and ‘down’. This is no accid ent. The
proton and neutron, which are the two isospin states of the nucleo n, diﬀer only by
their ﬂavors, and only the ﬂavor of one quark at that. If one could interchangeu
and d, one could interchange protons and neutrons.
Indeed, we can use quarks to explain the isospin symmetry of Sectio n 2.1. Pro-
tons and neutrons are so similar, with nearly the same mass and stro ng interactions,
becauseu andd quarks are so similar, with nearly the same mass and truly identical
colors.
So as in Section 2.1, let SU(2) act on the ﬂavor states C2. By analogy with that
section, we call this SU(2) the isospin symmetries of the quark mode l. Unlike the
color symmetries SU(3), these symmetries are not exact, becaus e u and d quarks
have diﬀerent mass and charge. Nevertheless, they are useful.
14
The isospin of the proton and neutron then arises from the isospin o f its quarks.
Deﬁne I3(u) = 1
2 and I3(d) = − 1
2 , making u and d the isospin up and down states
at which their names hint. To ﬁnd the I3 of a composite, like a proton or neutron,
add the I3 for its constituents. This gives the proton and neutron the right I3:
I3(p) = 1
2 + 1
2 − 1
2 = 1
2
I3(n) = 1
2 − 1
2 − 1
2 = − 1
2.
Of course, having the right I3 is not the whole story for isospin. The states p and
n must still span a copy of the fundamental rep C2 of SU(2). Whether or not this
happens depends on how the constituent quark ﬂavors transfor m under SU(2).
The states u ⊗u ⊗d and u ⊗d ⊗d do not span a copy of the fundamental rep
of SU(2) inside C2 ⊗ C2 ⊗ C2. So, as with color, the equations
p =uud, n =udd
fail to give us the whole story. For the proton, we actually need som e linear com-
bination of the I3 = 1
2 ﬂavor states, which are made of two u’s and one d:
u ⊗u ⊗d, u ⊗d ⊗u, d ⊗u ⊗u ∈ C2 ⊗ C2 ⊗ C2.
And for the neutron, we need some linear combination of the I3 = − 1
2 ﬂavor states,
which are made of one u and two d’s:
u ⊗d ⊗d, d ⊗u ⊗d, d ⊗d ⊗u ∈ C2 ⊗ C2 ⊗ C2.
Writingp = uud and n = udd is just a sort of shorthand for saying that p and n
are made from basis vectors with those quarks in them.
In physics, the linear combination required to make p and n work also involves
the ‘spin’ of the quarks, which lies outside of our scope. We will conte nt ourselves
with showing that it can be done. That is, we will show that C2 ⊗ C2 ⊗ C2 really
does contain a copy of the fundamental rep C2 of SU(2). To do this, we use the
fact that any rank 2 tensor can be decomposed into symmetric and antisymmetric
parts; for example,
C2 ⊗ C2 ∼
= Sym2C2 ⊕ Λ 2C2
and this is actually how C2 ⊗ C2 decomposes into irreps. Sym 2C2, as we noted in
Section 2.1, is the unique 3-dimensional irrep of SU(2); its othogona l complement
Λ 2C2 in C2 ⊗ C2 is thus also a subrepresentation, but this space is 1-dimensional,
and must therefore be the trivial irrep, Λ 2C2 ∼
= C. In fact, for any SU( n), the top
exterior power of its fundamental rep, Λ nCn, is trivial.
As a representation of SU(2), we thus have
C2 ⊗ C2 ⊗ C2 ∼
= C2 ⊗ (Sym2C2 ⊕ C)
∼
= C2 ⊗ Sym2C2 ⊕ C2.
So indeed, C2 is a subrepresentation of C2 ⊗ C2 ⊗ C2.
As in the last section, there is no reason to have the full C2 of isospin states
for nucleons unless there is a way to change protons into neutrons . There, we
discussed how the pions provide this mechanism. The pions live in sl(2, C), the
complexiﬁcation of the adjoint representation of SU(2), and this a cts on C2:
15
π N
N ′
This Feynman diagram is a picture of the intertwining operator sl(2, C) ⊗ C2 → C2
given by the representation of sl(2, C) on C2. Now we know that nucleons are made
of quarks and that isospin symmetry comes from their ﬂavor symme try. What
about pions?
Pions also ﬁt into this model, but they require more explanation, beca use they
are made of quarks and ‘antiquarks’. To every kind of particle, ther e is a cor-
responding antiparticle, which is just like the original particle but with opposite
charge and isospin. The antiparticle of a quark is called an antiquark.
In terms of group representations, passing from a particle to its a ntiparticle
corresponds to taking the dual representation. Since the quark s live in C2 ⊗ C3,
a representation of SU(2) × SU(3), the antiquarks live in the dual representation
C2∗ ⊗ C3∗. Since C2 has basis vectors called up and down:
u =
(
1
0
)
∈ C2 d =
(
0
1
)
∈ C2
the space C2∗ has a dual basis
u = (1, 0) ∈ C2∗ d = (0, 1) ∈ C2∗
called antiup and antidown. Similarly, since the standard basis vectors for C3 are
called red, green and blue, the dual basis vectors for C3∗ are known as anticolors:
namely antiredr, antigreeng, and antiblueb. When it comes to actual colors of
light, antired is called ‘cyan’: this is the color of light which blended with re d gives
white. Similarly, antigreen is magenta, and antiblue is yellow. But few ph ysicists
dare speak of ‘magenta antiquarks’—apparently this would be taking the joke too
far.
All pions are made from one quark and one antiquark. The ﬂavor sta te of the
pions must therefore live in
C2 ⊗ C2∗.
We can use the fact that pions live in sl(2, C) to ﬁnd out how they decompose into
quarks and antiquarks, since
sl(2, C) ⊆ End(C2).
First, express the pions as matrices:
π+ =
(
0 1
0 0
)
π0 =
(
1 0
0 −1
)
π− =
(
0 0
1 0
)
.
16
We know they have to be these matrices, up to normalization, becau se these act
the right way on nucleons in C2:
π− +p →n
π+ +n →p
π0 +p →p
π0 +n →n.
Now, apply the standard isomorphism End( C2) ∼
= C2 ⊗ C2∗ to write these matrices
as linear combinations of quarks and antiquarks:
π+ =u ⊗
d, π 0 =u ⊗u −d ⊗d, π − =d ⊗u.
Note these all have the right I3, because isospins reverse for antiparticles. For
example, I3(d) = + 1
2 , so I3(π+) = 1.
In writing these pions as quarks and antiquarks, we have once again neglected
to write the color, because this works the same way for all pions. As far as color
goes, pions live in
C3 ⊗ C3∗.
Conﬁnement says that pions need to be white, just like nucleons, an d there is only
a one-dimensional subspace of C3 ⊗ C3∗ on which SU(3) acts trivially, spanned by
r ⊗r +g ⊗g +b ⊗b ∈ C3 ⊗ C3∗.
So, this must be the color state of all pions.
Finally, the Gell-Mann–Nishijima formula also still works for quarks, pr ovided
we deﬁne the hypercharge for both quarks to be Y = 1
3 :
Q(u) = I3(u) +Y/ 2 = 1
2 + 1
6 = 2
3
Q(d) = I3(d) +Y/ 2 = − 1
2 + 1
6 = − 1
3.
Since nucleons are made of three quarks, their total hypercharg e is Y = 1, just as
before.
