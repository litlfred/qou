---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-002-41-feynman-diagrams
section_title: "Feynman Diagrams"
section_number: 4.1
pages: 29-36
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
and Hall algebras.
4.1 Feynman Diagrams
One of the ﬁrst steps in developing quantum theory was Planck’s new treatment
of electromagnetic radiation. Classically, electromagnetic radiation in a box can
be described as a collection of harmonic oscillators, one for each vibr ational
29
mode of the ﬁeld in the box. Planck ‘quantized’ the electromagnetic ﬁ eld by
assuming that the energy of each oscillator could only take discrete , evenly
spaced values: if by ﬁat we say the lowest possible energy is 0, the allo wed
energies take the form nℏω, where n is any natural number, ω is the frequency
of the oscillator in question, and ℏ is Planck’s constant.
Planck did not know what to make of the number n, but Einstein and others
later interpreted it as the number of ‘quanta’ occupying the vibrat ional mode
in question. However, far from being particles in the traditional sen se of tiny
billiard balls, quanta are curiously abstract entities—for example, all the quanta
occupying a given mode are indistinguishable from each other.
In a modern treatment, states of a quantized harmonic oscillator a re de-
scribed as vectors in a Hilbert space called ‘Fock space’. This Hilbert sp ace
consists of formal power series. For a full treatment of the elect romagnetic ﬁeld
we would need power series in many variables, one for each vibrationa l mode.
But to keep things simple, let us consider power series in one variable. In this
case, the vector zn/n! describes a state in which n quanta are present. A general
vector in Fock space is a convergent linear combination of these spe cial vectors.
More precisely, the F ock space consists of ψ ∈ C[[z]] with ⟨ψ,ψ ⟩< ∞, where
the inner product is given by
⟨ ∑
anzn,
∑
bnzn
⟩
=
∑
n!anbn. (7)
But what is the meaning of this inner product? It is precisely the inner
product in L2(E), where E is the groupoid of ﬁnite sets! This is no coincidence.
In fact, there is a deep relationship between the mathematics of th e quantum
harmonic oscillator and the combinatorics of ﬁnite sets. This relation suggests
a program of groupoidifying mathematical tools from quantum theory, such as
annihilation and creation operators, ﬁeld operators and their norm al-ordered
products, Feynman diagrams, and so on. This program was initiated by Dolan
and one of the current authors [4]. Later, it was developed much fu rther by
Morton [33]. Guta and Maassen [17] and Aguiar and Maharam [1] have a lso
done relevant work. Here we just sketch some of the basic ideas.
First, let us see why the inner product on Fock space matches the in ner
product on L2(E) as described in Theorem 45. We can compute the latter inner
product using a convenient basis. Let Ψ n be the groupoid with n-element sets
as objects and bijections as morphisms. Since all n-element sets are isomorphic
and each one has the permutation group Sn as automorphisms, we have an
equivalence of groupoids
Ψ n ≃ 1//Sn.
Furthermore, Ψ n is a groupoid over E in an obvious way:
v : Ψ n →E.
We thus obtain a vector Ψ
~
n ∈ RE following the rule described in Deﬁnition 10.
We can describe this vector as a formal power series using the isomo rphism
RE ∼= R[[z]]
30
described in Example 3. To do this, note that
v−1(m) ≃
{
1//Sn m =n
0 m ⁄=n
where 0 stands for the empty groupoid. It follows that
|v−1(m)| =
{
1/n! m =n
0 m ⁄=n
and thus
Ψ
~
n =
∑
m∈N
|v−1(m)|zm = zn
n!.
Next let us compute the inner product in L2(E). Since ﬁnite linear combi-
nations of vectors of the form Ψ
~
n are dense in L2(E) it suﬃces to compute the
inner product of two vectors of this form. We can use the recipe in T heorem 45.
So, we start by taking the weak pullback of the corresponding grou poids over
E:
⟨Ψ m, Ψ n⟩
/d122/d122/d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73
Ψ m
/d37/d37/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74 Ψ n
/d122/d122/d116 /d116 /d116 /d116 /d116 /d116 /d116 /d116 /d116 /d116
E
An object of this weak pullback consists of an m-element set S, an n-element
setT , and a bijection α :S →T . A morphism in this weak pullback consists of
a commutative square of bijections:
S
f
/d15/d15
α /d47/d47T
g
/d15/d15
S′
α ′
/d47/d47T ′
So, there are no objects in ⟨Ψ m, Ψ n⟩ when n ⁄= m. When n = m, all objects
in this groupoid are isomorphic, and each one has n! automorphisms. It follows
that
⟨Ψ
~
m, Ψ
~
n⟩ = |⟨Ψ m, Ψ n⟩| =
{
1/n! m =n
0 m ⁄=n
Using the fact that Ψ
~
n =zn/n!, we see that this is precisely the inner product in
Equation 7. So, as a complex Hilbert space, Fock space is the complex iﬁcation
of L2(E).
It is worth reﬂecting on the meaning of the computation we just did. The
vector Ψ
~
n =zn/n! describes a state of the quantum harmonic oscillator in which
31
n quanta are present. Now we see that this vector arises from the g roupoid
Ψ n over E. In Section 1 we called a groupoid over E a stuﬀ type , since it
describes a way of equipping ﬁnite sets with extra stuﬀ. The stuﬀ ty pe Ψ n is a
very simple special case, where the stuﬀ is simply ‘being an n-element set’. So,
groupoidiﬁcation reveals the mysterious ‘quanta’ to be simply elemen ts of ﬁnite
sets. Moreover, the formula for the inner product on Fock space arises from the
fact that there are n! ways to identify two n-element sets.
The most important operators on Fock space are the annihilation an d cre-
ation operators. If we think of vectors in Fock space as formal po wer series, the
annihilation operator is given by
(aψ)(z) = d
dzψ(z)
while the creation operator is given by
(a∗ψ)(z) = zψ(z).
As operators on Fock space, these are only densely deﬁned: for e xample, they
map the dense subspace C[z] to itself. However, we can also think of them as
operators from C[[z]] to itself. In physics these operators decrease or increase
the number of quanta in a state, since
azn =nzn−1, a ∗zn =zn+1.
Creating a quantum and then annihilating one is not the same as annhila ting
and then creating one, since
aa∗ =a∗a + 1.
This is one of the basic examples of noncommutativity in quantum theo ry.
The annihilation and creation operators arise from spans by degrou poidiﬁ-
cation, using the recipe described in Theorem 34. The annihilation ope rator
comes from this span:
E
1
/d127/d127/d126/d126/d126/d126 /d126/d126/d126 S↦→S+1
/d31/d31/d64/d64/d64/d64/d64/d64/d64
E E
where the left leg is the identity functor and the right leg is the funct or ‘disjoint
union with a 1-element set’. Since it is ambiguous to refer to this span b y
the name of the groupoid on top, as we have been doing, we instead c all it A.
Similarly, we call its adjoint A∗:
E
S↦→S+1
/d127/d127/d126/d126/d126/d126 /d126/d126/d126 1
/d31/d31/d64/d64/d64/d64/d64/d64/d64
E E
32
A calculation [33] shows that indeed:
A
~
=a, A
~
∗ =a∗.
Moreover, we have an equivalence of spans:
AA∗ ≃A∗A + 1.
Here we are using composition of spans, addition of spans and the ide ntity span
as deﬁned in Section 2. If we unravel the meaning of this equivalence , it turns
out to be very simple [4]. If you have an urn with n balls in it, there is one more
way to put in a ball and then take one out than to take one out and th en put
one in. Why? Because in the ﬁrst scenario there are n + 1 balls to choose from
when you take one out, while in the second scenario there are only n. So, the
noncommutativity of annihilation and creation operators is not a mys terious
thing: it has a simple, purely combinatorial explanation.
We can go further and deﬁne a span
Φ = A +A∗
which degroupoidiﬁes to give the well-known ﬁeld operator
φ = Φ
~
=a +a∗
Our normalization here diﬀers from the usual one in physics because we wish
to avoid dividing by
√
2, but all the usual physics formulas can be adapted to
this new normalization.
The powers of the span Φ have a nice combinatorial interpretation. If we
write its nth power as follows:
Φ n
q
/d126/d126/d124/d124/d124/d124/d124/d124/d124/d124 p
/d32/d32/d66/d66/d66/d66/d66/d66/d66/d66
E E
then we can reinterpret this span as a groupoid over E ×E:
Φ n
q×p
/d15/d15
E ×E
Just as a groupoid over E describes a way of equipping a ﬁnite set with extra
stuﬀ, a groupoid over E ×E describes a way of equipping a pair of ﬁnite sets
with extra stuﬀ. And in this example, the extra stuﬀ in question is a ve ry simple
sort of diagram!
More precisely, we can draw an object of Φ n as ai-element setS, aj-element
setT , a graph with i +j univalent vertices and a single n-valent vertex, together
33
with a bijection between the i +j univalent vertices and the elements of S +T .
It is against the rules for vertices labelled by elements of S to be connected
by an edge, and similarly for vertices labelled by elements of T . The functor
p×q : Φ n →E ×E sends such an object of Φ n to the pair of sets ( S,T ) ∈E ×E.
An object of Φ n sounds like a complicated thing, but it can be depicted
quite simply as a F eynman diagram. Physicists traditionally read Feynman
diagrams from bottom to top. So, we draw the above graph so that the univalent
vertices labelled by elements of S are at the bottom of the picture, and those
labelled by elements of T are at the top. For example, here is an object of Φ 3,
where S = {1, 2, 3} and T = {4, 5, 6, 7}:
5 4 7 6
1 3 2
In physics, we think of this as a process where 3 particles come in and 4 go out.
Feynman diagrams of this sort are allowed to have self-loops: edges with
both ends at the same vertex. So, for example, this is a perfectly ﬁ ne object of
Φ 5 with S = {1, 2, 3} and T = {4, 5, 6, 7}:
5 4 6 7
2 3 1
To eliminate self-loops, we can work with the normal-ordered powers or
‘Wick powers’ of Φ, denoted : Φ n : . These are the spans obtained by taking Φ n,
expanding it in terms of the annihilation and creation operators, and moving all
the annihilation operators to the right of all the creation operator s ‘by hand’,
34
ignoring the fact that they do not commute. For example:
: Φ 0 : = 1
: Φ 1 : = A +A∗
: Φ 2 : = A2 + 2A∗A +A∗2
: Φ 3 : = A3 + 3A∗A2 + 3A∗2A +A∗3
and so on. Objects of : Φ n: can be drawn as Feynman diagrams just as we did
for objects of Φ n. There is just one extra rule: self-loops are not allowed.
In quantum ﬁeld theory one does many calculations involving product s of
normal-ordered powers of ﬁeld operators. Feynman diagrams mak e these calcu-
lations easy. In the groupoidiﬁed context, a product of normal-or dered powers
is a span
: Φ n1 : · · · : Φ nk :
q
/d119/d119/d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112
p
/d39/d39/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79
E E.
As before, we can draw an object of the groupoid : Φ n1 : · · · : Φ nk : as a Feynman
diagram. But now these diagrams are more complicated, and closer t o those seen
in physics textbooks. For example, here is a typical object of : Φ 3: : Φ 3: : Φ 4: ,
drawn as a Feynman diagram:
5 8 7 6
1 4 2 3
In general, a F eynman diagram for an object of : Φ n1 : · · · : Φ nk : consists
of an i-element set S, a j-element set T , a graph with k vertices of valence
n1,...,n k together with i +j univalent vertices, and a bijection between these
univalent vertices and the elements of S +T . Self-loops are forbidden; it is
against the rules for two vertices labelled by elements of S to be connected by
an edge, and similarly for two vertices labelled by elements of T . As before, the
forgetful functor p ×q sends any such object to the pair of sets ( S,T ) ∈E ×E.
The groupoid : Φ n1 : · · · : Φ nk : also contains interesting automorphisms.
These come from symmetries of Feynman diagrams: that is, graph automor-
phisms ﬁxing the univalent vertices labelled by elements of S and T . These
35
symmetries play an important role in computing the operator corres ponding to
this span:
: Φ n1 : · · · : Φ nk :
q
/d119/d119/d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112
p
/d39/d39/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79
E E.
As is evident from Theorem 36, when a Feynman diagram has symmetr ies, we
need to divide by the number of symmetries when determining its cont ribution
to the operator coming from the above span. This rule is well-known in quan-
tum ﬁeld theory; here we see it arising as a natural consequence of groupoid
cardinality.
