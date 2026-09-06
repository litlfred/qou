---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-063-152-the-solution-space
section_title: "The solution space"
section_number: 15.2
pages: 458-469
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
15.2. The solution space
In this section we study the combinatorial properties of ideal triangulations
of three-manifolds in general. We study the space of solutions to the consis-
tency equations, we prove that it is a complex manifold and exhibit a concrete
parametrisation via the holonomy of peripheral curves.
15.2.1. Edges and tetrahedra.Throughout this section, we letN be a
compact oriented three-manifoldN with∂N =T1⊔...⊔Tc consisting of tori,
and deﬁneM = int(N). LetT be any ideal triangulation forM.
Proposition 15.2.1. The ideal triangulationT has the same numbern of
tetrahedra and edges.
Proof. Thetotalspace |T| ofthetriangulation T hasv vertices,e edges,f
faces, andt tetrahedra. Sinceχ(∂N ) = 2χ(N) for every compact 3-manifold
N and∂N consists of tori, we getχ(N) = 0. Therefore
v =v +χ(N) =χ(|T| ) =v−e +f−t =v−e +t
sincef = 2t. Thene =t. □
Recall that in the consistency equations we get one complex variablezi for
eachtetrahedronandoneequationforeachedge; sincewehavethesamenum-
ber of edges and tetrahedra, one would guess that the solutions form typically
a discrete set of points, but this is surprisingly not the case: we now show that
some equations are redundant, leaving some space for a higher-dimensional
space of solutions. The origin of this redundancy lies in the combinatorial
properties of three-dimensional triangulations.
15.2.2. Incidence matrices. We denote respectively by∆1,..., ∆n and
e1,...,e n the tetrahedra and edges ofT. We ﬁx an orientation onM, which
induces an orientation on each tetrahedron, and we assign numbers 1, 2, and 3
to pairs of opposite edges on each∆i in a way that is orientation-preservingly
isomorphic to Figure 15.5.
Wenowdeﬁnea 2n×3nintegralmatrix Athatencodessomecombinatorial
adjacencies between tetrahedra. The matrix A should be seen as a 2× 3
rectangle ofn×n sub-matrices as in Figure 15.6-(left), where:
• each column ofA corresponds to a pair of opposite edges of one
tetrahedron, morepreciselythecolumns i,i +n, andi +2n correspond
the opposite edges of type 1,2,3 of∆i;
• the ﬁrstn rows ofA correspond to the tetrahedra∆1,..., ∆n;
• the lastn rows ofA correspond to the edgese1,...,e n.
15.2. THE SOLUTION SPACE 451
1
1
2
2
3
3
1 2
3
Figure15.5. Welabeltheedgesofevery oriented tetrahedronasshown:
thelabellingisdeterminedoncewechosearbitrarilyapairofoppositeedges
and label them with 1 (left). The vertices of everyoriented triangle in the
triangulated boundary inherit labels as in the ﬁgure (right).
I I I n
n
n n n
c
n n
A
B
1
1
2 2
3
3
Figure 15.6. The incidence matricesA andB count the incidences be-
tween edge pairs, tetrahedra, edges, and ideal vertices.
Wheni⩽n, the entryAij is 1 or 0 depending on whether∆i contains thej-th
edge pair. In other words, the top threen×n sub-matrices ofA are three
identity matrices, see Figure 15.6-(left).
Wheni =n +i′ withi′> 0, the entryAij counts how many edges in the
j-th edge pair are glued to thei′-th edgeei′: this number is hence 0, 1, or 2.
Exercise 15.2.2. The entries on each column ofA sum to 3.
Let nowv1,...,v c be the ideal vertices ofT. We deﬁne anotherc× 2n
integral matrixB, which consists of twoc×n sub-matrices as in Figure 15.6-
(right), where:
• the rows ofB correspond to the ideal verticesv1,...,v c;
• the ﬁrstn columns ofB correspond to then tetrahedra ∆1,..., ∆n;
• the lastn columns correspond to the edgese1,...,e n.
Whenj⩽n, the entryBij is minus the number of times∆j is incident to
vi, and whenj =n +j′ withj′> 0 the entryBij is plus the number of times
ej′ is incident tovi. The possible entries are 0,−1,−2,−3,−4 and 0, 1, 2
respectively.
Exercise 15.2.3. The entries on each column ofB sum to−4 or 2.
452 15. HYPERBOLIC DEHN FILLING
The matricesA andB are designed to be interpreted as linear maps, and
to be composed.
Proposition 15.2.4. The following sequence is exact:
R3n A−→ R2n B−→ Rc−→0.
The proof of this proposition splits into three lemmas.
Lemma 15.2.5. We haveBA = 0.
Proof. Thei-th row ofB corresponds to the ideal vertexvi and thek-
th column ofA corresponds to thek-th pair of opposite edges. The sum∑2n
j=1BijAjk countsminus thenumberoftimes vi isincidenttothetetrahedron
containing the edge pair,plus the number of times it is incident to the two
edges of the pair. These numbers are equal and hence we get 0. □
Lemma 15.2.6. Thec rows inB are independent vectors.
Proof. Suppose there is a vanishing linear combination∑c
i=1λiBi = 0 of
the rowsBi ofB. If the edgeej has endpoints atva andvb, the entries in the
(n +j)-th columnBn+j are 1 at the rowsa and b and zero everywhere else:
therefore we getλa +λb = 0. If we apply this argument to the three edges
of a triangle we get
λa +λb = 0, λ b +λc = 0, λ c +λa = 0
which impliesλa =λb =λc = 0. Then all coeﬃcientsλa vanish. □
Lemma 15.2.7. Thec rows inB generate ker(A⊺).
Proof. SinceBA = 0 implies A⊺B⊺ = 0, we already know that the rows
in B are contained inker(A⊺), and we must prove that they generate it. We
pick a generic horizontal vectorq = (q1,...,q 2n)∈ R2n withqA = 0 and we
need to prove thatq is generated by the rowsBi ofB.
Recall that the columnsAj,Aj+n,Aj+2n ofA correspond to the edge pairs
of type 1, 2, and 3 of the tetrahedron∆j. We label the vertices of ∆j as
a,b,c,d , the edges of ∆j as pairs like ab, and the corresponding vertices
and edges inT as j(a) and j′(ab), interpreted as numbers in{1,...,c } and
{1,...,n } respectively. Moreover we setj(ab) =j′(ab) +n. We suppose that
ab,ac,ad are of type 1, 2, 3.
The conditionsqAj =qAj+n =qAj+2n = 0 say that
qAj =qj +qj(ab) +qj(cd ) = 0,
qAj+n =qj +qj(ac) +qj(bd ) = 0,
qAj+2n =qj +qj(ad) +qj(bc) = 0.
This implies that
(28) qj(ab) +qj(cd ) =qj(ac) +qj(bd ) =qj(ad) +qj(bc) =−qj.
15.2. THE SOLUTION SPACE 453
Wenowprovethat q =∑λiBi wherethecoeﬃcients λi aredeﬁnedasfollows.
Consider an ideal triangle in∆j with verticesa,b,c and deﬁne
λj(a) = qj(ab) +qj(ca)−qj(bc)
2 .
We check thatλj(a) does not depend on the ideal triangle: the triangle in∆j
with verticesa,b,d gives
λj(a) = qj(ab) +qj(da)−qj(bd )
2 = qj(ab) +qj(ca)−qj(bc)
2
using (28). Two triangles incident to the ideal vertexvj(a) are connected by a
path of adjacent tetrahedra and henceλj(a) is well-deﬁned.
Finally, we need to check that indeedq =∑λiBi. We consider the edge
j(ab) and recall that the(n +j(ab))-th column ofB is everywhere zero except
at rowsj(a) andj(b); hence the(n +j(ab))-th entry of∑λiBi isλj(a) +λj(b),
which by deﬁnition equalsqj(ab), so we are done.
Analogously, thej-th column ofB is everywhere zero except at the rows
j(a),j (b),j (c),j (d) and hence thej-th entry of∑λiBi is−(λj(a) +λj(b) +
λj(c) +λj(d)) which equals−qj(ab)−qj(cd ) =qj. The proof is complete. □
These three lemmas imply Proposition 15.2.4. In particular we get the
following:
Corollary 15.2.8.We have rkA = 2n−c.
15.2.3. A symplectic form.We deﬁne an alternating bilinear formω on
R3n as follows: for everyi = 1,...,n consider the form
ωi =


0 1 −1
−1 0 1
1 −1 0


on the subspaceVi generated byei,ei+n, and ei+2n, and deﬁneω =⊕iωi.
Strictly speaking, the formω is not symplectic because it is degenerate: its
radical is generated by all vectors of typeei +ei+n +ei+2n, that is by the ﬁrst
n rows of the matrixA. The formω becomes symplectic after quotientingR3
by the radical.
Proposition 15.2.9. The rows ofA generate a lagrangian subspace.
Proof. In other words, we need to prove thatω(Aj,Ak) = 0 for any rows
Aj,Ak ofA. The ﬁrstn rows lie in the radical, hence we are left to check that
ω(An+j,An+k) = 0 for all 0<j <k ⩽n corresponding to thej-th andk-th
edge of the triangulation.
Each tetrahedron∆i contributes to the numberω(An+j,An+k) as follows:
if two edges contained in some facef of ∆i correspond to the edgesj andk
of the triangulation, they contribute with a±1; the facef is also contained in
an adjacent tetrahedron where they contribute with opposite sign, and hence
everything sums to zero. □
454 15. HYPERBOLIC DEHN FILLING
15.2.4. The solution space.We now employ the combinatorial results of
the previous sections to study the consistency equations forT. We assign the
variableszj, 1
1−zj
, andzj−1
zj
to the edges of type 1, 2, and 3 in each tetrahedron
∆j. These three variables lie in the upper half-plane
C+ =
{
ℑz >0
}
which we see as the subsetC+⊂ ~C∗ consisting of allρeiθ with 0 < θ < π.
The consistency equation at the edgeei is the following equation in~C∗:
(29) gi (z) =
n∏
j=1
zAn+i,j
j
( 1
1−zj
)An+i,n +j(zj− 1
zj
)An+i,2n+j
=e2πi.
The elements 1
1−zj
, zj−1
zj
∈ C+⊂~C∗ depend holomorphically onzj∈ C+. We
have deﬁned a complex function
g : Cn
+−→
(~C∗)n
by settingg = (g1,...,g n). Thesolution spaceis the set
Def(M,T ) =g−1(e2πi,...,e 2πi ).
This space consists precisely of the solutions to the consistency equations
ofT. Each solution z∈ Def(M,T ) gives a hyperbolic metric onM, which
“deforms” asz varies: this justiﬁes the use of the symbol “Def”. We want to
prove that Def(M,T ) is a complex manifold of dimensionc.
15.2.5. Complex diﬀerentials.We use the biholomorphismlog :~C∗→ C
and deﬁne the functionG(z) = logg(z) for allz∈ Cn
+. Now
Def(M,T ) =G−1(2πi,..., 2πi ).
We may write
Gi (z) =
n∑
j=1
A′
i,j logzj +A′
i,n +j log(1−zj ) +Niπi
whereA′ is then× 2n integral matrix deﬁned by
A′
i,j =An+i,j−An+i,2n+j, A ′
i,n +j =−An+i,n +j +An+i,2n+j
andNi is some ﬁxed integer that depends on the way we interpretlog(1−zj ).
The complex diﬀerential ofG atz splits as a composition of two linear maps
dGz : Cn Z−→ C2n A′
−→ Cn
15.2. THE SOLUTION SPACE 455
where
Z =


1
z1
0 ... 0
0 1
z2
... 0
... ... ... ...
0 0 ... 1
zn
1
z1−1 0 ... 0
0 1
z2−1 ... 0
... ... ... ...
0 0 ... 1
zn−1


is obtained by diﬀerentiatinglogzj and log(1−zj ). Let now
B′ : Cn−→ Cc
be the linear map deﬁned by the right(c×n)-sub-matrixB′ ofB, that is
B′
i,j =Bi.n +j.
Proposition 15.2.10. The following sequence is exact:
C2n A′
−→ Cn B′
−→ Cc−→0.
Proof. Lemma 15.2.7 shows thatB is surjective, and its proof actually
shows thatB′ is surjective. Recall thatAdecomposes into six square matrices,
and via Gauss moves on columns we get
(30) A =
( I I I
A1 A2 A3
)
−→
( 0 0 I
A1−A3 −A2 +A3 A3
)
=
( 0 I
A′ A3
)
.
NowBA = 0⇒B′A′ = 0, and rkA = 2n−c⇒ rkA′ =n−c. □
This shows in particular that the image ofG lies in a ﬁxed aﬃne subspace
parallel to kerB′ of complex codimensionc. We now consider the standard
symplectic formω =
( 0 I
−I 0
)
on R2n.
Proposition 15.2.11. The rows ofA′ generate a lagrangian subspace.
Proof. We know that the rows ofA generate a lagrangian subspace with
respect to the degenerate form onR3n by Proposition 15.2.9. The Gauss
moves (30) imply the assertion. □
Proposition 15.2.12. For everyz∈ Cn
+ the following sequence is exact:
Cn dGz
−→ Cn B′
−→ Cc−→0.
Proof. We havedGz =A′Z. Proposition 15.2.10 gives an exact sequence
C2n A′
−→ Cn B′
−→ Cc−→0.
456 15. HYPERBOLIC DEHN FILLING
We only need to prove thatIm (A′Z) = Im A′, that isrk(A′Z) = n−c. We
prefer to consider the transpose matrixM = (A′Z)⊺ =Z⊺(A′)⊺. We have
Z⊺ =


1
z1
0 ... 0 1
z1−1 0 ... 0
0 1
z2
... 0 0 1
z2−1 ... 0
... ... ... ... ... ... ... ...
0 0 ... 1
zn 0 0 ... 1
zn−1

.
The mapZ⊺ : C2n→ Cn is obviously not injective, but its restriction
Z⊺|R2n : R2n−→ Cn
is an isomorphism of real spaces because1
zi
and 1
zi−1 are independent overR
(we use here thatzi⁄∈ R).
We deﬁne a symplectic formΩ on the real vector spaceCn by pushing-
forwardω alongZ⊺|R2n, that is we setΩ(Z⊺v,Z ⊺w ) =ω(v,w ). By construc-
tion Ω is a sum of symplectic forms on the coordinate complex lines ofCn.
Note that a symplectic form onC is unique up to rescaling.
Since Imzi > 0, the complex numbers 1
zi
and 1
zi−1 form a negatively-
oriented R-basis of C, and this implies thatΩ(v,iv ) < 0 for every non-zero
vector v ∈ Cn. In particular ⟨·,·⟩ = −Ω(·,i·) is a positive-deﬁnite scalar
product that induces a norm‖·‖ on Cn.
On each coordinate complex line ofCn, the formΩ is just a rescaling of
the standard symplectic form and hence⟨,⟩is a rescaling of the standard scalar
product. In particular we getΩ(iv,iw ) = Ω(v,w ) and⟨iv,iw ⟩ =⟨v,w⟩.
Finally, we suppose by contradiction thatrkM < n−c. Since Z⊺|R2n is
injective, therealsubspace M(Rn)hasrealdimension n−c. Since rkM <n−c,
there are vectorsv1,v 2∈ Rn such thatM(v1 +iv 2) = 0 while Mv1⁄= 0 and
Mv2⁄= 0. Proposition 15.2.11 gives
Ω(Mv1,Mv 2) =ω((A′)⊺v1, (A′)⊺v2) = 0
and therefore
0 =‖M(v1 +iv 2)‖2 =‖Mv1‖2 +‖iMv 2‖2 + 2⟨Mv1,iMv 2⟩
=‖Mv1‖2 +‖Mv2‖2− 2Ω(Mv1,−Mv2)
=‖Mv1‖2 +‖Mv2‖2
impliesMv1 =Mv2 = 0, a contradiction. □
Corollary 15.2.13.The solution spaceDef(M,T )⊂ Cn
+ is either empty or
a complex submanifold of dimensionc.
Proof. The image ofG : Cn
+→ Cn lies entirely in a(n−c)-dimensional
complex aﬃne spaceS parallel tokerB′⊂ Cn and by the previous proposition
the holomorphic mapG : Cn
+→S is a submersion onto its image. Therefore
the counterimage of any point is a either empty or is a complex submanifold
of dimensionn− (n−c) =c. □
15.2. THE SOLUTION SPACE 457
Figure 15.7. We mark with a dot all the interior angles thatγ encoun-
ters on its right as in the picture: each dot determines an edge in some
tetrahedron ∆j and hence an edge pair (left). We also consider the “de-
generate path” consisting of a single point “run counterclockwise”, and
recover the lastn rows ofA in this way (right).
Wenowwanttodeﬁneaniceholomorphicparametrisationforthemanifold
Def(M,T ), and to this purpose we need to investigate further the combina-
torial properties ofT by looking more closely at its ideal vertices.
15.2.6. Boundary curves. Recall thatM = int(N) and the ideal vertices
v1,...,v c ofT correspond to the boundary toriT1,...,T c of N, which are
triangulated byT. Recall also that there aren tetrahedra ∆1,..., ∆n inT and
each ∆i has three edge pairs labeled withi,n +i, and 2n +i.
Every simplicial closed oriented curveγ in a triangulated torusTi deter-
mines an integer vectorvγ∈ R3n that counts the (right-)incidences between
γ and the3n edge pairs ofT. More precisely, each interior angle of a triangle
inTi determines an edge in some tetrahedron∆j and hence an edge pair: we
deﬁne(vγ)j to be the number of timesγ encounters thej-th edge pair on its
right, as in Figure 15.7-(left).
We deﬁned an alternating degenerate formω on R3n and we now want to
extend Proposition 15.2.9. We denote byγ·γ′ the algebraic intersection ofγ
andγ′ inH1(∂M, Z).
Proposition 15.2.14.Letγ,γ′ be simplicial closed curves in∂N. We have:
• ω(vγ,vγ′) = 2γ·γ′,
• ω(vγ,Ai ) = 0 for every rowAi ofA.
Proof. The rowAi with i⩽ n lies in the radical ofω, andAn+i records
the incidences of thei-th edgeei ofT with the 3n edge pairs. We may write
An+i =vγ′ whereγ′ is a “degenerate” closed path consisting of a single point
(one of the endpoints ofei), see Fig 15.7-(right). Now the second assertion
is just a special case of the ﬁrst.
We draw the two pathsγ andγ′ in blue and red as in Figure 15.8, marking
with dots the angles they encounter on their right. A couple of blue and red
458 15. HYPERBOLIC DEHN FILLING
Figure 15.8. We draw the pathsγ,γ′ and their dots in blue and red.
+1 0 -1
Figure 15.9. Two dots in a triangle contribute toω(γ,γ′) with +1, 0,
or−1 according to their mutual position.
+1 0
1-1=0
+1
01-1+1=1 1-1=0
-1
Figure 15.10. Two portions of blue and red paths that intersect the
same triangle contribute to ω(γ,γ′) as shown here. The contribution
depends on their mutual conﬁguration, and changes by a sign if we inter-
change the blue/red colours. If one of the two portions contains at least
two edges (as in bottom-right) it determines a vector in the radical, and
the contribution is always zero.
15.2. THE SOLUTION SPACE 459
=
-1
=
+1
=
-1
=
+1
e e
Figure 15.11. Whenγ andγ′ encounter in diﬀerent truncated triangles
of the same tetrahedron∆i, they also contribute toω(γ,γ′).
dots in the same triangle contribute toω(γ,γ′) according to their mutual
position as shown in Figure 15.9. Therefore portions of blue and red paths
intersecting the same triangle contribute toω(γ,γ′) as shown in Figure 15.10.
For every contribution+1 as in Figure 15.10-(top-left), there is an analo-
gous but opposite contribution−1 provided by the other triangle adjacent to
the edge joining the coloured endpoints: these all cancel. We are left with a
+1 every time the red path exits leftward from an intersection with the blue
path, a−1 every time it enters from the left, and the opposite contributions
with the blue/red colours interchanged. We easily get a total of2γ·γ′.
The proof is not yet complete, because every tetrahedron∆i determines
four triangles in∂N and some contributions toω(γ,γ′) arise also from paths
intersecting distinct triangles of the same∆i: we need to prove that these
contributions all cancel.
Up to symmetries of the tetrahedron and up to interchanging the colours,
the possible non-zero contributions are all shown in Figure 15.11. Each con-
ﬁguration as in the ﬁrst row cancels with an opposite one produced by the
tetrahedron adjacent to the grey face. The contributions in the second row
arise whenγ and γ′ cross the endpoints of an edgee on opposite sides, and
460 15. HYPERBOLIC DEHN FILLING
I I I n
n
n n n
c
Figure 15.12. The enlarged matrix ¯A.
one checks that the contributions of all the cycle of tetrahedra incident toe
sum to zero (exercise). □
15.2.7. Holonomy parameters. We now ﬁx a non-trivial oriented simple
closed curveγi on eachTi and a representation ofγi as a simplicial (possibly
non-injective) path in the triangulatedTi.
We enlarge the incident2n× 3n matrixA to a (2n +c)× 3n matrix ¯A by
adding the vectorsvγ1,...,v γc at its bottom, see Figure 15.12.
Proposition 15.2.15.We haverk ¯A = 2n. The rows of¯A generate a maxi-
mal lagrangian subspace inR3n.
Proof. Letµi⊂Ti be a simplicial closed curve withγi·µi = 1. We already
know that the ﬁrst2n rows of ¯A generate a lagrangian subspace of dimension
2n−c, and to conclude it suﬃces to use Proposition 15.2.14 and deduce
that vµi is ω-orthogonal to all the rows of¯A except ¯A2n+i = vγi. Therefore
rk ¯A = rkA +c = 2n. □
Every pointz∈ Def(M,T ) determines a hyperbolic structure onM and a
homomorphism
˜µz :π1(Ti )→~C∗
for eachi = 1,...,c , see Deﬁnition 14.2.1. We deﬁne
hi (z) = ˜µz (γi ) =e−|γi|πi
n∏
j=1
z
¯A2n+i,j
j
( 1
1−zj
) ¯A2n+i,n +j(zj− 1
zj
) ¯A2n+i,2n+j
and get a holomorphic function
h : Cn
+−→
(~C∗)c.
