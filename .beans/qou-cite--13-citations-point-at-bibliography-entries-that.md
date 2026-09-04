
## Re-measured 2026-09-04 — 13 keys is now 4, and the gate's status is different

**Do not act on the table above; it is stale in both directions.** Re-measured by
**importing** `content/schema/references.ts` (827 entries) rather than grepping
for a spelling, which is the method this bean's own successor comment in
`scripts/run-validate.ts` recommends:

| key | status now | citing blocks left |
|---|---|---|
| `feigin-hashizume2009` | **PRESENT** | — |
| `dimofte-gaiotto-gukov2014` | **PRESENT** | — |
| `terashima-yamazaki2011` | **PRESENT** | — |
| `kashaev-tirkkonen2014` | **PRESENT** | — |
| `macdonald1971` | **PRESENT** | — |
| `lusztig1989` | **PRESENT** | — |
| `frenkel-reshetikhin2002` | absent, **and no longer cited** | 0 |
| `champanerkar-kofman-mullen2008` | absent — **fixed in this branch** | 0 |
| `faddeev1996` | absent | 2 |
| `bokut1978` | absent | 1 |
| `manuscript` | absent — but see below | 2 |

**The six were resolved CORRECTLY, and that is worth recording**, because this
bean's central warning was that they must not be collapsed into their
near-misses. They were not: `macdonald1971` is *Spherical Functions on a Group
of p-adic Type* and `lusztig1989` is *Modular representations and quantum
groups* — the two distinct works this bean names, added as themselves rather
than repointed at `macdonald1995` / `lusztig1990`.

### `champanerkar-kofman-mullen2008` needed no research either — it was already adjudicated

`references.ts:5251` carries a note on `champanerkar2003`: it was added
2026-06-28 to correct *"the phantom key 'champanerkar-kofman-mullen2008' … no
such Champanerkar–Kofman–Mullen 2008 A-polynomial paper exists (the 2008
Champanerkar–Kofman paper is on Khovanov homology)"*. That drain fixed one of
the two citing blocks; `q-zero-stokes-region-identification`, which `uses` the
block that was fixed, kept the dead key. Repointed here.

### The gate: it is wired, and it is deliberately `--strict`-only

This bean says the check "has never run". It now runs — **under `--strict`**.
`scripts/run-validate.ts` (`9f1322dd81f`, 2026-08-30) imports and calls
`configureReferenceRegistry`, inside `if (strict)`. A default run still prints
the `ℹ no reference registry configured` line and reports `✓ Valid — 14
issue(s)`; that is the documented choice, not a regression — enabling it
unconditionally would move the default from `Valid — 14` to `Invalid — 23` on an
untriaged backlog.

**So a clean default `run-validate` is NOT evidence the citations are clean.**
Use `--strict` when you want the citation gate.

### 🟡 `manuscript` — a DECISION, and AGENTS.md §1 contradicts itself

Not a typo and not research. AGENTS.md §1 says two things that cannot both hold:

> The `[key]` must match an entry in `content/schema/references.ts` exactly.
> If no published reference exists, use `[manuscript]` …

`manuscript` is **not** an entry — it is a CSL *type* name. So every site
following the second sentence violates the first. Measured: **4436 Lean
`-- Ref:` sites** use `[manuscript]`, plus the 2 content blocks here
(`categorical-proton`, `categorical-proton-properties`; neither `.md` contains
any `\cite{}`, so the key is hand-set metadata, not extracted from prose).

**The work it means IS held**, as `leitner2026` — *"Quantum Observable
Universe", Leitner, Fred, 2026, `type: "manuscript"`*, i.e. this paper.

Two ways to close it, and they differ in blast radius:

- **(a) Add an alias entry `manuscript` → the same work.** One bibliography
  entry. Makes §1 self-consistent and makes all 4438 sites resolve at once.
  Risk: a duplicate CSL entry for one work, which the duplicate-detection and
  BibTeX export would then see twice.
- **(b) Re-key the 2 content blocks to `leitner2026`, leave the Lean convention
  alone.** Two lines. `cites-resolve` does not validate Lean `-- Ref:`, so the
  4436 are untouched either way — but §1 stays self-contradictory and the next
  author to put `manuscript` in a `cites[]` reintroduces the defect.

**Default if nobody decides: nothing changes** — the two blocks keep a key that
cannot resolve, and the gate reports them under `--strict` only. That is safe;
no reader-visible claim is broken, because neither block's prose cites anything.

**My judgement, not a finding: (a).** It is smaller, it fixes the rule rather
than two instances of it, and the "duplicate entry" objection is weak for a
self-citation. But it edits the bibliography, so it is the owner's call and is
deliberately not done here.

### Still needing real research (2 keys, 3 blocks)

- **`faddeev1996`** — `inter-nucleon-channel-color-tube`,
  `pachner-pentagon-borromean`. Held Faddeev entries are `faddeev1994`,
  `faddeev1995`, `faddeev_kashaev1994`, `faddeev-kashaev-volkov2000`. The
  library holds no Faddeev 1996 either (INDEX scan: the Faddeev hits are
  Skyrme–Faddeev soliton papers and quantum-dilogarithm work by others).
- **`bokut1978`** — `phi-q-tower-algebraic-stratification`. Held Bokut entries
  are `bokut2001`, `bokut2005`, `bokutchen2011/2014/2015pbw`. Library holds
  `arxiv-0910.0096v1` (*Gröbner–Shirshov bases for Coxeter groups*), which
  *cites* Bokut–Shiao but is not the 1978 work.

Both still need checking against what the citing block claims. The bean's
standing warning holds for these two: repointing a citation at a different paper
is worse than a broken link.
