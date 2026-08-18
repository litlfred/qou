*Proof.* 
The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is built from $q$-Toffoli generators. By [Toffoli transfer matrix](#prop:toffoli-transfer-matrix), these act as elements of $H_3(q) \otimes \cdots \otimes H_3(q)$ on the tensor product of Reeb bundles $\bigotimes_i \mathcal{S}_{p_i}$. Each generator is unitary with respect to the Markov trace form (involution $\sigma_i \mapsto \sigma_i^{-1}$). Composition preserves unitarity, so $\mathcal{U}_{\mathrm{q\text{-}GoL}}^\dagger \mathcal{U}_{\mathrm{q\text{-}GoL}} = \mathbb{I}$. Reversibility follows from the invertibility of each generator in $H_n(q)$: the quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ gives the explicit inverse
$$
  \sigma_i^{-1} = \sigma_i - (q - q^{-1})\cdot 1 ,
$$
so every $\sigma_i$ is a unit and the composite is invertible. The generators are *not* involutions at generic $q$: $\sigma_i^{-1} = \sigma_i$ holds precisely when $q = q^{-1}$, i.e. in the classical limit $q \to 1$, which is where the $q$-Toffoli reduces to the ordinary Toffoli gate.

Universality follows from Bennett \cite{bennett1973}. Any reversible computation is simulated by Toffoli gates. Adding Hadamard gates promotes this to universal quantum computation \cite{fredkin1982, toffoli1980}.

The bandwidth bound follows by counting. Each $\mathrm{Toff}_q$ in the $3$-strand Hecke algebra requires three elementary crossings, taking three Planck steps. One generation applies one Toffoli gate per neighbour triple. This yields the stated bound.

The stability condition requires $P_{7,7}(q) \neq 0$ and $\Phi(q) \neq 0$. Both inequalities hold for $q > 1/\varphi^2$ by direct evaluation ([Toffoli LP-stability](#prop:toffoli-lp-stability)). $\square$
