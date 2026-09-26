---
# qou-8321
title: Bump .folio-assistant-pin off df28d02 — and the target is moving ~80 commits/hour
status: todo
type: feature
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-26T11:20:29Z
updated_at: 2026-09-26T11:53:59Z
parent: qou-n4r9
---

**Owner-gated. `qou-ty42` records this as step 5, "NOT DONE — owner's call".
Nothing here changes that; this story records what the bump now involves.**

## The target is moving fast enough to matter

Measured this session, roughly one hour apart:

```
e53bba80284   (first measurement)
42ccfb38b63   (second)      -> 80 commits
```

The pin is `df28d02` (2026-09-07), so it is now **~19 days and several hundred
commits behind**. Two consequences:

1. **Pick a sha and hold it.** "Bump to main" is not a reviewable instruction at
   this velocity — the sha that gets reviewed will not be the sha that lands.
   Name the exact sha in `.folio-assistant-pin` and in the commit message.
2. **Any plan written against main goes stale in hours.** This epic's own
   `qou-yf1y` had to be corrected mid-session for exactly that: a sibling reading
   said the declaration was folded into the config, and 80 commits later it is a
   separate `<name>.json`.

## The pin file's own rule, which binds this commit

From `.folio-assistant-pin`'s header:

> When you bump it, state the before/after issue counts in the commit message —
> a change in count is a platform behaviour change and should be looked at, not
> absorbed silently.

**Both counts must be taken at the SAME corpus commit**, which the last bump's
note is explicit about. The 2026-09-07 bump recorded `428ca5c → 6 lines / "9
issue(s)"` against `df28d02 → 3 lines / "3 issue(s)"`, and explained the delta
(three `Unknown field` warnings clearing because four block schemas began
extending `BlockBaseSchema`). That is the standard to meet.

Current baseline at the pin, measured 2026-09-26: `run-validate
content/quantum-observable-universe` → **2 issue(s)** (a bibliography info line +
`lem:piece-a-corner-removal-obligation` with no Lean declaration).

## Prerequisites, and one of them is a hard blocker

- **`qou-yf1y` MUST land first.** After the bump, `findDeclarationFile` decides
  what an instance is, and `harness.json` fails its test (stem `harness` ≠ name
  `qou`). Bump without it and qou has **no discoverable instance**.
- **`qou-pwp9` should land first.** `build.yml` calls the platform at `@main`,
  which bypasses the pin entirely — bumping the pin while that line stands
  improves nothing for the published build.
- `qou-utbr` and `qou-yqko` are independent of the bump and can land either side.

## The layout probe already handles both worlds

`setup-folio-assistant.sh` probes for `cat-harness/schemas/types.ts` and points
the symlink at whichever root holds the platform, so qou works against the
pre-split and split layouts. This session's run reported `platform layout:
pre-split (clone root)`. So the bump is not a cliff — but note the same script
**silently declines to move a dirty clone and still exits 0** (`qou-ty1p`), which
is precisely how a bump can appear to have happened and not have.

## Not started.



## Added 2026-09-26 — this bump now OWNS one deletion

`qou-yf1y` has landed `qou.json` + `qou.config.json` and deliberately left
`folio.config.json` in place, because at the pin it is the only config the platform reads.

**So the bump commit must also `git rm folio.config.json`.** Doing it earlier leaves the
folio unconfigured with no error — `profile-check.ts` reports `undetermined` and runs
every criterion including the paper adapter's LaTeX-shaped axes. Doing it later leaves two
configs that can disagree.

Also note `qaAxes` is now set in **both** files. At the pin it is a no-op (measured:
`archimedean-wall` is not an axis there); after the bump the `qou.config.json` copy is the
live one.
