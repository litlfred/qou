---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-011-5-flag-manifolds-as-matrix-manifolds
section_title: "Flag manifolds as matrix manifolds"
section_number: 5
pages: 16-19
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
By Proposition 3.2(iii) and (iv), we see that a ﬂag manifold may be regarded as a submanifold
of a product of Grassmannians. Since a Grassmannian can be represented as a subset of matrices
in Rn×n [28, Example 1.2.20],
Gr(k,n )∼={P∈ Rn×n :P 2 =P =P T, tr(P ) =k}, (31)
so can a ﬂag manifold; and we will discuss two diﬀerent ways do this, corresponding to (iii) and
(iv) in Proposition 3.2:
Flag(n1,...,n d;n)⊆ Gr(n1,n )× Gr(n2,n )×···× Gr(nd,n ),
Flag(n1,...,n d;n)⊆ Gr(n1,n )× Gr(n2−n1,n )×···× Gr(nd−nd−1,n ).
The correspondence in (31) is given by a map that takes a k-dimensional subspace W∈ Gr(k,n )
to its orthogonal projector,
ε : Gr(k,n )→ Rn×n, W↦→WW T, (32)
where W ∈ Rn×k is any orthonormal basis of W. Note that if W′ is another such n×k matrix,
then W′ = WQ for some Q∈ O(k) and so W′W′T = WW T and the map ε is well-deﬁned. It is
also injective and its image is precisely the set on the right of (31).
OPTIMIZATION ON FLAG MANIFOLDS 17
5.1. Projection coordinates for the ﬂag manifold. We will construct our ﬁrst analogue of
(32) for the ﬂag manifold. Let
ε : Flag(n1,...,n d;n)→ Rnd×nd, {Vi}d
i=1↦→ diag(V1V T
1,...,V dV T
d ), (33)
where Vi∈ Rn×ni is an orthonormal basis of Vi, i = 1,...,d , and the image is a block-diagonal
matrix in Rnd×nd with d blocks V1V T
1,...,V dV T
d ∈ Rn×n. In fact, the map in (33) is essentially the
map in (6) that we used to establish Proposition 3.2(iii) except that we identify the Grassmannians
with sets of projection matrices as in (31).
Proposition 5.1. The ﬂag manifold Flag(n1,...,n d;n) is diﬀeomorphic to
{P = diag(P1,...,P d)∈ Rnd×nd :P 2
i =Pi =P T
i, tr(Pi) =ni, PjPi =Pi, i<j}. (34)
Proof. One may check that ε in (33) has its image in contained in the set (34); and the map that
takesP = diag(P1,...,P d) to the ﬂag {im(Pi)}d
i=1∈ Flag(n1,...,n d;n) is its inverse. □
We will call the representation in Proposition 5.1 projection coordinates for the ﬂag manifold.
Unlike the orthogonal and Stiefel coordinates introduced earlier, which are not unique, projection
coordinates are unique. Let {Vi}d
i=1∈ Flag(n1,...,n d;n) with
(a) orthogonal coordinates JQK for some Q∈ O(n);
(b) Stiefel coordiantes JY K for some Y ∈ V(nd,n );
(c) projection coordinates P as in (34).
We have seen how we may easily convert between orthogonal and Stiefel coordinates after (26), we
now see how they may be interchanged with projection coordinates just as easily:
(a)→(c): Given Q = [q1,...,q n]∈ O(n), let Qi = [q1,...,q ni]∈ V(ni,n ); then Pi = QiQT
i , i =
1,...,d .
(b)→(c): Given Y = [y1,...,y nd] ∈ V(nd,n ), let Yi = [y1,...,y ni] ∈ V(ni,n ); then Pi = YiY T
i ,
i = 1,...,d .
(c)→(b): Given P = diag(P1,...,P d), let y1,...,y ni be an orthonormal basis of im( Pi); then Yi =
[y1,...,y ni]∈ V(ni,n ), i = 1,...,d .
(c)→(a): As above but appending an orthonormal basis ynd+1,...,y n of im(Pd)⊥ gives us Q =
[y1,...,y nd,ynd+1,...,y n]∈ O(n).
As is the case for the Grassmannian, the ﬂag manifold has several extrinsic coordinates systems
with which diﬀerential geometric objects and operations have closed-form analytic expressions
and where one coordinate representation can be transformed to another with relative ease. This
ﬂexibility to switch between coordinate systems can be exploited in computations but as we will
see next, it can also be exploited in deriving the requisite analytic expressions.
Proposition 5.2 (Tangent spaces IV). Let P = diag(P1,...,P d)∈ Flag(n1,...,n d;n) as repre-
sented in (34). Then the tangent space is given by
TP Flag(n1,...,n d;n) ={Z = diag(Z1,...,Z d)∈ Rnd×nd :ZiPi +PiZi =Zi =Z T
i,
tr(Zi) = 0, ZjPi +PjZi =Zi, i<j, i,j = 1,...,d. } (35)
Proof. Letγ(t) be a curve in Flag(n1,...,n d;n) as characterized by (34), i.e.,γ : (−1, 1)→ Rnd×nd,
t↦→ diag
(
P1(t),...,P d(t)
)
where
Pi(t)2 =Pi(t), Pi(t)T =Pi(t), tr(Pi(t)) =ni, Pj(t)Pi(t) =Pi(t), i<j, i,j = 1,...,d, (36)
for all t∈ (−1, 1). Taking derivatives of these relations at t = 0 gives the required description. □
Again the ease of translation from orthogonal and Stiefel coordinates to projection coordinates
yields counterparts of Proposition 4.4–4.9 readily. We will just provide expressions for geodesic and
parallel transport as examples.
18 K. YE, K. S.-W. WONG, AND L.-H. LIM
Proposition 5.3 (Geodesics IV). LetP = diag(P1,...,P d)∈ Flag(n1,...,n d;n) be as represented
in (34) and Z = diag(Z1,...,Z d)∈ TP Flag(n1,...,n d;n) be as represented in (35). Then there
exist Y ∈ V(nd,n ) and skew-symmetric B∈ Rn×n such that for Yi =YIn,ni, Bi =BIn,ni∈ Rn×ni,
Pi =YiY T
i , Z i =YiBT
i +BiY T
i , i = 1,...,d ; (37)
and a geodesic P (t) passing through P in the direction Z takes the form
{diag
(
P1(t),...,P d(t)
)
∈ Rnd×nd :Pi(t) =Yi(t)Yi(t)T, Yi(t) = [Y,Y ⊥] exp(tB)In,ni}. (38)
Proof. The matrixY is justP in Stiefel coordinates and may be obtained from (c)→(b) above. By
Proposition 4.14, in Stiefel coordinates, the geodesic through JY K in direction [Y,Y ⊥]BIn,nd is
J[Y,Y ⊥] exp(tB)In,ndK.
By (b)→(c), Y and P are related by Pi = YiY T
i , i = 1,...,d , which upon diﬀerentiation gives
Zi =YiBT
i +BiY T
i . The required expression (38) then follows. □
The observant reader might have noticed thatBd+1 does not appear in (37) — the reason is that
since B is skew-symmetric, Bd+1 is uniquely determined by B1,...,B d.
Proposition 5.4 (Parallel transport III). LetP , Z, Y , B, and P (t) be as in Proposition 5.3. Let
Y⊥∈ V(n−nd,n ) be such that [Y,Y ⊥]∈ O(n) and set
Yi(t) = [Y,Y ⊥] exp(tB)In,ni, X i(t) = [Y,Y ⊥] exp(tB)e−ϕtB(X)In,ni, i = 1,...,d. (39)
Then the parallel transport of the tangent vector Z along the geodesic P (t) is given by
Z(t) = diag
(
Z1(t),...,Z d(t)
)
, Z i(t) =Yi(t)Xi(t)T +Xi(t)Yi(t)T, i = 1,...,d. (40)
Proof. As in the proof of Proposition 5.3, we obtain the corresponding projection coordinates
P = diag(P1,...,P d), Pi = YiY T
i , Yi = YIn,ni, i = 1,...,d . Diﬀerentiating these relations give a
tangent vector Z = diag(Z1,...,Z d)∈TP Flag(n1,...,n d;n) in projection coordinates as
Zi =YiX T
i +XiY T
i , i = 1,...,d,
whereX∈TJY K Flag(n1,...,n d;n) is the expression of the same tangent vector in Stiefel coordinates
as in Proposition 4.11 and Xi =XIn,ni, i = 1,...,d . The required expressions (39) and (40) then
follow from the expression (30) for parallel transport in terms of Stiefel coordinates Y . □
5.2. Reﬁned projection coordinates for the ﬂag manifold. We discuss a variation of projec-
tion coordinates on ﬂag manifolds based on Proposition 3.2(iv). As in Section 5.1, if we identify
the Grassmannians as sets of projection matrices as in (31), then the map in (7) becomes
ε′ : Flag(n1,...,n d;n)→ Rnd×nd, {Vi}d
i=1↦→ diag(W1W T
1,...,W dW T
d ), (41)
where column vectors of Wi∈ Rn×(ni−ni−1) form an orthonormal basis of V⊥
i−1, the orthogonal
complement of Vi−1 in Vi, i = 1,...,d . This gives us another description of Flag( n1,...,n d;n) as
a matrix manifold, an analogue of Proposition 5.1.
Proposition 5.5. The ﬂag manifold Flag(n1,...,n d;n) is diﬀeomorphic to
{R = diag(R1,...,R d)∈ Rnd×nd :R2
i =Ri =RT
i, tr(Ri) =ni−ni−1, RiRj = 0, i<j}. (42)
We call the representation in Proposition 5.5 reduced projection coordinateson the ﬂag manifold
Flag(n1,...,n d;n). Again, it is straightforward to translate between the other three coordinates
systems and reduced projection coordinates. This readily yields expressions for metric, tangent
space, geodesic, and parallel transport in reduced projection coordinates as before. We will state
those for tangent space and metric as examples.
OPTIMIZATION ON FLAG MANIFOLDS 19
Proposition 5.6 (Tangent spaces V). LetR = diag(R1,...,R d)∈ Flag(n1,...,n d;n) be as repre-
sented in (42). Then the tangent space is given by
TR Flag(n1,...,n d;n) ={Z = diag(Z1,...,Z d)∈ Rnd×nd :RiZi +ZiRi =Zi =Z T
i,
tr(Zi) = 0, ZiRj +RiZj = 0, 1≤i<j ≤d.} (43)
Propositions 5.5 and 5.6 give an alternative way to obtain the metric g in Proposition 4.4. Let
gi be the standard metric on Gr( ni−ni−1,n ), i = 1,...,d . Then it is straightforward to verify
that g is the pull-back of ∑d
i=1gi via the embedding (7) in Proposition 3.2(iv). This also gives us
an expression for the metric in terms of reduced projection coordinates.
Proposition 5.7 (Riemannian metric III) . Let R = diag(R1,...,R d)∈ Flag(n1,...,n d;n) be as
in (42). Let W = diag(W1,...,W d),Z = diag(Z1,...,Z d)∈ TR Flag(n1,...,n d;n) be as in (43).
Then there exist Vi,Ai,Bi∈ Rn×(ni−ni−1) such that
ViV T
i =Ri, VT
i Vi =Ini−ni−1, ViAT
i +AiV T
i =Wi, VT
i Ai = 0, ViBT
i +BiV T
i =Zi, VT
i Bi = 0, (44)
and the metric g is given by
gR(W,Z ) =
d∑
i=1
tr(AT
iBi).
Proof. As the Grassmannian is just a ﬂag manifold with d = 1, all our earlier discussions about
Stiefel and projection coordinates also apply to it. So for Wi,Zi∈TRi Gr(ni−ni−1,n ) in projection
coordinates, there exist Vi,Ai,Bi∈ Rn×(ni−ni−1) satisfying (44). The standard Riemannian metric
gi on Gr(ni−ni−1,n ) at Ri is then given by gi(Wi,Zi) = tr(AT
iBi) and thus we have
gR(W,Z ) =
d∑
i=1
gi(Wi,Zi) =
d∑
i=1
tr(AT
iBi). □
