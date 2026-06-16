# Q_β heat-route — the bar-odd `a_1` gate (structural prune/support)

**Date:** 2026-06-13
**Probe:** [`computations/qbeta/qbeta_heat_kernel_a1_gate_probe.py`](../../computations/qbeta/qbeta_heat_kernel_a1_gate_probe.py)
**Scope:** tests the ONE gate for the §3-bis q-heat-kernel candidate for the open
`c_k`-recursion kernel `R(q,ξ)`
([`2026-06-10-qbeta-ck-state-of-play-synthesis.md`](2026-06-10-qbeta-ck-state-of-play-synthesis.md) §3-bis;
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).
**Discipline:** STRUCTURAL test only — NO `c_3` value is claimed or wired. A pass
is a positive signal for the candidate family (kernel `R` / assembly f-map still
open); a fail prunes a route. Per the flip-flop guard
([`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)),
`c_3` remains **near-match, not derived**.

## The gate

The synthesis requires the kernel's leading recursion coefficient to be
**bar-ODD** with `a_1 = −c_3 = √2·Φ₂ ≈ 2.07` (targets `2.0693` proton-anchor,
`2.0202` muon-anchor). The per-mode heat kernel is
`A_λ(t) = 1 − (q−1)·μ_λ·t` with `μ_λ(q) = ℏ_q²·Σ_□ [c]_q[c+1]_q`
(`ℏ_q=(q−1)/q`, Jackson `[k]_q`), so `a_1` is driven by the t-coefficient
**`(q−1)·μ_λ`** summed over active modes (elementary-symmetric `e_1` of the
per-mode kernels).

## Finding 1 — bar-parity selects the leading modes (positive signal)

`(q−1)·μ_λ` is **exactly bar-ODD** (`a(q⁻¹)/a(q) = −1`) **iff** the partition's
nonzero content-Casimir terms are dominated by the `c=1` cell:

| λ | `(q−1)μ_λ` @ q₀ | bar-ratio | parity |
|---|---|---|---|
| **(2)** | 0.0022781 | **−1.000** | **ODD** |
| **(2,1)** | 0.0022781 | **−1.000** | **ODD** |
| (3) | 0.0098916 | −0.855 | no |
| (1,1,1) | 0.0016658 | −1.870 | no |
| (4),(3,1),… | — | `≈ −q^{2c−1}` | no |

**Why (closed form).** `(q−1)μ_λ = (q−1)³/q² · Σ_□ [c]_q[c+1]_q`. The prefactor
`(q−1)³/q²` has bar-ratio `−q`; each Casimir term `[c]_q[c+1]_q` has bar-ratio
`q^{1−2c}`. For (2) and (2,1) the **only** nonzero term is the `c=1` cell's
`[1]_q[2]_q` (bar-ratio `q^{−1}`), and `(−q)·q^{−1} = −1` — exact bar-oddness.
Partitions with cells at `c≥2` or `c≤−1` mix bar-ratios → not odd.

Crucially, **(2)/(2,1) are the physically-leading heat-flow modes** (after the
`μ_(1)=0` equilibrium): the Peter–Weyl doc states "(2) and (1,1) contribute the
leading Reeb-invariant heat-flow." So the **bar-odd character the gate needs is
present, in exactly the right modes** — the gate effectively *selects* the
`c=1`-dominated leading modes.

## Finding 2 — magnitude is far off at the raw level (open)

Raw `(q−1)μ_λ ≈ 0.002–1.5` vs target `2.069` — a `~1.3×` (H₆ d_λ-weighted,
closest) to `~900×` (single (2) mode) gap. The Habiro `(u;u)_m → u^k`
change-of-basis (the open f-map; NOT applied in this probe) must bridge it. A
`~900×` factor for the single-mode case is large and not a clean power of
`1/u ≈ 117`; **unresolved**.

## Finding 3 — the q-dilog / q-hyperbolic route FAILS the gate (prune)

The Peter–Weyl doc notes the q-dilogarithm generates `Σ_λ log μ_λ`. Tested as an
alternative `a_1` source: bar-ratio `+0.86…+0.97` (**leans EVEN, not odd**),
magnitude `2–70×` off. **Fails both gate criteria.** This is consistent with the
catalogued refutations — `Li_2^q ×` spectral as mech #7 (PR #1609) and the
"Bloch–Wigner/dilog on non-hyperbolic links → `D(z)=0`" failure mode (the Hopf
link is non-hyperbolic). The productive q-hyperbolic content is the
**cyclotomic / roots-of-unity (ζ₄) skeleton** that `[c]_q` already supplies to
the heat kernel — not the dilog/volume itself.

## Verdict

| route | bar-parity | magnitude | verdict |
|---|---|---|---|
| **heat-kernel `(q−1)μ_λ`** (= q-difference) | **exact ODD** in (2)/(2,1) | off ~900× raw | **promising; right structure, magnitude open** |
| q-dilog `Σ log μ_λ` (q-hyperbolic) | not odd (leans even) | 2–70× off | **pruned on the gate** |

The §3-bis heat-route candidate is **not refuted and shows a genuine positive
bar-structure signal** in the leading modes; the open work is (a) the
change-of-basis that bridges the magnitude gap and (b) the multi-mode assembly
(f-map) that weights toward the (2)/(2,1) modes so the *sum* is cleanly bar-odd
(the unweighted sum is only `≈ −1.006`). The q-dilog route is the trap, now with
a compute-backed gate failure. **No `c_3` value derived or wired.**

## Finding 4 — the ε-order: heat-kernel structure is at ε³, NOT the ε¹ trap

Numerically (log-log slope as `q→1`), `(q−1)μ_λ` enters at **`ℏ_q³ = u^{3/2} = ε³`**
(ε ≡ √u) for every mode — its leading term is the `c=1` cell
`ℏ_q²·[1]_q[2]_q·(q−1) ≈ 2(q−1)³`. Placing the three objects on the ε-ladder:

| object | ε-order | u-order |
|---|---|---|
| Δtr_M block (`−2 = J_Hopf`) | **ε¹** | √u |
| **heat-kernel `(q−1)μ_λ`** | **ε³** | u^{3/2} |
| target `c_3` (`a_1`) | **ε⁶** | u³ |

This matters: the catalogued **accidental coincidence** (PR #1593) is that the
**ε¹** Δtr_M block `≈ −2` numerically matches `c_3` (at **ε⁶**) across a 5-order
gap. The heat-kernel bar-odd structure enters at **ε³** — a *different, higher*
order than that trap — so it is **not** the same accidental mechanism. The f-map
obligation becomes an **ε³ → ε⁶ structural lift** (factor `~ε³ = u^{3/2}`), to be
supplied by the Habiro `(u;u)_m→u^k` change-of-basis composed with the heat-time
↔ ladder `t ↔ u` identification — and it must be **bar-equivariant** so the
proved ε³ bar-oddness survives to `a_1`. That is the precise, bounded proof
obligation this probe isolates (it does not discharge it).

## Cross-references
- Synthesis §3-bis (heat route): [`2026-06-10-qbeta-ck-state-of-play-synthesis.md`](2026-06-10-qbeta-ck-state-of-play-synthesis.md)
- Recursion engine: [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
- μ_λ spectrum: [`prop:q-heat-kernel-peter-weyl`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.md)
- Depth-1 kernel (Lean): `QOU.BraidKnot.QBetaPreArchHeatDepthOneKernel`
- Tiers (flip-flop guard): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
