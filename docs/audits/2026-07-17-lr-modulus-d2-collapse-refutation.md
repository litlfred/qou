# The Lawrence–Rozansky modulus ID via SU(2)-fibre coloring is refuted — D=2 collapse (scope-(a))

**Date:** 2026-07-17 · **Axis:** W_λ keystone / m_p–m_μ root cause (s5-so3) ·
**Tier:** numerical (structural gate; scope-(a) negative) · **Discipline:** reuse
only; no fit; no W_λ value wired; the Lean `loc_matches` gate untouched; no tier
change.

## The gate

The W_λ keystone's last open piece (per the 07-12 McKay-Ê₈ value map +
framing-is-phase) is the modulus identification
`|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)`, colors mapped by
McKay(2I↔Ê₈)∘(A₅⊂S₅) onto the 4 conjugacy classes of `λ⊢5`. Before any
amplitude transcription, one structural gate is decisive (the recon's flagged
trap): does the SU(2)-colored order-5 fibre carry **4 independent modular
components** (needed for the 4 classes), or collapse to **2**?

## Result — D=2 collapse confirmed

[`keystone_lr_modulus_d2_collapse_test.py`](../../computations/probes/keystone_lr_modulus_d2_collapse_test.py)
(reusing the merged, machine-validated Σ(2,3,5) colored-false-theta machinery):

| color α | support (mod 60, folded) |
|---|---|
| 1 | {1, 11, 19, 29} |
| 2 | {7, 13, 17, 23} |
| 3 | {7, 13, 17, 23} |
| 4 | {1, 11, 19, 29} |

The supports **fold pairwise** — `α=1 ≡ α=4`, `α=2 ≡ α=3` (the `α ↔ 5−α`
symmetry of the false-theta support). The Ψ-value matrix over a 5-point q-grid
inside the convergence disk has **numerical rank 2** (singular values
`9.07, 0.50, 3.1e-41, 1.3e-42`).

So the SU(2)-fibre coloring spans only **2 independent components**, while the LR
modulus ID needs **4**. The identification via this insertion is therefore
**refuted (scope-(a))**: the order-5-fibre SU(2) coloring cannot carry the 4
value-map classes. This re-confirms the pre-existing bare-vs-4-dim refutation at
the *colored* level, and matches the standard `Σ(2,3,5)` fact that its SU(2)
vacuum row is 2-dimensional (golden-ratio φ).

## Consequence

A genuine geometric derivation of `W_λ` cannot come from SU(2)-coloring the
Σ(2,3,5) Seifert fibre. The recon-identified alternative is a **different
insertion** — knot-complement `Ẑ` / `F_K` blocks (which carry the full colored
dependence) — now the sharpened target for the W_λ keystone. The McKay value map
`d_q(λ) = [mark]_q` and framing-is-phase results are untouched; only *this*
route to the modulus is closed. Nothing is wired; the Lean gate closes only by
derivation.

## Cross-references

- Value map + framing (the two proved legs): [`2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md), [`2026-07-12-keystone-wlambda-framing-is-phase.md`](2026-07-12-keystone-wlambda-framing-is-phase.md)
- Colored machinery reused: [`../../computations/probes/keystone_colored_sigma235_wrt.py`](../../computations/probes/keystone_colored_sigma235_wrt.py)
- Attack spec + kill criteria: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md)
- Ledger: [`../coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
