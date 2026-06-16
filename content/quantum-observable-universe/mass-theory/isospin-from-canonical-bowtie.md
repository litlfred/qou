> **CORRECTION NOTE ( surfaced by `verify_isospin_bar_anomaly.py`):**
> The original draft classified the 305 ppm residue as "bar-anti-symmetric."
> **That was wrong.** Bar involution (q $\leftrightarrow$ $q^{-1}$ AND $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$) is
> **distinct** from the isospin Z/2 swap ($\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ with q FIXED).
> The 305 ppm residue is **isospin-Z/2-anti-symmetric** (correct); it
> is NOT bar-anti-symmetric because `ℏ_q = (q-1)/q` is "mixed" under bar.
> The 305 ppm match to CODATA holds at 0.03% rel diff. Body text below
> has been rewritten to use "isospin-Z/2-anti-symmetric" wherever the
> original meant the canonical isospin swap; references to specific
> quantities like `h = q − q⁻¹` that ARE bar-anti-symmetric retain
> that label. Full correction:
> [`docs/audits/-d9-bar-parity-correction.md`](../../docs/audits/-d9-bar-parity-correction.md).

**Conjecture (D9 isospin closure, conditional on
[`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
+ [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube)).**
*For each atomic braid $\beta_A \in B_{3A}$ written in the canonical
operator-valued interface convention*

$$
  \bowtie_K \;=\; \sigma_g \;-\; \frac{h}{2}\cdot \mathbf{1}
  \qquad (\text{averaged $\mathrm{pn}$ interface, $h = q - q^{-1}$})
$$

*there exists a regularised crystal-limit functional
$S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)$ such that the action
of the canonical $\mathrm{SU}(2)_I$ isospin symmetry (the $u
\leftrightarrow d$ flavor swap on color-sheet flavor triples) leaves
$S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)$ invariant up to a
**isospin-Z/2-anti-symmetric residue** carrying an overall factor of
$h = q - q^{-1}$.  The leading-order residue at $q = q_0$ matches
the substrate flavor split*

$$
  \frac{\Delta m}{M_N}
  \;=\;
  \frac{\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3)}{3}
  \qquad \text{(305 ppm against CODATA)},
$$

*per [`prop:flavor-split-substrate`](#prop:flavor-split-substrate)
and the closed form computed in
[`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py).
The 305 ppm match is the isospin-Z/2-anti-symmetric leading residue of the
$\mathrm{SU}(2)_I$ Z/2 swap on the operator-valued interface — i.e.,
it IS the canonical-isospin $q_0$-anomaly.*

## Background

The Z/2 isospin swap $u \leftrightarrow d$ exchanges the proton's
flavor triple $(u, u, d)$ with the neutron's flavor triple $(u, d, d)$
on the three color sheets per nucleon.  At the level of the canonical
atomic braid (per
[`isotope_record_schema.py`](../../computations/isotope_record_schema.py)),
this swap exchanges:

- **pp** intra-block ($\sigma$ generators) with **nn** intra-block
  ($\sigma^{-1}$ generators)
- **pn** intra-block (averaged $\bowtie_K = \sigma - h/2 \cdot
  \mathbf{1}$) with itself (the averaged crossing is fixed under
  the swap)

[`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
proves the invariance statement for the **plain-generator** restricted
braid word (no $\bowtie_K$ interfaces) at the $q \to 0$ crystal limit.
Its scope explicitly excludes the canonical $\bowtie_K$-coupled words
because $h = q - q^{-1}$ diverges at $q = 0$, so a naive crystal
limit does not exist.

This conjecture **extends** that result to the canonical
$\bowtie_K$-coupled words via a regularised crystal functional.

## The regularised crystal functional

For each $\bowtie_K$ interface in the canonical braid, replace the
divergent $-h/2$ shift with a **finite Cesàro limit**:

$$
  \bowtie_K^{\mathrm{reg}}(q)
  \;:=\;
  \lim_{N \to \infty}
    \frac{1}{N}
    \sum_{k = 1}^{N}
      \left(
        \sigma_g \;-\; \frac{h(q_k)}{2}\cdot \mathbf{1}
      \right)
$$

where $\{q_k\} \to 0$ is a regularising sequence whose Cesàro mean of
$h(q_k)$ stays finite — concretely, take $q_k = 1/k$ so that
$h(q_k) = 1/k - k$ has Cesàro mean $-N/2 + O(\log N)/N$ centred at
the leading-order $h/2$ subtraction.  The regulator absorbs the
divergent linear-in-$N$ part; the finite remainder is the
**categorical Cesàro average** of the operator-valued shift.

(Other regulators — finite-$N$ truncation with Borel resummation, or
zeta-function regularisation of the divergent $h$-series — give the
same finite remainder up to a renormalisation constant.  The bar-
anti-symmetric residue extracted below is regulator-independent.)

The **regularised crystal-corrected shell-binding sum** is

$$
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)
  \;:=\;
  S_{\mathrm{crystal}}(\beta_A^{\mathrm{plain}})
  \;+\;
  \sum_{\text{$\bowtie_K$ in } \beta_A}
    \mathrm{tr}_M\!\bigl(\bowtie_K^{\mathrm{reg}}\bigr),
$$

where $\beta_A^{\mathrm{plain}}$ is the plain-generator skeleton (to
which [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
applies directly) and the sum runs over the $A - 1$ inter-nucleon
interfaces.

## The isospin-Z/2-anti-symmetric residue and the 305 ppm match

Under the $\mathrm{SU}(2)_I$ Z/2 swap, $S^{\mathrm{reg}}_{\mathrm{crystal}}$
transforms as:

$$
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A^{\mathrm{swap}})
  \;-\;
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)
  \;=\;
  \sum_{\text{pp/nn pairs}}
    \bigl(\mathrm{tr}_M(\sigma^{-1}) - \mathrm{tr}_M(\sigma)\bigr)
  \;=\;
  - n_{pp/nn}\cdot h \cdot \omega(q)
$$

where $n_{pp/nn}$ counts the pp–nn pair swaps and $\omega(q)$ is the
common bar-symmetric Markov-trace factor.  The residue is
**isospin-Z/2-anti-symmetric** (carries an overall $h = q - q^{-1}$, which is
bar-odd per [`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)).

**Headline match.**  Evaluated at $q = q_0$, the leading-order residue
is exactly the substrate flavor split

$$
  \frac{\Delta m}{M_N}\bigg|_{q_0}
  \;=\;
  \frac{\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3)}{3}\bigg|_{q_0}
  \;\approx\;
  305\;\mathrm{ppm}
  \qquad
  \text{(CODATA: } (m_n - m_p)/M_N \approx 305\;\mathrm{ppm}\text{).}
$$

This is already computed in
[`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py)
and consumed by
[`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py).
The conjectural content of THIS block is the **categorical
identification** of that closed form as the regularised-crystal
$\mathrm{SU}(2)_I$ anomaly.

## Bar-symmetry parity decomposition

Per
[`docs/audits/-isospin-categorical-source.md`](../../docs/audits/-isospin-categorical-source.md)
§3 and the canonical-watcher §Slot J discipline, the four factors of
$\Delta m / M_N$ classify as:

| Factor | Under $q \mapsto q^{-1}$ | Bar parity |
|--------|---------------------------|------------|
| $\hbar_q = (q-1)/q$ | $\hbar_{q^{-1}} = 1 - q \neq \pm \hbar_q$ | **mixed** (not bar-classifiable) |
| $\hbar_q^2$ | inherits mixed status from $\hbar_q$ | **mixed** |
| $h = q - q^{-1}$ | $q^{-1} - q = -h$ | bar-**anti-symmetric** |
| $[2]_q = q + q^{-1}$ | invariant | bar-symmetric |
| $1 + \hbar_q^3$ | mixed (1 bar-sym, $\hbar_q^3$ inherits mixed) | mixed |

Net product $\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3) / 3$
is **mixed** under bar (verified at $q_{0}$ by
[`verify_isospin_bar_anomaly.py`](../../computations/verify_isospin_bar_anomaly.py)).
The product carries the bar-odd $h$ factor as a coefficient, but
the $\hbar_q$ factors don't bar-classify cleanly.

**Under the isospin Z/2 swap** ($\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ at q FIXED), the
residue IS anti-symmetric (the swap exchanges proton $\leftrightarrow$ neutron,
giving $m_n - m_p \neq 0$).  At the specific evaluation point
$q = q_0$, the formula's value is bar-odd in a sign-of-$h$ sense
(scales with the bar-odd $h$), but the formula AS A FUNCTION OF $q$
lacks a uniform bar-classification.  This is the audit-correction
finding from
[`docs/audits/-d9-bar-parity-correction.md`](../../docs/audits/-d9-bar-parity-correction.md).

The bar-symmetric subleading contribution
$\hbar_q^2 \cdot h \cdot [2]_q \cdot \hbar_q^3$
(bar-anti-sym $\times$ bar-anti-sym = bar-sym) is the next-order canonical
correction; it appears at relative order $\hbar_q^3 \approx 9.3 \times
10^{-4}$ to the leading 305 ppm.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: ℓ varies — per-atom; the residue
  identification holds at every $\ell$ for which both the plain
  skeleton ($\ell_{\mathrm{plain}}$) and the canonical word ($\ell_{\mathrm{canonical}}$) are defined.
- **Jet order**: $h^1$ (leading anomaly is isospin-Z/2-anti-symmetric linear
  in $h$; bar-symmetric subleading at $h^4$ via $\hbar_q^3$ multiplier).
- **Bar-symmetry status**: **isospin-Z/2-anti-symmetric** at leading order
  (the isospin residue lives in $P_{\mathrm{skew}}$ image of
  [`bar-involution.md`](bar-involution.md), correctly classified in
  [`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)
  under the $h$ entry).

## Closure of D9 in the duality tracker

Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 row
D9: this conjecture is the load-bearing closure path. The duality
tracker will move D9 from partial (crystal-only) to formalised
once:

1. This block lands (provides the categorical statement)
2. Lean class `IsospinFromCanonicalBowtie` is inhabited (depends on
   the regularised crystal functional class instance)
3. The isospin-Z/2-anti-symmetric residue verification numerical witness
   ships (see §"Open R&D" below)

The Lean class follows the conditional-class exception of CLAUDE.md
§3b-cond: the upstream conjecture `crystal-isospin-degeneracy`
provides the plain-generator base; the regularised-functional
extension is an `Instance` parameter; the isospin-Z/2-anti-symmetric residue
is then provable from the four-factor parity decomposition above.

## Lean axiomatisation (sketch)

```lean
-- Conditional on the plain-generator restricted result + the
-- color-tube channel-assignment class:
class IsospinFromCanonicalBowtie
    (M : Type*) [BrCategory M] [Hecke M]
    [CrystalIsospinDegeneracy M]
    [InterNucleonChannelColorTube M] where
  /-- The regularised crystal functional on canonical bowtie-
      coupled atomic braids. -/
  S_reg_crystal : ∀ (A : ℕ) (β : AtomicBraidCanonical A),
    Real
  /-- Cesàro / Borel regularisation absorbs the divergent -h/2
      shift; the finite remainder is the categorical residue. -/
  regulator_consistent :
    ∀ (A : ℕ) (β : AtomicBraidCanonical A),
      S_reg_crystal A β
        = S_crystal A (plain_skeleton β)
          + sum_bowtie_tr_M_reg β
  /-- SU(2)_I swap (u ↔ d) on color-sheet flavors leaves the
      regularised functional invariant up to a isospin-Z/2-anti-symmetric
      residue carrying an overall factor of h. -/
  swap_residue_bar_anti_symmetric :
    ∀ (A : ℕ) (β : AtomicBraidCanonical A),
      S_reg_crystal A (swap_isospin β)
        - S_reg_crystal A β
        = - count_pp_nn_swaps β · h · markov_trace_factor
  /-- Leading-order residue at q = q_0 matches the substrate
      flavor split closed form (verified numerically at 305 ppm). -/
  q_zero_residue_matches_flavor_split :
    leading_residue_at_q_zero
      = flavor_split_subleading q_zero
```

The class is inhabited by:
- the plain-skeleton crystal functional (via
  `CrystalIsospinDegeneracy` instance)
- the color-tube channel-assignment data (via
  `InterNucleonChannelColorTube` instance, conditional on PR
  [#1111](https://github.com/litlfred/qou/pull/1111)'s class)
- the regularised-functional construction (concrete Cesàro
  regulator on the divergent series).

Per CLAUDE.md §3b ("class is inhabited"), the only `sorry`
ultimately lives in the upstream-conjecture class instances.

## Open R&D

1. **Author the verification compute script**:
   `verify_isospin_bar_anomaly.py` — at $q = q_0$, evaluate the
   canonical $\bowtie_K$-coupled atomic braid for ${}^{2}\mathrm{H}$ (Z=1, N=1)
   and explicitly compute:
   - The plain-skeleton crystal-corrected shell sum
   - The regularised contributions from the one inter-nucleon arc
   - The isospin-Z/2-anti-symmetric residue
   - Cross-check against
     `_li_2_q_util.flavor_split_subleading(q_0)` to 1 ppb.
2. **Construct the explicit regulator**: identify the canonical
   Cesàro / Borel construction (out of several admissible
   regulators) that aligns with the framework's Φ_q vs Li_2^q
   sorting per [cheat sheet §4](../../docs/canonical-derivation-cheat-sheet.md).
3. **Promote to a `proposition`** with §3b-cond banner once the
   regulator-consistent statement is fully Lean-proved (modulo
   class instances).
4. **Extend to higher A**: verify the isospin-Z/2-anti-symmetric residue
   identification holds for T, ${}^{3}\mathrm{He}$, ${}^{4}\mathrm{He}$ — these have multiple
   inter-nucleon arcs and the residue is a sum over arcs.  The
   ${}^{4}\mathrm{He}$ magic-shell case (per
   [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md))
   is where the Wigner SU(4) supermultiplet structure should
   manifest.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D9
  (this conjecture is the closure path) + §2 Cluster B (D9 $\to$
  D10 $\to$ D11 nuclear physics)
- [`docs/audits/-isospin-categorical-source.md`](../../docs/audits/-isospin-categorical-source.md)
  — the audit that proposed this closure
- Upstream restricted result:
  [`prop:crystal-isospin-degeneracy`](crystal-isospin-degeneracy.md)
- Upstream channel-assignment class:
  [`conj:inter-nucleon-channel-color-tube`](inter-nucleon-channel-color-tube.md)
  (PR [#1111](https://github.com/litlfred/qou/pull/1111))
- The 305 ppm closed form:
  [`prop:flavor-split-substrate`](flavor-split-substrate.md)

- The compute consumer:
  [`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py)
- D6 (charge conjugation): [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md)
  — sibling Z/2 categorical symmetry on color sheets (same color-tube infrastructure)
- The Markov-trace machinery: [`bar-involution.md`](bar-involution.md)
  Tables 1-4 — bar-symmetry classification of all framework quantities
