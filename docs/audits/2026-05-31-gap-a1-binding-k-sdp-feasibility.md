# GAP-A-1 binding-operator-K SDP — feasibility assessment (scoping)

**Date:** 2026-05-31
**Branch:** `claude/gap-a1-binding-k-sdp-2026-05-31`
**Audience:** any agent picking up the Δ_λ-gated per-isotope binding problem
after #1591 / #1592 closed off the Hecke-character route.
**Status:** scoping + feasibility probe (in progress).

> **Verdict (short):** TBD — see §4. This document scopes the K-SDP precisely
> and asks the single decisive question: is the binding operator `K(𝔥)`
> determined by **already-canonical data alone** (substrate `q₀`, characters
> `χ^λ`, weights `y_λ`, the nucleon braids), or does fixing it require feeding
> in `B_AME` (the experimental binding energy) — the circularity #1591 warned
> about?

---

## 1. Why GAP-A-1 is the named forward lever

#1591 (`docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md`) proved
**GAP-A-3 (brane level `n_⋆`) and GAP-A-4 (prefactor `ρ`) both reduce to
Δ_λ**, and #1592 showed the genuine per-vertex Kashiwara crystal trace `ρ_w`
summed over the crystal equals `χ^λ` exactly (1.6e-49) — so there is **no
freedom beyond `χ^λ`** in the character data. The Markov-equivalence theorem
(proton/neutron/³He share bit-identical `χ^{[2,1]}=1.99418581`, `y=0.28092963`
yet need `ρ ∈ {1,1,2}`) means **no function `f(χ_λ, y_λ)` can separate them.**

#1591 §6 names the one upstream lever that is *not* a 7th Δ_λ fit:

> **GAP-A-1 (canonical-knot identification) first.** GAP-A-4's own closure path
> says ρ "closes as a corollary of GAP-A-1" — once the canonical binding
> operator `T_w(K) ∈ H_{3A}` is *uniquely fixed by the R5-full SDP from
> substrate + constituents alone* (no AME), its dominant λ* is determined and ρ
> follows. … it would simultaneously give `K` (⇒ ρ via A-4) and `K`'s block
> profile (⇒ Δ_λ).

The premise being tested here: **`K` carries per-block Wedderburn content that
`χ_λ` alone does not** (the Markov-equivalent atoms differ in their *binding
operator*, not in their nucleon-trefoil characters). If true, K-SDP is a
genuine non-circular lever. If extracting `B` (hence Δ_λ) from a known `K`
still needs a fitted normalization, GAP-A-1 reduces to Δ_λ like A-3/A-4.

---

## 2. The precise GAP-A-1 statement (from canonical sources)

### 2a. The factorisation (`conj:canonical-knot-id-sdp` §"Structural decomposition")

$$
  T_w(\mathfrak{H}) \;=\; K(\mathfrak{H}) \cdot \bigotimes_{i=1}^{A} T_w(\text{nucleon}_i)
  \qquad \text{in } H_{3A}(q_0),
$$

splitting into:

- **(a) Constituent uniqueness** — each `T_w(nucleon_i)` is the unique
  PSD-feasible canonical element at `H_3(q_0)` (the trefoil
  `(σ_1 σ_2^{-1})^3`). **Closed numerically** (R5-minimal,
  `joint_tower_sdp_solver_v2.py`).
- **(b) Binding-K uniqueness** — `K(𝔥) ∈ H_{3A}(q_0)` is the unique
  PSD-feasible Hecke element satisfying the joint-tower SDP cross-level
  consistency constraints. **Open** — this is the GAP-A-1 core.

| Nucleus | A | n₀=3A | binding K | constituents | ρ |
|---------|---|-------|-----------|--------------|---|
| ²H | 2 | 6 | `L_H` (Hopf) | {p, n} | 1 |
| ³H | 3 | 9 | `8₁₁`-class link | {p, n, n} | 2 |
| ³He | 3 | 9 | `L_{6a4}` | {p, p, n} | 2 |

### 2b. The two SDP formulations already in the repo (CRITICAL distinction)

The conjecture block states the SDP **objective two different ways**, and the
distinction is exactly the circularity question:

**Formulation A — the `B_AME`-in-the-objective SDP (`conj:canonical-knot-id-sdp` §Statement).**

$$
  \min_{T_w,\,\rho \in \mathbb{Z}_{>0}}
  \bigl\| \rho \cdot [\,|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,] \cdot \mathfrak{E}_0 \;-\; B_\mathrm{AME}(\mathfrak{H}) \bigr\|^2
$$

This **feeds `B_AME` into the cost.** Its global minimizer is by construction
the `T_w` whose mass formula reproduces the experimental binding — that is a
fit, not a derivation, and is the circularity #1591 warns against.

**Formulation B — the PSD-feasibility + Markov-fingerprint search
(`binding_k_enumerator.py`).** K is selected by: (i) PSD-feasibility per
Wedderburn block (`α_gap = 0` — the "binding-stability certificate"), and (ii)
Markov-trace fingerprint match against the *historical* `T_w(𝔥)`
(NOT against `B_AME`). This is **substrate-only** — no experimental binding in
the objective.

**The decisive question** (§4): does Formulation B (no `B_AME`) *uniquely* fix
`K`, and if so, does `K`'s per-block content yield `B` / Δ_λ **without** a
separate `B_AME`-fitted normalization?

---

## 3. Existing scaffold (survey 2026-05-31)

| Component | File | What it does | Uses B_AME? |
|---|---|---|---|
| **K factorisation evaluator** | `binding_k_solver.py` | Presupposes historical `T_w`; computes `K = atom_word ++ cp_inv_word`, per-block χ/det/eigs at H_{3A}. NOT a search. | no (but presupposes the historical braid) |
| **K explicit enumerator** | `binding_k_enumerator.py` | SEARCHES K over inter-nucleon generators; filters PSD-feasible; ranks by Markov-residual vs `z^{n₀−n_braid}·tr_M(T_atom)`. | no (ranking uses Markov fingerprint, not B_AME) |
| **R5-full canonical SDP** | `r5_full_canonical_knot_solver.py` | First substrate-only SDP check; ³He PSD-feasible α*=0, ²H α*=0.891 (needs multi-term cost). | (Formulation A cost compares to B_AME) |
| **SDP dual entry point** | `pyhecke/lp_dual_solver.py` `solve_psd_operator_selection_sdp(t,G,n_target)` | diagonal PSD lift `M(x)=diag(Gx)≽0`; emits X*, Z*, primal/dual/gap/eigenvalues. | n/a (generic solver) |
| **ρ-prefactor verifier** | `rho_prefactor_structural_verifier.py` | proves H_3-level `f(χ,y)` impossibility (the Markov-equivalence theorem). | no |

**Sibling overlap note.** #1582 ("real per-nucleus SDP") is a sibling working
the same area. This branch does NOT depend on its unmerged work; intent posted
on its PR. The scaffold above is all on `main`.

---

## 4. The decisive feasibility test (this branch) — VERDICT PENDING

(filled in once the probe runs — see §4 update below)

---

## 5. Cross-references

- `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` — #1591, A-3/A-4 ⊆ Δ_λ
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the Δ_λ gate
- `content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md` — GAP-A-1 conjecture
- `content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md` — Δ_λ formal definition
- `folio-assistant/computations/binding_k_enumerator.py` — Formulation B search
- `tools/pyhecke/python/pyhecke/lp_dual_solver.py` — SDP dual solver
