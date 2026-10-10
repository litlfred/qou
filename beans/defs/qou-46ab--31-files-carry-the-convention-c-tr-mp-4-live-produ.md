---
# qou-46ab
title: 31 files carry the convention-C tr_M(p); 4 live producers HARDCODE it as a reference
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:41:11Z
updated_at: 2026-10-10T06:49:40Z
parent: qou-cdx1
---

Generalised from qou-5ll9, where `atomic-tr-m-helium4.witness.json` was shown
to hold a convention-C |tr_M(proton)| — proven to 50 digits by
`computations/audits/he4_witness_convention_attribution_probe.py`:

    C-frame  1.0653062286131670594     recorded  1.0653062286131670594
    D-frame  1.1457597822878355047     |D-rec|/rec = 0.0755215

That value is a literal string, so the corpus can be scanned for it directly.

## MEASURED

    files containing 1.06530622861316   31   (incl. one __pycache__, ignore)
    files containing 0.92323329718615   20   (the C-frame neutron)

So this is NOT one stale witness. It is a class.

## THE SERIOUS SUBSET — 4 live producers HARDCODE it as a REFERENCE

Not stale outputs: hardcoded constants that other computations are CHECKED
AGAINST. None of the four declares itself convention-C.

    computations/skein_proton_canonical.py:184
        atlas_value = mp.mpf("1.0653062286131670")
    computations/markov/markov_weights_symbolic.py:302,344
        print(f"  markov_peel ref : 1.0653062286131670")
        "tr_M_proton_markov_peel_reference": "1.0653062286131670",
    computations/probes/rho_f_categorical_probe.py:114
        (1, 0): _mp.mpf("1.0653062286131670"),   # proton
    computations/canonical_tr_m_three_path_comparison.py:104
        "proton":  "1.0653062286131670",  # matches bridge to all digits

**That last comment is now provably FALSE.** The bridge computes
1.1457597823 under convention D; the constant is 7.55% away from it. A
comparison against these constants either fails, or "passes" against a C-frame
target while the framework is D — and `markov_weights_symbolic.py:344` EMITS
its C constant into a witness under the name `..._reference`, so the C value
propagates outward under a name that reads as authoritative.

## WHAT IS NOT YET ESTABLISHED

The 31 have NOT been triaged. Expected buckets:

  (a) stale witnesses needing regeneration under D,
  (b) DELIBERATE historical / C-vs-D comparison records — legitimate, and
      `q0_sweep_full_309_result.txt` and the `.derivation.json` files are
      likely here,
  (c) hardcoded constants in live code — the four above, and possibly more.

Only (c) is confirmed, and only for those four. Do NOT report "31 stale
files"; report "31 carry the value, 4 confirmed hardcoded as live references."

## 🛑 THE LITERAL SCAN MISSED CONTENT AND LEAN ENTIRELY (2026-09-05, from `qou-i229`)

Probe: `the_character_closure_block_and_a_lean_file_publish_convention_c_probe.py`
(5/5). Found by `scripts/witness-block-agreement.py`, not by any scan for this
value.

**The "31 files" count is a floor, and it undercounts by construction.** This
bean scanned for the literal `1.06530622861316`. Two live sites carry the same
C-frame quantity under different renderings and matched **zero times**:

    site                                             renders it as
    prop:q-hecke-seminormal-character-closure        1.06530622859
    QOU/Interactions/MarkovPeelH3.lean               1.065306228592389333
    (this bean scanned for)                          1.06530622861316

A literal scan cannot bridge three renderings of one number. This is the rounding
lesson `qou-i229` opened with, arriving from the other side: there it inflated a
count fourfold, here it silently zeroed one. **Anything relying on that 31 should
be re-derived with a rounding-aware match, and `content/` and `lean/` belong in
scope — the bean's own buckets (a)/(b)/(c) are all about `computations/`.**

### Both sites are the class this bean already fixed once

`prop:q-hecke-seminormal-character-closure` publishes the C-frame table for all
five nuclei. The canonical Hoefsmit + Wenzl bridge computes those same atoms by
the block's **own stated method** (`Σ_λ y_λ χ_λ`) and agrees with none:

    proton 1.0755x   neutron 1.0699x   deuteron 1.4813x
    tritium 2.2038x  ³He 1.9549x

The proton ratio is this bean's own `0.0755215` signature. The block's *"relative
error ~1e-15"* column is agreement between **two C-frame paths**, which says
nothing about which convention both are in — and it reads as a verification.

`MarkovPeelH3.lean` states the C value and claims it *"matches Hoefsmit + Wenzl
bridge witness `atomic-tr-m-mpfr-50dps.witness.json` to ~4·10⁻¹⁶"*. That witness
gives `1.1457597823152389404`; the gap is `7.02e-2`, **wrong by fourteen orders
of magnitude**, and word-for-word the claim this bean already disproved at
`canonical_tr_m_three_path_comparison.py:104`.

**Nothing recomputed.** Both sites labelled; migration is this bean's, and it
moves five published figures by 7–120 % — the Lean declaration must move in the
same pass or the two diverge further.

### ✅ BOTH SITES MIGRATED C → D (2026-09-05, owner-approved: "refresh and migrate")

Source: the canonical Hoefsmit + Wenzl bridge witness
`atomic-tr-m-mpfr-50dps.witness.json`, `q0Anchor: muon`, live pin.

    atom       was (C)          now (D)          ratio
    proton     1.06530622859    1.14575978232    1.0755
    neutron    0.92323329717    0.98774375682    1.0699
    deuteron   0.38828647155    0.57517232973    1.4813
    tritium    0.10405211868    0.22931014615    2.2038
    3He        0.20654085856    0.40376713691    1.9549

**The anchor is unchanged.** The C table's per-atom `D/C` ratios match this
bean's convention ratio at the **muon** pin to 8 digits and at the proton pin
only to 7, so the table was muon-anchored and this is a convention migration,
not a re-anchoring. The muon pin used is the live one — the same target as the
`q₀` refresh in the same pass, so the two land consistently.

**The two-column form is withdrawn rather than recomputed.** That table printed
*canonical* against *partition-sum* with a `~1e-15` "relative error" that read as
a verification. It was the agreement of **two C-frame paths**, which says nothing
about which convention both are in. The identity is convention-independent so the
paths agree under D too, but that has **not been re-measured** at these five
nuclei — the second path is `markov_peel`, whose proton and neutron entries this
bean deliberately removed as unreliable. Printing an unmeasured residual would
repeat the defect being fixed.

### `MarkovPeelH3.lean` — FIVE convention-C residues, not one

The false agreement claim was the one I found first. Reading the whole file for
the migration turned up four more, and one of them is load-bearing:

    the `z` field docstring     `z = 1/(q^{1/2} + q^{-1/2})`   <- C AS THE DEFINITION
    the symbolic ring relation  `z⁻¹ − q^{1/2} − q^{-1/2}`     <- C in the quotient
    `trH3` docstring            "cross-check ... to <= 4e-16"  <- the same false claim
    open-item note              "tr_M(proton)|q0 ~ 1.0653"     <- the C value
    the cross-check comment     +1.065306228592389333...       <- found earlier

The `z` docstring is the serious one: a **live definition in a formal artifact**
stating the excised convention as what `z` *is*. All five corrected; the
structural point that D needs no `√q` is now recorded at the ring relation, since
that is one of the reasons D is production.

Edits are **comment/docstring only** — 0 declaration lines touched, verified
against the diff. `lake` is not on PATH in this container so the file was not
re-typechecked; with no code line changed there is nothing to break, but that is
an argument, not a check.

### This bean's four hardcoded producer references are ALREADY DRAINED

Re-measured today: `skein_proton_canonical.py`, `rho_f_categorical_probe.py` and
`canonical_tr_m_three_path_comparison.py` carry the literal **zero** times, and
`markov_weights_symbolic.py`'s single remaining hit is the annotated historical
note from the 2026-08-30 fix. So the `computations/` side was already done; what
remained was `content/` and `lean/`, which the scan could not see.

### 🛑 BLOCKER FOUND EN ROUTE: `atomic_tr_m_mpfr_50dps.py` DOES NOT REPRODUCE ITS OWN WITNESS

Trying to close the loop properly — declare the bridge producer for the block it
produces, then regenerate — surfaced something worse than a missing declaration.

**Re-running the producer gives completely different numbers:**

    atom      committed witness        re-run today
    proton    1.14575978231523894      0.62932842249489294
    neutron   0.98774375682050346      0.47513351767415624

Not a pin shift, not a convention shift — the ratios are not even constant
(1.8206, 2.0789). The script is **unchanged since the witness was generated**
(`scriptCommitSha` `fca08de7d29a` is its last commit), so the difference is a
dependency, not the code.

### 🛑 DIAGNOSED, AND MY FIRST ANSWER WAS WRONG

I wrote above that "the difference is a dependency, not the code". **Backwards.
It is the code, and the change was authorised.**

`atom_braid_word_3A` lays each nucleon's confinement core down grouped or
alternating. The **owner ruling** of 2026-09-05 (`qou-hu1f`) made the alternating
`(σ₀σ₁⁻¹)³` — *borromean* — the default. This witness was computed **2026-08-29,
before the ruling**, and never regenerated. Measured at the muon pin with the
kernel forced down its pure-Python path:

    intra_order=grouped     tr_M(proton) = 1.1457598292260762   <- the witness
    intra_order=borromean   tr_M(proton) = 0.6293284926174815   <- the re-run

So the producer reproduces its witness exactly — under the *superseded*
ordering. It is a **stale witness**, not a broken producer, and that is a much
better diagnosis than the one I first published in the migration commit.

Ruled out en route: **not the kernel** (`--method hoefsmit-python` gives the
same), and **not my `pyhecke_native` rebuild** — the pure-Python fallback gives
`0.6293` too, so both paths agree and the native is irrelevant to the value.

### THE BACKLOG THIS EXPOSES IS NOT TRACKED ANYWHERE

`qou-hu1f` counts the consumers of `build_atom_nf_mp` (**7**). The ruling
actually landed on `atom_braid_word_3A`, which has

    339  live Python callers
      7  that name `intra_order` explicitly
    332  that SILENTLY take the new default
     57  committed witnesses referencing it

Every witness among those generated before 2026-09-05 and not regenerated since
is in this witness's position. **That is the real scope of the ruling, and it is
recorded in `qou-hu1f`.**

### CONSEQUENCE FOR THE MIGRATION IN THIS BEAN

The five nuclei were migrated C → D from this witness, so they are correct in
**convention** and wrong in **ordering** — `1.1458` where the ruling implies
`0.6293`, a factor of 1.82–2.08, far larger than the convention migration
itself. The block is **flagged rather than re-substituted**: those figures have
already moved once today on a witness that turns out to predate a ruling, and
moving them again before the ordering question is settled would compound the
error. The fix is the producer re-run under the ruling.

### A SEPARATE PROBLEM I INTRODUCED

My rebuilt `pyhecke_native` has an **incompatible API** —
`chi_lambda_all_partitions_mpfr` raises
`TypeError: argument 'q_str': 'mpf' object cannot be converted to 'PyString'`.
The kernel catches it and falls back to pure Python, so numbers are unaffected,
but every producer using this kernel is now silently taking the slow path. It
was built to satisfy an environment-record warning; the container had no
`pyhecke_native` before that.

**The committed values are the corroborated ones, not the re-run.**
`he4_witness_convention_attribution_probe.py`, run today, independently computes
D-frame proton `1.1457596924573008697` at the proton pin — matching
`atomic-tr-m-mpfr-50dps-proton.witness.json` to `1.4e-49`. Two independent
sources agree; the `0.6293` matches nothing.

**So the migration stands** (its target is independently confirmed) and the
declaration is **reverted**: declaring a producer means being able to regenerate
its witness, and regenerating this one would commit 46 lines of changed values
that no other source supports.

- [x] The two content/Lean sites are migrated.
- [ ] **Diagnose why `atomic_tr_m_mpfr_50dps.py` no longer reproduces.** A
      producer that silently returns different numbers than its committed
      witness is worse than a stale figure: every downstream comparison against
      that witness is checking against something the code can no longer make.
      This is a third provenance failure mode alongside "pointer on the verifier"
      and "witness transcribes rather than computes".
- [ ] Once it reproduces, declare `prop:q-hecke-seminormal-character-closure` on
      it — it IS that block's producer, computing those five atoms by the block's
      own stated method.
- [ ] Re-derive the "31 files" with a rounding-aware match rather than a literal,
      with `content/` and `lean/` in scope. The count as it stands is a floor
      that undercounts by construction.

## DO NOT SWEEP

AGENTS.md is explicit that a corpus-wide sweep must not be launched off a
count like this, and the reasons apply here in full: a C-named comparison is
not a defect, and several of these files may be recording history on purpose.
Triage file by file. The discriminator is cheap — whether the site DECLARES
itself convention-C — and the probe above gives the ground truth for any
value in question.

## Why this is worth more than the witness it came from

A stale witness is one wrong number. A hardcoded C constant used as a
`reference` is a wrong number that other computations are validated against,
so it can make a correct D-frame result look like a regression, and it can
make a C-frame result look confirmed.


## TRIAGE COMPLETE 2026-08-30 — and it is WORSE than the bean's headline

Two corrections to my own figures first.

**"31 files" was measured on one value and included untracked paths.** Tracked
files carrying EITHER C-frame value (proton `1.06530622861316` or neutron
`0.92323329718615`): **41**.

**"4 live producers hardcode it" was a floor, not the count. It is 15**, and in
every one of the 15 the occurrence is a hardcoded LITERAL, never a computed
value. None declares itself convention-C.

### The 15, by consequence

**(1) SEVEN habiro/ files take the C value as a DIRECT INPUT — the worst class.**

    habiro_correction_product_verify.py:69   tr_M   = mp.mpf("1.06530622861316705936…")
    habiro_exact_taylor_extraction.py:159    tr_M_val = …
    habiro_h9_correction_series.py:73        tr_M   = …
    habiro_h9_spectral_decomposition.py:124  tr_M   = …
    habiro_normalization_bridge.py:55        direct = …
    habiro_sub_ppm_third_factor.py:64        tr_M   = …
    habiro_coefficients_atomic.py:95-96      (docstring)

These are not references being compared against — the value is multiplied in:

    pred_0 = tr_M * plancherel_ratio * vol_over_hsq
    S      = hab_sum / pred_0

MEASURED consequence:

    habiro_normalization_bridge  ratio = hab/tr_M
       with C tr_M   127.7296637424353
       with D tr_M   118.7606760745057      rel 0.0755215
    h9_correction_series   S is 7.552 % HIGH under C   (S_C/S_D = 1.0755215)

And each of these files resolves `Q_50_DIGIT_STR` for `q` while hardcoding a
C-frame `tr_M` — a CONVENTION STRADDLE INSIDE ONE COMPUTED QUANTITY, the same
structural defect as the pin straddle in qou-y313, one layer up.

**(2) `derivation_chain.py` — 7 occurrences, incl. a full 50-digit string.**

    :79   comment;  :97-98 floats;  :112-113 50-digit strings;
    :146-147 with the comment "11-crossing typed B_3 (uud)"

**(3) Emitted outward under an authoritative name.**

    markov/markov_weights_symbolic.py:344  "tr_M_proton_markov_peel_reference"
                                     :347  "tr_M_neutron_markov_peel_reference"

**(4) Comparison constants whose comments are now provably false.**

    canonical_tr_m_three_path_comparison.py:104  "# matches bridge to all digits"
                                           :105  "# matches bridge"

The bridge computes 1.1457597823 under D. It does not match.

**(5) A THIRD value, float64-truncated.**

    probe_qbeta_form.py:32 and probes/probe_qbeta_form.py:21
        tr_M_p = mp.mpf('1.06530622861316626170946619823')

`…131666261…` vs the exact C `…131670594…` — they diverge at the 15th digit,
~7.5e-16, i.e. the C value round-tripped through float64. A separate (minor)
laundering defect sitting on top of the convention one.

Remaining: `graded_hecke_energy_probe.py:68-69`, `rho_f_categorical_probe.py:114-115`,
`skein_proton_canonical.py:184`.

### THE PRIOR REGENERATION SWEEP COULD NOT HAVE FIXED ANY OF THIS

`.work/convention-c-regen*.jsonl` records a producer-by-producer regeneration
pass (87 / 68 / 90 producers). `markov/markov_weights_symbolic.py` is in it and
is logged **`ok`, 5.2 s** — and it still emits the C constant today, because
re-running a producer cannot change a hardcoded literal. The other affected
producers (`atomic_tr_m_helium4`, `atomic_tr_m_mpfr_50dps`, `skein_proton_canonical`,
`rho_f_categorical_probe`, `canonical_tr_m_three_path_comparison`, all seven
habiro/) appear in **no** sweep log at all.

That is the structural point: a regeneration sweep is the wrong instrument for
this class and reports success against it. It is why these survived a migration
effort that reported completion.

### Legitimately NOT defects (do not touch)

    .work/convention-c-regen*.jsonl        run logs; the value is captured stdout
    computations/q0_sweep_full_309_result.txt   sweep output, historical
    docs/audits/2026-06-17-l1-1ppq-certification-gap.md   dated audit record
    computations/canonical-tr-m-three-path-comparison.witness.json  DECLARES C
    computations/audits/he4_witness_convention_attribution_probe.py  needs C by design
    .beans/*                                                        prose

    qou-mass/src/qou_mass/_internal/markov_weights_symbolic.py  GENERATED MIRROR --
    never hand-edit; fix computations/markov/markov_weights_symbolic.py and
    re-run scripts/sync-qou-mass-vendor.py --apply.

### Still open

The 11 witness files are untriaged individually. Each is presumably downstream
of one of the 15 code sites, so fixing the code and regenerating is the order —
not the reverse.


## 2026-08-30 — the code side is DRAINED; the witness side is done bar one

**Zero live convention-C tr_M literals remain in Python outside the one that
needs C by design.** Measured by AST rather than by grep, which is the
difference that matters here: a text search returns 19 files, and 4 of the 5
AST-visible constants are **docstrings** recording what was fixed.

    LIVE (non-comment) C tr_M constants in .py : 5
      he4_witness_convention_attribution_probe.py:2   docstring
      he4_witness_convention_attribution_probe.py:73  ← the only real one,
                                                        needs C BY DESIGN
      canonical_trm_reference.py:2                    docstring
      habiro/habiro_coefficients_atomic.py:84         docstring
      qou-mass/.../canonical_trm_reference.py:2       generated mirror of above

The 7 `habiro/` files, `markov_weights_symbolic.py` and both `probe_qbeta_form`
copies now carry the value only in **comments explaining the fix** — items (3),
(4) and (5) of the triage above are closed at the source.

### The three witnesses this bean deferred are regenerated

All three converted, verified by value:

    path-b-habiro-mass-probe        C 2 -> 0,  D 0 -> 2
    qbeta-habiro-element-probe      C 1 -> 0,  D 0 -> 2
    paper-six-term-isotope-sweep    term1_canonical_tr_M (proton, habiro mode)
                                    1.0653062286131671 -> 1.1457596924573008

That last is the **7.55 % C→D gap in a paper-facing sweep column**, in two
places (`/all_modes/habiro` and `/all_modes/combined`).

### 🛑 The environment blocker I recorded was WRONG

I reported these as needing "a Python 3.13 container I cannot produce here".
**`/usr/bin/python3.13` was already installed** — 3.13.12, byte-matching the
version the witnesses record. The default `python3` is 3.11, which is the whole
of it. Every dependency was reachable: mpmath/numpy/sympy/scipy/clarabel by
pip, the local packages by `pip install -e`, and `pyhecke_native` **built from
`tools/pyhecke-native` in 31 s** with the `maturin` already on PATH.

Nothing was missing except the check. Recorded because "I need an input I
cannot produce" is the most expensive kind of wrong claim to leave in a bean —
it stops the next agent from trying.

### Still open

- `markov-peel-atomic-tr-m.derivation.json` — no producer recorded anywhere in
  the artifact; cannot be regenerated. Unchanged.
- `qou-mass/.../data/_deprecated/markov_weights_symbolic.witness.json` —
  deprecated mirror, correctly left alone.
- The **Model B** leg of the six-term sweep, which turned out to be worse than
  a missing witness: the producer it names has never existed. Split to
  `qou-imkb` with the measurement.


## 2026-08-30 (second pass) — the "no producer" residue is SCOPED, and I was wrong about why

`markov-peel-atomic-tr-m.derivation.json` was listed here as unfixable — "no
producer recorded anywhere in the artifact; cannot be regenerated."

**True but misleading, and it is the fourth blocker I have understated this
session.** It is not a producer output at all. It is a **hand-authored
derivation-chain document** (PR #516) with a `steps` array of prose. There is
nothing to regenerate; the numbers are typed into a record. So the fix was
never a compute — it was an edit.

**Both of its numeric steps are convention C**, and it is worse than the one
value this bean was grepping for:

- **step 3** `tr_M_at_q0_both_pins` — proton `1.06530614425444998…`, muon
  `1.06530622861317006…`. Note the value this bean tracks is the **muon** one;
  the proton-pin C value differs at the 8th digit (the μ–p tension, 7.9e-8).
- **step 4** `peel_vs_bridge` — deuteron peel `0.38835714…` vs bridge
  `0.38835712…`, agreeing to 1.86e-8. **Both sides are C**, so the agreement is
  real *within C* and says nothing about D. The live D-frame bridge deuteron is
  `0.5751722439…` — **48 %** away.

**It also directly contradicts a file I migrated earlier today.**
`derivation_chain.py::TR_M_AT_Q0["p"]` is `1.1457596924573009` (D); this
document says `1.0653…` (C) for the same quantity. Two artifacts describing one
derivation, disagreeing by 7.55 %, and `derivation_chain_validator.py` passes
both — it validates structure, not convention.

**Fixed by scoping, not correction**, per the c_k-banner precedent: the values
are correct for C and are the historical record. Added a convention-C banner to
`target`, a scoping block to `description` carrying the live D values and their
source, and per-step notes on 3 and 4. Step 3's note warns specifically against
confusing its 7.9e-8 pin difference with the ~7.55 % convention gap — a factor
of a million apart, and the exact normalisation-vs-discrepancy confusion this
corpus keeps making.

Steps 0–2 (Hecke relation, GS normal form, Markov ascent) are
convention-independent and are marked as such.

**Residues after this pass:** one — the `qou-mass/.../data/_deprecated/`
mirror, correctly left alone.


## 2026-10-10 (session_01ST9RpvTF7JHNdUNafrjf9J) — linked from thread qou-moj0 (nucleon word/ordering).
