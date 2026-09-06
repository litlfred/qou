---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-002-4-extending-cocycles-on-genus-0-surfaces
section_title: "Extending cocycles on genus 0 surfaces"
section_number: 4
pages: 9-12
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
Let us deﬁne a punctured topological polyhedron which we will use as model for a “ver-
tex link” of ˆT when removing some prisms.
Deﬁnition 4.1. Let L be a topological polyhedron, i.e., a decomposition of an oriented
2-sphere into polygons. LetP1,. .. ,Pp be selected two-cells ofL such that ∂Pi ∩∂P j ⁄= ;
for all i ⁄= j . We call (L,L \ ⋃Pl ) a punctured topological polyhedron.
The complex L \ ⋃Pl will often be equipped with the following kind of cocycle.
Deﬁnition 4.2. Let X be a surface with boundary and with a decomposition into poly-
gons. A (SO3, SO2)-cocycle on X is a SO3-cocycle where edges in the boundary ∂X are
labeled by rotations Rω ∈ Im(SO2 ,→ SO3) about the z-axis.
10
The goal of this section is to give a criterion when such a cocycle onL \ ⋃Pl extends to a
SO3-cocycle on L.
Deﬁnition 4.3. Let X be a 2-complex. An edge-loop Γ is a word in the oriented edges
of X such that the end of one edge coincides with start of the next edge (when reading
the word from right to left and cyclically).
Note that by parametrizing the oriented edges ofX and concatenating them in the order
given by Γ, we obtain a geometric realization of Γ that is a (based) topological loop in
X . Also note that a G -cocycle on X assigns a value in G to an edge-loop Γ obtained by
multiplying the labels of the oriented edges in the respective order. The value assigned
to Γ depends only on the homotopy type of (the geometric realization of) Γ and, in
particular, is trivial if the loop is contractible in X .
Deﬁnition 4.4. Let (L,L \ ⋃Pl ) be a punctured topological polyhedron. A gimbal loop
Γ is a word in the oriented edges of L and the selected two cells P1, .. .,Pp such that
• each P1,. .. ,Pp is contained in Γ exactly once,
• each Pl in Γ is preceeded (when reading the word from right to left and cycli-
cally) by an edge e j such that the endpoint of e j is a vertex of ∂Pl , and
• dropping all P1, .. .,Pp from Γ results in an edge loop. This edge loop bounds
a disk in L \ ⋃Pl . The interior of the disk embeds into L \ ⋃Pl matching the
orientation of L.
Example 4.5. Figure 5 shows an example of a gimbal loopΓ for p = 3. The corresponding
word is e6P2e5e4P1e3e2P3e1.
P1
P2
P3
 
e1
e3
e5
e2
e4
e6
e7
e8
e9
e10
e11
e12
e13
e14
e15
e16
e17
e18
e19
 
P1
P2
P3
 
Figure 5. The edge loop obtained when
dropping the Pl from a gimbal loop Γ.
Figure 6. The edge loop obtained when
replacing Pl by ∂Pl in a gimbal loop Γ.
11
Deﬁnition 4.6. Let (L,L \ ⋃Pl ) be a punctured topological polyhedron and Γ be a
gimbal loop. Fix a (SO3,SO 2)-cocycle on L \ ⋃Pl . Assume we are given numbers
(d1,. .. ,dp). Recall that the cocycle assigns a SO3-matrix to every edge in Γ. Assign
to each Pl in Γ the rotation Rdl ∈ Im(SO2 ,→ SO3). We call the product of the matrices
assigned to the letters in Γ the gimbal matrix mΓ(d1,. .. ,dp). Furthermore, we call the
function
gΓ : Rp → R3, ( d1,. .. ,dp) 7→
(
mΓ(d1, ... ,dp)01,mΓ(d1, ... ,dp)02,mΓ(d1, ... ,dp)12
)
assigning the upper triangular entries of the gimbal matrix the gimbal function.
Recall that a (SO 3,SO 2)-cocycle on L \ ⋃Pl assigns a rotation Rω ∈ Im(SO2 ,→ SO3) to
each edge in∂Pl (with orientation induced from the orientation ofPl ⊂ L) where we pick
ω ∈ (−π, π]. Let δl denote the sum of all the angles ω over the edges of ∂Pl . For example,
δ2 in Figure 5 is the sum of the angles ω associated to the edges e−1
6 ,e19,e18,e17,e16, and
e15.
Lemma 4.7. Using the same setup as in Deﬁnition 4.6, we have gΓ(2π,. .. ,2π) =
gΓ(δ1,. .. ,δp) = (0, 0, 0).
Proof. Assume each dl = 2π. Then each Rdl is the identity and thus can be dropped
from the gimbal matrix mΓ(2π,. .. ,2π). Thus the gimbal matrix is equal to the matrix
the cocycle assigns to the edge loop obtained when dropping the Pi . This edge loop is
contractible. Thus the gimbal matrix is the identity and gΓ(2π, ... ,2π) = (0, 0, 0).
The gimbal loop Γ can also be turned into an edge loop by replacing each Pl in Γ by a
word in the oriented edges in ∂Pl . Here we use the orientation of ∂Pl induced from the
Pl ⊂ L and start traversing ∂Pl at the endpoint of the preceding edge. Figure 6 shows
this edge loop for Example 4.5. The corresponding word is:
e6(e−1
6 e19e18e17e16e15)e5e4(e−1
4 e14e13e12e11)e3e2(e−1
2 e10e9e8e7)e1.
Note that by deﬁnition of δl , the matrix assigned to this edge loop by the cocycle is
equal to the gimbal matrix mΓ(δ1,. .. ,δp). This edge loop is again contractible and thus
gΓ(δ1,. .. ,δp) = (0, 0, 0). To see that the edge loop is contractible, note that a genus 0 sur-
face with p boundary components can be obtained by attaching a 2-cell to a 1-complex
consisting of p loops and p arcs connecting the loops to common base point. The edge
looped can be homotoped into this form since it bounds a disk with interior embedding
into L \ ∪Pl , see Figure 7.
Let Dg Γ : Rp → M(3×p, R) denote the Jacobian ofgΓ and [Dg Γ(K )] be the interval closure
of Dg Γ(K ), i.e., the smallest (axis-aligned) closed box containingDg Γ(K ) when thinking
of the matrix space M(3 × p, R) as R3p. We say that [Dg Γ(K )] is invertible if every matrix
in [Dg Γ(K )] is invertible.
Deﬁnition 4.8. Using the same setup as in Deﬁnition 4.6, let K ⊂ Rp be a box. We say
that K avoids gimbal lock with respect to Γ if [Dg Γ(K )] is invertible.
12
P1
P2
P3
 
Figure 7. Homotoping the edge loop ob-
tained from gimbal loop Γ such that it
bounds a disk.
Figure 8. A gimbal.
Remark 4.9. The term gimbal lock is inspired by the mechanical device called gimbal
or Cardan suspension used to achieve an arbitrary rotation in SO3, see Figure 8. Letting
d1,d2 and d3 denote the Euler angles at the joints from the grounding boxes to the inner-
most ring, the rotation achieved by the gimbal is given by the matrix
(d1,d2,d3) 7→ Rd1
( −1
1
1
)
Rd2
( 1
1
−1
)
Rd3
and a conﬁguration of ( d1,d2,d3) where this map does not have full rank is known as
gimbal lock. Note the formal similarity of this product to the gimbal matrixmΓ(d1, .. .,dp).
The following lemma is not useful in the general setting, but illustrates the principle we
will use later (also see Example 6.1):
Lemma 4.10. Using the same setup as in Deﬁnition 4.6, let K ⊂ Rp be a box avoiding
gimbal lock with respect to Γ such that (2π,. .. ,2π) ∈ K . If (δ1, .. .,δp) ∈ K , then all
δl = 2π and the cocycle extends to L.
Proof. A standard result about the interval Newton method says that gΓ is injective on
K since [Dg Γ(K )] is invertible. Thus, Lemma 4.7 implies that δl = 2π.
