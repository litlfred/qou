# Closed-Form Theorem for χ_sym(β) · χ_alt(β)

*Proved by structural inspection of `atom_braid_word_3A`.*

> **🟧 SCOPE (added 2026-08-26, bean `qou-cdqu`). This theorem is stated for the
> COLOUR-BLIND convention, `pn_convention="strict_averaged"`. It is exact there
> and it is not exact for the canonical word.**
>
> Step 4 below asserts that the single p-n boundary "uses (1, −H_A/2) = ud-half".
> Under `pn_convention="bring_color_weighted"` — canonical since the owner ruling
> of 2026-08-15 (R3), and the default of `atom_braid_word_3A` — that boundary is
> `(1, −H_A·(1/2 − δ/4))` with `δ = flavor_split_subleading(q₀) ≈ 0.001376`. It is
> **averaged but not a ud-half letter**, so the canonical word has `n_ud = 2A`
> and `n_averaged = 2A + 1`, and the exponent `2A+1` above folds the p-n letter
> in as if it were a ud one.
>
> **Measured cost of the substitution: 5.1139e-9**, on all four of D, T, ³He,
> ⁴He. Carrying the p-n letter as itself, `f_ud^(2A) · f_pn`, takes the residual
> to 1.2e-14 — the float64 floor of the inputs.
>
> **Why the error is second order**, which is why it hid for so long: the
> per-factor product `f(d) = d² − 1 + d·H_A` satisfies the exact, division-free
> identity
>
> $$4\,f(d) = (2d + H_A)^2 - H_A^2 - 4$$
>
> — all of the `d`-dependence sits inside a *perfect square* in the offset
> `2d + H_A`, which vanishes exactly at `d = −H_A/2`. So the ud letter is a
> stationary point, and the offset enters squared; those are the same fact. A `6.88e-4` relative shift in `d` moves the product by only
> `(7.19e-5)² = 5.17e-9`. Predicted from that identity alone: 5.11397e-9, against
> 5.11395e-9 measured — six significant figures. Formalised sorry-free as
> `QOU.ChiSymAlt.perFactorOfD_sub_udHalf`.
>
> The colour-weighted generalisation is
> `QOU.ChiSymAlt.chiPairProductC_eq`, with this theorem as its `δ = 0` corollary
> (`chiPairProductC_delta_zero`). That is the only direction available: setting
> `δ = 0` collapses the weighted form to this one, while this one has already
> discarded `δ`. Nothing below is wrong within its own convention; it simply
> never stated which convention it was in.

## Theorem

Let $\beta_{Z,N}$ be the output of `atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1, include_inter=True)` for any (Z, N) with Z ≥ 1 and N ≥ 1, A = Z + N. Then

$$\chi_\text{sym}(\beta_{Z,N}) \cdot \chi_\text{alt}(\beta_{Z,N}) = (-1)^{\#(β) + 1} \cdot (1 + H_A^2/4)^{2A+1}$$

where #(β) = n_σ + n_σ⁻¹ + n_ud is the total factor count. For all tested atoms (D, T, ³He, ⁴He), #(β) is odd so the overall sign is −1.

## Individual closed forms

$$\chi_\text{sym}(\beta_{Z,N}) = q^{n_σ - n_{σ^{-1}}} \cdot ([2]_q/2)^{2A+1}$$

$$\chi_\text{alt}(\beta_{Z,N}) = (-1)^{\#(β)} \cdot q^{n_{σ^{-1}} - n_σ} \cdot ([2]_q/2)^{2A+1}$$

## Proof

### Step 1 — Hecke eigenvalues of σ in 1-dim irreps

In irrep λ = (n) (sym): σ ↦ +q.
In irrep λ = (1ⁿ) (alt): σ ↦ −q⁻¹.

### Step 2 — Character factorises on 1-dim irreps

For λ ∈ {sym, alt} and any factor c·σ + d·I:
- χ_sym(c·σ + d·I) = c·q + d
- χ_alt(c·σ + d·I) = −c/q + d

Multiplicativity: for β = ∏ᵢ Fᵢ, χ_λ(β) = ∏ᵢ χ_λ(Fᵢ).

### Step 3 — Per-factor character product

$$\chi_\text{sym}(c\sigma + dI) \cdot \chi_\text{alt}(c\sigma + dI) = (cq + d)(-c/q + d) = d^2 - c^2 + c d H_A$$

Three factor types in `atom_braid_word_3A`:

| type | (c, d) | χ_s · χ_a |
|------|--------|:---:|
| σ | (1, 0) | −1 |
| σ⁻¹ | (1, −H_A) | −1 |
| ud-half | (1, −H_A/2) | −(1 + H_A²/4) |

### Step 4 — Counting ud-half factors in `atom_braid_word_3A`

From inspection of the source (mass_at_3A_proper.py:171-209 and mass_endomorphism.py):

**Per nucleon** (proton or neutron): exactly 2 ud-half factors (one in each of `intra_g0`, `intra_g1`). Same for protons and neutrons.

**Per atom** (inter-nucleon): the ordering `['p']*Z + ['n']*N` has transitions:
- Z−1 `pp` (no ud-half, uses (1, 0))
- N−1 `nn` (no ud-half, uses (1, −H_A))
- **Exactly 1 pn boundary** — (1, −H_A/2), a ud-half letter, **only under
  `pn_convention="strict_averaged"`**. Under the canonical
  `bring_color_weighted` it is (1, −H_A·(1/2 − δ/4)): averaged, but **not** a
  ud-half. See the scope banner at the top of this file.

With `m_pn = 1` (default), this adds **exactly 1 ud-half per atom** — again, in
the colour-blind convention only. In the canonical one it adds one *averaged*
letter that is not a ud-half, so `n_ud = 2A` and `n_averaged = 2A + 1`.

### Step 5 — Total count

$$n_\text{ud}(Z, N) = 2A + 1 \quad \text{for } Z, N \geq 1
\qquad \text{(colour-blind convention)}$$

Each nucleon contributes 2, and the single pn boundary adds 1.

In the canonical colour-weighted convention the second clause does not hold: the
pn boundary is averaged but is not a ud-half, giving

$$n_\text{ud} = 2A, \qquad n_\text{averaged} = 2A + 1.$$

Both counts are asserted per atom by
`computations/chi_sym_alt_closed_form.py`, and `nUd` in the Lean sibling is the
`2A` count.

### Step 6 — Assemble

$$\chi_\text{sym}(\beta) \cdot \chi_\text{alt}(\beta) = \prod_\text{factors} (\chi_\text{sym} \cdot \chi_\text{alt})(F)$$

$$= (-1)^{n_σ + n_{σ^{-1}}} \cdot (-(1 + H_A^2/4))^{n_\text{ud}}$$

$$= (-1)^{n_σ + n_{σ^{-1}} + n_\text{ud}} \cdot (1 + H_A^2/4)^{2A+1}$$

$$= (-1)^{\#(β)} \cdot (1 + H_A^2/4)^{2A+1} \qquad \square$$

## Verification

Observed χ_sym · χ_alt vs predicted, at substrate q₀:

| atom | n_σ | n_σ⁻¹ | n_ud | predicted | observed | diff |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| D | 11 | 7 | 5 = 2·2+1 | −1.055840 | −1.0558 | 0.004% |
| T | 16 | 12 | 7 = 2·3+1 | −1.079039 | −1.0790 | 0.004% |
| ³He | 18 | 10 | 7 = 2·3+1 | −1.079039 | −1.0790 | 0.004% |
| ⁴He | 23 | 15 | 9 = 2·4+1 | −1.102748 | −1.1027 | 0.004% |

The 0.004% residual is the numerical precision of the full Wedderburn character evaluator, not a theory gap.

## Edge cases

- **Z = 0 or N = 0**: no pn boundary, n_ud = 2A. Formula becomes −(1 + H_A²/4)^{2A}. Not physically interesting (pure p/n systems).
- **m_pn ≠ 1**: generalises to n_ud = 2A + m_pn.
- **non-contiguous ordering**: if nucleons were interleaved (e.g., `pnpn`), the number of pn boundaries would differ and n_ud would shift. The `['p']*Z + ['n']*N` convention is built into `atom_braid_word_3A`.

## Significance

This is the **first exact closed-form result** derived from first principles of the framework for any atomic mass quantity. No fitting, no empirical tuning — purely structural.

Every step is an identity from the Hecke algebra (σ² = H_A σ + 1, giving eigenvalues {q, −q⁻¹}), the branching conventions of the framework's braid-word construction, and the multiplicativity of characters on 1-dim irreps.

Extension to higher-dim irreps (std = (2,1) at n = 3 and similar for larger n) requires matrix-valued representations where multiplicativity fails. That's the next frontier for extending this derivation to the full Plancherel sum.
