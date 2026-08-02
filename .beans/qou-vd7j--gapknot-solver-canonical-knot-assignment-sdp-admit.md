---
# qou-vd7j
title: 'GAP(knot-solver): canonical knot-assignment SDP admits 0/3558 at Frobenius level — open R5 gap (finitude/search-bounds/K(H) structural id)'
status: todo
type: task
created_at: 2026-08-02T13:56:51Z
updated_at: 2026-08-02T13:56:51Z
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
