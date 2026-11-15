# Results: H₂ with a γγ electron

Pre-registration: [`preregistration.md`](preregistration.md), commit `e1e22ebfb1d`, pushed before computing.
Producer `h2_gg_electron_probe.py`, witness `h2-gg-electron.witness.json`, 2/2 checks (E0: reproduces the
`h2_gg_atom` V³/T_w0 rows to 1e-18; E1: χ_(3)(V^k) = 1). mpmath 40 dps, convention D, proton pin.
Run time 989 s, 224 rows.

## Verdicts (nucleon V³ and V⁶ give identical verdicts)

| electron | bare H₂ word, pe / ep | bonds passing every level (bare word passing) | outcome |
|---|---|---|---|
| V⁰ (control, no electron letters) | pass / pass | V³ at s = 4, 5 | (i), degenerate |
| V¹ | fail 6–9 / fail 6–10 | — | (ii) |
| V² | fail 6–8 / fail 6–7 | — | (ii) |
| **V³** | **pass / pass** | **V³ at s = 4, 5** | **(i)** |
| V⁴ | fail 6–9 / fail 6–10 | — | (ii) |
| V⁵ | fail 6 / fail 6 | — | (ii) |
| **V⁶** | **pass / pass** | **V³ at s = 4, 5** | **(i)** |
| V⁷ | fail 6–9 / fail 6–9 | — | (ii) |

Trace ratios of the passing V³ bonds: 0.9984–0.9985 in every (i) cell (reported, not used; ruling B).
In (ii) cells some bonds (V or V² at s = 4) pass every level although the bare word fails; by the
pre-registered rule they do not count, and they are listed in the witness.

## Reading

- The bare H₂ word passes exactly when the electron passes reading 3 on its own three strands
  (k ∈ {0, 3, 6}, the same set as for the nucleon). Whenever it passes, the bond letters that pass
  are exactly V³, at either site. No other bond passes in any (i) cell.
- So under the one rule on three strands, nucleon, electron and bond are all drawn from {V³, V⁶},
  and the bond is V³ in every case. That is the same word that selects the core.
- **Nucleon and electron are not distinguished.** With m = k = 3 they are the same word. V³ vs V⁶
  is the only difference the grammar allows, and the probe does not choose between them. Which
  power is "the electron" is an owner question.

## Scope

Scope (a): three-strand γγ words up to V⁷, owner-option-1 cell (no p–e letter, no junction
letter), bond letters up to V³, convention D at the proton pin.
