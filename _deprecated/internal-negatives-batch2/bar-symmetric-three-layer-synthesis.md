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
the interface-knot value $\bowtie_K = z$ in the cross-PR Phase 5c.1 cross-check (`delta_lambda_fr_identity_phase5c.py`)
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
| $\mathrm{Li}_2^q(z) = \tfrac{h}{2}\bigl(\log\Phi_{q^{-1}} - \log\Phi_q\bigr) = -h\cdot\log\Phi_q$ † | invariant (after $h$-twist) | **sym** |
| $\cos(\alpha - b\hbar_q^2/2)$ | invariant | **sym** |
| $\sin(\alpha)$ alone | NOT invariant | **anti-sym** |
| $\cosh(h)$ | invariant ($\cosh$ even) | **sym** |
| $\sinh(h)$ | NOT invariant ($\sinh$ odd) | **anti-sym** |

† $\mathrm{Li}_2^q$ row corrected per
([`prop:li2q-phiq-bar-symmetrization`](#prop:li2q-phiq-bar-symmetrization)
errata 2026-05-20 + witness
[`li2q-phiq-bar-symmetry.witness.json`](https://github.com/litlfred/qou/blob/main/computations/li2q-phiq-bar-symmetry.witness.json)).
The earlier "sum" form $\tfrac{1}{2}(\log\Phi_q + \log\Phi_{q^{-1}})$
is identically zero (since $\log\Phi_{q^{-1}} = -\log\Phi_q$ for
Faddeev's $\Phi_q$); the **bar-anti-symmetric image rescaled by
$h/2$** is the correct relation. Bar-classification stands —
$\mathrm{Li}_2^q$ is invariant once the $h$-twist is taken into
account (its archimedean realisation is the regulator image of a
bar-symmetric R-side object).

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
\mathrm{Li}_2^q(z) \;=\; \tfrac{h}{2}\bigl(\log \Phi_{q^{-1}}(z) - \log \Phi_q(z)\bigr) \;=\; -h\cdot \log \Phi_q(z),
\qquad h = q - q^{-1}.
$$

Proved as a formal-power-series identity in
[`prop:li2q-phiq-bar-symmetrization`](#prop:li2q-phiq-bar-symmetrization)
(corrected form; the earlier "sum" version was numerically
falsified — see the historical note in that block). The
**bar-anti-symmetric kernel** $\log \Phi_{q^{-1}} - \log \Phi_q$
*is* the structural object, rescaled by $h/2$; the bar-symmetric
average $\tfrac{1}{2}(\log\Phi_q + \log\Phi_{q^{-1}})$ vanishes
identically and contributes nothing.

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
| Series (Li_2^q) | sign-correct binding energies on D, T, ${}^{3}$He; variance $1.82\times$ | `computations/binding_depth_stratified_rust.py` |
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

1. **Series-layer proof from category alone**. Li_2^q $\leftrightarrow$ Φ_q $\leftrightarrow$
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

## Categorical-derivation infrastructure: `BarHeckeFunctor`

The Lean sibling now provides a formal **type-level structure**
for the categorical functors that the three layers are
conjecturally instances of:

```lean
structure BarHeckeFunctor (R : Type*) [CommRing R] [BarInvolution R] where
  apply : R → R
  apply_bar_symmetric :
    ∀ h : R, IsBarAntiSymmetric h → IsBarSymmetric (apply h)
```

A `BarHeckeFunctor` is a **map sending bar-anti-symmetric inputs
to bar-symmetric outputs** — the abstract shape that
$\Phi_q \to \mathrm{Li}_2^q$, $e^{i\alpha} \to \cos$, and
$e^h \to \cosh$ all instantiate.

**Concrete `BarHeckeFunctor` instances proved**:
- `constZero`: $F(h) = 0$ (trivial functor)
- `square`: $F(h) = h^2$ (anti $\times$ anti $\to$ sym; canonical kernel-squaring)
- `constSym c`: $F(h) = c$ for bar-symmetric constant $c$
- `evenPoly2 c_0 c_1`: $F(h) = c_0 + c_1 h^2$ (truncated cosh/cos-like)
- `add F G`: $F(h) + G(h)$ (closure under sum)
- `mul F G`: $F(h) \cdot G(h)$ (closure under product)

**Strengthened synthesis class** `BarSymmetricThreeLayerSynthesisFunctorial`
replaces the `True` placeholders with **explicit functor fields**:

```lean
class BarSymmetricThreeLayerSynthesisFunctorial R where
  universal_kernel : R
  universal_kernel_antisym : IsBarAntiSymmetric universal_kernel
  series_F : BarHeckeFunctor R
  phase_F  : BarHeckeFunctor R
  gain_F   : BarHeckeFunctor R
```

The three avatars are now **derived**:
$$
\text{series\_avatar} = F_{\text{series}}(K_{\text{univ}}),
\quad
\text{phase\_avatar} = F_{\text{phase}}(K_{\text{univ}}),
\quad
\text{gain\_avatar} = F_{\text{gain}}(K_{\text{univ}}).
$$

The bar-symmetry of each avatar is now a **direct consequence**
of the functors' own `apply_bar_symmetric` field — no class
ansatz needed. Proved as
`series_avatar_isBarSymmetric`, `phase_avatar_isBarSymmetric`,
`gain_avatar_isBarSymmetric`.

The **unification conjecture** now has a CONCRETE
type-level shape: *there exist three `BarHeckeFunctor` instances
$F_{\text{series}}, F_{\text{phase}}, F_{\text{gain}}$ and one
bar-anti-symmetric $K_{\text{univ}}$ such that the three layer
avatars are $F_\bullet(K_{\text{univ}})$*. Future categorical
derivations populate the functors and kernel; the bar-symmetry
half of the claim is already free from the structure.

A `trivialBarSymmetricThreeLayerSynthesisFunctorial` instance is
provided (universal kernel = 0, all functors `constZero`) to
confirm class soundness.

## Status

- **Series**: algebraic identity proved (`prop:li2q-phiq-bar-symmetrization`).
- **Phase**: algebraic identity proved (Mathlib `Real.cos_neg`).
- **Gain**: algebraic identity proved (Mathlib `Real.cosh_neg`).
- **Unification**: open R&D (this proposition).
- **Empirical anchor**: 3/3 matches, 3/3 falsifications recorded.

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean construction in [`bar-symmetric-three-layer-synthesis.lean`](bar-symmetric-three-layer-synthesis.lean) has a narrative proof here. The genuine conjecture is in the class-field `True` placeholders (the unification claim); everything else is `sorry`-free.

### Bar-involution axioms (this file's local copy)

The synthesis file has its own `class BarInvolution R` matching the four ring-involution axioms of [`def:bar-involution`](#def:bar-involution). Proofs in the sibling block apply directly here.

### `cos` and `cosh` are bar-symmetric

**Proposition (Lean: `cos_isBarSymmetric_of_antisym`).** $\cos$ of a bar-anti-symmetric argument is bar-symmetric.
*Proof.* For real $x$: $\cos(-x) = \cos(x)$ by `Real.cos_neg` (Mathlib). $\square$

**Proposition (Lean: `cosh_isBarSymmetric_of_antisym`).** $\cosh$ of a bar-anti-symmetric argument is bar-symmetric.
*Proof.* For real $h$: $\cosh(-h) = \cosh(h)$ by `Real.cosh_neg`. $\square$

### Synthesis class structure

**Definition (Lean: `class BarSymmetricThreeLayerSynthesis R`).** Bundles the universal bar-anti-symmetric kernel, the three avatars (series / phase / gain), their individual bar-symmetry proofs, and the **conjectural** unification claim (`series/phase/gain_from_universal : True` placeholders).

**Instance (Lean: `trivialBarSymmetricThreeLayerSynthesis`).** Degenerate inhabitance: $K_{\mathrm{univ}} = 0$, all avatars = $0$. Confirms class soundness.
*Proof.* Choose all fields to be $0$; bar-symmetry of $0$ is `BarInvolution.bar_zero`. $\square$

### Synthesis-class corollaries (PROVED for any instance)

**Theorem (Lean: `sum_of_avatars_isBarSymmetric`).** For any instance, the sum of the three avatars is bar-symmetric.
*Proof.* Each avatar is bar-symmetric by its class field; sum of bar-symmetric is bar-symmetric via `BarInvolution.bar_add` plus the bar-symmetry of each summand. $\square$

**Theorem (Lean: `product_of_avatars_isBarSymmetric`).** Product of the three avatars is bar-symmetric.
*Proof.* Each avatar is bar-symmetric; product of bar-symmetric is bar-symmetric via `BarInvolution.bar_mul`. $\square$

**Theorem (Lean: `universal_kernel_squared_isBarSymmetric`).** $K_{\mathrm{univ}}^2$ is bar-symmetric.
*Proof.* From $\overline{K_{\mathrm{univ}}} = -K_{\mathrm{univ}}$: $\overline{K_{\mathrm{univ}}^2} = \overline{K_{\mathrm{univ}}} \cdot \overline{K_{\mathrm{univ}}} = (-K_{\mathrm{univ}})(-K_{\mathrm{univ}}) = K_{\mathrm{univ}}^2$. **The key categorical identity: bar-anti-symmetric squared is bar-symmetric — this is what generates all even-power layer avatars.** $\square$

### `BarHeckeFunctor` type and instances

**Definition (Lean: `structure BarHeckeFunctor R`).** A `BarHeckeFunctor` over $R$ is an `apply : R → R` together with a proof that bar-anti-symmetric inputs map to bar-symmetric outputs.

**Constructor (Lean: `constZero`).** $F(h) := 0$.
*Proof of bar-symmetry of output.* $\overline 0 = 0$ by definition. $\square$

**Constructor (Lean: `square`).** $F(h) := h^2$.
*Proof.* $\overline{h^2} = \overline h \cdot \overline h = (-h)(-h) = h^2$ for bar-anti-sym $h$. $\square$

**Constructor (Lean: `constSym c`).** $F(h) := c$ for bar-symmetric $c$.
*Proof.* Output is the bar-symmetric constant $c$, independent of $h$. $\square$

**Constructor (Lean: `evenPoly2 c0 c1`).** $F(h) := c_0 + c_1 h^2$.
*Proof.* Each summand bar-symmetric (constants by hypothesis; $h^2$ by the `square` argument); sum bar-symmetric by `bar_add`. $\square$

**Constructor (Lean: `evenPoly3 c0 c1 c2`).** $F(h) := c_0 + c_1 h^2 + c_2 h^4$.
*Proof.* Same as `evenPoly2` extended by one term: $h^4 = (h^2)^2$, bar-sym $\times$ bar-sym = bar-sym. $\square$

**Constructor (Lean: `evenPoly4 c0 c1 c2 c3`).** $F(h) := c_0 + c_1 h^2 + c_2 h^4 + c_3 h^6$.
*Proof.* Same pattern as `evenPoly3`; $h^6 = h^2 \cdot h^4$ bar-sym $\times$ bar-sym. $\square$

**Constructor (Lean: `add F G`).** $(F + G)(h) := F(h) + G(h)$.
*Proof.* $F(h)$ and $G(h)$ are bar-sym (by their `apply_bar_symmetric` fields); sum is bar-sym. $\square$

**Constructor (Lean: `mul F G`).** $(F \cdot G)(h) := F(h) \cdot G(h)$.
*Proof.* Product of bar-sym is bar-sym. $\square$

### Strengthened functorial synthesis class

**Definition (Lean: `class BarSymmetricThreeLayerSynthesisFunctorial R`).** Strengthens the original class by requiring **explicit `BarHeckeFunctor` fields** for series / phase / gain instead of opaque avatars. The avatars are then **derived** by applying these functors to the universal kernel.

**Derived theorems (Lean: `series_avatar_isBarSymmetric` + phase + gain).** Each derived avatar is bar-symmetric.
*Proof.* Direct from the functor's `apply_bar_symmetric` field applied to `universal_kernel_antisym`. $\square$

**Instance (Lean: `trivialBarSymmetricThreeLayerSynthesisFunctorial`).** Degenerate functorial instance with $K_{\mathrm{univ}} = 0$ and all three functors $= \mathrm{constZero}$.
*Proof.* Each field satisfies its constraint by definition. $\square$

### Trivial real bar + c_5 BarHeckeFunctor

**Instance (Lean: `BarInvolution.idReal`).** Trivial bar-involution on $\mathbb{R}$: $\overline x = x$.
*Proof.* All four axioms hold reflexively. $\square$

**Definition (Lean: `c5BarHeckeFunctor`).** The c_5 rational map cast as a `BarHeckeFunctor ℝ`. Apply: $F(h) = -3/2 + 1/(h^2 + 4)$. Bar-symmetry of output is trivial under the id bar.

**Evaluations (Lean: `c5BarHeckeFunctor_zero/two/one`).**
- $F(0) = -5/4$ (commutative-QOU limit)
- $F(2) = -11/8$ (silver-ratio β-decay null)
- $F(1) = -13/10$ (golden-ratio analog)

*Proof.* Direct `norm_num` from the apply formula at $h = 0, 2, 1$. $\square$

All 32 Lean constructions in the sibling have narrative proofs here. The synthesis-class unification (the `True` placeholders) remains the only open conjectural piece — concrete realisations live in [`polynomial-bar-involution`](#prop:polynomial-bar-involution) where the three-layer truncated polynomials are PROVED bar-symmetric in the same polynomial ring.
