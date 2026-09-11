---
# qou-w942
title: 'GAP: self_built_braid_word_audit is blind to SIBLING kernels — gram_transfer_quadratic raises on the canonical word and the detector reports 0'
status: todo
type: bug
priority: normal
created_at: 2026-09-11T15:07:09Z
updated_at: 2026-09-11T15:07:10Z
---

## Found 2026-09-11, re-running `qou-geqa`'s TIMEOUT bucket at a real budget

`computations/gram_transfer_quadratic.py` **fails on `main`-current code**, and
it fails on its own guard:

    2H: n=6 …
    Traceback (most recent call last):
      File ".../gram_transfer_quadratic.py", line 353, in main
        Ga, pl_a, norms_atom = gram_norm_zn(Z, N, include_inter=True)
      File ".../gram_transfer_quadratic.py", line 251, in gram_norm_zn
        norms = gram_all_lambda(word, n, dps=dps, q=qm)
      File ".../gram_transfer_quadratic.py", line 181, in gram_all_lambda
        raise ValueError(f"non-monotone word: gen {g} after {last}")
    ValueError: non-monotone word: gen 0 after 1

Reproduced from **both** `cwd=<producer dir>` and `cwd=<repo root>`, with
`PYTHONPATH` set — i.e. it survives all of `qou-geqa`'s seven harness
requirements. Exit 1 in **0.3 s**.

## This is `qou-y2o7`'s class, and `qou-y2o7` is COMPLETED and does not cover it

`qou-y2o7` — *"compute_tau_M_nucleon_H3 is locked to the grouped ordering by its
monotone-only chi kernel; 18 consumers inherit it"* — is the same mechanism: a
monotone-only transfer kernel meeting a canonical word that is non-monotone by
construction. Verified with the producer's own decoder:

    proton      gens [0,1,0,1,0,1,0,0,1,0,0]                          monotone: False
    neutron     gens [0,1,0,1,0,1,0,0,1,0,0]                          monotone: False
    deuteron    gens [0,1,0,1,0,1,0,0,1,0,0,2,3,4,3,4,3,4,3,3,4,3,3]  monotone: False

**Every** atom's canonical word is non-monotone. But `gram_transfer_quadratic`
is **not** in `qou-y2o7`'s scope: that bean is about the *silent* cases, which
"never raised because they built their own word", and it explicitly contrasts
them with *"`atom_braid_word_3A`, a producer that raises on a non-monotone
word"*. This one consumes `atom_braid_word_3A` and raises — a LOUD case, and it
has its **own kernel**, `gram_all_lambda`, not `chi_monotone_transfer.chi_all_lambda`.

No bean records it. `gram_transfer_quadratic` appears in exactly three bean
lines: twice in `qou-mnrd` (the float64 ratchet, a different subject) and once
in `qou-geqa`'s TIMEOUT list.

## 🛑 The detector `qou-y2o7` ASKED FOR cannot see it — measured, 0 of 71

`computations/audits/self_built_braid_word_audit.py` (PR #6960) is the
provenance-keyed selector that bean's closing section requested, precisely
because *"a selector keyed on BREAKAGE finds the loud cases"* and the silent ones
needed something better. Run today:

    chi-kernel call sites: 71
      CANONICAL 47   MIXED 2   SELF_BUILT 0   INHERITED 11   OTHER 11
    ACTIONABLE (monotone, undeclared): 0

    grep -c gram_transfer_quadratic  ->  0

**It enumerates χ-kernel call sites.** `gram_all_lambda` is a *gram* kernel —
a different function name carrying the identical monotone assumption — so it is
outside the detector's kernel list and invisible to it.

That is the corpus's recurring detector-blindness shape arriving one level up on
itself: `qou-y2o7` correctly diagnosed that keying on *breakage* misses the
silent cases and replaced it with keying on *provenance* — but the provenance
detector keys on the **kernel's name**, so a sibling kernel dodges it. Neither
selector covers both halves: the breakage-keyed sweeps would have caught this
one (it raises loudly) and the provenance-keyed one cannot.

## What would fix the detector

Key on the **guard**, not the kernel name. Every kernel of this family raises on
a non-monotone word, so the discriminator available to an AST pass is "calls a
function whose body asserts generator-index monotonicity" rather than a
hardcoded list of `chi_*` names. Cheaper interim: add `gram_all_lambda` to the
kernel list and re-run — but that fixes this instance, not the class, which is
the exact trade `qou-y2o7` already refused once.

## What is NOT established here

- **Whether the producer is wrong or the word is.** It may be that
  `gram_transfer_quadratic`'s quadratic transfer genuinely requires grouping and
  needs a different algorithm under the ruling, or that it should pin the
  grouped word explicitly and declare itself superseded-ordering. That is the
  same A/B/C decision `qou-y2o7` records as *"open and uncollided"* for
  `closed_form_tau_M` — do not pick one here.
- **When it broke.** `qou-geqa` recorded it as a TIMEOUT (>240 s) on
  2026-08-23; it now dies in 0.3 s. A 0.3 s crash cannot have been a 240 s
  timeout, so the word it receives changed in between — consistent with the
  ordering ruling, but I have **not** bisected it and am not asserting the
  commit.
- **Its consumers.** Not measured.
