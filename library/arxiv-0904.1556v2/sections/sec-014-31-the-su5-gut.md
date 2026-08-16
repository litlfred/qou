---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-014-31-the-su5-gut
section_title: "The SU(5) GUT"
section_number: 3.1
pages: 32-42
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
The SU(5) grand uniﬁed theory appeared in a 1974 paper by Howard Georgi and
Sheldon Glashow [12]. It was the ﬁrst grand uniﬁed theory, and is still considered
the prototypical example. As such, there are many accounts of it in the physics
literature. The textbooks by Ross [31] and Mohapatra [21] both de vote an entire
chapter to the SU(5) theory, and a lucid summary can be found in a r eview article by
Witten [39], which also discusses the supersymmetric generalization o f this theory.
In this section, we will limit our attention to the nonsupersymmetric v ersion of
SU(5) theory, which is how it was originally proposed. Unfortunately , this theory
has since been ruled out by experiment; it predicts that protons will decay faster
than the current lower bound on proton lifetime [26]. Nevertheless, because of its
prototypical status and intrinsic interest, we simply must talk abou t the SU(5)
theory.
The core idea behind the SU(5) grand uniﬁed theory is that because the Standard
Model representation F ⊕F ∗ is 32-dimensional, each particle or antiparticle in the
ﬁrst generation of fermions can be named by a 5-bit code. Roughly s peaking, these
bits are the answers to ﬁve yes-or-no questions:
• Is the particle isospin up?
• Is it isospin down?
32
• Is it red?
• Is it green?
• Is it blue?
There are subtleties involved when we answer ‘yes’ to both the ﬁrst two questions,
or ‘yes’ to more than one of the last three, but let us start with an e xample where
these issues do not arise: the bit string 01100. This names a particle that is down
and red. So, it refers to a red quark whose isospin is down, meaning − 1
2 . Glancing
at Table 1, we see just one particle meeting this description: the red left-handed
down quark, dr
L.
We can ﬂesh out this scheme by demanding that the operation of tak ing an-
tiparticles correspond to switching 0’s for 1’s in the code. So the cod e for the
antiparticle of dr
L, the ‘antired right-handed antidown antiquark’, is 10011. This is
cute: it means that being antidown is the same as being up, while being a ntired is
the same as being both green and blue.
Furthermore, in this scheme all antileptons are ‘black’ (the particle s with no
color, ending in 000), while leptons are ‘white’ (the particles with ever y color,
ending in 111). Quarks have exactly one color, and antiquarks have exactly two.
We are slowly working our way to the SU(5) theory. Next let us bring H ilbert
spaces into the game. We can take the basic properties of being up, down, red,
green or blue, and treat them as basis vectors for C5. Let us call these vectors
u,d,r,g,b . The exterior algebra Λ C5 has a basis given by wedge products of these 5
vectors. This exterior algebra is 32-dimensional, and it has a basis lab elled by 5-bit
strings. For example, the bit string 01100 corresponds to the bas is vector d ∧r,
while the bit string 10011 corresponds to u ∧g ∧b.
Next we bring in representation theory. The group SU(5) has an ob vious repre-
sentation on C5. And since the operation of taking exterior algebras is functorial,
this group also has a representation on Λ C5. In the SU(5) grand uniﬁed theory, this
is the representation we use to describe a single generation of ferm ions and their
antiparticles.
Just by our wording, though, we are picking out a splitting of C5 into C2 ⊕ C3:
the isospin and color parts, respectively. Choosing such a splitting o f C5 picks out
a subgroup of SU(5), the set of all group elements that preserve this splitting. This
subgroup consists of block diagonal matrices with a 2 × 2 block and a 3 × 3 block,
both unitary, such that the determinant of the whole matrix is 1. Le t us denote
this subgroup as S(U(2) × U(3)).
Now for the miracle: the subgroup S(U(2) × U(3)) is isomorphic to the Standard
Model gauge group (at least modulo a ﬁnite subgroup). And, when w e restrict the
representation of SU(5) on Λ C5 to S(U(2) × U(3)), we get the Standard Model
representation!
There are two great things about this. The ﬁrst is that it gives a con cise and
mathematically elegant description of the Standard Model represe ntation. The
second is that the seemingly ad hoc hypercharges in the Standard M odel must be
exactly what they are for this description to work. So, physicists say the SU(5)
theory explains the fractional charges of quarks: the fact that quark charges come
in units 1
3 the size of the electron charge pops right out of this theory.
With this foretaste of the fruits the SU(5) theory will bear, let us g et to work
and sow the seeds. Our work will have two parts. First we need to ch eck that
S(U(2) × U(3)) ∼
=GSM/N
33
where N is some ﬁnite normal subgroup that acts trivially on F ⊕F ∗. Then we
need to check that indeed
Λ C5 ∼
=F ⊕F ∗
as representations of S(U(2) × U(3)).
First, the group isomorphism. Naively, one might seek to build the SU( 5) theory
by including GSM as a subgroup of SU(5). Can this be done? Clearly, we can
include SU(2) × SU(3) as block diagonal matrices in SU(5):
SU(2) × SU(3) → SU(5)
(g,h ) ↦− →
(
g 0
0 h
)
.
but this is not enough, because GSM also has that pesky factor of U(1), related to
the hypercharge. How can we ﬁt that in?
The ﬁrst clue is that elements of U(1) must commute with the element s of
SU(2) × SU(3). But the only elements of SU(5) that commute with everybod y in
the SU(2) × SU(3) subgroup are diagonal, since they must separately commute with
SU(2) × 1 and 1 × SU(3), and the only elements doing so are diagonal. Moreover,
they must be scalars on each block. So, they have to look like this:
( α 0
0 β
)
where α stands for the 2 × 2 identity matrix times the complex number α ∈ U(1),
and similarly for β in the 3 × 3 block. For the above matrix to lie in SU(5), it must
have determinant 1, so α2β3 = 1. This condition cuts the group of such matrices
from U(1) × U(1) down to U(1). In fact, all such matrices are of the form
( α3 0
0 α−2
)
where α runs over U(1).
So if we throw in elements of this form, do we get U(1) × SU(2) × SU(3)? More
precisely, does this map:
φ: GSM → SU(5)
(α,g,h ) ↦− →
( α3g 0
0 α−2h
)
give an isomorphism between GSM and S(U(2) × U(3))? It is clearly a homomor-
phism. It clearly maps GSM into the subgroup S(U(2) × U(3)), and it is easy to
check that it maps GSM onto this subgroup. But is it one-to-one?
The answer is no: the map φ has a kernel, Z6. The kernel is the set of all
elements of the form
(α,α −3,α 2) ∈ U(1) × SU(2) × SU(3)
and this is Z6, because scalar matrices α−3 andα2 live in SU(2) and SU(3), respec-
tively, if and only if α is a sixth root of unity. So, all we get is
GSM/Z6 ∼
= S(U(2) × U(3))֒→SU(5).
This sets up a nerve-wracking test that the SU(5) theory must pa ss for it to
have any chance of success. After all, not all representations of GSM factor through
34
GSM/Z6, but all those coming from representations of SU(5) must do so. A repre-
sentation ofGSM will factor through GSM/Z6 only if the Z6 subgroup acts trivially.
In short: the SU(5) GUT is doomed unless Z6 acts trivially on every fermion.
(And antifermion, but that amounts to the same thing.) For this to b e true, some
nontrivial relations between hypercharge, isospin and color must h old.
For example, consider the left-handed electron
e−
L ∈ C−1 ⊗ C2 ⊗ C.
For any sixth root of unity α, we need
(α,α −3,α 2) ∈ U(1) × SU(2) × SU(3)
to act trivially on this particle. Let us see how it acts. Note that:
• α ∈ U(1) acts on C−1 as multiplication by α−3;
• α−3 ∈ SU(2) acts on C2 as multiplication by α−3;
• α2 ∈ SU(3) acts trivially on C.
So, we have
(α,α −3,α 2) ·e−
L =α−3α−3e−
L =e−
L.
The action is indeed trivial—precisely because α is a sixth root of unity.
Or, consider the right-handed d quark:
dR ∈ C− 2
3
⊗ C ⊗ C3.
How does (α,α −3,α 2) act on this? We note:
• α ∈ U(1) acts on C− 2
3
as multiplication by α−2;
• α−3 ∈ SU(2) acts trivially on the trivial representation C;
• α2 ∈ SU(3) acts on C3 as multiplication by α2.
So, we have
(α,α −3,α 2) ·dR =α−2α2dR =dR.
Again, the action is trivial.
For SU(5) to work, though, Z6 has to act trivially on every fermion. There are
16 cases to check, and it is an awful lot to demand that hypercharg e, the most
erratic part of the Standard Model representation, satisﬁes 16 relations.
Or is it? In general, for a fermion with hypercharge Y , there are four distinct
possibilities:
Hypercharge relations
Case Representation Relation
Nontrivial SU(2), nontrivial SU(3) ⇒ CY ⊗ C2 ⊗ C3 ⇒ α3Y −3+2 = 1
Nontrivial SU(2), trivial SU(3) ⇒ CY ⊗ C2 ⊗ C ⇒ α3Y −3 = 1
Trivial SU(2), nontrivial SU(3) ⇒ CY ⊗ C ⊗ C3 ⇒ α3Y +2 = 1
Trivial SU(2), trivial SU(3) ⇒ CY ⊗ C ⊗ C ⇒ α3Y = 1
Better yet, say it like a physicist!
35
Hypercharge relations
Case Representation Relation
Left-handed quark ⇒ CY ⊗ C2 ⊗ C3 ⇒ α3Y −3+2 = 1
Left-handed lepton ⇒ CY ⊗ C2 ⊗ C ⇒ α3Y −3 = 1
Right-handed quark ⇒ CY ⊗ C ⊗ C3 ⇒ α3Y +2 = 1
Right-handed lepton ⇒ CY ⊗ C ⊗ C ⇒ α3Y = 1
But α is sixth root of unity, so all this really says is that those exponents a re
multiples of six:
Hypercharge relations
Case Relation
Left-handed quark ⇒ 3Y − 3 + 2 ∈ 6Z
Left-handed lepton ⇒ 3Y − 3 ∈ 6Z
Right-handed quark ⇒ 3Y + 2 ∈ 6Z
Right-handed lepton ⇒ 3Y ∈ 6Z
Dividing by 3 and doing a little work, it is easy to see these are just sayin g:
Hypercharge relations
Case Hypercharge
Left-handed quark Y = even integer + 1
3
Left-handed lepton Y = odd integer
Right-handed quark Y = odd integer + 1
3
Right-handed lepton Y = even integer
Table 3: Hypercharge relations
Now it is easy to check that this indeed holds for every fermion in the s tandard
model. SU(5) passes the test, not despite the bizarre pattern fo llowed by hyper-
charges, but because of it!
By this analysis, we have shown that Z6 acts trivially on the Standard Model
rep, so it is contained in the kernel of this rep. It is better than jus t a containment
though: Z6 is the entire kernel. Because of this, we could say that GSM/Z6 is the
‘true’ gauge group of the Standard Model. And because we now kno w that
GSM/Z6 ∼
= S(U(2) × U(3))֒→SU(5),
it is almost as though this Z6 kernel, lurking inside GSM this whole time, was a
cryptic hint to try the SU(5) theory.
Of course, we still need to ﬁnd a representation of SU(5) that ext ends the Stan-
dard Model representation. Luckily, there is a very beautiful cho ice that works:
the exterior algebra Λ C5. Since SU(5) acts on C5, it has a representation on Λ C5.
Our next goal is to check that pulling back this representation from SU(5) to GSM
using φ, we obtain the Standard Model representation F ⊕F ∗.
As we do this, we will see another fruit of the SU(5) theory ripen. Th e triviality
of Z6 already imposed some structure on hypercharges, as outlined abo ve in Table 3.
As we ﬁt the fermions into Λ C5, we will see this is no accident: the hypercharges
have to be exactly what they are for the SU(5) theory to work.
To get started, our strategy will be to use the fact that, being re presentations
of compact Lie groups, both the fermions F ⊕F ∗ and the exterior algebra Λ C5 are
36
completely reducible, so they can be written as a direct sum of irreps . We will then
match up these irreps one at a time.
The fermions are already written as a direct sum of irreps, so we nee d to work
on Λ C5. Now, any element g ∈ SU(5) acts as an automorphism of the exterior
algebra Λ C5:
g(v ∧w) = gv ∧gw
where v,w ∈ Λ C5. Since we know how g acts on the vectors in C5, and these
generate Λ C5, this rule is enough to tell us how g acts on all of Λ C5. This action
respects grades in Λ C5, so each exterior power in
Λ C5 ∼
= Λ 0C5 ⊕ Λ 1C5 ⊕ Λ 2C5 ⊕ Λ 3C5 ⊕ Λ 4C5 ⊕ Λ 5C5
is a subrepresentation. In fact, these are all irreducible, so this is how Λ C5 breaks
up into irreps of SU(5). Upon restriction to GSM, some of these summands break
apart further into irreps of GSM.
Let us see how this works, starting with the easiest cases. Λ 0C5 and Λ 5C5
are both trivial irreps of GSM. There are two trivial irreps in the Standard Model
representation, namely ⟨νR⟩ and its dual ⟨
νL⟩, where we use angle brackets to stand
for the Hilbert space spanned by a vector or collection of vectors. So, we could select
Λ 0C5 = ⟨νL⟩ and Λ 5C5 = ⟨νR⟩, or vice versa. At this juncture, we have no reason
to prefer one choice to the other.
Next let us chew on the next piece: the ﬁrst exterior power, Λ 1C5. We have
Λ 1C5 ∼
= C5
as vector spaces, and as representations of GSM. But what is C5 as a representation
of GSM? The Standard Model gauge group acts on C5 via the map
φ: (α,g,h ) ↦− →
(
α3g 0
0 α−2h
)
.
Clearly, this action preserves the splitting into the ‘isospin part’ and the ‘color part’
of C5:
C5 ∼
= C2 ⊕ C3.
So, let us examine these two subrepresentations in turn:
• The C2 part transforms in the hypercharge 1 rep of U(1): that is, α acts as
multiplication by α3. It transforms according to the fundamental representa-
tion of SU(2), and the trivial representation of SU(3). This seems to describe
a left-handed lepton with hypercharge 1.
• The C3 part transforms in the hypercharge − 2
3 rep of U(1): that is, α acts
as multiplication by α−2. It transforms trivially under SU(2), and according
to the fundamental representation of SU(3). Table 1 shows that these are the
features of a right-handed down quark.
In short, as a rep of GSM, we have
C5 ∼
= C1 ⊗ C2 ⊗ C ⊕ C− 2
3
⊗ C ⊗ C3
and we have already guessed which particles these correspond to. The ﬁrst summand
looks like a left-handed lepton with hypercharge 1, while the second is a right-handed
quark with hypercharge − 2
3 .
37
Now this is problematic, because another glance at Table 1 reveals th at there is
no left-handed lepton with hypercharge 1. The only particles with hy percharge 1
are the right-handed antileptons, which span the representation
⟨
e+
R
νR
⟩
∼
= C1 ⊗ C2∗ ⊗ C.
But wait! SU(2) is unique among the SU( n)’s in that its fundamental rep C2 is
self-dual:
C2 ∼
= C2∗.
This saves the day. As a rep of GSM, C5 becomes
C5 ∼
= C1 ⊗ C2∗ ⊗ C ⊕ C− 2
3
⊗ C ⊗ C3
so it describes the right-handed antileptons with hypercharge 1 an d the right-handed
quarks with hypercharge − 2
3 . In other words:
Λ 1C5 ∼
= C5 ∼
=
⟨
e+
R
νR
⟩
⊕ ⟨dR⟩
where we have omitted the color label on dR to save space. Take heed of this: ⟨dR⟩
is short for the vector space ⟨dr
R,dg
R,db
R⟩, and it is three-dimensional.
Now we can use our knowledge of the ﬁrst exterior power to comput e the second
exterior power, by applying the formula
Λ 2(V ⊕W ) ∼
= Λ 2V ⊕ (V ⊗W ) ⊕ Λ 2W.
So, let us calculate! As reps of GSM we have
Λ 2C5 ∼
= Λ 2(C1 ⊗ C2 ⊗ C ⊕ C− 2
3
⊗ C2 ⊗ C3)
∼
= Λ 2(C1 ⊗C2 ⊗C) ⊕ (C1 ⊗C2 ⊗C)⊗(C− 2
3
⊗C⊗C3) ⊕ Λ 2(C− 2
3
⊗C⊗C3).
Consider the ﬁrst summand, Λ 2(C1 ⊗ C2 ⊗ C). As a rep of SU(2) this space
is just Λ 2C2, which is the one-dimensional trivial rep, C. As a rep of SU(3) it is
also trivial. But as a rep of U(1), it is nontrivial. Inside it we are juxtap osing two
particles with hypercharge 1. Hypercharges add, just like charge s, so the composite
particle, which consists of one particle and the other, has hypercharge 2. So, as a
representation of the Standard Model gauge group we have
Λ 2(C1 ⊗ C2 ⊗ C) ∼
= C2 ⊗ C ⊗ C.
Glancing at Table 1 we see this matches the left-handed positron, e+
L . Note that the
hypercharges are becoming useful now, since they uniquely identif y all the fermion
and antifermion representations, except for neutrinos.
Next consider the second summand:
(C1 ⊗ C2 ⊗ C) ⊗ (C− 2
3
⊗ C ⊗ C3).
Again, we can add hypercharges, so this representation of GSM is isomorphic to
C 1
3
⊗ C2 ⊗ C3.
38
This is the space for left-handed quarks of hypercharge 1
3 , which from Table 1 is:
⟨ uL
dL
⟩
where once again we have suppressed the label for colors.
Finally, the third summand in Λ 2C5 is
Λ 2(C− 2
3
⊗ C ⊗ C3).
This has isospin − 4
3 , so by Table 1 it had better correspond to the left-handed
antiup antiquark, which lives in the representation
C− 4
3
⊗ C ⊗ C3∗.
Let us check. The rep Λ 2(C− 2
3
⊗ C ⊗ C3) is trivial under SU(2). As a rep of SU(3)
it is the same as Λ 2C3. But because SU(3) preserves the volume form on C3, taking
Hodge duals gives an isomorphism
ΛpC3 ∼
= (Λ 3−pC3)∗
so we have
Λ 2C3 ∼
= (Λ 1C3)∗ ∼
= C3∗
which is just what we need to show
Λ 2(C− 2
3
⊗ C3) ∼
= C− 4
3
⊗ C ⊗ C3∗ ∼
= ⟨
uL⟩.
In summary, the following pieces of the Standard Model rep sit inside Λ 2C5:
Λ 2C5 ∼
= ⟨e+
L ⟩ ⊕
⟨ uL
dL
⟩
⊕ ⟨
uL⟩
We are almost done. Because SU(5) preserves the canonical volum e form on C5,
taking Hodge duals gives an isomorphism between
ΛpC5 ∼
= (Λ 5−pC5)∗
as representations of SU(5). Thus given our results so far:
Λ 0C5 ∼
= ⟨
νL⟩
Λ 1C5 ∼
=
⟨
e+
R
νR
⟩
⊕ ⟨dR⟩
Λ 2C5 ∼
= ⟨e+
L ⟩ ⊕
⟨ uL
dL
⟩
⊕ ⟨
uL⟩
we automatically get the antiparticles of these upon taking Hodge du als,
Λ 3C5 ∼
= ⟨e−
R⟩ ⊕
⟨
dR
uR
⟩
⊕ ⟨uR⟩
Λ 4C5 ∼
=
⟨ νL
e−
L
⟩
⊕ ⟨
dL⟩
Λ 5C5 ∼
= ⟨νR⟩.
39
So Λ C5 ∼
=F ⊕F ∗, as desired.
How does all this look in terms of the promised binary code? Remember , a 5-bit
code is short for a wedge product of basis vectors u,d,r,g,b ∈ C5. For example,
01101 corresponds to d ∧r ∧b. And now that we have found an isomorphism Λ C5 ∼
=
F ⊕F ∗, each of these wedge products corresponds to a fermion or antif ermion. How
does this correspondence go, exactly?
First consider the grade-one part Λ 1C5 ∼
= C2 ⊕ C3. This has basis vectors
called u,d,r,g, and b. We have seen that the subspace C2, spanned by u and d,
corresponds to ⟨
e+
R
νR
⟩
.
The top particle here has isospin up, while the bottom one has isospin d own, so we
must have e+
R = u and
νR = d. Likewise, the subspace C3 spanned by r,g and b
corresponds to
⟨dR⟩ = ⟨dr
R,dg
R,db
R⟩.
Thus we must have dc
R =c, where c runs over the colors r,g,b .
Next consider the grade-two part:
Λ 2C5 ∼
= ⟨e+
L ⟩ ⊕
⟨ uL
dL
⟩
⊕ ⟨
uL⟩.
Here e+
L lives in the one-dimensional Λ 2C2 rep of SU(2), which is spanned by the
vector u ∧d. Thus, e+
L = u ∧d. The left-handed quarks live in the C2 ⊗ C3 rep
of SU(2) × SU(3), which is spanned by vectors that consist of one isospin and o ne
color. We must have uc
L = u ∧c and dc
L = d ∧c, where again c runs over all the
colors r,g,b . And now for the tricky part: the
uL quarks live in the Λ 2C3 rep of
SU(3), but this is isomorphic to the fundamental representation o f SU(3) on C3∗,
which is spanned by antired, antired and antiblue:
r =g ∧b, g =b ∧r, b =r ∧g.
These vectors form the basis of Λ 2C3 that is dual to r,g, and b under Hodge duality
in Λ C3. So we must have
uc
L =
c
where c can be any anticolor. Take heed of the fact that c is grade 2, even though
it may look like grade 1.
To work out the other grades, note that Hodge duality correspon ds to switching
0’s and 1’s in our binary code. For instance, the dual of 01101 is 1001 0: or written
in terms of basis vectors, the dual of d ∧r ∧b isu ∧g. Thus given the binary codes
for the ﬁrst few exterior powers:
Λ 0C5 Λ 1C5 Λ 2C5
νL = 1 e+
R =u e +
L =u ∧d
νR =d u c
L =u ∧c
dc
R =c d c
L =d ∧c
uc
L =
c
taking Hodge duals gives the binary codes for the rest:
40
Λ 3C5 Λ 4C4 Λ 5C5
e−
R =r ∧g ∧b e −
L =d ∧r ∧g ∧b ν R =u ∧d ∧r ∧g ∧b
uc
R =d ∧
c ν L =u ∧r ∧g ∧b
d
c
R =u ∧
c d
c
L =u ∧d ∧
c
uc
R =u ∧d ∧cPutting these together, we get the binary code for every particle and antiparticle
in the ﬁrst generation of fermions. To save space, let us omit the we dge product
symbols:
The Binary Code for SU(5)
Λ 0C5 Λ 1C5 Λ 2C5 Λ 3C5 Λ 4C4 Λ 5C5
νL = 1 e+
R =u e +
L =ud e −
R =rgb e −
L =drgb ν R =udrgb
νR =d u c
L =uc
uc
R =d
c ν L =urgb
dc
R =c d c
L =dc
d
c
R =u
c d
c
L =ud
c
uc
L =
c u c
R =udcTable 4: Binary code for ﬁrst-generation fermions, where c =r,g,b andc =gb,br,rg
Now we can see a good, though not decisive, reason to choose Λ 0C5 ∼
=
νL. With
this choice, and not the other, we get left-handed particles in the e ven grades, and
right-handed particles in the odd grades. We choose to have this pattern now, but
later on we need it.
Table 4 deﬁnes a linear isomorphism f :F ⊕F ∗ → Λ C5 in terms of the basis
vectors, so the equations in this table are a bit of an exaggeration. When we write
say,e+
R = u, we really mean f (e+
R) = u. This map f is an isomorphism between
representations of GSM. It tells us how these representations are the ‘same’.
More precisely, we mean these representations are the same when we identify
S(U(2) × U(3)) with GSM/Z6 using the isomorphism induced by φ. In general, we
can think of a unitary representation as a Lie group homomorphism
G → U(V )
whereV is a ﬁnite-dimensional Hilbert space and U( V ) is the Lie group of unitary
operators onV . In this section we have been comparing two unitary representatio ns:
an ugly, complicated representation of GSM:
GSM → U(F ⊕F ∗)
and a nice, beautiful representation of SU(5):
SU(5) → U(Λ C5).
We built a homomorphism
φ:GSM → SU(5),
41
so it is natural to wonder if is there a fourth homomorphism
U(F ⊕F ∗) → U(Λ C5)
such that this square:
GSM
φ /d47/d47
/d15/d15
SU(5)
/d15/d15
U(F ⊕F ∗) /d47/d47 U(Λ C5)
commutes.
Indeed, we just showed this! We have seen that there exists a unit ary operator
from the Standard Model rep to Λ C5, say
f :F ⊕F ∗ ∼
→ Λ C5,
such that the induced isomorphism of the unitary groups,
U(f ): U(F ⊕F ∗)
∼
→ U(Λ C5),
makes the above square commute. So, let us summarize this result a s a theorem:
Theorem 1. The following square commutes:
GSM
φ /d47/d47
/d15/d15
SU(5)
/d15/d15
U(F ⊕F ∗)
U(f ) /d47/d47 U(Λ C5)
where the left vertical arrow is the Standard Model represen tation and the right one
is the natural representation of SU(5) on the exterior algebra of C5.
