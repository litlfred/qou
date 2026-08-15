---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-000-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 2-3
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
Let V be a compact domain with smooth boundary in 3-space, and let VF ~V! be the space of
smooth vector ﬁelds on V with the L2 inner product ^V,W&5*VVWd (vol). By ‘‘smooth,’’
equivalently C‘ , we mean that derivatives of all orders exist and are continuous.
If we think of the smooth vector ﬁeld V on V as a distribution of electric current, then the
Biot–Savart formula
BS~V!~y!5~1/4p! E
V
V~x!3~y2x!/uy2xu3 d~volx!
gives the resulting magnetic ﬁeld BS( V) throughout 3-space. If we restrict this magnetic ﬁeld to
the domain V, then we get the Biot–Savart operator,
BS:VF~V!!VF~V!.
Theorem A: The equation „ 3BS(V)5V holds in V if and only if V is divergence-free and
tangent to the boundary of V.
a!Electronic mail: cantarel@math.uga.edu
b!Electronic mail: deturck@math.upenn.edu
c!Electronic mail: gluck@math.upenn.edu
JOURNAL OF MATHEMATICAL PHYSICS VOLUME 42, NUMBER 2 FEBRUARY 2001
8760022-2488/2001/42(2)/876/30/$18.00 © 2001 American Institute of Physics
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
It is well known that curl is a left inverse to the Biot–Savart operator when the input ﬁeld V
is divergence-free and tangent to the boundary. The new information is that this result holds in no
other cases. The impact of this is that eigenvalue problems for the Biot–Savart operator, which are
central to the study of helicity, cannot in general be converted to eigenvalue problems for curl
~that is, to a system of partial differential equations !.
Theorem B: The kernel of the Biot –Savart operator is precisely the space of gradient vector
ﬁelds which are orthogonal to the boundary of V.
Actually, somewhat more is true. If V is a smooth gradient vector ﬁeld deﬁned on V and
orthogonal to its boundary, then its magnetic ﬁeld BS( V)50 throughout 3-space. Conversely, if V
is a smooth vector ﬁeld deﬁned on V whose magnetic ﬁeld BS( V)50i n V, then V is a gradient
ﬁeld orthogonal to the boundary of V, and hence BS( V)50 throughout 3-space.
Theorem C: The image of the Biot –Savart operator is a proper subspace of the image of
curl, whose orthogonal projection into the subspace of ‘‘ﬂuxless knots’’ is one-to-one .
Vector ﬁelds on the domain V which are divergence-free and tangent to its boundary are
called ﬂuid knots; we explain this terminology in Sec. IV. Fluxless knots are ﬂuid knots with zero
ﬂux through every cross-sectional surface ( S,
]S),(V,]V). The above theorems lead to several
interesting examples of ‘‘impossible’’ magnetic ﬁelds. Nevertheless, Theorem C falls short of
giving a precise characterization of the image of the Biot–Savart operator, and hence of those
ﬁelds in a domain V which are magnetic ﬁelds of current distributions within V.
Theorem D: The Biot –Savart operator is a bounded operator, and hence extends to a
bounded operator on the L
2 completion of its domain, where it is both compact and self-adjoint .
The eigenﬁelds of this operator which correspond to its extreme eigenvalues turn out to be the
vector ﬁelds in V with minimum energy for given helicity. If we start with a vector ﬁeld V which
is divergence-free and tangent to the boundary of its domain V, that is, a ﬂuid knot, then its
magnetic ﬁeld BS( V), though divergence-free, will in general not be tangent to the boundary of
V. In such a case, we simply modify the Biot–Savart operator BS by following it by orthogonal
projection back to the subspace of ﬂuid knots. The eigenﬁelds of this modiﬁed Biot–Savart
operator which correspond to its extreme eigenvalues are then the ﬂuid knots in V with minimum
energy for given helicity. When the domain V is simply connected, these energy-minimizers
model the stable plasma ﬁelds in V.
