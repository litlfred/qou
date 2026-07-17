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

| L2 miss(es) | Root cause | The named closing computation | Owner / live PR | Gap |
|---|---|---|---|---|
| Q_β ~160×, m_n ~416×, Δ_pn ~159× (shared root; Q_β is the bottleneck) | c₃ exact value (bar-**odd** channel) | **Jackson q-Borel / Écalle acceleration of the D-ladder** (≡ Φ_b odd carrier). Anchors in hand: 2-adic bar-parity grading (2 = unique graded prime, Lean-anchored) + q\* (third decay-sector q₀ determination) | even-κ resurgence on **#3683**; GGM Stokes integer on **#3805** | **the odd-channel q-Borel acceleration itself is UNOWNED** |
| m_p ~437×, m_μ ~964× (μ–p pin tension) | substrate q₀ (Subgoal-2, open for all) | **colored Lawrence–Rozansky modulus identification** `\|S_{0λ}^{Σ(2,3,5)}(ζ)\| = d_ζ(λ)/D(ζ)` — the W_λ/McKay keystone's last open piece (value-map + framing-is-phase already exact/proved on main) | McKay route landed on main; `keystone-infra.md` / `s5-so3-keystone.md` | **modulus ID UNOWNED** |
| α_EM (headline, per `#3612`) | photon 1-loop measure | **Bring-Jacobian photon determinant** `1/(πb₁) = 1/(8π)` — one computation certifies all loop orders; θ-graph 2-loop candidate already 1.3σ parameter-free, contingent on it. Proved-exact: it is NOT the zero-mode measure 1/(12π) (fails 1-loop by ~9500σ) | AG program on **#3807** (b₁ = 8 proved exact); `alpha-em.md` | **the determinant computation UNOWNED** (multi-week) |
| (L1) | — | — | — | **CLOSED** |

## Recommended sequencing (highest scoreboard leverage first)

1. **D-ladder q-Borel/Écalle acceleration** — one derivation can flip **3** of
   the 5 misses (2/7 → 5/7). Highest leverage; currently unowned. Coordinate
   with #3683 (even κ-tower) + #3805 (Stokes integer) so the odd carrier reuses
   their resurgence surface rather than forking it.
2. **α_EM Bring-Jacobian determinant** — sharpest single-wall problem in the
   program; second genuine 100× prediction gated on exactly one computation.
3. **Lawrence–Rozansky modulus ID** — closes the only route to the two largest
   misses (m_p/m_μ); Subgoal-2, open for all.
4. **Support #3805's G3** rather than open a fourth front.

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

None of the three named computations is picked up here — they are the next
tranche, sequenced above. This session unblocks/coordinates; it does not fork
an owned thread.
