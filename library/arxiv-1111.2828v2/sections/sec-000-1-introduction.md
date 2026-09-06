---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
1.1. Statement of our results 4
1.2. Neumann’s conjecture 7
1.3. Overview of the paper 7
1.4. Acknowledgment 8
2. The Cheeger-Chern-Simons classes 8
2.1. Simply connected, simple Lie groups 8
2.2. Complex groups and volume 9
2.3. The universal classes and group cohomology 10
2.4. Compact manifolds with boundary 11
2.5. Central elements of order 2 11
3. The extended Bloch group 11
3.1. The regulator 12
3.2. The PSL(2, C)-variant of the extended Bloch group 12
3.3. Arbitrary ﬁelds 13
4. Decorations of representations 13
4.1. The fundamental class of a decorated representation 14
5. Generic decorations and Ptolemy coordinates 15
5.1. The geometry of the Ptolemy coordinates 16
5.2. p SL(n, C)-Ptolemy coordinates 17
Date: September 21, 2011.
The authors were supported in part by the NSF.
2001 Mathematics Classiﬁcation. Primary 57N10, 57M27, 58J28. Secondary 11R70, 19F27, 11G55 .
Key words and phrases: Ptolemy coordinates, SL(n, C)-representations, complex volume, Chern-Simons invarian t,
extended Bloch group, hyperbolic 3-manifolds, Cheeger-Chern-Simons class, Rogers dilogari thm, algebraic K-theory,
census manifolds, SnapPy.
1
2 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K. ZICKERT
5.3. Cross-ratios and ﬂattenings 17
6. A chain complex of Ptolemy assignments 18
6.1. The map to the extended Bloch group 19
6.2. Stabilization 20
6.3. p SL(n, C)-Ptolemy assignments 22
7. Independence of the decoration 22
7.1. p SL(n, C)-decorations 25
8. A cocycle formula for ˆc 25
9. Recovering a representation from its Ptolemy coordinate s 26
9.1. Obstruction cocycles and the p SL(n, C)-Ptolemy varieties 33
9.2. Proof of Theorem 1.3 and Theorem 1.8 34
10. Examples 35
11. The irreducible representations of SL(2, C) 39
11.1. Essential edges 40
12. Gluing equations and Ptolemy assignments 41
13. Other ﬁelds 42
References 42
1. Introduction
For a closed 3-manifold M , the Cheeger-Chern-Simons invariant [ 6, 7] of a representation ρ of
π1(M ) in SL(n, C) is given by the Chern-Simons integral
(1.1) ˆc(ρ) = 1
2
∫
M
s∗(
Tr(A ∧ dA + 2
3 A ∧ A ∧ A)
)
∈ C/4π2Z,
where A is the ﬂat connection in the ﬂat SL(n, C)-bundle Eρ with holonomy ρ, and s : M → Eρ
is a section of Eρ. Since SL(n, C) is 2-connected a section always exists, and a diﬀerent choice of
section changes the value of the integral by a multiple of 4π2.
When n = 2 , the imaginary part of the Cheeger-Chern-Simons invariant equals the hyperbolic
volume of ρ. More precisely, if D : ~M → H3 is a developing map for ρ and νH3 is the hyperbolic
volume form, Im(ˆc(ρ)) equals the integral of D∗(νρ) over a fundamental domain for M . In particular,
if M = H3/Γ is a hyperbolic manifold, and ρ is a lift to SL(2, C) of the geometric representation
ρgeo : π1(M ) → PSL(2, C), the imaginary part equals the volume of M . In fact, in this case we have
(1.2) ˆc(ρ) = i(Vol(M ) + iCS(M )),
where CS(M ) is the Chern-Simons invariant of M (with the Riemannian connection). Although
this result is known to experts, no proof seems to be availabl e (see [ 8, 20] for discussions). We
give a proof in Section 2. The invariant Vol(M ) + iCS(M ) is often referred to as complex volume .
Motivated by this, we deﬁne the complex volume VolC of a representation ρ : π1(M ) → SL(n, C) by
(1.3) ˆc(ρ) = i VolC(ρ)
and deﬁne the volume of ρ to be the real part of the complex volume, i.e. the imaginary p art of
the Cheeger-Chern-Simons invariant. Surprisingly, as we s hall see, the relationship to hyperbolic
volume seems to persist even when n > 2.
The set of SL(n, C)-representations is a complex variety with ﬁnitely many com ponents, and the
complex volume is constant on components. This follows from the fact that representations in the
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 3
same component have cohomologous Chern-Simons forms. Henc e, for any M , the set of complex
volumes is a ﬁnite set.
We show that the deﬁnition of the Cheeger-Chern-Simons inva riant naturally extends to compact
manifolds with boundary, and representations ρ : π1(M ) → SL(n, C) that are boundary-unipotent,
i.e. take peripheral subgroups to a conjugate of the unipote nt group N of upper triangular matrices
with 1’s on the diagonal. We formulate all our results in this more g eneral setup.
The main result of the paper is a concrete algorithm for compu ting the set of complex vol-
umes. The idea is that the set of (conjugacy classes of) bound ary-unipotent representations can be
parametrized by a variety, called the Ptolemy variety, which is deﬁned by homogeneous polynomials
of degree 2. The Ptolemy variety depends on a choice of triangulation, b ut if the triangulation is
suﬃciently ﬁne, every representation is detected by the Pto lemy variety. We show that a point c
in the Ptolemy variety naturally determines an element λ(c) in Neumann’s extended Bloch group
ˆB(C), such that if ρ is the representation corresponding to c, we have
(1.4) R(λ(c)) = i VolC(ρ),
where R : ˆB(C) → C/4π2Z is a Rogers dilogarithm.
There is a canonical group homomorphism
φn : SL(2 , C) → SL(n, C)
coming from the natural SL(2, C)-action on the vector space Sym n−1(C2). The map φn preserves
unipotent elements, and we show that composing a boundary-u nipotent representation in SL(2, C)
with φn multiplies the complex volume by
( n+1
3
)
. If M = H3/Γ is a hyperbolic 3-manifold, the
geometric representation ρgeo always lifts to a representation in SL(2, C), but if M has cusps, lifts
are not necessarily boundary-unipotent. In fact, by a resul t of Calegari [ 5], if M has a single cusp,
any lift of the geometric representation takes a longitude t o an element with trace −2. When n is
even, we shall thus, more generally, be interested in bounda ry-unipotent representations in
(1.5) p SL(n, C) = SL( n, C)
/
⟨±I⟩.
Such representations have a complex volume deﬁned modulo π2i, and our algorithm computes these
as well. By studying representations in p SL(n, C), we make sure that when M is hyperbolic, there
is always at least one representation with non-trivial comp lex volume, namely φn ◦ ρgeo.
Walter Neumann has conjectured that every element in the Bloc h group B(C) is an integral linear
combination of Bloch group elements of hyperbolic 3-manifolds. Since the extended Bloch group
equals the Bloch group up to torsion, Neumann’s conjecture wo uld imply that all complex volumes
are, up to rational multiples of iπ2, integral linear combinations of complex volumes of hyperb olic
3-manifolds. In particular, the volumes should all be integr al linear combinations of volumes of
hyperbolic manifolds.
Our algorithm has been implemented by Matthias Goerner. The algorithm uses Magma [ 3]
to compute a primary decomposition of the Ptolemy variety, a nd then uses ( 1.4) to compute the
complex volumes. For n = 2 , we have computed primary decompositions of the Ptolemy var ieties
for all census manifolds with ≤ 8 simplices (these usually ﬁnish within a fraction of a second ) and
all link complements with ≤ 16 simplices in the SnapPy census [ 9] of knots with up to 11 crossings
and links with up to 10 crossings. When there are more than 16 s implices some of the computations
don’t terminate. For n = 3 , computations are feasible for many manifolds with up to 4 simplices,
but for n = 4 the computations run out of memory for all manifolds with mor e than 2 simplices. It
would be interesting to perform numerical calculations for n ≥ 4. Our computations have revealed
numerous (numerical) examples of linear combinations as pr edicted by Neumann’s conjecture. To
4 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K. ZICKERT
the best of our knowledge, our examples are the ﬁrst concrete computations (the ﬁrst of which were
carried out in 2009) of the Cheeger-Chern-Simons invariant (complex volume) f or n > 2.
