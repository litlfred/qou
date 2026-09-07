---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-011-71-a-black-box-algorithm
section_title: "A black box algorithm"
section_number: 7.1
pages: 25-26
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
The LP feasibility and optimization algorithms in [ DNV20] rely on a black-box subroutine
for approximate LP solutions, and use their outputs to ﬁnd ex act primal (and dual) optimal
solutions in time poly( m,n, log(¯κA +n)). For the black-box, one can use the fast interior-point
algorithms cited above.
More precisely, we require the following approximately fea sible and optimal solution ˜ x to
LP(W,d,c ) in time poly( n,m ) log((¯κA +n)/ε)
)
. Here OPT LP denotes the objective value of
LP(W,d,c ).
⟨c, ˜x⟩≤ OPTLP +ε‖c‖·‖ d‖
˜x∈W +d
‖˜x−‖≤ ε‖d‖
˜x∈ Rn
(APX-LP)
The feasibility algorithm makes O(m) calls, and the optimization algorithm makes O(nm) calls
to such a subroutine for ε = 1/(¯κA +n)O(1).
We now give a high-level outline of the feasibility algorith m in [ DNV20] for the system
x ∈ W +d, x ≥ 0. For the description, let us assume this system is feasible ; in case of
infeasibility, the algorithm recovers a Farkas-certiﬁcate. The main progress step in the algorithm
is reducing the dimension m of the linear space W by one, based on information obtained form
an approximate solution ˜x to ( APX-LP). We can make such an inference using the proximity
result Lemma 6.1.
If ˜x≥ 0 for the solution returned by the solver, we can terminate wi th x = ˜x. Otherwise,
let I⊆ [n] denote the set of ‘large’ coordinates of ˜x, i.e., where ˜xi>κ W‖˜x−‖1. By Lemma 6.1,
there must exist a feasible solution x∈ W +d, x≥ 0 such that xi is still suﬃciently large
for i∈ I. Therefore, one can drop the sign-constraint on I, as non-negativity can be enforced
automatically. We recurse on πJ (W ) for J = [n]\I, i.e. project out the variables in I.
Each recursive call decreases the dimension of the subspace , until a feasible vector is found.
The feasible solution on the remaining variables now has to b e lifted to the variables we projected
out, to get a feasible solution to the original problem x∈ W +d, x≥ 0. We use the lifting
operator LW
J (p) introduced in Section 4.1: for p∈ πJ (W ), z = LW
J (p) is the minimum-norm
vector in W such that zJ =p. According to Proposition 4.5,‖z‖∞≤κW‖p‖1; this bound can
be used to guarantee that the lifted solution is nonnegative on I.
Algorithm 1 gives a simpliﬁed description of the feasibility algorithm of [ DNV20]. For sim-
plicity, we ignore the infeasibility case and the details of the Adjust(d) that may replace d by
it projection to W ⊥ in certain cases. This is needed to ensure I ⁄=∅. Further, we omit an
additional proximity condition from the approximate syste m APX-LP.
Algorithm 1: Feasibility-Simplified
Input : Instance of LP(W,d,c ), ε> 0, with c = 0n.
Output: Feasible solution to the system in Lemma 6.1
1 d← Adjust(d) ; ⊲ Occasionally applies a projection
2 if d∈W then return 0n ;
3 ˜x← APX-LP(W,d, 0n,ε ) ; ⊲ Provided by Black box solver
4 I←{i : ˜xi≥κW‖˜x−‖},J ← [n]\I,;
5 z← Feasibility-Simplified(πJ (W ),dJ,ε );
6 return
[˜xI + [LW
J (z− ˜xJ )]I
z
]
As stated here, the computation complexity is dominated by t he at most m recursive calls
to the solver for the system ( APX-LP).
25
In [DNV20], these techniques are also extended to solve the minimum-c ost problem LP(W,d,c )
for arbitrary cost vector c∈ Rn. The optimization algorithm makes O(m) recursive calls to the
approximate solver to identify a variable xi that must be 0 in every optimal solution; this is
deduced using Theorem 6.4.
