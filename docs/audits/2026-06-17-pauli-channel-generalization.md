# Pauli-channel generalization — `Δ_λ` via spin-isospin Young symmetry (2026-06-17)

**Library:** [`computations/channel_binding.py`](../../computations/channel_binding.py)
(`weighted_channel_binding`, `PAULI_WEIGHTS`, `STANDARD_WEIGHTS`).
**Status:** structural generalization **built + verified**; the
`Δ_λ`-closure claim is **novel but UNTESTED** (a decisive
formalize-first test is specified below). Δ_λ-gated — must derive, not fit.

## The generalization

The 2-body Pauli-channel rule (pp/nn → alternating Hecke channel,
pn → standard) is the **n=2 special case** of a per-channel
**weighting**:

    B(K) = E₀ · Σ_bonds n_bond · Σ_ch w(bond, ch) · log(1/f_ch)

`weighted_channel_binding` implements this; `PAULI_WEIGHTS` reproduces
`B_pauli_ch` and `STANDARD_WEIGHTS` reproduces the production kernel
(both verified to machine precision).

**The lift.** The two 2-nucleon Hecke channels (symmetric `+q`,
alternating `−q⁻¹`) **are the two irreps of S₂**. For a k-nucleon
cluster they generalize to partitions **λ ⊢ k** — the Wedderburn blocks
of `H_k(q)` — and the weighted sum becomes the framework's per-isotope
formula

    B(K) = m_e · Σ_{λ ⊢ 3A} y_λ · χ^λ(β_K) · Δ_λ(K).

So **`Δ_λ` is the k-body generalization of the per-channel weight
`w(bond, ch)`** — and generalizing the Pauli-channel lands exactly on
the open Δ_λ problem.

**Deuteron reframing.** A weight of `≈0.572` on the pn standard channel
gives the deuteron exactly (`0.572·E₀·log(1/f_pn) = 2.224 MeV = AME`).
The persistent "fractional `f_pn=0.588` coupling" *is* a per-channel
weight. The whole open problem becomes: **derive the per-λ channel
weight from Pauli-Young symmetry.**

## Why this is a NEW Δ_λ angle (corpus-grep verified)

Per the corpus-grep discipline, checked against the six refuted ansätze
+ the 18-closure chain ([`2026-05-18-delta-lambda-gating-context.md`],
[`gap-a-path-b-lambda.md`], [`option-e.md`]). **None** used isospin,
Pauli antisymmetrization, or spin-exchange to set `Δ_λ`:

| ansatz | what set Δ_λ | uses Pauli/isospin? |
|--------|--------------|:-:|
| A Occam single-support | min \|Δ\| | no |
| B Frobenius co-Casimir | `1/dim_q(λ)` | no |
| C Demazure-fibre | `y_λ·D_w/D_{w₀}` | no |
| D LP-Plancherel/Frobenius | shadow price | no |
| E crystal-graph | Kashiwara mult. | no |
| F augmented Markov | augmented axioms | no |
| **current production** | `sgn(w₀^{S_λ'})·dim(V_λ)` (Macdonald sign + Burnside dim) | **no** |

Isospin enters only at the **bond-count** level (`n_pp=C(Z,2)`,
`n_pn=Z·N`, `n_nn=C(N,2)`, `derive_binding_bond_type.py`) — never at the
per-partition Δ_λ level. The Pauli factor `F_Pauli=0.6382` exists but
for **Q-values / weak-projection**, not Δ_λ. Type-B folding is the
**bar-involution** (`χ^λ ↔ χ^{λ'}` character transpose), not a
Pauli-weight determination. **Verdict: the spin-isospin Young-symmetry
projection for Δ_λ is genuinely novel — orthogonal to the refuted set.**

## The decisive test (formalize-first — NOT yet done)

Novel ≠ correct. For this to be a *derivation* (not the seventh fitted
ansatz the gate bars), the per-λ weight must come from **spin-isospin
representation theory**, with **zero tuned parameters**:

1. **State the projection.** For a configuration with `Z` protons + `N`
   neutrons, the spin-isospin state of each k-nucleon cluster has a
   definite Young symmetry (Pauli: the total wavefunction is
   antisymmetric). Define `Δ_λ(K)` as the overlap / projection of that
   spin-isospin Young symmetry onto the spatial Wedderburn irrep λ ⊢ 3A
   (e.g. via the inner product of `χ^λ` with the induced
   spin-isospin character, or the conjugate-partition `λ'` content).
2. **Derive, do not fit.** Compute the resulting `Δ_λ` from the
   projection alone and feed `B = m_e·Σ_λ y_λ χ^λ Δ_λ`. **No free
   constant.** In particular it must reproduce the deuteron's `0.572`
   pn-channel weight from the spin-triplet/isospin-singlet structure of
   the deuteron — not by tuning.
3. **Pass/fail.** If the parameter-free projection reproduces the AME
   light-isotope bindings (or fails cleanly), report it. If it needs a
   tuned normalisation to match, it is **refuted** as the seventh
   ansatz — the discipline review will (correctly) reject it.

This test is decidable and substrate-grounded. It has not been run; it
is the genuine open next step the generalization exposes.
