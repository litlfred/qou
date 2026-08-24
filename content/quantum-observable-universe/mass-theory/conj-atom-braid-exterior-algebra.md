**Conjecture (atom-braid exterior-algebra structure).**
*Let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word. Its image in $H_{3A}(q)$ generates a sub-algebra whose Gröbner-Shirshov normal-form filtration shape is given by:*

$$
  \dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{k - (Z - 1)}.
$$

*The sub-algebra is isomorphic to the exterior algebra $\Lambda^*(R^{3A - Z})$ with grade shift $\delta = Z - 1$.*

The canonical atom-braid populates a fermion Fock-space subalgebra of $H_{3A}(q)$. Each interface between adjacent strands contributes one binary degree of freedom. The proton count $Z$ enforces dimension reduction (removing one degree of freedom per proton) and a grade shift (offsetting the filtration bound).

This exterior structure restricts the active dimension. For $^4\mathrm{He}$, the dimension collapses from the $12!$ standard Wedderburn basis to exactly $2^{10} = 1024$. The restriction governs the computational complexity of the canonical solver.
