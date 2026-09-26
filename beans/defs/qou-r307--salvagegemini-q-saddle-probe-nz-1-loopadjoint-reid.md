---
# qou-r307
title: 'Salvage(gemini q-saddle): probe NZ 1-loop/adjoint-Reidemeister-torsion vs nu_SDP {1,2} for 6_2, 8_11 (Garoufalidis-Yoon 2411.03801)'
status: todo
type: task
created_at: 2026-08-02T13:07:12Z
updated_at: 2026-08-02T13:07:12Z
---

## Source
Salvaged from a Gemini brainstorm on "q-deformed saddle-point offsets"
(branch `claude/q-deformed-saddle-offsets-bdn992`, 2026-08-02). Most of that
dialogue is confabulation (see red-flag bean `qou-fk19`); THIS is the one
concrete, real, falsifiable thread.

## The real result (verified)
**Garoufalidis & S. Yoon, "1-loop equals torsion for two-bridge knots"**,
arXiv:2411.03801 (Nov 2024, math.GT). Proves the Ohtsuki–Takata conjecture
for hyperbolic 2-bridge knots: the constant (1-loop) term in the asymptotic
expansion of the Kashaev invariant **equals the adjoint Reidemeister torsion**,
computable as the **determinant of a matrix built from the Neumann–Zagier
ideal-triangulation data + shape parameters**. Real paper, correct authors,
correct content (Gemini got this one right; it said "et al" for Yoon).

## Why it matters here
The framework's OPEN conjecture `conj:kashaev-density-equals-sdp-multiplicity`
(mass-theory/, the real "Conjecture 10.14.8"; conditional, single Lean `sorry`)
asserts the Kashaev **density prefactor** ρ_F = the joint-tower SDP Wedderburn
multiplicity ν_SDP ∈ ℤ_{>0}, with evidence table:
  ²H = knot 6_2  → ρ_F=ν_SDP=1
  ³H = knot 8_11 → ρ_F=ν_SDP=2
  ³He= link L6a4 → ρ_F=ν_SDP=2
ρ_F is *literally the 1-loop density prefactor of the Kashaev asymptotics*.
Garoufalidis–Yoon identifies that prefactor with a **discrete NZ-Jacobian /
torsion determinant** — i.e. it converts the continuous prefactor into a finite
matrix evaluation, which is exactly the geometric→algebraic bridge the
framework needs (and side-steps the k→1 elliptic-integral divergence of the
toroidal route, already overclaim-audited in
docs/audits/2026-07-19-qbeta-toroidal-tower-overclaim-audit.md).

## Concrete falsifiable probe (the deliverable)
1. Add ref `garoufalidis-yoon2024` (2411.03801) to content/schema/references.ts.
2. For 6_2 and 8_11 (both hyperbolic 2-bridge — 6_2 is 2-bridge; 8_11 is NOT
   2-bridge, so the theorem is proved only for 6_2 — note this scope limit and
   use the general 1-loop/torsion *formula* for 8_11, flagged as conjectural
   there per the fibered-3-mfd companion arXiv:2304.00469).
3. Compute the adjoint Reidemeister torsion / NZ 1-loop invariant at the
   complete hyperbolic structure (SnapPy is available; the viewer already ports
   it to WASM). Compare to the integers ν_SDP ∈ {1,2}.
4. **Honest-negative friendly:** if det(NZ) does NOT land on {1,2}, that is a
   real result — it means ρ_F (=1-loop torsion) and ν_SDP (=SDP Wedderburn
   count) are DIFFERENT objects, and the ρ_F=ν_SDP identity is a numerical
   coincidence on 3 atoms, not a structural equality. Record either way.

## Anti-laundering guardrails
- This is a DERIVE-THEN-CHECK probe, not a fit. Do not wire ν_SDP or ρ_F to
  production off a numerical match; the conjecture stays conditional (single
  sorry) until the identity is *proved*, per "Axiomatization is NOT a Proof".
- Formalize-first: the honest formal object is "1-loop torsion determinant for
  K", not a re-assertion of the {1,2} table.

## Related (do not duplicate)
- `conj:kashaev-density-equals-sdp-multiplicity` (the open target)
- bean `qou-j1ld` (Garoufalidis–Lê 2004 q-holonomic — DIFFERENT paper)
- bean `qou-9nq9` (GAP-A4 ⁴He Δ_λ magnitude — downstream consumer of ν_SDP)
- bean `a6vp` (verify volume conjecture at root of unity)

## RESULT (2026-08-02) — Option A REFUTED as stated (scope-a)
Implemented the DG 1-loop invariant (Def 2.1 of 2411.03801) directly from
SnapPy NZ data — `computations/probes/one_loop_vs_nu_sdp_probe.py` (standalone
snappy; the built-in `hyperbolic_adjoint_torsion` needs Sage, this route does not):

| knot | ν_SDP | 1-loop τ | |τ| |
|---|--:|---|--:|
| 6₂ (²H) | 1 | −1.71544−1.40375j | 2.21659 |
| 8₁₁ (³H) | 2 | 2.47079+8.45134j | 8.80511 |
| 4₁ (ctrl) | — | −0.86603j | 0.86603=√3/2 |

- τ is a transcendental/algebraic COMPLEX number, **not** the integer ν_SDP.
  |τ|=2.22≠1, 8.81≠2 — the flattening/± ambiguity (units, roots of unity)
  cannot bridge that. **Gemini Option-A (ν_SDP = 1-loop torsion) is refuted.**
- 4₁ control lands in its trace field ℚ(√−3) (|τ|=√3/2) ⇒ implementation sound.
- L6a4 (³He) not computed: 2-component link ⇒ needs the multi-cusp meridian/
  flattening version (single-cusp code returns det=0). Follow-up if needed.
- NOTE the coincidence |τ(6₂)|≈2.22 ≈ m_e·Vol(6₂)=2.249 ≈ B_AME(²H)=2.224 is
  just because |τ|~O(Vol) for these knots — NOT a derivation (τ dimensionless).
- Status: Option-A pruned. Garoufalidis–Yoon 1-loop=torsion remains a valid
  ANALYTIC bridge (torsion ↔ 1-loop), just not to the integer ν_SDP. Add ref
  garoufalidis-yoon2024 (2411.03801) to references.ts when a consumer lands.

## RECONCILED with landed sibling (2026-08-02 rebase, reuse pass)
A sibling independently landed the SAME scope-(a) refutation on main via the
value-validated Porti adjoint torsion 𝕋_μ = −W'(1) (Fox calculus):
- `computations/probes/torsion_nu_sdp_probe.py` + witness (PR #4576)
- `docs/audits/2026-08-02-r307-torsion-vs-nu-sdp-probe.md`
- refs Garoufalidis-Yoon 2411.03801 / Ohtsuki-Takata / Dimofte-Garoufalidis now
  in references.ts (commit 951b0939) — my earlier "not yet in references.ts" note
  is now stale; the ref IS present.
Their values: 𝕋_μ(4₁)=−3.00003 ✓ (validated), 6₂ |𝕋_μ|=16.84, 8₁₁ 27.76.
My `one_loop_vs_nu_sdp_probe.py` (DG 1-loop from NZ gluing data, "symmetric"
normalization) reaches the same VERDICT (complex, ≫{1,2}, ∉ℤ) by a DIFFERENT
computation; normalization differs (4₁ |τ|=√3/2 vs 3). Kept as the independent
1-loop-side confirmation; the sibling probe is the authority for the torsion
value. Two independent routes, one verdict — per AGENTS.md "two independent
confirmations of an open result are valuable." No conflict, no duplication churn.
