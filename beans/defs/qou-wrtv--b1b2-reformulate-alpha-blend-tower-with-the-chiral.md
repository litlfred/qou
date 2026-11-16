---
# qou-wrtv
title: 'B1/B2: reformulate alpha_blend_tower with the chirality term H_A^2 Phi_3 and excise the fitted alpha*'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T00:31:29Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-3l2l
---

IMPLEMENTED (B1) AND MEASURED. The chirality term is real, exact, and does NOT
rescue the prediction — which refutes the premise B1 rested on.

## What was actually missing

alpha_blend_tower already had an alt CHANNEL (W_ALT * lam_alt), labelled in its
own docstring 'THIS IS THE CHIRALITY CHANNEL'. That is not the canonical term.
thm:wedderburn-mass-formula states

    m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*( Phi_1 - 2[3]_q*Phi_2 + h_A^2*Phi_3 )

    Phi_1 = sum_i ln| z*(M_i)_12 + (M_i)_22 |    standard block
    Phi_2 = sum_i ln| det M_i |                  sym x alt
    Phi_3 = sum_i ln| lambda^sym_i / lambda^alt_i |   sym / alt  = CHIRALITY

so Term 5 is h_A^2 times a SUM OF LOG-RATIOS, not a Wedderburn block added to a
weighted volume. An alt channel and the h_A^2*Phi_3 term are different objects.

## alpha != alpha*

The alpha in the canonical formula is m_e * 8G (G = Catalan) = 3.74445965994 MeV
— DERIVED, from CAL-1 and a pure constant. alpha* was the free blend parameter
of the superseded 2-term frame, fitted by root-finding against CODATA M_p, M_n.
Same glyph, different objects; the overloaded-symbol trap AGENTS.md names.

## Verified analytically, not just run

Every invariant has a closed form I derived by hand and matched to all digits:

    Phi_2 (both)     2*ln(1 + h^2/4)   0.021736    vs 0.02173457734
    Phi_3 proton     6*ln q            0.626053    vs 0.6260443219
    Phi_3 neutron    2*ln q            0.208684    vs 0.2086814406

Two structural results fall out. Phi_3 = w*ln q with INTEGER w (6 proton,
2 neutron) — the chirality invariant is an integer multiple of ln q. And Phi_2
is p/n-IDENTICAL because both chains carry exactly two (1,-h/2) factors while
every other factor contributes det = -1, so the -2[3]_q*Phi_2 term cancels
identically in any p-n difference.

## The negative

Parameter-free p-n splitting, alpha = m_e*8G, no fitting anywhere:

    predicted   corr(n) - corr(p) = -0.62398159878 MeV
    CODATA      m_n - m_p         = +1.29333236   MeV
                                     err -148.2 %, WRONG SIGN

    without the chirality term:    -0.5557 MeV,  err -143.0 %

So h_A^2*Phi_3 moves the splitting by -0.068 MeV — the WRONG WAY, and the sign
was already wrong without it.

## What this refutes

canonicalization-review.md §3.1 says alpha* 'is absorbing what the chirality
term H_A^2 Phi_3 should contribute'. Measured: it is not. Restoring that term
does not recover the p-n splitting, does not fix the sign, and makes the
magnitude marginally worse. B1's premise is refuted; B2 (excise alpha*) stands
on its own merits, since alpha* is a fit either way.

Scope-(a): this says the 2-term frame's deficit is NOT the chirality term. It
does not exclude chirality from the mass formula — the term is canonical, exact,
and integer-quantised. Whatever the nucleon channel is missing is something
else.

## 2026-11-16 — On-`main` Verification & `Q-3L2L-1 = 1` Cross-Link (`litlfred/qou#8141`)

- **Verified on `main`:**
  - The B1/B2 measurement above and the conditional per-loop assembly `folio/quantum-observable-universe/lean/QOU/Archimedean/PerLoopMeasureShadowAssembly.lean` (landed in `d68b998f91`, moved to `folio/` in `114b24ba5b`, `0` `sorry`) + `computations/alpha_em_b5_shadow_assembly_probe.py` (`computations/alpha-em-b5-shadow-assembly.witness.json`) are on `main`.
  - Cross-linked with the $(4,1)$ standard block Hoefsmit/Markov Gram and Schur reduction formalization in `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`qou-mxnu`, `qou-vbz4`, commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`).
- Kept at `status: in-progress` per owner governance.
