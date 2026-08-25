---
# pxhb
title: "Follow-up session: work the open-conjecture frontier surfaced by the 2026-07-02 closure sweep — 5nx8 (\U0001D519 fibre-descent: binding kernel characterized-not-closed, single-\U0001D519 assembly open) + 1jrh (AW 3-term recurrence, gated on c3^even) + the s013 q-Bessel self-conjugate target; per docs/audits/2026-07-02-internal-conjecture-closure-sweep.md these are advance-paths, not mechanical closures"
status: in-progress
type: task
priority: normal
created_at: 2026-07-02T17:04:06Z
updated_at: 2026-08-19T14:22:31Z
---

## Triage 2026-08-07 — all three named children are CLOSED; residual is 2 items

| child | bean status | outcome |
|---|---|---|
| `5nx8` 𝔙 fibre-descent | **completed** | ζ₄-partner relation proved sorry-free (`QOU/Mass/ComplexVolumeZeta4Partner`); descent *advanced, not closed* |
| `1jrh` AW 3-term recurrence | **completed** | formalize-first prune — test GATED on c₃^even, no scan run |
| `s013` q-Bessel / LR S-matrix keystone | **completed** | merged PR #3190 |

So this parent's queue is drained as *stated*. What survives is not a
mechanical closure but two research items, per
`docs/audits/2026-06-28-frakV-descent-zeta4-partner.md`:33-34:

1. **`Im 𝔙` Q_β fibre kernel — GATED.** Needs the `c_k` Habiro element /
   SW-residue jet-prolongation symbol `R(q,ξ)`
   (`conj:qdifference-kernel-prolongation-symbol`). Fitting `Φ₂` is the
   forbidden "seventh ansatz" (2026-06-09 scope). The gate is the *anti-fit*
   discipline, not a scope gate — a derived kernel is in scope, a fitted one
   never was.
2. **single fibre `𝔙` (the descent) — OPEN.** Proved so far: ζ₄ generator
   coupling, ζ₄-partner relation, bar-parity class. Missing: **both** fibre
   kernels *and* their assembly into one `tr_M` trace object.

Calibration for whoever picks this up: the 2026-07-02 closure sweep's headline
is *"the closeable set remains ≈ empty"* and it classes these as **advance-paths,
not mechanical closures**. Neither item is a session-tail task, and neither
should be "closed" by supplying a fitted kernel. Left `in-progress`; the honest
re-scope is to either retitle this parent to the two residual items or close it
and open a bean per item.

## CORRECTION 2026-08-08 — the triage above was STALE; corpus-grep caught it

The 2026-08-07 triage called the single-`𝔙` descent assembly **OPEN**, citing
`2026-06-28-frakV-descent-zeta4-partner.md`. Two audits postdate that and change
the verdict. This is a worked instance of the AGENTS.md corpus-grep checklist
doing its job: the cited source file's status note lagged the corpus by a month.

| item | 2026-06-28 (what the triage read) | actual current state |
|---|---|---|
| fibre descent itself | "characterized-not-closed" | **CONFIRMED exactly** — `2026-07-04-eta-square-fibre-descent-confirmed.md`: `η := arcsinh(O)` is bar-odd at **all orders ≤ 17**, and `η² ∈ ℚ(√3)[[ũ]]` with **margin 9** (8 rungs solved, 9 held-out orders vanish identically). Exact ℚ(√3), ORD-17. Not a numerical-coincidence class. |
| single-`𝔙` assembly | "OPEN" | **REFUTED exactly, scope-(a)** — `2026-07-17-eta-square-functional-g-refutation.md`: `E = G(η²)` dies at rung `ũ¹` (η² starts at `ũ³` while `E₁ = 3√3/4 ≠ 0`); even granting an arbitrary 2-rung carrier it dies at rung 4, with rungs 4,5,7,8 carrying nonzero exact obstructions. `g₁,g₂` are *forced* by rungs 3 and 6, so these are **parameter-free obstructions, not a fit rejection** (margin 4). |
| §3b formalization of the descent | queued | **moot in the strong form** — there is no functional descent to formalize. `ComplexVolumeZeta4Partner` + the 07-04 membership witness are the honest record. |

**Scope discipline.** The 07-17 result is correctly labelled scope-(a): what is
refuted is *that construction as-is* — `E` as a power series in `η²` alone
(which kills both named candidate profiles, q-Bessel-type and ζ₄-rotation
cosh-type, since both are functions of `η²` alone). What is **not** refuted is
the η²-descent, which stands exactly. The structural reading: the fibre needs
**at least two independent bar-even generators** (`ũ` itself *and* `η²`), and
their relation is not a finite-window power-series identity.

**Why the failure was structurally expected** — worth recording so nobody
re-runs it. Per KC21/KC22 in the ck-dk registry, the odd channel factors
`S = h·D(ũ)` with `D` outside every tested (q-)holonomic class
(transcendental/resurgent). A finite algebraic `E = G(η²)` would have tied the
even channel to the odd generator by a finite relation — in *tension* with that
transcendence. Its failure is consonant, not surprising.

**Where the live frontier actually is** (per `2026-07-17-1ppq-path-reassessment.md`):
the **q-Borel / Écalle acceleration of the D-ladder** is the one live odd-channel
route. There is **no fibre-level shortcut through η²**. Any future agent
proposing an `η²`-profile identification should read the 07-17 refutation first
— that class is closed.

**Net effect on this bean:** of the two residual items recorded 2026-08-07, the
single-`𝔙` assembly is *answered* (refuted scope-(a)), not open. The `Im 𝔙` Q_β
kernel item stands as recorded, still gated on *deriving* the Habiro/SW-residue
prolongation symbol (fitting Φ₂ remains the forbidden seventh ansatz).

## Triage 2026-08-19 (fibre workplan) -- the residual is now four named options

Re-triaged this axis against what the qou-cds1 arc established (observable level DEGENERATE: Im(q0)=0 => real weights => real trace => Im frakV == 0, so any live frakV is fibre-level). Options written up in docs/audits/2026-08-19-frakv-fibre-workplan-options.md and beaned:

 qou-jqjc  F  witness machine-surface repair (assertions:[] + allPassed)   -- cheapest, independent
 qou-e58e  D  q-parameterise the atom word builder => tr_M(q0^-1)          -- unblocks the rest
 qou-ztod  A  bridge CyclicFaddeevPhi(N=4) to the zeta4 analytic model     -- both halves already sorry-free
 qou-sglq  E  re-scope the four "Q_beta is bar-odd" corpus sites

Not beaned, deliberately: NZ/A-polynomial (option C) is real but does not become concrete until qou-e58e lands; Habiro/cyclotomic (option B) routes through the GATED c_k Habiro element and is NOT recommended now. Pre-existing todos 5lcg (zeta4-residue Lean certificate + surviving cubic) and pusy (zeta4 character-parity prune, generic R) remain the Lean-side complements to qou-ztod and are NOT duplicated by it.
