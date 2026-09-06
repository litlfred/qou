---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-007-5-feynman-diagrams-and-stuﬀ-operators
section_title: "Feynman Diagrams and Stuﬀ Operators"
section_number: 5
pages: 22-28
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
From here we could go in various directions. But since we are d reaming
about the future of mathematics, let us choose a rather specu lative one, and
discuss some applications of categoriﬁcation to quantum theory . By now it
is clear that categoriﬁcation is necessary for understandi ng the connections
between quantum ﬁeld theory and topology. It has even played a role in
some attempts to ﬁnd a quantum theory of gravity. But having r eviewed
these subjects elsewhere [4, 2, 3], we restrict ourselves he re to some of the
simplest aspects of quantum physics.
One of the ﬁrst steps in developing quantum theory was Planck ’s new
treatment of electromagnetic radiation. Classically, ele ctromagnetic radia-
tion in a box can be described as a collection of harmonic osci llators, one
for each vibrational mode of the ﬁeld in the box. Planck ‘quan tized’ the
electromagnetic ﬁeld by assuming that energy of each oscill ator could only
take the discrete values ( n + 1
2 )ℏ ω , where n is a natural number, ω is the
frequency of the oscillator in question, and ℏ is a constant now known as
Planck’s constant. Planck did not really know what to make of the num-
ber n, but Einstein and others subsequently interpreted it as the number
of ‘photons’ occupying the vibrational mode in question. Ho wever, far from
being particles in the traditional sense of tiny billiard ba lls, these photons
are curiously abstract entities — for example, all the photo ns occupying a
given mode are indistinguishable from each other.
The treatment of this subject was originally quite ad hoc, bu t with further
work the underlying mathematics gradually became clearer. It turns out
22
that states of a quantized harmonic oscillator can be descri bed as vectors
in a Hilbert space called ‘Fock space’. This Hilbert space co nsists of formal
power series in a single variable x that have ﬁnite norm with respect to a
certain inner product. For a full treatment of the electroma gnetic ﬁeld we
would need power series in many variables, one for each vibra tional mode,
but to keep things simple let us consider just a single mode. T hen the power
series 1 corresponds to the state in which no photons occupy t his mode.
More generally, the power series xn/n ! corresponds to a state with n photons
present.
Now, the relation between power series and structure types s uggests an
odd notion: perhaps FinSet {x} is a kind of categoriﬁed version of Fock space!
This notion becomes a bit more plausible when one recalls tha t the power
series xn/n ! correspond to the structure type of being an n-element set. In
fact, if we think about it carefully, what Einstein really di d was to categorify
Planck’s mysterious number ‘ n’ by taking it to stand for an n-element set:
a set of photons. So perhaps categoriﬁcation can help us unde rstand the
quantized harmonic oscillator more deeply.
To test this notion more carefully, the ﬁrst thing to check is whether we
can categorify the inner product on Fock space. In fact we can ! Given power
series
f (x) =
∞∑
n=0
fn
n! xn , g (x) =
∞∑
n=0
gn
n! xn ,
their Fock space inner product is given by
⟨f, g ⟩=
∞∑
n=0
f ngn/n ! .
Categorifying, we deﬁne the inner product of structure type s F and G as
follows:
⟨F, G ⟩=
∞∑
n=0
(Fn × Gn)/ /n ! .
Note that the result is a groupoid. If we take the cardinality of this groupoid,
we get back the inner product of the generating functions of F and G:
|⟨F, G ⟩|= ⟨|F |, |G|⟩.
23
Even better, this groupoid has a nice interpretation: its ob jects are ﬁnite
sets equipped with both a structure of type F and a structure of type G, and
its morphisms are bijections preserving both structures.
To go further, we should categorify linear operators on Fock space, since in
quantum theory observables are described by self-adjoint o perators. For this,
we really need the ‘stuﬀ types’ mentioned at the end of the pre vious section,
and we need to use a little more category theory. The inner pro duct on
structure types extends naturally to an inner product on stu ﬀ types, the inner
product of U: F → FinSet0 and V : G → FinSet0 being a groupoid ⟨F, G ⟩
called their ‘weak pullback’. We deﬁne a stuﬀ operator to be a groupoid O
equipped with a functor U: O → FinSet0 × FinSet0. Stuﬀ operators really
work very much like operators on Fock space. We can act on a stu ﬀ type F
by a stuﬀ operator O and get a stuﬀ type OF . There is a nice way to add
stuﬀ operators, there is a nice way to compose stuﬀ operators using weak
pullbacks, and any stuﬀ operator O has an adjoint O∗ with
⟨F, OG ⟩∼= ⟨O∗F, G ⟩
for all stuﬀ types F and G. Just as any stuﬀ type F satisfying a certain
ﬁniteness condition has a generating function |F | which is a vector in Fock
space, any stuﬀ operator O satisfying a certain ﬁniteness condition gives an
operator on Fock space, which we call |O|. This operator is characterized by
the fact that
|OF | = |O|(|F |)
for any stuﬀ type F for which |F | lies in Fock space. And as one would hope,
we have
|O + O′| = |O| + |O′|, |OO ′| = |O| |O′|, |O∗| = |O|∗.
for any stuﬀ operators O and O′.
In physics, the most important operators on Fock space are th e annihi-
lation and creation operators, a and a∗. The annihilation operator acts as
diﬀerentiation on power series:
(af )(x) = f ′(x),
while the creation operator acts as multiplication by x:
(a∗f )(x) = xf (x).
24
As their names suggest, these operators decrease or increas e the number of
photons by 1. These operators are adjoint to one another, but not inverses.
Instead, they satisfy the famous relation
aa∗ − a∗a = 1.
While this relation plays a crucial role throughout quantum theory, it remains
slightly mysterious: why should ﬁrst creating a photon and t hen destroying
one give a diﬀerent result than ﬁrst destroying one and then c reating one?
If categoriﬁcation is going to help us understand the quanti zed harmonic
oscillator, it must give an explanation of this fact.
To give such an explanation, we must ﬁrst describe the stuﬀ op erator A
that serves as the categoriﬁed version of the annihilation o perator. Since A
actually maps structure types to structure types, instead o f giving its full
deﬁnition we shall take the more intuitive course of saying h ow it acts on
structure types. Given a structure type F , a structure of type AF on the
ﬁnite set S is deﬁned to be a structure of type F on S + 1, where 1 is the
1-element set. Note that
|AF |(x) =
∞∑
n=0
|(AF )n|
n! xn =
∞∑
n=0
|Fn+1|
n! xn = d
dx|F |(x),
or in short:
|A| = a.
Next let us describe a categoriﬁed version of the creation op erator. We
could simply deﬁne A∗ to be the adjoint of A, but A∗ actually maps structure
types to structure types, so let us say how it does so. For any s tructure type
F , a structure of type A∗F on S consists of a choice of element s ∈ S together
with a structure of type F on S − {s}. This is the same thing as chopping
S into two disjoint parts and putting the structure of ‘being a 1-element set’
on one part and a structure of type F on the other, so
A∗F = xF
and thus
|A∗| = a∗.
Next we we should check that our annihilation and creation op erators
satisfy a categoriﬁed version of the commutation relations aa∗ − a∗a = 1. Of
25
course we wish to avoid minus signs, and having categoriﬁed w e should speak
of natural isomorphism rather than equality, so we write thi s as
AA∗ ∼= A∗A + 1.
We will not give a rigorous proof of this here; instead, we wil l we just sketch
the proof that AA∗F ∼= A∗AF + F when F is is a structure type. To put a
structure of type AA∗F on a ﬁnite set S is to put a structure of type A∗F
on the set S + 1. This, in turn, is the same as choosing an element s ∈ S + 1
and putting a structure of type F on S + 1− {s}. Now either s ∈ S or s /∈ S.
In the ﬁrst case we are really just choosing an element s ∈ S and putting a
structure of type AF on S − {s}. This is the same as putting a structure of
type A∗AF on S. In the second case we are really just putting a structure
of type F on S. We thus have
AA∗F ∼= A∗AF + F
as desired.
The interesting thing about this calculation is that it is pu rely combina-
torial. It reduces a fact about quantum theory to a fact about ﬁnite sets. If
we examine it carefully, it boils down to this: if we have a box with some
balls in it, there is one more way to put an extra ball in and the n take a ball
out than there is to take a ball out and then put one in!
Starting from here one can march ahead, categorifying huge t racts of
quantum physics, all the way to the theory of Feynman diagram s. For now
we content ourselves here with the briefest sketch of how thi s would go,
leaving the details for later [7]. First, we deﬁne the ﬁeld operator to be the
stuﬀ operator
Φ = A + A∗.
Our normalization here diﬀers from the usual one in physics b ecause we wish
to avoid dividing by
√
2, but all the usual physics formulas can be adapted
to this new normalization. More generally, we deﬁne the Wick powers of
Φ, denoted :Φ p:, to be the stuﬀ operators obtained by taking Φ p, expanding
it in terms of the annihilation and creation operators, and m oving all the
annihilation operators to the right of all the creation oper ators ‘by hand’,
ignoring the fact that they do not commute. For example:
:Φ 0: = 1
26
:Φ 1: = A + A∗
:Φ 2: = A2 + 2A∗A + A∗2
:Φ 3: = A3 + 3A∗A2 + 3A∗2A + A∗3
and so on.
In quantum ﬁeld theory one spends a lot of time doing calculat ions with
products of Wick powers. In the categoriﬁed context, these a re stuﬀ operators
of the form
:Φ p1: · · · :Φ pk : .
What is such a stuﬀ operator like? In general, it does not map structure
types to structure types, so we really need to think of it as a g roupoid O
equipped with a functor U: O → FinSet0 × FinSet0. An object of O is a
Feynman diagram: a graph with k vertices of valence p1, . . . , p k respectively,
together with univalent vertices labelled by the elements o f two ﬁnite sets,
say S and T . We draw Feynman diagrams like this:
/0
/0
/0
/1
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/1
/1
We draw the vertices labelled by elements of S on the top and think of
them as ‘outgoing’ particles. We draw the vertices labelled by elements of
T on bottom, and think of them as ‘incoming’ particles. We can t hink of
the Feynman diagram as the pair of sets ( S, T ) equipped with extra ‘stuﬀ’,
namely the body of the diagram. The functor U: O → FinSet0 × FinSet0
sends the Feynman diagram to the pair ( S, T ).
While Feynman diagrams began as a kind of bookkeeping device for quan-
tum ﬁeld theory calculations involving Wick powers, they ha ve increasingly
taken on a life of their own. Here we see that they arise natura lly from the
theory of ﬁnite sets equipped with extra structure, or more g enerally, extra
‘stuﬀ’. Since categoriﬁcation eliminates problems with di vergent power se-
ries (as we have already seen in the previous section), it is t empting to hope
that this viewpoint will help us understand the divergences that have always
27
plagued the theory of Feynman diagrams. Of course this may or may not
happen — it is diﬃcult to predict, especially when it comes to the future.
