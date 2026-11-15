---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-004-b-quaternion-valued-hilbert-spaces
section_title: "Quaternion-Valued Hilbert Spaces"
section_number: B
pages: 2-3
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
To introduce the concept of quaternion Hilbert space, we
ﬁrst need to deﬁne quaternion vector spaces and their algebraic
properties.
Since (H, +, ·) is a division ring and not a ﬁeld (it lacks the
commutativity property), strictly speaking it is not possible to
construct a general vector space over H; however, we can still
construct a left-module. A module [36], [37] is a generalisation
of vector space which allows for the scalar set to be a ring
(rather than a ﬁeld). We refer to a left-module H over H
as vector space [10] in which the non-commutative scalar
multiplication H × H →H is deﬁned on the left-hand side
by (q, x) →qx.
We next set out to restate the concepts of inner product
and left Hilbert space for quaternions, as these are required to
deﬁne quaternion-valued RKHSs.
Deﬁnition 1 (Quaternion Left Hilbert Space): A nonempty
set H is called a quaternion left Hilbert space if it is a
quaternion left module (i.e. built over H) and there exists
a quaternion-valued function ⟨·, ·⟩: H × H →H with the
following properties:
1) Conjugate symmetry: ⟨x, y⟩= ⟨y, x⟩∗.
2) Linearity: ⟨px + qy, z⟩= p ⟨x, z⟩+ q ⟨y, z⟩.
3) Conjugate linearity: ⟨x, py + qz⟩= ⟨x, y⟩p∗+⟨x, z⟩q∗.
4) ⟨x, x⟩≥0 and ⟨x, x⟩= 0 ⇐⇒x = 0.
5) Completeness: If {xn} ⊂H is a Cauchy sequence, then
x = limn→∞xn ∈H.
We refer to the function ⟨·, ·⟩as inner product and denote
its induced norm by ∥x∥= √⟨x, x⟩.
Observation 1: The space Hn, with the inner product
⟨p, q⟩= pT q∗is a quaternion left Hilbert space.
Observation 2: The space of quaternion-valued square-
integrable functions L2
=
{ f
:
X
∈
Hn
→
H, s.t.

X ∥f (x)∥2 dx
<
∞} with the inner product ⟨f, g⟩
=

X f (x)g∗(x)dx is a quaternion left Hilbert space.1
Standard properties of real and complex Hilbert spaces such
as the Cauchy-Schwarz inequality and the concept of orthog-
onality also extend to quaternion Hilbert spaces. In particular,
we highlight two properties that will be helpful in the next
section:
• The elements x, y ∈H are orthogonal, denoted by x ⊥y,
if and only if ⟨x, y⟩= 0.
• Two sets A, B ∈H are orthogonal if and only if x ⊥y,
∀x ∈A, y ∈B. We denote by A⊥the set of all elements
that are orthogonal to x ∈A.
For the properties of complex Hilbert spaces which also apply
to the introduced left quaternion Hilbert space see [10].
