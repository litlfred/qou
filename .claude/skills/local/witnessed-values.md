---
name: witnessed-values
roles: [reader, collaborator, owner]
---

# Witnessed Values Skill

## Purpose

Eliminate **numerical drift** between paper prose and the canonical
witness JSON files.  Every literal value the paper quotes for a
substrate-derived quantity (`q_0`, `\hbar_q`, `Vol(4_1)`, binding
energies, etc.) must come from a single source of truth — the
canonical witness file — so updating a witness automatically
propagates to every place the value is mentioned.

## How it works

A typed registry in
[`content/values/registry.ts`](../../../content/values/registry.ts)
maps short names (`q_0`, `B_4He_AME_MeV`, …) to the canonical
witness file and dotted JSON path.  In `.md` content authors write a
directive instead of the literal:

```markdown
The substrate parameter is :val[q_0]{precision=6}, which gives
$\hbar_q^2 \approx :val[hbar_q_sq]$.
```

At build time the renderer (`content/pipeline/render-value.ts`) loads
each witness JSON, extracts the value, and substitutes it with the
requested precision and units.  If the witness file changes the
rendered prose changes automatically.

### Directive syntax

```
:val[<name>]                              # uses defaultPrecision, default format
:val[<name>]{precision=8}                 # override precision
:val[<name>]{format=scientific}           # 1.22 \times 10^{-9}
:val[<name>]{format=measured}             # value ± err   (requires errorEntry)
:val[<name>]{units=none}                  # suppress units suffix
```

Authors do **not** write `$…$` around `:val[…]` themselves — the
renderer does it.  The directive works equally well **inside** an
existing math context (the math-mode regex pass picks it up):

```markdown
$\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=8}$
```

### Why the `:val[…]` syntax (not Liquid `{{…}}`)

The `:directive[arg]{attrs}` form is CommonMark generic-directive
syntax, already used in this repo for `:defterm[…]` / `:refterm[…]`
(the Phase A glossary system, mandated by
`.github/copilot-instructions.md §11.0`).  Liquid `{{ q_0 }}` would
collide with LaTeX's heavy use of `{…}` braces (`\frac{a}{b}`,
`\hat{H}_q`, `\mathfrak{p}`).  Using `:val[…]` keeps the syntax
disjoint from TeX, reuses the existing `remark-directive` infra, and
mirrors the muscle memory authors already have for term references.

## Authoring rules

### When to use `:val[name]`

**Use it for every literal whose value is derived from `q_0` or
another substrate witness — in *every* block kind**, not just prose.

This rule applies uniformly to:

| Block kind                                              | Apply `:val[…]`? |
|--------------------------------------------------------|------------------|
| `definition`                                            | yes — definition body, illustrative numerals |
| `theorem`, `lemma`, `proposition`, `corollary`          | yes — statement body and any quoted bound |
| `conjecture`                                            | yes — even more important: the conjectured value must track its witness |
| `proof`                                                 | yes — including witness-citing proof steps |
| `example`                                               | yes — concrete numerical instantiations |
| `remark`                                                | yes — interpretive numerals |
| `prose`                                                 | yes — narrative literals |
| `algorithm` / pseudo-code listings (where present)      | yes — anywhere a substrate-derived literal appears |
| `table`                                                 | yes (manual) — codemod skips tables; author rewrites by hand |
| `equation`                                              | yes — directives are picked up inside `$…$` and display math |
| `simulator`                                             | n/a — no `.md` body |
| `diagram`                                               | n/a — TikZ source |

The codemod and validator are kind-agnostic: they walk every `.md`
file regardless of the wrapping block kind.  The migration already
applied for this PR rewrote propositions, proofs, examples, remarks,
and prose without distinction.

The "n/a" rows above (`simulator`, `diagram`) are not exceptions to
the rule — they simply have no `.md` body for the codemod to scan.
The rule still applies to any text those blocks emit through other
channels.

### Short literals below the match threshold

The codemod only auto-migrates literals carrying at least
`MATCH_PRECISION = 6` significant digits.  Literals like `0.09908`
(4 sig digits) or `0.90092` (5 sig digits) are below the threshold
and **must be migrated by hand** — either edit them in place to use
`:val[name]`, or first extend the literal to the required precision
and re-run the codemod.  This is by design: at lower precisions a
literal may agree with several registry canonicals (e.g. `1.109`
matches a tritium half-life *and* `q_0` to 4 digits), so the codemod
refuses to guess.

Concretely, the rule is:

- **A statement of a proposition or theorem** that bounds, equates,
  or quotes a substrate-derived value uses `:val[…]` for that value.
  Hard-coded literals in a theorem statement are a drift risk.
- **A conjecture body** that asserts a numerical equality must use
  `:val[…]` — the whole point of the directive is that if the
  conjecture is later refined, the witness changes once and every
  citation follows.
- **A proof block** quoting an intermediate numerical value
  (e.g. "evaluating at $q_0$ gives $\hbar_q^2 \approx 0.00982$")
  uses `:val[…]` for that value.
- **An algorithm or pseudo-code block** specifying a numerical
  threshold or a precomputed constant uses `:val[…]` for that
  constant — the algorithm's correctness depends on the value
  matching the witness.
- **An example** demonstrating a computation at the substrate
  uses `:val[…]` for the input and the result.

### When **not** to use `:val[name]`

- Pure exposition examples that are not asserting the actual numerical
  value (e.g. illustrating an algebraic identity with `q = 2`).
- Values that are not in the registry.  **First add a registry entry**
  (with `needsReview: true` if the canonical witness has not yet been
  pinned), then use `:val[name]`.
- Inside fenced ` ```tex ` derivation blocks — the codemod skips these
  because they typically show the literal as part of a derivation, not
  as a final asserted value.

### Adding a new entry

1. Identify the canonical witness JSON in
   `computations/*.witness.json`.
2. Pick a stable, snake-case `name` mirroring the symbol when possible
   (`q_0`, `m_n_MeV`, `inv_alpha`).
3. Set `defaultPrecision` no larger than the underlying witness
   precision.  For PrecisionScalar envelopes use the `dps` field;
   for plain decimal strings use the count of significant digits.
4. `units` is plain text rendered after the number (e.g. `MeV`,
   `fm`).  Use `null` for dimensionless values.
5. If the canonical witness is uncertain, set `needsReview: true`
   with a placeholder `witnessFile`/`witnessPath`.  The codemod
   skips such entries; the validator emits a warning.

## Validation

Five rules run as Phase 5 of `bun run validate`:

| Rule                       | Level | What it checks |
|---------------------------|-------|----------------|
| `val-registered`          | error | name appears in `WITNESSED_VALUES` |
| `val-resolves`            | error | witness file exists, dotted path resolves |
| `val-precision-bounded`   | error | requested precision ≤ source precision |
| `val-units-consistent`    | warn  | `units=plain` only when entry has units |
| `val-pending`             | warn  | `needsReview: true` entry was cited |
| `val-block-computation`   | warn  | block cites `:val[…]` but `computation:` is absent or refers to a different witness file |

The last advisory is **informational**: the renderer never blocks on
it.  It exists so the existing witness-staleness audit picks the
implicit dependency up — if a block's prose depends on a witness, it
should ideally declare that dependency in its `computation:` field.

## Codemod (mass migration)

`content/pipeline/codemod-val.ts` rewrites known literals inside math
contexts to their `:val[…]` equivalent.

```bash
# Dry run — print per-file diff summary
bun content/pipeline/codemod-val.ts content/quantum-observable-universe

# Apply
bun content/pipeline/codemod-val.ts content/quantum-observable-universe --write
```

Properties:

- **Math-only.**  Prose text and fenced ` ```tex ` blocks are not
  touched.  Tables are skipped (review manually first).
- **Idempotent.**  Existing `:val[…]` regions are carved out before
  replacement, and rendered numerals do not match the literal patterns
  again.
- **Verified-only.**  `needsReview` entries are never auto-applied.
- **Conservative match.**  A literal must agree with the witness value
  to at least `MATCH_PRECISION = 6` significant digits.  This is set
  high on purpose — at 4 digits, `1.109` was accidentally matching a
  tritium half-life and an `E_0 = 1.109\,\mathrm{MeV}` energy.

## Failure modes

The renderer surfaces every failure in the rendered PDF rather than
dropping content silently:

| Situation                  | Rendered output |
|----------------------------|-----------------|
| Unknown name               | `:val[bogus_name]` literal in the PDF |
| Witness file missing       | `:val[name]` literal |
| Path does not resolve      | `:val[name]` literal |
| `needsReview: true` entry  | `\textbf{[TODO name]}` |

If you see any of these in a rendered chapter, fix the registry or
backfill the canonical witness — never paper over the failure with a
hard-coded literal.

## Disjoint from tunable knobs (`EVOLVE-VALUE` fences)

`:val[…]` / `:leanval[…]` are for **derived / fixed** substrate values —
things a witness *computes* and the text must not drift from. The
complementary case — values that are *legitimately tunable* (a truncation
order, an exploratory coefficient) — is handled by the **`EVOLVE-VALUE`
fence** convention in
[`production-vs-exploratory-discipline.md`](production-vs-exploratory-discipline.md)
§"Tunable-knob fences". The two are **disjoint**: a value is either
witnessed-derived (`:val`) or fenced-tunable (`EVOLVE-VALUE`), never both.
A `:val`-witnessed literal sitting inside an *exploratory* fence is a
contradiction to resolve (it is being treated as both derived and free).

## Skill routing

When asked to write or revise paper content that quotes substrate-derived
literals, **first check the registry**.  If the value is registered,
use `:val[name]`.  If it should be registered but isn't, add it
(with `needsReview: true` if the witness is uncertain) and *then*
cite it.  Avoid hard-coded literals in newly-authored prose.

## Lean-side companion: `:leanval[...]` codemod

Numeric literals inside `.lean` source files use the same registry
via a sibling codemod
[`content/pipeline/codemod-leanval.ts`](../../../content/pipeline/codemod-leanval.ts).

**Tag syntax** (line-anchored, end-of-line comment):

```lean
volume     := 2.029883212819307  -- :leanval[Vol_4_1]{precision=15}
mostow_gap := 0.5                -- :leanval[mostow_gap_4_1]{precision=1}
show (0 : ℝ) < 2.029883212819307  -- :leanval[Vol_4_1]{precision=15}
```

The codemod scans all `.lean` files (skipping `.lake/`,
`lake-packages/`, `build/`), finds lines whose final end-of-line
comment starts `-- :leanval[NAME]`, and rewrites the **immediately
preceding decimal literal on the same line** to the witness value
at `entry.witnessPath`, formatted to either the per-occurrence
`{precision=N}` attribute or the registry default.

**Modes** (all from repo root):

```bash
bun run content/pipeline/codemod-leanval.ts            # dry-run, summarises diffs
bun run content/pipeline/codemod-leanval.ts --write    # apply rewrites
bun run content/pipeline/codemod-leanval.ts --check    # CI gate (exit 1 on drift)
```

**CI integration** — `witness-pipeline.yml` runs `--check` after
the witness producers, so a Lean literal that has drifted from its
witness fails CI before merge.  The fix is always the same:
`bun run content/pipeline/codemod-leanval.ts --write`.

**When to use the Lean tag** — any `.lean` field/literal that
quotes a numerical invariant tracked by a witness JSON
(hyperbolic volumes, q-pinning constants, AME masses, …).  Class
fields like `MostowRigidity.figureEight.volume` are the canonical
example.  Tactic-level literals inside `show` / `norm_num` proofs
may also be tagged so the proof and the field stay in sync.

**When *not* to use it** — opaque mathematical constants computed
inline by Lean tactics (e.g. `1/2`, `√2` produced by `decide` /
`norm_num`).  The codemod is a numerical-drift safety net, not a
generic literal rewriter.
