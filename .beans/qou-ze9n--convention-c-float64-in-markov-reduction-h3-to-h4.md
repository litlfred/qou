---
# qou-ze9n
title: Convention-C + float64 in markov_reduction_h3_to_h4_verify — cited as Lean keystone evidence
status: completed
type: task
priority: normal
created_at: 2026-08-22T09:59:39Z
updated_at: 2026-08-29T16:35:03Z
---

## What was found

`computations/probes/markov_reduction_h3_to_h4_verify.py` carries two defects,
and its conclusion is quoted in `QOU/Machinery/MarkovTraceOnHecke.lean` as the
evidence for keystone ingredient 2 (the `Ind_{H3}^{H4}` Markov stabilization).

**1. Convention C, after the 2026-08-15 ruling excised it.** Line 60:

```python
z = float(+(1.0 / (mp.sqrt(Q_MP) + 1.0 / mp.sqrt(Q_MP))))
```

Measured at the proton pin: this is **0.4993203342**, which is `sqrt(q)/(q+1)`
= z_C exactly. Convention D is `q**3/(q**2+1)` = **0.6126880371**. They differ
by 0.113 — 23 %, a different quantity, not a rounding difference.

**2. float64 end to end**, against the STRICT 2026-08-18 "PROBES ARE NOT
EXEMPT" directive:

- `q = float(Q0_FLOAT)`
- line 60 computes inside `mp.workdps(100)` and immediately casts to `float` —
  the dps no-op the precision gates exist to catch, buying 100 digits and
  discarding them on the same line
- `np.eye`, `np.trace`, `float(np.trace(M))`
- `np.linalg.solve(A, b)` for the Markov weights `y_vec` — a linear solve on a
  character matrix, in float64, where conditioning can be far worse than 1e-16
- `TOL = 1e-9`

## Why this is not just hygiene

The directive's own reasoning applies exactly: *"A witness is a number that
gets re-derived; a probe conclusion is an argument that gets written into a
bean, an audit doc, a PR body and a content block, where nothing re-derives
it."* Here the argument was written into a **Lean docstring**, as the evidence
for a keystone ingredient, and has sat there since.

## Done under this bean

- Extended `scripts/convention-c-producer-audit.py` with `unwrap_casts()` so
  the cast-wrapped spelling is matchable at all — it was blind spelling #14,
  recorded in `docs/audits/2026-08-15-detector-blindness-taxonomy.md` §7.
  Self-test battery 50 -> 58, all pre-existing cases still pass.
- Re-measured: the fix moves the actionable count **1 -> 2**, not 0 -> 2. The
  other site (`qbeta_h_frame_rungs_probe.py:73`) was already detected.

## NOT done — deliberately

The probe has **not** been ported to D or to exact arithmetic. Both changes
alter what the keystone evidence says, and the Markov law
`tr_M4(x*sigma_2) = z*tr_M3(x)` contains `z` explicitly, so a C -> D swap can
change whether it holds. That is a re-derivation, not a migration — the same
distinction AGENTS.md draws for the c_k ladder under `qou-cds1` ("not a
z-swap, and that is proved").

Next honest step: re-derive under D in exact arithmetic and report whether the
stabilization law survives. If it does, the keystone evidence is upgraded from
float64/C to exact/D. If it does not, `MarkovTraceOnHecke.lean`'s ingredient-2
paragraph needs rewriting, and that is the more valuable outcome.


## ANSWERED (2026-08-22) — the conclusion is convention-robust

Re-ran the same over-determination test at **50 dps under both conventions**
(`computations/probes/markov_reduction_h3_to_h4_conventions.py`):

    z_C = 0.499320334184     worst |tr4(x.s2) - z*tr3(x)| = 1.336e-51
    z_D = 0.612688037146     worst |tr4(x.s2) - z*tr3(x)| = 4.009e-51
                             worst |tr4(x)     - tr3(x)|  = 2.673e-51  (both)

Nine over-determination words, 1e-30 tolerance. **PASS under both.**

Residuals at ~1e-51 with 50-dps arithmetic are agreement *to the limit of the
arithmetic used*, not an exactness claim — the same phrasing discipline the
float64 rule imposes, applied one tier up.

**Why it is robust, structurally.** `z` is an *input* to the weight solve: the
`y_lambda` are fitted so `tr(sigma-word of length k) = z^k`, and the reduction
is then checked on other words. The Ocneanu trace is a one-parameter family in
`z`, so the Markov law is insensitive to which member is chosen. The C defect
is real but does not touch the conclusion.

**So `MarkovTraceOnHecke.lean`'s ingredient-2 paragraph does NOT need
rewriting on convention grounds** — the outcome I had flagged as the more
valuable one did not occur. Docstring updated to carry the three caveats and
point at the companion probe.

## Also fixed: the cited probe did not run

Third defect, found while trying to reproduce it. Bootstrap omitted
`tools/qou-substrate/python` entirely and added
`tools/pyhecke/python/pyhecke` — the package directory — where the qou-mass
shim's `from pyhecke.syt_prefix_cache import *` needs the parent. Neither
package is installable (both 404 on PyPI), so this was fatal, not fragile.
Fixed; the probe now runs unaided.

## Left deliberately

The original stays float64 and convention C, as the historical record of what
the Lean docstring cites, with both facts now stated in its own docstring. New
work should use the companion. Porting the original would rewrite cited
evidence for no gain now that the conclusion is known to be robust.


## 2026-08-25 — LEFT ON C DELIBERATELY in the probe drain, and the detector still lists it

The probe/derived-tower convention-C drain (PR #5739) had
`computations/probes/markov_reduction_h3_to_h4_verify.py:84` in its assigned
file set and **did not migrate it**. Recording why, so the next drain does not
spend the same time re-deriving the decision.

The file's own docstring (added by this bean, 2026-08-22) already declares it
convention C, quantifies the gap (z_C = 0.4993203342 vs z_D = 0.6126880371,
23 %), records that the *conclusion* survives the swap because z is an INPUT to
the weight solve rather than an output, points at the 50-dps companion
`markov_reduction_h3_to_h4_conventions.py` that measures both frames
(worst residual ~1e-51 against a 1e-30 tolerance), and states the float64 is
kept deliberately as "the historical record of what the Lean docstring cites".
Migrating it would destroy that record. So: left alone, correctly.

**But `scripts/convention-c-producer-audit.py` still counts it ACTIONABLE**, so
it will be handed to every future drain as work. The detector decides
"deliberate" from the *variable name* —

    DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)   # :93

— and this file's variable is plain `z`. A docstring declaration, however
explicit, is invisible to it. The intended channel is the registry
(`docs/coordination/trace-convention-registry.json`), via `blocked_migrations`
or `intra_module_split_waivers`.

**Both of those lists are currently EMPTY (`[]`).** So nothing in the corpus is
registered as deliberately-C today, and adding the first row is a policy move
rather than routine maintenance — which is why the drain did not add one
unilaterally, especially with a sibling branch active on the same registry.

Next honest step is one of: (a) add the registry row and let the detector read
it, or (b) teach the detector to honour an explicit in-file marker. Until
either lands, this file re-surfaces as actionable on every run and each drain
has to re-read the docstring to find out it is fine.


### Addendum 2026-08-25 — the basis for leaving it was the DOCSTRING, not the classifier

Recording this explicitly because `qou-4bq3` has since shown the audit's
`deliberate` column is unreliable (its `re.I` regex case-folds `C_` to `c_`, so
ordinary identifiers like `qfac_3`, `c_k` and `c_mp` match), and a reader could
otherwise assume this file was skipped on that column's say-so.

It was not. The basis is the file's own prose, which meets the standard a
classifier cannot: it names convention C **and** convention D, gives both
numeric values (0.4993203342 vs 0.6126880371) and the 23 % gap, states WHY both
are present, and points at `markov_reduction_h3_to_h4_conventions.py` which
measures the over-determination test under both at 50 dps. That is a genuine
comparison record; the classifier's opinion was not consulted and would not
have changed it.

For completeness, this file's `deliberate` verdict was NOT among the seven
collisions `qou-4bq3` measured — but six other files in the same drain's set
were, and all six were migrated anyway because each was read.

Closed 2026-08-29: landed in PR #5754. markov_reduction_h3_to_h4_verify::z is registered blocked-on-C-by-design; verified on main today — it is the one row the audit excludes from ACTIONABLE.
