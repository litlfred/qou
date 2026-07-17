# 1ppQ program — ownership map (2026-07-17)

**Purpose.** A single coordination surface tying the whole 1ppQ program
together: the two precision legs, the *named* closing problems each L2 miss
reduces to after the 07-12→14 landing wave, and — the part the per-thread
ledgers and the assessment audit do **not** carry — **who owns each named
computation and where the ownership gaps are**.

**Not a reassessment.** The authoritative assessment is
[`docs/audits/2026-07-17-1ppq-path-reassessment.md`](../audits/2026-07-17-1ppq-path-reassessment.md)
(commit `6a529aa7`). This ledger is its coordination complement — read that
first for the evidence; read this for the who/what/next. Per-thread ledgers
remain authoritative for their thread (`1ppq-qbeta.md`, `alpha-em.md`,
`keystone-infra.md`, `s5-so3-keystone.md`, `z-ck-fmap-keystone.md`).

> **SAME-DAY UPDATE (2026-07-17 ~20:45Z).** Between the first draft of this
> map (~19:40Z) and now, the owner picked the three-front attack
> ([`2026-07-17-three-front-attack-specs.md`](../audits/2026-07-17-three-front-attack-specs.md))
> and a **swarm has taken all three previously-"unowned" computations** in a
> ~27-commit wave. **None of the three walls is unowned anymore** — the
> ownership table below is updated to reflect it. The coordination value has
> flipped from "flag the gaps" to "prevent collision": do **not** open a
> fourth parallel attack on the D-ladder — it is bean `qou-dri7` / #3817 plus
> the k→31 extension session. New capacity should either support a named
> owner or take genuinely-uncontended L2 work elsewhere.

## Leg status

| Leg | State | Source |
|-----|-------|--------|
| **L1** compute precision (≤ 1 ppQ cross-method) | **CLOSED** — 6/6 production atoms certified, worst \|Δ\| = 5.6e-50 | [`audits/2026-07-13-l1-4he-certification-complete.md`](../audits/2026-07-13-l1-4he-certification-complete.md); `precision-goals.md` L1 row updated this session |
| **L2** per-observable accuracy (σ_theory ≤ σ_exp/100) | **2/7** (m_e, m_K/m_π); 5 misses, all derivation-gated | `computations/per-observable-100x-status.witness.json` (`beats_100x_count=2`) |

L2 scoreboard unchanged this week **by design**: the whole 07-12→14 wave was
derivation / certification / honest-refutation, nothing wired to production.
The payoff is that each miss shrank from *a search over an open hypothesis
class* to *a single named computation*, with the surrounding negative space
proved closed (KC22 holonomic-class closure, framing-is-phase, the α_EM
loop-measure falsification).

## The three named walls — ownership map

| L2 miss(es) | Root cause | The named closing computation | Owner / live PR | State (20:45Z) |
|---|---|---|---|---|
| Q_β ~160×, m_n ~416×, Δ_pn ~159× (shared root; Q_β is the bottleneck) | c₃ exact value (bar-**odd** channel) | **Jackson q-Borel / Écalle acceleration of the D-ladder** (≡ Φ_b odd carrier). Anchors: 2-adic bar-parity grading + q\* | **#3817** (bean `qou-dri7`, parity split) + the **k→31 extension** session (`claude/dladder-qgevrey-extension-2026-07-17`); even-κ **#3683**; Stokes integer **#3805**; Φ_b carrier **#3773** | **OWNED, active.** Structural q-Gevrey drift *confirmed* → fixed-order Borel ruled out, Écalle acceleration is the honest object; parity split resolves ≥½ the drift, 3-adic normalization killed. Do not fork. |
| m_p ~437×, m_μ ~964× (μ–p pin tension) | substrate q₀ (Subgoal-2, open for all) | **colored Lawrence–Rozansky modulus identification** `\|S_{0λ}^{Σ(2,3,5)}(ζ)\| = d_ζ(λ)/D(ζ)` | **#3822** (`s5-so3-keystone.md` sessions-log) | **LANDED corrected-exact** (probe `9198ce51`, Lean fold `dac9ae28` sorry-free). Keystone's last open piece now has an exact identity. |
| α_EM (headline, per `#3612`) | photon 1-loop measure | **Bring-Jacobian photon determinant** `1/(πb₁) = 1/(8π)` — one computation certifies all loop orders | **#3810** (dilog-pentagon spine) + AG program **#3807** (b₁ = 8 exact); `alpha-em.md` | **OWNED, reframed.** `1/(πb₁)` and the additive `2/(3π)` shown to be the **same dilog-pentagon shadow** (`777234f5`); ζ-anomaly `ζ_Λ(0) = −b₁` count done. |
| (L1) | — | — | — | **CLOSED** (6/6 atoms). |

## Sequencing — all three fronts now owned (20:45Z)

The 19:40Z draft ranked these as unowned pickups; that is **superseded** — the
swarm took all three within the hour. Current reality:

1. **D-ladder q-Borel/Écalle** — OWNED (#3817 + extension). The next genuine
   step is the **per-channel parity-split local-index estimator on the extended
   k→31 rungs** (the intersection of the two active D-ladder sessions), and
   #3817's own handoff already queues it ("drop-in: same probe, higher ORD") —
   so it is **not** free capacity. New hands should *ask #3817/qou-dri7* before
   touching the D-ladder probe family.
2. **α_EM determinant** — OWNED (#3810 dilog-pentagon spine + #3807 AG). The
   `1/(8π)` derivation is now folded into the dilog-pentagon program, not a
   standalone front.
3. **LR modulus ID** — LANDED (#3822). The keystone's remaining work is the
   Lean `loc_matches` derivation gate, tracked in `s5-so3-keystone.md`.

**For genuinely-uncontended capacity:** the L2 scoreboard is comprehensively
covered by ~8 active sessions. Uncontended value is now in the *support* and
*integrity* layers — not a fourth parallel attack. Candidates: the ⁴He binding
stage-2 rebuild after the GP-kernel bug (`2026-07-14-gp-kernel-bug-and-he4-stage2.md`),
Model G content-block promotion (bean `qou-hfiw`), or the L1 defense-in-depth
third method — none of which any 1ppQ-front session is holding.

## This session's contribution (hygiene — additive, non-duplicative)

Branch `claude/focused-euler-ez3iu4`:

- `precision-goals.md` **L1 row currency fix** — "NOT certified (2026-06-17)"
  → "CERTIFIED (2026-07-13)"; the reassessment audit explicitly requested this
  edit (the row lagged the L1 closure).
- `onepb-status-dashboard.witness.json` refreshed post-certification
  (`all_within_1ppb` false → true).
- `authors-note` Lean-coverage stats refreshed (614/676/70/62 → 640/684/76/66)
  and the `refresh-authors-note --check` drift gate wired into
  `scripts/check-sidecars.sh` (agent preflight) + `witness-staleness.yml` (CI
  backup) so the advertised proved-counts can't silently drift again.
- This ledger.
- **⁴He binding stage-2 seminormal reverification** (the uncontended
  support-layer item flagged above) —
  [`2026-07-17-he4-stage2-seminormal-reverification.md`](../audits/2026-07-17-he4-stage2-seminormal-reverification.md).
  Rebuilt the `pyhecke_native` wheel, fixed a stale "exact GP χ" verdict-string
  mislabel, and re-ran the stage-2 witness on the seminormal engine (the
  committed one was GP-legged; the GP kernel was found buggy 2026-07-14).
  Result: dominant λ*(K) = **(9,3) survives**, but **(8,4) is near-degenerate
  (0.276 %)**, and the GP bug had **inflated tr_M(K) ~15 %** (0.06768 → 0.05723
  at 50 dps; Leg-A/B cross-check 2.09 → 8e-15). Added a fast f64 ranking
  companion + per-block checkpointing so the ~96-min run is session-boundary
  robust.

None of the three named 1ppQ-wall computations is picked up here (the swarm took
all three within the hour of the first draft; this session **deliberately did
not fork the owned D-ladder thread** #3817 — the same-day update above records
that collision-avoidance call). Its value stayed in the currency / hygiene /
coordination layer **plus the uncontended ⁴He stage-2 reverification**.
