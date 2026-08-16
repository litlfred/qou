---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-034-103-the-nonabelianization-map
section_title: "The nonabelianization map"
section_number: 10.3
pages: 65-66
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Given a nondegenerate spectral network W subordinate to a covering Σ → C, we have
deﬁned a nonabelianization operation which takes a twisted ﬂat rank 1 connection over Σ
to a twisted ﬂat rank K connection over C with ﬂag data. In this section we discuss the
corresponding map ΨW between moduli spaces of twisted ﬂat connections. For simplicity
we take the case where C only has punctures, not boundaries, and restrict attention to W
for which each o(sn) is a total ordering of the set of all sheets. 30
Let us ﬁrst describe the relevant moduli space of rank 1 connections∇ab. The covering
surface Σ has punctures s(i)
n , preimages of the sn onC. Fix a complex line bundleL over ˜Σ;
we will consider ﬂat connections onL with ﬁxed holonomy around the punctures. Namely,
ﬁx parameters m(i)
n ∈ R/Z, with m(i)
n ⁄= m(j)
n fori⁄=j. Let 𝓁n(i) be a small counterclockwise
loop around s(i)
n , and ˜𝓁n(i) its canonical lift to ˜Σ. We require that the holonomy of ∇ab
around ˜𝓁s(i)
n
is exp(2πim(i)
n ). As usual, we consider connections ∇ab only up to gauge
equivalence; our gauge group is the group of smooth maps ¯Σ→ C×, where ¯Σ is the closure
of Σ. LetM(Σ,GL (1); m) be the resulting moduli space of twisted rank 1 ﬂat connections.
M(Σ,GL (1); m) is a torsor for H1(¯Σ, C×)≃ (C×)2g, where g is the genus of ¯Σ.
Next, what can we say about the rank K ﬂat connections∇ we obtain by nonabelian-
ization? Fix a small clockwise loop 𝓁n around sn, and let ˜𝓁n be its canonical lift to ˜C. The
holonomy of ∇ around 𝓁n is the product of several factors: the holonomy of ∇ab along
the pieces of 𝓁n running between walls of W, and the transformations Tp attached to the
walls. With respect to the decomposition (10.10), the former are diagonal matrices whose
product is diag{exp[2πim(i)
n ]}, while the latter are unipotent upper triangular. Their prod-
uct is thus an upper-triangular matrix, with diagonal elements exp[2πim(i)
n ]. Since we have
assumed these values distinct, it follows that the monodromy of∇ around ˜𝓁n is semisimple,
with eigenvalues exp[2πim(i)
n ]. So, let M(C,GL (K); m) denote the moduli space of twisted
rank K ﬂat connections on C (with ﬁxed topology of the principal bundle), such that the
30Our discussion can be generalized to include marked points on boundaries; in that case the relevant
moduli spaces are spaces of connections with irregular singularities, on the surface obtained by shrinking
each boundary component of C to a point. In the special case K = 2 this was discussed in [3]. Examples
with irregular singularities and K >2 are discussed in [32].
– 63 –
monodromy around ˜𝓁n is conjugate to
diag{exp[2πim(1)
n ],..., exp[2πim(K)
n ]}. (10.14)
As we have noted, nonabelianization produces not only a twisted ﬂat connection over
C, but a twisted ﬂat connection over C equipped with ﬂag data. Thus we also deﬁne an
extended moduli spaceMF (C,GL (K); m), consisting of elements ofM(C,GL (K); m) with
ﬂag data.MF (C,GL (K); m) is a ﬁnite cover ofM(C,GL (K); m), as explained at the end
of§10.2. Nonabelianization gives a map
ΨW :M(Σ,GL (1); m)→M F (C,GL (K); m). (10.15)
One simple property of Ψ W is worth noting at once. Given a spectral network W,
letW∗ be obtained by reversing the labels on all walls and the orderings at all punctures.
Then we have
ΨW∗(L,∇ab) = ΨW(L∗, (∇ab)∗)∗. (10.16)
This fact may be of some practical use: the reason is thatW∗
ϑ =Wϑ+π, and determining the
relation between ΨWϑ and ΨWϑ+π is equivalent to determining the “spectrum generator”
which captures the full BPS spectrum.
For the rest of this section we will study ΨW as deﬁned above. However, we must note
that in the physical applications the actual moduli spaceM of the physical theoryS[g,C,D ]
compactiﬁed on S1 is not quiteM(C,GL (K); m); it is more closely related to the space of
SL(K) connections (but even this is a slight oversimpliﬁcation, see [21]). We expect that
there is a variant of our nonabelianization map for which the codomain is precisely M.
The domain of this variant map should not be quite M(Σ,GL (1); m); rather it should be
a space of twisted rank 1 connections on Σ subject to some additional constraints and/or
carrying some additional structure. This is related to the fact that the IR charge lattice of
S[g,C,D ] is not H1(Σ; Z), but rather an appropriate subquotient of it [3]. (See [49, 50] for
a careful discussion of subtle issues of this sort that arise in abelianization of Higgs bundles
for a general group G; we expect that, as far as these topological issues are concerned, the
story for moduli of twisted ﬂat connections will be similar.) We leave the proper extension
of our construction to account for these variations as an open problem. It is related to
open problem 2 of §1.
