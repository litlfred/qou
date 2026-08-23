---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-012-32-proof-of-the-key-lemma-let-n-be-a-noodle-and
section_title: "Proof of the Key Lemma. Let N be a noodle and let F be a fork. By"
section_number: 3.2
pages: 8-9
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
applying a preliminary isotopy, we can assume that T (F ) intersects N transversely
at a ﬁnite number of points, which we label z1, . . . , zl. Further, we can assume that
l is the minimal possible number of points of intersection. Let F ′ be a parallel copy
of F . Choose F ′ so that and T (F ′) intersects N transversely at z′
1, . . . , z′
l, where zi
and z′
i are joined by a short arc in N which meets no other zj or z′
j.
If l = 0 then clearly ⟨N, F ⟩ = 0. We now assume l > 0 and show that ⟨N, F ⟩ ⁄= 0.
We use the following lexicographic ordering on the set of monomials qatb.
Deﬁnition 3.4. We say qatb ≤ qa′
tb′
if and only if either
• a < a ′, or
• a = a′ and b ≤ b′.
For i, j ∈ { 1, . . . , l} we say that mi,j is maximal if mi,j ≥ mi′,j ′ for all i′, j′ ∈
{1, . . . , l}.
Claim 3.5. If mi,j is maximal then mi,i = mj,j = mi,j .
Proof. Suppose mi,j is maximal. Then ai,j is maximal among all the integers ak,l .
By Claim 3.2 it follows that ai and aj are maximal among all the integers ak. Thus
ai,i = aj,j = ai,j .
We now show that bi,i = bi,j . Suppose not. Then bi,i < b i,j . Let α be an
embedded arc from z′
i to z′
j along T (F ′). Let β be an embedded arc from z′
j to z′
i
along N .
If β does not pass through the point zi, let δ = αβ and let w be the winding
number of δ around zi. Then bi,j − bi,i = 2w.
If β does pass through zi, ﬁrst modify β in a small neighborhood of zi so that
zi lies to its left. Next let δ = αβ and let w be the winding number of δ around zi.
Then bi,j − bi,i = 2w − 1.
In either case, w is greater than zero.
Let D1 = D \ {zi}. Let ˜D1 be the universal cover of D1. Let ˜α be a lift of α to
˜D1. Let ˜β be the lift of β to ˜D1 which starts at ˜α(1). Let ˜γ be an embedded arc
in ˜D1 from ˜β(1) to ˜α(0) which intersects ˜α and ˜β only at its endpoints. Let γ be
the projection of ˜γ to D1. Choose ˜γ so that γ does not wind around any puncture
points.
Let ˜z′
k be the ﬁrst point on ˜α which intersects ˜β (possibly ˜α(1)). This lies in the
ﬁber over z′
k for some k = 1, . . . , l. Let ˜α′ be the initial segment of ˜ α ending at ˜z′
k.
Let ˜β′ be the ﬁnal segment of ˜β starting at ˜z′
k. Let ˜δ′ = ˜α′ ˜β′˜γ.
Now ˜δ′ is a simple closed curve in ˜D1, so by the Jordan curve theorem it must
bound a disc ˜B. Since γ passes clockwise around zi, there is a non-compact region
to the right of ˜δ′, so ˜δ′ must pass counterclockwise around ˜B.
Let δ′ be the projection of ˜δ′ to D. Then ak − ai is equal to the sum of the
winding numbers of δ′ around each of the points in P . This is equal to the number
of points in ˜B which are lifts of a point on P . This must be greater than zero, since
BRAID GROUPS ARE LINEAR 9
d1 d2
Figure 3. The edge E1 and the noodle N4
otherwise we could isotope T (F ′) so as to have fewer points of intersection with N .
Thus ak − ai is greater than zero, contradicting the fact that ai is maximal among
all integers ai′ . Therefore our assumption that bi,j > b i,i must have been false, so
bi,j = bi,i .
The proof that bi,j = bj,j is similar. This completes the proof of the claim.
This claim, together with the formula for ǫi,j given in Claim 3.3, implies that if
mi,j is maximal then ǫi,j = −mi,j |(q = 1 , t = −1). Thus all maximal monomials
occur with the same sign in equation (8). Therefore ⟨N, F ⟩ cannot equal zero. This
completes the proof of the Key Lemma.
