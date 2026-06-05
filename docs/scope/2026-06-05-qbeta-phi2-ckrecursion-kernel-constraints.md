# Φ₂ ↔ c_k-recursion kernel: formalize-first constraints from the cos(Φ(u)) reframe

**Status:** scope captured; formalize-first lemmas stated; bounded probe planned (consistency + bridge, NOT a kernel derivation).
**Owner direction:** 2026-06-05 session (litlfred) — "advance the Φ₂ closure".
**Disciplines:** *formalize-first* (constrain the kernel before any wide symbolic search), *corpus-grep* (the recursion block + #1871 chain inventoried first), *coordinate* (bridges PR #1887 → PR #1871; no file overlap).

---

## 0. TL;DR

PR #1887 established that the Q_β precision ladder is the u-Taylor expansion of a
single hyperbolic phase, `Q_β/Q_A = cos(Φ(u))`, with `Φ(u) = Φ₁u + Φ₂u² + …`,
`Φ₁ = √2` proved-exact (from the categorical `c_2 = −1`), and `Φ₂` the open rung.

The existing block
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
(on `main`) defines the **same** object from the Habiro side:
`F(q) = Q_β(q)/[Q_A(q)·cos(α_eff(q))]` satisfies a depth-`d` q-difference
equation `F(qξ) = R(q,ξ)·F(ξ)`, giving a linear recursion on the ladder
coefficients `c_{k+1} = Σ_{j=1}^d a_j(q_0)·c_{k+1−j}`. That block lists the
kernel `R` and the **symbolic `α_eff(q)`** as the two open inputs.

**The bridge (this PR):** `cos(α_eff(q))` in `F` is exactly `cos(Φ(u))` of
PR #1887, i.e.

> **`α_eff(u) = Φ(u)`** — so PR #1887 supplies the leading symbolic data the
> recursion block is missing: `Φ₁ = √2` (exact), and the open `Φ₂` is the
> kernel's leading coefficient up to `√2`.

This PR does **not** derive `Φ₂`'s value — that stays gated on the
SW-residue / Hoefsmit-`H₃(q)` kernel derivation (PR #1871's open frontier,
"no probe launched"). It contributes the **formalize-first constraints** the
kernel must satisfy, pruning that search and tying it to the #1887 parity wall.

---

## 1. The hypothesis class (what a kernel must do)

The depth-`d` recursion with the categorical seed:

| anchor | value | parity (bar `q↔q⁻¹`) | source |
|---|---|---|---|
| `c_1` | `0` | — | ladder starts at `k=2` (`F = 1 + c_2 u² + …`) |
| `c_2` | `−1` | bar-EVEN | proved (PR #1602, bar-even constraint) |
| `c_3` | `≈ −2.069` (proton) / `−2.020` (muon) | bar-ANTISYMMETRIC | cal-anchored; #1887 parity wall ⇒ bar-odd source |

A kernel `{a_j}` is admissible iff the recursion reproduces this anchor data.

## 2. The invariant that prunes the class (formalize-first)

Three structural facts constrain `{a_j}` **before** any symbolic `R` search:

1. **Depth ≥ 2 (unconditional).** A depth-1 kernel gives
   `c_2 = a_1·c_1 = a_1·0 = 0`, contradicting `c_2 = −1`. So **no depth-1
   kernel exists** — the recursion is at least depth-2.
   *(Lean: `ck_recursion_depth_one_refuted`.)*

2. **Leading coefficient pinned: `a_1 = −c_3 = √2·Φ₂` (unconditional, depth-2 reading).**
   With `c_1 = 0`, the first produced rung is
   `c_3 = a_1·c_2 + a_2·c_1 = a_1·(−1) = −a_1`, so `a_1 = −c_3`. Combined with
   the #1887 phase relation `c_3 = −Φ₁Φ₂` and `Φ₁ = √2`:
   `a_1 = −c_3 = Φ₁Φ₂ = √2·Φ₂`. **The kernel's leading coefficient and the
   #1887 Φ₂ are the same open object** (up to `√2`). The #1887 targets pin it:
   `a_1 = 2.0693…` (proton) / `2.0202…` (muon).
   *(Lean: `ck_a1_eq_neg_c3_depth_two`, `phi2_eq_kernel_leading_over_sqrt2`.)*

3. **Leading coefficient is bar-ODD (the #1887 wall, as a kernel constraint).**
   `c_3` is the first bar-antisymmetric rung (PR #1887: only the Reeb `sinh`
   channel can source it). Since `a_1 = −c_3`, `a_1` inherits the bar-odd
   parity — i.e. the kernel coefficient that produces `c_3` from the bar-even
   seed `c_2` must be bar-odd (`sinh`-type, `∝ h = q − q⁻¹ = 2 sinh η`), NOT
   bar-even. This is the same parity selection that refuted the cos/cosh
   even-avatar family (#1866).

**Consequence for the open kernel derivation (PR #1871):** the SW-residue /
Hoefsmit search for `R` may restrict to **depth ≥ 2 kernels whose leading
coefficient `a_1` is a bar-odd `√q`-radical object** evaluating to `√2·Φ₂` at
`q_0` — not the full `ℚ(q)[ξ,ξ⁻¹]` space. `a_2` is then pinned by the (currently
fitted) `c_4`; deriving `(a_1, a_2)` categorically discharges the `c_3`/`c_4`
fits at once.

## 3. What this PR delivers (bounded)

| Leg | Deliverable | NOT claimed |
|---|---|---|
| Lean | `depth_one_refuted`, `a1_eq_neg_c3`, `phi2 = a1/√2`, `a1` parity bridge — sorry-free ring/parity lemmas extending the #1887 phase lemmas | a derivation of `a_1`'s value |
| Compute | a consistency probe: depth-2 recursion with `a_1 = −c_3` (+ `a_2` from `c_4`) reproduces the ladder at both anchors; records `a_1 = √2·Φ₂` | a categorical kernel `R` |
| Coord | report to PR #1871 that `α_eff = Φ` (Φ₁=√2 exact) and `a_1 = √2·Φ₂` is their kernel's leading coefficient | |

The probe is explicitly a **bridge + consistency check**, not a closure: the
kernel coefficients are read from the anchors, not derived. The closure
remains GAP-A / SW-residue (PR #1871).

## 4. References

- Phase reframe + parity wall: PR #1887 (`QBetaReebSinhParity.lean`, `cos(Φ(u))`).
- c_k recursion block (open kernel): [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md).
- Binding G-recurrence sibling: PR #1871 `prop:binding-genfun-qdifference`, [`docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](https://github.com/litlfred/qou/blob/claude/confident-newton-R8lIx/docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md).
- c_2 = −1 proof: PR #1602 (bar-even constraint).
- c_3 truncation-order framing: [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
