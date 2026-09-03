# Is the germ on the full tower? No — it is underdetermined, hence representation-specific (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** "germ is on the full tower?"
**Scope:** scope-(a); a conceptual result + one retraction; no MeV, no fit, nothing wired.
**Probe:** [`magnus_germ_underdetermination_probe.py`](../../computations/deltalambda/magnus_germ_underdetermination_probe.py)
**Follows:** #6432 (two-row characters reduce to the 2-dim R-matrix, but the germ does not, 6.5% off).

## The question

#6432 found the germ `Ω₂` is representation-dependent (the 2-dim R-matrix reproduces two-row
*characters* to 140 digits but the germ-inserted trace by only 6.5%). The natural question:
is the germ a canonical **full-tower** object (a connection / q-curvature, as the corpus frames
it in `prop:germ-commutator-q-curvature`), so that the seminormal per-irrep computation is one
gauge of a single tower object? **Answer: no.** The germ is underdetermined by the algebra.

## The mechanism (verified exact)

The germ `A = q·(∂σ)·σ⁻¹` satisfies `{σ,σ'} = h'σ + h·σ'` (`h = q−q⁻¹`, `h' = 1+q⁻²`), from
differentiating the Hecke relation `σ² = hσ + 1`. In σ's eigenbasis (eigenvalues `q, −q⁻¹`),
per entry `(i,j)`: `(λ_i + λ_j − h)·σ'_{ij} = h'λ_i δ_{ij}`.

- **Diagonal** `i=j`: `2λ_i − h ≠ 0`, so `σ'_{ii}` is **fixed** ⇒ `A_ii = q·h'/(2λ_i − h) = ±1`
  (`+1` on the symmetric `q`-channel, `−1` on the antisymmetric `−q⁻¹`-channel).
- **Off-diagonal** `i≠j`: `λ_q + λ_₋ = q − q⁻¹ = h`, so the coefficient **vanishes** and
  `σ'_{ij}` is **FREE**.

Verified on a **genuine** 2×2 σ block (`σ_1` on `(2,1)`, off-diag(σ)=1.735): the σ-eigenbasis
**diagonal is `±1` in both** the seminormal and the R-matrix realizations (constraint-fixed),
while the **off-diagonal differs** — seminormal `0.171`, R-matrix `1.43`. Both are valid germs
(both pass `{σ,σ'} = h'σ + h σ'`); they differ only in the free part.

## Answer

**The germ is not a canonical full-tower object.** It is underdetermined by the differentiated
Hecke relation — its σ-eigenbasis diagonal is universal (`±1`) but its off-diagonal is free, so
*every* realization of an irrep gives its own germ. The seminormal per-irrep germ (which the
whole `qou-o6ov` arc uses, `base.germ_csr`) is **one specific gauge**; the Schur–Weyl full-tower
R-matrix germ is another. They disagree on genuine blocks, which is exactly why the two-row
R-matrix trace missed by 6.5% (#6432). The physical decay object
`P(A) = Σ_λ y_λ tr(ρ_λ Ω₂)` is therefore well-defined **specifically in the seminormal gauge**;
the "germ-commutator = q-curvature" connection is realized in that gauge, not as a
gauge-invariant tower object.

## Retraction (caught in-session, not shipped)

Because the diagonal is `±1`, I briefly conjectured the seminormal germ was the *channel-sign*
operator `A = 2P_q − I = (2σ − h)/[2]_q` (a closed form linear in σ), which would give
`Ω₂ = (4/[2]_q²)Σ[σ_g,σ_{g+1}]` — a major simplification. **This is FALSE and is retracted.**
It holds **only where σ is diagonal** (1×1 blocks, e.g. `σ_0` on `(2,1)`); the first check used
exactly that degenerate case and showed a spurious zero off-diagonal. On a **genuine** 2×2
block the matrix identity fails (`max|A − (2σ−h)/[2]_q| = 0.27`), because the seminormal germ has
a real nonzero off-diagonal (`0.171`) that is *not* linear in σ. The germ is genuinely richer
than the channel sign; there is no closed form `A = (2σ−h)/[2]_q`.

## Consequence for the arc

- **The arc's results stand** — every probe used the seminormal germ consistently, and that is a
  well-defined (if gauge-specific) object.
- **What is now precise:** the decay object lives in the seminormal gauge, not on a
  gauge-invariant tower; a "germ-natural" construction beyond hooks (#6432) must reproduce the
  *seminormal* off-diagonal, which the R-matrix does not. The exterior-power hook reduction
  (#6430) worked precisely because `Λʲ` of the seminormal `V` preserves the seminormal germ.
- **Open:** whether a gauge-invariant (curvature) formulation exists in which the decay is
  cleaner — i.e. whether the free off-diagonal can be fixed by a naturality condition that both
  makes the germ canonical *and* keeps the seminormal answer.

## Bottom line

No — the germ is not on the full tower. The differentiated Hecke relation fixes only its
σ-eigenbasis diagonal (`±1`) and leaves the off-diagonal free, so the germ is
representation-specific; the seminormal per-irrep germ is the arc's gauge, and the full-tower
R-matrix germ is a different valid one (verified: same diagonal, different off-diagonal). A
tempting channel-sign closed form is false on genuine blocks and is retracted. The two-row
mismatch (#6432) is now explained at the mechanism level.
