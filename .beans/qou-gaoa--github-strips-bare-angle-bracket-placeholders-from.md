---
# qou-gaoa
title: GitHub strips bare <angle-bracket> placeholders from comment bodies, and coordinate.md's templates are full of them
status: todo
type: task
priority: normal
created_at: 2026-08-21T23:05:29Z
updated_at: 2026-08-21T23:08:21Z
---

## Observed

My coordination comment on #5419
([`5375716115`](https://github.com/litlfred/qou/pull/5419#issuecomment-5375716115))
was posted containing this, inside a ```python fence:

    out = json.load(open("<main's version after #5367>"))   # 67 criteria

Reading the comment back through the API, the stored body is:

    out = json.load(open(""))   # 67 criteria

The placeholder is **gone from the stored body**, so it was removed before
storage, not at render time. The rest of the comment is intact, and every
backticked span survived.

**The code fence did not protect it.** That is the part worth knowing — the
instinct is that a fence makes text literal, and here it did not, which means
whatever strips it runs on the raw body ahead of any markdown parsing.

## Why it matters more than a cosmetic slip

The comment's entire purpose was telling a sibling how to resolve a `.qa.json`
conflict **without deleting 56 agent verdicts**. The mangled line is the one
showing which file to load. The prose instruction ("take the union, not your
side") is unambiguous and stands, so nothing was actually lost this time — but a
coordination comment whose worked example silently loses its filename is one
copy-paste from doing the harm it was written to prevent.

## The templates teach the pattern

[`local/coordinate`](.claude/skills/local/coordinate.md) §3 and §4 are the
templates every agent pastes from, and they are built out of exactly this
construct:

```
## Coordination from #<your PR>
**Picking up:** <one sentence — which workplan phase / task>
- I will not touch: `<the sibling's territory>`
- Landed in `<commit-sha>`: <one sentence>
## Sibling-PR triage report (<your PR>, <timestamp>)
## Progress from #<your PR> · `<short-task-name>`
```

Note the asymmetry already visible there: `` `<the sibling's territory>` `` and
`` `<commit-sha>` `` are backticked and would survive; the bare ones —
`#<your PR>`, `<one sentence …>`, `(<your PR>, <timestamp>)` — would not. So a
posted §3 comment reads *"Coordination from #"* and *"**Picking up:**"* followed
by nothing.

## Not fixed here, deliberately

Two reasons, and the second is the real one:

1. **Scope.** This is a content-manifest PR advertising a `content/` + `.beans/`
   only diff; a skill-doc edit does not belong in it.
2. **One sample.** I have exactly one observation and a plausible mechanism
   (HTML-tag sanitisation on the raw body). That is enough to *record*, not
   enough to assert as a rule — and this session has already produced three
   corrections that all came from asserting ahead of measuring. Confirm before
   editing the skill: post a throwaway comment carrying a bare `<x>`, a
   backticked `` `<x>` ``, an `&lt;x&gt;`, and one of each inside a fence, then
   read the body back.

## Fix, once confirmed

Backtick every placeholder in the `coordinate.md` templates. Costs nothing, is
correct whether or not the stripping is universal, and renders as code — which
is what a placeholder should look like anyway. Worth checking the other
skills that carry comment templates for the same construct.


---

## CONFIRMED — and my proposed fix was wrong

Ran the six-form test as a comment on #5367
([`5376315977`](https://github.com/litlfred/qou/pull/5367#issuecomment-5376315977))
and read the body back through the API.

| # | form written | stored |
|---|---|---|
| 1 | bare, tag-shaped — `&lt;div&gt;` | **gone** |
| 2 | bare, prose-shaped with spaces + apostrophe | **gone** |
| 3 | **backticked**, tag-shaped | **gone** (the backticks survive; the content does not) |
| 4 | **backticked**, prose-shaped | **gone** |
| 5 | HTML entities `&amp;lt;div&amp;gt;` | **SURVIVED** |
| 6 | inside a ```python fence, both shapes | **gone** |

**Backticking does not protect it.** That was the fix this bean proposed one
entry above, and it is refuted. I had inferred it from the wrong evidence:
backticked spans in my #5419 comment survived, but *none of them contained
angle brackets* — so what I actually observed was backticks surviving, not
angle brackets surviving inside backticks. Untested inference presented as the
remedy.

The discriminator also came back the aggressive way. Form 2 —
`main&#39;s version after the merge`, spaces and an apostrophe, nothing like a
tag name — vanished exactly as `&lt;div&gt;` did. So the sanitiser removes
**anything** between angle brackets, not merely valid HTML tags.

### The rule

> Angle-bracketed text is stripped from a GitHub comment body in **every**
> context — prose, inline code, and fenced code blocks alike. Only `&amp;lt;` /
> `&amp;gt;` entities survive.

Which layer strips it — GitHub on POST, or the MCP tool before it — I cannot
tell from here, and it does not change the authoring rule.

### Corrected fix for [`local/coordinate`](.claude/skills/local/coordinate.md)

Not backticks. Either:

- **entities** — `&amp;lt;your PR&amp;gt;`, correct but unreadable in the source
  template; or
- **drop angle brackets from the templates entirely** — `#NNN`,
  `{one sentence}`, `COMMIT-SHA`, `{the sibling's territory}`. Readable, safe,
  and it removes the trap rather than escaping around it.

The second is better. The templates are meant to be pasted and filled in by
agents who will not be thinking about HTML sanitisation, and a placeholder
syntax that silently deletes itself is a trap regardless of whether one
particular escape works.

Worth grepping the other skills that carry comment or PR-body templates for the
same construct before fixing, rather than fixing this one file and assuming.
