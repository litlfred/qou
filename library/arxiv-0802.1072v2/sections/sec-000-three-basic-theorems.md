---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-000-three-basic-theorems
section_title: "Three basic theorems"
section_number: null
pages: 1-3
source_pdf: 0802.1072v2 (1).pdf
source_sha256: 6f4d93f0b7ba5cd7
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
In this section we present the basic lemmas and theorems abou t links that are closed three-braids.
Initially, we will use the classical presentation for the br aid group B3:
< σ 1, σ2; σ1σ2σ1 = σ2σ1σ2 > (1)
∗ this article is an expanded version of the preprint “A note on transversal knots which are closed 3-braids”, arXiv
math/0703669.
† partially supported by the US National Science Foundation G rant DMS 0405586.
‡ partially supported by the US National Science Foundation G rant DMS 0306062
1
In the presentation (1) the generator σi is a positive interchange of strands i and i + 1, where i = 1
or 2.
Before we can state our ﬁrst theorem, we need a deﬁnition. Let L be a closed 3-braid, with
representative L∈ B3. Then:
• Lis said to admit a ﬂype if the conjugacy class of L has a representative which is in one of the
special forms illustrated in each of the four sketches in Fig ure 1. In particular its associated
(open) braids are conjugate to:
L = σu
1 σv
2σw
1 σǫ
2, for some u, v, w, ǫ∈ N, ǫ =±1. (2)
• A ﬂype is positive or negative, according as ǫ is +1 or −1.
• A ﬂype is non-degenerate when the braids L = σu
1 σv
2σw
1 σǫ
2 and L′ = σw
1 σv
2σu
1 σǫ
2 are in distinct
conjugacy classes. We are interested only in non-degenerat e ﬂypes.
A
u
w
v
--
crossings 
crossings 
crossings 
crossings 
crossings 
crossings 
A
+ +
positive flype template negative flype template 
crossings 
crossings 
crossings 
crossings 
crossings 
crossings 
u
w
v
u
w
v
u
w
v
Figure 1: Positive and Negative 3-braid ﬂypes
Theorem 1. The classiﬁcation theorem [5]: LetL be a link type which is represented by the
closure of a 3-braid L. Then one of the following holds:
(1)L has braid index 3 and every 3-braid which represents L is conjugate to L.
(2)L has braid index 3, and is represented by exactly two distinct conjugacy classes of closed
3-braids. This happens if and only if the conjugacy class of L contains a braid which admits
a non-degenerate ﬂype.
(3) The braid L is conjugate to σk
1 σ±1
2 for some k∈ N. These are precisely the links which are
deﬁned by closed 3-braids, but have braid index less than 3.
Remark: It is immediately clear that in order to use Theorem 1, the rea der will need deﬁnitive
tests for deciding when two 3-braids are conjugate, and when a conjugacy class admits a non-
degenerate ﬂype, and when a conjugacy class contains σk
1 σ±1
2 for some k. These matters will be
discussed in§2 below.
LetK be a knot. The standard knot tables classify unoriented knots. A sharper classiﬁcation
assumes that we ﬁx an orientation on both S3 and on a representative − →K . Let ← −K denote− →K with
2
its orientation reversed. We then deﬁne K to be invertible if there is an orientation-preserving
homeomorphism h of S3 such that h(− →K ) is smoothly isotopic to ← −K . Our second classiﬁcation
theorem treats the question of when an oriented link of braid index 3 fails to be invertible. As was
mentioned earlier, this is an interesting issue, because at this writing there is no eﬀective test that
recognizes whether an arbitrary link is or is not invertible . Using the standard presentation (1)
for B3, we note that if − →K is deﬁned by a cyclic word in the standard generators, then ← −K will be
deﬁned by the same cyclic word, read backwards.
Theorem 2. The invertibility theorem [5]: LetK be a link of braid index 3 with oriented 3-
braid representative− →K . Then K is non-invertible if and only if − →K and← −K are in distinct conjugacy
classes, and the class of − →K does not contain a representative which admits a non-degene rate ﬂype.
Proof: If− →K admits a non-degenerate ﬂype, then the isotopy of S3 which realizes the ﬂype takes− →K→← −K , so that K is invertible. If − →K does not admit a non-degenerate ﬂype, then by Theorem 1
the class of − →K is the only class that represents the oriented link K. The assertion follows. ‖
A knot is said to be transversal if it is everywhere transverse to the standard contact struc ture in
R3. A transversal knot type is the equivalence class of a transversal knot, under isotop ies which are
restricted so that every intermediate representative is tr ansversal. Our third classiﬁcation theorem
relates to transversal knot types that are closed 3-braids. It uses Theorem 1 and is related to
Theorem 2, however in Theorem 3 below we are interested expli citly in the conjugacy classes which
admit a non-degenerate negative ﬂype and do not at the same ti me admit a positive ﬂype, because
a positive ﬂype can be realized by a transversal isotopy. Rec all that a transversal knot type is
transversally simple if it is determined completely by its topological link type a nd its Bennequin
invariant.
Theorem 3. The transversal classiﬁcation theorem [6]: LetTK be a transversal knot type
which is represented by a closed 3-braid K1 = σu
1 σv
2σw
1 σ−1
2 . Assume that K1 does not also admit
a positive ﬂype. Then the braids K1 and K2 = σw
1 σv
2σu
1 σ−1
2 close to distinct transversal knot types
TK 1,TK 2 that are topologically invertible but are not transversall y invertible. In particular, TK 1
andTK 2 are not transversally simple.
