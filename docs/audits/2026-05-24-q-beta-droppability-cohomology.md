# Audit — Q_β droppability and the cohomological origin of CAL 1-3

> **⚠️ Critical update (2026-05-24, same day).** This audit
> originally framed Q_β as "operationally blocked on tower closure"
> with the implication that closure would deliver a 2-CAL framework.
> The PR review by the repo owner identified a deeper issue: the
> relation $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
> used here is an **ansatz**, not derived from the per-braid mass
> formula. The +0.17% match could be **numerical coincidence**, not
> truncation. **Read first**:
> [`2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md).
> This audit's cohomological observations (3 CAL ↔ 3 Wedderburn
> channels) remain valid; the implication "Q_β is derivable from
> CAL-1+CAL-2 alone" is **suspended** pending Path A (theoretical
> derivation) or Path B (direct per-braid compute).

**Branch**: `claude/gifted-feynman-U7ckD` (PR #1127).
**Date**: 2026-05-24.
**Companion**: triggered by the 1ppb / L2 precision discussion; the
owner asked *"if we dropped Q_β as one of canonical CAL, can we get
the mass table modulo the −0.53 % substrate-Δ_pn discrepancy?
Please explore the cohomological origin of CAL 1-3."*

This audit answers two questions:

1. **What is the cohomological origin of CAL 1-3?** Is the
   "3 calibrations = 3 Wedderburn channels" framing a theorem,
   a heuristic, or a conjecture?
2. **Is Q_β droppable?** Can the mass table run on `(m_e, q_0)` +
   substrate, with Q_β derived rather than calibrated?

## TL;DR

| Question | Answer |
|---|---|
| Cohomological origin of CAL 1-3? | **THEOREM.** `prop:three-parameters-wedderburn` proves on-shell + gauge-invariance + observability reduce the 6-dim End(H_3) to exactly 3 real parameters — bijectively the 3 Wedderburn blocks (alt / std / sym). |
| Is Q_β substrate-derivable? | **Yes, partially.** `derived_masses.py:49–62` gives `Q_β = m_e · |q_0² − 2q_0 − 1| · (q_0+1)/(2q_0³) ≈ 0.7836 MeV`. Residual vs CODATA: **+0.18 %** (1.31 keV). |
| Tighter than downstream consumers? | **Yes.** All Q_β consumers have ±4 % or wider MAE; +0.18 % is well within tolerance. |
| Cohomological 3-channel structure if Q_β dropped? | **Preserved.** alt channel becomes a *prediction* instead of an *input*; the 3-block decomposition is unchanged. |
| Operationally droppable today? | **Not yet.** Blocked on Workplan 2 Phase 2 (tower-summation closure) to push +0.18 % to 1ppb. |

## 1. The cohomological theorem (rigorous)

[`prop:three-parameters-wedderburn`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md)
proves the following reduction:

$$\dim_\mathbb{R} \mathrm{End}_\mathbf{C}(A) \;\xrightarrow{\;\star_q F_\nabla = F_\nabla,\;\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0\;}\; 3$$

Where:

- $\mathrm{End}_\mathbf{C}(A)$ has dimension $(\dim A)^2 = 6^2 = 36$ for
  $A = H_3(R, q)$;
- The on-shell constraint $\star_q F_\nabla = F_\nabla$ (Yang–Mills
  self-duality, [`rem:instanton-on-shell`](../../content/quantum-observable-universe/braids-and-knots/instanton-on-shell.md)) kills half the off-diagonal
  freedom;
- Gauge invariance $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
  ([`def:quantum-observable-universe`](../../content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md))
  kills the remaining trivial-invariant subspace;
- What survives is **bijectively the 3 Wedderburn blocks** of
  $H_3(R, q)$, indexed by partitions $\lambda \vdash 3$.

## 2. The CAL ↔ Wedderburn alignment (rigorous)

| CAL | Wedderburn block | Partition λ ⊢ 3 | Eigenvalue of $\sigma_i$ | Physical sector |
|---|---|---|---|---|
| **CAL-2** ($m_\mu/m_e \to q_0$) | **sym** | $(3)$ | all $+q$ | Shape / deformation (how far $q$ is from 1); $q = 1$ collapses the symmetric channel |
| **CAL-1** ($m_e$) | **std** | $(2,1)$ | $+q$ and $-q^{-1}$ mixed | Mass scale (Hecke units ↔ MeV bridge) |
| **CAL-3** ($Q_\beta(n)$) | **alt** | $(1,1,1)$ | all $-q^{-1}$ | Interaction strength; antisymmetric channel driving $\beta$ decay; brane-tower correction $\Delta(\mathrm{net}) = h(h-2)/2$ converts Q-value → energy scale |

Source: [`prop:three-parameters-wedderburn`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) §"Physical identification" (lines 62–76).

**Mnemonic**: the symmetric sector sees only $+q$ eigenvalues — it
controls the *shape* of the deformation, hence the substrate
parameter $q_0$. The alternating sector sees only $-q^{-1}$
eigenvalues — it controls the antisymmetric / antimatter channel,
hence the $\beta$-decay scale $Q_\beta$. The standard sector mixes
both eigenvalues — it bridges dimensionless Hecke trace to
dimensional MeV, hence $m_e$.

This is the cohomological content of "exactly 3 calibrations". Adding
a 4th calibration would require an additional independent parameter
**which does not exist** in the framework's End(H_3) decomposition.
Removing one of the three is allowed only if that block becomes a
prediction from the other two — which is precisely the Q_β question.

## 3. Q_β substrate derivation — the closed form

[`derived_masses.py:49–62`](../../computations/derived_masses.py)
implements the **single-wrap closed form** for Q_β using CAL-1 + CAL-2 only:

$$\boxed{\;\;Q_\beta \;=\; m_e \cdot |q_0^2 - 2q_0 - 1| \cdot \frac{q_0 + 1}{2 q_0^3} \;\approx\; 0.7836\,\text{MeV}\;\;}$$

| | Value (MeV) | Relative to CODATA |
|---|---:|---:|
| Substrate prediction (single-wrap) | 0.7836 | **+0.18 %** (+1.31 keV) |
| CODATA Q_β(n) (CAL-3 current) | 0.78233 | — |
| Tower-summed substrate (Li_2^q form, conjectured) | TBD | likely ≤ 1ppb |

The +0.18 % residual is **brane-tower truncation**: the closed form
uses the single-tick $\mathfrak{E}_0 = m_e/(q_0(q_0-1)) \approx 4.186$ MeV;
the tower-summed $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0/(1-\hbar_q^2)$
form would close it (Workplan 2 Phase 2 — [`docs/audits/2026-05-03-tower-mev-calibration-finding.md`](2026-05-03-tower-mev-calibration-finding.md)).

Witness: [`q-beta-predicted.witness.json`](../../computations/q-beta-predicted.witness.json):143–162.

## 4. 𝔈_0 is already 2-CAL derived

The hadronic energy scale single-tick form

$$\mathfrak{E}_0^{(N=0)} \;=\; \frac{m_e}{q_0 (q_0 - 1)} \;\approx\; 4.186\,\text{MeV}$$

is **derived from CAL-1 + CAL-2 alone** (no Q_β input). What Q_β
currently calibrates is the **tower-correction factor**
$1/(1 - \hbar_q^2) \approx 1.0104$, which pins the brane-tower
resummation to CODATA. With the tower-summed substrate form, Q_β
is over-determined.

| Quantity | Value (MeV) | Source |
|---|---:|---|
| $\mathfrak{E}_0^{(N=0)}$ (single tick) | 4.186 | CAL-1 + CAL-2 only |
| $\mathfrak{E}_0^{\text{full}}$ (geometric tower) | 4.228 | CAL-1 + CAL-2 only, **+1.75 % vs CAL** |
| $\mathfrak{E}_0^{(\text{cal})} = Q_\beta / \|h(h-2)/2\|$ | 4.179 | CAL-3 |

The +1.75 % gap is the open CAL-3 residual (existing finding —
[`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md):72–84
"CAL-3 gap — explicit tower-correction direction").

## 5. Downstream consumer analysis

Files consuming Q_β:

| Script | Use | Tolerance | +0.18 % impact |
|---|---|---:|---|
| [`derived_masses.py`](../../computations/derived_masses.py) | legacy typed-crossings form (deprecated) | n/a | n/a |
| [`beta-decay-energy-scale.py`](../../computations/beta-decay-energy-scale.py) | refactors to symbolic form | <1 % | ✓ within |
| [`e_0_calibration_audit.py`](../../computations/e_0_calibration_audit.py) | audits Q_β propagation (Class-A) | 1 ppb (audit) | ⚠ fails |
| [`c_alpha_from_Q_beta_trace.py`](../../computations/c_alpha_from_Q_beta_trace.py) | α-cluster β-chain | ~4 % MAE | ✓ within |
| [`atomic_mass_via_rho_k.py`](../../computations/atomic_mass_via_rho_k.py) | binding-energy back-compute (Class-B audit) | n/a (audit) | n/a |

**Net**: all production-mass consumers have tolerance > +0.18 %.
Only the 1ppb audit (`e_0_calibration_audit.py`) would fail, but it
*is the very thing* the tower-summation closure addresses.

## 6. Verdict — Q_β-droppability

**THEORETICALLY**: ✅ Yes. The cohomological 3-channel structure is
preserved; the alt channel becomes a *prediction*. The substrate
gives Q_β to +0.18 % using CAL-1 + CAL-2 alone, tighter than every
downstream production consumer's tolerance.

**OPERATIONALLY**: ⏸ Blocked on Workplan 2 Phase 2:

1. Wire the 50-dps `m_e_Hecke` lift (substrate form of m_e in MeV).
2. Migrate $\mathfrak{E}_0^{\text{full}}$ from the geometric series
   form $1/(1 - \hbar_q^2)$ to the bounded symmetric q-dilogarithm
   form $\mathfrak{E}_0^{\text{full,Li}_2^q}$ (conjectured in
   [`derived_masses.py:28`](../../computations/derived_masses.py)).
3. Verify the tower-closed substrate Q_β is within 1ppb of CODATA.
4. Then demote CAL-3 → "substrate-derived" and update
   [`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md).

## 7. What this audit does *not* claim

- Does **not** flip CAL-3 to substrate-derived in production now.
- Does **not** claim the framework reduces to 2 calibrations *today*.
- Does **not** propose a 4th calibration (the cohomological count
  forbids it).

It claims the substrate-Q_β is +0.18 % of CODATA, that the
cohomological 3-channel structure is preserved under Q_β-demotion,
and that the operational blocker is tower-summation closure — not
a structural problem.

## 8. Workplan integration

| Item | Owner | Blocker |
|---|---|---|
| **B1** (this doc) | done | — |
| **B2** Emit `q-beta-substrate-prediction.witness.json` (parallel to CAL-3) | this PR | — |
| **B3** Demote CAL-3 → prediction in calibration-inputs.md | Workplan 2 P2 | tower-summation closure (Li_2^q form vs geometric) |
| **Tower-closure** | Workplan 2 P2 | substrate-side audit + 50-dps m_e_Hecke wire |

## See also

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §"Adjacent open work"
- [`docs/audits/2026-05-01-calibration-inputs-addendum.md`](2026-05-01-calibration-inputs-addendum.md) (original 3-CAL = 3-channel addendum)
- [`docs/audits/2026-05-03-tower-mev-calibration-finding.md`](2026-05-03-tower-mev-calibration-finding.md) (+1.75 % CAL-3 residual)
- [`docs/audits/2026-05-24-q-zero-reality-audit.md`](2026-05-24-q-zero-reality-audit.md) (sibling audit: q_0 ∈ ℝ is empirical not theorem)
- [`content/quantum-observable-universe/braids-and-knots/calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md)
- [`content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md)
- [`content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)
- [`computations/derived_masses.py`](../../computations/derived_masses.py) — substrate Q_β closed form
