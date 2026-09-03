---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10 RESEARCH ARTICLE"
section_id: sec-002-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 RESEARCH ARTICLE — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An"
---
A two-variable link invariant – the HOMFLY-PT polynomial – can be recovered using a family of trace
functions on Iwahori–Hecke algebras in typeA satisfying analogues of the conditions in Markov’s the-
orem for the braid group (usually called ‘Markov moves’) [10]. The analogues of Markov moves can
be formulated for Iwahori–Hecke algebras of other Coxeter groups, leading to a general notion of the
Markov trace, see, for example, [3, 5, 7, 20]. The Markov traces were classiﬁed in typeA, where there
is, up to some change of scaling, a unique Markov trace, by Ocneanu and Jones [10], and in typesB and
D by Geck and Lambropoulou [3, 5]. In type B, Markov traces produce the invariants of the solid torus
links [13, 5].
Of particular interest are specialisations of the general Markov traces in types B, D coming from
geometry (or, alternatively, from the theory of Soergel bimodules). These were studied in [ 7]u s i n g
Lusztig’s Fourier transform, in [20, 21] using the equivariant Hecke category, and in [2] using the mon-
odromic Hecke category. The latter two geometric constructions are both matched with the one coming
from the Hochschild cohomology of Soergel bimodules, and, in type A, to the Soergel bimodule con-
struction of Khovanov–Rozansky homology [12]. Note that the construction of trace-like functionals
on the Hecke algebras through Hochschild cohomology of Soergel bimodules readily generalises to an
arbitrary Coxeter group.
Iwahori–Hecke algebras in types A, B, D contain families of commuting operators whose properties
are analogous to those of Jucys–Murphy elements in the group algebra of the symmetric group. Under
a standard normalisation, the Markov trace in type A is polynomial in the variable a. Its individual
coeﬃcients turn out to be ‘represented’ (in the sense explained in the main text) by the elementary sym-
metric polynomials in multiplicative Jucys–Murphy elements. It was shown in [2] that this fact admits
a categoriﬁcation to the level of Khovanov–Rozansky homology. Moreover, in type A, multiplicative
Jucys–Murphy elements themselves admit an interesting categoriﬁcation, deﬁning relative Serre func-
tors with respect to the embedding of a smaller Hecke category into a larger one [4, 9]. Our investigation
was motivated by a desire to see how far these patterns can be extended for other types.
In this paper, we give a new simple construction for Markov traces in typesB, D using the theory of
Jucys–Murphy elements in Iwahori–Hecke algebras of these types.
C© The Author(s), 2026. Published by Cambridge University Press on behalf of Glasgow Mathematical Journal Trust. This is an Open Access article,
distributed under the terms of the Creative Commons Attribution licence (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted
re-use, distribution and reproduction, provided the original article is properly cited.
at https://www.cambridge.org/core/terms. https://doi.org/10.1017/S0017089526101050
Downloaded from https://www.cambridge.org/core. IP address: 162.43.233.6, on 30 Jul 2026 at 23:50:49, subject to the Cambridge Core terms of use, available
2 Kostiantyn Tolmachov and Heorhii Zhylinskyi
The paper is organised as follows. In Section2, we collect the needed deﬁnitions about Coxeter groups
and Iwahori–Hecke algebras. In Section 2.5, we deﬁne a family of commuting elements in Iwahori–
Hecke algebras of type A, B, D coming from the extended aﬃne Hecke algebra in type A. See [16]f o r
the history and an alternative deﬁnition. We follow [17] in our treatment of these elements.
In Section 3, we ﬁrst deﬁne the Markov traces and give, as a warm-up, a construction of a Markov
trace deﬁned by a uniform formula in all types A, B, D. See Theorem 3.1.4. In Section 3.2, we recall
the results of Geck and Lambropoulou and give the formulas for the Markov traces in types B and D
depending on a free parameter (Theorem 3.2.2 and Corollary 3.2.5, respectively). In Section 3.3,w e
specialise our results to obtain the geometric Markov traces.
2. Iwahori–Hecke algebras and multiplicative Jucys–Murphy elements
2.1. Coxeter groups
Let (W, S), S ={ s1, ... , sn}, be a Coxeter system. Thus, W is a group with a presentation
(s0, ... , sn|(sisj)mij = e), where mij ∈ Z+ ∪{ ∞ }, with mii = 1, mji = mij ≥ 2 if i ⁄= j, and mij =∞ means
that there is no relation included for the pairsi, sj. Such a presentation is read oﬀ the Coxeter diagram of
(W, S) in a standard way: such a diagram is a non-oriented graph withS as a set of vertices, andmij − 2
edges between the verticessi and sj.L e tl : W → Z≥0 be the Bruhat length function with respect toS.
We will be primarily interested in Coxeter groups that are Weyl groups of classical typesA, B = C, D.
To ﬁx the numbering of the generators, their Coxeter diagrams are presented, with a vertex corresponding
to si ∈ S marked by i. The Coxeter diagram of typeAn is
nn − 121
,
of type Bn = Cn is
n − 110
,
and of type Dn is
n − 12
1
1′
.
When n is small, these are interpreted in a standard way as follows: the Coxeter system A1 = B1 = D1
has a single vertex, D2 = A1 × A1, D3 = A3. We also adopt the conventionA0 = B0 = D0 corresponding
to the empty Coxeter graph and the trivial Coxeter group.
Many of the results and deﬁnitions in this paper are valid in all types A, B, D, with deﬁnitions for
type An−1 naturally ﬁtting with deﬁnitions in types Bn, Dn. In this case, we will write ‘typeXn, where X
is A−1, B or D’ (or something in a similar vein).
2.2. Iwahori–Hecke algebras
Let A = Q(v). The Iwahori–Hecke algebraHv(W, S) = H(W, S) associated with a Coxeter system(W, S)
is a unital A-algebra with generators ts, s ∈ S, subject to the relations:
(i) ⟨tsi , tsj ⟩mij =⟨tsj , tsi ⟩mij , where ⟨x, y⟩m is an alternating product xyx ... of x and y with m factors.
(ii) (ts − v)(ts + v−1) = 0.
When (W, S) is of type Bn, we will also be interested in the Iwahori–Hecke algebraHv,v0 (W, S) with
unequal parameters v, v0 ∈ A. This is a unital algebra over the ringA, with the relation (ii) replaced by
the relations:
(ii′) (tsi − v)(tsi + v−1) = 0 for i > 0,
(ii′) (ts0 − v0)(ts0 + v−1
0 ) = 0.
https://www.cambridge.org/core/terms. https://doi.org/10.1017/S0017089526101050
Downloaded from https://www.cambridge.org/core. IP address: 162.43.233.6, on 30 Jul 2026 at 23:50:49, subject to the Cambridge Core terms of use, available at
Glasgow Mathematical Journal 3
When (W, S) is of typeXn with X ∈{ A, B = C, D}, we will writeW(Xn) and H(Xn) for W and H(W, S),
or Hv,v0 (Bn) if we need to emphasise that we use unequal parameters. In each of these cases, we will write
ti for tsi .
Let w = si1 ... sir , w ∈ W, sik ∈ S be a reduced expression. Then the elementtw = tsi1
... tsir in H(W, S)
is independent of the choice of a reduced expression, and H(W, S) is a free A-module with a basis
tw, w ∈ W. The elements tw are invertible, and the collection t−1
w , w ∈ W, gives another basis of H(W, S)
over A.
2.3. Trace functional and a pairing on H(W, S)
Let x ↦→ x be the Kazhdan–Lusztig involution on H(W, S).I ti sa Q-algebra involution, deﬁned by the
assignments v = v−1, tw = t−1
w−1 . Let ω : H(W, S) stand for theA-linear algebra anti-involution deﬁned by
ω(tw) = tw−1 .
For h ∈ H(W, S), x ∈ W, let hx stand for the t−1
x -coeﬃcient of h in the basis t−1
w , where w runs
through W.L e tτ : H(W, S) → A be a functional deﬁned by τ (h) = he, where e ∈ W is the unit. For
h, h′∈ H(W, S), deﬁne a pairing ⟨h, h′⟩=τ (ω(h)h′). We have the following standard proposition, see,
for example, [8, Chapter 8].
Proposition 2.3.1. The functional τ and the pairing ⟨, ⟩satisfy the following properties:
(a) The functional τ is an A-linear trace on H(W, S), that is, τ (hh′) = τ (h′h).
(b) The pairing ⟨, ⟩is A-antilinear in the ﬁrst argument andA-linear in the second argument and
satisﬁes the orthogonality relation⟨tw1 , t−1
w2 ⟩=δw1,w−1
2
.
(c) We have ⟨h1h2, h3⟩=⟨h1, h3ω(h2)⟩=⟨h2, ω(h1)h3⟩for any h1, h2, h3 ∈ H(W, S).
We will use the following straightforward corollary of this proposition repeatedly.
Corollary 2.3.2. Let (W′, S′) be a parabolic subgroup of W. Assume that x, y ∈ H(W′, S′) ⊂ H(W, S),
and assume that z ∈ spanA⟨tw, w ∈ W\W′⟩(resp. z ∈ spanA⟨t−1
w , w ∈ W\W′⟩). Then ⟨xz, y⟩=⟨zx, y⟩=0
(resp. ⟨x, yz⟩=⟨x, zy⟩=0).
2.4. ‘Full twist’ and Jucys–Murphy elements
Assume that (W, S) is of ﬁnite type. Letw0 stand for the longest element inW with respect to the Bruhat
length. Let S(W, S) = t−2
w0 ∈ H(W, S). In classical types, we will write S(Xn) ∈ H(Xn), when X is A, B or
D,o rs i m p l yS when the type is clear from the context.
The following proposition is also standard:
Proposition 2.4.1. The element S(W, S) is central in H(W, S).
We will need the following ‘Serre property’ of the operator of multiplication byS(W, S).
Proposition 2.4.2. For any h1, h2 ∈ H(W, S), we have the identity
⟨h1, S(W, S)h2⟩=⟨h2, h1⟩.
Proof. By Proposition2.3.1 (b), it is enough to prove the statement forh1 = t−1
w1 , h2 = tw2 for arbitrary
w1, w2 ∈ W. We have, by Proposition2.3.1 (c),
⟨t−1
w1 , S(W, S)tw2 ⟩=⟨tw0 t−1
w1 , t−1
w0 tw2 ⟩=⟨tw0w−1
1
, t−1
w−1
2 w0
⟩
= δw0w−1
1 ,w0w2 = δw1,w−1
2
= ⟨tw2 , t−1
w1 ⟩.
This completes the proof.
https://www.cambridge.org/core/terms. https://doi.org/10.1017/S0017089526101050
Downloaded from https://www.cambridge.org/core. IP address: 162.43.233.6, on 30 Jul 2026 at 23:50:49, subject to the Cambridge Core terms of use, available at
4 Kostiantyn Tolmachov and Heorhii Zhylinskyi
We have the natural embeddingιn : H(Xn) → H(Xn+1), where X is A, B or D, induced by the embed-
ding of the sets of labels of the Coxeter diagram. Using these embeddings, an element ofH(Xn) can be
considered as an element of H(Xm) for m > n.
Deﬁnition 2.4.3. For n ≥ 2,l e t JX
n = S(Xn)−1 · S(Xn−1) when X is A−1, B or D.W el e t JA
1 = 1, JB
1 = t2
0,
JD
1 = 1. We call these elements Jucys–Murphy elements of ﬁnite Hecke algebras in classical types.
We have the following corollary of Proposition2.4.1.
Corollary 2.4.4. For X equal to A−1, B or D, elements JX
k commute with each other when considered
lying in the same Iwahori–Hecke algebra via the embedding described above. The elementJX
n lies in the
centraliser of H(Xn−1) in H(Xn).
Remark 2.4.5. The elements JA
k are sometimes called multiplicative Jucys–Murphy elements in the
Iwahori–Hecke algebra of typeA. There seems to be no agreement in the literature on which elements to
call the Jucys–Murphy elements in other types. We chose our convention because under it the deﬁnition
of the Jucys–Murphy element is uniform in all types, but elementsjX
k for X = B, D deﬁned below arguably
also deserve the name.
