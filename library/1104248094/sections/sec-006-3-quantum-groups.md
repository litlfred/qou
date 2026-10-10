---
doc_id: 1104248094
doc_title: "Commun. Math. Phys. 140, 481-521 (1991) Communications in Mathematical Physics© Springer-Verlag 1991 Hochschild and Cyclic Homology of Quantum Groups"
section_id: sec-006-3-quantum-groups
section_title: "Quantum Groups"
section_number: 3
pages: 7-9
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
doc_brief: "Commun. Math. Phys. 140, 481-521 (1991) Communications in Mathematical Physics© Springer-Verlag 1991 Hochschild and Cyclic Homology of Quantum Groups — For an arbitrary complex linear semisimple Lie"
---
C[G] is made into a Hopf algebra by
V/eC[G], 0,/zeG, (Δ(f))(g,h) = f(gh\
\ (2.15)
where e is the identity of G.
The formal functions on G in the vicinity of identity, C^G), can be viewed as
a Hopf algebra dual to the universal enveloping algebra (7(g).
We now give a new complex for Hochschild homology of Hopf algebras.1 Let
mr9ml denote respectively the natural right, left multiplications of A on A, i.e.,
mr(a)b = ba, m^cήb = ab. Define a right action of A on A by
p(a) = (mr ® m,)(l ® S)Δ(a). (2.16)
This obviously defines a right action since A is algebra homomorphism and S is
antihomomorphism. To be more specific,
p(a)x = £a;xaj9 (2.17)
where Δ(a) = £ a{ ® aί? and άs — S(ά).
ί
Consider the following complex (C.(A\d}\
c^c^..., (2.18)
where d:Cn(A)-*Cn-ι(A\ such that
n-l
-f X (-I)ία0®-(g)αίflί+1(
®α,J_1. (2.19)
It is straightforward to check that d2 = 0, thus it indeed defines a complex. Note
that in this paper we also use d to denote the exterior derivative on G. We hope
there is no confusion as to which d we are referring to.
ξ(x®a®b(S) ®c)= X csί lsjasίx®ai®bj® ~®ck9 (2.20)
i,j,...,k
where Δ(a) = £ α (x) δt , etc.
1 This complex might have been known to other people, but we are unable to locate it in the
literature other than [13]
488 P. Feng and B. Tsygan
Proposition (2.4).
1) ξ:CH(A)^Ca(A)9
2) ξd = bξ, i.e., the following diagram is commutative,
Cΐ(A)
Proof. 1) We define £': Cn(Λ) -+ Cn(,4), by
We claim that £•£' = ξ' ξ = 1. Let us check it for rc = 1, the general case can be
shown similarly. Denote Δ(a) = YJAi®Bi9 Δ2(a) = (1 ® A)(a) = (4® l)(α) = £0,-®
fcyφcy, then, ' j
j j
where we have used m-(S® l) 4 = ε, and (ε® l) Λ= 1. Thus ξ-ξf = 1. Similarly,
2) Again we only check the n = 1 case.
/ \
ξ - d(x (x) α) = α Y J5*.χy4 — ε(α)x = Y JB* xA.. — ε(α)x,
\j J j
and
/ s \ s ί \
Wegetξ-d = d'ξ.
Note that (2.16, 2.17) is the standard complex for the functor Tor,,.. We have
Corollary (2.5).
HH+(A) = H+(C.(A\ d) = Tor£μ, /c),
where A is considered as a right A-module via p defined in (2.15), and k is considered
as a left A-module via the counit ε.
It is this new complex that we are going to use for computing the Hochschild
homology of quantum groups. The new functorial interpretation will be helpful
later in Sect. 6.
3. Quantum Groups
By quantum group we mean the Hopf algebra (over C[[/z]]) of the formal
deformation of the functions on a group. We will start with a connected, complex,
semi-simple Lie group G and consider the formal deformation of formal functions
Hochschild and Cyclic Homology of Quantum Groups 489
Cf(G) and algebraic functions C[G], resulting in respectively quantum formal
group C{(G) and quantum algebraic group Cή[G]. The data we need for the formal
deformation is a Poisson Lie group structure on G, which we refer to as the
quasίclassical limit of quantum groups. Dually this is equivalent to specifying a
Lie bialgebra structure on g, the formal deformation of which results in the
quantized universal enveloping algebra Uh(g).
We start with a description of the quasiclassical limit of quantum groups. Much
of what we state here can be found in [12, 28].
Definition (3.1). A Lie group G is called a Poisson Lie Group if it is a Poisson manifold
such that the group multiplication G x G -> G is a Poisson map, where G x G is
equipped with the product Poisson structure. The Poisson structure is specified by
a bivect or field π, the Poisson tensor,
V/, 06C°°(M). (3.1)
A map φ:M-+N between two Poisson manifolds is a Poisson map if
{Φ*f,Φ*g}M = {f,g}N
Definition (3.2). Let g be a Lie algebra over C, g* iίs dual We say that (g) is a
Lie bialgebra if there is a Lie algebra structure on g* such the map <5:g-> Λ2g
dual to the Lie bracket [,]: Λ2g*->g* is a 1-cocycle with the adjoint action of g
on Λ2g.
The following theorem states the relations between Poisson Lie groups and Lie
bialgebras.
Theorem (3.3). [11]
1) Let G be connected and simply connected, then there is one to one correspondence
between Poisson Lie group structures on G and Lie bialgebra structures on g;
