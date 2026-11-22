---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-019-rational-cherednik-algebras
section_title: "Rational Cherednik Algebras"
section_number: null
pages: 38-39
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
toc_source: outline
doc_brief: "Hecke algebras, generalisations and representation theory — 31 sections: Front matter; Algebras of Finite Type; Blocks"
---
Let W ⊂GL(h) be a complex reﬂection group. There is a natural pairing ( , ) : h × h∗→C given by
(y, x) := x(y). Let S be the set of all pseudo-reﬂections in W and let c : S →C be a conjugacy invariant
function, that is, a map such that
c(wsw−1) = c(s)
∀s ∈S, w ∈W.
Let V := h ⊕h∗and let TV ∗denote the tensor algebra on the dual space of V . For s ∈S, ﬁx αs ∈h∗
to be a basis of the one-dimensional vector space Im(s −idV )|h∗and α∨
s ∈h to be a basis of the one-
dimensional vector space Im(s −idV )|h. Let t ∈C. The rational Cherednik algebra Ht,c(W) of W is the
quotient of TV ∗⋊W by the relations:
[x1, x2] = 0, [y1, y2] = 0, [y, x] = t(y, x) −2
X
s∈S
c(s) (y, αs)(α∨
s , x)
(α∨s , αs)
s
(5.1)
for all x1, x2, x ∈h∗and y1, y2, y ∈h.
Example 5.1 Let W = Sn and h = Cn. Choose a basis x1, . . . , xn of h∗and a dual basis y1, . . . , yn of
h so that
σxi = xσ(i)σ
and
σyi = yσ(i)σ
∀σ ∈Sn, 1 ⩽i ⩽n.
The set S is the set of all transpositions in Sn. We denote by sij the transposition (i, j). Set
αij := xi −xj
and
α∨
ij = yi −yj
∀1 ⩽i < j ⩽n.
We have (α∨
ij, αij) = 2. There is a single conjugacy class in S, so take c ∈C. Then Ht,c(Sn) is the
quotient of TV ∗⋊Sn by the relations:
[xi, xj] = 0, [yi, yj] = 0, [yi, xi] = t −c
X
j̸=i
sij, [yi, xj] = c sij for i̸ = j.
Remark 5.2 For all λ ∈C×, we have Hλt,λc(W) ∼= Ht,c(W). So we only need to consider the cases
t = 1 and t = 0.
There is a natural ﬁltration F on Ht,c(W) given by putting V ∗in degree one and W in degree
zero. The crucial result by Etingof and Ginzburg is the Poincar´e–Birkhoﬀ–Witt (PBW) Theorem [EtGi,
Theorem 1.3].
Theorem 5.3 Let C[V ] be the set of regular functions on V (that is, the symmetric algebra Sym(V ∗) of
the dual space of V ). There is an isomorphism of algebras
grF(Ht,c(W)) ∼= C[V ] ⋊W,
given by σ(v) 7→v, σ(w) 7→w, where σ(h) denotes the image of h ∈Ht,c(W) in grF(Ht,c(W)). In
particular, there is an isomorphism of vector spaces
Ht,c(W) ∼= C[V ] ⊗C[W].
35
5.1
