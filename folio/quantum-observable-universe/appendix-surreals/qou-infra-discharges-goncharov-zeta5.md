**Conjecture (QOU's Hecke-NF + Bring-$S_5$ infrastructure discharges Goncharov's depth-3 conjecture at $F = \mathbb{Q}(\zeta_5)$).**

The depth-2 identification ([Depth-2 identification of $G^{(2)}(\mathcal{H}_q)$ with $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$](#prop:depth-2-identification-bloch-suslin)) is theorem-level via Bloch–Suslin. The depth-3 case requires Goncharov's motivic conjecture. The proposal is that QOU's infrastructure discharges Goncharov's conjecture for $F = \mathbb{Q}(\zeta_5)$. The motivic setting for polylogarithm values at $N$-th roots of unity, here $N = 5$, is the motivic fundamental group of $\mathbb{P}^1 \setminus \{0, \infty, \mu_N\}$, constructed in the category of mixed Tate motives over $\mathbb{Z}[\zeta_N, 1/N]$ in \cite[\S5]{deligne-goncharov2005}.

Goncharov's conjecture asserts $K_5^{\mathrm{ind}}(F) \otimes \mathbb{Q} \cong \mathfrak{B}_3(F) \otimes \mathbb{Q}$, with $\mathfrak{B}_3(F)$ the weight-3 Bloch group modulo the 22-term relation. For $F = \mathbb{Q}(\zeta_5)$, Borel gives $\dim_\mathbb{Q} K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q} = 2$. The Goncharov regulator maps this rank-2 space into $\mathcal{P}_3 / \mathcal{P}_2$ over $\mathbb{Q}(\zeta_5)$.

The reduced target for QOU is to prove that $\{\mathrm{Li}_3(\zeta_5^k) : k = 1, 2, 3, 4\}$ modulo the multiplication-formula identity span exactly this rank-2 image, with the only further relation being the Goncharov 22-term restricted to $\zeta_5$-arguments.

See [Table 1](#tbl:qou-infra-discharges-goncharov-zeta5-table1-data).

**First route — Jones-coincident pair generation.**
For each Jones-coincident pair of Bring-embeddable knots $(K_1, K_2)$ with $J_{K_1}(q) = J_{K_2}(q) \in \mathbb{Z}[q^{\pm 1}]$, there is a depth-2 equality $\mathrm{Vol}(K_1) = \mathrm{Vol}(K_2)$ and a depth-3 equality $\mathrm{CS}(K_1) = \pm\mathrm{CS}(K_2)$. Enumerating Jones-coincident pairs yields a generating list of depth-3 relations among CS invariants. If these relations span the kernel of $K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q} \to \mathbb{R}/\pi^4\mathbb{Q}$, then Goncharov's conjecture at $\mathbb{Q}(\zeta_5)$ is implied by Hecke NF redundancy.

**Second route — direct construction of the 22-term-style relation.**
Express Goncharov's 22-term relation restricted to $z \in \{\zeta_5^k\}$ as an element $G_{22}(\zeta_5) \in \mathbb{Q}\langle \mathrm{Li}_3(\zeta_5), \mathrm{Li}_3(\zeta_5^2), \ldots \rangle$ that equals $0$ modulo $\mathcal{P}_2$. Find a Hecke element $\beta \in H_n(q)$ such that $\tau_{\mathrm{arch}}(\mathrm{tr}_M(\beta))$ at $q \to \zeta_5$ equals $G_{22}(\zeta_5)$, and the Hecke NF of $\beta$ reduces to the identity element modulo depth-$\leq 2$ terms. Then $\mathrm{tr}_M(\beta) = 0 \pmod{\text{depth} \leq 2}$, so $G_{22}(\zeta_5) = 0$ in $\mathcal{P}_3 / \mathcal{P}_2$ by NF reduction alone.

If either route succeeds, one specific cyclotomic case is closed.

See [Table 2](#tbl:qou-infra-discharges-goncharov-zeta5-table2-data).
