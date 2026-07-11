# Jet-filtration residue weight w_n(K) — the q-difference kernel R(q,x) derive-or-refute

**Date:** 2026-07-11 · **Bean:** t7qv (θ_λ magnitude gate) · **Axis:** A≥3
binding closure · **Tier:** numerical derive-or-refute (scope-(a) negative) ·
**Discipline:** no fit, no value wired, no tier change. Probe
[`binding_wn_kernel_derive_refute.py`](../../computations/binding_wn_kernel_derive_refute.py).

## Context

The na-Stokes / Reeb jet-filtration binding
`B_strong(K) = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` has two factors: the **derived
extensive kernel** `a_D^(n)=lw(n−1)` (the super-exponential SW period / mean
quantum dimension — Lean-proved extensive in `QOU.Mass.JetFiltrationExtensive`,
sorry-free) and the **open residue weight** `w_n(K)`. Option #2 of the
[jet-filtration audit](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)
is the decisive backstop: does `w_n` follow a *parameter-free* q-difference
recursion `G(qx;q)=R(q,x)G(x;q)` (the conjecture's own prescription), or is it a
fit?

## Method (no per-isotope fit)

1. **Coulomb correction** `B_strong = B_AME + E_Coulomb` (from `coulomb_energy.py`)
   isolates the strong sector: D 2.225, ³H 8.482, ³He 8.716, ⁴He 29.203 MeV.
2. **A=3 mirror universality** — after Coulomb, ³H (pnn) and ³He (ppn) agree to
   **+2.73 %** (charge-symmetry-breaking, a small separate effect), so a
   body-order-only `w_n` is admissible.
3. **Extract** universal `w_2, w_3, w_4 = 4.353, 9.331, 15.919` (ratios
   w₃/w₂ = 2.143, w₄/w₃ = 1.706) from D / avg(³H,³He) / ⁴He — three equations,
   three unknowns, no tuning.
4. **Test** the ratios against parameter-free derived kernels.

| candidate R(q,n) | pred w₃/w₂ | pred w₄/w₃ | max \|err\| |
|---|---|---|---|
| geometric (r32 = r43?) | 2.143 | 1.706 | 22.7 % |
| R = [n]_q | 1.514 | 1.350 | 29.4 % |
| R = a_D self-ratio | 1.337 | 1.894 | 37.6 % |
| R ∝ n | 1.500 | 1.333 | 30.0 % |
| **R = [n]_q²** | **2.291** | **1.823** | **6.9 %** (lone near-miss) |

## Verdict — REFUTED (scope-(a))

No parameter-free derived kernel reproduces both ratios to 5 %. **`[n]_q²`** is
the lone near-miss (6.9 %), notably echoing the **`√C_λ` amplitude near-miss**
(11.14 vs 12.72, ~12 %) of the merged compact-weight PR #3518 — the true weight
sits *between* the q-integer and its square in both probes, a cross-probe
"squared-q-dimension near-but-not-exact" signature. A recursion tuned to
reproduce the three `w_n` would be a banned **seventh Δ_λ ansatz**.

This **confirms** the corpus finding
([`2026-07-06-reeb-flow-pn-magnitude-...md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md)
§2j tranche 8): the residue weight `w_n(K)` **is the Δ_λ / W_λ gate in
disguise** — free per-body-order data carrying the same irreducible content, not
a recursion output.

**Scope-(a), not (b).** This is "*this parameter-free recursion, alone,* does not
fix `w_n`" — **not** a structural exclusion of the mechanism. Two permanence
points stand:

- The na-Stokes extensive kernel `a_D^(n)=lw(n−1)` is a **permanent, correct
  contribution** (Lean-proved extensive) — refuting the *recursion form of the
  multiplier* says nothing against it.
- The **un-refuted route** is option #1: `w_n` = hyperbolic link-volume of the
  n-body inter-nucleon sub-link (a topological invariant, the literal
  "hyperbolic volumes via na-Stokes"; merges with gap #2). That needs SnapPy
  volumes, not a recursion — a separate compute, not a fit.

Owner-gated closure = the geometric `W_λ` knot-ideal projector (s5-so3 keystone,
narrow 2026-06-19 reversal). No production touch; no value wired; no tier change.

## Cross-references

- Jet-filtration audit (mechanism half): [`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)
- "w_n IS the Δ_λ gate" invariant: [`2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md) §2j
- √C_λ amplitude near-miss (prior probe): [`2026-07-11-he4-binding-subppb-reverse-fit-trace.md`](2026-07-11-he4-binding-subppb-reverse-fit-trace.md) §4b (PR #3518)
- Δ_λ gate status: [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md), Option-E ledger [`docs/coordination/option-e.md`](../coordination/option-e.md)
