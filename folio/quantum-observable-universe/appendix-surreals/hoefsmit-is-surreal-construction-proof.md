## Proof sketch

The Hoefsmit seminormal basis is built by inductively decomposing
$V^{\otimes n}$ via the chain
$H_1(q) \subset H_2(q) \subset \cdots \subset H_n(q)$. At each step
$k$, every existing eigenvector $v_t$ for $H_k(q)$ splits
under $\sigma_k$ into:

- $a^+_t \cdot v_{t \cup \square_{k+1}^{\to}}$ (extend tableau
  rightward; $q$-eigenvalue);
- $a^-_t \cdot v_{t \cup \square_{k+1}^{\downarrow}}$ (extend
  tableau downward; $-q^{-1}$-eigenvalue).

Conway's surreal construction at stage $k$ takes each existing
surreal $x$ with sign-sequence $s$ and produces *exactly two*
new surreals: $x^+$ (insert $+$ at position $k+1$) and $x^-$
(insert $-$ at position $k+1$). The embedding $\Phi$ matches each
tableau splitting with the corresponding sign extension
step-by-step. The tableau side, however, produces the antisymmetric
child only when the two-row shape constraint permits it (a box can
be added to the second row of $\lambda = (\lambda_1, \lambda_2)$
only if $\lambda_2 < \lambda_1$), while Conway's construction always
splits both ways — which is exactly why $\Phi$ is injective but not
surjective: the unmatched sign sequences are the non-tableau dyadic
rationals identified in the statement.

Compatibility with sums is forced by the eigenvalue convention:
$\sigma_i$'s $q$-eigenspace + $-q^{-1}$-eigenspace decomposition
matches Conway's $\{L \mid R\}$ pairing $L < x < R$.

For tableaux of shape $\lambda$ with $\ell(\lambda) \leq 2$, the
restriction to "first or second row" is exactly the $\mathrm{SU}(2)$
constraint that limits Young diagrams to two-rowed shapes —
giving the *binary* (rather than $r$-ary) split needed for the
sign-sequence interpretation.

Completing the step-by-step verification reduces to three ingredients:

- the Young--Jucys--Murphy successor relation on two-row standard tableaux;
- Gonshor's sign-sequence-to-surreal bijection on dyadic rationals;
- matching the eigenvalue conventions ($q$ and $-q^{-1}$ on the Hoefsmit side versus left/right cuts around the midpoint on the Conway side) along the [sign sequence functor](#def:sign-sequence-of-braid).
