By obligation (C) ([Body order equals jet degree](#lem:bond-order-eq-jet-degree)),
the binding is the body-order series,
$B(K)=\sum_{n}\,(\text{$n$-body term})$. By the conditional input (B), each
body term factors as $B_n = m_e\,a_D^{(n)}$. Substituting and pulling the
common scale $m_e$ out of the (finite) sum,

$$
B(K) \;=\; \sum_n B_n \;=\; \sum_n m_e\,a_D^{(n)} \;=\; m_e\sum_n a_D^{(n)} .
$$

Rewriting each period through the residue form
([The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum)) gives the second
displayed equality of the statement; the growth law of the $a_D^{(n)}$ is the
solution of the $q$-difference recurrence
([The binding generating function's q-difference equation gives a depth-d recurrence](#prop:binding-genfun-qdifference)). The
Lean witness [`QOU.Mass.binding_closure_conditional`](#thm:binding-closure-conditional)
carries (C) and (B) as the fields of the class `BindingClosureInput` and
derives the closed form by `Finset.mul_sum` and `Finset.sum_congr` — fully
verified modulo the class instance, which is exactly input (B). $\qquad\blacksquare$
