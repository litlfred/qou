# W16 — open conjectures outside the mass chain: ranked queue (2026-11-20)

Workstream w16 (was proposed as "W8" in PR #8527 §W8/§D2; relabelled because the
beans dispatcher's own W8 is `qou-6qbv`). Branch `claude/w16-conjectures-2026-11-20`.

## Population, measured

Open beans (`todo`/`in-progress`/`draft`) reachable by `parent:` from the six
roots `b9cj`, `qou-r9ih`, `qou-frzo`, `qou-n4nr`, `qou-m6dn`, `qou-qs0e`, read
from the mounted `beans/defs/` (5795 files) on 2026-11-20:

- **362 unique open beans** (the "195" in #8527 counted direct children only).
- **34 at priority `high`**, 0 `critical`.
- **265 of the 362 cite an `#8xxx` PR** — 80 distinct PRs, mostly the
  "Round NN … Brick" batch lane (`feat/qou-*`, `feat/round*`). Those PRs are
  W4's triage scope. This queue does **not** re-do them; where a bean's next
  step is "decide that PR", it is marked `[batch PR]` and left to W4.
- Excluded, owned elsewhere: the dispatcher's W7–W14 trees (`qou-dxbw`,
  `qou-6qbv`, `qou-qhcr`, `qou-c8p8`, `qou-ncxf`, `qou-uhx0`, `qou-v6so`,
  `qou-d4kh`) — no bean in my scope descends from them (checked by ancestor walk).
- **Excluded as mass-chain (W1/W2):** the Δ_λ covariance-kernel cluster under
  `qou-m6dn` — `qou-v8t7`, `qou-ogrk`, `qou-4wl1`, `qou-jy04`, `qou-ik5e`,
  `qou-g0n2`, `qou-r91v`. Their subject is the sign of the Δ_λ kernel, which is
  the binding-magnitude front. Flagged to main rather than worked.

## Ranked queue (high-priority beans, in working order)

Ranked by "can an agent take an honest, sorry-free step now, without an owner
decision", not by importance.

| # | bean | claim | Lean today | smallest honest next step | sorry-free lemma in reach? |
|---|---|---|---|---|---|
| 1 | `qou-qexu` | q-explicit formula `QExplicitFormula` | finite-`List` carrier proved **uninhabitable** for every datum (`not_qExplicitFormula`, axioms clean) | the repair the file names: an ordered infinite-spectrum carrier, and what it forces | **DONE this PR** — `QExplicitFormulaSeq` (no instance) + `partialSpectral_unbounded`, `not_qExplicitFormulaSeq_of_bounded`, `not_qExplicitFormulaSeq_of_summable` |
| 2 | `qou-krvm` (iv), m004 | volume functional concave + invariant on the m004 angle polytope; regular point is its maximiser | (i)–(iii) proved (`M004AngleStructure.lean`); **single-tetrahedron Rivin concavity already proved** (`Knot/RivinConcavity.lean`, `strictConcaveOn_tetVolLine`) — the bean text saying (iv) is "untouched" is **stale** | assemble: V = Σ Λ over all six angles is permutation-invariant (so σ,τ-invariant trivially), strictly concave along feasible directions, critical at the regular point ⇒ regular point is the unique maximiser | yes, ~100–150 lines, all inputs exist |
| 3 | `qou-krvm` (iv), L6a4 | same for the proton anchor (24 vars) | (i)+(ii) proved, generated file | same assembly over 8 tetrahedra; generator `computations/probes/gen_l6a4_angle_structure_lean.py` | yes, mechanical once #2 lands |
| 4 | `hypr` | `conj:surreal-limit-transfer` | instance exists at ℝ* but rests on a **two-valued birthday** model (`flatBirthday`) — birthday axioms do not characterise Conway birthday | split `SurrealField` into birthday-free base + mixin (~38 modules), or strengthen the axioms | **owner decision** (refactor) — see D-W16-1 |
| 5 | `qou-qspc` | spectral coordinate map α_i = q^{ρ_i} has a carrier | none; `Ω_q` overloaded three ways (`qou-9iwt`) | disambiguate `Ω_q` per use; then a carrier for the integer-period reading only | partial; research |
| 6 | `qou-rstq` / `qou-trns` / `qou-b7cy` / `qou-m3ad` / `qou-m1nz` / `qou-gz37` | 5₂ sum rule (80-dps verified, unproved) | pieces in `FiveTwoCyclotomicBloch.lean`, `FiveTwoSaddleSumRule.lean` | Gap A (`qou-glbl`, IFT bookkeeping) then assembly `qou-asem` | Gap A plausibly; `[batch PR]` #8193/#8213/#8286/#8301 pending |
| 7 | `qou-mfdq` | pole-to-cusp bijection | named Lean proves no bijection; `.md` is a cardinality mismatch | `.md` correction = content change | needs owner OK (content), Lean side research |
| 8 | `qou-mtc9` | `confinement_categorical` §3b-cond restructure | self-assuming projection removed; carries `sorry` | needs Hochschild `HH^k(A)=0` (absent from Mathlib) | no — Mathlib wall |
| 9 | `qou-8mtd`, `rtep`, `bws0` | topological volume (Mostow); RT ribbon functor + Kirby; BW=Hecke | scaffolds | multi-month Mathlib topology / a physics identification | no — walls; leave as beans |
| 10 | `qou-c1ln`, `qou-wgnx`, `qou-odh5`, `qou-qbe9x`, `qou-ei4q`, `qou-rtec` | C1 connection / q-native alien calculus | rows 1–3 proved | `qou-c1ln` is **PAUSED by owner 2026-08-08** ("axis finished as far as anything needs it") | not started, by owner instruction |

Lower: `qou-6eik` (false "ℍ has no Riemannian metric" claim; `[batch PR]` #8231),
`qou-offl` (cone-manifold route, candidate only), `qou-vdvE` (Gukov–Murakami for
links; numerics), `qou-2q85` (depth-0→2 bridge), `qou-uir6` (`[batch PR]` #8353).

## Status of each worked item

- **#1 `qou-qexu`** — commit on this branch. `lean -DautoImplicit=false -s 65536`
  exit 0 on `q-geometric-langlands/explicit-formula.lean` (Mathlib-only cone);
  `#print axioms` on the three new theorems = `[propext, Classical.choice,
  Quot.sound]`. The new carrier is **not refuted** — the conjecture stays open;
  the bean stays open (§13a).
