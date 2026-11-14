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

### MIS-PARENTED — 8, real work on the wrong milestone

> **🛑 This said 12, and 4 of those were CORRECTLY parented. Corrected
> 2026-10-10, same session.** The claim rested on treating `qou-cdx1` as a
> C-excision milestone. **It is not** — its title is *"excise convention C,
> **adopt proton pin + colour weighting** (owner ruling 2026-08-15)"* and its
> body names three rulings: **R1** convention D canonical, **R2** proton pin
> canonical, **R3** `bring_color_weighted` canonical. So a q₀-pin bean (R2) or a
> colour-weight bean (R3) belongs there by design.
>
> Withdrawn from this list and left under `qou-cdx1`: **`qou-3f7a`**,
> **`qou-q0rf`**, **`qou-324i`** (all R2) and **`qou-o3ta`** (R3). The
> retraction is appended to each of the four beans.
>
> The paragraph that used to follow said the pin group "inherited one milestone
> because R1 and R2 landed in the same ruling" — exactly backwards. They share a
> milestone because the milestone was *scoped* to cover all three, deliberately.

The 8 that really were mis-parented are live, worth doing, and **about none of
R1, R2 or R3**:

| axis | beans | moved to |
|---|---|---|
| float64 / laundering | `qou-b7cf`, `qou-nmza`, `qou-eg4l` | `qou-9nnz` *(Precision hygiene: float64, dps, gates, witness currency)* |
| `atom_per_generator_volumes` shape change | `qou-47sx` | `qou-9nnz` |
| q-integer convention (Gaussian bracket vs classical) | `qou-b8vx`, `qou-gl58`, `qou-qint`, `qou-6p3b` | **`qou-4cu3`** *(new epic — see below)* |

**Enacted 2026-10-10.** `qou-cdx1`: 57 → **49 children**. The q-integer four
went to a new epic `qou-4cu3` because no existing parent covered that axis;
`qou-9nnz` was already the right home for the other four and now has 86.

The q-integer group is the instructive one: it shares the *word* "convention"
with R1 and nothing else. `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)` versus the classical
`(qⁿ − 1)/(q − 1)` is a different question from `z = q³/(q²+1)` versus
`√q/(q+1)`, and four beans sat under the Markov-parameter milestone on the
strength of the overlap.

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
- **A detector or exemption that is itself wrong** — `qou-4bq3`, `qou-jyqd`,
  `qou-okkz`. **🛑 All three were re-measured against `main` `ac111c1814` later
  the same day and the verdicts above are wrong in three different ways — see
  §11.**
- **Open mathematics downstream of D** — `qou-cxon`, `qou-egqr`, `qou-v7qj`,
  `qou-vuaj`, `qou-5h5x` (premise moved: `pyhecke.gram` is D and the registry's
  `intra_module_split_waivers` is empty — cheap to re-read), `qou-580o`,
  `qou-zmw4`.
- **Already appended separately** — `qou-wgta`, `qou-m7py`.

### What this changes about the milestone

`qou-cdx1` went **57 todo → 49 children** (6 completed on evidence, 8
re-parented). Of those 49, exactly one (`qou-pmkh`) names a still-actionable
file; the rest are recorded numbers, reader-facing text, detector defects, or
mathematics behind `qou-cds1` — plus the R2 (proton-pin) and R3 (colour-weight)
work the milestone covers by design.

New sibling epic: **`qou-4cu3`** — the q-integer convention axis, four children.

## 10. Draining the LIVE 23 — what landed, 2026-10-10

Six of the 23 worked. The pattern across all six is one thing, and it is not
drain work: **the C surface in code is clean, and what survives is a LABEL that
disagrees with the arithmetic beside it.** Each fix moved a label and no number,
and in four cases the producer re-run proved it — exit 0 with a one-line
semantic diff.

| bean | what was wrong | disposition |
|---|---|---|
| `qou-46ab` | 4 hardcoded C `tr_M(p)` refs; one live producer publishing C values as its *verification targets* | 4 → 0; producer scoped. Stays `todo` (recorded-constant class) |
| `qou-5pgl` | both "check first" candidates | **off the convention queue** — `3.74446989` is `m_e·8G` (no Markov parameter), `1.2999219630934102` is deprioritised by the bean's own table. Stays `todo` |
| `qou-u5z0` | **4 producers wrote convention C into their own witnesses as a STRING** | all 4 fixed, re-run, witnesses agree. Stays `todo` (original instance live) |
| `qou-enn6` | §2 of a reader-facing block asserted "suppressed", the word *its own line 27* names as a C signature | fixed; `qa-sweep` 120 criteria, 0 findings. Stays `todo` (3-column table) |
| `qou-zzwm` | the labelling fix of #6156 **itself went stale** and now asserted three published rows are unreproducible under the convention they are computed in | fixed at 3 sites; 0 numeric fields moved. Stays `todo` (`needs-owner` item is `qou-cds1`) |
| `qou-zf9n` | item 3: is the supergolden root a C artefact? | **SETTLED** — yes, by exact division in `ℚ[u]`. Items 1-2 stay open (owner) |

### The sharpest finding: a convention can survive as a STRING LITERAL

Four producers — `qbeta_symbolic_chain_alpha_b.py`,
`qbeta_alpha_eff_hoefsmit_symbolic_probe.py`,
`nuclear_quotient_jones_torus_link_probe.py`,
`rigid_monoidal_gap_invariance_check.py` — had a live `z = q³/(q²+1)` **and**
wrote `"z = 1/(sqrt(q) + 1/sqrt(q))"` into a witness field as text. Every
detector on this campaign is blind:

| detector | keys on | sees it? |
|---|---|---|
| shape audit | `z` assignment / return **expressions** | no |
| **value audit** | compiles the RHS and **evaluates** it | **no — the RHS is a `str`; it evaluates to itself, never to `0.4993…`** |
| witness staleness | `scriptHash` drift | no — 3 of 4 **matched**, so it reported them *fresh*, correctly: each witness faithfully recorded a producer that misdescribed itself |
| algebraic signature | the answer's factorisation | no — there is no number to factor |

The value audit is the campaign's evasion-proof detector precisely because it
evaluates rather than matches. **It is beaten by not being an expression at
all** — and this is the exact mirror of the recorded root of taxonomy rows
22/25/26 (*"the interesting text is assumed to be a `str` in the AST"*). There
the text was a `str` read as an expression; here it **is** a `str` and every
detector assumes it is an expression.

### `qou-zf9n` item 3, settled

`det = −(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z+qz+1)/q⁸` over `ℚ(q,z)`. Under
convention C (`q = u²`, `z_C = u/(u²+1)`):

```
numer(z_C − q) = −u(u³ + u − 1)      ÷ (u³+u−1)  →  quotient −u, remainder 0
```

exact in `ℚ[u]`. **The supergolden cubic is the numerator of `(z − q)`.** Under
D that factor is `−q/(q²+1)`, which has no positive root, and D's identical
det-vanishing comes from `((q²+1)z − q³) ≡ 0` instead — while under C *that*
factor vanishes on `u > 0` only at `u = 1`, the classical point. The two
frames' vanishings have **disjoint mechanisms** and `1/ψ` has no D-frame
counterpart. Scope (a): nothing elsewhere is excluded, but item 2's "look for a
supergolden rank drop in another D-frame object" is now looking for a *new*
result, not recovering an old one. Probe
`computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py`,
6/6, exit 0.

Deliberately **not** the float64 evaluation: `z_C − q` at a float64 root reads
`5.55e-17`, the floor of that arithmetic. Reporting it as agreement is what
AGENTS.md forbids; the probe records it only to say why it is not the evidence.

### Two findings from the PR #7318 merge, both verified here rather than relayed

| finding | verified | disposition |
|---|---|---|
| **`Q_MP` is a 50-digit cap under `OUTPUT_DPS = 60`** — 366 files import it; measured in `Fraction` (never mpmath, which reads `0.0` by construction): `Q_MP` 167 bits / rel err `2.0148085403388985e-50`, **outside** the `1e-60` width; `mpf(Q_50_DIGIT_STR)` 236 bits / `4.594107363943758e-72`, inside. Ratio `4.39e21`. | yes, independently | new bean **`qou-4pdh`**, parented under `qou-9nnz` (precision hygiene), **not** the convention milestone. Four framed options; no sweep taken |
| **`bean-append-merge.py` refused every bean conflict on current `main`** — its pure-append test ran over the whole file, and the 2026-10-04 reorg *inserts* `priority:`/`tags:`/`parent:` mid-frontmatter | yes — the old predicate reproduced returning `False` | **fixed**: the test now applies to the body only; `--selftest` asserts the insertion case resolves, a rewritten paragraph is **still refused**, and a branch-only `status:` change is warned not lost |

**A sibling agent's report is not a primary source.** Its diagnosis of the
merge tool — *"it compares ours-vs-theirs on the frontmatter"* — is not what the
code does; it already compares both sides against the base. The cause was the
frontmatter being in scope at all. Symptom real, remedy direction right,
mechanism wrong. The same discipline AGENTS.md states for source-file `## Status`
notes applies to another agent's report.

### Also observed, restored rather than committed

`precision-gates.sh` dirties three audit witnesses as a side effect. Two are
volatile-only. The third is a real drain —
**`mpf-mixed-arithmetic-audit` reads `candidates 7 → 5`, `files 4 → 3`**,
dropping `computations/binding_rotation_phase_lead.py` — which happened between
that witness's last commit and today's tree. All three `git checkout --`'d so
the commits stay on their subjects; recorded on `qou-zzwm` so the drain is not
lost. Whoever owns that audit should re-run and commit it on purpose.

`qa-sweep` writes `test/attestations/block-qa/` into the working tree; removed,
not committed — the derived QA corpus lives on the cat-harness `qa-reports`
branch (owner ruling 2026-10-04).

And `render-latex.ts` has **no CLI** at the pinned platform: invoking it
directly exits 0 having run nothing. A silent `exit 0` from it is not a render
check, and it nearly got recorded as one here.

**Three corrections of mine are recorded in this file**, all the same class — a
claim about an artifact made without reading that artifact's own primary text
closely enough:

| what I claimed | what is true | where |
|---|---|---|
| 66 paper sites unscoped | 23; the other 43 say *was/now/withdrawn/retracted* in C-vs-D tables | §4 |
| `qou-m7py` measurably satisfied | its headline bug is fixed, its owner items are not | §9, and on the bean |
| 12 beans mis-parented | 8; `qou-cdx1` covers R2 and R3 by design | §9 above |

## 11. The three "wrong-detector" beans, re-measured — and §9 got all three wrong

§9 grouped `qou-4bq3`, `qou-jyqd` and `qou-okkz` as LIVE under *"a detector or
exemption that is itself wrong"*, on the strength of their bodies. Re-measured
against `main` `ac111c1814`:

| bean | §9's verdict | measured | now |
|---|---|---|---|
| `qou-4bq3` | LIVE — regex over-blocks 8 of 24 B3 | **fixed 2026-08-25**, six weeks before the triage | `completed` |
| `qou-jyqd` | LIVE — content still cites `_deprecated` | **3 hits, all CITATIONS**; zero live dependencies | `todo`, re-scoped |
| `qou-okkz` | LIVE — 229 edges / 122 consumers | **8 edges / 8 consumers**, −29× | `todo`, 7 hand verdicts |

### `qou-4bq3` — the regex has not existed since 2026-08-25

`convention-c-producer-migrate.py:58` — the line the bean names — is not a
regex. Line 66 is `DELIBERATE = is_deliberate_c_name`, from
[`scripts/lib/convention_c_names.py`](../../scripts/lib/convention_c_names.py),
which replaced the `re.I` blob with three case-aware patterns and carries
`SELFTEST_MUST_NOT_MATCH` as a regression lock naming **all eight** false-B3
bases from the bean plus a ninth (`desc_tr_M`) the implementer found
independently. **51 selftest rows, 0 FAIL.**

Confirmed from the output side as well, which is the check that cannot be
fooled by reading the patterns: `convention-c-triage.py --json` gives **133
records, 119 `deliberate=True`**, and every reason string names a genuine
C-named target (`z_c`, `Z_C`, `zC`, `z_C_expr`, `z_C_num`, `z_C_of_t`, `_zC`,
`z_C_historical()`). **Not one `c_k`, `q_fac_n`, `qfac_3`, `desc_tr_M` or
`__doc__`.**

**How §9 got it wrong, because it is this document's own subject one level up.**
The triage read the bean's `## Not fixed on PR #5738` and `## Fix` sections and
did not grep for the symbol. `grep -rn 'is_deliberate_c_name' --include='*.py' .`
settles it in one command. §path-6 of AGENTS.md says a bean's status note is not
authoritative, and this is an instance — made *more* persuasive by the bean
being well-measured, since the file, the line number and the regex all went
stale together.

### `qou-jyqd` — the detector works; its COUNT is being mis-cited

3 hits on `main` (was 2), and all three are CITATIONS rather than dependencies:
`integer-lp-gluon.py` is named by a struck-through, explicitly-retracted
paragraph (`qou-jqjx` landed); `protium-witness.py` by a QA note confirming a
braid-word error; `transfer_matrix_symbolic.py` by a *"Readout corrected
2026-09-05"* banner. So the live dependency §9 feared is **gone**.

What *is* live is a mis-citation of this bean's own script.
[`TOOLS_report.md`](../audits/2026-10-04-workplan-and-migration/TOOLS_report.md)
gave T13 the evidence *"shows 0 content citations into `_deprecated` before the
move"*. It shows 3 — and it is the wrong audit either way, scanning only the
**139 of 568** deprecated producers *carrying a convention-C shape*. T13 breaks
on any reference: **27 tracked `folio/` files** name `fsh-guts/deprecated/computations`,
one of them structurally (`wedderburn-weight-canonical.ts` carries
`computation.script` into `_deprecated` with `status: "verified"`). Corrected in
that report; recorded on `qou-6u3n` and `qou-vfy1`.

### `qou-okkz` — the drain happened, and the number proves it

| | 2026-08-24 | 2026-10-10 |
|---|---:|---:|
| witnesses scanned | 2938 | **3728** (+27 %) |
| carrying the `z_C` fingerprint | 36 | **14** |
| foreign READ edges of C witnesses | **229 / 122** | **8 / 8** |
| CONTROL-ARM | 1 | **1** |

**The growing denominator is what makes this conclusive.** A falling count
against a growing corpus cannot be a sampling artifact — the artifacts went
away. The bean's standing *"228 unmeasured, NOT clear"* warning survives in kind
and collapses in scale: **7 hand verdicts**, now listed verbatim in the bean,
two of them on `hadron-knot-table.witness.json` — which is independently the
corpus's one remaining `Q0_FLIP`.

### A fourth finding: the FIXED detector's first measured blind spot

`convention-c-triage.py` reports `computations/qbeta/qbeta_ck_cache.py:140` as
`deliberate=False`, bucket *"computations — live producers"* — the canonical
`c_k` producer. **It is a false positive**, and an earlier chat line in this
session wrongly offered it as the one live residual. The site's D path prints
REFUSING TO RUN and exits 2; C is reachable only via
`--historical-convention-C`; it is adjudicated `completed` under `qou-ckwt`.

It is invisible because the target is a bare **`z`** — the deliberateness lives
in a `convention != "C"` raise, a parameter and a CLI flag, so **no name-keyed
check can see it however the patterns are widened.** Recorded as **row 52** of
the detector-blindness taxonomy, and in the direction the module's docstring
declares acceptable: this *under*-blocks (a false actionable costs one reading)
where the `re.I` bug *over*-blocked (a false deliberate hid a defect).


---

*Measured 2026-10-10 on `main` `77695711d`. Bean `qou-am5t`. Every count in this
file is reproducible by the commands in §8 — re-run them rather than quoting
this file, and if a number here disagrees with a fresh run, the fresh run is
right and this file is stale.*

---

## 12. Re-measured 2026-11-14 — §3a has drifted, and the obvious fix is the wrong one

§1 and §3a were measured on 2026-10-10 against `main` `77695711d`. Re-run today
against `main` `fee4ad592` with the command §8 names:

```bash
python3 scripts/convention-c-value-audit.py --root computations
```

| quantity | §3a, 2026-10-10 | measured 2026-11-14 | drift |
|---|---:|---:|---|
| confirmed C bindings | 143 | **148** | +5 |
| of which adjudicated in the ledger | 143 | 143 | — |
| **BLOCKING** (confirmed, unadjudicated) | **0** | **5** | **+5** |
| convention-D bindings | 576 | **597** | +21 |

**So §1's "`BLOCKING` 0" is stale**, and the audit now exits 1 rather than 0.

**The ledger did not break, and that was checked before anything was concluded.**
A failed ledger load would report all 148 as `BLOCKING`, not 5. 143 are still
read as adjudicated, so the five are new sites rather than a tooling artifact —
the internal consistency of the count is itself the evidence.

### The five

| # | site | binding | co-bound with `z_D` at the same site? |
|---|---|---|---|
| 1 | `computations/probes/frobenius_s_parity_convention_d_probe.py:64` | `zC = sp.sqrt(qs)/(qs+1)` | yes |
| 2 | `computations/probes/frobenius_s_parity_convention_d_probe.py:191` | `zc = mp.sqrt(Q0)/(Q0+1)` | yes |
| 3 | `computations/probes/v9_markov_trace_convention_d_probe.py:161` | `z_c = 1/(t0 + 1/t0)` | yes |
| 4 | `computations/qbeta/qbeta_cos_resummation_d_probe.py:92` | `z_C_historical = 1/(√q + 1/√q)` | yes |
| 5 | `computations/spectral_decomposition_qvalue_d.py:72` | `_z_convention_C_HISTORICAL()` → `√q/(q+1)` | no |

### 🛑 Do NOT drain these, and `qou-ztee` predicted this exact report

`qou-ztee` (`completed`, 2026-09-06) is the bean that *built* the adjudication
ledger, and it was written to forecast precisely this moment:

> as the C surface drains, the census converges to a **floor** consisting
> entirely of deliberate comparison arms. At that point the report reads
> *"N confirmed convention-C bindings, exit 1"* with every entry deliberate, and
> the obvious next move — *"drain the last N"* — **deletes measurements**.

Its ruling: **"If the count is wrong, fix the REPORT."** Restructuring a
comparison probe so the detector stops seeing it is AGENTS.md §1a audit-dodging —
a move whose only effect is to make an audit pass without changing anything real,
and exactly what this value-level detector was built to defeat.

Four of the five are **co-bound with `z_D` at the same site**, which `qou-ztee`
notes "is itself a value-level signal and needs no name or comment". That is
consistent with the comparison-arm reading and is **not sufficient to establish
it** — a filename or a variable spelled `z_C_historical` is a label, and this
repo's 58-row detector-blindness taxonomy is built almost entirely out of
mistaking a label for the thing. Each of the five needs its code read to
establish whether the C value reaches a reported result or only a printed
comparison.

### What is NOT yet established in this section

- **The triage of the five** — comparison arm (⇒ ledger row) vs genuine leak
  (⇒ migration) vs dead historical path. In progress; rows go in
  `docs/audits/convention-c-comparison-ledger.json`, keyed on path + target +
  a source-line hash, and `--propose-ledger` stubs candidates whose D arm is an
  inline binding.
- **Two of the five are already claimed by `in-progress` beans that say the
  opposite of "adjudicate"**: `qou-zuva` *"M6: redo q-beta-cos-resummation family
  in convention D"* (site 4) and `qou-wlnx` *"M6: redo spectral-decomposition-qvalue
  in convention D"* (site 5), both last touched 2026-10-10. If those sites are
  comparison arms, those two bean titles are wrong; if the beans are right, the
  sites are leaks. The two readings are mutually exclusive and this is the thing
  to settle first.
- `computations/probes/frobenius_s_parity_convention_d_probe.py` (sites 1–2) is
  named in **no bean at all** — measured, `grep -rl` over `beans/defs/` returns 0.
- **The other roots** (`tools`, the shape audit, the Lean audit, the three
  disagreeing witness detectors) are not re-measured in this section. §3b–§3e
  still carry their 2026-10-10 figures and should not be quoted as current.

### One registry drift noted in passing

§2 says the registry's `blocked_on_rederivation` holds **12** rows; the file
holds **13**. The registry's own `updated` field still reads 2026-09-05.
