---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-015-52-twisted-alexander-polynomials-and-knot-concor
section_title: "Twisted Alexander polynomials and knot concordance"
section_number: 5.2
pages: 14-16
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
result in the study of slice knots is due to Fox and Milnor [FM6 6] who showed that if K is
a slice knot, then ∆ K
.=f (t)f (t−1) for some f (t) ∈ Z[t±1].
In this section we will give an exposition and a slight genera lization of the Kirk–Livingston
[KL99a] sliceness obstruction theorem, which generalizes the Fox–Milnor condition. Note
that we will state this obstruction using a slightly diﬀerent setup, but Theorem 5.2 is already
contained in [KL99a] and [HKL08].
Let K be a knot, as above we denote by NK the zero–framed surgery of S3 along K.
Now suppose that K has a slice disk D. Note that ∂(D4 \νD) = NK. Let R be a ring with
(possibly trivial) involution and as usual we extend the inv olution to R[t±1] by
t :=t−1. Let
α :π1(NK ) → GL(R[t±1],k ) be a unitary representation. Assume that α has the following
two properties:
(1) α factors through a representation π1(D4 \νD) → GL(k,R [t±1]), and
(2) the induced twisted modules H∗(D4 \νD;R[t±1]k) are R[t±1]–torsion,
then using Poincar´ e duality for Reidemeister torsion (cf. [KL99a, Theorem 6.1]) one can
show that τ (NK,α ) .=f (t)f (t) for some f (t) ∈R(t). We refer to [KL99a, Corollary 5.3] for
details.
Remark. Note that the canonical representation π1(NK ) → GL(1, Z[t±1]) extends over any
slice disk complement. It can be shown that H∗(D4 \νD; Z[t±1]) is Z[t±1]–torsion. We can
therefore recover the Fox–Milnor theorem from this discuss ion.
Most of the ideas and techniques of ﬁnding representations s atisfying (1) and (2) go back
to the seminal work of Casson and Gordon [CG86]. We follow the approach taken in [Fr04]
which is inspired by Letsche [Let00] and Kirk–Livingston [K L99a, HKL08].
In the following let K again be a knot in S3. We denote by Wk the cyclic k–fold branched
cover of K. Note that H1(Wk; Z) has a natural Z/k–action, and we can therefore view
H1(Wk; Z) as a Z[Z/k]–module. If H1(Wk; Z) is ﬁnite, then there exists a non–singular
linking form
λk :H1(Wk; Z) ×H1(Wk; Z) → Q/Z
with respect to which Z/k acts via isometries. We say that M ⊂H1(Wk; Z) is a metabolizer
of the linking form if M is a Z[Z/k]–submodule of H1(Wk; Z) such that λk(M,M ) = 0 and
such that |M |2 = |H1(Wk; Z)|. It is well–known that if K is slice, then λk has a metabolizer
for any prime power k. We refer to [Go78] for details.
Note that H 1(NK ; Z) = Z, in particular H 1(NK ; Z) has a unique generator (up to sign)
which we denote by φ. We now consider the Alexander module H1(NK ; Z[t±1]) which we
denote by H. Note that H is isomorphic to the usual Alexander module of K. It is well–
known that given k there exists a canonical isomorphism H/(tk − 1) → H1(Wk; Z) (cf.
e.g. [Fr04, Corollary 2.4] for details). Now let µ ∈ π1(NK ) be an element with φ(µ ) = 1.
Note that for any g ∈ π we have φ(µ −φ(g)g) = 0, in particular we can consider its image
[µ −φ(g)g] in the abelianization H1(Ker(φ)), which we can identify with H. Then we have a
well–deﬁned map
π → Z ⋉H → Z ⋉H/(tk − 1)
where the ﬁrst map is given by sending g ∈ π to (φ(g), [µ −φ(g)g]). Here n ∈ Z acts on H
and on H/(tk − 1) via multiplication by tn. We refer to [Fr04] and [BF08] for details.
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 15
Fix k ∈ N. Let χ : H1(Wk; Z) → Z/q → S1 be a character. We denote the induced
characterH →H/(tk − 1) = H1(Wk; Z) →S1 byχ as well. Let ζq be a primitive q–th root
of unity. Then it is straightforward to verify that
α(k,χ ) : π → Z ⋉H/(tk − 1) → GL(k, Z[ζq][t±1])
(j,h ) ↦→





0 ... 0 t
1 0 ... 0
.
.
. . . . .
.
.
0 ... 1 0





j




χ(h) 0 ... 0
0 χ(th) ... 0
.
.
. . . . .
.
.
0 0 ... χ (tk−1h)





deﬁnes a unitary representation. (Note the “ t” in the upper right corner.) Also note that
α(k,χ ) is not a tensor representation (cf. [HKL08]).
We can now formulate the following obstruction theorem whic h is well–known to the
experts. It can be proved using the above discussion, Propos ition 3.1, various well–known
arguments going back to Casson and Gordon [CG86] and [KL99a, Lemma 6.4]. We also
refer to Letsche [Let00] and [Fr04] for more information.
Theorem 5.2. LetK be a slice knot. Then for any prime power k there exists a metabolizer
M ofλk such that for any odd prime power n and any character χ :H1(Wk; Z) → Z/n →S1
vanishing on M we have
∆ α(k,χ)
NK
.=f (t)
f (t)
for some f (t) ∈Q(Z[ζn])[t±1] = Q(ζn)[t±1].
Note that the original sliceness obstruction of Kirk and Liv ingston [KL99a, Theorem 6.2]
(cf. also [HKL08, Theorem 8.1] and [Liv09, Theorem 5.4]) giv es an obstruction in terms of
twisted Alexander polynomials of a cyclic cover of S3\νK corresponding to one–dimensional
representations. Using Theorem 3.8 and Lemma 5.1 (cf. also [ KL99a, Lemma 6.3]) one can
show that the sliceness obstruction of Theorem 5.2 is equiva lent to the original formulation
by Kirk and Livingston.
Remark. In Theorem 5.2 and later in Theorems 5.3 and 5.5 we restrict ou rselves to characters
of odd prime power. Similar theorems also hold for character s of even prime power order,
we refer to [KL99a, Lemma 6.4] and [Liv09, Section 5] for more information.
Theorem 5.2 can be somewhat generalized using tensor repres entations. In the following
let k1,...,k n ∈ N. Assume we are given characters χi : H1(Wki; Z) → Z/q → S1,i =
1,...,n we also get a tensor representation
α(k1,χ 1) ⊗ · · · ⊗α(kn,χn) → GL(k1 · · · · ·kn, Z[ζq][t±1]).
We refer to [Fr04, Proposition 4.6] for more information.
The following theorem can be proved by modifying the proof of Theorem 5.2 along the
lines of [Fr04, Theorem 4.7].
Theorem 5.3. Let K be a slice knot. Let q be an odd prime power and let k1,...,k n
be coprime prime powers. Then there exist metabolizers M1,...,M n of the linking forms
λk1,...,λ kn such that for any choice of characters χi :H1(Wki; Z) → Z/q →S1,i = 1,...,n
vanishing on Mi we have
∆ α(k1,χ1)⊗···⊗α(kn,χn)
NK
.=f (t)
f (t)
16 STEF AN FRIEDL AND STEF ANO VIDUSSI
for some f (t) ∈Q(Z[ζq])[t±1] = Q(ζq)[t±1].
Remark. It was ﬁrst observed by Letsche [Let00] that non–prime power dimensional repre-
sentations can give rise to sliceness obstructions. It is sh own in [Fr03] that Letsche’s non–
prime power representations are given by the tensor represe ntations considered in Theorem
5.3.
The sliceness obstruction coming from twisted Alexander po lynomials is in some sense
less powerful than the invariants of Casson and Gordon [CG86 ] (cf. [KL99a, Section 6] for
a careful discussion) and Cochran–Orr–Teichner [COT03]. B ut to date twisted Alexander
polynomials give the strongest sliceness obstruction for a lgebraically slice knots that can be
computed eﬃciently. The Kirk–Livingston sliceness obstru ction theorem has been used by
various authors to produce many interesting examples, some of which we list below:
(1) Kirk and Livingston [KL99b] apply twisted Alexander pol ynomials to show that
some knots (e.g. 8 17) are not concordant to their inverses. This shows in particu lar
that knots are not necessarily concordant to their mutants. In [KL99b] it is also
shown that in general a knot is not even concordant to a positi ve mutant.
(2) Tamulis [Tam02] considered knots with at most ten crossi ngs which have algebraic
concordance order two. Tamulis used twisted Alexander poly nomials to show that
all but one of these knots do not have order two in the knot conc ordance group.
(3) In [HKL08] Herald, Kirk and Livingston consider all knot s with up to twelve cross-
ings. Eighteen of these knots are algebraically slice but ca n not be shown to be slice
using elementary methods. In [HKL08] twisted Alexander pol ynomials are used to
show that sixteen of these knots are in fact not slice and one k not is smoothly slice.
Therefore among the knots with up to twelve crossings only th e sliceness status of
the knot 12 a631 is unknown.
(4) The concordance genus gc(K) of a knot K is deﬁned to be the minimal genus among
all knots concordant to K. Livingston [Liv09] uses twisted Alexander polynomials
to show that the concordance genus of 10 82 equals three, which is its ordinary genus.
