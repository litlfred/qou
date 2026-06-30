# gm4q — generator-volume-decomposition binding blows up exponentially (8.25×10¹³ for ²¹⁰Bi)

**Bean:** `gm4q` (Author input needed).
**Block:** [`particle-interactions/generator-volume-decomposition`](../../content/quantum-observable-universe/particle-interactions/generator-volume-decomposition.md)
(+ `-proof`, + [`audit/generator-volume-decomposition-probe.md`](../../content/quantum-observable-universe/particle-interactions/audit/generator-volume-decomposition-probe.md)).
**Date:** 2026-06-30.

## The symptom

The probe reports the absolute binding `E(parent)` as the **sum of generator
volumes** `E = Σ_{i=0}^{A-2} V_i`:

| Nucleus | A | E(parent) |
|---|---|---|
| ²H | 2 | 1.174 |
| ⁴He | 4 | 4.136 |
| ¹⁴C | 14 | 47.17 |
| ⁶⁰Co | 60 | 3.89×10⁴ |
| ²¹⁰Bi | 210 | **8.25×10¹³** |

This is **super-exponential** in `A` and physically absurd: nuclear binding
**saturates** at `B/A ≈ 8 MeV/nucleon`, so `E(²¹⁰Bi)` should be `≈ 1.6×10³ MeV`,
not `10¹³` (of anything). The β-decay *differences* `ΔE` stay small for light
nuclei (²H `−0.174`) but are themselves contaminated for heavy ones
(⁶⁰Co `−3050`, ²¹⁰Bi `−6.24×10¹²`).

## Root cause (two compounding layers)

### Layer 1 — the volume is the *un-logged trace*; binding is its **log**

At generator `σ_i` the volume `V_i` is the **trace value** of a transfer-matrix
product over `k_i = A − i − 1` crossings (the `.md`'s `M_i = ∏_{j} T_j`). The
transfer matrix `T` (from `T² = (q−q⁻¹)T + 1`) has an eigenvalue `> 1` at the
substrate `q₀ > 1`, so

    V_i  ~  λ^{k_i},     λ > 1,

i.e. the volume grows **exponentially in the crossing count** `k_i`. At ²¹⁰Bi,
`k_0 = 209`, so `V_0 ~ λ²⁰⁹` — astronomical. Summing such volumes gives the
`10¹³`.

**This is the bug.** The canonical binding is the **logarithm** of the trace
ratio, not the trace itself:

    B_sym = α · ln( tr_free / tr_atom ),     α = E₀ = m_e / (q₀(q₀−1)),

(the production form, [`mass_binding_dashboard.py`](../../computations/mass_binding_dashboard.py);
audit `2026-06-16-b-sym-linear-chain-closed-form.md`). Under the log,
`ln(V_i) ~ k_i·ln λ` is **linear** in the crossing count, removing the
exponential: `Σ_i ln V_i ~ Σ_i k_i`, a *polynomial*.

### Layer 2 — all-pairs crossings give `A²`; saturation needs **adjacency** bonds

Even after logging, the decomposition uses **all-pairs** crossings —
`k_i = A − i − 1` at each generator, so

    Σ_{i=0}^{A-2} k_i  =  A(A−1)/2  =  binom(A,2),

which is **quadratic** in `A`. A `B ∝ A²` binding still over-binds heavy nuclei
(real `B ∝ A`). Physical **saturation** — the short range of the nuclear force —
means a nucleon binds only to its **neighbours**, not to all other nucleons. The
canonical saturating binding uses exactly the `(A−1)` **adjacency** bonds of the
monotone atom word:

    B_sym = α[ (Z−1)L_pp + L_pn + (N−1)L_nn ]   — linear in A ⇒ saturates,

with the parameter-free per-nucleon plateau
`a_V = E₀·ln(1/W_free) ≈ 7.584 MeV/nucleon ≈ empirical net B/A`
(merged PR #3131, [`probes/su4_occupancy_binding_probe.py`](../../computations/probes/su4_occupancy_binding_probe.py)).
The `binom(A,2)` all-pairs count is the same quadratic over-binding the
mass-binding dashboard's `B_qCLT_fac = α·(A−1)·⟨L⟩` already avoids by using
`(A−1)` bonds, not `binom(A,2)` pairs.

## Recommendation (the author input requested by gm4q)

The generator-volume-decomposition's **absolute** binding `E = Σ V_i` should be
replaced by the canonical **log-of-adjacency-chain** form already in production:

1. **Take the log.** Report `B = α · Σ_bond ln(suppression)` — the log-suppression
   per bond — not the raw trace volume `V_i`. This alone turns `8.25×10¹³` into a
   polynomial and is mandatory (the absolute volume is not an energy).
2. **Restrict to adjacency bonds** `(A−1)`, not all-pairs `binom(A,2)`, so the
   binding is **linear in A and saturates** at `a_V ≈ 7.584 MeV/nucleon`. The
   short-range/saturation physics is *why* only neighbours count.

**What stays valid.** The *jet-expansion* structure (1-jet = β-decay generator-
volume **difference**, 2-jet = double-β cross-term) is a sound organising
principle — it is a *difference of logs*, which is well-behaved. Only the
**absolute** binding `E = Σ V_i` (un-logged, all-pairs) is wrong; the small-A
`ΔE` look reasonable precisely because the exponential has not yet dominated. The
fix is to express the jets as variations of the canonical `B_sym` (log,
adjacency), not of the raw volume functional.

## Disposition

This is a **(a) scope-limited correction**, not a refutation of the
decomposition idea: the generator/jet bookkeeping is fine; the absolute-energy
*normalisation* (un-logged trace, all-pairs) is the defect, and the canonical
saturating form (`B_sym` / `a_V`) is the established fix. Recommend the block
adopt the log-adjacency normalisation and cite the saturation constant; the jet
machinery can be re-expressed as variations of `B_sym`.
