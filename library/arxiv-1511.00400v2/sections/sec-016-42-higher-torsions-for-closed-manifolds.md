---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-016-42-higher-torsions-for-closed-manifolds
section_title: "Higher torsions for closed manifolds"
section_number: 4.2
pages: 27-29
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
From Theorem 4.2, we can deﬁne torsions.
Deﬁnition 4.3. Let M 3 be a closed oriented hyperbolic three-manifold, with
spin structure σ, and let ̺k1,k2
σ = Symk1,k2 ○̺σ be as in (25).
For k1 ≠k2, deﬁne
τ k1,k2 (M 3, σ) ∶= tor(M 3, ̺k1,k2
σ ) ∈C∗/slash.l⟩ft±1 , (26)
and for k ≥1
τ k(M 3, σ) ∶= τ k,0(M 3, σ) = tor(M 3, ̺k
σ). (27)
When k = 1 one obtains the torsion of Deﬁnition 3.4:
τ 1(M 3, σ) = τ 1,0(M 3, σ) = τ (M 3, σ).
Remark 4.4. 1. For k1 or k2 odd, there is no sign indeterminacy as it is a
representation in C(k1+1)(k2+1), which is even dimensional (Remark 2.7).
2. For k1 + k2 even, Sym k1 ⊗
Symk2 factors through PSL 2(C), hence it does
not depend on the spin structure. In addition, the sign indetermina cy
can be avoided by using Turaev’s reﬁned torsion and an orientation in
homology, provided by Poincar´ e duality [96, 97].
3. By construction, τ k1,k2 (M 3, σ) =
τ k2,k1(M 3, σ).
4. When k1 = k2, ̺k,k may be not acyclic (for instance when it contains a
totally geodesic surface [64]), but sometimes it can be acyclic (e.g. a lmost
all Dehn ﬁllings on two bridge knots for k = 1 by [45, 88, 28] or on the
ﬁgure eight knot for k = 2 by [42]). When ̺k,k is acyclic, then τ k,k(M 3, σ)
is also well deﬁned.
27
5. Changing the orientation. Let M 3 and M
3
denote the same manifold
with opposite orientations and let σ and σ denote the corresponding spin
structures as in Proposition 3.1. Then
τ k1,k2(M
3
, σ) = (−1)b1(M 3)(k1+k2) τ k1,k2 (M 3, σ).
where b1(M 3) denotes the ﬁrst Betti number. Hence if M 3 is amphicher-
ical, then τ k1,k2(M 3, σ) is real for b1(M 3)(k1 + k2) even and purely imag-
inary for b1(M 3)(k1 + k2) odd.
In [72] W. M¨ uller found a beautiful theorem about the asymptotic b ehavior
when k → ∞:
Theorem 4.5 ([72]). Let M be a compact, oriented, hyperbolic 3 manifold with
a spin structure σ. Then
lim
k→∞
log /divid⟩s.alt0τ k(M 3, σ)/divid⟩s.alt0
k2 = 1
4π vol(M 3) . (28)
In particular, the volume can be computed from the sequence o f torsions.
Again, with our convention our torsion is the inverse of the usual an alytic
torsion, so Equation (28) has opposite sign to [72].
As noticed in [72], this theorem implies that there are ﬁnitely many manif olds
with the same sequence of torsions.
Question 4.6. Is there a ﬁnite collection of integers 0 < k1 < ⋯ < kn such that
there are ﬁnitely many manifolds with the same k1, . . . , kn-torsions?
The answer is yes under the extra hypothesis that the volume is bou nded
above. More precisely, an inﬁnite sequence of manifolds with bounde d volume
accumulates (for the geometric topology) to a ﬁnite set of cusped manifolds with
ﬁnite volume, this is Jørgensen-Thurston properness of the volum e function [92,
93]. For such a sequence of manifolds M 3
n, τ 2(M 3
n, σ) → ∞, by Corollary 4.25,
see also [82, Corollaire 4.18].
A priory, for some N ∈N there could exists an inﬁnite sequence of hyperbolic
manifolds whose volume goes to inﬁnity and with the same k-torsions for k ≤N .
By Theorem 3.7 the injectivity radius of this sequence would not conv erge to
inﬁnity.
M¨ uller proves Theorem 4.5 using analytic torsion and Ruelle zeta func tions.
There is ﬁrst a theorem of Wotzke [104] that generalizes Fried’s the orem (Theo-
rem 2.28) and from this he obtains a functional equation that relate s the volume,
the Ruelle zeta functions and the torsions. Theorem 4.5 has been ge neralized
by M¨ uller and Pfaﬀ [74] by working directly on the trace of the heat k ernel in
(12).
Theorem 4.7 ([74]). Let M 3 be a compact, oriented, hyperbolic 3-manifold
with a spin structure σ. Then
lim
k1→∞
log /divid⟩s.alt0τ k1,k2(M 3, σ)/divid⟩s.alt0
k2
1
= 1
4π (k2 + 1) vol(M 3) . (29)
Again, the sign convention here diﬀers from [74].
28
