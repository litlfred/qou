# The `q0Anchor: "independent"` disposition, adjudicated two ways

Bean `qou-324i` (the disposition's blind spot) under the migration bean
`qou-1c4y`. Measured on `main` at `cdbdc84af1`, 2026-08-28.

## The claim under test

Fifty-three committed witnesses declare `q0Anchor: "independent"` — *the
compute never reads q₀*. Five of them justify it with one sentence, copy-pasted
verbatim:

> "Reads no substrate value. PROVED by running this producer under
> `QOU_Q0_ANCHOR=muon` and `=proton` and diffing the emitted witness: the only
> non-ephemeral leaves that differ are `q0Anchor` and `q0Value` THEMSELVES —
> every substantive field is byte-identical."

That is a falsifiable experiment, stated in the artifact. This audit runs it,
and separately asks a question the experiment cannot answer about itself:
**can the override even reach this producer's q₀?**

## Why one test is not enough — and why the other is not either

`QOU_Q0_ANCHOR` is read by `q_parameter` at import. It moves a producer's q₀
**only** when the q₀ arrives through `q_parameter` / `qou_substrate.constants`.
Measured directly:

```
QOU_Q0_ANCHOR=physical  Q_50_DIGIT_STR = 1.1099785827513808075916690956…
QOU_Q0_ANCHOR=ideal     Q_50_DIGIT_STR = 1.10997859555733471989976322048…
```

So the override does work — for that path. Three paths defeat it, and on each
one a byte-identical flip is guaranteed *a priori*:

| defeater | why the override misses it |
|---|---|
| a q₀-shaped **literal** in code | an env var cannot change a string constant |
| a direct read of **`q-pinning-50-digit.witness.json`** | never consults `q_parameter`; the muon anchor-defining witness |
| a **peer import** — a q₀-bearing name from another producer | the pin is resolved in the peer, at its own layer |

The converse is equally true and was the bigger source of error here: the
static cone check (`q0_independence_checker`) reports a VIOLATION when *any*
module in the transitive import cone reads q₀, which is not the same as this
producer computing at one. **Both tests over-report in opposite directions, so
neither is a verdict on its own.**

## Verdicts

Nine witnesses are flagged VIOLATION by the static cone check. Adjudicated:

| producer | flip verdict | static evidence | verdict |
|---|---|---|---|
| `qbeta/qbeta_c3_rung_structure_analysis` | **MOVES, 5 fields** incl. `/data/at_q_0/c_3_full` | `Q_50_DIGIT_STR` via `q_parameter` | **DEFECT — substantive** |
| `probe_he4_magic_baryeven_prune` | **MOVES, 1 field** `/parameters/q0` | `Q0 = mpf(Q_50_DIGIT_STR)`, then `f(Q0)` in the prune predicate | **DEFECT — label** |
| `probes/lambda_scale_substrate_probe` | clean | reads `q-pinning-50-digit.witness.json` | **DEFECT — flip is blind** |
| `markov/markov_identity_symbolic_probe` | moves (see mask note) | two q₀ literals in code | **flip-blind; disposition needs the source check** |
| `probes/chi_content_eigenbasis_probe` | clean | imports `Q` = `sp.symbols('q')` | **FALSE POSITIVE — `independent` is correct** |
| `probes/eigenbasis_structural_lemmas_probe` | (pending) | imports `Q` = `sp.symbols('q')` | **FALSE POSITIVE — `independent` is correct** |
| `habiro/habiro_witness_convention_adjudication_probe` | (pending) | cone-only, via `hecke_laurent_fast` | pending |
| `qbeta/qbeta_habiro_f_from_shape_collapse` | (pending) | `Q_50_DIGIT_STR` via `q_parameter` | **sibling-claimed, not touched here** |
| `qbeta/qbeta_rung1_div25_framing_squared_test` | (pending) | `Q_50_DIGIT_STR` via `q_parameter` | **sibling-claimed, not touched here** |

### The sharpest one

`qbeta_c3_rung_structure_analysis` declares that every substantive field is
byte-identical under the flip. Running that experiment moves **five** fields,
and the example the diff surfaces is `/data/at_q_0/c_3_full` — the c₃ rung of
the Q_β precision ladder, a headline quantity. The artifact asserts an
experiment whose result refutes it.

### A false positive I nearly wrote up as a defect

`chi_content_eigenbasis_probe` and `eigenbasis_structural_lemmas_probe` import
`Q` from the peer module `hoefsmit_symbolic`. A peer-import detector keyed on
the *name* indicts both. Line 57 of that module reads

```python
Q = sp.symbols('q', positive=True)
```

— a sympy symbol, not a q₀. Both dispositions are correct, and the flip
confirms it independently (`clean`). The guard is now in the checker and in its
`--selftest`, alongside the known **true** positive
(`chirality_topology_binding_probe`'s `from hecke_channel_binding_probe import
Q0`, where `Q0 = Q_MP` is numeric), so a future narrowing cannot lose either
direction silently.

### A mask gap in the flip harness, found by using it

`markov_identity_symbolic_probe` reports three moved fields, the first being
`/results/0/bridge/elapsed_sec`. `anchor_flip_straddle_audit.EPHEMERAL` masks
`elapsed_seconds` but not `elapsed_sec`, so at least one of the three is the
harness measuring itself. Reported as such rather than as a defect count.

## Two harness defects, measured

1. **The flip runner does not set `PYTHONPATH`.** `anchor_flip_straddle_audit`
   runs a producer with `cwd=<producer dir>` and nothing else, so a producer
   importing a sibling under `computations/` exits non-zero and is reported
   `RUN-FAIL … UNTESTED`. Measured on `chi_content_eigenbasis_probe` and
   `eigenbasis_structural_lemmas_probe`: **exit 1 plain, exit 0 with
   `PYTHONPATH=computations:.`, zero tracebacks either way.** This is the
   producer-runner hazard AGENTS.md records at length; that gate is live in
   `scripts/staleness-gates.sh`, so it currently under-reports.

2. **Nothing runs `q0_independence_checker`.** It is referenced only by its own
   usage lines and one docstring. A checker no gate invokes is documentation.

## What this does NOT claim

* Nine flagged is not nine defects — two are false positives and two are left
  to their claiming sibling.
* A `MOVES` verdict is not automatically a straddle. It refutes *independence*,
  which is the only claim under test here.
* The static cone check remains correct about its own question; it is being
  used outside it, deliberately, and the disagreements are the finding.
