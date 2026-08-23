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

## 2026-08-23 — FIXED. The tolerance never followed the precision.

The ~19-digit ceiling had a single cause, in
`tools/hecke-engine/src/operator_selection_lp.rs`:

```rust
// Tolerances: 1e-12 is achievable by BOTH the f64 and the MPFR IPM ...
// MPFR can be pushed tighter via a custom settings build.
let eps     = F::from_f64(1e-12).unwrap();
let eps_red = F::from_f64(1e-8).unwrap();
```

`prec_bits` set the MPFR working precision and **nothing else**. The IPM then
terminated at an f64-scale tolerance no matter how wide the arithmetic was —
which is exactly the measurement: 3.81482e-16 identically at 167 and 333 bits.
The author knew (*"can be pushed tighter via a custom settings build"*); the
consequence, that the documented "50 dps" was unreachable, was not recorded.

**No custom settings build was needed.** The caller already passes the
precision, so the tolerance can follow it: `0.8 · dps` for the main tolerance,
`0.5 · dps` for the reduced one, clamped so f64 reproduces the old `1e-12` /
`1e-8` exactly.

### The first attempt broke the f64 path, and the test caught it

Scaling by `prec_bits` directly fails, because the function's own doc says it
is *"ignored (harmless) for non-MPFR `F`"* — for `F = f64` it reports whatever
the caller asked for while the arithmetic stays at 53 bits. Asking the f64 IPM
for 1e-40 returned `InsufficientProgress`, and
`operator_selection_lp::tests::mpfr_agrees_with_f64` failed —
**the very cross-validation test the fixed constants were chosen to protect.**

So the scale factor is now `F`'s *probed* working precision — the largest `k`
with `1 + 10^-k ≠ 1` — capped by the requested `prec_bits`. ~15 for f64, ~50 at
167 bits, at most 300 additions, and it cannot disagree with the type in play.

### Result

```
prec_bits  ~dps    primal_obj      duality_gap     y_star[0] - 1
       53  16.0    -5.82077e-11    5.83356e-11     1.974e-13
      167  50.3     3.57331e-44    3.60031e-44     3.094e-46
      333 100.2     3.81494e-84    3.82144e-84     1.75e-87
      500 150.5     3.81501e-124   3.82144e-124    0.0
```

Before: **3.81482e-16 at every setting.** At 167 bits the duals now carry ~46
genuine digits, not ~19.

**Cross-check against scipy, `n_target ∈ {1.0, 0.6614, 3.0}`:**

```
|Δ y0_star|    ≤ 7.5e-46        active_set  identical, [0]
max |Δ y_star| ≤ 2.8e-47
primal_obj     scipy 1.07e-10   clarabel 3.6e-44
```

The docstring's "cross-checked to 1e-25" precondition is met by ~20 orders.

**Tests:** 7/7 in `operator_selection_lp` including `mpfr_agrees_with_f64`;
208/208 across the crate.

**Docs corrected:** the `Cargo.toml` "50 dps" note now says it is the achieved
accuracy and why it was not before; `solve_operator_selection_lp_mpfr`'s
docstring carries the measured cross-check in place of the stale
"NOT yet cross-checked … needs a scipy+numpy environment".

### The default is deliberately NOT changed

Switching `backend` to clarabel moves every LP/SDP witness in the corpus at
once and `to_dict()`'s f64 fields feed arithmetic in 56 producers. That is an
owner call, not a side effect of fixing a tolerance. What has changed is that
the precision objection to making it the default is gone.

## Next

- [x] Build the binary and run the cross-check.
- [x] Diagnose the ~19-digit ceiling — hardcoded tolerance, now derived.
- [x] Correct the stale precision claims in both docs.
- [ ] **Owner: make `backend="clarabel"` the default for the LP path?** With
      the tolerance fixed, the `*_str` companions carry ~46 digits and route
      2's shadow rule already excuses their f64 mirrors — so the route-3
      carve-out becomes unnecessary on the LP path without touching
      `to_dict()`'s contract. That is the concrete way to shrink `qou/f7af`'s
      4,052 excused fields.
- [ ] The SDP path is still MPFR-in / f64-solve
      (`build_rho_lambda_mpfr_to_f64`); the carve-out stays justified there.

## 2026-08-23 (second) — SDP path: the f64 was at the OUTPUT boundary, not the solve

**Correction to my own note above.** I wrote *"the SDP path is still MPFR-in /
f64-solve (`build_rho_lambda_mpfr_to_f64`); the carve-out stays justified
there."* Wrong on both halves for the path that actually runs.

`solve_psd_operator_selection_sdp` enforces `M(x) = diag(Gx) ⪰ 0`. A PSD
constraint on a **diagonal** matrix is componentwise non-negativity — it is the
operator-selection LP. And `_solve_psd_via_clarabel_lp` says so and does so:

> "the faithful MPFR port delegates to the verified LP solver
> (`_solve_operator_selection_lp_clarabel`) … the PSD matrix's eigenvalues are
> its diagonal entries `(Gx)_i`."

So the diagonal-lift SDP has been solving at 167 bits all along, and after the
tolerance fix it is accurate to ~44 digits. `build_rho_lambda_mpfr_to_f64` is a
**different** path — the dense lift — and not what this entry point calls.

### The actual leak

`SdpDualResult.to_dict()` did

```python
"primal_obj": float(self.primal_obj),
"duality_gap": float(self.duality_gap),
"eigenvalues": list(self.eigenvalues),
```

and had **no `*_str` companions at all**, while `_solve_psd_via_clarabel_lp`
dropped `lp.x_star_str` / `lp.y_star_str` / … on the floor when repacking. A
~50-dps solve reached its witness as f64.

That is verbatim the defect `qou-t0rf` fixed for `LpDualResult` — whose own
docstring records it: *"`_lp_result_from_dict` kept them on the dataclass but
`to_dict` dropped them again, so a ~50-dps solve still reached its witness as
f64"* — and it was never fixed for the SDP twin.

### Second leak: the eigenvalues were recomputed in numpy

`gx = (G_f @ x_star)` with an f64 `x_star`, re-truncating the MPFR solve even
if the companions had been carried. Now recomputed with `mpmath` from
`x_star_str` at the solve's own working precision when available.

It matters here more than usual, because `x*` has entries of order `2.7e5` and
the tight constraint is a near-total cancellation:

```
(Gx)_0    f64   +8.003553e-11
          mpfr   3.48674832724324827173100129759035917630359719874442870395486e-44
```

Complementary slackness says `(Gx)_0 = 0` exactly at the active constraint.
The f64 value is 33 orders from it; the companion is at the solve's accuracy.

### Fixed

`SdpDualResult` gains `X_star_str`, `Z_star_str`, `primal_obj_str`,
`dual_obj_str`, `duality_gap_str`, `eigenvalues_str`, populated from the MPFR
solve and emitted by `to_dict()` alongside the f64 fields — same shape as
`LpDualResult`, so `to_dict()`'s arithmetic-consumer contract is untouched, and
route 2's shadow rule can now excuse the f64 mirrors on **SDP** witnesses too.
On the cvxpy/SCS path the companions stay `None` and `to_dict()` emits exactly
the seven keys it always did (asserted).

**Tests:** 193 passed / 44 skipped / 0 failed across `tools/pyhecke`; 208/208
in the Rust crate.

### What is genuinely still f64

Only the **dense** PSD lift — off-diagonal correlations / moment matrix — which
needs Clarabel's actual PSD cone. `sdp_clarabel_mpfr_prep.rs` records the
blocker: upstream defines `MaybeBlasFloatT: BlasFloatT + Copy` under
`cfg(feature = "sdp")` because *"the SDP code paths (chordal decomposition,
dense 3x3 eigen/svd, BLAS Cholesky) … contain hundreds of by-value reads"*, and
`MpfrFloat` is not `Copy`.

**But this is `litlfred/Clarabel.rs`, a fork** — so "upstream defines" is a
statement about a file in this repo's own dependency tree, not an external
constraint. The bound is `Copy` on a marker trait, and the fork has already
carried larger changes (`RealConst`, `RealSentinel`, `BitWidthDiagnostic`,
`MpfrFloat` itself). Whether relaxing it for the SDP paths is worth the
by-value-read churn is a scoping question, not an impossibility — and the
audit that concluded "not implementable"
(`docs/audits/exact-sdp-feasibility.md`) was reasoning about upstream.

## Next

- [x] Excise f64 from the diagonal-lift SDP path — companions carried,
      eigenvalues recomputed at precision.
- [ ] The dense PSD lift: scope relaxing `MaybeBlasFloatT: Copy` in the fork
      for the SDP code paths, or an MPFR eigensolver. Re-read
      `docs/audits/exact-sdp-feasibility.md` first — it may be reasoning about
      upstream Clarabel rather than this fork.
- [ ] Re-run the SDP producers so the committed witnesses pick up the
      companions, then re-measure `qou/f7af`'s excused count.

## 2026-08-23 (third) — producers pick it up automatically; and a SECOND laundering hole

### `backend="auto"` now serves MPFR, with no producer change

With `clarabel-operator-selection-lp` on disk, `solve_psd_operator_selection_sdp`'s
default `backend="auto"` selects it and returns all six `*_str` companions.
Every producer calling the default gets 50-dps results the moment the binary
is built — **the build IS the switch.** Worth knowing for CI and fresh
containers, where an unbuilt binary silently falls back to cvxpy/SCS f64.

### The rounding was destroying the value, not truncating it

`nucleus_operator_selection_sdp.py` recorded

```python
row["sdp_primal_obj"] = round(sdp.get("primal_obj", 0.0), 6)
```

On the MPFR backend that quantity is ~4.2e-44, so `round(…, 6)` wrote **`0.0`**
into the witness. Not a lossy copy — the value gone. Fixed to emit the solver's
value; the witness now carries

```
sdp_primal_obj       4.203895392974451e-44
sdp_primal_obj_str   4.203895392974451212771188749869748393840785825629547e-44
```

### That exposed a second hole in the shadow rule

`_is_full_precision_shadow` checked only that the companion carries **more than
17 significant digits**. It never checked that the companion describes the
**same number**. So the pair

```
sdp_primal_obj = 0.0     sdp_primal_obj_str = "4.2038…e-44"   (52 digits)
```

would have been excused as "f64 convenience copy + exact value", while the copy
was zero — and a consumer doing arithmetic on it, the reader the whole rule
exists to keep served, would get zero.

Sibling of the hole the rule already guarded (`qou-t0rf`: `x_str = str(x)`,
too *few* digits). Same shape, opposite direction, and I walked into it by
adding a companion to a rounded field.

**Closed**, with the tolerance chosen deliberately: **1e-9 relative, not f64
epsilon.** The defect is a companion describing a different number — a relative
error of 1 in the case above. Demanding correct rounding would also reject
hand-written fixtures and producers that truncated a float for display, which
is sloppy but not laundering, and would make the rule brittle for no gain.

**Measured before landing: 236 shadow pairs in the live corpus, 236 agree, 0
disagree.** Rejects nothing that was already honest.

### Correction: the self-test DID exist

I wrote above that `ftuv`'s claimed self-test "was never committed — grepped
2026-08-23", and started writing a second one. Wrong: `self_test()` is at
`witness_raw_float64_audit.py:490` and is thorough. I grepped `_selftest` /
`def test_` / `selftest` and missed `self_test`. My duplicate was removed and
the three new cases went into the existing suite instead — **25 cases, all
passing**, including both directions of the laundering guard.

### Verification

```
witness_raw_float64_audit --self-test   25/25 PASSED
witness_raw_float64_audit --strict      NEW 0, REGRESSED 0, exit 0
lp_dual_witness_validator --strict-wired  3/3 wired OK
pytest tools/pyhecke                    193 passed, 44 skipped, 0 failed
```

### `qou/f7af`'s 4,052 is unchanged, and why

The carve-out count moves only when an **LP** producer switches to
`backend="clarabel"`, and none has — that is the owner call this bean parked.
The SDP work above adds companions on a path whose field names
(`sdp_*`, `X_star`, `eigenvalues`) were never in `LP_DUAL_F64_FIELDS` anyway.
The mechanism is now proven end-to-end on committed data; what remains is the
decision, not the machinery.

## Next

- [x] Re-run an SDP producer so a committed witness carries the companions.
- [x] Close the agreement hole in the shadow rule, with a self-test case.
- [ ] **Owner: switch the LP producers to `backend="clarabel"`?** That, and
      only that, moves `f7af`'s 4,052.
- [ ] CI/fresh containers fall back to f64 silently when the Rust binary is
      unbuilt. If the MPFR path is meant to be the norm, that fallback should
      be loud — or the binary should be built in the gate.

## 2026-08-23 (fourth) — the fallback is now audible, and the witness says how it was solved

The remaining silent failure: `backend="auto"` picks clarabel-MPFR when the
Rust binary is on disk and scipy f64 when it is not, **with nothing printed and
nothing recorded**. Same producer, CI vs fresh container vs developer box,
writing witnesses whose residuals differ by ~28 orders of magnitude — and no
way to tell them apart afterwards. A witness that does not record how it was
solved is indistinguishable from one solved the other way.

That needed no ruling: it changes no numbers, only whether the difference is
visible.

**Provenance on the result, emitted by `to_dict()`** — `LpDualResult` and
`SdpDualResult` both now carry

```
backend         "clarabel-mpfr" | "scipy-highs"
precision_bits  167             | 53
```

**And the downgrade warns.** `QOU_REQUIRE_CLARABEL=1` already turned it into an
error, but the default path said nothing. It now raises a `RuntimeWarning`
naming the consequence (~16 digits instead of ~46) and both remedies.

Verified on all three paths:

```
clarabel available (auto)   backend='clarabel-mpfr'  bits=167  primal_obj +3.5733e-44   companions: yes
forced scipy                backend='scipy-highs'    bits=53   primal_obj +1.0662e-10   companions: no
clarabel missing (auto)     backend='scipy-highs'    + RuntimeWarning raised
```

### First movement on `qou/f7af`'s number: 4,052 → 4,004

Re-running `binding_sdp_bondgraph_degenerate.py` — no backend argument, just
the default — picked clarabel because the binary now exists, so its 48 carved
fields gained `*_str` companions and became **shadowed rather than carved**.
Its `y0_star` sharpened from `-0.0` to `-7.472446261721805e-46` in the process.

So the excused count moves **without** the owner decision, one producer at a
time, as producers are re-run in an environment where the binary is built. The
owner call is only about switching producers that *force* `backend="scipy"` —
`aK_via_lp_dual_full.py` being the one this bean was filed over, at 812 fields.

### Verification

```
witness_raw_float64_audit --self-test    25/25 PASSED
witness_raw_float64_audit --strict       NEW 0, REGRESSED 0, exit 0
                                         excused 4,052 -> 4,004 in 45 witnesses
lp_dual_witness_validator --strict-wired 3/3 wired OK
pytest tools/pyhecke                     193 passed, 44 skipped, 0 failed
```

## Next

- [x] Make the silent f64 fallback loud — warning + `backend` / `precision_bits`
      recorded in every result and witness.
- [ ] **Owner: switch the producers that force `backend="scipy"`.** That is
      now the only remaining lever, and `aK_via_lp_dual_full.py` (812 fields)
      is the whole reason this bean exists.
- [ ] Consider building the Rust binary in the gate, so CI does not quietly
      run at f64 while local runs are at 50 dps. The warning makes the
      divergence visible; building it removes the divergence.

## 2026-08-23 (fifth) — no float64 in CI

Two mechanisms, because either alone leaves a hole.

### 1. CI builds the MPFR solver, and a missing binary is an ERROR

`lp-dual-gate.yml` now installs `libgmp-dev`/`libmpfr-dev`, builds
`clarabel-operator-selection-lp --features clarabel-mpfr` (cached on
`Cargo.lock`; cold build ~3.5 min), and runs the whole job under
**`QOU_REQUIRE_CLARABEL=1`** so the fallback raises instead of downgrading.

Then it *proves* the binary took effect rather than assuming it:

```python
d = solve_operator_selection_lp(t, G, 1.0).to_dict()
assert d.get("backend") == "clarabel-mpfr", (
    f"CI solved with {d.get('backend')!r} — the MPFR binary did not take "
    "effect, so every witness this job could produce would be f64")
assert "y0_star_str" in d
```

A build step that succeeds while the binary is never found is exactly the
"absent check indistinguishable from a passing one" shape this whole arc keeps
turning up; the assertion is what closes it.

Verified locally, both directions:

```
with the binary      backend='clarabel-mpfr'  bits=167  primal_obj 3.5733e-44   ASSERTIONS PASS
binary missing + Q_R_C=1   RuntimeError: "refusing to fall back to scipy float64"
```

### 2. A committed f64-solved witness FAILS the gate

Building the binary only protects solves that happen *in* CI. A witness
produced on a box without it and committed would still sail through. So
`lp_dual_witness_validator.py` now reads the `backend` provenance and fails on
any flagged witness recording a float64 solver (`scipy-highs`, `cvxpy`, `scs`,
…), including the prefixed forms producers use for a second solver in one row
(`sdp_backend`, `lp_backend`).

**Ratchet, not sweep.** A witness with *no* `backend` field is reported and not
failed — 26 of the 27 flagged predate the field, and blocking on that backlog
would block every unrelated PR. Same scoping as the vacuity ledger gate and
`probe-float64-gate`.

**Shown to fail before being trusted.** Planted a fixture pair (a script
importing `linprog`, a witness recording `backend: "scipy-highs"`):

```
✗ float64 backend: 1 flagged witness(es) record a float64 solve:
  ✗  _tmp_f64_gate_probe.witness.json   backend=scipy-highs
Exit 1 (--strict mode).                       exit=1
fixture removed →                             exit=0
```

### Verification

```
lp_dual_witness_validator --strict-wired   exit 0
witness_raw_float64_audit --strict         NEW 0, REGRESSED 0, excused 4,004/45
witness_raw_float64_audit --self-test      25/25 PASSED
pytest tools/pyhecke                       193 passed, 44 skipped, 0 failed
```

### Still true, and worth stating plainly

All workflows in this repo are `workflow_dispatch:`-only under the 2026-06-30
Actions-billing directive, so none of this fires on push. It runs on demand and
locally. That is a property of the repo's CI posture, not of these gates.

## Next

- [x] Build the Rust binary in the gate; make a missing binary an error.
- [x] Fail CI on a committed witness that records a float64 solve.
- [ ] **Owner: switch the producers that force `backend="scipy"`** —
      `aK_via_lp_dual_full.py` at 812 fields chief among them. The new gate
      does not catch those: they record `backend="scipy-highs"` *honestly*,
      and forcing that backend is a deliberate choice the gate should not
      override on its own.
