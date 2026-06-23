# Interface operator — per-bond factor derivation + 4-body ⁴He assembly

**Date:** 2026-06-23
**Branch:** `claude/pauli-young-delta-test-hgp6jc` (PR #2630)
**Follow-up to:** [`2026-06-22-pauli-young-spin-isospin-delta-lambda-test.md`](2026-06-22-pauli-young-spin-isospin-delta-lambda-test.md)
(the parameter-free Δ_λ test that pointed binding away from partition weights
and toward the dynamics-side interface operator)

Two tasks on the interface-product binding
`B(K) = E₀·(tr_M(W_free) − tr_M(W_atom)) = E₀·τ_vac·(1 − ∏ᵢ fᵢ)`,
`E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV`, `τ_vac = τ_p^Z τ_n^N`.

---

## Task 1 — the per-interface factor is categorically DERIVED (✓)

`closed_form_tau_M.py` assigns each nucleon–nucleon bond a Markov factor:
positive σ → `z`, negative σ⁻¹ → `z−h`, averaged → `z−h/2`
(`z = 1/(√q+1/√q)`, `h = q−1/q`). These are **not three independent
heuristics**: they follow by **trace-linearity from a single categorical input**.

- **(H1) Hecke skein** `(σ−q)(σ+1/q)=0 ⟹ σ⁻¹ = σ − h·I` — verified exact (sympy).
- **(H2) Bar-invariant (charge-symmetric) crossing** `½(σ+σ⁻¹) = σ − (h/2)·I` — verified exact.
- **(H3) Markov move** (the one input): `tr(x·σ_g) = z·tr(x)`. Then by linearity
  - `tr(x·σ⁻¹) = tr(x·σ) − h·tr(x) = (z−h)·tr(x)` — **negative factor forced**;
  - `tr(x·½(σ+σ⁻¹)) = (z−h/2)·tr(x)` — **averaged (pn) factor forced**.

Checked numerically on explicit Hoefsmit seminormal matrices in the (2,1) block of
H₃ (so `x` ranges over a genuine non-trivial lower algebra H₂, not just identity):
residuals `~1e-52`; the module's `interface_factor()` equals the derived `z`, `z−h`,
`z−h/2` exactly. `z` itself is the Jones-normalized Markov parameter (the trace
normalization `tr(1)=1` + the Markov move); the bar-averaged pn factor encodes the
pn bond's no-preferred-chirality (charge) symmetry. **Zero free parameters.**

→ `interface_factor_categorical_derivation_probe.py` · `interface-factor-categorical-derivation.witness.json`

**Reading:** the per-bond factor is solid. Whatever is wrong with binding is *not*
the value of an individual interface factor.

---

## Task 2 — 4-body assembly: topology is NOT the missing scale (clean negative)

The canonical closed form models an atom `p^Z n^N` as a **linear chain** (A−1
bonds). Physically ³He/³H is a triangle and ⁴He a **tetrahedron** (6 bonds). We
replaced the chain by the genuine many-body **complete graph K_A** (all C(A,2)
pairs) and recomputed binding.

Validated building blocks: `τ_p = 1.2203628890867` (cached, phase5l); `τ_n =
1.1948624254` solved from the canonical `tr_M(D)=τ_p τ_n z`. Reconstructing all
four canonical atom traces from `(τ_p,τ_n)` × chain product matches to `~1e-8`
(the residual is the bring-color δ flavor-split of the pn bond, ≈7e-5/bond).

| atom | #chain bonds | #K_A bonds | B_chain | B_K_A | AME |
|------|----:|----:|--------:|------:|-----:|
| ²H | 1 | 1 | 3.056 (+37%) | 3.056 (+37%) | 2.225 |
| ³H | 2 | 3 | 6.236 (−26%) | 6.765 (−20%) | 8.482 |
| ³He | 2 | 3 | 5.592 (−28%) | 6.522 (−16%) | 7.718 |
| ⁴He | 3 | 6 | 8.256 (−71%) | 8.820 (−69%) | 28.296 |

**The decisive, convention-robust observable — the A-scaling B(⁴He)/B(D):**

| | B(⁴He)/B(D) |
|---|---|
| linear chain | 2.70 |
| complete graph (tetrahedron) | 2.89 |
| **AME** | **12.72** |

The genuine 4-body topology moves the ratio only **2.70 → 2.89**, still **4.4× short**
of AME. Since the chain (A−1 bonds) and the complete graph (C(A,2) bonds) **bracket**
every intermediate bond-counting topology, none of them supplies the ⁴He
tight-binding spike.

**Why bond-counting can't fix it.** `B = E₀·τ_vac·(1 − ∏f)`. Each factor `f < 1`,
so `∏f → 0` quickly as bonds accumulate and the deficit `(1 − ∏f)` **saturates to 1**
— extra bonds barely change `B`. The only residual A-growth is `τ_vac = τ_p^Z τ_n^N`,
geometric and too weak (gives ratio ≈2.9, not 12.7). The strong A-scaling of binding
(≈ B/A saturation, and the ⁴He spike) is therefore **not** an interface-counting
effect in this multiplicative-deficit form.

→ `interface_4body_assembly_probe.py` · `interface-4body-assembly.witness.json`

---

## Combined conclusion + where the frontier actually is

- **Task 1**: the interface operator's per-bond factor is categorically forced
  (one Markov move + the skein) — no fit, no slack there.
- **Task 2**: the *topology* of the bond graph (chain vs tetrahedron) is **not**
  the missing physics; the multiplicative deficit `(1−∏f)` saturates, so binding's
  A-scaling cannot come from counting bonds.

So the real lever is **not** more/better bonds but the **assembly form itself**: the
multiplicative interface deficit on top of a geometric `τ_p^Z τ_n^N` is structurally
incapable of the observed A-scaling. Candidates the evidence now points at:
1. an **additive / log (linked-cluster)** interface term `∑ᵢ log fᵢ` rather than the
   multiplicative `1−∏f` (an additive form grows ∝ #bonds, which *could* track A);
2. an **A-dependent E₀ scale** (the energy normalization is currently A-flat);
3. genuinely off-the-trace binding (the ⁴He spike as a shell/supermultiplet closure,
   not a pairwise sum at all).

This complements the 2026-06-22 result: spin-isospin Δ_λ (A-flat) can't carry
binding, and now bond-counting topology (A-bracketed, saturating) can't either —
narrowing the search to the assembly *functional form* and the energy scale.

## Artifacts
- [`computations/probes/interface_factor_categorical_derivation_probe.py`](../../computations/probes/interface_factor_categorical_derivation_probe.py)
- [`computations/interface-factor-categorical-derivation.witness.json`](../../computations/interface-factor-categorical-derivation.witness.json)
- [`computations/probes/interface_4body_assembly_probe.py`](../../computations/probes/interface_4body_assembly_probe.py)
- [`computations/interface-4body-assembly.witness.json`](../../computations/interface-4body-assembly.witness.json)

## Cross-refs
- [`computations/closed_form_tau_M.py`](../../computations/closed_form_tau_M.py) — the interface product
- [`computations/binding_canonical.py`](../../computations/binding_canonical.py) — `B = E₀(tr_M_free − tr_M_atom)`
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ / binding ledger (PROBE 2 = A=4 interface)

---

## Follow-up — candidate #1: additive / log linked-cluster interface form

Task 2 showed the *multiplicative* deficit `B = E₀·τ_vac·(1−∏f)` saturates
(`(1−∏f)→1`), capping the `B(⁴He)/B(D)` ratio at ~2.7–2.9 vs AME 12.72. The
natural fix: an **additive / linked-cluster** interface term, where per-bond
contributions **sum** (grow ∝ #bonds) instead of multiplying (saturate).
`log[τ_M(atom)/τ_M(vac)] = ∑ᵢ log fᵢ`, so the per-bond binding strength carried
additively is `∑ᵢ(−log fᵢ) > 0`. Scanned forms (all with the *same* single scale
E₀, **zero** tuned parameters) × chain/complete topology
(`binding_additive_linked_cluster_probe.py`):

| form | B(⁴He)/B(D) | RMS\|err\| | note |
|------|----:|----:|------|
| M (multiplicative deficit) | 2.70 / 2.89 | 44 / 41% | baseline; saturates |
| L  `E₀·∑(−log f)` (complete) | 6.78 | **27%** | best RMS; ⁴He −30% |
| LV `E₀·τ_vac·∑(−log f)` (complete) | **9.89** | 96% | closest scaling; overshoots light |
| DV `E₀·τ_vac·∑(1−f)` (complete) | 9.36 | 38% | **⁴He = 28.60 MeV, +1.07%** |

**Reading — direction CONFIRMED, not a closure.** Every additive form out-scales
the multiplicative baseline (2.7 → 6.8–9.9), so summing over bonds is the right
A-scaling mechanism. Two notable parameter-free near-hits: `DV/complete`
reproduces **⁴He to +1.07%** (28.60 vs 28.296), and `L/complete` gives the lowest
overall RMS (27%). But none closes: the additive×τ_vac forms overshoot the light
atoms (D +37%, T +47%) because τ_vac multiplies a bond-sum that already grows,
and the pure-additive `L` then undershoots ⁴He (−30%). The residual is a
**saturation curve** (the empirical B/A ≈ const that peaks at ⁴He): the per-bond
`−log f` weights are A-flat, so they can't bend B/A. Closing it needs either an
A-dependent E₀ or a bond weight beyond the bare Markov factor — i.e. a genuine
additional input, not a re-parameterization of the existing factors.

So candidate #1 moves binding from "wrong A-scaling" (multiplicative, 4.4× short)
to "right A-scaling, wrong curvature" (additive, ⁴He to ~1% but light-atom
overshoot) — a real step, and it localizes the remaining gap to the
saturation/curvature term rather than the interface factor or topology.

→ `binding_additive_linked_cluster_probe.py` · `binding-additive-linked-cluster-scan.witness.json`
