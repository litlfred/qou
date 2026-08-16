---
doc_id: arxiv-1012.1039v2
doc_title: "where vn is the volume of a regular ideal hyperbolic n–simplex. This result gener- alizes the fact that hyperbolic Dehn ﬁlling of a 3–manifold d oes not increase hyperbolic volume"
section_id: sec-005-3-main-result
section_title: "Main result"
section_number: 3
pages: 8-14
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
In this section we prove the main result, Theorem 1.5. The strategy is to modify
an eﬃcient relative fundamental cycle for ( M,∂M ) to a fundamental cycle on the
ﬁlling, without increasing norm by too much.
Lemma 3.1. Let X be a topological space. Let c ∈ Cn(X; R) be homologous to a
rational chain, and let ǫ >0. Then there is some c′ ∈ Cn(X; Q) homologous to c
so that ‖c′ −c‖1<ǫ . If c is symmetric, c′ can be chosen to be symmetric.
Proof. By assumption, there is some f ∈Cn+1(X; R) so that c +∂f ∈Cn(X; Q).
Since Cn+1(X; Q) is dense in Cn+1(X; R), there is some f ′ ∈ Cn+1(X; Q) with
‖f −f ′‖< ǫ
n+2 . The chain c′ =c +∂(f −f ′) satisﬁes ‖c′ −c‖<ǫ , since ‖∂n+1‖ =
n + 2.
Ifc is symmetric, we can take f andf ′ to be symmetric in the above argument,
and it will follow that c′ is symmetric. □
Deﬁnition 3.2. Let T be a ﬁnite triangulation of a space X, and let T ′ be its
barycentric subdivision. The (closed) star neighborhood of a simplex τ of T is the
union of those simplices of the subdivision T ′ intersectingτ . A point in the interior
of an n–simplex of X lies in at least one closed star neighborhood of a vertex, and
in at most n + 1 such closed stars.
The open star neighborhood of a simplex is the interior of its star neighborhood.
(So the open star neighborhood of a simplex does not include its prop er faces.) The
open star neighborhoods of the simplices of T form an open cover of X.
Let σ : ∆ n →X be a singular simplex. We say σ is small with respect to T if
the image of σ is contained entirely in the open star of some vertex of T ′.
A singular chain will be called small if all its simplices are small.
Given an order on the vertices of T there is a canonical way to homotope a small
chain to an aﬃne chain, as we describe in the next lemma.
Lemma 3.3. LetX be a space with a (combinatorial) triangulation T , and let <T
be a total order on the vertices of T . Canonically associated to any small singular
simplex σ : ∆ n →X are
(1) a “straightened” aﬃne simplex a(σ), and
(2) a homotopy ft(σ) so that f0(σ) = σ and f1(σ) = a(σ),
so that if F is a face of ∆ n, then a(σ|F ) = a(σ)|F and ft(σ|F ) = ft(σ)|F . (In
other words, homotopies on a face depend only on that face, so a cycle remains a
cycle throughout the homotopy.) Moreover, if σ is invariant under precomposition
with an aﬃne map τ , so are a(σ) and ft(σ).
Proof. The idea is illustrated quite well by the ﬁgure given in the proof of Prop o-
sition 6.5.1 in Thurston’s notes [Thu80]. We give a little more detail. (The ﬁ gure
given there is not of a combinatorial triangulation. In that case a to tal order on
the “corners” of the simplices must be given, rather than on the ve rtices. We avoid
this complication here by assuming a combinatorial triangulation.)
We begin by deﬁning the straightening a(σ). For x ∈ X deﬁne n(x) to be the
least vertexv of T so thatx is in the closed star neighborhood of v. Let {v0,...,v n}
be the vertices of the standard simplex ∆ n. Since σ is small, the image of σ lies in
the open star neighborhood of some simplex τ of T . (In fact there may be several
choices for τ , but the maps a(σ) and ft(σ) we deﬁne will not depend on the choice.)
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 9
It follows that n(σ(vi)) is a vertex of τ for each i. We deﬁne a(σ)(vi) = n(σ(vi))
and then extend to an aﬃne map a(σ) : ∆ n →τ . It is clear that if F is a face of
∆ n we have a(σ|F ) = a(σ)|F .
We now must deﬁne the homotopies ft(σ). For each x ∈ ∆ n, we let τ (x) be the
unique simplex of T so that
(1) σ(x) ∈τ (x), and
(2) τ (x) has minimal dimension subject to (1).
Since τ (x) lies in the open star neighborhood of τ , the simplex τ is a face of τ (x).
Thus both σ(x) and a(σ)(x) lie in τ (x). Convex combination is well-deﬁned for
points in the same simplex, so we may take, for t ∈ [0, 1],
ft(σ)(x) = (1 −t)σ(x) +ta (σ)(x).
The reader may check that ft is well-deﬁned, continuous, and satisﬁes the property
ft(σ|F ) = ft(σ)|F for each face F of ∆ n.
Finally, we note that if τ is some aﬃne map from ∆ n to itself so that σ ◦τ =σ,
then a(σ ◦τ ) = a(σ) and therefore ft(σ ◦τ ) = ft(σ) for all t. □
Lemma 3.4. Let N be a manifold, and let T be a triangulation of ∂N . If c ∈
Ck(N ; R) is a relative singular cycle in (N,∂N ) so that ∂c is small with respect to
T , then c is (relatively) homologous to c′ with ‖c′‖1 ≤ ‖c‖1 and∂c′ an aﬃne chain.
If c was symmetric, then so is c′.
Proof. The chainc is a ﬁnite linear combination c =∑ m′
i=1λiσi of singular simplices
σi : ∆ k → N . The idea is to “preassemble” the simplices to get a map φ : Kc →
N from a certain CW complex Kc, so that c is φ♯ of a linear combination of
characteristic maps. We can use Lemma 3.3 to homotope the “bound ary” of Kc to
a simplicial map, and then apply the homotopy extension property of CW pairs.
More precisely, let J = {1,...m ′}/ ∼, where i ∼ j if σi = σj ◦q for some
permutation q. We deﬁne
(6) Kc =

∐
[i]∈J
∆ k
[i]

/ ∼
where x1 ∼x2 whenever there are ( k − 1)–dimensional faces F1 ⊂ ∆ k
[i1] and F2 ⊂
∆ k
[i2] satisfying
(1) xj ∈Fi for j ∈ {1, 2}, and
(2) there is an aﬃne map τ : F1 →F2 so that τ (x1) = x2 andσi1 |F1 =σi2 ◦τ .
That is, if two singular simplices agree on a codimension 1 face, we glue t he corre-
sponding faces together in Kc. Moreover, if a codimension 1 face is unchanged by
precomposing with some isometry, we identify the face to itself by th e correspond-
ing symmetry. We thus obtain a CW complex Kc and a map φ : Kc →N given by
φ(x) = σi(x) where x ∈ ∆ k
[i]. In the complex Kc we can canonically build a chain
˜c made up of “characteristic maps” ∆ k
[i] →Kc so that
c =φ♯(˜c).
If c was symmetric, then so is ˜c.
The boundary ∂˜c is supported in some minimal subcomplex of Kc, which we’ll
refer to as ∂Kc. Because c is a relative cycle, the map φ described in the last
10 K. FUJIW ARA AND J. F. MANNING
paragraph is really a map of pairs
φ : (Kc,∂K c) → (N,∂N ).
After ﬁxing some total order on the simplices of T , Lemma 3.3 gives a homotopy
in∂N of φ|∂Kc to a “simplicial” map ψ; this map is simplicial in the sense that if
F is any face of one of the simplices ∆ k
[i] used to deﬁne Kc, and if ιF is the inclusion
map, then φ ◦ιF is aﬃne, with image in a single simplex of T .
By the homotopy extension property of CW pairs, the homotopy fr omφ|∂Kc to
ψ can be extended to all of Kc. Let
Φ t : Kc →N , t ∈ [0, 1]
be this homotopy, with Φ 0 =φ. The chain
c′ = (Φ 1)♯(˜c)
has all the properties we want. □
We need to show that tori can be triangulated so that every simplex of diameter
much smaller than the injectivity radius is small. Say that a triangulatio n of a torus
is K–fat if every singular simplex of diameter less than K is small with respect to
that triangulation.
Lemma 3.5. For each d ≥ 1 there is a constant 0 < Kd < 1 so that every ﬂat
torus of dimension d with injectivity radius R has a (KdR)-fat triangulation with
td = 2 dd! simplices.
Proof. LetT be a ﬂat d–torus, which we can think of as Rd/Λ, where Λ is some rank
d lattice. Every such lattice has a Lov´ asz–reduced basis [LLL82] B = {v1,..., vd}.
Fork ∈ { 1,...,d } deﬁne θk to be the angle made by vk with the subspace of Rd
spanned by the rest of the basis. Babai [Bab86] showed that, for all k,
sin(θk) ≥
(√
2
3
)d
.
Any basis B of Λ gives rise in a canonical way to a triangulation TB of T with
td simplices given by the ﬁrst barycentric subdivision of the parallelepipe d spanned
by B.
LetV be the set of all ordered bases of lattices in Rd, topologized as a subset of
Rd2
, and let F : V → R+ be the function which sends B to the least real k so that
TB is k–fat. The number F (B) is also the least number k so that triangulation of
Rd coveringTB is k–fat. We note the following useful properties of F :
(1) F is continuous and positive everywhere on V .
(2) If λ ∈ R+ and B ∈ V , then F (λB) = λF (B).
(3) If there is a length-decreasing map from B to B′ then F (B) ≥F (B′).
LetU ⊂V be the set of bases consisting of unit vectors, any two of which mak e
an angle θ with sin(θ) ≥
(√
2
3
)d
. Since U is compact, F takes some minimum,
positive value L on U . We will show that every torus of injectivity radius ≥ 1/2
has a triangulation which is L–fat. Linearity of F (property (2) above) then implies
the lemma for Kd = 2L.
Let T = Rd/Λ be a torus of injectivity radius at least 1 /2. A Lov´ asz-reduced
basis B = {v1,..., vd} for Λ has all angles between basis vectors within [ π/3, 2π/3],
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 11
by Babai’s result. Since the injectivity radius of T is at least 1/2, there is a distance-
decreasing map from B to a basis in U , namely
B′ =
{ v1
‖v1‖,..., vd
‖vd‖
}
.
Property (3) above tells us that F (B) ≥ F (B′) ≥ L, so the triangulation TB is
L–fat, and the proof of the lemma is completed. □
Lemma 3.6. For each d ≥ 1 and each s there is a constant K(d,s ) so that any
null-homologous real singular s–cycle z in a d–dimensional torus bounds a singular
(s + 1)–chain c with
‖c‖1 ≤K(d,s )‖z‖1
Proof. We follow the proof of [Thu80, Proposition 6.5.1],which discusses the c ase
d = s = 2. Let T be a d–dimensional torus, and let z be an s–cycle. Since there
are only ﬁnitely many singular simplices in z, their lifts to the universal cover Rd
have diameters bounded by some D> 0. Let Kd be the constant from Lemma 3.5,
and let ˜T
π
− →T be some cover of T with injectivity radius bigger than D/Kd. By
Lemma 3.5, there is a triangulation T of ˜T withtd simplices so that if ˜σ : ∆ s → ˜T
is any lift of a singular simplex appearing in z, then ˜σ is small with respect to T (in
the sense of Deﬁnition 3.2). The proof of Lemma 3.5 shows that the c ombinatorics
of this triangulation are independent of the particular chain z and the cover ˜T .
WriteC∗(X) for the real singular chain complex of X. There is a transfer map
trans : C∗(T ; R) →C∗( ˜T ; R)
which sends any singular simplex to the average of its lifts. The map tr ans is
an isometric embedding with respect to the l1 norm. The map π♯ : C∗( ˜T ; R) →
C∗(T ; R) induced by the covering is norm decreasing and ( π♯ ◦ trans) is the identity
map.
By the choice of ˜T and T , the chain trans( z) is small. By Lemma 3.3, the
simplices of trans( z) can be homotoped simultaneously and consistently to the
aﬃne singular simplices making up the singular chain a(trans(z)). Triangulating
this homotopy in a standard way, we ﬁnd that trans( z) −a(trans(z)) bounds an
(s + 1)–chain c1 inT , so that
‖c1‖1 ≤C1‖z‖1
for some constant C1 depending on the dimension s but otherwise independent of
z. The space of aﬃne real singular s–boundaries B is ﬁnite dimensional, and only
depends on the combinatorics of the triangulation T .
The aﬃne ﬁlling norm ‖b‖ﬁll on B is deﬁned, for a boundary b ∈ B, to be the
smallest l1–norm of an aﬃne ( s + 1)–chain bounded by b. Let
C2(d,s ) = sup {‖b‖ﬁll |b ∈B and ‖b‖1 = 1},
and note that C2(d,s ) only depends on the combinatorics of T .
The boundary a(trans(z)) bounds an ( s + 1)–chain c2 in T of l1–norm at most
C2(d,s )‖a(trans(z))‖1 ≤C2‖z‖1. Thus we have
trans(z) = ∂(c1 +c2)
and
z =π♯(∂(c1 +c2)) = ∂(π♯(c1 +c2))
12 K. FUJIW ARA AND J. F. MANNING
and
‖π♯(c1 +c2)‖1 ≤ ‖c1 +c2‖1 ≤ (C1(s) +C2(d,s )) ‖z‖1.
□
We now prove the main theorem.
Proof of Theorem 1.5. We suppose thatM is a compact n–manifold with boundary
a union of tori, so that the interior admits a complete hyperbolic metr ic of ﬁnite
volume. We ﬁx a 2 π–ﬁlling M (T1,...,T m). To prove the theorem we must show
0< ‖M (T1,...,T m)‖ ≤ Vol(V )
vn
,
where vn is the volume of a regular ideal hyperbolic n–simplex.
The lower bound follows from [MY] and is given above in Corollary 2.4.
We now establish the upper bound. The strategy is to ﬁrst choose a symmetric
representativec0 for the (relative) fundamental class of ( M,∂M ) which is close to
optimal, and then modify it to obtain a fundamental class c′
0 forM (T1,...,T m). If
such a modiﬁcation can be done in such a way that |c′
0|1 is within some arbitrarily
small constant of ‖M,∂M ‖, then we will have shown:
‖M (T1,...,T m)‖ ≤ ‖M,∂M ‖
The ﬁrst step is to pass to a rational cycle. Let ǫ> 0. Let c0 ∈Cn(M ; R) be a
real symmetric singular relative cycle representing [ M,∂M ], and satisfying
(7) ‖c0‖1< ‖M,∂M ‖ +ǫ
By Lemma 3.1, there is a symmetric rational singular relative cycle c1 ∈Cn(M ; Q)
homologous to c0 with ‖c1 −c0‖1<ǫ .
We now pick a ﬁnite cover and triangulation of the boundary so that ∂c1 lifts to
a chain which is small with respect to that triangulation. Let tn−1 = 2 n−1(n − 1)!.
Claim 3.7. We can choose a ﬁnite cover ˜M
π
− →M and a triangulation T of ∂ ˜M
satisfying the conditions:
(1) The restriction of π to any component of ∂ ˜M has degree bigger than m/ǫ,
wherem is the number of cusps of M .
(2) If trans : C∗(M ; R) → C∗( ˜M ; R) is the transfer map, then trans(∂c1) is
small with respect to T .
(3) Each boundary component of ˜M is triangulated by tn−1 (n − 1)–simplices.
Proof. The compact manifold M is homeomorphic to
M as described in the intro-
duction, a hyperbolic manifold minus a union of disjoint horospherical neighbor-
hoods of its cusps. We identify M with M . Any simplex in the support of ∂c1
therefore lifts to Hn. Only ﬁnitely many such simplices occur, so there some num-
ber r bounding the diameter of any such lift. Residual ﬁniteness of π1M implies
that we can pass to a ﬁnite cover ˜M →M so that
(1) Every boundary component of ˜M has injectivity radius bigger than r/Kn−1,
where Kn−1 is the constant from Lemma 3.5, and
(2) Every boundary component N of ˜M has area at least m/ǫ times more than
the area of the component of ∂M covered by N .
Lemma 3.5 implies that ∂ ˜M admits an r–fat triangulation with tn−1 (n − 1)–
simplices per component so that singular simplices lifted from ∂c are all small
respect to this triangulation. □
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 13
Let D be the degree of the cover coming from Claim 3.7. Since c1 is rational
and symmetric, trans(c1) must also be rational and symmetric. In particular,
trans(c1) = 1
qc2
for some integral symmetric chain c2 ∈ CS
∗ ( ˜M ; Z) and some positive integer q.
Homologically [c2] = q
D [ ˜M,∂ ˜M ] in Hn( ˜M,∂ ˜M ; R). Since trans : C∗(M ; R) →
C∗( ˜M ; R) is isometric, ‖c2‖1 =q‖c1‖1.
Since trans(∂c1) is small with respect to T , the chain ∂c2 is also small with
respect to T . Using Lemma 3.4, we ﬁnd a symmetric integral chain c3 with ‖c3‖1 ≤
‖c2‖1 so that c3 is (relatively) homologous to c2 and so that ∂c3 is an aﬃne chain,
i.e., ∂c3 ∈CT
n−1(∂ ˜M ; Z).
Let ˜N1,..., ˜Np be the boundary components of ˜M . We have [ c3] = q
D [ ˜M,∂ ˜M ]
inHn( ˜M,∂ ˜M ) and [∂c3] = q
D
∑ p
i=1[ ˜Ni] in Hn−1(∂ ˜M ).
The cycle ∂c3 is symmetric, aﬃne and represents q
D times the fundamental class
of ∂ ˜M . By Lemma 2.9, ∂c3 has no “degenerate” aﬃne simplices in its support.
It follows that ∂c3 consists of exactly q
D appropriately oriented copies of every
(n − 1)–simplex in T .
Each of the p boundary components of ˜M is triangulated with exactly tn−1
simplices of dimension n − 1. We therefore have
‖∂c3‖1 =pt n−1
q
D.
For each i between 1 and n, the ith boundary component of M is covered by pi
boundary components of ˜M , so that p =∑
ipi. The degrees of these components
are di1,...,d ipi , and ∑
jpij =D for each i. Since each dij ≥ m
ǫ , we get
D ≥pi
m
ǫ ∀i,
which implies that mD ≥p m
ǫ , and so p ≤ǫD. We therefore obtain
‖∂c3‖1 ≤ǫtn−1q.
Projecting c3 back down to M gives a chain c4 with [c4] = q[M,∂M ] in relative
homology, and with
‖c4‖1 ≤ ‖c3‖1 ≤ ‖c2‖1 =q‖c1‖1,
and with
‖∂c4‖1 ≤ ‖∂c3‖1 ≤ǫtn−1q.
Dividing by q we obtain a fundamental cycle c = 1
qc4 for [M,∂M ] satisfying ‖c‖1 ≤
‖M,∂M ‖ + 2ǫ and ‖∂c‖1 ≤tn−1ǫ.
Now we will take this relative cycle c for [M,∂M ], and modify it to an honest
cycle in M (T1,...,T m). We start by pushing it forward from M toM (T1,...,T m)
by a map of pairs
h : (M,∂M ) → (M (T1,...,T m),Z ),
where Z is the singular set of M (T1,...,T m) and h is the quotient map described
in Deﬁnition 1.3. (Here we are implicitly identifying M with the space M described
before Deﬁnition 1.3.) Let ∂h be h restricted to ∂M . The chain ( ∂h)♯(∂c) is an
(n − 1)–cycle in Z. Lemma 3.6 implies there is some K depending only on n so that
(∂h)♯(∂c) can be ﬁlled in Z with a n–chainc′ satisfying ‖c′‖1 ≤K‖(∂h)♯(∂c)‖1 ≤
14 K. FUJIW ARA AND J. F. MANNING
Kt n−1ǫ. It is easy to check that h♯c −c′ is a fundamental cycle for M (T1,...,T m).
Moreover, we have
‖h♯c −c′‖1 ≤ ‖M,∂M ‖ + (2 +Kt n−1)ǫ.
Letting ǫ tend to zero, we have established
‖M (T1,...,T m)‖ ≤ ‖M,∂M ‖.
An application of the proportionality theorem for ﬁnite volume hyper bolic manifolds
(Theorem A.1) gives the upper bound:
‖M (T1,...,T m)‖ ≤ Vol(V )
vn
.
□
