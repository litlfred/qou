The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is built
from $q$-Toffoli generators which, by
[Toffoli transfer matrix](#prop:toffoli-transfer-matrix), act
as elements of $H_3(q) \otimes \cdots \otimes H_3(q)$ on the
tensor product of Reeb bundles $\bigotimes_i \mathcal{S}_{p_i}$.
Each generator is unitary with respect to the Markov trace
form (involution $\sigma_i \mapsto \sigma_i^{-1}$), and the
composition of unitaries is unitary — so
$\mathcal{U}_{\mathrm{q\text{-}GoL}}^\dagger
\mathcal{U}_{\mathrm{q\text{-}GoL}} = \mathbb{I}$. Reversibility
is immediate from $\sigma_i^{-1} = \sigma_i$ up to Hecke
relations.

Universality follows from Bennett \cite{bennett1973}: any
reversible computation is simulated by Toffoli gates, and the
addition of Hadamard $H$ promotes this to universal quantum
computation \cite{fredkin1982, toffoli1980}.

The bandwidth bound follows by counting: each
$\mathrm{Toff}_q$ in the $3$-strand Hecke algebra requires
three elementary crossings (one per strand pair), hence three
Planck steps. A generation applies one Toffoli per neighbour
triple, giving the stated bound.

The stability condition reduces to requiring
$P_{7,7}(q) \neq 0$ and $\Phi(q) \neq 0$; both hold for
$q > 1/\varphi^2$ by direct evaluation
([Toffoli LP-stability](#prop:toffoli-lp-stability)).
$\qquad\blacksquare$
