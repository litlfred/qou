**Proposition (Interface-knot contribution to canonical-atom Markov trace).**

*Let $\beta_K \in H_{3A}(q)$ be the canonical atomic braid for atom
$K = (Z, N)$ with $A = Z + N$, decomposed as*
$$
  \beta_K \;=\; \beta_K^{\mathrm{constit}} \cdot \Delta_I^K
$$
*where $\beta_K^{\mathrm{constit}} = \beta_p^{(1)} \cdots \beta_n^{(N)}$
is the disjoint Hecke product on disjoint 3-strand blocks (constituent
vacuum, [`def:ew-interface-knot`](#def:ew-interface-knot)) and
$\Delta_I^K$ is the interface knot — a product of single-generator
crossings at the strand-block boundaries
$g \in \{3, 6, \ldots, 3(Z+N-1)\}$, each one either $\sigma_g$
(positive) or $\sigma_g^{-1}$ (negative).*

*Then the Markov trace ratio satisfies the **Markov-axiom interface
identity***
$$
  \boxed{\;
    \frac{\tau_M(\beta_K)}{\tau_M(\beta_K^{\mathrm{constit}})}
    \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)}
  \;}
  \tag{$\star$}
$$
*exactly, where $z(q) = 1/(q^{1/2}+q^{-1/2})$ is the Markov parameter,
$h(q) = q - q^{-1}$ is the Hecke skein parameter, and $p_+(K)$ /
$p_-(K)$ are the counts of positive / negative interface generators
in $\Delta_I^K$.*

### Proof (Markov axiom + Hecke skein)

For a positive interface generator $\sigma_g$, the **Markov axiom**
([`thm:jones-markov-trace`](#thm:jones-markov-trace)) gives
$$
  \tau_M(\alpha \cdot \sigma_g) \;=\; z \cdot \tau_M(\alpha)
  \qquad \forall\, \alpha \in H_{n}(q).
$$
For a negative interface generator $\sigma_g^{-1}$, the **Hecke skein
relation** $\sigma_g^{-1} = \sigma_g - h \cdot \mathbf{1}$ combined
with linearity of $\tau_M$ gives
$$
  \tau_M(\alpha \cdot \sigma_g^{-1})
  \;=\; \tau_M(\alpha \cdot \sigma_g) - h \cdot \tau_M(\alpha)
  \;=\; (z - h) \cdot \tau_M(\alpha).
$$
Iterating over the $p_+(K) + p_-(K)$ interface generators of
$\Delta_I^K$ — each one is "topmost" relative to the constituent
sub-braid below it — and applying the appropriate factor per sign
yields the boxed identity ($\star$).

### Empirical verification (4 atoms, 50-dps Rust kernel)

Computed via [`delta_lambda_fr_identity_phase5c.py`](../../../folio-assistant/computations/delta_lambda_fr_identity_phase5c.py)
using `pyhecke_native` for full $\tau_M$ at $H_n$ for $n \in \{6, 9, 12\}$:

| atom | $A$ | $p_+$ | $p_-$ | $\tau_M^{\mathrm{FULL}}/\tau_M^{\mathrm{CONSTIT}}$ | predicted $z^{p_+}(z-h)^{p_-}$ | rel. err. |
|---|:-:|:-:|:-:|---:|---:|---:|
| D    | 2 | 1 | 0 | 0.49932033 | 0.49932033 | $5\times10^{-16}$ |
| T    | 3 | 1 | 1 | 0.14493273 | 0.14493273 | $9\times10^{-16}$ |
| ³He  | 3 | 2 | 0 | 0.24932080 | 0.24932080 | $1\times10^{-15}$ |
| ⁴He  | 4 | 2 | 1 | 0.07236786 | 0.07236786 | $1\times10^{-15}$ |

Max rel. err. across all 4 atoms: $\sim 10^{-15}$ — exact at f64 precision.

Per-atom interface census (from `atom_braid_word_3A`):

- **D**: $p \cdot \sigma_3 \cdot n$ — 1 positive (p-n).
- **T**: $p \cdot \sigma_3 \cdot n \cdot \sigma_6^{-1} \cdot n$ — 1 positive (p-n) + 1 negative (n-n).
- **³He**: $p \cdot \sigma_3 \cdot p \cdot \sigma_6 \cdot n$ — 2 positive (p-p, p-n).
- **⁴He**: $p \cdot \sigma_3 \cdot p \cdot \sigma_6 \cdot n \cdot \sigma_9^{-1} \cdot n$ — 2 positive (p-p, p-n) + 1 negative (n-n).

### Structural reading

The interface knot $\Delta_I^K$ is **categorically the Markov-axiom
boundary contribution** to the canonical atomic braid:

- **Positive interface** $\sigma_g$ (p-p or p-n boundary) → factor $z$ exactly
  (single application of the Markov axiom).
- **Negative interface** $\sigma_g^{-1}$ (n-n boundary, antisymmetric quark
  pair) → factor $z - h$ exactly (Markov axiom + Hecke skein $\sigma^{-1} =
  \sigma - h \cdot \mathbf{1}$).

The crossing-sign / nucleon-flavor pairing is encoded in
$\Delta_I^K$ via $p_+(K)$ and $p_-(K)$ counts — these are determined
structurally by the canonical-braid construction, not phenomenologically
fit.

This locks PR #801's interface-knot factorisation as
*derivation-grade*: each interface in the canonical atomic braid
contributes a Markov-trace factor that is either $z$ or $z - h$,
determined by the crossing sign. No empirical-fit parameter remains
at the $\tau_M$ level.

### Consequences

1. **Atom-braid trace factorisation.** For any canonical atomic braid:
   $$
     \tau_M(\beta_K) \;=\; z^{p_+(K)} \cdot (z-h)^{p_-(K)} \cdot \tau_M(\beta_K^{\mathrm{constit}}).
   $$

2. **Per-Z step.** Adding a proton (Z+1) inserts one positive interface
   (p-* boundary): $\tau_M$ multiplies by $z$.

3. **Per-N step within a pair.** Adding a neutron after an existing
   neutron (n-n boundary) inserts one negative interface: $\tau_M$
   multiplies by $z - h$ (not by $z$).

4. **Per-N step crossing pair-flavor.** Adding a neutron after a proton
   (p-n boundary) inserts one positive interface: factor $z$.

5. **Phase 5b $\cosh(h)$ correction lives ELSEWHERE.** The per-Z step
   factor $\alpha \approx [3]_q^2 \cdot \cosh(h)$ identified in
   [`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction)
   is at the **single-block $|\Delta_\lambda^*|$ extraction level**,
   not the full $\tau_M$ ratio. The $\tau_M$-level identity is
   *exact* ($\star$); the single-block-level correction is *empirical*
   and structurally distinct.

### Implementation reference

- Script: [`folio-assistant/computations/delta_lambda_fr_identity_phase5c.py`](../../../folio-assistant/computations/delta_lambda_fr_identity_phase5c.py)
- Witness: `folio-assistant/computations/delta-lambda-fr-identity-phase5c.witness.json` (2 assertions; **Markov-axiom interface identity passes to $10^{-15}$ rel. err.**)
- Cross-reference (PR #801): [`def:ew-interface-knot`](#def:ew-interface-knot) (the canonical interface-knot definition).
- Cross-reference (PR #819): Phase 5c.1 audit doc covers the empirical extraction; this proposition is the categorical resolution.
