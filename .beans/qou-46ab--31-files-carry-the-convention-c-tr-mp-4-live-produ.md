---
# qou-46ab
title: 31 files carry the convention-C tr_M(p); 4 live producers HARDCODE it as a reference
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:41:11Z
updated_at: 2026-08-30T06:41:51Z
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
