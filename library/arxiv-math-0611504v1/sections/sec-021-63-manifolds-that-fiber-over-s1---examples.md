---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-021-63-manifolds-that-fiber-over-s1---examples
section_title: "Manifolds that fiber over S1 - Examples"
section_number: 6.3
pages: 35-40
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
the QHFT partition functions of mapping tori.
A speciﬁc class of distinguished ﬂat/charged I-
triangulations of ( ˜
W[ψ], ˜L[ψ], ρ) is obtained by composing one for the trivial mapping cylinder F ×
[−1, 1], say Ttriv, with the monodromy action on the e-triangulation (T, b) of F × {1}, and then gluing
the two boundary components. The monodromy action can always be decomposed as a sequence of
ﬂip moves: a single ﬂip on the ideal triangulation T ′ associated to T deﬁnes a ﬂip on (T, b) if it is
not adjacent to a marked corner, and it lifts to sequences as in Figure 17 otherwise. We view these
sequences as the result of gluing tetrahedra. Hence the monodromy action determines a branched
triangulated pseudo-manifold Ts. This can be completed with global charges, and, as for any ρ we are
free to choose the cocycle in Ttriv, we can also complete Ts to a ﬂattened I-triangulation. Equivalently
we can deﬁne a sequence
(23)
s : (T, b, L) →. . . →ψ(T, b, L)
of e-triangulations with (+)-Log-I-parameters compatible with ρ.
Note that the edges of the as-
sociated pattern Ts of ﬂat/charged I-tetrahedra are disjoint from the Hamiltonian link H. Since
HN(Ttriv) =N id, we deduce that HN( ˜
W[ψ], ˜L[ψ], ρ) =N HN(Ts).
Figure 17.
Lifts to e-triangulations (economic ones - see Remark 3.12 - at the ﬁrst
row) of ﬂip moves on the corresponding ideal triangulations near marked corners.
The tetrahedron associated to the ﬁrst ﬂip (ﬁrst and third ones for the second row)
degenerates for a sequence s with (−)-Log-I-parameters.
Using a similar construction we now prove the relationship with the quantum hyperbolic invariants
HN of ﬁbered cusped manifolds [5]. Recall that W \ L is homeomorphic to Int( ˜
W[ψ]). Denote by l
the number of components of L.
36
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
Proposition 6.11. If Int( ˜W[ψ]) supports a (necessarily unique) complete hyperbolic structure with
holonomy ρc, then HN( ˜
W[ψ], ˜L[ψ], ρc, 0, 0) =N N 2l HN(W \ L).
Proof. Let S \ V be the ﬁber of W \ L →S1, equipped with an ideal triangulation T ′. First we show
the existence of sequences s : T ′ →. . . →ψ(T ′) of ﬂip moves decomposing the monodromy action,
such that the associated pseudo-manifolds T ′
s are topological ideal triangulations of W \ L, which
moreover have maximal volume.
The ﬁrst condition follows from the fact that the monodromy is homotopically aperiodic (ie. pseudo-
Anosov), so that T ′
s is genuinely three-dimensional.
When S \ V is a once-punctured torus, the
second condition is a consequence of a result of Lackenby [23], showing that the monodromy ideal
triangulation of Floyd and Hatcher [17] is isotopic to the canonical Epstein-Penner cellulation. More
in general, since no edge of T ′
s is homotopically trivial, the results of [15] imply that we can straighten
the tetrahedra to oriented geodesic ones, possibly with overlappings, so that the algebraic sum of
volumes is Vol(W \ L). This is known to be maximal [16].
As in Section 6.2 we can complete T ′
s to a ﬂat/charged I-triangulation T ′.
Hence the invariants
HN(W \ L) can be computed as trace tensors HN(T ′). We note that in the case when there are
several ﬁbrations of W \ L, or T ′
s is not canonical, the invariance follows from Theorem 6.8 (2) in [5],
which shows that any two ﬂat/charged I-triangulations of W \ L with maximal volume are QHG-
isomorphic.
Let us denote T ′
s the result of cutting T ′ along the ﬁber.
The two boundary copies are marked
pleated hyperbolic surfaces (T ′, b′, L) →S \V and (T ′, b′, L) →ψ(S \V ), with shear-bend coordinates
(ie. (−)-Log-I-parameters) L that determine completely the log-branches of T ′
s . Recall from Section
5.5 the families of ﬂat/charged I-triangulations Ft and F, and let C ∈F, Ct ∈Ft have boundary
structures (T, b, L), associated to (T ′, b′, L), and (T, b, Lt), respectively, at F × {1}. We have:
HN(T ′)
=
Tr(HN(T ′
s ))
=
N −2l Tr

HN(T ′
s ) ⊗id⊗2l
=
N −2l Tr

HN(C) ◦(HN(T ′
s ) ⊗id⊗2l) ◦HN(ψ(C))−1
=
N −2l lim
t→id Tr

HN(Ct) ◦(HN(T ′
s,t) ⊗id⊗2l) ◦HN(ψ(Ct))−1
=
N −2l lim
t→id Tr(HN(Ct ∗T ′
s,t ∗(−ψ(Ct)))).
Here we use the invertibility of HN(C) (Proposition 5.12) and the equality HN(C) =N HN(ψ(C)).
We deﬁne T ′
s,t as the continuous deformation of T ′
s obtained from the sequence
st : (T, b, Lt) →. . . →ψ(T, b, Lt)
similarly as in (23) (see also Figure 17). In the last equality, Ct ∗T ′
s,t ∗(−ψ(Ct)) is for any ﬁxed t a
distinguished ﬂat/charged I-triangulation of the mapping cylinder of ψ. Hence HN(Ct∗T ′
s,t∗(−ψ(Ct)))
does not depend on t up to conjugacy, and we conclude with Lemma 5.10 (3).
✷
By following the above computation backwards, we see more in general that for any PSL(2, C)-
character ρ that can be realized by (−)-Log-I-parameters on some ideal triangulation of the ﬁber
S \ V , we have
(24)
HN( ˜W[ψ], ˜L[ψ], ρ, h, k) = N 2l Tr(HN(T ′
s ))
where T ′
s is a pattern of ﬂat/charged I-tetrahedra associated to a sequence similar to (23), but with
e-triangulations equipped with (−)-Log-I-parameters compatible with ρ.
Remark 6.12. The formula HN(W \ L) = Tr(HN(T ′
s )) expresses the quantum hyperbolic invariants
of ﬁbered cusped manifolds as amplitudes between two markings of the ﬁber, identiﬁed with a pleated
hyperbolic surface. For a similar construction based on representations of quantum Teichmuller spaces,
see [9].
Example: the ﬁgure-eight knot complement Here we compute the QHFT partition functions
of (S3, K0), where K0 is the 0-framed ﬁgure-eight knot in S3. Recall that S3 \ K is ﬁbered over
S1, with ﬁber the once-punctured torus Σ1,1; the 0-framing of K is induced by the ﬁbration. For
QUANTUM HYPERBOLIC GEOMETRY
37
simplicity, below we consider only characters ρ of injective representations π1(S3 \ K) →PSL(2, C).
The restriction to Σ1,1 of such representations can be realized by (−)-Log-I-parameters on any ideal
triangulation of Σ1,1, so that, by (24), we can determine the corresponding subspace (still denoted
Def(S3, K)) of the phase space of Deﬁnition 5.8 by using the monodromy ideal triangulation.
The monodromy Φ : Σ1,1 →Σ1,1 of S3 \ K is isotopic to the hyperbolic element
 2
1
1
1

=
 1
1
0
1
  1
0
1
1

∈SL(2, Z).
This description of [Φ] ∈Mod(Σ1,1) can be understood in terms of the Diagram of PSL(2, Z) (see eg.
[17]) via the action of Φ on topological ideal triangulations of Σ1,1, which can be represented by two
ﬂip moves. See Figure 18, where the left picture is a lift to R2 \ Z2 of such a triangulation.
B
A
C
B
A
D
Figure 18.
The composition of ﬂip transformations for the monodromy of S3 \ K.
The monodromy ideal triangulation T of S3\K is obtained by realizing each ﬂip move via the gluing of
an ideal tetrahedron, ﬁrst on a ﬁxed triangulation of Σ1,1, then on the resulting one. The remaining
four free faces are identiﬁed under Φ. It is not diﬃcult to see that T is isotopic to the canonical
geodesic ideal triangulation of S3 \ K with its complete hyperbolic structure. The gluing pattern of
the tetrahedra in T is shown in Figure 19.
A
B
D
A
B
D
C
C
Figure 19.
The face and edge identiﬁcations for the canonical geodesic ideal trian-
gulation of S3 \ K.
It is well-known (see [29]) that the deformation space of smooth (non necessarily complete) hyperbolic
structures on S3 \ K is isomorphic to the algebraic set Defhyp(S3 \ K) ⊂H2 × H2 of points (w2, z0)
such that
w2 ∈H2 \
1
2 + t
2i | t ≥
√
15

,
z0 = 1
2 +
1
4 +
1
w2(w2 −1)
 1
2
where w2 is the cross-ratio modulus of the edge e2 in the tetrahedron ∆+ with positive branching
orientation (back edge in the left tetrahedron of Figure 19), and similarly for z0 in ∆−. The space
Defhyp(S3 \ K) is a subspace of
(25)
C = {(w2, z0) ∈(C \ {0, 1})2 | w1w2
2z−2
0 z−1
1
= 1},
which is isomorphic to the whole set of solutions of the edge compatibility relations for cross-ratio
moduli (see Deﬁnition 2.6). By an easy computation we ﬁnd that the edge compatibility relations for
log-branches and charges are:
(S)
 f −
1 + 2f −
0 + 2f +
0 + f +
1 = (arg(w1) + 2 arg(w2) −arg(z1) −2 arg(z0)) −2∗+
1 + 2c−
0 + 2c+
0 + c+
1 = 0
38
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
where ∗+ is the sign of the imaginary part of the wi, and the ﬂattenings f +
i
and f −
i
correspond to
the cross-ratio moduli wi and zi of ∆+ and ∆−, respectively. Hence, by (2) we see that the QHFT
phase space Def(S3, K) is the covering of C given by
Def(S3, K) = {((w2; f +
2 −c+
2 , f +
0 −c+
0 ), (z0; f −
0 +c−
0 , f −
1 +c−
1 )) ∈ˆC× ˆC | (w2, z0) ∈C, (S) is satisﬁed }.
Let us point out some geometrically meaningful subspaces (compare with [25], Section 15).
The
dilation factors of the standard meridian m and longitude l of K are
µ(m) = z2w−1
2 ,
µ(l) = z2
0z−2
2 .
The complete hyperbolic structure of S3 \ K is obtained by solving µ(m) = 1 and µ(l) = 1 for points
of Defhyp(S3 \ K), which gives zj = (wj)∗= exp(iπ/3). We already noticed that the weights k for
this solution take values in 2Z (see [25], Proposition 5.2). Corresponding ﬂattenings satisfy
(27)
f −
2 −f +
2 = k(m),
2f −
0 −2f −
2 = k(l)
and (26) simpliﬁes to
(28)
f −
1 + 2f −
0 + 2f +
0 + f +
1 = 0.
Together with (27) this gives
(29)
f +
1 = k(l)
−1 −2f +
0 ,



f −
0 = k(m) −f +
f −
1 = 2k(m) −k(l)
2
+ 1 + 2f +
Similarly, integral charges are obtained by letting c+
i = −f +
i
on ∆+ and c−
i = +f −
i
on ∆−. It can
be checked that h = 0. Of course, (29) is still true for points of Def(S3, K) suﬃciently near the
complete solution, if now k(m) and k(l) are replaced with ˜k(m) = k(m) −log(µ(m))/
√
−1π and
˜k(l) = k(l) −log(µ(l))/
√
−1π. Hence, in the vicinity of the complete structure we have the strata
{((w2; 2f +
0 −˜k(l), 2f +
0 ), (z0; 2˜k(m) −2f +
0 , 2(2˜k(m) + 1 + 2f +
0 ) −˜k(l)), f +
0 ∈Z},
parametrized by the lifts k(m) and k(l) of µ(m) and µ(l).
For points of C corresponding to hyperbolic structures whose metric completion is obtained from S3\K
by (p, q) Dehn ﬁlling, we have pµ(m) + qµ(l) = 2π
√
−1. Hence the ﬂattenings f = f ′′ of Lemma 6.2
are to satisfy
p(f −
2 −f +
2 ) + q(2f −
0 −2f −
2 ) = −2
Let us ﬁx r, s ∈Z such that ps −qr = 1. Solving simultaneously (28) and the last equation gives
(30)
f +
1 = r −1 −2f +
0 ,

f −
0 = −2s −f +
f −
1 = −r + 4s + 1 + 2f +
The parity condition f +
0 + f +
1 + f −
0 + f −
1 ∈2Z (for the class h to be 0) is automatically satisﬁed.
Now we can compute the QHFT invariants of (S3, K0) as functions on Def(S3, K). Given a N-state
s of T , put α = s(ˆ2), β = s(ˆ0), γ = s(ˆ3) and δ = s(ˆ1), where ˆi denotes the face of ∆+ opposite to the
ith vertex. By 24) we have:
N −2HN(S3, K0, ρ) =
N−1
α,β,γ,δ=0
RN(∆+, b+, w, f +, c+)γ,δ
α,β RN(∆−, b−, z, f −, c−)δ,γ
β,α
=
N−1
X
α,β,γ,δ=0
(w
′−c+
0
w
′c+
0
)
N−1
2
g(w′
g(1) ζγβ+(m+1)γ2 ω(w′
0, w′−1
|α −γ) δ(α + β −δ)
×(z
′−c−
0
z
′c−
0
)
N−1
2
[z′
0]g(1)
g(z′
ζ−αδ−(m+1)δ2
δ(α + β −γ)
ω(z′
0/ζ, z′−1
|β −δ)
=
(w′−c+
1
0
w′c+
0
1
z′−c−
1
0
z′c−
0
1
)
N−1
2
[z′
0]g(w′
0)
g(z′
0)
N−1
X
α,β=0
ζβ2−α2 ω(w′
0, w′−1
1
|N −β) ω(z′
0/ζ, z′−1
1
|N −α)−1.
QUANTUM HYPERBOLIC GEOMETRY
39
By the proof of Proposition 8.6 in [5] we have
[z′
0]g(w′
0)
g(z′
0)
= g((z′
0)∗)∗g(w′
0)
|g(1)|2
and
ω(z′
0/ζ, z′−1
1
|N −α)−1 = ω((z′
0)∗, (z′−1
1
)∗|α)∗
where z∗is the complex conjugate of z. Thus, setting
S(w′
0, w′
1) =
N−1
X
β=0
ζβ2ω(w′
0, w′−1
1
|β) = 1 +
N−1
X
β=1
ζβ2
β
Y
k=1
w′−1
1
1 −w′
0ζk
we get
HN(S3, K0, ρ) = N 2(w′−c+
1
0
w′c+
0
1
z′−c−
1
0
z′c−
0
1
)
N−1
2
g((z′
0)∗)∗g(w′
0)
|g(1)|2
S(w′
0, w′
1) S((z′
0)∗, (z′
1)∗)∗.
Using (29) with k(m) = k(l) = f +
0 = 0 and the global charge with c+
0 = c−
0 = 0, we see that for the
complete hyperbolic structure ρcomp on S3 \ K we have
z′
0 = (w′
0)∗= exp(iπ/3N),
z′
1 = (w′
1)∗= exp(−5iπ/3N).
Hence
HN(S3, K0, ρcomp) = N 2 |g(eiπ/3N)|2
|g(1)|2
|S(eiπ/3N, e−5iπ/3N)|2.
Let us ﬁnally consider hyperbolic (p, q) Dehn ﬁlling of S3\K. Denote S3(K(p,q)) the surgered manifold,
L the core of the surgery, and ρ(p,q) its hyperbolic holonomy. Because of (30) the diﬀerence f ′′ −f
is given on the edges e0, e1 and e2 of ∆+ (resp. ∆−) by 0, r and −r (resp. −2s, 4s and 0). Put
N = 2m + 1. From Theorem 6.3 we deduce
HN(S3(K(p,q)), L, ρ(p,q)) = N 2(w
′−c+
1
0
w
′c+
0
1
z
′−c−
1
0
z
′c−
0
1
)
N−1
2
g((z′
0)∗)∗g(w′
0)
|g(1)|2
N−1
X
α,β=0
ζβ2−α2ω(w′
0, w′−1
1
|N −β) ω((z′
0)∗, (z′−1
1
)∗|α)∗ζr(N−β)(m+1)
N−2s
Y
j=1
(z′−1
1
)∗ζ−4sα(m+1)
1 −(z′
0)∗ζj+α
.
Remark 6.13. Recall the space C in (25).
As already mentionned after Deﬁnition 2.6, we have
a holonomy map hol : C →X to the character variety X = X(π1(S3 \ K)). (See [28] or [18] for
a complete description of the latter). The map hol is generically 2 : 1, and is onto the geometric
component of X [12]. We can express the above partition functions in terms of standard generators
of X by the following observation. Considering S3 \ K as the mapping torus of the monodromy Φ,
the edges e0, e1 of ∆+ are identiﬁed with a longitude l and meridian m of the punctured torus Σ1,1,
and in ∆−we have (e′
0 is opposite to e0):
e0 = Φ(l.m),
e1 = Φ(l),
e′
0 = Φ(m).
As above, assume that ρ has non trivial holonomy at m, l and l.m. Take a ﬂat/charged I-triangulation
of (S3, K0, ρ) as in Section 6.3, with PSL(2, C)-valued cocycle z. Denote zl the value at l, and so
on. Note that zΦ(m) = AzmA−1, where A = z(S1), the cocycle value on the standard meridian of the
knot K. Then the cross ratio moduli of ∆+ and ∆−are given by
w0 = [0 : zl(0) : zlzm(0) : zΦ(m)(0)],
z0 = [0 : zΦ(l)zΦ(m)(0) : zΦ(l)zΦ(m)zΦ(l)(0) : zmzl(0)].
(We use the branching to remove the twofold ambiguity of hol, as it allows to specify an equivariant
association of a ﬁxed point for each peripheral subgroup of ρ(π1(S3 \ K)).)
Remark 6.14. Formulas for Cheeger-Chern-Simons invariants H1(S3, K0, ρ) of arbitrary PSL(2, C)-
characters of S3 \ K come exactly in the same way (See Remark 1.1 and Remark 5.5). In the peculiar
situation of the complete hyperbolic structure and its hyperbolic Dehn ﬁllings, they coincide with
those of [25], Section 15.
40
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
