# MED wall-side drain — second half (bean `qou-med65`)

Scope: the second half of the MED `wall-side-correct` failures, derived fresh
from a clean tree. The first half is owned by a sibling agent; nothing outside
the list below is touched here.

## How the list was derived

```bash
bash scripts/setup-folio-assistant.sh
bun run scripts/check-wall-side.ts --sweep content/quantum-observable-universe
```

Baseline on this branch point (`3f1a4e3f23`): **1114/1190 pass**, 76 FAIL.
After this branch: **1146/1190 pass**, 44 FAIL — **+32**, which is exactly the
16 ports plus the 16 acknowledgements and no accidental collateral.

Each failing block's `lean.ref` was resolved the way the checker resolves it
(sibling `<root>.lean` first, then `<lakeRoot>/<Decl/Path>.lean`), the Lean
source was **comment-stripped**, its `import` lines dropped, and the Lean
punctuation tokens that merely *contain* an angle bracket (`=>`, `<;>`, `<|>`,
`|>`, `->`, `<-`) removed, before any regex ran. Then:

- **HEAVY** — `Real.<fn>`, `Complex`, integral/measure tokens → not MED
- **MED** — ordering only: `0 <`, `≤`/`≥`, `abs`/`|…|`, `linarith`, `positivity`,
  and **bare `>` / `<`** (the token class #4709's regex omitted)
- **OTHER** — no ordering token at all → the WEAK queue, not this one

The arrow-token step is not cosmetic. Without it `=>` alone makes essentially
every Lean file "MED": the first pass returned 69 MED / 6 OTHER, and
`habiro-ring` — which has no ordering anywhere — was called MED purely on the
`=>` inside `⟨fun _ => 0, by ring⟩`.

Result with the step: **65 MED**, 1 HEAVY (`quantum-dilog-convergence`),
10 OTHER. Two independent agreement checks:

- 65 is exactly the bean's own MED count;
- the OTHER set contains precisely the six blocks the WEAK-33 hand triage
  already named (`qmn-recursive-memoized`, `cpt-d6-d7-d8-closure`,
  `nucleon-ordering-factorization`, `q-gl-classical-limit`,
  `q-beta-radius-of-convergence-gate`, `qou-infra-discharges-goncharov-zeta5`).

Sorted alphabetically by `.ts` path, this branch takes **items 33–65** (33
blocks). Item 33 is the midpoint and is claimed here deliberately: a duplicated
block costs a merge conflict, a skipped block is silent.

`appendix-surreals/collatz-contact-boundary` is item 3 — first half, and in any
case owned by sibling PR #4722. Not touched.

## Verdicts

Standing rule from
[`…weak-triage.md` §8](2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md):
**a GENUINE verdict is a compile result, never a read.** Every GENUINE row below
was compiled with `lean -DautoImplicit=false` (exit 0) and re-checked with
`check-wall-side --block`.

### GENUINE — ported (16)

The typeclass is the weakest that admits the file's own content (§7c), not a
uniform `LinearOrderedField` stamp. Seven different targets appear:

| block | target | what decided it |
|---|---|---|
| `jet-filtered-knot-factor` | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` | its import: `QOU.MathlibExt.QPlancherel` is *already* generic over exactly this and was being pinned to `ℝ` |
| `symbolic-character-table` | `[Field R] [CharZero R]` | `sigmaOneCharacter` is already `[Field R]`; `sigmaOneCharacter_eq_card_mul` takes an explicit `(2 : R) ≠ 0` |
| `q-pochhammer-partial-product` | `[Field R]` | its own docstring: "the purely algebraic shadow", deferring the Faddeev asymptotics to a sibling file |
| `t-beta-markov-frobenius-collapse-general` | `[CommRing R] [PartialOrder R] [IsOrderedRing R]` | its own docstring said "general unital R-algebra" while the code said `ℝ`; the same bound is already proved generically in a sibling |
| `operator-selection-lp` | `[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]` | an LP is `Finset.sum`, `*` and `≤` |
| `sdp-regime-switch` | `[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]` | Sylvester's `d·Q = (d·x₀ + c·x₁)² + (dd' − c²)x₁²`; no division |
| `centered-hecke-variance-positive` | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` | an inverse, a square, `linarith`; `z` enters as a field, no radical is taken |
| `atomic-nf-witness` | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` | `F_Pauli = \|tr_alt / net\|` — division and an absolute value |
| `benzene-threading-emergence` | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` | `positivity` on `[3]_{q²} = q² + 1 + q⁻²`, `linarith` on the shadow price |
| `demand-stability` | `[CommRing R] [PartialOrder R]` | `dem_mag` / `tr_M` only compared, or tested `= 0` |
| `frobenius-positivity-filter` | `[CommRing R] [PartialOrder R]` | the proved core lives in `ZMod 2` + `Finset`; the `G`-products are only asked `0 ≤ ·` |
| `branching-qvalue-factorization` | `[CommRing R]` | `Finset.prod_univ_sum` + `pow_succ` + `ring`; the only order hypothesis is `0 < N` in `ℕ` |
| `q-gl-obstruction-calc` | `[CommRing R]` | the core is in `ℤ`; both curvature values are only tested against zero |
| `shell-filling-rule` | `[Semiring R]` | occupancies/capacities are `ℕ`; the only scalars satisfy `primal_obj = Z * y_0` |
| `co-lp-dual-binding` | `[Preorder R]` | `Φ₁` values are only ever compared |
| `co2-lp-dual-binding` | `[Preorder R]` | same |

The molecular LP family is where the same chapter splits both ways.
`ch4-lp-dual-binding` was correctly called LEGIT by #4745 — its `ℝ` are
`E_bind_CH` / `E_bind_per_bond`, **measured bond energies**. `co`, `co2` and
`benzene` carry an **abstract `Φ₁` shadow-price functional**, which is not a
measured quantity. Neither verdict is boilerplate.

### LEGIT — §7c note on the referring block (13)

Grouped by what makes `ℝ` load-bearing; each note cites its own file's construct.

- **Measured / substrate literals** — `hook-weight-derivation`
  (`|w_22 − 0.166| < 0.01`), `mass-side-kernel-formalize-first-gates`
  (`q_substrate := 1.10997858275138`, `directionTarget := 2.46`),
  `q-beta-bar-even-kernel-typeclass` (`uSubstrate := 0.008517234550156142`),
  `atomic-lp-stability` (`0.537` vs `1.109978595554181^(−10)`),
  `ilp-covalent-bond` (H₂ binding energy, `E < 5.0` for the 4.48 eV
  prediction), `parity-regime-selection` (`m_e`, `Q_value` in MeV),
  `substrate-consistency-window` (per-measurement-class half-widths `ε`).
- **Archimedean by meaning** — `lp-dual-stability` (`t_norm` is the Euclidean
  `‖t‖`, `κ_G` a condition number), `h2o-bond-angle-shift` (a bond angle,
  109.5° → 104.5°), `gs-spectral-decomposition-existence` (residues at roots of
  unity; `RootOfUnity.value` is documented as *"real part; full Mathlib version
  uses `Complex`"*).
- **Analysis in the consumed definition or the proof** —
  `jonquiere-cyclotomic-tate-rationality` (`jonquiereWrongParity` carries
  `Real.pi`), `brane-tower-q-laplacian-decay` (derives its closed form by
  *summing* a `tsum` via `tsum_geometric_of_lt_one`; `rho_L2` is an L² norm).
- **The file already implements the §7c split** — `mass-endomorphism-tower`,
  whose `Pre` tier is generic `{R} [Field R]` and whose `Arch` tier is `ℝ` with
  `1 < q` on purpose.

### BLOCKED by an `extends` edge (3)

Recorded, not silently skipped, so the next agent does not re-derive the
diagnosis. This is the `qmn_recursive_memoized` failure mode: **a file count
does not measure blast radius when the dependency runs through class
inheritance.**

| block | edge |
|---|---|
| `strangelet-crossing-energy` | context `extends QOU.Shared.MarkovTraceContext` — 16 extenders; tracked as bean `qou-mtcx` |
| `quantum-planck-constant` | its ordering hypotheses live on `QOU.SubstrateParameter`, mentioned by 42 library files |
| `qou-obstruction-reduction` | `QouObstructionReductionContext` is extended by `CollatzContactBoundaryContext` and consumed by four further files. On its own content it *is* portable — `phi_1_image` is only ever equated to an integer cast — but one affected file is owned by sibling PR #4722 |

### Attempted and reverted (1)

`gram-matrix-h3-symbolic` — see §"The one that did not pay" below.

## The one that did not pay: `gram-matrix-h3-symbolic`

The file is rational-function algebra in `u` (with `q = u²`) plus six
positivity lemmas: on a reading it is a textbook regenericisation candidate, and
the port itself is mechanical. The compiler said otherwise about the *cost*.

Baseline `lean`-direct on the `ℝ` version: **3 min 5 s**. The `[Field R]
[LinearOrder R] [IsStrictOrderedRing R]` version did not finish inside a **10×**
window. The reason is visible in the file: `gramScaled_det` expands a 6×6
determinant with `Matrix.det_fin_six` and closes it with `ring` under
`set_option maxHeartbeats 40000000`, and `gram_scale_rel` runs `field_simp <;>
ring` on 36 rational-function cells. Over a concrete `ℝ` those elaborate against
compiled instances; over a generic ordered field every arithmetic step carries
its typeclass argument.

So the honest verdict is **not** "LEGIT" and **not** "GENUINE": it is *portable
in principle, but the port costs more than the finding is worth at present*, and
a change nobody can afford to re-verify is worse than the `ℝ` it replaces. That
is the same lesson as #4745's `meson-em-sinh` first attempt, in a different
coordinate: a regenericisation that leaves a proof unverifiable is not an
improvement. Left on `ℝ`; the block keeps its existing status and is the one
row of this half neither ported nor acknowledged.

Independently worth knowing: §7c's own table lists "square root / radical → `ℝ`"
with a **Hoefsmit** example, and this file *is* the Hoefsmit seminormal Gram in
`u = √q`. A reader who stopped at that row would have called it LEGIT without
measuring anything. The measurement is the better record.

## Environment note (Lean, for the next agent)

Two things cost time here and are not written down anywhere else:

1. The shared QOU olean set is **missing**
   `QOU/BraidKnot/SytSmallShapeCountsLarger.olean`, so `lean`-direct on
   `symbolic_character_table.lean` fails on an import until that one module is
   compiled. It compiles from source in about a minute.
2. **Lean does not fall through `LEAN_PATH` roots** for a module's transitive
   imports. An overlay directory holding just the missing olean is never
   consulted — the error always names the first root. The overlay only works if
   it is a *full copy* of the QOU build tree with the missing module added.

## Validate baseline

`bun run scripts/run-validate.ts content/quantum-observable-universe` reports
**`✗ Invalid — 29 issue(s)`** at this branch point *before any edit on this
branch* (verified by stashing). Every failure is
`notation-register-tableN-data: Unresolved uses: ""` on the notation chapter,
which nothing here touches. The count is 29 before and 29 after — this branch is
delta-zero. The "`✓ Valid — 10 issue(s)`" figure still in circulation is stale.
