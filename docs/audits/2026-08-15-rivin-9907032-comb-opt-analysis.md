# Rivin, *Combinatorial optimization in geometry* (arXiv:math/9907032) — corpus utilization + Lean-formalization analysis

**Date:** 2026-08-15 · **Scope:** analysis-only, scope-(a), no fit, nothing wired.
**Source:** `library/arxiv-math-9907032v1/9907032v1.pdf` (owner upload, commit `73784ff`).
Igor Rivin, "Combinatorial optimization in geometry", arXiv:math/9907032v1 [math.GT]
6 Jul 1999; published *Advances in Applied Mathematics* **31** (2003) 242–271.

## 0. Why this paper matters to QOU

The QOU framework runs on an **LP/SDP primal–dual spine** (AGENTS.md §"LP / SDP
duals — first-class infra": `prop:operator-selection-lp`, `lp_dual_solver.py`,
the `y0_star`/`y_star`/`active_set`/`duality_gap` witness fields, the confinement
SDP, the `climax-volume-mass/` shadow-price cluster) and on the **Casson–Rivin
angle-structure polytope** (`RivinConcavity.lean`, `SymmetricOptimum.lean`,
`M004AngleStructure.lean`, `L6a4AngleStructure.lean`, `IdealTetrahedronConcavity.lean`,
`qou-krvm`, `qou-idvt`). This paper is the **foundational Rivin source** for both:
it recasts the existence/uniqueness of (singular Euclidean / ideal-polyhedral)
structures with prescribed dihedral angles as **linear programming + network-flow
duality**. The existing `angle-structure-lp-sdp-dictionary.md` audit is built on
Garoufalidis [1208.1663] — a *descendant* of this paper — and **uses** LP duality
without ever formalizing it.

**Registration gap:** math/9907032 is **not in `content/schema/references.ts`**
(grep-confirmed). It should be registered (`rivin2003` / `rivin-comb-opt`,
DOI 10.1016/S0196-8858(03)00093-9 — verify).

## 1. The load-bearing results (extracted from the PDF)

| # | Result | Statement (paraphrase) |
|---|--------|------------------------|
| **Thm 3.2** | **LP Duality Theorem** | `P: min cᵀx s.t. Ax=a, x≥0`; dual `P*: max aᵀλ s.t. λᵀA ≤ c`. `P` feasible ⇔ `P*` bounded; and (strong duality) equal optimal values when both feasible. |
| **Program L** | angle **feasibility LP** | A singular-Euclidean structure with prescribed dihedral angles exists ⇔ a linear program `L` (angles as strictly-positive primal variables) is feasible. |
| **Cutset conditions** | **network-flow feasibility** | Necessary+sufficient: vertex cone-angle sums `= 2π`; and over every **nontrivial cutset** of edges the angle sum is **`> 2π`** (a Hall / max-flow–min-cut-type criterion). |
| **Lemma 1.2** | cone-angle identity | cone angle at an interior vertex `v` = Σ of exterior dihedral angles at edges incident to `v` (boundary variant analogous). |
| **Thm 1.4** | **uniqueness** | At most one singular similarity structure with prescribed dihedral angles + holonomy (Euclidean structure unique up to scaling). |
| **Thm 4.8** | **finiteness reduction** | The infinitely-many subcomplex conditions reduce to checking only **simple** subcomplexes — makes feasibility *effective + efficient*. |
| **Thm 3.1 / 4.11** | existence + moduli | existence of the structure; the cells `M_T` carry a convex-**polytope** structure (moduli decomposition = polyhedral complex). |

## 2. Corpus mapping — what this paper supplies that QOU currently only asserts

- **The LP dual variables ARE the geometry.** The QOU witnesses emit `y_star`
  (shadow prices) / `active_set` and assert `duality_gap ≈ 0` **numerically**.
  Thm 3.2 is the theorem those numeric assertions are shadows of; the dual
  variables `λ` are the cutset/vertex Lagrange multipliers — the "most receptive
  sub-braids" reading in the AGENTS.md LP-dual section is *Rivin's* geometric
  duality, not a QOU coinage.
- **qou-krvm (ii) — uniqueness of the symmetric point** is **Thm 1.4** (+ the
  strictly-convex-objective-on-symmetric-convex-set argument already proved in
  `SymmetricOptimum.lean`, PR #4513). The two are the same fact from two sides.
- **qou-krvm (i) — the m004/L6a4 polytopes are angle-structure polytopes** is the
  **Program L / cutset** feasibility region (Thm 3.1 + cutset conditions).
- **qou-idvt (iv) — concavity** is the *other* Rivin paper ([rivin1994], the 1994
  Annals "Euclidean structures…"); 9907032 supplies the **polytope + uniqueness +
  LP feasibility** around it, not the volume-concavity itself.

## 3. Prioritized Lean-formalization targets (what is genuinely formalizable now)

Ranked by (value × feasibility). All algebraic/ordered-field → generic where
possible, `ℝ` only where an ordering/analysis is genuinely needed (§7c).

1. **LP weak duality + `duality_gap ≥ 0`** (HIGH value, HIGH feasibility).
   `cᵀx ≥ aᵀλ` for any primal-feasible `x`, dual-feasible `λ`; hence
   `primal_obj ≥ dual_obj` and `duality_gap = primal_obj − dual_obj ≥ 0`. A short
   Lean proof over a `LinearOrderedField`. **This gives the ubiquitous QOU LP-dual
   witness assertion a *proved* backing** instead of a numeric check — directly
   serves the AGENTS.md LP-dual STRICT rule. Mathlib has the linear-algebra
   primitives; no geometry needed.
2. **Strong duality / Farkas** (HIGH value, MEDIUM feasibility). Full Thm 3.2 needs
   a Farkas-lemma / separating-hyperplane input. Check Mathlib
   (`Mathlib.Analysis.Convex`, `Mathlib.LinearAlgebra` Farkas fillers); state the
   strong-duality equality conditionally on Farkas if not yet in Mathlib (honest
   §3b/`sorry` + `-- Ref:`), so the `dual_obj = primal_obj` equality is at least
   *stated* as the real proposition.
3. **Lemma 1.2 — cone-angle = Σ exterior dihedral angles** (MEDIUM value, HIGH
   feasibility). A finite `Finset.sum` identity over the incident edges; clean,
   generic, sorry-free-able. Anchors the angle-structure vertex constraints.
4. **Cutset feasibility criterion** (MEDIUM value, MEDIUM feasibility). State the
   vertex-sum `= 2π` + cutset-sum `> 2π` conditions as the defining
   (in)equalities of the angle-structure polytope; connect to
   `M004AngleStructure.lean` / `L6a4AngleStructure.lean`. The Hall/max-flow
   *equivalence* (necessary **and** sufficient) is the hard analytic core — state
   it, prove necessity (easy), leave sufficiency as honest `sorry` + `-- Ref:`.
5. **Uniqueness (Thm 1.4) ↔ `SymmetricOptimum`** (MEDIUM value, HIGH feasibility).
   Likely a short *reuse*: show the qou-krvm (ii) uniqueness hypothesis is exactly
   `SymmetricOptimum.optima_coincide`'s unique-maximiser premise instantiated at
   the angle-structure polytope + convex objective. Mostly wiring, not new proof.

**Not formalizable now** (honest): the existence theorems (Thm 3.1/4.11), the
moduli-polytope structure, and the Casson-theorem application need
hyperbolic/PL-geometry infrastructure Mathlib lacks — cite, don't fake.

## 4. Recommended next actions

- Register `rivin2003` in `references.ts` (DOI verify) — used by the targets above
  and by the existing angle-structure dictionary retroactively.
- File beans for targets **1** (LP weak duality — the highest-leverage, cross-cutting
  win) and **3/5** (Lemma 1.2 + uniqueness wiring). Target **1** is the one that
  pays off "across the paper": every LP/SDP-dual witness in the corpus inherits a
  proved gap-nonnegativity.
- Coordinate with `qou-krvm` / `qou-idvt` (live) — targets 4/5 touch the same
  angle-structure files.

**Discipline:** analysis-only; no fit; nothing wired. Formalization targets to be
executed under formalize-first + §1 (every `sorry` cited) + §7c.
