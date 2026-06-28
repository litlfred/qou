Proof-scope commentary for the categorical linking operation
$\mathrm{Lk}_R^{(k)}$: which of its five properties are generic
categorical facts and which depend on substrate-specific ribbon /
Hecke / Markov structure.

### Proof scope, Property 1 (linearity)

This proof uses only the $R$-linear
rigid-monoidal-category axioms; it makes no assumption about the
specific ribbon structure of the QOU substrate, the Hecke
algebra, or the Markov trace. So linearity holds for **any**
rigid monoidal $R$-linear category in which the trace-cut
definition makes sense — it is a generic categorical fact, not a
QOU-specific statement.

### Proof scope, Property 3 (multiplicativity in $k$)

Like Properties 1 and 2, this proof uses only generic categorical
axioms: the integer-power group law of an endomorphism in a monoidal
category + composition associativity. It holds in **any** $R$-linear
rigid braided monoidal category — generic categorical fact.

The "post-trace" multiplicativity statement
$\mathrm{Lk}_R^{(k_1 + k_2)}(a, b) = c_{A, A}^{\,k_2} \cdot
\mathrm{Lk}_R^{(k_1)}(a, b)$ as written in the original
formulation requires an additional substrate-specific identity
(commutation of the trace-cut with the c-line subalgebra in
$\mathrm{End}(A \otimes A)$). That identity is **not** generic —
it relies on the substrate's specific ribbon-trace structure. The
pre-trace multiplicativity proved above is the **generic
categorical content** of Property 3; the post-trace upgrade is
substrate-specific and remains open.

### Proof scope, Property 2 ($k = 0$ reduction)

The proof uses six ingredients:

1. integer-power identity $c^0 = \mathrm{id}$ (definition);
2. unital composition (category axiom);
3. monoidal-tensor associativity (monoidal axiom);
4. tensor-functoriality of composition (monoidal axiom);
5. unit isomorphism $\mathbf{1} \otimes A \cong A$ (monoidal axiom);
6. $R$-linearity of $\tau_R$ to extract the scalar factor.

None of these requires the QOU-specific ribbon / Hecke / Markov
structure. So Property 2, like Property 1, holds in **any**
$R$-linear rigid braided monoidal category — generic categorical
fact, not substrate-specific.

The remaining three properties (multiplicativity in $k$,
trace-cut symmetry, bar-involution compatibility) **do** depend
on the substrate's specific ribbon structure (specifically on the
behavior of $c_{A, A}$ under iteration and on its relation to the
Frobenius pairing); they are open.

### Proof scope, Property 4 (trace-cut symmetry)

Two substrate-specific axioms cited: Markov-trace cyclicity +
braiding inversion. Both hold in the QOU substrate (Hecke algebra
$H_n(q)$ over $R$ with canonical Markov trace) and more generally in
any rigid braided ribbon $R$-linear monoidal category. The
combinatorial step (the exponent shift $k - 1 \mapsto -k$) is the
**single non-trivial categorical content**.

### Proof scope, Property 5 (bar-involution compatibility)

One substrate-specific axiom cited: bar-involution functoriality
(with $\iota(c) = c^{-1}$ and $\iota(\tau_R) = \tau_R$). Once that
holds, the property follows by direct computation. Bar-functoriality
is the categorical analog of the Hecke antipode $\iota(\sigma_i) =
\sigma_i^{-1}$ — well-known in $H_n(q)$.
