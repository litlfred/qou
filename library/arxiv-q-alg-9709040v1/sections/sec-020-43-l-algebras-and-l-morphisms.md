---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-020-43-l-algebras-and-l-morphisms
section_title: "L∞-algebras and L∞-morphisms"
section_number: 4.3
pages: 11-13
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
Suppose that we have an odd vector ﬁeld Q of degree +1 on formal graded manifold (g[1]formal, 0) such
that the Taylor series for coeﬃcients of Q has terms of degree 1 and 2 only. The ﬁrst Taylor coeﬃcient Q1
gives a linear map g−→g of degree +1 (or, better, a map g−→g[1]). The second coeﬃcient Q2 : ∧2g−→g
gives a skew-symmetric bilinear operation of degree 0 on g.
It is easy to see that if [Q, Q] = 0 then g is a diﬀerential graded Lie algebra, with diﬀerential Q1 and
the bracket Q2, and vice versa.
In paper [AKSZ] supermanifolds endowed with an odd vector ﬁeld Q such that [Q, Q] = 0, are called
Q-manifolds. By analogy, we can speak about formal graded pointed Q-manifolds.
11
Deﬁnition. An L∞-algebra is a pair (g, Q) where g is a graded vector space and Q is a diﬀerential of degree
+1 on the graded coalgebra C(g).
Other names for L∞-algebras are “(strong) homotopy Lie algebras” and “Sugawara algebras” (see e.g.
[HS2]).
Usually we will denote L∞-algebra (g, Q) simply by g.
The structure of an L∞-algebra on a graded vector space g is given by the inﬁnite sequence of Taylor
coeﬃcients Qi of the odd vector ﬁeld Q (coderivation of C(g)):
Q1 : g−→g[1]
Q2 : ∧2(g)−→g
Q3 : ∧3(g)−→g[−1]
. . .
The condition Q2 = 0 can be translated into an inﬁnite sequence of quadratic constraints on polylinear
maps Qi. First of these constraints means that Q1 is the diﬀerential of the graded space g. Thus, (g, Q1)
is a complex of vector spaces over k. The second constraint means that Q2 is a skew-symmetric bilinear
operation on g, for which Q1 satisﬁes the Leibniz rule. The third constraint means that Q2 satisﬁes the
Jacobi identity up to homotopy given by Q3, etc. As we have seen, a diﬀerential graded Lie algebra is the
same as an L∞-algebra with Q3 = Q4 = . . . = 0.
Nevertheless, we recommend to return to the geometric point of view and think in terms of formal
graded Q-manifolds. This naturally leads to the following
Deﬁnition. An L∞-morphism between two L∞-algebras g1 and g2 is a pre-L∞-morphism F such that
the associated morphism F∗: C(g1[1])−→C(g2[1]) of graded cocommutative coalgebras, is compatible with
codiﬀerentials.
In geometric terms, an L∞-morphism corresponds to a Q-equivariant map between two formal graded
manifolds with base points.
For the case of diﬀerential graded Lie algebras a pre-L∞-morphism F is an L∞-morphism iﬀit satisﬁes
the following equation for any n = 1, 2 . . .
and homogeneous elements γi ∈g1:
dFn(γ1 ∧γ2 ∧. . . ∧γn) −
n
X
i=1
±Fn(γ1 ∧. . . ∧dγi ∧. . . ∧γn) =
= 1
2
X
k,l≥1, k+l=n
1
k!l!
X
σ∈Σn
±[Fk(γσ1 ∧. . . ∧γσk), Fl(γσk+1 ∧. . . ∧γσn)] +
X
i<j
±Fn−1([γi, γj] ∧γ1 ∧. . . ∧γn) .
Here are ﬁrst two equations in the explicit form:
dF1(γ1) = F1(dγ1) ,
dF2(γ1 ∧γ2) −F2(dγ1 ∧γ2) −(−1)γ1F2(γ1 ∧dγ2) = F1([γ1, γ2]) −[F1(γ1), F1(γ2)] .
We see that F1 is a morphism of complexes. The same is true for the case of general L∞-algebras. The
graded space g for an L∞-algebra (g, Q) can be considered as the tensor product of k[−1] with the tangent
space to the corresponding formal graded manifold at the base point. The diﬀerential Q1 on g comes from
the action of Q on the manifold.
Let us assume that g1 and g2 are diﬀerential graded Lie algebras, and F is an L∞-morphism from g1
to g2. Any solution γ ∈g1 ⊗m of the Maurer-Cartan equation where m is a nilpotent non-unital algebra,
produces a solution of the Maurer-Cartan equation in g2 ⊗m:
dγ + 1
2[γ, γ] = 0 =⇒deγ + 1
2[eγ, eγ] = 0
where eγ =
∞
X
n=1
1
n!Fn(γ ∧. . . ∧γ) ∈g1
2 ⊗m .
12
The same formula is applicable to solutions of the Maurer-Cartan equation depending formally on
parameter ¯h:
γ(¯h) = γ1¯h + γ2¯h2 + . . . ∈g1
1[[¯h]], dγ(¯h) + 1
2[γ(¯h), γ(¯h)] = 0 =⇒d g
γ(¯h) + 1
2[ g
γ(¯h), g
γ(¯h)] = 0 .
The reason why it works is that the Maurer-Cartan equation in any diﬀerential graded Lie algebra g
is the equation for the subscheme of zeroes of Q in formal manifold g[1]formal. L∞-morphisms map zeroes
of Q to zeroes of Q because they commute with Q. We will see in 4.5.2 that L∞-morphisms induce natural
transformations of deformation functors.
