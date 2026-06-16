**Conjecture (complex-volume unification of mass-binding and decay).**
*Binding and the $\beta$-decay $Q$-value are not two stories. They are
the real and imaginary parts of a single complex fibre observable — the
complexified mass-endomorphism convolution-defect*

$$
  \mathfrak{V}(K)\;=\;E_0\,\mathrm{tr}_M\big((\Pi_{\text{free}} - \mathbf{1})\circ\mathcal{M}\big)
  \;\in\;\mathbb{C},
  \qquad
  \mathfrak{E}_{\mathrm{bind}}(K) = \operatorname{Re}\mathfrak{V}(K),
  \quad
  \mathfrak{Q}_\beta(K) = \operatorname{Im}\mathfrak{V}(K),
$$

*the QOU analogue of the Neumann–Zagier complex volume
$\mathbb{V}(K) = \operatorname{Vol}(K) + i\,\mathrm{CS}(K)$.*

## The one object

Categorically — **no braid words**. For a confined knot $K$:

- $\mathcal{M} = \mathcal{M}(K) \in \operatorname{End}_{\mathbf{C}}(X_K)$
  is the **mass endomorphism** of the object $X_K$ representing $K$ in
  the rigid monoidal category $\mathbf{C}$;
- $\mathrm{tr}_M : \operatorname{End}_{\mathbf{C}}(X_K) \to k$ is the
  categorical **Markov trace** (the closed/categorical trace; CLAUDE.md
  §7a — the fibre functor $\tau$ is a *different* object, never
  $\tau_M$);
- $\Pi_{\text{free}} \in \operatorname{End}_{\mathbf{C}}(X_K)$ is the
  **idempotent projector** ($\Pi_{\text{free}}^2 = \Pi_{\text{free}}$)
  onto the **factorized sub-object**
  $X_K \twoheadrightarrow X_1 \otimes \cdots \otimes X_c$ — the
  constituents un-linked (the categorical projection onto the split
  tensor: the *same* R-matrix braiding with the inter-constituent
  confining crossings dropped).

The **convolution-defect** is the categorical trace of the part of
$\mathcal{M}$ that does *not* survive $\Pi_{\text{free}}$ — a
**projection defect** (no words, no overloaded $\Delta$, no new
trace-like symbol):

$$
  \mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\big)
  \;=\;
  \mathrm{tr}_M(\Pi_{\text{free}}\circ\mathcal{M}) - \mathrm{tr}_M(\mathcal{M})
  \;=\;
  \sum_\lambda y_\lambda\,\big(\chi^\lambda(\Pi_{\text{free}}\mathcal{M}) - \chi^\lambda(\mathcal{M})\big),
$$

the per-partition object of the canonical binding
([`prop:categorical-mass-markov`](#prop:categorical-mass-markov),
`binding_canonical`). This is a statement on **any confined knot $K$**;
the nuclear binding case — a nucleus is a confined nucleon knot,
factorized sub-object $\mathfrak{p}^{Z}\otimes\mathfrak{n}^{N}$ — is the
physical instance $\mathrm{tr}_M(\mathcal{M}) = \mathrm{tr}_M(W_{\text{atom}})$
of `binding_canonical`. Read over $\mathbb{C}$ the defect carries **one
bit more information than either observable alone**: its two
bar-parities.

## Why Re/Im is forced — the bar-parity = the complexification

Write $q = e^{\lambda}$, $\lambda = \log q$. The two crossing
eigenvalues $q, -q^{-1}$ split as

$$
  \underbrace{\tfrac{q+q^{-1}}{2}=\cosh\lambda}_{\textbf{bar-even}},
  \qquad
  \underbrace{\tfrac{q-q^{-1}}{2}=\sinh\lambda}_{\textbf{bar-odd}},
$$

so $\cosh\lambda \pm \sinh\lambda = e^{\pm\lambda}$ — the bar-even and
bar-odd parts are **one element $e^{\lambda}$ read on its two
parities**. Continue $\lambda \mapsto i\theta$ (the substrate $q$ rotated
onto the unit circle / a root of unity) and $\cosh\to\cos$,
$\sinh\to i\sin$: the **bar-even/bar-odd split becomes a Re/Im split**.
That is exactly the structure of the complex volume:

| | real part (bar-even, $\cosh$, real $q$) | imaginary part (bar-odd, $\sinh$, root-of-unity $q$) |
|---|---|---|
| **Neumann–Zagier** | $\operatorname{Vol}(K)$ (hyperbolic) | $\mathrm{CS}(K)$ (Chern–Simons) |
| **QOU** | $\mathfrak{E}_{\mathrm{bind}}(K)$ — **binding / mass** | $\mathfrak{Q}_\beta(K)$ — **$\beta$-decay** |

The mass/binding channel is the **volume** (real, $\cosh$) part; the
decay channel is the **Chern–Simons** (imaginary, $\sinh$) part of the
*same* $\mathfrak{V}$.

## What is proved, and the fibre-level caveat

- **Proved (algebra).** The bar-parity decomposition
  $\tfrac{q+q^{-1}}{2}\pm\tfrac{q-q^{-1}}{2} = q^{\pm1}$ holds over any
  field; the complex reconstruction $\mathfrak{E}_{\mathrm{bind}}+i\,\mathfrak{Q}_\beta
  = \mathfrak{V}$ follows from the two projection
  hypotheses ([Lean](#conj:binding-qbeta-complex-volume),
  `QOU.MassEndomorphism.ComplexVolumeUnification`, 0 sorries).
- **Proved (classical limit).** The free/factorized projection
  $\chi^\lambda_{\text{free}}$ is the disjoint-product factorization,
  proven at $q=1$ via Plancherel duality
  ([`rem:block-multiplicativity-v-free`](../mass-theory/block-multiplicativity-v-free.md));
  the $q$-deformed case is class-axiomatized (conjectural).
- **Conjectural (the unification itself).** That the *physical* binding
  and $\mathfrak{Q}_\beta$ are the Re/Im of the **same** $\mathfrak{V}$
  at a single normalization.
- **Fibre-level caveat (STRICT).** At the **archimedean / observable**
  level $\operatorname{Im}(q_0)=0$
  (`lusztig_q_0_imaginary_part_zero`): binding and $\mathfrak{Q}_\beta$ are both
  *real* measured numbers. The complex structure is therefore
  **fibre-level** (pre-$\tau$): $\mathfrak{V}(q)$ is a complex object in
  the fibre, and $\mathfrak{E}_{\mathrm{bind}}$, $\mathfrak{Q}_\beta$ are its Re/Im
  **shadows under different archimedean evaluations** (real-$q$ vs
  root-of-unity). There is no "complex mass" — there is one complex
  *fibre* object with two real observable shadows, exactly as
  $\operatorname{Vol}$ and $\mathrm{CS}$ are separately real.

## Computational corroboration (this PR)

The two channels really are distinct real components of one object: the
$E_0\cdot|\Delta(\mathrm{net})|$ **net-route** (the bar-even, binding-like
$E_0\cdot\Delta(\mathrm{tr})$) gives a precision-ladder $c_2 \approx -8.0$,
whereas the canonical $c_2 = -1$ lives in the bar-odd $\mathrm{tr}_M$
**brane-tower** ladder
([`docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md`](../../../docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md),
witness `qbeta-ck-sseries-operator-match`). Two different real $c_2$'s for
the two parities are exactly what Re/Im components of one complex
$c_2$ predict.

## Consequence — one story, and one proof

Conditional on the unification, the framework's mass/binding chapter and
its $\beta$-decay chapter are **one derivation**: compute the complex
defect $\mathfrak{V}(K)$ once; its real part is every binding energy, its
imaginary part is every $Q$-value. The "$0.17\%$ $\mathfrak{Q}_\beta$
residual" and the binding $\Delta_\lambda$ gap become the *same* unclosed
object — the imaginary and real parts of one defect — rather than two
independent open problems.

**Proof economy.** A relation proved for $\mathfrak{V}$ over a commutative
ring $R$ with the **bar-involution** $\sigma$ (the structural setting —
*not* $\mathbb{C}$, per CLAUDE.md §7c) descends to **both** the bar-even
(binding) and bar-odd ($\mathfrak{Q}_\beta$) parts from a *single* proof,
because the projections $x \mapsto x\pm\sigma x$ are additive. Formalised
sorry-free in [`QOU.MassEndomorphism`](binding-qbeta-complex-volume.lean):
`invol_descent` (one ring identity $\Rightarrow$ both parity identities)
and `recurrence_invol_descent` (a three-term $\mathfrak{V}$-recurrence with
a bar-even multiplier $c$, $\sigma c = c$, yields the binding and
$\mathfrak{Q}_\beta$ recurrences at once — the `c_k`-ladder mechanism). The
$\mathbb{C}$/Re–Im picture is the archimedean instance ($\sigma=$ complex
conjugation).
