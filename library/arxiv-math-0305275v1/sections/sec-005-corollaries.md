---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-005-corollaries
section_title: "Corollaries"
section_number: null
pages: 34-38
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2 , C)."
---
In this section we prove some corollaries that can be useful for stu dying
hyperbolic 3-manifolds.
First we show how from Theorem 6.1 one gets a proof of Mostow’s rigid ity
for non-compact manifolds (see [P] and [BCS] for a more general st atement
and a diﬀerent proof).
Theorem 7.1 (Mostow’s rigidity for non-compact manifold) Let f :
M → N be a proper map between two orientable non-compact, complet e
hyperbolic 3-manifolds of ﬁnite volume. Suppose that vol(M)=deg(f )vol(N).
Then f is properly homotopic to a locally isometric covering with t he same
degree as f .
Proof. Let ω be the volume form of N. For X = M,N let Γ X ∼= π1(X) be
the subgroup of PSL(2 , C) such that X = H3/Γ X. Let f∗ denote both the
map induced in homology and the representation f∗ :π1(M) → PSL(2, C).
First assume that the lift ~f : ~M → ~N has the cone-property on the
cusps. This implies that ~f is a pseudo-developing map for f∗. Since f∗[M] =
deg(f )[N] we have
vol(M) = deg(f ) · vol(N) = ⟨ω, deg(f )[N]⟩
= ⟨ω,f ∗[M]⟩ = ⟨f ∗ω, [M]⟩ = vol(f∗).
Thus, by Theorem 6.1 there exists an isometry ϕ such that for anyγ ∈ Γ M
f∗(γ) = ϕ ◦γ ◦ϕ−1.
34
As ~M ∼= H3, we consider the isometry ϕ as an f∗-equivariant map from ~M
to H3. Namely, for any x ∈ H3 and γ ∈ Γ M
ϕ(γ(x)) = f∗(γ)(ϕ(x)).
It follows that ϕ projects to a locally isometric covering ϕ : M → N and
the convex combination from ~f to ϕ projects to a proper homotopy from f
to ϕ. Since the degree of a map is invariant under proper homotopies, th en
deg(ϕ) = deg(f ).
We prove now that f is always properly homotopic to a map whose lift
has the cone property on the cusps. Let ~f be a lift of f . For each cusp Np =
Pp × [0, ∞) let fp = ~f |Pp×{0}. Since f is proper it follows that ~f (Np × {∞}) is
well-deﬁned. Let Fp :Np × [0, ∞) → H3 be the map obtained by coning fp to
~f (Np×{∞}) along geodesic rays. Let ~f ′ be the map obtained by replacing, on
each cusp Np, the map ~f |Np with the map Fp. The map ~f ′ obviously has the
cone-property on the cusps, and projects to a map f ′ :M →N. Moreover,
the convex combination from ~f to ~f ′ projects to a proper homotopy between
f and f ′.
✷
From Theorem 6.1, Theorem 7.1, Corollary 5.11 and the correspondin g
statements for compact manifolds, we get the following statement .
Theorem 7.2 Let M be a complete, oriented hyperbolic 3-manifold of ﬁnite
volume. Let Γ ∼=π1(M) be the sub-group of PSL(2, C) such that M = H3/Γ .
Let ρ : Γ → PSL(2, C) be a representation. Then |vol(ρ)| ≤ | vol(M)| and
equality holds if and only if ρ is discrete and faithful.
Corollary 7.3 Let M be an atoroidal, irreducible, ideally triangulated 3-
manifold. Let z ∈ { C \ {0, 1}}n be a solution of the hyperbolicity equations
such that vol(z) ⁄= 0. Then M is hyperbolic.
Proof. This immediately follows from Corollary 5.10 and Thurston’s Hyper-
bolization Theorem ([Th2]).
✷
In [F] the notion of geometric solution of the hyperbolicity equations
is introduced. Roughly speaking, a geometric solution of the hyperb olicity
equations for a given ideal triangulation τ is a choice of moduli which is
compatible with a global hyperbolic structure on M. In [F] it is shown that
not each solution of hyperbolicity equations is geometric (see [F] for more
details on algebraic and geometric solutions of hyperbolicity equation s).
35
Corollary 7.4 Let M be a complete hyperbolic 3-manifold of ﬁnite volume
and let τ be an ideal triangulation of M. If there exists a solution z ∈
{C \ {0, 1}}n of the hyperbolicity equations for τ , then there exists a solution
z′ of hyperbolicity equations that is geometric. Moreover suc h a solution is
the one of maximal volume.
Proof. Consider a natural straightening of τ , and let z′ be the moduli induced
on τ . By Proposition 3.7, we have only to prove that the moduli are not in
{0, 1, ∞}. Suppose that there is a degenerate tetrahedron ∆ i. Then at least
two vertices, say v and w, of ∆ i coincide.
Let ρ(z) be the holonomy relative to z and let Dz be a developing map
that is also a pseudo-developing map for ρ(z). Then Dz maps ∆ i into a
tetrahedron of modulus zi. But by hypothesis, z is in {C \ {0, 1}}n and so
the vertices of ∆ i are four distinct points. The last assertion follows from
Corollary 5.11 and Theorem 6.1
✷
Corollary 7.4 tells that, once one has a solution z ∈ { C \ { 0, 1}}n of
the hyperbolicity equations for a triangulation τ of a cusped manifold M, in
order to know if M admits a complete hyperbolic structure of ﬁnite volume, it
suﬃces to study the solution of maximal volume. Namely, if one succe eds to
prove that the solution of maximal volume is geometric, then M is hyperbolic.
Conversely, if one proves that such a solution is not geometric (for example
if its holonomy is not discrete) then M cannot be hyperbolic, and this does
not depend on the chosen triangulation.
As an example of application of Corollary 7.4 we give the following:
Corollary 7.5 Let M be a cusped 3-manifold equipped with an ideal trian-
gulation τ . If there exists a solution z ∈ { C \ {0, 1}}n of the hyperbolicity
equations for τ , and all the solutions have zero volume, then M is not hyper-
bolic.
We notice that the hypothesis that all the solutions have zero volum e can
be replaced by requiring that the volumes are too small . This is because the
set of the volumes of the hyperbolic manifolds is bounded from below b y a
positive constant.
Finally, we obtain another proof of the well-know fact that no Dehn ﬁ lling
of a Seifert manifold is hyperbolic.
Corollary 7.6 LetM be a 3-manifold such that ||(M,∂M )|| = 0 and let N
be a Dehn ﬁlling of M. Then N is not hyperbolic.
36
Proof. Suppose the contrary. Let ρ be the holonomy of the hyperbolic struc-
ture of N. From Theorem 5.1 it follows that vol( ρ) = 0, but from Proposi-
tion 4.20 and Corollary 4.15 it follows that vol( ρ) = vol(N)> 0.
✷
References
[BP] R. Benedetti, C. Petronio: Lectures on Hyperbolic Geometry.
Springer Verlag, Berlin-Heidelberg-New York, 1992.
[BCS] J. Boland, C. Connell, J. Souto: Volume Rigidity for Finite Volume
Manifolds. Preprint, available on:
http://www.math.uchicago.edu/~cconnell/papers.html
[D] N. Dunﬁeld: Cyclic surgery, degree of maps of character curves, and
volume rigidity for hyperbolic manifolds. Invent. Math. 136, 623-657
(1999).
[F] S. Francaviglia: Algebraic and geometric solutions of hyperbolic
Dehn ﬁlling equations. Preprint math.GT/0305077 available on
http://arxiv.org
[G] M. Gromov: Volume and Bounded Cohomology. Publ. Math. IHES
56, 5-100 (1082).
[GHL] S. Gallot, D. Hulin, J. Lafontaine: Riemannian Geometry (2nd Edi-
tion). Springer Verlag, 1993.
[Ka] M.Kapovich: Hyperbolic Manifolds and Discrete Groups: Notes
on Thurston’s Hyperbolization. Progress in Mathematics, 183.
Birkh¨ auser Boston, Inc., Boston, MA, 2001.
[Ku] T. Kuessner: Relative simplicial volume. PhD thesis T¨ ubingen Uni-
versity (2001)
[NZ] W. D. Neumann, D. Zagier: Volumes of hyperbolic three-manifolds.
Topology 24, 307-332 (1985).
[PP] C. Petronio, J. Porti: Negatively oriented ideal triangulations and
a proof of Thurston ’s hyperbolic Dehn ﬁlling theorem. Expo. Math.
18, 1-35 (2000), no. 1.
37
[PW] C. Petronio, J. R. weeks: Partially ﬂat ideal triangulations of cusped
hyperbolic 3-manifolds. Osaka J. Math. 37, 453-466 (2000), no. 2.
[P] G. Prasad: Strong rigidity in Q-rank 1 lattices. Invent. Math. 21,
255–286 (1973).
[Ra] J. G. Ratcliﬀe: Foundations of hyperbolic manifolds. Graduate Texts
in Mathematics, 149. Springer-Verlag, New York 1994.
[Ru] W. Rudin Real and complex analysis. Third edition. McGraw-Hill
Book Co., New York, 1987.
[Th1] W.P. Thurston: The geometry and topology of 3-manifolds. Mim-
eographed notes, Princeton University Mathematics Department ,
1979.
[Th2] W.P. Thurston: Three-dimensional manifolds, Kleinian groups and
hyperbolic geometry. Bull. Amer. Math. Soc. 6, 357-381 (1982).
38
