---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-020-71-algebraic-motivation
section_title: "Algebraic motivation"
section_number: 7.1
pages: 64-64
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
wrapped Floer cohomology, it is useful to understand the algebraic side ﬁrst. The
starting point is the following proposition ([40], statement (1.10)).
Proposition 7.1. Let X be a smooth quasiprojective variety over C, Y ⊂ X a
hypersurface, and U = X \Y the complement. Write Y = s−1(0), where s is the
canonical section of the line bundle L = OX (Y ). Let F be a coherent sheaf on X.
Multiplication by s deﬁnes an inductive system
(115) H ∗(X, F ⊗ Lr−1) /d47/d47H ∗(X, F ⊗ Lr) /d47/d47H ∗(X, F ⊗ Lr+1) /d47/d47· · ·
and the limit is
(116) lim
r→∞
H ∗(X, F ⊗ Lr) ∼=H ∗(U, F|U)
We spell out the application of this proposition to each of the cases w e consider
• UL: Since L = {y = 0} is a line, we identify L ∼= O(1) and take s =y. Thus
(117) H ∗(UL, O(d)) ∼= lim
r→∞
H ∗(CP2, O(d +r))
where the limit is formed with respect to multiplication by y. An element of
H 0(UL, O(d)) is a rational function f (x,y,z )/yr, where f is a homogeneous
polynomial of degree d +r.
• UC: Since C = {xz −y2 = 0 } is a conic, we identify L ∼= O(2) and take
s =p =xz −y2. Thus
(118) H ∗(UC, O(d)) ∼= lim
r→∞
H ∗(CP2, O(d + 2r))
where the limit is formed with respect to multiplication by p = xz −y2.
An element of H 0(UC, O(d)) is a rational function f (x,y,z )/pr, where f is a
homogeneous polynomial of degree d + 2r.
• UD: Since D = {yp = xyz −y3 = 0 } is a cubic, we identify L ∼= O(3) and
takes =yp. Thus
(119) H ∗(UD, O(d)) ∼= lim
r→∞
H ∗(CP2, O(d + 3r))
where the limit is formed with respect to multiplication by yp. An element of
H 0(UD, O(d)) is a rational function f (x,y,z )/(yp)r, where f is a homogeneous
polynomial of degree d + 3r.
For the purposes of computation, a useful simpliﬁcation comes fro m noting that
the line bundles O(d) may become isomorphic over the complements.
• UL: Since UL ∼= C2, all the line bundles O(d) are isomorphic over it.
• UC: The complement of a smooth conic in CP2 has H 2(UC; Z) ∼= Z/2Z, gen-
erated by c1(O(1)). The deﬁning section p : O → O(2) is an isomorphism over
UC, and so Pic( UC) ∼= Z/2Z as well.
• UD: Since UD ⊂UL, all the line bundles O(d) are isomorphic over it as well.
