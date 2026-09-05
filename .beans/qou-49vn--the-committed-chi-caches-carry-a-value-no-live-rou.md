---
# qou-49vn
title: 'The committed chi caches carry a value no live route reproduces: cached 0.5751722439 vs --fresh AND markov-peel 0.1519683392'
status: todo
type: task
priority: normal
created_at: 2026-09-05T19:13:20Z
updated_at: 2026-09-05T19:14:14Z
---


Found 2026-09-05 while re-verifying a claim I had **asserted without measuring**
in PR #6861 — *"re-running the chi producer today reproduces them"*. It does
not, and the discrepancy is a factor of 3.78.

## The measurement

Same container, same commit (`main` at `14c798b93c` + 2), same `mpmath 1.3.0`.
`computations/chi_at_q0_via_hoefsmit_mpfr.py deuteron`, differing **only** by
the `--fresh` flag:

| run | `tr_M_at_q0` |
|---|---|
| cached (resume: 11 partitions already cached) | `0.57517224391777187082653534398618088915249435289286` |
| `--fresh` | `0.15196833920423160759266569775106614127124096465527` |

The cached run reproduces the **committed** witness value to all 50 digits.

Independent corroboration, same day, different script —
`QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor
proton`:

    [peel]  tr_M(q_0) = 0.15196833920423160759266569775106614127124096465526   (deuteron)
    |bridge - peel|   = 1.15e-51

So the **markov-peel** and the **Hoefsmit+Wenzl bridge** agree with each other
at 1e-51 and with `--fresh` chi to **49 of 50 digits**. Three routes today give
`0.1519683392…`; the cache alone gives `0.5751722439…`.

The `--fresh` help text describes this exact failure: *"Use when a cache may
already have been stamped with the CURRENT q0 while holding values computed at
a different one — the resume check compares stored-vs-current q0, so it cannot
see that."*

## What moved, and what did not

Comparing the fresh witness against the committed one per partition: the
`y_lambda` are **unchanged**; **9 of 11 `chi_lambda` differ substantially**,
with sign flips — e.g. `λ=(5,1)`: `3.2163173422…` → `-0.6822850128…`. So this
is a **χ** change, the mirror of the 2026-08-10 move analysed in `qou-brkp`,
which was a **y** change.

The committed chi witness is also **self-stale**: `scriptHash c36a8a393fcd`
predates two producer fixes —

  * `41f517bf17` (2026-08-23) *"fix(qou-8chw): my own unblock turned a crash
    into silent cache poisoning — guarded"*
  * `d151898dd6` (2026-08-30) *"fix(L1): pin-specific numerical chi caches —
    5/6 atoms certified 1 ppQ (T + ³He recovered)"*

Both are about exactly this cache. `d151898dd6` is the leading candidate and is
**not** confirmed here.

## Scope: all three atoms, and the arbiter itself

The arbiter's committed witness (`atomic-tr-m-mpfr-50dps-proton.witness.json`,
computed **2026-08-19**) disagrees with a re-run today on **every** atom:

| atom | committed 2026-08-19 | today |
|---|---|---|
| proton  | `1.14575969245730086968…` | `0.62932840220292191816…` |
| neutron | `0.98774368811580957163…` | `0.47513351715568221250…` |
| deuteron | (chi cache) `0.5751722439…` | `0.15196833920423160759…` |
| tritium | (chi cache) `0.2293101021…` | `0.02914404236097206535…` |
| ³He | (chi cache) `0.4037670368…` | `0.05859625365443638021…` |

## 🛑 TWO CONFOUNDS — this does NOT establish which value is correct

1. **The Rust kernel was unavailable in today's run** — the arbiter printed
   `[rust] hecke-canonical-chi unavailable; falling back to Hoefsmit+Wenzl
   bridge`. The committed run may have used `canonical-rust`. The fallback is
   the documented graceful one, but it means today's "two routes" are closer
   kin than they look.
2. **The arbiter's own source drifted**: `scriptHash 7c63fadfb8d0 →
   db23b7ba36cb`.

The deuteron result survives both confounds, because `--fresh` chi is a
*different script* that also gives `0.1519683392…`. The proton/neutron rows do
not, and are recorded as observations, not verdicts.

**Nothing here says `0.152…` is right and `0.575…` wrong.** What it says is
that **no live route reproduces `0.575…` except the cache**, and that the cache
is the thing two producer fixes were written to distrust.

## What this retracts

`qou-brkp` item 1 was closed earlier today as *"answered — four routes, one
number (`0.5751722439…`)"*, on the strength of `qou-r9dv` / `aeb31dfb41`
(2026-08-23), which reports three independent methods agreeing exactly. **That
closure is retracted.** `aeb31dfb41` predates `d151898dd6` (2026-08-30), and
the arbiter it names now gives a different number. I closed a question on a
**baseline** instead of a fresh measurement — the precise trap this repo's own
agent-memory doctrine names (*"a BASELINE tells you what to measure, never the
current answer"*), in the same session in which I wrote that entry.

## Next, in order

1. **Build `hecke-canonical-chi` / restore the Rust kernel** and re-run the
   arbiter, to remove confound 1. Until then no verdict.
2. `git diff c36a8a393fcd..HEAD -- computations/chi_at_q0_via_hoefsmit_mpfr.py`
   and read `d151898dd6` — it claims a 1 ppQ certification for 5/6 atoms and
   may already contain the answer.
3. If `0.152…` is right, the blast radius is wide: `option_e_multi_isotope_
   delta_lambda_probe_v3` and every other reader of `chi-*-at-q0-50dps.witness
   .json` carries the superseded value, and `qou-r9dv`'s three-method
   certification needs re-running.
4. **Do not mass-regenerate.** One atom, with the Rust kernel present, decided
   first.

---

## Confound 1 REMOVED — Rust kernel built and re-run (2026-09-05, same day)

`cargo build --release --bin hecke-canonical-chi` succeeds in this container in
**39 s** (7 warnings, no errors). Re-running
`QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor
proton` with the binary present:

| atom | `[rust]` | `[peel]` | rel \|rust−peel\|/peel |
|---|---|---|---|
| proton   | `0.62932840220292191709…` | `0.62932840220292191816…` | **1.702e-18** |
| neutron  | `0.47513351715568221158…` | `0.47513351715568221250…` | **1.936e-18** |
| deuteron | `0.15194683953767166429…` | `0.15196833920423160759…` | **1.41475e-4** |
| tritium  | `0.02913991921797892047…` | `0.02914404236097206535…` | **1.41475e-4** |
| ³He      | `0.05858796377036033442…` | `0.05859625365443638021…` | **1.41475e-4** |

### What this settles

**`0.5751722439…` is reproduced by NO live route.** Not Rust, not markov-peel,
not `--fresh` chi. Three routes all land in the `0.1519…` neighbourhood. The
committed `chi-*-at-q0-50dps` values are cache-carried and superseded. The
earlier proton/neutron observations were **not** a fallback artifact — the Rust
kernel gives `0.6293…`/`0.4751…` too, so the committed 2026-08-19 arbiter values
`1.1457…`/`0.9877…` are genuinely superseded as well.

### 🛑 A stale BASELINE in a source comment — I read it as corroboration

`computations/canonical_tr_m_via_rust.py:68-70` states:

    # Measured after the fix, with the binary built from tools/hecke-engine:
    #   tr_M(p, q_0) = 1.14575969245730086935241774516176649113
    #   tr_M(n, q_0) = 0.98774368811580957144294046174148798302

Today, same binary path, same anchor: `0.62932840220292191709…` and
`0.47513351715568221158…`. **That comment is stale**, and I cited it as evidence
the committed values were the Rust ones. Third instance this session of the same
error class — a stored number read as a current answer, this time wearing the
words *"Measured after the fix, with the binary built"*, which is exactly the
phrasing that makes it look like a live check.

### What it does NOT settle, and the sharp new finding

Rust and peel **disagree on every composite atom** by

    rust/peel = 0.999858525356843903463281614406   (deuteron)
                0.999858525356843896710241513022   (tritium)
                0.999858525356843898527910951336   (³He)

— **one shared multiplicative constant, agreeing to 17 significant figures**
(spread across atoms `6.75e-18`, i.e. the kernels' own precision floor), while
the two single nucleons agree at `~1.7e-18`.

That shape is informative: the discrepancy is **atom-independent and does not
accumulate with A**, over different braid words and different partition sets. It
is therefore **one shared step in the composite path** implemented differently in
the two kernels — not drift, not accumulation, not a per-atom construction
difference. `1 − 0.9998585253568439 = 1.41474643e-4`.

**No identification of that constant is attempted here**, deliberately: fitting
a formula to a single measured ratio is exactly the move the anti-fit discipline
forbids. It is recorded as a structural signature for whoever localises it.

The discrepancy is **1.4e-4 relative — eleven orders above the 1 ppQ (1e-15) L1
target**, so it is not a precision artifact and both kernels cannot be right.

### Revised next steps

1. **Localise the shared factor.** Diff the composite path: `hecke_canonical_
   chi.rs` / `wenzl_lr.rs` against the Python markov-peel. The single-nucleon
   agreement at 1e-18 means the divergence is in what the composite path does
   *once*, not per crossing. Possible neighbour: bean `qou-1qsw` (three
   inconsistent `pyhecke.atom` nucleon constructions) — same class, different
   magnitude, not established as the same cause.
2. **Only then** decide which value is canonical and whether the
   `chi-*-at-q0-50dps` family should be regenerated.
3. **Still do not mass-regenerate.** One atom, decided, first.
4. `d151898dd6` (*"pin-specific numerical chi caches — 5/6 atoms certified
   1 ppQ"*) claims a certification that a 1.4e-4 kernel split would fail. Read
   it: it may already name this.

### Localisation: four structural exclusions, not yet a culprit

Measured, all from the ratio table above. Each rules out a class; none names
the step.

1. **Not a framing / writhe power of q₀.** `log(rust/peel)/log(q₀) =
   −0.0013559869167486641314` — not an integer, so the arbiter's own
   writhe-match idiom (*"integer ⇒ writhe match"*) excludes it.
2. **Not per-crossing.** The deuteron is `n = 6`; tritium and ³He are `n = 9`,
   with different crossing counts. A per-crossing discrepancy would compound to
   different totals. The ratio is identical to **17 significant figures**.
3. **Not per-strand and not per-nucleon.** Same argument, and sharper: a
   per-nucleon factor `f^A` would give `f²` for the deuteron (A=2) and `f³` for
   T and ³He (A=3). Identical ratio ⇒ the exponent is **0** ⇒ the factor is
   applied **exactly once, regardless of A**.
4. **Not Z/N dependent.** D (1,1), T (1,2) and ³He (2,1) span three different
   `(Z, N)` splits and give the same ratio, so the p/n colour weighting is not
   the differing step — despite the witness `convention` field naming it.

So: **one scalar, applied once, in the composite assembly only** — present for
every atom with A ≥ 2 and absent for both single nucleons. `1 − ratio =
1.41474643156097e-4`; `1/(1 − ratio) = 7068.4045`. Neither is identified, and
**no identification should be attempted numerically** — the anti-fit rule
applies with full force to a single measured ratio.

**One lead, unconfirmed.** `wenzl_lr.rs:250-262` documents an averaging-
convention change: the Rust path substitutes each averaged crossing directly as
`σ − (h/2)·I` (exactly `(σ + σ⁻¹)/2` under the Hecke relation, since
`σ⁻¹ = σ − (q − q⁻¹)`), and therefore reports `averaging_denominator = "1"` to
its Python consumer, where the pre-#682 implementation returned the
**unnormalised 2^k sub-word sum** and required caller-side division. A consumer
still dividing — or not dividing — on the wrong side of that contract is the
right *shape* of defect. **But it does not fit exclusion 2:** a `2^k` mismatch
is per-averaged-crossing and would differ between `n = 6` and `n = 9`. Recorded
as the nearest documented convention seam, not as the cause.

**Handoff.** The next step is reading the two composite assemblies side by side
— `hecke_canonical_chi.rs` / `wenzl_lr.rs` against the Python markov-peel — for
the one scalar that the A ≥ 2 path applies and the A = 1 path does not. The
exclusions above should make that a short search.
