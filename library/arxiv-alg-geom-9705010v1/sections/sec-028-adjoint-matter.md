---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-028-adjoint-matter
section_title: "Adjoint matter"
section_number: null
pages: 37-38
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
As soon as [MW] and [DW] appeared, each with a class of integrable systems
which solves its respective version of SYM, the question arose whether there was
a common generalization: an integrable system for SYM with adjoint matter and
arbitrary gauge group G, going to the periodic Toda system in the limit as m and
τ go together to ∞.
In [Mc], Martinec suggested that the elliptic Calogero-Moser system (cf. [OP])
may provide this common generalization. There is such a system for each semisim-
ple G, and the case G = SU(n) agrees exactly with the system in [DW]. There is
also a direct computation [I1] showing that the An and Dn systems can degenerate
to the respective Toda systems, and there is a deformed family of integrable systems
depending on some additional parameters (the elliptic spin models, [I2]). A way of
obtaining the An system by symplectic reduction is given in [GN].
One way to try to understand the geometry of these systems is as follows.
Fix an elliptic curve E, a semisimple group G, and its maximal torus T .
Let
38
RON Y. DONAGI
M, M′ denote the moduli spaces of semistable bundles on E with structue groups
G, T respectively. A special feature of genus 1 is that the natural map M′ →M
is surjective, in fact it is a Galois cover with group W. (It is not true that the
structure group of every semistable G-bundle on E can be reduced to T ; but every
S-equivalence class of semistable bundles contains one whose structure group can
be reduced). Now let X be the moduli space of Higgs bundles on E with ﬁrst
order pole at ∞, and let X′ be its ﬁnite cover induced by M′ →M. (A point of
X′ is an equivalence class of pairs (V, ϕ) where V is a T -bundle on E and ϕ is a
meromorphic Higgs ﬁeld on V ⊗T G). There is a “moment map”
µ : X′ →t⊥/T,
where t⊥⊂g∗is the annihilator of the Cartan t, and the T -action is coadjoint. Now
all the ﬁbers of µ are symplectic, of the minimal dimension 2r (where r = rank(g)),
and at least for some of them (but certainly not for all!), the restrictions of all
the X-Hamiltonians Poisson commute, giving a large family of small integrable
systems. (Presumably, this involves an analogue of the AKS proof of integrability
of the Toda system). As the elliptic curve degenerates to P1 with 0 glued to ∞,
this construction specializes to the periodic Toda.
The question remains, though: of all the possible T -orbits, which one corre-
sponds to SYM with adjoint matter? A necessary condition seems to be that the
T orbit O needs to be W-invariant; otherwise the limit as m →0 will not be the
Hitchin system T ∗M, but its ﬁnite cover T ∗M′. (Or something in-between, if O is
invariant under a subgroup of W.) For SU(n), there is a unique such class (up to
scalars), namely P
i̸=j eij. The natural analogue for arbitrary g would be P
α eα,
the sum over all roots. Unfortunately, this is ill deﬁned: the eα can be normalized
only up to sign, and diﬀerent signs give distinct T orbits. For the orthogonal groups,
there does not seem to be any W-invariant T orbit. David Lowe has pointed out
[L] that for Sp(n) there is an invariant orbit, namely the T orbit of the deﬁning
matrix J. (It is a signed sum of the long root vectors). This does give an integrable
system, but a rather boring one: it is the n-fold product of the SU(2) system, which
does not ﬂow to the pure N = 2 Cn spectral curves described earlier.
In sum, the elliptic Calogero-Moser systems (or their spin variants) seem to
be a promising general class of systems for realizing the SYM theory with adjoint
matter for arbitrary gauge group, but at the moment we lack a good geometric
understanding of these systems, e.g.
via spectral curves, except in the case of
SU(n).
