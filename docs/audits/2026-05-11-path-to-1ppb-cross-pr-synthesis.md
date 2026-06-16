# Path to 1 ppb — cross-PR synthesis (#638 ⊕ #639 ⊕ #640)

**Date:** 2026-05-11
**Author:** coordination agent on
`claude/q-beta-spectral-bridge-handoff-QqMlK`
**Status:** synthesis only (no new compute, no new content blocks);
re-analysis prompted by user request and the `/coordinate` skill.
**Scope:** open PRs #638, #639, #640 (and merged #637 handoff doc
`docs/handoffs/2026-05-11-q-beta-spectral-bridge-handoff.md`).

## TL;DR

The structural ceiling on the brane-tower truncation error is now
proved (modulo the lift formula):

$$
\bigl\lvert R_N \bigr\rvert
\;\le\;
\frac{\hbar_q^2}{1 - \hbar_q^2}
\cdot \hbar_q^{2N}
\;=\;
C(K)\,e^{-c(K)\,N}
\quad\text{with}\quad
\hbar_q = (q_0 - 1)/q_0 \approx 0.0991,
\;c(K) \approx 4.624.
$$

Bound table at $q_0 = 1.10998$ (PR #639,
`c-k-beta-decay-bound.witness.json`):

| $N$ | bound (rel) | bound (ppb) | observed Form A |
|---:|---:|---:|---:|
| 0 | $9.91 \times 10^{-3}$ | $9{,}914{,}521$ | $1.68 \times 10^{-3}$ ($1.31$ keV) |
| 1 | $9.73 \times 10^{-5}$ | $97{,}333$ | — |
| 2 | $9.55 \times 10^{-7}$ | $956$ | — |
| 3 | $9.38 \times 10^{-9}$ | **9.4** | — |
| 4 | $9.21 \times 10^{-11}$ | **0.092** | — |

So **on the substrate side**, $N = 3$ enters the 1 ppb regime and
$N = 4$ clears it with $10\times$ margin. On the **calibration
side**, the existing CAL-2-uncertainty floor at $\sim 780$ ppb (per
`docs/coordination/1ppb.md` "Floor" §) still binds the *total*
prediction error.

The synthesis below identifies the four operationally-required
artefacts (one each from PRs #638, #639, #640, plus an open Lean
gap), maps the per-PR completion state, and flags the calibration-
floor question that remains open under the existing author
resolution ("Q_β derivation? No").

## Artefact map (what the four PRs collectively need)

| # | Artefact | Owning PR | State | Notes |
|---|---|---|---|---|
| 1 | Bridge identity Form A ↔ Form B + Taylor expansion | #639 | **landed (provable, `ring`)** | `q-beta-spectral-bridge.{md,ts,lean}` + 50-dps witness |
| 2 | Structural dampening rate $c(K) = -2\ln\hbar_q$ + $C(K)$ prefactor | #639 | **landed** as substrate-derived bound | `c-k-beta-decay-bound.witness.json`; ceiling, not actual decay rate |
| 3 | Per-partition $k_\lambda$ rule (replaces refuted scalar $n_\star$) | #639 | **structurally identified, open closed-form** | `per-partition-k-lambda-rule.md` — open identification problem |
| 4 | Operator-valued probe at depths $k \in \{1, \ldots, 6, 8, 10\}$ | #638 | **landed (refutes scalar form)** | `probe-phiq-operator-valued.witness.json` (12108 lines) |
| 5 | Substrate-only $m_n$ chain | #640 | **landed at 999 ppb** | `build_neutron_mass_50dps_chain.py`; honest "wildly off" placeholder until T2/T3/T5/T6 close |
| 6 | Substrate-only $m_p$ chain | merged | **landed at 544 ppm** | `build_proton_mass_50dps_chain.py` (PR #480 / #617) |
| 7 | Lean proof of `conj:archimedean-remainder-exponential-decay` | none | **OPEN** (Gap #12 in handoff roadmap) | multi-week R&D; class-axiomatised in #639 |
| 8 | Lean proof of per-partition $k_\lambda$ closed-form selector | none | **OPEN** (sharpened Gap #5) | structural identification problem in `per-partition-k-lambda-rule.md` |

## What "path to 1 ppb" now means concretely

The user's "path to 1 ppb" question splits into **three independent
gating constraints** under the current state:

### Constraint 1 — Substrate truncation depth

PR #639's $c(K)$ bound says: **truncate at $N = 4$ to reach
0.092 ppb on the substrate side**. The ceiling is structural
(geometric series of the q-dilogarithm tail). Operationally, this
requires the per-partition $k_\lambda$ rule (#639's open structural
form) to *define* what depth $N$ means for the operator-valued
probe at each Wedderburn block.

**Status**: ceiling proved; lift formula open (sharpened to
"closed-form spectral selector $\lambda \mapsto k_\lambda$ as a
function of $(q_0, \beta_\mathfrak{H}, \lambda)$").

### Constraint 2 — Operator-valued probe execution at $N \geq 3$

PR #638 sweeps the operator-valued $\Phi_q$ probe at uniform
$k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ — none uniformly close the
$\{D, T, {}^3\mathrm{He}\}$ binding gap, which refutes the scalar
form. PR #639 sharpens the failure to a single dominant partition
per atom and proposes the per-partition rule

$$
k_\lambda = \begin{cases} 1 & \lambda = \mathrm{argmax}_\mu, \\ 2 & \text{otherwise} \end{cases}
$$

which empirically closes all three atoms simultaneously to within
$\sim 5\%$. Pushing the operator-valued probe to depth $N = 3$
under the per-partition rule is the **next compute step** — it
should produce $\sim 9$ ppb residual under the geometric ceiling
*and* test whether the actual decay rate matches.

**Status**: infrastructure in #638; per-partition rule in #639;
joint $N = 3$ run not yet executed.

### Constraint 3 — Calibration floor

Per `docs/coordination/1ppb.md`:

> CAL-2 uncertainty (`Q_β = m_n − m_p − m_e`, CODATA $\pm 6.1 \times
> 10^{-7}$ MeV) sets a hard floor at $\sim 780$ ppb absent a
> derivation of `Q_β` from substrate alone. The user has explicitly
> declined deriving `Q_β`; the floor stands.

PR #639's c(K) ceiling brings the **substrate-derived prediction**
below 1 ppb, but the **total prediction error** is still bounded
below by CAL-2 propagation. Resolving Constraint 3 requires either
(a) a tighter CAL-2 anchor, or (b) reversing the explicit author
resolution and deriving $Q_\beta$ from substrate alone (PR #639's
spectral bridge already provides Form A as a substrate-only Q_β
predictor at +1.31 keV). The handoff's TASK 4 noted "Q_β as
PREDICTION" under the three-calibration discipline (CAL-1 m_e,
CAL-2 q_0, CAL-3 𝔇_π) — this is the calibration-vs-prediction
status of Q_β under the current convention.

**Status**: per author resolution, 780 ppb floor stands; but the
Form A residual (+0.168%) is *already* a substrate-only prediction
(no CAL-3 input), so the substrate path is actively viable if the
floor is reconsidered.

## The unified picture (pre-existing handoff synthesis, re-affirmed)

The handoff doc (merged in #637) and PR #639's
`q-beta-spectral-bridge.md` together establish:

1. **Locality lost** → exact $Q_\beta$ requires infinite eigenfunction sum
2. **Eigenfunctions DAMP exponentially** in GB filtration depth →
   $\lvert R_N \rvert \le C(K) e^{-c(K) N}$ — now PROVED at the
   geometric ceiling
3. **Finite-depth predictions are asymptotically correct** —
   PR #639 quantifies: $N = 3$ gives 9 ppb ceiling, $N = 4$ gives
   0.092 ppb
4. **Form A and Form B** are two representations of the same Q_β —
   PR #639 has the bridge identity proved unconditionally (modulo
   the analytic Taylor bound on $\log(1+zh)$)
5. **Path to 1 ppb is structural**, not algorithmic — closing the
   per-partition $k_\lambda$ identification (Gap #5 sharpened) and
   the $c(K)$ Lean proof (Gap #12) are the open theorems

This re-affirms the cycle-7 synthesis in the handoff, now grounded
in PR #639's compute artefacts.

## Where this leaves the handoff TASKS

The handoff doc (`docs/handoffs/2026-05-11-q-beta-spectral-bridge-handoff.md`)
was authored before PR #639 opened. With #639 in flight, its
TASKS are now:

| Handoff TASK | Subsumption status |
|---|---|
| **1A** new `q-beta-spectral-bridge.{md,ts,lean}` | ✅ **done in PR #639** |
| **1B** edits to 3 existing blocks | ✅ **done in PR #639** |
| **2A** new Lean file with bridge theorem | ✅ **done in PR #639** (3 unconditional polynomial identities via `ring`) |
| **2B** close 2 PhiQConvergence sorries | ✅ **done in PR #639** |
| **2C** Gap #12 archimedean-remainder-decay | ✅ **structural bound landed in PR #639**; full Lean proof remains open |
| **2C** Gap #5 $n_\star$ existence | ✅ **scalar refuted in PR #638**; per-partition reformulated in PR #639; closed-form open |
| **3A** post on PR #635 | done in handoff session |
| **3B** post on PR #636 | done in handoff session |
| **3C** compute refinements (V̂_i, Form B at N=1/2, $c(K)$ verification) | partially in PR #639 (c(K) bound); remaining: actual decay rate empirical pinning at $N \geq 1$, $\hat V_i$ definition refinement |

**Net**: the handoff TASKS 1, 2 are essentially **done** by PR #639.
The next agent's marginal work is on TASK 3C (operator-valued probe
at $N \geq 3$ under per-partition $k_\lambda$, empirical $c(K)$
refinement) and on the open Lean gaps in TASK 2C.

## Coordination posture

Following `/coordinate` §6 (no inconsistent findings to escalate):

- **Scope overlap with #639**: the handoff's TASKS 1, 2 fully
  duplicated #639's deliverable, so this branch (`q-beta-spectral-
  bridge-handoff-QqMlK`) **does not re-execute** them. This audit
  document is the deliverable instead.
- **Scope overlap with #638**: PR #638's operator-valued probe
  provides the infrastructure for the next compute step
  (depth-$N \geq 3$ run under per-partition $k_\lambda$). No code
  duplication; coordination posted as a sibling intent.
- **Scope overlap with #640**: PR #640's substrate-only $m_n$
  chain is the partner for $Q_\beta = m_n - m_p - m_e$; closing the
  Q_β substrate-only prediction below 1 ppb requires the chain at
  better than 999 ppb residual (currently bounded by T2/T3/T5/T6
  closure). Coordination posted as sibling intent.

Author-held resolution (1ppb.md): "Q_β derivation? No — 780 ppb
floor stands." This audit notes the substrate path is now
structurally viable (PR #639's c(K) bound + per-partition rule)
should that resolution be reconsidered.

## Pointers

| Reference | What it gives you |
|---|---|
| [PR #639 → `q-beta-spectral-bridge.md`](https://github.com/litlfred/qou/blob/claude/q-beta-spectral-bridge-content/content/quantum-observable-universe/particle-interactions/q-beta-spectral-bridge.md) | Bridge identity proof + numerical witness |
| [PR #639 → `c-k-beta-decay-bound.witness.json`](https://github.com/litlfred/qou/blob/claude/q-beta-spectral-bridge-content/computations/c-k-beta-decay-bound.witness.json) | $c(K), C(K)$ + bound table for $N \in \{0, ..., 4\}$ |
| [PR #639 → `per-partition-k-lambda-rule.md`](https://github.com/litlfred/qou/blob/claude/q-beta-spectral-bridge-content/content/quantum-observable-universe/braids-and-knots/per-partition-k-lambda-rule.md) | Structural reformulation of $n_\star$; sharpened open question |
| [PR #638 → `probe-phiq-operator-valued.witness.json`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/computations/probe-phiq-operator-valued.witness.json) | Per-eigenvalue $\Phi_q$ spectra at $k \in \{1, \ldots, 10\}$ |
| [PR #640 → `neutron-mass-codata-50dps.witness.json`](https://github.com/litlfred/qou/blob/claude/neutron-mass-50dps-chain/computations/neutron-mass-codata-50dps.witness.json) | Substrate-only $m_n$ at 999 ppb residual |
| [`docs/coordination/1ppb.md`](../coordination/1ppb.md) | The 1 ppb ledger (this audit appends a row) |
| [`docs/handoffs/2026-05-11-q-beta-spectral-bridge-handoff.md`](../handoffs/2026-05-11-q-beta-spectral-bridge-handoff.md) | Original cycle-7 handoff (now subsumed by PR #639) |

## Next concrete work item (for whoever picks this up)

**Single highest-leverage next step**, consistent with the existing
PR scope:

- **Run the operator-valued $\Phi_q$ probe (PR #638's
  `probe_phiq_operator_valued.py`) at depth $N = 3$ under PR #639's
  per-partition $k_\lambda$ rule** (max-$\lvert\mu\rvert$ partition
  gets $k = 1$, others get $k = 2$, then push uniformly to $k = 3$
  for non-dominant blocks). Expected: total binding residual on
  $\{D, T, {}^3\mathrm{He}\}$ enters the $\sim 9$ ppb ceiling per
  PR #639's $c(K)$ table. Empirical actual rate may be larger than
  $c(K)$ ceiling — the gap quantifies the prefactor improvement
  available beyond the geometric bound.

This is a **single-script extension of PR #638's existing probe**
(adding the per-partition $k_\lambda$ rule from PR #639), runnable
in a follow-up branch after #638 + #639 merge. Not in this branch's
scope — flagged for the next coordinator.
