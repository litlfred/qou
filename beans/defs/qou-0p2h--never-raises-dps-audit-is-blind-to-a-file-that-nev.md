---
# qou-0p2h
title: never_raises_dps_audit is blind to a file that never NAMES mpmath — 5 live, 1 fixed, all computing at dps=15
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T15:57:17Z
updated_at: 2026-11-16T19:29:47Z
parent: qou-9nnz
---

## The blind spot, measured on the same file at two revisions

`computations/never_raises_dps_audit.py` exists to catch exactly this class and
does **not** see `computations/probes/casimir_epsilon_vacuum_probe.py`, which
computed its entire Casimir force table at mpmath's default `mp.dps = 15`.

Verified by running the audit against the pre-fix file, not by reading its code:

    $ git show HEAD~1:...casimir_epsilon_vacuum_probe.py > <the file>
    $ grep -c set_compute_dps <the file>        ->  0
    $ python3 never_raises_dps_audit.py | grep casimir_epsilon_vacuum
    (no output)                                 <- NOT flagged
      runnable producers never raising dps : 9
      NEW (not baselined)                  : 4

**Why it is invisible.** The pre-fix file names mpmath **zero times** —
`grep -cE "mpmath|\bmpf\(" ` returns 0. Its only mpf enters by IMPORT
(`from experimental_constants import HBAR_MEV_S`), and every subsequent
operation — `HBAR_MEV_S * 1e6 * _EV_TO_J_SI_EXACT`, then
`-pi_sq * HBAR_C_J_M / (240.0 * d_m**4)` — is mpf arithmetic performed at
dps 15. The audit counts "mpmath value CONSTRUCTIONS", so a file that
constructs none and inherits one is outside its population by design.

This is the mirror image of a bucket the audit already reports. It has a
"raise dps only VIA AN IMPORT" tier (7 files) for producers that *do*
construct mpf and inherit the RAISE. The blind spot is the other direction:
inherit the **value**, construct nothing, never raise.

## How it surfaced, which is the reusable part

Not by reading the audit. By the **float64-padding ratchet** contradicting the
**raw-float64 ratchet** on a change I had just made and believed clean:

    raw-float64      12 -> 0     looked like a drain
    float64-padding   0 -> 9     `claims 0.100000000000000005551115123125...`
                                 `really  0.1`

`fmt` had serialized a 53-bit value to 60 digits. `_precision.py`'s own
docstring predicts this verbatim. **The two ratchets are not redundant:
draining one while feeding the other is the failure mode, and only the second
one sees it.** Fixed in `6d620dfbcfc`; 12 -> 0 raw and 0 padding, 58 fields in
/ 58 out, max move 3.483e-15.

## The live class: 5 files, and it is NOT 23

Narrowed by TYPE, not by name. A first pass looked for "arithmetic on a
constant imported from a known constants module, never names mpmath, never
raises dps" and returned **23** — but most import `Q` / `HBAR_Q` / `HBAR_Q_SQ`
from `q_parameter`, and those are **float64** (`Q = float(_d["q"])`), so
arithmetic on them is a plain float64 path, i.e. the qou-840k class, not this
one. Resolving each imported name's runtime type (`experimental_constants` has
24 mpf exports, `q_parameter` 11, `knot_volumes` 7) leaves **5**:

    computations/atom_mass_derived.py                      via M_P_MEV
    computations/b_over_a_evaluator.py                     via ALPHA_EM_INV
    computations/d_density_derivation.py                   via M_E_MEV
    computations/gap_a1_binding_k_sdp_feasibility.py        via M_E_MEV
    computations/probes/homflypt_operator_valued_probe.py  via Q_NEUTRON_MEV

Do not quote 23. It over-matches by ~4.6x on exactly the distinction that
makes this a separate defect from qou-840k.

## Not yet done, and deliberately

Each of the 5 needs its own verified fix — run unmodified first, diff every
field, check BOTH ratchets — because `set_compute_dps()` moves published
numbers (here, 10 fields at ~3e-15; in a cancelling quantity it would be
larger). Fixing them qualifies under the ASK-FIRST exemption "it increases
precision", so no owner sign-off is needed; what is **not** authorised is
doing it as a blind 5-file sweep.

**Recommendation (my judgement, not a finding):** fix the 5 one at a time in
the current raw-float64 drain arc, and separately widen
`never_raises_dps_audit.py` to count arithmetic on an imported mpf-valued
name. The detector change is the durable half — without it the next file of
this shape is invisible again.

## Related, and distinct from all three

- `qou-yh08` / `qou-fl9i` — files that set `mp.dps` **too low** (952 / 838
  sites at 50/40/30, sub-canonical). This bean is files that set it **not at
  all**, i.e. 15, and that the dedicated audit cannot see.
- `qou-840k` — `float()`-casts and imports of float64 constants. Adjacent, and
  the reason the 23 over-matched.
- `qou-j6gb` — `mpf_import_time_dps_audit` not wired into `precision-gates.sh`.
  A different audit; this one IS wired and still misses the file.

Row 46 for `docs/audits/2026-08-15-detector-blindness-taxonomy.md` (45 rows as
of 2026-09-14). Its family is 22/25/26 — *the interesting thing is assumed to
appear syntactically at this site* — one level up: here the assumption is that
a file computing in mpmath will MENTION mpmath.


## 🛑 THE REMEDY THIS BEAN IMPLIES IS A NO-OP ON ALL FIVE FILES (measured 2026-09-14)

This bean's population is correct and its diagnosis of the audit's blind spot is
correct. Its **implied fix is not.** An agent that adds `set_compute_dps()` to
these five files will change **nothing at all** and record it as a precision fix.

### The measurement

`set_compute_dps()` is `mp.dps = 70`. It only affects **mpmath** arithmetic.
Measured across all five files:

| file | mpmath mentions | `mpf(` | `mp.*` calls | `fmt(` |
|---|---:|---:|---:|---:|
| `atom_mass_derived.py` | **0** | 0 | 0 | 0 |
| `b_over_a_evaluator.py` | **0** | 0 | 0 | 0 |
| `d_density_derivation.py` | **0** | 0 | 0 | 0 |
| `gap_a1_binding_k_sdp_feasibility.py` | **0** | 0 | 0 | 0 |
| `probes/homflypt_operator_valued_probe.py` | **0** | 0 | 0 | 0 |

`grep -nE "mpmath|import mpf"` over all five returns **nothing**. There is no
mpmath arithmetic in any of them for `mp.dps` to raise.

This bean already records that the pre-fix file "names mpmath zero times" — it
treats that as the *audit's* blind spot, which it is. What it does not say is
that the same fact makes the dps fix **inert**.

### What they actually are: the qou-840k class, and worse than the label

**All five import a float64 `Q`, and none imports the `Q_MP` twin:**

```
atom_mass_derived            from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val
b_over_a_evaluator           from q_parameter import Q as Q0
d_density_derivation         from q_parameter import Q as Q0
gap_a1_binding_k_sdp_...     from q_parameter import Q as Q_FLOAT   (then Q0 = float(Q_FLOAT))
probes/homflypt_operator...  from q_parameter import Q, HA
```

So the mpf constant each one imports (`M_P_MEV`, `ALPHA_EM_INV`, `M_E_MEV`,
`Q_NEUTRON_MEV`) enters float64 arithmetic and is demoted on first contact with
`Q`. The mpf import is the only reason they appear in this bean's population, and
it is the part that does not matter.

`atom_mass_derived` is the clearest case and shows the real shape. Its entire
Gröbner-Shirshov reduction is float64 **by construction**, not by dps:

```python
def hecke_mul(t1, t2):
    result = {}
    ...
            result[w] = result.get(w, 0.0) + c1 * c2      # <- float seed
    return {w: c for w, c in result.items() if abs(c) > 1e-15}
```

`0.0` seeds a Python float and `c1 * c2` stays one. `M_P_MEV` enters once, at the
very end, as `E0_MEV = M_P_MEV / PROTON_TR` with `PROTON_TR` float64. Thirteen
float-seeded accumulators in that file; `b_over_a_evaluator` additionally uses
`math.log`; `gap_a1` imports scipy.

### And the ORDER matters — dps first MANUFACTURES padding

If a value computed from the float64 `Q` later reaches `fmt`, raising dps first
writes binary64 garbage at full width. Measured at `mp.dps = 70`:

```
Q      (float64) = 1.1099785827513808
Q_MP   (mpf)     = 1.1099785827513808075916690956107688798744991218736
rel |Q_MP - mpf(Q)| / Q_MP = 2.7246e-17

fmt(1 - 1/mpf(Q)) = 0.0990817160442585323856217273770931223272006069395152743184997
fmt(1 - 1/Q_MP)   = 0.0990817160442585078391771175189060639852583733894449264766881
                                      ^ diverges after 18 characters
```

The two strings agree for **18 characters**, so `fmt` on the float64-sourced
value writes **~45 characters of binary64 expansion**. That is the
`casimir_epsilon_vacuum` defect (9 padding hits) with its magnitude measured
generally: **fix `Q` -> `Q_MP` FIRST, never dps first.**

### Load-bearing thresholds, so this is not a mechanical conversion either

Converting these to mpf changes *structural* decisions, not just digits:

- `atom_mass_derived` prunes GS words at `abs(c) > 1e-15` in two places
  (`hecke_mul`, `reduce_nf`) — that threshold decides **which words survive the
  reduction**, and it is sized to float64 noise.
- `d_density_derivation` *classifies* coefficients at `1e-12`
  (`elif abs(dd - (-H_A_VAL / 2)) < 1e-12`) — deciding which exact value a
  coefficient equals.
- `gap_a1_binding_k_sdp_feasibility` selects the LP **active set** at
  `yi > 1e-9`, and falls back to `float("nan")` for `y0_star`.

Same class as the three 1e-40 thresholds and the two hoefsmit tolerances drained
on `claude/raw-float64-drain-2026-09-13`: a threshold sized to the arithmetic it
sits on has to be re-derived when the arithmetic changes, and re-deriving it is a
judgement, not a sweep.

### Corrected recommendation

**This bean should be re-scoped or closed into `qou-840k`.** Its five files are
float64 producers needing a real conversion plus a threshold re-derivation each —
the same verdict my own earlier note reached for `jet_knot_invariants` (171
fields) and `delta_q_decoration` (158): *"also lack the call but compute in float
throughout, so it buys nothing."* The five here are that same class; the mpf-const
import is incidental.

**What the bean is still right about, and it is the valuable half:** the audit
`never_raises_dps_audit.py` cannot see a file that never names mpmath, and that
blind spot is real and worth keeping. It just does not follow that the files it
misses are one-liners.

### Correction to my own recommendation, one turn earlier

I told the author that `qou-0p2h` was higher-value than more serializer drains
because "a producer at dps 15 is COMPUTING wrong, not merely recording short."
**That reasoning does not apply to these five.** They are not computing at dps 15
— they are computing in float64, which is a larger problem with a different and
more expensive fix. The conclusion that they matter more than serializer drains
may well survive; the argument I gave for it does not.

Baseline established anyway, so the next agent does not pay for it again:
`atom_mass_derived` unmodified-first reproduces its committed witness EXACTLY —
189 fields, 0 lost, 0 gained, 0 moved, 0 structural, witness not rewritten. Cost
~6 min wall (25.8 s on the first atom rising to 166.8 s on the last). Note its
current output is already `Δ = -100.0000%` against observed mass; that is
pre-existing and not a precision artefact.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-9nnz`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Progress Update (Round 49 — PR #8170)

- Extended `mp_value_calls(tree)` in `computations/never_raises_dps_audit.py` with `MPF_CONST_MODULES` so scripts that never name `mpmath` directly but import an `mpf` constant (`HBAR_MEV_S`, `M_E_MEV`, etc.) without importing a float64 `Q` (`qou-840k` lane) and perform `ast.BinOp` arithmetic on it are detected by the audit.
- Added `.claude`, `.git`, `.lake`, `node_modules` to `SKIP_DIRS` and added 2 new self-test cases (15 total).
- PR: https://github.com/litlfred/qou/pull/8170 (`8b83507c7e14547848b5b991bdd3396fc7f3a703`)
