---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-017-a-proof-of-lemma-25
section_title: "A Proof of Lemma 2.5"
section_number: null
pages: 41-46
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Proof of Lemma 2.5 We show that the system of inequalities
1 + 
k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
k
i=1
μ(yi)

w∈	(Y)
eμ(w)

q∈	(x1)∩	(X)
eμ(q)
≥1 +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
yi∼X
k
i=1
μ(yi)

w∈	(Y)∩	(X)C
eμ(w),
(A.1)
which is equivalent to (2.12), holds under the assumptions of the lemma. We do so by proving
the following three claims. However, ﬁrst we would like to introduce some additional notation
to complement the notation from Sect. 2.2.
For given x1 ∈X and X = {x2, ..., x p} ⊂X let Q denote the set 	(x1) ∩	(X) and let C
denote the set of (non-empty) compatible subsets of Q. Furthermore, we deﬁne the family
33
Page 42 of 47
S. Jansen, L. Kolesnikov
(AU)U⊂Q, AU = AU(x1, Q, μ), indexed by all the subsets U ⊂Q (including the empty
set), by
AU = AU(x1, Q, μ) :=

k≥1

Y={y1,...,yk}
k
i=1
μ(yi)

w∈	(Y)\U
eμ(w),
where the sum is over subsets Y = {y1, ..., yk} ⊂X such that the following constraints are
satisﬁed: Y is an compatible set, Y ⊂	(x1), Y ∩Q = ∅and U = 	(Y) ∩Q.
Finally, deﬁne the family of coefﬁcients (βU)U⊂Q, βU = βU(x1, Q, μ), also indexed by all
the subsets U ⊂Q (including the empty set), by
βU = βU(x1, Q, μ) :=

q∈Q\U
e−μ(q) +

C∈C
C∩U=∅

c∈C
μ(c)

w∈(Q\U)\	(C)
e−μ(w).
Then the following statements hold true:
Claim A.1 The right-hand side of (A.1) is bounded from above by
1 +

U⊂Q
AU.
Claim A.2 The left-hand side of (A.1) is bounded from below by
β∅+

U⊂Q
βU AU.
(A.2)
Claim A.3 The lower bounds βU ≥1 hold for every U ⊂Q and thus
β∅+

U⊂Q
βU AU ≥1 +

U⊂Q
AU.
All the sums in the three claims above run over subsets of Q = 	(x1) ∩	(X) including
the empty set (so that the coefﬁcient β∅appears in (A.2) twice). The inequalities (A.1) follow
directly from the three claims. Proving the claims is thus sufﬁcient to conclude the proof of
the lemma:
Proof of Claim A.1 Reorder the sum in the right-hand side of (A.1) by putting the summand
together which belong to the same U := 	(Y)∩Q. Notice that the constraint Y ∼X implies
Y ∩Q = ∅since Y ⊂	(x1). The claim now follows directly from the simple observation
that 	(Y) ∩	(X)C ⊂	(Y)\U for any Y and thus

w∈	(Y)\U
eμ(w) ≥

w∈	(Y)∩	(X)C
eμ(w).
⊓⊔
Proof of Claim A.2 To see that the bounds stated in the claim hold, decompose the sum in the
left-hand side of (A.1) as
1 +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
k
i=1
μ(yi)

w∈	(Y)
eμ(w)
=1 +

C∈C∪{∅}

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{C=Q∩Y}
k
i=1
μ(yi)

w∈	(Y)
eμ(w).
(A.3)
Cluster Expansions: Necessary...
Page 43 of 47
33
Notice that for any C ∈C

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{C=Q∩Y}
k
i=1
μ(yi)

w∈	(Y)
eμ(w)
≥

c∈C
μ(c)

w∈	(C)∩Q
eμ(w)
⎛
⎜⎜⎝1 +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}1{Y∼C}
k
i=1
μ(yi)

w∈	(Y)\(	(C)∩Q)
eμ(w)
⎞
⎟⎟⎠.
This estimate is established by discarding the exponential weights corresponding to a subset
of 	(C): Multiplying the lower bound in the last line with

w∈	(C)\	(Y)\Q
eμ(w) ≥1
yields equality. No further estimates are necessary to prove the claim; we simply plug the
obtained lower bound into the right-hand side of (A.3) and get
1 +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}
k
i=1
μ(yi)

w∈	(Y)
eμ(w) +

C∈C

c∈C
μ(c)

w∈	(C)∩Q
eμ(w)
×
⎛
⎜⎜⎝1 +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}1{Y∼C}
k
i=1
μ(yi)

w∈	(Y)\(	(C)∩Q)
eμ(w)
⎞
⎟⎟⎠
or, equivalently,
1 +

C∈C

c∈C
μ(c)

w∈	(C)∩Q
eμ(w) +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}
k
i=1
μ(yi)

w∈	(Y)
eμ(w)
+

C∈C

c∈C
μ(c)

w∈	(C)∩Q
eμ(w) 
k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}1{Y∼C}
k
i=1
μ(yi)

w∈	(Y)\(	(C)∩Q)
eμ(w)
as a lower bound for the left-hand side of (A.3).
33
Page 44 of 47
S. Jansen, L. Kolesnikov
Reordering the last expression by summing over Y ﬁrst, one realizes that it is equal to
1 +

C∈C

c∈C
μ(c)

w∈	(C)∩Q
eμ(w) +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}
k
i=1
μ(yi)

w∈	(Y)
eμ(w)
×
⎛
⎜⎝1 +

C∈C
C∼Y

c∈C
μ(c)

w∈(	(C)∩Q)\	(Y)
eμ(w)
⎞
⎟⎠,
which may be rewritten as
1 +

C∈C

c∈C
μ(c)

w∈	(C)∩Q
eμ(w) +

k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
1{Y∩Q=∅}
k
i=1
μ(yi)

w∈	(Y)\(	(Y)∩Q)
eμ(w)
×
⎛
⎜⎝

w∈	(Y)∩Q
eμ(w) +

C∈C
C∼Y

c∈C
μ(c)

w∈(	(C)∪	(Y))∩Q
eμ(w)
⎞
⎟⎠.
From the last expression, we obtain precisely the sum in (A.2) by putting the summands
in the last expression which belong to the same U = 	(Y) ∩Q together and dividing by

q∈Q eμ(q). This yields the claimed lower bound.
⊓⊔
Proof of Claim A.3 Without loss of generality, we may assume that Q = 	(x1) ∩	(X) is a
ﬁnite non-empty set. Then the claim can be proven via induction over the cardinality of Q.
To start the induction consider the case Q = {q}, q ∈X. Then β∅= e−μ(q) + μ(q) ≥1
and β{q} = 1 by deﬁnition.
For the inductive step, let n ∈N, Qn = {q1, ..., qn} ⊂X and let Cn be the set of compatible
subsets of Qn. Furthermore, let qn+1 ∈X\Qn and let Qn+1 = Qn ∪{qn+1}. Naturally, there
exists a family of subsets n ⊂Cn, such that the set Cn+1 of compatible subsets of Qn+1 is
given by Cn+1 = {C ∪{qn+1}|C ∈n or C = ∅} ∪Cn =: n ∪Cn.
UndertheassumptionthatβU(Qn) ≥1forallU ⊂Qn itistoshowthatβU(Qn+1) ≥1for
all U ⊂Qn+1. Therefore let U ⊂Qn+1. If qn+1 ∈U then βU(Qn+1) = βU\{qn+1}(Qn) ≥1
by the inductive hypothesis. Left to consider is the case qn+1 /∈U (and thus U ⊂Qn). Recall
that we deﬁned the coefﬁcient βU(Qn+1) by
βU(Qn+1) =

q∈Qn+1\U
e−μ(q) +

C∈Cn+1
C∩U=∅

c∈C
μ(c)

w∈(Qn+1\U)\	(C)
e−μ(w).
Cluster Expansions: Necessary...
Page 45 of 47
33
Using the decomposition Cn+1 = n ∪Cn, we get
βU(Qn+1) = e−μ(qn+1)

q∈Qn\U
e−μ(q) +

C∈n
C∩U=∅

c∈C
μ(c)

w∈(Qn+1\U)\	(C)
e−μ(w)
+

C∈Cn
C∩U=∅

c∈C
μ(c)

w∈(Qn+1\U)\	(C)
e−μ(w)
= e−μ(qn+1)

q∈Qn\U
e−μ(q) + μ(qn+1)

q∈(Qn\U)\	(qn+1)
e−μ(q)
+ μ(qn+1)

C∈n
C∩U=∅

c∈C
μ(c)

w∈(Qn+1\U)\	(C∪{qn+1})
e−μ(w)
+ e−μ(qn+1)

C∈n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w)
+

C∈Cn\n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w).
Multiplying the second summand in the last expression by the products of negative exponen-
tial weights

w∈	({qn+1})
e−μ(w)) ≤1
and the third summand by

w∈	({qn+1})\	(C)
e−μ(w)) ≤1,
we obtain the following lower bound:
βU(Qn+1)
≥

e−μ(qn+1) + μ(qn+1)
	
⎛
⎜⎜⎝

q∈Qn\U
e−μ(q) +

C∈n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w)
⎞
⎟⎟⎠
+

C∈Cn\n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w)
Since e−μ(qn+1) + μ(qn+1) ≥1 for any μ, this last expression is in turn bounded from below
by

q∈Qn\U
e−μ(q) +

C∈n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w) +

C∈Cn\n
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w)
=

q∈Qn\U
e−μ(q) +

C∈Cn
C∩U=∅

c∈C
μ(c)

w∈(Qn\U)\	(C)
e−μ(w) = βU(Qn).
By the inductive hypothesis βU(Qn) is bounded from below by 1, hence we have shown
βU(Qn+1) ≥1. This concludes the induction and therefore also the proof of Claim A.3. ⊓⊔
33
Page 46 of 47
S. Jansen, L. Kolesnikov
Combining the three statements from the claims A.1, A.2 and A.3 immediately yields the
claim of Lemma 2.5.
⊓⊔
