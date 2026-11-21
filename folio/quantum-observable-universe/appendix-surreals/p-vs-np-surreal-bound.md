Express the Reeb-period complexity argument of [P vs NP in the QOU](#conj:p-vs-np-qou) as a literal surreal inequality.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), and let $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). A $q$-substrate computation accesses the Reeb-period budget $\Omega_q \asymp \varepsilon^{-1}$ ([surreal rate calculus](#prop:surreal-rate-calculus)). A classical computation accesses the mass-gap budget $\Delta_q \asymp \varepsilon^3$ per elementary step.

For an NP-complete instance of size $n$, let $\delta_n > 0$ denote the per-step standard-real efficiency of the $q$-algorithm. A classical simulation of the $q$-algorithm requires $2^n \cdot \delta_n^2 \cdot \Omega_q$ elementary steps to replicate a full Reeb holonomy. The mass-gap budget available over the same Reeb period is $2^n \cdot \Delta_q$. By [surreal squeeze](#lem:surreal-squeeze),

$$
\delta_n^2 \cdot \Omega_q \asymp \delta_n^2 \cdot \varepsilon^{-1} > \varepsilon^3 \asymp \Delta_q \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Multiplying through by the standard-real factor $2^n$ preserves the inequality. In $\omega$-adic form ([Big-O via $\ordw$](#rem:conway-normal-form)), $\ordw(2^n \cdot \delta_n^2 \cdot \Omega_q) = 1 > -3 = \ordw(2^n \cdot \Delta_q)$. The classical simulation sits at strictly higher $\omega$-order than the classical budget.

The classical simulation of any non-trivial $q$-algorithm (standard-real efficiency $\delta_n > 0$) exceeds its classical budget by a full $\omega$-order. Taking the standard part ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)) collapses the transfinite advantage of the $q$-algorithm. Under $\mathrm{st}_{\varepsilon \to 0}$, the $2^n$-fold Reeb speed-up is lost. Therefore, the classical complexity classes $\mathbf{P}$ and $\mathbf{NP}$ cannot be identified via the standard-part map, supporting [P vs NP in the QOU](#conj:p-vs-np-qou).

This remark does not prove $\mathbf{P} \neq \mathbf{NP}$ classically. It shows that the QOU framework propagates the separation $\mathbf{P} \subsetneq \mathrm{BQP}_q$ at positive $\varepsilon$ (a widely believed non-classical separation) to the classical separation under the standard-part map.

The classical NP-completeness structure is preserved by the standard part. Any Cook--Levin reduction on the $q$-substrate descends to a classical Cook--Levin reduction. Combined with the surreal squeeze above, the separation $\mathbf{P} \neq \mathbf{NP}$ follows from the strict inclusion at positive $\varepsilon$ and the non-compressibility witness of [P vs NP in the QOU](#conj:p-vs-np-qou).

Unlike the RH, NS, and Collatz bounds, the P-vs-NP squeeze is conditional on an independent conjecture (non-compressibility of $\mathrm{BQP}_q \to \mathbf{P}$ as $\varepsilon \to 0$). This places P-vs-NP in the conditional millennium-problem column.
