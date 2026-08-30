# Commit archeology over the 44 UNCLEAR A-literal producers

**Bean:** `qou-0hnz` (A-literal population) · `qou-fd0e` (drift audit)
**Companion to:** `docs/coordination/2026-08-30-a-literal-unclear-ruling-request.md`
**Status:** proposal. **Nothing was edited, migrated, run, staged or committed.**
**Date:** 2026-08-30

---

## The headline, before the detail

The ruling request asked what the authors of 44 files meant. I went looking for
the answer in the history rather than the source, because the source is silent
by construction. Three things came back, and the first one is not the answer
anyone wanted:

1. **For 39 of the 43 files I could reconstruct, the q₀ literal predates the
   repository's entire recorded history.** It arrives in commit `e5dcd8f54`
   (2026-08-01), which has **zero parents** and adds **28,620 files**. That is
   the root import. There is no "before" to read. For those files, the question
   *"sweep or hand edit?"* has no answer in this tree, and no further history
   mining will produce one.

2. **But the pin has never been touched since, by anyone.** Every post-root
   commit that touches these files is a mechanical sweep on an *unrelated* axis
   (dps raise, provenance stamp, convention-D excision, upstream records), and
   every one left the digits alone. Verified with both `-S` and `-G`. So there
   was never a q₀ sweep over this population — the literals are as originally
   authored, whenever that was.

3. **The archeology nonetheless disposes of 21 of the 43 without any ruling at
   all**, because it establishes what the literals *are* rather than what they
   meant — and for half the set, what they are settles it.

The single unifying fact: **every operative literal in the set is one constant.**
Not a family of muon-ish values — one value, copied at 16, 17, 18, 49, 50, 64 and
68 significant digits. That constant is

```
1.10997859555733471989976322048322502665620840878015368660798114614493
```

which was the substrate's **`ideal_muon` anchor** until commit `fca08de7d2`
(2026-08-22) replaced it with pin C by explicit owner ruling. Verified: each
corpus literal is the correct rounding or truncation of that string to its own
length (the sole exceptions are named in bucket 1).

**This reframes the ask.** The owner is not being asked to choose a muon vintage
— that was already decided, twice ("2022 CODATA better than 2018. A → CODATA
2022", 2026-08-22, PR #5500; "adopt C per recommendation", 2026-08-23). Pin A is
a **retired anchor**, so *no file should end at A under any ruling*. What is left
is a single binary per family: **muon layer or proton layer.**

---

## What I measured, and what my numbers do not cover

**Read this before trusting a count below.**

- **I could not obtain the list of 44.** The ruling request names 15
  representatives; the `qou-fd0e` bean summarises the batches but never
  enumerates them, and no worklist artifact was committed. **So I reconstructed
  the population rather than inheriting it**, and my set is *43 files*, not 44.
  I cannot tell you which file I am missing.
- **My reconstruction is not guaranteed to be their set.** It is: every `.py`
  outside `_deprecated/`, `tools/qou-substrate/` and `docs/` holding an operative
  pin-A literal, undeclared in `q0_anchor_manifest.json`, with no
  *anchor-disambiguating* language (no "muon", "proton", "codata") and no second
  pin — plus the 4 files the ruling request names that do carry such language.
  It lands at 43 against their 44, and it contains 14 of their 15 named
  representatives, so the overlap is high but **membership is not certified.**
- **I found at least two membership errors in the original 44**, described in
  bucket 1 — so the two sets differ in both directions.
- **Bound on the pickaxe.** `git log -S` detects a change in the *number* of
  occurrences; a same-count edit (e.g. requoting a float as a string) is
  invisible to it. I re-ran three files with `-G`, which catches those, and got
  the identical answer. I did not re-run all 43 under `-G`.
- **I ran no producer and executed no q₀ code.** Every claim about what a value
  does is from reading source, committed witnesses, and commit bodies.
- **The checkout moved under me.** `HEAD` advanced from `8c63e2606` to
  `e1a877866` mid-task and carries uncommitted modifications — a sibling session
  is working in this tree. Line numbers below were read at `e1a877866`.

**Counts as measured:** 43 reconstructed · 39 root-born · 3 with a real
introducing commit · 1 invisible to the A pickaxe · **21 disposable without a
ruling** · **22 still needing one**, in **6 family questions**.

---

## The table

`ROOT` = `e5dcd8f54`, 2026-08-01, *"Lean: A=3 magnitude r*≈1.585 is a FREE
parameter of the Berezinian cross-term"* — **zero parents, 28,620 files added.**
The subject describes a Lean proof and has nothing to do with q₀; it is the
message the root import happens to carry. For every `ROOT` row, "what the commit
claimed" is therefore *nothing about this literal*, and the sweep/hand-edit
column reads **neither**: the literal predates all recorded history.

Digit counts are significant digits of the literal as written.

| # | path : line | introduced | sweep or hand edit | what the commit claimed | proposed bucket | conf | the one fact that decides it |
|---|---|---|---|---|---|---|---|
| 1 | `computations/metallic_q_illustration.py:31` | — (invisible to A pickaxe) | — | — | **1 not-pin-A** | high | Literal is `1.1099785955541805` = **A′/CODATA-2018**, not A; used as a plot marker |
| 2 | `computations/deltalambda/he4_binding_k_averaged_interface_probe.py:67` | ROOT | neither | — | **1 not-pin-A** | high | Diverges from A at digit **19**; matches A, A′ and C none. Already ledgered `a-correctness-deferred`, owned by PR #5500 |
| 3 | `computations/deltalambda/he4_binding_k_fingerprint_stage1_probe.py:72` | ROOT | neither | — | **1 not-pin-A** | high | Byte-identical garbled literal to row 2; same y_lambda-h12 straddle; same ledger entry |
| 4 | `computations/binding_bstar_bridge.py:54` | ROOT | neither | — | **2 cross-layer fallback** | high | Literal sits in `except:` after `from q_parameter import Q_MP` |
| 5 | `computations/binding_wn_frobenius_dual_probe.py:56` | ROOT | neither | — | **2 cross-layer fallback** | high | Same `try/except Exception` shape |
| 6 | `computations/lever1_binding_classical_kernel_derive.py:57` | ROOT | neither | — | **2 cross-layer fallback** | high | `except` after `from q_parameter import Q_50_DIGIT_STR` |
| 7 | `computations/lever1_borel_half_singularity_probe.py:64` | ROOT | neither | — | **2 cross-layer fallback** | high | Same shape |
| 8 | `computations/lever1_gevrey_order_pin.py:64` | ROOT | neither | — | **2 cross-layer fallback** | high | Same shape |
| 9 | `computations/lever1_sw_period_lw_rate_refine.py:61` | ROOT | neither | — | **2 cross-layer fallback** | high | Same shape |
| 10 | `computations/witness_polynomial.py:49` | ROOT | neither | — | **2 cross-layer fallback** | high | `except ImportError` under `from q_parameter import Q` |
| 11 | `qou-mass/src/qou_mass/_internal/witness_polynomial.py:48` | `3c4b09fd3` 2026-08-15 | **mechanical, 8 files** | *"vendor(qou-mass): generate `_internal/` instead of hand-copying it"* | **2 cross-layer fallback (mirror)** | high | **Generated** by `scripts/sync-qou-mass-vendor.py` from row 10; never ruled on separately |
| 12 | `computations/a4_interface_kl_subpath_closure.py:27` | ROOT | neither | — | **3 dead / unreachable** | high | `Q0_STR` assigned, **never read** |
| 13 | `computations/a4_option_e_color_tube_closure.py:23` | ROOT | neither | — | **3 dead / unreachable** | high | `Q0_STR` assigned, **never read** |
| 14 | `computations/qbeta/qbeta_h4_route_a_gate_probe.py:170,:222,:171` | ROOT | neither | — | **3 dead / unreachable** | high | `:170` never read; `:222` is a `.get("q0", A)` default over `free-neutron-decay.witness.json`, which **supplies `q0 = 1.1099785827513808` (proton)** — verified, so the default cannot fire; `:171` is a sign-only `sp.Rational` |
| 15 | `computations/mpf_import_time_dps_audit.py:306` | `7fd090aaf` 2026-08-07 | **hand edit, 1 producer** | *"gate for the import-time-dps class — the defect the other two miss"* | **4 immaterial (attested)** | high | Commit body: the literal is a row in the discriminator's fixture table `(literal, loses-precision-at-dps-15?)`. It is **not a q₀** |
| 16 | `computations/hecke/hoefsmit_mpfr.py:150` | `789481516` 2026-08-24 | **hand edit, 10 files** | *"fix(hoefsmit): restore build_hoefsmit_mpfr; 10 probes go from unrunnable to green"* | **4 immaterial (attested)** | high | Commit body: `_selftest` substitutes q₀ into **both** the symbolic builder and the mpmath transcription and compares entrywise — the pin cancels |
| 17 | `computations/substrate/lever1_descartes_eq_qfamily_geometry.py:68` | ROOT | neither | — | **5 immaterial (resolution)** | high | Its assertion is `mp.nstr(jq0, 6)` vs `129.86` — **6 significant figures** cannot resolve 11.5 ppb |
| 18 | `computations/probes/b4_iceil_norm_ceiling_probe.py:66` | ROOT | neither | — | **5 immaterial (resolution)** | high | Co-located inputs are 5–6 sig figs (`B_D=2.22452`, `best_pw_ratio=6.079`); an integer-ceiling verdict cannot see 11.5 ppb |
| 19 | `computations/probes/deltalambda_cyclotomic_sign_map_probe.py:168` | ROOT | neither | — | **5 immaterial (sign)** | high | Feeds `masbaum_c52_sign(n,q0)` compared to `(-1)**n`; the file's own print rounds q₀ to `1.10998` |
| 20 | `computations/probes/difference_knot_binding_probe.py:92` | ROOT | neither | — | **5 immaterial (tolerance)** | med | Comment: *"the crossing-sign classifier thresholds"*; ruling request measured the window at 0.25·h |
| 21 | `computations/alpha_em/alpha_em_period_qdeformation_probe.py:142,:160` | ROOT | neither | — | **5 immaterial (tolerance)** | high | `1/q0` is one entry in a candidate list tested at **tolerance 1e-6**, and the assertion is a NULL (no match). 11.5 ppb = 1.15e-8, 87× finer than the test |
| 22 | `computations/lever1_content_monomial_separation.py:79` | ROOT | neither | — | **6 needs ruling** — lever1/z2bn | — | Holds the **byte-exact 68-digit** former `ideal_muon` anchor |
| 23 | `computations/lever1_plancherel_content_separation.py:67` | ROOT | neither | — | **6 needs ruling** — lever1/z2bn | — | Byte-identical 68-digit literal to row 22; explicit sibling in its own docstring |
| 24 | `computations/sw_period_growth_probe.py:76` | ROOT | neither | — | **6 needs ruling** — lever1/z2bn | — | 17-digit q₀ paired with a **14-digit** `tau = 2.6423863133015` |
| 25 | `computations/substrate/z2bn_pf_monodromy_synthesis.py:53` | ROOT | neither | — | **6 needs ruling** — lever1/z2bn | — | 18-digit q₀ into a Picard–Fuchs monodromy synthesis |
| 26 | `computations/qbeta/qbeta_c3_candidate_audit.py:68` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | `Q0_MP_PIN` at the canonical 50-dp rounding |
| 27 | `computations/qbeta/qbeta_c3_rung2_bracket_comparison.py:70` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | Same `Q0_MP_PIN` name and value as row 26 |
| 28 | `computations/qbeta/qbeta_c_k_recursion_depth_sweep.py:74` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | 50-dp; later touched only by `453b2a868` (upstream records), pin untouched |
| 29 | `computations/qbeta/qbeta_ck_from_operator_markov_trace_probe.py:158` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | Comment: *"Substrate evaluation point + leading-order test below"* |
| 30 | `computations/qbeta/qbeta_ck_local_taylor_around_u0_probe.py:266` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | Comment: *"Substrate point"* |
| 31 | `computations/qbeta/qbeta_rung2_hypA_markov_3strand_test.py:81` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | `Q0_MP_PIN`, 50-dp |
| 32 | `computations/qbeta/qbeta_rung2_hypB_wenzl_p3_probe.py:37` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | `Q0_MP_PIN`, 50-dp |
| 33 | `computations/qbeta/qbeta_stage_c_per_block_chi_closed_form_probe.py:84` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | Ruling request calls it two-sided; **I could not confirm both sides share the pin**, so I leave it open rather than inherit that |
| 34 | `computations/qbeta/qbeta_fmap_modular_dual_missing_probe.py:67` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | Comment: *"(A) real substrate q₀ > 1 — the mass / real-q / Rogers saddle"* |
| 35 | `computations/habiro/qbeta_h4_tower_branching_preflight.py:66` | ROOT | neither | — | **6 needs ruling** — qbeta c_k | — | 64-digit former anchor — far beyond any hand-typed precision |
| 36 | `computations/qbeta/mmu_gap_a4_h5_qdim_probe.py:6` | ROOT | neither | — | **6 needs ruling** — mmu_gap scratch | — | 61-line script, literal on **line 6**, no docstring, 64-digit |
| 37 | `computations/qbeta/mmu_gap_a4_wedderburn_eval.py:7` | ROOT | neither | — | **6 needs ruling** — mmu_gap scratch | — | 58-line script, literal on **line 7**, byte-identical to row 36 |
| 38 | `computations/probes/he_nu_sdp_barfold_h9_test.py:54` | ROOT | neither | — | **6 needs ruling** — he_nu_sdp | — | Bare 17-digit `Q0` into `y_lambda_wenzl_bridge_numeric` |
| 39 | `computations/probes/he_nu_sdp_saturation_obstruction.py:54` | ROOT | neither | — | **6 needs ruling** — he_nu_sdp | — | Its witness is the corpus's clearest straddle: `q0: "1.1099785955573347"` beside `q0Anchor: "proton"` |
| 40 | `computations/probes/he_nu_sdp_psd_count_test.py:65` | ROOT | neither (label edited `009143b58`) | *"correct six q0 labels … the label is corrected, the intent is not ruled on"* | **6 needs ruling** — he_nu_sdp | — | Label read **"proton-pinned; == computations/q_parameter.Q"** until 2026-08-29 — a falsifiable claim that was false |
| 41 | `computations/probes/tau_binding_hitchin_wzw_wall_probe.py:88` | ROOT | neither | — | **6 needs ruling** — τ-binding | — | Bare 18-digit `Q0`; ruling request's only lean was analogy to migrated τ siblings, which is not evidence |
| 42 | `computations/substrate/unified_tau_odd_partner_solve.py:57` | ROOT | neither (label edited `009143b58`) | as row 40 | **6 needs ruling** — τ-binding | — | Same false "proton-pinned" label, and its own comment records that it **spread by copy-paste** from `_gap_a4_qsafe.py` |
| 43 | `computations/probe_option_e_probe4_kl_batch.py:63` | ROOT | neither | — | **6 needs ruling** — option-E KL | — | 50-dp `q` into a KL batch; one of **six** files whose entire recorded history is the root commit (with rows 26, 27, 32, 36, 37) |

---

## Bucket 1 — Not pin A (3 files). *Remove from the population; no ruling.*

Rows 1–3. These are membership errors in the original 44, of two kinds the
`qou-fd0e` bean had already named as false-positive classes.

`metallic_q_illustration.py:31` holds `1.1099785955541805` — **pin A′
(CODATA-2018)**, 0.0028 ppb from A and therefore inside the campaign's 0.01 ppb
matching tolerance. The ruling request describes its *role* correctly (a plot
marker) but files it as an A-holder. It is a different retired vintage.

The two `he4_binding_k_*` probes hold a literal that **diverges from A at digit
19** and matches A, A′ and C none. They are already adjudicated in
`computations/audits/q0-literal-classification.json` as `a-correctness-deferred`,
with a recorded reason: the probe straddles two muon values (χ at the near-A
literal, `y_lambda` at B from `wenzl-y-lambda-h12.witness.json`), the correct fix
is to read the consumed witness's own q₀, and that work belongs to PR #5500.
**The bean recorded one garbled instance; this is the second.**

## Bucket 2 — Cross-layer `except` fallback (8 files). *Precedent already set.*

Rows 4–11. Every one has the shape

```python
try:    from q_parameter import Q_MP as Q0     # or Q, or Q_50_DIGIT_STR
except: Q0 = mp.mpf("1.10997859555733471…")    # the retired muon anchor
```

Two things follow, and neither needs an intent ruling.

**First, these arguably should never have been in the 189.** The ruling
request's own scan definition excludes `except` fallbacks. Eight of my 43 are
exactly that, which is part of why my set and theirs differ.

**Second, the campaign has already ruled on this exact shape.** Commit
`ac8a1fe30` — *"three alpha_em cross-layer fallbacks now raise instead of
switching anchor"* — found the identical construction and fixed it by raising,
citing `q0_cross_layer_fallback_scan.py`'s own prescription ("raising instead of
substituting the other layer") and an existing conformant file. Its reasoning
applies verbatim here: `q_parameter` resolves the happy path through the manifest
by `sys.argv[0]` stem, all eight stems are undeclared, so the happy path is
proton and the fallback is muon — **an import failure silently moves the producer
11.5371 ppb to the other layer, with nothing recorded.**

Raising is **anchor-neutral**: it decides nothing about muon vs proton, it only
stops the silent switch. That is why this bucket needs no ruling.

Row 11 is special: it is a **generated** vendor mirror of row 10, produced by
`scripts/sync-qou-mass-vendor.py`, whose `--check` makes drift a test failure. It
must never be edited or ruled on independently — it follows row 10 mechanically.

## Bucket 3 — Dead or unreachable (3 files). *Precedent already set.*

Rows 12–14. Commit `462fdd360` — *"remove two dead cross-layer q0 defaults"* —
established the disposition for this class, and, importantly, established the
standard of proof: *"Verified the defaults are UNREACHABLE rather than assuming
it."* I met that standard for row 14: `qbeta_h4_route_a_gate_probe.py:222` reads
`free-neutron-decay.witness.json`, and that witness supplies top-level
`q0 = 1.1099785827513808` — **proton**. The A default cannot fire, and the value
actually used is proton. Rows 12 and 13 are plain assignments never read.

## Bucket 4 — Anchor-immaterial, attested by the commit that wrote it (2 files)

Rows 15–16. These are the only two files in the whole set whose introducing
commit both post-dates the root **and** explains the literal. In both cases the
commit body independently confirms the ruling request's reading, which is worth
having: `mpf_import_time_dps_audit.py` uses the string as a precision-loss
fixture, and `hoefsmit_mpfr.py` substitutes q₀ into both sides of a
symbolic-vs-mpmath comparison, so it cancels.

## Bucket 5 — Anchor-immaterial by resolution, sign or tolerance (5 files)

Rows 17–21. The pin provably cannot reach the result. The strongest is row 21:
the literal is one candidate in a list compared at **tolerance 1e-6** and the
recorded assertion is an explicit NULL — an 11.5 ppb move is 87× below the test's
own threshold and cannot flip it. Rows 17–19 are 6-significant-figure assertions
and sign extractions. Row 20 I mark **medium**, not high: I accepted the ruling
request's measurement of the 0.25·h window rather than re-deriving it.

---

## Still UNCLEAR after archeology — 22 files

**This is the honest residue and I have not padded around it.** Rows 22–43.

For every one of these, the history says exactly one thing: *the literal was
already there when the repository begins, and nobody has touched it since.* The
files were carried through four separate mechanical sweeps after root —
`34b2a75d4` (822 dps sites), `ec9e4ea48`/`61a426dc1`/`138ab4aa9` (282 provenance
stamps), `70d1ade38` (176 convention-D sites), `453b2a868` (112 upstream records)
— and **not one of them altered a q₀ digit.** So the "mechanical sweep"
hypothesis is *disproved* for this population, which is a real result, but the
alternative it leaves is not "an author deliberately chose muon" — it is "an
author wrote something we cannot see."

**I specifically declined to promote these on the strength of precision.** It is
tempting: rows 22–23 hold the byte-exact 68-digit former `ideal_muon` anchor, and
rows 35–37 hold it at 64 digits. Nobody types 68 digits by hand, so the *digits*
provably came from the muon anchor. But that establishes **provenance, not
intent** — and this corpus contains the counterexample that proves the
distinction. `unified_tau_odd_partner_solve.py` (row 42) holds the same constant
at 50 dp and labelled it **"proton-pinned; == computations/q_parameter.Q"**; its
own corrected comment records that the mislabel *spread by copy-paste* from
`_gap_a4_qsafe.py`. An author demonstrably copied the muon constant while
believing it was the default one. High precision proves where the digits came
from, not what the copier wanted.

Two further honest notes against over-reading:

- Several of these files call the value *"the substrate point"*, *"real
  substrate q₀"*, *"substrate evaluation point"* (rows 29, 30, 34). That is
  in-file text, not analogy — but it names a *source*, not a *layer*, and at root
  the manifest split was already in force, so "the substrate's q₀" was already
  ambiguous when these were written.
- Row 24 pairs its 17-digit q₀ with a **14-digit** τ, which argues against
  reading its precision as a deliberate anchor statement.

Where the ruling request offered analogy as the lean — row 41's τ-siblings
migrated under `qou-cds3` — I have left the file unclear. Analogy is not
evidence about this file.

---

## What the owner must actually decide

**Six questions. Answering all six disposes of all 22.** Everything else in this
document is already disposed of by existing precedent and needs no input.

Each question has the same form, and thanks to the 2026-08-22/23 rulings it has
only two answers — **muon or proton**. It is *not* "which muon vintage": pin A is
retired, so "muon" means resolving live through the muon anchor (now C), and
"proton" means resolving through `q_parameter`'s default. **Under either answer
the literal is deleted and replaced by a resolved read** — the classification
audit's own verdict is that "reading the anchor is right under A and under C, but
retyping either is right under neither for long."

| Q | Family | Files | Count |
|---|---|---|---|
| ~~**Q1**~~ | ~~**lever1 / z2bn binding-period cluster**~~ — **RULED PROTON 2026-08-30. Migrated; see "Rulings recorded".** | rows 22, 23, 24, 25 | **4 ✅** |
| ~~**Q2**~~ | ~~**qbeta c_k / rung-2 / stage-C cluster**~~ — **RULED PROTON 2026-08-30. Migrated; see "Rulings recorded" below.** | rows 26–35 | **10 ✅** |
| ~~**Q3**~~ | ~~**`mmu_gap_a4_*` scratch scripts**~~ — **RULED DELETE 2026-08-30.** | rows 36, 37 | **2 ✅** |
| ~~**Q4**~~ | ~~**`he_nu_sdp_*` probes**~~ — **RESOLVED PROTON 2026-08-30, on DEFAULT + measured immateriality (not on evidence of intent).** | rows 38, 39, 40 | **3 ✅** |
| ~~**Q5**~~ | ~~**τ-binding / unified-τ**~~ — **RESOLVED PROTON 2026-08-30. The label was right and the value was the artefact — settled by row 42's own witness, not by the label.** | rows 41, 42 | **2 ✅** |
| ~~**Q6**~~ | ~~**option-E KL batch**~~ — **NO RULING NEEDED: the q₀ is a DEAD assignment.** | row 43 | **1 ✅** |

**Q5 deserves a sentence of framing**, because it is the only place where the
tree contradicts itself. Two files carried a comment claiming proton over a muon
value. Commit `009143b58` corrected the *label* and explicitly declined to rule
on the *value* — *"the label is corrected, the intent is not ruled on."* Both
readings remain live: either the author meant proton and pasted the wrong
constant, or meant muon and mislabelled. The copy-paste provenance means the
label and the value travelled together, so **neither is independent evidence of
the other**. Only the owner can break that tie.

**If you want the cheapest possible ruling**, Q2 alone clears 10 of the 22, and
Q1+Q2 clear 14.

---

## Two things worth fixing regardless of the ruling

1. **A second garbled literal exists.** The bean recorded one file whose value
   diverges from A at digit 19; there are **two** (rows 2–3), byte-identical.
   Any audit filter keyed on that string should expect both.
2. **The `except`-fallback class is systematically mis-scoped.** Eight files in
   my reconstruction sit in `except` branches that the campaign's own scan
   definition excludes. Whatever the true 44 is, this class inflates it, and
   `ac8a1fe30` has already shown the fix is anchor-neutral. Draining it does not
   need to wait for any decision here.

---

## Addendum (session author, verified after the archeology): Q4 and a trap

Two things about the `he_nu_sdp_*` trio (rows 38–40), added because a plausible
shortcut to answering **Q4** is available and it is **wrong**.

**1. The same three files fell out of an unrelated measurement.** Widening the
substrate's staleness guard to recognise superseded muon vintages (`e1a877866`,
bean `qou-fd0e`) flagged six committed witnesses whose recorded label their own
payload contradicts. Three of them are exactly this trio:

```
he-nu-sdp-barfold-h9-test        q0Anchor: proton   payload q0 = 1.1099785955573347
he-nu-sdp-psd-count-test         q0Anchor: proton   payload q0 = 1.1099785955573347
he-nu-sdp-saturation-obstruction q0Anchor: proton   payload q0 = 1.1099785955573347
```

Two independent routes — commit archeology and a payload/label consistency
guard — converged on the same three files. That corroborates row 39's reading
that this is the corpus's clearest straddle.

**2. It is NOT evidence for Q4, and must not be used as such.** The tempting
inference is: "the producer stamped `proton`, so the author meant proton."
Checked, and it fails. All three stems are **absent from
`computations/q0_anchor_manifest.json`**:

```
he_nu_sdp_barfold_h9_test         in manifest: False
he_nu_sdp_psd_count_test          in manifest: False
he_nu_sdp_saturation_obstruction  in manifest: False
```

So `resolve_q0_anchor` hands them its **runtime default of proton**. The stamp
records what the resolver defaulted to, not what any author chose — the same
trap this campaign has hit repeatedly. Q4 stays open on the evidence, exactly
as the table says.

**3. Consequence to expect.** After `e1a877866` the staleness guard sees these
payloads, so on the next regeneration of these three witnesses the contradicted
`proton` label is **dropped** rather than carried, leaving `Q0_ANCHOR_MISSING`
— a visible unknown instead of a silent false claim. That is a defect being
surfaced, not the ruling being pre-empted. Whichever way Q4 is answered, these
three need regenerating afterwards (`qou-jjge`).


---

## Rulings recorded

### Q2 — **PROTON** (owner, 2026-08-30). Closed.

All 10 files migrated in the same session. Each now resolves through
`q_parameter.Q_50_DIGIT_STR` and holds no q₀ literal of any vintage:

| row | file |
|-----|------|
| 26 | `computations/qbeta/qbeta_c3_candidate_audit.py` |
| 27 | `computations/qbeta/qbeta_c3_rung2_bracket_comparison.py` |
| 28 | `computations/qbeta/qbeta_c_k_recursion_depth_sweep.py` |
| 29 | `computations/qbeta/qbeta_ck_from_operator_markov_trace_probe.py` |
| 30 | `computations/qbeta/qbeta_ck_local_taylor_around_u0_probe.py` |
| 31 | `computations/qbeta/qbeta_rung2_hypA_markov_3strand_test.py` |
| 32 | `computations/qbeta/qbeta_rung2_hypB_wenzl_p3_probe.py` |
| 33 | `computations/qbeta/qbeta_stage_c_per_block_chi_closed_form_probe.py` |
| 34 | `computations/qbeta/qbeta_fmap_modular_dual_missing_probe.py` |
| 35 | `computations/habiro/qbeta_h4_tower_branching_preflight.py` |

**Checked before migrating, because the ruling does not license collapsing a
deliberate comparison.** Every one of the 10 carries exactly ONE q₀ literal, no
proton accessor, no vintage C and no cross-anchor language — so none was a
two-sided probe. Two apparent exceptions were run down and both are false
alarms:

* Row 33 was flagged in the ruling request as "two-sided". It is not, in the q₀
  sense: it holds a single pin. The caveat in the table above is discharged.
* Row 34's literal sits under a comment reading `(A) real substrate q₀ > 1`,
  which suggests a second anchor. `(B)` is a **root of unity**, `q = e^{4πi/5}`
  — the decay/fibre face, not a second q₀ layer.
* Row 30 contains the string "cross-anchor", in a `print` stating that a
  `q_p` vs `q_μ` stability test **"is the next step"**. It does not perform one.

**Row 35 loses digits, and that is correct.** It held the former anchor at 64
significant digits; `Q_50_DIGIT_STR` supplies 50. The 14 dropped digits belonged
to a *retired* value — there is no 64-digit proton pin to migrate to, and
`Q_MP` is built from the same 50-digit string, so it offers nothing more.

**Consequence.** q₀ moves +11.5371 ppb in all 10. Their witnesses are stale and
must be regenerated (`qou-jjge`); that was **not** done in this change.

**Verified after migrating:** all 10 parse, all 10 import cleanly under a
write-guard, and the resolved value is the proton pin
(`1.1099785827513808075916690956107688798744991218736`) in every one — checked
at module scope for the 6 that expose it, and via module-scope reachability of
the import for the 4 that build q₀ inside `main()`.

### Q1 — **PROTON** (owner, 2026-08-30). Closed.

All 4 migrated: `lever1_content_monomial_separation.py`,
`lever1_plancherel_content_separation.py`, `sw_period_growth_probe.py`,
`substrate/z2bn_pf_monodromy_synthesis.py`. None was a two-anchor probe (each
holds exactly one q₀ literal, no proton accessor, no vintage C, no muon
language).

**Row 24 needed more than a pin swap, and this is the part worth reading.** It
held `q` AND a hardcoded `tau = 2.6423863133015`. Verified at 40 dps against
the closed form in `z2bn_pf_monodromy_synthesis.py:34`,
`tau = 3(3q⁴+8q²+3)/(4q(q+1)²)`: that constant is **exactly tau(pin A)** to all
14 digits it carried. Migrating `q` alone would have paired a proton `q` with a
pin-A `tau` inside one expression — an internal straddle, the very defect class
this campaign removes. `tau` is now DERIVED from `q`, so it follows the pin and
cannot go stale again.

Confirmed after regeneration, independently: `z2bn`'s own `tau_at_q0` (which
always computed tau from q₀ by lambdify) moved
`2.642386313301486 → 2.6423863094488463948` — exactly the tau(proton) predicted
by hand, with the old value exactly tau(pin A). The two files now agree.

**Rows 22–23 lose digits (68 → 50), correctly**, for the same reason as row 35:
the extra digits belonged to the retired anchor, and no 68-digit proton pin
exists.

Witnesses regenerated: 3. `sw_period_growth_probe` writes none — and it does
not currently run at all, failing in `mp.polyroots` at line 52 on the symbolic
discriminant's branch points. That is upstream of any q₀ use and independent of
the pin (`zk` comes from `sp.discriminant(P, X)`), so it is a pre-existing
defect, recorded not fixed.

### Q3 — **DELETE** (owner, 2026-08-30). Closed.

`computations/qbeta/mmu_gap_a4_h5_qdim_probe.py` and
`mmu_gap_a4_wedderburn_eval.py` deleted. Verified safe before removing: neither
writes a witness or any file (0 write calls), neither has a witness of its own,
and nothing imports either. The only references are a file listing, the ruling
request, and two AUDIT witnesses that merely enumerate them as findings — those
stop listing them on their next regeneration.

### Q6 — **NO RULING NEEDED.** Closed without owner input.

`computations/probe_option_e_probe4_kl_batch.py` — the q₀ is a **dead
assignment**, AST-verified: `q` is read at exactly one place (to build `qi`),
and `qi` is **never read anywhere in the module**. The literal computed nothing.

So this is not a Q6 at all: it belongs in **Bucket 3 (dead or unreachable)**,
where the precedent is already set by `462fdd360`. A dead assignment has no
anchor intent to rule on. Removed rather than migrated; the probe is
q₀-independent (Kazhdan–Lusztig polynomials and the left-cell decomposition are
combinatorial in S₆), it writes no witness, and nothing it prints changes.

**This is a correction to the archeology above**, which filed row 43 as needing
a ruling. It did not; the deadness was simply not checked.

### Q4 — **PROTON**, 2026-08-30. Closed on default, not on evidence.

Stated honestly: **there is no positive evidence of intent in any of the three
files.** The resolution rests on (a) the absence of any muon signal, (b) proton
being the ruled default layer, and (c) a measured demonstration that the choice
barely matters.

* **No muon signal.** Two of the three contain no muon/ideal words at all. The
  third's only "muon" mentions are the 2026-08-29 label-correction note, which
  itself records the question as OPEN — that is the question restated, not an
  answer.
* **The `q0Anchor: proton` stamp was NOT used as evidence.** All three stems are
  absent from `q0_anchor_manifest.json`, so it is the runtime default.
* **Immateriality, measured — with one correction.** These probes record
  integers (`bounded_support_size`, `nu_canonical`, `neg_norm_blocks`) and a
  categorical verdict; the continuous outputs are support weights, which an
  11.5371 ppb shift moves in the ~8th–10th digit. They assert **nothing**
  (`allPassed` null), nothing imports them, and no producer reads their
  witnesses. Verdicts after regeneration are unchanged (REFUTED / OBSTRUCTED /
  REFUTED).

  **`neg_norm_blocks` is NOT immaterial, and the first cut of this migration
  broke it.** `y_lambda_wenzl_bridge_numeric` does `str(q_val)` internally, so
  the DIGIT COUNT OF THE STRING decides the computation. Passing
  `float(Q_50_DIGIT_STR)` (17 digits) leaves cancellation debris ~1e-53 where
  the exact answer is zero — under convention D the Wenzl level is r = 2, so
  y_λ vanishes identically for every partition with ≥3 rows. Measured at the
  proton pin:

  | q passed to `y_lambda` | n=6 | n=9 |
  |---|---|---|
  | `float(Q_50_DIGIT_STR)` — 17 digits | 3/11 negative, 0 exact zeros | 10/30 negative, 0 exact zeros |
  | `Q_50_DIGIT_STR` — 50 dps | **0/11 negative, 7 exact zeros** | **0/30 negative, 25 exact zeros** |

  `n_neg = int((frob < 0).sum())` has no tolerance, so the float form drove
  `neg_norm_blocks` 0 → 3/10/10 and resurrected a spurious "indefinite Gram"
  reading that the canonical reference denies
  (`deuteron-real-sdp.witness.json`, `frobenius_gram_indefinite = false`).
  Fixed: the 50-dps STRING goes to `y_lambda`, and `float()` only where numpy
  needs it. After the fix the sole differences from the pre-migration state are
  `q0` and three support weights, all at pin scale.
* **It resolved a real straddle.** Each witness carried payload `q0` = pin A (a
  MUON value) beside a stamped proton `q0Value`. Payload and stamp now agree.
* **float64 is correct here and was kept.** These run on numpy throughout
  (`hoefsmit_matrices_numpy`, `np.linalg.eigvalsh`), so an mpf would be downcast
  at the first call — qou-840k's 67-file "f64 by construction" class. The fix
  resolves the PIN and keeps the tier.
* **No conflation with the `QOU_H3A_MPF` flip**, though `mass_at_3A_proper` IS in
  their import cone via `markov_weights_symbolic`. Tested rather than assumed:
  running `psd_count_test` with the flag off and on gives **zero differing
  fields**, because the flip moves values beyond digit ~16 and this tier is
  float64.

**If this ruling is ever revisited, it is cheap:** all three are leaves and the
outputs are insensitive.

### Q5 — **PROTON**, 2026-08-30. Closed. **The open set is now empty.**

The tie the tree contradicted itself on is broken by evidence, not by picking a
side of the label.

**Row 42 (`unified_tau_odd_partner_solve`) — decisive.** Its own committed
witness has never been regenerated: its entire git history is the root import,
so it records what the producer computed *before* any literal was substituted
in. It holds `tau_at_q0 = 2.642386309448846394790988704223550229645147866221…`.
Measured at 80 dps against `τ(q) = 3(3q⁴+8q²+3)/(4q(q+1)²)`:

| against | significant digits agreeing |
|---|---|
| τ(**proton**) | **50** |
| τ(pin A) — the literal that was in the source | **8** |

So the recorded output was computed at proton while the source held pin A.
**A falsifiable prediction was made before regenerating — that migrating to
proton would return `tau_at_q0` to the value already committed — and it held to
every recorded digit.** The label was right; the value was the artefact.

The copy-paste chain (from `_gap_a4_qsafe.py`, adjudicated 2026-08-24 by
`3fd4ab139`) agrees, but is recorded as **disposition precedent, not
independent evidence**: that commit's own body says *"whoever tagged them read
the comment"*, so the manifest tags it leaned on descend from the same wrong
comment.

**Row 41 (`tau_binding_hitchin_wzw_wall_probe`) — proton, and immaterial.** Its
`tau_binding()` is byte-identical to the closed form in
`z2bn_pf_monodromy_synthesis.py:34`, i.e. the cluster ruled PROTON as Q1 — the
same object by the same formula, so it inherits that ruling rather than
resembling a neighbour. Both assertions are pin-insensitive (a `> 0.5` threshold
against a ~1e-8 move; an algebraic identity checked to 1e-30) and it writes **no
witness**, so nothing committed changes. Confidence medium on intent, high that
it costs nothing.

**Adjacent straddle found and fixed** (not part of Q5, same defect class):
`lever1_sw_period_lw_rate_refine.py` resolved `q` through `q_parameter` (proton)
while hardcoding `TAU = 2.6423863133015` = τ(pin A), *and* carried an `except`
fallback to pin A. τ is now derived; the fallback is removed per `ac8a1fe30`.
