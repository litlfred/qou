---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-004-existence-and-spherical-morse-functions
section_title: "Existence and Spherical Morse Functions"
section_number: null
pages: 26-32
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Definition 3.2.1.LetMbe a compact oriented manifold possibly with boundary∂M
andf:M→Ra Morse function. We say thatfis
•“admissible” iff:M→[a,b] such thataandbare regular values and∂M=
f−1(a)∪f −1(b);
•“excellent” if all critical values are distinct;
•“spherical” if all regular level sets are disjoint unions of spheres.
Standard Cerf theory, introduced in [Cer70], shows that two such admissible Morse
functionsf 0,f 1∈C ∞(M) are connected by a pathf t which fails to be “excellent”
Morse only at finitely many points. For a short working exposition in the context of
topological field theories, see the notes by [Fre12]. Passing through these bad points,
the Morse function goes through either a birth-death singularity or a critical values
exchange. We are interested in classifying those singularities whose regular level sets
are disjoint unions ofS 2, the defining feature of CF generators.
Proposition 3.2.2.CandFgenerators satisfy commutative Frobenius relations.
Proof.We handle the proof in two parts. The first part handles relations due to birth-
death singularities, and the second part handles exchanges.
1. A birth-death singularity is the creation/annihilation of a pair of critical points
whose indices are adjacent (i,i+ 1),i= 0,1,...,dim(M). In 3 dimensions, the
possible birth-death singularities are between (0,1), (1,2), and (2,3). Near the
birth of these singularities, the pathf t has the local form (up to a constant)
ft(x,y,z) =x 3−tx±y 2±z 2, t∈[−1,1].
More specifically, for (0,1) birth 1, the local form is
ft(x,y,z) =x 3−tx+y 2 +z 2.
where the two critical points are (±
q
t
3,0,0) of index 0,1 respectively. Geometri-
cally, consider filling one of the missing 3-balls inS 3\int(D 3⊔D 3⊔D 3), resulting
inS 3\int(D 3⊔D 3).
The former is a representative of the pair of pants bordismm, while the latter is
diffeomorphic toS 2×Iwhich is a representative for the identity morphismid S2.
The filling 3-ball is a representative of the unit bordism 1. The first equality in
figure 3.1 provides a familiar geometric intuition. The local form of the birth of
(0,1) critical points encodes the geometric fact that 1 is the unit with respect to
the multiplication:
m◦(1⊗id S2)∼=idS2.
The local form for the birth of (2,3) critical points is
ft(x,y,z) =x 3−tx−y 2−z 2.
1For the death version, takef −t
26
∼= ∼=
S2×I
Figure 3.1: The birth and death of a pair of critical points of index (0,1) and (2,3). The
first equality, when read from left to right, shows the death of critical points of indices 0 and
1. One can imagine pushing the left cone up until the bottom tip is level with the crouch of
the pair of pants, then smoothly deform the result into a straight cylinder. When read from
right to left, it depicts the birth of critical points of indices 0 and 1. The second equality
when read from left to right depicts the birth of 2 and 3.
which corresponds to the same picture but turned upside down as illustrated in
figure 3.1 as the second equality, encoding the geometric fact thattris the counit
with respect to co multiplication 2:
(tr⊗id S2)◦m ∨∼=idS2.
2. This part of the proof is inspired by [Fre12]. By a classic theorem in Morse theory
[Hir76] Thm 3.4 and 3.5, iff: cM→[a,b] is a Morse function on a closed manifold
cM, andv k is the number of critical points offof indexk, then
χ(cM) =
dim(M)X
k=0
(−1)kvk.
We want to classify all possible connected bordisms before and after exchanges
of two critical values. We demand such a bordism has two critical points at all
times along the Cerf pathf t. Let (i,j) denote the indices of the critical points
whose critical values are exchanged. We know that neitherinorjcan be 0 –
indeed, at the singular time when the critical values coincide, the critical level set
must be connected. Otherwise it takes a handle attachment to connect the index
0 critical point to the other critical point, which is only possible ifMhas at least
3 critical points.
A similar argument shows that neitherinorjcan be 3.
2Strictly speaking, the left side needs to be pre-composed with a unitor. We shall ignore the unitors and
associators for this part of the proof for clarity. However much of the rest of the paper work with them more
carefully and explicitly.
27
So there are only three possible exchanges we need to classify: indices (1,1), (1,2),
and (2,2) exchanges. The (2,1) exchange is the reversal of the (1,2) exchange by
takingf−t.
Sincemandm ∨ are the generators of index 1 and 2 in CF, we need only consider
relations involving these two generators. They respectively decreases/increases
the number of boundary components by 1. By using only two of them, the only
possible changes in incoming to outgoing boundary components is 1→1, 2→2,
3→1, and 1→3.
LetMbe such a bordism, and let cMbe the closed manifold one obtains by filling
in the boundary components. Then
0 =χ( cM) =v 0−v 1 +v 2−v 3.
wherev 0 is the number of incoming components andv 3 is the number of outgoing
components. 3
For the case of 3→1, we learn that−v 1 +v 2 =−2, and since we only have two
critical points onMat all times, the critical points being exchanged must have
indices (1,1). Therefore we are looking for two combinations of twom’s which
are both bordisms with three incoming and one outgoing boundary components.
There are only two, illustrated in figure 3.2-(a), which are the three dimensional
analogue of the associativity condition in two dimensions:
m◦(m⊗id S2)∼=m◦(id S2⊗m).
∼= ∼=
(a) (b)
Figure 3.2: (a) Associativity of multiplication. (b) Coassociativity of comultiplication.
3Secretely using the fact that one can glue two Morse functions together
28
For the case of 1→3, we learn that−v 1 +v 2 = 2, meaning the exchange is
of type (2,2), so we are looking for ways to compose twom ∨ which results in
one incoming and two outgoing boundary components. The only two possible
compositions illustrated in figure 3.2-(b) are the three dimensional analogue of
coassociativity in two dimensions:
(m∨⊗idS2)◦m ∨∼= (idS2⊗m∨)◦m ∨.
For the case of 2→2, we learn that−v 1 +v 2 = 0, so the exchange is of type
(1,2). The only two possible compositions of onemand onem ∨ which result
in a bordism from two incoming to two outgoing boundary components are the
analogue of the Frobenius relation:
m∨◦m∼= (m⊗id S2)◦(id S2⊗m∨).
This is depicted in figure 3.3.
∼=
Figure 3.3: Frobenius relation
So far we have demonstrated that CF has units, counits, associativity, coassocia-
tivity, and the Frobenius relation. By [Koc03] these are equivalent to the relations
which define a Frobenius algebra, namely these bordisms form the Frobenius PROP.
We have co/commutativity as well, upgrading to a commutative Frobenius relation.
All together we see that CF generators satisfy commutative Frobenius relations.
Remark3.2.3.It is worth drawing attention to the fact that even though type (1,2)
birth-death singularities are allowed by generic Cerf theory along pathf t connect-
ing two Morse functionsf 0,1 :M→R, it does not constitute a relation among the
CF generators– these generators, along with their pre-equipped Morse functions, have
spherical regular surfaces. However the local form of type (1,2) birth singularity is
given by
ft(x,y,z) =x 3−tx−y 2 +z 2, t∈[−1,1].
Fort <0 there are no critical points.t= 0 has a degenerate critical point at the
origin. Fort>0 there are two critical points (±
q
t
3,0,0), of index 1 and 2 respectively.
Letr∈f t(±
q
t
3,0,0) be a regular value, one can show that the regular level surface
29
Figure 3.4: The local picture of the regular surfacef −1(r) after the birth of a pair of critical
pointsc 1,2 of index 1 and 2, wheref(c 1)<r <f(c 2). Notice that this surface has genus at
least 1, hence is not spherical.
f−1
t (r) has genus at least 1 (see figure 3.4). Therefore there is no type (1,2) birth-death
relations between CF generators.
Cerf-theoretically, this means the type (1,2) birth-death singularities cannot occur
if we demand the pathf t between two “good” Morse functionsf 0,f 1 remains “good”
Morse. By “good” Morse here we mean spherical admissible Morse functions– whose
regular level sets are all disjoint unions of two-spheres.
Remark3.2.4.It is also worth noting that we did not treat the type 1→1 exchanges,
which has−v 1+v2 = 0, meaning the critical values being exchanged are of indices (1,2).
There is only one such bordism which is a composition of CF generators, analogous to
the pants decomposition of the torus in two dimensions in figure 3.5-(a) :
h
(S2×S 1)\int(D 3⊔D 3)
i
=m◦m ∨.
To understand what happens if one insists on a (1,2) exchange to occur, consider
the following Morse function introduced earlier in remark 2.0.8
S2×S 1 proj
−→S 1 Height
−→R.
The standard decomposition of this Morse function induces the composition
[S2×S 1] =tr◦m◦m ∨◦1
where the elementary bordisms are of index 3,1,2,0 respectively, in descending critical
value . If we exchange the critical values of the critical points whose indices are (1,2),
30
0
2
1
3 3
2
1
0
(a) (b)
Figure 3.5: Two different decompositions ofS 2×S 1. Figure (a) is the usual “pants” de-
composition which resembles the pants decomposition of a torus in 2-dimensions. A regular
surfacef −1(r), for anyrbetween the index 2 and 1 critical values, is the disjoint union
S2⊔S 2. In contrast, figure (b) is the (minimal) Heegaard decomposition, where a regular
surfacef −1(r), for anyrbetween the index 1 and 2 critical values, is a torus.
the indices would read 3,2,1,0 in descending critical value. But the only way to attach
a 1-handle to a ball would increase the bounding surface genus by 1. So the regular
surface between index 2 and 1 is a torus, and this Morse function gives the (minimal)
Heegaard splitting 5.2.4 ofS 2×S 1, illustrated in figure 3.5-(b).
While this type of exchange is perfectly normal in generic Cerf theory, it does not
give us a relation between CF generators, which requires that the Morse functions
before and after have no regular level set which has a non-zero genus component.
We will say more about this in example 1 after introducing an important lemma.
Lemma 3.2.5.Let[M]be a morphism inCob(3) S2,CF . Then there exists an admis-
sible excellent spherical Morse function on a representativeM.
Proof.Each CF generator comes with a standard Morse function which is spherical.
SinceMcomes with a decomposition in terms of glueing CF generators, we can glue
their Morse functions together in a collared neighbourhood of the glueing boundaries
after appropriate shifts. The resulting Morse function is by definition spherical and
admissible onM. If two critical values coincide, take a small perturbation of the Morse
function, rendering the values distinct and the function excellent.
Remark3.2.6.The lemma addresses the existence of an admissible excellent spherical
Morse function. It is always possible that there is a different composition, giving rise
to a different admissible excellent spherical Morse function onM. Given that these
compositions are the Morse data of two Morse functions, we know the full theory
31
of Cerf can be employed. Therefore these two compositions must be related by a
sequence of Cerf moves. However, the example below shows that we cannot maintain
the “spherical-ness” of the Cerf path in 3 dimensions. Therefore it raises the question
whether CF relations are sufficient. The next two sections ensure that they are indeed
sufficient.
Example 1.(S 2×S 1 Pants to Heegaard to Pants) Take any pants decomposition of
S2×S 1, induced by a Morse function we callf pants. There is a path fromf pants to
itself, which first exchanges the order of the 1-handle and 2-handle attachments, then
exchanges the order again, undoing the first switch. As we explained in remark 3.2.4,
a Morse function along the path after the first exchange has a toric regular level set
between the index 1 and 2 critical values, hence the interval between the two exchanges
are aspherical, corresponding to the minimal Heegaard splitting ofS 2×S 1. Figure 3.6
presents the Kirby graphics of this Cerf path.
3
0
2
1
3
0
2
1
3
0
2
1
| {z }
pants
| {z }
pants
| {z }
Heegaard Splitting
fpants fpantsfHeegaard
Figure 3.6: The Kirby graphics for a path atf pants :S 2×S 1 which fails to remain spherical
as it exchanges the index 1 and 2 critical points. After the exchange the Morse function
along the path segment now gives the genus 1 Heegaard splitting ofS 2×S 1.
