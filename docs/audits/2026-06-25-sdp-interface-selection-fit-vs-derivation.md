# Confinement SDP knot-operator selection — structural (derivation), Δ_λ-gated binding

**Date:** 2026-06-25 (rewritten — see Retraction below)
**Branch:** `claude/great-ramanujan-g5m05s` · PR #2754
**Verified by running:** [`computations/gap_a1_binding_k_sdp_feasibility.py`](../../computations/gap_a1_binding_k_sdp_feasibility.py)
**Collective probe:** [`computations/probe_collective_binding_residual.py`](../../computations/probe_collective_binding_residual.py)

## Retraction (what this doc originally got wrong)

The first version of this audit (and the now-removed
`probe_sdp_interface_selection.py`) treated the canonical confinement SDP as
if it **fit the p-n interface crossing to the measured binding `B_AME`**, then
argued "per-isotope selection is fitting." **That was a straw man — wrong on
two counts:**

1. **Wrong object.** I varied the scalar interface crossing `d` *inside the
   mass word* `atom_braid_word_3A`. The SDP does not select that; it selects
   the **binding knot operator `K`** in `B = m_e·Vol(K)·Δtr` (a different
   object in a different binding model).
2. **Wrong objective.** The SDP does **not** minimise `‖B − B_AME‖`. It
   selects `K` by a **structural least-action criterion** with **no
   experimental input** (`B_AME` enters only as a downstream residual check).

The interface probe, its witness, and the "joint-tower-optimal" comment added
to `atom_braid_word_3A` are retracted. What follows is the verified correct
picture.

## What the confinement SDP actually selects (structural — a derivation)

Per [`prop:operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp.md):
the knot operator `Φ = Σxᵢbᵢ` is selected by **minimum categorical action**

$$\min_x \sum_i t_i x_i = \mathrm{tr}_M(\Phi)\quad\text{s.t.}\quad Gx \ge 0\ (\text{Frobenius positivity}),\ \textstyle\sum_i x_i = n_{\text{target}},$$

with `tᵢ = tr_M(bᵢ)`, `Gᵢⱼ = tr_M(bᵢbⱼ)` — **all Hecke-algebra data, no
experimental input.** For the nucleon, B₃ = (σ₀σ₁⁻¹)³ is independently the
**crossing-minimal Brunnian** link ([`confinement-operator-selection.md`](../../content/quantum-observable-universe/particle-interactions/confinement-operator-selection.md), "uses no physical input").

### Deuteron p-n → ²H — verified output of `gap_a1`

The substrate-only enumerator (`binding_k_enumerator.py`: shortest PSD-feasible
word in `{σ₃, σ₃⁻¹}`, Markov-fingerprint ranked, **NO B_AME**) selects

$$K(^2\mathrm{H}) = \sigma_3^2 = \text{Hopf link } L_H.$$

Running `gap_a1_binding_k_sdp_feasibility.py` (q₀ = 1.10998, m_e = 0.51100 MeV):

- **Per-block χ^λ(K)** at H₆(q₀) for all 11 partitions of 6; dominant block
  **λ\*(K) = (4,2)** by |y_λ·χ^λ|.
- **Operator-selection SDP over K's Wedderburn blocks** (canonical
  dual-emitting `solve_psd_operator_selection_sdp`): `primal_obj = −0.395884`,
  `dual_obj = −0.395884`, **`duality_gap = 4.18e-7`, feasible = True** — strong
  duality holds; the structural selection is internally consistent.

**So the operator selection IS a derivation** — exactly as the framework
claims and as the owner pointed out. There is no fit here.

## The genuine open gap — the binding *energy* is Δ_λ-gated

`gap_a1`'s decisive verdict (verbatim): knowing `K` gives its **dimensionless
character** χ^λ(K); the binding *energy* needs the mass-functor per-block
component `M_λ(K)` (MeV), with `Δ_λ(K) = (M_λ − m_e y_λ χ^λ)/(m_e y_λ χ^λ)`.
The deuteron binding equation

$$B/m_e = \sum_{\lambda \vdash 6} y_\lambda\,\chi^\lambda(K)\,\Delta_\lambda$$

is **1 equation in p(6) = 11 unknowns Δ_λ** — a 10-dimensional underdetermined
solution set. The only known map χ^λ → M_λ (`per_block_phi_q.fit_three_E0`) is
a **fit** to {e⁻, p, n}. Verdict: **`GAP-A-1 ⊆ Δ_λ`** — the operator is
derived; closing the binding energy is the gated Δ_λ problem (six ansätze
failed; AGENTS.md Δ_λ gate).

**Net:** the place a fit currently hides is **not** the operator selection
(structural) but the **binding-scale map** χ^λ(K) → MeV. That is where the
keystone effort (beans `w5tg`/`z2bn`/`thb7`, `conj:canonical-knot-id-sdp`)
belongs.

## Collective-residual corroboration (this PR's surviving contribution)

[`probe_collective_binding_residual.py`](../../computations/probe_collective_binding_residual.py)
characterises the binding-scale residual structurally (no fit). Per-nucleon
binding across ²H–¹⁶O shows two signals:

- **General collective under-binding** — `F = B_AME/B_sym` rises 0.94 (³H) →
  2.11 (¹⁶O).
- **⁴He α-magic local spike** — over the A=3↔A=6 interpolation of `B/A`, ⁴He's
  excess is **+98% in AME** but only **+4%** in the additive chain: a per-bond
  additive sum cannot make a doubly-magic α-core singularity.

This **independently corroborates** the `a567-atom-knot-sdp` workplan's
finding that `f(Z,N) = Vol(K)/8G` is a **magic-shell-closure** quantity
(⁴He f = 8.29 ≫ 6 pairs, +47%), *not* pairwise — i.e. the missing binding-scale
factor is 4-body (⁴He / Borromean α-core), the same channel `gap_a1`'s Δ_λ gate
points at. Scope: a structural narrowing (a), not a closed form.

## Reproduce

```bash
cd computations
python3 -u gap_a1_binding_k_sdp_feasibility.py     # structural K=σ₃² selection + Δ_λ gate
python3 -u probe_collective_binding_residual.py    # collective-residual structural form
```

(`gap_a1`'s SDP-duals step needs `cvxpy`; the collective probe is pure-python.)
