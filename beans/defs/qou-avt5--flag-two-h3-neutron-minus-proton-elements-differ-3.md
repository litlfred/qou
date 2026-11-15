---
# qou-avt5
title: 'FLAG: two H_3 "neutron minus proton" elements differ 39% at the substrate, with no disambiguation row'
status: completed
type: task
priority: high
created_at: 2026-08-26T04:30:52Z
updated_at: 2026-08-26T06:43:03Z
---

Parent: `qou-avtq`. Surfaced while checking `qou-avt2`'s premise (are the
hand-derived per-block characters right?) before building a general-n tool.

NOT A BUG REPORT. This MEASURES a discrepancy and does NOT determine which object
is intended. Do not cite it as showing either one wrong.

## The two objects

(A) `Delta = NF(n) - NF(p)` -- the GROBNER-SHIRSHOV NORMAL FORM difference.
    `nuclear-interactions/qbeta-counit-closed-form.md` derives
    `eps(Delta) = h^2/2 - h`, `tr_M(Delta) = h^2/2 - h*z`, and qou-cds1
    verified `eps(Delta)*E_0` reproduces the committed Q_A closed form exactly.
    This is what the ladder phase is built from (`eps - tr_M = h(z-1) = 2*alpha`).

(B) `Delta_T_beta` -- whose per-block characters are the hand-derived closed
    forms in `qbeta_utils.py` and Lean `QBetaPerBlockChiClosedForms`
    (`-- Ref: [hoefsmit1974]`). Their source witness
    `qbeta-per-block-paper-closed-forms` calls them `chi_lambda(beta_n - beta_p)`
    -- the RAW BRAID difference, not the normal form.

## The test and the measurement

The counit is the 1-dim rep `sigma_i -> q`, i.e. exactly the `lambda = (n)`
block, so for ONE AND THE SAME element `chi_(3)(X) = eps(X)` identically.

    q            chi_(3)(Delta_T_beta) / eps(Delta)
    1+1e-2       1.030454535251763
    1+1e-4       1.000300045004500
    1+1e-8       1.000000030000000
    q -> 1       1                    (exact limit)
    q0           1.39090616920312     <- 39% at the substrate

They AGREE CLASSICALLY and DIVERGE AT THE SUBSTRATE. Both are linear in hbar_q at
leading order (each -> -2*hbar_q), which is why a leading-order check missed it.

Downstream: `Delta_tau_M = sum y_lambda chi_lambda(Delta_T_beta)` is NOT
`tr_M(Delta)` in either weighting (-0.18443 dim-weighted / -0.15802
un-dim-weighted vs -0.10624), so the two feed different consumers with no note.

## Why this is a flag and not a shrug

Agreeing at q=1 and differing at q0 is exactly what TWO DIFFERENT
q-DEFORMATIONS OF ONE CLASSICAL OBJECT look like -- real, common, and not
automatically an error. What IS a defect is that the corpus carries NO registry
section-2 disambiguation row for these two and nothing in docs/, content/ or
computations/ states that they differ. AGENTS.md names this exact class
("distinct objects sharing a glyph is a recurring root cause") and registry
section 2 exists for it.

## What would settle it (NOT attempted here)

Exhibit the two WORDS.
* If `NF(n)-NF(p)` and `beta_n - beta_p` are genuinely distinct elements of
  H_3(q): add the disambiguation row and move on.
* If they are meant to be the SAME element: one of the two closed forms is wrong
  at O(hbar_q^2), and either the ladder (via eps/tr_M) or the per-block c_k
  extraction inherits the error. That would be consequential -- the ladder's
  whole phase is eps - tr_M.

Probe: computations/qbeta/qbeta_delta_vs_deltaTbeta_discrepancy_probe.py (5/5)

## SETTLED 2026-08-26 — and it resolves AGAINST this bean's own reading

The bean said: *"agreeing at q=1 and differing at q0 is exactly what TWO
DIFFERENT q-DEFORMATIONS OF ONE CLASSICAL OBJECT look like."* **That reading is
WITHDRAWN.** It is one VERIFIED element against one ASSERTED polynomial.

### Side B is now VERIFIED, and the paper forms are CORRECT

The nucleon words ARE exhibited — `hecke_core._PROTON_G0/G1`,
`_NEUTRON_G0/G1`, typed-crossing chains `(c, d, gen)` with `d ∈ {0, −h/2, −h}`.
Through the **d-preserving** path (`chi_monotone_transfer.chi_all_lambda`) they
reproduce the "paper closed forms" EXACTLY, all three blocks, at q0:

    lambda      chi(n)-chi(p) from WORDS      chi_block (paper)     ratio
    (3)            -0.260387641790121    -0.260387641790121          1.0
    (2,1)          -0.106814457651578    -0.106814457651578          1.0
    (1,1,1)        -0.171538643776599    -0.171538643776599          1.0

So `Delta_T_beta = beta_n - beta_p`, the `[hoefsmit1974]` transcription checks
out, and side B is closed.

### Side A has NO ELEMENT

`eps(Delta)` is `QOU.Interactions.QBetaEnergyScale.epsNPq` — a **bare `def`**, a
polynomial in q. No Hecke element is constructed anywhere; `Qbeta_closed` is a
ring identity between two closed forms. The content block has NO `.lean` sibling
(`validation: "not_checked"`) and states its closed forms without a word.

### Why that makes them different ELEMENTS

The counit IS the 1-dim rep `sigma_i -> q`, i.e. exactly the `lambda = (3)`
block. And Grobner-Shirshov normal form is a REWRITING to a canonical
representative of the SAME algebra element, so chi is invariant under it:
`chi_(3)(NF(n) - NF(p)) = chi_(3)(beta_n - beta_p)` NECESSARILY. Measured at q0:

    chi_(3)(beta_n - beta_p) = -0.2603876417901208   <- exhibited element
    epsNPq ("eps(Delta)")    = -0.1872071945293783   <- asserted def
    eps/chi                  =  0.718955758585

So `epsNPq` is not the counit of the exhibited difference. It is the counit of
some other, never-exhibited object — plausibly the "single-wrap" / "N=0"
truncation its own prose names.

### Why it matters

`Q_A = -E_0 * eps(Delta)`. So Q_A — and hence the WHOLE Q_beta ladder, whose
phase is `eps - tr_M` — rests on that asserted polynomial, while the corpus's
verified element gives a different number at the same q0.

NOT CLAIMED: that either is wrong. A single-wrap truncation is a legitimate
object and may well be the intended one. What is established is that they are
DIFFERENT, that only one is exhibited, and that no disambiguation row exists.
**Settling which belongs in Q_A needs the single-wrap element written down.**

NOT MEASURED: the ratio's q-dependence. The words are q0-BAKED (their `d` are
literal `-h(q0)/2`, `-h(q0)`) and `word_to_mpfr` classifies `d` against `h(q)`,
so a q-sweep raises rather than re-lifting. Every number is at q0 only.

### The process failure this run produced, recorded because it is instructive

My FIRST attempt at this computed chi from the words and got a THREE-WAY
disagreement, including an OPPOSITE SIGN on the (2,1) block. It calibrated
"exactly" against `compute_tau_M_nucleon_H3` — and was wrong, because that
function was itself wrong by 15.3 % (proton) / 27.3 % (neutron). A sibling had
root-caused and fixed it on main FOUR HOURS EARLIER (`e5deb145c`, bean
`qou-qu2w`: the marshaller "emits signs and drops `d` entirely", replacing the
Markov factor `z - h/2` by `z` at two sites per nucleon) while this branch sat
16 commits behind.

**Calibrating against the corpus does not protect you when you are behind the
corpus.** The calibration passed precisely because both sides shared the defect.
Merge before trusting a cross-check against a live producer — and note the
earlier probe's chi_(3)-vs-eps measurement was NEVER affected, because both its
sides were closed forms; only the word-derived column was contaminated.

Probe: computations/qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py (7/7)
Supersedes: qbeta_delta_vs_deltaTbeta_discrepancy_probe.py
