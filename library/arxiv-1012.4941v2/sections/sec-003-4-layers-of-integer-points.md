---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-003-4-layers-of-integer-points
section_title: "Layers of Integer Points"
section_number: 4
pages: 9-11
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
Our goal is to describe an algorithm for the eﬃcient solution of a highly symmetric integer
linear program. Again we consider ILP( A,b,c ) with a group Γ of automorphisms as above.
Let us assume that the objective function c⁄= 0 is projectively rational . This means
that we require c to be a constant real multiple of a rational vector. For such a vect orc let
coprime(c) be the unique integral vector with coprime coeﬃcients such that c =ρ coprime(c)
for some positive real ρ. If c is a multiple of a standard basis vector, the single non-zero
coeﬃcient of coprime( c) is deﬁned to be ±1. For an integer k the k-th c-layer is the aﬃne
hyperplane
Hc,k = ker ( x↦→ctx) + k
‖coprime(c)‖2 coprime(c).
We have Hc,k =Hρc,k for all ρ> 0, and H−c,k =−Hc,k =Hc,−k. All points in Hc,k attain
the same value k with respect to the rescaled objective function coprime( c). We call k the
number of the c-layerHc,k. The intersection of Hc,k with the line Rc is called the center.
Lemma 24. If c⁄= 0 is projectively rational, the integral point x∈ Zn is contained in the
c-layer with number coprime(c)tx.
Proof. The number k = coprime(c)tx is an integer. We abbreviate d = coprime(c) and
compute
ct( k
‖d‖2d
)
= ct(dtxd
‖d‖2
)
= dtd
‖d‖2ctx = ctx.
Hencex− (k/‖d‖2)d is contained in the kernel of the linear form ct, that is, the point x lies
in the aﬃne hyperplane Hc,k. □
For the following result it is crucial that the coeﬃcients of coprime( c) are coprime.
Proposition 25. If c⁄= 0 is projectively rational, the c-layers Hc,k for k∈ Z partition the
set Zn of all integral points.
Proof. From Lemma 24 is clear that each integral point is contained in some c-layer. By
construction it is also obvious that the c-layers are pairwise disjoint. It remains to show
that Hc,k∩ Zn is non-empty for all k∈ Z.
Let d = coprime(c). Since the coeﬃcients d1,d 2,...,d n are coprime there are integral
coeﬃcients x1,x 2,...,x n such that
x1d1 +x2d2 +··· +xndn = gcd( d1,d 2,...,d n) = 1 .
However, the left side of this equation equals ctx, whence the point x is contained in the
ﬁrst c-layerHc,1. Now ct(kx) = kct(x) = k implies that the k-th layer contains the integral
point kx for arbitrary k∈ Z. □
10 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
Input: (A,b ) such that Sym(ILP( A,b, /BD )) acts transitively on standard basis
Output: optimal solution of ILP( A,b, /BD ) or “infeasible”
1 let z =ζ /BD be a symmetric optimal solution of the LP relaxation LP( A,b, /BD )
2 k←⌊nζ⌋
3 repeat
4 if it exists then
5 let x be integral point in P (A,b )∩H
/BD ,k
6 else
7 k←k− 1
8 until feasible x found or k <n⌊ζ⌋
9 return x or “infeasible”
Algorithm A: Reduction to /BD -layers
Another way of putting the statement above is that coprime( c) is the unique generator
of the unique minimal Hilbert basis of the one-dimensional pointed con e R≥0c.
Remark 26. An important consequence of Proposition 25 is that for any given bo unds
ℓ,u ∈ R there are only ﬁnitely many c-layers with feasible integral points whose objective
values lie between ℓ and u. This does not hold if the objective function is not projectively
rational.
Theorem 27. For given A and b such that Sym(ILP(A,b, /BD )) acts transitively on the stan-
dard basis the Algorithm A solves the integer linear program ILP(A,b, /BD ).
Proof. Recall that throughout we assumed that the set of feasible points of the linear relax-
ation is bounded. Hence it cannot occur that the integer linear prog ram is unbounded.
Let Γ ≤ Sym(ILP(A,b, /BD )) be a transitive group of automorphisms. The ﬁxed space is
spanned by /BD . If z is an optimal solution of the relaxation LP(A,b /BD ), then, by Proposition 13,
the barycenter β(Γz) = ζ /BD for ζ = 1/n(z1 +z2 +··· +zn) is also an optimal solution.
Now⌊ζ⌋ /BD is an integral point in the ﬁxed space with an objective value not exce eding the
optimal value of the linear programming relaxation. Each /BD -layer with a feasible integral
point meets the one-dimensional polyhedron P ′ ={β(Γx)|x∈P (A,b )}. We infer that no
integral optimal solution of ILP( A,b, /BD ) can have an objective value strictly less than n⌊ζ⌋.
Due to Proposition 25 the /BD -layers partition Zn, and so the feasible points of ILP( A,b,c )
are contained in the set
⌊nζ⌋⋃
k=n⌊ζ⌋
H
/BD ,k.
□
The beneﬁt of Algorithm A is that it reduces a (symmetric) n-dimensional integer linear
programming problem to n integer feasibility problems in one dimension below. Since
the latter is still an NP-complete problem not much is gained, in genera l. The situation
changes, however, if we assume higher degrees of transitivity for the action of the group of
automorphisms.
Remark 28. Searching a family of parallel aﬃne hyperplanes for integer points as in Algo-
rithm A also plays a key role in Lenstra’s algorithm for integer linear pro gramming which
requires polynomial time in ﬁxed dimension [11].
SYMMETRIC LINEAR AND INTEGER PROGRAMS 11
