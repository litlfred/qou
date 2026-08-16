---
# qou-cds1
title: 'S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved'
status: todo
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T13:22:34Z
---

Parent: `qou-cdx1`. **The largest science item in the ruling.** Supersedes the
`disputed` outcome of `qou-b3nk`.

## What moves (registry §9g, probe `qbeta-c3-ladder-trace-convention-sensitivity`, 9/9)

| fact | C frame | D re-extraction | consequence |
|---|---|---|---|
| `c₃` (proton / muon) | −2.06934258 / −2.02020024 | **−974.43 / −974.38** | every ≈−2 value-level fact is C-conditional |
| anchor swing | 0.0491423 | 0.0493990 (ratio 1.0052) | REFUTED-as-real-q **survives** |
| implied empirical `c₂` | −1.0176 | **−9.299** | `c₂ = −1` is a C-frame statement |
| N2/N1 residual ratio | 0.017 (58× rung gain) | 0.89 (**no convergence**) | rung convergence is C-frame only |
| bar parity of `z` | `bar(z_C) = z_C` | `bar(z_D) = q⁻⁴·z_D` | KC13's prune is C-scoped |

**C-conditional downstream, all named in §9g:** (H1) `c₃^even = −Vol(4₁)`,
`[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`.

## The load-bearing constraint — this is NOT a z-swap

`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free, PR #5111): **any**
faithful normalised Markov trace at the ladder's `z_C` carries `y_(1³) ≠ 0`, for
**every** substrate `s = √q > 1` (the coincidence locus `s⁷+s⁵ = s⁴+1` factors
as `(s−1)(s⁶+s⁵+2s⁴+s³+s²+s+1)` and is empty there).

So *"keep the C-frame ladder"* and *"the two-row forcing applies here"* are
**mutually exclusive**. Under the ruling the decay trace is `z_D` — and **the
existing ladder is not that trace.** The ladder must be **re-derived**, not
re-evaluated.

**`c₃ ≈ −974` is a sensitivity measurement, not a proposed value.** It is what
the *current extractor* returns when fed `z_D`. Do not wire it anywhere.

## Live C sites in the decay channel

- `computations/qbeta/qbeta_utils.py::markov_parameter` + `substrate_ladder_quantities`
  (`α = (z−1)h/2` at `z_C` feeds every committed `c_k` extraction)
- `computations/qbeta/qbeta_ck_sseries_exact_rational.py:20,248` — the KC21/KC22
  `D(ũ)`-ladder core. **Naming hazard:** the `D` there is KC21's bar-even ℚ(√3)
  ladder *function* `D`, **not** convention D. Those lines evaluate `z = √q/(q+1)`.
- `content/.../lean/QOU/QBeta/ZBarParity.lean:59-79` (KC13 bar-even `z`)

## Discipline

Formalize-first: before any wide numerical re-fit of the ladder, state the
structural constraint the D-frame ladder must satisfy and check whether it
prunes the class. A re-derivation that lands on a nice number by search is a
fit, not a derivation, and the anti-laundering rule applies unchanged.

## Red-team verdict (2026-08-16, adversarial audit — docs/audits/2026-08-16-ck-ladder-red-team.md)

BOTTOM LINE: the c_k ladder is convergence-framework PHYSICS wrapped around higher-coefficient NUMEROLOGY, and the corpus already separates them correctly.

Per-claim:
- c_2 = -1: symbolic-exact but the Lean is a ring tautology (1-b2h4 = 1-(bh2)^2); the N=2-factor identification is asserted in a docstring, not derived. Anchor-stable to 1e-50 (real). C-frame (implied empirical c2 under D = -9.299).
- c_3 = -2 = J_Hopf(q=1): FITTED/near-match. Extracted by inverting the single Q_beta anchor; ~2 reliable digits; swings 2.98% cross-anchor (15000x its rigidity); REFUTED as real-q. The '=-2' is a 1-2 digit shadow coincidence 5 eps-orders off the ladder order.
- c_k>=4: FITTED/noise. c_4 vanishes when c_3 extracted exactly (normalisation artifact); zero reliable digits at k>=4; c_6/c_7 imposed in extraction (self-consistency); c_8 pattern breaks (wrong sign).
- KEY Q: series convergence is REAL (radius=u_substrate, kappa=0, KC22 Lean); N(eps) 'derivation' only holds for O(1) coeffs which c_k>=3 are NOT; the N=4->N=5 non-monotonicity is a fit tell the framing itself flags. Production wires c_2 ONLY -- the fit was caught and never shipped.
- C->D: does NOT survive. Ladder is z_C end-to-end (qbeta_utils.py:124). Under D c_3->-974, convergence vanishes, and decayLadder_zC_threeRow_ne_zero PROVES it's not a z-swap (C ladder trace and D two-row trace mutually exclusive). Honest status: UNKNOWN pending D re-derivation.
- (H1) c3^even = -Vol(4_1): NOT derived -- defined residual S_leak:=c3+Vol(4_1); not determinable from anchor data; '0.48%' agreement is 0.031 sigma = no evidence.

DOF-vs-precision: ladder fits ONE experimental scalar (Q_beta) with unboundedly many residual-absorbing coefficients; only c_3 carries signal (~2 digits) and those swing 3% across anchors. No high-precision identification exists.

Do NOT: re-quote any C-frame c_k as a D result; resurrect c_3=-2=J_Hopf as a derivation (that is flip-flop #5).
