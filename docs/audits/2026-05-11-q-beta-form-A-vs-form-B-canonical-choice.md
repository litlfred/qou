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

## Update 2026-05-11 cycle 5 — REFUTATION

Per owner directive: "Form A ≡ Form B at single-wrap A=1 with full
L_i, R_i context matrices [TEST THIS] … paper is sloppy. we need to
see what we really need from derivation. no paper changes until it
is worked out."

**Numerical test done with full L_i · T · R_i context for β-decay's
two changed crossings** (n → p: pos 1 = (u₁,d₂)→(u₁,u'₂) = ud→uu,
pos 3 = (d₂,d₃)→(u'₂,d₃) = dd→ud):

| Computation | Value | Scale to match Q_β=0.7823 |
|---|---:|---:|
| **(a)** Σ-per-position with proper L_i, R_i | 0.0909 dimensionless | 8.62 MeV/unit |
| **(b)** Full-braid end-to-end log-ratio | 0.0993 dimensionless | 7.89 MeV/unit |
| Form A reference | 0.7836 MeV | — (canonical) |

**No natural framework scale matches** the required 8.62 MeV/unit:
  - m_e = 0.511 MeV
  - E_0 = 4.186 MeV (off by 2×)
  - 2 · E_0 = 8.37 MeV (close but NOT exact)
  - m_e · c_q² = 42.25 MeV (way too large)
  - m_e / (q_0 − 1) = 4.65 MeV
  - m_e / ℏ_q = 5.16 MeV

The ratio Σ_per-position / |Δ(net)_A| = 0.4855 ≈ 1/2 hints at a
missing factor of 2 (perhaps a kinematic Lorentz factor in
β-decay's two-body decay vs three-body, or a Markov-parameter
normalization), but 1/2 doesn't close exactly — the residual after
the 2× correction is still 0.8%, not the 0.17% of Form A.

### Verdict on the conjecture Form A ≡ Form B

**REFUTED at the numerical level** under the V̂_i = z · M_{i,11} +
M_{i,21} definition in `beta-decay-transfer-matrix.md` with any
natural framework scaling.

Three possibilities (all require framework R&D, NOT paper edits
at this time per owner directive):

1. **V̂ definition is wrong** in the existing markdown.
   The doc's V̂_i = z · M_{11} + M_{21} may be incorrect or
   incomplete. The correct V̂_i for energy purposes might involve
   higher-order entries or a different normalization.

2. **L_i, R_i interpretation is wrong**. I used parent (neutron)
   matrices for L_i, R_i throughout. The doc's notation is
   ambiguous — possibly L_i should be the daughter context, or
   L_i should be the symmetrized par+dau context.

3. **Form B genuinely computes a DIFFERENT observable**, not Q_β.
   The transfer-matrix log-ratio is naturally a TRANSITION
   AMPLITUDE or DECAY-RATE factor (probability flow); calling
   it "Q-value in log form" in the doc was likely sloppy
   notation that conflates two related but distinct observables.

### Working hypothesis (most likely)

Option 3 is most plausible — the framework has two related but
DISTINCT observables conflated under the label "Q-value":

- **Energy released** = Q_β (Form A canonical)
- **Decay amplitude** = log-ratio (Form B, related to lifetime/rate)

In standard QFT these are different: the energy is from rest-mass
differences (Form A), the rate is from matrix elements (Form B).
They're related via Fermi's golden rule but not equal.

If this hypothesis is correct, the paper needs:
- Form A explicitly canonical for Q-value (energy)
- Form B explicitly renamed to "decay amplitude" / "transition
  matrix-element log" (rate, lifetime, branching ratio, etc.)
- Bridge formula (Fermi's golden rule analog) connecting them

But these paper changes are DEFERRED per owner directive — first
need to determine which derivation is the right one for which
observable, then update the paper coherently.

## What's needed from the derivation (per owner directive)

The audit should drive the framework's authors to settle:

1. **WHICH physical observable does each form compute?**
   - Q-value (energy released)
   - Decay rate (lifetime)
   - Transition amplitude (cross-section)

2. **WHAT bridge formula connects Form A and Form B** when both
   should give related quantities?

3. **IS the V̂_i definition correct** for energy-scale quantities?
   The simple `z · M_{11} + M_{21}` may be incomplete.

4. **WHAT is the canonical convention** for L_i, R_i context
   matrices in the parent-vs-daughter computation?

Until questions 1-4 are answered, the paper has notation drift
that propagates into computational ambiguity. **No paper
changes** in this PR until the underlying derivation is
unambiguous.

### What this PR delivers

PR #637 stays on Form A throughout (empirically correct +0.17%
residual). The audit doc records the Form A vs B refutation as a
research finding for future framework cleanup. Lean roadmap Gap
#11 (Form A ≡ Form B equivalence) remains open per this audit.
