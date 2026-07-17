# Φ_b 2-loop follow-up: exact deformed shape (gluing), the −u·log z coupling refuted, and A₁ does not rescue the F1 k=21 gate

**Date:** 2026-07-17 · **Branch:** `claude/phib-2loop-followup-2026-07-17` ·
**Tier:** derived + scope-(a) negatives · **Discipline:** no `c_k` wired; no fit; L2 unchanged (2/7).
**Follows:** the merged Φ_b 2-loop b-dictionary (#3854, `6715ac2`).

Two owner-directed follow-ups to #3854 (options "2" then "1").

## (2) Exact two-variable deformed gluing — and the meridian coupling that ISN'T

#3854 recovered the deformed saddle `z*(q₀)` by a single-constraint Newton on
`Im V(z)=Vol(q₀)` (flagged there as the one modeling approximation). This probe uses the
**exact** Thurston figure-eight gluing `z(z−1)·w(w−1)=1`, `w=m²z` (corpus `solve_shape`):

    exact deformed shape  z*(q₀) = 0.4504458794 + i·0.7773944942
    #3854 approx  shape          = 0.4052940009 + i·0.9141863994   (DIFFERS)

So #3854's flagged caveat was **real**: the single-constraint shape is genuinely off, and
the correct deformed shape is the gluing solution. **But** the natural guess for the
deformed *potential* — the meridian coupling `V_u(z) = Li₂(z) − Li₂(1/z) − u·log(z)`
(`u = 2 ln q₀`) — is **refuted** by the critical-point gate:

    GATE D1:  V_u'(z*(q₀)) = −0.2995 + i·0.1061  ≠ 0   → the −u·log z coupling is REFUTED.

The exact deformed shape is not the critical point of `V_u`, so `−u·log z` is not the
right meridian term. **No deformed A₁ is claimed** (formalize-first: the gate withheld a
number built on a wrong potential). The precise open piece is now named: the correct 4₁
meridian-deformed potential whose critical point equals the gluing shape (a
Neumann–Zagier / Dimofte deformed action — the `−u·log z` ansatz is too naive; the
longitude/meridian NZ datum couples through the *pair* z, w=m²z, not a single `log z`).

## (1) Feeding A₁ to the merged F1 acceleration — a clean structural negative

Does the certified complete-structure b-dictionary `A₁ = 1/3 + 0.27263763·i` (#3854,
gated G1/G2/G3) rescue the merged F1 acceleration's k=21 estimator gap
(root-test radius 0.1692 vs ratio radius 0.1498, gap 0.0194)? **No — and structurally so:**

- The 2-loop b-dictionary normalizes the state-integral **prefactor**; in the
  coefficient plane it is an **overall scale** on the `d_k`.
- Root-test radius `|d_k|^{−1/k}` and ratio radius `|d_{k−1}/d_k|` are both
  **homogeneous of degree 0** in an overall scale ⇒ **invariant** under the A₁
  normalization. Measured: gap 0.0194 → 0.0194 (unchanged).

**Honest verdict:** the b-dictionary fixes the resummed **value's normalization**, not the
**singularity location**. It does *not* close the k=21 gate; the gate needs **more rungs**
(the merged k=31 extension already confirmed the q-Gevrey drift persists). This corrects a
plausible misconception — that the missing normalization was what stalled F1 at k=21 — with
a one-line scaling argument.

## Net

- **Derived/confirmed:** the exact deformed shape `z*(q₀)` (gluing) — #3854's approximation
  caveat was real.
- **Scope-(a) negatives (both clean):** the `−u·log z` meridian coupling is refuted (the
  correct deformed potential is the named open piece); and A₁, being scale-invariant, does
  not move F1's k=21 estimator gap.
- **Unchanged:** #3854's complete-structure A₁ (1/3 + 0.27263763·i, three gates) stands.
  L2 = 2/7; no `c_k` wired; coordinated with #3805 (even-channel GGM).

## Compute

- Probe: [`computations/qbeta/qbeta_phib_2loop_deformed_gluing_and_f1_feed.py`](../../computations/qbeta/qbeta_phib_2loop_deformed_gluing_and_f1_feed.py) (exit 0)
- Witness: `computations/qbeta/qbeta-phib-2loop-deformed-gluing-f1-feed.witness.json`

## Cross-references

- The merged 2-loop b-dictionary: [`2026-07-17-phib-2loop-bdictionary.md`](2026-07-17-phib-2loop-bdictionary.md)
- Merged F1 acceleration (the k=21 gate): [`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md)
- Gluing solver: `computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py`
