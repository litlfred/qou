---
# qou-2pnv
title: 'DERIVE-OR-RETRACT: B = -alpha*ln|tr_M| is posited - no derivation, nothing in Lean, only a notation-table row, and a dead citation'
status: in-progress
pr: 8198
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:53:53Z
updated_at: 2026-11-16T20:55:00Z
parent: qou-10v9
---

## SELF-CORRECTION 2026-08-25 — significance over-claimed, measurement stands

I called the 12.4347 prefactor gap 'the single most concrete unresolved item on the
binding leg'. Wrong. m_e/hbar_q^2 is the prefactor of m = m_e*Vol*rho/hbar_q^2, and that
shape is DEPRECATED for absolute mass - its own runtime DeprecationWarning says
'per_knot_density_borromean is the lambda_A fit (... -> 966 MeV) - NOT the canonical
absolute nucleon mass. Use the canonical_mass facade.' That is the lambda_A route excised
by the 2026-06-24 owner ruling. The dashboard's live mass route is the muon-anchored
Hecke energy and does not use vol_density at all.

So: ONE live prefactor (E0), one belonging to an excised shape. Not a contradiction. And
for binding ratios AGENTS.md keeps vol_density_per_block valid precisely because SCALE
CANCELS - the prefactor drops out of a ratio entirely.

SURVIVES: the measurement (exact to 1e-49, q0^3/(q0-1) = 1/(c_q^2 hbar_q^3)), and the
2026-08-09 gap-4 finding that nothing validates E0 at the binding scale - that is about
E0's own justification and is independent of the deprecated shape.

Root cause of my error: I read the mass formula's SHAPE out of the AGENTS.md banner and
did not check whether that shape is live. The banner that states the shape is the same
banner that deprecates it.

## 2026-09-04 — owner has adopted this as the working assumption; three of the four objections discharged

Owner ruling: **Option B with the Option C framing, and the 2.656 factor stated
as open.** Option B is exactly this bean's `B = -alpha.ln|tr_M|`, in the form

    B = E_0 . log( tr_M(beta_free) / tr_M(beta_atom) ),   E_0 = m_e/(q0(q0-1))

Against this bean's four objections ("posited — no derivation, nothing in Lean,
only a notation-table row, and a dead citation"):

- **DERIVATION — supplied.** `tr_M` is multiplicative along the chain (the closed
  form is a product); binding energy is extensive. `log` is the unique map
  carrying one to the other, so the functional is forced, not posited. Stronger:
  the tower's own Markov relation `tr_{n+1}(x.sigma_n) = z.tr_n(x)` makes
  `nu(x) = log_z tr_M(x)` the additive counter, and `b_pp = z` exactly, so a p-p
  bond IS one Markov reduction. Option B is `nu`'s archimedean realization at q0.
- **LEAN — supplied.** `QOU/Hecke/BindingExtensivity.lean`, 6 decls, sorry-free,
  `[propext, Classical.choice, Quot.sound]`, lean-direct exit 0.
- **MEASUREMENT — supplied.** p5-p95 residual **1.225x** over 2548 measured AME
  nuclides at the DERIVED `E_0`, against **1592x** for `B = s.Delta_tr`.

**STILL OPEN, and now sharper:** `E_0` is **2.656x** below the best single scale
(11.119 MeV) — the "nothing validates E0 at the binding scale" gap this bean's
own self-correction preserved. And see `qou-q7ga`: the deformation's contribution
is net-negative, so what is currently earned is "the algebra produces an
extensive quantity", not the specific bond energies.

Not marking complete: the derive half is done, the SCALE is not.
`docs/audits/2026-09-04-binding-law-options-decision-frame.md`.


## 2026-09-04 (qou-rp9i) — two surfaces created today after #6611's branch and before its merge stated B = Q_β·Δtr: docs/audits/2026-09-04-cyclic-triple-word-class-prune-and-probe.md and computations/probes/cyclic_triple_bond_cross_term_probe.py. Both now carry superseded-law notes pointing at 2026-09-04-cyclic-triple-under-log-law.md. The wider sweep remains unscoped.

## 2026-09-05 — the retraction sweep is DONE, and it was one file

This bean tracked the sweep across every surface stating `B = Q_beta.Delta_tr`.
Measured rather than estimated: the only LIVE surface is
`computations/binding_canonical.py` (two call sites). Everything else a grep
catches is a false positive — `mba-step09b-per-isotope-binding.md` is a different
calibrated CKRecursion model, the notation entries are symbol disambiguation, and
the `docs/audits/*` hits are dated snapshots that should NOT be rewritten.

Landed: a module-level SUPERSEDED banner plus an inline note at each call site,
stating the refutation, the replacement, the ruled scale, and where the full
record is. The computation is unchanged — `B_MeV` still returns the old quantity
for provenance and comparison — because changing it would break every consumer,
and the sweep's purpose is that no surface states the refuted law without saying
so.

The derive half of this bean closed 2026-09-04 (derivation, Lean, full-table
measurement); the scale half closed 2026-09-05 with the tower ruling
(`qou-qkbp`). Full record:
`docs/audits/2026-09-05-binding-law-arc-synthesis.md`.

## Round 54 Progress (PR #8198)
- [x] Added `deprecated_vs_canonical_prefactor_ratio`, `prefactor_ratio_eq_inv_cq_sq_hbar_cu`, and `binding_ratio_scale_invariant` to `folio/quantum-observable-universe/lean/QOU/Hecke/BindingExtensivity.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified 80-dps prefactor ratio `q₀³ / (q₀ - 1) = 12.43471049...` and scale cancellation in `computations/probes/boxcontent_ward_nv_interface_binding_probe.py` (`computations/probes/boxcontent-ward-nv-interface-binding.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8198 (`1f80984f96ba3e6334bf43a2df76dd82a90eba3e`).
