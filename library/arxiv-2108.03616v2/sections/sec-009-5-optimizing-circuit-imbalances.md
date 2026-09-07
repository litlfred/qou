---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-009-5-optimizing-circuit-imbalances
section_title: "Optimizing circuit imbalances"
section_number: 5
pages: 18-24
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
Recall that Dn is the set of n×n positive deﬁnite diagonal matrices. For every D ∈ Dn,
AD represents a column rescaling. This is a natural symmetry in linear programming, and
particularly relevant in the context of interior point algo rithms, as discussed in Section 7.2.
The condition number κAD may vastly diﬀer from κA. In terms of the subspace W = ker(A),
this amounts to rescaling the subspace by D−1; we denote this by D−1W . It is natural to ask
for the best possible value that can be achieved by rescaling :
κ∗
W = inf{κDW : D∈ Dn} .
In most algorithmic and polyhedral results in this paper, th e κW dependence can be replaced
by κ∗
W dependence. For example, the diameter bound in Theorem 4.8 is true in the stronger
form with κ∗
W , since the diagonal rescaling maintains the geometry of the polyhedron.
Even the value κ∗
W can be arbitrarily large. As an example, let W ⊆ R4 be deﬁned as
W = span{(0, 1, 1,M ), (1, 0,M, 1)}. Both generating vectors are elementary, and we see that
κW =M . Rescaling the third and fourth coordinates have opposite e ﬀect on the two elementary
vectors, therefore we also have κ∗
W =M , i.e. the original subspace is already optimally rescaled.
A key result in [ DHNV20] shows that an approximately optimal rescaling can be found :
18
Theorem 5.1 ([DHNV20]). There is an O(n2m2 +n3) time algorithm that for any matrix
A∈ Rm×n, computes an estimate ξ of κA such that
ξ≤κA≤ (κ∗
A)2ξ
and a D∈ Dn such that
κ∗
A≤κAD≤ (κ∗
A)3.
This is in surprising contrast with the inapproximability r esult Theorem 4.3. Note that there
is no contradiction since the approximation factor ( κ∗
A)2 is not bounded as 2 poly(n) in general.
The key idea of the proof of Theorem 5.1 is to analyze the pairwise imbalances κij = κW
ij
introduced in Section 3.3. In the 4-dimensional example above, we have κ34 = κ43 = M . Let
D ∈ D and let d∈ Rn denote the diagonal elements; i.e. the rescaling multiplie s the i-th
coordinate of every w∈W bydi. Then, we can see that κDW
ij =κijdj/di. In particular, for any
pair of variablesi andj,κDW
ij κDW
ji =κijκji. Consequently, we get a lower bound κijκji≤ (κ∗
W )2.
Theorem 5.1 is based on a combinatorial min-max characterization that e xtends this idea.
For the rest of this section, let us assume that the matroid M(W ) is non-separable. In case it
is separable, we can obtain κ∗
W by taking a maximum over the non-separable components.
Let G = ([n],E ) be the complete directed graph on n vertices with edge weights κij. Since
M(W ) is assumed to be non-separable, Proposition 2.2 implies that κij > 0 for any i,j ∈ [n].
We will refer to this weighted digraph as the circuit ratio digraph .
LetH be a cycle inG, that is, a sequence of indices i1,i 2,...,i k,ik+1 =i1. We use |H| =k
to denote the length of the cycle. (In this terminology, cycles refer to objects in G, whereas
circuits to objects in CW .)
We use the notation κ(H) = κW (H) = ∏ k
j=1κW
ijij+1. The observation for length-2 cycles
remains valid in general: κ(H) is invariant under any rescaling. This leads to the lower bo und
(κ(H))1/|H|≤κ∗
W . The best of these bounds turns out to be tight:
Theorem 5.2 ([DHNV20]). For a subspace W⊆ Rn, we have
κ∗
W = max
{
κW (H)1/|H| : H is a cycle in G
}
.
The proof relies on the following formulation:
κ∗
W = min t
κijdj/di≤t ∀(i,j )∈E,
d> 0.
(8)
Taking logarithms and substituting zi = logdi, we can rewrite this problem equivalently as
mins
logκij +zj−zi≤s ∀(i,j )∈E,
z∈ Rn.
(9)
This is the dual of the minimum-mean cycle problem with weigh ts log κij, and can be solved in
polynomial time (see e.g. [ AMO93, Theorem 5.8]).
Whereas this formulation veriﬁes Theorem 5.2, it does not give a polynomial-time algorithm
to compute κ∗
W . In fact, the values κij are already NP-hard to approximate due to Theorem 4.3.
Nevertheless, the bound κijκji≤ (κ∗
W )2 implies that for any elementary vector gC with support
i,j∈C, we have
κij
(κ∗
W )2≤ 1
κji
≤
⏐⏐⏐⏐
gj
gi
⏐⏐⏐⏐≤κij. (10)
To ﬁnd an eﬃcient algorithm as in Theorem 5.1, we replace the exact values κij by estimates
ˆκij obtained as |gC
j /gC
i| for an arbitrary circuit C∈C W with i,j ∈ C; these can be obtained
using standard techniques from linear algebra and matroid t heory. Thus, we can return ξ =
max(i,j)∈E ˆκij as the estimate on the value of κA. To estimate κ∗
A, we solve ( 9) with the estimates
ˆκij in place of the κij’s.
19
5.1 Perfect balancing: κ∗
W = 1
Let us now show that κ∗
A = 1 can be eﬃciently checked.
Theorem 5.3. There exists a strongly polynomial algorithm, that given a ma trix A∈ Rm×n,
returns one of the following outcomes:
(a) A diagonal matrix D∈ Dn such that κAD = 1 showing that κ∗
A = 1 . The algorithm also
returns the exact value of κA. Further, if ker(A) is a rational linear space, then we can
selectD with integer diagonal entries that divide ˙κA.
(b) The answer κ∗
A> 1, along with a cycle of circuits H such that κA(H)> 1.
Proof. As noted above, we can assume without loss of generality that the matroid M(W ) is
non-separable, as we can reduce the problem to solving on all connected components separately.
We obtain estimates ˆκij for every edge (i,j ) of the circuit ratio graph using a circuit C∈C W
withi,j∈C. Assuming that κ∗
W = 1, ( 10) implies that ˆκij =κij holds and the rescaling factors
di must satisfy
ˆκijdj =di ∀i,j∈ [n]. (11)
If this system is infeasible, then using the circuits that pr ovided the estimates ˆκij, we can obtain
a cycle H such that κA(H)> 1, that is, outcome (b). Let us now assume that ( 11) is feasible;
then it has a unique solution d up to scalar multiplication. We deﬁne D∈ Dn with diagonal
entriesDii =di.
SinceM(W ) is non-separable, we can conclude that κ∗
A = 1 if and only if κAD = 1. By
Theorem 3.4, this holds if and only if A′ =A−1
B AD is a TU-matrix for any basis B.
We run Seymour’s algorithm [ Sey80] for A′. If it conﬁrms that A is TU (certiﬁed by a
construction sequence), then we return outcome (a). In this case, |gC
j /gC
i| is the same for any
circuit C with i,j ∈C; therefore κij = ˆκij, and we can return κA = max (i,j)∈E ˆκij.
Otherwise, Seymour’s algorithm ﬁnds a k×k submatrix T of A′ with det(T ) /∈{ 0,±1}. As
in the proof of Proposition 3.2, we can recover a circuit C inCA′ =CAD with two entries i,j ∈C
such that|¯gj|⁄=|¯gi| for the corresponding elementary vector ¯g∈F (AD). Note that ˆκijdj =di
for the rescaled estimates. Hence, the circuit C ′ with i,j ∈C ′ used to obtain the estimate κij,
together with C certiﬁes that κ∗
A > 1 as required for outcome (b).
Finally, if ker(A) is a rational linear space and we concluded κ∗
A = 1, then let us select the
solutiondi to ( 11) such that d∈ Zn and gcd(d) = 1. We claim that di| ˙κW for all i. Indeed, let
k = lcm(d). For each pair i,j ∈ [n], dj/di =r/q for two integers r,q| ˙κA. Hence, for any prime
p∈ P, νp(k)≤νp( ˙κA), implying k| ˙κA.
LetW⊆ Rn be a linear space such that M(W ) is non-separable. Recall from Theorem 3.21
thatKW
ij ⊆K W
ik·KW
kj for all i,j,k ∈ [n]. We now characterize when equality holds for all triples.
Proposition 5.4. LetW⊆ Rn be a linear space such that M(W ) is non-separable. Then, the
following are equivalent:
(i) κ∗
W = 1,
(ii) |KW
ij| = 1 for all i,j ∈ [n],
(iii) KW
ij =KW
ik·KW
kj holds for all distinct i,j,k ∈ [n].
Proof. (i)⇔ (ii): Consider any rescaling D ∈ Dn with diagonal entries di = Dii. Then,
KDW
ij ={1}, and KDW
ij = dj
di
KW
ij . Hence, if κDW = 1 for some D∈ Dn, then KDW
ij ={1}
implying|KW
ij| = 1 for every i,j ∈ [n]. If |KW
ij| > 1 for some i,j , it follows that κDW ⁄= 1 for
any diagonal rescaling.
20
(ii)⇒ (iii): We have KW
ij ⊆K W
ik·K W
kj by Theorem 3.21. If all three sets are of size one, then
equality must hold.
(iii)⇒ (i): Let i,j ∈ [n] arbitrary but distinct and let us deﬁne
Γij :={κ(H)|H closed walk in G, (i,j )∈E(H)}.
Note that either Γ ij ={1} or Γ ij is inﬁnite as any cycle H can be traversed multiple times to
form a closed walk. Note that by (iii) we have for any i,j∈ [n] that
Γij⊆
⋃ {
Π (k,ℓ)∈E(H)Kk,ℓ|H closed walk in G, (i,j )∈E(H)
}
=Kij·Kji. (12)
The setKij·Kji is ﬁnite, implying that Γ ij ={1}. This, together with Theorem 5.2 gives (i).
A surprising ﬁnding by Lee [ Lee89, Lee90] is that if ˙κW is an odd prime power, then κ∗
W = 1
holds.1 We ﬁrst present a proof sketch following the lines of the one i n [ Lee89, Lee90]. We also
present a second, almost self-contained proof, relying onl y on basic results on TU matrices.
Theorem 5.5 (Lee [ Lee89, Lee90]). Each W for which ˙κW = pα where p∈ P, p >2, α∈ N,
then κ∗
W = 1.
Proof. A theorem by Tutte [ Tut65] asserts that W can be represented as the kernel of a uni-
modular matrix, i.e. κ∗
W = 1 or W has a minor W ′ such that C(W ′)∼=C(U 4
2 ) where U 4
2 is the
uniform matroid on four elements such that the independent s ets are the sets of cardinality at
most two. Here, a matroid minor corresponds to iteratively e ither deleting variables or project-
ing variables out. In the ﬁrst case we are done, so let us consi der the second case. Note that
W ′⊂ R4 and by Lemma 3.16 we have that for all i,j ∈ [4] we have that KW ′
ij ⊆K W
ij and so in
particular ˙κW ′ =pβ for some β≤α. An easy consequence of the proof of Proposition 3.18 and
the congruenceC(W ′)∼=C(U 4
2 ) is that W ′ can be represented by A′, i.e. ker(A′) = W ′ such that
A′ =
[1 0 pγ1 pγ2
0 1 pγ3 pγ4
]
(13)
for γi∈ N∪{ 0} and i∈ [4]. Further, by C(W ′)∼=C(U 4
2 ) and ∆ A′| ˙κW ′ (Proposition 3.18) we
have that
0⁄= det
(pγ1 pγ2
pγ3 pγ4
)
=pγ1+γ4−pγ2+γ3|pβ. (14)
It is immediate that ( 14) cannot be fulﬁlled for p> 2.
Alternative Proof of Theorem 5.5. LetA∈ Rm×n be such that A = ker(W ) satisfying the prop-
erties in Proposition 3.18 in basis form A = (Im|A′); for simplicity, assume the identity matrix
is in the ﬁrst m columns. Let G =
(
[n],E (G)
)
be a directed multigraph associated with A
with edge set E(G) = ⋃
k∈[m]Ek(G) where Ek(G) = {(i,j ) : AkiAkj ⁄= 0}. Further, deﬁne
γ : E(G)→ R+ where for e∈Ek we let γ(e) =|Akj/Aki|. For a directed cycle C inG we deﬁne
γ(C) := ∏
e∈E(C)γ(e).
Claim 5.5.1. All cycles C in G fulﬁll γ(C) = 1 .
Proof. For a contradiction, assume that there exists a cycle C such that γ(C)⁄= 1 and let C
be a shortest cycle with this property. Then C has no chord f∈ E(G), as otherwise C∪{f}
contains two shorter cycles C1,C 2 such that γ(C1)γ(C2) = γ(C) ⁄= 1 and so in particular
γ(C1)⁄= 1 or γ(C2)⁄= 1. This also means that the support of the corresponding sub matrix
AI,J of A where I :={i∈ [m] : Ei(G)∩E(C)⁄= 0} and J := V (C) is exactly the set of
1The statement in the paper is slightly more general, for k-adic subspaces with k > 2; the proof is essentially
the same.
21
non-zeros of an incidence matrix of a cycle. We have that det( AI,J )⁄= 0 as the corresponding
cycle C has γ(C)⁄= 1. Recall the Leibniz determinant formula. As AI,J is supported on the
incidence matrix of a cycle there exist only two bijective ma ps ϕ,ψ : I→ J, ϕ⁄= ψ such that∏
i∈IAi,ϕ(i)⁄= 0 ⁄= ∏
i∈IAi,ψ(i) is non-vanishing. One of the maps corresponds to traversing
the cycle forward, the other corresponds to traversing it ba ckwards. As all the entries of A are
powers ofp we therefore have that 0⁄= det(AI,J ) =±pα±pβ for some α,β ∈ N. This contradicts
Proposition 3.18(iii) for p> 2.
The above claim implies the existence of a rescaling of rows a nd columns ˜A :=LAR where
L∈ Dn,R∈ Dm such that ˜A∈{− 1, 0, 1}m×n. If ˜A is TU, then we are done by Proposition 3.2
as nowκ∗
W = 1. Otherwise, we use a result by Gomory (see [ Cam65] and [ Sch98, Theorem 19.3])
that states that any matrix B with entries in {−1, 0, 1} that is not totally unimodular has a
submatrix B′ with| det(B′)| = 2. Let I⊆ [m] and J⊆ [n] such that | det( ˜AI,J )| = 2. Note
that w.l.o.g. the diagonal entries of L and R are of the form pα for some α∈ Z. Therefore,
| det(AI,J )| = ∏
i∈ILii
∏
j∈JRjj| det( ˜AI,J )| = 2pβ for some β∈ Z. As | det(AI,J )|∈ N we must
haveβ≥ 0 and 2 || det(AI,J )|. This again contradicts Proposition 3.18(iii) for p> 2.
6 Hoﬀman proximity theorems
Hoﬀman’s seminal work [ Hof52] has analyzed proximity of LP solutions. Given P ={x∈ Rn :
Ax≤ b}, x0∈ Rn, and norms ‖.‖α and‖.‖β, we are interested in the minimum of ‖x−x0‖α
over x∈ P . Hoﬀman showed that this can be bounded as Hα,β(A)‖(Ax0−b)+‖β, where the
Lipschitz-bound Hα,β(A) is a constant that only depends on A and the norms. Such results
are known as Hoﬀman proximity bounds in the literature and have been extensively studied; we
refer the reader to [ GHR95, KT95, PVZ20] for references. In particular, they are related to δ
studied in Section 4.2, see e.g. [ GHR95].
In this section, we show a Hoﬀman-bound H∞,1 = κW for the system x∈ W +d, x≥ 0,
namely. Related bounds using ¯χA have been shown in [ HT02]. We then extend it to proximity
results on optimal LP solutions. These will be used in the bla ck-box LP algorithms in Section 7.1,
as well as for the improved analysis of the steepest descent c ircuit augmentation algorithm in
Section 8.4.
A central tool in this section are conformal decompositions into circuits as in Lemma 2.1.
The next proof is similar to that of Proposition 4.5.
Lemma 6.1. If the system x∈W +d, x≥ 0 is feasible, then the system
x∈W +d
‖x−d‖∞≤κW‖d−‖1
x≥ 0,
is also feasible.
Proof. Let x be a solution to LP(W,d,c ) such that ‖x−d‖∞ is minimal, and subject to that,
‖x−d‖1 is minimal. Let D ={i∈ [n] : di< 0 = xi}.
Take a conformal circuit decomposition of the vector x−d∈W as in Lemma 2.1 in the form
x−d = ∑ t
k=1gk for some t∈ [n]. We claim that supp( gk)∩D⁄=∅ for all k∈ [t]. Indeed, if
supp(gk)∩D =∅, then x′ =x−εgk for someε> 0 is another solution with‖x′−d‖∞≤‖x−d‖∞
and‖x′−d‖1 <‖x−d‖1.
Consider any index i /∈ D. For every elementary vector gk with i∈ supp(gk), there exists
an index j∈D such that|gk
i|≤ κW|gk
j|. By conformity,
|xi−di| =
⏐⏐⏐⏐⏐
t∑
k=1
gk
i
⏐⏐⏐⏐⏐ =
t∑
k=1
⏐⏐⏐gk
i
⏐⏐⏐≤κW
∑
j∈D
t∑
k=1
⏐⏐⏐gk
j
⏐⏐⏐ =κW
∑
j∈D
|dj|≤ κW‖d−‖1,
22
completing the proof.
We note that [ DNV20] also provides a strongly polynomial algorithm that, for a g iven z∈
W +d, and an estimate ˆκ onκW , either ﬁnds a solution as in Lemma 6.1, or ﬁnds an elementary
vector that reveals ˆκ>κ W .
We next provide proximity results for optimization. For vec tors d,c∈ Rn, let us deﬁne the
set
Λ(d,c ) := supp(d−)∪ supp(c+). (15)
Note that for c≥ 0,
‖‖dΛ(d,c)
‖‖
1 =‖d−‖1 +
‖‖‖d+
supp(c)
‖‖‖
1
. Consequently, if c≥ 0 and dΛ(d,c) = 0,
then x =d and s =c are optimal primal and dual solutions to LP(W,d,c ).
Lemma 6.2. If the system LP(W,d,c ) is feasible, bounded and c≥ 0, then there is an optimal
solution such that
‖x−d‖∞≤κW
‖‖dΛ(d,c)
‖‖
1.
Proof. Similarly to the proof of Lemma 6.1, let x be an optimal solution to LP(W,d,c ) chosen
such that ‖x−d‖∞ is minimal, and subject to that, ‖x−d‖1 is minimal; let D ={i∈ [n] :
di < 0 = xi}. Take a conformal circuit decomposition x−d = ∑ t
i=1gk for some t∈ [n].
With a similar argument as in the proof of Lemma 6.1, we can show that for each gk, either
supp(gk)∩D⁄=∅, or gk is an objective-reducing circuit, i.e.
⟨
gk,c
⟩
< 0. Since c≥ 0, the latter
requires that for some i∈ supp(gk), gk
i < 0 and ci > 0, implying i∈d+
supp(c). A similar bound
as in the proof of Lemma 6.1 completes the proof.
Lemma 6.3. Let W ⊆ Rn be a subspace and c,d ∈ Rn. Let (˜x,s ) be an optimal solution to
LP(W, ˜x,c ). Then there exists an optimal solution (x∗,s ∗) to LP (W,d,c ) such that
‖x∗− ˜x‖∞≤ (κW + 1)‖ΠW ⊥(d− ˜x)‖1 .
Proof. Letx = ˜x + ΠW ⊥(d− ˜x). Note that W +x =W +d, and also W ⊥ +s =W ⊥ +c. Thus,
the systems LP(W,d,c ) and LP(W,x,s ) deﬁne the same problem.
We apply Lemma 6.2 to (W,x,s ). This guarantees the existence of an optimal ( x∗,s ∗) to
LP(W,x,s ) such that
‖x∗−x‖∞≤κW‖xΛ(x,s)‖1 =κW
(‖‖x−‖‖
1 +
‖‖‖x+
supp(s)
‖‖‖
1
)
.
Since ˜x≥ 0, we get that ‖x−‖1≤‖ xsupp(x−)− ˜xsupp(x−)‖1. Second, by the optimality of
(˜x,s ), we have ˜xsupp(s+) = 0, and thus xsupp(s+) = xsupp(s+)− ˜xsupp(s+). These together imply
that
‖x∗− ˜x‖∞≤‖x∗−x‖∞ +‖x− ˜x‖∞≤ (κW + 1)‖x− ˜x‖1
= (κW + 1)‖ΠW ⊥(d− ˜x)‖1.
We can immediately use Lemma 6.3 to derive a conclusion on the support of the optimal
dual solutions to LP( W,d,c ), using the optimal solution to LP( W, ˜d,c ).
Theorem 6.4. Let W⊆ Rn be a subspace and c,d ∈ Rn. Let (˜x,s ) be an optimal solution to
LP(W, ˜x,c ) and
R :={i∈ [n] : ˜xi> (κW + 1)‖ΠW ⊥(˜x−d)‖1}.
Then for every dual optimal solution s∗ to LP(W,d,c ), we have s∗
R = 0.
Proof. By Lemma 6.3 there exists an optimal solution ( x′,s ′) to LP( W,d,c ) such that ‖x′−
˜x‖∞≤ (κW + 1)‖ΠW ⊥(d− ˜x)‖1. Consequently, x′
R > 0, implying s∗
R = 0 for every dual optimal
s∗ by complementary slackness.
23
In Section 8.4, we use a dual version of this theorem, also including upper b ound constraints
in the primal side. We now adapt the required proximity resul t to the following primal and dual
LPs, and formulate it in matrix language to conform to the alg orithm in Section 8.4.
min⟨c,x⟩
Ax =b,
0≤x≤u.
max⟨y,b⟩−⟨u,t⟩
A⊤y +s−t =c,
s,t≥ 0.
(16)
Note that any y ∈ Rm induces a feasible dual solution with si = ( ci−⟨ai,y⟩)+ and ti =
(⟨ai,y⟩− ci)+ for i∈ [n]. A primal feasible solution x and y∈ Rm are optimal solutions if and
only if⟨ai,y⟩≤ ci if xi<u i and⟨ai,y⟩≥ ci if xi> 0.
Theorem 6.5. Let (x′,y ′) be optimal primal and dual solutions to (16) for input (b,u,c ′), and
(x′′,y ′′) for input (b,u,c ′′). Let
R0 :={i∈ [n] :
⟨
ai,y ′⟩
<c ′
i− (κW + 1)‖c′−c′′‖1},
Ru :={i∈ [n] :
⟨
ai,y ′⟩
>c ′
i + (κW + 1)‖c′−c′′‖1}.
Then x′′
i = 0 for every i∈R0 and x′′
i =ui for every i∈Ru.
Proof. Let ¯A =
(A 0
In In
)
. It is easy to see that κ ¯A = κA. Let ¯d∈ R2n such that ¯A ¯d =
(b
u
)
.
With ¯c = (c, 0n), the primal system can be equivalently written as min ⟨¯c, ¯x⟩, ¯x∈ ker( ¯A) + ¯d,
¯x≥ 0. The statement follows by Theorem 6.4 applied for W = (ker( ¯A))⊥ = im( ¯A⊤).
