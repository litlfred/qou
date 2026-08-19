---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-012-46-choice-of-edges-in-the-summation-for-index
section_title: "Choice of edges in the summation for index"
section_number: 4.6
pages: 20-26
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
with r≥ 1 torus cusps and let T be an ideal triangulation ofM with N tetrahedra and,
hence, N edges which we denotee1,...,e N. LetG be the 1-skeletonT(1) of T together with
one (ideal) vertex for each cusp ofM. Note that G has r vertices andN edges, and may
contain loops (i.e. edges with both ends at a single vertex) or multiple edges between the
same two vertices. The incidence matrixC = (chi) forG is anr×N matrix whose(h,i ) entry
gives the number of ends of edgei on cusph. Note that eachchi∈{ 0, 1, 2} and the sum of
entries is 2 in each column ofC. Let E(ei) = Ei⊂ Z2N be the edge equation coeﬃcients
corresponding to edgeei in T, and let
(19) Λ =
{∑
k∈ZN
kiEi
}
⊂ Z2N
be the lattice of all integer linear combinations of these. In other words,Ei is theith row of
the Neumann-Zagier matrix(A| B), and Λ is the integer row space of this matrix.
From the work of Neumann and Zagier (see [NZ85] and [Neu92, Thm 4.1]), the lattice
Λ has rankN−r and the matrixC gives the linear relations between the edge equation
coeﬃcientsEi∈ Z2N. More precisely,
(20)
∑
i
chiEi = 0 for allh = 1,...,r
and any other linear relation between theEi arises from a real linear combination of the
rows ofC.
Deﬁnition 4.2.A subset of the edges of a graphΓ is amaximal tree with 1- or 3-cyclein Γ
if (together with the vertices) it consists of any maximal treeT together with one additional
edge that either (1) is a loop at one vertex, or (2) forms a 3-cycle together with two edges
in T.
Theorem 4.3.There exists an integer basis forΛ consisting ofN−r of the edge equation
coeﬃcientsE1,...,E n. In fact, we can choose such a basis by omittingr edge equations
corresponding to a maximal tree with 1- or 3-cycle inG.
Remark 4.4. In other words, we can choose any maximal tree with 1- or 3- cycle for our set
X of excluded edges, and hence choose the remaining edges as our setB of basic edges.
This result and its proof were inspired by Jeﬀ Weeks’ argument in [Wee85, pp. 35–36].
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 21
Proof. First we show that we can ﬁnd a maximal tree with 1- or 3-cycle. If there exists a loop
in G we use this loop together with any maximal tree. If not, any face of the triangulation
has its ideal vertices on 3 distinct cusps. Pick two edges of this face and extend these to a
maximal treeT⊂G. Adding the third edge of the face gives the desired subgraph.
Now letS be a maximal tree with 1- or 3-cycle. Next we show that theN−r equations
E(e) corresponding to the edgese /∈ S give an integer basis forΛ. We show that for each
s∈ S, the equationE(s) can be written as an integer linear combination of the equations
E(e) withe /∈S. Given this, theN−r equationsE(e) withe /∈S form an integer spanning
set for Λ. The work of Neumann and Zagier ([NZ85] and [Neu92, Thm 4.1]), implies that
these equations are also linearly independent, hence form an integer basis forΛ, and we are
done.
So, we have to show that everyE(s) can be written as an integer linear combination of
theE(e) fore /∈S. To organise the construction, we use the following sequence ofdecorated
graphs. At each step we have a graphGk whose edges are labelled by names of edges ofG.
We decorate each end of each edge ofGk with a sign. Each vertexv of Gk is then incident
to a set of ends of edges with signs. We list the names of the edges, together with the sign
associated to this end:{(eiv(1),ϵv(1)), (eiv(2),ϵv(2)),..., (eiv(d),ϵv(d))}. Here d is the degree
of the vertexv. To this vertex we associate the equation
Rk(v) =
d∑
l=1
ϵv(l)E(eiv(l)) = 0.
For eachGk we have a subsetSk of the edges ofGk which is a maximal tree with 1-or
3-cycle inGk. We setG0 =G and S0 =S, with all signs set to+. Note that the equations
associated to the vertices ofG0 are then the same as those given by (20).
We obtain the graph and edge subset(Gk+1,Sk+1) from (Gk,Sk) as follows. We arbitrarily
choose a vertexv of Gk that has only one end of one edges of Sk incident. If there are no
such vertices then the sequence ends at(Gk,Sk). Let w be the other end ofs, which by
assumption is distinct fromv. The graphGk+1 is the result of collapsing the edges of Gk;
the two ends ofs,v andw, are identiﬁed inGk+1. We label the edges ofGk+1 with the same
names as inGk and setSk+1 = Sk\{s}. All of the signs decoratingGk+1 are the same as
in Gk, except that the ends of edges that were incident tov have their signs ﬂipped. See
Figure 8.
Note that at each step of the sequence, both ends of each element ofSk have a + sign,
since they do inG0 and we never collapse an edge from a vertex with more than one incident
edge end inS. Consider the equations associated to the vertices ofGk and Gk+1. We have
Rk(v) = +E(s)+
∑
l,eiv(l)⁄=s
ϵv(l)E(eiv(l)) = 0, R k(w) = +E(s)+
∑
m,eiw(m)⁄=s
ϵw(m)E(eiw(m)) = 0.
If we useRk(v) to solve forE(s) we get
E(s) =
∑
l,eiv(l)⁄=s
−ϵv(l)E(eiv(l)).
Substituting this intoRk(w) gives
22 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
v
w
s
+
+
− +
−
+ +
+
+ +
+
+ +
+
+−+
−
Figure 8. Collapsing the edge s ﬂips the signs on the ends of the edges
incident tov. Edges inS are drawn dashed.
∑
l,eiv(l)⁄=s
−ϵv(l)E(eiv(l)) +
∑
m,eiw(m)⁄=s
ϵw(m)E(eiw(m)) = 0.
This is the equation associated to the vertex ofGk+1 formed by the identiﬁcation ofv with
w. Thus, the sequence of graphs gives an expression forE(s) for each edges∈ S which is
removed.
This expression is an integer linear combination of theE(e) fore /∈S. The sequence ends,
at GK say. By constructionGK has no vertices for which only one end of an edge ofS is
incident. If we are in case (1) of Deﬁnition 4.2 thenGK has one vertex,SK has one edge
and GK looks like Figure 9 (left). If we are in case (2) thenGK has three vertices,SK has
three edges, andGK looks like Figure 9 (right).
In the ﬁrst case, the equation from the last vertex is of the form
2E(s) +
∑
l,ei(l)⁄=s
ϵ(l)E(ei(l)) = 0.
Notice that since all edges are now loops, eachE(ei) appears with total coeﬃcient either
−2, 0 or 2. So we can divide the entire equation by2, and getE(s) as an integer linear
combination of theE(ei).
The second case is slightly more complicated. We have three verticesx,y,z , with three
edgessx,sy,sz∈S connecting the vertices into a triangle. The three vertices give equations
of the form
E(sy) +E(sz) +X = 0, E (sz) +E(sx) +Y = 0, E (sx) +E(sy) +Z = 0,
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 23
s +
+
+
+
−+
− −
(a) The last
graph when S
has a 1-cycle.
sz sx
sy
y
x z
X
Z
Y
+
+
+
+
+ +
−
+
+
−
−
−
+
−
−+
−
−+
−
(b) The last graph whenS has a
3-cycle.
Figure 9. The last graph in the sequence has one of these two forms.
where X,Y,Z are terms coming from the edges not inS. We can solve these equations for
E(sz) as
2E(sz) =−X−Y +Z,
and the other two expressions similarly. We just have to show that−X−Y +Z has even
coeﬃcients, and then we will be done. As before, any loops contribute a coeﬃcient in
{−2, 0, 2} to one ofX,Y orZ. For edges with the same endpoints as one ofsx,sy orsz, their
coeﬃcients are1 or−1 at two ofX,Y andZ and 0 at the third. Thus their contribution to
−X−Y +Z is also in{−2, 0, 2}, and so−X−Y +Z has even coeﬃcients, as required.□
Example 4.5.The following example shows that the edges omitted must be chosen carefully
in the multi-cusped case. LetM be the Whitehead link complement (with the triangulation
given by m129 in SnapPy notation). Then the matrix of edge equations is
(A| B) =


2 −1 1 1 1 −2 0 0
−1 0 0 0 −1 1 1 1
0 1 −1 −1 1 0 −2 −2
−1 0 0 0 −1 1 1 1


The cusp incidence matrix is
C =
(
1 2 1 0
1 0 1 2
)
and the corresponding graphG is shown in Figure 10.
e1 e3
e0
e2
c0 c1
Figure 10. The graph of edges and cusps for the Whitehead link.
24 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
The rowsE0,E 1,E 2,E 3 of (A| B) satisfy the relations:
E0 + 2E1 +E2 = 0 (from cusp 0)
and
E0 +E2 + 2E3 = 0 (from cusp 1),
which imply thatE1 =E3.
It follows thatE0,E 1 are linearly independent and form an integer basis for theZ-span of
{E0,E 1,E 2,E 3}. (This basis corresponds to removing the edgee2 in a maximal tree and an
additional loope3.)
On the other hand, E0, E2 are also linearly independent and 2E1 is in the Z-span of
{E0,E 2} but E1 is not inZ-span of{E0,E 2}. So Z-span{E0,E 2} is an index 2 subgroup in
Z-span{E0,E 1}. Thus, a summation usingE0,E 2 will most likely give a diﬀerent result for
the index than usingE0,E 1.
4.7. A reformulation of the deﬁnition of the index.It is sometimes convenient to work
with a slight variation on the tetrahedral index function (5). Whenevera−b,b−c∈ Z we
deﬁne
(21) J∆(a,b,c ) = (−q
1
2 )−bI∆(b−c,a−b) = (−q
1
2 )−cI∆(c−a,b−c) = (−q
1
2 )−aI∆(a−b,c−a).
Note that the above expressions are equal by the triality identity (9) forI∆, and by using the
duality identity (8), it follows thatJ∆ is invariant underall permutationsof its arguments.
Further, we have
(22) J∆(a +s,b +s,c +s) = (−q
1
2 )−sJ∆(a,b,c ) for alls∈ R.
We also note that the quadratic identity (11) can be rewritten in the form
(23)
∑
a∈Z
J∆(a,b,c )J∆(a +x,b,c )qa =δx,0.
This follows since
LHS =
∑
a∈Z
(−q1/2)−bI∆(b−c,a−b) (−q1/2)−bI∆(b−c,a−b +x)qa
=
∑
e∈Z
I∆(m,e )I∆(m,e +x)qe =δx,0
by (11) withm =b−c and e =a−b.
Now suppose thatM is a 3-manifold whose boundary∂M consists ofr≥ 1 tori. Let A, B
and C be the matrices of angle structure equation coeﬃcients as in Deﬁnition 2.13, and let
¯aj, ¯bj, ¯cj for j = 1,...N denote the columns ofA, B and C respectively. For eachk∈ ZN
and oriented multi-curveϖ in ∂M representing a homology class[ϖ]∈H1(∂M, Z), let
¯aj(k,ϖ ) =k· ¯aj + ¯aϖ,j, ¯bj(k,ϖ ) =k· ¯bj + ¯bϖ,j, ¯cj(k,ϖ ) =k· ¯cj + ¯cϖ,j,
and
aj(k,ϖ ) = ¯aj(k,ϖ )− ¯bj(k,ϖ ), bj(k,ϖ ) = ¯cj(k,ϖ )− ¯bj(k,ϖ ).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 25
Then the deﬁnition (17) of the index of the triangulationT of a manifoldM can be written
(24) IT(ϖ)(q) =
∑
k∈ZN−r⊂ZN
(−q
1
2 )k·ν+νϖ
N∏
j=1
I∆(−bj(k,ϖ ),aj(k,ϖ )),
where the sum is overk in any coordinate planeZN−r⊂ ZN corresponding to a set B of
N−r basic edges as given by Theorem 4.3.
Letk = (k1,...,k N),ν = (ν1,...,ν N) and let¯bij be the (i,j ) entry of B. Then we have
k·ν =
∑
i
kiνi =
∑
i
2ki−
∑
i,j
ki¯bij =
∑
i
2ki−
∑
j
k· ¯bj
and νϖ =−∑¯bϖ,j, so
k·ν +νϖ =
∑
i
2ki−
∑
j
¯bj(k,ϖ ).
Hence, grouping together the contributions from tetrahedronj, we have
IT(ϖ)(q) =
∑
k∈ZN−r
q
∑
iki
∏
j
(−q
1
2 )−¯bj(k,ϖ)I∆(¯bj(k,ϖ )− ¯cj(k,ϖ ), ¯aj(k,ϖ )− ¯bj(k,ϖ ))
=
∑
k∈ZN−r
q
∑
iki
∏
j
J∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ )),(25)
where ZN−r⊂ ZN corresponds to a setB of N−r basic edges as given by Theorem 4.3.
In particular, this expression shows that the index does not depend on the quad-choice
used in the original deﬁnition.
Remark 4.6. Next we show that the deﬁnition of index in (17) does not depend on the choice
of integer basis for the integer row spaceΛ⊂ R2N of the Neumann-Zagier matrix(A| B).
Eachx∈ Λ can be written in the form
(26) x =
∑
i
kiEi
whereEi is theith row of(A| B) andk = (k1,...,k N)∈ ZN. We claim that the expression
(27) J(x,ϖ ) =q
∑
iki
∏
j
J∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ ))
is well-deﬁned, depending only onx∈ Λ and not on the choice ofk in (26).
To see this, consider the linear mapψ : RN→ R2N deﬁned byψ(k1,...,k N) = ∑
ikiEi
and let⟨C⟩⊂ RN be the real subspace generated by the cusp relation vectors(ch1,...,c hN)
where the cusp indexh varies over{1,...,r }. Then ψ(⟨C⟩) = 0 by the cusp relations (20),
and the work of Neumann and Zagier ([NZ85, Neu92]) also shows thatdim Imψ = N−r and
dim⟨C⟩ =r where r is the number of cusps. Hence⟨C⟩ = kerψ.
So ifx =∑
ikiEi =∑
ik′
iEi wherek′ = (k′
1,...,k ′
N)∈ RN thenk′ =k+c wherec∈⟨C⟩.
We claim that replacingk byk′ does not change the expression (27). To see this, suppose we
replacek byk′ wherek′
i =ki +schi fori = 1,...,N ands∈ R. Then the termq
∑
iki in (27)
is multiplied byqsnh wherenh is the number of vertices in the triangulation of cusph, while
¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ ) are increased bys for each triangle of tetrahedronj lying in the
26 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
cusp h. By (22), this changes∏
jJ∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ )) by a factor (−q1/2)−2snh
since there are2nh triangles on cusph. Hence the right hand side of (27) does not change.
We conclude that the expression for index in (25) can be rewritten in the form
(28) IT(ϖ) =
∑
x∈Λ
J(x,ϖ )
and so does not depend on a choice of basis for Λ. Further, we can evaluate IT(ϖ) by
choosing an integer basis forΛ corresponding to a set of basic edges as given by Theorem
4.3, and we recover the deﬁnition of index in (17).
It also follows that we can write the index in the form
(29) IT(ϖ) =
∑
k∈S
q
∑
iki
∏
j
J∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ )),
where S⊂ ZN is any complete set of coset representatives for(ZN +⟨C⟩)/⟨C⟩⊂ RN/⟨C⟩.
