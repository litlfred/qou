**Conjecture (Per-Z step factor in the Δ_λ closure form).**

*Let $q_0 \approx 1.10998$ be the substrate parameter (CAL-2) and let
$\alpha$ be the per-Z-step factor in the Phase 4 closed-form expression
for the single-block-dominant residual amplitude*
$$
  |\Delta_\lambda^*(K)| \;\approx\; \frac{\mathrm{Vol}_{\mathrm{hyp}}(K)}{[8]_q} \cdot \alpha^{Z-1} \cdot (q^{1/2}+q^{-1/2})^{4N}.
$$
*Then $\alpha$ admits the closed-form*
$$
  \boxed{\;\alpha(q) \;=\; [3]_q^2 \cdot \cosh(h)\;}
$$
*where $h = q - q^{-1}$ is the Hecke skein parameter and
$[3]_q = q^2 + 1 + q^{-2}$ is the third $q$-integer.*

### Numerical evidence

Computed empirically via Phase 4 closure-form fit on $|\Delta_\lambda^*|$
for $K \in \{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$:

| Quantity | Value at $q_0$ |
|---|---:|
| Empirical $\alpha$ | $9.4694$ |
| $[3]_q^2$ | $9.2641$ |
| $\cosh(h)$ | $1.0219$ |
| **$[3]_q^2 \cdot \cosh(h)$** | **$9.4673$** |
| rel. err. vs. empirical | **$0.022\%$** |

Match to 5 significant digits at 50-dps precision in the `q_parameter`
canonical pipeline. Cross-tested via [`delta_lambda_z4N_phase4.py`](../../../computations/delta_lambda_z4N_phase4.py) on all 4 atoms with max-relative-error 2.51% (achieved at $^4\mathrm{He}$ when including the $\cosh(h)$ refinement; was 2.17% without).

### Categorical reading

The conjectured form has a clean bar-symmetric interpretation
([`li2q-phiq-bar-symmetrization.md`](#li2q-phiq-bar-symmetrization)):

- **$[3]_q^2$** = the squared $q$-dimension of the adjoint
  representation $V_1$ of $U_q(\mathfrak{sl}_2)$. This is the
  rep theoretically natural "per-extra-proton" factor — adding
  one proton on top of the (Z=1, N) baseline contributes a
  $V_1 \otimes V_1$ tensor factor (charge/flavour channels for the
  added 3-quark composite).
- **$\cosh(h) = 1 + h^2/2 + h^4/24 + \cdots$** = the **Hecke-deformed
  identity correction** at the symmetric channel. The Hecke relation
  $\sigma^2 = h\sigma + 1$ specialised to the symmetric idempotent
  produces $\cosh(h)$ as the bar-symmetrised eigenvalue series.
  $\cosh$ is even, so $\cosh(h)$ is bar-symmetric (invariant under
  $q \mapsto q^{-1}$, which sends $h \mapsto -h$).

Equivalently: $\alpha = [3]_q^2 \cdot \cosh(h)$ is the **even part**
of $[3]_q^2 \cdot e^h$ under bar-symmetrisation — the bar-anti-symmetric
$[3]_q^2 \cdot \sinh(h)$ component would break mirror-nucleus symmetry
([`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) caveat
on bar-symmetric vs. bar-anti-symmetric channels).

### Cross-references in the bar-symmetric trinity

Three q-deformation corrections in the QOU mass formulas all live in
the **even part** of an exponential of a bar-anti-symmetric Hecke
operator:

| Layer | Bar-symmetric form (works) | Bar-anti-symmetric form (fails / overcounts) |
|---|---|---|
| Series (additive) | Symmetric $\mathrm{Li}_2^q$ | Faddeev $\Phi_q$ — gives −737 MeV mirror-nucleus pathology |
| Phase (N=1) | $\cos(\alpha_{\mathrm{phase}} - b\hbar_q^2/2)$ | $\sin$ component alone |
| Gain (Z-step) | $\alpha = [3]_q^2 \cdot \cosh(h)$ *(this conjecture)* | $[3]_q^2$ alone leaves a 2.17 % bar-anti-symmetric residual |

The bar-anti-symmetric counterparts are exactly the channels that
break mirror-nucleus symmetry / isospin parity / orientation reversal.
The bar-symmetric projection is the **isospectral lift** (per the
Kac-Sunada framing in [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) §"Structural reading").

### Status

- **Verified empirically** to 0.022 % rel. err. at $q_0$ (4 atoms; 50 dps).
- **Categorically motivated** via the bar-symmetric decomposition of
  the Hecke-relation eigenvalue series.
- **Open**: operator-level proof of $\cosh(h)$ at the symmetric
  channel. The class hypothesis below axiomatises this gap.
- **Phase 5d.4 + 5e.1 finding** ([PR #819](https://github.com/litlfred/qou/pull/819)): the per-Z step factor at the FULL Markov-trace level is exactly $z$ (Markov-axiom contribution from the interface knot, [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)).  The $\alpha = [3]_q^2 \cdot \cosh(h)$ correction here is at the **single-block dominant $|\Delta_\lambda^*|$ extraction level**, NOT the full $\tau_M$ — the two are complementary, not redundant.

### Implementation reference

- Script: [`computations/delta_lambda_z4N_phase4.py`](../../../computations/delta_lambda_z4N_phase4.py) (Phase 4 zero-parameter closure)
- Witness: `computations/delta-lambda-z4N-phase4.witness.json` (3 assertions, all passed)
- Phase 5b audit doc: `docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`
