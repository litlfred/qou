---
# qou-cds4
title: 'S4 (SCIENCE): p/n convention — 6 live non-comparison files + 28 witnesses off bring_color_weighted'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-26T13:20:06Z
---

Parent: `qou-cdx1`. Ruling R3: `pn_convention="bring_color_weighted"` is
canonical.

## Measured 2026-08-15 (live Python assignments, excluding `_deprecated/`)

| value | assignment sites |
|---|---|
| **`bring_color_weighted`** (canonical) | **16** |
| `chi_lambda_braid` | **9** |
| `strict_averaged` | **6** |

83 files mention `pn_convention` overall (`.py`+`.json`+`.md`).
**28 committed witnesses** record a non-colour-weighted `pn_convention`.

## R3 is largely already true

`bring_color_weighted` is already the default in the production path:
`closed_form_tau_M.py` (×4) and `mass_at_3A_proper.py`. R3 makes it canonical
and puts the alternatives on notice.

## The 8 live Python files off-canon

```
computations/_habiro_coefficient_extract.py
computations/atomic_tr_m_helium4_canonical.py
computations/binding_bring_enhancement_compare.py      <- name says comparison
computations/binding_canonical.py                      <- READ THIS FIRST
computations/binding_combiner_markov_peel_fallback.py  <- PN_CONVENTION = "strict_averaged"
computations/chi_monotone_transfer.py
computations/closed_form_tau_M_verification_phase5q.py
computations/iterative_knot_builder.py
```

**`binding_canonical.py` first.** A file with `canonical` in its name assigning a
non-canonical p/n convention is either a naming defect or a real one, and the
two need different fixes.

`*_compare` and `*_fallback` are plausibly legitimate under R3 — a **labelled**
comparison against a non-canonical convention is fine. Confirm the label exists;
do not assume it from the filename.

## Why SCIENCE and not hygiene

`chi_lambda_braid` vs `strict_averaged` vs `bring_color_weighted` is the p/n
interface factor — the Bring colour-weighted asymmetry. Switching it moves
binding numbers. This is not a rename.

## MEASURED 2026-08-19 — the two off-canon conventions are 1210x apart, and the bean lists them as one job

Claimed from `todo`. The bean above says *"switching it moves binding numbers.
This is not a rename"* — true, but with no magnitude the eight files read as one
queue. They are two populations, three orders of magnitude apart.

Per p-n interface factor at the proton-pinned q0 (50 dps, `closed_form_tau_M`
+ `_avg_color_delta`):

    chi_lambda_braid  -> positive  z              = 0.6126880371464652516
    strict_averaged   -> averaged  z - h/2        = 0.50815788774864559388
    bring_color_wtd   -> weighted  z - h(1/2-d/4) = 0.50822978937673896258

    chi_lambda_braid -> canonical :  -17.0492 %
    strict_averaged  -> canonical :   +0.0141 %

Ratio **1210x**. The `-17.05%` is the legacy marshalling drop that
`canonical_interface_kinds`' own docstring describes — *"maps (c=1, d=-h/2) to
(sign=+1, gen) and silently drops the -h/2 coefficient"* — and it independently
reproduces the ~21% figure Phase 5q recorded from the other direction.

**Do not order S4 by file count.** The 9 `chi_lambda_braid` assignments are the
whole tranche's weight; the 6 `strict_averaged` ones are the delta question this
arc has spent four PRs on, and are 1210x smaller than the convention sitting
next to them.

### The effect does not grow with A

`canonical_interface_kinds` models the atom as the block word `p^Z n^N`, so the
census is **Z-1 p-p, exactly 1 p-n, N-1 n-n** — verified D through 12C:

    5Li  Z=3 N=2  {positive: 2, averaged: 1, negative: 1}
    12C  Z=6 N=6  {positive: 5, averaged: 1, negative: 5}

One p-n boundary per atom, for every atom. So the per-bond figure IS the tr_M
figure, with no compounding, and every Z>=1,N>=1 atom in the table takes the same
single multiplicative hit. That is convenient for the migration and worth stating
plainly: this is a uniform rescale of the affected rows, not an A-dependent one.

### Blast radius of the `_habiro_coefficient_extract.py` site specifically

27 committed `habiro-coefficients-*.witness.json`. The module declares its
convention in its own docstring (*"the production `chi_lambda_braid`
convention"*), so it is not an accident — it is a file that was correct before
the migration and was never revisited. `atomic_tr_m_helium4_canonical.py` and
`closed_form_tau_M_verification_phase5q.py` are the same shape.

Note on Phase 5q: its witness validates the closed form against the empirical
slow path to 1e-49 **under `chi_lambda_braid`**. That is a self-consistency check
*within* the legacy frame. It is not evidence for the frame, and it will need
re-running rather than re-reading once S4 lands.

### Next step

`binding_canonical.py` first, per the bean and the ruling. But the ordering
inside the tranche should be by convention, not by filename: settle the 9
`chi_lambda_braid` sites as one decision, then the 6 `strict_averaged` ones as a
separate and much smaller one.

## ROOT CAUSE 2026-08-21 — the mass table's p-n interface comes from caches built before the weighting existed

Owner authorised picking the frame for `canonical_mass_table_extended.py` (the
producer of both `canonical-mass-table-extended` and, via a thin wrapper,
`low-isotope-mass-table`). Traced it rather than flipped it, and the answer is
not a convention flag anywhere in that producer — it has none. `grep
pn_convention canonical_mass_table_extended.py` returns **zero**.

### Measured

    branching combiner, deuteron   0.575090872290275361250124   <- COLOUR-BLIND
    closed form, strict_averaged   0.575090871629810316751633      (agrees, 6.6e-10)
    bridge / fixed symbolic path   0.575172243917771870826535   <- weighted
                                                                   gap 1.4e-4

The producer routes A ≥ 2 through `canonical_tr_m_via_branching`, whose
docstring says it applies `σ − h(½ − δ/4)·𝟙`. It does not, and the reason is
structural rather than a wrong line:

- `intra_block_word()` builds its word from `atom_canonical_crossings(1,0)` and
  `(0,1)` — **free nucleons**, which have no p-n bond. So the `d_for_ctype` call
  there (correct, and fixed for exactly this reason in an earlier pass) never
  sees `averaged_weighted`. The comment above it — *"the if/elif this replaces
  raised on averaged_weighted, i.e. on every Z≥1,N≥1 atom"* — is true of a
  different call path and reads, in place, as though it covered this one.
- The **interface** between blocks is not computed at all. It is loaded from
  precomputed A-operator extract witnesses, keyed `(n_strands, iface)`:

      (6,  "pn") -> sublemma-2-1-A-operator-extract.witness.json     computedAt 2026-05-05
      (9,  "pn") -> A-operator-extract-h9-pn.witness.json            computedAt 2026-05-18
      (12, "pn") -> A-operator-extract-h12-pn.witness.json
      (15, "pn") -> A-operator-extract-h15-pn.witness.json
      (18, "pn") -> A-operator-extract-h18-pn.witness.json

Both checked extracts predate the colour weighting by ~three months, and
**neither carries `convention_fingerprint`, `convention_label`, or
`pn_convention`** — so nothing downstream can tell which interface they encode,
and nothing invalidates them when the convention moves.

### This is `45789ddfa0`'s finding, one cache family over

That commit fixed exactly this shape for the **chi** caches — resume logic keyed
on partition coverage or q₀ alone, "no notion of which word produced the cached
entries, so a cache written before the colour-weighting landed looks complete
forever" — and introduced `convention_fingerprint` in `canonical_braid_crossings`
as the derived guard. The **A-operator** extracts have the same defect and were
not covered.

So the answer to "which frame is the mass table in" is: **it is in whatever
frame its A-operator caches were built in, which is pre-weighting, and no code
in the producer expresses a choice at all.** Flipping a `pn_convention` argument
would fix nothing, because there is none to flip.

### Fix path (NOT executed here — this is a compute job, not an edit)

1. Apply the `convention_fingerprint` guard to the A-operator extracts, so a
   pre-weighting cache is DISCARDED rather than resumed. Same mechanism, same
   module, already written.
2. Regenerate the five `(n, "pn")` extracts with the weighted interface. H₆ is
   cheap; H₁₅/H₁₈ are long-compute and need the `-u … | tee` discipline.
3. Re-run `canonical_mass_table_extended.py` and expect every Z≥1,N≥1 row to
   move by ~1.4e-4 relative — the same migration the low-isotope witness took.
4. Only then is `recomputed-low-isotope-mass-table.md`'s "three paths agree to
   machine epsilon" true of all three; two of them now agree at 3.4e-25 after
   the `qou-4e5k` fixes, and this producer is the third.

### Also found, unrelated to the frame

`canonical_mass_table_extended.py:310` passes `q_val=float(Q_FLOAT)` — a float64
q₀ into a 50-dps pipeline. Caps the branching path at ~1e-16 regardless of
`target_dps`. Precision defect, not a convention one; worth its own fix.


## Contained-scope finding from `qou-058n` (2026-08-23)

Fixing the one live colour-blind interface in `mass_tower_operator_valued`
(bean `qou-058n`), I swept the other consumers of the A-operator extracts to
see how wide the class is. **It is narrower than the grep suggests** — of the
A-operator consumers carrying a `-h/2`, `mass_tower_operator_valued` was the
only genuine instance. Each of the others was checked by running it, not by
reading the literal:

| file | verdict |
|---|---|
| `mass_tower_operator_valued` | **was the bug** — loaded a colour-weighted A, built χ at `-h/2`. Fixed; identity 3.32e-04 → 1.12e-15 |
| `sublemma_2_1_h9_tritium_verify` | **NOT a defect.** Already carries an `[H_6 frame guard] consumed extract vs canonical colour-weighted I_pn`, which passes at **5.51e-15**. 30/30 λ verify, max rel 1.22e-13 |
| `probes/A_operator_per_interface_probe` | **self-consistent**, not broken. It runs its own `np.linalg.lstsq` per interface at the same `d_int` it then tests. The residual claim is valid; what is off is only the *label* — its `"pn"` row is the colour-**blind** crossing `(1, -h/2)`, not the canonical `averaged_weighted` p-n boundary. A per-interface probe whose `pn` is not the canonical `pn` is worth renaming or re-pointing, but nothing it reports is wrong |
| `canonical_tr_m_via_branching` | **NOT a defect.** It derives `d` correctly via `d_for_ctype`, and the `float(...)` around it is consistent with a module that is float64 end to end (`_compiled_sigmas(…, "double")`, `complex(d)` two lines later). Flagging the cast would have been a false positive |

I had predicted `h9_tritium_verify` was a second live instance — it loads the
committed A witnesses *and* builds `I_pn` at `-h/2`, which is exactly the
failing shape. Running it refuted that: someone had already put the guard in.
Recording the prediction and its refutation because the grep signature alone
is not sufficient evidence for this class, in either direction.


## Preserved note (2026-08-25): chi_monotone_transfer oracle frame

The Part-F baseline entry for `chi_monotone_transfer.py::_self_test` was removed
as stale — the live `pn_convention=` assignment is gone, only a comment remains,
so the test reported it as no longer needed. Its warning is still live and is
recorded here so it is not lost with the entry:

> The self-test's oracles are `chi-{deuteron-h6,tritium-h9,helium-3-h9,
> helium-4-h12}-at-q0-50dps` — the colour-BLIND chi family from 45789ddfa0,
> which also lacks provenance. The same file already runs a colour-WEIGHTED
> check at n=6, so it is explicitly two-framed rather than blind. **When those
> oracles are regenerated weighted, the self-test must flip too**, or it starts
> comparing across frames and still passes.

## binding_canonical.py: DONE (2026-08-25, PR #5767)

Moved to `bring_color_weighted`. The baseline entry's own condition — *"moving
it to canonical means moving both halves together, or they diverge by 1.4e-4"* —
was satisfied: the local `_factor_from` could not express the weighted interface
at all (no branch for `-h(1/2 - δ/4)`; it fell through to `sp.nsimplify`), so it
was given the structural branch from `atom_nf_symbolic_D` and `_D_HECKE_TOL`
tightened to 1e-9. Verified two ways: the deuteron closed form moves off the
colour-blind value `qou-4e5k` names as wrong onto that bean's bridge/peel value,
and this file's closed-form and transfer paths now agree to 15 figures where
they disagreed by 1.5e-4.


## Item-2 adjudication 2026-08-25 (PR #5783): 6 -> 5 baselined

`binding_combiner_markov_peel_fallback` MIGRATED to canonical. Its stated
blocker — *'a numeric δ cannot be represented as an exact polynomial in the
formal symbol q, so the exact-symbolic trace path can only carry the
colour-blind averaged crossing'* — is refuted twice:

1. δ(q) = (q−1)²(1−q⁻⁴)/3, so the weighted shift is the exact RATIONAL function
   (q²−1)(−6q⁴+(q−1)²(q⁴−1))/(12q⁵), evaluating at q₀ to −0.10445824776972629,
   matching the numeric route to 15 digits. The claim demands a POLYNOMIAL; the
   requirement is rational, and the path already carries h = q − 1/q.
2. `markov_peel` has carried it all along via `word_to_element` /
   `crossing_from_cd` (qou-8zjd).

Verified by prediction stated in advance: D |tr_atom| 0.57509087 -> 0.57517224,
the qou-4e5k peel value; and B(D), B(4He) now match `binding_canonical`'s
#5767 values exactly. Two paths that disagreed, agreeing, neither tuned.

**Remaining 5, adjudicated:**
- `binding_bring_enhancement_compare` — LEGITIMATE, verified: computes BOTH
  conventions and reports the delta.
- `closed_form_tau_M_verification_phase5q` — LEGITIMATE: its slow path is
  *bound* to chi_lambda_braid via `marshal_to_chi_lambda_braid`, so pinning the
  closed form there is what preserves the verification.
- `_habiro_coefficient_extract` ×2 and `atomic_tr_m_helium4_canonical` — THIS
  BEAN'S TRANCHE, still open. The ⁴He one is a ~17 % move in tr_M(⁴He) and is
  coupled to the Phase-5q slow path; not a rename.


## Progress 2026-08-25 (PR #5801)

All three genuinely-off-canon PRODUCTION files are now flipped:

    binding_canonical.py                 strict_averaged   -> canonical  (#5767)
    binding_combiner_markov_peel_fallback.py               -> canonical  (#5783)
    atomic_tr_m_helium4_canonical.py     chi_lambda_braid  -> canonical  (#5801)
    _habiro_coefficient_extract.py       chi_lambda_braid  -> canonical  (#5801, 25 witnesses)

`test_ctype_consumer_coverage.py` Part F now reports **2 baselined, 0
unadjudicated**, and both survivors are LEGITIMATE, not backlog:

  * `binding_bring_enhancement_compare.py::build_witness` — a labelled
    comparison against a non-canonical convention, which R3 permits.
  * `closed_form_tau_M_verification_phase5q.py::main` — deliberately left on
    chi_lambda_braid by the 2026-06-03 audit, because it is the empirical
    slow-path validator and must match the frame it validates.

### Still open on this bean

  * `chi_monotone_transfer.py` — COUPLED, do not flip alone. Its four oracle
    witnesses `chi-{deuteron-h6,tritium-h9,helium-3-h9,helium-4-h12}-at-q0-50dps`
    are colour-BLIND; the file compares on the matching word deliberately.
    Flipping it before those oracles are regenerated makes the self-test compare
    across frames AND STILL PASS. Regenerate the oracles first.
  * `iterative_knot_builder.py` — not examined this session.
  * The 28 committed witnesses recording a non-colour-weighted pn_convention:
    25 of them were the habiro table and are now canonical.

### Bean's own framing, confirmed by measurement

The bean says "do not order S4 by file count: the 9 chi_lambda_braid
assignments are the whole tranche's weight". Measured on the habiro table:
the flip moved every atom by a factor 1.2055 (-17.05 % old-normalised,
+20.55 % new-normalised), versus 0.0141 % for a strict_averaged site.
That is the 1210x the bean predicted, confirmed on real witnesses.


## 🛑 CORRECTION 2026-08-26 — my "the oracles are colour-blind" claim was WRONG

The progress note above says `chi_monotone_transfer.py` is COUPLED and must not
be flipped until its four oracle witnesses are regenerated, because they are
colour-blind. **That is false, and it was never measured — by me or by the
comment I took it from.**

I read it in `test_ctype_consumer_coverage.py`'s 2026-08-21 adjudication
comment, which asserted the oracles "used the strict_averaged pn convention",
and I relayed it as established fact into PR #5801's body, this bean, and three
check-in notes without testing it. The witnesses record no convention field and
no `scriptFile`, so the claim could not have been checked against them by
reading — only by recomputation.

Measured, recomputing each oracle under both conventions (max rel), and
independently reproduced by me after a sibling (`qou-9ag4`) reached it first:

    atom   strict_averaged   bring_color_weighted
    D          2.625e-04           5.743e-50
    T          5.482e-04           8.257e-50
    3He        5.281e-04           7.487e-50
    4He        1.883e-03           4.079e-49

The oracles were **always canonical**. They reproduce exactly at the 50-dps
working precision under colour-weighting and miss by 2.6e-4 .. 1.9e-3 under
strict_averaged, so all four DISCRIMINATE. The self-test was therefore not
"about to break" — it was ALREADY FAILING on main, quietly, because the
comparison word was stale. The residual grows with A because the p-n `d`
differs by 7.19e-05 and compounds per interface: a colour-weighting scale,
not a precision scale.

`chi_monotone_transfer.py` is flipped and green on main (sibling work,
`qou-9ag4`); its Part F baseline entry is drained. Nothing here was blocked.

### What I did about it

  * Deleted the orphaned adjudication comment from the ctype test. It had
    outlived its entry and sat immediately above the closing brace, so the
    next reader attaches it to a surviving entry — which is how it reached me.
    Replaced with the measurement above plus a note on why it must be measured.
  * Fixed `atom_word_braid_letter_census_probe.py`, which was making main RED
    on the ctype test (pre-existing, confirmed on a clean tree): a private
    ctype vocabulary plus a family-blind `k == "averaged"` census. It counted
    correctly only because its private classifier's FALLBACK swallowed
    averaged_weighted; importing the canonical `classify_crossing`, which
    returns averaged_weighted as a distinct ctype, would have silently
    undercounted every p-n interface. Fixed both halves together; totals
    unchanged (2H 5=2A+1/32 closures, 3He 7/128, 4He 9/512) and the witness
    now reports the colour-blind/colour-weighted split, which is 1 weighted
    letter per isotope — the single p-n interface.

### Lesson, recorded because it is the bean's own subject matter

A dated, specific, confident comment in the corpus is not a primary source.
AGENTS.md says exactly this for `## Status` notes and for sibling beans; it
applies to test-baseline adjudications too. Measure, then cite the script.


## File list DRAINED 2026-08-26

All 8 files the bean named are now canonical or legitimately excepted:

    binding_canonical.py                      canonical  (#5767, mine)
    binding_combiner_markov_peel_fallback.py  canonical  (#5783, mine)
    atomic_tr_m_helium4_canonical.py          canonical  (#5801, mine)
    _habiro_coefficient_extract.py            canonical  (#5801, mine, 25 witnesses)
    chi_monotone_transfer.py                  canonical  (sibling, qou-9ag4)
    iterative_knot_builder.py                 canonical  (sibling; was strict_averaged)
    binding_bring_enhancement_compare.py      LEGITIMATE — labelled comparison, R3 permits
    closed_form_tau_M_verification_phase5q.py LEGITIMATE — validates the legacy frame,
                                              must match the frame it validates

`test_ctype_consumer_coverage.py` Part F reports 2 baselined / 0 unadjudicated,
and both survivors are the two legitimate ones. That 2 is the FLOOR, not a queue.

Not closing the bean: the "28 committed witnesses recording a non-colour-weighted
pn_convention" line is only partly discharged (25 were the habiro table). The
remainder has not been enumerated.


## WITNESS LINE DISCHARGED 2026-08-26 (PR #5821) — and my earlier count was wrong

I reported this line "discharged to 4". **Wrong**, and the reason generalises:
I scanned only the field name `pn_convention`. The corpus states this
convention in a HETEROGENEOUS vocabulary. Keying on the field name
`convention` as well gives 70 witnesses / 93 declarations, of which **22** are
on the colour axis under names the first scan never looked for:
`averaged-crossings`, `colour-weighted-averaged-crossing`,
`sign-only-crossings`.

### The 22, classified by whether a p-n interface EXISTS

     4  single nucleon (chi-proton-h3, chi-neutron-h3)  no p-n interface
     7  free / vacuum words                             no interface
     2  dineutron, diproton                             nn/pp only
     1  markov-identity-symbolic                        records BOTH; deliberate
     4  older non-at-q0 generations                     superseded by siblings
     4  -at-qinv- siblings                              REAL DEFECT -> qou-1oxx

Most are legitimately colour-blind because there is nothing to weight.

### Fixed

  * `binding-combiner-markov-peel-fallback` — STALE WITNESS. PR #5783 flipped
    PN_CONVENTION and never re-ran, so the witness DECLARED "strict_averaged
    used" while the code computed canonical (scriptHash be64814b80ef vs file
    a1402f7398b8). Note now derived from PN_CONVENTION, so it cannot drift.
  * `canonical_ordering_dof_probe` — MY staleness from PR #5767, twice: it
    claimed binding_canonical passes strict_averaged, and used that as the
    `production_size` row, labelling a non-production convention as
    production. Fixed; effect -0.076% / +0.061% / +0.60%, structure and
    verdict unchanged, 22/22.

### Scanning note for whoever comes next

`chi_lambda_braid` is BOTH a pn_convention value AND the name of the character
function `pyhecke_native.chi_lambda_braid`. A value-level grep returns 18
witnesses, mostly prose naming the FUNCTION. Key on the field NAME.

### Handed off, not closed

The 4 `-at-qinv-` mismatches are bean `qou-1oxx` — structural, live (7
consumers, several bar-parity), bounded at 0.0141 % per p-n interface.

**This line is now discharged.** The bean's remaining scope is whatever else
it names, not the witness count.


## CLOSED 2026-08-26 — landed on main as 0bc2794da9 (PR #5821, rebase-merge)

Both lines are discharged: the 8-file list drained (2 legitimate exceptions,
which is the FLOOR not a queue) and the witness line closed. The residual —
the four `-at-qinv-` frame mismatches — is handed to `qou-1oxx`, which is
NOT a defect-with-a-known-fix: see that bean's two corrections.
