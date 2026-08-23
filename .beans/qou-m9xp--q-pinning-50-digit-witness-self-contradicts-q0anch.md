---
# qou-m9xp
title: 'q-pinning-50-digit witness self-contradicts: q0Anchor=muon but calibration_inputs.anchor=m_p/m_e'
status: completed
type: task
priority: normal
created_at: 2026-08-19T17:19:14Z
updated_at: 2026-08-21T16:33:52Z
---

## The contradiction

`computations/q-pinning-50-digit.witness.json` states its anchor **both ways**:

| field | value |
|---|---|
| `.q0Anchor` | `muon` |
| `.q0Value` | `1.1099785955573347198997632…` ← the **muon** value |
| `.derived_50_digit.q` | `1.1099785955573347198997632…` ← the **muon** value |
| `.calibration_inputs.anchor` | **`m_p/m_e`** ← proton |
| `.physical_anchoring_bound.anchor` | **`m_p/m_e`** ← proton |

The *numbers* are muon throughout; two *metadata* fields say the calibration
input was the proton ratio. Both cannot be true. A reader checking the anchor
gets whichever answer they happen to grep for.

For reference the two pins differ by **11.54 ppb** — the μ–p substrate tension
itself:

    muon   q0 = 1.1099785955573347
    proton q0 = 1.1099785827513808
    relative  = 11.54 ppb

## Why it matters now

`computations/alpha/alpha_k_jones_markov_h12.py` reads this witness for its
substrate constants:

```python
Q_PIN  = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_mpf = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
q0_f64 = float(q0_mpf)
h_f64  = float(q0_mpf - 1 / q0_mpf)
z_mark = q0_mpf**3 / (q0_mpf**2 + 1)
```

So `q0`, `h` and the Markov parameter `z` are all **muon**-pinned there, while
the owner directive of 2026-08-07 makes the **proton/experimental** pin the
default for all agents and all production code, and the rest of the surface
this producer sits in has moved: `y-lambda-at-q0.witness.json` now records
`parameters.q_0 = 1.10997858275138080759…`, i.e. **proton**.

`alpha-k-jones-markov-h12` is also one of the remaining convention-C
witnesses (`qou-lt8x`). Migrating its C→D convention **without** settling the
pin would produce a quantity that straddles: convention D evaluated at the
muon anchor, feeding a corpus that is proton elsewhere. AGENTS.md
§"q₀ anchor convention" is explicit that straddling is a defect regardless of
its size, and the measured cost of the last straddle was this same 11.54 ppb.

## Note for AGENTS.md currency

AGENTS.md §"q₀ anchor convention" rule 2 says the `computations/` layer
"historically carries **muon-q₀** witnesses:
`…/q-pinning-50-digit.witness.json` holds the muon value". That is still
accurate for *this* file — but the **companion claim is now stale for
`y-lambda-at-q0`**, which has been rebuilt at the proton pin. The straddle
hazard the rule describes (cache muon-built, caller passes proton `Q`)
therefore does **not** apply to the y_λ cache any more. Worth correcting when
someone next touches that section, so a reader does not avoid a hazard that
has already been removed — or, worse, assume the remaining muon files were
migrated too.

## To close

1. Decide which anchor this witness records, and make all five fields agree.
   The value is muon; the `calibration_inputs.anchor` / `physical_anchoring_bound.anchor`
   fields saying `m_p/m_e` are the ones that look wrong.
2. Decide whether `alpha_k_jones_markov_h12` should stay muon-pinned (it is an
   ideal-layer 3-CAL computation) or move to proton (the standing default for
   compute). Record the choice **in the producer**, not only here.
3. Only then migrate its convention C→D, so the result is not a straddle.

Found while answering a direct question about whether this session's work used
the correct pin. The work committed so far — `probe_1b_li6_orthogonality`, via
`y_lambda_at_q0_mpmath(18, q_parameter.Q)` — is **proton**, verified. This
producer is the next one on that list and is not.

## CORRECTION (2026-08-15): not stale data — a declared manifest entry, and a re-run cannot fix it

I filed this as a self-contradiction to be resolved by re-running the
producer. Measured: **the re-run reproduces it exactly**, and the mechanism
is a deliberate design I had not read.

`computations/q0_anchor_manifest.json` (schema `q0-anchor-manifest/v1`)
carries two lists, `ideal_muon` and the implicit proton remainder, and
[`substrate/q_parameter.py`](../computations/substrate/q_parameter.py) L90-103
auto-selects **by the running producer's stem**:

    _stem = Path(sys.argv[0]).stem
    if _stem in _man.get("ideal_muon", []):
        _anchor = "ideal"

`q_pinning_50_digit` **is on the `ideal_muon` list**. Under that branch
`q_at` is *redefined* to return the muon literal `_MUON_Q_STR`. So:

    python3 q_pinning_50_digit.py          -> q_at gives MUON   (stem matches)
    import q_pinning_50_digit              -> q_at gives PROTON (stem is "-c")

which is why the witness holds muon while a direct import of the same module,
through the same `q_parameter.py`, gives proton. Nothing is stale; the
producer is *declared* an ideal-layer (CAL-2 𝔇_β) artifact and behaves as
declared.

### What is actually wrong, then

Not the number — the **prose around it**. Under the muon override `q_at`
returns a *literal*; the Newton solve never runs. But the witness says:

    description                     "...derived from Vol(4_1) and m_p/m_e
                                    (CODATA 2022) through the proton
                                    substrate identity (q_parameter.q_at
                                    Newton solve)"
    calibration_inputs.anchor       "m_p/m_e"
    physical_anchoring_bound.anchor "m_p/m_e"

Three fields describe a proton derivation that did not execute in the run
that produced the file. The word "anchor" is doing three different jobs here
— the *layer* the witness reports at (`q0Anchor`), the *route* the code would
take absent the override (`calibration_inputs`), and the *uncertainty budget*
being quoted (`physical_anchoring_bound`) — which is why it reads as a
contradiction on a grep.

### Revised close

1. ~~Re-run the producer.~~ Does not help; verified.
2. Fix the prose so each field says which job it is doing, and say plainly
   that under the `ideal_muon` manifest entry the value is the muon literal,
   not a Newton solve. **Done in this commit.**
3. Leave the manifest entry alone. Whether *the* q-pinning witness should be
   the ideal or the physical artifact is an owner-layer call, not an agent's
   — AGENTS.md keeps the ideal framing for the canonical chain while the
   2026-08-07 directive moves *compute* to proton, and this witness is the
   canonical-chain artifact.
4. `alpha_k_jones_markov_h12` no longer depends on this: it was repinned to
   `q_parameter.Q_50_DIGIT_STR` (proton) earlier in this arc, so the
   downstream hazard this bean flagged is already closed.

### Generalisation worth carrying

**A producer's behaviour can depend on `sys.argv[0]`.** Importing a module to
inspect its constants can therefore give a *different* answer than running
it, with no error and no warning. Any anchor investigation that reads a
constant by import — as my first three probes here did — must confirm by
running the producer under its own name before concluding.


## 2026-08-19 — the file moved to PROTON, and that broke the muon anchor's definition

The contradiction above has since been "resolved" in the proton direction, and
nothing updated the consumer that treats this file as the *definition* of the
muon pin. Current committed state (identical on `origin/main`, on this branch,
and in the tree):

```
computations/q-pinning-50-digit.witness.json
  .q0Anchor                  "proton"
  .derived_50_digit.q        1.109978582751380807591669…   <- the PROTON value
  .computedAt                2026-08-15T11:35:10Z
  last touched by            9a9c6b31c "sweep(tnjb): first 25 witnesses
                             regenerated at the proton pin; driver fixes"
```

But `qou_substrate/witness.py::_q0_value_for_anchor` still reads exactly this
path as the muon pin:

```python
if anchor == "muon":
    p = _repo_root() / "computations" / "q-pinning-50-digit.witness.json"
    val = json.loads(p.read_text())["derived_50_digit"]["q"]
```

So, measured in this tree:

```
_q0_value_for_anchor("muon")   -> 1.109978582751380807
_q0_value_for_anchor("proton") -> 1.109978582751380807
```

**The two anchors now resolve to the same value, and it is the proton one.**
The muon pin has no definition left in the tree at the path its own accessor
points to.

### Consequence, measured

`computations/audits/q0_anchor_consistency_audit.py --strict` compares every
muon-anchored witness against `_q0_value_for_anchor("muon")`, so it compares
them against the *proton* pin and reports each as a flip:

```
FAIL (--strict): 262 Q0_FLIP witness(es).
  ... anchor=muon but q0Value=1.10997859555733… (expected 1.109978582751…)
```

The "expected" in that message is the proton value under the label `muon`,
which is the tell. The committed `q0-anchor-consistency-audit.witness.json`
records `computed: 0, allPassed: true` — on `origin/main` too, timestamped
2026-08-19T13:06Z — so the gate is reading green against a corpus in which the
comparand is wrong. Note the failure is one-sided by construction: if the muon
read had *failed* instead of returning the wrong value, `classify` returns
`Q0_VALUE_MISSING`, which is not counted as a failure and the gate goes green
anyway. Neither branch of that read can currently make the audit tell the
truth about a muon witness.

Reproduced in a clean `git worktree` at this branch's tip with no local edits,
so it is not an artifact of in-flight work; `9a9c6b31c` is on main.

### Not fixed here

Deliberately out of scope for `claude/convention-d-tranche-2026-08-18`, whose
diff is import paths. Recording it rather than patching, because the fix is a
ruling, not an edit: either the muon accessor needs a pin file that still holds
the muon value, or the muon anchor is retired and the 262 witnesses plus the
`muon` branch of `_q0_value_for_anchor` go with it. That is `qou-1c4y`
territory and needs the owner. Whichever way it goes, the LABEL and the
COMPUTED VALUE have to move together — the same discipline this function's own
docstring records having violated once already.


## RESOLVED 2026-08-19 — and the blast radius was 208 producers, not an audit nit

The entry above stopped at "the audit compares muon witnesses against the
proton pin". That understated it by a lot. `computations/substrate/q_parameter.py:113`
guards the muon override on the same file:

```python
_d = _json.loads(_QPIN.read_text())["derived_50_digit"]
if not _d["q"].startswith("1.109978595557"):
    raise ValueError(f"q-pinning witness q={_d['q'][:16]} not canonical muon")
```

and `q_parameter` refuses to fall back — correctly, per its own beans yfvb /
tnjb anti-corruption note. So on the committed tree every producer whose stem
sits in `q0_anchor_manifest.json` `ideal_muon` dies at import:

```
RuntimeError: q_parameter: ideal/muon anchor requested (QOU_Q0_ANCHOR='ideal')
but the muon override could not be established: ValueError('q-pinning witness
q=1.10997858275138 not canonical muon'). Refusing to fall back to proton
silently (bean yfvb / tnjb anti-corruption).
```

Measured over all 257 `ideal_muon` stems (all 257 have live files):

| tree | pin-guard failures | imports clean |
|---|---|---|
| committed (proton pin) | **208** | 47 |
| muon value restored | **0** | 253 |

Pre-existing on `origin/main` 391604e9f: a 20-producer sample fails 14/20
there, the other 6 dying earlier on import wiring. Fixing the wiring *increases*
what is visible here rather than causing it.

### Why it went unnoticed for four days

Two independent blindnesses, and both are worth recording because each one
alone would have been enough:

1. **The importability audit's own loader.** It ran `python3 -c "<loader>"
   <file>`, so `sys.argv[0]` was `-c`. `q_parameter` resolves the anchor from
   the argv *stem*, so no stem ever matched the manifest, every producer pinned
   to proton, and the muon branch was never executed. The audit reported all
   257 importable. Fixed in `5c1149565` — the loader now sets
   `sys.argv = [<producer filename>]`.

2. **The audit witnesses were green off dirty trees.** Committed
   `q0-anchor-consistency-audit.witness.json` records `Q0_FLIP: 0` at
   2026-08-19T13:06Z on main, while the committed pin file was already proton.
   Both are only true together if a producer had transiently rewritten the pin
   file back to muon in the working tree at run time. `Q0_OK 658 = 396 + 262`
   exactly — the same witness set moving between OK and FLIP as the comparand
   changes.

### Fix

`1f25060f2` restores the file's pre-sweep content from `9a9c6b31c^` — identical
key set, only values differ. This is a **restore, not a re-pin**: the proton
50-digit string already exists as `qou_substrate.constants.Q_50_DIGIT_STR`, so
regenerating this file at proton produced a duplicate of a constant we already
had and left nothing in the tree holding the muon value. It does not touch the
2026-08-07 proton-default directive, which governs what *new compute* pins to,
not whether the muon anchor still has a definition.

Result: pin-guard 208 -> 0, `Q0_FLIP` 262 -> 0, all blocking precision gates
green.

**The general lesson for the tnjb / qou-1c4y sweeps:** a witness that some
piece of infrastructure reads as *the definition of an anchor* is not a
migratable witness. Re-pinning it does not move a value to the other layer, it
removes the layer. Worth an exclusion list before the next batch runs.


## 2026-08-21 — NOT closeable: the restore reverted the prose fix, and a live consumer was straddling

Checked for closure and found item 2 alive again.

### The restore undid the prose fix

`1f25060f2` restored the pin file from `9a9c6b31c^` to recover the muon anchor
value. That worked — and it also reverted the §"Revised close" item 2 fix,
because the restore predates it and only the *value* was verified afterwards.
Measured on main before this commit: `q0Anchor: muon`,
`calibration_inputs.anchor: m_p/m_e`, and a description still claiming a
"proton substrate identity (q_parameter.q_at Newton solve)" that the
`ideal_muon` override means never ran. Exactly the contradiction this bean
opened on.

**General shape worth carrying: a restore-to-fix-A silently reverts fix-B in
the same file when only A is re-verified.** Neither commit was wrong; the gap
is that "did the restore preserve the other fixes to this file?" is nobody's
checklist item.

Fixed at the producer (`q_pinning_50_digit.py`) rather than by hand-editing the
witness, and re-run. The value is a fixed point, as this bean established —
`derived_50_digit.q` is byte-identical across the re-run.

### A live consumer was reading the contradiction and straddling on it

`probes/qbeta_habiro_residual_probe.py:99` was commented
`# --- 1. CANONICAL q₀ (live, proton-pinned) ---` and then computed at the
**muon** value, because it reads `calibration_inputs.anchor` (`m_p/m_e`, the
derivation ROUTE) as though it named the emitted layer.

Measured, so the severity is not guessed:

| | |
|---|---|
| straddle | 11.54 ppb |
| the probe's own stated q₀ budget (`sigma_CAL_q0_ppb`) | **0.0074 ppb** |
| ratio | **~1558x** |
| its 100x target (`target_100x_ppb`) | 7.8 ppb — *smaller than the straddle* |
| headline (`residual_N2_ppb_PRODUCTION`) | 1248 ppb vs 7.8 target |

So it does **not** flip the verdict — a ~160x miss either way — but the error
budget does not cover the error, and any statement about *reaching* the 100x
target is anchor-limited rather than physics-limited.

`_assert_anchor_matches_value()` now refuses to proceed when `q0Anchor` and
`derived_50_digit.q` disagree. It keys on `q0Anchor` (the LAYER) and
deliberately not on `calibration_inputs.anchor` (the ROUTE) — the route field
is *allowed* to say m_p/m_e while the override emits muon, so keying on it
would fire on the correct configuration.

**My first version of that guard could not fire.** Its threshold was `1.2e-8`,
above the `1.15e-8` separation it exists to detect; a synthetic
proton-under-a-muon-label passed with room to spare. A threshold set at the
size of the thing being detected detects nothing. Now `1e-10`, with a test
asserting `_STRADDLE_TOL < 1.15e-8` so it cannot regress that way again.

### Incidental: a stale CODATA uncertainty, found by the re-run

The re-run moved `m_p_over_e_err` `1.1e-07 -> 3.2e-08` and
`codata_relative_uncertainty` `2.853e-12 -> 8.300e-13`. Not drift: the live
table (`qou_substrate.constants.MASS_RATIO_P_E_ERR = float(_P_E.uncertainty)`)
carries **0.017 ppb**, and the committed witness plus this producer's own
docstring were both stale at **0.06 ppb**. Docstring corrected.

**`AGENTS.md` repeats the stale 0.06 ppb figure** (§q₀ anchor convention and
the canonical-chain cheat sheet). Not corrected here — that is a doc with an
owner-facing framing and the edit should be deliberate, but it is stale and
someone should take it.

### Remaining before this can close

1. Whether `qbeta_habiro_residual_probe` *should* be muon (it computes Q_β, the
   CAL-2 proxy, arguably ideal-layer) or proton (2026-08-07 default) is the
   "explicit reason" judgement, not an agent call. It now computes at muon and
   says so, instead of computing at muon and claiming proton — which is the
   part that was a defect either way.
2. The AGENTS.md 0.06 ppb staleness above.

---

# CLOSED 2026-08-21 — premise wrong, NOT done. Full evidence for re-opening.

**Do not re-file this as written.** The fix this bean asks for is a
**regression**, not a no-op. Everything needed to re-litigate is below.

## What this bean claimed

That `computations/q-pinning-50-digit.witness.json` self-contradicts:
`q0Anchor: muon` with muon numbers, while `calibration_inputs.anchor` and
`physical_anchoring_bound.anchor` say `m_p/m_e` — *"Both cannot be true. A
reader checking the anchor gets whichever answer they happen to grep for."*

## Why that is wrong: the three `anchor` fields have three different jobs

`computations/probes/qbeta_habiro_residual_probe.py`, in the docstring of
`_assert_anchor_matches_value` (lines 131–144 as of `ae571e445d`):

> The q-pinning witness uses "anchor" for three different jobs — the layer
> it reports at (`q0Anchor`), the derivation route (`calibration_inputs`),
> and the uncertainty budget (`physical_anchoring_bound`) — and a consumer
> that greps for one and computes with another straddles the layers with no
> signal at all. That is how this probe came to announce proton and compute
> at muon.
>
> So: compare the LAYER field against the emitted number and refuse to
> proceed when they disagree. **Checked against `q0Anchor`, deliberately, not
> against `calibration_inputs.anchor` — the route field is allowed to name
> `m_p/m_e` while the `ideal_muon` override emits the muon literal, and
> keying on it would make this guard fire on the correct configuration.**

So the current field values are **the correct configuration**, deliberately
arranged, with a live guard built around them:

| field | value | job |
|---|---|---|
| `q0Anchor` | `muon` | the **layer** reported at |
| `q0Value` / `derived_50_digit.q` | muon 50-digit | the emitted number |
| `calibration_inputs.anchor` | `m_p/m_e` | the **derivation route** (proton substrate identity) |
| `physical_anchoring_bound.anchor` | `m_p/m_e` | the **uncertainty budget** |

## What executing this bean would have done

1. **Fired `_assert_anchor_matches_value` on a correct file** — the guard's
   docstring says so explicitly.
2. **Risked the `qou-cezp` failure.** This witness *defines* the muon anchor:
   `qou_substrate.witness._q0_value_for_anchor("muon")` reads it. Commit
   `9a9c6b31c7` re-pinned it and produced **262 Q0_FLIPs** plus a hard
   `RuntimeError` on `QOU_Q0_ANCHOR=ideal|muon`, including on the producer
   that would regenerate the anchor. `q0_repin_sweep.py` now lists it under
   `ANCHOR_DEFINITIONS` for that reason.

## The real defect, found while investigating — fixed in PR #5378

`content/values/registry.ts:549` (`codata_rel_unc`) described its value as
*"CODATA relative uncertainty on **m_μ/m_e**"*, while the witness field it
reads is **proton**-derived:

| field | value | which pin |
|---|---|---|
| `physical_anchoring_bound.codata_relative_uncertainty` ← what registry reads | `8.30e-13` | **proton** |
| `physical_anchoring_bound.muon_cross_check_relative_uncertainty` | `1.223e-9` | muon, ~1470× looser |

Every `:val[codata_rel_unc]` in the paper rendered a proton σ under a muon
label. Corrected.

Plus three hardcoded CODATA-2018 figures in the producer's f-strings, now
computed: `limited_by` `0.06 ppb` → `0.017 ppb`; `description`
`2.85e-12 (2853 ppQ)` → `8.30e-13 (830 ppQ)`; and the bound comment.

## Verification that this closure is not itself stale

`ae571e445d` ("qbeta_habiro_residual -> PROTON, owner ruling") **modified the
very file** quoted above. The `_assert_anchor_matches_value` docstring is
**unchanged** by that ruling — checked, not assumed. So the reasoning here
survives the proton ruling.

## What WOULD justify re-opening

Any one of these, and none of them hold today:

1. The `_assert_anchor_matches_value` docstring is rewritten to drop the
   three-job distinction, or the guard is changed to key on
   `calibration_inputs.anchor`.
2. A consumer is found that reads `calibration_inputs.anchor` **as the layer**
   and computes with it. (Searched: the only readers are that probe, which
   reads it for display and checks `q0Anchor` instead, and
   `content/values/registry.ts`, whose defect was the *description*, now
   fixed.)
3. The owner rules that the route/layer distinction should collapse — i.e.
   that a muon-layer witness must also name `m_mu/m_e` as its route. That is
   a schema decision with corpus-wide blast radius, not a one-file relabel,
   and it must account for the `ANCHOR_DEFINITIONS` protection.
4. `q0Anchor` and `q0Value` are found to disagree — the thing the guard
   actually checks. They agree: `muon` / `1.10997859555733471989…`.

## Related

- `qou-cezp` (completed) — the 262 Q0_FLIPs this would have risked.
- `qou-1c4y` — the tracked muon→proton witness migration. **Distinct from
  this**: that is about which pin new compute uses, not how an
  anchor-defining witness labels its own route.
