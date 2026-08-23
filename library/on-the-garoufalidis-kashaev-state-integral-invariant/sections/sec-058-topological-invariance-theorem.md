---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "On the Garoufalidis-Kashaev state-integral invariant"
section_id: sec-058-topological-invariance-theorem
section_title: "Topological Invariance Theorem"
section_number: null
pages: 56-58
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
doc_brief: "On the Garoufalidis-Kashaev state-integral invariant — 61 sections: ACKNOWLEDGMENTS; ABSTRACT; LIST OF TABLES"
---
Theorem 9 (Topological Invariance). LetM be a compact, oriented 3-manifold with
torus boundary and H2(M, Z) = 0. Then the state-integral
FF,M : H1(∂M ;C)→ C
is independent of the choice of ideal triangulation X and balanced angle structure θ,
and thus defines a topological invariant of M.
Remark 8.C = cR×× R× denotes the coefficient system arising from the Gaussian
group, reflecting the multiplicative harmonic analysis used in defining the model.
The target space H1(∂M ;C) parametrizes generalized boundary holonomies: that is,
values of the angle structure assigned to edges lying in the boundary torus. These
data specify the “external” parameters for the quantum wavefunction defined by the
state-integral.
47
Remark 9. LetC = cR×× R× be the self-dual Gaussian group used for the state
variables. It acts (by pointwise multiplication) on the boundary edge chain group
C1(∂X; Z).
After we integrate out the internal face variables and impose the face–pairing
constraints, the resulting tempered distribution is supported on assignments that
satisfy the edge relations; hence it factors through edge homology:
FF,M :A(∂X)2−→H1(∂M ;C)−→ C.
Each boundary component of M is a torus, so H1(∂M ; Z) is free abelian. For a
free abelian group F there is a canonical isomorphism F⊗C ∼= Hom(F,C); hence
H1(∂M ;C) =H1(∂M )⊗C ∼= Hom(H1(∂M ),C).
We therefore regardH1(∂M ;C) as theparameter space of generalised boundary holonomies.
It is this finite–dimensional quotient, not the full space A(∂X)2, that supplies the
“external parameters” for the state–integral.
Remark 10. The condition H2(M; Z) = 0 is imposed for analytic reasons: it rules
out closed normal surfaces that would cause squared Dirac δ-factors when the kine-
matical kernel is multiplied by the pushed-forward dynamical content, see [1, Proof
of Theorem 7] and [6]. It does not imply the existence of a globally balanced angle
structure on any given triangulation.
Remark 11. The balancing condition requires that the angle sum around each internal
edge equals (2, 1)∈C . This enforces a discrete flatness condition—zero holonomy
around internal edges—which is essential for gluing consistency. It parallels the kernel
48
constraints in Andersen–Kashaev [1], where vanishing holonomy ensures the state-
integral is a well-defined distribution.
Remark 12. It also ensures that the product of the kinematical kernel and the dynam-
ical content defines a well-behaved distribution after integrating out the internal edge
parameters. More precisely, it guarantees that the quantum operator algebra defined
by the edge equations is non-degenerate, which is necessary for consistent gluing.
This mirrors the analytic condition in the TQFT construction of Andersen–Kashaev
[1], where a gluing distribution GY is
 well-defined only when certain operator combi-
nations vanish. These correspond to cycles generating ker[H 1(∂M )→ H1(M)], and
their vanishing is equivalent to H2(M, Z) = 0.
