---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-006-a-riesz-representation-theorem
section_title: "Riesz Representation Theorem"
section_number: A
pages: 3-4
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
We can now introduce the following theorem in order to
guarantee the existence of a reproducing kernel for any given
QRKHS.
Theorem 1 (Quaternion Riesz Representation Theorem):
For every bounded linear functional L
deﬁned over a
quaternion left Hilbert space H, there exists a unique element
g ∈H such that L( f ) = ⟨f, g⟩, ∀f ∈H.
Proof: The proof follows from [10, Th. 6.2.4] and the
properties of the inner product in quaternion left Hilbert spaces
stated in Deﬁnition 1.
Denote by A = { f ∈H : L( f ) = 0} the null space of L.
By continuity2 of L, A is a closed linear subspace of H. If A =
H, then L = 0 and L( f ) = ⟨f, 0⟩. If A̸ = H, then there exists
at least one element g0 ∈H, such that g0̸ = 0 and g0 ∈A⊥
[10, Corollary 6.2.3]. By deﬁnition of g0, L(g0)̸ = 0, and for
1We considered the quaternion norm ∥q∥= √q∗q and the Lebesgue
measure dx in Hn deﬁned in analogy to the Lebesgue measure in R4n (for
instance for n = 1, dx = dxr dxidx j dxk).
2A bounded linear operator between normed spaces is always continuous,
see [10, Th. 4.4.2].
any f ∈H the element f −L( f )
	
L(g0)

−1g0 ∈A. As a
consequence,

f −L( f )
	
L(g0)

−1g0, g0

= 0.
Applying the properties of the inner product space we have
L( f )
	
L(g0)

−1 ⟨g0, g0⟩= ⟨f, g0⟩,
then, replacing ⟨g0, g0⟩= ∥g0∥2 and right-multiplying both
sides by L(g0)
∥g0∥2 yields
L( f ) = ⟨f, g0⟩L(g0)
∥g0∥2 .
(4)
Now, by denoting g = L∗(g0)g0/ ∥g0∥2 we arrive at the
desired L( f ) = ⟨f, g⟩.
To prove uniqueness, assume g1, g2 ∈H such that L( f ) =
⟨f, g1⟩= ⟨f, g2⟩. Therefore, ⟨f, g1 −g2⟩= 0 for all f ∈H;
in particular, by taking f = g1 −g2 we have ∥g1 −g2∥2 =
0 ⇒g1 = g2.
□
Remark 5: Observe that the right-multiplication by L(g0)
∥g0∥2 ,
which yields Eq. (4), holds the key to differentiate the proof
for Thm. 1 from that of the complex and real cases. Due to the
non-commutative property of the quaternion ring, the element
g = L∗(g0)g0/ ∥g0∥2 is different from ¯g = g0L∗(g0)/ ∥g0∥2,
which is used in the proof for the real/complex cases in
[10, Theorem 6.2.4].
Corollary 1 (Reproducing Property): For any f ∈H, there
exists a unique element Kx ∈H such that the evaluation map
Lx = f (x) in (3) can be expressed as Lx = ⟨f, Kx⟩.
Proof: As Lx is itself a bounded linear operator, based on
the quaternion Riesz representation theorem there exists an
element g ∈H such that Lx( f ) = ⟨f, g⟩. The element g =
g(x) is unique for a given functional Lx, or equivalently, for
a given x ∈X. Therefore, we can deﬁne Kx ≜g and write
Lx = ⟨f, Kx⟩.
□
Since Kx(·) ∈H, it can be evaluated for any y ∈X. This
allows us to deﬁne
K : X × X −→H
(x, y) −→K(x, y) = Kx(y),
whereby the function K is referred to as the reproducing kernel
of the QRKHS H. Its existence and uniqueness properties are
a direct consequence of the quaternion Riesz representation
theorem (Theorem 1). Similarly to the standard real- and
complex-valued cases, the reproducing property of K can be
expressed as
∀f ∈H and x ∈X, f (x) = ⟨f, Kx⟩.
The following relationships are readily obtained by applying
the reproducing property on the functions Kx = K(x, ·) ∈H
and Ky = K(y, ·) ∈H:
• K(x, y) =

Kx, Ky

=

Ky, Kx

∗= K ∗(x, y).
• K(x, x) = ⟨Kx, Kx⟩= ∥Kx∥2 ≥0.
• Kx = 0 ⇐⇒f (x) = ⟨f, Kx⟩= 0, ∀f ∈H.
We have therefore shown, through the quaternion Riesz
representation theorem, that for an arbitrary QRKHS there
exists a unique reproducing kernel. This makes it possible to
compute inner products in a quaternion-valued feature space
using the kernel trick.
Observe that although Theorem 1 gives theoretical support
for quaternion kernel estimation, it is far from being useful
in practice on its own, since the design of a QRKHS suited
for a speciﬁc task can be rather difﬁcult. To this end, we next
complement the Riesz representation theorem with the Moore-
Aronszajn theorem, in order to show that any quaternion kernel
(within a certain class of kernels) generates a unique QRKHS.
