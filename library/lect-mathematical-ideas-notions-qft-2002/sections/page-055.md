---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-055
section_title: "Page 55"
pages: 55-55
pdf_page: 55
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 55

Definition 8.1. The Hamiltonian (or energy function) of the system with La-
grangian £ is the function H : T*X — R, which is the Legendre transform of £
along fibers; that is, H(q,p) = po — L(q, vo), where vo is the (unique) critical point
of pu — L(q,v). The manifold T*X is called the phase space (or space of states).
The variable p is called the momentum variable.

For example, if £ = v?/2 —U(q), then H(q, p) = p?/2 + U(q).

Remark. Since Legendre transform is involutive, we also have that the La-
grangian is the fiberwise Legendre transform of the Hamiltonian.

Let gq; be local coordinates on X. This coordinate system defines a coordinate
system (q;,pi) on T*X.

Proposition 8.2. The equations of motion are equivalent to the Hamilton equa-

tions
OH . OH

G = 7 Pi =- Zz:
Opi 4:
in the sense that they are obtained from Hamilton’s equations by elimination of p;.

It is useful to write Hamilton’s equations in terms of Poisson brackets. Recall that
the manifold T*X has a canonical symplectic structure w. In fact, w = da, where
a is a canonical 1-form on T*M constructed as follows: for any 2 € T(q,»)(I*X),
a(z) = (p,dr(q,p)z), where 7 : T*X —+ X is the projection. In local coordinates,
we have a = > pidq;, and w = Yo dp; A dq.

Now let (M,w) be a symplectic manifold (in our case M = T*X). Since w is
nondegenerate, one can define the Poisson bivector w~!, which is a section of the
bundle A?T'M. Now, given any two smooth functions f,g on M, one can define a
third function — their Poisson bracket

{f.9} = (df ® dg,w~")
This operation is skew-symmetric and satisfies Jacobi identity, i.e. it is a Lie bracket
on C™(M). For M = T*X, in local coordinates we have

_sn( af 20 _ of 9
{fig} = =a Op; Opi ba):

This shows that Hamilton’s equations can be written in the following manner in
terms of Poisson brackets:

(21) < Flatt). nit) = {f, H}(a(t), p@).

for any smooth function (“classical observable”) f € C%°(I*X). In other words,
Hamilton’s equations say that the rate of change of the observed value of f equals
the observed value of {f, H}.

Note that for a given Lagrangian, the unique function H (up to adding a con-
stant) for which equations (21) are equivalent to the equations of motion is the
Hamiltonian. This provides another definition of the Hamiltonian, which does not
use the notion of the Legendre transform.

8.2. Hamiltonians in quantum mechanics. The yoga of quantization says that
to quantize classical mechanics on a manifold X we need to replace the classical
space of states T* X by the quantum space of states — the Hilbert space H = L?(X)
on square integrable complex half-densities on X (or, more precisely, the corre-
sponding projective space). Further, we need to replace classical observables, i.e.
