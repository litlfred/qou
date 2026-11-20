---
# qou-3kni
title: 'Two conj: labels named by the pole-to-cusp producers have no carrier -- and neither producer can be re-run here to fix the docstring'
status: todo
pr: 8283
type: task
priority: normal
created_at: 2026-09-14T19:57:29Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---

Measured 2026-09-14 (PR #7401, issue #7400), while exploring `qou-mfdq` Finding 1.
**Nothing edited in `computations/` here** — the reason is below and it is not
caution, it is that the fix cannot be verified in this container.

## The finding

Both live producers of the pole-to-cusp arc declare, in their **Manuscript
references** docstrings, conjecture labels that have **no carrier file anywhere
in the tree**:

```
computations/q_pochhammer_seed.py:11-14     computations/snappy_cusp_seeding.py:26-28
  - def:q-pochhammer-partial-product   OK      - conj:shared-denominator-cusp-holonomy   OK
  - conj:shared-denominator-cusp-holonomy OK   - conj:pl-jsj-mass-integration-equivalence  DEAD
  - conj:denominator-zeros-as-sw-critical-points  DEAD   - conj:denominator-zeros-as-sw-critical-points  DEAD
  - conj:pl-jsj-mass-integration-equivalence      DEAD
```

Measured with `git ls-files | grep -c <label>`:

| label | carrier files |
|---|---|
| `shared-denominator-cusp-holonomy` | 5 |
| `algebraic-geometric-dilog-equivalence` | 5 |
| **`pl-jsj-mass-integration-equivalence`** | **0** |
| **`denominator-zeros-as-sw-critical-points`** | **0** |
| **`jet-gb-pl-correspondence`** | **0** |

`snappy_cusp_seeding.py:16-17` goes further than citing one: *"The output is a
witness for `conj:shared-denominator-cusp-holonomy` **and
`conj:pl-jsj-mass-integration-equivalence`**"* — a producer declaring itself the
witness for a conjecture that does not exist.

The third label, `prop:jet-gb-pl-correspondence`, is named in
`brings-surface/thurston-relaxation.md:9` as the carrier of the **"GB-PL
bijection"** — the corpus's only statement identifying Gröbner-Shirshov
reduction depth with the ideal-tetrahedron count. That identification is
load-bearing for the whole `n`-overload question (`qou-mfdq`, and the sixth
"depth" sense now registered in `notation-collisions.md`), and its carrier is
gone.

All three lived under `folio/quantum-observable-universe/descartes-universe/`,
which no longer exists (`ls -d` → No such file or directory).

## Why no checker catches any of them

- `uses-resolve` reads **manifest `uses[]`**. Two of these are in **Python
  docstrings** and the third is **plain parenthetical prose**, not a
  `[...](#label)` link. None is a manifest edge.
- The witness validators read `contentBlock`, and both producers call
  `w.set_content_block("conj:shared-denominator-cusp-holonomy")` — a **live**
  label. So the machine-readable field is clean and the prose is not.

## Why the producer docstrings were NOT edited

`scriptHash` is a whole-file hash, so a docstring-only edit drifts it and the
witness goes stale. AGENTS.md's remedy is "just re-run the producer". **Neither
can be re-run in this container:**

- `snappy_cusp_seeding.py` — `import snappy` → `ModuleNotFoundError`. Not
  installed, not pip-installable here.
- `q_pochhammer_seed.py` — runs, but local `mpmath` is **1.3.0** against the
  witness's recorded **1.4.1**. Re-running would stamp an environment
  **downgrade** into the witness. (This is not hypothetical: a stray
  `qbeta-ck-basis-constrained-pslq.witness.json` in the working tree at the
  start of this session carried exactly that 1.4.1 → 1.3.0 regression, and was
  reverted rather than committed.)

So editing either docstring here buys a correct comment and a stale witness,
which is a worse trade than leaving the comment wrong and findable.

## What to do, and what it needs

1. **In a container with `snappy` and `mpmath 1.4.1`**: correct both Manuscript
   reference blocks (mark the two labels as having no carrier, naming the
   removed `descartes-universe/` chapter), then re-run both producers and commit
   the refreshed witnesses in the same commit. Cheap — recorded `durationMs` is
   **15** and **45**.
2. **Separately and independently**: decide what `prop:jet-gb-pl-correspondence`
   should be. Either the GB-PL bijection is restated somewhere live, or
   `thurston-relaxation.md:9` should stop asserting it. That is a mathematical
   call, not a bookkeeping one — see `qou-mfdq` and the "triangulation size"
   entry in `notation-collisions.md`, both of which record that the
   identification is currently *asserted* rather than supported.
3. **Worth considering, not proposed**: a checker for `conj:`/`prop:`/`def:`
   labels appearing in `computations/*.py` docstrings, which is a surface no
   existing gate reads. Three dead labels in two files is a small sample; the
   population is unmeasured.

## Default if nothing is done

The two producers keep declaring themselves witnesses for a non-existent
conjecture, and `thurston-relaxation` keeps citing a carrier that is not there.
No number moves; no witness is wrong; the cost is entirely that a reader
following those citations lands on nothing, and that the GB-PL identification
reads as backed when it is not.


---

## Re-checked 2026-10-10 — the producer half is MORE blocked, and this bean's third finding is misdescribed

**Environment, measured in a fresh container (not the one that wrote this bean):**
`snappy` absent as before, and so are **`mpmath`, `numpy`, `scipy` and `sympy`** —
all four. So the docstring half stays blocked and the block is wider than
recorded: the two producers cannot be imported here, let alone re-run to
re-stamp `scriptHash`. Nothing in `computations/` was edited.

**🛑 The third finding above is wrong about WHERE the label is named, and the
error propagated into `notation-collisions.md`.** This bean says
`prop:jet-gb-pl-correspondence` *"is named in
`brings-surface/thurston-relaxation.md:9` as the carrier of the GB-PL
bijection"*. It is not. The whole of line 9's claim is

> The Gröbner--Shirshov reduction depth maps to the number of ideal tetrahedra
> used in the triangulation (GB--PL bijection).

— a bare parenthetical with no label and no link. Measured: `jet-gb-pl`,
`GB-PL` and `GB--PL` together occur in that file **exactly once**, on that line.

That misdescription reached `notation-collisions.md` in PR #7401, whose
`n`-overload entry read *"the carrier it names for that … has no file in the
tree"*. Provenance checked, not assumed: main before #7401's merge had **0**
occurrences of that clause, the branch side **1**. Corrected in PR #7546.

**The correction makes the claim STRONGER.** "Cites a dead carrier" is a
dangling reference; "names no carrier" means the GB-PL assertion is
**unreachable by label at all** — an agent grepping the label to find the claim
lands only on the register entry recording its absence, never on the assertion.

**Carrier counts re-measured on `main` 77695711d2** (the 2026-09-14 figures
above are a month and ~500 commits old):

| label | carriers | was |
|---|---|---|
| `jet-gb-pl-correspondence` | 0 | 0 |
| `pl-jsj-mass-integration-equivalence` | 0 | 0 |
| `denominator-zeros-as-sw-critical-points` | 0 | 0 |
| `shared-denominator-cusp-holonomy` | **6** | 5 |
| `algebraic-geometric-dilog-equivalence` | 5 | 5 |

And **no witness either**: the `jet-gb-pl-correspondence.witness.json` that
`docs/audits/2026-05-18-compute-integration-sweep.md:145` lists does not exist.
Both dated audits place the block at
`folio/quantum-observable-universe/descartes-universe/`, which the
`content/` -> `folio/` move left behind.

**Still open, and why it is not closeable here** (per the rule against closing a
bean whose subject is an open conjecture): the two *docstring* labels need a
container that can run the producers, and whether `thurston-relaxation.md:9`'s
uncited GB-PL identification should be scoped, retired, or given a carrier is a
mathematics decision for the owner — clause (1) of
`conj:algebraic-geometric-dilog-equivalence` defers to that line for the
depth-equals-tetrahedron-count identification, so changing it moves what the
conjecture is understood to rest on.

## 2026-10-10 — owner ruling on the GB–PL line: scope it

Owner chose "Scope it" on a decision card (scope / retire / give a carrier / leave).
`thurston-relaxation.md` line 9 now says the depth-equals-tetrahedron-count identification
is asserted, not established, names clause (1) of `conj:algebraic-geometric-dilog-equivalence`
as resting on it, and gives it that conjecture's tier. No mathematics was decided. A
carrier block is still possible later. This bean stays `todo`: the identification is
still open, and the producer re-run half is tracked separately.

## 2026-10-10 — producer half done: docstrings corrected, both re-run, payloads byte-identical

Installed snappy 3.3.2, mpmath 1.4.1, numpy 2.4.6, scipy 1.17.1, sympy 1.14.0 and
clarabel 0.11.1, which matches every recorded `environment` field except python
(3.11.15 recorded, 3.13.16 here) and `pyhecke_native_build`.

- **`snappy_cusp_seeding.py` was broken on main.** It imported `IM_PERTURBATION` from
  `q_pochhammer_seed`, which now exports only `IM_PERTURBATION_STR = "0.1"`, so it died
  with `ImportError` before computing anything. The fix uses the shared string constant
  (`complex(0, float(IM_PERTURBATION_STR))`, the same 0.1j kick).
- Both Manuscript-reference blocks now mark `conj:pl-jsj-mass-integration-equivalence`
  and `conj:denominator-zeros-as-sw-critical-points` as `[no carrier]`.
- Re-run with the volatile fields masked (computedAt, commitSha, scriptHash,
  scriptCommitSha, durationMs, invocation, environment): **0 payload differences in
  either witness.** A baseline run before the edit also reproduced q-pochhammer-seed
  unchanged.
- `precision-gates.sh`: the RED set is identical with and without these changes (10
  pre-existing ratchets), and no RED line names either file. snappy-cusp-seeding still
  carries 121 raw float64 fields. That is pre-existing, the values are unchanged, and the
  fix (carry mpf through SnapPy output) is not made here.

Stays `todo`: the GB–PL identification is still an open conjecture-tier claim (scoped
the same day), and the two dead labels still have no carrier.


## 2026-10-10 (later) — the environment blocker is GONE; the producer half has a DIFFERENT blocker

**Both environment claims above are now measurably false in this container**, and
one of them was never about the environment at all.

### `snappy` IS pip-installable

This bean says *"Not installed, not pip-installable here."* Measured:
`python3 -m pip install snappy` → **SnapPy 3.3.2, `snappy.Manifold` available**
(one harmless `Plink failed to import tkinter` warning; GUI only). `qou-m6gp`
independently recorded the same correction on 2026-09-07 — *"SnapPy 3.3.2 was
ALREADY present in this container; the absent-from-every-container premise does
not hold"* — so this is the second time the claim has been retracted, and the
first retraction was not propagated here.

**One trap worth recording, because `pip` reported success while doing nothing
useful:** this container has `python3` = `/usr/local/bin/python3` (3.11.17) and
`pip` = `/usr/bin/pip` (**python 3.13**). `pip install` exits 0 and installs into
an interpreter nothing here uses; `python3 -c "import mpmath"` still fails. Use
`python3 -m pip`. Same shape as every other finding in this session: a tool
reporting success for work done in the wrong place.

### The `mpmath` downgrade blocker is resolved, and the re-run is CLEAN

This bean correctly refused to re-run `q_pochhammer_seed.py` under local
`mpmath 1.3.0` against the witness's recorded **1.4.1**, since that stamps an
environment downgrade. `python3 -m pip install mpmath==1.4.1` installs
(sympy warns about its own `<1.4` pin; nothing here imports sympy on this path).

Full environment now stamped, against the recorded block:

| key | recorded | here | |
|---|---|---|---|
| `mpmath` | 1.4.1 | **1.4.1** | match |
| `numpy` / `scipy` / `sympy` | 2.4.6 / 1.17.1 / 1.14.0 | identical | match |
| `clarabel` | 0.11.1 | **0.11.1** | match |
| `pyhecke_native` | 0.9.0 | **0.9.0** | built from `tools/pyhecke-native` (`maturin build --release`, Cargo.toml says 0.9.0) |
| `python` | 3.11.15 | 3.11.17 | patch **upgrade** |
| `pyhecke_native_build` | `e3fab84c4c1df76a` | `f674395cadf67f1a` | **expected to differ** |

That last row is not a regression and must not be read as one:
`qou_substrate.witness` computes it as `sha256(<compiled .so>)[:16]` and its own
comment says the field *"is NOT a version and must never be ORDERED"*, with the
measured reason — ordering a hex digest makes the verdict depend on whether it
starts with a digit — and notes the corpus already carries **five distinct
values across 811 witnesses**.

**`q_pochhammer_seed.py` re-ran here and the producer's own guard said it:**

> `↑ environment: recording a STRONGER environment block than the copy on disk;
> rewriting provenance only (payload unchanged).`

The diff is **exactly five lines and every one is provenance** — `computedAt`,
`commitSha`, `scriptCommitSha`, the python patch bump, the build hash. Zero
payload change; `scriptHash` untouched. So the docstring edit this bean defers
is now safe for that producer. **The tree was restored afterwards**
(`git checkout -- computations/`) per the sibling-witness discipline; nothing was
committed, because the docstring edit itself has not been made.

### But `snappy_cusp_seeding.py` CANNOT RUN, for an unrelated reason

With `snappy` installed it gets two lines further and dies:

    File "computations/snappy_cusp_seeding.py", line 47
      from q_pochhammer_seed import IM_PERTURBATION
    ImportError: cannot import name 'IM_PERTURBATION' from 'q_pochhammer_seed'

`q_pochhammer_seed.py` carries `IM_PERTURBATION_STR = "0.1"` and reconstructs the
complex value as `mpc(0, mpf(IM_PERTURBATION_STR))` — the NO-FLOAT64 migration
dated **2026-09-13** in its own docstring. The consumer's import was never
updated. **Byte-identical on `origin/main`**, so this is pre-existing, not
branch damage.

And it is invisible to every staleness path: `snappy_cusp_seeding.py`'s
`scriptHash` is `f4733c216049`, its witness records `f4733c216049` — **IN
SYNC** — `computedAt 2026-08-28`, three weeks before the rename. A witness
claiming currency with a producer that cannot be imported.

**So item 1 of this bean has a second blocker its text does not name**, and the
first one is no longer the obstacle. Tracked as **`qou-2cz1`**, with a calibrated
AST audit ([`computations/audits/local_import_resolution_audit.py`](computations/audits/local_import_resolution_audit.py))
that finds this class corpus-wide: **4 unresolved bindings of 5935 checked**, of
which three have **no mechanical replacement** (`_dense_mul` has no candidate of
any name), so no fix is proposed here.

### Still blocked, and still nothing edited in `computations/`

The docstring correction for `snappy_cusp_seeding.py` would drift its
`scriptHash` and its witness cannot be regenerated until `qou-2cz1` is decided.
`q_pochhammer_seed.py`'s docstring half is now unblocked and could land alone —
but the two blocks name the same two dead labels, and splitting them leaves half
the finding wrong in the tree. Left as one unit.

Re-verified on this tree: `pl-jsj-mass-integration-equivalence` **0** carrier
files, `denominator-zeros-as-sw-critical-points` **0**,
`jet-gb-pl-correspondence` **0**, against
`shared-denominator-cusp-holonomy` **6** and
`algebraic-geometric-dilog-equivalence` **5**.

## 2026-10-10 — item 3 MEASURED: 25 dead labels, not three, and the worst is cited nine times

Item 3 above reads *"Three dead labels in two files is a small sample; the
population is unmeasured."* It is now measured, and the sample understated it
**by 8×**.

[`computations/audits/docstring_label_carrier_audit.py`](../../computations/audits/docstring_label_carrier_audit.py),
run on `main` `2ab87236c9`:

| quantity | measured |
|---|---|
| distinct corpus labels cited in `computations/` docstrings | **487** |
| files doing the citing | **860** |
| labels resolving to **no** block in `folio/` or `content/` | **25** |
| citations pointing at nothing | **57** |

Worst by citing-file count:

```
 9  prop:li2q-phiq-bar-symmetrization
 8  prop:constit-factor-tau-M-proton-identity
 6  conj:delta-lambda-categorical-closure
 6  prop:mass-formula-iterative-lp-dual
```

`prop:li2q-phiq-bar-symmetrization` is cited by nine files including
`computations/_li_2_q_util.py`, which the mass-formula banner in AGENTS.md
names as load-bearing (`vol_density_*`). So this is not confined to the two
pole-to-cusp producers this bean was opened about.

**The regex's character class IS the blind spot, and that is what the
self-test asserts.** A `[a-z0-9-]` tail truncates
`prop:constit-factor-tau-M-proton-identity` at the uppercase `M` and reports
the **fragment** as dead — a false positive that reads exactly like a real
finding. The selftest asserts the full label is captured **and** that the
fragment is not, plus two known-dead and two known-live classifications, and
is mutation-tested four ways. The first mutation attempt patched the memo
cache rather than the return value, so it blinded nothing and "passed" —
recorded rather than asserted, per taxonomy row 45: an audit that
self-certifies its calibration cannot discover its own blind spot.

The audit **skips its own file**: its calibration note quotes the truncated
fragment as documentation, and once the file sat under `computations/` the
selftest failed on a clean tree.

**Wired ADVISORY** into `scripts/precision-gates.sh`, with the flip-to-blocking
condition stated inline: it flips when the dead count reaches 0. It is not
blocking now because most of the 25 name blocks in the removed
`descartes-universe/` chapter, and whether each becomes a restored carrier, a
retired citation, or a scoped citation is **a content decision per label, not
a sweep** — under AGENTS.md's ASK-THE-OWNER rule that is the owner's call, not
an agent's.

**Item 3 is therefore done as far as an agent may take it**: the checker it
calls "worth considering, not proposed" exists, is calibrated, and is wired.
**The bean stays `todo`** — items 1 and 2 are untouched, and item 2 turns on
the `A_ω → S` identification, which is an open conjecture.

### The decision this leaves with the owner

Nothing changes if you say nothing: the gate is advisory, prints the 25, and
blocks no commit. The 57 dead citations stay as they are.

- **Restore the carriers** (write the missing blocks back). Costs a content
  block per label, 25 of them, several naming removed-chapter material whose
  statements would have to be reconstructed; risks re-publishing a claim the
  chapter was removed *for*. Commits the corpus to supporting each label.
- **Retire the citations** (edit the 57 docstring sites to drop or rephrase).
  Costs 57 small edits over ~40 files; risks deleting the only pointer to what
  a producer was *for*, which is the blocker recorded in this bean's own
  §"Why the producer docstrings were NOT edited". Commits to nothing.
- **Scope them** (keep the label, mark it `[no carrier]` inline, as
  `snappy_cusp_seeding.py` already does for its two). Costs 57 edits of one
  clause; no risk to the record; commits to nothing, and makes the gate
  flippable to blocking.

**My recommendation, as judgement rather than finding:** scope them, in one
pass, the way `snappy_cusp_seeding.py` already reads. It is the only option
that preserves the provenance a reader needs while making the surface
drainable — and it is reversible, where restoring a carrier is not.

---

## 2026-10-10 — the gate is BLOCKING, as a draining ratchet at 26 (owner ruling "c1")

Owner, relayed: the label gate *"blocks only when the count INCREASES, not at
0. Also pin its cwd to the repo root: run from `computations/` it reports 399
instead of 25."* Both halves landed — `d16a0362f1` (cwd) and `66fab2f5de`
(ratchet + flip), PR #7586.

### Zero is unreachable, and a FIX is what proved it

This bean's own §"The decision this leaves with the owner" says the scope-them
option *"makes the gate flippable to blocking"*, with 0 as the implied trigger.
**That trigger cannot be met.** The audit cannot distinguish CITING a dead
label from DOCUMENTING that one is dead, so a producer that explains a retired
label in prose RAISES the count. Measured: redirecting
`prop:per-partition-k-lambda-rule`'s two citations to the audit doc holding its
record moved the count **25 -> 26** and the citations **57 -> 58**, because the
explanatory note has to name both the `prop:` and the `rem:` spelling in order
to say they are gone. The corpus surface did not grow; the documentation did.

No syntactic discriminator is proposed — "mentioned in a sentence saying it is
dead" is not a property of the AST — so a zero-threshold gate would punish
exactly the fix it is meant to reward. Recorded as a known false-positive class
in the audit's own header, with the instance worked through.

`--max N` inverts it: the bound may only fall. Verified, all five branches —
`--max 26` rc=0 at the bound; `--max 30` rc=0 "DRAINED by 4, lower the bound";
`--max 25` rc=1 RATCHET FAILED; `--max` bare and `--max abc` rc=2; `--selftest`
unaffected. Replayed through the harness loop verbatim with the args field.

### The cwd swing was 15x, and both halves of the audit hid it

Same tree, same commit, varying nothing but the cwd: **26 dead / 58 citations**
from the root, **400 dead / 1052 citations** from `computations/`. (The relayed
figure was 399; re-measured here at 400 after the k_lambda redirect, which is
the same +1 the ratchet note above explains.) The scan itself is
cwd-independent — both runs report the same **488 labels over 862 files**,
because `ROOT` comes from `__file__` — so the two halves disagreed *silently*:
`git ls-files` listed only `computations/`, and `git grep -- folio/ content/`
matched nothing because neither path exists relative to `computations/`. Every
git call is now pinned to `git rev-parse --show-toplevel`, and `--selftest`
asserts `folio/` is in the tracked set with >= 1000 entries, so the pin cannot
be lost quietly.

### Four citations redirected (A1), count unchanged at 26

`conj:pl-jsj-mass-integration-equivalence` in `q_pochhammer_seed.py` and
`snappy_cusp_seeding.py` -> the `f86ea9d7ac` removal record;
`probes/lr_hecke_character_probe.py` -> the parent
`prop:hecke-branching-trace-decomposition`, verified live (which is why
distinct labels go 488 -> 489 while dead stays 26). The fourth,
`b_over_a_evaluator.py`, was not merely a dead *label* but a **markdown link to
a `.md` file deleted in `c703e576b5`** — a reader following it got a 404.
Replaced with that commit's own finding, quoted: the formula *"is NOT the
canonical formula. v3 was attacking the wrong target."*

### 🛑 Correction to my own plan: the import gate reads 3 here, not 0

I reported that the companion import gate was ready to flip "now that it reads
0". **That 0 is a property of a branch.** Same hour, same audit, varying only
the checkout: `claude/qou2cz1-unresolved-imports-2026-10-10` reads **0**, this
branch reads **3**, `origin/main` reads **3**, and `ac520bba3b` is **not** an
ancestor of main (`git merge-base --is-ancestor`, not inferred). Flipping would
have shipped a gate red on arrival — the failure `precision-gates.sh`'s own
header says gets a gate muted rather than fixed. It stays advisory, with all
three counts and the flip condition recorded in place. Same class as the
`qou-wu38` cost-figure error: a figure measured in one place, quoted about
another.

**The bean stays `todo`.** Items 1 and 2 are untouched, item 2 still turns on
the open `A_ω → S` identification, and the per-label disposition of the 26 is
still the owner's call — the ratchet makes the surface *drainable*, it does not
decide how.

---

## 2026-10-11 — THE SURFACE IS DRAINED: 26 → 0, and the threshold was never the thing to change

All three groups retired. `26 → 0` dead labels, `58 → 0` citations; the gate
runs at `--max 0` and now blocks any NEW dead citation from zero.

### 🛑 This corrects my own reasoning from yesterday

I argued — in the audit's header, the gate entry, this bean and two PR comments
— that **0 is unreachable** "while any producer explains a retired label in
prose", and built a draining ratchet around that premise. **The premise held
only because the explanations were written in LABEL SYNTAX.**

Drop the `prop:`/`conj:` prefix — write *"the retired
`constit-factor-tau-M-proton-identity` proposition"* and point at the record
doc — and the prose keeps every pointer a reader needs while the detector stops
counting it. The audit scans `computations/**/*.py` docstrings only, so a record
doc in `docs/` is outside its scan by construction.

So **the ratchet was the right mechanism for a surface that could not drain; it
turned out this one could.** The ratchet stays (it is what blocks a regression),
but at 0 rather than 26.

### What a reader gains, not loses

| before | after |
|---|---|
| a bare `prop:X` in a docstring, resolving to nothing | the stem (still greppable through history) + [`docs/audits/2026-10-11-retired-label-records.md`](../../docs/audits/2026-10-11-retired-label-records.md), carrying per label what it **stated**, the commit that **retired** it, and the exact command to **recover** the content |

Group A's paths are **commit-pinned** at `0763606e4f^`, since `_deprecated/`
left `main` on 2026-10-10.

### The three groups, drained per label and not per group

| group | labels | citations | remedy |
|---|---:|---:|---|
| C — never existed | 7 | 8 occ / 6 files | named in words, no prefix; nothing to point at |
| B — deleted outright | 9 | 17 occ / 11 files | de-prefixed + the deleting commit |
| A — demoted to `_deprecated/` | 10 | 45 occ / 39 files | de-prefixed + record doc §A |

**Read per label, not per group.** `prop:per-partition-k-lambda-rule` is in C
("never existed") but its **content** existed under the `rem:` spelling in B,
so its citation is **redirected** to `2026-06-17-refuted-ansatz-lemmas.md`, not
removed — a blanket "C → delete" would have thrown away a live pointer.

### Two things deliberately NOT done

- **`channel_product_mass.py`'s witness field** still carries a retired label
  verbatim (`w.set_content_block(…)` with the `rem:`-prefixed string). That
  writes a **committed witness**, so correcting it is a witness regeneration,
  not a docstring edit. Flagged in the docstring and left.
- **No content block restored.** The owner's ruling was record-in-an-audit-doc,
  explicitly *not* restore.

### Verification, and one check that was load-bearing

**No code changed in any of the 39 group-A files** — verified by comparing each
file's AST **with docstrings stripped**: 39/39 identical. That check is not
ceremonial: **two of the original 58 sites were CODE, not docstrings**, and one
of them writes a witness. A grep-driven sweep would have hit both.

**The selftest was asserting the defect.** Draining the surface broke it three
ways at once — *"not captured"*, *"not even cited"* ×2 — on a tree where the
detector worked perfectly, because two assertions required the corpus to **still
cite** a retired label. A calibration keyed on corpus state goes stale exactly
when the corpus is fixed. Both are now **synthetic**: assertion 1 runs `LABEL`
over a fixture string, assertion 2 tests carrier lookup, which is independent of
citation state.

**Mutation-tested 4/4 CAUGHT**: buggy regex tail (reports the truncated fragment
verbatim — the original defect), `has_carrier` always `True`, always `False`,
cwd-scoped git layer. A fifth attempt **did not apply at all** and printed
`SELFTEST PASS` — that was the *unmutated* file passing, not a mutant escaping.
Recorded because reading it as a result is taxonomy row 45 exactly: **a mutation
that misses is evidence about the mutation, not the detector.**

One self-inflicted finding: my own group-B fix for `channel_product_mass.py`
quoted the retired label **verbatim** inside the warning note it added, so the
fix re-created the very false positive it was fixing, one level down.

### Status

Item 3 of this bean is **done**: the population was unmeasured, is now measured
(489 labels / 862 files, 26 dead / 58 citations), disposed of, and gated at
zero. **The bean stays `todo`** — items 1 and 2 are untouched, and item 2 turns
on the `A_ω → S` identification, which is an open conjecture.

## Round 56 Implementation Progress (PR #8283)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8283 (head `f53a095b5ee34373c44ef4b0b400e85b12af4c1c`, Commit 1 `0e2f86d58bac8f2f07854f3515aabf15d9779cd3`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/MellorMelvinModDeltaAndBws0DegreeFourClosure.lean` (`pole_to_cusp_carrier_inventory_and_gb_pl_tetrahedron_match`)
- **80-dps Witness:** `computations/probes/round56-mellor-melvin-bws0-stokes-dt-qholonomic.witness.json` (`scriptHash: d98411981e4d`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8283, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-10-11: "beans(qou-3kni): item 3 done — surface drained 26 -> 0; bean stays todo"). The work may be partly or fully done. Read the bean before you close it.
