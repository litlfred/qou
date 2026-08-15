---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography Andreas Belaey,∗ Thomas G. Mertens,† Jacopo Papalini,‡"
section_id: sec-003-quantum-hyperbolic-disk
section_title: "Quantum hyperbolic disk"
section_number: null
pages: 9-11
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
doc_brief: "Probing the singularity at the holographic screen via q-holography Andreas Belaey,∗ Thomas G. Mertens,† Jacopo Papalini,‡ — We study the emergence ofq-deformed spacetime in a lower-dimensional"
---
We have up to this point only discussed the boundary quantum algebra action on boundary
correlation functions. Here we show how this almost uniquely fixes the non-commutative
geometrical features of the induced bulk region if this is to be the boundary theory. This
roughlyreversestheargumentsof[42,49]. Tomatchwithconventionalnotationforquantum
groups, we change the notation from the previous subsection into:
q2L0→K, L +1→E+, L −1→E−. (2.28)
We introduce a new antiholomorphic coordinatez∗, and if we demand that the boundary
is at the locuszz∗ = 1, we can deduce the full bulk structure as follows. Firstly, from
compatibility of the coproduct
∆(K) =K⊗K, ∆(E+) = 1⊗E+ +E+⊗K−1, ∆(E−) =K⊗E− +E−⊗ 1, (2.29)
8
with this boundary condition, we can obtain the action of the generators on both bulk coor-
dinates z and z∗. The specific generators which generate quantum Möbius transformations
on the coordinatez can be found by looking at the spin-0 corepresentation (2.5). The asso-
ciated generators are then given by the induction procedure in Appendix A, which act on
holomorphic monomials as
Kf (z) =f(q2z), (2.30)
E−f(z) = q−1/2
z
f(q2z)−f(z)
q−q−1 , (2.31)
E+f(z) =−q−1/2zf(q−2z)−f(z)
q−q−1 , (2.32)
We now treatz∗ on the same footing asz, and apply these transformations on the boundary
constraintzz∗ = 1 directly. This yields e.g.
K(z⊗z∗)≡K(z)K(z∗) = 1, (2.33)
where we used the grouplike coproduct structure∆(K) =K⊗K andK(c) = 1 for constants.
This fixes thenK(z∗) which by holomorphicity holds everywhere in the bulk. This allows
us to bootstrap the action ofK,E + and E− on arbitrary monomialsf(z∗).3 We obtain
Kf (z∗) =f(q−2z∗), (2.34)
E−f(z∗) =q−1/2z∗f(q−2z∗)−f(z∗)
q−q−1 , (2.35)
E+f(z∗) =−q−1/2
z∗
f(q2z∗)−f(z∗)
q−q−1 . (2.36)
These three relations, together with the previous ones acting onz, implement the action
of the quantum group transformations on the two bulk coordinatesz and z∗. Secondly,
ansatzing a non-commutativity relation z∗z = Azz∗ + B for c-numbers A and B, and
working out e.g.E−(z∗z) = E−(Azz∗ +B) via the coproduct immediately fixesA and B
as:
z∗z =q2zz∗ + 1−q2. (2.37)
This means thatz∗z = 1 =zz∗ describes the boundary, where hence these two coordinates
commute. To sum up, the boundary Uq(sl(2, R)) quantum algebra symmetry, implies the
bulk needs to have non-commutative coordinates (2.37) to be compatible.
3We find K(z∗) = q−2z∗, E+(z∗) = −q1/2 and E−(z∗) = −q−3/2z∗2. By successively using the
coproduct to find the action onz∗n
, one deduces (2.34) - (2.36).
9
These two coordinates can be conveniently written by introducing a radial coordinate
y = 1−zz∗ [49], with non-commutativity:
zy =q−2yz, z ∗y =q2yz∗. (2.38)
The y-coordinate classically ranges between 1 (the origin), and 0 (the boundary). Finally
introducing new coordinates asy =e−r (where r classically ranges from 0 (the origin) and
+∞ (the boundary), andz∗−1
z =e2iφ, we obtain
[φ,r ] =−2i logq. (2.39)
If we would have taken0 < q <1, this would be a standard noncommutativity relation,
telling us that spacetime is fundamentally fuzzy with elementary (Planckian) cell size of
2|logq| (see Fig. 2).4 In the following, we will instead haveq on the unit circle, and the
Figure 2: Quantum hyperbolic disk with fuzzy cells of size2|logq| in (r,φ ) coordinates where
r∈ [0, +∞[ and φ∈ [0, 2π[ where the cell sizes are uniform.
above fuzzyness is still there, but furthermore complexified.
Just as JT gravity provides an explicit realization ofAdS2 spacetime within a quantum
gravity model, can we similarly embed the quantum hyperbolic disk into a fully dynamical
bulk gravitational system?
