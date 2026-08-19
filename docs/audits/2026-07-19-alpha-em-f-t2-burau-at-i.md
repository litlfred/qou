# α_EM F-construction T2 — Burau at the degenerate locus (2026-07-19)

**Bean:** `qou-yuff` (T2) of milestone `qou-a46k`. Upstream: T1 merged
([#4039](https://github.com/litlfred/qou/pull/4039) — cover structure, (3,1)
derived). Literature now in `library/` (owner-delivered):
`mcmullen-braids-hodge-2013.pdf`, `deligne-mostow-1986.pdf`,
`squier-burau-unitary-1984.pdf`, `gambaudo-ghys-braids-signatures-2005.pdf`.

**Probe:** [`computations/alpha_em/alpha_em_f_t2_burau_at_i_probe.py`](../../computations/alpha_em/alpha_em_f_t2_burau_at_i_probe.py)
→ [`alpha-em-f-t2-burau-at-i.witness.json`](../../computations/alpha_em/alpha-em-f-t2-burau-at-i.witness.json)
— 4/4 PASS, sympy-exact.

**Scope guard (STRICT):** local model only (disk around the two branch
points); global monodromy is T3/T5; no fit; nothing wired; `1/(8π)` stays
phase-4.

## Why this was the kill-test

If the cover's local monodromy at the deck character had been *semisimple*
at the degenerate locus, the McMullen route could not reproduce the
framework's Jordan-block H₂(i) module (#3992) and the F-construction would
be dead. It is not — the specializations line up exactly.

## Results

1. **Parameter dictionary.** Burau eigenvalues {1, −q_B} vs §7a Hecke
   {q_H, −q_H⁻¹} force `q_B = q_H⁻²`. At the degenerate locus `q_H = i`:
   `q_B = −1` — which is simultaneously (a) the Burau **integral**
   specialization, (b) the **Gambaudo–Ghys signature-jump locus**, and (c)
   `χ(deck)²` for the T1 deck multiplier χ = i (the half-twist squares to
   the local full twist). Three independent readings of one point.
2. **Jordan structure.** `σ_B(−1) = [[2,−1],[1,0]]`: char poly `(λ−1)²`,
   `σ_B ≠ 1`, `(σ_B−1)² = 0` — the local monodromy is genuinely
   non-semisimple.
3. **Exact module match.** `σ_H := i·σ_B(−1)` satisfies the §7a Hecke
   relation at q_H = i and is **explicitly GL₂(ℂ)-conjugate** to the
   `VertexLocalTauModel` block `!![i,1;0,i]` (conjugating matrix computed,
   `S·P = P·J`, det P ≠ 0). The cover's local monodromy module **is** the
   framework's H₂(i) module.
4. **ρ-partner.** Entrywise conjugation sends σ_H to a `(σ+i)² = 0`
   generator — `rho_carries_module` (#3992) reproduced on the monodromy
   side.

## Plan state (milestone `qou-a46k`)

```
T1 cover structure                       MERGED #4039
T2 local monodromy = H₂(i) module        THIS — kill-test passed
T3 ρ-equivariance globally (CW conj)     next
T4 weight-value transport (¾,¼)          open
T5 assembly + F = framework-τ residual   open
```
