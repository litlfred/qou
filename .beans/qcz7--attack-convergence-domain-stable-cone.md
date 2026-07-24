---
# qcz7
title: 'Attack A: reaches_cycle — convergence over the domain-stable cone'
status: in-progress
type: task
priority: medium
parent: qcz6
created_at: 2026-07-24T16:46:17Z
updated_at: 2026-07-24T20:34:38Z
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
