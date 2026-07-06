# GAP-A-1 binding-operator-K SDP — feasibility assessment (scoping)

**Date:** 2026-05-31
**Branch:** `claude/gap-a1-binding-k-sdp-2026-05-31`
**Audience:** any agent picking up the Δ_λ-gated per-isotope binding problem
after #1591 / #1592 closed off the Hecke-character route.
**Status:** scoping + feasibility probe — **complete**.

> **Verdict (short): CIRCULAR — GAP-A-1 ⊆ Δ_λ.** Substrate-only data *does*
> uniquely fix the binding operator `K(²H) = σ₃²` (PSD-feasible +
> Markov-fingerprint, **no `B_AME`**). But the per-isotope binding consumes
> the mass-functor per-block component `M_λ(K)` (MeV), and `K`'s character
> `χ^λ(K)` does not determine `M_λ(K)` — the only available map `χ^λ → M_λ`
> ([`per_block_phi_q.fit_three_E0`](../../computations/_deprecated/per_block_phi_q.py))
> *fits* per-block energy scales `E₀^λ` to `{e⁻, p, n}`. The deuteron binding
> equation is **1 equation in `p(6)=11` unknowns `Δ_λ`** (10-dim solution set),
> underdetermined without an external `M_λ` source (≡ `B_AME`). So GAP-A-1's
> binding-K leg supplies the **same** `χ^λ` data #1591/#1592 already showed is
> insufficient. This is a clean negative — equal in value to a closure per the
> task discipline — and it **delimits exactly** the missing categorical input:
> a parameter-free `χ^λ(K) → M_λ(K)` map (substrate-derived per-block `E₀^λ`).
> See §4.

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

## 4. The decisive feasibility test (this branch)

> **Verdict: CIRCULAR — GAP-A-1 ⊆ Δ_λ.** The binding operator `K` **is**
> uniquely fixed from substrate-only data, but `K`'s per-block content is a
> *character* `χ^λ(K)`, not the *mass* `M_λ(K)` the binding formula needs.
> Fixing `M_λ(K)` from `K` is exactly the open Δ_λ(K) problem.

Probe: [`gap_a1_binding_k_sdp_feasibility.py`](../../computations/gap_a1_binding_k_sdp_feasibility.py)
→ [`gap-a1-binding-k-sdp-feasibility.witness.json`](../../computations/gap-a1-binding-k-sdp-feasibility.witness.json)
(deuteron ²H, A=2, n₀=6). No parameter tuned to `B_AME`; `B_AME` used only for
the final residual print.

### 4a. The good half: `K` IS substrate-determined (no B_AME)

`binding_k_enumerator.py` (Formulation B) selects the **unique shortest
PSD-feasible inter-nucleon binding** for ²H, `K = σ₃²` (Hopf `L_H`), from the
substrate-restricted generator set `{σ₃, σ₃⁻¹}` by PSD-feasibility (`α_gap = 0`)
+ Markov-trace fingerprint — **no `B_AME` in the objective.** So the §3.2
warning of #1591 ("the H_{3A} form needs the binding operator K") is *answerable*
at the level of identifying `K`: substrate data does pin `K`. (Caveat: the
enumerator's tie-break for ³H/³He is a min-length / positive-Hopf *convention*,
not a structural selector — it returns `σ₃²` for all three atoms; the genuine
8₁₁ / L6a4 bindings need the extended generator set. So even the "good half" is
only clean for ²H today.)

### 4b. The fatal half: `χ^λ(K)` ≠ `M_λ(K)` — the binding needs the mass, not the character

The canonical mass formula ([`prop:rho-k-h3a-refinement`](../../content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md))
defines

$$
  \Delta_\lambda(K) = \frac{M_\lambda(K) - m_e\, y_\lambda\, \chi^\lambda(\mathcal{B}_K)}{m_e\, y_\lambda\, \chi^\lambda(\mathcal{B}_K)},
  \qquad
  B(K) = m_e \sum_{\lambda \vdash 3A} y_\lambda\, \chi^\lambda(\mathcal{B}_K)\, \Delta_\lambda(K),
$$

with `M_λ(K)` the **mass-functor's λ-block component** (a MeV quantity).
Knowing `K` gives `χ^λ(K)` — a *dimensionless* Hecke trace. The probe computes
all 11 of them at H₆(q₀); with `Δ_λ ≡ 0` the Schur–Weyl identity
`Σ_λ y_λ χ^λ = |tr_M|` collapses the formula to the **constituent mass**
(zero binding). All the binding lives in `Δ_λ`, and `Δ_λ` is *defined through*
`M_λ(K)`, which `χ^λ(K)` does not determine.

**The only map `χ^λ → M_λ` in the repo is a fit.**
[`per_block_phi_q.py`](../../computations/_deprecated/per_block_phi_q.py)
(**deprecated**) gets per-block masses via `fit_three_E0` — a linear
least-squares fit of three per-block energy scales `(E₀^sym, E₀^std, E₀^alt)`
to `{e⁻, p, n}`. That is the circularity: to turn `K`'s character into a
binding, you fit the per-block MeV normalizations to known masses.

**The deuteron equation is underdetermined.** `B(D) = m_e·Σ_λ y_λ χ^λ Δ_λ` is
**1 equation in `p(6) = 11` unknowns `Δ_λ`** → a 10-dimensional affine solution
set. No amount of substrate-only `χ^λ(K)` data closes it; the missing input is
`M_λ(K)` (equivalently `B_AME`).

### 4c. SDP dual evidence (what the operator-selection SDP does and does not buy)

The operator-selection SDP over `K`'s Wedderburn blocks
(`solve_psd_operator_selection_sdp`, channels = blocks, `t_λ = -|y_λ·χ^λ(K)|`)
solves with **strong duality**:

| field | value |
|---|---|
| `primal_obj` | −3.958842e-01 |
| `dual_obj` | −3.958838e-01 |
| `duality_gap` | 4.18e-07 |
| `feasible` | true |
| dominant λ*(K) | `(4,2)` (by `|y_λ·χ^λ(K)|`) |

The dual `y_star` are the per-block shadow prices; they identify which blocks
`K` saturates. But the SDP selects the *dominant block*, it does **not** supply
`M_λ(K)`. So the dual variables — the binding-energy *shadow prices* of
AGENTS.md's LP/SDP-duals rule — confirm the block structure of `K` without
closing the MeV binding. This is the cleanest statement of why GAP-A-1 stalls
exactly where Δ_λ does.

### 4d. Relation to #1591 / #1592

#1592 proved the Kashiwara crystal trace `ρ_w` summed over the crystal equals
`χ^λ` (no freedom beyond the character). GAP-A-1's binding-K leg supplies the
**same** `χ^λ` data (now of the *binding* operator `K` rather than the atomic
braid), and #1591 proved `χ^λ`-only rules cannot separate the Markov-equivalent
atoms. The binding operator `K` does carry *more* structure than the
nucleon-trefoil characters — its block profile `χ^λ(K)` differs across atoms —
but the quantity the mass formula consumes is `M_λ(K)`, not `χ^λ(K)`, and the
`χ → M` step is the open Δ_λ determination. **GAP-A-1 ⊆ Δ_λ ∪ GAP-A-1's own
`M_λ` gap**, which is Δ_λ. No shortcut.

### 4e. What new categorical input would actually close L2 Subgoal-1

The probe delimits the missing piece precisely: a **parameter-free map
`χ^λ(K) → M_λ(K)`** — the per-block action of the Archimedean realization
functor in MeV — that does *not* fit `E₀^λ` to known masses. Candidate
directions (all *upstream* of GAP-A-1, none a 7th Δ_λ ansatz):

1. **Derive the per-block `E₀^λ` from the substrate** (not LSQ-fit them). This
   is the genuine open item; it is the per-block analogue of the single global
   `E₀ = m_e/(q₀(q₀−1))` scale, and is presently unknown.
2. **Option E crystal trace `ρ_w(K)`** (still "NOT EXIST" per #1591 §3.3) — if
   `ρ_w(K)` is derived from KLR/Lecouvey structure it would supply `M_λ` as a
   structural identity rather than a fit.
3. **Path B (Borromean tower)** bypasses Δ_λ entirely at the cost of the
   per-atom `λ(K)` substrate-derivation — a different open problem, not this one.

---

## 5. Cross-references

- `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` — #1591, A-3/A-4 ⊆ Δ_λ
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the Δ_λ gate
- `content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md` — GAP-A-1 conjecture
- `content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md` — Δ_λ formal definition
- `computations/binding_k_enumerator.py` — Formulation B search
- `tools/pyhecke/python/pyhecke/lp_dual_solver.py` — SDP dual solver
