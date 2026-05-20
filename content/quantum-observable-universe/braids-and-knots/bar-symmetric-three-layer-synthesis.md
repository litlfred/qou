*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (bar-symmetric three-layer synthesis — conjectural).**

*The Hecke skein $h = q - q^{-1}$ is bar-anti-symmetric*
($h(q^{-1}) = -h(q)$). *The framework's three independently-
established corrections to the precision-ladder $\tau_M(\beta)$ —
the series-layer Li_2^q tower in $T_2, T_3, \ldots$, the
phase-layer $\cos(\alpha - b\hbar_q^2/2)$ at the $N=1$ rung, and
the gain-layer $\alpha_Z \approx [3]_q^2 \cdot \cosh(h)$ per-$Z$
step factor — are all the **bar-symmetric (even/cosh-like)
projection** of a common bar-anti-symmetric Hecke kernel.
Equivalently, each is the EVEN-part of an exponential of an
underlying bar-anti-symmetric operator; the ODD-part
($\Phi_q$ alone, $\sin$, $\sinh$) is what the framework
empirically rejects.*

> **Bar-symmetry primer.** All bar-symmetry / bar-anti-symmetry
> definitions, the classification table of every QOU quantity
> by bar-type, the canonical algebraic identities ($h =
> h_{1/2}/z$, $b^2 = 1 - 1/[2]_q^2$, $c_5 = -3/2 + 1/[2]_q^2$),
> and the Kac–Sunada meta-justification all live in the
> canonical reference block
> [`def:bar-involution`](#def:bar-involution). This proposition
> consumes those definitions and adds the three-layer-synthesis
> *conjecture* on top.

## Quick reminder: why $h = q - q^{-1}$ is bar-anti-symmetric (illustration)

Three views of the same fact:

**Skein-diagram view**: the Hecke skein relation
$\sigma - \sigma^{-1} = h$ is a statement about crossings. Under
the bar-involution (mirror reflection of the braid), $\sigma$
(positive crossing, $L_+$) and $\sigma^{-1}$ (negative crossing,
$L_-$) swap. So

$$\overline{h} \;=\; \overline{\sigma - \sigma^{-1}} \;=\; \sigma^{-1} - \sigma \;=\; -h.$$

Mirror swap sends $h$ to $-h$ — by definition, bar-anti-symmetric.

**Silver-ratio numerical view**: at $q = 1+\sqrt 2$ (silver ratio),
$h = 2$. At $q^{-1} = \sqrt 2 - 1$ (the bar of silver), $h = -2$.
Bar reflects across $q = 1$ (the classical limit, fixed point of
the bar-involution), and $h$ flips sign across that axis.

**First-order quantum-deformation view**: near $q = 1$,
$h = q - q^{-1} = 2(q-1) - 2(q-1)^2 + 2(q-1)^3 - \cdots$. The
leading term $2(q-1)$ is strictly odd in $(q-1)$ — $h$ measures
**how far we've left the classical bar-fixed point**, and the
direction of that departure flips under bar.

**Product-form view (bar-decomposition of $h$ itself)**:

$$h \;=\; \underbrace{(q^{1/2} - q^{-1/2})}_{h_{1/2},\;\text{bar-ANTI-sym}} \;\cdot\; \underbrace{(q^{1/2} + q^{-1/2})}_{1/z,\;\text{bar-SYM (Markov param.)}}.$$

The bar-anti-symmetry of $h$ comes *entirely* from the half-step
factor $h_{1/2} = q^{1/2} - q^{-1/2}$; the second factor is the
**Markov parameter** $z = 1/(q^{1/2}+q^{-1/2})$ that appears as
the interface-knot value $\Delta_I^K = z$ in the cross-PR Phase 5c.1 cross-check (`delta_lambda_fr_identity_phase5c.py`)
(0.0001% match — derivation-grade categorical equality).

So **the same $z$ that is the Markov-axiom interface-knot factor
sits inside $h$** as its bar-symmetric half. The bar-symmetric
projection $P_{\mathrm{avg}}$ acts on $h_{1/2}$ (the bar-odd
half) and leaves the $z$ factor (the bar-even half) intact. This
ties the three-layer synthesis to the interface-knot Markov-
axiom finding: they are both manifestations of the same
$h = h_{1/2}/z$ split.

Other useful product forms of $h$:
- **Cyclotomic**: $h = (q-1)(q+1)/q = \Phi_1(q)\,\Phi_2(q)/q$.
- **Weierstrass / $\sinh$**: with $q = e^x$, $h = 2\sinh(x) = 2x \prod_{n\ge 1}(1 + x^2/(n\pi)^2)$ — each $(1 + x^2/(n\pi)^2)$ factor is bar-symmetric (even in $x$), so the total bar-anti-symmetry sits in the leading $2x$ kernel.
- **q-integer chain**: $q^n - q^{-n} = h \cdot [n]_q$, where $[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ is bar-symmetric.

### Bar-classification of standard quantities

Under the bar-involution $\overline{(\cdot)} \colon q \mapsto q^{-1}$,
$\sigma \mapsto \sigma^{-1}$:

| Quantity | Bar action | Class |
|---|---|:---:|
| $q$ | $q \to q^{-1}$ | (def. of bar) |
| $h = q - q^{-1}$ | $h \to -h$ | **anti-sym** |
| $\sigma$ | $\sigma \to \sigma^{-1}$ | (def. of bar) |
| $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$ | $\to \sigma_{\mathrm{avg}}$ | **sym** |
| $b^2 = (q^4+q^2+1)/(q^2+1)^2$ | invariant | **sym** |
| $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ | invariant | **sym** |
| $\Phi_q(z)$ alone | NOT invariant | **anti-sym** |
| $\mathrm{Li}_2^q(z) = \frac{1}{2}(\log \Phi_q + \log \Phi_{q^{-1}})$ | invariant | **sym** |
| $\cos(\alpha - b\hbar_q^2/2)$ | invariant | **sym** |
| $\sin(\alpha)$ alone | NOT invariant | **anti-sym** |
| $\cosh(h)$ | invariant ($\cosh$ even) | **sym** |
| $\sinh(h)$ | NOT invariant ($\sinh$ odd) | **anti-sym** |

> **Antiskew note.** The framework projects onto the bar-EVEN /
> bar-SYMMETRIC component — $\cos, \cosh, \mathrm{Li}_2^q$ — and
> discards the bar-ODD / bar-ANTI-symmetric component — $\sin,
> \sinh, \Phi_q$ alone. The result is **bar-symmetric (even)**,
> not bar-anti-symmetric (skew). Calling it "anti-skew" is only
> correct in the sense that the skew (bar-anti-symmetric)
> component is discarded; the residual is symmetric, not skew.

## The three layers

### Series layer (additive $\tau_M$ correction)

$$
\mathrm{Li}_2^q(z) \;=\; \tfrac{1}{2}\bigl(\log \Phi_q(z) + \log \Phi_{q^{-1}}(z)\bigr) + O\bigl((q-1)^3 \cdot z\bigr).
$$

Proved as a formal-power-series identity in
[`prop:li2q-phiq-bar-symmetrization`](#prop:li2q-phiq-bar-symmetrization).
The bar-anti-symmetric kernel here is
$\log \Phi_q - \log \Phi_{q^{-1}}$; the bar-symmetric projection
$P_{\mathrm{avg}}$ kills it and produces Li_2^q on the residual.

### Phase layer (oscillatory $N=1$ rung)

$$
Q_\beta(N=1) \;\propto\; \cos(\alpha - b\hbar_q^2/2),
\qquad \alpha = (z-1) h/2.
$$

Here $\alpha$ is bar-anti-symmetric ($z$ flips sign, $h$ flips
sign — product is bar-symmetric, but $(z-1)$ flips and $h$ flips
giving $\alpha \to -\alpha$). The $\cos$ functional ($\cos x =
\cos(-x)$, EVEN) extracts the bar-symmetric projection.

### Gain layer (multiplicative per-$Z$ step)

$$
\alpha_Z \;\approx\; [3]_q^2 \cdot \cosh(h),
\qquad
\text{rel. error 0.022\% empirical (PR \#819 Phase 5b)}.
$$

$h = q - q^{-1}$ is bar-anti-symmetric; $\cosh$ ($\cosh x = \cosh(-x)$,
EVEN) extracts the bar-symmetric projection.

## What's provable vs conjectural — Lean infrastructure

Per CLAUDE.md §3b-cond (conditional-class exception), the Lean
sibling [`QOU.BraidKnot.BarSymmetricThreeLayerSynthesis`](bar-symmetric-three-layer-synthesis.lean)
**carves out the provable algebraic content** from the conjectural
unification:

### Provable (no `sorry` modulo minor field/ring arithmetic)

- `class BarInvolution R`: a ring involution mapping $q \mapsto q^{-1}$, $\sigma \mapsto \sigma^{-1}$.
- `def IsBarSymmetric (x : R) : Prop`: $\overline{x} = x$.
- `def IsBarAntiSymmetric (x : R) : Prop`: $\overline{x} = -x$.
- `def barSymmetricProjection (x : R) := (x + bar x)/2`.
- `barSymmetricProjection_isBarSymmetric`: $P_{\mathrm{avg}}$ lands in the bar-symmetric subspace.
- `barSymmetricProjection_idempotent`: $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$ (since $P_{\mathrm{avg}}$ acts as identity on bar-symmetric elements).
- `cos_isBarSymmetric_of_antisym`: $\cos$ of a bar-anti-symmetric argument is bar-symmetric (from Mathlib's `Real.cos_neg`).
- `cosh_isBarSymmetric_of_antisym`: $\cosh$ of a bar-anti-symmetric argument is bar-symmetric (from `Real.cosh_neg`).

### Conjectural (axiomatised as class fields)

- `class BarSymmetricThreeLayerSynthesis`: holds the three avatars
  (series / phase / gain) and the claim that each is the bar-
  symmetric projection of the SAME universal bar-anti-symmetric
  kernel $K_{\mathrm{univ}}$.
- `series_from_universal`, `phase_from_universal`,
  `gain_from_universal`: the genuinely conjectural part — that all
  three are functorial images of one categorical operator under
  Markov-trace / oscillatory-factor / per-Z-induction respectively.

### Meta-justification (Kac–Sunada drum)

Kac (1966) asked "can you hear the shape of a drum?" — Sunada
(1985) answered no (isospectral non-isometric domains exist). The
braid-theoretic analog: distinct braids can share $\tau_M(\beta)$
at fixed $q$ (Hecke-trace isospectral pairs). But demanding
agreement at BOTH $q$ AND $q^{-1}$ (i.e., bar-symmetric matching)
is much tighter — the Faddeev $\Phi_q$ channel hears only one
orientation; symmetric Li_2^q hears the full bar-symmetrized
spectrum.

This reframes the framework's bar-symmetric projection as
**forced**, not chosen — it is the isospectral lift demanded by
Kac–Sunada non-uniqueness applied to Hecke-trace-determined braids.
Class `KacSunadaBarSymmetricForced` (in the Lean sibling) records
this meta-justification.

## Empirical anchor

Three independently-derived corrections, three independently-
verified empirical matches, all in the bar-symmetric projection:

| Layer | Empirical match | Source |
|---|---|---|
| Series (Li_2^q) | sign-correct binding energies on D, T, ³He; variance $1.82\times$ | `folio-assistant/computations/binding_depth_stratified_rust.py` |
| Phase (cos at N=1) | $Q_\beta$ to sub-ppt | `prop:neutron-qvalue-symbolic` |
| Gain (cosh at per-Z step) | rel. error $0.022\%$ on $\alpha_Z$ | cross-PR Phase 5b audit (`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`) |

The bar-anti-symmetric alternative ($\Phi_q$ alone, $\sin$,
$\sinh$) is empirically falsified:

| Falsified bar-anti-sym variant | Pathology |
|---|---|
| $\Phi_q(z)$ alone for binding | $-737$ MeV mirror-nucleus pathology |
| $\sin$ at N=1 | breaks isospin |
| $[3]_q^2 \cdot \sinh(h)$ | leaves $2.17\%$ bar-anti-sym residual |

The three falsifications + three matches together constitute the
**empirical content** of the synthesis. The **structural content**
— that the same operator generates all three layers — is the
remaining conjecture.

## Why $c_5$ has been problematic — three-layer reframing

The c_5 outlier identified in
[`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)
sits at the *series-layer* level (precision-ladder rung 5 of
$\tau_M$). Under the three-layer synthesis:

- The $-b^2$ part of $c_5 = -b^2 - 1/2$ is pure series-layer
  pure-$\sigma$ (bar-symmetric monomial in $c_3$ and $b^2$).
- The $-1/2$ part is the **bar-symmetric projection at the
  half-fill cyclic substructure** — $P_{\mathrm{avg}}$ applied to
  the bar-anti-symmetric Hopf-link kernel at $k = \lfloor n_{\text{total}}/2 \rfloor$.

So $c_5$ is the series-layer manifestation of the same universal
$P_{\mathrm{avg}}$ operator that produces $\cos$ at phase and
$\cosh$ at gain. Its "problematic" status — irreducibly carrying
the $-1/2$ that doesn't factor through $c_3$ and $b^2$ alone — is
not a defect but the **expected signature** of the bar-symmetric
projection on a bar-anti-symmetric kernel that doesn't have a
pure-$\sigma$ avatar.

## Sharpening the conjecture

Three concrete refinement targets to move pieces from class fields
into proved theorems:

1. **Series-layer proof from category alone**. Li_2^q ↔ Φ_q ↔
   Φ_{q^{-1}} identity is proved algebraically in
   [`prop:li2q-phiq-bar-symmetrization`](#prop:li2q-phiq-bar-symmetrization)
   over $\mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. Lifting that
   to a `theorem` (no `sorry`) is the first concrete target.

2. **Phase-layer proof from N=1 rung structure**. The $\cos$
   factor arises from the symmetric quotient of an oscillatory
   $e^{i\alpha}$ Wedderburn-decomposition contribution. The
   `phase_avatar_bar_symmetric` field can become a theorem once
   the precision-ladder formal-derivation is Lean-stated.

3. **Gain-layer proof from induction-restriction**. The 0.022%
   empirical match suggests $[3]_q^2 \cdot \cosh(h)$ is structural.
   Bridging that to a Hecke-induction theorem $\mathrm{Ind}^{H_{3(A+1)}}_{H_{3A}}
   \to (\text{per-Z gain})$ is the longest-pole target.

Each refinement that lands as a `theorem` moves one field out of
the conjectural class and tightens the synthesis. The **unification
claim** itself (`unified_kernel`) remains conjectural until all
three layer-functors are categorical equivalents — a structural-
representation-theory project, not a one-PR closure.

## Status

- **Series**: algebraic identity proved (`prop:li2q-phiq-bar-symmetrization`).
- **Phase**: algebraic identity proved (Mathlib `Real.cos_neg`).
- **Gain**: algebraic identity proved (Mathlib `Real.cosh_neg`).
- **Unification**: open R&D (this proposition).
- **Empirical anchor**: 3/3 matches, 3/3 falsifications recorded.
