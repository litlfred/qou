---
# qou-5lib
title: 'GAP: the 40 = |S_5|/3 Bring prefactor and the depth-90 tower are not derived — only their arithmetic consequence is'
status: in-progress
pr: 8198
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T21:48:29Z
updated_at: 2026-11-16T20:55:00Z
parent: qou-n4nr
---

## What was closed, and what was not

`observations/n-v-leading-order-derivation.lean` carried

    axiom v_over_m_e_bridge :
      ∃ ε₁ : ℝ, |ε₁| ≤ 0.006 ∧
        v_ew_real / m_e_real = 40 * q_0_real^90 * (1 + ε₁)

with `q_0_real`, `m_e_real`, `v_ew_real` all concrete decimal literals. That
makes it a FINITE ARITHMETIC FACT about rationals, not an open claim, and it
is now a proved theorem (witness = the exact residual, bound by `norm_num`;
lean-direct exit 0 in 3.2 s). `n_v_leading_order` went from naming the axiom
in `#print axioms` to the standard three.

## The gap this bean is for

Proving the number does not derive the STRUCTURE. Fix the two integers and
everything else is arithmetic — which is exactly why the axiom carried no
conjectural content: it asserted the arithmetic and left the categorical
claim unstated. Open:

  (i)   `BraneTowerLevel` as a Gröbner–Shirshov filtration grade;
  (ii)  the q_0-rescaling-per-generation lemma (each Hecke generation
        rescales the mass scale by q_0, so v/m_e ∝ q_0^depth);
  (iii) the categorical derivation of the |S_5|/3 = 40 Bring fibre-functor
        prefactor;
  (iv)  the Coxeter tower depth from m_e to v being 90.

None exists in Lean. No carrier was invented for them, deliberately: a class
that merely re-pins 120 and 90 would be PROVABLE and so would assert nothing
— the defect this tranche has been draining elsewhere.

## Numbers, recomputed — the file's own check was wrong

Exact rational arithmetic (`fractions.Fraction`), cross-checked at mp.dps=50:

    v / m_e   = 481840.5197653147
    q_0^90    =  11977.4350125798      (docstring said ~12012, 0.29 % high)
    ratio     =     40.2290239320      (docstring said ~40.11)
    ε         =      0.0057255983      (docstring said ~0.003)

So |ε| ≤ 0.006 holds with a headroom factor of only **1.048**. The old
docstring understated ε by 1.9× and made the bound look about twice as slack
as it is. Anyone tightening the bound, or re-pinning q_0, should know it is
4.8 % from failing. Corrected in the file.

## Cross-refs

Sibling `conj:n-v-bring-action` carries `axiom s5_acts_on_ew_slice` and is
the last remaining `axiom` carrier in the conjecture corpus
(`scripts/conjecture-carrier-kind-audit.ts`). Whether it is the same
situation — a decidable statement assumed — has NOT been checked.

## Round 54 Progress (PR #8198)
- [x] Added `v_over_m_e_residual_two_sided_bounds` (`0.0057 < ε < 0.0058`), `bring_s5_prefactor_factorization`, and `tower_generation_rescaling` to `folio/quantum-observable-universe/observations/n-v-leading-order-derivation.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified exact rational and 80-dps two-sided residual enclosure in `computations/probes/boxcontent_ward_nv_interface_binding_probe.py` (`computations/probes/boxcontent-ward-nv-interface-binding.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8198 (`1f80984f96ba3e6334bf43a2df76dd82a90eba3e`).
