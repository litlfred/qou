---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-006-25-geometric-local-systems
section_title: "Geometric local systems"
section_number: 2.5
pages: 5-6
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
---
geometric local systems (which we do not use here, and recall solely for motivational pur-
poses). Let X be a smooth irreducible complex variety. The following deﬁnition is due to
Deligne (see [De1]).
Deﬁnition 2.7. A Betti Q-local system ρ on X is said to be geometric if there exists a non-
empty Zariski open subset X◦⊂X and a smooth proper surjective morphism π : Y →X◦
such that ρ|X◦is a direct summand in the monodromy representation of the Gauss-Manin
connection on Hi(π−1(x), Q), x ∈X◦, for some i.
6
PAVEL ETINGOF AND ALEXANDER VARCHENKO
Remark 2.8. 1. If ∇has ﬁnite monodromy group G then it is geometric. Indeed, ∇is a
direct summand in a multiple of π∗∇triv, where ∇triv is the trivial connection on the trivial
line bundle on a Galois cover π : eX →X with Galois group G, which implies the statement.
2. By the Decomposition Theorem, any geometric system ρ is semisimple.
3.
The category of geometric systems is invariant under pullbacks, external products
(hence tensor products), and duals. Thus for every X, we have the semisimple Q-linear
Tannakian category GB(X) of geometric Betti local systems on X, which is a tensor subcat-
egory of the Tannakian category LB(X, Q) of all Betti Q-local systems on X. Similarly, the
extension of scalars GB(X)C is a tensor subcategory of the Tannakian category LB(X, C) of
all Betti C-local systems on X.
4. The same deﬁnition can be used in the de Rham realization (for O-coherent D-modules
with regular singularities). Thus for every X, we also have the semisimple C-linear Tannakian
category GdR(X) of geometric de Rham local systems on X, which is a tensor subcategory of
the Tannakian category LdR(X) of all de Rham local systems on X with regular singularities.
Moreover, if X is deﬁned over Q then we have the full category LdR(X, Q) ⊂LdR(X) of all
de Rham local systems on X with regular singularities deﬁned over Q.
5. The Riemann-Hilbert correspondence (taking monodromy of a regular ﬂat connection)
sets up a canonical tensor equivalence LdR(X) ∼= LB(X, C) ([De2]), which in general (for X
deﬁned over Q) does not map the full subcategory LdR(X, Q) into LB(X, Q)C. In other
words, the monodromy of a holonomic system of linear diﬀerential equations deﬁned over
Q need not be deﬁned over Q. However, the Riemann-Hilbert correspondence does restrict
to an equivalence between the subcategories GdR(X) and GB(X)C, i.e., the monodromy of a
direct summand of a Gauss-Manin connection is always deﬁned over Q. In particular, every
object of GdR(X) can be found in the de Rham cohomology of π−1(x) where π : Y →X◦
is deﬁned over Q, hence is itself deﬁned over Q. This striking property follows from the
fact that monodromy of a geometric de Rham local system can be computed in the Betti
realization by following the deformation of twisted cycles in Yx as x varies along X◦.
