---
# qou-x2nv
title: 198 library documents are sectioned but UNREGISTERED — and bulk registration is unsafe from extracted metadata
status: todo
type: task
priority: normal
created_at: 2026-09-07T10:08:09Z
updated_at: 2026-09-07T10:09:09Z
---

Measured 2026-09-07, after the orphan drain (#7029) closed the *invisible* population.
These are the opposite failure: **greppable but not citable**. `library/` holds them, they
have `sections/`, `summarize-library.py` gives them an INDEX row — but no
`content/schema/references.ts` entry, so **no content block can cite them**.

## Measured

`scripts/library-propose-references.py` on `main`:

    198 unregistered:  high 161  |  medium 27  |  low 7   (3 already registered)

## Bulk registration is UNSAFE, and the tool's own author says why

The script writes nothing by design. Its docstring records that an earlier mechanical
pass passed *"HAL is a multi-disciplinary open access archive"* and
*"ANNALES DE LA FACULTÉ DES SCIENCES"* **as paper titles** — repository boilerplate and a
journal masthead. *"A bibliography that lies about a title is worse than one that omits it."*

**`medium` (27) and `low` (7) are not registrable from extracted metadata at all.**
Confirmed by inspection: the medium band is largely mastheads and boilerplate —
`AMERICAN MATHEMATICAL SOCIETY`, `ANNALES DE L'INSTITUT FOURIER`, `Pacific Journal of
Mathematics`, `UC Santa Barbara` — with authors like `olume, V` and `workshop, The`.

**Even `high` is not clean.** The tool itself declares it could not parse the authors for
**60 of 161 (37%)**, e.g. `arxiv-0705.1468v1` where the raw is
`Department of Mathematical Sciences, Durham University`. One title carries confirmed
kerning damage: `arxiv-0808.2716v4` → `CUSP AREAS OF F AREY MANIFOLDS`.

So roughly **100 of 198 look registrable**, and each still needs its page 1 read.

## The authoritative source is BLOCKED in this container

161 of them have arXiv ids, so exact metadata exists upstream — but
`export.arxiv.org:443` is refused by the agent proxy:

    kind: connect_rejected
    detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
    host: export.arxiv.org:443

A **policy denial**, not a transient failure, so retrying will not help. Any registration
done in this container rests on OCR-extracted text, not on the source.

## 🛑 A caution for whoever drains this, learned the hard way

I tried to quantify the `high` band's defect rate with hand-rolled text heuristics and
**over-flagged three times in a row**, catching each only by reading my own output:

| heuristic | false positive |
|---|---|
| `\b[A-Z] [A-Z]{2,}` for kerning | matched the **article** in `A STATE-SUM FORMULA` |
| same, articles excluded | matched the **possessive** in `KEROV'S CENTRAL`, `TANNAKA'S RECONSTRUCTION` |
| trailing capitalised tail = glued author | matched the clean title `On the Definitions of Difference **Galois Groups**` |

First pass said 51% defective; corrected it is ~38%, and only **one** kerning case is real
out of six flagged. **Do not trust a regex over this text.** The one reliable signal is the
tool's own `(not parsed)` declaration, because that is the parser reporting on itself rather
than a second guess layered on its output.

## What would actually close it

1. Unblock `export.arxiv.org` (or run the drain where it is reachable) and register the 161
   arXiv-id documents from authoritative metadata. That is the only route that does not
   guess.
2. The remaining ~37 (medium + low + non-arXiv high) need page 1 read by hand; `low` in
   particular is scans and mojibake and cannot be done from the text at all.

## Default if nothing is done

Nothing breaks. The documents stay greppable via corpus-grep path 5 tiers 1–4 — the drain in
#7029 guaranteed that much — they simply cannot be *cited* by a content block, so a proof or
remark that wants one has to fall back to prose. That is a real but bounded cost, and it is
strictly better than the pre-#7029 state where they could not even be found.

## Related

- `qou-b9c3` — the orphan drain (invisible → greppable). Completed; this is the next tier up.
- `qou-cvx9` — the write-path guard, plus `scripts/library-orphan-audit.py` (#7041) which
  checks the *invariant* so no write path can reintroduce orphans.
