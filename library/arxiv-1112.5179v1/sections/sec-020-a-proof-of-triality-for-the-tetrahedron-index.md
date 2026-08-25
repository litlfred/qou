---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-020-a-proof-of-triality-for-the-tetrahedron-index
section_title: "A Proof of triality for the tetrahedron index"
section_number: null
pages: 68-70
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
We would like to prove that the index is invariant under the aﬃne σeST transformation
discussed in Section 3.2. We will prove it in the form
I∆(m,e ;q) =
(
−q
1
2
)mI∆(−e−m,m ;q), (A.1)
which immediately implies the middle equality of (3.11) as well.
There are several possible ways to show this, but one of the easiest (and most instructive)
is to invoke the diﬀerence equations for the index. Recall from Section 3.3 that
(ˆp+ + ˆx−1
+ − 1)I∆(m,e ) = (ˆp− + ˆx−1
− − 1)I∆(m,e ) = 0, (A.2)
where ˆp±, ˆx± are deﬁned by
ˆx± =q
m
2e∓∂e, ˆp± =q
e
2e±∂m. (A.3)
The validity of (A.2) is trivial to show in a fugacity basis, using formula (3.3), and the fugacity-
basis operators (2.32). We claim that the equations (A.2) determine the index completely as
long as two of its values are ﬁxed, on either the m ore axis (and also assuming thatI∆(m,e )
is a formal series in q
1
2 for every (m,e )).
To see this, ﬁrst suppose that we knewI∆(m,e ) everywhere on (say) them-axis, ate = 0.
Then the equations (A.2) involve a single shift in e, in opposite directions, so they can be
used to solve for I∆(m,e ) everywhere else. To get I∆(m,e ) on the m-axis, we can rewrite
the operators ˆx±, ˆp± in terms of the rotated operators
ˆη =e∂e, ˆϵ =qe ; ˆ ηm =e∂m, ˆϵm =qm. (A.4)
Then, essentially by using elimination in a left ideal, we can eliminate the electric shiftη from
(A.2), and ﬁnd a single equation only involving ˆϵ, ˆϵm, ˆηm. At e = 0 (ˆϵ = 1), it reads
(
ˆηm + ˆη−1
m + ˆϵ−1
m − 2
)
I∆(m, 0) = 0, (A.5)
– 67 –
or
I∆(m + 1, 0) +I∆(m− 1, 0) + (q−m− 2)I∆(m, 0) = 0. (A.6)
This is a second-order diﬀerence equation in m, whose coeﬃcients are nowhere vanishing.
Therefore, knowing I∆(m, 0) at two values of m is suﬃcient for ﬁnding a unique solution
along the entire m-axis. (A similar story holds for the e-axis, but we will not need it.)
Now, let’s deﬁne I′(m′,e′)≡
(
−q
1
2
)m′
I∆(−e′−m′,m′;q) =I(σeST )−1◦T∆(m′,e′). The
diﬀerence equations thatI′(m′,e′) obeys are the aﬃne-symplectic (σeST )−1–images of (A.2).
For example, from the inverse of (3.20), we ﬁnd that we should send
ˆx±→− 1
ˆp′
±
1
ˆx′
±
, ˆp±→ ˆx±, (A.7)
so that the operators annihilating I′(m′,e′) are
ˆp± + ˆx±− 1 → ˆx′
±− ˆx′
±ˆp′
±− 1 =−ˆx′
±(ˆp′
± + ˆx′
±
−1− 1). (A.8)
Therefore, since ˆx′
± is invertible, the transformed index I′(m′,e′) satisﬁed exactly the same
diﬀerence equations, in the new variables:
(ˆp′
+ + ˆx′
+
−1− 1)I′(m′,e′) = (ˆp′
− + ˆx′
−
−1− 1)I′(m′,e′) = 0. (A.9)
Then, to prove (A.1), it suﬃces to show that I′(m′,e′) = I∆(m′,e′) at two points on the
m′-axis.
It is trivial that I′(0, 0) = I∆(0, 0). For our second point, we take ( m′,e′) = (−1, 0),
and need to show thatI′(−1, 0)≡−q− 1
2I∆(1,−1) =I∆(−1, 0). But this follows from parity
symmetry (3.9) of the tetrahedron index! So we are done.
For completeness, since we never proved parity explicitly in the text, let us do so here.
In an electric fugacity basis, parity symmetry takes the form
I∆(m;ζ,q ) =
(
−q
1
2
)mζ−mI∆(−m;ζ,q ). (A.10)
Using formula (3.3) for the tetrahedron index, we then check
I∆(−m,ζ )
I∆(m,ζ ) =
∞∏
r=0
1−qr+m
2 +1ζ−1
1−qr+m
2ζ
1−qr−m
2ζ
1−qr−m
2 +1ζ−1
=



∏m−1
r=0
1−qr−m
2 ζ
1−qr−m
2 +1ζ−1 m≥ 0
∏|m|−1
r=0
1−qr+m
2−1ζ−1
1−qr+m
2 ζ
m< 0
=
(
−q
1
2
)−mζm,
by straightforward algebra, exactly as desired.
– 68 –
