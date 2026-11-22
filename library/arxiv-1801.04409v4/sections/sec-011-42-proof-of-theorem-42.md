---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-011-42-proof-of-theorem-42
section_title: "Proof of Theorem 4.2"
section_number: 4.2
pages: 16-17
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
theory of vertices of modular representations and the Green correspon-
dence (see e.g. [A], Chapter III), which we will now recall. Let M be
a ﬁnite dimensional representation of a ﬁnite group G over a ﬁeld k of
characteristic p. Let H be a subgroup of G.
Deﬁnition 4.4. We say that M is relatively H-projective if M is a
direct summand in IndG
HV for some ﬁnite dimensional H-module V .
Proposition 4.5. (see e.g. [A], Section 9) For each indecomposable
G-module M, the minimal subgroups H ⊂G such that M is relatively
H-projective are conjugate, and they are p-groups.
Deﬁnition 4.6. The minimal subgroup H ⊂G such that M is rela-
tively H-projective (well-deﬁned up to conjugation thanks to Proposi-
tion 4.5) is called the vertex of M.
Proposition 4.7. ([G], Theorem 9) If dim M̸ = 0 in k then the vertex
of M is the Sylow p-subgroup P ⊂G.
Proof. The result is well known, but we give a proof for reader’s conve-
nience. Let H be the vertex of M, so M is a direct summand of IndG
HV
for some H−module V . For the sake of contradiction assume that H
is not conjugate to P. We will prove:
(a) any direct summand of IndG
HV has dimension zero.
This is a contradiction with our assumption on H, since M is one
of such direct summands. We deduce (a) from the following stronger
statement:
(b) any direct summand of ResG
PIndG
HV has dimension zero.
16
To prove (b), recall that by the Mackey formula (see [A, III.8, Lemma
7]):
ResG
PIndG
HV =
M
s∈P \G/H
IndP
P ∩sHs−1RessHs−1
P ∩sHs−1s(V ).
By the assumption P ∩sHs−1 is strictly contained in P for any s.
Since P is p−group, P ∩sHs−1 is a subnormal subgroup of P. Thus
by Green’s indecomposability Theorem (see [A, III.8, Theorem 8]) the
functor IndP
P ∩sHs−1 sends indecomposable modules to indecomposable
ones. In particular, any direct summand of IndP
P ∩sHs−1RessHs−1
P ∩sHs−1s(V )
is induced from P ∩sHs−1 and has dimension divisible by the index
[P : P ∩sHs−1], hence vanishes in k, see [A, III.8, Lemma 4]. The
result follows.
□
Theorem 4.8. [A] (Green’s correspondence) For each p-subgroup H ⊂
NG(P), there is a bijection between indecomposable representations of
G with vertex H and indecomposable representations of NG(P) with
vertex H, given by X 7→X◦for X ∈Repk G, such that X|NG(P ) =
X◦⊕N, where N is a direct sum of indecomposable NG(P)-modules
with vertices other than H.
We can now prove Theorem 4.2. Let T ∈Rep G be a simple object.
Then T = X, where X ∈Rep G is an indecomposable module of
nonzero dimension. Hence, by Proposition 4.7, the vertex of X is P.
Hence, by Theorem 4.8, X|NG(P ) = X◦⊕N, where N is a direct sum
of indecomposable NG(P)-modules whose vertices are diﬀerent from P.
Then by Proposition 4.7, the dimension of each of these indecomposable
modules is zero, hence N is negligible. This means that F(T) = X◦,
which is a simple object of Rep NG(P). This shows that the functor F
is injective.
Now let Z ∈Rep NG(P) be a simple object. Then Z = Y for some
Y ∈Rep NG(P). But Y is a direct summand in (IndG
NG(P )Y )|NG(P ).
Hence, Z is a direct summand in F(IndG
NG(P )Y ), proving that F is
surjective.
Thus, F is an equivalence, as claimed.
