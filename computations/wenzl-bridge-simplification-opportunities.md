# Simplification opportunities enabled by the Wenzl-bridge

PR #427's Wenzl-bridge closed form (`prop:y-lambda-closed-form-wenzl-bridge`)
gives us $y_\lambda(q) = s_{\lambda, r}(Q) / Z$ in $\mathbb{Q}(q^{1/2})$
for **any** partition at **any** $n$, in $O(p(n) \cdot \max\text{hooks})$
time. This **supersedes** several legacy compute paths that can now
be retired or shortened.

## Compute-pipeline speedups

| Legacy path | Bottleneck | Wenzl-bridge replacement |
|---|---|---|
| `y_lambda_jones_markov_witness.py` (linear-system inversion) | sympy 20-min timeout at $n = 5$ | One-shot Schur principal-specialization, ~50 ms per $n$ at $n = 12$ |
| `y_lambda_mpfr_witness.py` (Hoefsmit MPFR matmul, Rust kernel) | Failed at $n = 12$ (462×462 matrices) | Symbolic eval via Wenzl-bridge, then `sp.N(..., dps)` |
| `schur_element_identify.py` (10-candidate harness) | Negative result; convention puzzle unresolved | Convention puzzle CLOSED — replace harness with bridge derivation note |
| MPFR ladder $n = 11$ at 25 min | seminormal Hoefsmit matmul | Bridge produces 270 partitions at $n = 2..12$ in 45 s total |

**Concrete savings** at the agent-runtime level: any future
$y_\lambda$ extension (say to $n = 13, ..., 21$) takes seconds
instead of needing the upstream Rust kernel work.

## Proof / exposition simplifications

### `prop:explicit-alpha-k-h3` (closed-form $\alpha_k$ at $H_3$)

The explicit derivation in the proof can now **forward-reference**
the Wenzl-bridge:

> *Alternative derivation*: by [Wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge),
> $y_\lambda$ at $H_3$ are q-rational in $\mathbb{Q}(q^{1/2})$.
> The Markov pairings $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$
> on the four E_∞ classes inherit this q-rationality.

This shortens the existing proof from 4 separate Markov-pairing
calculations to a single uniform reduction.

### `prop:alpha-k-derivation-procedure` (general procedure)

The "Algorithm (per-$n$ $y_\lambda$ extraction)" section currently
describes the 4-step linear-system solve. This can be replaced by:

> *Closed form available*: by [Wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge),
> $y_\lambda(q) = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$
> directly, with $Q = q^2$ and $X = Q^r$ given explicitly. The
> linear-system path (steps 1–4 below) is now optional.

Reducing the procedure proposition from 4-step algorithm to a
single closed-form formula plus the (now-historical) linear-system
verification.

### `prop:wedderburn-bratteli-recursion` (the Bratteli factor)

The recursion factor $F_q(c, h)$ stated as conjectural can now be
derived from the Wenzl-bridge by taking the ratio
$y_\lambda^{(n+1)} / (z \cdot y_\mu^{(n)})$ symbolically. This
**proves** the recursion form rather than leaving it as a
"candidate matching the Wenzl-bridge derivation" stub.

## What does NOT simplify

- **$\alpha_k \to$ MeV $\alpha_k$ bridge** is unaffected — the
  units-bridge problem (`alpha_lambda_mev_bridge_probe.py`,
  PR #433) remains open. The Wenzl-bridge gives clean closed forms
  for $y_\lambda$, but doesn't change the fact that the
  $\alpha_k^{\mathrm{MeV}}$ in the fitted mass formula are not
  related to $\alpha_k^{\mathrm{struct}}$ by a constant κ.

- **Atom-knot identification for ⁶Li/⁷Li** is unaffected — this
  needs hyperbolic-volume + framework-prefactor work, orthogonal
  to the Hecke-algebra closure.

- **$\alpha_{\mathrm{EM}}$ derivation** is structurally **unaffected**:
  the formula $1/\alpha = 45 \cdot [3]_q \cdot (1 + \delta_{\mathrm{CS}} + 8q \, \delta_{\mathrm{CS}}^2)$
  uses $q$-integers $[3]_q$, $[5]_q$ and the gluon-octet identification
  $\kappa = 8q$ — these don't simplify via the Wenzl-bridge because
  α_EM uses Hecke-algebra **inputs** (q-integers, q-rational characters)
  rather than **outputs** (Markov-trace weights). The Wenzl-bridge
  could however give a cleaner derivation of WHY the prefactor has
  this specific structure if combined with a Plancherel completeness
  argument; this is open work.

## Implementation status

This PR (#433) commits the **simplification analysis** as
documentation. Actual rewrites of the affected propositions
(`explicit-alpha-k-h3.md`, `alpha-k-derivation-procedure.md`,
`wedderburn-bratteli-recursion.md`) to incorporate the
forward-references will happen in a follow-up commit if requested.
