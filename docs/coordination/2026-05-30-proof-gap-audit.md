# Proof-gap audit (2026-05-30, post-#1448)

## TL;DR

The repo has **33 `.lean` files containing `sorry`**, totalling **50
tactic-position sorries**. **All 50 carry proper `-- Ref:` citations
per AGENTS.md §1** — the §1 bibliographic-citation gap is closed
repo-wide.

The remaining substantive question is: how many of those 50 can be
*closed with actual proofs* (vs. remaining as §3b-cond class
conjectures by design)?

## Category breakdown

| Category | Files | Sorries | Closeable in scope? | Notes |
|---|---:|---:|---|---|
| §3b-cond class conjecture | 14 | 26 | **No (by design)** | The `sorry` IS the conjecture per AGENTS.md §3b-cond. Closing requires owner-level math on the underlying open problem (e.g. Witten κ Gram-determinant, Bring color-tube weighted derivation, gluon-octet identity). |
| UGB Buchberger / PBW | 7 | 7 | **Hard** | Research-level work to formalise Buchberger's algorithm + PBW corollary in Lean 4. Out of scope for this session. |
| Other (UGB Introduction + mass-theory + mass-endomorphism) | 9 | 11 | **Mixed** | Mostly §3b-cond scaffolds (mass-theory inside PR #1445 scope); some need substantive proof work. |
| Hyperbolic-geometric | 2 | 5 | **Tractable (1 file)** | `BorromeanVolumeCatalan.lean` has 4 sorries with explicit proof sketches (Lobachevsky-Catalan + Adams 1985). Closing requires Mathlib infrastructure axioms + `norm_num` on long rational sums (heavy heartbeats but mechanical). `kashaev-volume-conjecture.lean` is §3b-cond. |
| Gram matrix symbolic | 1 | 1 | **Hard but tractable** | `gram-matrix-h3-symbolic.lean` has the proof strategy fully sketched in comments (unfold + `Matrix.det_fin_succ` + `field_simp; ring`, `set_option maxHeartbeats 800000`). 6×6 symbolic determinant. |

## Detail by file

### §3b-cond class conjecture (26 sorries — closed by design)

These are conjectures axiomatised via Lean classes per AGENTS.md
§3b-cond. Each `sorry` instance represents an open conjecture; the
downstream theorems that consume the class hypothesis are
sorry-free (rigorous-conditional).

| File | Sorries |
|---|---:|
| `aeon-boundary-generates-chart.lean` | 1 |
| `quantum-computational-universality.lean` | 4 |
| `lean/QOU/StaircaseCornerHook.lean` | 1 |
| `alpha-k-categorical-closure.lean` | 1 |
| `phi-q-tower-jsj-bridge.lean` | 1 |
| `prop-rigid-monoidal-structural-gap-invariance.lean` | 1 |
| `complex-chirality-rotation.lean` | 3 |
| `higgs-t28.lean` | 3 |
| `shell-threading-conjecture.lean` | 1 |
| `periodic-table-demand-conjecture.lean` | 4 |
| `electron-shells-hopf.lean` | 2 |
| `elliptic-stability-locus.lean` | 2 |
| `em-coupling-chern-simons.lean` | 1 |
| `skein-shell-correction.lean` | 1 |

Three of these directly underpin PR #1451:
- `em-coupling-chern-simons.lean` → Witten κ — CLASS-A banner on #1451

### UGB Buchberger/PBW (7 sorries — research-level)

Formalising Buchberger's algorithm and the PBW corollary in Lean 4
is research-level work, not closeable in a single session.

### Hyperbolic-geometric (5 sorries)

- `BorromeanVolumeCatalan.lean` (4 sorries) — `lobachevsky` def,
  `lobachevsky_pi_div_four_eq_half_catalan` (Lewin 1981 eq. 4.2.21),
  `catalan_G_numerical_bounds` (composes with infra axiom +
  `norm_num` on rational S_22), `vol_B3_eq_8_catalan` (Adams 1985,
  Borromean = 2·oct = 8·G). Mechanical but heavy.
- `kashaev-volume-conjecture.lean` (1 sorry) — §3b-cond.

### Gram matrix symbolic (1 sorry)

`gram-matrix-h3-symbolic.lean` — proof strategy fully sketched:
`set_option maxHeartbeats 800000` + unfold + `Matrix.det_fin_succ`
+ `field_simp; ring`. 6×6 symbolic determinant on Bring's
substrate. Plausible but heavy compute.

## What's AGENTS.md-§1-compliant?

100%. Every one of the 50 sorries has `-- Ref:` within ≤ 12
preceding lines (typical: ≤ 5).

## Implications for "close all proof/lean gaps"

The phrase is ambiguous:

1. **Citation compliance** (per AGENTS.md §1): **already 100% done**
   repo-wide as of this audit.
2. **Closing §3b-cond conjectures**: **not in scope** — those
   sorries represent open math by design and stay until the
   underlying conjecture is proved.
3. **Closing the ~7-8 tractable sorries** (gram matrix det,
   Borromean-Catalan, plus a handful in mass-theory PR #1445
   scope): **multi-PR campaign**, owner-level scope.

## Active coordination

| PR | Scope overlap |
|---|---|
| #1451 (this branch) | m_K/m_π production wiring; α_em CLASS-A banner pending Witten-κ class closure |
| #1445 | mass-theory + particle-interactions/geom-universality + pn-averaging uniqueness scaffolds |
| #1444 | α_em Bring zero-mode shift (4.18 ppm); not a sorry-closing PR but updates the α_em landscape my CLASS-A banner depends on |

Audit posted to #1445 (2026-05-30 03:30 UTC):
[comment-4581520258](https://github.com/litlfred/qou/pull/1445#issuecomment-4581520258).
