# Residue-A unblock — the locus, and the kernel keystone (scope)

**Date:** 2026-06-04
**Status:** SCOPE (kernel first-cut to follow on this branch)
**Registry:** [`../coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)

## Purpose

Pin down **where** in the canonical derivation chain the residue-A / `c_k`
structure arises, and **what** the unblock concretely is, so the search stops
chasing the wrong objects (real-q forms and finite roots of unity — both now
refuted). This doc is the conceptual frame; the kernel first-cut probe follows.

## Symbols (for mid-stream readers)

| symbol | meaning |
|---|---|
| `q₀` | substrate deformation parameter, proton-pinned ≈ 1.10998 (CAL-2 / τ_n) |
| `ℏ_q` | substrate ℏ, `= (q − 1)/q` |
| `b` | Hoefsmit `b` factor; appears in the ladder variable `u = b·ℏ_q²` |
| `u`, `u_substrate` | ladder variable `u = b·ℏ_q²`; `u_substrate ≈ 0.00852` is its value at q₀ |
| `ε` | imaginary distance from q₀ to the nearest singularity (≈ 4.4e-7); `= b` in PR #1821 — chosen over `δ` to avoid visual collision with the `Δ` family (Δ_λ, Δ_pn) |
| `τ` | Archimedean / fibre functor — evaluates a fibre object to MeV at q₀ |
| `T_w`, `T_β` | the confinement-SDP-selected operator |
| `ξ` | the shift variable of the q-difference equation `F(qξ) = R(q,ξ)·F(ξ)` |
| `c_k` | Q_β precision-ladder coefficients, `Q_β = Q_base·∏(1 + c_k u^k)` |
| `A` | residue of `F` at the simple pole `u = u_substrate` (≈ 1.804e-15) |
| `[n]_q` | q-integer `(qⁿ − q⁻ⁿ)/(q − q⁻¹)`; `[n]_q → n` as q→1 |
| `CAL-2 (τ_n)` | the neutron-β-decay-width calibration that pins q₀ |

## The chain

```
q₀ → 𝐂 categorical action → Yekutieli non-abelian Stokes → 𝐇_n(q) Hecke
   → Wedderburn ⊕_λ M_{d_λ} → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
   → confinement SDP → canonical T_w → Archimedean functor τ at q₀ → MeV
```

Q_β is an **observable** at the τ-evaluation (far right). But the `c_k` ladder
and the residue `A` are properties of the **fibre object**

```
F(q) = Q_β(q) / [Q_A(q) · cos α_eff(q)]
```

viewed as a function of the *formal* fibre variable q, **before** τ collapses
it. So the locus is the **steps 5→6 stretch**: Frobenius pairing → confinement
SDP → Archimedean functor.

## Step-by-step placement

| chain step | what happens | singularity status |
|---|---|---|
| 1–3 (action → Stokes → Hecke) | q₀ holonomy lands in `H_n(q)`; q generic | none (semisimple) |
| 4 (Wedderburn) | `⊕_λ M_{d_λ}`; Frobenius Gram det = Schur elements `s_λ(q)` | **roots of unity** (Schur-element zeros) — on the unit circle |
| 5 (Frobenius pairing) | `tr_M = Σ_λ y_λ χ_λ`, `y_λ ~ 1/s_λ`; `F = Q_β/[Q_A cos α_eff]` born as a **ratio**; `c_k` = its `u`-ladder coeffs, `u = b·ℏ_q²` | ratio creates a **new** singularity, not at a root of unity |
| 6 (confinement SDP → τ@q₀) | SDP fixes `Q_A`, `cos α_eff`, selects `T_w`; τ evaluates `F` at `u_substrate` | **near-real simple pole at `u_substrate`** |

## Established facts (cite these)

1. **Radius of convergence of `Σ c_k u^k` = `u_substrate`** — `c_{k+1}/c_k →
   1/u_substrate ≈ 117.4` at k=8,9,10 ([PR #1713](https://github.com/litlfred/qou/pull/1713),
   [`qbeta_singularity_type_probe.py`](../../folio-assistant/computations/qbeta/qbeta_singularity_type_probe.py)).
2. **Simple pole**, residue `A ≈ 1.804e-15` at `u = u_substrate`
   ([PR #1727](https://github.com/litlfred/qou/pull/1727)).
3. **Pole is near-real at q₀**: imaginary distance `ε ≈ |c_3|/|dc_3/dq| ≈ 4.4e-7`
   (called `b` in PR #1821 — **distinct** from the Hoefsmit `b` in `u = b·ℏ_q²`,
   and written `ε` not `δ` to avoid collision with the `Δ` family);
   the nearest root of unity (`ζ₁=1`, `|q₀-1| ≈ 0.11`) is **~2.5e5× farther**
   ([PR #1821](https://github.com/litlfred/qou/pull/1821)). ⇒ the residue-A
   pole is **NOT** the step-4 Schur-element (root-of-unity) singularity.
4. **Finite-RoU evaluation refuted independently**: the `/25` denominator is
   `1/[5]_q²`, pinned at the `q=1` (N→∞) fibre point where `[5]_q² → 25`, not
   any finite root ([PR #1811](https://github.com/litlfred/qou/pull/1811)).
5. **A is precision-limited to ~4 sig figs** with only `c_2…c_10` — extrapolation
   fails (PR #1805). The limiter is asymptotic convergence (rung count), not
   arithmetic precision.
6. **Only `c_2 = -1` is canonical** (Kashiwara `f̃₁²`); `c_3` empirical/refuted-
   real-q, `c_4` empirical/fit, `c_5+` open (registry §3).

## The keystone (what the unblock IS)

The fibre object `F` satisfies a **q-difference equation**
`F(qξ) = R(q,ξ)·F(ξ)` (the recursion block,
`prop:q-beta-c-k-recursion-from-habiro-q-difference`, sorry-free **conditional**
scaffolding). The kernel `R(q,ξ)` induces the `c_k` linear recursion
`c_{k+1} = Σ_j a_j(q₀) c_{k+1-j}`. **Deriving `R` is the keystone:**

```
R(q,ξ)  ⟹  c_k recursion  ⟹  canonical c_11…c_15  ⟹  A to high precision
        ⟹  structural identification of A
```

This is **categorical work at the Frobenius-pairing ⟷ SDP-duality junction**,
not numerology — which is exactly why the real-q and root-of-unity attacks
looked in the wrong place: the object is the *ratio's near-real analytic
structure*, governed by the SDP normalization, not a cyclotomic evaluation.

## Interpretive synthesis (NOT yet derived — flagged)

The following is a structural reading, consistent with the infra but unproven:

- **Two dualities meet here.** (i) The **Frobenius self-duality**
  `H_n(q) ≅ H_n(q)*` produces the `y_λ` weights; its degeneracies are the
  root-of-unity Schur-element zeros (*not* our pole). (ii) The **confinement
  SDP primal–dual** has shadow prices `(y₀*, y*)` (the `lp_dual_solver` infra);
  per CLAUDE.md *"the dual variables ARE the binding-energy shadow prices."*
- **Hypothesis:** residue `A` is a **dual/shadow-price quantity of the
  confinement SDP at a strict-complementarity boundary**, and q₀'s CAL-2 (τ_n)
  pinning places the SDP solution *at* that boundary — which *is* the near-real
  pole. (Cf. `2026-06-03-qbeta-sdp-strict-complementarity-partial.md`: marginal
  strict complementarity = a boundary singularity.)
- **Why `c_3` is hyper-sensitive** (`dc_3/dq ≈ 4.6e6`): it is a high-order
  coefficient of `F`, and τ evaluates `ε ≈ 4e-7` from `F`'s pole. The `c_k`
  swing and the residue-A ~4-sig-fig ceiling are **the same phenomenon** —
  proximity to one near-q₀ singularity.

## Concrete plan (this branch)

1. **Kernel first cut** — linear-recurrence / C-finite analysis of the existing
   `c_2…c_10` (from `qbeta-decay-sdp-extended-ck.witness.json`): Hankel-rank
   minimal recurrence order; rigorously extend the "no constant kernel ≤ d=4"
   result (commit `eca145ca`); extract the best determinable kernel `{a_j}`;
   **check whether the characteristic polynomial's dominant root = 1/u_substrate**
   (the pole). Report what the data CAN and CANNOT pin about `R`.
2. **Lean** — formalize the pole↔recurrence claim that grounds the extraction:
   *a rational `F(u) = P/Q` with `deg Q = d` ⇒ `c_k` is order-`d` C-finite with
   characteristic polynomial `Q^rev`, and the pole `u_substrate` is a root of
   `Q`.* This makes "find `R`" ≡ "find the minimal `Q`" rigorous.
3. **Honest verdict** — what order/structure the existing `c_k` support, and the
   precise additional input (canonical `c_11+` OR a categorical derivation of
   `Q_A·cos α_eff`'s zero) the kernel still needs.

## Anti-pattern guards

- No ansatz/fit for `c_k`; the recurrence is *extracted and validated by
  overdetermination*, not fitted.
- TIERED honesty: established / interpretive / open kept separate.
- Diagnostic-only; no production wiring; the registry governs tiers.
