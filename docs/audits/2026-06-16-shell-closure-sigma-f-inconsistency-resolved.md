# shell-closure-stability — σ_F monotone-vs-local-max inconsistency (RESOLVED)

**Date:** 2026-06-16
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348)
**Class:** content correction (owner-authorised "please resolve") + diagnostic.

## The inconsistency

[`prop:shell-closure-stability`](../../content/quantum-observable-universe/particle-interactions/shell-closure-stability.md)
asserted two things about the **same** function `σ_F(P^Z, q) = n_target·y₀*`:

- **claim 1** — σ_F is *monotone non-decreasing* in Z;
- **claim 2** — σ_F attains a *strict local maximum* at noble-gas
  Z ∈ {2,10,18,36,54,86}.

A monotone non-decreasing function has **no strict interior local maximum**, so
claims 1 and 2 are mutually contradictory. The
[interprets remark](../../content/quantum-observable-universe/particle-interactions/shell-closure-stability-interprets.md)
papered over it two ways: it called σ_F *"piecewise-monotone with local maxima"*
(contradicting claim 1's "non-decreasing"), and it *defined* the ionisation
energy `I₁(Z) = tr_M(P^Z) − tr_M(P^{Z-1}) − tr_M(e⁻)` (a marginal trace-gap)
then asserted `I₁ ∝ σ_F` (a monotone total) — which can't both hold.

Corpus-grep (docs/audits, content, coordination) returned no prior note of this;
the QA sidecar even records the Lean as "matching the three narrative claims."

## Why the Lean didn't catch it

Two Lean files carry the prop:

- The **library** version
  [`QOU/BraidKnot/ShellClosureStability.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ShellClosureStability.lean)
  (conditional-class: `HasFrobeniusStability`, `ShellClosureMonotone`,
  `shell_closure_monotone`, `shell_closure_noble_multiplicity`,
  `shell_closure_terminality`) formalises **only** claim 1 (`monotone`,
  `σ_F_prev ≤ σ_F`) and claim 2's **multiplicity** part (`μ ≥ 2`). There is
  **no theorem asserting a local maximum of σ_F** — so the *theorems* are
  internally consistent; only the docstring prose echoed the contradiction.
- The **content-block sibling**
  [`particle-interactions/shell-closure-stability.lean`](../../content/quantum-observable-universe/particle-interactions/shell-closure-stability.lean)
  is a **vacuous model** (`frobeniusStability := fun _ q => 0*q`,
  `mu := fun _ _ => 2`), so its theorems are trivial (`0 ≥ 0`, `2 ≥ 2`) and the
  contradiction is invisible. (This sibling **shadows** the real library decl —
  a separate `no-shadowing-stubs` issue, flagged as follow-up below.)

So the inconsistency lived **purely in the narrative prose** + the vacuous-model
docstring; the substantive Lean theorems were already the consistent pair
(monotone + μ≥2).

## The resolution (applied)

σ_F (the cumulative dual objective) **is** monotone (claim 1 — proven by
SDP-relaxation, confirmed numerically in
[`electron_sigma_f_chain.py`](../../computations/electron_sigma_f_chain.py),
gap ≈ 1e-9). The quantity that **peaks** at the noble gases is the **marginal
increment**

$$
  \Delta\sigma_F(Z) = \sigma_F(P^{(Z)}) - \sigma_F(P^{(Z-1)}) = I_1(Z),
$$

i.e. the ionisation energy — together with the multiplicity μ ≥ 2. Edits:

| file | fix |
|---|---|
| `shell-closure-stability.md` | claim 2 → "the **marginal gain** Δσ_F = I₁ attains a strict local max; σ_F itself is monotone (no interior max)"; claim-2 proof's "establishing the local maximum" → spectral-gap jump of Δσ_F; ionisation corollary → `I₁ = Δσ_F` (not ∝ σ_F), with the alkali troughs Z=3,11,19,… |
| `shell-closure-stability-interprets.md` | "piecewise-monotone σ_F" → "σ_F monotone, Δσ_F=I₁ peaks"; "I₁ ∝ σ_F" → "I₁ = Δσ_F" |
| both `*.lean` docstrings | same "non-decreasing **and** local maxima of σ_F" → "monotone σ_F; marginal Δσ_F=I₁ peaks" |

No theorem changed (the Lean theorems were already the consistent pair); no
`uses[]`/label/kind/schema change — prose + docstring only.

## Demonstration

[`electron_sigma_f_marginal.py`](../../computations/electron_sigma_f_marginal.py):

- **(a)** input the 2n²/Madelung capacities {2,8,8,18,18,32} → σ_F monotone, and
  Δσ_F = I₁ has local maxima exactly at {2,10,18,36,54,86} — the noble gases.
  **But circular**: the closures *are* the capacities put in.
- **(b)** the *actual* categorical transfer matrix `T_γe` is **2×2** (eigenvalues
  λ_± = 1.1073, −0.9027; `shell-structure-eigenvalues`), so each shell power gives
  a **2-fold** eigenspace → capacity 2 per shell → closures at {2,4,6,…}, **not**
  the periodic table. **T_γe does not produce 2n².**

## Follow-ups (open, flagged — not fixed here)

1. **Emergent peaks need a 2n² derivation.** Reproducing σ_F/Δσ_F peaks at the
   noble gases requires the 2n² shell capacities, which are an **input**
   (`prop:noble-gas-characterization`, `S_i = 2n²·T_{2,3}`), not derived from the
   2×2 `T_γe`. Until 2n² is derived categorically, any peak-reproducing level-6
   cost-operator model is **circular**. This is the genuine open problem behind
   the "level-6 cost-operator cut."
2. **Shadowing vacuous stub.** `particle-interactions/shell-closure-stability.lean`
   (σ_F≡0) shadows the real `BraidKnot/ShellClosureStability.lean` per the
   `lean.ref` sibling-first resolution → the prop's pointed-to formalisation is
   vacuous. Align per the STRICT `no-shadowing-stubs` rule (2026-06-14) in a
   separate change.
