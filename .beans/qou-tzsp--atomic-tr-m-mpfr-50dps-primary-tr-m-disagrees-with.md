---
# qou-tzsp
title: 'atomic-tr-m-mpfr-50dps: primary tr_M disagrees with its own peel_cross_check by 1.85e-9'
status: completed
type: task
priority: normal
created_at: 2026-08-16T21:23:42Z
updated_at: 2026-08-17T01:02:37Z
---

## Evidence (PR #5260, rho_k_h3a_residual_decomposition.py)

`atomic-tr-m-mpfr-50dps.witness.json` carries two deuteron tr_M values that
disagree with each other:

    results.tr_M_at_q0_50dps                  = 0.57517232916588433221594741758...
    results.peel_cross_check.tr_M_at_q0_50dps = 0.57517233101788385191979179668...
    difference                                = 1.8519995e-9

An INDEPENDENT route — the Schur-Weyl sum Sum_lambda y_lambda chi^lambda, built
from the Wenzl-bridge y_lambda and a fresh Hoefsmit chi, evaluated at the
witness's own muon q_0 — lands on:

    0.5751723310178838519197917966871536588755

i.e. it matches the **peel_cross_check** branch to 3.1e-49 (the 50-dps engine
floor) and misses the **primary** branch by exactly 1.852e-9.

Two independent computations agreeing to the floor is strong evidence the
PRIMARY value is the wrong one. That matters beyond bookkeeping: `primary` is
the field consumers read (`rho_k_h3a_refinement.py:303` takes
`r["tr_M_at_q0_50dps"]`), so every downstream self-check has been differencing
against the less reliable of the witness's own two numbers.

Same magnitude appears on the other atoms in that witness (helium-3, helium-4,
tritium rows each show a primary/peel gap in the 1e-9 range), so this is likely
systematic in the peel-vs-direct routes rather than specific to the deuteron.

**Not fixed here** — the fix belongs to that witness's producer, and deciding
WHICH branch is canonical needs the producer's author. Scope-(a): this is a
localisation, not a proof that `peel` is right; it is evidence, and the third
independent route is what would settle it.


---

## RESOLVED (PR #5260, 2026-08-17) — PRIMARY is wrong; the mechanism is a layer straddle inside it

The verdict this bean recorded ("evidence the primary value is the wrong one")
holds. The *reason* I gave for it was weak — "two independent routes agree" —
and the actual mechanism is now pinned to one line.

`tr_M_via_wenzl_bridge_mpfr` (`computations/tr_m_wenzl_bridge_mpfr.py:402`)
loaded its y_λ table with a bare

    y_table = _load_y_lambda(n, y_lambda_path)      # y_lambda_path=None

whose `None` default is `_Y_LAMBDA_DEFAULT = y-lambda-mpfr-**proton**-witness.json`.
So every caller evaluating at the **muon** pin combined **proton y_λ** with
**muon χ** — precisely the straddle that `load_y_lambda_for_q0` in the same
module was written to refuse, bypassed by calling the raw loader instead of it.
That guard's own docstring says "Refusing is the point"; nothing routed through
it.

**Proof, by swapping only the table:**

    y_λ table = proton (today's default)  ->  reproduces committed primary to 0.0
    y_λ table = muon   (layer matched)    ->  matches peel_cross_check to 4.97e-51

Magnitude checks out independently: the μ–p tension is 11.54 ppb, and
11.54 ppb x y_(6) ~ 0.115 is ~1.3e-9, which is the per-partition y deviation
measured. Summed over the four ℓ(λ)≤2 partitions it gives the observed
1.852e-9 on tr_M.

**Three hypotheses I tested and refuted before landing on this**, recorded so
nobody re-walks them:

1. *Colour-blind vs colour-weighted crossing.* No — the bridge word's d-value
   multiset matches the canonical word exactly (11 σ, 7 σ⁻¹, 4 averaged,
   1 averaged_weighted).
2. *The word built at a different q than it is evaluated at.* No — rebuilding
   the word at the muon q reproduces the committed primary to 1.3e-51, so the
   word was already materialised at the right q.
3. *`flavor_split_leading` vs `flavor_split_subleading` δ.* Real (the two differ,
   and the bridge uses leading while `d_for_ctype`'s default is subleading) but
   far too small — worth 2.3e-11 in d and 2.6e-11 in tr_M, not 1.85e-9. Left
   as-is; it is a separate question from this bean.

The discriminating measurement was per-partition: **χ agree to ~1e-50 (engine
floor) while y_λ disagree at ~1e-9** — which points at the weight table, not the
character engine.

**Fix:** the bridge now selects the table by the layer of `q_str`
(`load_y_lambda_for_q0`) when the q is a recognised pin. An explicit
`y_lambda_path` still wins, and an unrecognised q (a sweep) keeps the historical
default rather than raising — refusing there would break every sweep for no
safety gain.

**Blast radius:** 14 importers of the bridge; **5 muon-anchored witnesses**
produced by them carry the defect —
`atomic-tr-m-mpfr-50dps`, `binding-canonical`, `mass-table-comprehensive`,
`wedderburn-lp-ew-wiring`, `ame-2020-binding-energies`. Only the first is
regenerated on this PR; the other four are named, not silently left.
