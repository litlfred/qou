---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-019-7-independence-of-the-decoration
section_title: "Independence of the decoration"
section_number: 7
pages: 22-26
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
We now show that the extended Bloch group element of a decorate d representation is indepen-
dent of the decoration. We ﬁrst prove that we can choose logar ithms of the Ptolemy coordinates
independently, without aﬀecting the extended Bloch group el ement.
Deﬁnition 7.1. Let c : ˙∆ k
n(Z) → C∗ be a Ptolemy assignment. A lift of c is an assignment
~c : ˙∆ k
n(Z) → C such that exp(~c) = c.
For any lift ~c of a Ptolemy assignment c on ∆ 3
2, we have a ﬂattening
(7.1) λ(~c) = (~c03 +~c12 −~c02 −~c13,~c01 +~c23 −~c02 −~c13) ∈ˆC.
Deﬁnition 7.2. The log-parameters of a ﬂattening (e, f) ∈ˆC are deﬁned by
(7.2) wij =



e if ij = 01 or ij = 23
−f if ij = 12 or ij = 03
−e + f if ij = 02 or ij = 13.
Lemma 7.3. Let~c : ˙∆ 3
2(Z) → C be a lifted Ptolemy assignment, and let wij be the log-parameters
of λ(~c). Fix i < j ∈ { 0, . . . ,3} and let ~c′ be the lifted Ptolemy assignment obtained from ~c by
adding 2π√−1 to~cij. Then
(7.3) λ(~c′) − λ(~c) = χ(wij + 2π
√
−1δij),
where δij is 1 if ij = 02 or 13 and 0 otherwise.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 23
Proof. Denote the ﬂattening λ(~c) by (e, f). If ij = 03 or 12, it follows from ( 7.1) that λ(~c′) = ( e +
2π√−1, f). Similarly, λ(~c′) = ( e, f + 2π√−1) if ij = 01 or 23, and λ(~c′) = ( e − 2π√−1, f − 2π√−1)
if ij = 02 or 13. By Lemma 3.4,
(7.4)
(e + 2π
√
−1, f) − (e, f) =χ(−f )
(e, f + 2π
√
−1) − (e, f) =χ(e)
(e − 2π
√
−1, f − 2π
√
−1) =χ(−e + f + 2π
√
−1).
This proves the result. □
Let ~c be a lift of a Ptolemy assignment c. For each α ∈ ∆ 3
n−2(Z), ~c induces a lift ~cα of cα.
Consider the element
(7.5) τ =
∑
α∈∆ k
n− 2(Z)
λ(~cα) ∈ ˆP(C).
Fix a point t0 ∈ ˙∆ k
n(Z). We wish to understand the eﬀect on τ of adding 2π√−1 to ~ct0 . This
changes τ into an element τ ′ ∈ ˆP(C). Let wij(α) denote the log-parameters of λ(~cα). Note that t0
either lies on an edge, on a face, or in the interior of ∆ 3
n.
Lemma 7.4. Suppose t0 is on the edge ij of ∆ 3
n. Then
(7.6) τ ′ − τ = χ(wij(α) + 2π
√
−1δij),
where α = t − ei − ej, (i.e. α is such that t0 is an edge point of ∆ 3(α)).
Proof. This follows immediately from Lemma 7.3. □
Lemma 7.5. Suppose t0 is on a face opposite vertex i. Then τ ′ − τ = (−1)iχ(κ + 2π√−1), where
κ is given by
(7.7) κ =~cηi(0,−1,1) −~cηi(0,1,−1) −
(
~cηi(−1,0,1) −~cηi(1,0,−1)
)
+~cηi(−1,1,0) −~cηi(1,−1,0),
where ηi inserts a zero as the ith vertex.
Proof. For simplicity assume i = 0 . The other cases are proved similarly. There are exactly thr ee
α’s for which t0 is an edge point of ∆ 3(α). These are
(7.8) α0 = t0 − (0, 0, 1, 1), α 1 = t0 − (0, 1, 0, 1), α 2 = t0 − (0, 1, 1, 0).
Note that ~ct = (~cα0)23 = (~cα1 )13 = (~cα2)12. Since adding 2π√−1 to~ct0 leaves~cα unchanged unless
α ∈ {α0, α1, α2}, Lemma 7.3 implies that
(7.9) τ ′ − τ = χ(w23(α0)) + χ(w13(α1) + 2π
√
−1) + χ(w12(α2)).
One easily checks that
(7.10)
w23(α0) =~c(1,0,−1,0) +~c(0,1,0,−1) −~c(1,0,0,−1) −~c(0,1,−1,0)
w13(α1) =~c(1,0,0,−1) +~c(0,−1,1,0) −~c(1,−1,0,0) −~c(0,0,1,−1)
w12(α2) =~c(1,−1,0,0) +~c(0,0,−1,1) −~c(1,0,−1,0) −~c(0,−1,0,1),
from which the result follows. □
Lemma 7.6. If t0 is an interior point, τ ′ = τ .
24 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Proof. If t0 is an interior point, there are six α’s for which t0 is an edge point of ∆ 3(α). These are
α0, α1 and α2 as deﬁned in ( 7.8) as well as
(7.11) α3 = t0 − (1, 1, 0, 0), α 4 = t0 − (1, 0, 1, 0), α 5 = t0 − (1, 0, 0, 1).
Again, by Lemma 7.3
(7.12) τ ′ − τ = χ(w23(α0)) + χ(w13(α1) + 2π
√
−1) + χ(w12(α2))+
χ(w01(α3)) + χ(w02(α4) + 2π
√
−1) + χ(w03(α5)).
Using ( 7.10) as well as
(7.13)
w01(α3) =~c(0,−1,0,1) +~c(−1,0,1,0) −~c(0,−1,1,0) −~c(−1,0,0,1)
w02(α4) =~c(0,1,−1,0) +~c(−1,0,0,1) −~c(0,0,−1,1) −~c(−1,1,0,0)
w03(α5) =~c(0,0,1,−1) +~c(−1,1,0,0) −~c(0,1,0,−1) −~c(−1,0,1,0)
we see that all terms in ( 7.12) cancel out. Hence, τ ′ = τ . □
Proposition 7.7. Let c be a Ptolemy assignment on K. For any lift ~c of c, the element
(7.14) λ(~c) =
∑
i
∑
α∈∆ k
n− 2(Z)
ǫiλ(~ci
α) ∈ ˆP(C)
is independent of the choice of lift. In particular, if c is the Ptolemy assignment of a decorated
representation ρ, λ(~c) is the extended Bloch group element of ρ.
Proof. Let~c and~c′ be lifts of c. Let t0 ∈ ˙∆ 3
n(Z). We wish to prove that λ(~c) = λ(~c′). It is enough
to prove this when ~c′ is obtained from ~c by adding 2π√−1 to~ct. If t0 is an interior point, the result
follows immediately from Lemma 7.6. If t0 is a face point, t0 lies in exactly two simplices of K, and
it follows from Lemma 7.5 that the two contributions to the change in λ(~c) appear with opposite
signs (by ( 3.5), 2χ(2π√−1) = 0 ). Suppose t0 is an edge point. Let C be the 3-cycle obtained by
gluing together all the ∆ 3(α)’s having t0 as an edge point, using the face pairings induced from K.
Let e be the (interior) 1-cell of C containing t0. The argument in Zickert [ 30, Theorem 6.5] shows
that the total log-parameter around e is zero. It thus follows from Lemma 7.4 that adding 2π√−1
to~ct0 changes λ(~c) by 2-torsion which is trivial if and only if the number n of simplices in C for
which t is a 02 edge or a 13 edge is even. Consider a curve λ in C encircling e. The vertex ordering
induces an orientation on each face of each simplex of C, such that when λ passes through two
faces of a simplex in C, the two orientations agree unless e is a 02 edge or a 13 edge. Since M is
orientable, it follows that n is even. The second statement follows by letting ~c = log c. □
Proposition 7.8. The extended Bloch group element of a decorated boundary-uni potent represen-
tation is independent of the decoration.
Proof. By performing a barycentric subdivision if necessary, we may assume that any decoration
is generic. Fix a lift ~∆ i of each simplex ∆ i of K. A decoration D assigns a coset gi
jN to each
vertex j of ~∆ i. Suppose we have another decoration D′ of ρ with cosets hi
jN . Since equivalent
decorations have the same fundamental class, we may assume t hat hi
j = gi
jdi
j, where the di
j’s are
diagonal matrices (see Remark 4.5). Let c and c′ denote the Ptolemy assignments on K induced by
D and D′. Suppose di
j = diag(di
j0, . . . , di
j,n−1). By ( 5.1) we have
(7.15) ci′
t = ci
t
t0∏
k=0
di
0k
t1∏
k=0
di
1k
t2∏
k=0
di
2k
t3∏
k=0
di
3k.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 25
Fix a lift ~c of c. Letting log denote a logarithm, deﬁne a lift ~c′ of c′ by
(7.16) ~c′i
t =~ci
t +
t0∑
k=0
log(di
0k) +
t1∑
k=0
log(di
1k) +
t2∑
k=0
log(di
2k) +
t3∑
k=0
log(di
3k).
Using this, one easily checks that λ(ci
α) = λ(c′i
α) for each i and each α ∈ ∆ 3
n−2(Z). The result now
follows from Proposition 7.7. □
7.1. p SL(n, C)-decorations. Let n be even. All results in this section have natural analogs for
p SL(n, C). The proofs of these are obtained by replacing 2π√−1 by π√−1, and logarithms by lifts
of C
exp
− − →C∗/
⟨±1⟩. In particular, we have
Proposition 7.9. The fundamental class [ρ] ∈ ˆB(C)PSL of a decorated boundary-unipotent repre-
sentation ρ : π1(M ) → p SL(n, C) is independent of the decoration. □
8. A cocycle formula for ˆc
Let i∗ : H3(SL(n, C)) → H3(SL(n, C), N) denote the natural map. We wish to prove that the
composition
(8.1) H3(SL(n, C))
i∗ /d47/d47 H3(SL(n, C), N) λ /d47/d47 ˆB(C) R /d47/d47 C/4π2Z
equals the Cheeger-Chern-Simons class ˆc. Note that i∗ is induced by the map (g0, . . . , g3) ↦→
(g0N, . . . , g3N ).
We shall make use of the canonical isomorphisms
(8.2) H3(SL(n, C)) ∼= H3(SL(3, C)) ∼= H3(SL(2, C)) ⊕ K M
3 (C).
The ﬁrst isomorphism is induced by stabilization (see Susli n [ 25]) and the second isomorphism is
the ±-eigenspace decomposition with respect to the transpose-i nverse involution on SL(3, C) (see
Sah [ 23]).
Lemma 8.1 (Suslin [ 25]). Let D ⊂ SL(3, C) be the subgroup of diagonal matrices. The K M
3 (C)
summand of H3(SL(3, C)) is generated by the elements Bρ∗([T ]), where T = S1 × S1 × S1 is the
3-torus, and ρ : π1(T ) → D is a representation. □
Lemma 8.2. Let T = S1 × S1 × S1 and let ρ : π1(T ) → D be a representation. The extended Bloch
group element [ρ] ∈ ˆB(C) of ρ is trivial.
Proof. We regard T as a cube C with opposite faces identiﬁed, and triangulate C as the cone
on the triangulation on ∂C indicated in Figure 4 with cone point in the center. We order the
vertices of each simplex by codimension, i.e. the 0-vertex is the cone point, the 1-vertex is a face
point etc. Let ρ : π1(T ) → D be a representation, and pick a decoration of ρ by cosets in general
position (the triangulation is such that this is always poss ible). Note that for every 3-simplex ∆
of T , there is a unique opposite 3-simplex ∆ opp, such that the faces opposite the cone point are
identiﬁed. We may assume that the cone point is decorated by t he coset N . If a simplex ∆ is
decorated by the cosets (N, g0N, g1N, g2N ), the simplex ∆ opp must be decorated by the cosets
(N, dg0N, dg1N, dg2N ), where d is the image of the generator of π1(T ) pairing the faces of ∆ and
∆ opp. It thus follows from ( 5.2) that the fundamental class is represented by a sum of terms o f the
form
(8.3) (N, dg0N, dg1N, dg2N ) − (N, g0N, g1N, g2N ) ∈ C gen
3 (SL(n, C)/N).
26 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Let c and c′ be the Ptolemy assignments associated to the tuples (N, g0N, g1N, g2N ) and (N, dg0N,
dg1N, dg2N ). Letting d = diag( d1, . . . , dn), we have c′
t = ct
∏ n
i=t0 di. Fix a lift ~c of c, and consider
the lift
(8.4) ~c′
t =~ct +
n∑
i=t0
log(di)
of c′. One now checks that λ(~c′
α) = λ(~cα) for all α ∈ ˙∆ k
n(Z), so λ(~c) − λ(~c′) = 0 . This proves the
result. □
Theorem 8.3. The composition R ◦ λ ◦ i∗ equalsˆc.
Proof. Since λ commutes with stabilization, it follows from Goette-Zicke rt [ 16] that R ◦ λ ◦ i∗ =ˆc
on H3(SL(2, C)). Since ˆc is zero on K M
3 (C) (this follows from Lemma 8.1 and [ 6, Theorem 8.22]),
the result follows from ( 8.2) and Lemma 8.2. □
Figure 4. Triangulation of ∂C .
Remark 8.4. By deﬁning ˆc = R ◦ λ : H3(SL(n, C), N) → C/4π2Z, we have a natural extension of
the Cheeger-Chern-Simons class to bundles with boundary-u nipotent holonomy, and we can deﬁne
the complex volume as in Deﬁnition 2.11.
