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
- [x] **Owner: switch the producers that force `backend="scipy"`** —
      `aK_via_lp_dual_full.py` at 812 fields chief among them. The new gate
      does not catch those: they record `backend="scipy-highs"` *honestly*,
      and forcing that backend is a deliberate choice the gate should not
      override on its own. **Owner ruled: switch them.** See below.


---

## The forced-`scipy` sites, enumerated and switched (2026-08-23)

Owner asked what was still overriding the backend and why. Twelve sites forced
`backend="scipy"`. Their stated justifications, verbatim from the source:

| justification | sites |
| --- | --- |
| "Pin scipy: committed-witness producer → byte-deterministic" | 4 |
| "availability varies by environment; f64 is ample" | 1 |
| *(no reason given at all)* | 5 |
| comparison harness — scipy is the point | 1 |
| already on clarabel | 1 |

**The byte-determinism reason never distinguished the backends.** Measured it
rather than reasoning about it: six identical clarabel-MPFR solves produced one
output hash. Byte-determinism is true of *both* paths, so it was never a reason
to prefer either.

The real concern underneath it was different and legitimate: `backend="auto"`
chose silently by whether the Rust binary happened to be built, so the same
script could produce f64 or MPFR numbers depending on the box. Pinning answers
that — but pinning to `clarabel` answers it just as well as pinning to `scipy`,
and `QOU_REQUIRE_CLARABEL=1` turns a missing binary into an error instead of a
changed answer.

**Eleven of twelve switched to `backend="clarabel"`.** The twelfth,
`clarabel_lp_crosscheck.py`, keeps scipy deliberately: it is the harness that
compares the two, so removing scipy would remove the comparison.

## The same truncation, a third time — in the producers

Switching the backend was necessary and not sufficient. Seven of the
regenerated witnesses still recorded **no backend at all**, and none carried a
single full-precision digit, because the producers do not serialize via
`to_dict()`. They cherry-pick the numeric fields off the result and
`float(...)`-cast each one:

```python
"primal_obj": float(res_dict["primal_obj"]),
"y_star": [float(y) for y in res_dict.get("y_star", [])],
```

That is the *same* defect `qou-t0rf` fixed on the dataclass and this module's
`to_dict` docstring describes fixing again one layer up — recurring a third
time, one layer further out. The solver produced 51 digits; the last step threw
50 of them away.

Fixed once, in `pyhecke.lp_dual_solver.provenance(res)`, spread into each
producer's row. It accepts a result dataclass *or* its `to_dict()` — producers
hold both forms, and a helper that silently returned `{}` for the dict form
would be another absent check indistinguishable from a passing one. New `*_str`
fields are picked up from one `PROVENANCE_STR_FIELDS` tuple rather than needing
a matching edit in ten producers.

## Two stale claims retracted

**`ak_lp_dual_quotient_probe.py`** carried, next to its f64 duals:

> float64-intentional: … the solver … works in double precision. There is no
> exact route to a number the solver only ever computed as a double.

Accurate when written about the scipy path; **false** once the backend was
pinned to clarabel-MPFR at 167 bits. Rewritten to say why those fields stay f64
(consumers do arithmetic on them) and to point at the `*_str` companions that
now carry the exact decimals.

**`nucleus_operator_selection_sdp.py`** contained both halves of the same
argument three lines apart. Its SDP block refuses `round(..., 6)` — "the value
destroyed outright, not merely truncated" — while its LP block did exactly that
to the row above:

```
lp_y0_star     0.0        ← round(-2.4e-43, 5)
lp_primal_obj  0.0        ← round(4.2e-44, 6)
```

`y0_star = 0` happens to be the exact certificate for `t = G e₀`, so the
written value was not wrong. But rounding is not what established that: it
would equally have written `0.0` for a value that ought to be `3e-6`. The check
was absent and its absence was indistinguishable from its passing. Rounding
removed; the row now carries the solver's value beside a companion that agrees
with it to 51 digits — which also keeps the audit's laundering guard satisfied
rather than tripped, since a rounded `0.0` paired with a true `6.65e-46`
companion is precisely the contradiction that guard exists to catch.

## Effect on the carve-out

The route-3 carve-out is not a target in itself — the point is that fewer f64
fields need excusing because they now carry their own evidence.

```
4,052  start of arc
4,004  bondgraph auto-picked MPFR
3,331  11 producers switched to backend="clarabel"
2,714  provenance() carried through the producers   (42 witnesses, was 45)
```

A third of the carve-out discharged, by the `*_str` shadow rule (route 2)
rather than by the carve-out list (route 3).

### Verification

```
witness_raw_float64_audit               NEW 0, REGRESSED 0, excused 2,714/42
witness_raw_float64_audit --self-test   25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0
pytest tools/pyhecke                    193 passed, 44 skipped, 0 failed
bun run scripts/run-validate.ts         ✓ Valid — 27 issue(s)  (unchanged)
```

Every regenerated witness now records its own backend; `lp-dual` unannotated
count fell 25 → 21 of 27 flagged.

## Next

- [x] **21 flagged LP/SDP witnesses still record no backend.** Drained to 11;
      see below.

---

## Draining the unannotated backlog — and what it turned up (2026-08-23)

Of the 21, **17 route through the canonical entry point** and four bypass it
with a direct `linprog`. None of the 17 pinned a backend: every one was on
`auto`, which is *worse* than the forced `scipy` this arc started with — a
forced backend is at least honest and reproducible, while `auto` picks by
whether the Rust binary happens to be on the box, so the same script yields
different numbers in different places. Fourteen pinned to `clarabel`, plus
`lp_confinement_nf_forcing.py`'s multi-line call.

Unannotated: **21 → 11**. `alpha_5_lp_dual_crystal.py` is pinned but its
witness is unregenerated: the producer does not finish here, hanging in
`global_wedderburn_sum_q_hecke_seminormal` for the tritium stratum — pure
representation theory, upstream of any solve, so unrelated to this work. The
pin is a no-op in this environment anyway (`auto` resolves to `clarabel-mpfr`
where the binary exists) and protective where it does not.

### One site keeps scipy, and it is the only measured exception

`rho_k_h3a_gg_trajectory.py` **regressed under the pin** — `feasible: true,
primal_obj: 1.2745` became `NaN, feasible: false` for every nucleon, with
non-finite values entering the witness. Diagnosed rather than reverted blind:

    t = 1/(dim_q · |y·χ|), floored at 1e-15  ⇒  t spans 1.1 … 1e15

A cost **dynamic range** of 15 orders. Clarabel's interior-point method
returns a false `infeasible`; HiGHS's simplex solves it. Not precision —
167 / 333 / 500 bits fail identically. Reverted to `scipy` with that
measurement written at the call site. Its SDP sibling is deliberately left on
`auto`: the SDP path takes only `auto`/`cvxpy`/`clarabel`, cvxpy is absent
here, and pinning it to clarabel would swap an honest "SDP requires cvxpy" for
the same false infeasible — turning a missing dependency into what reads as a
mathematical verdict.

The underlying `1e-15` floor ("set to a large finite cost so the LP naturally
avoids that channel") is a modelling smell — dropping those channels would say
the same thing without a 1e15 cost — but changing it changes the model, so it
is the owner's call, not this arc's.

### The gate rewarded laundering; now it does not

Recording that backend honestly made `rho-k-h3a-gg-trajectory` trip the
float64 gate. That exposed a design flaw in the gate as shipped: a producer
with a legitimate need for the f64 backend fails, and **the cheapest way to
make it pass is to stop recording `backend` at all** — dropping into the
unannotated bucket, which the gate only reports. The gate paid for deleting
provenance.

Closed with `F64_BACKEND_EXEMPT`: an allowlist keyed by witness basename whose
value is the *reason*, printed on every run. An exemption you must name and
justify beats a blind spot that costs nothing to enter.

### A false-infeasible rescue, and its limits

While diagnosing the above, found a *separate* real defect: with the default
`M_bound=1e6`, cost magnitudes at or above ~1e6 drive clarabel to a spurious
infeasible even at uniform scale.

`t` appears **only in the objective** — the feasible set is
`{x : Σx = n_target, G-positivity, x ≥ -M_bound}` and never mentions `t`. So
rescaling the cost vector cannot change feasibility, and a verdict that flips
under rescaling was a numerical artifact. The rescue re-solves with `t` scaled
by a **power of two** (exact in both f64 and MPFR, no rounding either way) and
scales the t-linear outputs back; `x_star` and `active_set` are
scale-invariant and pass through. It fires only after an infeasible verdict,
so it cannot perturb any currently-working solve, and it records
`rescaled_by_pow2` rather than acting silently.

Verified exact: rescued answer matches scipy to `rel 0.0e+00` with an
identical active set. **It does not fix `rho_k`** — scaling shifts the
magnitude of `t` but not the ratio between its entries, and the ratio is what
conditions that solve. Stated plainly because the rescue was built for `rho_k`
and does not rescue it.

### Every construction site now names its solver

Six `LpDualResult` constructors; three recorded nothing. The serious one:
`solve_frobenius_dual_lp`'s **success** branch was anonymous while its
infeasible branch already set `backend`. So a *successful* f64 solve through
that entry point was invisible to the float64 gate and only a **failed** one
was caught — an absent check indistinguishable from a passing one, inside the
gate this arc built. It is public with live callers (`frobenius_repose_probe`,
`all_nuclides_sdp_admissibility`). The two infeasible branches were anonymous
too, which matters because an infeasible verdict is a claim about the LP and
the backends demonstrably disagree on badly-conditioned costs.

### Tests, shown to fail first

`tools/pyhecke/tests/test_lp_dual_provenance.py`, 9 cases. The first draft of
the frobenius test **passed with the fix removed** — it called
`solve_operator_selection_lp`, whose scipy path already named itself, so it
never touched the hole it claimed to cover. Same defect class as the bug,
inside its own test. Rewritten against `solve_frobenius_dual_lp` and confirmed
to fail without the fix (`backend=None` on a successful solve).

### Verification

```
witness_raw_float64_audit               NEW 0, REGRESSED 0, excused 2,561/40
witness_raw_float64_audit --self-test   25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0   (unannotated 21 → 11)
pytest tools/pyhecke                    202 passed, 44 skipped   (was 193)
clarabel_lp_crosscheck                  all cases agree
bun run scripts/run-validate.ts         ✓ Valid — 27 issue(s)  (unchanged)
```

Carve-out across the whole arc: **4,052 → 2,561**, all of it discharged by the
`*_str` shadow rule rather than by widening the carve-out list.

## Next

- [ ] **11 flagged witnesses still record no backend**, four of them because
      their producers call `scipy.optimize.linprog` directly and never reach
      the canonical entry point at all (`benzene_assembly_spine`,
      `co_bond_order_active_set`, `three_quark_borromean_lp_sweep`,
      `two_quark_active_set_mahler_sweep`). Those are out of contract with
      AGENTS.md §LP/SDP first-class infra, not merely unannotated.
      `compound_shift_nf.py` also calls `linprog` directly but justifiably —
      as a *discrete oracle* for the active set, with every value then
      recomputed in mpmath.
- [ ] **Four producers cannot run at all** and their committed witnesses are
      therefore unverifiable: `borromean-axial-coupling.py` (KeyError
      `gram_inverse`), `habiro_correction_shadow_price_test.py` and
      `wedderburn_pair_volumes.py` (mpf `__format__`), and
      `r5_full_canonical_knot_solver.py` (no `pyhecke_native`). All four are
      pre-existing — confirmed against a clean tree — and none is caused by
      this arc.
- [ ] **Owner: the `1e-15` floor in `rho_k_h3a_gg_trajectory.py`.** Dropping
      the dead channels would express the same intent without a 1e15 cost, and
      would let that site join the MPFR backend. Changes the model, so not
      this arc's call.


---

## A regression I shipped, and the three defects behind it (2026-08-23)

**`wedderburn-lp-ew-wiring` went from a real answer to 72 NaNs in my own
commit, and every gate stayed green.** At the pre-arc baseline it had
`y0_star = 5.237018636555333e-06`; pinning it to clarabel turned the whole
dual vector into NaN. The ratchet counts raw f64 fields and **NaN is a
float**, so the count never moved. `--strict-wired` passed because the witness
is not content-wired. The audit self-test passed because it tests the audit.
Nothing in the suite asks *"did a number become NaN?"*

Found it only by reading `y_star` while chasing something else. Added the
missing check as a sweep of every touched witness against the pre-arc base,
comparing NaN counts and `feasible` tallies; it now reports **0 regressed**
and two improvements. That sweep is what should have existed before the first
pin landed.

### Defect 1 — "the solver gave up" was reported as "the LP has no solution"

`operator_selection_lp.rs` had

```rust
let feasible = matches!(status, SolverStatus::Solved | SolverStatus::AlmostSolved);
```

which collapses eight distinct Clarabel statuses into one bool. Measured on
wedderburn (d = 28, |t| ~ 1e-5, n_target ~ 3e-4, optimum 1.67e-9, Gram
well-conditioned at cond 53):

```
prec_bits=113   AlmostSolved            feasible
prec_bits=167   InsufficientProgress    "infeasible"  → 72 NaNs
```

`InsufficientProgress` is a statement about the **solver**; only
`PrimalInfeasible` / `DualInfeasible` are statements about the **problem**.

And the cause of the non-convergence was *my own earlier fix*: `tol_gap_abs`
and `tol_feas` are **absolute**, and deriving them from the arithmetic width
alone asked for a 1e-40 residual on a problem whose optimum is 1e-9. Higher
precision made a solve fail that lower precision completed.

Fixed with a **tolerance ladder**: try tight, and on a non-convergence status
loosen 8 decades and retry, down to `1e-8` — the constant this code used
before the precision-derived pair replaced it, so the ladder can never be
worse than what it replaced. The floor is deliberately not `e_red`, which
scales with precision and would bottom out at 1e-50 at 333 bits. A genuine
infeasibility certificate stops the ladder immediately; loosening on one would
turn a correct "no solution" into a fabricated one. The achieved tolerance and
every rung tried go into the status string:

```
AlmostSolved@1e-25 after [InsufficientProgress@1e-40, InsufficientProgress@1e-32]
```

wedderburn now returns `1.670447353422837e-09` against scipy's
`1.6704473534228322e-09`, and carries 50-digit companions.

### Defect 2 — the rescue returned a wrong answer, confidently

The false-infeasible rescue from earlier in this arc **corrupted `rho_k`**.
Scaling `t` cannot change the feasible set — but on a cost vector spanning
1.1 … 1e15 it pushes the small entries to ~1e-15, where the solver treats them
as zero and optimises a *different* objective. It then solves that one well:

```
rescued primal_obj   1.4571747644416917     relative duality gap 1.2e-30
true optimum         1.2745481388661641     (scipy)
```

14 % wrong, with a gap of 1e-30 vouching for it. **The gap cannot police
this** — it is small because the solver solved the substituted problem
correctly. I had verified the rescue as "exact" on a case where the scaling
was benign, which is the same absent-check shape: the test could not fail.

Fixed by certifying the answer **against the original data** before accepting
it. LP duality requires `y0·1 + Gᵀy ≤ t` with `y ≥ 0`; a `y` optimal for a
rescaled `t` violates it. Normalised by the objective the duality theorem ties
it to:

```
max(y0·1 + Gᵀy − t) / max(|primal_obj|, 1)     1.4e-16   vs   1.1e-01
                                              (correct)      (wrong)
```

Eight orders apart — a discriminating test, not a threshold fitted to two
points. A solve that fails certification is reported infeasible with the
reason, never returned. The same check gates a laddered solve, which answers a
slightly different question by construction.

### Defect 3 — a false `DualInfeasible`

Clarabel emits `DualInfeasible` on uniform ~1e6 costs where scipy solves the
problem at 104901.11715303971. So even a "genuine certificate" status can be
wrong on badly-scaled data, which is why the rescue still exists and is now
certified rather than trusted.

### `rho_k` stays on scipy, and the reason is now stronger

Not "clarabel says infeasible" but "clarabel's answer fails certification
against the original cost vector". `F64_BACKEND_EXEMPT` stands.

### On the dense PSD lift — the blocker is not `Copy`

This bean and `qou/f7af` both frame it as *"the bound is `Copy` on a marker
trait … a scoping question, not an impossibility."* Having read the fork:

```rust
pub trait MaybeBlasFloatT: BlasFloatT + Copy + NumCast + ToPrimitive {}
```

`Copy` is the third bound and the least of them. **`BlasFloatT` is sealed**
(`private::BlasFloatSealed`, impl'd only for f32/f64) and requires eleven
LAPACK/BLAS scalar traits — `xsyevr`, `xpotrf`, `xpotrs`, `xgesdd`, `xgesvd`,
`xgemm`, `xgemv`, `xsymv`, `xsyrk`, `xsyr2k`, `xgesv` — each an `unsafe` FFI
call into compiled FORTRAN that exists only for machine floats. Relaxing
`Copy` is necessary and nowhere near sufficient; the actual task is
**implementing LAPACK at arbitrary precision**. That is not a scoping
question. Anyone picking this up should either write an MPFR eigensolver for
the specific decompositions the PSD cone needs, or use f64 to *find* the
solution and MPFR to *certify* it — the shape `compound_shift_nf.py` already
uses on the LP side, and the shape `_certifies_optimality` now uses here.

Worth stating plainly because the dense lift is **not** where the remaining
f64 is. Ranked, the top sources are LP witnesses, not SDP ones.

### Carve-out

```
4,052  start of arc
2,561  previous commit
1,843  companions carried into per-partition slices and row-level mirrors
1,774  after the ladder + certification re-runs
```

`a-K-via-lp-dual-full` and `pn-alpha-lp-dual` were the two largest and were
**pure plumbing**: 308 fields in `per_partition[]` re-slicing `x_star`/`y_star`
without their companions, and 164 in row-level mirrors copied up from a
`lp_dual` sub-dict that had them. The digits existed; the producer dropped
them. `pn-alpha`'s row-level `primal_obj` additionally came from an inline
scipy solve with a `[-10, 10]` box: measured across all 41 rows, that LP and
the canonical one agree on the optimum to 3.55e-15 and differ only in which
argmin they land on (the optimum is 0, the optimal face is large, and the box
binds in all 41 rows). The inline number was f64 noise around a true zero;
the canonical solve of the same objective was already in the row at 50 digits.

### Verification

```
NaN / feasibility sweep vs pre-arc base   0 regressed, 1 improved
witness_raw_float64_audit                 NEW 0, REGRESSED 0, excused 1,774/39
witness_raw_float64_audit --self-test     25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0
pytest tools/pyhecke                      205 passed, 44 skipped   (was 202)
cargo test --lib (clarabel-mpfr)          208 passed, 0 failed
clarabel_lp_crosscheck                    all cases agree
bun run scripts/run-validate.ts           ✓ Valid — 27 issue(s)  (unchanged)
```

Rust doctests fail on unicode in doc comments (`⊗`, `·`, `×`) — pre-existing,
confirmed against a clean tree.

## Next

- [ ] **`solve_frobenius_dual_lp` has no MPFR path at all** — no `backend`
      parameter, `scipy.optimize.linprog` hardcoded. It is the single largest
      remaining f64 source (`frobenius-repose` 278 fields,
      `all-nuclides-sdp-admissibility` 144). The Rust change is small: the
      Frobenius block becomes a `ZeroConeT(d)` with `b = u_demand` instead of
      a `NonnegativeConeT(d)` with `b = 0`; the A matrix is unchanged.
      Worth knowing first: for invertible `G` the equality system
      over-determines `x`, and the dual optimum is then a **line** rather than
      a point, so `y0_star` is not uniquely determined and whatever the solver
      returns is one arbitrary point on it. `frobenius_repose_probe` runs at
      `rank(G) = 5, d = 6`, i.e. singular, where its `np.linalg.inv(G)` is not
      meaningful either.
- [ ] **1,282 of the remaining carved fields sit in witnesses that record no
      backend at all** — untouched producers. That is where the f64 is, not in
      the dense PSD lift.


---

## The Gram is exactly singular, and a feasibility test was passing on round-off (2026-08-23)

Went to give `solve_frobenius_dual_lp` an MPFR path — the item this bean's
previous "Next" named as the largest remaining f64 source. **The port would
have fixed nothing.** All 143 carved fields in `frobenius-repose` come from
`_variant_a`, which never calls the LP solver; it computes `x = G⁻¹nf` and
`y = G⁻ᵀt` with numpy. Checking that first is what turned up the real problem.

### G has no inverse

```
dps= 60   det(G) = -2.008684335e-57    |eig|min = 1.478983446e-57
dps=120   det(G) = +5.724314033e-117   |eig|min = 4.215451518e-117
```

The determinant tracks the working precision instead of converging, sign flip
included. That is an **exactly zero** determinant seen through floating point.
`G` has a one-dimensional kernel
`v ≈ (-0.4727, 0.4259, 0.4259, -0.3837, -0.3837, 0.3457)`, confirmed by
`‖Gv‖∞ = 3.4e-76` at 80 dps.

So `frobenius_repose_probe.py` was inverting a matrix with no inverse — and
its docstring asserted the opposite (*"G is invertible ⇒ nf ∈ range(G) is
mathematically guaranteed"*), while flagging the symptom as *"the known infra
ceiling (needs mpfr)"*. **Precision cannot fix this**: at 120 dps the condition
number is 1e117 and an inverse-based solve still has zero correct digits.

### A feasibility test that passed on round-off

The committed baseline reported **`feasible=True` for 20 nuclei** with
`rel_resid ≈ 2e-16`. It is a false positive: `|G⁻¹| ~ 7.6e15`, so `x = G⁻¹nf`
is large enough that `G @ x` reproduces `nf` to machine epsilon through
round-off alone, and the relative-residual check passed on that.

The truth, measured at 80 dps: the census `nf` vectors are **not in
`range(G)`** at all. For symmetric `G`, `range(G) = kernel⊥`, and

```
v·nf / ‖nf‖   =  0.37 (p)   0.41 (n)   0.32 (2H)   0.22 (3He)   0.21 (4He)
```

O(1), not round-off. `Gx = nf` has no solution for any of them. Twenty nuclei
were being reported as Frobenius-admissible when the system defining
admissibility is unsolvable.

This **strengthens** the probe's honest-negative verdict rather than changing
it — the test now admits nothing rather than everything, and is non-selective
either way.

### What IS well defined

`t` is in `range(G)` exactly (`v·t = -3.4e-76`), so `Gy = t` is solvable, with
`y` unique up to a kernel vector. The minimum-norm representative is canonical
and is what `gram_pseudo_inverse_solve` now returns. It is not an
approximation of the old row:

```
via G⁻¹        0.75,  0.5,   0.25,  0.5,    0.154, -0.311
minimum-norm   0.777, 0.201, 0.201, -0.181, -0.181, 0.163
```

off by 1e7–1e8 relative — and the old row **breaks the exact symmetry**
`y[1] = y[2]`, `y[3] = y[4]` that the true solution has, which is independent
evidence it was round-off rather than a nearby answer.

`x_star` is now `null` where no solution exists, instead of a vector.

### Two bugs in my own helper, both caught by tests

1. **Absolute rank cutoff.** A fixed `1e-40` is not scale-invariant, and is
   *tighter than the arithmetic* below ~50 dps — so a genuinely zero
   eigenvalue computed as 1e-31 at dps=30 read as nonzero and the kernel was
   missed. Now relative to `|eig|max`.
2. **Working precision above input precision.** At dps=80 against 50-dps input
   strings the zero eigenvalue read as ~1e-50 *invented* noise, the kernel was
   missed, and the H_3 solve returned `y[0] = 1.0` with the symmetry broken.
   The cutoff is now bounded by the digits actually present in the input. A
   helper that answers a question its inputs cannot support is the same absent
   check this arc keeps finding — this time in the fix.

`test_pseudo_inverse_rank_is_stable_across_working_precision` pins it: rank is
a property of the data, so dps must not change it.

### The other caller was ordinary

`all_nuclides_sdp_admissibility.py`'s 144 fields were `solve_operator_selection_lp`
on an unpinned `auto` backend. Pinned; `to_dict()` carried the companions.

### Carve-out

```
4,052  start of arc
1,774  previous commit
1,352  frobenius-repose 143 -> 0 bare, all-nuclides 144 -> 0 bare
```

### Verification

```
NaN / feasibility sweep vs pre-arc base   1 flagged, investigated: a CORRECTION
                                          (20 false-positive feasibles removed)
witness_raw_float64_audit                 NEW 0, REGRESSED 0, excused 1,352/37
witness_raw_float64_audit --self-test     25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0
pytest tools/pyhecke                      209 passed, 44 skipped   (was 205)
clarabel_lp_crosscheck                    all cases agree
bun run scripts/run-validate.ts           ✓ Valid — 27 issue(s)  (unchanged)
```

The sweep cannot distinguish "corrected a false positive" from "broke
something" — it sees `feasible` going down either way. That is the right
behaviour for a tripwire; it fired, and the flip was investigated against the
80-dps range test rather than waved through.

## Next

- [ ] **Owner: 20 nuclei lost Frobenius admissibility.** No downstream content
      block cites `frobenius-repose` (it is not in the wired set), so nothing
      breaks mechanically — but anything that reasoned from "the Frobenius
      test admits these" was reasoning from a false positive.
- [ ] **`solve_frobenius_dual_lp` still has no MPFR path**, and is still
      worth giving one — the Rust change is small (`ZeroConeT(d)` with
      `b = u_demand` in place of `NonnegativeConeT(d)` with `b = 0`). It is
      just no longer the largest f64 source, and on this Gram every call it
      receives is infeasible before precision matters.
- [ ] **~1,100 of the remaining carved fields are in witnesses recording no
      backend** — untouched producers, the same mechanical treatment.


---

## A local reimplementation shadowing the canonical solver, with a sign error (2026-08-23)

Draining `e-0-lp-dual-h3` (120 fields) turned up something worse than
truncation. `derive_e_0_lp_dual_h3.py` **defined its own function named
`solve_operator_selection_lp`** — the canonical entry point's exact name — as a
local `scipy.optimize.linprog` wrapper. A reader, or a grep-based audit looking
for producers on the canonical path, finds that name and concludes the
canonical solver is in use. It was not.

And the reimplementation had a **sign error**: `y_0_star = -eq_marg[0]` where
the canonical takes `+eq_marginals[0]`.

```
local      primal_obj +0.3753866308623884   y_0_star -0.3753866308623884
           dual_obj   -0.3753866308623884   duality_gap 0.7507732617247768
canonical  primal_obj +0.3753866308623884   y_0_star +0.3753866308623884
           dual_obj   +0.3753866308623884   duality_gap 0.0
```

Its own strong-duality check therefore computed a gap equal to **twice the
objective** — maximally violated — and recorded it rather than failing. Every
`results_per_target_cone` entry in the committed witness carried
`y_0_star = -0.12449094312996863` with `duality_gap ≈ 2 × primal_obj`, in a
witness whose entire purpose is the LP-dual certificate. The file emits **no
assertions at all**, so nothing could have caught it. `E_0` is derived
downstream as `y_0_star · m_e`, so the sign propagated into an energy.

Both of its modes were expressible by the canonical solver all along —
`cone=False` is `M_bound=M_bound`, `cone=True` is `M_bound=0.0` — so the
reimplementation was never needed. Now delegates, with the return shape kept
verbatim so callers are unaffected. After:

```
y_0_star  +0.3753866308623884    duality_gap 2.67e-51    backend clarabel-mpfr
```

### Why it had gone unnoticed for three months

The producer **could not run**. Its upstream,
`beta-decay-energy-scale.witness.json`, had been moved to `_deprecated/` while
**nine live scripts still read it** — this one, `derived_masses`,
`meson_mass_from_hecke`, `derivation_chain`, `q_beta_predicted`,
`derive_m_e_hecke_path_a`, two probes and an audit. `_deprecated/README.md`'s
own criteria require that nothing live consume a witness before it moves, and
the README already documents this exact failure once: `hecke_core_legacy.py`
was moved back OUT because nine importers depended on it.

So the witness sat frozen at **2026-05-11** carrying a broken certificate,
because the script that would have refreshed it died on import.

Resolved conservatively: the producer now resolves the live path first and
falls back to the deprecated copy, with the situation spelled out at the call
site. Verified the two copies' `nucleon_nf` payloads are **identical**, so the
fallback changes no number — it only lets the script run. Restoring the witness
to the live area is the fix the README's own precedent prescribes, but it is
the owner's call: it partly reverses a deprecation, and the corpus ratchet
baseline is documented drains-only, so the restored file would either fail
`--strict` as a NEW dirty witness or require growing a baseline that is not
supposed to grow.

### `pyhecke-native` built — and it surfaced six pre-existing failures

`scripts/build-pyhecke-native.sh` works in this sandbox (~2.5 min) and unblocks
`he4_binding_k_stage2_probe` (158 fields) and `r5_full_canonical_knot_solver`
(40), both of which died on `ModuleNotFoundError: pyhecke_native`.

Installing it moved 31 tests from *skipped* to *running*, and **6 of them
fail**:

```
test_native_version              '0.9.0' == '0.4.0'   (test stale vs the crate)
test_native_gram_matches_python   max|Δ| 6.6e-08  vs a 1e-14 tolerance
test_native_markov_z_matches_python, test_native_trace_weights_match_python,
test_bridge_det_uses_native, test_native_version_bumped
```

Not caused by this arc — `operator_selection_lp.rs` is not on the Gram path,
and these tests were skipped for want of the module, so they could not fail.
Another check invisible from its own absence. The wheel is ephemeral (dies with
the container), so CI is unaffected either way, and nothing committed here
depends on it being present.

`he4_binding_k_stage2_probe` is a long resumable compute (exact χ_λ via
seminormal MPFR over 77 blocks, ~154 characters); it was pinned to clarabel and
left running. The pin is a no-op for the numbers where `auto` already resolves
to clarabel-MPFR, and protective where it does not.

### Carve-out

```
4,052  start of arc
1,352  previous commit
1,287  aK aggregates + per-basis slices + deuteron mirrors
1,168  derive_e_0 on the canonical MPFR solver
```

### Verification

```
witness_raw_float64_audit --strict        exit 0, NEW 0, REGRESSED 0
witness_raw_float64_audit --self-test     25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0, 2 reasoned exemptions
NaN / feasibility sweep vs pre-arc base   1 flagged — the known frobenius
                                          false-positive correction
bun run scripts/run-validate.ts           ✓ Valid — 27 issue(s)  (unchanged)
pytest tools/pyhecke (no native)          209 passed, 44 skipped
pytest tools/pyhecke (native installed)   234 passed, 13 skipped, 6 FAILED
                                          — pre-existing, see above
```

## Next

- [ ] **Owner: `beta-decay-energy-scale.witness.json` is deprecated with nine
      live readers.** The README's `hecke_core_legacy` precedent says move it
      back; the ratchet's drains-only baseline says that costs a `--strict`
      failure. Needs a ruling, not a workaround.
- [ ] **Six native tests fail once the wheel is installed.** Invisible while it
      is absent, which is why they have stayed red.
- [ ] `he4-binding-k-stage2` (158) and `r5-full-canonical-knot-solver` (40)
      are now runnable and unregenerated.


---

## Both flagged items fixed (2026-08-23)

### The six native tests: stale pinned constants, not kernel bugs

All six failures traced to literals the tests pinned and then let drift. None
was a defect in the Rust kernels.

**Five were a stale q_0.** The tests hardcoded `1.1099785955541805`; the
canonical `pg.q0` is `1.1099785827513808`. They diverge at the 9th significant
digit (dq ~ 1.3e-8), so the test fed the Rust kernel one q_0 and compared
against the Python kernel at another, then reported the difference as a
mismatch:

```
gram_matrix(stale literal)   max|native - python| = 6.6446e-08   FAIL vs 1e-14
gram_matrix(canonical q_0)   max|native - python| = 0.0000e+00   exact
```

The kernels were never wrong. Fixed by sourcing q_0 from `pyhecke.gram`, so a
test comparing two implementations of a q_0-derived quantity can no longer
evaluate them at different q_0.

**Two were a stale version pin.** `assert __version__ == "0.4.0"` against a
crate at `0.9.0` — asserted through five bumps despite the test's own comment
saying to update it in the same commit. Now read from `Cargo.toml`, which
checks the *wiring* (`env!("CARGO_PKG_VERSION")` reaching Python) instead of a
literal, and additionally cross-checks `pyproject.toml`.

**The sixth was the interesting one.** `test_bridge_det_uses_native` pinned
`det = -0.3608011166161873` to within 1e-10. That is not a drifted value — it
is **15 orders of magnitude** from the truth. The determinant is *zero*:

```
numpy.linalg.det(pg.G)             3.998399968397726e-17
pyhecke_native.gram_determinant    0.0
bridge.gram_det_from_rust()        3.5985600328525204e-16
mpmath det of the 50-dps strings  -2.00868433511e-57
```

**This was the one test in the repo that would have caught the H_3 Gram going
singular, and it has been failing invisibly** — `test_native.py` skips
entirely when the `pyhecke_native` wheel is absent, which it usually is. A
check that cannot run cannot fail, which is this arc's recurring shape, here
guarding the very fact the arc later had to rediscover from scratch.

Rewritten to assert the property: the bridge must return what the native
kernel returns (that is what "uses native" means), and that value must be zero
to f64 resolution, with an explicit "do not re-pin, investigate" if it ever is
not.

```
pytest tools/pyhecke   234 passed, 6 FAILED  ->  240 passed, 0 failed
```

### The deprecated witness with nine live readers

Fixed at the single point that serves all of them rather than per script.
`_path_bridge.witness_path` builds `_WITNESS_DIRS` by skipping `_`-prefixed
directories, so a witness moved to `_deprecated/` becomes invisible to the
resolver and every live reader dies on `FileNotFoundError`. Measured: of the
nine readers of `beta-decay-energy-scale.witness.json`, `derived_masses.py`
and `q_beta_predicted.py` failed outright ("Run the beta-decay-energy-scale
compute first") and `derive_e_0_lp_dual_h3.py` could not run at all.

`witness_path` now falls back to `_deprecated/` as a **last resort**, after
every live directory. A live copy always wins, so this is not a general
un-deprecation — it fires only when no live copy exists, which is precisely
the broken-dependency case. All three scripts run again, and the local
workaround added to `derive_e_0_lp_dual_h3.py` in the previous commit is
removed in favour of it.

**Not done, deliberately.** Restoring the witness to the live area would need
its 57 raw floats drained, and they are drainable — the upstream
`free-neutron-decay.witness.json` carries `coefficient_symbolic`, an exact
expression in q, so the NF coefficients can be re-derived at 50 dps rather than
read from `coefficient_numeric`. But that changes the NF values downstream in
`derived_masses`, `q_beta_predicted` and others, which is a content change, not
a plumbing one. The `float64-integrator` tier does not apply either: that
carve-out is for integrators where "the integrator IS the source", and here
there is a symbolic source.

Running those scripts as a test also regenerated three unrelated stale
witnesses (`electron-m_e-derivation`, `meson-mass-from-hecke`,
`q-beta-predicted` — the last gaining a raw float, 17 -> 18). Reverted: they
are now runnable after years of not being, but folding three unreviewed
regenerations into a path-resolver fix is not the same as regenerating them
deliberately.

### Verification

```
pytest tools/pyhecke (native installed)   240 passed, 13 skipped, 0 failed
witness_raw_float64_audit --strict        exit 0, NEW 0, REGRESSED 0
witness_raw_float64_audit --self-test     25/25 PASSED
lp_dual_witness_validator --strict-wired  exit 0
bun run scripts/run-validate.ts           ✓ Valid — 27 issue(s)  (unchanged)
```

## Next

- [ ] **Drain `beta-decay-energy-scale.py` from `coefficient_symbolic`** and
      restore its witness to the live area. This is the real fix for the
      deprecation; the resolver fallback only stops the bleeding.
- [ ] **Three witnesses are stale and now regenerable** —
      `electron-m_e-derivation`, `meson-mass-from-hecke`, `q-beta-predicted`.
      Deliberate regeneration + review, not a side effect.
- [ ] `he4-binding-k-stage2` (158) still computing; `r5-full` (40) runnable.
