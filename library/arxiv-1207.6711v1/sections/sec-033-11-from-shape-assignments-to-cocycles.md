---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-033-11-from-shape-assignments-to-cocycles
section_title: "From shape assignments to cocycles"
section_number: 11
pages: 39-41
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
We now prove that the bottom row of diagram (1.5) consists of one-one correspondences.
The idea is to ﬁrst prove that a shape assignment determines a natural cocycle on each
doubly truncated simplex. This is a consequence of the internal gluing equations. The face
and edge equations imply that the cocycles glue together to a cocycle on M; the middle
edges glue together because of the face equations, and the edge equations imply that we can
ﬁll in the prisms.
Lemma 11.1. If two shape assignments z and w agree on two faces i and j, then z = w,
i.e. ifze
s =we
s whenei =si = 0 orej =sj = 0, thenze
s =we
s for all (s,e )∈ ∆3
n−2(Z)× ˙∆3
2(Z).
40 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Proof. We may assume that z and w agree on face 2 and 3. It is enough to prove that
z1100
s = w1100
s for all s = (s0,s 1,s 2,s 3)∈ ∆3
n−2(Z). By assumption, this holds if either s2
or s3 is 0. Suppose by induction that z1100
s = w1100
s for all s with s2 +s3 < k, and let
s∈ ∆3
n−2(Z) be a subsimplex with s2 +s3 =k. Since the result holds, when either s2 ors3 is
0, we may assume that s =α + 0011, withα∈ ∆3
n−4(Z). Let t =s + 1100. By Lemma 6.10,
z and w satisfy the internal gluing equations, i.e. we have
(11.1)
z0011
α+1100z0101
α+1010z0110
α+1001z1001
α+0110z1010
α+0101z1100
s =w0011
α+1100w0101
α+1010w0110
α+1001w1001
α+0110w1010
α+0101w1100
s ,
which equals 1. Note that for all terms except z1100
s and w1100
s , the lower index satisﬁes
s2 +s3 <k . By induction, each term z1111−I
α+I equalsw1111−I
α+I . Hence z1100
s =w1100
s , completing
the induction. □
Lemma 11.2. The factorization of the middle edges is unique, i.e. if
(11.2)
n−1∏
k=1
(n−k∏
i=1
xi(1)
n−k−1∏
i=1
Hi(ak,i)
)
=
n−1∏
k=1
(n−k∏
i=1
xi(1)
n−k−1∏
i=1
Hi(bk,i)
)
,
then ak,i =bk,i for all k,i .
Proof. Suppose (11.2) holds. In particular, all diagonal entries are equal. Hence, as in
Remark 10.17, the equality ∏n−2
i=l
∏n−1−i
k=1 ak,i =∏n−2
i=l
∏n−1−i
k=1 bk,i holds for all l = 1,...,n .
The result now follows by induction. □
Proposition 11.3. The map Z from generic decorations on ∆ 3
n to shape assignments on
∆3
n is surjective.
Proof. Let z be a shape assignment. We wish to construct a decoration D withZ(D) = z.
Let D = (B,q 1B,β 012q1B,γ 012β013q1B) and let z′ =Z(D). By Lemma 11.1, it is enough
to prove that z′ agrees with z on face 2 and 3. We prove this for face 3 ( s3 = 0), face 2
being similar. We use induction on s2. Let β′ and γ′ denote the labelings of the natural
cocycle of D. Let Xt and X′
t denote the X coordinates of z and z′. Note that β′
012 = β012
and γ′
012 = γ012. Since γ′
012 = γ012, the equality z1100
s = w1100
s holds for s2 = 0 proving the
induction start. Since β′
012 =β012, it follows from Lemma 11.2 that Xt =X′
t for all t on face
2 and 3. Now suppose by induction that z1100
s = w1100
s holds for s2 < k. Let t = s + 1100.
We have
(11.3) −z1100
s z1010
t−1010z0110
t−0110 =Xt =X′
t =−z′1100
s z′1010
t−1010z′0110
t−0110.
By induction, z1010
t−1010 = z′1010
t−1010 and z0110
t−0110 = z′0110
t−0110, so we must also have z1100
s = z′1100
s .
This proves the result. □
Theorem 11.4. The bottom row of diagram (1.5) consists of one-one correspondences.
Proof. We ﬁrst prove this for a simplex. The map Lαβγ is bijective by Remark 9.14. In-
jectivity ofZ follows from Theorem 10.14, and surjectivity was proved in Proposition 11.3.
Now supposez is a shape assignment on (M,T ). We must prove thatz determines a generic
decoration, or equivalently a natural cocycle. By Proposition 11.3 z determines a natural
cocycle on each doubly truncated simplex. We must prove that these ﬁt together to form
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 41
a cocycle on M. The labelings of long edges obviously match up, and by (10.22) and Re-
mark 10.10, the middle edges match up if and only if the face equations are satisﬁed. Now
all that is left to prove is that the induced labeling on the prisms are cocycles. This is a
direct consequence of the edge equations. □
Remark 11.5. It follows from Theorem 11.4 that (10.22) gives an explicit map from shape
assignments to cocycles. Combined with Remark 9.14 this gives explicit inverses of Z and
Lαβγ. Similarly, we have explicit inverses of C andLαβ via (10.4).
