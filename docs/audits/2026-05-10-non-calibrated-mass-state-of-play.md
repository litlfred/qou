# Non-calibrated mass state of play

**Status:** research note documenting the state of nucleon mass
prediction in **non-calibrated mode** (CAL-1 $m_e$ + CAL-2 $q_0$
only, no CAL-3 $Q_\beta$ input). Per owner directive 2026-05-10:
"we are NOT TO USE calibration except three allowed".

## Three allowed calibrations (AGENTS.md three-calibration-discipline)

| Cal | Source | Value |
|---|---|---|
| CAL-1 | $m_e$ (electron rest mass) | 0.51099895 MeV (CODATA 2022) |
| CAL-2 | $q_0$ (substrate parameter via $m_\mu/m_e$) | 1.10998 |
| CAL-3 | $Q_\beta$ (free-neutron β-decay Q-value) | 0.78233 MeV |

**Non-calibrated mode = CAL-1 + CAL-2 only**, i.e. predict $Q_\beta$
and all masses purely from $m_e$ and $q_0$. This is what
`derived_masses.q_beta_predicted_mev()` (commit `4649650f`) does.

## What we get in non-calibrated mode

### Q_β prediction (per-block, β-decay sector)

$$Q_\beta = |\Delta(\mathrm{net})| \cdot E_0^\text{derived}
        = h(h-2)/2 \cdot m_e/(q_0(q_0-1))
        \approx 0.7836 \text{ MeV}$$

vs CODATA 0.78233 MeV — **+0.17% / +1.31 keV** (commit
`4649650f`). This is the framework's CURRENT BEST non-calibrated
prediction. Works because the NF-coefficient-sum DIFFERENCE
$\Delta(\text{net})$ sidesteps the per-nucleon mass derivation.

### Per-nucleon mass predictions (3-term assembly)

Three framework formula implementations, all non-calibrated, all
DIFFER:

| Implementation | $m_p$ pred (MeV) | $m_n$ pred (MeV) | Direction | Source |
|---|---:|---:|---|---|
| 6-term witness, $E_0 \cdot T_1 + T_4$ at A=1 | +5.74 | +5.14 | $m_p > m_n$ ✗ | `mass-formula-6term-mpfr-50dps.witness.json` |
| 6-term witness, all 6 with $E_0$ derived | −19.97 | −19.20 | $m_n > m_p$ ✓ (but negative) | same |
| `mass_endomorphism.py` Φ_q tower | **+955.5** | **~411** | $m_p \gg m_n$ ✗✗ | `mass-endomorphism.witness.json`, np-discrepancy-resolution.md |
| CODATA target | 938.272 | 939.565 | $m_n > m_p$ ✓ | — |

**None match CODATA in non-calibrated mode.** mass_endomorphism
gets proton close (+1.84%) but neutron is off by −56%. 6-term gives
~6 MeV — way under (T2+T3 = 0 at A=1 per PR #533).

### Q_β derivation from per-nucleon masses

| Formula source | $Q_\beta = m_n - m_p - m_e$ | vs CODATA |
|---|---:|---:|
| Per-block $|\Delta(\mathrm{net})| \cdot E_0$ | +0.7836 | +0.17% / +1.31 keV |
| 6-term $E_0 \cdot T_1 + T_4$ | −1.110 | wrong sign (n < p) |
| mass_endomorphism Φ_q tower | −544.5 | nonsensical |

## Where we are under, and where we are over

> **"w/ non-calibrated mass, we are under?"** — answer per
> implementation:

| Implementation | Proton | Neutron |
|---|---|---|
| 6-term (no tower at A=1) | UNDER by ~163× | UNDER by ~183× |
| mass_endomorphism Φ_q tower | **OVER** by 1.84% | UNDER by 56% |
| Per-block $|\Delta(\mathrm{net})| \cdot E_0$ | n/a (no per-nucleon) | n/a |

So depending on which framework implementation you trust, we're
either **under by 99%** (6-term) or **OVER for proton, UNDER for
neutron** (mass_endomorphism). The two implementations disagree
about the A=1 brane tower's magnitude (PR #533 says it's
structurally empty; mass_endomorphism gives ~10⁶ cat-units).

## Adding all the terms: does it close?

> **"can we add all the terms to that now?"** — answer: yes, but
> it doesn't close.

Tested 7 different all-terms recipes (E_0 · T1, E_0 · T1 + T4,
E_0 · T1 + T4 + T6·m_e, etc.) — none reaches 938 MeV with the
right n-p direction. The closest with right sign is the
dimensionally-mixed "all 6 sum · m_e" recipe at +0.094 MeV for
Δm (vs CODATA +1.293), which only gets the sign right by relying
on the sign-indefinite T5 (chirality BW).

The ONLY thing that closes is the **calibrated** form (using
CAL-3 $Q_\beta$ as E_0), per `np-discrepancy-resolution.md`:

| With β-calibration $E_0 = 0.782$ MeV (CAL-3) | $m_p$ | $m_n$ |
|---|---:|---:|
| Prediction | 938.272 | 939.054 |
| vs CODATA | exact (by calibration) | +0.05% |

But this **consumes CAL-3** as input. We can't both consume CAL-3
and predict $Q_\beta$.

## The deep structural issue

Two structural problems lock the residual at this level:

1. **A=1 brane tower disagreement**. PR #533 says it's structurally
   empty in the canonical Wenzl-bridge formulation; `mass_endomorphism.py`
   gives ~$10^6$ cat-units via direct Φ_q at H_3 generators. Until
   the framework resolves this inconsistency, mass predictions at
   A=1 are inconsistent.

2. **Φ_q pole-distance asymmetry**. Even taking mass_endomorphism
   at face value: $\hat{V}_\text{proton} \approx 0.989$ sits near
   the $q_0$ pole at 1.110 (distance 0.121), so $\Phi_q$ blows up
   close to its singularity — proton mass comes out right (1.84%
   off). $\hat{V}_\text{neutron} \approx 0.854$ is much farther
   from the pole (distance 0.256), so $\Phi_q$ is much smaller —
   neutron mass undershoots by 56%. **This is a genuine framework
   structural issue, not a fitting choice.**

## Verdict

Per owner directive (no calibration beyond the 3 allowed), the
framework's CURRENT BEST non-calibrated predictions are:

| Observable | Best prediction | Residual | Source |
|---|---|---|---|
| $Q_\beta$ | **0.7836 MeV** | **+0.17% / +1.31 keV** | commit `4649650f` |
| $m_p$ | 955.5 MeV (mass_endomorphism) | **+1.84%** | mass-endomorphism.witness.json |
| $m_n$ | ~411 MeV (mass_endomorphism) | **−56%** | np-discrepancy-resolution.md |
| $m_n - m_p$ | not cleanly derivable | (nonsense from raw tower) | — |

To close further, the framework needs to:

1. Resolve the A=1 brane-tower inconsistency (open R&D)
2. Fix the Φ_q pole-distance asymmetry for the neutron (deeper R&D)
3. EITHER allow CAL-3 β-decay calibration (which closes everything to <0.1%) OR derive its substrate-only equivalent (the open `brane-tower-z-habiro.md` level-selection $n_\star$ conjecture)

## Probes summary (this session, all NO-FITTING)

| Probe | Approach | Result |
|---|---|---|
| Single-wrap symbolic Q_β | $|\Delta(\text{net})| \cdot E_0$ derived | **+1.31 keV ✓ current best** |
| LP-dual at H_3 | $y_0^\star \cdot m_e$ | y_0^* dimensionless — doesn't give MeV |
| N=1 brane-tower multiplicative | $\Phi_q^{(1)}$ on Δ_NF volumes | 42-134× WORSE |
| Mittag-Leffler residue (Δ_NF) | residue at roots of unity | +17 keV (13× wrong) |
| Per-nucleon residue diff | residue per β_K then subtract | −113 keV (86× wrong) |
| 3-term assembly (T1+T4+T5+T6) | $m_K$ from full formula | wrong sign on $m_n - m_p$ |
| All-terms non-calibrated | every combination tried | none closes |

Every closure path inside non-calibrated mode hits one of the two
structural issues above. The current best (+1.31 keV) is the
framework's structural bound at single-wrap symbolic level. Further
closure requires deeper R&D.
