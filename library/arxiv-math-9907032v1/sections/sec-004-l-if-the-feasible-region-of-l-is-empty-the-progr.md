---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-004-l-if-the-feasible-region-of-l-is-empty-the-progr
section_title: "If the feasible region of L is empty, the program is said to be infeasible. Now"
section_number: L
pages: 7-9
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
we can state the Duality Theorem:
Theorem 3.2 ( Duality Theorem of Linear Programming ). Let P be a
linear program of the form:
· 8
Minimize c⊥x, subject to the constraints Ax = a, x ≥ 0.
Then the dual of P is the program P ∗:
Maximize a⊥λ, subject to the constraints λ⊥A ≤ c.
The feasible region of P is nonempty if and only if the objective of P ∗ is bounded.
Conversely, the feasible region of P ∗ is nonempty if and only if the objective of P
is bounded. If neither feasible region is empty, then the val ues of the objective
functions of P and P ∗ are equal.
Remark. While the primal program P in the statement of Theorem 3.2 appears
to be of a very special form, it is not hard to see that any linear prog ram can
be written in this form. Indeed, if our linear program asked us to max imize the
objective, we can always convert it to a minimization problem by multiply ing c
by −1. If our program did not require the variables to be non-negative, we can
always replace a variable x byx+ −x−, where x+ and x− are both required to be
non-negative. If the program had some inequalities of the form ai⊥x ≥a, or of the
form ai⊥x ≤a we can ﬁrst convert all the inequalities of the ﬁrst type to those of
the second type by negation, and then convert them to equations by introducing
slack variables xi ≥ 0, and requiring ai⊥x +xi =a. Similarly, any program can be
made to look like the dual program P ∗ in the statement of Theorem 3.2.
Program L is almost in the primal form needed by the duality theorem, but for
two diﬀerences: there is no objective function, and we want the pr imal variables
(the angles of the triangles) to be strictly positive, rather than ju st non-negative.
For the moment, let us sweep these issues under the rug, by settin g the objective
function to be 0, and allowing the angles to vanish – it will be quickly appa rent
how to ﬁx things up later. Let the modiﬁed program be L1. The dual L∗
1 of L1 is
the following:
The dual program. Maximize F (u, v) : π ∑
t∈F (T )ut + ∑
e∈E(T ) ∆( e)ve, subject
to the conditions ut +ve ≤ 0 whenever e is an edge of t.
Theorem 3.3. Assume that the conditions described in conditions 2.1 and 2 .2
are satisﬁed. Then the objective function of L∗
1 is nonpositive. It equals 0 if and
only if there is a u, such that ut = −ve =u, for all t ∈F (T ), e ∈E(T ).
Proof. Observation 1. Note that if there is a u as required in the statement
of the Theorem, the objective function is, indeed, equal to 0. This is nothing other
than the equality case of Condition 2.2.
Now, let u = min(u1,...,u F (T )). Let u(1)
i = ui −u, and let v(1)
j = vj +u,
for all values of the indices. The new variables are still feasible for L∗
1, and by the
observation 1 above, this transformation does not change the va lue of the objective.
Furthermore, if u(1)
i = 0 for all i, then the objective is non-positive, and is equal to
zero only if all of v(1)
j are equal to zero as well – this is so, since all of the vj must be
non-positive, and all of their coeﬃcients are positive, by Observat ion 2.1. Assume,
then, that u(1)
t > 0 for t ∈ F (1); F (1) is a proper subset of F (T ) by construction.
Observation 2. Suppose now that u(1)
t =u, for all t ∈ F 1. Then
F ≤π
∑
t∈F (1)
u −
∑
e∈E(F (1))
∆( e)u< 0,
· 9
by 3.
Now, let u(1) = min t∈F (1)(u(1)
t ), and let u2
t =u(1)
t = 0 if t /∈ F (1), and otherwise
u(2)
t = u(1)
t −u(1). Likewise, v(2)
e = v(1)
e if e /∈ E(F (1), and otherwise v(2)
e =
v(1)
e +u(1).
This still leaves us in the feasible region of L∗
1 and strictly increases the value of
the objective (by Observation 2). The new nonzero set F (2) is a proper subset of
F (1), and we can repeat this process. In the end, we will wind up with a fea sible
point u(k), v(k), with u(k) = 0, where the value of the objective is non-positive
(by Observation 1), and strictly greater than the value of the obj ective at u, v (by
Observation 2), thus completing the proof.
The above theorem shows that the feasible region of L1 is non-empty. In order
to ﬁnd a solution with strictly positive angles, we write our angles αi asαi =βi +ǫ.
We require all of the βi to be non-negative, and our new objective is simply −ǫ.
Call the resulting program L2. Its dual L∗
2 has the following form:
Second dual. Maximize F (u, v) : π ∑
t∈F (T )ut + ∑
e∈E(T ) ∆( e)ve, subject to
the conditions ut +ve ≤ 0 whenever e is an edge of t, and also 3 ∑
t∈F (t)ut +
2 ∑
e∈E(T ),e / ∈∂T ve + ∑
e∈E(T ),e ∈∂T ve ≤ −1.
Theorem 3.4. The optimal value of the objective of L∗
2 is strictly negative.
Proof. Suppose the contrary. Then ut = −ve =u, for some u, by Theorem 3.3.
However, in that case the last inequality of L∗
2 is not satisﬁed, since the left hand
side of the last constraint of L∗
2 vanishes. Indeed, it is equal to
u

3
∑
t∈F (t)
1 − 2
∑
e∈E(T ),e / ∈∂T
1 −
∑
e∈E(T ),e ∈∂T
1

.
Observe, however, that 3 ∑
t∈F (t) 1 counts each non-boundary edge with multiplic-
ity 2, and each boundary edge with multiplicity 1 .
