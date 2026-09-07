---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-007-centering-the-linear-program
section_title: "Centering the linear program"
section_number: null
pages: 13-14
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Initially, we consider the linear programF(A,b,ℓ,u,c). In order to detect reflection
symmetries, we would like to center each variable at the center of its domain. This
can be achieved using an affine transformation that offsets the variables.
Proposition 5For any scalarδ∈R,x∈P(A,b,ℓ,u)holds if and only ifx ′ :=x−δ∈
P(A,b−Aδ,ℓ−δ,u−δ)holds. Moreover,c ⊺x′ =c ⊺x−c ⊺δholds.
13
ProofIt is sufficient to observe thatAx=b⇐⇒Ax−Aδ=b−Aδ⇐⇒Ax ′ =b−Aδ
and thatℓ≤x≤u⇐⇒ℓ−δ≤x−δ≤u−δ⇐⇒ℓ−δ≤x ′≤u−δ. Moreover,
c⊺x′ =c ⊺x−c ⊺δfollows by definition ofx′.□
The main idea that we use Proposition 5 for in the context of equitable partitions
is that thatF(A,b−Aδ,ℓ−δ,u−δ,c)may admit a coarser equitable partition than
F(A,b,ℓ,u,c). We note that there are infinitely many choices forδto do so, so it
is not clear howδmay be chosen. Frequently, we use Proposition 5 to center the
variables at their domains by usingδw := uw+ℓw
2 . For variables with infinite lower or
upper bounds, such a centeredδw value is not well-defined. Later on, we will clarify
how one should chooseδw in such cases. For now, we analyze the equitable partitions
ofF(A,b−Aδ,ℓ−δ,u−δ,c)for any finiteδ∈R.
Furthermore, we note thatδcorresponds to an offset of the primal variables. It
is also possible to expand the results in this work by using an offset for the dual
variables, which corresponds to adding weighted multiples of the rows to the objective.
One could hope that doing so may help to construct additional variables that have
identical objective value, which would lead to potentially coarser equitable partitions.
In order to simplify the presentation, we do not consider this extension here.
