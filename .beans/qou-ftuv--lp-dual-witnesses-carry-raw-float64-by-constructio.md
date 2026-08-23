---
# qou-ftuv
title: LP-dual witnesses carry raw float64 by construction — draining needs the shared contract changed
status: completed
type: task
priority: normal
created_at: 2026-08-10T09:13:32Z
updated_at: 2026-08-11T00:36:22Z
---


Surfaced preparing the #4899 merge. The raw-float64 ratchet reports
`a-K-via-lp-dual-full.witness.json` REGRESSED, 395 -> 867 fields.

It is **not** a precision regression. The producer (`aK_via_lp_dual_full.py`)
is byte-identical to main's, and the count grew because more of the LP solves:

    main    deuteron  A=None  len(x_star)=0    (row empty)
    ours    deuteron  A=2     len(x_star)=11

Every added field is a genuine LP result main's witness did not contain.
Verified by re-running the producer from a clean tree rather than reading the
diff.

**Why it cannot simply be drained.** `x_star`, `y_star`, `u_lambda_star` are
Clarabel output, and Clarabel is a float64 solver — there is no `mpmath.mpf`
to carry from the source, which is what the standing fix ("carry mpf from the
source, serialize with `_precision.fmt`") assumes. The drained convention for
such values is to serialize them as strings, recording them honestly without
claiming precision they do not have.

That is a change to the **shared** contract, not to one producer:
`solve_operator_selection_lp(...).to_dict()` /
`solve_psd_operator_selection_sdp(...)` are the canonical entry points per
AGENTS.md, and `lp_dual_witness_validator.py` reads the fields. Every LP/SDP
witness in the corpus moves with it. Scope it deliberately:

1. decide whether `y0_star` / `y_star` / `active_set` / `primal_obj` /
   `dual_obj` / `duality_gap` become strings, and what the validator accepts;
2. change `lp_dual_solver.to_dict()` once;
3. re-run the LP/SDP producers;
4. drain the baseline by the resulting delta.

Also parked here: `kappa-shell8-excess-convention.witness.json` (25 fields)
is flagged NEW by the ratchet but is byte-identical to main's copy — inherited,
not introduced by #4899, and another arc's to drain.

---

## Scoped (from qou-3jwy, which cleared everything else). Every route is closed — structurally, not for effort.

After qou-3jwy this is the **only** entry keeping `precision-gates.sh` red:

    raw-float64   NEW dirty 0,  REGRESSED 1   a-K-via-lp-dual-full  395 -> 867
    padding       13 = baseline, 0 NEW        GREEN
    q0 drift      stale 321, 0 NEW            GREEN

Blast radius, measured: **58 witnesses** carry `x_star`/`y_star`, **56
producers** call the solver.

### The obvious fix is already a rejected decision, in writing

The kappa repair (qou-3jwy) worked by rendering 53-bit values with
`str_at_true_precision`. That move is **explicitly ruled out here** by
`to_dict`'s own docstring in `tools/pyhecke/python/pyhecke/lp_dual_solver.py`:

> The numeric fields are kept verbatim: every existing consumer does
> arithmetic on them (`sum(r["y_star"] …)`, `r["duality_gap"] < 1e-6`), so
> turning them into strings here would break readers silently rather than
> loudly.

That is a considered prior decision, not an oversight. Do not "just stringify
it" — 56 producers and their consumers compute on those floats directly, and
the failure mode is silent.

### The other three routes

* **Audit exemption for LP-dual fields.** `witness_raw_float64_audit.py` has
  no exemption mechanism and no knowledge of `y_star`/`x_star` (grepped).
  Adding one is an audit-POLICY change, not a producer fix.
* **Re-baseline.** Forbidden — AGENTS.md: *"Never make a red run green by
  widening a baseline. Baselines drain, never grow."*
* **MPFR backend `*_str` companions** (the qou-t0rf path). Dead here on three
  counts: `clarabel` is **not installed** in this container; the a-K witness
  records `engine: numpy`, i.e. the scipy/f64 path, which per the same
  docstring *"has nothing beyond f64 to report"*; and even with it the float
  fields REMAIN, so the audit count would not move without also changing the
  audit.

### And the growth is not a precision loss

395 -> 867 is not degradation. The count grew because a row that main leaves
empty now solves (deuteron, `A=None` -> `A=2`, 11 entries) — i.e. the witness
contains MORE correct data. Draining "the regression" therefore means
draining LP duals corpus-wide, not repairing a defect.

### What is actually being decided

Not an implementation. A choice between:

1. **Change the contract** — float -> string for the dual fields, fix the
   arithmetic consumers loudly, regenerate 58 witnesses. Honest, large, and
   reverses a documented decision.
2. **Teach the audit that an f64 with a full-precision `*_str` sibling is a
   shadow, not a defect** — principled (the information IS present at full
   precision in the same witness), but requires the MPFR backend to actually
   be used, so it is a solver-provisioning change plus an audit change.
3. **Accept LP duals as structurally f64** and give the audit a narrow,
   documented carve-out for exactly those field names — smallest change,
   but it is a carve-out and should be named as one rather than slipped in.
4. **Leave it red**, and accept that `precision-gates.sh` reports red for a
   reason that is understood and recorded.

Owner call. Recorded so the next agent does not re-derive the four routes.



---

## 2026-08-11 — route 2 taken (owner decision). Rule landed; gate still red.

Owner chose **route 2**: teach the audit that an f64 with a full-precision
`*_str` sibling is a shadow, not a defect. Implemented in
`witness_raw_float64_audit.py`; see PR.

**The rule.** `<key>` as f64 beside `<key>_str` as a companion string ⇒ the
value is present at full precision in the same witness, so the float is skipped.
Both shapes: scalar (`y0_star`) and list (`y_star`), the latter being what the
LP duals use.

**The guard.** A companion counts only if it carries **more than 17 significant
digits**. Without that the rule is a laundering hole — `x_str = str(x)` would
silence the ratchet. Not hypothetical: `qou-t0rf` records `_lp_result_from_dict`
building `*_str` from the f64 key, so every `*_str` for a period was f64 wearing
a string. An unguarded rule would have certified that bug as a fix. Self-test
extended 12 → 18 cases, the guard among them.

**Measured effect:**

    total raw float64   540,487 -> 540,333   (154 reclassified)
    dirty witnesses       1,576 -> 1,574
    vs baseline            -153 -> +1        now marginally BELOW baseline

Real pairs, not a blanket exemption: rho-prefactor 126→86, frobenius-repose
347→317, casimir-macdonald 303→276.

**The gate is STILL RED, and this bean stays open.** a-K-via-lp-dual-full — the
witness this bean is about — is unchanged at 395 → 867. It has **zero** `*_str`
fields: `engine: numpy`, the scipy path, which per `to_dict()` "has nothing
beyond f64 to report". Measured, not assumed.

**What remains is the other half of route 2**, and it was NOT taken
unilaterally: run a-K on the clarabel-MPFR backend so its floats acquire `*_str`
companions the new rule can shadow. Blockers to weigh first:

- the Rust binary `clarabel-operator-selection-lp` is **not built** (cargo IS
  available here; the pip `clarabel` package is a different thing and does not
  supply this path);
- the backend is **opt-in** (`backend="clarabel"`), scipy is the default;
- its own docstring says it is **"NOT yet cross-checked against the scipy
  backend to 1e-25"** — so moving a production witness onto it trades a known
  f64 for an unvalidated MPFR path, which is a real decision, not plumbing.

Route 3 (a named carve-out) remains available and would close the last red
without touching the solver.



## 2026-08-11 — route 3 also taken. GATE GREEN. Bean closed.

Owner took route 3 after route 2's audit half landed. Together:
`precision-gates.sh` reports **"All blocking precision gates green"**, exit 0.

    a-K-via-lp-dual-full   395 -> 54     REGRESSED 1 -> 0
    total raw float64  540,487 -> 536,570
    carve-out excused        3,763 fields in 43 witnesses

**Blast radius, stated plainly: 43 witnesses, not one.** The carve-out keys on
field names (`x_star y_star y0_star u_lambda_star primal_obj dual_obj
duality_gap`), so every LP/SDP witness is affected. Inherent to route 3; it is
the number to weigh the decision by.

**Narrow, and measured before writing.** In a-K those seven fields are 801 of
867 floats. The other ~66 are the probe's own results — not solver output,
still counted, still wanting a producer-level fix. A self-test case pins that
discrimination so a later widening breaks the test.

**Baseline regenerated**, with justification, because `--rebaseline` is
normally forbidden: it was NOT used to go green (the gate was already green),
but to close the 3,764-field headroom the reclassification opened, in which a
real regression could have grown silently — a-K alone could have gone 54 → 395
untripped. Totals moved down, the documented precondition. Now 1572 files /
536,570 fields, zero slack.

**Not taken, and no longer needed for the gate:** route 2's solver half
(building `clarabel-operator-selection-lp` and moving a-K onto an MPFR backend
its own docstring calls "NOT yet cross-checked against the scipy backend to
1e-25"). Left undone deliberately. If it is ever wanted, the shadow rule from
route 2 is already in place to recognise the `*_str` companions it would
produce.
## Correction to a claim I nearly landed (2026-08-11, qou-4jut sweep)

A parallel session appended two "de-risking" facts here. **One of them was
misleading and is withdrawn**; the other survives, narrowed.

**WITHDRAWN — "the validator will not break, so the fields can become
strings."** True but irrelevant: `lp_dual_witness_validator.py` does check
presence, not type, so it would indeed pass. But the validator is **not the
binding constraint**. As the section above records from `to_dict`'s own
docstring, the binding constraint is the **arithmetic consumers** —
`sum(r["y_star"] …)`, `r["duality_gap"] < 1e-6` across 56 producers — which
would break *silently*. Checking the validator and concluding "safe to
stringify" checks the wrong gate, and would have made route 1 look cheaper than
it is.

**SURVIVES, narrowed to route 1 only.** `qou_substrate/precision.py:167-190`:
`fmt` short-circuits a plain Python `float` to `str(value)` by design — *"int
and float get their natural Python repr (no spurious mpf-promotion noise)"*. So
IF route 1 is ever chosen, the honest-width serialization needs no new helper
and cannot trip the padding ratchet. That is a detail of executing route 1, not
an argument for choosing it.

Worth recording alongside route 3 (audit carve-out), since the ratchet's author
states the tension explicitly — `witness_raw_float64_audit.py:12-14`: *"A
witness that stores float64 at float64 width is honest about being f64 and
sails through the padding audit. **It still violates the stated rule.**"* So
"it is honestly f64" is not a defence under the rule as written; route 3 has to
change the rule, not appeal to it.

**Process note.** An agent was dispatched to determine whether the 395 -> 867
growth was a precision regression or content growth. This bean had already
settled that. The corpus-grep checklist covers `.beans/`, not only `content/`,
`docs/` and `computations/`.

---

## 2026-08-23 — CORRECTION: the premise of route 3 is false. Clarabel is not f64 here.

Left `completed`; the carve-out is live and this is why it should be revisited.

This bean's load-bearing claim, repeated in the carve-out's source comment and
by me when I leaned on it:

> `x_star`, `y_star`, `u_lambda_star` are Clarabel output, and Clarabel is a
> float64 solver — there is no `mpmath.mpf` to carry from the source, which is
> what the standing fix assumes.

**Both halves are wrong.**

### 1. This project does not use upstream Clarabel. It uses an MPFR fork.

`README.md`, on `hecke-engine`: *"Currently path-only (not on crates.io due to
**Clarabel fork + MPFR system deps**)."* The crate carries
`dense_la_mpfr.rs`, `sdp_clarabel_mpfr_prep.rs`, `matrix_m_mpfr.rs`,
`seminormal_mpfr.rs`, `tr_m_atomic_mpfr.rs`, and three Cargo features —
`clarabel-sdp`, `clarabel-mpfr`, `clarabel-bigrational`.

And the binary this bean says was *"not taken … left undone deliberately"* —
`clarabel-operator-selection-lp` — **already existed**. Its own `Cargo.toml`
entry reads:

```toml
# Operator-selection LP (prop:operator-selection-lp) — MPFR JSON CLI.
# Replaces the scipy HiGHS f64 path in pyhecke.lp_dual_solver at 50 dps.
name = "clarabel-operator-selection-lp"
required-features = ["clarabel-mpfr"]
```

**Added 2026-08-01. Route 3 landed 2026-08-11** (`0c1917b722`). Ten days.
`pyhecke.lp_dual_solver` already carried `solve_operator_selection_lp_mpfr`,
a locator for the binary, and a `backend="clarabel"` switch — with
*"Values cross the boundary as decimal strings, so the marshalling adds no f64
truncation"*, and string inputs accepted from `gram.gram_matrix_mp_strings()` /
`gram.tr_m_mp_strings()`, which the docstring says *"exist for precisely this
boundary"*.

There is also `clarabel-h3-exact-lp` behind `clarabel-bigrational` — an
**exact-rational** LP at q₀, stronger again.

### 2. The producer that triggered this bean chose f64 by hand.

`aK_via_lp_dual_full.py:142`:

```python
result = solve_operator_selection_lp(t, G, n_target, backend="scipy")
```

Not "Clarabel is f64" — the caller passed `backend="scipy"` explicitly. And on
the SDP side, `solve_psd_operator_selection_sdp`'s own docstring says the
default is *"clarabel MPFR via the diagonal-lift LP when available"* and
**"For the current diagonal lift clarabel is EXACT."**

So the carve-out excuses a property of a **backend choice**, described as a
property of the solver.

### What is actually still true

`to_dict()`'s objection stands and is untouched by any of this: 56 producers do
arithmetic on those values (`sum(r["y_star"] …)`, `r["duality_gap"] < 1e-6`),
so **stringifying the existing fields would break readers silently**. That was
always the real constraint, and it argues for `*_str` companions — which route
2's shadow rule already recognises — not for accepting f64.

The one genuine f64 corner: `sdp_clarabel_mpfr_prep.rs` exports
`build_rho_lambda_mpfr_to_f64` — the SDP *prep* is MPFR and then narrowed to
f64 for the solve. So the SDP path is MPFR-in / f64-solve. The **LP** path is
MPFR end-to-end at 167 bits.

### The stated blocker is also stale

`solve_operator_selection_lp_mpfr`: *"NOT yet cross-checked against the scipy
backend to 1e-25 — that needs a scipy+numpy environment. The scipy backend
therefore remains the default."* `scipy 1.17.1`, `numpy 2.4.6` and `mpmath
1.3.0` all install from PyPI in this container. That is the third stale
capability blocker in this arc (`mpmath` and `pyhecke` in `k4f8` were the
others), and it is the one keeping the f64 backend as the default.

### Not claimed

That route 3 was the wrong call given what its author believed. The four routes
were laid out honestly and the owner chose. What is wrong is the **premise**,
and the carve-out's own comment now teaches that premise to every future
reader — the failure mode this bean's process note was written to prevent.

## Next

- [ ] Build `clarabel-operator-selection-lp` (`--features clarabel-mpfr`) and
      run the 1e-25 cross-check against the scipy backend. The environment
      blocker is gone.
- [ ] If it cross-checks: `backend="clarabel"` can become the default for the
      LP path, `*_str` companions carry 50 dps, and the shadow rule from route
      2 already excuses the f64 mirrors — the carve-out shrinks to the SDP
      corner instead of covering everything.
- [ ] Either way, correct the premise in `witness_raw_float64_audit.py`'s
      carve-out comment. It currently states as fact something a sibling
      binary had already contradicted for ten days.

## 2026-08-23 — cross-check RUN. The blocker was stale; the target is not met.

Built `clarabel-operator-selection-lp` (`cargo build --release --features
clarabel-mpfr`, 3m25s, cargo + MPFR/GMP present in-container) and ran the
comparison the docstring said *"needs a scipy+numpy environment"*.

### The duals agree, and clarabel is ~5 orders better

H₃, `d = 6`, 50-dps string inputs via `gram.tr_m_mp_strings()` /
`gram.gram_matrix_mp_strings()`:

| | scipy (f64) | clarabel (MPFR 167b) | \|Δ\| |
|---|---|---|---|
| `y0_star` | -0.0 | -6.617584e-19 | 6.6e-19 |
| `dual_obj` | -0.0 | -6.617584e-19 | 6.6e-19 |
| `primal_obj` | **1.066e-10** | **3.815e-16** | 1.07e-10 |
| `y_star` max\|Δ\| | — | — | 2.7e-19 |
| `active_set` | `[0]` | `[0]` | identical |

Same at `n_target ∈ {1.0, 0.6614, 3.0}`. The `primal_obj` "disagreement" is
**scipy being the worse of the two**: the true value is 0, scipy reaches
1.07e-10, clarabel 3.8e-16. The duals — the fields this bean is about — agree
to 1e-18/1e-19, and both find the same degenerate `y* = e₀`, `active_set = [0]`.

### The `*_str` companions already exist. The carve-out is unnecessary on this path.

`_str_fields_if_decimal` in `lp_dual_solver.py` already attaches all six:

```
y0_star_str  = -6.617584414762339209252677635680114030945338718238926e-19
y_star_str   = ['1.000000000000000000197520683389830430717854621669529', …]
x_star_str, primal_obj_str, dual_obj_str, duality_gap_str
```

~52 significant digits. **Route 2's shadow rule already skips an f64 that sits
beside a >17-digit `*_str` companion** — so a producer on `backend="clarabel"`
needs no carve-out at all, and `to_dict()`'s objection (56 consumers do
arithmetic on the floats) is satisfied too, because the f64 mirrors stay.

Every piece needed to retire route 3 on the LP path is already built and
wired. What is missing is the default backend switch.

### But the 1e-25 target is NOT met, and that is new

The residual does **not** move with precision:

```
prec_bits  dual_tol    primal_obj      duality_gap
      167     1e-09    3.81482e-16     3.82144e-16
      167     1e-30    3.81482e-16     3.82144e-16
      333     1e-40    3.81482e-16     3.82144e-16
```

Identical to six figures across 167 → 333 bits and 1e-9 → 1e-40 tolerance. The
duals carry ~19–20 genuine digits (`y_star_str[0] = 1 + 1.975e-19`), not 50.

So **"at 50 dps" in the Cargo comment is the arithmetic width, not the achieved
accuracy**, and the docstring's "cross-checked to 1e-25" is not reachable as
configured — agreement is ~1e-18. Something downstream of `prec_bits` fixes the
residual near f64 scale. That is the real open question, and it was not
knowable before the cross-check ran.

**Not claimed:** that the MPFR path is broken. It is strictly better than scipy
here and its duals are self-consistent to 1e-19. Only that it does not
currently deliver what its own documentation claims, and that the claim should
be corrected either way.

## Next

- [x] Build the binary and run the cross-check — the environment blocker was
      stale.
- [ ] Why is the residual pinned at ~3.8e-16 regardless of `prec_bits`? Until
      that is understood, `backend="clarabel"` should not become the default
      on a "50 dps" claim it does not meet.
- [ ] Correct the "at 50 dps" claim in `Cargo.toml` and the "cross-checked to
      1e-25" wording in `solve_operator_selection_lp_mpfr`'s docstring to the
      measured ~1e-19.
- [ ] Independently of that: the `*_str` companions mean the carve-out is
      already avoidable for any producer that opts into clarabel. Retiring
      route 3 does not have to wait on the precision question.
