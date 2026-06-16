**Conjecture (complex-volume unification of mass-binding and decay).**
*Binding and the $\beta$-decay $Q$-value are not two stories. They are
the real and imaginary parts of a single complex fibre observable — the
complexified mass-endomorphism convolution-defect*

$$
  \mathfrak{W}(K)\;=\;E_0\big(\mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{knot}})\big)
  \;\in\;\mathbb{C},
  \qquad
  \mathfrak{B}(K) = \operatorname{Re}\mathfrak{W}(K),
  \quad
  \mathfrak{Q}_\beta(K) = \operatorname{Im}\mathfrak{W}(K),
$$

*the QOU analogue of the Neumann–Zagier complex volume
$\mathbb{V}(K) = \operatorname{Vol}(K) + i\,\mathrm{CS}(K)$.*

## The one object

There is **one** Markov trace $\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$
(CLAUDE.md §7a; the fibre functor $\tau$ is a *different* object — hence
$\mathrm{tr}_M$, never $\tau_M$). What varies is the **braid word** fed
to it. For a confined knot $K$, both words live in the *same* Hecke
algebra $H_n(q)$:

- $W_{\text{free}}$ — the **split / factorized** word ($K$'s
  constituents un-linked; its trace *multiplies* over components),
- $W_{\text{knot}}$ — the **linked / confined** word (the
  knot-convolved braid).

They differ by the **inter-constituent (confining) crossings** — the
*same* R-matrix $\sigma_i \mapsto R$ applied at the linking crossings
that $W_{\text{free}}$ lacks (one R-matrix, two words — not two
R-matrices). Equivalently, `free` is the trace **composed with a
projection**: $\mathrm{tr}_M(W_{\text{free}}) = \mathrm{tr}_M(\Pi_{\text{free}}\,\mathcal{M})$,
where $\Pi_{\text{free}}$ is the idempotent projection of $H_n(q)$ onto
the **parabolic (Young) subalgebra**
$H_{n_1}(q)\otimes\cdots\otimes H_{n_c}(q)$ of the constituents — the
categorical projection onto the factorized tensor / conditional
expectation onto the split-word subalgebra (no inter-constituent
braiding); and $W_{\text{knot}} = \mathcal{M}$ is the un-projected mass
endomorphism. The **convolution-defect** is their Markov-trace
difference; since $\mathrm{tr}_M$ is linear it is the trace of the
single **confinement element** $\mathcal{M} - \Pi_{\text{free}}\mathcal{M}$ —
the part of $\mathcal{M}$ that does *not* survive $\Pi_{\text{free}}$ (a
**projection defect**, written as an explicit trace-difference — *not*
an overloaded $\Delta$, *not* a new trace-like symbol):

$$
  \mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{knot}})
  \;=\;
  \mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\,\mathcal{M}\big)
  \;=\;
  \sum_\lambda y_\lambda\,\big(\chi^\lambda_{\text{free}} - \chi^\lambda_{\text{knot}}\big).
$$

This is a statement on **any confined knot $K$**; the nuclear binding
case — a nucleus is a confined nucleon knot, split tensor
$\mathfrak{p}^{Z}\otimes\mathfrak{n}^{N}$ — is the physical instance
$\mathrm{tr}_M(W_{\text{knot}}) = \mathrm{tr}_M(W_{\text{atom}})$ of
`binding_canonical`.

the per-partition object of the canonical binding
([`prop:categorical-mass-markov`](#prop:categorical-mass-markov),
`binding_canonical`). Read over $\mathbb{C}$ it carries **one bit more
information than either observable alone**: its two bar-parities.

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
| **QOU** | $\mathfrak{B}(K)$ — **binding / mass** | $\mathfrak{Q}_\beta(K)$ — **$\beta$-decay** |

The mass/binding channel is the **volume** (real, $\cosh$) part; the
decay channel is the **Chern–Simons** (imaginary, $\sinh$) part of the
*same* $\mathfrak{W}$.

## What is proved, and the fibre-level caveat

- **Proved (algebra).** The bar-parity decomposition
  $\tfrac{q+q^{-1}}{2}\pm\tfrac{q-q^{-1}}{2} = q^{\pm1}$ holds over any
  field; the complex reconstruction $\mathfrak{B}+i\,\mathfrak{Q}_\beta
  = \mathfrak{W}$ follows from the two projection
  hypotheses ([Lean](#conj:binding-qbeta-complex-volume),
  `QOU.MassEndomorphism.ComplexVolumeUnification`, 0 sorries).
- **Proved (classical limit).** The free/factorized projection
  $\chi^\lambda_{\text{free}}$ is the disjoint-product factorization,
  proven at $q=1$ via Plancherel duality
  ([`rem:block-multiplicativity-v-free`](../mass-theory/block-multiplicativity-v-free.md));
  the $q$-deformed case is class-axiomatized (conjectural).
- **Conjectural (the unification itself).** That the *physical* binding
  and $Q_\beta$ are the Re/Im of the **same** $\mathfrak{W}$
  at a single normalization.
- **Fibre-level caveat (STRICT).** At the **archimedean / observable**
  level $\operatorname{Im}(q_0)=0$
  (`lusztig_q_0_imaginary_part_zero`): binding and $Q_\beta$ are both
  *real* measured numbers. The complex structure is therefore
  **fibre-level** (pre-$\tau$): $\mathfrak{W}(q)$ is a complex object in
  the fibre, and $\mathfrak{B}$, $\mathfrak{Q}_\beta$ are its Re/Im
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

## Consequence — one story

Conditional on the unification, the framework's mass/binding chapter and
its $\beta$-decay chapter are **one derivation**: compute the complex
convolution-defect $\mathfrak{W}(K) = \mathfrak{W}(K)$ once;
its real part is every binding energy, its imaginary part is every
$Q$-value. The "$0.17\%$ $Q_\beta$ residual" and the binding $\Delta_\lambda$
gap become the *same* unclosed object — the imaginary and real parts of
one complex volume — rather than two independent open problems.
