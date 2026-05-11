# Q_β notational choice — settle on Form A (additive counit)

**Status:** audit + recommendation. Per owner directive 2026-05-11
("are you using convolution knot operators correctly?" → "yes
please" verify → "make sure paper is appropriately documented when
switching notations — or can we settle on one?").

## Recommendation: settle on Form A as canonical

The paper has **two functionally distinct Q_β formulations** with
no clean numerical bridge between them. **Form A** gives +0.17%
residual; **Form B** under any natural scaling gives −34% to
+436%. Form A is the empirically-correct canonical form for Q_β
as a physical energy.

| | Form A (counit / additive) | Form B (convolution / log-ratio) |
|---|---|---|
| Source | `prop:neutron-qvalue-symbolic`, `prop:beta-decay-energy-scale` | `prop:beta-decay-transfer-matrix` |
| Formula | $Q_\beta = \lvert\Delta(\text{net})\rvert \cdot E_0$ | $\ln \frac{P_\text{dau}}{P_\text{par}} = \sum_i \ln \frac{\hat V_i^\text{dau}}{\hat V_i^\text{par}}$ |
| Algebra structure | **Frobenius counit** $\varepsilon$ applied to NF subtraction | **Multiplicative / transfer-matrix product** (universal $\Delta_\beta(q)$) |
| At single-wrap (β-decay sector) | $\Delta(\text{net}) = h(h-2)/2$ | $\ln(V_\text{pp}/V_\text{nn})$ |
| Numerical (with $L_i, R_i = I$) | 0.7836 MeV | $0.0993 \cdot \text{(scale)}$ — no natural scaling gives CODATA |
| Residual vs CODATA | **+0.17% / +1.31 keV** | unmatched (any natural scale off by 34–436%) |
| Dimensions of summand | dimensionless × MeV | dimensionless (log) |

## Why Form A is canonical

1. **Empirically tight**: Form A's +0.17% residual sits at 17% of
   the framework's own structural N=0 bound ($\hbar_q^2 / (1-\hbar_q^2)$).

2. **Structurally clean**: $\varepsilon$ is the **Frobenius counit**,
   the standard categorical projection on any Frobenius algebra. By
   `2026-05-11-q-beta-residual-decomposition.md §"Dual-basis
   identity"`, $G^{-1} \cdot t = e_\gamma$, so the counit IS the
   dual-basis-paired quantity against the identity element. No
   weighted-form has missing structure to add.

3. **A=1 base case**: At single wrap, the framework explicitly
   verifies Form A reduces to the crossing-decomposition Form C
   (`q-value-transition.md §"Crossing-level decomposition"`):
   $Q = \sum_\text{changed} \Delta E_\times - S_q(e)$ becomes
   $\lvert h(h-2)/2 \rvert \cdot E_0$.

4. **q-anomaly compatible**: Form A correctly accounts for the
   $\delta_q \propto (A-1)/A^2 \cdot \hbar_q^2$ q-anomaly
   (vanishing at A=1, providing the +1.31 keV brane-tower
   residual at N=0 single-tick).

## Why Form B doesn't replace Form A (as currently written)

`beta-decay-transfer-matrix.md:138-145` documents Form B as
"Q-value in log form" but under the natural V̂ definition
$\hat V_i = z \cdot M_{i,11} + M_{i,21}$ with simple L_i = R_i = I
context matrices, the resulting $0.0993 \cdot (\text{scale})$
doesn't yield CODATA $Q_\beta = 0.782$ MeV under any tested
scaling (m_e, E_0, m_e · c_q², m_e / ℏ_q, etc. — all off by 34%
to 436%).

**Two non-exclusive explanations**:

(a) **Form B is actually the DECAY-RATE / TRANSITION-AMPLITUDE
    formula**, not the energy Q_β. In standard QFT, the
    transfer-matrix product gives a probability flow, not the
    rest-mass difference. The "Q-value" wording in the markdown
    is then a misnomer — should be "transition amplitude" or
    "decay rate factor".

(b) **Form B is Q_β but requires the L_i, R_i context matrices**
    explicitly. The reduction to ln(V_pp/V_nn) via telescoping
    works ONLY if L_i and R_i are scalar multiples of I; for
    non-trivial L, R the log-ratio doesn't telescope and the
    sum-over-affected-crossings gives a different value.

Either way, the paper currently presents Form B as if it's a
drop-in equivalent of Form A. **It is not** (numerically verified
in this commit).

## Recommended doc-level fixes

| File | Current statement | Recommended fix |
|---|---|---|
| `beta-decay-transfer-matrix.md:138` | "The Q-value in log form: $\ln(P_\text{dau}/P_\text{par}) = \sum_i \ldots$" | Either: (1) rename to "transition amplitude" / "decay rate factor", OR (2) prove the equivalence to Form A explicitly with the right L_i, R_i, OR (3) add caveat "this gives a related dimensionless invariant, not Q_β in MeV directly" |
| `prop:beta-decay-transfer-matrix.md` § "decay formula" | Implicit "energy" framing | Make explicit which physical observable it computes (energy vs rate vs amplitude) |
| `neutron-qvalue-symbolic.md` | Form A | Keep — flag this as the **canonical Q_β derivation** for paper consumers |
| `prop:beta-decay-energy-scale` | Defines E_0 | Cross-reference Form A as the canonical Q_β |

## What "settle on one approach" means concretely

For the paper:
- **Q_β at A=1 (free neutron β-decay)**: use Form A — $Q_\beta = \lvert h(h-2)/2 \rvert \cdot E_0$ (single-wrap symbolic closed form).
- **Q-value at A≥2 (nuclear β-decays)**: extend Form A — $Q = M(\text{par}) - M(\text{dau})$ via `q-value-transition.md` definition, with the q-anomaly correction $\delta_q$ added at A≥2.
- **Transfer matrices** (`beta-decay-transfer-matrix.md`): retain for **theoretical infrastructure** (proving the universal $\Delta_\beta(q)$ exists, level-independence, etc.), but **do not present as a numerical Q_β derivation** in the paper unless the equivalence to Form A is proved with full L, R context.

For Lean (`MassComputationChainRoadmap.lean`):
- Gap 4 (Φ_q convergence): unchanged — relevant for the brane-tower
  closure regardless of which Q_β form.
- Gap 5 (n_⋆ existence): unchanged — same.
- **NEW Gap 11** (suggested): prove Form A ≡ Form B (when properly evaluated with L, R context) at single-wrap A=1. Currently OPEN — numerical evidence says they DIFFER. Either a structural equivalence theorem is needed, or Form B is reframed as a different observable.

## Impact on PR #637 deliverables

No changes needed. PR #637 already uses Form A throughout:
- `derived_masses.q_beta_predicted_mev` — Form A
- `q_beta_predicted.py` — Form A
- `np-discrepancy-resolution.md` — references Form A
- `energy-scale-planck.md` — Form A's $E_0$

This audit *adds* the recommendation to flag Form B as
non-equivalent or rename it; it does NOT request modifying any
existing Form A material.

## TL;DR

**Yes, settle on one** — Form A (counit / additive / single-wrap
symbolic) is empirically correct and structurally clean. Form B
(transfer-matrix log-ratio) does not numerically reduce to
Q_β under any natural scaling; should be either renamed (to
decay rate or transition amplitude) or have its Q_β-equivalence
proved explicitly with the L_i, R_i context matrices.
