# Φ₂ ↔ c_k-recursion kernel: formalize-first constraints from the cos(Φ(u)) reframe

**Status:** scope captured; formalize-first lemmas stated + Lean-verified; bounded refutation probe (constant depth-2 kernel) — NOT a kernel derivation.
**Owner direction:** 2026-06-05 session (litlfred) — "advance the Φ₂ closure".
**Disciplines:** *formalize-first* (constrain/refute kernel sub-classes before any wide symbolic search), *corpus-grep* (recursion block + #1871 chain inventoried first), *coordinate* (bridges PR #1887 → PR #1871; no file overlap).

---

## 0. Parity convention (used throughout)

Under the bar involution `q ↔ q⁻¹` (equivalently `η = log q ↦ −η`), a function `g`
of `η` is:

- **bar-even** ≙ symmetric: `g(−η) = g(η)` (e.g. `cosh(kη)`, `[2]_q = 2cosh η`);
- **bar-odd** ≙ antisymmetric: `g(−η) = −g(η)` (e.g. `sinh(kη)`, `h = q−q⁻¹ = 2sinh η`).

This is the single convention for the whole document (the table and the numbered
constraints both use `bar-even` / `bar-odd`).

## 1. TL;DR

PR #1887 established the Q_β precision ladder is the u-Taylor expansion of a single
hyperbolic phase, `Q_β/Q_A = cos(Φ(u))`, `Φ(u) = Φ₁u + Φ₂u² + …`, `Φ₁ = √2`
proved-exact (from the categorical `c_2 = −1`), `Φ₂` the open rung.

The on-`main` block
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
defines the **same** object from the Habiro side:
`F(q) = Q_β(q)/[Q_A(q)·cos(α_eff(q))]` satisfies a depth-`d` q-difference equation
`F(qξ) = R(q,ξ)·F(ξ)`, giving a depth-`d` linear recursion on the ladder
coefficients. That block lists the kernel `R` and the **symbolic `α_eff(q)`** as the
two open inputs.

**The bridge (this PR):** `cos(α_eff(q))` in `F` is exactly `cos(Φ(u))` of PR #1887:

> **`α_eff(u) = Φ(u)`** — PR #1887 supplies the leading symbolic data the recursion
> block is missing: `Φ₁ = √2` (exact), and the open `Φ₂` is the kernel's leading
> coefficient up to `√2`.

This PR does **not** derive `Φ₂`'s value — that stays gated on the SW-residue /
Hoefsmit-`H₃(q)` kernel derivation (PR #1871's open frontier). It (i) **constrains**
the kernel and (ii) **refutes** the constant depth-2 sub-class.

## 2. Coefficient indexing (the recursion's actual carrier)

The q-difference equation constrains the **Taylor coefficients of `F`**, so the
recursion is stated on `f_n := [u^n]\,F(u)`, the Taylor coefficients of
`F = Q_β/Q_A = cos(Φ(u))`:

| `n` | `f_n` | relation to ladder | parity |
|----|------|--------------------|--------|
| 0 | `1` | constant term of `F` (the seed, **not** a ladder coefficient) | bar-even |
| 1 | `0` | no `u¹` term | — |
| 2 | `c_2 = −1` | `f_2 = c_2` | bar-even |
| 3 | `c_3 ≈ −2.069` (p) / `−2.020` (m) | `f_3 = c_3` | bar-odd |
| 4 | `c_4` (fitted `≈ −0.972`) | `f_4 = c_4` | — |

The product-form ladder `F = ∏_{k≥2}(1 + c_k u^k)` and the Taylor series agree
**through `u⁴`**: cross-terms first appear at `u⁵ = c_2c_3`, so `f_n = c_n` for
`2 ≤ n ≤ 4` — the low-order constraints below are insensitive to the product/Taylor
distinction. The depth-`d` recursion `f_n = Σ_{j=1}^d a_j(q_0)·f_{n−j}` is asserted
for `n ≥ d` (it consumes `d` seed values `f_0, …, f_{d−1}`).

## 3. The constraints (formalize-first; all Lean-verified, sorry-free)

1. **Depth ≥ 2 — unconditional.** A depth-1 recursion `f_n = a_1 f_{n−1}` forces
   `a_1 = f_1/f_0 = 0`, then `f_2 = a_1 f_1 = 0 ≠ −1`. No depth-1 kernel exists.
   *(Lean: `ck_recursion_depth_one_refuted`.)*

2. **Depth-2 second coefficient pinned: `a_2 = c_2 = −1`.** At `n = 2`,
   `f_2 = a_1 f_1 + a_2 f_0 = a_2` (using `f_1 = 0`, `f_0 = 1`), so `a_2 = f_2 = −1`.
   *(Lean: `ck_a2_eq_c2_depth_two`.)*

3. **Depth-2 leading coefficient pinned: `a_1 = −c_3`.** At `n = 3`,
   `f_3 = a_1 f_2 + a_2 f_1 = −a_1` (using `f_2 = −1`, `f_1 = 0`), so `a_1 = −c_3`
   regardless of `a_2`. *(Lean: `ck_a1_eq_neg_c3_depth_two`.)*

4. **`a_1 = √2·Φ₂` — the kernel's leading coefficient is the #1887 Φ₂ target.**
   With `a_1 = −c_3` and the #1887 phase relation `c_3 = −Φ₁Φ₂`, `Φ₁ = √2`:
   `a_1 = Φ₁Φ₂ = √2·Φ₂`. The #1887 targets pin it: `a_1 = 2.0693…` (proton) /
   `2.0202…` (muon). *(Lean: `ck_a1_eq_sqrt2_phi2`.)*

5. **`a_1` is bar-odd (the #1887 wall, as a kernel constraint).** `c_3` is the first
   bar-odd rung (PR #1887: only the Reeb `sinh` channel sources it). Since
   `a_1 = −c_3` pointwise in `η`, `a_1` is bar-odd — the kernel coefficient producing
   `c_3` from the bar-even seed `c_2` must be bar-odd (`sinh`-type, `∝ h = 2sinh η`),
   NOT bar-even. Same parity selection that refuted the even cos/cosh avatars (#1866).
   *(Lean: `ck_a1_bar_odd`.)*

6. **Constant depth-2 kernel REFUTED.** Constraints 2–3 fully determine a *constant*
   depth-2 kernel `(a_1, a_2) = (−c_3, −1)`, which then **predicts**
   `c_4 = f_4 = a_1 f_3 + a_2 f_2 = (−c_3)(c_3) + (−1)(−1) = 1 − c_3²`. Numerically
   `1 − c_3² ≈ −3.282` (proton) / `−3.081` (muon), versus the CODATA-residual
   `c_4 ≈ −0.972` — a ~3.4× / 3.2× miss. So the raw-`u^k` ladder is **not** generated
   by a constant depth-2 recursion. *(Lean: `ck_c4_constant_depth_two_prediction`;
   probe: numerical refutation at both anchors.)*

   **Caveat.** `c_4`'s fitted value sits near the `c_k` precision floor, so the
   *magnitude* of the miss is soft; but `−3.28` vs `−0.97` is a sign-preserving
   factor-3 gap, robustly outside any plausible floor. The reading: the recursion is
   either **depth ≥ 3**, or **non-constant** — i.e. it lives in the Habiro `(u;u)_m`
   basis (the block's "change-of-basis" caveat is load-bearing), not the raw `u^k`
   basis.

## 4. Consequence for the open kernel derivation (PR #1871)

The SW-residue / Hoefsmit search for `R` may restrict to kernels that are
**depth ≥ 2** (constraint 1), **not constant-depth-2** (constraint 6), with a
**bar-odd leading coefficient `a_1`** (constraint 5) evaluating to `√2·Φ₂` at `q_0`
(constraint 4) — not the full `ℚ(q)[ξ,ξ⁻¹]` space. This prunes the search and ties
it to the #1887 Reeb-`sinh` parity wall. `a_2`-and-higher are pinned by `c_4…` once
the categorical kernel is derived; that derivation discharges the `c_3`/`c_4` fits at
once and remains the open GAP-A / SW-residue frontier.

## 5. What this PR delivers (bounded) vs. NOT claimed

| Leg | Deliverable | NOT claimed |
|---|---|---|
| Lean | `ck_recursion_depth_one_refuted`, `ck_a2_eq_c2_depth_two`, `ck_a1_eq_neg_c3_depth_two`, `ck_a1_eq_sqrt2_phi2`, `ck_c4_constant_depth_two_prediction`, `ck_a1_bar_odd` — sorry-free, extending the #1887 phase lemmas | a derivation of `a_1`'s value |
| Compute | constant depth-2 refutation probe (predicts `c_4 = 1 − c_3²`, compares to fit at both anchors) + witness | a categorical kernel `R` |
| Coord | report to PR #1871: `α_eff = Φ` (Φ₁=√2 exact), `a_1 = √2·Φ₂` bar-odd, constant-depth-2 ruled out | |

No fits wired; Δ_λ gate held. The closure remains GAP-A / SW-residue (PR #1871).

## 6. References

- Phase reframe + parity wall: PR #1887 (`QBetaReebSinhParity.lean`, `cos(Φ(u))`).
- c_k recursion block (open kernel): [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md).
- Binding G-recurrence sibling: [`prop:binding-genfun-qdifference`](../../content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md) + [SW-residue / jet-filtration workplan](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md) (both on `main` as of PR #1871).
- c_2 = −1 proof: PR #1602 (bar-even constraint).
- c_3 truncation-order framing: [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
