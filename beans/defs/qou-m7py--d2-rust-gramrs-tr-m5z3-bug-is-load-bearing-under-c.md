---
# qou-m7py
title: 'D2: Rust gram.rs TR_M[5]=z^3 bug is load-bearing under convention D'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

## The coupling

`tools/hecke-engine/src/gram.rs` **is** convention D already. Per the banner in
`tools/pyhecke/python/pyhecke/gram.py` (lines 44–130), it survives convention
D's degeneracy **only because** it still carries the pre-2026-05-19
`TR_M[5] = z^3` bug that the Python side fixed.

So the Rust bug is not independently fixable: correcting `TR_M[5]` is expected
to make the Gram form singular in the native path too, exactly as it is in the
Python path. The two must be planned together with `qou-w8zz` (D1(b), invert
`G` on the quotient `H_3/rad`).

**Do not "just fix the Rust bug."** That is the trap this bean exists to name.

## Live split, and a caveat on where it was measured

The prior session measured, with `pyhecke_native` v0.9.0 installed:

- `pyhecke_native` → `markov_z(q0) = 0.6126880371464652` = **convention D**
- `pyhecke.gram.z` → `0.4993203341836945` = **convention C**

and `tests/test_gram_values.py:50` *pins* the C value deliberately.

**Caveat — not reproduced in this container.** The session that took over
PR #4928 (2026-08-14) found `pyhecke_native` **not installed**
(`ModuleNotFoundError`). So the split above is not currently observable here,
and `build_atom_nf` / `atom_per_generator_volumes` fall back to the pure-Python
path. Anyone picking this up should first record whether the native wheel is
present, because the whole failure mode is conditional on it. Do not assume the
earlier measurement still holds without re-taking it.

## Why it matters

`gram.py` exports `G_INV` **at import** into `constants.py`, `atom.py`,
`molecular.py`, `sdp.py` and nine corpus consumers. Once the wheel is rebuilt
from a branch carrying the Rust fix, those two functions return D while `z` /
`TR_M` / `G` / `G_INV` in the same module stay C — a silent mixed-convention
module, which is worse than the stale convention held consistently.

And `np.linalg.inv` does not protect anyone: on the D matrix it raises nothing
and returns entries to 7.6e15 with `||G @ G_INV − I|| = 1.64`.

## Related

- `qou-w8zz` — D1(b), the Python-side quotient inverse. Same repair.
- `qou-fu8c` — the `a_K` LP dual degenerating under D. Third instance of the
  same shape (the `ℓ(λ) ≥ 3` blocks are the radical under D).
- `qou-j6il` — a Rust binary returning convention C while its source read D.


## Update 2026-08-14 — the coupling is PROVED, not asserted (PR #5025)

`computations/probes/gram_radical_exact_probe.py`. The banner's claim was that
the Rust mirror "survives the degeneracy **only because** it still carries the
pre-2026-05-19 `TR_M[5] = z^3` bug". Decided by building the same **exact**
Gram (rational arithmetic, no floating point) with each value of `TR_M[5]`:

| q | `TR_M[5] = h·z² + z` (correct) | `TR_M[5] = z³` (the Rust value) |
|---|---|---|
| 11/10 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |
| 7/5 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |
| 13/7 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |

So the coupling is real: **fixing the Rust bug WILL make the native Gram
singular.** The two cannot be planned independently, exactly as recorded.

**The bug is still live.** `tools/hecke-engine/src/gram.rs:89` ends
`trace_weights` with `[1.0, z, z, z*z, z*z, z*z*z]`; the crate's own module
docstring (lines 9–10, 724) documents the divergence from `pyhecke.gram.TR_M`.

**Size of the error.** At the proton pin under convention D:

```
z                        = 0.6126880371464652
TR_M[5]  correct h·z²+z  = 0.6911664783584445
TR_M[5]  Rust    z³      = 0.2299948980341014     -66.72 %
```

The Markov trace of the 3-strand cap element is off by two thirds, and that
error is precisely what has been holding the form non-degenerate.

## What this changes for the plan

The repair now has its projector in closed form (from the same probe, under
`qou-w8zz`): the radical is spanned by the q-antisymmetriser
`Σ_w (−1/q)^ℓ(w) T_w`. So both sides — `pyhecke/gram.py` and
`hecke-engine/src/gram.rs` — need the same quotient construction, and it is
explicit rather than numerically extracted.

Sequencing follows: fix `TR_M[5]` and adopt the quotient **together**, in one
change, on both sides. Fixing the trace alone lands a singular Gram in the
native path with `np.linalg.inv`-equivalent behaviour downstream.

**Not attempted here:** `pyhecke_native` is not installed in this container, so
the compiled wheel's live behaviour was not measured — only the mathematics it
implements. Anyone picking this up should record whether the wheel is present,
since the observable split is conditional on it.

## Update 2026-08-15 — Python side has LANDED; crate re-read; one prior claim corrected

`pyhecke.gram` and `pyhecke.trace_formal` are now convention D (PR #5055).
That makes this bean the last split, and it is now *guarded* rather than
merely noted: `build_atom_nf` / `atom_per_generator_volumes` REFUSE to
dispatch to the native wheel (`_native_ok()` raises), because with Python
on D and the crate diverging, merely installing the wheel would silently
change results on some machines and not others. Override with
`QOU_ALLOW_NATIVE_DIVERGENCE=1`. So the ~100× speedup is off until this
bean lands — that is the cost of the guard and the reason to prioritise it.

### CORRECTION: the crate is NOT "on convention C"

Earlier wording (mine, and in this bean's title context) said the Rust was
convention C. **It is not.** Re-read of `tools/hecke-engine/src/gram.rs`:

```rust
/// z = q³/(q² + 1) — Markov closure parameter, **trace convention D**
pub fn trace_weights(q: f64) -> [f64; 6] {
    let z = markov_z(q);
    [1.0, z, z, z * z, z * z, z * z * z]   // <-- TR_M[5] = z³, the unported bug
}
pub const Q_0: f64 = 1.1099785955541805;   // <-- the MUON pin
```

So `markov_z` is already D. Two real divergences remain:

| # | Divergence | Rust | Python | Size |
|---|---|---|---|---|
| 1 | `TR_M[5]` | `z*z*z` | `h*z² + z` | structural — see below |
| 2 | `Q_0` anchor | 1.1099785955541805 (muon) | 1.1099785827513808 (proton) | 2.19e-8 rel on z |

### Why #1 and the quotient must land in ONE commit

`z³` is what keeps the crate's Gram **non-singular**. Fix the trace alone
and a singular Gram drops into a native path that has no radical, no
pseudoinverse, and no notion that either is needed. Verified on the exact
probe at three rational q: correct TR_M[5] → rank 5, det 0 exactly; `z³` →
rank 6. So the port is: TR_M[5] fix **+** `RADICAL` **+** quotient inverse
in a single change.

### #2 is independently a violation

The hardcoded muon `Q_0` contradicts AGENTS.md's owner directive
(2026-08-07): all production compute defaults to the experimental/proton
pin. Worth fixing in the same PR since it is a one-constant change, but it
is a *separate* defect from the trace rule — do not let fixing one imply
the other is done.

### Reference implementation to port against

- `tools/pyhecke/python/pyhecke/gram.py` — `TR_M`, `RADICAL`, `G_PINV`,
  `gram_quotient_inverse()`, and `gram_inverse()` raising `NotImplementedError`.
- `tools/pyhecke/tests/test_gram_values.py::test_gram_determinant_is_exactly_zero_over_Q`
  — the exact-ℚ rank/determinant test. Worth mirroring in Rust: a float64
  determinant (3.998e-17) cannot distinguish singular from tiny, so an
  `f64`-only Rust test cannot actually assert the degeneracy either.
- The crate's own `z_at_q0_matches_python` test pins the muon value
  0.6126880505455892 and will need the proton value 0.6126880371464652.

### Definition of done

1. `trace_weights` → `[1, z, z, z², z², h*z² + z]`.
2. `Q_0` → proton pin; update `z_at_q0_matches_python`.
3. Radical + quotient inverse exposed; no 6×6 inverse.
4. Exact-rational (not f64) test asserting rank 5 / det 0.
5. Remove the `_native_ok()` guard in `pyhecke/gram.py` and its three
   tests in `test_gram_values.py`, restoring the native speedup.

## 2026-08-15 (2) — my own definition-of-done above was WRONG; PR #5069

The 5-step "definition of done" I wrote earlier today treated this as a
port. It is not. Reading the prior agent's decline note in `gram.rs` and
measuring the consumers, **that decline was correct** and this bean
under-scoped the work. Correcting it here rather than leaving a plan that
would have walked the next agent into a breaking change.

### Why the z³ fix is NOT a port

`z³` is what keeps the crate's Gram non-singular. Correcting it deletes
`gram_inverse` — and unlike Python's `G_INV` (measured at **zero**
consumers before removal), this one has a live downstream family:

| consumer | use |
|---|---|
| `pyhecke-native/src/lib.rs:50` | exposed as a pyfunction |
| `gram.rs:619` | certificate builder |
| `borromean-axial-coupling.py:197` | `GRAM_INV[np.ix_(A, A)]` — arithmetic |
| `delta_lambda_master_formula_h3_probe.py` | reads the witness field |
| `delta_lambda_full_variance_phase5e_1.py` | calls the pyfunction |
| `bound_state_observable_validator.py` | **requires** the field |
| `audit_frobenius_pairing.py` | **requires** the field |

The honest replacement is dualisation on `H_3(q)/rad`, which is a
**different object** from what those witnesses hold — so it cannot be
swapped under the same key. Owner decision.

### Why the Q_0 re-pin is separately gated

Measured: **53** `certificate-*.json`, **657** files carrying the muon
literal. AGENTS.md posture for this (bean `tnjb`) is "do not
mass-regenerate" without scoped sign-off. The prior agent's note said the
same. Not taken.

### What PR #5069 landed instead (additive, non-breaking)

`trace_weights_markov`, `gram_from_weights`, `gram_matrix_markov`,
`gram_radical`, `gram_quotient_inverse` — correct objects, 16 cargo tests,
including a cross-language check against `numpy.linalg.pinv` (1e-9) run at
the proton pin passed **explicitly**, so it does not prejudge the Q_0 call.
The switch is now a one-line repoint of `gram_matrix`.

### Revised definition of done

1. **[OWNER]** decide the `gram_inverse` deletion + what replaces the
   dualisation for the seven consumers.
2. **[OWNER]** decide the `Q_0` re-pin (53 certificates).
3. Repoint `gram_matrix` → `trace_weights_markov`; update
   `det_at_q0_convention_d` and `gram_first_row_matches_trace_weights`.
4. Migrate the seven consumers to the quotient inverse under a NEW key.
5. Rebuild `pyhecke_native`; only THEN remove the `_native_ok()` guard in
   `pyhecke/gram.py` and its three tests.

### Related regression found while scoping this (fixed in #5055)

Two producers build their Gram from `pyhecke.gram.TR_M` and call
`np.linalg.inv` themselves — which does NOT raise on the singular D Gram
(entries 7.6e15, ‖G@inv − I‖ = 4.14). Guarded by
`pyhecke.gram.safe_inverse()`.

## 2026-08-15 (3) — Q_0 DONE; trace flip measured

**Q_0 re-pin: owner-approved and landed** (PR #5069). muon
1.1099785955541805 → proton 1.1099785827513808. `markov_z(Q_0)` is now
bit-identical to `pyhecke.gram.z`. 183 cargo tests pass; one pinned
determinant moved by 2.28e-8, consistent with the 1.15e-8 q shift.

**53 certificates NOT regenerated** — they record a superseded anchor and
nothing enforces them (no test cross-checks a committed certificate against
the live Q_0). That is the `tnjb` mass-migration and still needs its own
sign-off.

### Measured impact of the remaining flip (`z³` → `h·z² + z`)

| | value |
|---|---|
| `TR_M[5] = z³` | 0.2299948980341014 |
| `TR_M[5] = h·z² + z` | 0.6911664783584446 |
| change | **+200.5 %** — a tripling, not a correction |

Gram: 19/36 entries change; rank 6 → 5; det −0.152 → 0; cond 12 → 4.9e16.

**‖G⁺ − G⁻¹‖ = 4.26, i.e. 73.3 % relative.** The replacement object is
*substantially* different, so every downstream number derived from
`gram_inverse` moves — this is a re-derivation, not a patch.

### The split that must not be lumped

The two defects hit different consumers:

* **Rust-fed** (`z³` trace rule): `delta_lambda_full_variance_phase5e_1.py`,
  via `pyhecke_native.gram_inverse`.
* **Python-witness-fed** (inverting a singular D Gram):
  `borromean-axial-coupling.py`, `delta_lambda_master_formula_h3_probe.py`,
  `bound_state_observable_validator.py`, `audit_frobenius_pairing.py`.
  Guarded by `safe_inverse` in #5055.

Do not describe all five as "broken by the z³ bug" — only the first is.

### Remaining

1. **[OWNER]** flip `trace_weights`, given the 73 % re-derivation cost.
2. Migrate consumers to the quotient inverse under a NEW key.
3. Rebuild `pyhecke_native`; only then drop the `_native_ok()` guard.
4. **[OWNER/tnjb]** regenerate the 53 certificates.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — BOTH divergences this bean names were resolved on 2026-08-15, ONE DAY after its last substantive update (bean `qou-am5t`)

This bean's premise is *"the Rust bug is not independently fixable … **Do not
'just fix the Rust bug.'** That is the trap this bean exists to name."* That
premise is **overtaken**, and the reason it went unnoticed is a one-day miss:
the bean's last substantive entry is 2026-08-14 and the fix landed 2026-08-15.

`tools/hecke-engine/src/gram.rs`, module header, verbatim:

> *"Both long-standing divergences from the Python mirror are RESOLVED as of
> 2026-08-15: **1.** `TR_M[5]` is now `h·z² + z`, matching `pyhecke.gram.TR_M`.
> It was `z³` here from before 2026-05-19 … **2.** The Gram is therefore
> SINGULAR, and that is correct, not a defect."*

So the coupling this bean predicted **did materialise and was handled**:

- `gram_inverse` is **REMOVED** (`:383`), not deprecated and deliberately *not*
  rebound to the pseudoinverse — *"they differ exactly on the radical, which is
  the entire content of this change; handing a caller a different matrix under a
  name they already trust is how a wrong number keeps circulating."*
- `gram_quotient_inverse` (Moore–Penrose on `H_3(q)/rad`) and `gram_radical`
  are the replacements, which is this bean's Remaining item 2 — *"migrate
  consumers to the quotient inverse under a NEW key"* — done, and done the way
  the item asked.
- The re-derivation cost in Remaining item 1 is measured in that same header:
  `TR_M[5]` +200.5 % (0.2300 → 0.6912), 19 of 36 Gram entries move, rank 6 → 5,
  `‖G⁺ − G⁻¹‖` **73.3 %** relative — *"this was a re-derivation, not a patch"*.

**NOT verified by me, and the reason this bean stays open:** Remaining items 3
and 4 — rebuild `pyhecke_native` and drop the `_native_ok()` guard, and
regenerate the 53 certificates (marked `[OWNER/tnjb]`). `pyhecke_native` is not
installed in this container, which is the same caveat this bean already records
for the C/D split measurement, so the live split is still not observable here.

**Correction of my own, made the same hour:** in the `qou-cdx1` re-audit append
I listed this bean as *"measurably satisfied"* on the strength of a single
grepped line (`gram.rs:138`). That was too fast and it is retracted — the
headline bug is fixed, the bean is not. Retracted on `qou-cdx1` as well. It is
an instance of exactly the hazard the re-audit's own status doc warns about: a
path- or line-level match tests whether a *file* still carries a defect, not
whether a *bean's claim* is closed.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

See the dedicated 2026-10-10 append: both divergences it names were resolved
2026-08-15, ONE DAY after its last substantive update, but Remaining items 3-4
(rebuild `pyhecke_native`, drop the `_native_ok()` guard; regenerate the 53
certificates, [OWNER]) are unverified and `pyhecke_native` is absent here. I
called this one satisfied off a single grepped line and retracted it within
the hour.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## 2026-10-10 — the wheel was built and measured; items 1–3 hold, item 4 is the only live part

This bean's standing caveat was that `pyhecke_native` had never been present in
the container that judged it, so the live split was "not observable here". It is
now observed. Built with `bash scripts/build-pyhecke-native.sh` on `main`
`fbc1f5f580` (pyhecke-native 0.9.0, Python 3.13), then compared at the proton
pin `q0 = pyhecke.gram.q0`:

| check | result |
|---|---|
| `markov_z(q0)` native vs registry D | `0.6126880371464652`, diff `0.0` |
| `max|trace_weights − TR_M|` | `0.0` |
| `TR_M[5]` native | `0.6911664783584446` = `h·z² + z`, not `z³` |
| `max|gram_matrix − G|` | `0.0` |
| `max|gram_quotient_inverse − G_PINV|` | `4.44e-16` (f64 floor) |
| `gram_determinant(q0)` | `0.0` |
| `pyhecke.gram._native_ok()` | `True` — the self-check passes, native path ENABLED |
| `tools/pyhecke/tests/test_gram_values.py` | 24 passed, 1 skipped (the wheel-absent test, by design) |
| `cargo test --release gram` (hecke-engine) | 22 passed |

The test file needs `computations/substrate` on `PYTHONPATH` for `hecke_core`;
without it three tests fail with `ModuleNotFoundError`, which is an environment
fact, not a defect.

So Remaining items 1–3 of the 2026-08-15 (3) list are done and now verified
against a real wheel: the trace flip landed, consumers moved to the quotient
inverse under a new key, and the old refusal guard was replaced by a runtime
convergence self-check that a correct wheel passes. Note the self-check compares
in f64 at `atol 1e-9`; it cannot see a divergence below that.

**Live remainder: the 51 `tools/hecke-engine/certificate-*.json`** (the bean
says 53; 51 is the hecke-engine set, the other 2 are under `_deprecated/`). Their
`*_f64` fields were evaluated at the literal `1.10998` (1277 ppb from proton).
`scripts/reanchor_certificates.py` dry run, same commit:

- 22 re-anchorable (exact Laurent polynomial in the file; the stored f64
  reproduces from it, then re-evaluates at proton),
- 12 blocked (`tr_markov_f64` has no exact source; a partial write would leave a
  file on two anchors),
- 1 keep (v9 used MPFR, committed value is the accurate one),
- 16 skipped (no exact polynomial; these need their generator re-run).

Writing the 22 is not done. It needs the owner's sign-off per the
mass-regeneration posture (`tnjb`), and it is the only thing keeping this bean
open. Consumers found by grep are the v9/v10/v11 binaries and `_deprecated/`
scripts only, so no paper-facing number reads these fields.


## 2026-10-10 — after #7606 merged: the 12 BLOCK files are convention C

The 22 re-anchorable certificates landed on `main` (574778dcd2). Of the 29
left (12 BLOCK, 1 KEEP, 16 SKIP), the 12 BLOCK carry a `tr_markov_f64` the
script called "no exact source". Measured: `v9.rs` computes it as
`Σ_ℓ jets[ℓ]·z^ℓ / 2^pn_count` with `z = 1/(t+t⁻¹)`, `t = √q`, i.e.
`z_C = √q/(q+1)`. The exact `jets` reproduce the committed value at
`q = 1.10998` to ~12 digits on 4H (0.34245912352), 5He, 5Li, 8Be, 8Li; the
ill-conditioned files differ by float64 cancellation only (40Ar's jets are
65 entries, 1 non-empty, so there `tr_markov_cleared` is the source).

So these 12 values are **convention-C**, not merely un-anchored; re-anchoring
gives C at the proton pin. A D value needs a re-derivation, not a z-swap.
Consumers: `fsh-guts/deprecated/computations/{certificate-to-mass,
atom_mass_integrated,isotope-mass-table}.py` only. `v9.rs` is a Rust
convention-C site that the `.py`-only detectors cannot see. Disposition put
to the owner on a decision card (record / strip / re-derive / leave);
data unchanged. Bean stays open: the 12 + 16 are not resolved.

## 2026-10-11 — convention-D derivation done (owner: "do fresh conv D derivation")

**Correction to the 2026-10-10 entry.** v9's `tr_markov_f64 = Σ_w c_w z^len(w)`
is not a Markov trace in any convention, not merely "convention C": the trace
is not multiplicative in length (`tr(σ₀σ₁σ₀) = h·z² + z`, not `z³` — the
`gram.rs` `TR_M[5]` defect, at every length). Matching the committed value
under that rule identifies the formula; it does not make it a trace.

**Second finding.** 34 of the 35 v9 certificates (all stamped at eight
2026-04-05 commits, `62d305e` …) were built with the pre-fix n-n crossing
`t⁴σ + t − t³`, which is not ∝ `σ⁻¹ = σ − h` under v9's own `σ² = hσ + 1`.
Their exact polynomials carry odd t-powers; the current crossing gives none.
Only 40Ar (`1b1b1d5`) is on the fixed crossing. So the 22 fields re-anchored
in #7606 evaluate a mis-built element. Consumers: `fsh-guts` deprecated only.

**Derivation.** `computations/probes/v9_markov_trace_convention_d_probe.py`
builds the full crossing product exactly in the T_w basis of H_A(q), takes the
Ocneanu trace with z formal, then sets `z = q³/(q²+1)` at the proton pin, ÷2^pn.
Independent check: equals v9's own per-word dump (new `V9_DUMP_ELEM` env var)
coefficient for coefficient for 4H, 5He, 5Li, 8Be, 8Li.

| nucleus | tr_M^D / 2^pn |
|---|---|
| 4H | 0.18985120016031935518 |
| 5He | 0.04540796648400091477 |
| 5Li | 0.09459886467903922151 |
| 8Be | 0.01175448834274849400 |
| 8Li | 0.00499350907470217024 |
| 10B | 0.02426288147931621954 |
| 10Be | 0.01524043161227817558 |

Not computed: 12B (T_w-basis product exceeded container memory); every
A > 12 certificate and v9's own 10B/10Be/12B runs strip mid-construction,
so the stored object is not a product. No certificate data changed; what to
do with the corpus is put to the owner.

## 2026-10-11 (2) — v9 computes the trace; the 35 are regenerated (#7686, merged)

Owner picks on #7685: delete `tr_markov_f64`, keep the old version on
fsh-guts, and have v9 compute the real trace. Done, and merged as 33d54fd71b.

- `tr_markov_f64` / `tr_markov_cleared` / `tr_markov_denom_power` are gone from
  v9 and `certificate.rs`. The removed code and every certificate's old values
  (before and after regeneration) are on `cat/cat-harness/fsh-guts` at
  4b5f1247f9, `fsh-guts/deprecated/tools/hecke-engine/v9-tr-markov-zlen/`.
- v9 now writes `tr_markov_d`: the element is re-expanded in the T_w basis and
  traced exactly by `tr(x T_{n−1} y) = z·tr(xy)`, as a polynomial in z over
  ℤ[t, t⁻¹]; then `z = q³/(q²+1)` at the 50-digit proton pin, ÷ 2^pn,
  60 digits, with the exact terms. A runtime self-check asserts
  `tr(σ₀σ₁σ₀) = h z² + z`.
- It is computed only when nothing was stripped mid-construction: **12 of 35**
  (4H 5H 5He 5Li 6H 7Be 7H 7He 8Be 8H 8He 8Li). All 12 agree with the Python
  probe to 1e-60 relative. The other 23 record why (stripped, so not the
  product).
- All 35 v9 certificates are regenerated with the current crossing at the
  proton pin. F_Pauli moved by up to three orders of magnitude (8H 0.81 → 1397);
  word counts grew from A to as many as 23263 (13N). So the 22 fields #7606
  re-anchored are superseded.

**Still open, so the bean stays `todo`:** the 16 non-v9 certificates
(`hecke-crt`, `hecke-modular`) that `reanchor_certificates.py` SKIPs still carry
`*_f64` fields at the 5-digit `1.10998` anchor, and have no exact polynomial to
re-anchor from; they need their own generators re-run. And 23 v9 nuclei have no
trace, because v9 strips them; a strip-free build of A ≥ 9 did not fit in memory
here (12B).

## 2026-10-11 (3) — the other 16 certificates, and the trace past A = 8

- `hecke-modular` (v11) evaluated at a local literal `1.10998` while recording
  `gram::Q_0`. Fixed, and all 15 hecke-crt / hecke-modular certificates are
  regenerated at the proton pin (`4he-crt` carries residues only). Issue #7717.
- **Finding:** for builds that strip words mid-construction, `f_pauli`
  depends on the strip threshold, not only on the nucleus. Measured on 11B:
  0.31 / 0.89 / 2.92 / 2.80 / 9.25 / 31.9 / 81.4 at thresholds
  1e3 / 5e3 / 1e4 / 2e4 / 5e4 / 1e5 / 2e5. The old 11B/12C/14N/16O
  certificates recorded no argv, so their threshold cannot be recovered.
- **Trace for A ≥ 9:** `computations/probes/markov_trace_two_row_tower_probe.py`.
  Under convention D only two-row shapes carry weight,
  `y_(n-k,k) = [n-2k+1]_q / [2]_q^n`, so the trace is a sum of two-row
  seminormal characters built up the Hecke tower (Gelfand–Tsetlin basis,
  each level embedded block-diagonally into the next). It agrees with v9's
  `tr_markov_d` to all 60 printed digits on all 12 nuclei v9 could do. 63
  isotopes computed (Z = 1…8, A ≤ 16), covering every certificate nucleus
  with 9 ≤ A ≤ 16. Cost grows like Catalan(A): A = 14 takes about 3 min,
  A = 16 about 48 min, in Python. 19F, 20Ne, 40Ar, 40Ca and 60Co are still
  out of reach.
- 2026-10-12 (owner "1 2 3"): the tower values are written into 49
  certificates' `tr_markov_d` by `tools/hecke-engine/scripts/attach_tower_trace.py`
  (textual splice, so nothing else in a file changes; pn checked against
  `pn_count`). Each value now carries `method`: v9's own trace, or the tower
  probe's. A Rust port (for 19F/20Ne) and a structure search for A = 40 are
  under way.

## 2026-10-12 (stream 4, session_01PmZzY27QHceKGXwNivRt64) — Rust/MPFR port of the tower trace

`tools/hecke-engine/src/bin/two_row_tower_trace.rs` (`two-row-tower-trace <Z> <N>`). Same element,
same convention-D two-row weights, same seminormal basis as the Python probe, but computed
**column by column**: `chi(E) = Σ_j (E e_j)_j`, each `E e_j` by applying the sparse factors
`a + bσ_i` to one vector in reverse order. Memory O(d) per thread instead of O(Catalan(A)),
which is what makes A = 19, 20 possible at all (Catalan(20) ≈ 6.6e9 entries). rug/MPFR at 300
bits, q0 from its 50-digit string, rayon over columns (4 threads). Self-checks as the probe
(worst residual 1.2e-89).

Validated against the Python witness, all 60 printed digits identical: 6Li, 9Be, 12C, 16O.
16O: 71 s wall (Python: ~48 min). Throughput ~6e7 factor-applications/s on 4 threads;
projected 19F ≈ 1.4 h, 20Ne ≈ 6 h. Runs launched; results to follow.

## 2026-10-12 — follow-up (3): Yang–Baxter / R-matrix structure for A = 40. FINDINGS ONLY, no result.

Probe `computations/probes/v9_element_ybe_structure_probe.py`, 5/5, exact sympy over Q(q), no float.

- **B1 Baxterisation (holds).** All three v9 factors are the Jones-Baxterised R-matrix
  `R(x) = xσ − x⁻¹σ⁻¹` up to scalars: pp = lim x⁻¹R(x) (x→∞), nn = lim −xR(x) (x→0), pn = −iR(i).
- **B2 YBE (holds).** `R₁(x)R₂(xy)R₁(y) = R₂(y)R₁(xy)R₂(x)` on every irrep of H₃.
- **B3 — but no difference-type spectral parameters fit.** A vertex-model reading needs
  `x_ik = u_i/u_k`; pp would need `R(1)`, and `R(1) = h·1` is a scalar, not σ. (A product form
  `x_ik = u_i u_k` fits only in the degenerate limit u_p→∞, u_n = i/u_p→0.)
- **B4 — and the labels are by POSITION, not strand.** At A = 6, 13 of 15 crossings carry an (i,k)
  label that is not the pair of strands actually meeting there. So the v9 element is not a vertex-model
  partition function on its own braid diagram, and commuting-transfer-matrix / Bethe-ansatz
  integrability does not apply to it as defined.
- **B5 — the one exact reduction:** the last factor is the only use of σ_{A−2}, so
  `tr(E) = (a + b z_D)·tr(E')` (Markov). It does not iterate (σ_{A−3} is used twice).

**Cost wall for A = 40.** The irrep decomposition is already optimal for this element:
column work `L·Catalan(A)` ≈ 780 × 2.6e21. No route to A = 40 was found. Scope (a): this is about the
v9 element *as constructed*; whether a strand-labelled element (a modelling change, owner's call)
would be integrable is untested.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8378, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-15: "docs(pyhecke-native): native gram path ENABLED — qou-m7py resolved"). The work may be partly or fully done. Read the bean before you close it.
