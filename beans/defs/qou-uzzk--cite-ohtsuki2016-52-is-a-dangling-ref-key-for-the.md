---
# qou-uzzk
title: 'CITE: [ohtsuki2016-52] is a dangling Ref key for the held ohtsuki2016 — M — FiveTwoOhtsukiBridge.lean:161'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:05:25Z
updated_at: 2026-09-04T09:05:25Z
parent: qou-8lxd
---

**Class M — a one-character-class fix: a `-- Ref:` key with a suffix the registry
does not have, over a source that IS held.**

`content/quantum-observable-universe/lean/QOU/Archimedean/FiveTwoOhtsukiBridge.lean:161`:

```
-- Ref: [ohtsuki2016-52] doi:10.4171/QT/83
```

**`ohtsuki2016-52` is not in `references.ts`.** The registered key is
**`ohtsuki2016`** (`references.ts:10003`), and it is **held** — `library.docId =
104171-qt-83`, i.e. exactly the DOI `10.4171/QT/83` the dangling line quotes. So
this is the *same paper*, reached by a key that does not exist.

The suffix `-52` presumably marks *"the 5₂ result"*, which is what the file is
about. That is a locator, not a key: it belongs after the bracket
(`-- Ref: [ohtsuki2016] §… (5₂)`), not inside it.

`ohtsuki2016` is currently cited in only **3** files, so this dangling site is a
meaningful fraction of its citation surface.

**Fix:** rewrite the line as
`-- Ref: [ohtsuki2016] doi:10.4171/QT/83 — the 5₂ asymptotic expansion`,
with the section locator if one is to hand. No registry change needed.

Found alongside `[hatcher2002]` in a 70-key sweep of `-- Ref:` keys across
`Eightfold/`, `QuantumObservableUniverse/`, `BringsSurface/` and `Archimedean/`
(4 unresolved); see `docs/audits/2026-09-04-citation-gap-inventory.md`.
