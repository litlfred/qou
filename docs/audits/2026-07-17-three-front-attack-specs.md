# Attack specs for the three named 1ppQ walls (owner-picked 1+2+3)

**Date:** 2026-07-17 · Companion to [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md).
Recon-distilled, pre-registered kill criteria; no fit, no c_k wired, no tier change.

## 1. D-ladder (Q_β odd channel) — the "more terms" arm, running

Probe [`qbeta_dladder_extension_singularity_probe.py`](../../computations/qbeta/qbeta_dladder_extension_singularity_probe.py):
extend the exact ℚ(√3) d_k past k=21 (ORD 43→63, targets k≈31) and re-measure
(a) the divergence-class C drift, (b) the Borel–Leroy s\*, (c) the dlog-Padé vs
root-test singularity gap. Decides **finite-k shadow vs structural q-Gevrey
drift** — the question the 07-13 probe explicitly left open. Note: the
upstream generating-function module takes ORD via argv (import-time).

## 2. Lawrence–Rozansky modulus ID (W_λ keystone, m_p/m_μ root cause)

Target: `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)` at fibre roots of unity, colors
mapped by McKay(2I↔Ê₈)∘(A₅⊂S₅), values on **marks** ([e]_q refuted). Reuse the
machine-validated Hikami machinery in
`computations/probes/keystone_valuemap_genuine_smatrix_s013.py` (τ_N Gauss sum,
Thm-10 exact anchor) and add the color-α insertion in the p₃=5 numerator; α=1
must reproduce bare τ_N to machine zero before any conclusion.
**Kill criteria:** ratio-vector mismatch at every N; the **D=2 collapse** (only
2 independent colored components — the decisive structural trap: the probe must
show how McKay-labelled coloring escapes it or it re-derives the existing
refutation); split node returning [6]_ζ instead of [5]_ζ+1; conjugation-modulus
violation. Success = evidence, not proof (the Lean `loc_matches` gate closes
only via derivation). Bib gap: `lawrence-zagier-1999`, `hikami2005brieskorn`
need `references.ts` entries before any Lean `-- Ref:`.

## 3. Bring-Jacobian photon determinant (α_EM single wall)

Target: derive `1/(πb₁) = 1/(8π)` as the photon 1-loop determinant
normalization on `J(M) = H¹/H¹(ℤ)` (dim 8; Jac(Bring) ~ E⁴ with E = Bring/S₄,
so the 8-dim determinant factors through one elliptic modulus). Mirror the
proved 1/(12π) template (mode count × per-mode weight × geometric identity;
arithmetic in Lean, identification cited). **First check (structural lead):**
the flat-torus scale anomaly `ζ_Λ(0) = −b₁` — the one place a bare b₁ *count*
(not an area/covolume) canonically appears in a ζ-regularized determinant.
**Kill criteria:** if every natural normalization yields Area/covolume factors
and never a bare b₁, record scope-(a) negative — do NOT stretch μ-scale
conventions until 8π appears (the ζ-determinant μ-dependence can absorb any
constant; that is the fitting trap). Any candidate reproducing 1/(12π) is the
9500σ-falsified branch. The working 1/(8π) is empirically selected — a
derivation must force it, not be reverse-engineered from it.

## Cross-references

Recon sources: `2026-07-14-alpha-em-2loop-derivability-map.md`,
`2026-07-12-keystone-wlambda-{derivation-mckay-e8-route,framing-is-phase}.md`,
`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`,
`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`;
ledgers `s5-so3-keystone.md`, `alpha-em.md`, `ck-dk-canonical-registry.md` (KC21/KC22).
