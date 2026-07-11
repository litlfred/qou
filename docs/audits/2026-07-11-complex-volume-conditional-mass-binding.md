# Conditional mass & binding via the complex volume conjecture

**Date:** 2026-07-11 · **Branch:** `claude/complex-volume-conjecture-wiring-2026-07-11` ·
**Tier:** conditional-formalization structure (scope-(a); anti-laundering respected).

Answers the owner questions: *do we have a proper formulation of the complex
volume conjecture (or do we need AJ)? can we use it for conditional mass and
binding?* Short: **proper formulation = the deformed complex volume conjecture
(AJ not required for the leading observables); mass is conditionally rigorous
(indeed the volumes are proved), binding needs one more open map.**

## Proper formulation — the deformed complex volume conjecture (not AJ)

- The object is the **generalized/parametrized complex volume conjecture**
  (Gukov 2003; H. Murakami): `J_N(K; e^{(2πi+u)/N}) → 𝔙(u) = Vol(u) + i·CS(u)`,
  the complex volume of the `u`-deformed knot (`u` = log meridian holonomy). For
  **4₁ it is a theorem** (Ohtsuki 2016 asymptotic expansion; Murakami–Yokota for
  the deformation), and `𝔙(u)` is **explicitly computable** via Neumann–Zagier /
  the A-polynomial (the `(√3/2)|u|²sin 2φ` leading form,
  `qbeta_c3_barodd_gluing_newton_solve.py`).
- **AJ (Garoufalidis) is not required** for mass/binding: the generalized VC +
  A-polynomial NZ already gives `𝔙(u)`. AJ (the exact q-difference recurrence =
  quantized A-polynomial) is only needed for the **exact all-orders `c_k` tower**,
  not the leading `S`.

## The split — mass = Re 𝔙, binding = Im 𝔙

Matches the bar-even/bar-odd (mass/decay) split established earlier:

| observable | `𝔙` part | evaluated at | conditional on | status |
|---|---|---|---|---|
| **Mass** (`Vol(K)` input of `m=m_e·Vol·ρ/ℏ²`) | **Re 𝔙 = Vol** | **complete `u=0`** | **plain VC** | **PROVED** for the links used — 4₁ (m_μ), Borromean `Vol=8G` (m_p) |
| **Binding** (`S`, `c₃` bar-odd, `Q_β`) | **Im 𝔙 = CS** | **deformed `u=u(q₀)`** | **deformed VC + `u(q₀)` map** | deformed VC ✔ (4₁); **`u(q₀)` OPEN** |

- **Mass is conditionally rigorous — better, the volumes are *proved*.** Mass
  needs `Re 𝔙` at the *complete* structure `= Vol(K)`; **no deformation map**.
  The VC is a *theorem* for 4₁ and the Borromean rings, so the `Vol(K)` inputs are
  rigorous, not conjectural. The only conjectural piece is the *framework* map
  (`mass = m_e·Vol·ρ/ℏ²`), not the volumes.
- **Binding is not unlocked even granting the deformed VC.** `S = Im 𝔙` at
  `u=u(q₀)`; the deformed VC gives `𝔙(u)` (available for 4₁), but you still need
  the **substrate→deformation map `u(q₀)`** — the archimedean functor, the same
  open object every S-route hit this session. That is why **mass works** (`u=0`,
  no map) and **binding/`S` is stuck** (`u(q₀)` needed).

## What was formalized here (§3b-cond, honest)

1. **The dangling `conj:binding-qbeta-complex-volume` is fixed** — it was omitted
   from the content graph by a schema violation (`lean.ref` array vs `z.string()`),
   so its four `interprets`/`uses` referrers saw "label not found." It is the
   `S = Im 𝔙` block (`𝔙 = E₀·tr_M((Π_free−1)∘𝓜)`, `binding = Re 𝔙`, `Q_β = Im 𝔙`).
2. **`asymptotic_volume_of_vc`** (`algebraic-geometric-dilog-equivalence.lean`) —
   the explicit conditional: *VC saddle asymptotic → V* **and** *V = D(z(x))*
   (pole-cusp match) **⟹** the §2 Bloch–Wigner asymptotic. The two hypotheses
   carry the content (Ohtsuki for 4₁; the proved pole side + the cusp-holonomy
   conjecture); the composition is a limit-point substitution. This is the
   **rigorous-conditional wiring of the bar-even mass part** — not a proof of the
   VC, and it does **not** touch the bar-odd `S`.

## Bottom line for the owner's plan

- **Conditional mass:** yes — and the `Vol(K)` inputs are actually *proved*
  (VC theorem for 4₁, Borromean). Formalizable now as a clean rigorous-conditional.
- **Conditional binding / `S` (and odd higher `c_k`):** needs the deformed complex
  VC (available for 4₁) **plus** the open `u(q₀)` map — so it is **not** unlocked
  by assuming the VC. `u(q₀)` = the archimedean functor
  (`conj:algebraic-geometric-dilog-equivalence` deformation content) remains the
  single genuinely-open object.

## Cross-references
- `conj:binding-qbeta-complex-volume` (fixed): [`binding-qbeta-complex-volume.ts`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.ts)
- Kashaev grounding: [`qbeta_c3_kashaev_invariant_grounding.py`](../../computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py)
- Provability triage: [`2026-07-11-algebraic-geometric-dilog-provability.md`](2026-07-11-algebraic-geometric-dilog-provability.md)
- AGENTS.md §"Axiomatization is NOT a Proof"; §3b.
