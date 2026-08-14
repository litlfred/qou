---
# qou-tdp0
title: The WITHDRAWN resurgent/Ecalle inference is still asserted live in 1ppq-qbeta.md
status: todo
type: task
created_at: 2026-08-14T19:37:12Z
updated_at: 2026-08-14T19:37:12Z
---

Found while fixing the same defect one file over, in PR #5022 (registry §3).
Copilot flagged the registry instance; this is the un-fixed remainder.

## The fact

The 2026-08-09 convergence correction
([`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](../docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md))
**withdrew** the resurgent/Écalle inference for the odd-channel D-ladder. The
KC22 row of `ck-dk-canonical-registry.md` records the withdrawal correctly —
the sentence is struck through and marked `WITHDRAWN 2026-08-09`, with the
reason: the inference was drawn from a *divergence*, and the ladder is
**convergent** (`k²Δ²log|d_k| → 1`, `kΔ² → 0`, so `κ = 0`).

The correction was applied to the KC22 row and **not propagated to the
summaries that restate it**. Two sites:

1. **`ck-dk-canonical-registry.md` §3 (line ~140)** — FIXED in PR #5022. It
   asserted "a genuine c₃ closure, if any, is transcendental/resurgent
   (Écalle class), not a q-difference equation" — nearly verbatim the
   sentence KC22 strikes through.
2. **`docs/coordination/1ppq-qbeta.md:1055-1058`** — **STILL LIVE.** Reads
   "(validator green): the odd-channel element is transcendental/**resurgent**
   (Écalle class) — the low-order (q-)holonomic search class is CLOSED. Do
   not …". This one is worse than a stale summary: it is an **instruction to
   future agents** resting on a retracted premise.

## What is NOT claimed here (scope discipline)

**This is not a refutation of the Écalle/Borel route.** The withdrawal is
specific and narrow: it kills the *inference from divergence*, because the
divergence is not there. It does **not** establish that Borel/Écalle
machinery is inapplicable — a convergent series with a log branch point
(`D(w) = φ(w)log(1−w/ρ) + ψ(w)`, KC22's own closed form) is still a legitimate
object for that machinery, and "Écalle median / M-dictionary lateral" as used
around `1ppq-qbeta.md:2143,2151` is a *normalization technique*, a different
usage that this bean does not touch.

Scope-(a): the defect is that a **withdrawn inference is stated as live**, not
that the surviving route is wrong. Do not convert this into a scope-(b)
exclusion without a proved invariant.

## Work

1. ~~Triage the `Écalle|resurgent` hits in `docs/coordination/1ppq-qbeta.md`.~~
   **DONE 2026-08-14.** 16 hits triaged, owner-directed fix style (append +
   inline markers + correct the one non-sequitur outright):

   | class | lines | action |
   |---|---|---|
   | (a) withdrawn inference stated live | 1055–58, 1170, 1313, 1407, 1532 | `[SUPERSEDED 2026-08-09]` marker in place; **no dated entry rewritten** |
   | (a′) invalid *inference*, not merely stale | 1809 | **corrected outright** — framing bullet, not a dated entry |
   | (b) Écalle as technique | 1486, 2143, 2151 | left — normalization scheme |
   | (c) different object | 851, 2549, 2579, 2771, 2817 | left — κ-tower / GGM–GPPV / 4₁ |

   **Root cause found:** the ledger's last entry is dated 2026-08-09 (PR #4865,
   the 5₂ saddle sum rule) — the *same day* as the convergence correction — but
   the correction itself **never got a ledger entry**. The five stale sites are
   symptoms; the missing entry is the disease. Now appended as a dated
   2026-08-14 entry, per the file's own correction convention (cf. its earlier
   `CORRECTION` / `SUPERSEDED` entries).

   **Spun out:** line 1809's "no A-polynomial recurrence *hence* resurgent" is
   invalid *independently* of the 2026-08-09 correction — non-holonomic does not
   imply divergent, and KC22's convergent-yet-not-P-finite `φ·log + ψ` is the
   counterexample. Corpus-wide sweep for that step: **`qou-arvu`**.
2. ~~**Then** check whether any open Écalle bean is *motivated* by the withdrawn
   inference rather than by the technique.~~ **DONE 2026-08-14** — see below.
3. Grep wider (`docs/`, `content/`) for the same restatement — the pattern is
   a correction applied to a detail row and not to its summaries, so other
   summary sites are likely.

## Step 2 RESULT (2026-08-14) — triaged; 4 were never live, 3 scrapped, 1 unaffected

**Correction to this bean's own framing.** It implied eight open beans. Four
were **not open**: `qou-a1bi` (scrapped), `qou-r2nh` (scrapped), `qou-jjka`
(completed), `qou-u7kc` (completed). Only four had live status, and seven of the
eight had **completely empty bodies** — frontmatter only.

| bean | disposition |
|---|---|
| `qou-a1bi`, `qou-r2nh` | already **scrapped** — no action |
| `qou-jjka`, `qou-u7kc` | already **completed** — no action |
| `qou-b00b`, `qou-xuc4` | **consolidated into `qou-dri7`**, scrapped |
| `qou-dri7` | **scrapped** — carrier; holds the full reasoning |
| `qou-vkg5` | **LEFT OPEN — unaffected** |

**The three were one task under three titles**, all created 2026-07-17, all
empty: q-Borel/Écalle acceleration + median-Watson resummation of the bar-odd
D-ladder. The titles alone settle it — acceleration, median/Watson and
Borel–Leroy all exist to sum a **divergent** series, and the ladder is proved
**convergent** (`ρ = 0.1428`, `κ = 0`). KC22 already supplies the closed form and
the parameter-free asymptotic that the "estimator gate" was to have measured.

**Scope-(a):** the *stated* task has no target. No invariant is named excluding
q-Borel methods from this function — a study of the `log(1−w/ρ)` branch point
would be a different task and needs a new bean stating that motivation.

**The distinction that keeps `qou-vkg5` alive** — two objects, one word:

| | object | regularity | resurgence applies? |
|---|---|---|---|
| `qou-dri7` et al. | bar-odd D-ladder `D(ũ)` | **convergent**, `ρ = 0.1428` | no |
| `qou-vkg5` | C1 at `∞` | **irregular**, slope `½` | **yes** |

`qou-vkg5` is live and productive (sorry-free Lean; `0`- and `∞`-side exponents
computed and cross-checked via `det A`; weight lattice pinned to `q^{½ℤ}` up to
the deck sign). Nothing here touches it. The failure mode this whole arc keeps
hitting is one name for two objects — cf. the KC21/KC22 `q*` collision (PR #5022
§9a); this is the same shape at the level of a *technique name*.

## Why it matters

Same defect class as PR #5022's two: a summary out-running the detail row that
corrects it. The corpus-grep discipline in AGENTS.md exists because agents
trust status lines; an instruction that says "the search class is CLOSED, do
not …" on a retracted basis will steer work wrongly and is the most expensive
version of this bug.
