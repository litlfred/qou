---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-024-2-this-deﬁnition
section_title: "This deﬁnition"
section_number: 2
pages: 31-33
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
is consistent with the Z3 symmetry of the tetrahedron: the triality symmetry permutes three
equivalent polarizations Π Z, ΠZ′, ΠZ′′ in ( 2.9) which, on the N = 2 gauge theory side,
correspond to the three duality frames ( 3.26) of the theory T1 permuted by the ST element
of SL(2, Z).
The second step is the deﬁnition of T{∆i},˜Π, the theory associated to the union of N
tetrahedra ∆i, in a generic polarization ˜Π. We can always write ˜Π = g◦{ Πi} for some
g∈Sp(2N, Z), where{Πi} is a polarization deﬁned as a product of independent polarizations
Πi of the individual tetrahedra. We choose each Π i to be either Π Zi, ΠZ′
i
or ΠZ′′
i
. Then we
deﬁne
M =
N⋃
i=1
∆(Π)
i ↝ T{∆i},˜Π = g◦
N⨂
i=1
T∆i,Πi (4.3)
where we regard the product of N copies ofT1 theories as a theory with a canonical coupling
to a U(1)N background gauge ﬁeld. We should think of each U(1) as corresponding to an
independent position coordinate in the polarization ˜Π. This deﬁnition is independent of the
choice of Πi∈{ ΠZi, ΠZ′
i
, ΠZ′′
i
} due to the the symmetry ST◦T 1 =T1.
In order to deﬁne the actual SCFT TM,Π associated to the 3-manifold M, we need to
implement a ﬁeld-theory version of the gluing constraints CI→ 2πi for each internal edge I
in the triangulation. The basic idea is to choose a polarization ˜Π =g◦{ Πi} for the collection
of tetrahedra such that
1) it is compatible with the ﬁnal desired polarization Π of the boundary P∂M ; and
2) all the internal edge coordinates CI are “positions” in ˜Π.
If we are careful, we can then construct operators OI in the theory T{∆i},˜Π, one for each
internal edge. These operators will be charged under a subset of U(1) ﬂavor symmetries, also
associated to the edges CI — or rather to independent linear combinations of them. We can
then deﬁne TM,Π by adding a superpotential to T{∆i},˜Π of the form
W =
∑
I∈ internal
edges of M
OI. (4.4)
This superpotential breaks all the U(1) symmetries under which the OI are charged. It also
sets the R-charge of each OI equal to 2. We will see later that this is precisely equivalent to
setting CI = 2πi.
– 30 –
In addition to the internal edge operators OI, the theories T{∆i},˜Π andTM,Π also have
a set of operators OE associated to the external edgesthat are “positions” in Π ⊂ ˜Π. These
operators are charged precisely under theU(1) gauge symmetries that persist as symmetries of
TM,Π — one for each independent position in Π. Indeed, it is easy to see that the ﬂavor group
ofTM,Π will contain exactly 1
2 dimP∂M U(1)’s. In summary, we have built a correspondence:
geometry gauge theory
∆, ΠZ T∆,ΠZ =T1
{∆i},{Πi} T{∆i},{Πi} =⊗iT∆i,Πi
positions, e.g. Zi operatorsOZi with U(1) symmetries
{Πi}→ ˜Π =g◦{ Πi} T{∆i},{Πi}→T{∆i},˜Π =g◦T{∆i},{Πi}
internal edgesCI operatorsOI
external positions, e.g. XE operatorsOE
CI→ 2πi (sympc reduction) W =∑
IOI
M =∪i∆i, Π TM,Π =T{∆i},˜Π + superpotentialW
(4.5)
The construction of operators OI (and alsoOE) in the product theory T{∆i},˜Π is a little
tricky. In order to describe it, we must distinguish two classes of edges. We call an edge “easy”
if its classical coordinate CI (orXE) is a sum containing at most one of the edge parameters
Zi, Z′
i, Z′′
i for any tetrahedron ∆ i; otherwise the edge is “hard.” Thus, CI = Z1 +Z2 or
CI = 2Z′′
1 +Z3 +Z′
4 would be examples of easy edges, while the internal edges ( 2.30) in the
standard triangulation of the ﬁgure-eight knot complement are hard.
Suppose that a triangulation M ={∆i}N
i=1 only contains easy edges, and let us focus
on the internal ones CI. For every edge I, we can deﬁne a polarization {ΠI
i} so that the
tetrahedron parameters appearing in CI are all position coordinates. Due to the deﬁnition
of easy edges, we can always choose Π i∈{ ΠZ, ΠZ′, ΠZ′′} so that the product polarization
has this property. Then, in the theory T{∆i},{ΠI
i} there will automatically exist an operator
OI for the edge CI, constructed as a product of elementary chiral ﬁelds. For example, if
our easy edge is CI = 2Z′′
1 +Z3 +Z′
4, we choose a product polarization {ΠI
i} that includes
ΠI
1 = ΠZ′′
1
, ΠI
3 = ΠZ3, and ΠI
4 = ΠZ′
4
. Then T{∆i},{ΠI
i} will have operators OZ′′
1
,OZ3 and
OZ′
4
, all elementary chiral ﬁelds, from which we deﬁne OI = (OZ′′
1
)2OZ3OZ′
4
.
Now, we are really interested in the theory T{∆i},˜Π, associated to the polarization ˜Π in
which every internal edge is a position coordinate. For each individual CI, there exists an
(aﬃne) Sp(2N, Z) transformation gI such that
˜Π =gI◦{ ΠI
i}, T {∆i},˜Π =gI◦T{∆i},{ΠI
i}. (4.6)
This is not quite an arbitrary transformation. In particular, sinceCI is a position coordinate in
both{ΠI
i} and ˜Π, the action ofgI cannot gauge any of theU(1) ﬂavor symmetries under which
– 31 –
the operatorOI transforms. Therefore, we can easily pull OI through the transformation on
the right of ( 4.6) to deﬁne the corresponding internal edge operator in T{∆i},˜Π.
If a triangulation only contains easy edges, we can repeatedly use this construction to
deﬁne all the operators appearing in the superpotential (4.4). Notice, however, that we deﬁne
eachOI using a diﬀerent mirror Lagrangian description of T{∆i},˜Π. In any given description,
one of the internal edge operators is “simple,” being a gauge-invariant product of elementary
chiral multiplets. The other operators may appear more complicated, and will in general take
the form of monopole operators.
Just as we deﬁned operators for internal edges, we can also deﬁne operators OE for any
easy external edges (or cusp holonomies) that are positions in Π ⊂ ˜Π. In various mirror
duality frames, they will appear either as products of chiral ﬁelds or monopole operators, and
they will be charged under the ﬂavor symmetries of TM,Π that correspond to the positions
XE (or U, etc.).
Currently, we only have a rigorous construction of operators OI andOE for triangula-
tions with easy edges. Indeed, it appears that if we try to deﬁne a theory TM,Π using a
triangulation of M with hard edges, the theory will be slightly degenerate — and potentially
missing some expected operators. We will see an example of this behavior in Section 4.6.
Fortunately, it seems that we can always reﬁne a given triangulation of a 3-manifold M so
that no hard edges are present, and then use this triangulation to construct TM,Π.
One of our central claims is that the theories TM,Π constructed here are topological in-
variants of a three-manifoldM (and a polarization of its boundary), which do not depend on
the actual triangulation being used to deﬁne them — or on the choice of reﬁnement, should
a given triangulation include hard edges. In particular, we claim that diﬀerent triangula-
tions lead to diﬀerent mirror-symmetric descriptions of the same underlying 3d SCFT. To
understand this, we now proceed to analyze the simplest and most important example of a
triangulated 3-manifold: the bipyramid.
