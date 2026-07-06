**Setup.**
We define the categorical structure over the commutative ring

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Every quantity below lives in $R$ and survives any ring map $\iota \colon R \to k$ to a target commutative ring $k$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe over $R$ with substrate parameter $q$ and force-carrier generators $T_{2,9}$ (crossing number $c_s = 9$) and $T_{3,5}$ (crossing number $c_w = 10$). The electromagnetic fine structure constant, defined as the $\tau$-trace of the singlet idempotent $e_-$ normalised by the force-carrier categorical complexity, is

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-integer.

To avoid division outside the integral Laurent subring $\mathbb{Z}[q, q^{-1}] \subset R$, we express this as the cleared-denominator relation

$$
  [9]_q \cdot [10]_q \cdot \alpha_{\mathrm{EM}} \;=\; q^{-1}.
$$

**Derivation.**
The electromagnetic coupling between two charged localized knots $(c_1, K_1)$ and $(c_2, K_2)$ factorises into three finite contributions.

*Layer 1: Charge.*
The electromagnetic charge of a knot $K$ is its $q$-writhe, the antisymmetric crossing count under the crossing reversal involution $\sigma$:

$$
  Q_q(K) =  [w(K)]_q
  =  \frac{q^{w(K)} - q^{-w(K)}}{q - q^{-1}}
$$

where $w(K) = \sum_i \epsilon_i \in \mathbb{Z}$ is the writhe. For a torus knot $T_{m,n}$, all crossings share the same sign, giving $w(T_{m,n}) = \pm m(n-1)$.

*Layer 2: Coupling strength.*
The two-strand spectral completeness theorem decomposes the braiding into central idempotents:

$$
  c_{A,A} \;=\; q^{1/2}\, e_+ \,-\, q^{-1/2}\, e_-,
  \qquad e_+ + e_- = \mathrm{id}_{A \otimes A},\;\; e_+ e_- = 0.
$$

The singlet $e_-$ projects onto the unique copy of the unit object $\mathbf{1} \subset A \otimes A$. Its fibre-functor trace evaluates to

$$
  |\mathrm{tr}_\tau(e_-)|^2 \;=\; q^{-1} \,\in\, R.
$$

By uniqueness of the singlet, this is the full scalar exchange amplitude.

*Layer 3: Force-carrier complexity.*
By the genus-$4$ uniqueness theorem, the force-carrier sector of a Bring-supported QOU is exactly the set $\{T_{2,9}, T_{3,5}\}$. Their categorical $q$-dimensions are $\dim_q T_{2,9} = [9]_q$ and $\dim_q T_{3,5} = [10]_q$. The product $[9]_q \cdot [10]_q$ is the categorical complexity of the force-carrier object. The electromagnetic coupling is the singlet trace divided by this normalisation:

$$
  \alpha_{\mathrm{EM}}
  \;=\;
  \frac{|\mathrm{tr}_\tau(e_-)|^2}{\dim_q T_{2,9} \cdot \dim_q T_{3,5}}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q} \,\in\, R.
$$

**Completeness.**
Plancherel completeness $w_+ + w_- = 1$ ensures no scalar channel is omitted. The Frobenius mass of $\mathrm{End}(A \otimes A)$ is exhausted by these two idempotents. The fine structure constant is a ring-theoretic invariant of the Descartes universe.
