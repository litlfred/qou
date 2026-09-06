---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-009-22-compactification-and-isometries-of-hyperbolic
section_title: "Compactification and isometries of hyperbolic space"
section_number: 2.2
pages: 67-72
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
xn
xn
d 0
t
d
de-t
g
1
g
3
g
1
g
3
Figure 2.9. Two vertical linesγ1 and γ3 in the half-space modelHn
at Euclidean distanced. Thehyperbolic length of the horizontal segment
between them at heightxn is d
xn and hence tends to zero asxn→∞ (left).
Using as a height parameter the more intrinsic hyperbolic arc-length, we
see that the two vertical geodesicsγ1 andγ3 approach at exponential rate,
sinced(γ1(t),γ 3(t))⩽de−t (right).
is equivalent toγ2 sinced(γ2(t),γ 3(t)) =| ln yn
xn|for allt and is also equivalent
toγ1 becaused(γ1(t),γ 3(t))→ 0 as shown in Figure 2.9.
Supposethat γ1 andγ2 convergetodistinctpointsin ∂Dn. Wecanusethe
half-space model again and suppose thatγ1 is upwards vertical andγ2 tends to
someotherpointin {xn = 0}. Inthatcaseweeasilyseethat d(γ1(t),γ 2(t))→
∞: for anyM >0 there is at0> 0 such thatγ1(t) andγ2(t) lie respectively
in{xn+1>M} and
{
xn< 1
M
}
for allt >t0. Whatever curve connects these
two open sets, it has length at leastlnM2, henced(γ1(t),γ 2(t))> lnM2 for
allt >t0. □
2.2.2. The compactiﬁcation.We can giveHn the topology ofDn, and
in that way we havecompactiﬁedHn by adding its points at inﬁnity. The
interior of Hn is Hn, and the points at inﬁnity form a sphere∂Hn.
The topology on Hn may also be deﬁned intrinsically: for anyp∈ ∂Hn
we deﬁne a system of open neighbourhoods ofp in Hn as follows. Letγ be a
half-line with [γ] =p andV be an open neighbourhood of the vectorγ′(0) in
the unitary sphere inTγ(0)Hn. Pickr >0 and deﬁne the subset ofHn:
U(γ,V,r ) =
{
α(t)
⏐⏐α(0) =γ(0), α′(0)∈V, t >r
}
⋃{
[α]
⏐⏐α(0) =γ(0), α′(0)∈V
}
where α indicates a half-line inHn and [α]∈∂Hn its class, see Figure 2.10.
We deﬁne an open neighbourhoods system{U(γ,V,r )} forp by lettingγ,V,
andr vary. The resulting topology onHn coincides with that induced byDn.
Note that Hn is a complete Riemannian manifold (and hence a complete
metric space), while its compactiﬁcationHn is only a topological space: a
point in∂Hn has inﬁnite distance from any other point inHn.
60 2. HYPERBOLIC SPACE
p
g(0)
g
Figure 2.10. An open neighbourhoodU(γ,V,r ) ofp∈∂Hn (in yellow).
We use the Klein model here.
2.2.3. Klein model. In the Klein modelKn⊂ RPn, the compactiﬁcation
is obtained by adding the quadric∂Kn ={x 2
1 +... +x 2
n−x 2
n+1 = 0}, which
is the image of the light cone inRn+1. Analogously, in the hyperboloid model
In we may represent∂In as the set of rays in the light cone.
A nice feature of the Klein model is that the pointsx ∈ RPn that lie
“beyond the inﬁnity”, that is outsideKn, can also be given a natural geometric
interpretation. One such x ∈ RPn\Kn is a space-like ray inRn+1 and as
such it deﬁnes a hyperplanex⊥ of signature(n− 1, 1) in Rn+1, which projects
to a hyperbolic hyperplane inKn. The points beyond the inﬁnity are in 1-1
correspondence with the hyperbolic hyperplanes inKn.
2.2.4. Incident, parallel, and ultraparallel subspaces. A k-subspace
S⊂ Hn has a topological closureS in the compactiﬁcationHn. The boundary
∂S =S∩∂Hn ofS is a (k− 1)-sphere.
For instance, the boundary of a linel consists of two distinct points, the
endpoints ofl. The boundary of a plane is a circle. Two distinct points in∂Hn
are the endpoints of a unique line. A circle in the sphere∂D 3 is the boundary
of a unique plane in the disc model.
The usualdistance d(A,B ) between two subsetsA,B in a metric space is
deﬁned as
d(A,B ) = inf
x∈A,y∈B
{
d(x,y )
}
.
There are three types of conﬁgurations for two subspaces inHn, depicted
in Figure 2.11.
Proposition 2.2.3.LetS andS′ be subspaces inHn of arbitrary dimension.
Precisely one of the following holds:
(1) S∩S′⁄= ∅,
(2) S∩S′ = ∅ andS∩S′ is a point in∂Hn; moreoverd(S,S′) = 0 and
there is no geodesic orthogonal to bothS andS′,
2.2. COMPACTIFICATION AND ISOMETRIES OF HYPERBOLIC SPACE 61
Figure 2.11. Two incident, asymptotic parallel, and ultraparallel lines.
Figure 2.12. Two ultraparallel subspacesS,S′ and a lineγ orthogonal to both.
(3) S∩S′ = ∅; moreover d = d(S,S′) > 0 and there is a unique
geodesicγ orthogonal to bothS andS′: the segment ofγ between
S andS′ is the unique arc connecting them of lengthd.
Proof. IfS∩S′ contains two points then it contains the line connecting
them and henceS∩S′⁄= ∅.
In (2) we use the half-space model and sendS∩S′ at inﬁnity. ThenS and
S′ are Euclidean vertical subspaces and Figure 2.9 shows thatd(S,S′) = 0 .
Geodesics are vertical or half-circles and cannot be orthogonal to bothS and
S′.
In (3), letxi ∈ S and x′
i ∈ S′ be such thatd(xi,x′
i )→ d. Since Hn is
compact, on a subsequencexi → x ∈ S and x′
i → x′∈ S′. By hypothesis
x⁄=x′ and hencex,x′∈ Hn sinced <∞. Therefored >0.
Let γ be the line passing throughx and x′. The segment betweenx and
x′ has lengthd(x,x′) = d. The line is orthogonal toS and S′: if it had an
angle smaller thanπ
2 withS′ we could ﬁnd another pointx′′∈S′ nearx′ with
d(x,x′′) < d. We can drawS,S′,γ as in Figure 2.12 by placing the origin
betweenx andx′: no other line can be orthogonal to bothS andS′. □
Two subspaces of type (1), (2) or (3) are called respectivelyincident,
asymptotically parallel, andultra-parallel.
62 2. HYPERBOLIC SPACE
2.2.5. The conformal sphere at inﬁnity.The sphere at inﬁnity∂Hn has
no metric structure, but it has instead aconformal structure, that is a Rie-
mannian structure considered up to conformal transformations. Before deﬁn-
ing it we note the following.
Proposition 2.2.4.Every isometryϕ: Hn→ Hn extends to a unique home-
omorphismϕ : Hn→ Hn. An isometryϕ is determined by its traceϕ|∂Hn at
the boundary.
Proof. The extension ofϕ to∂Hn is deﬁned intrinsically: a boundary point
is a class[γ] of geodesic half-lines and we setϕ([γ]) = [ϕ(γ)].
To prove the second assertion we show that an isometryϕ that ﬁxes the
points at inﬁnity is the identity. The isometryϕ ﬁxes every line as a set
(because it ﬁxes its endpoints), and since every point is the intersection of two
lines it ﬁxes also every point. □
We give ∂Hn the conformal structure of the sphere∂Dn. The group
Isom(Hn) is generated by sphere inversions, which act conformally: although
the metric tensor of∂Dn is not preserved by this action, its conformal class is
preserved and hence the conformal structure on∂Hn is well-deﬁned.
2.2.6. Elliptic, parabolic, and hyperbolic isometries. It is convenient
to classify the isometries ofHn into three types.
Proposition 2.2.5.Letϕ be a non-trivial isometry ofHn. Precisely one of
the following holds:
(1) ϕ has at least one ﬁxed point inHn,
(2) ϕ has no ﬁxed points inHn and has exactly one in∂Hn,
(3) ϕ has no ﬁxed points inHn and has exactly two in∂Hn.
Proof. The extensionϕ : Hn→ Hn is continuous and has a ﬁxed point by
Brouwer’s Theorem. We only need to prove that ifϕ has three ﬁxed points
P1,P 2,P 3 at the boundary then it has some ﬁxed point in the interior. The
isometryϕ ﬁxes the liner with endpointsP1 andP2. There is only one lines
with endpointP3 and orthogonal tor (exercise): the isometryϕ must also ﬁx
s and hence ﬁxes the pointr∩s. □
Isometriesoftype(1),(2),and(3)arecalledrespectively elliptic,parabolic,
and hyperbolic. A hyperbolic isometry ﬁxes two pointsp,q ∈∂Hn and hence
preserves the unique linel with endpointsp and q. The linel is theaxis of
the hyperbolic isometry, which acts onl as a translation.
2.2.7. Horospheres. Parabolic transformations are related to some ob-
jects in Hn called horospheres.
Deﬁnition 2.2.6. Letp be a point in∂Hn. A horosphere centred inp is a
connected complete hypersurface orthogonal to all the lines exiting fromp.
2.2. COMPACTIFICATION AND ISOMETRIES OF HYPERBOLIC SPACE 63
Figure 2.13. A horocycle inH2 centred inp∈∂H2 is a circle tangent
top. It is orthogonal to all the lines exiting fromp.
Horospheres may be easily visualised in the half-space modelHn by sending
p at inﬁnity. The lines exiting fromp are the Euclidean vertical lines and the
horospheres centred atp are precisely the horizontal hyperplanes{xn = k}
withk >0.
Remark 2.2.7. Since the metric tensorg = 1
x 2n
gE is constant on each
hyperplane{xn =k}, each horosphere isisometric to the EuclideanRn.
The horospheres centred atp⁄=∞ in ∂Hn or at any pointp∈∂Dn are
precisely the Euclidean spheres tangent inp to the sphere at inﬁnity. The
horospheres in H2 are circles and are calledhorocycles, see Figure 2.13. The
portion of Hn delimited by a horosphere is called ahoroball.
Let us go back to the isometries ofHn. We sometimes write a point in
the half-spaceHn as a pair(x,t ) with x∈ Rn−1 and t >0. Isometries with
nice ﬁxed points have nice expressions in the conformal models.
Proposition 2.2.8. Letϕ be an isometry ofHn:
(1) ifϕ is elliptic with ﬁxed point0∈Dn then
ϕ(x) =Ax
for some matrixA∈ O(n);
(2) ifϕ is parabolic with ﬁxed point∞ inHn then
ϕ(x,t ) = (Ax +b,t )
for some matrixA∈ O(n− 1) and some vectorb;
(3) ifϕ is hyperbolic with ﬁxed points0 and∞ inHn then
ϕ(x,t ) =λ(Ax,t )
for some matrixA∈ O(n− 1) and some positive scalarλ⁄= 1.
64 2. HYPERBOLIC SPACE
Proof. Point (1) is obvious. In (2) the isometryϕ ﬁxes∞ and hence
permutes the horospheres centred at∞: we ﬁrst prove that this permutation
is trivial. The mapϕ sends a horosphereO0 at heightt =t0 to a horosphere
O1 at some heightt = t1. If t1⁄= t0, up to changingϕ with its inverse we
may suppose thatt1<t 0.
We know that the mapψ : O1→ O0 sending (x,t 1) to (x,t 0) is a con-
traction: hence ϕ◦ψ :O1→O1 is a contraction and thus has a ﬁxed point
(x,t 1). Thereforeϕ(x,t 0) = (x,t 1). Sinceϕ(∞) =∞, the vertical geodesic
passing through(x,t 0) and (x,t 1) is preserved byϕ, and hence we have found
another ﬁxed point(x, 0)∈∂Hn, a contradiction.
We now know thatϕ preserves the horosphereO at heightt, for allt. The
metric tensor onO is Euclidean (rescaled by 1
t2), henceϕ acts onO like an
isometryx↦→Ax +b. Sinceϕ sends vertical geodesics to vertical geodesics,
it acts with the same formula on each horosphere and we are done.
Concerning (3), the axisl ofϕ is the vertical line with endpoints0 = (0, 0)
and∞, andϕ acts onl by translations: hence it sends(0, 1) to some (0,λ ).
The diﬀerentialdϕ at (0, 1) is necessarily
(A 0
0 λ
)
for someA∈ O(n− 1) and
henceϕ is globally as stated. The caseλ = 1 is excluded because(0, 1) would
be a ﬁxed point inHn. □
The minimum displacementd =d(ϕ) of an isometryϕ of Hn is
d(ϕ) = inf
x∈Hn
d
(
x,ϕ (x)
)
.
A pointx realises the minimum displacement ifd(x,ϕ (x)) =d(ϕ).
Corollary 2.2.9.The following hold:
(1) an elliptic transformationϕ hasd = 0 realised on its ﬁxed points;
(2) a parabolic transformationϕ with ﬁxed pointp∈ ∂Hn has d = 0
realised nowhere and ﬁxes every horosphere centred inp;
(3) a hyperbolic transformationϕ with ﬁxed pointsp,q ∈∂Hn hasd >0
realised on its axis.
Proof. Point (1) is obvious. Point (2) was already noticed while proving
Proposition 2.2.8. Concerning (3), letl be the axis of the hyperbolic trans-
formationϕ. The hyperplane orthogonal tol at a pointx∈l is sent to the
hyperplane orthogonal tol in ϕ(x). The two hyerplanes are ultraparallel and
by Proposition 2.2.3 their minimum distance is realised at the pointsx and
ϕ(x). Hence the points onl realise the minimum displacement forϕ. □
