---
# qou-46ab
title: 31 files carry the convention-C tr_M(p); 4 live producers HARDCODE it as a reference
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:41:11Z
updated_at: 2026-08-30T12:15:51Z
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
