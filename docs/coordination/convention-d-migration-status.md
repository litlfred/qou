# Convention C → D migration: measured status, 2026-10-10

**Read this file first.** It exists because the migration's state was spread
across 487 beans, 16 scripts, a registry and an adjudication ledger, and the
question *"what is migrated and what is not"* had no single answer. Every number
below was measured on 2026-10-10 against `main` at `77695711d`, with the command
that produced it named, so it can be re-run rather than quoted.

Scope: the Markov parameter `z`. Convention **C** is `z = √q/(q+1) ≈ 0.4993203`
at the proton pin; convention **D** is `z = q³/(q²+1) ≈ 0.6126880`. D is
canonical by owner ruling (2026-08-15); C is excised.

---

## 1. The one-paragraph answer

**The migration is done except for one channel, and that channel is blocked on
one piece of mathematics, not on any remaining drain work.** Three of the four
trace channels are `agreed` with definitional and production convention both D.
The fourth, `qbeta-decay`, is `agreed-migration-pending`: its definition is D and
its production is still C. Exactly **one non-probe production file** in the repo
binds convention C — `computations/qbeta/qbeta_ck_cache.py:140`, the canonical
`c_k` ladder producer — and it cannot be migrated by substituting `z_D`, by a
sorry-free Lean result. Everything else that an audit still reports is one of:
an adjudicated comparison arm (143), a registry-declared site pending that same
re-derivation (12), a site that stays C permanently by design (1), or a
deliberately-named historical Lean definition (18).

---

## 2. Channel table — the authoritative statement

From `docs/coordination/trace-convention-registry.json`, which remains the
source of truth for *which convention a channel is in*:

| channel | definitional | production | status |
|---|---|---|---|
| `mass` | D | D | **agreed** |
| `binding` | D | D | **agreed** |
| `borromean-binding-single-pipeline` | D | D | **agreed** |
| `qbeta-decay` | D | **C** | **agreed-migration-pending** → `qou-cds1` |

All four `entry_points` rows are convention D.

The registry's own `updated` field reads **2026-09-05** — 35 days stale as of
this measurement. Its *content* is still correct; only its date is behind, which
is why this file states its own measurement date in every table.

---

## 3. Code — measured today

### 3a. Python, by VALUE (authoritative: evaluates the expression)

`python3 scripts/convention-c-value-audit.py --root <root>`

| root | confirmed C | adjudicated | **BLOCKING** | D bindings |
|---|---:|---:|---:|---:|
| `computations` | 143 | 143 | **0** | 576 |
| `tools` | 0 | — | **0** | 8 |
| `qou-mass` | 1 | 0 | 1 † | 14 |
| `folio` | 0 | — | **0** | 0 |
| `scripts` | 0 | — | **0** | 0 |

**`BLOCKING` was 6 this morning and is 0 now.** The six were adjudicated into
`docs/audits/convention-c-comparison-ledger.json` in this pass (137 → 143
entries) after reading each one. All six are two-convention comparison arms;
five bind `z_C` and `z_D` on adjacent lines, and the sixth
(`computations/audits/intra_ordering_value_fingerprint_audit.py:187`) is a
**value-keyed detector for which `z_C` is the reference value it detects with** —
its own fingerprint table enumerates the convention as one axis of the key, so
binding only `z_D` would delete four of its five rows. Rationales are in the
ledger per site; `--selftest` passes.

† The `qou-mass` hit is
`qou-mass/src/qou_mass/_internal/schur_principal_mpmath.py:121`, scope
`_wenzl_constants_convention_C_HISTORICAL` — the **generated mirror** of
`computations/schur_principal_mpmath.py:123`, which *is* adjudicated. It reads as
unadjudicated only because the ledger keys on `computations/` paths. Not a
defect, and **not to be hand-edited** (`scripts/sync-qou-mass-vendor.py` owns
that tree).

Also reported and **not** convention C: 6 sites of shape `1/(x + 1/x)` where `x`
is a *q*-variable, which is `1/[2]_q`; plus one site the audit lists as
`UNRESOLVED` because it cannot type the variable —
`qbeta_skein_normalisation_admissibility_robustness_probe.py:335`,
`kern = zj/(zj²+1)`. Resolved by reading: `zj` is a free `sympy` symbol
(declared at `:196`), so `kern` is the kernel function *generic in its argument*,
used to prove `1/2 − kern` has numerator `(zj−1)²`. That is a
convention-independent algebraic fact, not a `z_C` binding. Left out of the
ledger deliberately — the ledger's verdict vocabulary is `comparison`, and this
is `not-C`.

### 3b. Python, by SHAPE (`convention-c-producer-audit.py`)

```
  6 sites   probes / exploratory
  6 sites   computations/qbeta — BLOCKED on the qou-cds1 re-derivation
  1 site    computations/probes — BLOCKED on C by design
  1 site    computations — live producers        <-- qbeta_ck_cache.py:140
119 sites   deliberately C-named (labelled comparisons, not defects)
---
 13 ACTIONABLE (excludes blocked-by-design)
```

**The single most important line in this document is that `1 site … live
producers`.** It is `computations/qbeta/qbeta_ck_cache.py:140`,
`z = sqrt(q) / (1 + q)` — the canonical `c_k` producer, and the only non-probe
production file in the repo still on C. It is the `qbeta-decay` channel in §2,
and §5 is about why it is not drainable.

Keep the two Python audits separate when quoting. The value audit answers *"is
this expression convention C"* and over-counts nothing; the shape audit answers
*"does this site look like C"* and classifies by disposition. They disagree in
both directions by construction and neither supersedes the other.

### 3c. Rust / `tools/`

Measured by hand, because **no convention audit in the repo scans `.rs`** — the
value audit's `--root` reaches `tools/` but only walks `*.py` (8 D bindings, 0 C).

- The only convention-C `z` in Rust is `tools/hecke-engine/src/archive/v2.rs:205`
  — an `archive/` directory, historical by placement.
- `tools/hecke-engine/src/gram.rs` is convention D, and the `TR_M[5] = z³` bug
  that bean `qou-m7py` is about is **fixed**: `:138` records *"This entry was
  `z³` until 2026-08-15"*, and `:137` gives the corrected `TR_M[5] = h·z² + z`.

### 3d. Lean

`python3 scripts/lean-markov-convention-audit.py` — 3923 files, 243 sites.

| | defs | all sites |
|---|---:|---:|
| C-plain | 10 | 18 |
| C-sqrtvar | 13 | 18 |
| C-shape-unbound | 0 | 4 |
| **D** | **57** | **203** |

**23 convention-C definitions → 0 actionable, 23 deliberate.** Quote `defs`, not
`all`: a `q³/(q²+1)` inside a proof *mentions* a convention while one inside a
`def` body *defines* it, and conflating them inflates the count several-fold.
`deliberate` means the site announces itself — a `_legacy` name, an
`@[deprecated]`, or a docstring saying comparison/historical. That is evidence of
**intent, not a clean bill**: a deliberate C object can still be cited as though
it were D, which is a separate defect class and is what `qou-6moa` is about.

---

## 4. The paper — measured today

Scan: every `.md` and `.ts` under `folio/quantum-observable-universe`, matching
the name *convention C* or the shape `√q/(q+1)` / `1/(√q + 1/√q)`.

```
159 mentions over 89 files
  136  carry an explicit non-canonical marker (excised / was-now / retracted /
       withdrawn / C-frame / scoped / comparison table / "has not been re-derived")
   23  residual — candidates needing an eye
```

**The paper side is in good shape and it is scoped rather than corrected**, which
is the right disposition: a figure computed in the C frame is correct for the
frame it was produced in, and re-deriving it under D is separate work. Typical
live phrasing, from `observations/atom-mass-full-hecke.md`: *"The convention-C row
is retained because the results tabulated below were computed in it and have not
been recomputed under D."*

**My first classifier reported 66 unscoped and was wrong about essentially all of
them.** Reading the output, the sites it flagged say *was* / *now* / *gives* /
*withdrawn* / *excluded* / *retracted* and sit in two-column C-vs-D comparison
tables — all correctly scoped, in vocabulary the regex did not have. Broadening
the vocabulary from what those sites actually say took 66 → 23. Recorded because
the 66 would have read as a large live defect, and because this is the
detector-blindness class the corpus already catalogues 49 rows of: **the residual
below is a high-recall candidate list, not a defect list.**

Of the 23, the one worth a decision is
`predicted-spectra/spectrahedral-phase-collapse.md:3` — a block of kind
`theorem` whose statement opens **"Theorem (convention C)."** Its own §Scope says
*"this is a convention-C statement, and the reading does not survive convention
D"*, so it is honestly labelled; the question is whether a `theorem` block may
stand on an excised convention, which is bean `qou-zf9n` and is not mine to
settle. The rest are comparison tables, scope headers, a `tags: "convention-c"`
field, and corrections-of-corrections.

---

## 5. What actually blocks the last channel — and it is not drain work

`qou-cds1`: re-derive the `Q_β` `c_k` ladder under D. **This is not a `z`-swap**,
and that is proved rather than argued:
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame ladder
and the mass channel's three-row forcing mutually exclusive.

**It is also not blocked on the ladder phase `α` (`qou-pdix`), and the corpus
said it was in two places until 2026-09-14.** The ladder's N=2 factor is
`F_N2(α) = cos(α − u/2)·(1 − u²)`, so `cos ≤ 1` caps it at
`1 − u² = 0.99992745` for **every real α**. What the ladder must supply on the
ruled `z_D` base is `F_required = 1.75923699418` (order-zero `E₀`) or
`1.20016236389` (the dashboard-scored cell). Both exceed the cap, so **no value
of α unblocks it.** The two cells a cosine *can* reach — the retired `z = 1` cell
(0.998) and the augmentation `z = q` (0.889) — are exactly the two the 2026-09-08
ruling does not select.

So the live question is **what object supplies a factor above 1 at all** — about
the base or the assembly, not the phase. `qou-pdix` stays open (α is still
underived); only its priority changes.

Established twice independently, sorry-free (PRs #7355, #7262) and verified in
the merged audit
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1.

**Consequence for "restart the migration": there is no drain to restart.** The
remaining surface is one research question plus the accounting around it. An
agent sent to sweep convention-C sites will find comparison arms and
registry-declared pending rows, and "fixing" either is the shrink-the-number
failure the registry exists to prevent.

---

## 6. Why the tracker is unreadable — measured

This is the part the audits do not cover and the reason the state was hard to
find.

| | count |
|---|---:|
| beans mentioning a convention | **487** |
| of those, open (`todo` / `in-progress`) | **269** |
| children of the milestone `qou-cdx1`, all `todo` | **57** |
| lines in `qou-cds1` alone | **8593** |
| separate `convention-c-*` scripts in the repo | **16** |

Three specific defects:

1. **Recency is destroyed for half the tracker.** `updated_at` is
   `2026-10-04` on **2592 of 5513** beans (47 %) — the bean-reorg commit stamped
   them. Every open convention bean falls in that bucket, so *sorting them by
   recency orders them by nothing.* `created_at` survived and is the only usable
   time signal.

2. **The designated P0 ledger's own title is stale by ~30×.** `qou-wgta` is
   named, in `qou-cds2`, as *"the canonical ledger for the convention-C excision
   family"*, and its title reads **"174 py + 61 lean + tools/ Rust"**. Measured
   today: **0 blocking py, 0 actionable Lean, 0 live Rust outside `archive/`**. A
   reader who opens the canonical tracker gets the worst available answer.

3. **57 open children, 1 of which names a still-actionable file.** Intersecting
   every concrete path named in each child against today's live sets (6
   then-blocking + 12 blocked-on-rederivation + 18 Lean-C + 1 stays-C) gives:

   | bucket | n |
   |---|---:|
   | names a still-actionable file | **1** (`qou-pmkh`) |
   | names no path — claim-level, must be read | 15 |
   | every named file is clean | 41 |

   **The 41 are NOT closeable on this evidence and were not closed.** The
   intersection tests whether a bean's *files* still carry a C binding; most of
   these beans are about something else — published figures (`qou-zzwm`),
   witnesses (`qou-eea0`), detector blind spots (`qou-ng7j`, `qou-okkz`),
   q-integer conventions (`qou-gl58`, `qou-qint`), laundering (`qou-b7cf`). Those
   survive a clean code surface. Closing them off a path heuristic would be
   exactly *"shrinking the number without changing the corpus"*, which
   `blocked_on_rederivation_note` in the registry names as the thing it exists to
   prevent. The bucket is a **reading queue**, and each needs its own verdict
   with evidence.

---

## 7. Where to look, in order

1. **This file** — for state.
2. `docs/coordination/trace-convention-registry.{md,json}` — for which
   convention a channel is in, and the declared `blocked_on_rederivation` /
   `blocked_migrations` lists. Authoritative on conventions; `updated` is behind.
3. `docs/audits/convention-c-comparison-ledger.json` — for *why* a surviving C
   site is deliberate, one rationale per site. Current against `computations/`
   (zero stale entries).
4. `qou-cds1` — the one science blocker. Read §5 here first; the bean is 8593
   lines and its own framing of the blocker was wrong until 2026-09-14.
5. `docs/audits/2026-08-15-detector-blindness-taxonomy.md` — before trusting any
   count in any convention audit, including the ones above.

## 8. Reproducing every number here

```bash
python3 scripts/convention-c-value-audit.py                 # §3a, root=computations
python3 scripts/convention-c-value-audit.py --root tools    # §3a, other roots
python3 scripts/convention-c-value-audit.py --selftest
python3 scripts/convention-c-producer-audit.py              # §3b
python3 scripts/lean-markov-convention-audit.py             # §3d
python3 scripts/convention-c-witness-audit.py               # §3e below
```

### 3e. Witnesses

**Three witness detectors exist and they disagree. Say which you ran.**

| detector | result 2026-10-10 |
|---|---|
| `convention-c-witness-audit.py`, structural (nonzero `y_λ` on a 3+ row block) | **0** |
| `convention-c-witness-audit.py`, symbolic (half-integer power of `q` in a weight) | **1** — `computations/y-lambda-macdonald-telescope.witness.json`, 14 expressions |
| `computations/audits/y_lambda_convention_c_fingerprint_audit.py` | **1** — `computations/probes/sdp-o3-falsifier.witness.json`, `λ=(1,1,1) y=1.45e-17` |

The fingerprint hit is **not a convention-C weight**: under convention D
`y_(1³)` is exactly 0, so `1.45e-17` is a float64 zero — the DEAD_TOL
float64-noise sub-class that `qou-a6yh` already named. The structural detector's
0 and the fingerprint detector's 1 are the same tree seen through two
thresholds, and that disagreement is precisely the blind spot `qou-bvk7` is
about, so it is live evidence rather than a tooling nuisance.

Bean `qou-eea0` is titled *"regenerate all 84 convention-C witnesses"*; the live
figure is 1, and it is noise.

> **Measurement hazard — a live worktree inflates every repo-wide audit.** The
> fingerprint audit reported *2* files, one of which was
> `.claude/worktrees/agent-<id>/computations/probes/sdp-o3-falsifier.witness.json`
> — a dispatched agent's own copy of the other. Any audit that walks the repo
> root double-counts while a `isolation: "worktree"` agent is running. De-dupe
> on the path suffix, or quiesce the agent, before quoting a count.

---

## 9. The 41-bean reading queue — verdicts, 2026-10-10

§6 item 3 established that 41 of the 57 `qou-cdx1` children name only
already-clean files, and that this is a **reading queue, not a close list**.
Each of the 41 has now been read. Verdicts and evidence are appended to the
beans themselves; this is the index.

### CLOSED — 6, each on evidence

| bean | why it closed |
|---|---|
| `qou-ev2b` | `compound_shift_nf.py:321` is now `z = q0**3/(q0**2+1)` — D. Its claim that the module is C is measurably false. |
| `qou-pc7l` | **Fixed here.** Docstring `:8` *and* the runtime banner `:524` both labelled C while `z_num`/`z_sym` were D. Both corrected; producer exits 0 printing the canonical `0.612688`. |
| `qou-eea0` | "84 convention-C witnesses" → **1**, and that 1 is `y=1.45e-17`, a float64 zero, not a C weight. |
| `qou-a6yh` | Same measurement; the "mixed population of 25" is now the one noise entry this bean itself identified. |
| `qou-htsi` | Its scope item 1 — re-run the value and producer audits — was executed today. It found 6 unadjudicated sites and 3 stale trackers, so the owner's "be suspicious of closed gates based on compute" was right and is now discharged. |
| `qou-lt8x` | Superseded by method. It finds that a READ-SET blast radius missed 31 of 43 structurally-C witnesses; the value audit uses no read-set — it evaluates every binding — so the gap it names cannot exist under the current detector. |

### MIS-PARENTED — 12, real work on the wrong milestone

These are live and worth doing, and **none of them is about the Markov
parameter.** They are why the convention question looked 57 beans deep.

| axis | beans |
|---|---|
| float64 / laundering (`qou-840k` family) | `qou-b7cf`, `qou-nmza`, `qou-eg4l` |
| q-integer convention (Gaussian bracket vs classical) | `qou-b8vx`, `qou-gl58`, `qou-qint`, `qou-6p3b` |
| q₀ **pin** axis (ruling R2, not R1) | `qou-3f7a`, `qou-q0rf`, `qou-324i` |
| other migrations reached via this work | `qou-47sx` (`atom_per_generator_volumes` shape change), `qou-o3ta` (Gram null-vector science) |

The pin group is the instructive one: R1 (convention D) and R2 (proton pin)
landed in the **same 2026-08-15 ruling**, which is how they came to share a
milestone — but they are independent surfaces with independent audits, and
folding them together makes each look worse than it is.

**Re-parenting is proposed, not enacted.** It reshapes someone's milestone, and
the owner's call is whether these get a sibling milestone each or move under the
existing float64 / q-integer / pin trackers.

### LIVE — 23, and the reason they survive a clean code surface

Grouped by *what makes them invisible to a value-based detector*, which is the
useful axis:

- **A recorded NUMBER, not a binding** — `qou-46ab` (31 files carrying a C
  `tr_M(p)`; 4 producers hardcode it), `qou-5pgl` (8 files whose constants were
  *calibrated* before `hecke_core.z` flipped), `qou-u5z0` (a C dependency
  surviving as a derived identity), `qou-ng7j`, `qou-bvk7`. **This is the
  sharpest group:** a published constant cannot be re-spelled into visibility,
  and no detector that reads `z` can see one.
- **Reader-facing content** — `qou-enn6` (C weights in the three-channel H₃
  table), `qou-zzwm` (published accuracy figures), `qou-2cof`, `qou-34oo`,
  `qou-zf9n` (a `theorem` block stated in convention C).
- **A detector or exemption that is itself wrong** — `qou-4bq3` (the DELIBERATE
  regex matches `c_` inside ordinary identifiers, over-blocking 8 of 24),
  `qou-jyqd` (`_deprecated/` is skipped by design while content still cites it),
  `qou-okkz` (consumer-side control arms — and today's six new adjudications
  grew that population 137 → 143, so this got *more* load-bearing, not less).
- **Open mathematics downstream of D** — `qou-cxon`, `qou-egqr`, `qou-v7qj`,
  `qou-vuaj`, `qou-5h5x` (premise moved: `pyhecke.gram` is D and the registry's
  `intra_module_split_waivers` is empty — cheap to re-read), `qou-580o`,
  `qou-zmw4`.
- **Already appended separately** — `qou-wgta`, `qou-m7py`.

### What this changes about the milestone

`qou-cdx1` is now **51 todo / 6 completed** rather than 57 todo. If the 12
mis-parented beans move, the convention-excision milestone is **~39 children**,
of which one (`qou-pmkh`) names a still-actionable file and the rest are
recorded numbers, reader-facing text, detector defects, or mathematics behind
`qou-cds1`.

---

*Measured 2026-10-10 on `main` `77695711d`. Bean `qou-am5t`. Every count in this
file is reproducible by the commands in §8 — re-run them rather than quoting
this file, and if a number here disagrees with a fresh run, the fresh run is
right and this file is stale.*
