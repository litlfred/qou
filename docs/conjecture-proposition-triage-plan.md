# Conjecture-vs-proposition triage plan

## Problem

138 content blocks have an **import/call mismatch**: they
`import { conjecture }` from builders but call `proposition()` or
`remark()` with a `prop:` / `rem:` label. This causes two CI failures:

1. **bun-validate**: "proposition is not defined" ReferenceError (the
   imported name doesn't match the called name), cascading into
   ~90 "Unresolved uses" downstream errors.
2. **witness-pipeline §3b gate**: 89 → 139 compliance gaps when the
   blocks are forced to load as propositions (a proposition downstream
   of a conjecture needs a §3b-cond banner).

## Root cause

The blocks were authored as conjectures (deliberate `import
{ conjecture }`, filenames like `*-conjecture.ts`, `open-problem`
tags) but had their **call + label** mis-converted to
`proposition()` / `prop:` at some point, leaving the import stale.
The earlier mechanical "make import match call" fix locked in the
wrong (proposition) reading.

## Triage (138 blocks)

| Class | Count | Signal | Fix |
|-------|-------|--------|-----|
| **Strong conjecture** | 83 | filename `*-conjecture` OR `open-problem`/`conjecture` tag | flip call→`conjecture()`, label→`conj:`, update all consumer `uses[]` from `prop:`→`conj:` |
| **Likely proposition** | 45 | no conjecture signal beyond stale import | fix import→`proposition` (call+label already correct) |
| **Remarks** | 10 | call=`remark()` | fix import→`remark` |

## Cascade

Flipping 83 blocks to `conj:` touches ~153 consumer references. Each
flip may also trigger **conjectural propagation**: a `theorem`/`prop`
that `uses[]` a now-conjecture must either become a conjecture itself
or carry a §3b-cond conditional-class banner (CLAUDE.md §3b/§3b-cond).

## Execution order (incremental, validate after each)

1. **Pilot: appendix-surreals** (~17 blocks, Millennium-problem
   conjectures, terminal — fewest consumers). Validate.
2. **fluid-dynamics + q-geometric-langlands** (NS + Langlands
   conjectures). Validate.
3. **Remaining strong-conjecture chapters**. Validate.
4. **Likely-proposition blocks** (import fix). Validate.
5. **Remarks** (import fix). Validate.
6. **§3b propagation pass**: any provable block now downstream of a
   flipped conjecture gets a banner or demotion. Re-run the §3b gate
   to 0.

Each step is its own commit; the §3b gate count is reported after
each to track progress toward 0.
