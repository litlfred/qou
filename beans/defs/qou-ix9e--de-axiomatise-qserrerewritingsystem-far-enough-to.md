---
# qou-ix9e
title: De-axiomatise qSerreRewritingSystem far enough to prove its rules monic, discharging the hlc left hanging on ugb_pbw_corollary
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T10:15:22Z
updated_at: 2026-11-18T10:37:00Z
parent: qou-1o8n
---


---

## 2026-08-10 — done, and it turned up a second false axiom

`qSerreRewritingSystem` is a **definition**. The five q-Serre rules are built
explicitly (`qSerreRule1 … qSerreRule5`), each leading monomial is **proved**
(`qSerre_lm_1 … qSerre_lm_5`), and `qSerre_rules_monic` discharges the `hlc`
that qou-lzoo deliberately left hanging on `ugb_pbw_corollary`. That was the
task; two defects fell out of it.

### Defect 1 — the generator ranking mis-oriented rule 3

`SU2Gen.rank` had `K = 2 < E_+ = 3`, so `[K,E_+] < [E_+,K]` and rule 3
(`K·E_+ → q²E_+·K`) had leading monomial `[E_+,K]` — its own right-hand side.
The system rewrote in the direction opposite to its docstring.

The rules impose `rank K > rank E_+ > rank E_-` (`K_inv` unconstrained).
Corrected to `E_- < K_inv < E_+ < K`. The five `qSerre_lm_*` theorems now check
the orientation instead of asserting it, which is why the bug surfaced at all.

### Defect 2 — `pbw_monomials_are_normal_forms` was FALSE

Refuted, sorry-free, no framework axiom:
`pbw_monomials_are_not_all_normal_forms`. The witness is `⟨a,b₊,b₋,c⟩ =
⟨0,1,1,0⟩`, whose word is `[K,K⁻¹]` — rule 1's leading monomial exactly, so it
is reducible.

`PBWMonomial.toMonomial` lays letters out as `E_+^a K^{b₊} K⁻¹^{b₋} E_-^c`, and
**three** of its joins are leading monomials:

| join | when | lm of |
|---|---|---|
| `[K,K⁻¹]` | `b₊ ≥ 1 ∧ b₋ ≥ 1` | rule 1 |
| `[K,E_-]` | `b₊ ≥ 1 ∧ c ≥ 1` | rule 4 |
| `[E_+,E_-]` | `a ≥ 1 ∧ b₊ = b₋ = 0 ∧ c ≥ 1` | rule 5 |

The axiom's own justification is where it went wrong: it argued the word has no
forbidden subword "because generators appear in canonical order with each block
homogeneous" — but homogeneity *within* blocks says nothing about the joins
*between* them.

Reading the orientations off the rules, reduction moves `E_-` left past `E_+`
and moves `K` right past both, so the normal words are `E_-^c E_+^a K^b`, with
`K` and `K⁻¹` never mixed. The letter order in `PBWMonomial` is simply not this
system's normal-form order.

`ugb_pbw_corollary` no longer claims that half. It states existence + uniqueness
of normal forms, both discharged, and says in its docstring why the PBW half was
withdrawn. Establishing normality for the corrected shape is the genuine
remaining content of Bokut–Malcolmson Thm 3.2 — open.

### Live risk, recorded rather than hidden

`qSerre_is_gs_basis` is **now falsifiable and unverified**. While the system was
opaque the axiom said nothing checkable; now it is a concrete claim about five
explicit rules, and the six S-polynomial computations have **not** been carried
out against this construction. Defect 2 is the precedent for taking that
seriously — that axiom was refuted the moment it became checkable. Discharging
the six computations is the next step. Noted on the axiom itself.

### Verification

All 28 UGB modules `lean`-direct exit 0. `#print axioms`:
`qSerre_rules_monic`, `qSerre_lm_3`, `pbw_monomials_are_not_all_normal_forms`
each `[propext, Classical.choice, Quot.sound]` — no framework axiom.
`ugb_pbw_corollary` + `local_confluence`, `qSerre_is_gs_basis`,
`reduction_well_founded`.

- Round 79 (`lane-e667`): Formalized `qou-ix9e`, `qou-lncp`, `qou-ulfe`, `qou-znz5`, `qou-pso0` in `QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness` with 80-dps `mpmath` 2-commit witness stamp (`0e73e1d84b41af22cbe0a7adb5792bfd6ad829c7` -> `f1e0c5f0a53084f645586bcab55a711f50415015`, `scriptHash=6f730a2d7a28822fd4184de185390b3fa00ae1e8c3c649430e85284ae55ef0da`) in PR `litlfred/qou#8430` (`status: in-progress`).
