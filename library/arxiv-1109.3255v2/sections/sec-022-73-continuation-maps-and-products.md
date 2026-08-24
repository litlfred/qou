---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-022-73-continuation-maps-and-products
section_title: "Continuation maps and products"
section_number: 7.3
pages: 68-70
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
generators of CF ∗(L(d1),L (d2);rH ) all have degree 0, so there are no diﬀerentials,
and we can identify these complexes with their homologies. In order t o obtain the
wrapped Floer cohomology, we must determine the continuation map s.
Let it be understood that we require r ∈ Z in case L,r ∈ 2Z in case C, and r ∈ 3Z
in case D.
To get started, we consider the wrapped Floer cohomology of L(d1) with itself.
Each complex CF ∗(L(d1),L (d1);rH ) has a distinguished element er, sitting at the
minimum of H. The complexes are ﬁltered by action, and the continuation maps ar e
non-increasing with respect to this ﬁltration. Under the r → r′ continuation map,
er ↦→er′; er and er′ are the unique generators of minimal action in their respective
complexes, and in fact their actions are equal, so the only strip is the constant map
to the minimum.
At this point we bring in the product structure.
Proposition 7.2. Let Li one of the Lagrangians L(di) for i = 1, 2, 3. Under the
identiﬁcation
(124) CF ∗(Li,L j;rH ) ∼=CF ∗(φrH (Li),L j)
The product
(125) HF ∗(L2,L 3;rH ) ⊗HF ∗(L1,L 2;sH) →HF ∗(L1,L 3; (r +s)H)
which counts inhomogeneous pseudo-holomorphic triangles corresponds to the product
(126) HF ∗(φrH (L2),L 3) ⊗HF ∗(φ(r+s)H(L1),φ rH (L2)) →HF ∗(φ(r+s)H(L1),L 3)
counting pseudo-holomorphic triangles with no inhomogene ous term.
Proof. First we recall the equation for the product in the wrapped setting . The disk
with three boundary punctures S is equipped with strip-like ends: at the inputs
they are parametrized by ( s,t ) ∈ (0, ∞) × [0, 1], while at the output we have ( s,t ) ∈
(−∞, 0)×[0, 1]. S is also equipped with a closed one form β ∈ Ω 1(S), whose restriction
to ∂S vanishes, such that on the strip-like ends of S, β has the form rdt , sdt and
(r +s)dt for the two inputs and the output respectively. The curves we cou nt are
solutions of
(127) ( du −XH ⊗β)0,1 = 0
Becauseβ is closed and S has no ﬁrst homology, we may ﬁnd a primitive τ ∈C ∞(S)
such that dτ = β, and we assume τ = 0 on the boundary corresponding to L3.
Denoting by φt
H the ﬂow of XH for time t, we can deﬁne a new map v = φ−τ
H ◦u,
MIRROR OF THE PROJECTIVE PLANE 69
meaning that for p ∈ S, we take u(p) and ﬂow it for time −τ (p) by XH. This has
the eﬀect of collapsing each Hamiltonian chord to a single point. Then t he map v
is pseudo-holomorphic without inhomogeneous term, but with a doma in-dependent
almost complex structure obtained by conjugating the original J byφτ
H at each point.
We must relate the products
(128) HF ∗(φrH (L2),L 3) ⊗HF ∗(φ(r+s)H(L1),φ rH (L2)) →HF ∗(φ(r+s)H(L1),L 3)
deﬁned with respect to this domain-dependent almost complex stru cture {Jp}p∈S to
the operation that we studied in Section 4, where the complex struc ture J was ﬁxed.
We ﬁx attention to one strip-like end, say the one corresponding to L2 and L3. On
this end the complex structure depends only on t ∈ [0, 1]. There is a continuation
map
(129) HF ∗(φrH (L2),L 3; {Jt}) →HF ∗(φrH (L2),L 3;J)
counting strips with a domain-dependent almost complex structure that interpolates
between {Jt} and J. We claim that, in our situation, all such strips are constant.
This means that the bases of intersection points on the two sides of the continuation
map correspond. These continuation maps intertwine the product with respect to
{Jp} and the one deﬁned using J, implying that these products agree when expressed
in the basis of intersection points on either side of the corresponde nce.
It remains to prove the claim that all the continuation strips are con stant. Let
u denotes such a strip. Because the Hamiltonian ﬂow preserves the s tructure of the
Lefschetz ﬁbration, each Jp forp ∈S is a complex structure with the property that the
tangent space to a ﬁber is complex, and the projection to the base is holomorphic, once
we equip the base with a suitable complex structure jp. As u is pseudo-holomorphic
with respect to {Jp}, this implies that π ◦u has the property that its diﬀerential at
each point has rank either 0 or 2. Thus the image of π ◦u is a set whose boundary
is contained in the images of the Lagrangians φrH (L2) and L3. Because there are no
topological strips in the base joining diﬀerent intersection points of the base paths, we
conclude that π ◦u must be constant, and the image of u is contained in a ﬁber. But
in the ﬁber there are also no topological strips joining diﬀerent inter section points.
Hence u itself is constant. □
When the diﬀerentials on the Floer complexes vanish, the identiﬁcatio n of the
products holds at the chain level as well. Tracing the isomorphisms th rough, we ﬁnd
that the product with er induces the naive inclusion map on generators
(130) µ2(er, ·) = i :HF ∗(L(d1),L (d2);sH) →HF ∗(L(d1),L (d2); (r +s)H)
Due to the compatibility of the product with the continuation maps, a nd the fact
that er ↦→er′ under continuation, we ﬁnd that the naive inclusion maps commute
with the continuation maps:
(131) HF ∗(L(d1),L (d2);sH)
=
/d15/d15
i /d47/d47HF ∗(L(d1),L (d2); (s +r)H)
cont.
/d15/d15
HF ∗(L(d1),L (d2);sH)
i /d47/d47HF ∗(L(d1),L (d2); (s +r′)H)
70 JAMES PASCALEFF
Thus the continuation map agrees with the naive inclusion map, at leas t on those
generators which are in the image of HF ∗(L(d1),L (d2);sH). It follows that the
continuation maps agree with the naive inclusion maps, at least for r large enough
depending on a particular generator. Hence
(132) HW ∗(L(d1),L (d2)) = lim
r→∞
HF ∗(L(d1),L (d2);rH ),
where the limit is formed with respect to the continuation maps, or wit h respect
to the naive inclusion maps, or (what is equal) the multiplications by the various
elementser.
Spelling this out a bit more gives a precise correspondence with sectio n 7.1. Con-
sider the isomorphism
(133) HF ∗(L(d1),L (d1);rH ) ∼=HF ∗(L(d1 −r),L (d1)) ∼=H ∗(CP2, O(r))
• L: For r ∈ Z, this isomorphism identiﬁes er with yr.
• C: For r ∈ 2Z, this isomorphism identiﬁes er with pr/2.
• D: For r ∈ 3Z, this isomorphism identiﬁes er with (yp)r/3.
Thus the directed systems computing wrapped Floer cohomology ar e identiﬁed with
those computing the cohomology of line bundles on the divisor complem ents.
We can identify the basis of HW ∗(L(d1),L (d2)) with ˆB( 1
d2−d1
Z), where ˆB =
ˆBL, ˆBC, ˆBD is the completion of the aﬃne manifold. The sets B( 1
d2−d1+r Z) embed
in ˆB( 1
d2−d1
Z) and this latter is their limit as r → ∞ ; the map is dilation by d2−d1+r
d2−d1
centered at the minimum of H.
Using the products we computed in section 4, we can identify this bas is ˆB( 1
dZ) for
HW ∗(L(0),L (d)) with a basis of H ∗(U; O(d)), and complete the proof of Theorem
1.2
• L: The point qa,i of ˆBL( 1
d Z) corresponds to the function x−apiyd+a−2i fora ≤ 0,
and zapiyd−a−2i for a ≥ 0. In this case i ≥ 0 can be arbitrarily large, so the
exponent of y is allowed to be negative.
• C: The point qa,i of ˆBC( 1
dZ) corresponds to the function x−apiyd+a−2i for
a ≤ 0, and zapiyd−a−2i for a ≥ 0. In this case i ≤
⌊
d−|a|
2
⌋
can be negative,
so the exponent of p is allowed to be negative, while the exponent of y is
non-negative.
• D: The point qa,i of ˆBD( 1
dZ) corresponds to the function x−apiyd+a−2i for
a ≤ 0, and zapiyd−a−2i fora ≥ 0. In this case i ∈ Z, so the exponents of y and
p are allowed to be negative.
