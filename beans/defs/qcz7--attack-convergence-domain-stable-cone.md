---
# qcz7
title: 'Attack A: reaches_cycle — convergence over the domain-stable cone'
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:46:17Z
updated_at: 2026-11-18T10:36:00Z
parent: qcz14
---

Goal: every domain-stable positive Skein element reaches {q^-1,1+q^-1}.

Routes (try in order; each is a chip, may partially close):
A1. CHARACTERIZE the domain-stable cone D∞ = {P : ∀k, C^[k]P in domain}.
    Conjecture from the probe: D∞ = backward-orbit tree ⋃_k C^{-k}(cycle).
    If proved, convergence is immediate (tautological). Lean: define
    inDomain, D∞ predicate; prove cycle ⊆ D∞ (have the 2-cycle lemmas);
    prove each branch-inverse lands back in D∞.
A2. DESCENT MEASURE (q-analog of Collatz stopping time). Define the
    [2]_q-adic valuation v_[2](P) (already def:collatz-contact-boundary).
    Prove per-cycle contraction [3]_q/[2]_q^3 < 1 (have the archimedean
    identities in QOU/QCollatz.lean: qInt_gap, contraction_ratio_lt_one).
    Build a well-founded descent function on D∞ minus the cycle ⇒
    convergence by well-founded recursion. This is the paper's contact
    condition ⟨v_[2]⟩>=2 made into a Lean measure.
A3. If A1/A2 stall: prove the WEAKER conditional "if v_[2] descent holds
    then reaches_cycle" (a §3b-cond theorem taking the descent as a class
    hypothesis) — honest partial, wires nothing to production.

Deliverable per route: a sorry-free Lean lemma OR an honest documented
wall. Preflight: lean_leansearch for well-founded-recursion / valuation
descent lemmas before hand-rolling.

PROGRESS (A2/A3): reaches_cycle_of_descent PROVED sorry-free (QCollatz.lean) — convergence follows from ANY strictly-descending measure mu + forward-invariance. Factors the open conjecture into (proved reduction) + (open: existence of mu, the q-analog stopping-time / <v_[2]>>=2 contact bound). Still open: construct mu (A1 D-infinity characterization + A2 [2]_q-adic descent).

WALL (honest): reaches_cycle_of_descent + qcollatz_attractor_orbit_bounded PROVED. Remaining hard core = construct the descent measure mu (q-analog Collatz stopping-time). Needs a Lean [2]_q-adic valuation over LaurentPolynomial Z + global-descent proof. No elementary construction known — documented in the 2026-07-18 audit.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-11-18 — Round 67 PR #8429 (`claude/round67-devacuify-6qbv-b9cj`)

- PR: https://github.com/litlfred/qou/pull/8429 (`309fbd8f12dcf4d789f3437e4bedf0425965e331`, C1 `202ce0a6f5124bc5df548850fb8706709c33eae1`)
- Probe: `computations/probes/round67_devacuify_6qbv_b9cj_probe.py` (`scriptHash = scriptSha256 = 33016f917e977bd9e4a22e14e192b44ea617b7cd335221741598e8aee1a1a640`, `dps = 80`, `allPassed = true`)
- Directory-mode static audits: `0 CRITICAL, 0 major, 0 advisory` across all 6 scripts; `0` `sorry` and `0` `axiom`.
