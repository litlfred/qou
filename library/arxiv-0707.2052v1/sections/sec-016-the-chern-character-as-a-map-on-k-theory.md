---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-016-the-chern-character-as-a-map-on-k-theory
section_title: "The Chern character as a map on K-theory."
section_number: null
pages: 22-24
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
To show that the Chern character descends to a map on K-theory we give
a characterization of the Chern character similar to that of Markarian [10].
For any object E ∈ D(X), which is to be considered an object of D(pt ×
X), there are the following two maps:
ιE : HH•(X)→ Hom•
D(X×X)(E , ΣX ◦ E ); v ↦→ v
E
and
ιE : Hom•
D(X×X)(E , E )→ HH•(X);
E
ϕ ↦→ ϕ 
E
pt
X
.
22
Recall that the Mukai pairing is a non-degenerate pairing on HH•(X) and
that the Serre pairing is a perfect pairing between Hom•
D(X×X)(E , ΣX ◦ E )
and Hom•
D(X×X)(E , E ). With respect to these pairings the two maps ιE and
ιE are adjoint in the following sense.
Proposition 11. For ϕ ∈ Hom•(E , E ) and v ∈ HH•(X) the following equal-
ity holds:
⟨v, ι E ϕ⟩M = ⟨ιE v, ϕ ⟩S
Proof. Here in the third equality we use the invariance of the Serre t race
under the partial trace map.
⟨
v, ι E ϕ
⟩
M
=
⟨
v , ϕ 
E
pt
X
⟩
M
:= Tr

 ptv ϕ 
E
X


= Tr

 v
E
ϕ 
X pt

 = Tr


ϕ 
E
v pt
X


=:
⟨
v
E
,
E
ϕ 
⟩
S
=: ⟨ιE v, ϕ ⟩S.
Note that, using this, the Chern character could have been de ﬁned as
ch(E ) := ιE (IdE ).
Then from the above proposition the following is immediate.
Lemma 12. For v ∈ HH0(X) and E ∈ D(X) there is the equality
⟨v, ch(E )⟩M = Tr(ιE (v)),
and this deﬁnes ch(E ) uniquely.
The fact that the Chern character descends to a function on th e K-group
can now be demonstrated.
Proposition 13. For E ∈ D(X) the Chern character ch(E ) depends only
on the class of E in K0(X). Thus the Chern character can be considered as
a map
ch : K0(X)→ HH0(X).
Proof. It suﬃces to show that if F→ G→ H → F [1] is an exact triangle
in D(X), then
ch(F ) − ch(G ) + ch(H ) = 0
in HH0(X).
23
For G , H ∈ D(X), α : G→ H and v ∈ HH•(X) the diagram on the left
commutes as it expresses the equality on the right:
G α ✲ H
ΣX ◦ G
ιG (v)
❄ IdΣ X ◦ α✲ ΣX ◦ H .
ιH (v)
❄
;
α 
v
H
G
= v
H
α 
G .
In other words, from an element v ∈ HH•(X) we get τR(v) ∈ Hom(IdX, ΣX),
which in turn gives rise to a natural transformation between the functors
IdD(X): D(X)→ D(X) and ΣX ◦ − : D(X)→ D(X). This leads to a map of
triangles
F ✲ G ✲ H ✲ F [1]
SXF
ιF (v)
❄
✲ SXG
ιG (v)
❄
✲ SXH
ιH (v)
❄
✲ SXF [1].
ιF (v)[1]
❄
Observe that if we represent the morphism v by an actual map of complexes
of injectives, and the objects F , G and H by complexes of locally free
sheaves, then the resulting maps in the above diagram commut e on the nose
(no further injective or locally free resolutions are neede d), so we can apply
[11, Theorem 1.9] to get
TrX(ιF (v)) − TrX(ιG (v)) + TrX(ιH (v)) = 0.
Therefore, by the lemma above, for any v ∈ HH•(X),
⟨v, ch(F ) − ch(G ) + ch(H )⟩M = 0.
Since the Mukai pairing on HH0(X) is non-degenerate, we conclude that
ch(F ) − ch(G ) + ch(H ) = 0.
