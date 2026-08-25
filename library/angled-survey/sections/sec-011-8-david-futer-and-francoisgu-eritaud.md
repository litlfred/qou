---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-011-8-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 8
pages: 8-8
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
Proposition 3.2. Let τ be an ideal triangulation ofM, containingn tetrahe-
dra. The set of all ways to assign a real number to each pair of opposite edges of each
tetrahedron is naturally identiﬁed withR3n.T h e nA(τ) is a convex, ﬁnite–sided,
bounded polytope inR3n.I f A(τ) ⁄=∅,i t sd i m e n s i o ni s
dimA(τ)= |τ|+|∂M|,
where |τ| = n is the number of tetrahedra and|∂M| is the number of boundary tori
in M.
Proof. Condition (1) of Deﬁnition 3.1 is a system of strict inequalities that
constrains the coordinates ofA(τ) to the open cube (0,π)3n. Meanwhile, conditions
(2) and (3) impose a system of linear equations, whose solution set is an aﬃne
subspace ofR
3n. The intersection between this aﬃne subspace and (0,π)3n will be
a bounded, convex, ﬁnite–sided polytope.
We claim that the number of edges in the triangulationτ is n,t h es a m ea s
the tetrahedra. To see this, observe that each tetrahedron gives rise to 4 boundary
triangles that lie in∂M.T h u s∂M is subdivided into 4n boundary triangles. These
triangles have a total of 12n sides, glued in pairs; thus∂M has 6n edges. Since
every component of∂M is a torus,
χ(∂M)=0=4 n−6n+2n,
hence there are 2n vertices on∂M. Since every edge ofτ accounts for two vertices
on ∂M, the number of edges inτ is n, as claimed. It will be convenient to think of
the tetrahedra as numbered 1 ton, and the edges as numberedn+1to2 n.
Deﬁnition 3.1 involves 2nequations and 3n unknowns. This system can be
encoded in a (2n×3n)m a t r i xA, as follows. Each column ofA corresponds to a
pair of opposite edges of one tetrahedron. For 1≤ i ≤ n,t h ee n t r ya
ij records
w h e t h e ro rn o tt h eith tetrahedron contains thejth edge pair. In other words,aij
will be 1 when 3i−2 ≤ j ≤ 3i,a n d0o t h e r w i s e .F o rn+1 ≤ i ≤ 2n,t h ee n t r yaij
records how many edges out of thejth edge pair become identiﬁed to theith edge
of the glued-up manifold. Thus the entries in the bottom half ofA c a nb e0 ,1 ,o r
