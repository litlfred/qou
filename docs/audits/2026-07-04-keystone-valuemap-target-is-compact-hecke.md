# Keystone value map (s013): the target is COMPACT Hecke quantum-dimension data — why every geometric route failed, and where the honest resolution sits

**Date:** 2026-07-04
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Follows:** [`2026-07-04-keystone-sigma345-largerD-seifert-refuted.md`](2026-07-04-keystone-sigma345-largerD-seifert-refuted.md) (redirect (i) closed) and [`2026-07-02-keystone-valuemap-qbessel-gate.md`](2026-07-02-keystone-valuemap-qbessel-gate.md) (single-arg q-Bessel refuted).
**Script:** [`computations/probes/keystone_valuemap_target_is_compact_hecke.py`](../../computations/probes/keystone_valuemap_target_is_compact_hecke.py)
**Witness:** [`computations/probes/keystone-valuemap-target-is-compact-hecke.witness.json`](../../computations/probes/keystone-valuemap-target-is-compact-hecke.witness.json)
**Status:** consolidating grounding. Two machine-verified facts + a made-precise type argument that explain the whole refutation series. Scope (a) on the tested q-Bessel forms; no structural exclusion of a Plancherel-fixed row asserted. No fit; nothing wired.

## The two facts

**FACT 1 (machine-verified) — the target is compact SU_q(2)/Hecke quantum
dimension.** bwS0(λ) = d_q(λ)/D at n=5 is exactly

| class | d_q | Hecke label | value at q₀ |
|---|---|---|---|
| (5) | [1]_q | 1 | 1 |
| (4,1) | [4]_q | 4 | 4.10968 |
| (3,2) | [5]_q | 5 | 5.22044 |
| (3,1,1) | [4]_q[3]_q/[2]_q | product | 6.22044 |

Three are **single balanced q-integers** [m]_q = q^{m−1}+…+q^{−(m−1)} — finite
**Laurent polynomials** in q₀ (verified: [m]_q equals its balanced expansion to
10⁻⁴⁵) — and the self-conjugate block is the sole product. This vector is the
**Verlinde ratio S₀λ/S₀₀** of the Hecke modular category: the compact quantum
dimension.

**FACT 2 (source scan) — the uploaded Murakami paper has no colored block.**
`library/arxiv-2205.01282v2/2205.01282v2.pdf` (Murakami, GPPV proof that WRT = radial limit of the
homological block Ẑ) over 18 pages has **0** occurrences of
color/colour/decorat/wilson/refined/equivariant (32 "homological block", 9
"false theta", 4 "knot" — all bibliographic). Its homological block is the
**undecorated** false theta; for Σ(2,3,5) that is the Lawrence–Zagier **D=2**
golden object already refuted. The paper contributes no colored/decorated block
that could carry a 4-class family.

## Why every geometric route failed — the type argument, made precise

The target values (Fact 1) are **Laurent polynomials in q₀** — compact, finite,
algebraic characters of finite-dimensional SU_q(2)/Hecke modules. Every
geometric candidate tried was the wrong *type* for this target:

- **Compact modular S-matrices** (Σ(2,3,5) D=2, Σ(3,4,5) D=6) are built from
  **rational-angle sines** independent of q₀ — they cannot even *depend* on the
  substrate (redirect (i) refutation, 2026-07-04).
- **The non-compact q-Bessel / E_q(2) row** is built from the Hahn–Exton
  J_ν(x;q), a **non-terminating ₁φ₁ q-series** — a transcendental function of the
  radial argument x, whose value at a generic x is not a q-integer. To hit the
  compact-algebraic target it must **tune x** to land a transcendental on
  algebraic q-integer values:
  - the disciplined **single-argument** (1-dof, overdetermined) form is
    **refuted** (2026-07-02 qbessel-gate §4, best 13% off);
  - a **multi-argument** form gives each of the 4 channels its own radial
    argument ⇒ **≥4 free reals for 4 targets ⇒ an unfalsifiable fit** (dof ≥
    constraints) — unless the arguments are **fixed by the E_q(2) Plancherel
    measure**, which needs the **Koelink–Swarttouw q-Hankel kernel**, a source
    **not in `library/`**.

So redirect (ii) is **not disciplined-actionable in-repo**: the uploaded
Murakami paper supplies no colored block, the only falsifiable q-Bessel form is
refuted, and the falsifiable multi-argument form needs an un-uploaded Plancherel
kernel (and even then chases a transcendental class for a compact target).

## The honest resolution — and what it does and does not buy

Fact 1 says the value map **is** the compact Verlinde/Hecke datum
S₀λ/S₀₀ = d_q — which is exactly redirect (iii), `BWVacuumRowIsHecke`. This is
**near-definitional**: within the Hecke modular category the vacuum row of the
Verlinde S-matrix *is* the normalized quantum dimension, by construction.

**What this buys:** it closes the value-map *question* — "what object realizes
bwS0?" — cleanly and honestly: the compact Hecke quantum dimension, no geometry
required.

**What it does NOT buy (said plainly, per the critical-distance license):** it is
**not** the geometric derivation the s5-so3 keystone was reversal-gated to
pursue. The original hope was that the *manifold-side* WRT(S³/2I) data would
independently realize the Hecke quantum dimensions and thereby help fix q₀ /
the normalization D (Subgoal-2). But the manifold's WRT category is D=2 (golden),
a **different** modular category from the n=5 Hecke category (4-class); the
Verlinde identity holds **within the Hecke side tautologically** and supplies no
independent constraint on q₀ or D. The compact-vs-geometric **type mismatch** is
the reason the geometric program stalled: bwS0 is compact representation-theoretic
data, and there is no q₀-dependent *geometric* object of the right type among the
routes tried.

## Consequence for the keystone program

- Redirects (i) [larger-D Seifert] and (ii)-via-Murakami [uploaded GPPV paper]
  are closed. Redirect (ii) survives **only** as the Koelink–Swarttouw
  Plancherel-fixed q-Bessel row, which requires the un-uploaded primary source
  and even then targets a transcendental class for a compact target.
- Redirect (iii) resolves the value-map *question* definitionally but does not
  advance the Subgoal-2 geometric-derivation goal.
- **Owner decision surfaced:** either (a) drop Koelink–Swarttouw (q-Hankel /
  E_q(2) Plancherel) into `library/` to test the one remaining disciplined
  q-Bessel form, or (b) accept redirect (iii) as the honest resolution of the
  value map and record the geometric Subgoal-2 route as stalled at the
  compact/geometric type mismatch, or (c) pivot the keystone effort elsewhere.

No fit; no q-Bessel formula is written in the probe (fabrication-avoidance); the
only computed quantities are the exact compact quantum dimensions and a text
scan. Three-calibration discipline untouched; nothing wired.

# Ref: [murakami2022wrt] arXiv:2205.01282 (library/arxiv-2205.01282v2/2205.01282v2.pdf)
# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694
