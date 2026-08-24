---
doc_id: arxiv-q-alg-9504020v1
doc_title: "A link invariant from quantum dilogarithm"
section_id: sec-004-4-three-dimensional-description
section_title: "Three-Dimensional Description"
section_number: 4
pages: 5-9
source_pdf: 9504020v1.pdf
source_sha256: 0baef40fa9934c91
doc_brief: "A link invariant from quantum dilogarithm — The link invariant, arising from the cyclic quantum dilogarithm via the particular R-matrix construction, is proved to coincide with the invariant of"
---
In this section we establish the connection of the link invar iant constructed in
Sect. 3 with the invariant of triangulated links of [14], rel ated in turn to cyclic
quantum dilogarithm [11]. First, remind the necessary form ulas from [14] in
slightly diﬀerent notations.
We will assume that the integer N is odd, and the square root of ω will be
thought to be taken as an N -th root of unity:
ω 1/ 2 =ω (N +1)/ 2. (4.1)
For complex x,y,z , satisfying the Fermat equation
xN +yN =zN, (4.2)
and integers m,n deﬁne the function
w(x,y,z |m,n ) = w(x,y,z |m −n)ω n2/ 2, (4.3)
4
where
w(x,y,z |n) =
n∏
j=1
y
z −xω j. (4.4)
The Fermat equation (4.2) ensures the periodicity relation :
w(x,y,z |n +N ) = w(x,y,z |n). (4.5)
This latter property enables us to consider the ﬁnite set ZN instead of Z.
For any non-coinciding complex numbers z0,z 1,z 2,z 3, and α,β,γ,δ,a,c ∈
ZN deﬁne two functions:
T 0123(a,c )γ,δ
α,β =ρ0123ω c(γ −α )+αδ +ac/ 2w(x03x12,x 01x23,x 02x13|γ −a,α )δβ,γ +δ,
(4.6)
and
T 0123(a,c )α,β
γ,δ =
ρ0123ω c(γ −α )−αδ −ac/ 2δβ,γ +δ
w(x03x12/ω,x 01x23,x 02x13|γ +a,α ), (4.7)
where
xij = (zi −zj)1/N , i,j = 0, 1, 2, 3, (4.8)
withN -th root being chosen to be real for real diﬀerence zi −zj; scalar functions
ρ0123 andρ0123 depend on only z’s and their explicit form can be found in [14].
These symbols can be associated with tetrahedrons in R3 as is described below.
In what follows for a polyhedron X, considered as a collection of vertices,
edges, triangles, and tetrahedrons, we will denote by Λ i(X),i = 0, 1, 2, 3 the sets
of simplices of corresponding dimension. Consider a topolo gical 1 tetrahedron
t in R3. Order the vertices by ﬁxing a bijective map
u: {0, 1, 2, 3} ∋ i ↦→ui ∈ Λ 0(t). (4.9)
Put an arrow on each edge, pointing from a “larger” vertex (wi th respect to
above ordering) to a “smaller” one. Each face also gets its’ o wn orientation.
Let ul be the top of the tetrahedron. Let us look from it down at the ve rtices
ui,u j,u k, where
{i,j,k } = {0, 1, 2, 3} \ {l}, i<j <k. (4.10)
We will see two possible views: either ui,u j,u k, in the order which they are
written, go round in the counter-clockwise direction (the “ right” orientation)
or, in the clockwise one (the “left” orientation). The tetra hedron itself has
two possible orientations in the following sense. Call the t etrahedron “right
(left)”-oriented if the face u0u1u2 has the right (left) orientation in the above
sense.
Introduce three maps:
s: Λ 0(t) →C, c : Λ 1(t) →ZN, α : Λ 2(t) →ZN, (4.11)
1 the term “topological” here means that edges and faces of the tetrahedron can be curved
5
where s is injective, and c satisﬁes the following relations:
∑
e∋v
c(e) = 1/ 2, v ∈ Λ 0(t). (4.12)
Let cij = c(uiuj) (uiuj is the edge having ends ui and uj), α i = α (ujukul),
{j,k,l } = {0, 1, 2, 3} \ {i}, and zi = s(ui). Deﬁne the symbol associated with
the tetrahedron t:
tu(s,c,α ) =
{
T 0123(c01,c 12)α 2,α 0
α 3,α 1, right orientation;
T 0123(c01,c 12)α 3,α 1
α 2,α 0, left orientation. (4.13)
The variables associated with the second map in (4.11) will b e called ZN -
charges. Using symbols (4.13), one can associate a “partiti on” function to any
ﬁnitely triangulated three-manifold with a triangulated t angle passing through
the all interior 0-simplices. The construction goes as foll ows.
Let M be a ﬁnite triangulation of an oriented 3-dimensional manif old with
boundary. Fix a subset of 1-simplices T ⊂ Λ 1(M \∂M ) in such a way that any
interior 0-simplex belongs to exactly two elements from T , so the latter is some
triangulated tangle in M , passing through the all interior vertices. Denote
I = {0, 1,...,K − 1}, where K is the number of vertices in M , and ﬁx the
following maps:
u:I → Λ 0(M ), s : Λ 0(M ) →C, c T : Λ 3(M )×Λ 1(M ) →ZN, α : Λ 2(M ) →ZN,
(4.14)
where u is bijective, s, injective, and cT satisﬁes the restrictions:
e ⁄∈Λ 1(t) ⇒cT (t,e ) = 0;
∑
e∋v
cT (t,e ) = 1/ 2, v ∈t ∈ Λ 3(M ); (4.15)
∑
t∈Λ 3(M )
cT (t,e ) =
{ 0, e ∈T ;
1, e ∈ Λ 1(M \∂M ) \T . (4.16)
Denote the total ZN -charges on Λ 1(∂M ) by
∂c tot: Λ 1(∂M ) ∋e ↦→
∑
t∈Λ 3(M )
cT (t,e ) ∈ZN, (4.17)
and also the restrictions of the remained maps in (4.14) by
∂u: Λ 0(∂M ) →I, ∂s : Λ 0(∂M ) →C, ∂α : Λ 2(∂M ) →ZN. (4.18)
Then, the partition function reads:
M∂u (T,∂s,∂c tot,∂α ) = N −K0
∑
α,∂α =ﬁxed
∏
t∈Λ 3(M )
tu(s,c T,α )
∏
e∈Λ 1(M \∂M )\T
⟨s(∂e)⟩−1,
(4.19)
where
⟨s(∂e)⟩ = (s(uj) −s(ui))(N −1)/N , e =uiuj; (4.20)
andK0 being the number of interior 0-simplices. As is reﬂected in t he left hand
side of (4.19), the partition function depends (up to N -th roots of unity) only
6
on the boundary data as well as on the topological class of the triangulated
tangle (see [14] for the deﬁnition). This is the consequence of the relations the
symbols (4.13) satisfy, which are described in [14]. When ∂M = ∅ partition
function (4.19) multiplied by N 2 reduces to the invariant of triangulated links
[14].
To make contact with the results of Sect. 3, we have just to spe cify the
triangulated 3-manifold with tangle, corresponding to R-symbol (2.8). The
most economic way is to consider singular triangulated mani folds [17].
Letu1,u 2,u 3,u 4 be four points in R3, specifying the right-oriented tetrahe-
dron u1u2u3u4. Glue to four faces of the latter four other tetrahedrons
u1u2u4u5, u 2u3u4u5′, u 0u1u2u3, u 0′u1u3u4.
We have added four new vertices u0,u 0′,u 5,u 5′. Among the latter identify the
“primed” vertices with the corresponding “non-primed” one s:
u0 =u0′, u 5 =u5′. (4.21)
While doing this, we glue also the added tetrahedrons pairwi se along the cor-
responding faces. As a result we get a triangulated octahedr on u0u1u2u3u4u5.
The next step consists in attaching four more tetrahedrons,
u0u1u2u5, u 0u2u3u5, u 0u3u4u5, u 0u1u4u5,
to the octahedron, each one being glued along two faces. For e xample, tetra-
hedron u0u1u2u5 is attached along faces u0u1u2 and u1u2u5, and similarly the
others. Thus we obtain singular triangulated three-ball B, where among others
four diﬀerent 1-simplices have coinciding ends u0 and u5. We will distinguish
them by specifying the tetrahedron to which they belong. For example,
[u0u5]12 ∈ Λ 1(u0u1u2u5), (4.22)
and similarly for the others. Besides, Λ 2(∂B ) consists of four pairs of 2-
simplices, each being given by one and the same triple of vert ices:
Λ 2(∂B ) = {[u0uiu5]±, i = 1, 2, 3, 4}, (4.23)
where we distinguish elements within each pair by their orie ntation (+ ( −) cor-
responds to the right (left) orientation). To write down the partition function,
we have to specify the tangle. Let us choose it as follows:
T = {u1u3,u 2u4}. (4.24)
Now, providing B with additional data (4.14), one can calculate the partitio n
function (4.19). The result reads:
B∂u (T,∂s,∂c tot,∂α )
= (s05)N −1
N −1∑
i1,i 2,i 3,i 4=0
R(i1,i 2,i 3,i 4|c12,c 23,c 34,c 14)
4∏
m=1
ψ α −
m−α +
m+cm
m,i m ,(4.25)
7
where
α ±
m =α ([u0umu5]±), s ij = (s(ui) −s(uj))1/N (4.26)
cm =∂c tot(umu5), c ij =∂c tot([u0u5]ij), (4.27)
and
ψ k
m,j =ω jks[k−1]
0m s[−k]
m5 , (4.28)
see also (2.4). The role of ψ -functions is to intertwine the indices of diﬀerent
nature. Note that the ZN -charges are related with the angle-dependent data
for the enhanced R-matrix.
Formula (4.25) enables us to prove the second part of Theorem 1. Indeed,
let we are given a link, represented by a two-strand tangle. T hen, using cor-
respondence (4.25), we associate to the latter partition fu nction of a singular
triangulated three-ball with four boundary 0-simplices, t he tangle by its strands
being attached to two of them. To get the invariant in S3, we have to glue the
ball with another (empty) one, making the tangle to pass thro ugh the other two
vertices and converting it into the link under consideratio n. This last process
is equivalent to choosing boundary conditions (3.2).
One can prove also the YBE (2.13) via consideration the trian gulated three-
balls, corresponding to two sides of YBE, and transforming t hem to each other
by a sequence of elementary moves deﬁned in [14].
A remark is in order. In [15] it has been shown that the univers al R-
matrix in Drinfeld double can be represented as a product of s olutions to the
constant pentagon relation, the canonical element in Heise nberg double being
such solution. This construction can be extended also to the case of non-
constant solutions to the pentagon relation. In particular , using cyclic quantum
dilogarithm of [11] and specializing the parameters, one ca n derive R-matrix
(2.12). The derivation given in this section is essentially equivalent to the latter.
On the other hand, the cyclic quantum dilogarithm can be obta ined from the
quantum dilogarithm with q non-root of unity 2 in the limit, where q approaches
a root of unity [6]. Thus, it is natural to consider R-matrix (2.12) as a cyclic
counterpart of the universal R-matrix in Uq(sl(2)).
