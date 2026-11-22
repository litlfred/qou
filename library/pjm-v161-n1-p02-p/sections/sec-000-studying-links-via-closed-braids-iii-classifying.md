---
doc_id: pjm-v161-n1-p02-p
doc_title: "Studying links via closed braids. III. Classifying links which are closed 3-braids"
section_id: sec-000-studying-links-via-closed-braids-iii-classifying
section_title: "STUDYING LINKS VIA CLOSED BRAIDS III: CLASSIFYING LINKS WHICH ARE CLOSED 3-BRAIDS"
section_number: null
pages: 2-22
source_pdf: pjm-v161-n1-p02-p.pdf
source_sha256: a93e922eab1ee67c
toc_source: inferred
doc_brief: "Studying links via closed braids. III. Classifying links which are closed 3-braids — 59 sections: Front matter; STUDYING LINKS VIA CLOSED BRAIDS I; it"
---
PACIFIC JOURNAL OF MATHEMATICS
Vol. 161, No. 1, 1993
STUDYING LINKS VIA CLOSED BRAIDS III:
CLASSIFYING LINKS WHICH ARE CLOSED 3-BRAIDS
JOAN S. BIRMAN AND WILLIAM W. MENASCO
A complete solution is given to the classification problem for ori-
ented links which are closed three-braids. The Classification Theo-
rem asserts that, up to a finite list of exceptional cases, links which
can be represented by closed 3-braids are represented by a unique
conjugacy class in the group of 3-braids. The exceptional cases are
the expected ones (links of braid index 1 and 2) and an unexpected
infinite family of invertible links, each member of which has two 3-
braid axes. The two axes correspond to diagrams which are related
by "braid-preserving flypes".
An algorithm is given which begins with an arbitrary closed 3-braid
(or alternatively any link diagram with 3 Seifert circles), and converts
it into a normal form which characterizes its oriented link type in
oriented 3-space. One can decide from the normal form whether the
link is prime or composite, split or irreducible, amphicheiral and or
invertible. One can decide if the braid index is 3, 2 or 1. Using
related results of P. J. Xu, one may determine the genus and construct
a surface of maximum Euler characteristic with boundary the given
link.
It is proved that the stabilization index of a link which is repre-
sented by a closed 3-braid is < 1, i.e. any two 3-braid representatives
of the same link type become conjugate after a single stabilization to
B4.
1. Introduction. This manuscript is the third in a series of six papers
in which the authors have been studying the closed braid representa-
tives of links. The other five are referenced here as [B-M I, II, IV-VI]
In [B-M, I] the authors prove that, with an appropriate definition of
the complexity of a closed braid representative of a link, there are
finitely many conjugacy classes of braids of minimum complexity. In
this paper we work out in detail the first non-trivial example of this
"finiteness theorem": we prove that for links of braid index n < 3
there are at most two conjugacy classes of minimum complexity. We
then use this result to give a complete numerical invariant of link type,
and an algorithm to find it, starting with an arbitrary closed 3-braid.
The complexity function which was used in [B-M, I] relates to in-
compressible surfaces which are bounded by the link. These surfaces
have maximum Euler characteristic, among all oriented surfaces with
25
26 
JOAN S. BIRMAN AND WILLIAM W. MENASCO
boundary the given oriented link. It was shown in [Be] and in [B-M,
II] that when the link has braid index < 3 these surfaces are especially
simple. As a result, the combinatorial data which was introduced in
[B-M, I] to describe the surfaces reduces to a cyclic word in a special
set of generators for the braid group B^. The algorithm which we
give then not only solves the link problem for links of braid index 3,
it also (with the help of results in [X]) provides a surface of maximal
Euler characteristic with boundary the given link. The long range goal
of the series of manuscripts [B-M, I-VI] is to generalize these results
to arbitrary braid index n .
Let JSP be an oriented link type in oriented S
3, let L be a rep-
resentative of S*, and let A be an oriented circle in S
3 — L. We
say that L is a closed n-braid with braid axis A if there is a choice
H = {H# θ e [0, 2π]} oΐafibration H of the open solid torus 
S
3-A
by meridian discs H# such that L intersects each H# transversally.
The number n is the number of points in L n H ^ . In 1923 James
Alexander proved in [Al] that every link could be so-represented,
in many ways and for many different values of n. The connection
between braids and links was further developed by Emil Artin. In
his 1925 manuscript [Ar] he introduced the n-string braid group Bn
(n = 1, 2, 3, ...) and uncovered its structure. In 1935 A. A. Markov
studied the disjoint union B^ of all the Bn 's, describing in [Ma] the
equivalence relation in B^ which relates all of the open braids whose
closures have the same oriented link type. Two elementary equiva-
lences are needed: conjugacy in Bn and a stabilization move which
changes n. In 1968 Garside [Ga] solved the conjugacy problem in
Bn . This was a highly non-trivial step in the translation of Markov's
equivalence relation into an algorithmic solution to the link problem.
The role of "stabilization" in Markov's equivalence relation (and
indeed in many other areas of low dimensional topology such as Hee-
gaard theory, bridge representations of links, Kirby's Calculus, and
Waldhausen's study of the Heegaard splittings of S
3) has been some-
what mysterious. The present investigation began with an attempt to
understand what is accomplished when one stabilizes, in the situation
of Markov's theorem. In the papers [B-M, I-VI] and subsequent ones
we hope to establish a version of Markov's theorem which does not
involve stabilization, i.e. in which one studies the braid representa-
tives of a link in Bn , for fixed n, rather than in the disjoint union
Boo of all of the braid groups. In this manuscript we do exactly that
for the first non-trivial case, n = 3. The classification of links which
STUDYING LINKS VIA CLOSED BRAIDS III 
27
are closed 3-braids follows immediately, as there are several known
algorithmic solutions to the conjugacy problem in £3 ([SC], [G], [X]),
each yielding unique normal forms for conjugacy classes.
By the work of Yamada [Y] links which are defined by closed n-
braids have an alternative interpretation as links which are defined by
diagrams with n Seifert circles. A computer program is now available
[F] which begins with an arbitrary link diagram with n Seifert circles
and produces from it a closed n-braid representative (in fact, for n =
3 the program gives a 3-braid which is defined by the special generators
&\, &2> #3 which are introduced in this paper). We also have a second
program which yields normal forms for conjugacy classes in B$. Thus
our results are very concrete.
Two other special cases of Markov's theorem without stabilization
are proved in [B-M, IV] (which is a study of the n-braid representa-
tives of split links and composite links) and [B-M, V] (where the n-
braid representatives of the r-component unlink are studied for fixed
n>r). 
The pathologies which are investigated in the three papers [B-
M, III], [B-M, IV] and [B-M, V], all come into play if one attempts
to generalize the results of this paper to higher braid index.
To state our result, let σ\ and σ-i be the standard elementary braids
which generate the 3-string braid group #3. The central result in this
paper may be stated in the following way:
THE CLASSIFICATION THEOREM (Version I). A link & which is rep-
resented by a closed 3-braid admits a unique conjugacy class of 3-braid
representatives, with the following exceptions:
(i) £? is the unknot, which has three conjugacy classes of 3-braid
representatives, namely the classes of σ\σ2, ^f
1^
1 
and σiσ^
1 •
(ii) & is a type (2, k) torus link, k Φ ±\, which has two conju-
gacy classes of 3-braid representatives, namely the classes of o\θ2 and
kσ-\
σ2
(iii) J2? is one of a special class of links of braid index 3 which have
3-braid representatives which admit "braid-preserving flypes". These
links have at most two conjugacy classes of 3-braid representatives,
namely the classes of σfσ|σ[σ| and σfσ|σ[σ|, where p, q, r are
distinct integers having absolute value at least 2 and where δ = ± 1 .
The exceptional cases (i) and (ii) are the expected ones, but (iii)
was not previously recognized except in special cases (see [Mu]). It is
σΐ
σ2
28
JOAN S. BIRMAN AND WILLIAM W. MENASCO
Q
0
FIGURE 1.1: A flype
P
twists
-r
1
\
q
twists
1
r
twists
s
1
\
"Ή. ί
L^-- 
-J
f
P
tv/ists
: ΓTct
H
I'
twists
V
1
b
V
- ι -
1
1
1
1
1
1
FIGURE 1.2: A braid-preserving flype
an infinite family of counterexamples to the long-standing conjecture
that the map from conjugacy classes in 2?3 to oriented link types was
injective on links of braid index 3. The examples in (iii) are especially
important because they generalize to related examples for every braid
index n > 3, so we discuss them briefly.
The left picture in Figure 1.1 shows part of a link diagram (enclosed
in a dotted oval). The right picture shows a different projection of
the same part of the diagram. The left and right pictures differ by
a flype. It is easy to see that diagrams which contain regions which
are related by flypes, but are identical everywhere else, determine the
same oriented link type. Figure 1.2 shows a pair of closed 3-braid
projections of the same link, related by a braid-preserving flype. The
flype occurs inside the disc which is bounded by the dotted curve.
During the flype the link L cuts through the braid axis A. Notice
that the defining open braids have the form of the examples given in
(iii) above.
Figure 1.3 shows the same phenomena from a different point of
view, exhibiting the braid axis A' as it would appear threaded into the
STUDYING LINKS VIA CLOSED BRAIDS III
29
Inequivalent axes for
n-braid structure on
FIGURE 
1.3
projection shown in the left picture of Figure 1.2. At the same time,
Figure 1.3 shows how flypes generalize to produce similar examples for
every n . The strands are labeled with integers n\, ni, ft 3, indicating
that the single strand which is illustrated is to be replaced by n\ > 1
parallel strands. Thus the braid which is labeled P in Figure 1.3 is
a braid on (n\ + πι) strands, and so-forth. The generalized braid in
Figure 1.3 has a very special form, even though P , Q and R are
arbitrary braids on the appropriate numbers of strands.
We wish to answer the question: when can S* be represented by
more than one conjugacy class in J53 ? We choose a representative L
of S*, and study the related geometric question: when can L have
two axes, A and A' for 3-braid structures, with A
r not isotopic to
A in S
3 - L ? We wish to show that this only happens under very
special circumstances. Since it is known exactly how many axes are
possible in the special cases when the braid index of 3* is 2 or 1, we
may assume (and shall do so from now on) that & has braid index
3. It will also be convenient to make the assumption that 3? is prime
and non-split, since composite and split links complicate the proof
even though it is well known (via the work of Murasugi in [Mu] and
Morton in [Mo, 1], or see [B-M, IV]) that composite and split links of
braid index 3 have unique conjugacy classes of 3-braid representatives.
Therefore, from now on, we assume that S* is prime, nonsplit and
has braid index 3.
The first step in our work is to attach extra structure to our braid
representatives. 
Let S be an oriented surface, with boundary an
30
JOAN S. BIRMAN AND WILLIAM W. MENASCO
Portion of F
embedded in 3-space
Foliation on
2 discs and
one of the bands
which joins them
Example
Benneαuin surfaces
FIGURE 1.4
oriented link K of braid index n. We call S a Bennequin surface
(see Figure 1.4) if the following conditions hold:
(i) S has maximal Euler characteristic χ(S), among all connected
oriented surfaces with boundary the oriented link K.
(ii) K = dS is a closed n-braid relative to the braid axis A and
to some choice of a fibration H of the open solid torus S
3 - A by
meridian discs.
(iii) S has a decomposition as a union of n discs, each pierced once
by A, joined up by half-twisted bands, each of which has exactly one
STUDYING LINKS VIA CLOSED BRAIDS III 
31
saddlepoint tangency with a fiber of H. Each disc is radially foliated
by its intersections with fibers of H.
Bennequin surfaces were introduced (implicitly) in Proposition 3
of [Be]. They diίfer from the obvious Seifert surface S' spanned by
a closed n-braid in the following way: Both S and S' have K as
boundary, and both are a union of n discs D i , . . . , D n joined up
by half-twisted bands; however the bands in S' are usually limited to
ones which join Dz to D/+i for each / = 1, 2, ... , « - 1, whereas in
a Bennequin surface S one may have half-twisted bands joining any
pair of discs D7 and D^ .
An arbitrary link Sf of braid index n may or may not have a
Bennequin spanning surface, but links of braid index 3 always do.
Even more it is proved in [B-M, II] that the following holds:
BENNEQUIN'S THEOREM (see [B-M, II]). Let <S? be prime and non-
split and have braid index 3. Let L be a representative which is a
closed 3-braid relative to the axis A. Let H = {Hθ 
θ e [0, 2π]} be
a fibration of the open solid torus S
3 - A by meridian discs. Then
any connected, oriented surface F' of maximal Euler characteristic
with boundary L is isotopic to a Bennequin surface F with the same
boundary, relative to H.
A Bennequin surface for a closed 3-braid has a natural decompo-
sition as a union of three horizontal discs joined up by half-twisted
bands. We label the discs Di, D 2 , D3 and let α, denote a half-twisted
band which joins D/ to D/+i (mod 3) > in the standard disc-band de-
composition of F relative to H. See Figure 1.5 (next page). Then F
and L = d¥ can be described by a cyclic word:
in the symbols a\, a-i, a^ and their inverses, which records the se-
quence of half-twisted bands encountered as the polar angle varies over
the interval [0, 2π]. This word describes the surface F as an embed-
ded surface in S
3 - A. It is a shortest such word because χ(¥) is max-
imal. This is one of the very nice features of Bennequin surfaces—the
braid word which describes L also describes a very nice spanning sur-
face F.
By hypothesis, our link Jϊ? has two axes A and A
; for 3-braid
structures, with associated fibrations H = {Hθ 
θ e [0, 2π]} and
H' = {H^ φ e [0, 2π]} . If we arrange things so that L = OF, where
32
JOAN S. BIRMAN AND WILLIAM W. MENASCO
I
elementary 3-braids
9i a, a.
projection onto the walls
of a cylinder, viewed from
inside the cqlinder
(dotted sides to be identified
in front of the visible braid)
FIGURE 
1.5
F is a Bennequin surface relative to H, then Bennequin's Theorem
tells us there is an isotopy h$ of S
3 , s G [0, 1 ], with /zn = identity
such that Ai(F) is a Bennequin surface relative to H'. Therefore,
by modifying the fibers of H as we modify F, replacing each h^ by
h\(Hθ), we obtain as an immediate corollary:
COROLLARY 1.1. We may assume that F is simultaneously a Ben-
nequin surface relative to both H and H'. Moreover, there is a sec-
ond shortest word W = W'{h), necessarily of the same length as
W = W(L), in generators b\y hi, Z?3 which describes the Bennequin
disc-band decomposition of F relative to H'.
We now describe the strategy of our proof of the Classification The-
orem, which is contained in §§2-6. Motivated by the results in an early
version of this paper, P. J. Xu has studied cyclically symmetric pre-
sentations of i?3 using the generators a\, a^, a^. She gives in [X]
an algorithm for finding a shortest representative for each conjugacy
class, and she also investigates the collection of all shortest words in
each conjugacy class. Using one of her results (see Lemma 2.2) we
show in §2 that we may choose among all Bennequin surfaces with a
given 3-braid as boundary ones with additional structure. Their defin-
ing words W and W have two properties: first, they have the shortest
possible syllable length, and second they use all three generators. We
call them "admissible" words.
In §3 we introduce additional geometric structure in the form of a
family Ω of essential discs which we call digons which "plug up the
STUDYING LINKS VIA CLOSED BRAIDS III 
33
holes" in the standard disc-band decomposition of F. The foliation
of the digons by their arcs of intersection with fibers of H and H
7
will be the key to our proof. The standard axis A is disjoint from
Ω and the foliation of each digon which is induced by the standard
fibration H is free of singularities in the interiors of the digons. The
non-standard axis A
7, however, may pierce Ω repeatedly, and we
need to understand the relationship of A
7 and the fibers of H
7 to Ω.
We prove that S
3 split along FuΩ is a union of three 3-balls Bi, B 2,
B3 and a solid torus T. We show that L has a natural "projection"
onto dΎ. We show that W can be determined from the projection
of L on <9T. We then prove that A
7, like A, may be assumed to be
disjoint from the union of all the digons.
In §4 we study the foliation of the digons which is induced by the
fibration H
7 of S
3-A'. 
We show that its singularities are very special,
and begin to show (see Corollary 4.9) how knowledge of the foliation
enables us to draw conclusions about W.
In §5 we show that we may assume that A
7 is inside T.
In §6 we use all of this structure to prove the Classification Theorem.
In §7 the Classification Theorem is translated into an algorithmic
solution to the link problem for links which are defined by closed
3-braids. The algorithm depends directly upon known solutions to
the conjugacy problem in B3. In addition to giving a unique and
complete invariant for links defined by closed 3-braids, the algorithm
answers other questions: Is J2?
7 invertible or amphicheiral or both? Is
the braid index 3, 2 or 1? Is £? split or composite? With the help of
[X], one can also answer the question: what is the genus of £? ? We
also prove that the stabilization index for two 3-braid representatives
of the same link is one.
Knowing a complete invariant for a class of links such as links of
braid index < 3, it is natural to ask how this invariant compares to
"Jones invariants" i.e. the Jones polynomial [J] and its generalizations.
We call a link type invariant a Jones invariant if it is constructed from
traces in matrix representations of the braid group. The key prop-
erty is that the traces in question change in a very simple way when
one changes the defining braid by the moves which generate Markov's
equivalence relation. It is to be expected that Markov equivalence
will imply the existence of trace identities in any representation of #3
which admits a Jones invariant. We discuss this question briefly at the
end of §7. We prove that, for any N > 0, there exist infinitely many
sets, each of which contains N distinct links of braid index 3 which
34 
JOAN S. BIRMAN AND WILLIAM W. MENASCO
share the same 2-variable Jones polynomial. It would be important
to know whether any finite collection of Jones invariants suffices to
classify links of braid index 3.
Section 8 contains a brief discussion of the closed braid representa-
tives of composite links of braid index 3. They have unique conjugacy
classes of 3-braid representatives; however our proof would have been
more complicated if we had included them in the main body of the
proof. That was a hint to us of pathology which needed to be under-
stood. That pathology will be investigated in detail in the next paper
in this series, [B-M, IV], which studies the closed braid representatives
of split and composite links.
REMARKS. (1) While links defined by closed 3-braids are special,
they are also in many ways a rich class of links. Their "crossing num-
bers" are unbounded, unlike the links of < 13 crossings which have
served as a principal source of examples for knot theorists up to now
(e.g. see the Appendix to [Ro]). "Most" of them are non-amphicheiral
and non-invertible (we will make this precise in §7). Their geometry
includes many examples of hyperbolic link spaces. Their Alexander
and Jones and Kauffman polynomials are special (see [J], [Ta], [Bi, 2]),
yet they are not fully understood at this writing, suggesting interesting
new questions for investigation.
(2) The Classification Theorem is striking for its simplicity, but our
proof is long. This raised a question which has troubled us repeatedly
during the four years when the work reported on here was in progress:
Knowing the correct statement of the Classification Theorem, it seems
possible that there is a very easy proof. For, if one has a finite collec-
tion of link type invariants which sufficed to distinguish link type for
the special class of links which are defined by closed 3-braids, then all
one would need to do would be to show that braids in distinct conju-
gacy classes defined links with distinct invariants. Unfortunately we
do not know of any such collection. It would be interesting to know
if there is such a collection, and in particular if there is one which is
adapted to the normal form in this paper.
Acknowledgment. We thank the Mathematics Department at Rut-
gers University Newark for its hospitality in hosting an extended sem-
inar in which we presented some of the details in this paper. In partic-
ular, we thank Lee Mosher, Ulrich Oertel, Mark Feighn, Jane Gilman,
Kay Tatsuoka, Rollie Trapp and Pei-Jun Xu. Their insights and ques-
tions were invaluable to us. We also wish to thank the referee, who
read our manuscript with great care and expertise.
STUDYING LINKS VIA CLOSED BRAIDS III 
35
2. Admissible words. In this section we begin the new work needed
for our proof of the Classification Theorem. Let <S?, L, F, A, A
7,
W, W be as in § 1. We say that W is admissible if W is a shortest
representative of its conjugacy class in 2?3, also if among all shortest
words it has shortest syllable length k, and finally if it involves all
three generators a\, a2 > #3 non-trivially.
LEMMA 2.1. Given any closed 3-braid L which represents a prime,
non-split link of braid index 3, there is a Bennequin surface F with
d¥ - L such that W = W(L) is admissible.
Proof. We may assume that L is the boundary of a Bennequin
surface F with defining word W. From this it follows that W is a
shortest representative of the conjugacy class of L, for if not the Euler
characteristic χ(F) would not be maximal. Among all Bennequin
surfaces with boundary L, assume we have chosen ours so that the
syllable length of W is also minimal. Then either W uses all three
generators, in which case we are done, or (up to conjugation by a
rotation which cyclically permutes the generators) we may assume that
W = {aι)P^a2)
p2(aι)P^ " (a2)
p2s, where each pt φ 0 and s > 1. If
s = 1 then £f is the connected sum of a type (2, p\) and a type
(2, p2) torus link, so s > 2. Thus W contains a subword
U
of syllable length 4.
Since the assertion of Lemma 2.1 can be proved for any choice of
orientations on J& and on 3-space, we may if necessary replace W by
its inverse for the purposes of the proof, so we may assume without
loss of generality that p$ > 0. Now observe the following relation
holds:
(2.1) 
a2ax = a3a2 = axa3.
But then, we may apply the relation a2a\ = a\a?> repeatedly to the
subword (a2)
pi{a\) of U, replacing it by {a\){a{)
pi. Thus U has the
equivalent form (a\)
pι
+ι(a^)
p^(aι)
p^~
ι(a2)
p4. 
Since W is by hypoth-
esis a shortest word and has shortest syllable length, each of the four
syllables in the new expression for U must be non-trivial, and the
lemma is proved. 
D
36 
JOAN S. BIRMAN AND WILLIAM W. MENASCO
For future use we record the following consequences of the relations
(2.1):
(2.2) (ai)
δ(ai±x)
δ(aiγ 
= (ai±ι)
r(ai)
δ(ai±ι)\ 
δ = ±l, any r φ 0.
(2.3) 
ai = 
(ai+ι)-
1(ai-l)(ai+ι)
(2.4) 
(fl/)
p(fl/-i) = (fl/-i)(fl/+i)
p, 
any p ,
(2.5) 
01-iβΓ
1 =fll"
1fl/+i
where ι = 1,2, 3 and subscripts are always understood to be mod 3.
P. J. Xu has taken a new look at the conjugacy problem in #3 and
has found a constructive procedure to determine all admissible words,
starting with an arbitrary representative of the conjugacy class of L.
She has proved the following important fact:
LEMMA 2.2 [X]. Any two shortest words W, W" which represent the
same conjugacy class in 2?3 are related by a finite sequence of shortest
words W = W o, ... , W/ = W" of shortest words, such that each W/
differs from W/_i by a single application of relations (2.1).
By Corollary 1.1 the surface F is a Bennequin surface with respect
to both H and H'. Therefore we can assign to it a second defining
word W in elementary braids b\, bi, 63 which describes the second
disc-band decomposition of F.
COROLLARY 2.3. We may assume that L = <9F, where F is a Ben-
nequin surface with defining words W (with respect to H) and W
(with respect to H'), such that both W and W are admissible.
Proof. By Corollary 1.1 we may assume that F is a Bennequin
surface relative to both H and H', with defining words W and W .
By Lemma 2.1, we may assume that W is admissible. If W
7 is too, we
are done. If not, we know from Lemma 2.1 that there is a Bennequin
surface relative to H' which has an admissible defining word W
;. By
Xu's Lemma 2.2 the words W and W" are related via a sequence
of shortest words, with adjacent members in the sequence differing
by a single application of relations (2.1). Since each of the relations
in (2.1) can be realized geometrically by an isotopy of F (a simple
picture will show this), there is an isotopy hs of S
3 taking F to a new
Bennequin surface Ai(F) which has the defining word W" relative to
STUDYING LINKS VIA CLOSED BRAIDS III
P 2
37
FIGURE 2.1
H'. As in the proof of Corollary 1.1, we may then replace each fiber
H<9 of H by h\(Hβ) in order to preserve the relationship of F to
H, to obtain a new surface with the desired properties. Thus we
could have assumed to begin with that both W and W were admis-
sible. 
D
We record and review notation which will be used throughout this
paper. Fibers in the standard (resp. non-standard) fibration will be
parametrized by polar angle θ (resp. φ). We will depict fibers of
H and H' so that their boundaries (the braid axes A and A') are
oriented clockwise, as in Figure 2.1. With this convention the polar
angle functions increase clockwise. The symbols Hθ, pj9¥iθ9 
... 9
(resp. Hφ, p'j, Fjψ, ...) will be used to indicate a non-singular fiber,
a point where the axis pierces F, an arc of intersection of the fiber
with F, ... in the standard (resp. non-standard) case. See Figure 2.1.
Braids will always be oriented top to bottom in our pictures, as in
Figure 1.5. The axes A and A' are oriented by the right hand rule,
relative to the given orientation on L. The outward-drawn normal
to F is also determined by the right hand rule relative to the given
orientation on L. Notice that with this convention the axes A and A'
pass from F~ to F
+ as they pierce F. A tangency of a fiber of H or
38 
JOAN S. BIRMAN AND WILLIAM W. MENASCO
H' is a positive (resp. negative) singularity if the sense of the oriented
normal bundle to F at the point of tangency agrees (resp. disagrees)
with the direction of increasing θ or φ. With this convention the
elementary braids depicted in Figure 1.5 are positive.
We will regard the surface F and its boundary, the link L as
being defined by two words: a standard word W in the elemen-
tary braids a\, ci2, a^ and their inverses, and a non-standard word
W' = W\b\, bι, 63) in elementary braids b\, b-χ, 63. There is
a homeomorphism h of S
3 which takes A' onto A, fibers of FT
onto fibers of H, and L onto a closed braid Λ(L) about the axis
A. The braid Λ(L) will be defined, up to conjugacy, by the word
X = W'(a\, aι, Λ3). Since A' is not isotopic to A in S
3 - L, this
implies that W and X represent distinct conjugacy classes in B3. As
we will see, most prime, non-split links of braid index 3 do not have
two such representatives, and none has more than two.
3. Digons. In this section we will introduce additional structure
into S
3 - L, beyond that provided by a Bennequin surface F. The
additional structure will be in the form of a set Ω of discs called
"digons" which are properly embedded in S
3 split along F. We will
prove that S
3 split along Fu Ω is a union of four components whose
closures are 3-balls Bi, B2, B3 and a solid torus T. (See Proposition
3.1.) We show that there is a natural and symmetric way to visualize
our 3-braid via a link diagram on the boundary <9T of the solid torus
(Proposition 3.2). We prove that the non-standard axis A' may be
assumed to be disjoint from all of the digons (Proposition 3.4).
We focus for the moment on the geometry determined by the stan-
dard axis A and fibration H. Consider the closure M of the 3-
manifold obtained by splitting S
3 open along F, dM = F
+ U F~,
F
+ n F~ = L. A disc Δ which is properly embedded in M will
be called a digon if Δ is essential and if dA meets L in exactly
two points. We now construct a collection Ω = {Δj(fc) 1 < k < rx?,
1 = 1,2,3} of digons. Let {D, , / = 1, 2, 3} be the discs in the stan-
dard disc-band decomposition of F and let {b/(fc) k = 1, 2, ... , r/}
be the bands which join discs D, and D / +i. The construction begins
with a rectangle • which is a model for a typical digon, its boundary
being divided into four arcs labeled e\, eι, ^3, ^4 in clockwise order
about d • . We want to attach • to F along d • . To describe the
attaching curves it will be convenient to think of the bands as rectan-
gles, the singular leaves in the standard foliation being parallel to the
sides and through the center of the band. In Figure 3.1(b) we have
STUDYING LINKS VIA CLOSED BRAIDS III
39
(a)Bands embedded in 5-space
LOO
c.
^ : : : : . 
^
y
. . £. . . 7^: .
K - T T - T
/ 
,
r
• •/• 
• 
-J
J
•jyyy-y'y-
\
<.
If the half-twist is positive 
If the half-twist is negative
(b) Digon attaching curves on b^k)
to D,
to D.
to D j + 1
(c) Digon attaching curves on Di
FIGURE 3.1
sketched two arcs ciλ and ci2 on the band b/(fc). Our rules are:
Attach β\ to F+ along Dz between bz (fc) and b/(fc+l),
close to L.
Attach e2 to b, (fc+ 1) along ci2.
Attach ^3 to F" along D / + 1 , between b/(fc + 1) and
b, (fc), close to L.
Attach ^4 to b, (fc) along c z l.
40
JOAN S. BIRMAN AND WILLIAM W. MENASCO
to D i + 1
to D.•i-i
Example of an embedded dίgon
FIGURE 3.2
The decomposition of F into
subsets Γ, 1", 2} 3
FIGURE 3.3
The intersections of the attaching curves with a typical disc are shown
in Figure 3.1 (c). The visible side is F
+ . Figure 3.1 (b) and (c) use solid
and dotted arcs to distinguish places where the digons are attached to
F
+ from places where they are attached to F~ .
An example is given in Figure 3.2 of a digon as it would appear
when F is imbedded in 3-space. Notice that each digon is properly
embedded in M and that the digons are pairwise disjoint. In particu-
lar, we have attached Δz (fc) to Dz along F
+ and to D/+i along F~ ,
to insure that A((k) nΔί+i(/c) is empty.
Figure 3.3 shows a decomposition of the surface F into subsurfaces
which are defined via the structure introduced here. We will need
it later (see the discussion before Lemma 3.3 and the proof of the
lemma).
On the other hand, if we regard the digons as subsets of S
3 rather
than as subsets of M, then distinct digons Δz(/c) and Δ;(m) may
intersect, but only in a very special way:
(i) Int(Ai(k))nAj(rn) 
= 0.
(ii) dAi(k)ΠdAj(m) 
= 0 unless \k-m\ = 1, and both digons pass
through the singular point on the band or bands which they share.
(iii) dAi(k) intersects <9Δz±1(m) in either 0, 1 or 2 points on the
disc Di.
Each digon Δ/(fc) crosses L twice, once on bj(k) and once on
bi(k + 1). The crossover points will be called crossing dots. The
crossing dots on b/(/c) cut off a subarc of L which we have labeled
Lz(/c) in Figure 3.1(b). There is one of these arcs on each band, the
one on the band bj(k) (resp. bt{k + 1)) having its endpoints on the
digons Aj(k - 1) and Aj(k) (resp. Δ/(/c) and Δ/(fc + 1)). The two
STUDYING LINKS VIA CLOSED BRAIDS III
L;(K) — — ^ 
i / \ 
degenerate leaf
41
crossing dots
degenerate leaf
standard foliation of Δ.(k)
FIGURE 3.4
crossing dots on the digon Δ/(fc) divide dA((k) into two sub-arcs,
one of which is in F
+ and the other in F~ . The subarc of L which
lies between the two crossing dots on b, (fc) is labeled L/(fc). There
is one such subarc of L on each band. We call these r, arcs the
undercrossing arcs (for reasons which will become clear shortly).
The fibration H induces a standard foliation of each digon Δ (fc).
The fact that F is in a very nice position relative to the axis A and
the fibers in H implies that this foliation may be assumed to be free
of singularities in the interior of Δ/(/c) (see Figure 3.4). There will,
however, necessarily be two degenerate leaves in the foliation. Notice
that the crossing dots are nearby to but do not coincide with the de-
generate leaves. A degenerate leaf can be in F
+ or in F~ . One of the
four possibilities has been illustrated in Figure 3.4. The undercrossing
arcs are of course transverse to the fibers of both H and H'.
PROPOSITION 3.1. S
3 split along F u Ω has four open components.
Their closures are 3-balls B{f B 2, B 3 and a solid torus T. The bound-
ary dBif 
i = 1,2,3, is made up of r, digonsf a disc subset of F+
which contains D/+i and a disc subset of F~ which contains Df . The
boundary dΊ is a union of r - rx+r2 + r3 digons and subsets of F
+
and F~.
Proof. We study how FuΩ meets a generic fiber Hθ of the standard
fibration H. See the top left picture in Figure 3.6 on p. 43, which is
the same as Figure 2.1 (a), but labeled to stress different aspects of the
42
JOAN S. BIRMAN AND WILLIAM W. MENASCO
singular point
——.... _L 
—v—-
FIGURE 3.5
geometry. We have added the intersections of HΘ with the digons, i.e.
the three arcs λχθ , λ2θ , hθ By
 0 U Γ r u l
e s f°
r attaching the digons to
F, the arc λiθ begins on the plus side of ¥iθ and ends on the minus
side of F z + 1 6>. Thus, if θ is non-singular, Hθ split along HθΓ\(¥\jΩ)
will be four discs, labeled Biθ, B2Θ , B30 and T# . The 3-balls B!,
B2 , B3 and the solid torus T are defined to be the regions swept out
by B10, B2Θ, B 3 0 and Ίθ as θ is varied from θ\ to 
θ\+2π.
The only possible complication in the above description is that as
θ is varied we will pass through singular fibers and crossing dots,
so we need to be sure our four discs are always well-defined. Some
preliminary remarks are in order. See Figure 3.5. Let S\ be a surface
and S2(φ) a family of surfaces, with S\ transverse to S2(Φ) except
at φ — φo, where a saddle point tangency occurs. Then there are arcs
x and y in S\ ^ΛS2{φ) which coalesce as φ —• ΦQ. We show in Figure
3.5 a pair of joining arcs a(φ) and β(φ) and a disc A(φ) which the
joining arcs cobound. As φ —• φo the joining arcs and the disc shrink
to points. The joining arcs are a convenient way to describe the future
singularity.
Now see the eight snapshots in Figure 3.6. We have chosen to
illustrate a positive singularity of type a2 (which occurs at 0 = 0 5).
Our conventions dictate that for a positive singularity between the
disc D 2 and D 3 in the standard disc-band decomposition of F the
joining arc β (illustrated at θ\ as a dotted arc, but omitted from
succeeding pictures) runs between the negative sides of F20 and F30 .
As we approach the instant of the singularity, this arc shrinks to a
point. The arc λ2θ will also shrink to a point as we pass through
the band, because the attaching curves for the digons run through the
singularities of F. Therefore, just before the instant of degeneracy the
endpoint of λ2θ which is on F
+ must "migrate" from the + to the -
STUDYING LINKS VIA CLOSED BRAIDS III
43
FIGURE 3.6
side of F 20, as it has done in the passage from 02 to Θ4. A crossing
dot lies on the fiber at 0 3. At the instant of crossover the digon will
intersect L, and the intersection point (illustrated earlier in Figures
3.1-3.4) is one of the crossing dots. The F-singularity occurs at θ5.
At #6 the arcs of F n Hβ draw apart again, but in a new way. At θη
the arc λ2β migrates across L a second time, now from the - side
to the + side of F 3#, to restore the generic configuration at θ$. It
is clear from these pictures that the discs Bϊθ, 
B2Θ , B3# and Ύθ are
well-defined, even at 0 3, θ5 and ΘΊ. The fact that the region swept
out by T# is a solid torus results from the fact that ΎΘΓ\ΎΘ> is empty
if θ φ θ
f. On the other hand, if we denote the subarc of A which
runs between pt and p / + 1 by A/, / = 1, 2, 3, then Biθ nBiθ» = A/
for all (9, <9'e[0,2π]. 
D
44
JOAN S. BIRMAN AND WILLIAM W. MENASCO
Typical 2-sphere dB^
viewed from inside B.
Decomposition of F into subsets
Γ, 1", 2 and 3, viewed on dBj
FIGURE 3.7
PROPOSITION 3.2. There is a natural diagram for L on the bound-
ary dΊ of the said torus T, visible to an observer who is inside T.
The overcrossing arcs are on dT. The undercrossing arcs are the arcs
{Lt(k), 
k = 1, ... , n:, ι = l , 2 , 3 } . They are on ΘBλ U dB2 U <9B3,
and thus are not visible to an observer who is inside T.
Proof, The link L is in <9T except for small ^-intervals about each
F-singularity, e.g. [0 3, θΊ] in Figure 3.6, when L penetrates into B2 .
A few moments reflection should make it clear that the part of L
which penetrates B2 is precisely the subarc we called L2(fc) in Figure
3.1(b). Figure 3.7 shows how these arcs look on a typical 2-sphere
<9B;. They are the connecting threads which join up the digons in a
circular ring. For later use, we have also illustrated in Figure 3.7 how
the decomposition of F into subsets 1', 1", 2 and 3 will appear on
0Bf .
It follows immediately that if we stand inside T and look out onto
dT, we will see the link L minus the union of the r subarcs L/(fc),
k = 1, 2,... , rxr, one for each crossing point in the diagram on dΊ.
EXAMPLE. When we defined the planar projection of the elementary
braids aγ, a2, <z3 in Figure 1.5 we showed them as they would appear
to a viewer who was standing outside T, between p\ and /?3 with his
feet on the plane of the paper and his head above the paper, and also
as they would look to a viewer inside T.
STUDYING LINKS VIA CLOSED BRAIDS III
45
\::::| I 
>£::::::
lylil 
1 . ' >£::jj:jj:j
