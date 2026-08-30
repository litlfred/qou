---
# qou-silm
title: AGENTS.md's frozen canonical muon pin is stale — the anchor moved to CODATA-2022 on 2026-08-28
status: todo
type: task
priority: normal
created_at: 2026-08-30T01:17:44Z
updated_at: 2026-08-30T02:36:55Z
---

Found while diagnosing a declaration/content mismatch under `qou-5wng`. NOT a
corpus break — I raised that alarm and it was wrong. The finding is a
documentation-currency one.

## What is true

`computations/q-pinning-50-digit.witness.json`, the anchor-DEFINING witness that
`qou_substrate.witness._q0_value_for_anchor("muon")` reads, was regenerated
**2026-08-28T20:47:21Z** and now holds

    1.109978595642739046681795129380001752700065561029011556...

AGENTS.md §"q₀ anchor convention" names the **frozen canonical pin** as
`1.1099785955573347…`, and lists `…56427390…` as merely one of three values
called "the muon q₀" ("lepton tower, CODATA 2022"). That mapping is now
inverted: what the document calls a derivation variant IS the live anchor, and
what it calls the frozen pin is carried by exactly one witness in the tree.

## What is NOT true — my own alarm, retracted

AGENTS.md constraint 1 warns that re-pinning this file produces corpus-wide
`Q0_FLIP`s (262 in the recorded incident) and hard-fails every `ideal_muon`
producer. **That did not happen here.** Measured over all 3206 tracked
`*.witness.json`, comparing each recorded `q0Value` against its own stamped
anchor on the COMMON PREFIX: everything agrees except one witness rounded to 16
digits (`qbeta-hoefsmit-chi-cross-anchor-stage-b-unblocked-probe` — float64
precision, not a different pin) and one muon witness still carrying
`1.109978595557334719899763`. The anchor moved and the corpus moved with it.

## I measured it wrong THREE times, each differently

Worth recording, because it is the pattern this corpus keeps paying for:

1. **Fixed-width prefix (24 chars)** → 29 "flips", 28 of them false. Witnesses
   record q₀ at different precisions; a 17-digit `1.1099785827513808` is not a
   disagreement with a 50-digit anchor.
2. **`rstrip("0")` + `startswith`** → false "REAL disagreements" whose printed
   `recorded` and `anchor` rows were visibly IDENTICAL. Cause: a witness may
   record MORE digits than the anchor string, so `ref.startswith(v)` fails on
   agreement.
3. **Common prefix, `min(len(v), len(ref))`** → correct. Most apparent
   divergences sit at digit 50, beyond the anchor's own defined precision.

Two numbers recorded at different precisions are not compared by string
equality, and I reached for string equality twice.

## The decision, and it is the owner's

Whether AGENTS.md should be updated to name `1.109978595642739046…` as the live
muon anchor. I have NOT edited it.

* **What it means** — the document's stated canonical value and the value the
  code resolves have diverged; an agent following the document computes at a pin
  nothing in the tree uses.
* **What it costs** — a paragraph in §"q₀ anchor convention" plus the
  three-values table, which currently labels the live anchor as a variant.
* **What it risks** — low if the CODATA-2022 update was deliberate; if it was
  NOT, documenting it would ratify an unintended re-pin of the one file the
  document says must never be re-pinned. The tree cannot tell me which: the
  regeneration is consistent, and that is what both cases look like.
* **What it commits to** — treating the muon anchor as CODATA-tracking rather
  than frozen, which changes what "the muon pin" means for every future witness.
* **Default if nothing is done** — the document stays stale and agents keep
  reading `…5557334…` as canonical while the code returns `…56427390…`.

**My judgement, not a finding:** corpus consistency says this was carried out
deliberately, so AGENTS.md should be updated — but "frozen" is a strong enough
word that I would not change it without the owner confirming the re-pin was
intended.

## Blast radius in real terms

`_q0_value_for_anchor` feeds every `ideal_muon` producer's stamp, and
`q_parameter`'s anti-corruption guard hard-fails when the muon anchor cannot be
established. The single witness still on the old pin is in the `y-lambda`
family. Nothing is currently failing.


## ANSWERED 2026-08-30 (owner asked "moved from what?") — and my framing was wrong twice

**From** `1.10997859555733471989976322048322502665620840878015368660798114614493`
**To**   `1.109978595642739046681795129380001752700065561029011556974045769999095`

**Commit `fca08de7d2`, 2026-08-22 21:23 UTC** — *"muon anchor -> CODATA 2022
(owner ruling): derive it, stop the self-certification"*, quoting the owner:
*"2022 CODATA better than 2018. A --> CODATA 2022."*

### Two corrections to what this bean said

1. **The date was wrong.** I wrote 2026-08-28. That is the `computedAt` of a
   LATER regeneration (`83bab99730`, "carry convention D through to the stale
   witnesses"). The VALUE changed on **2026-08-22**. Reading a `computedAt`
   stamp as the date a value changed is the same class of error as reading a
   `scriptCommitSha` as provenance — the stamp records the last run, not the
   last change. `git log -- <file>` was the right instrument and I did not use
   it until asked.
2. **The open question is closed.** I framed this as "was the re-pin
   deliberate? I cannot tell from the tree." It was an explicit owner ruling,
   quoted verbatim in the commit message — i.e. the tree DID say, in the one
   place I had not looked.

### Why the old value had to go — sharper than "a CODATA update"

Per `fca08de7d2`: the old anchor inverts to `m_μ/m_e = 206.768282989315`, which
matches **no published CODATA**, and disagrees by **1.4 ppb** with the ratio the
SAME witness declares in its own `calibration_inputs` (`206.7682827`, CODATA
2022). The witness contradicted its own stated input. Root cause named in that
commit: `q_pinning_50_digit.py` is listed `ideal_muon`, so `q_parameter` rebound
`q_at` for that very producer and it self-certified.

### What actually remains

Only the documentation gap: **AGENTS.md §"q₀ anchor convention" still names
`1.1099785955573347…` as the "frozen canonical pin"**, eight days after a ruling
replaced it, and its three-values table still lists the live anchor
(`…56427390…`) as merely "lepton tower, CODATA 2022". No risk analysis is needed
— the change was ruled, the corpus is consistent with it (measured: 3206
witnesses, no genuine Q0_FLIPs), and the word "frozen" is simply out of date.
