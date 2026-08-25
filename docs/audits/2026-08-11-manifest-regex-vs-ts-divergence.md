# The QA checkers parse manifests with regex, and it diverges from the truth

Found 2026-08-11 while working `prn1` tranche 3. Bean: `prn1`.

The detangler and hygiene checkers read `uses[]` and `foreshadows[]` by
matching the manifest **text**:

```ts
content.match(/uses\s*:\s*\[([\s\S]*?)\]/)      // loadChapterGraph
tsSrc.match(/\bforeshadows:\s*\[([\s\S]*?)\]/)  // parseForeshadows
```

then pulling every quoted string out of the captured region. The content
pipeline, by contrast, *imports* the manifest and reads the real array.
The two disagree, and where they do, every ordering metric is computed on
the wrong data while `validate` stays green.

Three failure modes, all observed — two live in the corpus, one self-inflicted.

## 1. A quoted string in a comment becomes a phantom entry

```ts
uses: [
  // conj:regularity-breakdown removed (2026-06-08 §3b): this prop is the
  // unconditional reformulation "NS blowup ⟺ obstruction level n*", not a
  // result that assumes blow-up occurs; ...
  "prop:descent-condition",
  ...
]
```

`lifting-and-descent/p3-blowup-yekutieli.ts`. The TS loader sees 3 entries.
The checkers see **4**, the extra being `NS blowup ⟺ obstruction level n*` —
a label that cannot resolve, inflating out-degree and cone size.

## 2. A quoted `uses: [...]` anywhere earlier in the file wins

`braids-and-knots/hecke-log-decomposition-table-data.ts` has an
`authorNotes` body that *quotes* a manifest snippet as prose:

```ts
"`uses: [\"prop:hecke-log-decomposition\"]`, and no block with that " +
"label exists anywhere in the corpus — ..."
```

The regex is unanchored and takes the **first** match in the file, so the
checkers read that quoted example instead of the block's actual `uses[]`.
The extracted entry even carries the escape artifact
`prop:hecke-log-decomposition\\`.

Note the irony: that authorNote is documenting a *previous* fabricated-edge
incident, and the act of documenting it fabricated another.

## 3. A closing bracket in a comment truncates the list — silently

The non-greedy `[\s\S]*?\]` stops at the first `]`. A comment inside the
array containing one — `// moved out of uses[]` — ends the match early, and
every entry after it is dropped.

This is the worst of the three because **a truncated array is
indistinguishable from a shorter one**: no checker can detect it, and
`uses-resolve` has nothing unresolvable to complain about. Self-inflicted
during `cnd4` and caught only because a reconciliation count came out wrong;
it had already produced one false "criterion passed" on a list two entries
short.

## Scope

Four entries corpus-wide do not resolve to any block label, all from modes
1 and 2:

| file | field | phantom entry |
|---|---|---|
| `lifting-and-descent/p3-blowup-yekutieli.ts` | `uses` | `NS blowup ⟺ obstruction level n*` |
| `braids-and-knots/hecke-log-decomposition-table-data.ts` | `uses` | `prop:hecke-log-decomposition\\` |
| `nuclear-interactions/q-beta-form-a-n1-symbolic-table-data.ts` | `uses` | `prop:q-beta-form-a-n1-symbolic\\` |
| `mass-endomorphism/atomic-mass-gb-nf-interpretation.ts` | `uses` | `sec:atomic-braid-mass-foundations` |

`validate` exits 0 on all four, because the TS loader never sees them. Mode 3
leaves no trace at all, so the true corpus-wide count is unknown and cannot
be established by this method.

## What would fix it

The checkers should read the manifest the way the pipeline does — import it,
or parse TypeScript — rather than regex its text. Short of that:

- **strip comments before extracting** (`s.replace(/\/\/[^\n]*/g, '')` on the
  captured region) — kills modes 1 and 3;
- **anchor the field match** to a top-level property position rather than
  first-in-file — kills mode 2.

Both are patches on a parser that is guessing at a grammar it could simply
read. Recorded here rather than fixed: the fix belongs in
`folio-assistant`'s `qa-checkers-extended.ts`, and it wants its own change
with its own tests.

## Authoring rule until then

Inside a `uses[]` or `foreshadows[]` array, a comment may contain **no
closing square bracket and no quotation marks**. Both are already noted at
the two affected sites.
