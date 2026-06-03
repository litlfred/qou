# Q_β pre-archimedean recursion — steps 1/2/3 status

**Date:** 2026-06-02
**Branch:** `claude/qbeta-habiro-recursion-and-bridge-2026-06-02` (PR #1739)
**Scope:** Owner directive "1 y 2 y 3 y" — (1) symbolic c_k extraction, (2) integrality/Habiro membership, (3) bridge Lean. Honest per-step status.

## Established (pre-archimedean, exact) — the recursion

`z(q) = √q/(1+q)` satisfies `(4+6w+2w²)·z′ + w·z = 0` (`w = q−1`), giving

```
4(n+1)·a_{n+1} + 6n·a_n + (2n−1)·a_{n−1} = 0,   a₀=1/2, a₁=0
```

and the one-parameter family for `z^k`:

```
4(n+1)·b_{n+1} + 6n·b_n + (2(n−1)+k)·b_{n−1} = 0,   b₀=(1/2)^k, b₁=0
```

Verified exact to 12 orders; generates all coefficients with no q₀/CODATA. This is the **recursion ↔ q-difference equation** identity. (`qbeta_prearchimedean_z_recursion.py`)

## Step 3 — bridge Lean: PARTIAL (the recursion, sorry-free) ✅

`content/quantum-observable-universe/lean/QOU/BraidKnot/MarkovParameterRecursion.lean` formalises the recursion **sorry-free**:

- `markovParamCoeff : ℕ → ℚ` — the recursion-defined sequence
- `markovParamCoeff_two/_three/_four` — exact values (`−1/16`, `1/16`, `−13/256`)
- `markovParamCoeff_recursion` — the defining relation `4(n+2)·a_{n+2} + 6(n+1)·a_{n+1} + (2n+1)·a_n = 0`, proved by `field_simp; ring`

This is the **q-difference equation a Habiro element would satisfy** — a concrete step toward the bridge. The FULL bridge instance (`QbetaHabiroTaylorBridgeClass` in `habiro-precision-ladder-equivalence.lean`) is NOT discharged: it requires the c_k ↔ Habiro-Taylor identification, which is blocked by step 1 below.

(Lean toolchain sandbox-blocked — release.lean-lang.org unreachable; CI `lean_ci.yml` verifies.)

## Step 1 — symbolic c_k extraction: OBSTRUCTED (the open f-map)

The precision-ladder c_k do NOT come directly from the bare-z recursion. Three obstructions, all pre-existing-open:

1. **Rational q-dependent weights.** `τ_M(T_β) = A(q) + B(q)·z(q)` with `A, B ∈ ℚ(q)` (from the `z²,z³ → q/(1+q)²` reductions). Hence `τ_M`'s `a₁ ≠ 0` (witness: `a₁/a₀ = 0.145`) whereas bare `z` has `a₁ = 0` in **both** `w` and `ℏ_q` variables (verified). So `τ_M`'s recursion is higher-order than z's, carrying the `A, B` structure.

2. **Variable reparametrisation.** The ladder is in `u = b·ℏ_q²`; the recursion is in `w = q−1`. Connecting them is a (pre-archimedean, derivable) change of variables, not yet done.

3. **The `Q_A·cos` baseline + archimedean weights.** The c_k descend from `τ_M` via the `Q_A·cos` comparison (structural_finding's "finite algebraic exercise"), AND the NF weights `d_k` come from the min-L2-norm SDP solved at q₀ (archimedean, not yet q-rational).

Together these three are the long-documented **open "f-map"** (`f: Δtr_M(√u) ↦ Q_β(c_3 at u³)`, audit `2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`; eigenphase falsified at u¹, `2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`). This branch did NOT close it — it characterised it precisely (the three obstructions above) and supplied the bare-z recursion as the clean pre-archimedean backbone.

## Step 2 — integrality / Habiro membership: BLOCKED on step 1

Habiro-ring membership is a property of the **correction factor** `Π(1+c_k u^k)`, which requires the symbolic c_k from step 1. Without them, the integrality `(q;q)_n ∈ ℤ[q]` test cannot be run on the right object.

Partial observation: the bare-z coefficients `a_n` have **dyadic denominators** (powers of 2) — `a_n ∈ ℤ[1/2]`. This is a 2-integrality signature but is the *Taylor*-expansion structure, NOT the *cyclotomic* `(q;q)_n` integrality that defines Habiro membership; they should not be conflated.

## Honest bottom line

- **Real, new, exact:** the pre-archimedean recursion / q-difference equation for the Markov parameter (z and z^k), extending coefficients to all orders, formalised sorry-free in Lean.
- **NOT closed:** the connection from this backbone to the precision-ladder c_k (the f-map: rational weights + reparametrisation + archimedean baseline), hence the integrality test and the full bridge instance remain open.
- This sharpens "the c_k are derived not fitted" from *aspiration* to *a precisely-located gap* — the f-map — with the holonomic backbone now in hand.

## Cross-references

- Recursion probe: `folio-assistant/computations/qbeta/qbeta_prearchimedean_z_recursion.py`
- Lean: `content/quantum-observable-universe/lean/QOU/BraidKnot/MarkovParameterRecursion.lean`
- Habiro-ladder Lean (bridge target): `content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.lean`
- Scope: `docs/coordination/2026-06-02-qbeta-habiro-recursion-prearchimedean-scope.md`
- f-map audits: `docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`, `docs/audits/2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`
