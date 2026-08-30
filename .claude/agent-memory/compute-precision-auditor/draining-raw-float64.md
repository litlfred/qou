# Draining a raw-float64 field — the decision procedure

Companion to `MEMORY.md`. Read before draining anything.
Established 2026-08-30 draining `onepb-status-dashboard.witness.json` 3 → 1.

---

## The question is always "does an EXACT source exist upstream?"

Not "can I make this a string". Three outcomes, and only the first two are
drains:

| the value is | do this | why |
|---|---|---|
| **READ** from an exact source (a vendored table, a CODATA decimal, a spec constant) | emit the source's decimal text **verbatim** | it carries exactly the digits the source quotes |
| **COMPUTED** from exact inputs (exact rational / mpf at full working precision) | `_precision.fmt` at `OUTPUT_DPS` | every digit is determined by the inputs |
| a **float64 residue** with no exact source | **LEAVE IT A FLOAT** and say so | any serialization invents digits |

## TRAP — `fmt()` is NOT the universal answer, and using it on a READ value pads

`AGENTS.md` says "carry `mpmath.mpf` from its source and serialize with
`_precision.fmt`", and an agent reads that as a rule about *all* fields. It is
right for the **computed** row and **wrong for the read row**.

`fmt(mpf("2.2245662"))` → `2.22456620000000000000000000000000000000000000000000000000000` —
a 9-significant-figure measurement printed as if measured to 60. Worse, if the
value reached `mpf` via a `float`, you get the binary tail instead of zeros:
`"8.4817962000000015621026250300928950309753417968750000000000"`, which is the
padding audit's own worked example.

`computations/ame_2020_binding_energies.py` states the rule outright in
`_binding_mev_exact`'s docstring and is the exemplar to copy: parse with
`json.load(..., parse_float=str)`, carry `Decimal`, emit `str(Decimal)`.
`_precision` itself says `fmt` "is right for a value computed at full working
precision and wrong for one that reached mpf from a [limited] source".

## TRAP — a float→string flip in a witness is NOT automatically a drain

The ratchet counts **JSON floats**. A value that becomes a string leaves its
view whether or not it gained any information. Two ways this happens without
anyone intending it:

- **An upstream constant became an `mpf`.** `experimental_constants.M_E_MEV` is
  now `mpf`, so `x / M_E_MEV` is an `mpf` and the witness writer renders `mpf`
  as text. Measured on `rho_f_volume_binding_gap.py`: re-running the
  **unmodified** producer flipped 28 fields float→string and the committed
  witness was simply older than the constant change.
- **`mp.dps` was never raised.** `import _precision` leaves `mp.dps` at
  mpmath's default **15**. So those strings carried 15 significant digits —
  float64-grade, in string clothing the ratchet can no longer see.

**Before crediting a float→string flip as a drain, check both:** was
`set_compute_dps()` called, and what is the *divisor's* precision?

## TRAP — raising dps can make it WORSE, so check the ceiling first

`rho_f_volume_binding_gap.py` divides by a SnapPy volume that
`experimental_constants` stores as a **float64 literal quoted ±1e-12**
(`VOL_FIGURE_EIGHT`, `VOL_THREE_TWIST`; `VOL_BORROMEAN_50DPS_STR` is the one
exact one). At `dps=15` the quotient prints 15 digits; at `dps=70` it prints
the volume's **binary tail** out to 60. Calling `set_compute_dps()` there
would have manufactured ~48 fake digits per field while looking like the
textbook fix.

When the ceiling cannot be raised, **record it in the witness as data** rather
than let the serialization imply one (`data.precision_ceiling_note`). The
raw-float64 audit's own header names this pattern, citing
`jpsi_boundstate_mass_probe.py`: "a library (SnapPy) has its own precision
ceiling that must be recorded rather than assumed".

## TRAP — a residue at 2⁻⁵⁴ / 2⁻⁵⁵ is the arithmetic floor; trace it, do not drain it

`5.551115123125783e-17` is `2⁻⁵⁴`; `2.7755575615628914e-17` is `2⁻⁵⁵`. When a
"structural identity check" reports one of these, the number is measuring the
**rounding**, not the identity. Follow it to the producer before touching it.

Worked case: `onepb`'s `structural_max_non_anchor_delta_ppb` ← `codata-
reconciliation`'s `α₂ − z²` row ← `alpha/alpha_k_jones_markov_h3.py`, which is
**numpy float64 end to end** — `float(np.trace(M))` for the χ_λ table and
`np.linalg.solve` for the y_λ weights. There is no exact source to carry, so
there is nothing to serialize. It was left a float, with the reasoning written
at the *read site* so the next agent does not pad it.

## Verify a drain against the padding detector's own discriminator

Do not assert it. Import the audit and ask:

```python
import witness_float64_padding_audit as P
P.is_double_expansion(emitted_string)          # must be False
```

and build the counterfactual — `mp.nstr(mpf(<the float64>), 60)` — and confirm
that one **is** `True`. Measured on the 2026-08-30 drain, the honest value and
its padded twin diverge at **digit 18**, exactly where float64 information
ends. That contrast is the evidence; the absence of a filename in the audit's
output is not.

## Baseline drain mechanics

- Measure with the audit's **own** scanner, never by hand:
  `import witness_raw_float64_audit as A; A.scan()["computations/<w>.json"]`.
- A witness that reaches **0 is REMOVED** from `raw-float64-baseline.json`, not
  set to `0`. Removal is strictly stricter: a future regression then fails as
  **NEW** rather than being tolerated up to the old count.
- Update `files_count` **and** `fields_count`; they must equal `len(files)` and
  `sum(files.values())`.
- Rewrite with `json.dumps(..., indent=2, ensure_ascii=False)`. Without
  `ensure_ascii=False` the file's em-dash becomes `—` and the diff gains a
  spurious line.

## Separate YOUR reds from main's — by measurement

`scripts/precision-gates.sh` is red on arrival for reasons that have nothing to
do with you. **Stash your change, re-run the whole family on pristine
`origin/main`, and diff the two RED lists.** Absence of your filenames from the
output is weaker evidence and can mislead — a traceback path containing your
worktree name greps as a hit.

Measured 2026-08-30, identical before and after: `q0-anchor flip`,
`q0-anchor refill ratchet`, `mpf(<float>) source`, `float64-padding`,
`q0-value drift`, `mixed mpf/f64 -> serializer`, `witness scriptFile
provenance`.

**And do NOT commit an audit witness whose movement is main's.** The gate tells
you to regenerate stale audit witnesses; that is right only for the ones *your*
change moved. On 2026-08-30 `witness-float64-padding-audit.witness.json` moved
`new_not_baselined 0 → 4` from `option-e-phase1-gram-h6.witness.json`, which
landed on main in `6e08f1f570`. Committing it would have made the PR look like
it caused four new padding occurrences.

## Environment

Two gates cannot run here: `q0_value_drift_audit.py` and the padding audit's
own witness write both die on `ModuleNotFoundError: qou_substrate` unless
`tools/qou-substrate/python` is on `PYTHONPATH` (the package is **not**
pip-installable — 404 on PyPI). Add it alongside `computations/`.

A bare container has **mpmath 1.3.0 and no scipy/clarabel**, while the
committed witnesses record **mpmath 1.4.1, scipy 1.17.1, clarabel 0.11.1**.
`pip install "mpmath==1.4.1" "clarabel==0.11.1" "scipy==1.17.1"` before
re-running a producer, or the regenerated `environment` block silently records
*less* than the one it replaces. `sympy` declares `mpmath<1.4` and warns; the
pairing mpmath 1.4.1 + sympy 1.14.0 is nonetheless what this corpus records.
