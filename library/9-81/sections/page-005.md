---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
toc_source: undetermined
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
3.
Singular Euclidean Structures
In this section, we consider when S admits a singular Euclidean structure. To discuss that, we will use some results of
hyperbolic geometry. At ﬁrst, we prepare some elementary notations.
Consider the upper half-space model of H3 and an ideal simplex in it. Let A, B, C, 1 be the vertices of the ideal
simplex, and , , 	 be the dihedral angles at the edges 1A, 1B, 1C respectively. Notice that , , 	 are equal to the
angles of the triangle ABC on xy-plane which is seen as a Euclidean triangle. According to the Milnor’s formula (see [2]
or [6]), the volume of the ideal simplex is expressed as the following:
V ¼ Vð; ; 	Þ ¼ LðÞ þ LðÞ þ Lð	Þ
ð2Þ
where LðxÞ is the Lobachevsky function
LðxÞ ¼ 
Z x
0
logð2 sin 
Þd
:
ð3Þ
Remark.
Usually the integrand of (3) is denoted by log j2 sin 
j. But we will only consider the case where each angle
is less than . Then we adopt the deﬁnition above.
Lemma 3.1 ([3, Theorem 2.1]).
V is convex on fð; ; 	Þ 2 R3j > 0;  > 0; 	 > 0;  þ  þ 	 ¼ g.
Deﬁnition.
A volume V ðA Þ of a locally Euclidean structure A 2 AðS; wÞ is the sum of the volumes of the ideal
simplices of which dihedral angles are equal to the angles of the 2-faces which are assigned from A .
Lemma 3.2.
V is convex on AðS; wÞ.
Proof.
From Lemma 3.1, V is convex on fð1; 1; 	1; . . . ; l; l; 	lÞ 2 R3lji > 0; i > 0; 	i > 0; i þ i þ 	i ¼  for
1  i  lg. The constraints from a weight determines an aﬃne subspace, then V is convex on AðS; wÞ.

Lemma 3.3.
If AðS; wÞ is not empty, then V has only one critical point on AðS; wÞ which gives the maximum value.
Proof.
Let AðS; wÞ be the closure of AðS; wÞ. The closure AðS; wÞ is compact and V is continuous on it. Then to prove
the assertion, it is suﬃcient to show that the critical point is not on @AðS; wÞ.
Let p 2 @AðS; wÞ and q 2 int AðS; wÞ. Let pi and qi be the i-th coordinates of p and q respectively. We may assume
that q is suﬃciently close to p so that max1in jqi  pij < 1. Let v ¼ q  p and rðtÞ ¼ p þ tv. We will show that the
inequality V ðp þ tvÞ > V ðpÞ holds for a suﬃciently small value t. Reorder the coordinates of p as p1 ¼    ¼ pi0 ¼ 0
and 0 < pi0þ1; . . . ; pn < . Let fðtÞ ¼ V ðrðtÞÞ. When t > 0, it is seen that
f 0ðtÞ ¼
X
n
i¼1
@V
@ri

rðtÞðqi  piÞ:
Let MðpÞ ¼ mini0inðminðpi;   piÞÞ, and assume that t < t0 ¼ MðpÞ=ð2kvkÞ, then
f 0ðtÞ >
X
i0
i¼1
@V
@ri

rðtÞ
ðqi  piÞ  ðn  i0Þ log 2 sin MðpÞ
2



:
ð4Þ
Since the function logð2 sin xÞ is continuous on ð0; Þ and goes to 1 at both 0 and , we can take suﬃciently small
value ti for each 1 < i < i0 so that the inequality
@V
@ri

rðtÞ
ðqi  piÞ > ðn  i0Þ log 2 sin MðpÞ
2




ð5Þ
holds for 0 < t < ti. Let tmin ¼ minðt1; . . . ; ti0Þ. Then the inequality f 0ðtÞ > 0 holds for 0 < t < tmin from (4) and (5). By
the mean value theorem, there exists some value  for 0 <  < tmin such that V ðrðtminÞÞ  V ðpÞ ¼ fðtminÞ 
fð0Þ ¼ f 0ðÞ. Thus V ðrðtminÞÞ ¼ fðtminÞ > fð0Þ ¼ V ðpÞ.

Now we consider the gluings of the adjacent 2-faces of S which admits the locally Euclidean structures coming from
w. Let c ¼ ft1; t2; . . . ; tk ¼ t1g be an ordered collection of the 2-faces of S such that ti and tj share an edge if
ji  jj ¼ 1. The collection c is called a dual cycle of S.
Deﬁnition.
Let ti be a Euclidean triangle and assign ti ¼ ABC satisfying AB ¼ ti1 \ ti and AC ¼ ti \ tiþ1. The
dilatation of ti with respect to the vertex A is the quantity Dðti; AÞ ¼ log jACj  log jABj.
