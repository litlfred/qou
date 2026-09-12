# γγ word selection, step 4 — the vertex is the `q`-deformed 3-cycle; vertex powers are symmetric only when scalar

**Bean:** `qou-ales` (owner ruling 2026-09-08: every canonical braid word is *selected* by
γγ pair production + the confinement SDP at `q₀`, never by census). Steps 1+2 (#7184) and 3
(#7192) are on `main`. This record closes §4.3 of the step-3 record
(`2026-09-11-gamma-gamma-word-selection-step3.md`) — the `k ≥ 2` non-symmetry — by algebra
rather than measurement, and explains *why* `k = 3` is the survivor.

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/GammaGammaVertexOrder.lean`
(31 theorems; `#print axioms` on every one: at most `[propext, Classical.choice,
Quot.sound]`; no `sorryAx`). **Probe:** `computations/probes/gamma_gamma_vertex_order_probe.py`
(+ witness, 8/8; proton pin, 60 dps; reads the step-3 witness as its comparison target).

Nothing below reads AME2020, a CODATA binding value, or a census.

## 1. The algebra

Let `h = q − q⁻¹`, and let `V` be the Hoefsmit `(2,1)`-image of the pair-production vertex
`σ₀σ₁⁻¹` (step 3, `stdImage_vertex_entries`):

```
V = [[ q(a − h),      q·b        ],
     [ −q⁻¹·b,   −q⁻¹(a' − h) ]],   a = h/(1 − q⁴),  a' = h/(1 − q⁻⁴),  b² = a·a' + 1.
```

From the three Hoefsmit relations alone (generic field, `q² ≠ 1`):

| fact | Lean | note |
|---|---|---|
| `a·q·(1 + q²) = −1` | `hoefsmit_a_mul` | the only step needing `q² ≠ 1` |
| `tr V = −1 − h²` | `vtx_trace` | so `2 cos θ = −1 − h²` |
| `det V = 1` | `vtx_det` | `V ∈ SL₂` |
| `V² = (tr V)·V − 1` | `vtx_sq` (via `sq_eq_of_det_one`) | Cayley–Hamilton, entrywise |
| `V^k = α_k V + β_k 1` | `vtx_pow_eq_lin` | `α_{k+1} = t α_k + β_k`, `β_{k+1} = −α_k`, `(α₀, β₀) = (0, 1)` |

The first five coefficient pairs are `(1,0), (t,−1), (t²−1, −t), (t³−2t, −(t²−1)),
(t⁴−3t²+1, −(t³−2t))` (`lin_one` … `lin_five`).

## 2. Symmetry of `V^k`

On `ℝ` with `0 < q` and `b ≠ 0`, the off-diagonal defect of `V` is `V₀₁ − V₁₀ = b(q + q⁻¹) ≠ 0`,
and that of `V^k` is `α_k` times it (`pow_off_diagonal`). Hence

* **`V^k` is symmetric ⇔ `α_k = 0`** (`vtx_pow_isHermitian_iff`), and
* **`V^k` is symmetric ⇔ `V^k = 1` or `V^k = −1`** (`vtx_pow_isHermitian_iff_scalar`; the
  scalar is `±1` because `det V^k = 1` forces `β_k² = 1`).

So the *literal* `Matrix.PosSemidef` reading of the confinement SDP admits a non-trivial γγ
word in `H₃` **iff some vertex power is a scalar**, i.e. iff `θ/π ∈ ℚ` where `2 cos θ = tr V`.
Step 3 proved the `k = 1` case and measured `k ≤ 5` at the pin; this replaces the measurement
by the general criterion.

## 3. Why `k = 3`: the `q`-deformed 3-cycle

`lin_three` gives `V³ = (t² − 1)·V − t·1`, and with `t = −1 − h²`:

```
V³ = (2h² + h⁴)·V + (1 + h²)·1,        V³ − 1 = h²·((2 + h²)·V + 1).
```

(`vtx_three`, `vtx_three_sub_one`.) Therefore **`V³ = 1 ⇔ h = 0`** (`vtx_three_eq_one_iff`),
i.e. exactly at `q = 1`, where `σᵢ ↦ sᵢ` and the vertex is the 3-cycle `s₀s₁ ∈ S₃`. The `k = 3`
survivor of step 3 — `β_Bor`, the nucleon core, and on the `H₆` interface the pp bond
`(σ₂σ₃⁻¹)³` — is the **`q`-deformation of the identity**, with defect of order `h² ≈ 0.0437`.
That is the structural reason for two numbers in the step-3 record:

* `V³` lies within `0.11` of the identity at `q₀` (`|V³ − 1|_F = 0.1126`, probe), and
* the selected pp bond moves the diproton by only `4.47` keV (`tr_atom/tr_free = 1.00106`).

Both are `h²`-small because the bond is `h²`-close to doing nothing.

## 4. The step-3 table is the Chebyshev recurrence, on an interval

`trace_pow_eq` gives `χ_k := tr V^k = α_k t + 2β_k`, i.e. the recurrence
`χ_{k+1} = t χ_k − χ_{k−1}`. In closed form with `x = h²` (`trace_vtx_pow_one` … `_five`):

| k | `χ_(2,1)(V^k)` | at `q₀` (`x = 0.043706…`) | step-3 witness `chi_21` |
|---|---|---|---|
| 1 | `−1 − x` | −1.04370620853 | −1.04370620853 |
| 2 | `x² + 2x − 1` | −0.91067735027 | −0.91067735027 |
| 3 | `2 − 3x² − x³` | +1.99418581298 | +1.99418581298 |
| 4 | `x⁴ + 4x³ + 2x² − 4x − 1` | −1.17066676370 | −1.17066676370 |
| 5 | `−x⁵ − 5x⁴ − 5x³ + 5x² + 5x − 1` | −0.77235364358 | −0.77235364358 |

Agreement with the step-3 witness (which came from `hoefsmit_mpmath.seminormal_matrices_mp`,
not the closed forms) is `2.6e−60`; with the directly computed powers `5.4e−61`.

Two interval statements, proved for **every** `0 < x ≤ 1/10`:

* `chi_signs_of_small` — the signs are `(−, −, +, −, −)` for `k = 1..5`; so under the
  **Frobenius reading** (`χ_(2,1) ≥ 0`) the minimal non-zero survivor is `k = 3` on the whole
  interval, not just at the pin;
* `lin_ne_zero_of_small` — `α_k ≠ 0` for `k = 1..5`; so under the **literal reading** no
  `k ≤ 5` survives on the whole interval (`hoefsmit_vtx_pow_not_isHermitian`, stated for the
  actual Hoefsmit data and `1 < q ≤ 23/20`).

`h_sq_le_of_q_le` shows `1 ≤ q ≤ 23/20 ⇒ h² ≤ 1/10`; the proton pin `q₀ = 1.10998` is inside,
with `h² = 0.0437` and `min_{k≤5} |α_k| = 0.0893` (at `k = 3`).

## 5. What stays open

1. **Whether some `V^k` is ever scalar** — `θ/π ∈ ℚ` at the pin. Informational only, from the
   probe: `θ/π = 0.67475909…`, `3θ − 2π = 4.37°`, and the closest approach of `V^k` to a scalar
   for `k ≤ 60` is `|α_k| = 0.0355` at `k = 40`. No claim is made; `q₀` is pinned by inverting a
   transcendental relation and nothing here decides the arithmetic.
2. **The PSD reading is still the owner's call** (step-3 §4.1; asked in chat 2026-09-11). This
   record sharpens the choice: the literal reading selects nothing non-trivial for any `k ≤ 5`
   at any `q` in the interval, and its general content is "some vertex power is `±1`"; the
   Frobenius reading selects `k = 3` on the whole interval.
3. The non-γγ letters (step-3 §4.2) are untouched.

## 6. Verification

* Lean: `lean -DautoImplicit=false -s 65536` against a hardlinked `QOU` shadow in which the
  whole import cone (`GluonVertexPsdParity`, `ChiralFermionBraidWords`,
  `GammaGammaWordSelection`, `GammaGammaSelectorH3`) was rebuilt from source — **exit 0,
  0 errors, 0 warnings**; `#print axioms` on all 31 theorems clean of `sorryAx`.
* Probe: 8/8 assertions; every numeric comparison at `≤ 2.7e−60` on 60 dps.
