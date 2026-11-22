---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10"
section_id: sec-003-iwahori-hecke-algebras-and-multiplicative-jucys
section_title: "Iwahori-Hecke algebras and multiplicative Jucys-Murphy elements"
section_number: null
pages: 2-3
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
toc_source: outline
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An, Bn and Dn."
---
2.1. Coxeter groups
Let (W, S), S = {s1, . . . , sn}, be a Coxeter system. Thus, W is a group with a presentation
(s0, . . . , sn|(sisj)mij = e), where mij ∈Z+ ∪{∞}, with mii = 1, mji = mij ≥2 if i̸ = j, and mij = ∞means
that there is no relation included for the pair si, sj. Such a presentation is read oﬀthe Coxeter diagram of
(W, S) in a standard way: such a diagram is a non-oriented graph with S as a set of vertices, and mij −2
edges between the vertices si and sj. Let l : W →Z≥0 be the Bruhat length function with respect to S.
We will be primarily interested in Coxeter groups that are Weyl groups of classical types A, B = C, D.
To ﬁx the numbering of the generators, their Coxeter diagrams are presented, with a vertex corresponding
to si ∈S marked by i. The Coxeter diagram of type An is
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
When n is small, these are interpreted in a standard way as follows: the Coxeter system A1 = B1 = D1
has a single vertex, D2 = A1 × A1, D3 = A3. We also adopt the convention A0 = B0 = D0 corresponding
to the empty Coxeter graph and the trivial Coxeter group.
Many of the results and deﬁnitions in this paper are valid in all types A, B, D, with deﬁnitions for
type An−1 naturally ﬁtting with deﬁnitions in types Bn, Dn. In this case, we will write ‘type Xn, where X
is A−1, B or D’ (or something in a similar vein).
2.2. Iwahori–Hecke algebras
Let A = Q(v). The Iwahori–Hecke algebra Hv(W, S) = H(W, S) associated with a Coxeter system (W, S)
is a unital A-algebra with generators ts, s ∈S, subject to the relations:
(i) ⟨tsi, tsj⟩mij = ⟨tsj, tsi⟩mij, where ⟨x, y⟩m is an alternating product xyx . . . of x and y with m factors.
(ii) (ts −v)(ts + v−1) = 0.
When (W, S) is of type Bn, we will also be interested in the Iwahori–Hecke algebra Hv,v0(W, S) with
unequal parameters v, v0 ∈A. This is a unital algebra over the ring A, with the relation (ii) replaced by
the relations:
(ii′) (tsi −v)(tsi + v−1) = 0 for i > 0,
(ii′) (ts0 −v0)(ts0 + v−1
0 ) = 0.
When (W, S) is of type Xn with X ∈{A, B = C, D}, we will write W(Xn) and H(Xn) for W and H(W, S),
or Hv,v0(Bn) if we need to emphasise that we use unequal parameters. In each of these cases, we will write
ti for tsi.
Let w = si1 . . . sir, w ∈W, sik ∈S be a reduced expression. Then the element tw = tsi1 . . . tsir in H(W, S)
is independent of the choice of a reduced expression, and H(W, S) is a free A-module with a basis
tw, w ∈W. The elements tw are invertible, and the collection t−1
w , w ∈W, gives another basis of H(W, S)
over A.
