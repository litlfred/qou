---
# qou-ibbr
title: 'atomic_tr_m_mpfr_50dps muon leg now reads the PROTON y_lambda table: a straddle created by cbc8237daa'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:31:51Z
updated_at: 2026-08-21T22:00:55Z
---


## What happens

`atomic_tr_m_mpfr_50dps` is a two-pin comparison producer: it emits
`atomic-tr-m-mpfr-50dps.witness.json` (muon leg) and
`atomic-tr-m-mpfr-50dps-proton.witness.json` (proton leg), and its recorded
`median_rel_move` across the q₀ migration is 1.1537e-08 — the μ–p gap to
three figures, which is what a correct two-pin comparison should show.

Upstream `cbc8237daa` ("fix(y_lambda_tower): gate against the PROTON table")
switched `y_lambda_tower_infra.CANONICAL` from the muon y_λ table to the
proton one. That commit is right on its own terms — it fixed a genuine
straddle where the closed form was evaluated at the proton pin and gated
against the muon table. But it is global, so **every** consumer of the tower
now gets proton y_λ, including the leg of this producer that is supposed to
be muon.

## The evidence, measured

Regenerating the producer on a tree containing `cbc8237daa`:

    tr_M_at_q0_50dps   1.14575978171993650736…  ->  1.14575982831999277043…
                       ~40.7 ppb

    abs_diff_vs_bridge  ~1e-9  ->  ~5e-8      (50x WORSE)

The second number is the diagnostic, not the first. This producer computes
tr_M two ways and compares; the disagreement between its own two methods grew
fiftyfold. A pin change moves both methods together and leaves their agreement
intact. Only a straddle — one method on proton y_λ, one not — degrades the
*internal* cross-check like that.

40.7 ppb is also not the μ–p gap (11.54 ppb); it is the gap amplified through
y_λ, the same amplification `cbc8237daa`'s own message measures as 2.40e-09 at
n=2.

## Why nothing on main shows it yet

Main's committed witness predates `cbc8237daa` and has not been regenerated
there. The straddle is latent: it appears the moment anyone re-runs this
producer, on any branch. PR #5349 hit it only because the migration
regenerates producers; I reverted that regeneration rather than ship a
straddled number, so #5349 leaves main's witness untouched.

## To close

1. Decide whether the muon leg should still exist at all. Under the
   proton-everywhere directive (AGENTS.md rule 4, recorded 2026-08-19) the
   answer may be no — in which case this producer becomes single-pin and the
   question dissolves.
2. If it should exist, the muon leg must take muon y_λ explicitly. The
   per-anchor caches already exist (`regenerate_y_lambda_mpfr.OUTPUT_BY_ANCHOR`,
   `y-lambda-mpfr-witness.json` vs `y-lambda-mpfr-proton-witness.json`), so
   this is a call-site change, not a rebuild.
3. Re-run and confirm `abs_diff_vs_bridge` returns to ~1e-9. That number, not
   tr_M itself, is the test that the straddle is gone.


---

## CORRECTION — the attribution above is REFUTED by measurement

I attributed this to `cbc8237daa` switching the y_λ tower to the proton table, and called it a pin straddle. **Measured, the pin cannot account for it.**

### What actually moved

Regenerating on pristine `main` (no changes of mine) reproduces the degradation, so it is a property of `main`, not of #5349. Splitting the producer's two methods:

| side | `main` committed | pristine re-run | verdict |
|---|---|---|---|
| **peel** | `1.14575978228783550472` | `1.14575978228783550472` | **byte-identical** |
| **bridge** | `1.14575978171993650736` | `1.14575982831999277043` | **moved ~40.7 ppb** |

So the peel is a stable reference and **only the bridge moved**. That much of the bean stands.

### Why the pin is not the cause

Computing the bridge for the proton atom under each y_λ table, everything else held fixed:

```
pre-D muon table       tr_M = 1.065306260974836199652016
current muon table     tr_M = 1.145759828887891988742418
current proton table   tr_M = 1.145759828319992770436796
main committed bridge      = 1.145759781719936507366600
peel (unchanged)           = 1.145759782287835504720000
```

**Muon table vs proton table differ by 5.7e-10.** The regression is **4.6e-8** — roughly **80× larger**. The pin choice is the wrong order of magnitude, so "the muon leg reads the proton table" cannot be the explanation, even though it is a true statement about the code.

The `~1e-9 → ~5e-8` cross-check figure in the bean is right, and my reading of it as diagnostic-of-a-straddle was wrong: **5.7e-10 is what a pin straddle looks like here**, and it is roughly the size of the *original, healthy* `abs_diff_vs_bridge` (5.68e-10). A straddle of this kind is invisible at the scale of the regression.

Note also that neither current table reproduces the committed value, and the pre-D table gives `1.0653…` — nowhere near it. So the committed bridge value came from a state matching neither.

### Status: cause NOT established

`993e15015b` ("both y_lambda roots to **convention D** — muon cache and the 28k-entry wenzl table") re-rooted the muon table from `0.41539578633…` to `0.50540422769…` at the *same q₀* — a convention change, not a pin change, and the right order of suspicion. But I have **not** verified that the peel is still on convention C, so "the cross-check now compares C against D" remains a hypothesis, not a finding. It is the next thing to test — AGENTS.md gives an anchor-free test for it (the deuteron denominator factoring as `192·q²³·(q²+1)³` under D).

**What this means for `abs_diff_vs_bridge`:** if the hypothesis holds, the field no longer measures what its name says, and its regression is expected rather than a defect. Do not "fix" it by re-pinning anything.

### What landed anyway, on its own merits

`tr_m_wenzl_bridge_mpfr._load_y_lambda` now derives its default table from the caller's own `q_str` (explicit `y_lambda_path` still wins; unrecognised q₀ keeps the old default). The bridge already accepted `q_str` and already had `anchor_of_q0`, and its own comment complains that it "accepts q_str and then ignored it when choosing weights" — repointing the default at the proton table fixed the majority case and left the exact mirror live.

That is a real latent defect and worth closing, but it is **not** this bean's cause, and it is honestly small: **5.7e-10** on the muon leg. Verified a no-op for the production consumer — `binding_canonical` re-run is byte-identical in every mathematical field (timings and provenance only).

Bean stays **open** on the unestablished cause, re-scoped away from the pin.


---

## 2026-08-21 (later) — seven causes eliminated; the question is now sharper and NOT a pin question

Continued from the correction above. Every candidate I could name is refuted **by measurement**, so recording the eliminations rather than guessing an eighth.

The quantity: main's committed bridge `tr_M` for the proton atom is `1.14575978171993650736` (landed `c3a7e16856`, 2026-08-11). Re-running the same producer today gives `1.14575982831999277043` — **~40.7 ppb** — while the peel side is **byte-identical**.

| # | candidate | measurement | verdict |
|---|---|---|---|
| 1 | pin / layer straddle | muon vs proton y_λ table move tr_M by **5.7e-10**; regression is 4.6e-8 | **refuted** — 80× too small |
| 2 | convention C vs D | a C→D table swap moves tr_M **~7.5 %** (`1.0653` vs `1.1458`) | **refuted** — ~6 orders too large |
| 3 | y_λ table drift | proton n=3 weight byte-stable across `cbc8237daa` and to main; muon table stable since `993e15015b` (08-10, *before* the 08-11 value) | **refuted** |
| 4 | bridge code | only commit touching `tr_m_wenzl_bridge_mpfr.py` since 08-11 is my own `9e3d984719` | **refuted** |
| 5 | environment | committed witness records `python 3.11.15 / mpmath 1.3.0 / pyhecke_native 0.9.0`; this container **matches exactly** | **refuted** |
| 6 | Rust-path confound | both the committed run and mine record `effective_method: hoefsmit-python-fallback` | **refuted** |
| 7 | table coverage / precision | both tables `dps=50`, identical weight counts at n=3 and n=9 | **refuted** |

Also worth striking from the record: **`cbc8237daa` never touched the bridge at all.** Its diff is `y_lambda_tower_infra.py` + three witnesses. My original attribution was wrong about the mechanism *and* about the file.

And the `y-lambda-at-q0.witness.json` cached-accessor trap (AGENTS.md §q₀ rule 4) does not apply — `wedderburn_jones_markov.y_lambda_at` already carries a guard whose docstring says that cache "holds C weights and must NOT be served".

**Run-to-run determinism confirmed:** two consecutive local runs are byte-identical (`1.145759828887891988742418`).

### The sharpened question

Same repository state, same recorded environment, same effective method, deterministic — and the producer **does not reproduce its own committed value**. The 40.7 ppb is not a pin, not a convention, and not a code or dependency change that git can see.

This is the same sentence as sibling **#5386**'s title, about a different producer: *"Repin q-beta-operator-valued-N3 to proton — and its committed witness does not reproduce."* Two independent producers failing to reproduce committed values under matched conditions is more likely one cause than two. That connection is the most promising lead and is worth pursuing jointly rather than separately.

### Re-scope

Bean stays **open**, re-scoped from "muon-leg straddle" to **"committed value not reproducible under a matched environment; cause unknown; 7 candidates eliminated"**. `abs_diff_vs_bridge` degrading 50× remains the sharpest *symptom* — the peel is a stable reference and the bridge is what moves — but it is not diagnostic of a straddle, which is where I went wrong twice.

**Do not** re-pin, re-root, or rebaseline anything to make the number agree. Nothing measured supports any of those, and the committed witness on `main` is untouched.
