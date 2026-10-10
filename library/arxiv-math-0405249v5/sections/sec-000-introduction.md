---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
---
Cyclic homology and cohomology were independently discove red by Alain
Connes [1] and Boris Tsygan [21] in the early 1980’s, and shou ld be
thought of as extensions of de Rham (co)homology to various c ategories
of noncommutative algebras. Quantum groups also appeared i n the same
period, with the ﬁrst example of a “compact quantum group” in the C*-
algebraic setting being Woronowicz’s “quantum SU (2)” [24].
The noncommutative diﬀerential geometry (in the sense of Co nnes)
of quantum SU (2) was thoroughly investigated by Masuda, Nakagami
∗Supported until 31/12/2003 by the EU Quantum Spaces - Noncom mutative Geometry
Network (INP-RTN-002) and from 1/1/2004 by an EPSRC postdoc toral fellowship
1
and Watanabe [15]. They calculated the Hochschild and cycli c homology
of the coordinate algebra A(SLq(2)) of quantum SL(2) as well as the
K-theory and K-homology of the C*-algebra of the compact qua ntum
SU (2) group. This work was extended by Feng and Tsygan [5], who
computed the Hochschild and cyclic homology of the standard quantized
coordinate algebra A(Gq) associated to an arbitrary complex semisimple
Lie group G. The homologies are roughly speaking those of a classical
space labelling the symplectic leaves of the Poisson-Lie gr oupG (the semi-
classical limit ofA(Gq)). In particular, the Hochschild dimension of A(Gq)
equals the rank of G. This “dimension drop” had already been observed
for other quantizations of Poisson algebras. Many authors r egarded it as
an unpleasant feature and asked for generalizations of cycl ic homology
which detect the quantized parts of quantum groups as well.
One candidate is twisted Hochschild and cyclic (co)homolog y deﬁned
by Kustermans, Murphy and Tuset [12], relative to a pair of an algebra
A and automorphism σ. This reduces to ordinary Hochschild and cyclic
(co)homology of A on taking σ to be the identity. The standard theory
is intimately related with the idea of considering tracial f unctionals on
noncommutative algebras as analogues of integrals, wherea s the twisted
theory arises naturally from functionals whose tracial pro perties are of
the form h(ab) = h(σ(b)a). Noncommutative spaces equipped with such
functionals include duals of nonunimodular groups, type II I von Neumann
algebras and compact quantum groups. The aim of [12] was to ad apt
Connes’ constructions relating cyclic cohomology and diﬀe rential calculi
to covariant diﬀerential calculi in the sense of Woronowicz , since the vol-
ume forms of such calculi deﬁne in general twisted cocycles r ather than
usual ones [17]. The possibility of pairing twisted cyclic c ocycles (e.g. over
quantum homogeneous spaces) with equivariant K-theory was demon-
strated in [16], and it seems an interesting problem to inves tigate how
far this original motivation of cyclic cohomology extends t o the twisted
setting.
In this paper we compute the twisted Hochschild and cyclic ho molo-
gies HHσ
∗ (A), HCσ
∗ (A) for the coordinate algebra A = A(SLq(2)) of
the quantum SL(2) group, with generic deformation parameter q. We
consider all automorphisms σ of the form a,b,c,d ↦→λa,µb,µ −1c,λ −1d,
wherea,b,c,d are the standard generators, and λ,µ are nonzero elements
of k. As an overview we collect the dimensions of HHσ
n (A) as a k-vector
space, see the main text for explicit formulas for generator s:
theorem 1.1 We have
dimHHσ
n (A) = 0, n> 3,
dimHHσ
3 (A) =
{
N + 1 λ =q−(N+2),µ = 1,
0 otherwise ,
dimHHσ
2 (A) =



N + 1 λ =q−(N+2),µ = 1,
2 λ =q−(N+1),µ =q±(M +1),
0 otherwise ,
dimHHσ
1 (A) =



0 λ /∈q−N,µ =q±(M +1),
0 λ⁄= 1,µ /∈qZ,
4 λ =q−(N+1),µ =q±(M +1),
∞ otherwise,
dimHHσ
0 (A) =



∞ µ = 1,
2 λ =q−(N+1),µ =q±(M +1),
0 otherwise ,
2
for M,N ∈ N.
Strikingly (Theorem 4.12), there exists a family of automor phisms for
which the twisted Hochschild dimension takes the classical value three
(note also that the homological dimension of A(SLq(2)) is three [13]) -
the twisted theory avoids the “dimension drop”. Remarkably , the sim-
plest such automorphism ( λ = q−2,µ = 1) is the canonical modular au-
tomorphism associated to the Haar functional on A. Similar results were
obtained for Podle´ s quantum spheres [7] and quantum hyperp lanes [20].
In [5], Feng and Tsygan considered formal quantizations, wi thA(Gq)
a Hopf algebra over C[[ℏ]] with q = eℏ . They showed that for a Hopf
algebraA over a ﬁeld k, with coproduct ∆, counit ε and antipode S, and
anA-bimoduleM, there is an isomorphism
Hn(A,M)≃ TorA
n (M′,k ) (1)
Here,M′ isM as a linear space with right action given by
m ◭a :=
∑
S(a(2))ma(1) (2)
using Sweedler’s notation for the coproduct, and k =A/kerε is the trivial
leftA-module. Then they computed these Tor-groups using the spec tral
sequence associated to the ﬁltration induced by ℏ.
In this paper we compute Tor A
n (M′,k ) from a Koszul-type free reso-
lution
0→A→A 3→A 3→A→ k→ 0 (3)
ofk. Noncommutative Koszul resolutions were studied by severa l authors,
in particular Wambst [22], but as far as we know were not appli ed to
quantum groups. In our opinion this resolution shows very cl early the ge-
ometric mechanisms behind the computations. We will see tha t the maps
of the resulting complex computing the twisted Hochschild h omology be-
come zero for q = 1, so one obtains the Hochschild-Kostant-Rosenberg
theorem for SL(2) (the algebraic cotangent bundle of SL(2) is trivial).
However, for q⁄= 1 this does not happen for any twisting automorphism.
A summary of this paper is as follows. In section 2 we recall ho w the
twisted theory was discovered [12], then give the deﬁnition s of HHσ
∗ (A)
and HCσ
∗ (A), and the underlying cyclic object. We specialize to Hopf
algebras and explain the methods adapted from [5]. We then pr esent the
general scheme of the noncommutative Koszul complexes used here. In
section 3 we introduce the quantum SL(2) group. In section 4 we present
our calculations of HHσ
∗ (A) forA =A(SLq(2)).
