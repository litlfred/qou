---
# qou-vd7j
title: 'GAP(knot-solver): canonical knot-assignment SDP admits 0/3558 at Frobenius level — open R5 gap (finitude/search-bounds/K(H) structural id)'
status: in-progress
pr: 8344
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T13:56:51Z
updated_at: 2026-11-20T15:40:00Z
parent: qou-v2om
---

## Finding (2026-08-02) — the solver runs; the Frobenius selector is empty
Ran the existing chart-wide solver `all_nuclides_sdp_admissibility.py` (deps:
numpy/scipy/mpmath/sympy/cvxpy + local pyhecke; AME data at
computations/data/ame2020.json — the script's hardcoded
`/home/user/qou-mass/...` path needs a symlink or fix, filed inline):

- **Swept 3558 AME nuclides at q₀.**
- (a) active-channel count, **scalar LP** (n_target=A): {1: 2221} — 2221
  nuclei admit a feasible scalar-net solution, all with a single active channel.
- (b) permitted nuclei, **scalar LP**: 2221/3558.
- (b) permitted nuclei, **Frobenius** (u_demand = nucleus's own NF profile):
  **0 / 3558.** The demanding per-nucleus Frobenius-profile test admits ZERO
  nuclei.

**Interpretation (honest).** The scalar-LP test (2221) is weak — it only asks
for a feasible net trace. The **Frobenius test is the real selector** (does the
SDP reproduce the nucleus's own categorical normal form?) and it currently
admits **nothing**. So the canonical knot-assignment SDP, as presently
formulated, does NOT select real nuclei at the level that would derive K_w /
ν_SDP. The deuteron single-nucleus SDP (`deuteron_real_sdp.py`) separately shows
the Frobenius **Gram is indefinite at q₀** (neg-norm blocks (3,1,1,1),(2,2,1,1),
(1⁶)) and 2/6 encodings are ⚠ANSATZ — consistent with the 0/3558.

## The open R5 gap (per conj:canonical-knot-id-sdp) — do NOT launder
Closing this requires (all open):
1. **Finitude of the NF candidate set** — bound the Gröbner–Shirshov normal-form
   candidates per H_{3A}(q₀) so the SDP search is over a finite, enumerable set.
2. **Rigorous SDP search bounds** — certify the global minimizer (not a local
   feasible point), handling the indefinite Gram (bar-involution fold / PSD
   restriction to the physical cone).
3. **Structural identification of K(𝔥) ∈ H_{3A}(q₀)** — the binding operator,
   beyond the 3 volume-matched atoms (6₂/8₁₁/L6a4).

Anti-fit: hand-assigning knots to atoms by volume-match to hit B_AME is a FIT,
not a derivation — must be labeled and NOT wired as canonical. The 1-loop
torsion route (bean qou-r307) does NOT supply ν_SDP (refuted). ν_SDP as a
spherical-partition-algebra dimension (bean qou-0rp2) is the remaining
derivational candidate for piece (3).

## Cheap next step
Fix the AME path in `all_nuclides_sdp_admissibility.py` (parents[2]→ resolve
computations/data), and add a Frobenius-feasibility diagnostic that reports WHY
each nucleus fails (which constraint / which neg-norm block) — turns "0/3558"
into an actionable per-constraint breakdown.

## DIAGNOSTIC (2026-08-02) — the 0/3558 is an OVER-DETERMINATION artifact, not an obstruction
`computations/probes/frobenius_admissibility_diagnostic.py` decomposes the failure:

- **Gram spectrum** (H_3 NF basis [γ,σ₀,σ₁,L₊,L₋,e⁻]): [−0.855, 0.102, 0.855,
  0.855, 0.855, 3.477] — rank 6, **exactly 1 neg-norm block** (indefinite but
  invertible).
- **nf ∈ range(G)** for every light nucleus (residual ~1e-15) — the Frobenius
  demand is reachable; the neg-norm block is NOT what blocks light nuclei.
- **Root cause = over-determination.** The Frobenius LP imposes 7 equalities
  (1 net `1ᵀx=A` + 6 Frobenius `Gx=nf`) on 6 unknowns. `Gx=nf` already fixes
  x=G⁻¹nf uniquely, so its implied net is `1ᵀG⁻¹nf` — which is O(1) (p 0.596,
  2H 0.437, 4He 0.802, 12C 2.34), NOT the mass number A. The net row `1ᵀx=A` is
  therefore inconsistent with the Frobenius rows for EVERY nucleus ⇒ 0/3558.
- **Heavy nuclei (A≳50)**: separate cause — f64 `build_atom_nf` overflows (56Fe
  nf ~1e16), the known mpfr-needed infra limit.

**Reframing (honest, scope-limited).** The 0/3558 is a **test-formulation
artifact**: the admissibility LP is over-determined by an inconsistent net
normalization (`1ᵀx=A` vs the NF-implied `1ᵀG⁻¹nf`). It is NOT evidence the
Gram/knot machinery can't select operators. The fix targets the net constraint
(drop the redundant row, or use the consistent net), NOT the Gram. **This does
NOT derive ν_SDP** — it removes a spurious "obstruction" reading and re-points
the open R5 work at the net normalization + the mpfr overflow for heavy A.

## 2026-09-08 — re-activated by owner ruling (bean qou-ales): word selection goes through γγ production + the confinement SDP at q₀, no census. The 'cheap next step' (fix the net-row over-determination, per-constraint diagnostic) is now on the critical path.


## 2026-09-08 (qou-ales step 2) — the cheap fix was run, and D changed the diagnosis
computations/probes/frobenius_admissibility_net_row_probe.py (proton pin, 60 dps, no AME): under convention D the H3 Gram is rank 5 (radical = q-antisymmetriser v) and 1'v = 0.0902 != 0, so the net row 1'x=A is ALWAYS satisfiable along the kernel whenever Gx=nf is — the over-determination above (a rank-6, convention-C diagnosis) is gone. The obstruction is now <v, nf(W)> = eps(W), the alternating character of the word, a product of nonzero factors for every crossing type (S: -1/q, I: -q, C: -1/q+D_PN, gamma-gamma vertex: 1 exactly, Lean altChar_eq_one). Result: 0/4238 candidate words survive for p,n,2H,pp,nn,3H,3He,4He. Scope-(a): about the Gx=nf demand formulation, NOT the PSD confinement SDP. Audit: docs/audits/2026-09-08-gamma-gamma-word-selection-step1.md.


## Progress Update (PR #8344)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`291dd36ab34a42866efb444b586e05f0b621971e` -> `38f4a86a95df28f43dea57e331b0e3b812f7f526`) in PR #8344.


## 2026-11-20 — PR #8564: the over-determination fix, in Lean
The 2026-08-02 net-row diagnosis was convention C. Under D (net_row_probe, on main: rank 5, 1'v = 0.0902) Lean now states both halves: net_row_satisfiable (once G x0 = nf, the net row is met along the radical) and demand_infeasible_of_radical (G x = nf fails iff <v, nf> != 0). chi_(1^3)(V^k) = 1 for k = 0..10, so gammaGamma_demand_infeasible_of_pairing_eq_altChar (pairing = altChar carried as a hypothesis, measured) shows the G x = nf test admits NO gamma-gamma word, ever. That is a property of the test. The owner-ruled admissibility is reading 3; run per nucleus on #8564. Bean stays in-progress: items 1-3 of the R5 gap (finitude, SDP search bounds, K(H) identification) are not touched.
