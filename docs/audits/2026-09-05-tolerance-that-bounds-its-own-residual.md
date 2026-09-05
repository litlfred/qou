# A tolerance that bounds its own residual — the `qou-tol0` root cause, and its detector

**Date** 2026-09-05 · **Bean** `qou-tol0` (root cause), `qou-26f2` (the sibling class) ·
**Detector** [`computations/audits/tolerance_from_residual_audit.py`](../../computations/audits/tolerance_from_residual_audit.py)

## The claim

`Assertion.passed` is `|computed − expected| ≤ tolerance`. When the tolerance is
itself a function of that residual, the inequality holds for every input and the
assertion cannot fail. **Seven such assertions are live on `main`**, in six
producers, and every existing assertion audit misses all seven.

This is the *shape* behind `qou-tol0`. That bean's own instance —
`atom_mass_derived.py`, ten assertions under `tolerance=max(abs(r.delta_MeV)*2, 50)`
where `delta_MeV` **is** the residual — was fixed in `7f95ad5962`. The shape was
never made detectable, so nothing stopped it recurring or noticed where it
already had.

## Why six existing audits miss it

Checked against the pre-fix `atom_mass_derived.py` at `7f95ad5962^`; **zero hits
from any of them**.

| audit | what it asks | why it is blind here |
|---|---|---|
| `self_fulfilling_assertion_audit` | is `computed` the same AST as `expected`? | they differ, and they differ *correctly* |
| `always_vacuous_assertion_scan` | same | same |
| `scripts/tautological-assertion-census` (`qou-26f2`) | same, corpus-wide | same |
| `vacuous_pass_assertion_scan` | are both sides zero-initialised counters? | neither side is a counter |
| `assertion_on_literal_audit` | does `computed` trace to a literal? | it traces to a real computation |
| `tolerance_below_arithmetic_floor_audit` | is the tolerance too **small** to be reachable? | the **mirror** of this question |

The witness-level `witness_assertion_slack_audit` sees it only by its
*consequence* — it fires when the recorded `tolerance ≥ |expected|`, which
happens when the computed value collapses toward zero. A tautological tolerance
on a producer whose numbers happen to land close records a small tolerance and is
invisible there. **Source is the only place the defect is always visible.**

## Method: two provable shapes and one heuristic, reported separately

| shape | basis | what it catches |
|---|---|---|
| `identical-after-substitution` | proof | `computed` and `expected` are the same expression once single-assignment names are substituted — residual identically 0, and the tolerance never enters |
| `triangle-bound` | proof | tolerance is `k·max(\|c\|,\|e\|)` with k ≥ 2, `k·(\|c\|+\|e\|)` with k ≥ 1, or `k·\|c−e\|` with k ≥ 1 |
| `residual-named` | name + dataflow | a residual-named identifier in the tolerance resolves, through assignments, to something mentioning both sides' quantities |

The first two are **proofs about arithmetic**, not signals: the assertion is
unfalsifiable whatever the data. Only the third is heuristic, and it is the one
the `qou-tol0` instance needs, because `abs(r.delta_MeV)` is an attribute whose
relation to the residual lives two hundred lines away.

**Closing both sides over assignments is what makes the third route work.** The
tolerance reaches `delta`, defined `delta = M_derived − M_obs`, while `computed`
reads `r.M_derived_MeV`. Those names never meet — the link is the dataclass
keyword `M_derived_MeV=M_derived` one construction earlier. Comparing the
residual's reach against the call's raw leaves put the known positive in
**review**; closing both sides recovers it as **blocking**.

## Both corrections shrank it: 38 → 7

The first corpus run reported 38 blocking. Reading them rather than counting them
found two unsoundness sources, now pinned by a negative control in `--selftest`:

- **A container assigned once and then mutated is not a constant.**
  `wired = []` followed by `wired.append(...)` counts as a single assignment, so
  substituting the initialiser turned the real coverage check
  `len(wired) == len(per_nucleus)` into `len([]) == len([])`
  (`audit_lean_uniqueness_ref_wiring.py:195`). One assignment is not one value
  when the object is mutable.
- **Raw-identical arguments belong to the existing census.** `computed=3,
  expected=3` is `qou-26f2`'s finding, already counted there at 266 corpus-wide.
  Reporting them here would have inflated this audit with hits someone else
  owns. What is new is only the case that needs an *indirection* to see.

## The seven, each verified by hand

| producer:line | assertion | why it cannot fail |
|---|---|---|
| `mass-from-q-symbolic.py:568` | `𝔪(𝔅₃) Borromean topological mass` | `borromean_mass_ratio` is defined as `VOL_BORROMEAN / HBAR_Q_SQ0` (line 246); `expected` restates it |
| `mass-from-q-symbolic.py:577` | `𝔪(𝔅₃) in MeV` | both sides expand to `VOL_BORROMEAN / HBAR_Q_SQ0 * M_E_MEV`; **witness records residual 0.0 exactly** |
| `confined_knot_binding.py:289` | `W_sym equals W_alt` | `W_SYM` and `W_ALT` are the same expression, character for character (lines 42, 44) |
| `confined_knot_binding.py:308` | `V_pn = W_std*(z+d_pn)` | `expected` restates `V_pn_exact`'s definition (line 251) |
| `yekutieli_borromean_h2_extraction.py:216` | `kappa_computed` | `tolerance = 2·max(\|c\|,\|e\|)`; no data can exceed it |
| `compute_atom_chi_rust.py:164` | `rust_kernel_loaded` | `float(x)` against `x`, same subscript — the `float()` is what hides it from the raw-AST census |
| `channel_asymmetry_crossing_budget_bound_probe.py:204` | `budget_is_s_squared` | `c_inter = s * s` (line 134); `expected` is `s * s` |

Two are worth reading twice.

**`W_sym equals W_alt`** carries `source="Wedderburn-Artin: dim_q((3))=dim_q((1,1,1))=1"`.
It advertises a check of a representation-theoretic fact — that the two
one-dimensional Hecke blocks have equal q-dimension. It checks nothing: the two
constants are one expression written twice. **If the Wedderburn–Artin fact were
false, this assertion would still pass.** That is the failure mode in its purest
form — the `source` field is doing all the epistemic work and none of it is
tested.

**`kappa_computed`** is the one with a live wrong number behind it. Recorded:
`computed = 0.1875`, `expected = −0.915965594177219…`, `tolerance = 1.8319…`,
`passed: true`. The two do not share a sign; the residual is **1.1035**, a 121 %
miss. It passes because `2·max(|c|,|e|) = 1.8319` and `|c − e| ≤ |c| + |e| ≤
2·max(|c|,|e|)` for all real values. `witness_assertion_slack_audit` already lists
this one under **review** on the recorded numbers; what is added here is *why* —
the bound is a theorem, not a threshold.

## The name signal alone found nothing

All four `review` hits — residual-named tolerance, no dataflow confirmation —
are false or already adjudicated:

- `codata_reconciliation.py:298`, `tolerance=row['codata_err'] * 2` — a 2σ
  **experimental** error bar. Correct, and the model's error has nothing to do
  with it. It matched only because `codata_err` contains `err`.
- `kummer_reflection_zeta5.py:186,197` — a residual compared to zero under a
  *fixed* `RESID_TOL`. Correct; `computed` is named for the residual, the
  tolerance is not derived from it.
- `binding_energy_scale_probe.py:122`, `E0_improves_deuteron` — computed
  `|err_e0|`, expected 0, tolerance `|err_qb|`: "the E₀ error is no worse than
  the Q_β error". The tolerance is a **different** error from the one being
  bounded, so it can fail. The `qou-tol0` bean already calls this defensible.

So the heuristic tier is 0-for-4, and both provable tiers are 7-for-7. That is
worth stating rather than hiding: a name is evidence about what an author called
a quantity, never about what it holds — and this audit keeps the two apart on
purpose instead of folding them into one verdict.

> **🛑 That sentence overstated the dataflow route, and fixing a producer is
> what showed it (corrected the same day).** "0-for-4" and "7-for-7" are both
> accurate *on `main` as it stood*: all seven blocking hits were provable-shape,
> and the dataflow half of the `residual-named` tier fired on **nothing** there.
> But I read its zero as soundness. It was untested.
>
> Once `mass-from-q-symbolic:599` was given an independent `expected`, it was
> **still** reported blocking — its tolerance `borromean_mass_MeV_err` is
> residual-named and reaches both sides. It is a 1σ **propagated uncertainty**,
> `sqrt((ratio_err·m_e)² + (ratio·m_e_err)²)`, and entirely correct. An
> error-propagation formula mentions the measured quantities for exactly the
> same reason the residual does, so name-plus-reachability cannot separate them.
>
> The discriminator is that **a residual is a difference**. `_reaches_subtraction`
> now requires a `Sub` in the provenance; that keeps the `qou-tol0` positive
> (`delta = M_derived − M_obs`) and drops the class. Recorded as row 34 of the
> detector-blindness taxonomy.
>
> **Zero hits is not the same as verified sound.** The general form of this
> error is worth more than the instance: a tier that has never fired has been
> measured for recall and not at all for precision.

## What would close this

Fix at the producer, per assertion, and expect some of them to go **red**:

- **`kappa_computed` — DONE.** Two falsifiable assertions replace it;
  `yekutieli_kappa_equals_minus_G` **fails** at 121 % and `allPassed` is now
  false. κ = 3/16 was verified exact (residual `0.0` at dps 30, 50 and 80)
  before being asserted — the producer had been *printing*
  `mpmath.identify(κ) = (3/16)` and asserting nothing about it. The same
  expression was also the witness's only raw-float64 field, so the drain is
  1 → 0.
- **`mass-from-q-symbolic:568,577` — DONE.** Both now compare against
  `Vol / (1 − 1/q)²` recomputed from `q` rather than against the precomputed
  `HBAR_Q_SQ0`, verified equal to the bit before wiring. Falsifiable: a 1 ppm
  drift in `q₀` moves the value by 0.0136 against a 1e-6 tolerance. The
  assertion names and `source` fields state plainly that this is a **regression
  guard on the constants**, not evidence for the mass formula.
- **`confined_knot_binding:289,308` — OPEN, deliberately.** The obvious repair
  is ruled out by measurement: `y_lambda_at(3, q₀)[(1,1,1)] = 0.0` under the
  SU(2) truncation while `W_ALT` is nonzero, so `W_λ` and `y_λ` are different
  objects sharing a subscript. Repairing these needs the intended independent
  source for `W_ALT`, which is research rather than a substitution.
- The two self-reports (`rust_kernel_loaded`, `budget_is_s_squared`) are the
  benign class `always_vacuous_assertion_scan` already documents. Renaming is
  enough; they inflate `allPassed` but assert nothing false.

**Do not widen anything to make this green.** The audit exits 1 on any blocking
hit, and the fix is always at the assertion, never at the detector.
