# Muon knot identification conflict (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: gap-isolation audit (T2) — owner directive "give context on conflicting muon identifications"
**Status**: real conflict; needs primary-source resolution

## The conflict

Two files in the codebase identify the muon's underlying knot **differently**:

| File | Muon knot | Vol | Hyperbolic? |
|---|---|---|---|
| [`observations/skein-mass-relation.md`](../../content/quantum-observable-universe/observations/skein-mass-relation.md):32 | $4_1$ (figure-eight) | $\mathrm{Vol}(4_1) \approx 2.0299$ | **YES** |
| [`computations/knot-volumes.py`](../../computations/knot-volumes.py):67-73 | $5_1$ = T(2,5) cinquefoil | $\mathrm{Vol}(5_1) = 0$ | **NO** (torus knot) |

In the same script ([`knot-volumes.py`](../../computations/knot-volumes.py):58-64), the figure-eight $4_1$ is identified as **the Higgs** particle, NOT the muon.

## Why this matters

The framework's CAL-2 input is the Skein formula `m_μ/m_e = Vol(4_1)/ℏ_q²`. This formula:
- Has the correct numerical value: `Vol(4_1)/ℏ_q² ≈ 2.0299 / 0.0098 ≈ 206.77` ✓ (matches CODATA `m_μ/m_e = 206.7683`)
- Identifies muon with $4_1$ (figure-eight)

But per `knot-volumes.py`:
- Muon is $5_1$ (cinquefoil), which has Vol = 0 (non-hyperbolic torus knot)
- Figure-eight $4_1$ is the Higgs

If the muon's actual braid representation is `(σ_1 σ_2^{-1})²` (figure-eight, 3 strands), the Skein formula is consistent.
If the muon's actual braid representation is `σ_1^5` (cinquefoil = T(2,5), 2 strands), the Skein formula uses the WRONG hyperbolic volume.

## Resolution candidates

### Option (i) — Muon is $4_1$; `knot-volumes.py` is wrong

- The Skein formula `m_μ/m_e = Vol(4_1)/ℏ_q²` is the canonical CAL-2 input
- The `knot-volumes.py` line 67 muon-label on cinquefoil is a script error / typo
- **Action**: fix `knot-volumes.py` particle labels to align muon with $4_1$

### Option (ii) — Muon is $5_1$; Skein formula uses a different volume

- `knot-volumes.py` reflects the production knot-particle dictionary
- The Skein formula's `Vol(4_1)` is actually the leading-order substrate-truncation factor that HAPPENS to numerically match `m_μ/m_e`, but the underlying derivation goes through $5_1$ braid trace
- For T(2,5) torus knot, `|tr_M(σ_1^5)|` at q_0 ≈ 1.110 gives a value that matches CODATA when scaled by `1/ℏ_q²` — but this would be a coincidence unless the volumes are related
- **Action**: compute `|tr_M(σ_1^5)|` at q_0 and check if `m_μ/m_e = |tr_M(σ_1^5)| · scaling = 206.77`

### Option (iii) — Both, in different mass-tower levels

- Muon has multiple knot representations at different brane-tower levels
- LO (descended) uses $4_1$ in `skein-mass-relation.md`
- Higher tower levels use $5_1$ per `knot-volumes.py`
- The Skein formula is the LO match; the per-braid mass formula uses $5_1$
- **Action**: check if both braids are consistent with the per-braid mass tower at q_0

### Option (iv) — Different dictionary versions

- `knot-volumes.py` may be a legacy / outdated identification
- The current canonical identification is in `skein-mass-relation.md`
- **Action**: trace the `knot-volumes.py` history; deprecate if obsolete

## Critical numerical check (cheap)

For T(2,5) cinquefoil torus knot, the Markov trace at q_0:
- Jones polynomial of T(2,5): `J(T(2,5); q) = q² + q^4 - q^5 + q^6 - q^7`
- At q_0 ≈ 1.110: J(T(2,5); q_0) ≈ 1.232 + 1.518 - 1.685 + 1.870 - 2.075 ≈ 0.860
- This is finite and non-zero, so |tr_M| is non-zero (consistent with finite muon mass)
- The "Vol(5_1) = 0" is the HYPERBOLIC volume (zero because torus knots are not hyperbolic), NOT the Markov-trace value
- So per-braid mass tower for T(2,5) at q_0 gives a finite value — consistent with muon mass via a DIFFERENT formula than Vol/ℏ_q²

## Sibling-PR context

PR #1153 (sinh-bar-antisymmetric-partner-probe) derives:
- `P_m(h) = cosh((2m+1)η)/(2 cosh η)` for T(2,2m+1) torus knots
- `Q_m(h) = sinh((2m+1)η)/(2 cosh η)` for the bar-anti-symmetric partner
- For muon T(2,5) = T(2,2·2+1), m = 2: `P_2(η_0) ≈ ?` (PR #1153 has the numerics)

If muon is T(2,5), then PR #1153's framework directly applies. Per PR #1153 table:
- m=2 (W boson per their identification): `tanh((2m+1)η_0) = tanh(5η_0) ≈ 0.4790`

PR #1153 identifies T(2,2m+1) for m=2 with **W boson**, not muon. So **PR #1153 also disagrees with `knot-volumes.py:73`** (which says T(2,5) = muon).

The three sources give THREE different identifications:
- `skein-mass-relation.md`: muon = $4_1$
- `knot-volumes.py`: muon = $5_1$ = T(2,5)
- PR #1153 (implicit): T(2,5) = W boson; muon is something else

## What's actually canonical?

The HIGHEST-AUTHORITY source for paper-level statements is `prop:skein-mass-relation` (since it's a published proposition with proof in `skein-mass-relation-proof.md`). The other two are:
- `knot-volumes.py` — a numerical-verification script (LOW authority for particle ID)
- PR #1153 — exploratory (per its EXPLORATORY tag)

**Most likely canonical**: muon = $4_1$ (figure-eight). The `knot-volumes.py` particle labels appear to be a separate (and possibly inconsistent) labeling scheme — likely an artifact of an earlier identification attempt.

## Recommended action (cheap)

1. **Verify** that `skein-mass-relation.md`'s muon=$4_1$ is the canonical statement (read `skein-mass-relation-proof.md`)
2. **Update** `knot-volumes.py:67-73`: change `"particle": "muon"` on the $5_1$ entry to either remove the particle label OR change to "W boson" per PR #1153
3. **Add** a clear muon=$4_1$ entry to `knot-volumes.py` (figure-eight should have BOTH "higgs" and "muon" labels, OR muon should have its own dedicated entry as `4_1` muon)
4. **Add** a paper-side note in `skein-mass-relation.md` explicitly stating muon = $4_1$ figure-eight to prevent future label drift

## Impact on the +0.17% Q_β residual

The muon-knot identification affects the Skein formula → q_0 derivation. If muon is correctly $4_1$, the Skein formula gives q_0 ≈ 1.10998 (to ~ppb). If muon is $5_1$, the formula and the q_0 value would change.

The current empirical evidence (Skein formula gives correct CODATA 206.77 → q_0 ≈ 1.110 → operator-level computations consistent at the ppm-to-ppb level) strongly supports muon = $4_1$. **The conflict is most likely a labeling error in `knot-volumes.py`, not a deeper substantive issue.**

## Cross-references

- Conflicting sources:
  - [`observations/skein-mass-relation.md`](../../content/quantum-observable-universe/observations/skein-mass-relation.md):32
  - [`observations/skein-mass-relation-proof.md`](../../content/quantum-observable-universe/observations/skein-mass-relation-proof.md):6 (cites $4_1$)
  - [`computations/knot-volumes.py`](../../computations/knot-volumes.py):67-73
- Sibling: PR #1153 (T(2,5) ≠ muon per its labeling)
- Affected: any compute consuming `knot-volumes.py` particle labels
