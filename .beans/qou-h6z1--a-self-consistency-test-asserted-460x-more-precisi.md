---
# qou-h6z1
title: A self-consistency test asserted 460x more precision than its CODATA input carries
status: todo
type: task
created_at: 2026-08-24T00:14:09Z
updated_at: 2026-08-24T00:14:09Z
---

`mass-from-q-symbolic.witness.json` flipped two assertions PASS -> FAIL during
the staleness drain. It is **neither a stale pass nor a defect** — it is an
assertion demanding agreement far tighter than the experimental uncertainty of
its own reference constant, which stopped being satisfiable the moment CODATA
was corrected.

## The two assertions

    ℏ_q² = Vol(4_1) / (m_μ/m_e)
      computed  0.009817188513985985
      expected  0.009817188527722428
      tolerance 1e-15                    <- miss is 1.37e-11, i.e. 13,700x
      source    "Definitional (q_parameter.py)"

    m_μ/m_e from Vol(4_1)/ℏ_q²  (self-consistency)
      computed  206.76828298931505
      expected  206.7682827               (= MASS_RATIO_MU_E, CODATA 2022)
      tolerance 1e-08                     <- miss is 2.89e-7, i.e. 29x

## The measurement that settles it

`MASS_RATIO_MU_E = 206.7682827 ± 4.6e-06`.

The value implied by the recorded muon pin is **206.768282989315059**, so the
discrepancy is **2.89e-7 against a 1-sigma experimental error of 4.6e-6** —
about **0.06 sigma**. The pin is not wrong; it agrees with CODATA to a small
fraction of the error bar.

Equivalently, on the q side:

    q0 derived from current CODATA   1.10997859564273905119…
    recorded muon pin                1.10997859555733471990…
    difference                       8.54e-11 absolute, 7.69e-11 relative

**A self-consistency check at tolerance 1e-08 — and worse, 1e-15 — against a
constant known to 4.6e-06 is asserting 460x more precision than its input
carries.** It could only ever pass while the pin was numerically identical to
the then-current CODATA value, which it was: the pin was derived from it. When
`codata_constants.py` was corrected on 2026-08-19 (the commit whose message
records that the canonical reference was *"hand-typed and 7 of 11 were
wrong"*), the exact identity became an approximate one — still well inside
experimental error, and now failing an exactness test.

## Also surfaced: the producer has NO anchor manifest entry

`q0_anchor_manifest.json` holds 645 entries (513 physical_proton, 110
ideal_muon, 22 ambiguous) and **`mass-from-q-symbolic` is in none of them**, so
`q_parameter`'s stem-based auto-select falls through to the proton pin —

    default run           q0 = 1.1099785827513808…   (PROTON)
    QOU_Q0_ANCHOR=muon    q0 = 1.1099785955573347…   (MUON)   assertion 2 PASSES its q0 check

The producer's entire subject is deriving `m_μ/m_e` from `Vol(4_1)/ℏ_q²`, which
is the CAL-2 **ideal=muon** definition the manifest's own `_convention` string
describes. It looks mis-classified by omission. Note that running it under the
muon anchor still fails both tolerances — the anchor and the tolerance are
independent problems, and fixing the anchor alone does not clear this.

## The decision

Two defensible resolutions, and this is deliberately not chosen here:

  (a) **Re-derive the muon pin from corrected CODATA.** Makes the identity
      exact again by construction. Moves a load-bearing constant by 7.69e-11
      relative — small, but it is a substrate anchor with ~110 manifest
      consumers, so the blast radius is the question, not the size.

  (b) **Relax both tolerances to the uncertainty they inherit.** A quantity
      derived from a constant known to 4.6e-6 cannot be asserted to 1e-15. The
      honest tolerance is propagated from `MASS_RATIO_MU_E_ERR`, not chosen.

**Do NOT simply widen the numbers to green.** The ratchet's own output warns
against exactly that, and (b) is only legitimate if the new tolerance is
DERIVED from the stated error and says so in `source`. The current
`source: "Definitional (q_parameter.py)"` on a 1e-15 test is the part that
misleads: it reads as an exact definitional identity when it is an empirical
one.

Whichever is chosen, add `mass-from-q-symbolic` to the manifest so the anchor
stops being decided by fallthrough.

## Attribution

Unresolved. The witness was rewritten at 22:40:23 during the drain and appears
in no run log kept by either agent. HEAD's copy was computed 2026-04-14 — over
four months old — so the flip surfaced whenever it was next run, by whoever ran
it. The witness in the tree has been restored to HEAD pending this decision.
