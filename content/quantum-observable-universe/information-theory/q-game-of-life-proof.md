*Proof.* 
The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is built from $q$-Toffoli generators. By [Toffoli transfer matrix](#prop:toffoli-transfer-matrix), these act as elements of $H_3(q) \otimes \cdots \otimes H_3(q)$ on the tensor product of Reeb bundles $\bigotimes_i \mathcal{S}_{p_i}$. Each generator is unitary with respect to the Markov trace form (involution $\sigma_i \mapsto \sigma_i^{-1}$). Composition preserves unitarity, so $\mathcal{U}_{\mathrm{q\text{-}GoL}}^\dagger \mathcal{U}_{\mathrm{q\text{-}GoL}} = \mathbb{I}$. Reversibility follows from $\sigma_i^{-1} = \sigma_i$ modulo Hecke relations.

Universality follows from Bennett \cite{bennett1973}. Any reversible computation is simulated by Toffoli gates. Adding Hadamard gates promotes this to universal quantum computation \cite{fredkin1982, toffoli1980}.

The bandwidth bound follows by counting. Each $\mathrm{Toff}_q$ in the $3$-strand Hecke algebra requires three elementary crossings, taking three Planck steps. One generation applies one Toffoli gate per neighbour triple. This yields the stated bound.

The stability condition requires $P_{7,7}(q) \neq 0$ and $\Phi(q) \neq 0$. Both inequalities hold for $q > 1/\varphi^2$ by direct evaluation ([Toffoli LP-stability](#prop:toffoli-lp-stability)). $\square$
