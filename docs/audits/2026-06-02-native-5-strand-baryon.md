# Native-5-strand baryon (Escape 2): does h⁴ = −3/4 live at n = 5?

**Date:** 2026-06-02
**Branch:** `claude/native-5-strand-baryon-2026-06-02` (PR #1694)
**Trigger:** Author directive *"take a run at one of the two escapes"*
(2026-06-02) following the Young's-lattice synthesis, which named two
non-fit routes past the keystone vertical obstruction; this audit tests
Escape 2 (native-5-strand baryon).
**Scope:** Test **Escape 2** of the Young's-lattice synthesis
([`2026-06-02-young-lattice-gauge-synthesis.md`](2026-06-02-young-lattice-gauge-synthesis.md),
reframe #2 of [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md),
PRs #1684/#1691): the hypothesis that the 3-strand Borromean baryon
`B₃ = (σ₁⁻¹σ₂)³` is a **Markov-destabilized shadow** of a canonical
**native-5-strand** object, so the keystone `h⁴ = −3/4` coefficient lives
natively at `n = 5` and there is **no vertical map** to construct — the
keystone dissolves.
**Compute:**
[`native_5_strand_baryon.py`](../../computations/native_5_strand_baryon.py),
witness
[`native-5-strand-baryon.witness.json`](../../computations/native-5-strand-baryon.witness.json)
(audit-only, 7 assertions pass; RAW Markov traces; `h⁴ = −3/4` is a
**FALSIFICATION reference**, never a target).

---

## VERDICT (one line)

**ESCAPE 2 FAILS (verdict iii).** No **canonical** native-5-strand carrier has
`B₃` as its Markov-destabilized shadow. Every forced candidate either
**forbids** `B₃` as a shadow by definition (Brunnian-5), is **not a braid
index** at all (icosahedral A₅), or fails the Markov disjointness axiom so its
RAW trace bears no relation to `B₃` (the S₅-pattern 5-braid: `tr_M(w₅) = 0.0088`
vs `z²·tr_M(B₃) = 0.249`, a **96.5 % mismatch**). The keystone obstruction does
**not** dissolve. `h⁴ = −3/4` is recovered **only** at the 3-strand `B₃`;
choosing any 5-strand carrier to reproduce it is exactly the fit the discipline
forbids. **Escape 1** (geometric / icosahedral-holonomy / cusp cross-ratio
section) is the remaining non-fit route.

---

## 1. The 3-strand baryon datum (where `h⁴ = −3/4` comes from)

Established, RAW-verified. The baryon is the Borromean rings `B₃` (3-component
link, closure of the 3-braid `(σ₁⁻¹σ₂)³`). Its Markov trace is the
Jones-polynomial normalization

$$
  \mathrm{tr}_M(B_3) \;=\; \frac{V(B_3,\,q^2)}{[2]_q^{2}}
  \;=\; \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4},
  \qquad h = q - q^{-1},
$$

whose `h`-expansion is purely even with **`h² = 0`** and first nontrivial
coefficient **`h⁴ = −3/4`** — the first topological invariant distinguishing
`B₃` from the unlink, carried entirely by the `(2,1)` std block
([`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md)).
The probe re-derives this exactly (`baryon_h4_eq_minus_3_4` and
`baryon_h2_eq_0` assertions pass). This `−3/4` is the falsification reference
for everything below.

## 2. The three forced 5-strand candidates

The discipline requires the 5-strand carrier be **forced** by symmetry already
in the corpus, never chosen to make `h⁴` appear. Three forced candidates exist:

### C-A — the canonical Brunnian-5 link (Borromean generalization)

**Forced** (the Brunnian property + minimal crossing determine the object).
**Decisively falsified by the definition of Brunnian.** A 5-component Brunnian
link has the defining property that **every proper sublink is trivial**: deleting
any one component yields the 4-component **unlink**, not `B₃`. So `B₃` — a
*nontrivial* 3-component link — is **not a sublink/shadow of any Brunnian-5
link** at all. Markov destabilization (removing a strand disjoint from the
closure) also fails axiom-3 disjointness, exactly as it does for `B₃` itself
(census PR #1677). **The "`B₃` = shadow of Brunnian-5" picture contradicts the
definition of Brunnian.** `destabilizes_to_B3 = False`.

### C-B — the icosahedral A₅ / dim-5 ℓ=2 carrier

**Forced** (s5-so3 audit: `A₅ ≅ I`, the ℓ=2 fiber is the dim-5 irrep `H`).
**Not a 5-STRAND carrier.** `A₅` is the SO(3) finite **rotation** subgroup
acting on the 3 color sheets — a *fiber group*, not a braid index. There is no
braid/Markov destabilization between an `A₅` irrep and a braid closure (different
category). Read as "natively the `A₅` carrier", the `(2,1)` `h⁴` channel appears
with **multiplicity 2** (`Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)`, recomputed RAW via
exact characters, dim-check passes) — the **same multiplicity-2 obstruction** the
keystone caught. Choosing a line in the 2-dim Hom-space is a fit. No dissolution.

### C-C — the S₅-symmetric 5-braid `w₅ = (σ₁⁻¹σ₂σ₃⁻¹σ₄)³`

The **word** is forced by S₅-symmetry (it is the unique S₅-equivariant lift of
`B₃`'s `(σ₁⁻¹σ₂)³` pattern). But the **destabilization to `B₃` is not canonical.**

This is the candidate where a genuine RAW Markov-trace computation is decisive.
Computing `tr_M(w₅)` at H₅ via the canonical Wedderburn sum (Hoefsmit seminormal
characters × Wenzl `y_λ`, the production tr_M route) at the proton-pinned `q₀`:

| quantity | RAW value @ q₀ |
|---|---|
| `tr_M(w₅)` | **0.008799** |
| `z²·tr_M(B₃)` (clean double destabilization H₅→H₃) | 0.248962 |
| relative mismatch | **0.9647 (96.5 %)** |

A genuine native-5 carrier with `B₃` as its Markov shadow would satisfy
`tr_M(w₅) = z²·tr_M(B₃)`. It misses by 96.5 %. **`w₅` does not destabilize to
`B₃`** — consistent with the axiom-3 disjointness failure (the word uses
`σ₃,σ₄` non-trivially, so strands 4,5 are not disjoint from the closure). One
*can* collapse `w₅ → B₃` by **hand-deleting** `σ₃,σ₄` from the word — but that is
a chosen projection, not Markov destabilization, i.e. the fit the discipline
forbids. The Brunnian non-disjointness obstruction is **inherited at n = 5**.

**Per-block breakdown of `tr_M(w₅)` (RAW):** no `λ ⊢ 5` block carries a
coefficient resembling `−3/4`. The `(2,1)`-restricting blocks have characters
`χ_q(w₅)` = `(4,1): −1.137`, `(3,2): −0.136`, `(3,1,1): +1.392`,
`(2,2,1): −0.136` — none distinguished, none `−3/4`. The contributions are
`0.118, −0.124, −0.008, +0.023, −0.001, +0.001, +0.0001`, summing to `0.0088`.

## 3. Does `h⁴ = −3/4` appear canonically at `n = 5`?

**No.** RAW, with the fit-flag honored:

- The exact `h⁴ = −3/4` is reproduced **only** at the 3-strand `B₃` (verified).
- At `n = 5`, `tr_M(w₅)`'s value (0.0088) and its per-block decomposition show
  no canonical `−3/4` coefficient; no distinguished `λ ⊢ 5` block carries it.
- Making `−3/4` appear at `n = 5` requires either (i) choosing a line in the
  multiplicity-2 `A₅`/`(2,1)` Hom-space (C-B), or (ii) hand-deleting strands to
  collapse `w₅ → B₃` (C-C), or (iii) appealing to a Brunnian-5 object that by
  definition has no `B₃` shadow (C-A). All three are fits or contradictions.

## 4. The dissolution check

Escape 2's promise was: *if* the baryon is natively 5-strand with `B₃` its
Markov shadow, then the multivalued `Res^{H₅}_{H₃}` is irrelevant — the baryon
never needed to map down. **This does not happen.** There is no forced 5-strand
object whose Markov destabilization is `B₃`. The obstruction is therefore **not
dissolved**: it is exactly relocated to "there is no canonical 5-strand
pre-image of `B₃`," which is the same multivalued/multiplicity-2 phenomenon the
keystone identified, now seen from the 5-strand side. The keystone stands.

## 5. Where this leaves the keystone

Escape 2 is **closed**. The remaining non-fit route is **Escape 1**
(non-functorial / geometric section): the canonical nominator of the `(2,1)`
copy comes from *extra* structure beyond Hecke rep theory — the icosahedral
holonomy / color-tube cross-ratio on Bring's quintic
([`flavor-dependent-cusp-shape`](2026-06-01-flavor-dependent-cusp-shape.md),
[`complex-fibre-cross-ratio`](2026-06-01-complex-fibre-cross-ratio.md),
[`reeb-bring-geometric-escape`](2026-06-01-reeb-bring-geometric-escape.md)),
which can pick a distinguished vector that branching alone cannot.

## What this audit does and does not claim

- **Does** reproduce, RAW and exactly, the 3-strand baryon datum
  `h⁴ = −3/4` and `h² = 0` from `tr_M(B₃) = V(B₃,q²)/[2]_q²`.
- **Does** compute a genuine RAW Markov trace `tr_M(w₅) = 0.0088` at H₅ via the
  canonical Hoefsmit-seminormal × Wenzl-`y_λ` route, and show the
  destabilization relation `tr_M(w₅) = z²·tr_M(B₃)` fails by 96.5 %.
- **Does** recompute the icosahedral `Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)` (RAW,
  dim-checked) and the Brunnian-property obstruction.
- **Does** report forced-vs-chosen status per candidate honestly, and conclude
  Escape 2 fails (iii) with no fit and no fabrication.
- **Does NOT** propose, fit, or tune any 5-strand carrier, braid word,
  multiplicity, or normalization to reproduce `−3/4`. The h⁴ value is a
  falsification reference only.
- **Does NOT** wire to production; does NOT advance L1/L2 numerically; does NOT
  discharge any Lean `sorry`; no LP/SDP solve (no dual emission required).

## Cross-references

- The keystone + the two escapes:
  [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md) (#1684),
  [`2026-06-02-young-lattice-gauge-synthesis.md`](2026-06-02-young-lattice-gauge-synthesis.md) (#1691).
- The 3-strand baryon datum (h⁴ = −3/4):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md).
- Brunnian property (proper sublinks trivial):
  [`brunnian-property-of-borromean.md`](../../content/quantum-observable-universe/particle-interactions/brunnian-property-of-borromean.md).
- Markov (de)stabilization = vertical α_V (z-factors, disjointness axiom):
  [`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md),
  census [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md) (#1677).
- The remaining Escape 1 (geometric section):
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md),
  [`2026-06-01-reeb-bring-geometric-escape.md`](2026-06-01-reeb-bring-geometric-escape.md).
