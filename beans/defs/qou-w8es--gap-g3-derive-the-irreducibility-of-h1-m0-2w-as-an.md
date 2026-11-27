---
# qou-w8es
title: 'GAP G3: derive the irreducibility of H1(M0) = 2W as an A5-representation (chi = -6 chain)'
status: todo
type: task
priority: high
tags:
    - bring-foundations
    - research
    - open-derivation
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-22T21:59:12Z
parent: qou-6qbv
---
Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The gap was named in `docs/audits/2026-11-17-bring-foundations-trace-sites-and-genus-attack.md` §3 and had no bean.

**Statement.** H¹(M0) ⊗ ℂ = 2W with W an irreducible A5-representation is an input of the genus-4 chain (`hdim` / `hχ` in the Lean). Derive it from the QOU axioms.

**Known.**
- With H_W, the Lefschetz/RH enumeration (audit §3 table) gives g ∈ {4, 5}; S5 then gives 4.
- Without irreducibility, A5 admits g = 6, 9, 10, … (audit table).

**Candidate source named in the audit:** a "no proper invariant subsystem of periods" statement. The natural carrier is the Gauss–Manin system rank used in `prop:prolonged-periods-fixed-depth`, which currently reads rank 8 off Bring (circular).

**Open; do not close** (AGENTS.md §13a).

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Nothing landed. The only named carrier (Gauss–Manin rank 8 in prop:prolonged-periods-fixed-depth) is still read off Bring, so it is circular as the bean says. Open; stays open.

## 2026-11-22 tracker hygiene (qou-w3yy, owner-approved)

Parent set to `qou-6qbv`: old parent `qou-qhcr` is not an epic/milestone/feature; re-pointed to its nearest legal ancestor. No change to this bean's scope or status.

## 2026-11-27 — χ = −6 chain thread (session_01VQDpPbyS5NspZ1YQT2xsE6, PR #9726)

PR #9726: G3 is no longer necessary for χ = −6 if the least-hyperbolic selection principle is adopted (`chi_le_neg_six_of_A5_map`: any hyperbolic A₅-map has χ ≤ −6, attained). G3 itself is unchanged and stays open.

## 2026-11-27 (χ = −6 chain thread, with the q-Bessel dictionary thread): G3 given genus 4, and why it is circular here
The q-Bessel thread (branch claude/bring-harmonics-exhaustive-2026-11-27, file `QOU/BringsSurface/BringSymmetryQuotientGenus.lean`, not pushed yet) derives H¹(B, ℂ) = 2·[2,1,1,1] as an S₅-rep, hence 2W with W irreducible 4-dim for A₅. Inputs: g = 4, an S₅-action, Riemann–Hurwitz quotient genera, Chevalley–Weil, the S₅ character table. **It starts from g = 4, so it cannot be used to derive the genus**: it confirms G3 on Bring, which the chain already reads off. As a step toward χ = −6 it is circular. For the χ = −6 chain the non-circular replacements for G3 are PR #9726 (least hyperbolic A₅-surface) and the S₅ least-genus arithmetic (next PR). Side finding filed as qou-efxy: H⁰(K) is std ⊗ sgn, not std. E⁴ splitting: quoted (Riera–Rodríguez), not derived. Stays open.
