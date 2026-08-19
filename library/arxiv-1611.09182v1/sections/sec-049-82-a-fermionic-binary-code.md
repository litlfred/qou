---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-049-82-a-fermionic-binary-code
section_title: "A fermionic binary code"
section_number: 8.2
pages: 71-76
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
It turns out that there is a very eﬃcient way of describing the standard model’s fermions,
which is helpful in understanding SU (5), Spin(10), Pati-Salam theories, and incidentally,
also upcoming R⊗ C⊗ H⊗ O models based on Cl(12). This is in terms of a binary code,
[7], [64]. For a thorough explanation of this topic, the reader is encouraged to consult [7].
This fermionic binary code can be thought of as a sequence of answers to ﬁve diﬀerent
yes or no questions:
63
Is the fermion red?
Is the fermion green?
Is the fermion blue?
Does the fermion have isospin up?
Does the fermion have isospin down?
The set of answers to these ﬁve questions can be represented by an exterior algebra,
ΛC5, which is 2 5 = 32-complex dimensional. For example, a fermion which is red, r, and
has isospin up, u, would be represented by r∧u. A fermion which is said to be both red,
r, and blue, b, and has both isospin up, u, and isospin down, d, would be represented by
r∧b∧u∧d, and so on. (It may seem odd for a particle to be both red and blue, or to
have both isospin up and isospin down, but this should become clear shortly.) Please see
Figure 8.1.
1
bg ur d
g^ b b^ r r ^ u r ^ dr ^ g g ^ u g ^ db ^ u b ^ d u ^ d
r^ g ^ b r ^ g ^u r ^ g ^ db ^ r ^ ug ^ b ^ u g ^ b ^ d g ^ u ^ d b ^ u ^ d
r ^ g ^b ^u r ^ g ^b ^ d r ^ g ^u ^ db^ r ^u ^ dg^ b ^u ^d
b^ r ^ d r ^ u ^ d
r ^ g ^b ^u ^ d
Figure 8.1: The exterior algebra Λ C5, representing a fermionic binary code.
Now, complex linear combinations of the basis vectors,r, g, b, u, d,may be acted upon
by SU (5), where they form the irreducible representation, 5 . By extension, the bivectors
of ΛC5 form the 10, the three-vectors form the 10∗, the four-vectors form the 5∗, whereas
both the unit, 1, and the ﬁve-vector form singlets. We then see that we have exactly
64
the right SU (5) representations to describe one generation of standard model particles,
together with the right-handed neutrino, including all corresponding antiparticles. Please
see Figure 8.2.
1
bg ur d
g^ b b^ r r ^ u r ^ dr ^ g g ^ u g ^ db ^ u b ^ d u ^ d
r^ g ^ b r ^ g ^u r ^ g ^ db ^ r ^ ug ^ b ^ u g ^ b ^ d g ^ u ^ d b ^ u ^ d
r ^ g ^b ^u r ^ g ^b ^ d r ^ g ^u ^ db^ r ^u ^ dg^ b ^u ^d
b^ r ^ d r ^ u ^ d
r ^ g ^b ^u ^ d
1
5
10
10
5
1
*
*
SU(5)
Figure 8.2: The exterior algebra Λ C5, representing a fermionic binary code, broken
down into irreps of SU (5). Here, basis elements which are part of the same irreducible
representations are connected by red lines.
Upon spontaneous symmetry breaking, the 5 breaks into
(
3, 1,− 1
3
)
and
(
1, 2, 1
2
)
,
and the rest of Λ C5 can then be seen to follow suit. This then allows us to identify each
element of ΛC5 with one of the standard model’s fermions, as shown in Figure 8.3.
Readers may notice that SU (5) respects the grading of Λ C5, and that all left-handed
particles reside in the even grades, while all right-handed particles reside in the odd grades.
8.3 Spin(10) uniﬁcation
Although the SU (5) model was able to draw together the three gauge groups of the stan-
dard model into a single group, it only partially uniﬁed the standard model’s fermions into
65
1
bg ur d
g^ b b^ r r ^ u r ^ dr ^ g g ^ u g ^ db ^ u b ^ d u ^ d
r^ g ^ b r ^ g ^u r ^ g ^ db ^ r ^ ug ^ b ^ u g ^ b ^ d g ^ u ^ d b ^ u ^ d
r ^ g ^b ^u r ^ g ^b ^ d r ^ g ^u ^ db^ r ^u ^ dg^ b ^u ^d
b^ r ^ d r ^ u ^ d
r ^ g ^b ^u ^ d
d R
r d R
g d R
b e R
+ v R
v L
u L
r u L
g u L
b u L
r u L
g u L
b d L
r d L
g
d L
b e L
+
e R
-
d R
r dR
g d R
b u R
r u R
g u R
b u R
r u R
g u R
b
v L e L
-
d L
r d L
g
d L
b
v R
Figure 8.3: The exterior algebra Λ C5, representing a fermionic binary code, with the
corresponding standard model particles written underneath. Here, basis elements which
are part of the same irreps under GSM are connected by blue lines.
the 5∗ and the 10 . One might wonder if an alternate Lie group might exist, which could
fully unify not only the standard model’s gauge bosons, but also its fermions.
One Lie group which does hit the mark isSpin(10). The Spin(10) grand uniﬁed theory
is more commonly known in the literature as the “ SO(10)” model, and was proposed by
H. Georgi in 1974/1975, [37], and independently by H. Fritzsch and P. Minkowski in 1975,
[31].
Spin(10) is the double cover of the group SO(10), and is of rank 5, [48]. It uniﬁes the
standard model’s gauge group, and extends it from 12 dimensions to 45. A generation of
quarks and leptons in this model is uniﬁed into a 16-dimensional spinor, with a conjugate
spinor accounting for the required anti-particles. This spinor representation can be seen
to naturally account for a right-handed neutrino, [7].
The group, Spin(10), is associated with the Cliﬀord algebra Cl(10), which has an
irreducible representation given by a 32-dimensional Dirac spinor. Under Spin(10), this
Dirac spinor breaks down into two irreducible representations, known as Weyl spinors,
which are each 16-dimensional. Now, it can be shown, [7], that Dirac spinors of the group
66
Spin(2n) can be represented by the exterior algebra, Λ Cn. Hence, we see that the exterior
algebra, Λ C5, which we just described in the previous section, is capable of acting not
only as a representation of SU (5), but also as a representation of Spin(10). Please see
Figure 8.4.
Readers may recognize that this same pattern has appeared more than once in this
thesis. That is, minimal left ideals, such as Ψ L and Su, have been built using raising
operators of the Cliﬀord algebras Cl(2) and Cl(6), respectively. These raising operators
may be viewed as generating exterior algebras. For example, by looking at equation (6.19)
of Section 6.4, it is easy to see how the Dirac spinor, Su, is built from the exterior algebra,
ΛC3, generated by α†
1, α†
2, and α†
3.
1
bg ur d
g^ b b^ r r ^ u r ^ dr ^ g g ^ u g ^ db ^ u b ^ d u ^ d
r^ g ^ b r ^ g ^u r ^ g ^ db ^ r ^ ug ^ b ^ u g ^ b ^ d g ^ u ^ d b ^ u ^ d
r ^ g ^b ^u r ^ g ^b ^ d r ^ g ^u ^ db^ r ^u ^ dg^ b ^u ^d
b^ r ^ d r ^ u ^ d
r ^ g ^b ^u ^ d
d R
r d R
g d R
b e R
+ v R
v L
u L
r u L
g u L
b u L
r u L
g u L
b d L
r d L
g
d L
b e L
+
e R
-
d R
r dR
g d R
b u R
r u R
g u R
b u R
r u R
g u R
b
v L e L
-
d L
r d L
g
d L
b
v R
Spin(10)
16
16
R
L
Figure 8.4: The exterior algebra Λ C5, representing a fermionic binary code, with the cor-
responding standard model particles written underneath. Here, basis elements connected
by lines in the even part of the algebra form one irreducible representation underSpin(10),
with left-handed chirality. Similarly, those basis elements in the odd part of the algebra
form another irreducible representation under Spin(10), with right-handed chirality.
Now, it can be shown that our representation of SU (5) resides inside that of Spin(10),
[7]. As with SU (5), the group Spin(10) can be seen to respect the chirality of particles; it
does not mix left- and right-handed species. However, it does not respect the grading of
67
ΛC5, as do SU (5) and GSM .
