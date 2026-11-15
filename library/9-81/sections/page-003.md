---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
toc_source: undetermined
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
Proof.
The assertion follows immediately from the deﬁnition of a weight.

Next we will see that the necessary condition above turns out to be a suﬃcient condition, that is, if w satisﬁes the
condition of Lemma 2.1, then S always admits locally Euclidean structures. To see that, we regard the set of the locally
Euclidean structures on S coming from w as the feasible region of a linear program. Furthermore we use the following
theorem, which is known as Duality Theorem of linear programming. See [1] for the proof of Duality Theorem. Also
see [1] or [5] for basic notations of linear programming.
Theorem 2.2 (Duality Theorem).
Let P be a linear program of the form:
minimize cxT; subject to the constraints AxT ¼ aT and x 
 0:
Then the dual program P is the following form:
maximize aT; subject to the constraints A  cT:
The feasible region of P is empty if and only if the objective function of P is not bounded. Conversely, the feasible
region of P is empty if and only if the objective function of P is not bounded. If neither feasible region is empty, then
the values of the objective functions of P and P are equal.
Now we set a linear program corresponding to the locally Euclidean structures on S coming from w. Let l ¼ jFðSÞj
and m ¼ jEðSÞj. Let valðeÞ be the valence of the edge e of S. Consider the following linear program.
Minimize ð0; . . . ; 0Þ  ð1; 1; 	1; . . . ; l; l; 	lÞT, subject to
1. each angle is strictly positive,
2. for each 2-face t, the sum of three angles t þ t þ 	t is equal to ,
3. for each edge e, wðeÞ ¼ PvalðeÞ
i¼1 i where each i is the angle at the vertex which is opposite to e.
At ﬁrst, we loosen the ﬁrst constraint as each angle may be 0, and denote the linear program by P. We can express P
using a matrix as the following.
Minimize ð0; . . . ; 0Þ  ð1; 1; 	1; . . . ; l; l; 	lÞT, subject to
1
1
1
0
0
0
. . .
0
0
0
0
0
0
1
1
1
. . .
0
0
0
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
0
0
0
0
0
0
. . .
1
1
1
0
1
0
0
0
0
. . .
0
0
1
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
..
.
1
0
0
0
1
0
. . .
1
0
0
0
B
B
B
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
C
C
C
A
1
1
	1
...
l
l
	l
0
B
B
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
C
C
A
¼


..
.

wðe1Þ
..
.
wðemÞ
0
B
B
B
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
C
C
C
A
and
1; 1; 	1; . . . ; l; l; 	l
	


 0:
Then the dual program of P turns out to be the following form.
Maximize Fðu; vÞ ¼  P
t2FðSÞ ut þ P
e2EðSÞ wðeÞve, subject to
1. ut þ ve  0 whenever e is an edge of t.
Lemma 2.3.
If the condition of Lemma 2.1 is satisﬁed, then the objective function Fðu; vÞ of the dual program of P is
nonpositive, and it is equal to 0 if and only if there exists a value u such that ut ¼ ve ¼ u for all t 2 FðSÞ and all
e 2 EðSÞ.
Proof.
Let u ¼ minðu1; . . . ; ulÞ. Let uð1Þ
i
¼ ui  u and vð1Þ
j
¼ vj þ u. It is obvious that the vector ðuð1Þ; vð1ÞÞ satisﬁes the
constraints of the dual program. Furthermore
Fðuð1Þ; vð1ÞÞ  Fðu; vÞ ¼ u l 
X
e2EðSÞ
wðeÞ
 
!
¼ 0
from Lemma 2.1, so that Fðu; vÞ ¼ Fðuð1Þ; vð1ÞÞ. Consider the case where uð1Þ
i
¼ 0 for all i. Since all vð1Þ
j
must be
nonpositive and all of their coeﬃcients are positive, the objective function Fðu; vÞ is nonpositive and is equal to 0 only
if all vð1Þ
j
are equal to 0. Then we assume that uð1Þ
t
> 0 for some t 2 FðSÞ. Let Fð1Þ be the subset of FðSÞ such that
