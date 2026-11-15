---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
toc_source: undetermined
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
uð1Þ
t
> 0 for each t 2 Fð1Þ and uð1Þ ¼ mint2Fð1Þðuð1Þ
t Þ. Let lð1Þ ¼ jFð1Þj. Let uð2Þ
t
¼ uð1Þ
t
¼ 0 if t =2 Fð1Þ and otherwise
uð2Þ
t
¼ uð1Þ
t
 uð1Þ. Also let vð2Þ
e
¼ vð1Þ
e
if e is not contained in some element of Fð1Þ and otherwise vð2Þ
e
¼ vð1Þ
e þ uð1Þ. The
vector ðuð2Þ; vð2ÞÞ still satisﬁes the constraints of the dual program. Furthermore
Fðuð2Þ; vð2ÞÞ  Fðuð1Þ; vð1ÞÞ ¼ u lð1Þ 
X
e incident to Fð1Þ
wðeÞ
 
!
> 0
from Lemma 2.1, so that Fðuð2Þ; vð2ÞÞ > Fðuð1Þ; vð1ÞÞ. We take the new nonzero set Fð2Þ as a proper subset of Fð1Þ, and we
repeat this process. At the end, we will wind up with the feasible point ðuðkÞ; vðkÞÞ with uðkÞ ¼ 0 where the value of the
objective function is nonpositive and strictly greater than the value of the objective function at ðu; vÞ. Then the assertion
follows.

Next we strengthen the ﬁrst constraint as each angle is strictly positive. To consider that, we put each angle  as
 ¼ 0 þ  and require that all 0 are nonnegative. Set the new objective function as ð0; . . . ; 0; 1Þ  ð10; 10;
	10; . . . ; l0; l0; 	l0; ÞT and denote this linear program by P0. We can express P0 using a matrix as the following.
Minimize ð0; . . . ; 0; 1Þ  ð10; 10; 	10; . . . ; l0; l0; 	l0; ÞT subject to
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
3
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
3
...
...
...
...
...
...
..
.
...
...
...
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
3
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
valðe1Þ
...
...
...
...
...
...
..
.
...
...
...
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
valðemÞ
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
1
0
1
0
	1
0
...
l
0
l
0
	l
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
C
A
¼


..
.

wðe1Þ
...
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
1
0; 1
0; 	1
0; . . . ; l
0; l
0; 	l
0; 
	


 0:
Then the dual program of P0 turns out to be the following.
Maximize Fðu; vÞ ¼  P
t2FðSÞ ut þ P
e2EðSÞ wðeÞve, subject to
1. ut þ ve  0 whenever e is an edge of t,
2. 3 P
t2FðSÞ ut þ P
e2EðSÞ valðeÞve  1.
Lemma 2.4.
The optimal value of the objective function of the dual program of P0 is strictly negative.
Proof.
Suppose the contrary. Then by Lemma 2.3, ut ¼ ve ¼ u for some u. In this case, the left hand side of the
second constraint is
3
X
t2FðSÞ
ut þ
X
e2EðSÞ
valðeÞve ¼ u 3
X
t2FðSÞ
1 
X
e2EðSÞ
valðeÞ
 
!
:
Here the right hand side is equal to 0 then the inequality is not satisﬁed. It contradicts the ﬁrst assumption.

From Theorem 2.2 and Lemma 2.4, the objective function of P0, that is ð0; . . . ; 0; 1Þ  ð10; 10; 	10; . . . ; l0;
l0; 	l0; ÞT ¼ , is strictly negative, so that there are the solutions that each angle is strictly positive. Thus the
condition of Lemma 2.1 turns out to be a suﬃcient condition.
Lemma 2.5.
Let F0  FðSÞ, and let E0 be the set of all edges contained in F0. Assume that w satisﬁes the following
condition:
X
e2E0
wðeÞ 
 jF0j
with equality if and only if F0 ¼ FðSÞ or F0 ¼ . Then S admits locally Euclidean structures coming from w.
We denote the set of all locally Euclidean structures on S coming from w by AðS; wÞ. It is a subset of R3l whose
coordinates are the angles of the 2-faces of S.
