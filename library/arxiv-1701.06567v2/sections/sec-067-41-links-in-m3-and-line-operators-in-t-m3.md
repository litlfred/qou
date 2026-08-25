---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-067-41-links-in-m3-and-line-operators-in-t-m3
section_title: "Links in M3 and line operators in T [M3]"
section_number: 4.1
pages: 56-60
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Consider a knot K in M3 colored by a representation R of G. As described above, it corre-
sponds to a certain half-BPS line operator Γ K,R in T [M3;G]:
(K,R) ↦−→ ΓK,R ∈ C. (4.2)
whereC is the category of BPS line operators in N = 2 SCFT T [M3,G ]. The homological
invariant for a combined system of a knot and a 3-manifold is then given by the BPS Hilbert
space of T [M3] on the disk D2 with ΓK,R inserted at O, the center of the disk (see Figure 1):
Ha[M3;K,R]≡H T [M3](D2, ΓK,R;a), a ∈ (TorH1(M3, Z))N/SN (4.3)
where a denotes the choice of boundary condition, the same as in the case without a knot.
It has the same gradings as before, namely the q-grading i and the homological (R-charge)
grading j:
Ha[M3;K,R] =
⨁
i∈∆a+Z,j∈Z
Hi,j
a [M3;K,R] (4.4)
– 55 –
And, as before, the graded Euler characteristic gives the partition function on D2×S1:
ˆZa(q; ΓK,R)≡ZT [M3](D2×S1, ΓK,R;a) =
∑
i,j
(−1)jqiHi,j
a [M3;K,R] (4.5)
now, in 3dN = 2 theoryT [M3] with an extra 1d “impurity” ΓK,R supported on O×S1. The
analogue of the Conjecture 2.1 is then the following:
Conjecture 4.1 The WRT invariant of M3 with a knot K colored by representationR can
be decomposed into the following form:
ZSU (2)k[M3;K,R] = (i
√
2k)b1(M3)−1 ∑
a,b∈
TorH1(M3,Z)/Z2
e2πik𝓁k(a,a)Sab ˆZb(q; ΓK,R)|
q→e
2πi
k
(4.6)
where
ˆZb(q; ΓK,R)∈ 2−cq∆bZ[[q]] ∆ b∈ Q, c ∈ Z+ (4.7)
convergent in|q|< 1 and Sab is the same as in Conjecture 2.1
For certain 3-manifolds with an extra symmetry, preserved by the knot K, we have an extra
grading whose value we denote by 𝓁:
Ha[M3;K,R] =
⨁
i∈∆a+Z,j,𝓁∈Z
Hi,j;𝓁
a [M3;K,R] (4.8)
In practice, to compute these homological invariants, one needs a convenient ultra-violet
(UV) description of the ﬁvebrane setup ( 4.1) or, better yet, of the IR superconformal theory
T [M3]. In general, the brane system ( 4.1) and the 3d theoryT [M3] may admit many such UV
descriptions, in various duality frames, all of which ﬂow to the same IR physics and produce
the same homological invariants (space of BPS states).
In a given UV gauge theory description of T [M3], the objects in the tensor category C
of BPS line operators can be understood as vector spaces — the “Hilbert spaces of N = 2
quantum mechanics on the line, coupled to the bulk gauge theory”. The most familiar line
operators are Wilson operators Wλ, labeled by a representation λ of the UV gauge group 44
G (which, in general, has little to do with G). The corresponding object of the category C
is, tautologically, the representation λ. The Wilson lines are expected to form a complete
basis of line operators in the IR theory, in the sense that any line operator (not necessarily
associate to a knot) should have the following decomposition:
IRz }| { UVz }| { (4.9)
ΓK,R =
⨁
λ,i,j,𝓁
Wλ⊗Hλ;i,j;𝓁
K,R .
44In general,G is diﬀerent fromG. For a quiver theory, it may be given by a product×iGi over the vertices.
– 56 –
The reason is very simple — one can always decompose the “defect Hilbert space” into
representations of G, with the multiplicity space Hλ
Γ associated with the representation λ.
The symmetry G plays the role of the ﬂavor symmetry in QM on the line, which couples
to 3d theory T [M3] by gauging G in the bulk. If Γ is a generic physical line operator ( cf.
superposition of physical line operators), the corresponding multiplicity spacesHλ
Γ are honest
vector space that are at least doubly-graded, with the (i,j )-grading coming fromU(1)q×U(1)R
symmetry of the brane system (4.1). When the ﬂavor symmetry U(1)β is a symmetry of both
T [M3] and Γ, the third 𝓁-grading is also present.
As a trivial example, consider a line defect given by a quantum mechanics that is com-
pletely decoupled from the bulk. Then,
ΓQM = W0⊗H QM, (4.10)
whereHQM is the Hilbert space of the quantum mechanics and W0 is the trivial Wilson
loop. So, we see that ( 4.9) has a chance of being correct, even if there are inﬁnitely many
possibilities of engineering defects via 1d-3d coupled systems. In this sense, λ is analogous
to the label “a” of the homological blocks, which reduces inﬁnitely many possible boundary
conditions to a ﬁnite set. In fact, this isn’t just an analogy — it comes from the equivalence
of two categories
C∼=CB. (4.11)
Namely, a line operator can be viewed as the interface between two boundary conditions,
and picking a “reference boundary condition” ( e.g. the one giving ˆZ0 with zero brane charge)
will identify the two categories. This equivalence is a special feature of 3d quantum ﬁeld
theories, which associate categories to S1, with the objects that can be interpreted either as
line operators or as boundary conditions at spatial inﬁnity.
At this point, λ can still be an arbitrary representation of the UV gauge group G, and
one might naively think that C is
CUV = Rep(G), (4.12)
given by the representation category ofG. But in light of the equivalence (4.11), we expectC to
be much smaller, sinceCB is generated by ﬁnitely many simple objects (boundary conditions
that give homological blocks), as we have seen in all our examples.
Indeed, (4.12) is often redundant, due to presence of Chern-Simons couplings in T [M3].
There is a set Λ M3 of “integrable representations” of G giving a complete basis of Wλ in
T [M3;G], and every Wilson loop labeled by a non-integrable representation can be decom-
posed as
Wν =
⨁
λ∈ΛM3
i,j,𝓁∈Z
Wλ⊗Hλ;i,j;𝓁
ν . (4.13)
All such relations generate an ideal (in the categorical sense) of CUV, andC is given by the
quotient
C =CUV/I. (4.14)
– 57 –
As a vector space, C is the same as Λ M3⊗ C, but the algebra structure depends on I and is
determined by the theory T [M3] in a non-trivial way. BothCUV andI depend on the duality
frame (presentation of M3), but it is expected that the quotient category C is a topological
invariant ofM3. It describes line operators / boundary conditions in the IR theory, which is
what usually meant by T [M3].
We expect, for arbitrary M3, the independent Wilson loops in the theory T [M3;G] are
labeled by elements in 45
ΛM3 = TorH1(M3, Λrt)/WG, (4.15)
where Λrt is the root lattice of g andWG is the Weyl group (not to be confused with Wilson
lineWλ in UV description ofT [M3]). The argument for this statement parallels our discussion
of boundary conditions given by M2-brane charges “a”, which take values in exactly the same
set. And the fundamental Wilson loops are expected to come from knots K wrapping torsion
1-cycles, colored by a representation R of G (i.e.R∈ Λchar(G)/WG).
IfG is abelian, then ΛM3 is a group and one can introduce an action of line operators on
boundary conditions, which we call the shift action in what follows. This action is expected
because Wilson line operators Wλ, λ∈ ΛM3, can be engineered using M2-branes46 as in (4.1),
and the label “a” for homological blocks also measures M2-brane charges. In other words, a
Wilson loop Wλ relates two Hilbert spaces
HT [M3](D2,Wλ;a) ∼ HT [M3](D2,Wλ;a−λ). (4.16)
One does not a priori know whether this is an isomorphism or not, or how the gradings on
the two sides are related. However, in various examples below we observe that, at the level
of homological blocks ˆZa(q), Wilson loop acts as a simple shift operator, even for G =SU (2)
if the Weyl group action is properly taken into account.
As before, our main tools for probing the new homological invariants are SUSY-protected
quantities. In particular, using a UV descriptions of T [M3] and a half-BPS impurity Γ K,R,
one can compute the partition function of T [M3] onD2×S1 with ΓK,R inserted alongO×S1
as follows:
ˆZa(q,t ; ΓK,R)≡ZT [M3](D2×S1, ΓK,R;a) =
=
∫ dz
2πiz [same as without ΓK,R]
∑
λ∈ΛM3
i,j,𝓁∈Z
χλ(z)qit𝓁(−1)j dimHλ;i,j;𝓁
K,R (4.17)
where z stands for the gauge fugacities of the UV gauge group G and χλ is the character of
theG-representationλ.
45So far, we have ignored the diﬀerence between G and the Langlands dual group G∨ because the quantities
considered so far are not sensitive to the global structure of the group. However, the spectrum of Wilson loops
is sensitive to this diﬀerence, and ( 4.15) is stated for the adjoint form G =Gad. If G has a center, one needs
to add the representations of G where the center acts non-trivially. Reader interested in this subject may
consult [69] where this issue was extensively discussed in a similar brane system.
46i.e. Wλ = ΓK,R when torsion homology class of R-cable of K is given by λ∈ ΛM3
– 58 –
Similarly, we can consider the S2×S1 superconformal index with half-BPS impurities
inserted at one (or both) poles of S2. The UV localization formula for the index is modiﬁed
as follows (when the impurity is at the north pole):
I(q,t ; ΓK,R)≡ZT [M3](S2×S1; ΓK,R) =
=
∑
m
∫ dz
2πiz [same as without Γ]
∑
λ∈ΛM3
i,j,𝓁∈Z
χλ(zqm/2)qit𝓁(−1)j dimHλ;i,j;𝓁
K,R . (4.18)
As we demonstrate in a variety of examples, it obeys the modiﬁed factorization formula
I(q,t ; ΓK,R) =
∑
a
|Wa|ˆZa(q,t ; ΓK,R)ˆZa(q−1,t−1). (4.19)
Note, all of the above relations depend only on the IR data, namely on K and its color R,
not on the UV description of ΓK,R. In particular, note that λ is always summed over in these
relations, which goes back to the basic relation between IR line operators ΓK,R (“impurities”)
and their description ( 4.9) in the UV theory via Wλ.
The reader should keep in mind that there are two non-trivial maps (dualities) involved
in the study of knots. 47 First, there is a rather non-trivial map ( 4.9) between line operators
in the IR theory T [M3] and its UV description (or, rather, one of many UV descriptions).
This UV/IR map has nothing to do with applications to low-dimensional topology and is a
standard phenomenon in quantum ﬁeld theory. In addition, there is a map between knots
and links colored by R in a TQFT on M3 and half-BPS line operators (“impurities”) in the
3dN = 2 theory T [M3]. This map is a chapter in the so-called 3d/3d correspondence. The
reason one should pay attention to both of these maps is that it is their composition which
relates homological invariants of K⊂M3 to concrete calculations in T [M3;G],
UV line
operators Wλ
UV/IR map
←−−−−−−→
1
2-BPS impurity
ΓK,R
3d/3d correspondence
←−−−−−−−−−−−−→link K⊂M3
colored byR
Because each of these maps can be rather non-trivial, one should not confuse the representa-
tion λ that labels half-BPS line operators in the UV description with the “color” of K. The
latter is denoted byR and, whenever non-trivial, leads to theR-colored link homology [43,79]
in our setup ( 4.1).
So far, the discussion in this section is very general and, as such, may be somewhat
abstract. We will now give some very concrete examples for G =SU (2).
