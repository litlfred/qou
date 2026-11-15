# Results: option 1 rescue probe

Pre-registration: [`preregistration.md`](preregistration.md), commit `595351ba20a`, pushed before computing.
Producer `h2_option1_rescue_probe.py`, witness `h2-option1-rescue.witness.json`, 2/2 checks. mpmath 40 dps,
convention D, proton pin. Run time 17 s.

## Outcome (iii): no hydrogen atom in the family

| a (p–e letter σ₂^a) | failing levels | most negative block at level 6 |
|---|---|---|
| −3 | 4, 5, 6 | (3,3) = −0.7053 |
| −2 | 6 | (3,3) = −0.3150 |
| −1 (corpus letter) | 4, 5, 6 | (3,3) = −0.7712 |
| 0 (control) | 6 | (3,3) = −0.4762 |
| +1 | 5, 6 | (3,3) = −0.8707 |
| +2 | 6 | (3,3) = −0.6583 |
| +3 | 6 | (3,3) = −1.0083 |

No power of the p–e letter makes the hydrogen atom V³ · σ₂^a · σ₀³σ₁ pass reading 3. Stage 2 therefore
had nothing to run.

- **A0** (control a = 0 reproduces the closed form −0.31373335326276292589): pass.
- **J1** (a single junction letter σ₅⁻¹ leaves the level-6 ratio unchanged, as derived): pass to 1e-18.

## Reading

Under option 1 (γγ hadronic only, positivity everywhere), the trefoil electron σ₀³σ₁ admits no hydrogen
atom with nucleon V³ and any single p–e letter power |a| ≤ 3, and no single junction letter can repair level 6.
Scope (a): this family only. Not tested: other nucleon words, multi-letter p–e insertions, a 2-strand
trefoil σ₀³.
