---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-016-33-the-patisalam-model
section_title: "The Pati–Salam Model"
section_number: 3.3
pages: 48-55
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
Next we turn to a uniﬁed theory that is not so ‘grand’: its gauge grou p is not a simple
Lie group, as it was for the SU(5) and Spin(10) theories. This theor y is called the
Pati–Salam model, after its inventors [28]; it has gauge group SU(2) ×SU(2)×SU(4),
which is merely semisimple.
We might imagine the SU(5) theory as an answer to this question:
Why are the hypercharges in the Standard Model what they are?
The answer it provides is something like this:
Because SU(5) is the actual gauge group of the world, acting on th e
representation Λ C5.
But there are other intriguing patterns in the Standard Model tha t SU(5) does not
explain—and these lead us in diﬀerent directions.
First, there is a strange similarity between quarks and leptons. Eac h generation
of fermions in the Standard Model has two quarks and two leptons. For example,
in the ﬁrst generation we have the quarks u and d, and the leptons ν and e−. The
quarks come in three ‘colors’: this is a picturesque way of saying that they transform
in the fundamental representation of SU(3) on C3. The leptons, on the other hand,
are ‘white’: they transform in the trivial representation of SU(3) o n C.
Representations of SU(3)
Particle Representation
Quark C3
Lepton C
Could the lepton secretly be a fourth color of quark? Maybe it could in a theory
where the SU(3) color symmetry of the Standard Model is extende d to SU(4).
48
Of course this larger symmetry would need to be broken to explain th e very real
diﬀerence between leptons and quarks.
Second, there is a strange diﬀerence between left- and right-han ded fermions.
The left-handed ones participate in the weak force governed by SU (2), while the
right-handed ones do not. Mathematically speaking, the left-hand ed ones live in a
nontrivial representation of SU(2), while the right-handed ones liv e in a trivial one.
The nontrivial one is C2, while the trivial one is C ⊕ C:
Representations of SU(2)
Particle Representation
Left-handed fermion C2
Right-handed fermion C ⊕ C
But there is a suspicious similarity between C2 and C ⊕ C. Could there be another
copy of SU(2) that acts on the right-handed particles? Again, this ‘right-handed’
SU(2) would need to be broken, to explain why we do not see a ‘right-h anded’
version of the weak force that acts on right-handed particles.
Following Pati and Salam, let us try to sculpt a theory that makes the se ideas
precise. In the last two sections, we saw some of the ingredients we need to make
a grand uniﬁed theory: we need to extend the symmetry group GSM to a larger
group G using an inclusion
GSM֒→G
(up to some discrete kernel), and we need a representation V of G which reduces
to the Standard Model representation when restricted to GSM:
F ⊕F ∗ ∼
=V.
We can put all these ingredients together into a diagram
GSM /d47/d47/d15/d15
G
/d15/d15
U(F ⊕F ∗) ∼ /d47/d47 U(V )
which commutes only when our G theory works out.
We now use the same methods to chip away at our current challenge. We asked
if leptons correspond to a fourth color. We already know that ever y quark comes
in three colors, r, g, and b, which form a basis for the vector space C3. This is the
fundamental representation of SU(3), the color symmetry grou p of the Standard
Model. If leptons correspond to a fourth color, say ‘white’, then we should use the
colors r, g, b and w, as a basis for the vector space C4. This is the fundamental
representation of SU(4), so let us take that group to describe co lor symmetries in
our new GUT.
Now SU(3) has an obvious inclusion into SU(4), using block diagonal ma trices:
g ↦→
( g 0
0 1
)
When restricted to this subgroup, the fundamental representa tion C4 breaks into a
direct sum of irreps:
C4 ∼
= C3 ⊕ C.
49
These are precisely the irreps of SU(3) that describe quarks and le ptons. For anti-
quarks and antileptons we can use
C4∗ ∼
= C3∗ ⊕ C.
It looks like we are on the right track.
We can do even better if we start with the splitting
C4 ∼
= C3 ⊕ C.
Remember that when we studied SU(5), the splitting
C5 ∼
= C2 ⊕ C3
had the remarkable eﬀect of introducing U(1), and thus hypercha rge, into SU(5)
theory. This was because the subgroup of SU(5) that preserves this splitting is
larger than SU(2) × SU(3), roughly by a factor of U(1):
(U(1) × SU(2) × SU(3))/Z6 ∼
= S(U(2) × U(3))
It was this factor of U(1) that made SU(5) theory so fruitful.
So, if we choose a splitting C4 ∼
= C3 ⊕ C, we should again look at the subgroup
that preserves this splitting. Namely:
S(U(3) × U(1)) ⊆ SU(4).
Just as in the SU(5) case, this group is bigger than SU(3) × SU(1), roughly by a
factor of U(1). And again, this factor of U(1) is related to hyperc harge!
This works very much as it did for SU(5). We want a map
U(1) × SU(3) → SU(4)
and we already have one that works for the SU(3) part:
SU(3) → SU(4)
h ↦→
( h 0
0 1
)
So, we just need to include a factor of U(1) that commutes with eve rything in the
SU(3) subgroup. Elements of SU(4) that do this are of the form
(
α 0
0 β
)
where α stands for the 3 × 3 identity matrix times the complex number α ∈ U(1),
and similarly for β in the 1 × 1 block. For the above matrix to lie in SU(4), it must
have determinant 1, so α3β = 1. Thus we must include U(1) using matrices of this
form: (
α 0
0 α−3
)
.
This gives our map:
U(1) × SU(3) → SU(4)
(α,h ) ↦→
( αh 0
0 α−3
)
.
50
If we let U(1) × SU(3) act on C4 ∼
= C3 ⊕ C via this map, the ‘quark part’ C3
transforms as though it has hypercharge 1
3 : that is, it gets multiplied by a factor
of α. Meanwhile, the ‘lepton part’ C transforms as though it has hypercharge −1,
getting multiplied by a factor of α−3. So, as a representation of U(1) × SU(3), we
have
C4 ∼
= C 1
3
⊗ C3 ⊕ C−1 ⊗ C.
A peek at Table 1 reveals something nice. This is exactly how the left-h anded
quarks and leptons in the Standard Model transform under U(1) × SU(3)!
The right-handed leptons do not work this way. That is a problem we n eed to
address. But this brings us to our second question, which was abou t the strange
diﬀerence between left- and right-handed particles.
Remember that in the Standard Model, the left-handed particles live in the
fundamental rep of SU(2) on C2, while the right-handed ones live in the trivial rep
on C ⊕ C. Physicists write this by grouping left-handed particles into ‘doublet s’,
while leaving the right-handed particles as ‘singlets’:
( νL
e−
L
) νR
e−
R
.
But there is a suspicious similarity between C2 and C ⊕ C. Could there be another
copy of SU(2) that acts on the right-handed particles? Physically s peaking, this
would mean that the left- and right-handed particles both form dou blets:
( νL
e−
L
) ( νR
e−
R
)
but under the actions of diﬀerent SU(2)’s. Mathematically, this wou ld amount to
extending the representations of the ‘left-handed’ SU(2):
C2 C ⊕ C
to representations of SU(2) × SU(2):
C2 ⊗ C C ⊗ C2
where the ﬁrst copy of SU(2) acts on the ﬁrst factor in these ten sor products, while
the second copy acts on the second factor. The ﬁrst copy of SU( 2) is the ‘left-handed’
one familiar from the Standard Model. The second copy is a new ‘right- handed’
one.
If we restrict these representations to the ‘left-handed’ SU(2) subgroup, we ob-
tain:
C2 ⊗ C ∼
= C2
C ⊗ C2 ∼
= C ⊕ C.
These are exactly the representations of SU(2) that appear in th e Standard Model.
It looks like we are on the right track!
Now let us try to combine these ideas into a theory with symmetry gro up SU(2)×
SU(2)×SU(4). We have seen that letting SU(4) act on C4 is a good way to unify our
treatment of color for all the left-handed fermions. Similarly, the d ual representation
on C4∗ is good for their antiparticles. So, we will tackle color by letting SU(4) act
on the direct sum C4 ⊕ C4∗. This space is 8-dimensional. We have also seen that
51
letting SU(2) × SU(2) act on C2 ⊗ C ⊕ C ⊗ C2 is a good way to unify our treatment
of isospin for left- and right-handed fermions. This space is 4-dimen sional.
Since 8 × 4 = 32, and the Standard Model representation is 32-dimensional, le t
us take the tensor product
V =
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
.
This becomes a representation of SU(2) × SU(2) × SU(4), which we call the Pati–
Salam representation . To obtain a theory that extends the Standard Model, we
also need a way to map GSM to SU(2) × SU(2) × SU(4), such that pulling back V
to a representation of GSM gives the Standard model representation.
How can we map GSM to SU(2) ×SU(2)×SU(4)? There are several possibilities.
Our work so far suggests this option:
U(1) × SU(2) × SU(3) → SU(2) × SU(2) × SU(4)
(α,g,h ) ↦→
(
g, 1,
( αh 0
0 α−3
))
Let us see what this gives. The Pati–Salam representation of SU(2) × SU(2) ×
SU(4) is a direct sum of four irreducibles:
V ∼
= C2 ⊗ C ⊗ C4 ⊕ C ⊗ C2 ⊗ C4 ⊕ C2 ⊗ C ⊗ C4∗ ⊕ C ⊗ C2 ⊗ C4∗.
We hope the ﬁrst two will describe left- and right-handed fermions, so let us give
them names that suggest this:
FL = C2 ⊗ C ⊗ C4,
FR = C ⊗ C2 ⊗ C4.
The other two are the duals of the ﬁrst two, since the 2-dimensiona l irrep of SU(2)
is its own dual:
F ∗
L = C2 ⊗ C ⊗ C4∗,
F ∗
R = C ⊗ C2 ⊗ C4∗.
Given our chosen map from GSM to SU(2) × SU(2) × SU(4), we can work out
which representations of the GSM these four spaces give. For example, consider
FL. We have already seen that under our chosen map,
C4 ∼
= C 1
3
⊗ C3 ⊕ C−1 ⊗ C
as representations of U(1) × SU(3), while
C2 ⊗ C ∼
= C2
as representations of the left-handed SU(2). So, as represent ations of GSM we have
FL ∼
= C 1
3
⊗ C2 ⊗ C3 ⊕ C−1 ⊗ C2 ⊗ C.
Table 1 shows that these indeed match the left-handed fermions.
If we go ahead and do the other four cases, we see that everythin g works except
for the hypercharges of the right-handed particles —and their antiparticles. Here we
just show results for the particles:
52
The Pati–Salam Model — First T ry
Particle Hypercharge: predicted Hypercharge: actual
( νL
e−
L
)
−1 −1
( uL
dL
)
1
3
1
3
νR −1 0
e−
R −1 −2
uR 1
3
4
3
dR 1
3 − 2
3
The problem is that the right-handed particles are getting the same hypercharges
as their left-handed brethren. To ﬁx this problem, we need a more c lever map from
GSM to SU(2)×SU(2)×SU(4). This map must behave diﬀerently on the U(1) factor
of GSM, so the hypercharges come out diﬀerently. And it must take advan tage of
the right-handed copy of SU(2), which acts nontrivially only on the r ight-handed
particles. For example, we can try this map:
U(1) × SU(2) × SU(3) → SU(2) × SU(2) × SU(4)
(α,g,h ) ↦→
(
g,
( αk 0
0 α−k
)
,
( αh 0
0 α−3
))
for any integer k. This will not aﬀect the above table except for the hypercharges
of right-handed particles. It will add k/3 to the hypercharges of the ‘up’ particles
in right-handed doublets ( νR and uR), and subtract k/3 from the ‘down’ ones (e−
R
and dR). So, we obtain these results:
The Pati–Salam Model — Second T ry
Particle Hypercharge: predicted Hypercharge: actual
( νL
e−
L
)
−1 −1
( uL
dL
)
1
3
1
3
νR −1 + k
3 0
e−
R −1 − k
3 −2
uR 1
3 + k
3
4
3
dR 1
3 − k
3 − 2
3
Miraculously, all the hypercharges match if we choose k = 3. So, let us use this
53
map:
β: U(1) × SU(2) × SU(3) → SU(2) × SU(2) × SU(4)
(α,g,h ) ↦→
(
g,
( α3 0
0 α−3
)
,
( αh 0
0 α−3
))
.
When we take the Pati–Salam representation of SU(2) × SU(2) × SU(4) and pull
it back along this map β, we obtain the Standard Model representation. As in
Section 3.1, we use complete reducibility to see this, but we can be mor e concrete.
We saw in Table 4 how we can specify the intertwining map precisely by us ing a
speciﬁc basis, which for Λ C5 results in the binary code.
Similarly, we can create a kind of ‘Pati–Salam code’ to specify an isomor phism
of Hilbert spaces
ℓ:F ⊕F ∗ →
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
,
and doing this provides a nice summary of the ideas behind the Pati–Sa lam model.
We take the space C2 ⊗ C to be spanned by uL and dL, the left-isospin up and
left-isospin down states. Similarly, the space C ⊗ C2 has basis uR anddR, called
right-isospin up and right-isospin down . Take care not to confuse these with
the similarly named quarks. These have no color, and only correspon d to isospin.
The color comes from C4 of course, which we already decreed to be spanned by
r, g,b andw. For antiparticles, we also require anticolors, which we take to be th e
dual basis r, g, b and w, spanning C4∗.
It is now easy, with our knowledge of how the Pati–Salam model is to wo rk, to
construct this code. Naturally, the left-handed quark doublet co rresponds to the
left-isospin up and down states, which come in all three colors c =r,g,b :
uc
L =uL ⊗c d c
L =dL ⊗c.
The corresponding doublet of left-handed leptons is just the ‘white ’ version of this:
νL =uL ⊗w e −
L =dL ⊗w.
The right-handed fermions are the same, but with R’s instead of L’s. Thus we get
the Pati–Salam code for the fermions:
FL FR
νL =uL ⊗w ν R =uR ⊗w
e−
L =dL ⊗w e −
R =dR ⊗w
uc
L =uL ⊗c u c
R =uR ⊗c
dc
L =dL ⊗c d c
R =dR ⊗c
The result is very similar for the antifermions in F ∗
L andF ∗
R, but watch out: taking
antiparticles swaps up and down , and also swaps left and right , so the particles in
F ∗
L are right-handed, despite the subscript L, while those in F ∗
R are left-handed.
This is because it is the right-handed antiparticles that feel the wea k force, which
in terms of representation theory means they are nontrivial unde r the left SU(2).
So, the Pati–Salam code for the antifermions is this:
F ∗
L F ∗
R
e+
R =uL ⊗
w e +
L =uR ⊗
w
νR =dL ⊗w νL =dR ⊗w
d
c
R =uL ⊗
c d
c
L =uR ⊗
c
uc
R =dL ⊗
c uc
L =dR ⊗
c
54
Putting these together we get the full Pati–Salam code:
The Pati–Salam Code
FL FR F ∗
L F ∗
R
νL =uL ⊗w ν R =uR ⊗w e +
R =uL ⊗
w e +
L =uR ⊗
w
e−
L =dL ⊗w e −
R =dR ⊗w
νR =dL ⊗w νL =dR ⊗w
uc
L =uL ⊗c u c
R =uR ⊗c
d
c
R =uL ⊗
c d
c
L =uR ⊗
c
dc
L =dL ⊗c d c
R =dR ⊗c
uc
R =dL ⊗
c uc
L =dR ⊗
c
Table 5: Pati–Salam code for ﬁrst-generation fermions, where c = r,g,b and c =
r,b,g.
This table deﬁnes an isomorphism of Hilbert spaces
ℓ:F ⊕F ∗ →
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
so where it says, for example, νL =uL ⊗w, that is just short for ℓ(νL) = uL ⊗w.
This map ℓ is also an isomorphism between representations of GSM. It tells us how
these representations are the ‘same’, just as the map h did for F ⊕F ∗ and Λ C5 at
the end of Section 3.1.
As with SU(5) and Spin(10), we can summarize all the results of this s ection in
a commutative square:
Theorem 3. The following square commutes:
GSM
β /d47/d47
/d15/d15
SU(2) × SU(2) × SU(4)
/d15/d15
U(F ⊕F ∗)
U(ℓ) /d47/d47 U
((
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗))
where the left vertical arrow is the Standard Model represen tation and the right one
is the Pati–Salam representation.
The Pati–Salam representation and especially the homomorphism β look less
natural than the representation of SU(5) on Λ C5 and the homomorphism φ:GSM →
SU(5). But appearances can be deceiving: in the next section we sh all see a more
elegant way to describe them.
