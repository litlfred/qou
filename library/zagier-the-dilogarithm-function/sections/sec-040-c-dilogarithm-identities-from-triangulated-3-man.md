---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-040-c-dilogarithm-identities-from-triangulated-3-man
section_title: "Dilogarithm identities from triangulated 3-manifolds. Finally, we"
section_number: C
pages: 37-39
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
describe a simple method for producing examples of torsion elements in Bloch
groups, using combinatorial triangulated 3-manifolds. (See also [18].) For this
purpose, it is convenient to think of L or D as functions of real or complex
oriented 3-simplices. By an orientedn-simplex in P
1(C)w em e a na n(n + 1)-
tuple of points in P1(C) together with an ordering up to even permutations;
more precisely, such a simplex has the form [x 0,...,x n] with xj ∈ P1(C)
and with the convention that [xπ(0),...,x π(n)]=s g n (π)[x0,...,x n]f o rπ ∈
Sn+1 .L e tCn denote the free abelian group on orientedn-simplices. There are
boundary maps∂ : Cn → Cn−1 deﬁned by the usual formula∂([x0,...,x n]) =∑n
i=0(−1)i[x0,..., ˆxi,...,x n], and the sequence (with ε([x]) = 1)
···−→ C4
∂
−→ C3
∂
−→ C2
∂
−→ C1
∂
−→ C0
ε
−→ Z −→ 0 (22)
is exact. The function D : C → R deﬁnes a function ~D : C3 → R which
associates to a 3-simplex in P1(C) the value of D on the cross-ratio of its
vertices,~D([a,b,c,d ]) =D
(a−d
a−c
b−c
b−d
)
, as in Chapter I. This is well-deﬁned (i.e.,
transforms under the action ofπ∈ S4 by sgn(π)) and is 0 on∂(C4) by the ﬁve-
term relation, since the elementV (x,y ) in (17) is simply the boundary of the
4-simplex [∞,0,x,1,y −1] and any 4-simplex is equivalent to such a one under
the action of PGL2(C)o n C3. (Notice that ~D is invariant under the action
of PGL2(C)o n C3, since the cross-ratio is.) Because of the exactness of (22),
we can say equivalently that ~D vanishes on Ker( C3
∂
→ C2)o rt h a ti tf a c t o r s
through ∂ : if we deﬁne a map
≈
D : C2 → R by
≈
D([a,b,c ]) =−~D([a,b,c, ∞])
(here “∞” could be replaced by any other ﬁxed base-pointx0 ∈ P1(C)), then
for every oriented 3-simplex [a,b,c,d ]∈ C3 we have
≈
D
(
∂([a,b,c,d ])
)
=
≈
D
(
−[a,b,c ]+[ a,b,d] − [a,c,d ]+[ b,c,d]
)
= ~D
(
[a,b,c, ∞]− [a,b,d, ∞]+[ a,c,d, ∞]− [b,c,d, ∞]
)
= ~D
(
[a,b,c,d ]− ∂([a,b,c,d, ∞])
)
= ~D([a,b,c,d ])
and hence ~D =
≈
D◦∂ .
We can think of an element ξ of Ker( C3
∂
→ C2) as a closed, triangulated,
oriented near-3-manifold M, smooth except possibly at its vertices (it is a
union of oriented tetrahedra glued to each other along their faces, and is
hence automatically smooth on the interior of its 3-, 2- or 1-simplices, while
at a vertex its topology is that of a cone on some compact oriented surface),
together with a mapφ from the vertices ofM to P
1(C). Any such elementξ =
40 Don Zagier
∑[σi] gives an identity~D(M,φ ): =∑~D(σi) = 0 among values of the Bloch-
Wigner dilogarithm. This identity can be written explicitly as a combination
of ﬁve-term equations by the calculation above (just replace each simplex
σ =[a,b,c,d ]o f M by [σ,∞]: =[a,b,c,d, ∞]). We can also perform the same
construction over R, starting from a triangulated near-3-manifold M and a
map φ from its 0-skeleton to P
1(R) ; then the element~L(M,φ ) deﬁned as the
sum over the 3-simplices σ of M of the value of L at the cross-ratio of the
images of the vertices of σ under φ will be an integral multiple of π2/2b y
virtue of the functional equation of the Rogers dilogarithm.
Here is an example. Let M be the join of an m-gon and an n-gon,
where m and n are two positive integers. If we write these two polygons
as{xj}j (mod m) and{yk}k (mod n), then this means that M is the union of
3-simplices [xj,xj+1,yk,yk+1]( j∈ Z/mZ, k∈ Z/nZ). Then
∂(M)=
∑
j,k
(
[xj+1,yk,yk+1]−[xj,yk,yk+1]+[xj,xj+1,yk+1]−[xj,xj+1,yk]
)
vanishes because the ﬁrst two terms in the parentheses cancel when we sum
over allj withk ﬁxed and the last two when we sum over allk withj ﬁxed. If
we map them+n vertices ofM to pointsx
j,y k ∈ C (which we simply denote
by the same letters, omitting the mapφ), then we get a functional equation
∑
j (mod m),k (mod n)
D
( yk−yk+1
yk−xj
xj −xj+1
yk+1−xj+1
)
=0 ,
valid for any complex numbersxj,y k. Specializing to xj =e2iXj , yk =e2iYk
with Xj,Y k ∈ R gives real cross-ratios and a Rogers dilogarithm identity
2
π2
∑
j (mod m),k (mod n)
L
( sin(Yk−Yk+1)
sin(Yk−Xj)
sin(Xj −Xj+1)
sin(Yk+1−Xj+1)
)
∈ Z,
where the value of the resulting integer depends on the ordering of the points
X
j and Yk on the circle R/πZ. In particular, if they are equally spaced we
ﬁnd
1
π2
∑
j (mod m)
k (mod n)
L
( sin
(π
n
)
sin
(π
m
)
sin
(kπ
n − jπ
m +t
)
sin
((k +1 )π
n − (j +1 )π
m +t
)
)
= min(m,n)− 1.
If also m =n, then each term occurs n times, so the equation reduces to
1
π2
∑
k (mod n)
L
( sin2(π
n
)
sin2(kπ
n +t
)
)
=1 − 1
n (n∈ N,t ∈ R).
The Dilogarithm Function 41
Finally, specializing a fourth time tot =0a n du s i n gL(+∞)= π2/3=2 L(1),
we ﬁnd
L(1)−1 ∑
0<k<n
L
( sin2(π/n)
sin2(kπ/n)
)
=4 − 6
n,
an equation well known in the physics literature.
