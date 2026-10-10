---
# qou-2cz1
title: Four local imports in computations/ name a module-level name that does not exist -- two producers cannot be imported, and scriptHash reports them IN SYNC
status: todo
type: task
priority: high
created_at: 2026-10-10T07:57:44Z
updated_at: 2026-10-10T12:10:14Z
parent: qou-5vkl
---

Found 2026-10-10 (PR #7546) while unblocking `qou-3kni`'s producer half. **Nothing
in `computations/` was edited** — see "Why no fix is proposed" below; it is not
caution, it is that three of the four have no mechanical answer.

## The finding

Four `from <local-module> import <name>` bindings in `computations/` name a
module-level name that **does not exist**. Two break the script at import time;
two sit inside a function and fire only when that path is taken.

| site | imports | from | status of the name |
|---|---|---|---|
| `snappy_cusp_seeding.py:47` | `IM_PERTURBATION` | `q_pochhammer_seed` | renamed to `IM_PERTURBATION_STR` (NO-FLOAT64, 2026-09-13) |
| `probes/qbeta_g3_annihilator_certification.py:52` | `tet_norm` | `probes/qbeta_g3_fourone_index_assembly` | module defines `tet_abs`; rename plausible, **unconfirmed** |
| `probes/qbeta_g3_annihilator_certification.py:52` | `_dense_mul` | same | **no candidate of any name** |
| `atom_braid_active_partitions.py:128` | `hook_length_dim_lambda` | `hecke/hecke_characters` | absent; no `__getattr__` |

`series_str`, imported on the same line as the two `qbeta_g3` names, **does**
exist (line 152) — so that import statement is half-valid, which is why the file
reads as maintained.

## Why no detector fires, and this is the reusable half

**The consumer's own file hash does not change.** `snappy_cusp_seeding.py`'s
`scriptHash` is `f4733c216049` and its witness records `f4733c216049` — **IN
SYNC** — with `computedAt 2026-08-28`, three weeks before the dependency was
renamed. So the witness claims currency with a producer that **cannot be
imported**, and every `scriptHash`-keyed staleness path reports it healthy.

This is `AGENTS.md`'s **import-cone drift** class, but one step worse than the
case that class was written for. There, a byte-stable producer's *number* moves
because a numeric module in its cone changed. Here the cone change does not move
a number — it stops the producer running at all, which no staleness metric can
express.

`witness_import_cone_staleness_audit.py` does **not** catch it. Run here, its
output is dominated by one mover (`substrate/experimental_constants.py`,
**2135** witnesses) and ranks by *"a cone module changed more recently than the
witness"* — a recency heuristic. It never asks whether the import resolves, and
`snappy_cusp_seeding` does not appear in its report.

**And `import snappy` fails first**, which is how this stayed hidden: every
container that tried to run the script died at line 42 before reaching line 47.
`qou-3kni` recorded the `ModuleNotFoundError` and stopped there, reasonably. The
second, deeper breakage is only visible once SnapPy is installed — and it is
(see below).

## The audit, and what it cost to calibrate

[`computations/audits/local_import_resolution_audit.py`](computations/audits/local_import_resolution_audit.py).
Pure AST: nothing is imported or executed, so **no producer writes a witness**
while it runs — which matters, because `AGENTS.md` records that producers write
*sibling* witnesses and a sweep that imports them leaves a dirty tree reading as
real work. Exits 1 when anything is unresolved, so it can be a gate.
`--selftest` asserts the one known true positive is found and four known-good
imports are not, and **fails** rather than passing quietly.

**The first version reported 34 and 30 were false positives.** Both causes are
blind spots worth recording, because both made the audit *over*-report, and an
over-reporting audit is abandoned as noise:

1. **Star re-export shims out of the tree.** `_precision` and `witness_base`
   are back-compat shims re-exporting from `qou_substrate.*`, so an
   enumeration of their own AST finds neither `set_compute_dps` nor
   `WitnessBuilder`. Now: a module whose exports cannot be fully enumerated is
   **UNDECIDABLE and skipped**, never guessed at. 8 modules.
2. **Ambiguous stems.** `witness_provenance_audit.py` exists in BOTH
   `computations/` and `computations/audits/`, and `setdefault` over
   `sorted()` silently read the wrong one — 7 false positives against a module
   whose names (`written_filenames:224`, `builder_names:270`) are plainly
   there. Which file a bare-name import resolves to depends on `sys.path`
   order, so it is genuinely undecidable statically. Now skipped. 2 modules.

A third class was correctly *not* a defect: `codata_constants` has a module
`__getattr__` implementing the 2026-05-10 `M_P_MEV -> M_P_MEV_VALIDATION`
rename, so its 24 flagged imports **resolve at runtime**. A module-level
`__getattr__` can serve any name, so such a module is undecidable too.

Live result: **5935 bindings checked, 4 unresolved, 8 undecidable, 2 ambiguous.**
Quote the undecidable and ambiguous counts with the 4 — they are the audit's
stated coverage limit, not noise.

## Why no fix is proposed

Only one of the four has a mechanical answer, and even that one is a judgement:

- `IM_PERTURBATION` was a **complex** value (`seeds = [s + IM_PERTURBATION for s
  in real_seeds]`, `s` real). The module now carries `IM_PERTURBATION_STR =
  "0.1"` and reconstructs it as `mpc(0, mpf(IM_PERTURBATION_STR))`. But the
  consumer's neighbourhood is **numpy/float** (`complex(s)` on SnapPy shapes,
  `np.argmin`, `float(seed.real)`), so putting an `mpf` there decides a
  NO-FLOAT64 question about which side of that boundary the perturbation lives
  on. That is a precision decision, not a rename.
- `tet_norm -> tet_abs` is *plausible* and unverified. A norm and an absolute
  value are not the same function in general.
- **`_dense_mul` has no candidate at all.** Something was removed, and guessing
  a replacement for a dense multiply is inventing mathematics.
- `hook_length_dim_lambda` likewise has no candidate in `hecke_characters`.

Per `AGENTS.md` §ASK THE OWNER and the owner's standing *"do not can with any
code changes that are speculation"*, three of these are speculation. Proposing a
patch for one and leaving three would also misrepresent the state.

## What it means for the corpus

- `snappy-cusp-seeding.witness.json` **cannot be regenerated** until this is
  fixed, so `qou-3kni` item 1 has a second blocker its text does not name.
- The two `probes/` scripts have **no witness**, so nothing claims currency —
  but per §"PROBES ARE NOT EXEMPT", a probe's conclusion is written into beans,
  audit docs and PR bodies where *nothing re-derives it*. A probe that cannot
  run is a conclusion that can never be re-checked. Treat any recorded
  `qbeta_g3_annihilator_certification` finding as unverifiable until it runs.
- Same family as `qou-n7ue` (two producers that crash and cannot be
  regenerated) but a **different mechanism**: those raise in logic, these fail
  to resolve a name. And `qou-m6gp` is the same *silent*-failure shape one level
  over — an `ImportError` read as a refutation.

## Options

1. **Fix all four, owner-directed per site.** Needs a decision on the mpf/float
   boundary and on what replaced `_dense_mul` and `hook_length_dim_lambda`.
   Then re-run `snappy_cusp_seeding` and commit the refreshed witness in the
   same commit (`durationMs` recorded as **45**, so the run is free).
2. **Fix only `IM_PERTURBATION`**, as the one with a known replacement, and
   leave the rest flagged. Unblocks `qou-3kni` item 1 and nothing else.
3. **Wire the audit into `scripts/precision-gates.sh`** so the class cannot
   recur, without fixing the four. Cheap, and the four stay visible.
4. **Do nothing.** The audit exists and reports them; a reader who runs it sees
   the list. Default.

**Recommendation (judgement, not a finding): 3 then 1.** Wiring the gate is in
§ASK-THE-OWNER exemption 1 by the same reasoning the warn-only precision hook
was accepted under — it makes a silent wrong state impossible — and it is the
half that stops the next rename doing this again. The four fixes want the owner
per site.

## A taxonomy row

This is a detector blind spot of the kind
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues: the
staleness metric is a **file hash of the consumer**, and the defect is in the
*dependency's* namespace. Not added to the table in #7546 — that PR had already
corrected the table's row count once and this is a different arc. The two
calibration failures above (star re-export shims; ambiguous bare-name stems)
are candidate rows in their own right.

## Reproduce

    python3 -I computations/audits/local_import_resolution_audit.py --selftest
    python3 -I computations/audits/local_import_resolution_audit.py


## 2026-10-10 — 1 of the 4 is FIXED by a sibling session; 3 remain

`915e5a28c7` (session `016AEU7xkxdUcw9r7adTXgyr`, merged into
`claude/triangulation-citation-chain-2026-10-10`) fixes
`snappy_cusp_seeding.py` and re-runs both producers. Independent convergence:
that work and this measurement happened in parallel, which is the dynamic
AGENTS.md §"Parallel exploration is valuable" describes.

**They made the NO-FLOAT64 judgement this bean declined to guess, and took the
float side:**

```python
-from q_pochhammer_seed import IM_PERTURBATION
+from q_pochhammer_seed import IM_PERTURBATION_STR
-    seeds = [s + IM_PERTURBATION for s in real_seeds]
+    seeds = [s + complex(0, float(IM_PERTURBATION_STR)) for s in real_seeds]
```

**That is the defensible call, and it is not a precision regression**, which is
worth stating because `float(` in a `computations/` script is normally a defect.
The whole enclosing function is float-domain already — `complex(s)` on SnapPy's
shape parameters, `np.argmin` over the distances, `float(seed.real)` into the
witness — so an `mpf` here would have been a lone high-precision value inside a
float64 pipeline, which buys nothing and would have had to be cast back one line
later. It also restores the pre-rename behaviour exactly rather than changing
the computed object. The NO-FLOAT64 question for this arc is whether the
*pipeline* should be mpf, which is a different and larger change.

They also marked both dead labels `[no carrier]` in the Manuscript-references
block with a pointer to `qou-3kni`, and noted in the prose that the producer
"once named" the carrier-less conjecture rather than deleting the history.

### The 3 that remain, unchanged

| site | imports | status |
|---|---|---|
| `probes/qbeta_g3_annihilator_certification.py:52` | `tet_norm` | module defines `tet_abs`; rename **plausible, unverified** — a norm and an absolute value are not the same function |
| same | `_dense_mul` | **no candidate of any name** |
| `atom_braid_active_partitions.py:128` | `hook_length_dim_lambda` | absent from `hecke/hecke_characters`, no `__getattr__` |

The last one is **latent, not import-time**: it sits in a function body, in the
`else:` branch for the empty word (`χ_λ(1) = dim V_λ`), so the module imports
fine and fails only when that path is taken. That is harder to notice, not
easier.

Still no fix proposed for these three. `_dense_mul` in particular has nothing to
rename to — something was removed, and inventing a dense multiply is inventing
mathematics.

### The audit and the gate question are untouched

`computations/audits/local_import_resolution_audit.py` stands, and re-running it
after the merge is the way to confirm the count moved 4 → 3 rather than taking
it from this note. The recommendation above (option 3: wire it into
`scripts/precision-gates.sh` so the class cannot recur) is unaffected by any of
the four being fixed — a gate is about the next rename, not this one.


---

## 2026-10-10 — measured all three; 1 FIXED (corpus-decided), 2 OPEN and NOT what this bean said they were

PR #7584, branch `claude/qou2cz1-unresolved-imports-2026-10-10`, one commit,
one file. Audit `local_import_resolution_audit.py`: **UNRESOLVED 3 → 2**,
`--selftest` PASS. The clone is SHALLOW (410 commits, back to 2026-09-14), and
all three breakages predate that window — `git log -S` finds every name only in
this bean's own commits, and the `qbeta_g3` consumer is byte-identical to the
shallow boundary. So `-S` is useless for dating them; everything below is
decided by corpus artifacts, not by history.

### Site 1 — `atom_braid_active_partitions.py:128` `hook_length_dim_lambda` → **FIXED as `specht_dim`**

**Measured.** The name is not in `hecke_characters`, has no module
`__getattr__`, and appears NOWHERE else in the tree — ripgrep over the whole
repo including `beans/`, `docs/`, `.lean` and witnesses returns only the two
consumer lines. **It was never defined**; this is not a rename whose source was
lost. The branch is live: `expand_to_branches` starts from `[(1, [])]`, so the
all-identity leaf of any word with an Avg crossing keeps the empty word —
confirmed on `atom_braid_word_3A(1, 1)`.

**Why the corpus decides it** (AGENTS.md exemption 2 — each checkable against an
artifact, not against my reasoning):

1. The call site's own comment names the quantity: *"Empty word = identity
   element; χ_λ(1) = dim V_λ"*.
2. `hecke_characters.specht_dim`'s docstring IS that quantity, in the absent
   name's own words: *"Integer Specht-module dimension `f^λ = #SYT(λ) =
   n! / ∏ hook(c)` (hook-length formula)"*.
3. `partition_utils.dim_lambda` — the declared single source of truth —
   records itself as replacing ad-hoc `partition_dim` / `syt_count` /
   **`hook_length_dim`** copies across compute scripts. The absent name is that
   family plus `_lambda`.

**Verified, not assumed** (proton pin, via `_path_bridge`): `#SYT(λ) ==
specht_dim` for every `λ ⊢ n`, `n = 1..7`; the seminormal rep's matrix
dimension `== specht_dim` for `n ≤ 6`, so `tr(identity)` — which is what
`χ_λ(1)` is — **is** `specht_dim`; Burnside `Σ_λ (f^λ)² = n!` exactly for
`n = 1..8`, confirming the ordinary `q → 1` dimension rather than a
q-deformation; `specht_dim == partition_utils.dim_lambda` exactly, so choosing
between the two centralisation sites does not move the number; and the fixed
branch executes and matches the closed form `χ(σ₁) + (−h/2)·dim V_λ` to
< 1e-40. **Not `dim_q`** (the only other candidate in the module): that is the
q-deformed dimension, `2.0108968702` vs `2` at `λ = (2,1)` at the proton `q₀`.

### Sites 2 + 3 — `qbeta_g3_annihilator_certification.py:52` — **OPEN, deliberately not fixed**

**🛑 This bean's framing of site 2 is wrong and should not be carried forward.**
It records `tet_norm → tet_abs` as *"rename plausible, unconfirmed"*. It is not
a rename: **the corpus names `tet_norm` as a BUG and `tet_abs` as its fix.**

- `docs/coordination/1ppq-qbeta.md` (#3813, 2026-07-18): *"its `tet_norm`
  under-summed the per-factor series, reported a spurious negative lead for
  large-argument I_Δ, and its convergence guard then wrongly rejected the
  convergent bare sum as a 'flat divergent wing.'"*
- `qbeta_g3_fourone_index_assembly_corrected.py`: *"consumes `tet_index_exact`
  … as I_Δ — **NOT the buggy `tet_norm`**"*.
- `qbeta-g3-fourone-index-assembly.witness.json` names the mechanism exactly:
  *"the 'divergent flat wing' was a truncation artifact of **rebasing each
  tetrahedron factor to its (un-cancelled) minimum exponent**; computing I_Δ at
  **absolute degree** instead makes the flux sum converge"* — and `tet_abs`'s
  docstring is *"ABSOLUTE x-degrees … **No min-degree rebasing**"*.

So `abs` here means **absolute degree, not absolute value**, and the bean's
"a norm and an absolute value are not the same function" caution, while
correct in spirit, is aimed at the wrong distinction. The two also have
different return contracts — `tet_norm` is unpacked `sh1, s1 = tet_norm(...)`,
i.e. `(shift, dense_list)`; `tet_abs` returns a flat tuple of `(deg, coeff)`
pairs. Substituting it would mis-unpack **silently** when the tuple has
length 2.

**`_dense_mul` confirmed to have no candidate under any name**, as this bean
says. Ripgrep over the whole tree: every `*dense*` hit in Python is a
matrix/representation helper in an unrelated probe, and the only
`dense_dense_mul` family is Rust **matrix** multiply. Nothing is a
Laurent-series multiply. Its contract is nonetheless fully readable off the
call site: `prod = _dense_mul(s1, s2, order - off)` followed by
`for d, c in enumerate(prod)` ⇒ it returns a **dense list indexed by degree**.

**The script is a pre-rewrite fossil, and its job already runs elsewhere.** The
provider's own `main()` step **[5]** *is* the annihilator certification
(`quantum_a_poly_op` → "quantum A-polynomial L̂_4₁ annihilates I_41, DGG eq
C.7"); its step [0] ties `tet_abs` to the certified `tet_index_exact`; and
`qbeta-g3-fourone-index-assembly.witness.json` records
`quantum_a_polynomial_annihilation` → **PASS**. The standalone script's witness,
dated the same day as #3813, records the opposite —
`assembly_certified_by_annihilator` **FAIL**, `certified_candidate_unique`
**FAIL**, `"error": "candidate non-convergent at grid point"` — which is
literally the `return None` from the rejection guard the ledger adjudicated as
wrong, and a published FAILED verdict ("no candidate annihilated — operator
reading or assembly space needs revisit") attached to content block
`conj:im-q-physical-role`.

**Why not fixed.** Restoring the two names would resurrect the exact rebasing
mechanism the corpus names as the bug, to re-derive a verdict the corpus has
already reached by the corrected route. A probe conclusion is an argument that
gets written into beans, audit docs and content blocks where nothing
re-derives it, so this is the expensive kind of wrong. Note also that it is
**not an import fix at all**: `ser_mul` (the corrected path's multiply) returns
a **dict**, so a port must also change the `enumerate(prod)` loop — i.e. edit
the algorithm.

**One part is NOT superseded and needs neither broken import.**
`trefoil_calibrate()` — extracted and run in isolation — reproduces its
recorded witness assertion exactly: pinned convention annihilates `δ_{e,3m}`,
all 15 other conventions FAIL, `n_conventions_passing = 1`. The provider's step
[5] does **not** re-verify that 16-convention uniqueness. So the file splits
cleanly: `trefoil_calibrate` works and is unique; `_assemble` / `assemble` /
`annihilator_residual` / `main` are broken and superseded.

**The observation that would settle it** is a disposition choice, not a
measurement — which is why it is left here:

1. **Retire the script.** Cheap; the certification already PASSES in the
   provider and the calibrator result is already recorded in the witness.
   Costs the calibrator's standalone re-runnability.
2. **Reduce it to `trefoil_calibrate` alone** — delete `_assemble`,
   `annihilator_residual` and the two broken imports, keep the unique
   16-convention uniqueness check, and re-emit a witness carrying only the
   assertion that passes. Removes the published FAILED verdict, which is the
   strongest argument for it.
3. **Port `_assemble`** to `tet_index_exact` + `ser_mul` + window stability
   (dropping the adjudicated-wrong rejection guard). Most work, and duplicates
   the provider's step [5]; only worth it if an independent second
   implementation of the certification is wanted.

**Recommendation (my judgement, not a finding): option 2.** It is the only one
that both removes a published FAILED certification the corpus has since
reversed and keeps the one result in the file that nothing else computes.
Option 1 is a close second and strictly cheaper. **Default if nothing is done:**
the audit keeps reporting 2 unresolved, the script stays un-importable, and its
witness keeps publishing the superseded FAIL — i.e. the no-op is *not*
harmless here, which is the one reason not to defer indefinitely.

### Also found: a SECOND, independent defect in the site-1 file — reported, NOT fixed

Fixing the import exposed that the producer still cannot run, for an unrelated
reason. The module-level float64 literal `HA = 0.20906032198987945` has drifted
**2.319e-08** from the live `hecke_core.h = 0.20906029879563937` — seven orders
above the `1e-12` guard tolerance — so `expand_to_branches` raises
`ValueError: unexpected d=-0.209060298795639` on every live word. Measured `d`
values in `atom_braid_word_3A(1, 1)`: `-0.20906029879563932` (= −h),
`-0.10453014939781966` (= −h/2), `-0.10445824776972629` (colour-weighted), `0`.

**It is not only a guard problem — the stale literal is also the empty-word
branch's coefficient, so it contaminates results.** At `λ = (2,1)` the exact
value is `0` and comes out at `−2.3194e-08`, exactly the drift.

Replacing a hardcoded literal with a derived value is AGENTS.md exemption 1, so
this is *eligible* to fix without asking — but it moves the producer's numbers
and needs a witness regeneration, which is outside this bean. **Observation that
would settle it:** whether `HA` / `H_HALF` should be derived from
`hecke_core.h` at the live pin (and the `1e-12` guards re-expressed against it),
and which anchor the regenerated `atom-braid-active-partitions.witness.json`
should carry. Worth its own bean.

### Process note — shared working tree

This container's tree is shared with a concurrent agent in the same session. My
`git checkout -b` moved it off `claude/taxonomy-row-cache-universe-2026-10-10`
and that agent's next commit (`a49b625c39`, "taxonomy row 55") landed on my
branch. Moved back with `git branch -f` so it sits on their branch — additive,
local only, nothing force-pushed; `git branch --contains a49b625c39` confirms
reachability. Their uncommitted work (`scripts/precision-gates.sh`, six
regenerated audit witnesses, `docstring_label_carrier_audit.py`) was left
untouched and is not in my commit.
