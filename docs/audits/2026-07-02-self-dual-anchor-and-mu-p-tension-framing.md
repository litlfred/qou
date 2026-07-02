# Audit: the CS=0 self-dual framing and the μ–p substrate tension (bean `tnjb`)

**Date:** 2026-07-02
**Branch:** `claude/formula-for-q-bzym14`
**Scope:** what the complex-volume / self-duality keystone
([`prop:self-dual-higgs-real-volume`](../../content/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-volume.md),
merged in PR #3196) does — and does **not** — contribute to the μ–p
substrate tension that sits behind bean `tnjb`.

## TL;DR

- **Bean `tnjb` itself is completed** — the data-integrity bug (a dashboard
  reading the muon-q₀ `m_mu_pred_MeV` and scoring the CAL-2 tautology as a
  100×-MET *prediction*) was fixed by PR #2897 + the 2026-06-28 canonical
  regen. This note is about the **live substance** behind it: the μ–p
  substrate tension (11.5 ppb in q₀ ≈ 240 ppb in m_p), documented in
  [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md).
- **The new framing contributes (A) a principled canonical-anchor
  justification** — the muon pin is the unique **CS = 0 / self-dual /
  imaginary-free** q₀ determination — which is a *structural* reason to keep
  the ~840 `computations/` witnesses muon-anchored (exactly what `tnjb`
  guards).
- **It does NOT quantitatively explain the 240 ppb floor.** The tempting
  "modulus `|tr_M|` discards an imaginary face ⇒ 11.5 ppb leakage" mechanism
  fails a rough check and is recorded here as a **scope-limited negative**
  (per the refuted-claim discipline) so no future agent re-chases it.
- **Closing the floor is Subgoal-2** (substrate derivation of q₀), out of
  scope without owner reversal.

## (A) The structural anchor justification — the robust, in-scope win

The tension is between two q₀ pins of the *same* H¹(Bring) datum:

| Pin | formula | q₀ | object's bar/complex structure |
|---|---|---|---|
| **muon** (canonical CAL-2 proxy) | `m_μ/m_e = Vol(4₁)/ℏ_q²` | 1.10997859555… | **CS(4₁)=0**: `4₁` amphichiral ⇒ `𝕍(4₁)=Vol(4₁)+i·0` is **purely real** |
| **proton** (experimental precision pin) | `m_p/m_e = 2·Vol(4₁)/ℏ_q²·F_Bor(q) − 12` | 1.10997858275… | many-body: `F_Bor = abs(tr_M(β_Bor))`, the **modulus** of a binding endomorphism whose bar-odd (Q_β) face is projected out |

The keystone `prop:self-dual-higgs-real-volume` (`J_N(4₁;q)=J_N(4₁;q⁻¹)`,
Lean-proved sorry-free as `QOU.Knot.SelfDuality.higgs_complex_volume_real`)
makes the muon pin's cleanliness **structural, not incidental**: the muon
scale is set by a *single amphichiral knot with zero Chern–Simons phase*, so
it carries no imaginary/decay content at all. The proton scale is set by a
*many-body* trace whose imaginary (Q_β / 𝔇_β) face is real physics, folded
through a modulus.

This upgrades the anchor convention ([AGENTS.md](../../AGENTS.md) §"$q_0$ anchor convention";
[`epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md))
from *"muon-anchor is the canonical convention"* to *"the muon is the
structurally-cleanest, decay-free q₀ determination."* It is the same
Frobenius/Hopf self-duality already recorded at the **Wedderburn-partition**
level in
[`bound-state-frobenius-self-dual-channel`](../../content/quantum-observable-universe/mass-theory/bound-state-frobenius-self-dual-channel.md)
(transpose partitions `(3,1)ᵀ=(2,1,1)`), now stated at the **knot /
complex-volume** level (`CS=0`). It is also the structural *why* behind the
owner's 2026-06-26 decay-width ruling
([`2026-06-28-calibration-canon-decay-width-ruling.md`](2026-06-28-calibration-canon-decay-width-ruling.md)):
CAL-2 = 𝔇_β pinned via `m_μ/m_e` because that anchor is the bar-even /
imaginary-free face of the substrate.

## (B) Scope-limited negative — the "modulus leakage" mechanism does NOT source the floor

**Claim tested (and refuted, scope-limited):** *the 11.5 ppb q₀ tension is the
second-order cost of projecting the proton's complex binding defect onto its
real axis via `|tr_M|`, measured against the CS=0 muon reference —
`|z| ≈ Re(z)·(1 + ½(Im/Re)²)`.*

**Why it fails:** at the **observable / archimedean** level `Im(q₀)=0`
(verified: `lusztig_q_0_imaginary_part_zero`), so `tr_M(β_Bor)` at real q₀ is
**real** and `|tr_M|` merely fixes a sign — it discards nothing. The bar-odd
face is not a ppb-scale rounding of the bar-even face; it is **O(1)**. From
the `/dashboard-low` Entanglement table at q₀:

| nucleon | retained `E₀·bar-even` (MeV) | emitted `E₀·abs(bar-odd)` (MeV) | `abs(bar-odd)/bar-even` |
|---|---|---|---|
| p | 2.373 | 2.087 | **0.88** |
| n | 2.327 | 1.538 | 0.66 |

A ratio of 0.66–0.88 would source an **O(1)** effect, not 240 ppb — and that
bar-odd part *is* Q_β, a real, fully-accounted energy (the emitted γγ̄
channel), **not** a hidden projection error. So the observable-level
modulus-projection mechanism, **alone**, does not produce the μ–p floor.

**Scope (per the "refuted/ruled-out" discipline):** this is a **scope-limited negative** (case (a) of the
refuted/ruled-out rubric) — the observable-level mechanism does not, by itself,
explain the floor. It is **not** a structural exclusion: a **fibre-level**
version (the c_k Taylor coefficients live in the formal-q fibre, where Im(q)
is unconstrained — [AGENTS.md](../../AGENTS.md) §"$\mathrm{Im}(q)$ at fibre vs observable level") is *not*
tested here and is not ruled out. But the fibre-level route is precisely
substrate-derivation of q₀ = **Subgoal-2**, out of scope without owner
reversal.

## Consequence for `tnjb` / production discipline

1. **Keep `computations/` muon-anchored.** (A) gives the affirmative
   structural reason, not just convention. No migration of the ~840 witnesses
   (still owner-gated).
2. **The 240 ppb floor is not fittable.** (B) reaffirms
   [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md):
   the tension is not a modulus rounding error one can absorb with an integer
   `u`-tower; the only in-discipline path below the floor is the
   operator-valued **complex** binding combiner (Subgoal-1), i.e. carrying the
   full `𝕍 = 𝔈_bind + i·Q_β` binding defect, not its real projection.
3. **No new fit introduced.** This note adds framing + one refuted mechanism;
   it changes no production compute and re-runs no dashboards (unchanged from
   baseline).
