# The naive per-pair magnitude `z` is PHYSICAL at A=2 (deuteron) but still does NOT close it — the A=4 scope-(b) exclusion completed, plus the two-model reconciliation

**Date:** 2026-08-02 · **Branch:** `claude/deltalambda-magnitude-deuteron-2026-08-02` · **PR #4615** ·
**Axis:** Δ_λ / deuteron binding magnitude · **Tier:** derivation probe (formalize-first,
derive-then-check) · **Verdict:** HONEST NEGATIVE — scope-(a) insufficiency at A=2 + scope-(b)
cross-A death of the uniform-`z` mechanism.

**Scope (STRICT):** nothing fitted; nothing wired; `B_AME` used only as a diagnostic ratio,
never inverted; `free_parameters = 0`; L2 unchanged.

- Lean: [`QOU/MassTheory/DeuteronNaiveZMagnitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronNaiveZMagnitude.lean)
  — Mathlib-free core Lean, `lean`-direct **exit 0**, sorry-free (`decide`), wired into the QOU umbrella.
- Probe: [`computations/deltalambda/deuteron_naive_z_physical_probe.py`](../../computations/deltalambda/deuteron_naive_z_physical_probe.py)
  · witness `deuteron-naive-z-physical-but-does-not-close.witness.json` (50 dps mpmath, all assertions pass).

## 0. BLUF

The A=4 interface-magnitude audit
([`2026-08-02-a4-interface-magnitude-one-scalar-gate.md`](2026-08-02-a4-interface-magnitude-one-scalar-gate.md))
proved the naive uniform per-pair magnitude **`z = 1/[2]_v`** (`v = √q₀`, a derived substrate
object) is scope-(b) **EXCLUDED for ⁴He**: the `[1⁴]` complete-graph exchange spectrum
`{±√5, ±1}` gives `det(I + z·S) = (1 − 5z²)(1 − z²) < 0` because `5z² > 1` (`z ≈ 0.4993 > 1/√5`).
That exclusion is A=4-specific — the `√5` eigenvalue is the 2p+2n complete graph. The audit
**left the deuteron explicitly unchecked**.

This note runs the derive-then-check. **The deuteron (A=2, 1p+1n) has exchange graph `K₂`,
spectrum `{±1}`, `det(I + m·S) = 1 − m²`, ceiling `m < 1`, and `1 − z² = 0.751 > 0` — so `z`
is PHYSICAL there.** Yet it still does **not** close the deuteron, under any 0-fit scale.
Result: the naive-uniform-`z` per-pair mechanism is **dead across A** — excluded where it is
NEEDED (A=4) and insufficient where it is PHYSICAL (A=2).

## 1. Derive (locked before compute, 0-fit)

| object | definition | value | nature |
|---|---|---|---|
| `z = 1/[2]_v` | `[2]_v = √q₀ + 1/√q₀` | `0.499320334` | derived Markov bond factor |
| `g_reeb` | `1/√(5 + (q₀−1)²/q₀)` | `0.446730` | derived q-Reeb eigenphase (C_knot audit candidate #1) |
| `b₂(m)` | `−ln det(I + m·S_{K₂}) = −ln(1 − m²)` | — | A=2 connected cumulant |
| `m_e`, `μ₀`, `E⁺` | `m_e`; `m_e/(3h/2)`; `m_e[3]_q[4]_q/3` | `0.511`, `1.630`, `2.131` MeV | the only derived MeV scales |

Master-Σ deuteron binding (committed, pinned weight): `B_cat = m_e·|S(D)| = 0.511 × 0.7438 =
0.380 MeV`; `B_AME(²H) = 2.2246 MeV`; fitted deficit `C_knot = 5.853`.

## 2. Check — `z` is physical at A=2 but does not close it

**Physicality (the derived cited invariant).** The *same* derived `z`:

| | A=2 (`K₂`, `{±1}`) | A=4 (`[1⁴]`, `{±√5,±1}`) |
|---|---|---|
| determinant | `1 − z² = +0.7507` | `(1 − 5z²)(1 − z²)` with `1 − 5z² = −0.245` |
| sign | **> 0 (physical)** | **< 0 (excluded)** |
| writhe ceiling | `m < 1` | `m < 1/√5 = 0.4472` |

`z ≈ 0.4993` sits **below** the A=2 ceiling `1` but **above** the A=4 ceiling `1/√5`. Lean
`z_physical_A2_but_excluded_A4` (decide, scaled integers).

**Insufficiency (derive-then-check, no 0-fit closure).** With `z` physical, the A=2 cumulant is
`b₂(z) = −ln(1 − z²) = 0.2868` — a *reduction* (`< 1`), pointing the wrong way for a `5.85×`
deficit. Three independent 0-fit reads, all short:

| candidate closure (0-fit) | value | target |
|---|---|---|
| interface-as-binding `E_s·b₂(z)`, `E_s ∈ {m_e, μ₀, E⁺}` | `0.147 / 0.467 / 0.611` MeV | `2.2246` |
| required scale to hit `B_AME` | `E_s = 7.757` MeV | undrivable (no derived scale) |
| master-Σ dressing `B_cat/(1 − z²)` | `0.506` MeV | `2.2246` (one factor `< 2×`) |
| required dressing exponent `(1−z²)^{−k}` | `k = 6.16` | non-integer, no structural `k` |

`g_reeb` behaves the same (`b₂ = 0.2227`; required scale `9.99` MeV; required exponent
`k ≈ 7.94`). The `k ≈ 7.94 ≈ 8` for `g_reeb` is a **numerology-trap near-coincidence** — it is
not exact and there is no structural reason for `det^{−8}`; **not chased**, per the standing
single-knot-count / clean-number guard.

Lean `one_interface_factor_insufficient`: `1/(1−z²) < 2` (since `z² < 1/2`) ⟹ `2·B_cat < B_AME`
by a wide margin (`0.760 < 2.225` MeV).

**Structural reinforcement — the deuteron is not a `[1^A]` singlet.** The `−ln det(I+G)` cumulant
is **He4-LOCAL**: `rank Λ^A(ℂ⁴) = C(4,A)`, and only `A = 0, 4` are the rank-1 SINGLET (closed
shell); `A = 2` has rank `C(4,2) = 6`. So the He4-local `[1⁴]`-singlet cumulant has **no reason
to transfer** to the deuteron in the first place — applying it there (even with a physical `z`)
is doubly inappropriate. Lean `deuteron_not_singlet` (`C(4,2)=6 ≠ 1 = C(4,4)`).

## 3. Verdict (honest)

- **scope-(a):** the derived per-pair magnitudes `z`, `g_reeb` — physical at A=2 — do **not**
  close the deuteron; no 0-fit scale or structural dressing exponent reaches `B_AME`.
- **scope-(b) (cross-A):** the uniform per-pair magnitude `z = 1/[2]_v` cannot be the binding
  mechanism at any A — it is EXCLUDED at A=4 (`det < 0`, cited invariant = the `{±√5,±1}`
  spectrum) and INSUFFICIENT at A=2. This **completes** the A=4 audit's open thread: the naive
  `z` route is dead, not merely A=4-excluded.
- **What survives (unchanged):** the deuteron magnitude is a genuine per-knot Δ_λ / χ^λ-magnitude
  object above the chirality-cancellation floor (`C_knot` audit §5), NOT reachable by any derived
  per-pair magnitude, uniform scale, level-only rescale, dimension, or writhe factor. The named
  surviving opening (C_knot audit candidate #1, the q-Reeb `Δθ_λ`) is here shown, at least in its
  naive uniform-`g_reeb` per-pair reading, to also fall short — differences only, not magnitude.

## 4. Reconciliation context — the two deuteron binding models (NOT overclaimed)

For the reader's orientation (this section asserts no new derivation): the corpus carries **two
distinct** deuteron binding formulas with very different accuracy, and they are **not** reconciled.

| model | formula | deuteron | scope |
|---|---|---|---|
| **master-Σ** (binding conjecture) | `B = m_e·|Σ_{λ⊢6} y_λ χ^λ (−1)^{n(λ)} f^λ|` | `0.380 MeV` (**−82.9%**, `C_knot = 5.85` fitted) | uses the full H₆ Wedderburn decomposition; non-universal across isotopes (#4556) |
| **rotational E_unit** | `B = E⁺(1 + g₂ h²)`, `E⁺ = m_e[j]_q[j+1]_q/3`, `j = n/2 = 3` | `2.2238 MeV` (**−0.036%** at `g₂=1`) | uses ONLY the highest-weight rep; the deuteron is the UNIQUE isotope where this works — A≥3 fails 37–69% ([`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md)) |

The rotational route closes the deuteron to `−0.036%` with `g₂ = 1.0087` a **near-match**
(underived; the three derivation attempts — cosh `9/8`, BCH `0`, parity sweep — all failed,
[`2026-07-25-eunit-g2-derivation-attempt.md`](2026-07-25-eunit-g2-derivation-attempt.md)), and the
residual `r = g₂−1 = +0.87%` is the **binding residual magnified by `1/h²`**, needing the deuteron
predicted to `~36 ppm` ([`2026-07-26-deuteron-r-is-binding-residual-magnified.md`](2026-07-26-deuteron-r-is-binding-residual-magnified.md)).

A relevant structural fact (from [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md) §2):
the deuteron pn-channel word is `σ₁³` — a **single generator** — so the Magnus inter-crossing
commutator tower vanishes exactly (`[X,X]=0`), and `exp(Ω₁)` is exact. The `g₂ h²` correction the
model needs is therefore **not** of braid-word (inter-crossing) origin; the surviving candidate is
the **transverse NA-Stokes surface-curvature pairing** on the pn Seifert surface — "data the corpus
lacks." So both open deuteron residuals — the master-Σ `C_knot` and the rotational `g₂` — point at
the same missing surface/transverse object, at two different starting magnitudes. **This is
recorded as a reconciliation observation, not a proof that the two residuals are the same object.**

## 5. Anti-fit ledger

| statement | status |
|---|---|
| `z` physical at A=2 (`1−z² > 0`), excluded at A=4 (`1−5z² < 0`) | **Lean sorry-free (decide) + probe** |
| `b₂(z) = 0.287` a reduction; no derived scale reaches `B_AME` (needs 7.76 MeV) | **measured, 0-fit** |
| one A=2 interface factor `< 2×` ⟹ `2·B_cat < B_AME` | **Lean sorry-free** |
| required dressing exponent `k = 6.16` (non-integer); `g_reeb k ≈ 7.94` near-8 NOT chased | **measured, guard-flagged** |
| deuteron not a `[1^A]` singlet (`C(4,2)=6 ≠ 1`) | **Lean sorry-free** |
| uniform-`z` per-pair mechanism dead across A | **Lean + probe** |
| the deuteron binding magnitude derivation | **OPEN** (`qou-3q7t` lineage; GAP bean filed) |

`z = 1/[2]_v`, `g_reeb`, `m_e`, `μ₀`, `E⁺` all derived; `B_AME` used only as a diagnostic ratio,
never inverted; nothing wired; exact mpmath 50 dps.

**Refs:** A=4 exclusion [`2026-08-02-a4-interface-magnitude-one-scalar-gate.md`](2026-08-02-a4-interface-magnitude-one-scalar-gate.md),
[`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py) (#3924);
C_knot non-universality [`2026-08-02-c-knot-nonuniversal-pinned-weight.md`](2026-08-02-c-knot-nonuniversal-pinned-weight.md) (#4556);
rotational route [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md),
[`2026-07-26-deuteron-r-is-binding-residual-magnified.md`](2026-07-26-deuteron-r-is-binding-residual-magnified.md).
