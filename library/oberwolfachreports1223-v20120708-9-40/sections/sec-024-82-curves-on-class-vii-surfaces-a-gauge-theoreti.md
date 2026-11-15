---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-024-82-curves-on-class-vii-surfaces-a-gauge-theoreti
section_title: "Curves on class VII surfaces. A gauge theoretical approach for proving existence of a cycle"
section_number: 82
pages: 48-52
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Curves on class VII surfaces. A gauge theoretical approach for
proving existence of a cycle
Andrei Teleman
Let M be a 4-manifold with b1 = 1 and b+ = 0 (negative deﬁnite intersection
form). Suppose for simplicity π1(M, x0) = Z, and put b := b2(M). Donaldson’s
ﬁrst theorem: qM is standard, so H2 has a basis (ei)1≤i≤b with eiej = −δij. We
put I0 := {1, . . . , b}, for I ⊂I0 put ¯I := I0 \ I, eI := .
i∈I eI. The characteristic
elements with vanishing SW expected dimension have the form cI := eI −e¯I.
The Seiberg-Witten invariants are not well deﬁned [1]: A generic SW moduli
space contains a circle of reductions and ﬁnitely many regular irreducible points.
What can try to deﬁne an invariant by counting only the irreducible points (by
taking into account the signs deﬁned by the ﬁxed orientation data).
But one
can see that, deforming the parameters, some irreducible points might become re-
ducible and then disappear, so the algebraic cardinality of the irreducible part of
the moduli space will jump. One has a countable chamber structure in the param-
eter space, and the SW “invariant” obtained by counting algebraically irreducible
points can take inﬁnitely many values [1].
Idea: forget about SW and use ideas from original GW theory: count only ratio-
nal curves in the given class. The corresponding Gromov-Witten moduli space of
rational curves will be: MGW
ei
( ˆH) = {Ei} , so this approach produces apparently
a well deﬁned “invariant” of the complex structure (which takes the values 1), but
this invariant is not constant in deformations:
Example: X →D with Xt = blown up Hopf surface for t̸ = 0 and X0 a so
Invariants in Low-Dimensional Topology and Knot Theory
49
called Kato surface (a known minimal class VII surface). X0 does not contain
any eﬀective divisor (irreducible or not) in the classes ei. A natural question is:
What happens with the exceptional curves Ei,t as t →0? Why do they vanish?
The answer is: Explosion of area. The area of Ei,t tends to inﬁnity as t →0! A
more sophisticated answer is given in a recent paper with G. Dloussky: “Inﬁnite
bubbling”.
About Kato surfaces: they are the known minimal class VII surfaces with b2 >
0. Any Kato is a deformation of blown up Hopf surfaces and has (intriguing) b2
rational curves. So the total number of rational curves is constant in the known
deformations, but the classes which are represented by these curves are not. Curves
appear in classes with negative expected dimension. . .
and we have no tools to
count all rational curves in all possible homology classes (including those with
negative GW expected dimension).
2. Class VII surfaces (not classiﬁed yet) V II ⊃V IIb2>0
min
⊃Kato surfaces (the
known surfaces in the class).
Conjecture 1. If X ∈V IIb2>0
min
then X has b2 rational curves. This would imply
that X is Kato, so it would complete classiﬁcation. It is equivalent to the GSS
conjecture.
Conjecture 2. If X ∈V IIb2>0
min
then X has a cycle of rational curves. This would
imply that X is a deformation of blown up Hopf surfaces, so it would complete
classiﬁcation up to deformation equivalence.
3. Using Donaldson theory: E Hermitian 2-bundle D := det(E) ﬁx a ∈A(D).
Put MASD
a
(E) := {A ∈Aa(E) |(FA)+
0 = 0}/Γ(SU(E)). The obvious pimorphism
ρ : H1(M, Z) →{±1} deﬁnes a ﬂat line bundle Lρ. Important ⊗Lρ deﬁnes an
involution on MASD
a
(E): its ﬁxed points are twisted reductions (whose pull-back
on the double cover ˜
Mρ associated with ρ are split) and its quotient is the usual
moduli space of PU(2) instantons on ¯PE.
Example: b = 2. Take E with c2(E) = 0, c1(E) = e1 + e2. One has −p1( ¯PE) =
∆(E) = 4c2(E) −c2
1(E) = 2 ≤3, so the corresponding moduli space is compact.
It contains two circles of reductions corresponding to the topological splittings
E = L0 ⊕Le1+e2, E = Le1 ⊕Le2. Any circle Ci has a neighborhood which is a
ﬁbration over Ci with ﬁbre cone over P1 (= D3) so smooth! If π1(M) ≃Z, one
can count also the twisted reductions and gets two isolated twisted reductions.
For generic metric one gets a smooth 4-manifold. Its signature σM := σ(M) is a
C∞-invariant of M.
We will prove: If M is the underlying diﬀerentiable manifold of an unknown
minimal class VII surface with b2 = 2 then M ≃S4, and using this fact, we will
prove Conjecture 2 for b2 = 2. Therefore the moduli space M can be accurately
described (although the information we have on the base manifold M is very vague)
using complex geometry. The main tool will be the KH correspondence, relating
instantons to stable bundles. This correspondence has been used by Donaldson
to compute Donaldson invariants, so he used complex geometry to solve gauge
50
Oberwolfach Report 28/2012
theoretical problems. This time we use gauge theory to solve complex geometric
problems.
Dichotomy: Either the signature invariant σ is always trivial (which will sub-
stantially simplify the proof of Conjecture B in the case b2 = 2) or is not trivial,
which would be interesting from a topological point of view.
Remark: Using a standard cobordism argument and the Donaldson class µ(h),
where h is a generator of H1(M, Z), it follows that the two circles Ci belong to the
same component of the moduli space.
Let now X be a minimal class VII surface with b2 = 2, and M := MASD
a
(E) =
Mpst
K (E) (the Kobayashi-Hitchin correspondence) is compact, has a structure of
smooth complex surface in the complement of the reductions (on the stable part).
Known pieces of M: (1) 2 circles of reductions C1, C2, (2) 2 twisted reductions
B1, B2, (3) four strata of stable extensions Mst
I , I ⊂{1, 2}.
Mst
I consists of
extensions of the form 0 →L := K ⊗M∨→E →M →0 with c1(M) = cI.
Mst
{1,2} is a P1-bundle over a punctured disk, Mst
{1}, Mst
{2} are punctured disks,
and Mst
∅= {A, A′ := A ⊗LR}, where A is the central term of a non-trivial
extension:
(1)
0 →K →A →O →0.
Step 1: M0 := C1 ∪C2 ∪{B1, B2} ∪(∪I̸=∅Mst
I ) is a connected component of M.
Using the fact that the two circles of reductions belong to the same component,
one can see that this component (the known component of the moduli space) is
isomorphic to S4.
Dichotomy: Either A belongs M0 (the known component of the moduli space
space), or it belongs to a smooth compact surface Y ⊂Mst.
Remark: If A belongs to M0 then X has a cycle of rational curves!
1This can
be proved easily: Suppose for instance that A belonged to one of the strata Mst
I ,
I̸ = {1, 2}. In this case the bundle A (which was deﬁned as the central term of the
nontrivial extension (1)) could be written as an extension in a diﬀerent (new) way.
If this was the case, composing the epimorphism of the exact sequence (1) with
the monomorphism of the new exact sequence we obtain a line bundle morphism,
which is neither trivial nor isomorphism. The zero locus of this composition is a
non-empty eﬀective divisor, and one can prove that it is a cycle.
Step 2: The appearance of a new compact connected component Y in the moduli
space leads to a contradiction.
For this statement we have two proofs: for the ﬁrst one, which uses the classiﬁ-
cation of complex surfaces, we refer to [3]. A new proof is based on very recent
results of Bismut, namely on a reﬁnement of the GRR theorem in the non-K¨ahler
case, which gives the computation of the Chern character of the total direct image
1A cycle of rational curves is en eﬀective divisor of the form C = !
i∈Zk Ci, where either
k = 1 and C0 is a rational curve with a simple singularity, or k ≥2 and Ci ·Ci+1 = 1, Ci ·Cj = 0
for i −j̸ = ±1.
Invariants in Low-Dimensional Topology and Knot Theory
51
in Bott-Chern cohomology. This proof might be generalized to arbitrary b2 (work
in progress).
References
[1] Ch. Okonek, A. Teleman, Seiberg-Witten invariants for 4-manifolds with b+ = 0, Complex
Analysis and Algebraic Geometry, eds. T. Peternell, F. O. Schreyer, de Gruyter Berlin-New
York, 347–357, 2000.
[2] A. Teleman, Donaldson Theory on non-K¨ahlerian surfaces and class VII surfaces with
b2 = 1, Invent. Math. 162 (2005), 493–521.
[3] A. Teleman, Instantons and holomorphic curves on class VII surfaces, Annals of Mathe-
matics, 172 (2010), 1749–1804.
[4] A. Teleman, Gauge theoretical methods in the classiﬁcation of non-K¨ahlerian surfaces,
Algebraic Topology - Old and New, (the Postnikov Memorial Volume), Banach Center
Publications, vol. 85, 2009.
Functorial maps and weak parities
Igor Nikonov
Parity theory introduced by V.O. Manturov [1] has many interesting applica-
tions. One of them is the construction of functorial maps [2, 3]. Functorial map
is deﬁned as transformation of knot diagrams that replaces classical crossings of
diagrams with virtual ones in a way compatible with Reidemeister moves: if two
diagrams diﬀer with a Reidemeister move then the functorial map transforms them
into two diagrams that diﬀer with a Reidemeister move. So any functorial map
determines a well-deﬁned map from knots to knots and thus allows to get new
knot invariants as compositions of the functorial map with known knot invariants.
Weak parities deﬁned by V.O. Manturov give another description of functorial
maps. Among weak parities there is a distinguished one — the maximal nontrivial
weak parity. In the talk we describe the maximal nontrivial weak parity for knots
in a given surface and show that all the weak parities (and functorial maps) on
the classical knots are trivial.
References
[1] V. O. Manturov, On free knots, arXiv:0901.2214.
[2] V. O. Manturov, A Functorial Map from Knots in Thickened Surfaces to Classical Knots
and Generalisations of Parity, arXiv:1011.4640.
[3] D. Ilyutko, V. O. Manturov, I. Nikonov, Virtual Knot Invariants arising from Parities,
arXiv:1102.5081.
52
Oberwolfach Report 28/2012
