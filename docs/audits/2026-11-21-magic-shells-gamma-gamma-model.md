# Magic shells through γγ processes in Hecke normal form: the model

Bean `qou-mgg1`. This is the owner request of 2026-11-21, with these card answers:

- **D1:** the nucleus is modelled as a single strand.
- **D2:** the full photon, with three processes modelled: excitation, interaction, binding.
- **D3:** report both binding tests.

This document fixes the model before any computation. Every choice is listed in §3 so the owner can change it.

## 1. Algebra

`A = H_{Z+1}(q)` with generators `σ_0, …, σ_{Z-1}` and the Hecke relation
`(σ_i − q)(σ_i + q⁻¹) = 0`.

- Strand 0 is the nucleus `𝒩`, quotiented to one strand as in `conj:shell-closure-nf-term-count`.
- Strand `k` (`1 ≤ k ≤ Z`) is electron `e_k`.

The photon is `def:photon`, with the owner-ruled fourth term `σ_iσ_{i+1}⁻¹`:

```
γ_i(φ) = 1 + φ₀ σ_i + φ₁ σ_{i+1} + φ₀₁ σ_i σ_{i+1}⁻¹ ,   0 ≤ i ≤ Z−2.
```

## 2. The three processes

| Process | Operator | Reading |
|---|---|---|
| **Binding (capture) of electron `k`** | `K_k = A_{0k}⁻¹` | `A_{0k} = σ_{k−1}⋯σ_1 σ_0² σ_1⁻¹⋯σ_{k−1}⁻¹` is the pure braid in which strand `k` encircles strand 0, so the closure of strands `0, k` is a Hopf link. The inverse carries the negative nucleus–electron orientation of the corpus table (`𝒩–e = σ⁻¹`). |
| **Particle interaction, electron with electron** | `I_k = σ_{k−1}` (`k ≥ 2`) | One positive crossing between neighbouring electrons `k−1, k`, from the corpus table (`e–e = σ`). |
| **Photon emission / absorption** | `E_k = γ_{k−2}(φ)` (`k ≥ 2`) | A photon on strands `k−2, k−1, k`. On capture it is the emitted photon; applied to a finished atom it is an absorbed photon. |

**The atom** is built one electron at a time:

```
W_1 = K_1 ,        W_k = W_{k−1} · K_k · I_k · E_k   (k ≥ 2),
```

and the **binding operator** that adds electron `k` is `O_k = K_k I_k E_k`.

**Excitation** of the `Z`-electron atom by an absorbed photon at site `i` is `W_Z · γ_i(φ′)`.

## 3. Choices that are the owner's to change

1. The capture braid is the pure braid `A_{0k}⁻¹`. The earlier model used `(σ⁻¹)^Z` on a two-strand quotient, which is not a braid in `H_{Z+1}`.
2. Each capture emits exactly one photon, on the last three strands.
3. The interaction couples only neighbouring electrons, with one crossing.
4. One photon `φ` is used for every capture. `φ` is **not derived**: it is kept as a variable, and every result is reported over a region of `φ`. Selecting a `φ` because it reproduces 2 or 10 would be selection against the target, and is not done.

## 4. What is measured at each `k`

**Complexity of `O_k` and of `W_k`** (exact; generic `q` and `φ` modulo a large prime):

- the normal-form term count;
- the longest normal-form word;
- the number of Hecke reductions.

**Binding test 1: Frobenius positivity** (reading 3, owner 2026-09-12). `χ_λ(W_k) ≥ 0` for every two-row `λ ⊢ k+1`, at the proton `q₀`. Convention D kills the three-row weights, so only two-row `λ` carry `y_λ > 0`. The result is reported as the set of `φ` on a grid where the test holds, and whether the bare `φ = 0` passes.

**Binding test 2: SDP value.** The corpus σ_F (`sigma_f_electron_shell_chain.py`) depends only on `k`, through Wedderburn weights, and not on the element. A per-element confinement value has to be defined before it can be reported. That definition is an open item for the owner, and the probe does not guess it.

## 5. Reach

Normal-form counts need the full `H_{k+1}` (dimension `(k+1)!`), which is feasible to about `k = 7`. The positivity test needs only the two-row irreducibles, whose dimensions stay small, so it reaches `k = 10`: neon, the first noble-gas closure past helium.

## 6. First results (`computations/probes/gamma_gamma_shell_probe.py`, 2026-11-21)

Part A is exact: computed modulo 1000003 and 999983, at `q = 7` and `q = 5`, with two generic choices of `φ`; the two runs agree. Part B uses arb intervals at 256 bits, at the proton `q₀`; every sign reported is certified, and a sign whose interval contains 0 is reported as undecided.

**Normal-form complexity, `k = 1..7`.** This is smooth, with no feature at a closure.

| k | terms of `W_k` | longest word in `W_k` | Hecke reductions for `W_k` | terms of `O_k` | longest word in `O_k` |
|---|---|---|---|---|---|
| 1 | 2 | 1 | 1 | 2 | 1 |
| 2 | 6 | 3 | 17 | 4 | 3 |
| 3 | 24 | 6 | 65 | 8 | 5 |
| 4 | 96 | 10 | 293 | 12 | 7 |
| 5 | 384 | 14 | 1361 | 20 | 9 |
| 6 | 1536 | 18 | 6293 | 36 | 11 |
| 7 | 6144 | 22 | 28769 | 68 | 13 |

- The term count of `W_k` is exactly `6·4^{k−2}`.
- The term count of `O_k` is `2^k + 4`.
- The longest words grow by fixed steps (+4 per electron in `W_k`, +2 in `O_k`).
- The binding operator `O_k` gets steadily larger, at the same rate before, at and after `Z = 2`.
- `k = 10` is not reached here, because Part A needs the full algebra.

**Frobenius positivity (reading 3), `k = 1..10`.**

- **Bare photon (`φ = 0`).** The atom binds for `Z = 1, 2` and fails for every `Z ≥ 3`. The failure is always and only in the block `(Z−1, 2)`, where `χ` falls smoothly: `−1.13, −1.30, −1.49, −1.71, −1.98, −2.28, −2.65, −3.07`. That block first exists at `Z = 3` (`n = 4`). So the stop after helium coincides with that block appearing: it is not yet evidence for a helium closure. There is no change at `Z = 10`.
- **Full grid `φ ∈ {−1, −½, 0, ½, 1}³` (`k ≤ 6`).** The atom binds at 125, 63, 61, 36, 44 and 31 of the 125 points.
- **Axis points (`k = 7..10`).** Only `φ₁ = +1` binds at every `k`.
- None of this singles out `Z = 2` or `Z = 10` beyond the block-appearance effect above.

**Binding test 2 (SDP value) is not computed.** It needs the per-element definition asked for in §4.

## 7. Binding region in φ-space and the positivity margin (owner A1, B1; 2026-11-21)

`computations/probes/gamma_gamma_shell_region_probe.py` computes the margin
`m(W) = min over λ ⊢ k+1 with at most two rows of χ_λ(W) / dim λ`.

- It is positive exactly when the atom binds.
- Its relative form divides by the largest `|χ_λ / dim λ|`.
- φ grid: 7³ points for `k ≤ 8`, 5³ for `k = 9, 10`.
- Arithmetic: certified arb at the proton `q₀`.

The column "binds on {−1,0,1}³" uses the 27 points shared by both grids, so it is comparable across all `k`.

| Z = k | binds / grid | binds on {−1,0,1}³ | best relative margin | bare relative margin |
|---|---|---|---|---|
| 1 | 343/343 | 27 | 0.659 | 0.659 |
| 2 | 172/343 | 11 | 0.998 | 0.454 |
| 3 | 167/343 | 13 | 0.889 | −0.860 |
| 4 | 97/343 | 8 | 0.936 | −0.438 |
| 5 | 114/343 | 10 | 0.763 | −0.310 |
| 6 | 83/343 | 8 | 0.748 | −0.254 |
| 7 | 108/343 | 11 | 0.614 | −0.228 |
| 8 | 85/343 | 8 | 0.557 | −0.216 |
| 9 | 42/125 | 11 | 0.490 | −0.215 |
| 10 | 33/125 | 8 | 0.430 | −0.206 |

What the table shows, read as a scope-(a) result for this model only:

- **The binding region never vanishes and never reopens.** It alternates with parity: odd `Z` gives 10–13 of the 27 shared points and even `Z` gives 8. This is the same even/odd pairing signal as the April 2026 normal-form work, and it carries no `Z = 2` or `Z = 10` feature.
- **The best relative margin declines smoothly from `Z = 4`.** Nothing marks `Z = 10`.
- **The bare margin rises monotonically toward 0.**

The negative constrains this capture rule only: one Hopf capture, one neighbour crossing and one photon per electron. It does not exclude other capture rules (§3).
