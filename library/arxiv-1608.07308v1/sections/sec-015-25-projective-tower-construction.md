---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-015-25-projective-tower-construction
section_title: "Projective tower construction"
section_number: 2.5
pages: 15-18
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
(2.23) C∗× C∗ ↷ FHilbn
which scales the matricesX,Y independently. We denote the basic characters of this action by
q andt, so the C∗× C∗ action is explicitly given by:
(z1,z 2)· (X,Y ) = (q(z1)X,t (z2)Y ), ∀ (z1,z 2)∈ C∗× C∗
In the matrix presentation, the tautological bundle Tn on FHilbn has ﬁbers consisting simply
of the vector spaces V on which the matrices X,Y act. The fact that ﬂag Hilbert schemes
are deﬁned as B–quotients means that this vector bundle need not be trivial. Therefore, the
matricesX,Y :V→V give rise to endomorphisms of the tautological bundle on the whole of
FHilbn, which we will denote by the same letters:
qTn
X
−→Tn, t Tn
Y
−→Tn
In the formulas above, one must twist the tautological bundle by the torus characters q,t in
order for the endomorphismsX,Y to be C∗× C∗ equivariant. Since a point of the ﬂag Hilbert
scheme entails the choice of a ﬁxed ﬂag ofV , there is a full ﬂag of tautological vector bundles:
Tn↠Tn−1↠...↠T1
on FHilbn. Flag Hilbert schemes are easier to work with than usual Hilbert schemes because
they can be built inductively. Speciﬁcally, we have the maps:
(2.24)
for any∗∈{ C2, C, point}. When ∗ = C we set yn+1 = 0 and when∗ = point we further
setxn+1 = yn+1 = 0. What makes (2.24) manageable is that it is a projective bundle, so we
conclude that ﬂag Hilbert schemes are projective towers. Speciﬁcally, consider the complexes:
(2.25)
for any∗∈{ C2, C, point}, with the maps deﬁned by:
(2.26) Ψ(w) =
(
− (Y−yn+1)w, (X−xn+1)w, 0
)
(2.27) Φ(w1,w 2,f ) = (X−xn+1)w1 + (Y−yn+1)w2 +fv
Here, xn+1,yn+1 are the coordinates on the second factor of FHilbn(C2)× C2, which are
specialized to yn+1 = 0 (resp. xn+1 = yn+1 = 0 ) when∗ = C (resp. ∗ = point ). When
∗ = point, the leftmost bundle in the complex (2.25) isTn−1. This implicitly uses the fact that
16 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
the mapsX,Y :Tn→T n become nilpotent, hence they factor throughTn↠Tn−1. In the next
Subsection, we will prove the following inductive description of ﬂag Hilbert schemes ([44]):
Theorem 2.6. The mapsπ of (2.24) can be written as projectivizations:
(2.28) FHilbn+1 = P
(
H0(En)∨)
:= ProjFHilbn
(
S•(
H0(En)
))
This holds for each of the three variants∗∈{ C2, C, point} of ﬂag Hilbert schemes. The line
bundleLn+1 on the left hand side coincides with the tautological sheafO(1) on the right.
Example 2.7. Example 2.1 shows that the space FHilb2 can be obtained as Proj of an explicit
algebra. Let us obtain the same result using Theorem 2.6. SinceT1 =O, we have:
E1(C2) =
[
qtO
(−y1+y2,x1−x2,0)
−−−−−−−−−−→qO⊕ tO⊕O
(x1−x2,y1−y2,1)
−−−−−−−−−→O
]
≃
≃
[
qtO
(−y1+y2,x1−x2)
−−−−−−−−−→qO⊕ tO
]
⇒ S•(
E1(C2)
)
= C[x1,x 2,y 1,y 2,z,w ]
(x1−x2)w− (y1−y2)z
precisely as in (2.4). Here,z andw are the two basis vectors ofqO⊕tO. If we sety1 =y2 = 0
in the above computation, we obtain the case∗ = C of (2.5). Finally, we have:
E1(point) =
[
qO⊕ tO⊕O
(0,0,1)
−−−→O
]
≃ [qO⊕ tO] ⇒ S• (E1(point)) = C[z,w ]
as expected from (2.6).
Example 2.8. Let us study Theorem 2.6 in the case whenn = 2 and∗ = point, in which case:
FHilb2(point) = P1
with respect to which we haveT1 =O andT2 =O⊕O (1). With this in mind, the complex
(2.25) is explicitly given by:
E2(point) =
[
qtO
Ψ
−→qO⊕ tO⊕O⊕ qO(1)⊕tO(1)
Φ
−→O⊕O (1)
]
and the maps are given by:
Ψ =


0
0
0
−z1
z0


, Φ =
(
0 0 1 0 0
z0 z1 0 0 0
)
It is clear from the above that the map Φ is surjective, which is a general phenomenon that
follows from the cyclicity of triples (X,Y,v ). Therefore, we have:
E2(point)
q.i.s.
∼=
[
qtO
(0,−z1,z0)
−−−−−→qtO(−1)⊕qO(1)⊕tO(1)
] q.i.s.
∼= qtO(−1)⊕O (2)
Therefore, Theorem 2.6 implies that:
(2.29) FHilb3(point) = PP1
(O(1)
qt ⊕O (−2)
)
which is a Hirzebruch surface. It is also the resolution of the singular cubic cone, which is
nothing but the subvariety of the Hilbert scheme consisting of ideals supported at the origin.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 17
2.6. Proving Theorem 2.6. Without loss of generality, we will treat the case∗ = C2. We will
proceed by induction byn, by studying the ﬁbers of the map (2.24):
(2.30)
Recall that points of FHilbn(C2) are triples (X,Y,v ) consisting of two commuting lower tri-
angular matrices (for simplicity, we ﬁx the ﬂag of vector spaces), together with a cyclic vector.
Over such a triple, ﬁbers ofπ are completely determined by extendingX,Y,v by a bottom row:
¯X =
(
X 0
w1 xn+1
)
, ¯Y =
(
Y 0
w2 yn+1
)
, ¯v =
(
v
f
)
wherew1,w 2∈T ∨
n andf∈O . The triple (w1,w 2,f ) must satisfy the following properties:
• The closed condition [ ¯X, ¯Y ] = 0 is equivalent to:
(2.31) w1· (Y−yn+1) =w2· (X−xn+1)
• (w1,w 2,f ) is only deﬁned up to conjugation by:
V ⋊ C∗ = Ker(Bn+1↠Bn) =
(
Id 0
w c
)
(w,c )∈V ⋊ C∗
In other words, we do not consider the action of the group of n×n lower triangular
matricesBn because it has already been trivialized locally onFHilbn(C2). In formulas:
(2.32) (w1,w 2,f )∼ (cw1 +w· (X−xn+1),cw 2 +w· (Y−yn+1),cf +w·v)
• Since we already know that (X,Y,v ) is cyclic, the extra condition that ( ¯X, ¯Y, ¯v) be
cyclic is equivalent to the fact that:
(2.33) Cn+1 is generated by
{
¯v, Im ( ¯X−xn+1), Im ( ¯Y−yn+1)
}
This fails precisely when there exists a linear functionalλ : Cn→ C such that:
λ(v) =f, λ ((X−xn+1)w) =w1·w, λ ((Y−yn+1)w) =w2·w
for allw∈V . This is equivalent to (w1,w 2,f )∼ (0, 0, 0) with respect to (2.32).
Proof. of Theorem 2.6: The three bullets above establish the fact that the triple(w1,w 2,f ) that
determines points in the ﬁbers of FHilbn+1(C2)→ FHilbn(C2)× C2 is a non-zero element in:
(2.34) H0
(T∨
n
qt
Ψ∨
←−T∨
n
q ⊕T∨
n
t ⊕O
Φ∨
←−T ∨
n
)
modulo rescaling. Note that (2.34) is the dual of (2.25), which completes the proof.
□
Remark 2.9. Note that the map Φ of (2.25) is surjective, according to the equivalent description
(2.33) of a point being cyclic. This implies thatEn(∗) is quasi-isomorphic to a complex:
(2.35) En(∗)
q.i.s.
∼=
[
qtTn−δ∗
point
Ψ
−→Ker Φ
]
of vector bundles on FHilbn(∗)×∗ , which lie in degrees−1 and 0.
18 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
