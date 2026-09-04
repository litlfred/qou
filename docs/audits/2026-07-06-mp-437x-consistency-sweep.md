# m_p ~437× de-fit — corpus-wide consistency sweep (2026-07-06)

> **🛑 CURRENCY (2026-09-03): the count this sweep ENFORCED is itself now
> superseded. Do not use this document as the authority on the L2 count.**
>
> This sweep aligned the corpus to **2/7** (m_e, m_K/m_π), which was
> correct on 2026-07-06. Two later audits moved it twice:
>
> - **2026-08-18** — `beats_100x_count = 2` counts **calibration inputs**
>   alongside predictions. `m_e` is the CAL-1 input that *defines* the MeV
>   unit, so its `err_ppb` is zero by construction, not by measurement —
>   the same ground `m_p` was already excluded on. Separating inputs from
>   predictions gives **1 of 5 scoreable**, and it is `m_K/m_π`. Quote
>   `beats_100x_scoreable` / `scoreable_total`, never bare
>   `beats_100x_count`.
>   ([audit](2026-08-18-mass-binding-accuracy-what-is-closeable.md))
> - **2026-08-22** — even that 1 is inflated: `m_K/m_π`'s sub-100× result
>   is manufactured by an EM correction whose truncation order beats the
>   untruncated series (chosen against the data) and whose `α_em` input is
>   conditional on an open Lean `sorry`. The **unconditional
>   parameter-free** count is **0/5**.
>   ([red-team](2026-08-22-mK-mpi-l2-red-team.md))
>
> **State it as "1/5 scoreable — and that 1 is truncation-fitted +
> α_em-`sorry`-conditional ⇒ 0/5 unconditional".** The
> `observable-sector-tracker.md` was already updated to the 1/5 framing;
> the fourteen documents this sweep corrected to "2/7" were **not**
> re-swept, so expect stale 2/7 wording in them.
>
> The sweep's *method and hit table below remain valid* as the record of
> what the 2026-07-04 de-fit ruling touched — only the count it propagated
> has moved.

**Date:** 2026-07-06
**Bean:** `mo5p`
**Branch:** `claude/cheat-sheet-derivation-gaps-0ykco4` (PR #3440)
**Ruling swept for:** [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md)
— the fitted Habiro tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` was dropped from
production m_p (PR #3280); de-fitted documented-pin round-trip **+1.35 ppb**
(~437× miss of the 100× target); authoritative L2 count **2/7** (m_e,
m_K/m_π) per `per-observable-100x-status.witness.json`
(`beats_100x_count=2`).

## Scope

Docs-only sweep (`docs/`, `content/`, `computations/*.md`, `README*`) for
claims contradicting the ruling: "3/7" / "3 of 7" / "4/7" L2 counts,
"m_p PASSES", "0.0004 ppb" as live, `beats_100x_count=3`, the `(1+46u⁴)`
tower cited as production. Excluded: the 2026-07-04 audit itself, AGENTS.md
and `docs/precision-goals.md` (reference state, verified current),
`docs/canonical-derivation-cheat-sheet.md` (verified current — §"L2 100×
Subgoal-1 close-out" already carries the 2026-07-05 2/7 update), historical
blocks already carrying a supersession banner, and false positives (magic-
number "4/7 derived", the `3/7` rational candidate in λ_scale spikes,
`24/77` partition coverage, `docs/audits/_deprecated/`). No compute or
witness files touched; the committed witness already carries
`beats_100x_count=2`. **`content/` tree: zero hits** (no content-block
edits, so no render-QA battery was needed).

## Hits and dispositions

Class legend: **(a)** live doc — corrected inline / bannered this sweep;
**(b)** content block `.md` — none found; **(c)** historical / dated
snapshot or already-superseded — listed, not edited.

### Class (a) — fixed this sweep (14 files, 3 commits)

| path:line(s) | stale claim | action |
|---|---|---|
| `docs/observable-sector-tracker.md:1,44-65,123-136,246-248` | "3/7 beat 100×"; m_p 0.0004 ppb ✓✓; stale m_n/Q_β/Δ_pn residuals | 🛑 banner + L2 table corrected to 2/7 (m_p +1.35 ppb ✗ ~437×); m_n 2.389 ppb (~416×), Q_β 1248 ppb (160.1×), Δ_pn 755.6 ppb refreshed from live witness; baryon rows + priority queue item 2 corrected | commit `cda34e834d4` |
| `docs/audits/2026-06-28-calibration-canon-decay-width-ruling.md:60,83` | "L2 = 3/7"; "Summary unchanged 3/7" (AGENTS.md read-first doc) | inline currency notes (ruling itself unaffected) | `bcd043140b4` |
| `docs/audits/2026-06-26-l2-dashboard-status-and-tnjb-caveat.md:23,46,57,66,80` | "Canonical count: 3/7" (the tnjb reference doc) | 🛑 top supersession banner; tnjb caveat explicitly kept standing | `bcd043140b4` |
| `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md:13-20` | headline "3 of 7 fail"; m_p row ✓ 0.0004 (cited from AGENTS.md + precision-goals) | 🛑 refresh note: failing set now 5/7, met 2/7; trio analysis stands | `bcd043140b4` |
| `docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md:8-10` | its own currency banner said "live dashboard is 3/7" | banner parenthetical updated to 2/7 | `bcd043140b4` |
| `docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md:172-173` | "live count **3/7**" | inline correction | `bcd043140b4` |
| `docs/audits/2026-06-20-binding-gate-stocktake-post-qbk2.md:114,122` | "3/7 L2 met" (twice); "foreground the 3 met observables (m_p, …)" | inline corrections | `bcd043140b4` |
| `docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md:108` | "L2 = 3/7 (m_e, m_p anchors + m_K/m_π)" | inline correction | `bcd043140b4` |
| `docs/audits/2026-07-03-trace-convention-decision-package.md:201` | "canonical L2 dashboard stance (3/7, m_μ FAIL)" | inline correction | `bcd043140b4` |
| `docs/audits/2026-06-23-over-zealous-binding-closure-review.md:92` | "precision-goals.md: 3/7 L2 met" | inline date-scoped correction | `bcd043140b4` |
| `docs/audits/2026-06-23-delta-lambda-three-lever-status.md:123` | same citation | inline date-scoped correction | `bcd043140b4` |
| `docs/audits/2026-06-24-l2-shared-root-currency-triage.md:17,25` | margins table m_p "0.0004 ppb ✓"; "3/7 meet" | 🛑 top currency banner | `bcd043140b4` |
| `docs/audits/2026-06-24-fbor-q3-exact-habiro-ratio-fit.md:43-57` | `habiro_ratio` shown as production at +0.0004 ppb | 🛑 banner: tower DROPPED 2026-07-04; `/q³`-exact + Li₂^q findings stand | `e7cf2a2114a` |
| `docs/audits/2026-06-24-mp-habiro-c4-keystone-characterization.md` | c₄ ≈ 46 presented as the keystone mass-sector target | 🛑 banner: c₄ pin-dependent (0 at proton pin); keystone target is the 11.5 ppb μ–p splitting | `e7cf2a2114a` |

### Class (b) — content blocks

**None.** All content-tree greps returned zero hits; the math-bearing
`content/**` blocks never carried the 3/7 count or the m_p-pass claim.

### Class (c) — historical / already-current (listed, not edited)

| path:line | why skipped |
|---|---|
| `docs/precision-goals.md`, `AGENTS.md`, `docs/canonical-derivation-cheat-sheet.md:318` | reference state — verified already 2/7-current |
| `docs/audits/2026-07-04-qbeta-derived-ladder-tiers.md:37` + `docs/audits/scripts/qbeta_derived_ladder_tiers_probe.py:35` | already state the 3/7→2/7 drop correctly |
| `docs/audits/2026-07-05-cheat-sheet-currency.md:26,37` | documents the correction (quotes the stale text deliberately) |
| `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md` | already carries a ⚠ SUPERSEDED banner; superseded-sharpened by the 2026-07-04 audit itself |
| `docs/audits/2026-06-06-l2-shared-root-post-klr-update.md:61`; `2026-06-03-m-n-delta-pn-qbeta-cal-anchored-acceptance.md:70`; `2026-06-03-l2-closure-habiro-3-q-25-universal-template.md:94`; `2026-05-30-qbeta-c3-wiring.md:64`; `2026-05-30-alpha-shift-universal-derivation-chain.md:88`; `2026-06-23-trM-crosscheck-colorweighting-split-at-C.md:98`; `2026-06-24-q0-layer-migration-scope.md:90`; `2026-05-29-low-mass-sweep-full-audit.md:72,167` | dated snapshots whose counts/values are date-scoped in context ("as of", PR-effect tables); the corrected reference docs above are what agents consult for currency |
| `docs/coordination/1ppq-qbeta.md:153` | dated ledger row; the ledger self-corrects at line ~683 ("m_p (#3280, MERGED). The `(1+46u⁴)…` Habiro tower was a CODATA fit") |
| `docs/coordination/2026-05-26-proton-mass-identity-workplan.md:67`; `docs/workplans/2026-05-27-1ppQ-reassessment.md:5`; `docs/workplans/2026-06-30-j1hg-z5vu-overcount-q0repin-sequencing.md:36` | already describe the tower as a CODATA fit / +242 ppb regression / purged |
| `docs/coordination/2026-07-02-lambda-a-excision-consumer-lanes.md:101` | dated lane-migration record; its "0.0004 ppb" result column reflects the pre-drop witness the script read at that date. Note for readers: post-drop the substrate-identity witness yields +1.35 ppb on regeneration |
| `docs/audits/_deprecated/*` (magic-number "4/7"), λ_scale-spike `3/7` rational candidates, `24/77` partition coverage, `2026-05-06-staircase` 8/16 rows, `13/71` crossing fractions | false positives — not L2 counts |

## Counts

- **Class (a):** 14 files fixed (1 live tracker + 13 audit docs), 3 commits.
- **Class (b):** 0.
- **Class (c):** ~20 listed, untouched.

## Authoritative state (post-sweep)

**L2 100× met count is 2/7 — m_e (CAL-1 anchor) and m_K/m_π — per
`computations/per-observable-100x-status.witness.json`
(`beats_100x_count=2`).** m_p misses ~437× (+1.35 ppb de-fitted
documented-pin round-trip; the former "0.0004 ppb pass" rode the fitted
Habiro tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)`, dropped 2026-07-04). The other
misses: m_μ ~964× (209.8 ppb, μ–p tension), m_n ~416× (2.389 ppb),
Q_β ~160× (1248 ppb), Δ_pn ~159× (755.6 ppb). Any doc asserting 3/7 (or
4/7) as *current*, or citing m_p at 0.0004 ppb as *live*, is stale; the
reference chain is AGENTS.md §Precision goals → `docs/precision-goals.md`
→ [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md).
