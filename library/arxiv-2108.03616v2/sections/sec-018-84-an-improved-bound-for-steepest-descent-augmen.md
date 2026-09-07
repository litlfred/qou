---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-018-84-an-improved-bound-for-steepest-descent-augmen
section_title: "An improved bound for steepest-descent augmentation"
section_number: 8.4
pages: 33-36
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
We now prove Theorem 8.4. The proof follows the same lines as that of the Goldberg–Tar jan
algorithm; see also [ AMO93, Section 10.5] for the analysis. A factor log n improvement over
the original bound was given in [ RG94]. A key property in the original analysis is that for a
ﬂow around a cycle (i.e., an elementary vector), every edge c arries at least 1 /|V| fraction of the
ℓ1-norm of the ﬂow. This can be naturally replaced by the argume nt that for every elementary
ﬂow g, the minimum nonzero value of |gi| is at least ‖g‖1/(1 + (m− 1)κA).
33
The Goldberg–Tarjan algorithm has been generalized to sepa rable convex minimization with
linear constraints by Karzanov and McCormick [ KM97]. Instead of κW , they use the maximum
entry in a Graver basis (see Section 9 below). Lemma 10.1 in their paper proves a weakly
polynomial bound similar to Lemma 8.8 for the separable convex setting. However, no strongly
polynomial analysis is given (which is in general not possib le for the nonlinear setting).
Our arguments will be based on the dual of LP(A,b,c,u ):
max⟨y,b⟩−⟨u,t⟩
A⊤y +s−t =c
s,t≥ 0.
(25)
Recall the primal-dual slackness conditions from Section 6: if x is feasible to LP(A,b,c,u ) and
y∈ Rm, they are primal and dual optimal solutions if and only if ⟨ai,y⟩≤ ci if xi < ui and
⟨ai,y⟩≥ ci if xi> 0.
Let us start by formulating the steepest-descent direction as an LP. Let ¯A = (A|− A)∈
Rm×(2n) and ¯c =
(c
−c
)
∈ R2n. Clearly, κ ¯A =κA. For a feasible solution x =x(t) to LP(A,b,c,u ),
we deﬁne residual variable set
N (x) ={i∈ [n] : xi<u i}∪{ n +j :j∈ [n] : xj > 0}⊆ [2n],
and consider the system
min⟨¯c,z⟩
¯Az = 0
⟨/BD
2n,z⟩ = 1
z[2n]\N (x) = 0
z≥ 0.
(26)
We can map a solution z∈ R2n to g∈ Rn by setting gi =zi−zn+i. We will assume that z is
chosen as a basic optimal solution. Observe that every basic feasible solution to this program
maps to an elementary vector in ker( ¯A). The dual program can be equivalently written as
minε
⟨¯ai,y⟩≤ ¯ci +ε ∀i∈N (x). (27)
For the solution x, we let ε(x) denote the optimal solution to this dual problem; thus, the
optimal solution to the primal is −ε(x). If ε = 0, then x and y are complementary primal and
dual optimal solutions to LP(A,b,c,u ). We ﬁrst show that this quantity is monotone (a key
step also in the analysis in [ DLHL15]).
Lemma 8.7. At every iteration of the circuit augmentation algorithm, ε(x(t+1))≤ε(x(t)).
Proof. Let ε = ε(x(t)) and let y be an optimal solution to ( 27) for N (x(t)). We show that the
samey is also feasible for N (x(t+1)); the claim follows immediately. There is nothing to prove i f
N (x(t+1))⊆N (x(t)), so let i∈N (x(t+1))\N (x(t)).
Assume ﬁrst i∈ [n + 1, 2n]; let i = n +j. This means that x(t)
j = 0 < x(t+1)
j ; therefore,
the augmenting direction g has gj > 0. Thus, for the optimal solution z to ( 26), we must have
zj > 0. By primal-dual slackness, ⟨aj,y⟩ =cj +ε; thus,
⟨¯ai,y⟩ =⟨−aj,y⟩ =−cj−ε< −cj = ¯cj.
The case i∈ [n] is analogous.
The next lemma shows that within every n iterations,ε(x(t)) decreases by a factor depending
on κA.
34
Lemma 8.8. For every iteration t, ε(x(t+n))≤
(
1− 1
1+(m−1)κA
)
ε(x(t)).
Proof. Let us set N =N (x(t)), ε =ε(x(t)), and let y =y(t) be an optimal dual solution to ( 27)
for x(t). Let
T :={i∈N :⟨¯ai,y⟩> ¯ci}⊆ [2n] ;
that is, if i∈ [n] then ⟨ai,y⟩ > ci, and if i∈ [n + 1, 2n], i = n +j, then ⟨aj,y⟩ < cj. In
particular,|T∩{i,i +n}|≤ 1 for every i∈ [n]. Let z(t) be the basic optimal solution to ( 26)
for x(t). By complementary slackness, every i∈ supp(z(t)) must have ⟨¯ai,y⟩ = ¯ci +ε, and thus,
supp(z(t))⊆T .
Claim 8.8.1. Let us pick k>t as the ﬁrst iteration when for the basic optimal solution z(k) to
(26), we have supp(z(k))\T⁄=∅. Then k≤t +n, and the solution (y,ε ) is still feasible for (27)
for x(k).
Proof. Forr∈ [t,k− 1], let T (r) =T∩N (x(r)). We show that T (r+1) ⊊ T (r). Since |T|≤ n, this
implies k≤ t +n. Let z(r) be the basic optimal solution for ( 26); recall that the augmenting
direction is computed with gj = z(r)
j −z(r)
n+j. By the choice of k, supp(z(r))⊆ T (r). Thus,
we may only increase xi for i∈ T∩ [n] and decrease it for i = j−n for j∈ T∩ [n + 1, 2n].
Consequently, every index i entering N (x(r+1)) has ⟨¯ai,y⟩ < ¯ci, and therefore ( y,ε ) remains
feasible throughout.
We now turn to the proof of T (r+1) ⊊ T (r). Since we use a maximal augmentation, at least
one index leaves T (r) at each iteration. We claim that T (r+1)\T (r) =∅. For a contradiction,
assume there exists i∈ T (r+1)\T (r). If i∈ [n], then i +n must be in the support of z(r); in
particular, i +n∈ T (r). But this would mean that {i,i +n}⊆ T , in contradiction with the
deﬁnition of T . Similarly, for i∈ [n + 1, 2n].
Let us now consider the optimal solution z =z(k) to ( 26) at iteration k; by the above claim,
(y,ε ) is still a feasible dual solution. Select an index j∈ supp(z)\T .
⟨−¯c,z⟩ =
⟨
¯A⊤y− ¯c,z
⟩
≤ε
∑
i∈supp(z)\{j}
zi = (1−zj)ε≤
(
1− 1
1 + (m− 1)κA
)
ε.
In the ﬁrst inequality, we use that ⟨¯ai,y⟩− ¯ci≤ε by the feasibility of ( y,ε ), and⟨¯aj,y⟩− ¯cj≤ 0
by the choice of j /∈ T . In the second equality, we use the constraint ∑
izi = 1. The ﬁnal
inequality uses that z is a basic solution, and therefore, an elementary vector in k er( ¯A). In
particular|supp(z)|≤ m, and zi≤κ ¯Azj =κAzj. Consequently, zj≥ 1/(1 + (m− 1)κA).
We say that the variable j∈ [2n] is frozen at iteration t, if j /∈N (x(t′)) for any t′≥t. Thus,
for j∈ [n], xj = uj, and for j∈ [n + 1, 2n], j = i +n, xi = 0 for all subsequent iterations.
We show that a new frozen variable can be found in every O(nmκA log(mκA)) iterations; this
implies Theorem 8.4.
Lemma 8.9. For every iteration t≥ 1, there is a variable j∈N (x(t)) that is frozen at iteration
k for k =t +O(nmκA log(κA +n)).
Proof. Let ε =ε(x(t)). By Lemma 8.8, we can choose k =t +O(nmκA log(n +κA)) such that
ε′ =ε(x(k))< ε/(2n(κA + 1)). Consider the primal and dual optimal solutions ( z,y,ε ) to ( 26)
and ( 27) at iteration t and (z′,y ′,ε ′) at iteration k.
Claim 8.9.1. There exists a j∈ supp(z) such that ⟨¯aj,y ′⟩> ¯cj + 2n(κA + 1)ε′.
Proof. For a contradiction, assume that ⟨¯aj,y ′⟩− ¯cj≤ 2n(κA + 1)ε′ for every j∈ supp(z). Then,
ε =⟨¯c,z⟩ =
⟨
¯A⊤y− ¯c,z
⟩
≤ 2n(κA + 1)ε′ ∑
j
zj = 2n(κA + 1)ε′,
contradicting the choice of ε′.
35
We now show that all such indices are frozen at iteration k by making use of Theorem 6.5
on proximity. Let x′ = x(k) and x′′ = x(k′′) for any k′′ > k; let ( y′′,ε ′′) be optimal to ( 27) at
iteration k′′; we have ε′′≤ε′ by Lemma 8.7.
Let us deﬁne the cost c′∈ Rn by
c′
i :=



⟨¯ai,y ′⟩ if 0 <x ′
i<u i
max{ci,⟨¯ai,y ′⟩} if x′
i =ui
min{ci,⟨¯ai,y ′⟩} if x′
i = 0.
If we replace the cost c by c′, then x′ and y′ satisfy complementary slackness, and hence are
optimal to LP(A,b,c,u ) and ( 25). Moreover, the optimality of ( y′,ε ′) to ( 27) guarantees that
‖c′−c‖∞≤ε′.
We similarly construct c′′ for y′′, and note that x′′ and y′′ are primal and dual optimal
solutions for the costs c′′,‖c′′−c‖∞≤ε′′. Further,
‖c′−c′′‖1≤n‖c′−c′′‖∞≤n
(
‖c′−c‖∞ +‖c′′−c‖∞
)
≤n(ε′ +ε′′)≤ 2nε′
We thus apply Theorem 6.5 for (x′,y ′) for c′ and (x′′,y ′′) for c′′, showing that every variable j
as in Claim 8.9.1 must be frozen.
