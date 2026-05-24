# Q_β `net`-ansatz fitting finding (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)  ·  **Triggered by**: owner directive "I think only 2 CAL is numerical coincidence... no fitting PLEASE"  ·  **Status**: open finding, requires follow-up Path A / Path B (see below)

## Finding (one sentence)

The framework's free-neutron Q-value closed form
$Q_\beta = m_e \cdot |q_0^2 - 2 q_0 - 1| \cdot (q_0+1)/(2 q_0^3) \approx 0.7836$ MeV
**presented as a 2-input prediction** rests on a relation
$Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
that is **postulated "by construction"**, not derived from the
canonical per-braid mass formula, leaving open whether the +0.17%
match to CODATA is genuine truncation residual or numerical
coincidence (fitting).

## Step-by-step derivation chain audit

| Step | Status | Source / evidence |
|---|---|---|
| **1.** Proton braid word = [u, u, d] in $B_3$ | ✓ **Derived** | Standard Model quark content (forced) |
| **2.** Neutron braid word = [u, d, d] in $B_3$ | ✓ **Derived** | Standard Model quark content (forced) |
| **3.** Typed-crossing operators: $C(\mathfrak{u},\mathfrak{u};\sigma_k) = \sigma_k$, $C(\mathfrak{d},\mathfrak{d};\sigma_k) = \sigma_k - h$, $C(\mathfrak{u},\mathfrak{d};\sigma_k) = \sigma_k - h/2$ | ✓ **Derived** | [`def:typed-crossing-operator`](../../content/quantum-observable-universe/braids-and-knots/typed-crossing-operator.md): up-up = positive orientation, down-down = inverse via Hecke relation, mixed = symmetric midpoint forced by $\mathfrak{u} \leftrightarrow \mathfrak{d}$ swap symmetry |
| **4.** Single-wrap convention: proton ≡ $\sigma_0 \cdot (\sigma_1 - h/2)$, neutron ≡ $(\sigma_0 - h/2)(\sigma_1 - h)$ | ✓ **Derived** as N=0 brane-tower truncation | Minimal braid (one crossing per generator); higher orders = higher tower levels |
| **5.** NF reduction in H_3(q): exact algebra | ✓ **Derived** | Hecke relation $\sigma_i^2 = h \sigma_i + 1$; proton → $L_+ - (h/2)\sigma_0$; neutron → $L_+ - h\sigma_0 - (h/2)\sigma_1 + (h^2/2)\gamma$ |
| **6.** $\Delta(\mathrm{net}) = \mathrm{net}(n) - \mathrm{net}(p) = h(h-2)/2$ where $\mathrm{net} = \sum_i c_i$ over the 6 NF basis elements | ⚠️ **Computation derived; identification of `net` with mass-formula NOT derived** | [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md) and [`beta-decay-energy-scale.md`](../../content/quantum-observable-universe/archimedean-universe/beta-decay-energy-scale.md) compute the unweighted sum, but DO NOT prove this sum equals the leading-order contribution to $\mathfrak{m}(W)$ |
| **7.** Energy scale $\mathfrak{E}_0 = m_e/(q(q-1))$ (single-tick / N=0 truncation) | ✓ **Derived** | [`energy-scale-planck.md`](../../content/quantum-observable-universe/braids-and-knots/energy-scale-planck.md): Planck-tick energy quantum from cohomological mass formula |
| **8.** $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ | ⚠️ **POSTULATED, NOT DERIVED** | [`pre-archimedean-derivation-chain.md`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) line 391: "**so $Q_\beta = \|\Delta(\mathrm{net})\| \times \mathfrak{E}_0$ by construction**". This is the gap. |
| **9.** Closed form $Q_\beta = m_e \cdot \|q^2 - 2q - 1\| \cdot (q+1)/(2q^3)$ | ✓ **Algebraic consequence of (6, 7, 8)** | Pure substitution; valid IF the ansatz (8) is valid |
| **10.** Numerical: 0.7836 MeV vs CODATA 0.7823 MeV (+0.17%) | ✓ **Empirically verified** | Match holds at the substrate $q_0 \approx 1.10998$ |

## Why this matters

The framework's canonical mass formula is the **per-braid mass tower**
[`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md):

$$\mathfrak{m}(W) = |\mathrm{tr}_M(W)| + \sum_n \left[\sum_{\xi \in \mathcal{S}^{(n)}_1} \Phi_q(|\mathrm{tr}_M(\xi)|) + z^2 \sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2} \Phi_q(|\mathrm{tr}_M(\xi\xi')|)\right] + R_N$$

This uses the **Markov-trace-weighted** sum: $\mathrm{tr}_M(\gamma) = z$,
$\mathrm{tr}_M(\sigma_i) = z^2$, $\mathrm{tr}_M(L_+) = z^3$, etc.
Different NF basis elements contribute with different weights.

The "net" in the Q_β derivation is the **unweighted** sum $\mathrm{net}(W) = \sum_i c_i$
where $W = \sum_i c_i e_i$ in the NF basis $\{e_i\}$. **This is a different quantity**.

The relation $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
**asserts that the unweighted NF sum gives the leading-order
mass difference at first order in $h$** — but this is asserted
"by construction", not proved as an expansion of the per-braid
mass tower.

## Two possibilities for the +0.17% residual

| Possibility | Implication |
|---|---|
| **(a) Genuine truncation residual** | The unweighted `net` formula is the correct leading order; the +0.17% gap is the $O(h^2)$ tower correction, closeable by tower-summation. Q_β IS derivable from CAL-1 + CAL-2 at 1ppb after tower closure. |
| **(b) Numerical coincidence (fitting)** | The unweighted `net` formula happens to match Q_β to 0.17% at the specific substrate $q_0 \approx 1.110$, but is not the correct leading order. No amount of "tower closure" will close the gap because the wrong leading-order operator was identified. Q_β is NOT derivable from CAL-1 + CAL-2; it remains genuinely independent. |

The framework currently assumes (a) implicitly. The +0.17% match is taken as evidence FOR the ansatz. **But there is no independent derivation.**

## Three paths to resolve

| Path | What | Cost | Verifies |
|---|---|---|---|
| **A. Theoretical derivation** | Expand the per-braid mass tower $\mathfrak{m}(W) = \|\mathrm{tr}_M(W)\| + \sum \Phi_q + \dots$ at leading order in $h$. Show $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e = \|\Delta(\mathrm{net})\| \cdot \mathfrak{E}_0 + O(h^3)$. | 1-2 days analytical work | If derivation succeeds: (a). If fails or finds discrepancy: (b). |
| **B. Direct compute** | Compute $\mathfrak{m}(p)$ and $\mathfrak{m}(n)$ DIRECTLY via the per-braid mass tower (Markov-trace-weighted + Φ_q). Compare $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ to CODATA. | 1-2 hours implementation + run | Whether canonical mass formula even produces correct $Q_\beta$ without the ansatz. |
| **C. Cleanup** | Update all paper content blocks claiming Q_β derivation to honestly label the relation $Q_\beta = \|\Delta(\mathrm{net})\| \cdot \mathfrak{E}_0$ as an **ansatz** pending A or B. | ~1 hour mechanical edits | Honesty in present claims. |

**This finding selects all three paths.** B + C are in scope for the current PR; A is queued for a follow-up branch.

## Action items (this branch)

- [x] Revert duplicative `prop:q-beta-substrate-prediction` block (commit `6c317e19`)
- [ ] Cleanup `neutron-qvalue-symbolic.md` — add ansatz banner via `authorNotes`
- [ ] Cleanup `beta-decay-energy-scale.md` — flag `Q_β = |Δ(net)|·E_0` as ansatz
- [ ] Cleanup `pre-archimedean-derivation-chain.md` — clarify "by construction" = ansatz
- [ ] Cleanup `calibration-inputs.md` §"CAL-3 gap" — honestly state dual status
- [ ] Update PR description to surface this finding prominently

## Follow-up branches queued

- `claude/q-beta-direct-per-braid-compute-<utc-ymd>` — Path B: per_braid_q_beta_direct.py
- `claude/q-beta-net-ansatz-leading-order-<utc-ymd>` — Path A: theoretical derivation
- `claude/q-beta-im-q0-coupling-<utc-ymd>` — sequels: connect +0.17% to complex-q exploration, Φ_q under bar/star/skew

## Cross-references

- Authoritative ansatz statement (the gap): [`pre-archimedean-derivation-chain.md:391`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md#L391)
- Canonical mass formula (the right formalism): [`per-braid-mass-tower.md`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md)
- The current "prediction" block (will be updated): [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md)
- Owner directive flagging this: PR #1127 chat (2026-05-24): *"I think only 2 CAL is numerical coincidence, but I don't know what you are doing exactly. please justify every step. no fitting PLEASE"*

## Open structural questions raised by owner (same chat)

1. **q_0 ∈ ℂ exploration**: if (b) holds, the +0.17% gap is NOT brane-tower truncation. Could it be Im(q_0) effects? Answered no in the current framework (q_0 fixed by real $m_\mu/m_e$ ratio per [`skein-mass-relation.md`](../../content/quantum-observable-universe/observations/skein-mass-relation.md): $\mathrm{Vol}(4_1)/\hbar_q^2$ where Vol is real). To make this question well-posed, would need an Im observable to constrain.
2. **Φ_q under bar / star / skew involutions, pre vs post Archimedean**: if the per-braid mass formula has involutive structure that the unweighted `net` formula doesn't reproduce, that's evidence FOR (b). Open analytical work; not yet started.
3. **q_0 = Re(complex observable)?**: in current framework, no. q_0 is the real solution to the real equation $\mathrm{Vol}(4_1)/\hbar_q^2 = 206.768$. Extending would require either a complex-valued $m_\mu/m_e$ observable (none in the current framework) or postulating that the categorical observable IS complex but only Re is measured.

The fitting concern (b) is the dominant gap; the structural questions are secondary until A or B disambiguates.
