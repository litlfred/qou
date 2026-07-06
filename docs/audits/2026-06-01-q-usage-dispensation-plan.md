# q-usage audit — dispensation / resolution plan

**Source**: [`docs/audits/2026-06-01-q-usage-audit.witness.json`](./2026-06-01-q-usage-audit.witness.json)
**Sweep run**: 2026-06-01 (`q-usage-audit.ts` on `claude/gracious-cannon-Skhqb`)
**Watcher**: [`.claude/skills/local/q-usage-watcher.md`](../../.claude/skills/local/q-usage-watcher.md)

## Author preferences (drives every dispensation)

The repo owner stated, for resolving every q-usage finding, this
ladder of preferred fixes (apply the **earliest** that works for the
block at hand):

1. **Keep `q` symbolic / generic-`R` as long as possible.** Don't
   specialise to `ℝ` until the actual numerical evaluation. Don't
   assume characteristic. Don't assume archimedean.
2. **When an inequality on `q` is needed, prefer `|q| > 1` over
   `q > 1`** (resp. `|q| < 1` over `0 < q < 1`). The modulus form is
   valuation-theoretic and works over any normed / valued field
   (ℝ, ℂ, p-adic, …).
3. **Even more general: state in terms of a valuation `v(q)`.** If
   the underlying claim is about convergence of a formal power series,
   `v(q) > 0` / `v(q) < 0` is the cleanest form.
4. **Real-line inequality `q > 1` / `0 < q < 1` is reserved for the
   archimedean specialisation** — and the specialisation should live
   in a dedicated downstream block, not be silently baked into the
   categorical statement.
5. **Numerical pin `q = q_0 ≈ 1.10977859…` belongs in a separate
   substrate-evaluation block** in an archimedean chapter (typically
   `appendix-qvalues`, `observations`, or `predicted-spectra`), with
   the categorical block citing it via `interprets:` or `uses:`.

## Resolution ladder (apply in order; stop at the first that works)

When deciding how to fix a flagged block, walk this ladder top-to-
bottom and apply the **first** option that's tractable:

| Tier | Fix pattern | Example signature shift |
|------|-------------|--------------------------|
| **1. Pure formal** | Re-state over `Polynomial K[q]` / `K⟦q⟧` formal power series; never compute a square root | `q : K[X]` instead of `q : ℝ` |
| **2. Algebraic adjoin** | Replace `Real.sqrt q` with the splitting-field formal element. `K' := K[X]/(X² - q)` makes `q^{1/2}` an element of `K'`, no archimedean needed | `b : K[X]/(X² - q)` instead of `Real.sqrt q` |
| **3. Normed / valued field** | `[NormedField K]` + `‖q‖ > 1` ; or `[Valued K Γ]` + `v(q) < 0`. Works for ℝ, ℂ, p-adic, formal-power-series rings | `(hq : ‖q‖ > 1)` instead of `(hq : 1 < q)` |
| **4. Generic ordered field** | `[LinearOrderedField K]` + `0 < q`. Drops p-adic but keeps generic char-0 ordered | `{K : Type*} [LinearOrderedField K] (q : K) (hq : 0 < q)` |
| **5. Real specialisation** | `q : ℝ, 0 < q` — most specific. Only use when the *purpose* of the block is the archimedean evaluation. The block's `.ts` must carry `wall: "archimedean"` or `archimedean-specialisation` tag | `noncomputable def f (q : ℝ) (hq : 0 < q) := …` |
| **6. Fixed `q_0` numerical** | `q = q_0 ≈ 1.10977859…`. Only inside a dedicated substrate-evaluation block in an archimedean chapter | only in `<block>-substrate-evaluation.md` in `appendix-qvalues` |

## Findings — by criterion + dispensation

Aggregate counts from the witness:

| Criterion | Fails | Warns | Dispensation policy |
|-----------|-------|-------|---------------------|
| `q-usage-archimedean-in-categorical-chapter` | 16 | 0 | Refactor per ladder. Most cases → tier 2 or 3. |
| `q-usage-fixed-q0-leak` | 11 | 0 | Split the block: categorical statement stays generic; substrate-evaluation moves to archimedean chapter. |
| `q-usage-positivity-implicit` | 0 | 12 | Replace `Real.sqrt q` per ladder (tier 2 preferred). |
| `q-usage-modulus-vs-real-mismatch` | 0 | 3 | Mechanical rewrite `q > 1 → |q| > 1`. |
| `q-usage-root-of-unity-undeclared` | 0 | 19 | Add explicit `q = ζ_N` / "primitive N-th root" declaration in prose. |
| `q-usage-narrative-chapter-mismatch` | 0 | 498 | Mostly secondary signals — discharged by the per-regime fixes above. Re-sweep after the per-regime backlog drains. |

### A. `q-usage-modulus-vs-real-mismatch` — apply mechanically (3 fails)

Author has standing approval for the mechanical rewrite per
preference #2. Targets:

1. `information-theory/prop:q-exponential-taylor`
   ([`md:45-46`](../../content/quantum-observable-universe/information-theory/q-exponential-taylor.md))
   — `0 < q < 1` table row and `q > 1` table row are formal-power-
   series convergence regimes for the q-exponential. Mechanical
   rewrite to `|q| < 1` / `|q| > 1`.
2. `mass-theory/prop:full-pole-structure-mass-trace`
   ([`md:84,97`](../../content/quantum-observable-universe/mass-theory/full-pole-structure-mass-trace.md))
   — "regime `q > 1`" → "regime `|q| > 1`" (formal-pole context;
   the pole structure is a statement about the modulus regime).
3. `particle-interactions/thm:groebner-shirshov-energy`
   ([`md:52`](../../content/quantum-observable-universe/particle-interactions/groebner-shirshov-energy.md))
   — "(since `q > 1` ensures `q - q⁻¹ > 0`)". This one is the
   one exception: the parenthetical genuinely uses a real-line
   ordering to deduce sign-of-difference. Options:
   - Replace with: "since `v(q) < 0` (equivalently `|q| > 1`),
     `q − q⁻¹` is a unit and its leading term has positive
     `v`-degree" — works generically.
   - OR keep `q > 1` and add a "(specialising to ℝ; substrate
     value `q_0 ≈ 1.1098 > 1`)" footnote.

### B. `q-usage-root-of-unity-undeclared` — add declaration (19 warns)

Apply preference #1 in declared form: every Lusztig / Kashiwara /
fusion-category / divided-power construction in a non-`q-geometric-
langlands` chapter prefixes the relevant section with:

> Throughout this block, $q$ is a primitive $N$-th root of unity
> (specifically $q = \zeta_N := e^{2\pi i / N}$, with $N$ as
> specified per construction).

For each block, decide:

1. **Add declaration in `.md`** (most cases) — author-auto-discharge.
2. **Hoist to `q-geometric-langlands` chapter** (if the construction
   doesn't depend on braids-and-knots scaffolding) — sometimes a
   better fit.
3. **Banner-tag** as "fibre-level construction, archimedean
   evaluation lives elsewhere" — for the few cases where the block
   is the structural definition + the root-of-unity is just one
   special evaluation.

The 19 warns concentrate in `braids-and-knots`, `appendix-surreals`,
and `q-geometric-langlands` (which is exempt — those warns indicate
the detector regex needs tightening). See witness for the per-block
list.

### C. `q-usage-positivity-implicit` — refactor `Real.sqrt q` (12 warns)

These are the explicit user concern ("Real.sqrt q without 0 < q
hypothesis"). Apply the ladder, preferring tier 2 (algebraic adjoin).

**Pattern 1** — `markovZ q := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)`
(appears in `markov-axioms-primitive`, `braid-group-n-strand`,
`hoefsmit-V21-cos-symmetrization`, `q-beta-spectral-bridge`):

The expression equals `Real.sqrt q / (q + 1)`. Generic form:

```lean
-- Tier 2 (preferred): adjoin u with u² = q, then markovZ = u / (u² + 1)
variable {R : Type*} [CommRing R] (q : R)
noncomputable def markovZ' : Polynomial R := Polynomial.X / (Polynomial.X^2 + 1)
-- evaluated at any u : R' with u² = q gives markovZ
```

Or in the absence of a generic adjoinment, use a normed-field
formulation:

```lean
-- Tier 3
variable {K : Type*} [NormedField K] (q : K) (hq : ‖q‖ ≥ 1)
noncomputable def markovZ (q : K) : K := …
```

**Pattern 2** — `Hoefsmit matrix entries` with `Real.sqrt`
(`hoefsmit-V21-cos-symmetrization`, `chi-v21-hoefsmit-matrix-
derivation`): the Hoefsmit matrix has entries of the form
`Real.sqrt (b_sq q)` where `b_sq` is a polynomial in `q`. Replace
with the formal splitting-field element:

```lean
-- Tier 2
variable {R : Type*} [CommRing R] (q : R)
noncomputable def hoefsmitMatrix (b : R) (h : b^2 = b_sq q) :
    Matrix (Fin 2) (Fin 2) R := !![d1 q, b; b, d2 q]
-- Concrete value: instantiate (b := Real.sqrt (b_sq q)) only at
-- numerical evaluation time.
```

**Pattern 3** — `algebraic-geometric-dilog-equivalence`,
`dilogarithm-archimedean-limit`: these use `Real.log` on
`partialProductLocal q`. The block kind / chapter is `mass-theory`
(archimedean — actually allowed), so these may be legitimate
archimedean specialisations. Decision: add the missing
`(hq : 0 < q)` hypothesis (tier 5 — they're in the right chapter,
just need the explicit positivity declaration).

**Pattern 4** — `toffoli-lp-stability` — Lean file explicitly
threads `0 < q + Real.sqrt q - 1`. The hypothesis pattern doesn't
match my heuristic; add `hq : 0 < q` to the surrounding theorem
signature.

**Pattern 5** — `qbeta-c-k-closed-forms`, `ck-extraction-from-
algebraic-rules`: `Real.sqrt (q^4 + q^2 + 1) / (q^2 + 1)`. The
radicand `q^4 + q^2 + 1` is always `> 0` for real `q`, but the
generic form is:

```lean
-- Tier 2
let K' := AdjoinRoot (Polynomial.X^2 - (Polynomial.X^4 + Polynomial.X^2 + 1))
-- in K', the root exists by construction; no Real.sqrt
```

### D. `q-usage-archimedean-in-categorical-chapter` (16 fails)

Two sub-classes:

**D1 — MeV / CODATA / ppm references in `.md`** (~10 cases —
`proton-mass-substrate-identity`, `meson-em-sinh-closed-form`,
`meson-qcg-fusion-identity`, `habiro-precision-ladder-equivalence`,
`reading-a-conditional-linking-weight`):

These blocks bundle a categorical-statement-of-identity with a
numerical-comparison-at-q_0. Resolution: **split**.

- Keep the categorical block (e.g.
  `prop:proton-mass-substrate-identity`) with the algebraic identity
  for generic `q`; remove all CODATA / ppm references.
- Create a sibling
  `<block>-substrate-evaluation.md` in `appendix-qvalues` (or
  `observations`) with the numerical comparison at `q_0`. The
  evaluation block `uses: [original-block]`.

**D2 — `Real.*` / `linarith` / `positivity` in `.lean`** (~6 cases):

Same resolution as §C above — refactor per the ladder. These
overlap with the positivity-implicit warns.

### E. `q-usage-fixed-q0-leak` (11 fails)

Concentrate in `appendix-surreals` (8) and `braids-and-knots` (3,
overlapping D1).

**E1 — `appendix-surreals/`** (`diophantine-birthday`,
`on-p-modular-hecke`, `wenzl-positivity-implies-substrate-positivity`,
`standard-part-functor`, `algebraic-core-survives`,
`analytic-obstructions`, `collatz-hausdorff-comparison`,
`infinitesimal-frobenius`, `casimir-epsilon-vacuum`):

The surreal appendix is the "numbers-after-the-numbers" companion
to the substrate-q_0 narrative — it intrinsically discusses how
the substrate value sits relative to the surreal number system.
The chapter's expected-regime profile should probably include
`fixed-q0`. **Policy decision A — see "Policy decisions" below.**

**E2 — `braids-and-knots/`** — same as D1.

### F. `q-usage-narrative-chapter-mismatch` (498 warns)

Drop. This criterion fires when the detected regime vector is
**disjoint** from the chapter's expected set — a weak signal that
mostly overlaps with B / C / D / E above. Re-sweep after the
per-regime backlog drains and most will disappear.

The remaining ones are signal worth investigating, but they're
secondary to the per-regime checks. Defer.

## Policy decisions (need owner approval)

### Policy A — surreal appendix expected profile

The `appendix-surreals` chapter expects `[generic-R, na, symbolic]`
but most of its blocks discuss the substrate `q_0` relative to the
surreal number system (which is intrinsically substrate-pinned).

1. **Expand expected profile** to include `fixed-q0` for
   `appendix-surreals`. Reduces the 8 fixed-q0-leak fails to 0,
   no narrative changes needed.
2. **Keep narrow profile**; treat the 8 blocks as `wontfix-acknowledged`
   (Class-A in the canonical-watcher sense). Each block adds a
   `wall: "archimedean"` tag to its `.ts`.
3. **Refactor the appendix** to be archimedean-only, move the
   generic-R surreals to `lifting-and-descent`.

**Recommended: 1** (the appendix is by nature substrate-q_0-relative).

### Policy B — Hoefsmit `Real.sqrt` refactor

For the ~4 Hoefsmit / Markov `Real.sqrt q` cases, the formal-adjoin
form (tier 2) is the most-generic fix but it's the heaviest
refactor (changes the Hoefsmit matrix module's API).

1. **Apply tier 2** (formal adjoin) — most-generic, but ~50 LOC
   API change + downstream callsites need updating.
2. **Apply tier 3** (normed-field) — keeps API but parameterises
   on `[NormedField K]` instead of `ℝ`. Works for ℂ + p-adic.
3. **Apply tier 5** (real specialisation) — just add the missing
   `hq : 0 < q` hypothesis, keep the `ℝ` signature, tag the block
   `wall: "archimedean"`. Cheapest, least general.

**Recommended: 3** — the Hoefsmit matrix IS a representation-
theory tool whose entries are constructed via square-root
extraction; doing it formally introduces a wrapper layer that
doesn't pay for itself for the current paper's scope.
**Alternative: 2** if a sibling agent is willing to take the
normed-field rewrite.

### Policy C — MeV/CODATA split for the 5 `braids-and-knots` D1 blocks

Splitting each block into `<block>` (categorical) + `<block>-
substrate-evaluation` (archimedean) is a ~5-block × 2-files = 10
new files + cross-link rewires.

1. **Split now**, all 5 blocks, this PR (large but coherent
   refactor).
2. **Split incrementally** — open follow-up PRs per block,
   prioritised by downstream-dependent count.
3. **Banner-tag the existing blocks** with `wall:
   "archimedean-specialisation"` and defer the split.

**Recommended: 2** — the proton-mass and meson-em blocks are
high-value to split first; the others can ride later branches.

## Per-finding action table (top blocks)

| Block | Criterion(s) | Recommended action |
|-------|--------------|--------------------|
| `braids-and-knots/prop:proton-mass-substrate-identity` | fixed-q0-leak + archimedean-in-cat | Split (Policy C/1) — high-priority |
| `braids-and-knots/prop:meson-em-sinh-closed-form` | fixed-q0-leak + archimedean-in-cat | Split (Policy C/1) — high-priority |
| `braids-and-knots/prop:meson-qcg-fusion-identity` | archimedean-in-cat | Drop the at-q_0 ppm reference; keep generic identity |
| `braids-and-knots/prop:habiro-precision-ladder-equivalence` | archimedean-in-cat | Banner-tag (Policy C/3) — it's the ladder block by purpose |
| `braids-and-knots/rem:braid-group-n-strand` | archimedean-in-cat + positivity-implicit | Tier 3 (`NormedField`) on `markovZ`, keep block in chapter |
| `braids-and-knots/rem:markov-axioms-primitive` | archimedean-in-cat + positivity-implicit | Tier 3 — same as above |
| `braids-and-knots/prop:lagrange-resolvent-transform` | archimedean-in-cat | False-positive — `Real.sqrt 5` is a constant, not `Real.sqrt q`. Add explicit comment + suppress |
| `braids-and-knots/prop:knot-eigenbasis-complete` | archimedean-in-cat | `positivity` tactic is OK over `R_q` ordered-ring — possibly false-positive; verify |
| `lifting-and-descent/cor:quantum-dilogarithm` | archimedean-in-cat | Investigate — `linarith` in lifting-and-descent is unusual; check if the lemma is actually generic |
| `lifting-and-descent/ex:vacuum-state-su2` | fixed-q0-leak | Split (Policy C/1) — numerical evaluation block |
| `mass-theory/prop:hoefsmit-V21-cos-symmetrization` | positivity-implicit | Add `(hq : 0 < q)` + tier 3 wrap (Policy B/3) |
| `mass-endomorphism/rem:chi-v21-hoefsmit-matrix-derivation` | positivity-implicit | Same as above |

## Sweep + re-audit protocol

After applying A/B/C/D/E from above:

1. Re-run `bun run content/pipeline/q-usage-audit.ts`.
2. Per-block sidecars regenerate; the global witness updates.
3. Findings that survive land in the watcher queue
   (`todos/q-usage-watcher-queue.json`).
4. Open a follow-up PR per the `claude/iw-q-usage-<theme>` branch
   pattern (per `integration-watcher.md §5j`) when batching the
   per-criterion refactors.

## Cross-references

- Watcher skill: [`.claude/skills/local/q-usage-watcher.md`](../../.claude/skills/local/q-usage-watcher.md)
- Detector source: [`content/pipeline/qa-checkers-q-usage.ts`](../../content/pipeline/qa-checkers-q-usage.ts)
- CLI: [`content/pipeline/q-usage-audit.ts`](../../content/pipeline/q-usage-audit.ts)
- Witness: [`2026-06-01-q-usage-audit.witness.json`](./2026-06-01-q-usage-audit.witness.json)
- Base-ring convention (AGENTS.md §7c): [`AGENTS.md`](../../AGENTS.md)
