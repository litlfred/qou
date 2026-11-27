---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-004-32-discrete-exterior-calculus
section_title: "Discrete exterior calculus"
section_number: 3.2
pages: 8-10
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
Discrete exterior calculus provides discrete deﬁnitions to many of the exte-
rior calculus operators (e.g., exterior derivative, Hodge star, wedge product, etc.)
[15, 16]. These discrete operators have the advantage that they satisfy many of the
rules/identities that characterizes their smooth counterparts. Such mimetic behav-
ior of the discrete operators is known to result in preserving the physics implied
in the smooth governing equations at the discrete level [12], which consequently
improves the physical ﬁdelity of the numerical discretization method.
The key entities in exterior calculus are diﬀerential forms, which according to
Flanders [21] are best thought of as “the things which occur under integral signs”
[18]. For example, considering the integration of a scalar function over a three
dimensional space; i.e.
∫
Ω a dV , an example of a 3-form is b3 = a dV , where
the superscript 3 indicates a 3-form. Similar examples for 2-forms /1-forms can
be deduced from integration of a vector ﬁeld over areas /lines, whereas a 0-form
represents a scalar function. While a smooth diﬀerential form can be integrated on
a k-dimensional domain, the evaluation of a discrete k-form can be thought of as
the integration carried out on discrete k-dimensional mesh objects; i.e., line, area
or volume. Therefore, a discrete di ﬀerential k-form ultimately associates a scalar
with a discrete k-dimensional mesh object through integration. For example, for
the smooth velocity 1-form u♭, its discretization can be deﬁned on primal edges
σ1 as
[∫
σ1 u.dl
]
, or on dual edges⋆σ1 as
[∫
⋆σ1 u.dl
]
, representing a primal or dual
8
discrete 1-form, respectively. Similarly, discrete 0-forms are deﬁned as scalars
on the primal or dual nodes, and the discrete 2-forms are scalars resulting from
the integration of smooth 2-forms on primal 2-simplices (triangles) or dual 2-cells
(polygons).
The space of discrete k-forms deﬁned on primal and dual mesh complexes
is denoted by Ck(K) and Dk(⋆K), respectively. Such spaces are related via the
discrete exterior derivative and Hodge star operators as shown in the following
diagrams for both 2D and 3D cases:
C0(K)
d0
− −−−− →C1(K)
d1
− −−−− →C2(K)↓∗0
↓∗1
↓∗2
D2(⋆K)
−dT
0
← −−−− −D1(⋆K)
dT
1
← −−−− −D0(⋆K)
(12)
C0(K)
d0
− −−−− →C1(K)
d1
− −−−− →C2(K)
d2
− −−−− →C3(K)↓∗0
↓∗1
↓∗2
↓∗3
D3(⋆K)
dT
0
← −−−− −D2(⋆K)
dT
1
← −−−− −D1(⋆K)
dT
2
← −−−− −D0(⋆K)
(13)
The discrete exterior derivative operator d k maps primal k-forms to primal
(k + 1)-forms. The discrete exterior derivative operator that maps dual k-forms to
dual (k + 1)-forms is the transpose of the d (N−k−1) operator, with a negative sign
only for the d T
0 operator in 2D (due to the deﬁned mesh orientation convention).
The discrete Hodge star operator ∗k maps primal k-forms to dual ( N− k)-forms.
The inverse map of the discrete∗k operator is∗−1
k , which maps dual (N− k)-forms
to primal k-forms.
The discrete exterior derivative operator dk is a sparse matrix that is deﬁned as
the transpose boundary operator for the (k+1)-simplices. For example, for the 2D
mesh in Fig 1, the discrete d 1 operator, that maps the primal 1-forms deﬁned on
the primal edges to 2-forms deﬁned on the triangles, is an N2× N1 matrix deﬁned
as
[d1]i j =

+1, if the edge j is a face to the triangle i,
and their orientations are consistent,
−1, if the edge j is a face to the triangle i,
and their orientations are not consistent,
0, if the edge j is not a face to the triangle i.
(14)
9
For the primal nodes laying on the domain boundary; e.g. node 3 in Fig. 1,
the boundary of their dual 2-cells (polygons) includes primal boundary edges.
Accordingly, the [−dT
0 ] matrix, represented by the transpose boundary operator of
these dual 2-cells, is complemented by an additional operator accounting for the
primal boundary edges. The discrete Hodge star operator ∗k, on the other hand,
is a diagonal matrix with the i-th diagonal element being the ratio between the
volume of the dual ( N− k)-simplex⋆σk
i and the volume of its primal k-simplex
σk
i ; i.e.
|⋆σk
i|
|σk
i| . In regards to the wedge product operator, its discrete deﬁnition is
provided within the discretization presentation in the next two subsections.
