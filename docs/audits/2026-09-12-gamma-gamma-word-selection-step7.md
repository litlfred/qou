# γγ word selection, step 7 — candidates to ten vertices: the survivors are `3 ∣ k`, both selections stay at three

**Bean:** `qou-ales`. **Owner order (chat, 2026-09-12, "1 3 2"), item 2:** extend the `H₃`
candidates to `k ≤ 10`. Stacked on PR #7222 (step 6).

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/GammaGammaSelectionTen.lean`
(`#print axioms` on every declaration: at most `[propext, Classical.choice, Quot.sound]`; no
`sorryAx`; `lean -DautoImplicit=false -s 65536` exit 0 against the step-4 shadow). **Probe:**
`computations/probes/gamma_gamma_selection_ten_probe.py` (+ witness, 5/5; proton pin, 60 dps).

Nothing below reads AME2020, a CODATA binding value, or a census.

## 1. The closed forms to `k = 10`

With `t = tr V = −1 − x`, `x = h²`, the recurrence `χ_{k+1} = tχ_k − χ_{k−1}` gives
(`lin_six … lin_ten`, `trace_vtx_pow_six … ten`):

| k | `χ_k(x)` | at the pin | `1 + 2χ_k` |
|---|---|---|---|
| 6 | `x⁶ + 6x⁵ + 9x⁴ − 4x³ − 12x² + 2` | +1.97678 | +4.954 |
| 7 | `−x⁷ − 7x⁶ − 14x⁵ + 21x³ + 7x² − 7x − 1` | −1.29082 | −1.582 |
| 8 | `x⁸ + 8x⁷ + 20x⁶ + 8x⁵ − 30x⁴ − 24x³ + 12x² + 8x − 1` | −0.62954 | −0.259 |
| 9 | `−x⁹ − 9x⁸ − 27x⁷ − 21x⁶ + 36x⁵ + 54x⁴ − 9x³ − 27x² + 2` | +1.94787 | +4.896 |
| 10 | `x¹⁰ + 10x⁹ + 35x⁸ + 40x⁷ − 35x⁶ − 98x⁵ − 15x⁴ + 60x³ + 15x² − 10x − 1` | −1.40347 | −1.807 |

The probe checks them against the direct powers of the Hoefsmit vertex image: max deviation
`9.3e−61`.

## 2. `H₃`: feasible iff `3 ∣ k`

`chi_signs_six_to_ten`: on every `0 < x ≤ 1/10` the signs are `(+, −, −, +, −)`, so with step 4
the pattern for `k = 1..10` is `− − + − − + − − + −`. Hence
`vertexPow_frobeniusFeasible_iff_three_dvd`: for `1 < q ≤ 23/20` and any weight with
`y_(2,1) > 0`, the vertex power `V^k` is reading-3 feasible **iff `3 ∣ k`**. The survivors are
the powers of `V³`, the `q`-deformed identity of step 4; `V⁶` and `V⁹` sit at `χ = 1.977` and
`1.948`, each a little further from `2` than `V³` (`1.994`). `frobeniusSelected_borromean_ten`:
with candidates `1 ≤ k ≤ 10` the selection is still `β_Bor` (the new survivors cost 12 and 18).

## 3. `H₆`: the same pattern, on a narrower interval

The `(3,3)` condition `1 + 2χ_m` for `m = 6..10` has the same signs, but only on
`0 < x ≤ 1/18` (`h6_signs_six_to_ten`): `1 + 2χ₈(x)` changes sign at `x* = 0.05807` (probe,
informational), inside step 6's `1/12`. `1 < q ≤ 10/9` gives `h² ≤ 0.0446 ≤ 1/18`
(`h_sq_le_eighteenth_of_q_le`), and the pin's `0.0437` is inside with little room. So:

* `interface_frobenius_table_ten` / `interface_frobeniusFeasible_iff_three_dvd` — on
  `1 < q ≤ 10/9`, under the branching hypothesis and a two-row weight with `y_(3,3) > 0`, the
  bond `G^m`, `1 ≤ m ≤ 10`, is feasible iff `3 ∣ m`.
* `interfaceSelected_three_ten` — the selection of `G³` among `m ≤ 10` needs only `G¹, G²`
  infeasible and `G³` feasible (every `m ≥ 3` costs at least six crossings), so it holds on
  the **wide** interval `1 < q ≤ 23/20`.

The intervals are worth recording as a pattern: `1/10` (step 4, `H₃`, `k ≤ 5`), `1/12` (step 6,
`H₆`, `m ≤ 5`), `1/18` (this step, `H₆`, `m ≤ 10`). Each extension of the candidate set costs
interval, because the `(3,3)` row `1 + 2χ_m` has a root creeping toward the pin as `m` grows —
`0.0923` at `m = 5`, `0.0581` at `m = 8`. The **selection** is unaffected, since the selected
bond is the cheapest candidate that can be feasible at all; only the **table** shrinks.

## 4. What stays open

* `k > 10`; whether `3 ∣ k` persists for all `k` is the `θ/π` question of step 4 in another form.
* The branching rule (`InterfaceBranching`) is still a hypothesis; the diproton sign is still
  a measurement.

## 5. Verification

Shadow compile, exit 0 (one `rw`-in-hypotheses slip in the power-bound helper on the first
attempt, replaced by a direct `calc`); `#print axioms` clean. Probe 5/5 at `≤ 9.3e−61`.
