---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-004-iwahori-hecke-algebras-and-multiplicative-jucys
section_title: "Iwahori-Hecke algebras and multiplicative Jucys-Murphy elements."
section_number: null
pages: 2-4
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
Iwahori-Hecke algebras and multiplicative Jucys-Murphy elements.
2.1
Coxeter groups. Let (W, S), S = {s1, . . . , sn}, be a Coxeter system. Thus, W
is a group with a presentation (s0, . . . , sn|(sisj)mij = e), where mij ∈Z+ ∪{∞}, with
mii = 1, mji = mij ≥2 if i̸ = j, and mij = ∞means that there is no relation included
for the pair si, sj. Such a presentation is read off the Coxeter diagram of (W, S) in a
standard way: such a diagram is a non-oriented graph with S as a set of vertices, and
mij −2 edges between the vertices si and sj. Let l : W →Z≥0 be the Bruhat length
function with respect to S.
We will be primarily interested in Coxeter groups that are Weyl groups of classical
types A, B = C, D. To fix the numeration of the generators, their Coxeter diagrams
are presented below, with a vertex corresponding to si ∈S marked by i. The Coxeter
diagram of type An is
n
n −1
2
1
,
of type Bn = Cn is
n −1
1
0
,
and of type Dn is
n −1
2
1
1′
.
When n is small, these are interpreted in a standard way as follows: the Coxeter system
A1 = B1 = D1 has a single vertex, D2 = A1 × A1, D3 = A3. We also adopt the
convention A0 = B0 = D0 corresponding to the empty Coxeter graph and the trivial
Coxeter group.
2
Many of the results and definitions in this paper are valid in types all types A, B, D,
with definitions for type An−1 naturally fitting with definitions in types Bn, Dn. In this
case, we will write “type Xn, where X is A−1, B or D” (or something in a similar vein).
2.2
Iwahori-Hecke algebras. Let A = Q(v). The Iwahori-Hecke algebra Hv(W, S) =
H(W, S) associated to a Coxeter system (W, S) is a unital A-algebra with generators
ts, s ∈S, subject to the relations
(i). ⟨tsi, tsj⟩mij = ⟨tsj, tsi⟩mij, where ⟨x, y⟩m is an alternating product xyx . . . of x
and y with m factors.
(ii). (ts −v)(ts + v−1) = 0.
When (W, S) is of type Bn we will also be interested in the Iwahori-Hecke algebra
Hv,v0(W, S) with unequal parameters v, v0 ∈A. This is a unital algebra over the ring
A, with the relation (ii) replaced by the relations
(ii'). (tsi −v)(tsi + v−1) = 0 for i > 1,
(ii''). (tsi −v0)(tsi + v−1
0 ) = 0.
When (W, S) is of type Xn with X ∈{A, B = C, D}, we will write W(Xn) and
H(Xn) for W and H(W, S), or Hv,v0(Bn) if we need to emphasize that we use unequal
parameters. In each of these cases, we will write ti for tsi.
Let w = si1 . . . sir, w ∈W, sik ∈S be a reduced expression.
Then the element
tw = tsi1 . . . tsir in H(W, S) is independent of the choice of a reduced expression, and
H(W, S) is a free A-module with a basis tw, w ∈W. The elements tw are invertible,
and the collection t−1
w , w ∈W, gives another basis of H(W, S) over A.
2.3
Trace functional and a pairing on H(W, S). Let x 7→x be the Kazhdan-
Lusztig involution on H(W, S). It is a Q-algebra involution, defined by the assignments
v = v−1, tw = t−1
w−1. Let i : H(W, S) stand for the A-linear algebra anti-involution
defined by i(tw) = tw−1.
For h ∈H(W, S), x ∈W, let hx stand for the t−1
x -coefficient of h in the basis t−1
w ,
where w runs through W. Let τ : H(W, S) →A be a functional defined by τ(h) = he,
where e ∈W is the unit. For h, h′ ∈H(W, S), define a pairing ⟨h, h′⟩= τ(i(h)h′). We
have the following standard proposition, see, for example, [GP00, Chapter 8].
Proposition 2.3.1. The functional τ and the pairing ⟨, ⟩satisfies the following prop-
erties.
(a). The functional τ is an A-linear trace on H(W, S), that is τ(hh′) = τ(h′h).
(b). The pairing ⟨, ⟩is A-antilinear in the first argument, A-linear in the second ar-
gument and satisfies the orthogonality relation ⟨tw1, t−1
w2 ⟩= δw1,w−1
2 .
(c). We have ⟨h1h2, h3⟩= ⟨h1, h3i(h2)⟩= ⟨h2, i(h1)h3⟩for any h1, h2, h3 ∈H(W, S).
We will use the following straightforward corollary of this proposition repeatedly.
Corollary 2.3.2. Let (W ′, S′) be a parabolic subgroup of W.
Assume that x, y ∈
H(W ′, S′) ⊂H(W, S), and assume that z ∈spanA⟨tw, w ∈W\W ′⟩(resp.
z ∈
spanA⟨t−1
w , w ∈W\W ′⟩). Then ⟨xz, y⟩= ⟨zx, y⟩= 0 (resp. ⟨x, yz⟩= ⟨x, zy⟩= 0).
3
2.4
“Full twist” and Jucys-Murphy elements. Assume that (W, S) is of finite
type. Let w0 stand for the longest element in W with respect to the Bruhat length. Let
S(W, S) = t−2
w0 ∈H(W, S). In classical types, we will write S(Xn) ∈H(Xn), when X is
A, B or D, or simply S when the type is clear from the context.
The following proposition is also standard:
Proposition 2.4.1. The element S(W, S) is central in H(W, S).
We will need the following “Serre property” of the operator of multiplication by
S(W, S).
Proposition 2.4.2. For any h1, h2 ∈H(W, S) we have the identity
⟨h1, S(W, S)h2⟩= ⟨h2, h1⟩.
Proof. It is enough to prove the proposition for h1 = t−1
w1 , h2 = tw2 for arbitrary w1, w2 ∈
W. We have, by Proposition 2.3.1 (c),
⟨t−1
w1 , S(W, S)tw2⟩= ⟨tw0t−1
w1 , t−1
w0 tw2⟩= ⟨tw0w−1
1 , t−1
w−1
2
w0⟩=
= δw0w−1
1
,w0w2 = δw1,w−1
2
= ⟨tw2, t−1
w1 ⟩.
This completes the proof.
We have the natural embedding ιn : H(Xn) →H(Xn+1), where X is A, B or D,
induced by the embedding of the sets of labels of the Coxeter diagram. Using these
embeddings, an element of H(Xn) can be considered as an element of H(Xm) for m > n.
Definition 2.4.3. For n ≥2, let JX
n = S(Xn)−1 · S(Xn−1) when X is A−1, B or D.
We let JA
1 = 1, JB
1 = t2
0, JD
1
= 1. We call these elements Jucys-Murphy elements of
finite Hecke algebras in classical types.
We have the following corollary of Proposition 2.4.1.
Corollary 2.4.4. For X equal to A−1, B or D, elements JX
k commute with each other
when considered lying in the same Iwahori-Hecke algebra via the embedding described
above. The element JX
n lies in the centralizer of H(Xn−1) in H(Xn).
Remark 2.4.5. The elements JA
k are sometimes called multiplicative Jucys-Murphy
elements in the Iwahori-Hecke algebra of type A. There seem to be no agreement in
the literature on which elements to call the Jucys-Murphy elements in other types. We
chose our convention because under it the definition of the Jucys-Murphy element is
uniform in all types, but elements jX
k for X = B, D defined below arguably also deserve
the name.
