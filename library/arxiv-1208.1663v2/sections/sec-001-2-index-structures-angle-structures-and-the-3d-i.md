---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-001-2-index-structures-angle-structures-and-the-3d-i
section_title: "Index structures, angle structures and the 3D index"
section_number: 2
pages: 3-5
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
2.1. Index structures. Consider two r×s matrices A and B with integer entries and a
column vector v∈ Zr, and let M = (A|B|v).
Deﬁnition 2.1. (a) We say that M supports an index structure if the rank of ( A|B) is r
and for every Q :{1,...,s }→{ 1, 2, 3} there exists (α,β,γ )∈ Q3s that satisﬁes
(2.1) Aα + Bγ =ν, α +β +γ = (1,..., 1)T
and Q(α,β,γ ) > 0. The latter means that for every i = 1,...,s the following inequalities
are satisﬁed:
(2.2)



αi > 0 if Q(i) = 1
βi > 0 if Q(i) = 2
γi > 0 if Q(i) = 3
(b) We say that M supports a strict index structure if the rank of (A|B) isr and there exists
(α,β,γ )∈ Q3s
+ that satisﬁes (2.1), where Q+ is the set of positive rational numbers.
It is easy to see that if M supports a strict index structure, then it supports an index
structure, but not conversely. As we will see in Section 2.2, ideal triangulations T give rise
to matrices M, and a strict index structure on M is a strict angle structure on T . On the
other hand, index structures are new and motivated by Theorem 2.4 below.
The next deﬁnition discusses two actions on M: an action of GL( r, Z) on the left which
allows for row operations on M, and a cyclic action of order three at the pair of the ith
columns of (A|B).
4 STA VROS GAROUF ALIDIS
Deﬁnition 2.2. (a) There is a left action of GL( r, Z) on M, deﬁned by
P∈ GL(r, Z) M = (A|B|v) PM = (PA|PB|Pv )
An index structure on M is also an index structure on PM.
(b) There is a left action of ( Z/3)s on M acting on the ith columns (ai|bi) of ( A|B) (and
ﬁxing all other columns) given by
(2.3) ( ai|bi|v)
S
↦→ (−bi|ai−bi|v−bi),
where
(2.4) S(a|b|v) = (−b|a−b|v−b)
satisﬁes S3 = Id. We extend S to act on an index structure ( α,β,γ ) of M by
(2.5) ( αi,βi,γi)
S
↦→ (βi,γi,αi)
and ﬁxing all other coordinates of ( α,β,γ ). It is easy to see that if ( α,β,γ ) is an index
structure on M and S∈ (Z/3)s, then S(α,β,γ ) is an index structure of SM.
Deﬁnition 2.3. Given M, and m = (m1,...,m s),e = (e1,...,e s)∈ Zs consider the sum
(2.6) IM(m,e )(q) =
∑
k∈Zr
q
1
2v·k
s∏
i=1
I∆(mi−bi·k,ei +ai·k)
Theorem 2.4. IM(m,e )(q)∈ Z((q1/2)) is convergent for all m,e ∈ Zs if and only if M
supports an index structure. In that case, IM is q-holonomic in the variables (m,e ).
Remark 2.5. q-holonomicity in Theorem 2.4 follows immediately from [27]. Convergence
is the main diﬃculty.
Remark 2.6. By deﬁnition, IM is a generalized Nahm sum in the sense of [10], where the
summation is over a lattice.
Corollary 2.7. Applying Theorem 2.4 to the case r = 1, s = 3, M = ( A|B|v) =
(1 1 1|0 0 0|2) and the strict index structure 2 = 2
3· 1 + 2
3· 1 + 2
3· 1, it follows that the
right hand side of the pentagon identity (3.5) is convergent in Z((q1/2)).
The next remark discusses the invariance of the index under the actions of Deﬁnition 2.2.
Remark 2.8. Fix M that supports an index structure. Then, for P ∈ GL(r, Z) and S∈
(Z/3)s, it follows thatPM andSM also supports an index structure. In that case, Theorem
2.4 implies that IM, IP M and ISM are all convergent. We claim that
IP M =IM, I SM =IM.
The ﬁrst equality follows by changing variablesk↦→Pk in the deﬁnition ofIM given by (2.6).
The second equality follows from the fact that the tetrahedron index I∆ satisﬁes Equation
(3.2); this is shown in part (a) of Theorem 3.7.
The next corollary follows easily from Theorem 2.4 and the deﬁnition of an index structure
on (A|0|v0).
