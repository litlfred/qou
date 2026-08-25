---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-018-20-st-ephane-baseilhac1-riccardo-benedetti-2
section_title: "ST ´EPHANE BASEILHAC1, RICCARDO BENEDETTI 2"
section_number: 20
pages: 21-22
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 27 sections: ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE"
---
(b) ρj(Xs) = q−1yj
ki,ai
yj
ki,bi
Aki
aiAki
bi
, if es is an edge of a single triangle τj
ki
, and eki
ai, eki
bi
are the
edges of τj
ki
identiﬁed to es, with eki
ai on the right of eki
bi
.
Consider the diagonal exchange λj→λj+1, and the corresponding triangulated (abstract) squares Q
andQ′, as in Figure 3. The standard representations ρj
i :T →End(CN) associated to the triangles of
Q deﬁne a standard local representationρQ of Tq
λj|Q. Denote by ρQ′ the standard local representation
of Tq
λj+1|Q′ deﬁned fromρQ by the relations (26), where (∆,b, w) is the QH-tetrahedron of (TCφ,˜b, w)
bounded by Q and Q′; we describe below the relations between w and ρj (and hence ρQ). The
representationρQ′ extends (by fusion) to a standard local representation
ρj+1 = (ρj+1
1 ⊗... ⊗ρj+1
2m )◦iλj : Tq
λj+1
→ End((CN)⊗2m)
by stipulating that ρj+1
i = ρj
i on the common triangles of ( S,λj) and (S,λj+1). Since ( S,λj+1) is
given the weak-branching ˜bj+1 induced by its positive side in ( TCφ,˜b, w), for every triangle τj+1
i of
(S,λj+1) where ˜bj+1 diﬀers from the weak-branching given by (S,λj) orQ′, replace the corresponding
representation ρj+1
i by (QT
N)r(F)◦ρj+1
i (X)◦ (QT
N)−r(F), as in Lemma 4.3. For simplicity, we keep
however the same notation for ρj+1. Deﬁne
Lρjρj+1
λjλj+1
: End((CN)⊗2m)→ End((CN)⊗2m)
as the operator acting as the identity on all factors except on the representation space CN⊗ CN ↪→
(CN)⊗2m of ρQ, where it acts by
(
(QT
N)r(F2)⊗ (QT
N)r(F0)
)
◦LT
N(∆,b, w). Here, as usual we denote
by F2 and F0 the 2-faces supporting the target space of LT
N(∆,b, w). By construction, for every
X∈ Tq
λj+1
we have
(29) Lρjρj+1
λjλj+1
◦ρj◦ϕq
λjλj+1
(X′)◦ (Lρjρj+1
λjλj+1
)−1 =ρj+1(X).
Finally, assuming that a standard local representation ρj is given for j = 0, by working as above we
can deﬁne inductively a sequence of standard local representation ρj, j = 0,...,k , and set
Lρ0,ρk
λ0,λk
:=Lρk−1ρk
λk−1λk
◦···◦ Lρ0ρ1
λ0λ1
.
Comparing with (8) we see that
Lρ0,ρk
λ0,λk
=Hred
N (TCφ,˜b, w)T.
Now we have to specialize the choice of ρ0, structurally related to the triangulation ( TCφ,˜b, w).
Similarly to the “classical” lateral shape parameters W +
j (e) (Section 3.1), put:
Deﬁnition 4.4. For every edgee of (S,λj), the lateral quantum shape parameterW+
j (e) is the product
of the quantum shape parameters w(E) of the abstract edges E→ e carried by tetrahedra lying on
the positive side of (S,λj). The quantum shear-bend coordinates of (S,λj) are the scalars
xj(e) :=−q−1W+
j (e).
Denote by λ(1)
j the set of edges of the ideal triangulation λj.
By Proposition 3.2, the quantum shear-bend coordinates xj(e), e∈ λ(1)
j , form a system of N-th
roots of the shear-bend coordinates xj(e) of λj. By ﬁxing w and varying w over w in the tuple
(TCφ,˜b, w), one obtains a family of systems {xj(e)}e∈λ(1)
j
such that x0(e) = xk(φ(e)) for every edge e
of λ =λ0.
The QH-triangulation (TCφ,˜b, w) determines xj(es) for all j∈{ 0,...,k } and every edge es of λj.
Consider the case j = 0, and the regular map
π0 :{y0 = (y0
i,k)i,k}→{ x0 = (x0(es))es∈λ(1)
0
}
deﬁned by
(30) x0(es) = y0
li,aiy0
ri,bi or y0
ki,aiy0
ki,bi
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 21
according to the cases (a) or (b) described at the beginning of Step 3. A simple dimensional count
shows thatπ0 is surjective, with generic ﬁbre isomorphic to (C∗)3m. Then, take a point y0∈π−1
0 (x0).
We get
(31) ρ0(Xs) = x0(es)Ali
ai⊗Ari
bi
or ρ0(Xs) =q−1x0(es)Aki
aiAki
bi
again according to the cases (a) or (b) above. We have to check that the sequence of local representa-
tions ρj constructed by starting from ρ0 is consistent, that is, compatible with w under the diagonal
exchanges. Using the notations of Figure 3, by the tetrahedral and edge relations satisﬁed by the
quantum shape parameters, for all j∈{ 0,...,k } we have
(32) xj(e5) =−q−1w2, xj+1(e5) =−qw−1
2
and
(33) xj+1(e1) = xj(e1)w−1
0 , xj+1(e2) = xj(e2)w−1
1
xj+1(e3) = xj(e3)w−1
0 , xj+1(e4) = xj(e4)w−1
1 .
In particular, (32) for j = 0 is consistent with the relation w2 =−qy3
1y1
0 required by Proposition
