# Φ_b 2-loop follow-up: exact deformed shape (gluing); −u·log z coupling refuted; the A₁↔d_k role is the open question for the F1 k=21 gate

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

## (1) Feeding A₁ to the merged F1 acceleration — the real open question is the A₁↔d_k role

Does the certified complete-structure b-dictionary `A₁ = 1/3 + 0.27263763·i` (#3854,
gated G1/G2/G3) rescue the merged F1 acceleration's k=21 estimator gap
(root-test radius 0.1692 vs ratio radius 0.1498, gap 0.0194)? **This turns entirely on
how A₁ enters the D-ladder — which is not pinned here.** Two candidate roles, with opposite
consequences (self-review; no external reviewer to catch an over-claim):

- **(i) prefactor normalization.** A₁ is a constant term in `log Z` (the 2-loop of the
  `√(2πℏ/−V'')·exp(Σ Aₙℏⁿ)` prefactor). A constant in `log Z` shifts only the **k=0**
  coefficient of the log-expansion ⇒ leaves every `d_k` (k≥1) and hence every singularity
  estimator **exactly** unchanged. Under (i): A₁ *cannot* move the k=21 gap.
- **(ii) ladder coefficient.** The loop invariants `Aₙ` and the S-ladder `d_k` are related
  objects; if A₁ corresponds to a specific `d_k`, "feeding" it would **correct** that rung
  and could move the estimators — but the `A₁↔d_k` map must be derived first.

**Honest verdict (corrected from the first draft of this PR).** The earlier draft asserted
the strong "(i), scale-invariant ⇒ definitively no rescue" reading. That over-claimed: it
presumed role (i). The `A₁↔d_k` correspondence — is the state-integral 2-loop a *prefactor
normalization* (route-2's word) or a *ladder coefficient*? — **is the real open question**,
and it decides whether A₁ is even the right object to feed. If (i) holds (the literal
"normalization" reading), A₁ does not touch the k=21 singularity structure and the gate needs
more rungs; if (ii), the map must be derived. This probe does **not** decide (i)/(ii); it
names the decision as the next step and reports the k=21 baseline (gap 0.0194) unmodified.

## Net

- **Derived/confirmed:** the exact deformed shape `z*(q₀)` (gluing) — #3854's approximation
  caveat was real.
- **Scope-(a) results:** the `−u·log z` meridian coupling is refuted (the correct deformed
  potential is the named open piece); and the `A₁↔d_k` role (prefactor-normalization vs
  ladder-coefficient) is unresolved — the real open question gating whether A₁ can affect
  F1's k=21 gate at all (under the prefactor reading it touches only k=0 and cannot).
- **Unchanged:** #3854's complete-structure A₁ (1/3 + 0.27263763·i, three gates) stands.
  L2 = 2/7; no `c_k` wired; coordinated with #3805 (even-channel GGM).

## Compute

- Probe: [`computations/qbeta/qbeta_phib_2loop_deformed_gluing_and_f1_feed.py`](../../computations/qbeta/qbeta_phib_2loop_deformed_gluing_and_f1_feed.py) (exit 0)
- Witness: `computations/qbeta/qbeta-phib-2loop-deformed-gluing-f1-feed.witness.json`

## Cross-references

- The merged 2-loop b-dictionary: [`2026-07-17-phib-2loop-bdictionary.md`](2026-07-17-phib-2loop-bdictionary.md)
- Merged F1 acceleration (the k=21 gate): [`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md)
- Gluing solver: `computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py`
