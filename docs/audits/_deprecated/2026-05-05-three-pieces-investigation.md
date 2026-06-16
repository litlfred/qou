> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# Three-pieces investigation: Piece 1 (dimensional bridge), Piece 2 (linked-cluster), Piece 3 (interface/intra split)

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Refs:**
- [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md)
- [`docs/audits/2026-05-05-kashaev-limit-pair-gen-investigation.md`](2026-05-05-kashaev-limit-pair-gen-investigation.md)
- [`computations/piece1_dimensional_bridge_probe.py`](../../computations/piece1_dimensional_bridge_probe.py)
- [`computations/piece2_linked_cluster_probe.py`](../../computations/piece2_linked_cluster_probe.py)
- [`computations/piece3_interface_vs_intra_probe.py`](../../computations/piece3_interface_vs_intra_probe.py)
- Sibling PR [#546](https://github.com/litlfred/qou/pull/546) — closed-form $\mathrm{tr}_M(p)$ with leading $-1/12$
- Sibling PR [#545](https://github.com/litlfred/qou/pull/545) — Term-6 closed-form $A \geq 2$

## Piece 1 — dimensional bridge $E_0 \leftrightarrow \alpha$

**Targets at $q_0$:**
- $E_0 / \alpha = 46.55$ (from proton calibration of six-term theorem)
- $m_p / m_e = 1836.15$ (CODATA)

**Best categorical fits** (`piece1-dimensional-bridge.witness.json`):

| Formula | Value | Error vs target |
|---|---:|---:|
| $12 \cdot 153 = 1836$ | $1836.00$ | $-0.008\%$ (suspect: 153 not categorical) |
| $18 / \hbar_q^2$ | $1833.52$ | $-0.143\%$ |
| $9 \cdot [2]_q / \hbar_q^2$ | $1843.51$ | $+0.401\%$ |

**Striking match: $m_p / m_e \approx 18 / \hbar_q^2$** to 0.14 % — and the **18** is **exactly the per-proton coefficient in the atomic-shift formula** $\mathrm{shift} = 18 Z + 21 N + 1$ from `docs/audits/2026-05-03-w3-habiro-unblocked.md`.

This is suggestive of a deeper identity:
$$m_p / m_e \;=\; \mathrm{shift}_p / \hbar_q^2 \;+\; \mathrm{(small correction)}$$
where $\mathrm{shift}_p = 18$ is the per-proton intra-nucleon shift coefficient and $\hbar_q = (q-1)/q$ at $q_0$.

For $E_0/\alpha$, no clean fit within 5 %; the closest is $8G \cdot 6 = 43.97$ ($-5.5\%$), where $6 = |S_3|$. The factor of $46.6$ remains structurally open.

**Closing Piece 1** requires:
- Derivation of $m_p / m_e \approx 18/\hbar_q^2$ from H_3$(q)$ rep-theory + atomic-shift coefficient $(18, 21, 1)$
- Or: PR #546's closed-form $\mathrm{tr}_M(p) = -1/12 \cdot \mathrm{poly}(q)$ resolved with the factor-of-2 normalisation, giving $E_0$ directly

## Piece 2 — linked-cluster structure $T_2$ vs $T_3$

**Targets** (`piece2-linked-cluster.witness.json`, from `paper-six-term-isotope-sweep`):

| Atom | $A$ | $T_2$ | $T_3$ | $T_3 / T_2^2$ |
|---|--:|--:|--:|--:|
| p | 1 | $1.618$ | $0.198$ | $0.076$ |
| n | 1 | $1.526$ | $0.176$ | $0.076$ |
| D | 2 | $3.393$ | $1.357$ | $0.118$ |
| T | 3 | $5.072$ | $3.326$ | $0.129$ |
| ³He | 3 | $5.350$ | $3.730$ | $0.130$ |
| ⁴He | 4 | $7.030$ | $6.692$ | $0.135$ |

**Finding:** $T_3 / T_2^2$ varies $0.076 \to 0.135$ (54 % spread). **Not** a simple cumulant relation $T_3 = T_2^2 / 2$ (which would predict constant $0.5$).

Instead: $T_3 / T_2^2$ **monotonically increases with $A$** from $0.076$ at $A = 1$ to $0.135$ at $A = 4$. This rules out classic linked-cluster but suggests **A-dependent cluster expansion** with a structure like
$$T_3 \;=\; f(A) \cdot T_2^2 / 2$$
where $f(A)$ grows with $A$ — possibly reflecting interface count or LR-block multiplicity.

**Closing Piece 2** requires:
- Interpretation of the monotonic A-trend (interface-count $A - 1$? LR-block dim?)
- Structural derivation that gives $T_3$ in terms of $T_2$ via the refined Sub-lemma 2.1's operator-valued $A^\lambda_{\mu, \nu}(I)$

## Piece 3 — interface vs intra-generator split

**Most striking finding** (`piece3-interface-vs-intra.witness.json`):

The single-gen log-volume sum $\Sigma_i \ln|V_i^{\mathrm{full}}|$ splits cleanly:

| Measure | Value (mean across $Z = 1..20$) | Spread |
|---|---:|---:|
| Per-nucleon intra log-sum | $-0.114$ | $< 1\%$ |
| Per-interface inter log-sum | $-1.40$ | $< 1\%$ |

**Two universal categorical constants** capture the entire single-gen formula:

$$\alpha \cdot \Sigma_i \ln|V_i^{\mathrm{full}}| \;\approx\; \alpha \cdot \bigl[-0.114 \cdot A \;-\; 1.40 \cdot (A - 1)\bigr]$$

In MeV at $q_0$:
$$\alpha \cdot \Sigma_i \ln|V_i^{\mathrm{full}}| \;\approx\; -0.426 \cdot A \;-\; 5.24 \cdot (A - 1) \;\;\;[\text{MeV}]$$

This is **far cleaner** than the per-generator decomposition. The $0.18\%$ atomic-mass accuracy of `prop:atomic-braid-mass` is captured by **two universal numbers** at $q_0$, not the full per-generator sum.

**Significance:**

1. The "single-gen formula" is structurally a **two-constant linear-in-$A$ correction**, not a true per-generator sum.
2. The intra constant ($-0.114$) characterises the per-nucleon braid log-volume — derivable from the proton/neutron braid words alone.
3. The inter constant ($-1.40$) characterises the per-interface braid log-volume — directly comparable to the operator-valued $A^\lambda_{\mu, \nu}(I)$ from refined Sub-lemma 2.1.

**Closing Piece 3** requires:
- Closed-form expressions for the per-nucleon intra log-sum and the per-interface inter log-sum at $q_0$
- Connection of the per-interface $-1.40$ to $\ln|A^\lambda_{\mu, \nu}(I)|$ for the $\sigma_{n_1}$ boundary generator (refined Sub-lemma 2.1)

## Combined picture

The three pieces are interconnected:

- **Piece 3** shows the single-gen formula reduces to a clean two-constant form with universal intra ($-0.114$) and inter ($-1.40$) coefficients.
- **Piece 1** shows $m_p / m_e \approx 18 / \hbar_q^2$ to $0.14\%$, where 18 is the per-proton intra-nucleon shift coefficient. Suggestive that the per-nucleon intra constant ($-0.114$) is structurally tied to the shift coefficient $18$.
- **Piece 2** shows $T_3 / T_2^2$ has A-dependent structure, not pure cumulant — likely reflecting interface count $(A - 1)$ from Piece 3.

**Working hypothesis (open):**

$$\rho_K \cdot m_e \cdot |\mathrm{tr}_M(\beta_K)| \;=\; \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\text{constituent}} \;+\; \underbrace{c_{\mathrm{intra}} \cdot A}_{\text{intra correction}} \;+\; \underbrace{c_{\mathrm{inter}} \cdot (A - 1)}_{\text{interface correction}} \;+\; (\text{higher})$$

with categorical constants
$$c_{\mathrm{intra}} \;=\; \alpha \cdot (-0.114) \;\approx\; -0.426 \text{ MeV per nucleon}$$
$$c_{\mathrm{inter}} \;=\; \alpha \cdot (-1.40) \;\approx\; -5.24 \text{ MeV per interface}$$

These should be derivable from:
- $c_{\mathrm{intra}}$: per-nucleon Hoefsmit closed form (PR #546's $\mathrm{tr}_M(p)$ closed form is the input)
- $c_{\mathrm{inter}}$: refined Sub-lemma 2.1's operator-valued $A^\lambda_{\mu, \nu}(I)$ at the boundary generator

Combined with **Piece 1's $m_p/m_e \approx 18/\hbar_q^2$** identity, the entire categorical mass program reduces to:
1. Derive $m_p / m_e$ closed form (anchored by 18 and $\hbar_q$).
2. Compute closed forms for $c_{\mathrm{intra}}, c_{\mathrm{inter}}$ from PR #546 + refined Sub-lemma 2.1.

## Cross-coordination with sibling PRs

| Piece | Closes via | Sibling PR |
|---|---|---|
| Piece 1 | Closed-form $\mathrm{tr}_M(p)$ + factor-of-2 resolution | [#546](https://github.com/litlfred/qou/pull/546) |
| Piece 2 | Term-6 closed form for $A \geq 2$ | [#545](https://github.com/litlfred/qou/pull/545) |
| Piece 3 | Closed-form $A^\lambda_{\mu, \nu}(I)$ for boundary $\sigma$ | refined Sub-lemma 2.1 (this branch) |

Both sibling PRs have been notified and asked to cross-post relevant progress.

## Open question synthesis

The categorical-mass program reduces to **two open derivations**:

**(I) Derive $m_p / m_e \approx 18 / \hbar_q^2$ from H_3$(q)$ rep-theory + atomic-shift coefficient $(18, 21, 1)$.**

**(II) Derive the universal categorical constants** $c_{\mathrm{intra}} = -0.114 \cdot \alpha$ and $c_{\mathrm{inter}} = -1.40 \cdot \alpha$ from per-nucleon Hoefsmit + per-interface refined Sub-lemma 2.1.

Closing both gives the full categorical mass formula with **zero empirical inputs** beyond $q_0$ and $m_e$.
