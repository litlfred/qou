---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-021-wirtinger-presentation-of-fundamental-groups
section_title: "Wirtinger presentation of fundamental groups"
section_number: null
pages: 81-85
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
We often make use of the fundamental group of 3-manifolds. There is a systematic
algorithm to compute these for complements of Wilson line networks known as the
Wirtinger presentation. We refer for further background to [98, chapter 9].
Suppose we consider the complement of a network of Wilson lines in S 3. Al-
ternatively, we could also thicken the Wilson lines and consider a knotted genus-g
boundary, but we will continue to think of network of Wilson lines. Choose a pro-
jection to the plane and endow all arcs with orientations. For concreteness, we will
– 81 –
explain this for the handlebody-knot5 2 appearing in (5.8). We use the presentation
52 =
a
be
d
c
h
f g (A.3)
Every arc will lead to one generator in the fundamental group, and we labeled the
arcs witha,b,c,d,e,f,g,hin the picture. We choose a base point for the fundamental
group outside the screen closer to the reader. Each generator associated to an arc
corresponds to the loop starting at the base point, going around the arc according the
right-hand rule (so that the thumb goes along the direction of the chosen orientation
and the remaining fingers indicate the orientation of the loop) and returning to the
base point.
Relations.Clearly, reversing the direction of the chosen orientation corresponds
to choosing the inverse generator. For every junction and every over- and under-
crossing, we get one relation. For a junction with only outgoing arrows, the counter-
clockwise product of all the generators is unity, since the concatenation of the paths
is contractible behind the figure (drawn for concreteness for a cubic junction):
x1
x2
x3
:x 1x2x3 = 1.(A.4)
For a crossing, we also produce a relation in which the new generator after the cross-
ing gets conjugated by the generator of the strand that overcrosses it. Concretely,
if we orient the arrows as in the figure, then the blue path corresponding tox 3 is
equivalent to the pathx 2x1x−1
2 ,
x2
x1
x3
x−1
2
:x 3 =x 2x1x−1
2 .(A.5)
In any given network of lines, we can always omit one of the relations coming from a
vertex or a crossing. The relations can all be understood as the statement that the
– 82 –
loop behind the vertex or the crossing is contractible. Any such given loop may be
rewritten as a concatenation of loops around all the other vertices and its triviality
is thus implied by all the other relations.
The 5 2 handlebody-knot.If we apply this to the generators as in (A.3), then
we obtain the following presentation for the fundamental group:
π1(52)∼=

a, b, c, d,
e, f, g, h

dfe−1 = 1, a−1bg−1 = 1, e=hbh−1, h=bcb−1,
g=cfc −1, a=fhf −1, c=a−1da

.(A.6)
The first two relations are the vertex relations, while the other relations are the
crossing relations. We can clearly simplify this presentation dramatically. Let us
intially do this by hand. We can easily eliminate the generatorsd, e, f, g, hby
solving relations 1, 2, 3, 4 and 7 and expressing them in terms of the other generators
a,bandc,
g=a −1b, d=aca −1, e=bcbc −1b−1, f=ac −1a−1bcbc−1b−1, h=bcb −1 .(A.7)
This leaves only the relations 5 and 6, which can easily be seen to be equivalent, in
line with what we explained above that one of the relations may be dropped since it
is implied by all the others.
This simplifies the group to
π1(52)∼=⟨a, b, c|cac−1a−1bcbc−1b−1c−1b−1a= 1⟩.(A.8)
Thus there is only one relationR(a,b,c) = 1, with
R(a,b,c) =cac −1a−1bcbc−1b−1c−1b−1a(A.9)
in the fundamental group. All fundamental groups of interest to us in this paper are
of this form.
Whitehead algorithm.The fundamental group in the form (A.8) is simplified,
but it can be difficult to see whether it is isomorphic to another group of the form
G =⟨a,b,c|R ′(a,b,c) = 1⟩(A.10)
whereR ′ is a different relation. This is the case if there is an (possibly outer)
automorphismϕ:F 3→F 3 withR(a,b,c) =R ′(ϕ(a),ϕ(b),ϕ(c)), whereF 3 is the free
group on three generators. For the free group, the Whitehead algorithm constructs
ϕ(or rules out its existence).
Let us describe the algorithm for a free groupF n with generating setX=
{x1,...,x n}. We findϕas a composition of basic automorphisms known as the
Whitehead automorphisms. There are two types:
– 83 –
1. Forσ∈S n ands∈{±} n, define
ϕ(1)
σ,s(xi) =x si
σ(i) (A.11)
2. Forx∈X∪X −1 andA⊆(X∪X −1)\{x,x −1}, define
ϕ(2)
x,A(xi) =



xix, x i∈Aandx i̸∈A−1∪{x,x −1},
x−1xi, x i∈A−1 andx i̸∈A∪{x,x −1},
x−1xix, x i∈Aandx i∈A−1,
xi,otherwise.
(A.12)
Every automorphism ofF n can be written as a composition of such basic Whitehead
automorphisms.
Let noww∈F n be a reduced word inF n (meaning that occurrences ofx ix−1
i
have been canceled). Let|w|be its length, i.e. the number of letters. By definition,
|xn
i|=|n|. The Whitehead algorithm aims to find an automorphismϕ, such that
the length|ϕ(w)|is minimized. The crucial fact about Whitehead automorphisms is
the following: Ifwis not of minimal length (i.e. ifϕexists such that|ϕ(w)|<|w|),
then we can chooseϕto be a Whitehead automorphism. Thus, the algorithm tests
if|ϕ(w)|<|w|for any Whitehead automorphismϕ(for which there are finitely
many). If yes, we pickϕfor which the length decreased and repeat the procedure.
If no (i.e. if|ϕ(w)|=|w|for all Whitehead automorphismsϕ), thenwhas minimal
length. We then find all words with minimal length equivalent tow(of which there
are finitely many) by repeatedly applying Whitehead algorithms until we do not
produce any new words of minimal length. When applying this algorithm to two
different words, we can conclusively check whether the sets of equivalent minimal-
length words agree. If yes, then the resulting group obtained from the relationw= 1
is isomorphic, otherwise they are non-isomorphic.
We exemplify this produce at the example ofw 1 =R(a,b,c) given in (A.9),
which has length 12. Then
ϕ(2)
c,{a−1,b−1}(w1) =w 2 =ac−1a−1b2c−1b−2a ,(A.13)
which has length 9. It then finds
ϕ(2)
b,{a,c,c−1}(w2) =w 3 =ac−1a−1bc−1b−1ab ,(A.14)
which has length 8. Finally
ϕ(2)
a−1,{b−1}(w3) =w 4 =ac−1bcb−1ab ,(A.15)
which has length 7. At this point, no Whitehead automorphism exists that reduces
the length further. We then apply all Whitehead automorphisms tow 4 and keep
– 84 –
all words of length 7. After iterating this procedure 5 times, we have found all
6720 words of length 7 that are equivalent tow 4. We can pick out a canonical
representative by taking the word that appears first in lexicographic order given by
a3b2c2. It is obtained from the composition
a3b2c2 =ϕ (2)
b−1,{c,c−1}◦ϕ(2)
a−1,{b−1,c,c−1}◦ϕ(2)
a−1,{b−1,c}◦ϕ(1)
(12),{+,+,−}◦ϕ(2)
b−1,{a,a−1}(w4).(A.16)
The final automorphism that satisfiesR(ϕ(a),ϕ(b),ϕ(c)) =a 3b2c2 is the rather non-
trivial automorphism
ϕ(a) =b−1a−2bcb−1aba3ba2b ,(A.17a)
ϕ(b) =b−1a−2bcb−1aba3b ,(A.17b)
ϕ(c) =b−1a−1bc−1b−1a2b .(A.17c)
In particular, this algorithm showed that the groupπ1(52) is not free (since otherwise
R(a,b,c) = 1 would be equivalent to the relationa= 1) and thus the handlebody-
knot5 2 is not a handlebody.
