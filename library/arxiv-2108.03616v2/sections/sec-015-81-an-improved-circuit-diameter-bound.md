---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-015-81-an-improved-circuit-diameter-bound
section_title: "An improved circuit diameter bound"
section_number: 8.1
pages: 29-29
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
In a recent paper Dadush et al. [ DKNV21] gave the following bound on the circuit diameter:
Theorem 8.1 ([DKNV21]). An LP of the form LP(A,b,c,u ) has circuit diameter boundO(m2 log(m+
κA) +n logn).
Let us highlight the main ideas to prove Theorem 8.1. The argument is constructive but
non algorithmic in the sense that the augmentation steps are deﬁned using the optimal solution.
We ﬁrst show the bound in Theorem 8.1 for LP(A,b,c ) (i.e., without upper bounds u) and
then extend the argument to systems of form LP(A,b,c,u ). Let x∗ be a basic optimal solution
to LP(A,b,c ) corresponding to basis B, and let N = [n]\B. Thus, x∗ is the unique optimal
solution with respect to the cost vector c = (0B, /BD
N ).
For the current iterate x(t), consider a conformal circuit decomposition h1,...,h k ofx∗−x(t),
and select a circuit hi,i∈ [k] such that ‖hi
N‖1 is maximized. We ﬁnd the next iterate x(t+1) =
x(t) +αhi for the maximal stepsize α > 0. Note that the existence of such a decomposition
does not yield a circuit diameter bound n due to the maximality requirement in the deﬁnition
of circuit walks. Nonetheless, it can be shown that we will no t overshoot hi by too much.
More precisely, one can show that the step length will be α∈ [1,n ]. Further, the choice of hi
guarantees that‖x(t)
N‖1 decreases geometrically.
The analysis focuses on the index sets Lt ={i∈ [n] : x∗
i >nκ A‖x(t)
N‖1} and Rt ={i∈ [n] :
x(t)
i ≤nx∗
i}. For every i∈Lt, xi must already be ‘large’ and cannot be set to zero later in the
algorithm; Rt is the set of indices that have essentially ‘converged’ to th e ﬁnal value x∗
i . Since
‖x(t)
N‖1 is decreasing, once an index enters Lt, it can never leave again. The same property can
be shown for Rt. Moreover, a new index is added to either set Rt orLt everyO(m log(m +κA))
iterations, leading to the overall bound O(m2 log(m +κA)).
For a system LP(A,b,c,u ) with upper bounds u, the above argument yields a bound O(n2 log(n+
κ)) using a simple reduction. To achieve a better bound, [ DKNV21] gives a preprocessing se-
quence of O(n logn) circuit augmentations that reduces the number of variable s to ≤ 2m.
This preprocessing terminates once the set of columns in AD are linearly independent for
D ={i∈ [n] : x∗
i ⁄= xi and x∗
i ∈{ 0,ui}}. Since a basic solution x∗ may have ≤ m entries
not equal to the lower or upper bound, at this point there are ≤ 2m variables xi⁄= x∗
i . This
leads to a circuit diameter bound of O(m2 log(m +κA) +n logn).
