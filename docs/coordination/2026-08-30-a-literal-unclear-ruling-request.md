# Ruling request: 44 producers hold a superseded q₀ pin with no recoverable intent

**Bean:** `qou-0hnz` (A-literal population) · `qou-fd0e` (drift audit)
**Status:** blocked on an owner/author decision. Nothing below has been changed.
**Date:** 2026-08-30

## What was done

Every `*.py` outside `_deprecated/` was AST-scanned for an **operative** q₀ literal
matching pin **A** = `1.10997859555733471989976322048322502665620840878` — assigned
or passed, not in a comment, not an `except` fallback, not a `startswith` sentinel.
The substrate package, its tests and `docs/` were excluded (they must keep an A
literal — one *defines* the pin, the others assert it).

**189 producers.** 169 of them are UNDECLARED in `q0_anchor_manifest.json`, so the
manifest offers no answer. Those 169 were triaged file-by-file against source
comments, dataflow, and upstream witnesses:

| verdict | count | |
|---|---|---|
| CROSS-ANCHOR | 76 | A is the *muon arm* of a deliberate comparison — **must not be migrated** |
| **UNCLEAR** | **44** | **this document** |
| MUON-INTENT | 39 | migratable to the pinning witness |
| PROTON-INTENT | 10 | migratable to `q_parameter`; 5 done, 5 in review |

## Why these 44 cannot be decided mechanically

Pin A is **11.5371 ppb** from the proton pin and **0.0769 ppb** from the current
muon pin C. Choosing wrong is a physics change, not a refactor. And the two
signals one would naturally reach for are both unavailable here:

1. **The manifest is silent** — all 44 are undeclared.
2. **The `q0Anchor` stamp is not evidence.** `resolve_q0_anchor`
   (`tools/qou-substrate/python/qou_substrate/witness.py:393`) returns `"proton"`
   for *any* stem absent from the manifest — its own comment calls this "the
   runtime default". The payload fallback cannot rescue it either: `_Q0_PREFIXES`
   at `:278` recognises the muon layer only as pin **C**, so a payload holding pin
   **A** matches neither prefix and falls through to that default.
   **Every one of these 44 therefore carries a `proton` stamp by construction**,
   regardless of what it computes. `he-nu-sdp-saturation-obstruction.witness.json`
   shows the straddle plainly: `q0: "1.1099785955573347"` beside
   `q0Anchor: "proton"`.
3. **Witness evidence is mostly absent** — in one batch of 42, **40 producers'
   witnesses carry no `q0Anchor`/`q0Value` at all**.

## The 44 split three ways, and only two need you

### (a) No anchor language anywhere — ~20 files. **Needs a ruling.**

A bare literal feeding real arithmetic, no comment, no second pin, no declaring
witness. Representative:

- `computations/lever1_plancherel_content_separation.py:67` — 68-digit A → `mp.mpf`,
  used at `:172`. Zero anchor words in the file. Its sibling
  `lever1_content_monomial_separation.py:79` carries the **byte-identical** literal,
  equally unlabelled.
- `computations/qbeta/mmu_gap_a4_wedderburn_eval.py:7` — 57-line scratch script, no
  docstring, no witness, no anchor word.
- `computations/probes/he_nu_sdp_barfold_h9_test.py:54` — bare A into
  `y_lambda_wenzl_bridge_numeric`. Two sibling probes carry the identical
  unlabelled literal.
- `computations/probes/tau_binding_hitchin_wzw_wall_probe.py:88` — bare A; the only
  lean is that its τ-family siblings were migrated to proton under `qou-cds3`.

**What we need:** for each family (`lever1_*`, `he_nu_sdp_*`, the `mmu_gap_a4_*`
scratch scripts, the τ-binding probes) — was the pin meant as the *ideal/muon*
layer or the *experimental/proton* layer? One answer per family would settle most
of this group.

### (b) The repo already declares the intent open — 2 files. **Needs a ruling.**

Both were touched earlier in this campaign; both had a *false label* corrected to
match their value, and both say in-source that the remaining question is yours:

- `computations/probes/he_nu_sdp_psd_count_test.py:56-59` — *"this is the MUON pin,
  not the proton one — it read 'proton-pinned…' until 2026-08-29 … Label corrected,
  value untouched; **whether muon is INTENDED is open (bean qou-fd0e)**."*
- `computations/substrate/unified_tau_odd_partner_solve.py:53-57` — same shape, same
  bean reference, plus: the identical literal and near-identical wording appeared in
  `_gap_a4_qsafe.py`, so **this mislabel spread by copy-paste**.

**What we need:** confirm the value, or rule that the label was right and the value
should move.

### (c) Anchor-immaterial — ~22 files. **No ruling needed; documenting is enough.**

The pin provably cannot affect the result, and migrating them is churn:

- **Dead code** — `a4_option_e_color_tube_closure.py:23` and
  `a4_interface_kl_subpath_closure.py:27` assign `Q0_STR` and never read it.
  The honest fix is deletion, not migration.
- **Both sides share the pin** — `hecke/hoefsmit_mpfr.py:150` (self-test, same q₀ on
  both sides), `qbeta_stage_c_per_block_chi_closed_form_probe.py` (shared evaluation
  point for a two-sided validation).
- **Not a q₀ at all** — `mpf_import_time_dps_audit.py:306` uses the string as a
  precision-loss fixture; `metallic_q_illustration.py:77` uses it as a matplotlib
  tick label.
- **Resolution far coarser than the gap** — `lever1_descartes_eq_qfamily_geometry.py:98`
  asserts to 6 significant figures, which cannot resolve 11.5 ppb;
  `difference_knot_binding_probe.py` uses it for classifier thresholds with a 0.25·h
  window.

## Two defects found while triaging, worth knowing before you rule

1. **`gen_q0_anchor_manifest.py:26` matched muon by the pin-**A** prefix only.** A
   producer correctly migrated to the *current* muon pin C matched neither prefix,
   was omitted from the manifest, and was then defaulted to **proton** at runtime.
   Migrating a producer to the current muon pin silently re-declared it proton.
   **Fixed** (now matches A, A′ and C).
2. **`witness.py:278` recognises the muon layer only as pin C** — the mirror image.
   **Not fixed**: changing it restamps witnesses corpus-wide and is not a unilateral
   call. It is the reason item 2 above holds.

## What happens with no ruling

The 44 stay as they are. They are not broken — they compute what they have always
computed. But they are pinned to a vintage the corpus has moved off, they are
invisible to the manifest, and every one of them reports `q0Anchor: proton` while
holding a muon-family value. The next agent to run a pin audit will re-derive this
same list.
