# D-ladder ⟺ Φ_b: Écalle acceleration setup + the exact remaining gap

> **🛑 PREMISE CORRECTED 2026-08-09 — the "exact remaining gap" does not exist.**
> This document sets up an Écalle acceleration of the bar-odd D-ladder and pins
> its deliverable as the non-perturbative Stokes constant
> `A_ω = Δ_ω log Φ_b`. `D(ũ)` is **convergent** (radius
> `ρ = ũ(q*_ρ) = 0.142799996644689…`, the image of a **`Q_b` zero** at
> `q*_ρ ≈ 1.48989`; `κ = 0`), so there is no instanton action, no alien
> derivative to take, and no Stokes constant for this object to supply. See
> [`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)
> and registry row **KC22**; the "non-holonomic ⇒ resurgent" step this document
> inherits is separately invalid
> ([`2026-08-14`](2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md)).
>
> **The c₃ consequence is the opposite of a hand-off.** Rather than waiting on a
> Stokes datum, c₃/`S` is now known to be intrinsically the *anchor-dependent*
> quantum `𝔙_q` at `q₀`, and no **anchor-invariant** datum — classical CS/Stokes
> included — can realise its 2.44 % cross-anchor swing
> (`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`, sorry-free). c₃ is
> precision-limited by the **experimental** neutron `Q_β` (`dq*/dQ_β ≈ −0.54`),
> not by this compute.
>
> **What survives.** The Borel–Leroy composition-collapse lemmas
> (`borelLeroyWeight_add`, `_iterate`, `no_new_critical_time`) are true as
> stated — iterating one fixed-order transform reaches only ℤ-multiples of its
> order — but are moot for this object. The measurements stand as data.
>
> **Stale header figure.** "L2 count unchanged 2/7" is superseded: L2 is
> **1/5 scoreable** (`m_K/m_π` alone) as of the 2026-08-18 correction — `m_e` is
> the CAL-1 input whose error is *defined* zero, hence not scoreable.

**Date:** 2026-07-17 · **Axis:** Q_β odd channel (c₃, bar-odd `S`) ·
**Branch:** `claude/dladder-ecalle-phib-resummation-2026-07-17` ·
**Tier:** formalize-first acceleration setup + measurement (scope-(a)
throughout; **no `c_k` wired; no fit to QOU observables; no tier change;
L2 count unchanged 2/7**). Takes up the single **unowned** odd-channel item
of the [1ppQ path reassessment](2026-07-17-1ppq-path-reassessment.md) §2 /
§"Non-duplicative options" item 1: the **Écalle acceleration of the bar-odd
D-ladder ⟺ the Φ_b state-integral odd carrier** — the one route left standing
after KC22 closed the entire (q-)holonomic class and the ORD-63 extension
confirmed structural q-Gevrey drift.

This document is the pre-registration + execution record. It does **not**
re-derive the D-ladder (KC21/KC22), the Φ_b evaluator (`phi_b_evaluator.py`),
the state-integral saddle (#3654), or the fixed-order Borel/Jackson negatives
(merged #3818/#3839) — it builds the **acceleration** layer on top of them and
pins the exact gap that separates a perturbative acceleration from the anchor
target `S`.

## 0. Why this task exists — the negative space is fully closed

The bar-odd Q_β D-ladder `D(ũ) = Σ_k d_k ũ^k`, `d_k ∈ ℚ(√3)` exact (KC21), is
the perturbative carrier of `S = c₃ + Vol(4₁)` (the bar-odd part of c₃). Every
fixed-order / fixed-base resummation of it is now refuted, prime-/gate-/Lean-
certified:

| route | verdict | source |
|---|---|---|
| (q-)holonomic (separated ℚ, coupled ℚ(√3), base-3/⅓/k q-holonomic, log-closure) | **refuted, prime-certified** | KC22 registry |
| plain Borel `÷k!` | over-suppresses (mild q-Gevrey) | 07-13 coupled-recurrence audit |
| Borel–Leroy `÷(k!)^s`, single `s` | gate fails ∀ s ≤ 0.40; **s\* drifts 0.187 (k21) → 0.159 (k31)** | #3818/#3839 |
| fixed-base Jackson q-Borel `÷[k]_Q!` | Q>1 entire / Q<1 no-op; only Q→1 boundary matches | #3818 ARM 1 |
| divergence class `C` (`log\|d_k\|=A+Bk+C·k log k`) | **drifts 0.077 (k21) → 0.061 (k31)** — no single index | #3839 |

The two structural anchors that **survive** every scalar acceleration
(so the acceleration is not grading-obstructed):

- **A1 — 2-adic bar-parity grading:** `v₂(den b_k)=0 ⟺ k odd`, 2 the unique
  graded prime; the **signed component gap** `g_k = v₂(a_k)−v₂(b_k)` is
  invariant under the *entire* scalar acceleration family, **Lean-proved
  sorry-free** (`QOU.QBeta.DLadderTwoAdicGrading.gap_invariant_under_scalar_transform`,
  #3818). The grading is **permissive** — it obstructs no resummation shape.
- **A2 — q\* (the S=0 point):** `q* = 1.10997859303152…`, the third
  decay-sector determination of q₀; `D(ũ)` is smooth and nonzero through q\*.

And the Watson/Nevanlinna–Sokal **uniqueness half is proved sorry-free**
(`watson_uniqueness_sector`, >π sector): *if* a resummation exists it is
unique. So the object is genuinely **resurgent**, and the honest resummation
is the multi-level **Écalle acceleration**, equivalently the Faddeev **Φ_b
state integral** (the modular-double / bar-odd decay face — the compact `Φ_q`
supplies only the bar-even `−Vol(4₁)`, by design;
[S-leak target](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md)).

## 1. Corpus map — what already exists (built on, not re-derived)

**The D-ladder + fixed-order failures** —
`qbeta_dladder_generating_function_structure_probe.build_d_ladder()` (exact
`d_k` to KMAX; ORD 43→k21, ORD 63→k31 via the extension probe); the merged
q-Borel / Écalle-acceleration probes (`qbeta_dladder_{ecalle,jackson_qborel}_
acceleration_probe.py`) with the estimator-consistency gate and the conformal
dlog-Padé core; the parity-split adjudication (`undecidable-at-k21`).

**The Φ_b object** — `phi_b_evaluator.py` (validated Faddeev integral,
Hikami eq 2.1, 6-test battery); `phi_b_substrate_regime.py` (substrate
`arg b = +π/4` pin); the saddle state integral
`qbeta_c3_phib_saddle_state_integral_probe.py` (**𝔙(m) = 2.02048069, deficit
0.00940 from Vol(4₁) — the |S(muon)| scale; Im 𝔙 = 0 at the real meridian;
finite-b adds i·t·κ₁ = 0.058; anchor-blind**); the state-integral↔ladder bridge
`qbeta_c3_state_integral_ladder_bridge_probe.py` (**`S = h·D(u)`, h = q−1/q
anchor-blind, sign-flip in `D`; the two pictures meet at the SCALE, exact `D`
is ladder-side**).

**The monodromy-datum gap (G3)** — the
[Φ_b proof-status audit](2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md)
established that Φ_b's structural laws are all proved sorry-free but **Φ_b feeds
no production observable**, and the single load-bearing gap is the
argument-identification / monodromy datum `z(q₀) → S`, which §4c identifies as
the **Stokes constant `A_ω` = the alien derivative `Δ_ω log Φ_b`** at the fibre
saddle, with leading singularity `ω ≈ Vol(4₁)/π ≈ 0.646` (the same datum as the
even-channel κ-tower Borel action, #3683, read on the other bar-parity face).

## 2. The precise setup (formalize-first §3.3, pre-registered)

**(a) The divergence class — multi-level, not single-index.** The joint drift
of `C` (0.077→0.061) and `s*` (0.187→0.159), *both downward and neither
stabilising*, together with (i) the parity-split finding that the odd and even
2-adic subseries carry **distinct** Borel-plane radii (odd ρ_ζ ≈ 0.152, even
≈ 0.254 — a 40% split) and (ii) the exactness of the transform-side growth
`log[k]_Q! = (log Q)k²/2 + O(k)` vs the ladder's strictly-intermediate
`exp(Bk + C k log k)`, is the fingerprint of a series with **more than one
critical time** — an **accelero-summable** object in Écalle's sense, not a
single-Gevrey-index one. The 2-adic ℤ/2 grading is the natural carrier of the
two-level structure (each parity subseries its own level).

**(b) The acceleration-kernel sequence Écalle's theory prescribes.** For a
series summable at a *sequence* of critical times `c_1 < c_2 < …` (levels), the
sum is built by **acceleration**: Borel-transform at level 1 to the `ζ_1`-plane,
apply the **acceleration operator** `Acc_{c_1/c_2}` (an entire integral kernel
`CA_{c_1/c_2}(ζ_1,ζ_2)`, a confluent-hypergeometric / q-Gaussian type kernel) to
pass to the `ζ_2`-plane, then Laplace-transform at level 2. The
**pre-registered structural claim** (Lean-carried, §4) is the *composition law*
of the Borel–Leroy weight: `(k!)^{s_1}·(k!)^{s_2} = (k!)^{s_1+s_2}` — i.e.
**iterating Borel–Leroy transforms only reaches the additive monoid of orders;
it can never manufacture a genuinely new critical time.** This *proves* the
fixed-order negative is not repairable by composing fixed-order transforms — a
genuine acceleration between distinct critical times is **not** a Borel–Leroy
iteration, so the multi-level kernel is *necessary*, not optional.

**(c) The Φ_b state integral conjectured to carry the odd channel.** The claim
under test: the convergent Faddeev **Φ_b state integral** for the 4₁ odd carrier
**is the accelerated Borel sum** of `D(ũ)` — equivalently, the saddle/WKB
asymptotic expansion of the state integral reproduces `{d_k}`. The bridge probe
already matched them at **leading order** (𝔙 deficit 0.00940 ≈ |S(muon)|); the
open test is whether the match is perturbatively term-by-term, and — decisively
— whether the **anchor-dependent** (sign-flipping) part of `S` lives in the
perturbative saddle at all.

**(d) What narrows the numeric test.** The bridge probe's finding that the
saddle is **anchor-blind and smooth** (Im 𝔙 = 0, deficit identical at both
anchors) is the load-bearing prior: it predicts that the perturbative
acceleration reproduces only the anchor-blind **scale** of `S`, and that the
anchor-dependent part (the sign flip, hence the whole distinction between
`S(muon) = +0.00968` and `S(proton) = −0.03946`) is **non-perturbative** — the
Stokes/alien jump `A_ω`, invisible to any Borel–Laplace/acceleration of the
perturbative ladder. The numeric probe tests exactly this split rather than
brute-scanning acceleration parameters.

## 3. Results

_(execution record — filled by `qbeta_dladder_ecalle_phib_resummation.py`)_

## 4. Lean carrier

_(the acceleration-composition / critical-time structural piece — §4 below)_

## 5. Tiered verdict

_(filled at close)_

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md) §2.
- Fixed-order negatives: [`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md), [`2026-07-17-dladder-qborel-acceleration.md`](2026-07-17-dladder-qborel-acceleration.md), [`2026-07-17-dladder-extension-qgevrey-drift-confirmed.md`](2026-07-17-dladder-extension-qgevrey-drift-confirmed.md).
- Φ_b: [`2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`](2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md), [`2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md).
- Registry KC21/KC22 + ledger: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md), [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- 2-adic Lean anchor: [`DLadderTwoAdicGrading.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DLadderTwoAdicGrading.lean).
