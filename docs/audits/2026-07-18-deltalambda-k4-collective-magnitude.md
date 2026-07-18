# Δ_λ closure — attack Vector 1: the collective magnitude as a K₄ graph object

**Date:** 2026-07-18 · **Axis:** per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the many-body magnitude wall ·
**Tier:** structural forward-test (scope-(a) + scope-(b); no fit, no AME inversion,
nothing wired). Executes attack Vector 1 of
[`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md)
§4 row 1.

Probe: [`computations/deltalambda/deltalambda_k4_complete_graph_collective_magnitude_probe.py`](../../computations/deltalambda/deltalambda_k4_complete_graph_collective_magnitude_probe.py)
· witness `deltalambda-k4-complete-graph-collective-magnitude.witness.json` (exit 0,
6/6 assertions pass).

## 0. The question

#3943 ([`deltalambda_perpair_bond_magnitude_derive_probe.py`](../../computations/deltalambda/deltalambda_perpair_bond_magnitude_derive_probe.py))
proved that an **additive per-pair** magnitude cannot close the four light-isotope
deficits, and that the ³H/³He mirror split shows the residual is **collective /
non-additive**. Vector 1 asks the next question: is the missing collective term a
parameter-free **graph object on the complete coordination graph K₄** (6 edges) —
a Laplacian-spectrum / spanning-tree / graph-determinant invariant — rather than a
sum of independent pair terms?

The coordination graph is `K_A` on `A` vertices: **²H = K₂, ³H/³He = K₃, ⁴He = K₄**
(induced subgraph on the `A` nucleons of the doubly-magic ⁴He closure, per the #3924
`C(4,A)` locality).

## 1. Parameter-free invariants used (functions of A only)

| iso | A | edges C(A,2) | spanning trees A^{A−2} | Laplacian pseudo-det A^{A−1} | alg. connectivity λ₂=A |
|-----|---|--------------|------------------------|------------------------------|------------------------|
| ²H  | 2 | 1 | 1 | 2 | 2 |
| ³H  | 3 | 3 | 3 | 9 | 3 |
| ³He | 3 | 3 | 3 | 9 | 3 |
| ⁴He | 4 | 6 | 16 | 64 | 4 |

K₄ Laplacian spectrum = `{0, 4, 4, 4}` (eigenvalue 0 once, `A=4` with multiplicity
`A−1=3`); spanning-tree count `τ(K₄) = 4² = 16` (Cayley `A^{A−2}`); Laplacian
pseudo-determinant `∏ nonzero λ = A^{A−1} = 64`. The **complement** of `K_A` is the
empty graph (0 edges) — no non-trivial magnitude, not tabulated. A **hyperbolic
volume of a K₄-associated link** is a candidate of the same class but is a
topological invariant carrying no proton/neutron label, so it is covered by the
isospin-blindness argument in §3 (not computed separately).

## 2. Forward test — E₀·invariant vs deficit (no free prefactor)

Inputs consumed from #3943's committed witness (NOT recomputed, NOT refit):
deficit = `B_AME − B_dim` MeV = **{²H 1.844, ³H 6.573, ³He 5.373, ⁴He 25.257}**;
substrate unit `E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV`.

For each invariant `f`, `pred = E₀·f(A)` and the **required prefactor**
`= deficit/pred` (reported, never solved-for — solving it would be the forbidden
seventh fit). A genuine parameter-free match needs a **constant** prefactor.

| invariant | required-prefactor spread (max/min) | simultaneous match? |
|-----------|-------------------------------------|---------------------|
| edge count `C(A,2)` | **2.35×** | no |
| spanning trees `A^{A−2}` | **1.39×** | no |
| Laplacian pseudo-det `A^{A−1}` | **2.34×** | no |
| algebraic connectivity `A` | **6.85×** | no |

Key rows:

- **Additive edge count** matches ⁴He almost exactly (`pred/deficit = 0.99`,
  `E₀·6 = 25.12` vs `25.26`) but **overshoots ²H/³H/³He ~2×**. Edge count is the
  *additive* pair count, so this is the #3943 additive route re-seen: right at A=4,
  wrong for the lighter isotopes.
- The **super-additive collective** invariants — spanning trees (16) and Laplacian
  pseudo-det (64) — **overshoot ⁴He by 2.6× and 10.6×** respectively. The deficit's
  magnitude therefore does **not** grow like a super-additive graph object.

**Outcome (scope-(a)):** no single parameter-free graph invariant × E₀ reproduces
the four deficit magnitudes simultaneously. If anything, the data prefers *additive*
pair-count scaling at A=4 and resists any super-additive collective magnitude.

## 3. The ³H/³He mirror diagnostic (the crux)

³H (`pnn`) and ³He (`ppn`) are the **same graph K₃**. Therefore:

- **Every parameter-free UNSIGNED invariant** `f(A)` gives
  `deficit(³H)/deficit(³He) = 1.000`, while the data needs **1.223**. A pure graph
  invariant is **isospin-blind** and structurally cannot carry the p/n split.
- The **only** K_A graph object that distinguishes the pair is the **signed/colored**
  graph (pp=+1, nn=−1, pn=±1) — but that is exactly the #3924 b4 exchange
  determinant `−ln det(I + m·S)`, which needs the **gated** per-pair magnitude `m`
  (so it is not a parameter-free *collective* object) and at the corpus
  parameter-free `m = g_reeb` gives a **2.75×** split — wrong magnitude and
  direction vs data 1.223× (reproducing #3943's ~2.3–2.7× finding).

## 4. Verdict — double honest negative, well-scoped

**(b) Structural exclusion (cited invariant).** A parameter-free **unsigned** K_A
graph invariant cannot supply the p/n mirror split. *Invariant:* the coordination
graph `K_A` depends only on `A = Z + N` (isospin-blind) — the same invariant proved
for the antisymmetrizer trace / Reeb pn-magnitude det-conjugation
([`QOU/MassTheory/ReebPnMagnitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ReebPnMagnitude.lean);
attack-vector map §2.1). A K₄-associated hyperbolic volume inherits the same limit
(a link's volume carries no p/n label).

**(a) Scope-limited negative.** No single parameter-free graph invariant × E₀
reproduces the four-isotope deficit magnitudes (required prefactors span
~1.4–6.8×); super-additive collective invariants overshoot ⁴He 2.6–10.6×, only the
additive edge count matches ⁴He (0.99×) but overshoots the lighter isotopes ~2×.

**Refined reading (the value of this negative).** The "collective" character of the
#3943 residual is an **isospin (p/n) degree of freedom, not a super-additive graph
magnitude.** This distinguishes two hypotheses that #3943 left merged:

- *collective = super-additive graph magnitude* → **refuted here** (scope-(a): the
  data resists it; graph-collective invariants overshoot ⁴He).
- *collective = isospin-dependent split* → **the surviving reading**; a K₄ graph
  object cannot carry it (scope-(b): unsigned is isospin-blind; the signed graph
  needs the gated `m` and gives the wrong split).

Vector 1 therefore **sharpens** the search rather than closing it: the missing DOF is
the mirror split, which is not a K₄ graph-collective term. This is consistent with —
and does not exclude — a *signed/isospin-resolved* many-body object at the correct
magnitude (permanence principle: the proved locality/sign/ceiling of #3924 stand; a
correct closure re-weights the signed graph, it does not add an unsigned graph term).

**Nothing is wired.** Deficits were never inverted; no prefactor was solved from the
data (no seventh fit). Lean is 403-blocked in this sandbox — the isospin-blindness
invariant is cited from the already-merged `ReebPnMagnitude.lean` (det-conjugation)
and hand-audited here; no new machine Lean verification was run.

## Cross-references

- Additive negative + committed deficits: #3943
  [`deltalambda_perpair_bond_magnitude_derive_probe.py`](../../computations/deltalambda/deltalambda_perpair_bond_magnitude_derive_probe.py)
- K₄ exchange spectrum {±√5,±1}, signed-graph det, gated magnitude: #3924
  [`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)
- Coordination-graph tower framing:
  [`mnk_coordination_graph_selection.py`](../../computations/mnk_coordination_graph_selection.py)
- Attack-vector map (Vector 1 spec, §2.1 isospin prune):
  [`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md)
- Gate reversal (open for all): [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md)
- Isospin-blindness invariant: `QOU/MassTheory/ReebPnMagnitude.lean` (pn-sign det invariance)
