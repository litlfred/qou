# γγ word selection, step 6 — the `H₆` pp bond `(σ₂σ₃⁻¹)³` is selected through branching, on an interval

**Bean:** `qou-ales`. **Owner order (chat, 2026-09-12, "1 3 2"):** after merging step 5
(#7207, `03d6c9485c`), put the `H₆` pp bond in Lean (this record), then extend the `H₃`
candidates to `k ≤ 10`.

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/GammaGammaH6Interface.lean`
(36 declarations; `#print axioms` on every one: at most `[propext, Classical.choice,
Quot.sound]`; no `sorryAx`; `lean -DautoImplicit=false -s 65536` exit 0, 0 warnings, against
the step-4 shadow with `GammaGammaFrobeniusSelection` compiled in). **Probe:**
`computations/probes/gamma_gamma_h6_interface_branching_probe.py` (+ witness, 7/7; proton pin,
60 dps; reads the step-3 witness as its comparison target).

Nothing below reads AME2020, a CODATA binding value, or a census.

## 1. What step 3 measured, and what explains it

Step 3 tested the γγ bond candidates `G^m = (σ₂σ₃⁻¹)^m` on all eleven blocks of `H₆` with the
full Hoefsmit matrices on the interface (middle) strands, and found under the Frobenius reading:
`G³` feasible, `G¹, G², G⁴, G⁵` infeasible, with `(3,3)` the worst block every time. The
mechanism is the **branching rule**. The bond lives in the parabolic `⟨σ₂,σ₃⟩ ≅ H₃`; restricted
to it, `V_λ` splits into `H₃` irreducibles with multiplicities `(a_λ, b_λ, c_λ)` for
`((3), (2,1), (1³))`, and since the `(3)` and `(1³)` characters of a γγ word are `1`,

    χ_λ(G^m) = a_λ + b_λ · χ_(2,1)(V^m) + c_λ.

The multiplicities are path counts in Young's lattice from `μ ⊢ 3` to `λ ⊢ 6` (for the
middle-strand embedding, conjugate to the first-strand one by the distinguished coset
representative `T_d`; Dipper–James). Computed in Lean by `decide`:

| `λ` | `f^λ` | `(a, b, c)` | `χ_λ(G^m)` |
|---|---|---|---|
| `(6)` | 1 | `(1, 0, 0)` | `1` |
| `(5,1)` | 5 | `(3, 1, 0)` | `3 + χ_m` |
| `(4,2)` | 9 | `(3, 3, 0)` | `3 + 3χ_m` |
| `(3,3)` | 5 | `(1, 2, 0)` | `1 + 2χ_m` |

`dim_eq_branch` checks `f^λ = a + 2b + c` on all eleven blocks and `fDim_sq_sum` checks
`Σ (f^λ)² = 720`. The probe recomputes the path counts by an independent recursion and checks
the branched formula against the step-3 witness's `chi_by_block` on the four two-row blocks for
`m = 0..5`: **24 values, max deviation `7.2e−60`**. That is the numerical content of the
hypothesis, middle-strand embedding included.

## 2. Convention D is what makes `(3,3)` decisive

Convention D is the two-row truncation (owner ruling 2026-08-15; D7 on 2026-09-08). At `n = 6`
the SU(2) Markov weight `y_lambda_su_n(6, q, 2)` is positive exactly on `(6), (5,1), (4,2),
(3,3)` and **exactly zero** on the other seven (probe: max `|y|` off two-row `= 0.0`). So under
reading 3 only the four rows above are constrained, and since `1 + 2χ ≤ 3 + 3χ ≤ 3 + χ` for
`χ ≥ −1` and `(6)` is constant, feasibility of `G^m` is the single condition

    1 + 2 χ_(2,1)(V^m) ≥ 0        at (3,3).

At the pin: `−1.087, −0.821, +4.988, −1.341, −0.545` for `m = 1..5`.

## 3. The interval is `h² ≤ 1/12`, not step 4's `1/10`

`1 + 2χ_5(x) = −2x⁵ − 10x⁴ − 10x³ + 10x² + 10x − 1` changes sign at `x* = 0.09234` (probe,
informational), inside step 4's `(0, 1/10]`. So the `H₆` selection is **not** a theorem on
`x ≤ 1/10`: near `x = 0.0924` the bond `G⁵` becomes feasible and would be selected over nothing
cheaper only if `G³` failed, which it does not — but the table's `m = 5` row flips. The honest
interval is `0 < h² ≤ 1/12` (`h6_signs_of_small`), and `1 < q ≤ 23/20` still lands inside it:
`h² ≤ (129/460)² = 0.0787` (`h_sq_le_twelfth_of_q_le`). The proton pin has `h² = 0.0437`.

## 4. What is proved

* `interface_frobeniusFeasible_iff` — under `InterfaceBranching`, reading-3 feasibility of
  `G^m` is the sign condition on the branched characters of the positive-weight blocks.
* `interface_frobenius_table` — for every `1 < q ≤ 23/20`, every block data satisfying the
  branching hypothesis, every weight supported on the two-row blocks with `y_(3,3) > 0`:
  `G¹, G², G⁴, G⁵` infeasible, `G³` feasible.
* `interfaceSelected_three` — the minimal-crossing feasible non-zero bond with `m ≤ 5` is
  `G³ = σ₂σ₃⁻¹σ₂σ₃⁻¹σ₂σ₃⁻¹` (`interfaceBond_three`); `interfaceSelected_length_eq_six`.
* `gammaGamma_shift`, `interfaceBond_gammaGamma` — the bond is γγ-produced.

## 5. What is NOT proved

1. **The branching rule** is the hypothesis `InterfaceBranching q B`, not a theorem here: the
   corpus has the Young-lattice branching for SYT (`QOU/Mathlib/SkewBranchingSum.lean`,
   `SYTBranchingComplete.lean`) but not the Hoefsmit-representation restriction to a middle
   parabolic. The 24-value check is evidence at the pin, not a proof.
2. **The diproton sign** `B_pp = −4.47` keV (step 3 §2.3) needs the full 11-letter nucleon
   words in `H₆` and the log law; it stays a measurement. What this step adds is that the bond
   it is computed with is the one reading 3 selects on the whole interval.
3. `m > 5`, non-γγ letters, `θ/π` — as before.

## 6. Verification

Lean: shadow compile, exit 0, 0 warnings (two arity slips on `List.map_append` /
`List.length_map` on the first attempt, nothing else); `#print axioms` on 36 declarations
clean. Probe 7/7 at `≤ 7.2e−60`. `scripts/check-sidecars.sh` and
`scripts/precision-gates.sh --changed` as recorded in the PR.
