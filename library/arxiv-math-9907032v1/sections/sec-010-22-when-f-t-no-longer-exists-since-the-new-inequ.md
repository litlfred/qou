---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-010-22-when-f-t-no-longer-exists-since-the-new-inequ
section_title: "(when F = T ) no longer exists. Since the new inequalities require u to be"
section_number: 2.2
pages: 17-19
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
non-negative, it follows that for the objective function to equal 0 ,u must be 0.
Now, we follow Section 3 again, to deﬁne a program L′
2 in the same way as before
(that is, since we want the angles to be strictly positive, we set αi = βi +ǫ, etc,
and to also deﬁne its dual L′∗
2 . By the same reasoning as before, it follows that the
objective of L′∗
2 , and hence of L′
2, is negative. In fact, we can do more: we can also
require all of the slack variables xe to be strictly positive. The (yet another) new
dual program L′∗
3 will have the form:
Third dual. Maximize F (u, v) : π ∑
t∈F (T )ut + ∑
e∈E(T ) ∆( e)ve, subject to the
conditions
ut +ve ≤ 0 whenever e is an edge of t.
ve ≤ 0, when e is a boundary edge of T .
3 ∑
t∈F (t)ut + 2 ∑
e∈E(T ),e / ∈∂T ve + 2 ∑
e∈E(T ),e ∈∂T ve ≤ −1.
If we omit the last constraint, we remain with the dual program L′∗
1 , and as the
discussion above showed, the objective of that can only be 0 if ut ≡ve ≡ 0, which
is at odds with the last constraint of L′∗
3
Theorem 6.3. Letp1,...,p n be a set of points in the plane, and D their Delau-
nay triangulation. Assume that the shortest edge of D has length 1, and the excess
of every non-trivial subcomplex of D is no smaller than d0. Then
diameterD ≤
( 4n
d0
) n
.
The proof of Theorem 6.3 will depend on a couple of easy auxillary resu lts:
Lemma 6.4. Let ABC be a triangle with a/c,a/b < ǫ, 0 < ǫ <1/10. Then,
α< 2ǫ.
Proof. This is an immediate consequence of the theorem of Cosines, or the
theorem of Sines.
Lemma 6.5. Let F be a subcomplex of D. Then the excess of F is
∑
triangles ABC such that AB ∈ F
γ(ABC ),
whereγ(ABC ) is the angle at C.
Proof. This is immediate from the deﬁnition of excess.
Proof of theorem 6.3. Suppose that the conclusion of the theorem does not
hold. Assume, without loss of generality, that the edge between th e vertices p0 and
p1 is the shortest one (and thus of length 1).
We construct a family of disks D1,D 2,...,D n, all centered on p0, and such that
the radius of Di is equal to
( 4n
d 0
) n
. Let Ai = Di+1\Di, and let Fi to be the
· 18
maximal closed subcomplex of D contained in Di. The hypothesis of the theorem
ensures that at least one of the annuli Ai contains no vertices of D, let this annulus
be Aj . Then we claim that the excess of Fj is smaller than d0. Indeed, consider a
triangle ABC of D adjacent to Fj along an edge AB. The vertex C of ABC lies
outside Dj+1, and thus the lengths of AC and BC are at least
(
4n
d0
) j+1
−
(
4n
d0
) j
,
while the length of AB is at most
(
4n
d0
) j
. Thus,
γ(ABC )< 2
4n
d0
− 1 < d0
n,
by lemma 6.4. Thus, by lemma 6.5, it follows that
excess Fj <d 0,
contradicting the hypothesis of the theorem.
Proof of Theorem 6.1. We only need to show that the positive excess condi-
tions are suﬃcient, since they are obviously necessary. In addition , we may assume
that the 1-skeleton of the Poincar´ e dual T ∗ is connected (if not, we prove the
theorem for each connected component separately).
Now, we pick a pair of adjacent base vertices v1,v 2 ∈V (T ), and ﬁx d(v1,v 2) = 1.
Now, for v,w ∈V (T ) we deﬁne dc(v,w ) to be equal to the combinatorial distance
between v and w in the 1-skeleton of T . Now, deﬁne Fi to be the span of all
verticesu, such that dc(v1,u ) ≤i. The complex Fi is ﬁnite by local ﬁniteness of T .
In addition, ⋃
i Fi = T , so every ﬁnite subcomplex of T belongs to some Fi. For
each Fi we consider a geometric realization S(Fi), whose existence is guaranteed
by lemma 6.2 (there are many such realizations, we pick any one of the m).
Now, enumerate the faces of T , in such a way that t1 contains the edge v1v2, and,
for any j, the faces tj andtj+1 are adjacent (that is, share an edge) in T . For each
triangle, we have the space of shapes (similarity classes), given (fo r example) by the
complex parameterz, obtained by placing the ﬁrst two vertices of the triangle at the
points 0 and 1 in the complex plane, and reading oﬀ the position of the t hird point
(in the upper half-plane, assuming the triangle is positively oriented) . Theorem 6.3
tells us that for any face t of T , the set of shape parameters of realizations of t is
contained in a compact set Ct (since the ratio of lengths of any two sides is bounded
by some constant, depending on the function ∆). We can think of ea ch S(Fi) as
being an element of C = ∏
jCtj , which is a compact set by Tykhonov’s theorem,
and hence we can extract a convergent subsequence from S(F1),...,S (Fk),... . Call
the limit of that subsequence S. Since the dihedral angles are obviously continuous
functions of the triangle parameters, the dihedral angles of S will be given by ∆,
and so S is the sought-after realization.
Note. For the comfort of more analytically inclined readers, it should be poin ted out
that the last argument is just an Arzela-Ascoli – uniform converge nce on compact
sets argument.
· 19
