# Regeneration queue — rewritten 2026-09-13 after the 702-commit merge

The previous contents are obsolete. Main's `qou-sv7h` arc made the kernel
EXACT — the accumulator had been multiplying 167-bit inputs at ambient dps 15
and the log layer was float64 on top — so **everything downstream of
`hecke_core_legacy` computed before this merge is superseded by construction**,
not merely stale. That is a much wider statement than the old queue's, and it
replaces it.

## 1. The nuclide table — RESTARTED FROM ZERO, 2026-09-13 (second supersession)

**Superseded twice now, by the same mechanism.** `qou-sv7h` made the kernel
exact and invalidated the 2026-09-07 19/19 run; the 218-commit merge of
2026-09-13 brought `qou-oiz3` ("carry mpf through mu_lambda, s_* and the whole
UIC resolvent cone", owner directive "excise float64") and invalidated the run
that replaced it, at 6/19.

`oiz3` rewrites, among eight float64 sites its own message says "reach a binding
number", exactly the three that matter here:

| function | what it feeds |
|---|---|
| `atom_markov_trace` | the table's `tr_M` column |
| `atom_frobenius_norm_sq` | the Frobenius verdicts — all of §2 |
| `unified_iterative_correction_jet` | `binding_energy`'s first term, so `B_MeV` |

**Stopped and merged at 6/19 rather than finishing first.** Finishing would have
spent ~8 hours producing 19 atoms under a kernel main had already replaced;
stopping cost 40 minutes. Same judgement as §1's previous text records for
2026-09-07 and the opposite outcome, for the reason stated there: that merge
changed a key file by a pure **rename**, so the cache was provably valid and
re-stamping was right; this one changes the **arithmetic**, so the cache is
wrong and discarding is right. The key did its job both times; what differs is
what the diff said.

**Checkpoint and memo both discarded.** The checkpoint is preserved in history
at `3f2e6574102` and was deleted, not re-stamped. The 7.5 MB / 1656-file kernel
memo was deleted too — though it did not strictly need to be: `_memo_build_id()`
hashes `hecke_core_legacy.py` alongside the compiled kernel, precisely so a
Python-side change like this one misses rather than serves, which is the defect
that cost the *previous* memo its 38 MB (§3). Every entry was already
unreachable; deleting only reclaimed the disk.

**Early signal, measured on the restart:** proton / neutron / protium reproduce
byte-identically (`0.6293284243136999689635…`, `0.4751335192365202839866…`,
`1.1463377114864981773456…`). `oiz3`, like `sv7h`, bites on the accumulation
rather than at A=1, so divergence should appear from deuterium onward. If an
A=1 value had moved, something other than the intended change would have.

**Walls under the pre-merge kernel, for comparison when these land:**
deuterium 278.8 s, tritium 928.4 s, he3 926.9 s.

### ⚠ `B_MeV` ROUGHLY DOUBLES IN THE NEW TABLE. That is CORRECT and OWNER-RULED.

Measured on the first six atoms of the restart, against the pre-merge
checkpoint (`3f2e6574102`):

| atom | `tr_M` | `B_MeV` pre | `B_MeV` post | ratio |
|---|---|---|---|---|
| proton / neutron / protium | **identical** | 0.0 | 0.0 | — |
| deuterium | **identical** | −7.27110259868 | **−15.81419578544** | 2.1749 |
| tritium | **identical** | −7.74212739951 | **−16.11146582226** | 2.0810 |
| he3 | **identical** | −7.45619979733 | **−16.03835259525** | 2.1510 |
| he4 | **identical** | −6.82859416455 | **−14.61968714601** | 2.1410 |

Extended to ⁴He 2026-09-13 against the pre-merge 7/19 checkpoint
(`8e73c88095f`, the merge's own first parent). ⁴He's `tr_M` agrees to all 48
published digits: `1.585008128481302646181274372854265156921902187277`. Its
`frobenius_stable` is still `True` with 0 violations, so the gate drop has not
disturbed the Frobenius column at A=4 — the first real datum for §2, though
si28/ca40/fe56 are where the FAILs live and they are still to come.

**`tr_M` is bit-identical at every atom**, so this is not `oiz3` moving the
trace. It is `156f03f53b0`, "drop the UIC Pass-2 sign gate — honesty, NOT
accuracy". `unified_iterative_correction` used to admit a Wedderburn block only
when `final_tr_sign <= 0`; the owner ruled on 2026-09-12 to drop that, after
the justification was refuted **sorry-free** in
`QOU.MassTheory.UICGateNotFromComplementarySlackness` on four independent
mismatches. It now returns the ungated sum, so more blocks are admitted and the
magnitude grows. The ratio is **not constant** (2.0810 / 2.1510 / 2.1749),
which is the signature of more blocks rather than a rescale.

**Do not read this as a regression, and do not try to recover the old numbers.**
The landing commit is explicit: *"THE NUMBERS GET WORSE, AND THE DROP IS STILL
RIGHT"* — both old and new have the wrong sign against AME2020's +2.2246 MeV for
²H, and the new one is further away. What it buys is that the producer reports
what its functional actually gives instead of a subset chosen by a rule nobody
can derive. Its closing instruction: *"Do not reinstate the gate and do not hunt
a replacement selection that restores the old numbers; that is selection against
the target."*

The old gated value is still emitted, renamed
`gated_total_MeV` → `gated_total_DISPROVED_SELECTION_MeV`, because a neutral
name on a disproved selection is what let it be read as the answer.


## 2. `qou-3uvs` — re-confirm, and the SIZE ARGUMENT NOW NEEDS RE-DERIVING

The si28 / ca40 / fe56 Frobenius verdicts (all FAIL) came from the old kernel
and must be read off the new witness, not assumed.

The margin argument still stands on its own terms — the violations are
**10 %–84 % of the scale** and ~1e9 × the tolerance, so nothing that moves
values at ~1e-15 can flip them. **What no longer stands is the premise**, and
the correction matters more than the conclusion:

That "~1e-15" was measured for `qou-sv7h`. The 2026-09-13 merge brought
`qou-oiz3`, which rewrites **`atom_frobenius_norm_sq` itself** — this section's
own subject — replacing a float64 accumulation with mpf. A float64
accumulation's error is not bounded at 1e-15: it grows with the number of terms
summed, and these are the atoms with the most terms. So the shift on
si28 / ca40 / fe56 is exactly the case where the old bound is least likely to
transfer.

The verdicts will very probably survive a 10 %–84 % margin regardless. But
**quote the new witness's own numbers**, and do not carry the 1e-15 figure
across — it was measured against a different change, on a different function.

## 3. The kernel memo — DELETED, re-port only with a wider key

38 MB discarded, not ported. `_memo_build_id()` hashed ONLY the compiled
native module, and sv7h is a **Python** change, so the old cache would have
been served unchanged against a numeric path that had moved — a stale-value
failure, which is worse than no cache.

Re-port it against a key that hashes the Python numeric path too. Main already
uses that idiom: `he4_magnus_omega2_sign_sparse_probe.py` stamps
`_ck_src = sha256(open(__file__,'rb').read())` into every cached row and drops
rows that do not match. Same fix as the `_ckpt_key` widening.

`scripts/hkt-resume.sh` still sets `QOU_KERNEL_MEMO`; it is inert and says so.

## 4. Everything else — RE-CHECK against the merged tree first

The old queue's entries were measured before 702 commits landed. Do not act on
them as written. In particular main independently fixed several things this
branch was carrying:

* the `mp.mpf(repr(<mpf>))` trap (`qou-gxsd`) in at least three more places,
  and better — dividing directly rather than round-tripping through a string;
* the witness truncation window, by building the payload BEFORE `open(...,"w")`
  rather than by writing to a sibling temp (`qou-m549`; this file had been
  committed to main at **0 bytes**);
* `scriptFile` in `stamp_staleness_metadata` (`qou-4383`).

Re-measure before re-doing.

## 5. `qou-qe81`'s two stale error-row witnesses — RE-RUN ONLY, no code owed

Re-measured 2026-09-13; neither needs a producer fix any more.

* `computations/sweeps/paper_six_term_isotope_sweep.py` — returns EMPTY rather
  than raising (fixed on this branch); its committed witness still carries 8
  `FileNotFoundError` rows.
* `computations/term6_residues_at_roots.py` — its 4 rows were
  `LaurentQ.from_sympy: non-Laurent factor`, on an expression that IS Laurent
  (`-q²/12 + q/6 + 5/12 + q⁻²/12 − q⁻³/6 + q⁻⁴/12`). **Main fixed the parser**
  under `qou-ls7l` with an expand-and-retry; verified here against the exact
  failing input.

Both still serialise `allPassed: true` over exception text because they
predate the error-row gate. Re-running is what makes that verdict visible.

## 6. `qou-85wn` leftovers — `probe_he4_canonical_tr_m_fingerprint.py` — RE-RUN ONLY

Producer prose fixed 2026-09-13; the witness still carries the old
`description` until it is re-run. **No code owed beyond the prose edit** — no
computed value, assertion or tolerance was touched.

`qou-85wn` (a sibling session's bean, still `todo`) regenerated the `.md`
table, the `.ts` title and docstring, `CITED_PCT`/`CITED_TR_M`, and the
producer's two `[cited …]` print literals against the 2026-09-06 chi
regeneration. It missed four prose sites **inside the producer**, which is why
the witness's own `description` still read `tr_M = 0.160974145442` against data
of `0.0112374176598` — a factor R_quark = 14.3248, with two blocks sign-flipped
and the trivial rep going 5.96 % → 85.398 %, i.e. from near-nothing to leading
the ranking.

Fixed: the module docstring's "Cited values" block and its "86.6 %" note,
`w.set_description(...)`, and the `source=` strings on the `tr_M_at_q0` and
`trivial_rep_pct` assertions. Superseded figures kept and dated, per 85wn's own
convention — the gap is the evidence, and overwriting it would have destroyed
the only record that the producer's prose and its pinned constants had parted.

Cheap: reads one upstream cache and sums 77 partitions of 12. Queued rather
than run only because the `qou-uiut` table holds the checkout and two producers
must never run concurrently here.

## 7. `h2o_bond_angle_magnitude_vsepr.py` — RE-RUN ONLY, prose fixed 2026-09-13

Producer said `θ ≈ 107.2°` / `narrows ≈ 2.3°` in both its docstring and its
`set_description`, while computing `theta_pred_coulomb_n1_deg = 106.70642` and
`narrowing_pred_n1_deg = 2.764776`. The witness's **own `finding` field** already
carried the right numbers (`≈106.71°`, `≈2.8°`), so the document contradicted
itself in two prose fields at once — the exact shape `qou-n62l` was opened on.
No computed value touched. Fast probe; queued only because the table holds the
checkout.

## 8. Two `--pairs` drifts — RE-RUN ONLY, prose fixed 2026-09-13

Both found by the new advisory `--pairs` detector (`qou-n62l`), which compares a
prose number only against the field its own sentence names.

* `computations/binding_via_interface_knot.py` — `q_0 ≈ 1.1097` in three places
  (docstring ×2, `set_description`) against q₀ = 1.1099785827513808. Wrong in
  its own 4th decimal: 1.10998 rounds to 1.1100, never 1.1097. Now 1.10998.
* `computations/probes/binding_lp_with_inter_nucleon_bonds_probe.py` —
  `L_nn = 0.907262271178` against data of `0.907262265533`, a 5.6e-9 gap which
  is exactly the y-table precision this probe's own docstring names; and the
  mirror ratio read `1.17022` against `1.170237`. **The description is now
  INTERPOLATED** from the same variables the matching `add_data` calls
  serialise, so it cannot drift again. Eight of its ten hardcoded figures were
  still correct roundings — which is the trap: a description that is mostly
  right reads as maintained.

## 9. The three `--pairs` items left open on 2026-09-13 — RESOLVED, RE-RUN ONLY

* **`sdp_gamma_gamma_to_qqbar.py`** — prose `tr_M ≈ 0.73` against data `0.8485`.
  A **q₀-migration casualty**: `tr_M_at_q_0` read `0.7302040595096824` until
  `3563e08910a` ("migrate(q0) batch 4") moved it to `0.8485266504695027`, while
  `alt_eigenvalue_at_q_0` changed only in its 9th decimal and `c_1`, `c_sigma`
  and `sym_eigenvalue` did not move at all. The description is now
  **interpolated** from `bw['tr_M_at_q_0']`.
  **A previous correction in this same file got it backwards** and is also
  fixed: a `print` at line ~235 asserted "tr_M ≈ 0.73 … was never the trace —
  0.7312 is the magnitude of the alt eigenvalue". The git record refutes that.
  The two quantities sit 0.1 % apart by coincidence, and that coincidence turned
  a drift into a misdiagnosed conflation — while the `set_description` the note
  was correcting was left asserting 0.73 anyway.

* **`implied_c2_closed_form_search_50dps.py`** — docstring stated
  `c_implied = -0.91628187612727488…` against a live
  `-0.9162938090685661243645362`. They diverge at the **5th** decimal, 1.2e-5,
  which is **24× the 1 ppm (5e-7) criterion this search applies**. A prior
  author found this and recorded it in a caveat rather than fixing it
  ("reported, not silently corrected"); corrected now, and the caveat rewritten
  to carry the history rather than a present-tense falsehood. The two near-
  candidates moved with it (-G +3.2e-4 → +3.3e-4, -11/12 -3.8e-4 → -3.7e-4).
  **The code was never affected** — `compute_implied_c2(dps=50)` is called live.
  FOLLOW-UP: `set_description` runs *before* `c_implied` is computed, so it
  could not be interpolated without reordering builder calls. Do that when the
  checkout is free and the producer can actually be run.

* **`alpha_em_period_qdeformation_probe.py`** — NOT a prose defect, no fix owed.
  Prose `q15 = 0.62556` against data `q15 = 3.73205080756887729` (2 + √3). The
  witness's own failing assertion is named `dictionary_endpoint_q15_computed`
  and its verdict already reads "INCONCLUSIVE — an assertion failed; re-derive
  before citing". `--pairs` found the same failure from the other side.
  Separately worth fixing whenever that probe is revisited: all four of its
  assertions carry `computed=None, expected=None, tolerance=None, source=None`,
  so the FAIL records nothing about *what* failed.

## 10. `rho_pp_kind_weight_does_not_close_b3_probe.py` — RE-RUN ONLY, anchor label fixed 2026-09-13

`q0Anchor` read `physical_proton`, which is a **manifest category**, not a
witness-field token. `q0_anchor_manifest.json` has exactly three
(`ideal_muon` / `physical_proton` / `ambiguous`) and `WitnessBuilder.build()`
translates them out (`qou_substrate/witness.py:459`). This producer hand-rolls
its witness dict, never enters `build()`, and so skipped the translation. Now
`proton`. `q0_anchor_consistency_audit` was reporting it as a label that maps to
no pin — which is not a flip but an **unchecked** witness, and worse.

Also queued from the same reading, but **not fixed** (it is `qou-y98b`'s, a
sibling's claimed bean, and a cluster rather than a defect):
`qbeta_derived_w_overdetermined_test_probe.py` needs **no** source change — its
source already says `q0_anchor="proton"` with the prose split into
`q0_anchor_reason`; only its committed witness is stale at
`'proton (experimental pin)'`. Re-run clears it.

## 11. `weak_channel_is_a_flavour_flip_probe.py` — RE-RUN ONLY, CODATA literal de-hardcoded 2026-09-13

`M_N_OVER_M_P` was the literal `1.00137841917` — **CODATA 2010**. The registry
carries `1.00137841946` (2022); 2018's `1.00137841931` sits between them. Now
`codata("neutron-proton mass ratio").value`, verified to resolve under the
probe's own `sys.path` setup and to return an `mpf`.

Nothing the probe concludes can move: both uses are inside f-strings and the
assertion's predicate is `mn > mp_ and m3h > m3he`, which never reads the
constant. But it was printed as "experiment" in the probe's output, so a stale
edition was on a reader's screen.

**This took the `CODATA stale-edition` gate from RED to GREEN** — it was its
single finding corpus-wide, and it flags executable sites only.

## 12. `qbeta_habiro_taylor_investigation.py` — RE-RUN ONLY, float64 carried through 2026-09-13

Four `float()` narrowings on the numeric path, three of them flagged by
`mpf_mixed_arithmetic_audit` as one cause:

```
tr_p_num     = float(sp.N(..., 30))     30 digits computed, 16 kept, 18 printed
tr_n_num     = float(sp.N(..., 30))     same
delta_tr_num = tr_n_num - tr_p_num      a DIFFERENCE of two narrowed neighbours
_series_at_q0 = float(sum(<Rationals> * eps0**n))   exact sum, narrowed
```

`delta_tr_num` is the one that matters: it is the quantity the probe is *about*
(printed as Δtr_M(q₀), serialised, and compared against the ε-series), and a
difference of two nearly-equal values is where float64 cancellation is worst.
Measured on the same shape: a genuine 1e-20 gap between two values near 1.41
comes out **exactly 0.0** in float64 and survives in mpf.

`_series_at_q0` was fixed in the same pass **because fixing only the other side
would have been worse than fixing neither**: `_series_gap` compares the two
routes, so once `delta_tr_num` became exact, a narrowed series would have made
the gap measure float64 truncation rather than a disagreement. The 1e-9 gate is
the O(ε₀¹⁰) truncation (~2.6e-10), so the assertion passed either way — but a
two-route comparison has to be symmetric to mean what it says.

Verified before changing the types: mpmath's `mpf` implements `__format__`, so
the `{:.15f}` f-strings still print 15 places; `mpf(str(sp.N(x, 30)))` keeps all
30 digits where `float()` keeps 16.

Gate effect: `mpf_mixed_arithmetic_audit` 10 → 7 candidates, over-baseline 7 → 4.

## 13. `b3_brunnian_count_channel_probe.py` — RE-RUN ONLY, two reference literals de-hardcoded 2026-09-13

Both flagged by `codata_truncation_audit` (the `reference-literal ratchet`):

* `M_E_MEV = mpf("0.51099895000")` — **[DIVERGENT]**, i.e. a *wrong* value
  rather than merely a hardcoded one. That is CODATA **2018**; the registry
  carries `0.51099895069` (2022). Now `mpf(str(codata_constants.M_E_MEV))`.
* `Q0 = mpf("1.1099785827513808")` — **[TRUNCATED]**, 17 digits of a 50-digit
  anchor, discarding 33. The relative gap is **6.84e-18** — invisible at
  float64, which is exactly why it survived, and *not* invisible at the
  `mp.dps = 50` this file's own docstring declares ("NO FLOAT64: mpmath at 50
  dps throughout"). Now `q_parameter.Q_MP`.

Required adding the cluster's path-bridge idiom, which this file lacked —
`_sys.path.insert(parent.parent)` then `import _path_bridge`, matching
`a3_units_consistency_probe.py`. `codata_constants` lives in
`computations/substrate/`, so the bridge is what makes the bare-name import
resolve; without it the import fails at *runtime* while `compile()` still
passes.

**Numbers will move**, at ~1e-18 from `Q0` and ~1.4e-9 relative from `M_E_MEV`.
Both are corrections, not drift.

## 14. Two import-time dps defects — RE-RUN ONLY, fixed 2026-09-13

`mpf_import_time_dps_audit` had 6 NEW files; two were genuine and are fixed by
moving the idempotent `set_compute_dps()` to module scope **above** the
constant, which is the pattern the audit documents.

* **`molien_blast_radius_remainder_triage_probe.py`** — the severe one.
  `Q_NEAR_ONE = mp.mpf("1") + mp.mpf("1e-25")` was built at mpmath's import-time
  default of dps 15, where that expression is **exactly 1** (measured). The
  constant's whole purpose is to be near one and *not* one: it is fed to
  `y_lambda_su_n(n, Q_NEAR_ONE, 2)`, a q-deformed weight, so the probe was
  silently evaluating the **classical q = 1 limit** rather than the approach
  from just above. Now `1.0000000000000000000000001`, with `== 1` → `False`.
* **`beta_ew_n3_second_trace_probe.py`** — `COT_THETA_W_CODATA =
  mp.mpf("1.82306787")` built at dps 15 is the float64 expansion
  (`1.82306787000000003473587639746256172657012939453125`), not the decimal.

Both verified by **importing** the module, not compiling it: dps reaches 70 at
module scope and `Q_NEAR_ONE != 1`.

Gate: 6 NEW files → 4, total findings 30 → 28. **The remaining 4 are not
defects** — see the `qou-fl9i` note: three import `q_parameter` before the
flagged literal, which already raises dps 15 → 50 through the
`qou_substrate/constants.py` floor, and this audit does not model that.

## 15. `paper_six_term_isotope_sweep.py` — chirality factor serialised at true precision 2026-09-13

**Same witness as §5** (`qou-qe81`'s re-run item), second defect, independent of
the error rows.

All **16** `witness_float64_padding_audit` findings in
`paper-six-term-isotope-sweep.witness.json` are one field:
`term5_chirality_factor_a_K`, in three places (`rows[]`,
`all_modes.brane-legacy.rows[]`, `all_modes.drop.rows[]`).

It is genuinely float64 and deliberately so. `aK_v2` narrows q with
`qf = float(q_val)` because **its cache is keyed on a float64-rounded q** — its
own docstring says as much — `_aK_v2_cached` returns `float(total)`, and `aK_v2`
promotes that back with `mp.mpf(aK_f)`. The value carries 53 bits; `fmt()` was
rendering 60:

```
fmt()                 1.5032359764467355667250103579135611653327941894531250000000
str_at_true_precision 1.5032359764467356          <- the audit's own "really" value
```

Now `str_at_true_precision`. **Value-preserving** — only the rendering changes,
and `aK_v2` is untouched, because per `qou-qrsp` the remedy for a
genuinely-float64 quantity is to stop serialising 53 bits at 50 dps rather than
to fake precision it never had. The neighbouring terms stay on `fmt`: they are
mpf all the way down, which is what the long comment above that dict is about.

Clears 16 of the gate's 54 NEW once this witness is regenerated.

## 16. `binding_factor_f_decomposition.py` — RE-RUN ONLY, err_pct serialised in mpf 2026-09-13

`err = (f_ext / f_pred - 1) * 100` is mpf all the way — both operands are — and
`"err_pct": float(err)` narrowed it to 53 bits **at the witness boundary**. It
was the only field in its own dict doing so: `f_pred_bondcount` and
`f_extracted` beside it both use `mp.nstr(..., 20)`. Now matches them.

Accounts for **4 of the 5** raw float64 the ratchet counts in
`binding-factor-f-decomposition.witness.json`. The fifth is
`assertions[0].expected = 1.0`, an exact flag rather than a measurement.

Verified the consumer two lines below still works: it reads the value back with
`mpf(he4_err)`, and `mpf` parses a decimal string faithfully
(`mp.nstr(e,20)` → `15.701291645735583333`, round-trips; `float(e)` gave
`15.701291645735584`).

## 17. `hecke/hecke_division.py` — RE-RUN ONLY, was computing at q = 1.110 while stamping q₀

**The witness's stamp was right and its computation was not.**
`hecke-division.witness.json` declares `q0Anchor: proton` and the full 50-digit
`q0Value = 1.1099785827513808075916690956107688798744991218736`, while
`parameters.q = 1.11` — the producer ran the whole Gröbner–Shirshov division at
a `q_val = 1.110` float literal, **19.3 ppm** away from the anchor it claimed.

No anchor audit catches this shape. `q0_anchor_consistency_audit` checks that
the LABEL maps to a pin and that `q0Value` is correct; both were. Nothing checks
that the producer *used* it.

**Corpus scan, 2026-09-13** — 3427 witnesses, 1560 carrying a `q0Value` stamp,
compared against `parameters.{q,q0,q_0,q_val,…}`:

| finding | count |
|---|---|
| disagreement > 1e-12 | **4** |
| …of which serious | **1** (this file, 1.93e-5) |
| …display truncation to 11 digits (`1.10997858275`) | 3, all at 1.24e-12 |

So the class is real and **narrow**. The other three are
`low-isotope-binding-model-comparison`, `binding-sym-vs-lin-two-models` and
`binding-recurrence-spectral-bridge`, all the same 11-digit rounding.

Five `q_val=1.110` sites now read `Q_DEFAULT = float(_Q_MP)`.

**`float()` is deliberate and narrow here.** This module's arithmetic is float64
throughout — `1.0 / q_val`, `q_val ** 0.5`, `self.hecke_a = q_val - q_inv` — so
handing it an mpf would change every operation's type, and that cannot be
verified without re-running, which the `qou-uiut` table blocks. **This change
fixes the wrong-VALUE defect only.** Carrying mpf through `HeckeDivision` is a
separate, larger piece of work and the witness's 30 raw float64 fields stay
until it happens.

## 18. NEW GATE `q0_stamp_vs_parameter_audit.py` — wire it in AFTER §17 regenerates

Built 2026-09-13 for the class §17 uncovered: a witness that **stamps** the
anchor and **computes** at something else. Every existing q0 gate reads the
stamp — `q0_anchor_consistency_audit` (label maps to a pin, `q0Value` correct),
`q0_anchor_ratchet` (stamp present), `q0_value_drift_audit` (stamp not stale) —
and none reads what the producer used.

Current run: 1699 stamped witnesses, **648 comparable**, **1 disagreement** —
`hecke-division.witness.json` at 1.93e-5, which is the witness §17's producer
fix already addresses. So it will report **zero** once that regenerates.

**Do not add it to `scripts/precision-gates.sh` until then.** That file's own
header says a gate red on arrival gets skipped, and this one is red *only*
because its single finding is queued behind the table. Wiring it while red is
the exact failure it would be guarding against.

Blocks at ZERO with no baseline — after §17 there is no backlog to tolerate.
`--self-test` 8/8, including both directions of the tolerance band.

## 19. `casimir_macdonald_probe.py` — the substrate anchor was the FLOAT64 `Q`

**Not a serialization fix.** Every Macdonald norm in this probe was computed
from the anchor truncated to 53 bits.

`computations/substrate/q_parameter.py` exports both `Q` (a Python **float**)
and `Q_MP` (the same anchor as an `mpf`, 50 digits). Line 209 read

    q = mpf(Q)

which promotes 53 bits to the ambient 70 dps, and `q` then feeds all seven
`t`-specializations and every norm in the table. Now `q = Q_MP`.

REPRODUCED WITHOUT RUNNING THE PRODUCER, which is why this could be settled
while the table holds the checkout: under the producer's own import prologue,
`fmt(mpf(Q))` returns

    1.10997858275138083783417641825508326292037963867187500000000

and the committed witness's `parameters.substrate_q` is that string truncated
at OUTPUT_DPS. `is_f64_padded` says True on it and False on `fmt(Q_MP)`.
Relative gap `Q` vs `Q_MP`: **2.725e-17**.

Accounts for both padded fields the ratchet counts here — `parameters.substrate_q`
and `data.macdonald_norms_per_t_specialization.t=q⁻¹.(1,)`, which is `1/q` and
inherits the downcast rather than adding one.

**NUMBERS MOVE at the 17th digit.** This is a precision recovery, not a
re-render, so the regeneration is its own commit. Same shape as §17.

## 20. `binding_word_3A_reembedding_probe.py` — a wall-clock timing is exactly a float64

`t_fixed = time.monotonic() - t0` is a duration in seconds and carries 53 bits
and nothing more. Line 752 wrote `fmt(mp.mpf(t_fixed))`, which serializes at
OUTPUT_DPS and so emitted

    0.12464838699997926596552133560180664062500000000000

for a value that is `0.12464838699997927`. `fmt` routes a `float` to its
natural repr, so `fmt(float(t_fixed))` writes exactly what the timer measured.

**VALUE-PRESERVING** — `mpf(x) == mpf(float(mpf(x)))` holds for every value
that reached mpf from a float, so no digit that was ever there is lost. Both
of this witness's padded fields (`A2_path_sum_cost_s.fixed_Hk` and
`.three_A`) are this one call.

Worth noting separately and NOT fixed here: a wall-clock duration in
`data.*` is ephemeral content in a substantive field, so this witness moves
on every run for no informational reason, and the gate harness's DRIFT-ONLY
revert (which knows about `durationMs`) cannot recognise it. That is a
question about the field, not about its serialization.

## 21. `binding_production_route_C_vs_D_probe.py` — RE-RUN ONLY, and a provenance question I could not settle

No source fix owed on this tree, measured two independent ways:

1. `data.{tritium,helium-3}.E_0_MeV` is written by `str(E_0)` where
   `E_0 = experimental_constants.Q_NEUTRON_MEV`. Reproduced under the
   producer's own import prologue and **under both import orders** (constants
   before and after `set_compute_dps()`): the live source yields
   `0.782333409310000…0012`, which `is_f64_padded` rejects. The committed
   witness carries `0.78233340930999994977668166029616259038448333740234375`,
   the exact binary64 expansion — a string this source does not produce.
2. `B_AME2020_MeV` is `8.481821`, the hand-typed value that
   `be50b759681` replaced with the registry lookup `_B(1, 3)` → `8.4817962`.
   The current source cannot emit `8.481821` at all.

**The contradiction, recorded rather than guessed at.** The witness's
`computedAt` is 2026-09-13T16:22 and its commit (`4c6c247ea76`, a sibling's)
says it was deliberately re-run with `--atoms tritium,helium-3`. Yet
`experimental_constants.py` is byte-identical between that commit and HEAD,
so the import order cannot explain it. The AME evidence says the run happened
on a tree without `be50b759681` — plausibly the sweep's detached worktree at
some other base — but I did not confirm which, and a re-run settles it either
way. If a re-run still writes the padded string, this section is wrong and
the defect is live.

Earlier state for reference: at `4c6c247ea76^` the field was
`0.7823334093100222` — a bare 17-digit float, below the padding audit's
`MIN_SIG_FRAC` and so invisible to it. The 09-07 flip of the experimental
constants to `mpf` is what made the same downcast visible.

## 22. `b_over_a_evaluator.py` — three hand-typed AME literals, all wrong, and the padding was their shadow

Two defects, one cause. `AME_BA` held per-nucleon AME2020 binding energies as
**typed float literals**, and all three disagree with the registry
(`codata_constants.ame_binding_mev(Z, A) / A`), measured 2026-09-13:

| | typed | registry | relative |
|---|---|---|---|
| ⁴He  | 7.07391420 | 7.0739156 | **1.98e-7** |
| ¹²C  | 7.68014481 | 7.6801446 | 2.73e-8 |
| ⁴⁰Ca | 8.55130323 | 8.5513046 | **1.60e-7** |

**Why two sweeps missed them, and it is the same reason twice.**
`be50b759681` routed "the last 23 AME typo sites; 0 literals left tree-wide"
— it looked for TOTAL binding energies, and these are per-nucleon, a factor
of A away. `codata_truncation_audit`'s CANON carries `B_2H` … `B_7Li` as
totals for the same reason, so a B/A literal cannot be matched against any
canonical value and cannot be called a truncation of one. This file has
**zero entries in that gate's baseline** — invisible by construction rather
than tolerated. Not extended here, and now MEASURED (2026-09-14)
rather than merely deferred: **the extension cannot work the way the
total-binding rows do.** Built a B/A canon from the registry (684 values,
Z<=30, unbound nuclides dropped -- they come back NEGATIVE) and swept every
tracked `.py` for >=6-significant-digit literals inside its range:

    median relative gap between neighbouring B/A values   2.76e-4
    values in the 6.4-8.8 MeV band                        620
    union of their 1e-4 windows covers                    41.6% of that band

So a literal in that band matches *something* about two times in five by
coincidence. That is the prose-drift band detector's defect one dataset over:
no null model, so "close to some canonical value" is the COMMON case rather
than the surprising one. Total binding energies work because they span
2-500+ MeV sparsely; per-nucleon values all pile into 2.4 MeV.

The sweep's 30 hits bear that out -- `8.4817962` (tritium's TOTAL binding)
matching B/A(Si-32) at 3.86e-5, an LP-solver residual, a raw-float64 test
fixture. **Zero are B/A literals.** The single tight one (5.69e-8) is
`vs measured peak B/A = 8.794555 at A = 62` in a print statement: the Ni-62
peak, quoted correctly, agreeing with the registry.

What could work instead, not attempted here: the gate's own
`MIN_SHARED_DIGITS = 6`, which is scale-free and far tighter than a relative
window, or requiring a nuclide name or (Z, A) in the literal's context.
Either is a different check from the one CANON implements, so it is a gate
DESIGN question and not a row addition.

THE FIRST RUN OF THIS SWEEP WAS WRONG, and the shape is worth keeping:
`abs(x - v) / v` with a negative `v` (B-6 is unbound, -2.8 MeV) yields a
negative "distance" that passes every upper-bound filter, so the first pass
reported every literal in the tree -- pi, sqrt(2), Vol(4_1), the anchor.
`abs()` was on the numerator only.

**The padding was downstream of the typo.** `fit_c_s_to_4he` solves `c_S` so
that ⁴He's predicted B/A hits the target exactly, so a binary64 target made
the fitted `c_S` and every predicted B/A a dyadic rational — hence the
committed `B_over_A_predicted_MeV`
`7.0739141999999999299575392797123640775680541992188`, the double's expansion
of the typed literal, which is the ratchet's single finding here. An exact
decimal target leaves nothing to pad.

VERIFIED IN-PROCESS without running the producer (called the two pure
functions, wrote no witness):

    c_S                    -509.00258077810748  ->  -509.00267848523
    B_over_A_predicted_MeV  ...1999999999299575392797  ->  7.0739155999…97895
    is_f64_padded                          True  ->  False

The new value is still a long run of 9s and that is correct, not padding: it
is the fit reaching its target to ~2e-51, and `is_double_expansion` keeps it
because those digits are not the nearest double's. The same shape the
detector's own docstring names for `tr_M(1)`.

**NUMBERS MOVE — every row.** `c_S` is fitted, so all three nuclei shift at
the 7th digit. Regeneration is its own commit.

Divided by a plain `int`: mpmath is not imported in this module and an int
divisor is exact, so adding the import would buy nothing.

Not touched, and worth a separate look: this module also takes
`from q_parameter import Q as Q0` — the float64 anchor, the same downcast
§19 fixes in the Casimir probe. Its header marks the module
`archimedean_by_design` for a 6×6 float64 eigensolve and says "substrate
precision is the q-arithmetic input", which argues the anchor should be
`Q_MP`; but the eigen path genuinely is float64, so which values that
rationale covers needs deciding rather than assuming.

## 23. `qbeta_markov_trace_norm_probe.py` — 50 digits asked of a 53-bit input

All 6 padded fields are one call. `x_L2_at_q0 = [sp.Float(coords_witness[k], 50)
…]` takes coefficients out of `qbeta-decay-sdp-knot-operator.witness.json` and
asks sympy for 50 digits of a value that has 53 bits, and the witness then
wrote `str(v)` of that:

    0.074450296843839289251398838587192585691809654235840
    for a value that is 0.07445029684383929

**The upstream witness is innocent**, which is why this is NOT one of the two
upstream-fix cases this bean lists. It stores those coefficients as bare JSON
floats at their shortest round-tripping repr — honest for an SDP solution.
The padding is added on this side.

Promoting to 50 dps for the ARITHMETIC stays: `x_M` is genuinely computed at
that precision and the comparison needs a common one. Only the serialization
of the INPUT changes, to `repr(coords_witness[k])`.

Verified against the real upstream values: all 6 go `is_f64_padded` True ->
False, and each new string equals the audit's own `real_digits` of the
committed one. **Value-preserving** — no digit that was ever there is lost.

## 24. Four `rev_*` probes — `seconds` is a wall-clock duration the gate could not recognise

All 24 raw-float64 fields in the three NEW entries on that ratchet are named
`seconds`, and every one is a timing:

    rev-excess-scaling-exponent   11    scaling_R2[i].seconds    0.08 .. 1374.86
    rev-edge-relaxation-window     7    rows[i].seconds          0.34 ..   54.74
    rev-exact-maximiser-small-n    6    exact_rows[i].seconds    0    ..   63.43

**Not a precision defect.** `witness_raw_float64_audit` already carves out
wall-clock durations — 101 fields across 59 witnesses — but only under a key
it recognises. Renamed to `elapsed_sec`. Verified with the audit's OWN
counter (`_count` on the real documents, key renamed in memory):

    rev-edge-relaxation-window     raw  7 -> 0    ephemeral 0 -> 7
    rev-exact-maximiser-small-n    raw  6 -> 0    ephemeral 0 -> 6
    rev-excess-scaling-exponent    raw 11 -> 0    ephemeral 0 -> 11

**WHY THE FIX IS A RENAME AND NOT A WIDER CARVE-OUT.** The obvious move —
add `seconds` to `qou_substrate.witness._EPHEMERAL_META_FIELDS` — **does
nothing, silently.** The audit does not use that set; it uses a SUBSTRING
SELECT over it (`"dur" in n or "elapsed" in n`), so a name in the mask that
matches neither is never carved. Its own source says so in capitals and
records that an agent tried exactly that and had to retract the
prescription; widening needs both halves and is the open question on bean
`qou-ywee`. `elapsed_sec` satisfies both — it is in the mask and it contains
"elapsed" — so it needs no gate change at all.

And widening would have been wrong on its own terms. `seconds` is a generic
word: a half-life is legitimately in seconds, and reserving the name by fiat
would silence a real finding the day one appears. Measured first — only
these 3 witnesses carry a `seconds` leaf corpus-wide, all timings, so there
is no counterexample today and the hazard is entirely about tomorrow. The
neighbouring trap is in the same comment: a `/time/` substring would excuse
`y_times_chi`, the Frobenius pairing, 177 fields.

Also renamed in `rev_max_large_n_scan.py`, whose witness is NOT committed —
so the same NEW would arrive the moment anyone ran it.

NO CONSUMER READS THE FIELD. Every other `"seconds"` in the tree is
`isoformat(timespec="seconds")` or a write site; `producer_repad_sweep.py`
writes one into a plain JSON report, not a witness, and is left alone.

**VERIFICATION IS PARTIAL AND THAT IS STATED.** These four run at module
level — the dict literals holding the field ARE module-level statements — so
they cannot be imported without running them, and the table holds the
checkout. `ast.parse` clean on all four; the change introduces no name, only
a dict-key string and two comments; and the drain is verified against the
audit's own counter rather than predicted. What is not verified is a live
re-run.

Side benefit worth knowing: as `seconds` these fields were substantive, so
each witness showed a real diff on every re-run for no informational reason.
As `elapsed_sec` the drift machinery ignores them, the way it already does
`durationMs`.
