---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-012-72-layered-least-squares-interior-point-methods
section_title: "Layered least squares interior point methods"
section_number: 7.2
pages: 26-28
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
In this section, we brieﬂy review layered least squares (LLS ) interior-point methods, and high-
light the role of the circuit imbalance measure κW in this context. The central path for the
standard log-barrier function is the parametrized curve gi ven by the solutions to the system
following system for µ∈ R++
Ax =b
A⊤y +s =c
xisi =µ ∀i∈ [n]
x,s> 0
(17)
A unique solution for each µ> 0 exist whenever LP(A,b,c ) possesses strictly feasible primal and
dual solutions, i.e. primal resp. dual solutions with x >0 resp. s >0; the duality gap between
these solutions is nµ. The limit point at µ→ 0 gives a pair of primal and dual optimal solutions.
At a high level, interior point methods require an initial so lution close to the central path for
some large µ and proceed by following the central path in some proximity t owards smaller and
smaller µ, which corresponds to converging to an optimal solution. A s tandard variant is the
Mizuno–Todd–Ye [MTY93] predictor-corrector method. This alternates between predictor and
corrector steps. Each predictor step decreases the parameter µ at least by a factor (1 −β/√n),
but moves further away from the central path. Corrector step s maintain the same µ but restore
better centrality.
Let us now focus on the predictor step at a given point ( x,s ); we use the subspace notation
W = ker(A), W ⊤ = im(A⊤) as in LP(W,d,c ). The augmentation direction is computed by the
aﬃne scaling (AS) step , that can be written as weighted least squares problems on th e primal
and dual sides:
∆ x := arg min
{ ∑
i∈[n]
(xi + ∆ xi
xi
)2
: ∆ x∈W
}
∆ s := arg min
{ ∑
i∈[n]
(si + ∆ si
si
)2
: ∆ s∈W ⊥
} (18)
The update is then performed by setting x← x +α∆ x, s← s +α∆ s for some α∈ [0, 1]. As
such, this algorithm can ﬁnd ε-approximate solutions in weakly polynomial time. However , it
does not even terminate in ﬁnitely many iterations, because using the weighted ℓ2-regressions
problems ( 18) will never set variables exactly to 0 as required by complem entary slackness. For
standard interior point methods, a ﬁnal rounding step is req uired.
The layered least squares interior-point method by Vavasis and Ye [VY96] not only terminates
ﬁnitely, but has an iteration bound of O(n3.5 log( ¯χW +n)), depending only on A, but independent
of b and c. We will refer to this as the VY algorithm.
Recall from Theorem 4.2 that log( ¯χA +n) = Θ(log( κA +n)). For certain predictor iterations,
they use a layered least squared (LLS) step instead of aﬃne scaling. Variables are split into layer s
according to the xi values: we order the variables as x1≥x2≥... ≥xn, and start a new layer
whenever there is a big gap between consecutive variables, i .e. xi > O(n2) ¯χAxi+1. For a point
(x,s ) on the central path, the ordering on the si’s will be approximately reverse.
We illustrate their step based on a partition of the variable set [n] into two layersB∪N = [n];
the general step may use an arbitrary number of layers. The la yered least squared step is given
26
in a 2-stage approach via
∆ xll
N := arg min
{ ∑
i∈N
(xi + ∆ xi
xi
)2
: ∆ xN∈πN (W )
}
,
∆ xll
B := arg min
{ ∑
i∈B
(xi + ∆ xi
xi
)2
: (∆ xB, ∆ xN )∈W
}
,
∆ sll
B := arg min
{ ∑
i∈B
(si + ∆ si
si
)2
: ∆ sB∈πB(W ⊥)
}
,
∆ sll
N := arg min
{ ∑
i∈N
(si + ∆ si
si
)2
: (∆ sB, ∆ sN )∈W ⊥
}
.
(19)
Whereas the predictor-corrector algorithm—as most standa rd interior point variants—is invari-
ant under rescaling the columns of the constraint matrix, th e VY algorithm is not: the layers are
chosen by comparing the xi values. For this reason, it was long sought to ﬁnd a scaling-i nvariant
version of [ VY96], that would automatically improve the running time depend ence from ¯χW to
the best possible value ¯χ∗
W achievable under column rescaling. In this line of work fall the results
of [ MT08, MT03, MT05], but none of them achieving dependence on the constraint ma trix only
while being scaling-invariant.
This question was ﬁnally settled in [ DHNV20] in the aﬃrmative. A key ingredient is re-
vealing the connection between ¯χW and κW . Preprocessing the instance via the algorithm in
Theorem 5.1 to ﬁnd a nearly optimal rescaling for κW (and thus for ¯χW ), and then using the
VY algorithm already achieves O(n3.5 log( ¯χ∗
W +n)). Beyond this, [ DHNV20] also presents a new
LLS interior point method based on the pairwise circuit imba lancesκij that is inherently scaling
invariant, as well as an improved analysis of O(n2.5 log(n) log( ¯χ∗
W +n)) iterations. We give an
outline next. Details are omitted here, a self-contained ov erview can be found in [ DHNV20].
What determines a good layering? We illustrate the LLS step in the following hypothetical
situation. Assume that the partition B∪N is such that x∗
N = 0 and s∗
B = 0 for optimal
primal and dual solution ( x∗,s ∗) to LP(W,d,c ). In particular, the LLS direction in ( 19) will set
∆ xll
N =−xN . Note that this does not hold for the AS direction ∆ xN that solves ( 18). This
beneﬁt of the LLS direction over the AS direction will result in us being able to choose α larger
for the LLS step compared to the AS step.
To terminate with an optimal solution in a single step, we nee d to be able to select the
step size α = 1, which requires that xB + ∆ ll
B ≥ 0. But as in the computation of ∆ xll
N the
components in B are ignored we need to ensure the choice of ∆ xll
N does not impact ∆ xll
B by too
much. By that we mean that there is a vector z∈ RB such that|zi/xi|≪ 1 for all i∈B and
(z, ∆ xN )∈W . The norm of this z is exactly governed by the lifting operator we introduced in
Section 4.1. Let Wx = diag(x)−1W ={(wi/xi)i∈[n] : w∈W} denote the space W rescaled by
the 1/xi values. Then,
‖‖‖
(zi
xi
)
i∈B
‖‖‖ =
‖‖‖LW x
N
((∆ xll
i
xi
)
i∈N
)‖‖‖≤‖LW x
N ‖·
‖‖‖
(∆ xll
i
xi
)
i∈N
‖‖‖. (20)
By Lemma 4.5, note that ‖‖‖
(zi
xi
)
i∈B
‖‖‖≤nκW x
‖‖‖
(∆ xi
xi
)
i∈N
‖‖‖. (21)
Further, notice that the lifting cost imposed on variables i n B by ∆ xll
N are given by the circuit
imbalances in the rescaled space Wx: For i∈B andj∈N we are interested in κW x
ji =κjixj/xi.
In particular, if these quantities are small for all i∈ B and j∈ N , then the low lifting cost
discussed above is achieved and we can select stepsize α = 1.
27
The choice of layers The Vavasis-Ye algorithm deﬁnes the layering based on the ma gnitude
of the elements xi. This guarantees that κjixj/xi is small since xi > O(n2)κAxj if i is on a
higher layer than j. However, this choice is inherently not scaling-invariant .
The LLS algorithm in [ DHNV20] directly uses the scaling invariant quantities κjixj/xi to
deﬁne the layering. In the ideal version of the algorithm, th e layers are selected as the strongly
connected components of the directed graph formed by the edg es where this value is large.
Hence, κjixj/xi is small whenever i is on a higher layer than j.
This ideal version cannot be implemented since the pairwise imbalances κji are hard to
compute or even approximate. The actual algorithm instead w orks with lower estimates ˆκji.
Thus, we may miss some edges from the directed graph, in which case the lifting may fail. Such
failure will be detected in the algorithm, and in turn reveal s better estimates for some pairs
(i,j ).
