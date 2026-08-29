---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-007-33-the-ﬁrst-polyanalytic-bergman-metric-we-conti
section_title: "The ﬁrst polyanalytic Bergman metric. We continue the setting of the preceding subsec-"
section_number: 3.3
pages: 5-6
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
tion. Following in the footsteps of Bergman (see Subsection 3.1), we would like to introduce
polyanalytic analogues of Bergman’s ﬁrst and second metrics, respectively. Let us ﬁrst discuss
a property of the weighted Bergman kernel K = K1 (with q = 1). The function K(z, w) on Ω× Ω
is uniquely determined by its diagonal restriction K(z, z). This is so because because the diagonal
z = w is a set of uniqueness for functions holomorphic in (z, ¯w). So, if we ﬁx the weight ω, the
ﬁrst and second Bergman metrics both retain all essential properties of the kernel K(z, w) itself.
The same can not be said for the weighted q-analytic Bergman kernel Kq. To remedy this, we
consider the double-diagonal restriction z = w and z′ = w′ in the lifted kernel E⊗2[Kq] instead:
(3.3.1)
E⊗2[Kq](z, z′; z, z′) =
+∞
X
j=1
|E[φj](z, z′)|2,
(z, z′) ∈Ω× C.
If we know just the restriction to the double diagonal z = w and z′ = w′ of E⊗2[Kq] we are able
to recover the full kernel lifted kernel E⊗2[Kq]. If we put z′ = z+ǫ, where ǫ ∈C, we may expand
the extension of φj in a ﬁnite Taylor series:
(3.3.2)
E[φj](z, z + ǫ) =
q−1
X
k=0
1
k!
¯∂k
zφj(z)¯ǫk.
6
ANTTI HAIMI AND HAAKAN HEDENMALM
As we insert (3.3.2) into (3.3.1), the result is
(3.3.3)
E⊗2[Kq](z, z + ǫ; z, z + ǫ) =
q−1
X
k,k′=0
¯ǫkǫk
k!(k′)!
+∞
X
j=1
¯∂k
zφj(z)∂k′
z ¯φj(z),
(z, ǫ) ∈Ω× C.
So, to generalize the ﬁrst Bergman metric we consider the family of (possibly degenerate)
metrics
(3.3.4) ds③
q,ω,ǫ(z)2 := E⊗2[Kq](z, z + ǫ; z, z + ǫ)ω(z)|dz|2 =
q−1
X
k,k′=0
¯ǫkǫk′
k!(k′)!
+∞
X
j=1
¯∂k
zφj(z)∂k′
z ¯φj(z)ω(z)|dz|2,
indexed by ǫ ∈C. We observe that in (3.3.4) we may think of (ǫ0, . . ., ǫq−1) as a general vector
in Cq, by forgetting about the interpretation of the superscript as a power, and (3.3.4) still
deﬁnes a (possibly degenerate) metric indexed by the Cq-vector (ǫ0, . . ., ǫq−1); this should have
an interpretation in terms of jet manifolds. In other words, the q × q matrix
(3.3.5)
ω(z)


E⊗2[Kq](z, z; z, z)
· · ·
1
(q−1)!∂q−1
z′ E⊗2[Kq](z, z′; z, z′)

z′:=z
...
...
...
1
(q−1)! ¯∂q−1
z′ E⊗2[Kq](z, z′; z, z′)

z′:=z
· · ·
1
(q−1)!(q−1)! ¯∂q−1
z′ ∂q−1
z′ E⊗2[Kq](z, z′; z, z′)

z′:=z


,
which depends on z ∈Ω, is positive semi-deﬁnite.
