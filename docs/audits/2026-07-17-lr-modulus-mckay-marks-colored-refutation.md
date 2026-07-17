# LR modulus ID — the McKay-mark colored Σ(2,3,5) route is refuted (scope-(a))

**Date:** 2026-07-17 · **Axis:** W_λ keystone / L2 m_p·m_μ root cause ·
**Executes:** [`2026-07-17-three-front-attack-specs.md §2`](2026-07-17-three-front-attack-specs.md)
(companion to [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)) ·
**Probe:** [`keystone_valuemap_colored_marks_s013.py`](../../computations/probes/keystone_valuemap_colored_marks_s013.py) ·
**Tier:** scope-(a) numerical falsification; no fit, nothing wired, no tier change.

## What was tested

The keystone value-map target is `W_λ = bwS0(λ) = d_ζ(λ)/D(ζ)`, a **4-class**
family at n=5 with ratios `(1, 4.110, 5.220, 6.220)` for the S₅ partitions
`(5), (4,1), (3,2), (3,1,1)`. The merged
[`s013`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py)
probe validated the genuine Σ(2,3,5) false-theta S-matrix (Hikami math-ph/0405028)
and **refuted** the naive identification of `bwS0` with the theory's **D=2**
vacuum row (2 components, golden-ratio φ). The three-front spec §2 asked the
refined question: does the **McKay-mark coloring** escape that collapse?

The mapping (spec §2, values on **marks** — the `[e]_q` exponent map was refuted):
the 4 bwS0 classes carry S₅-dimensions `{1, 4, 5, 6}`, four of the Ê₈ marks /
2I irrep dimensions `{1,2,2,3,3,4,4,5,6}` under McKay(2I↔Ê₈)∘(A₅⊂S₅). Insert the
color `α = dim_{S₅}(λ)` on the **p₃=5 numerator fibre** of the WRT invariant
(SU(2) coloring: `sin(nπ/(N·5)) → sin(α·nπ/(N·5))`).

**Anti-fabrication anchor (passed to machine zero):** color `α=1` reproduces the
bare `s013.tau_N` exactly (`max_N |τ_N^{α=1} − τ_N| = 0` at N∈{3,5,7,11,13}).

## Result — REFUTED (scope-(a)), the pre-registered K1/K2/K3 outcome

The spec-§2 target `|S_{0λ}| = d_ζ(λ)/D` fails. The would-be vacuum→(1,1,α)
S-matrix entry is `|S_{0,(1,1,α)}| = √(32/P)·|sin(π/4)·sin(π/3)·sin(6απ/5)|`, and
on the marks:

| class | α (mark) | \|S_{0λ}\| | \|S_{0λ}\|/\|S_{0,(5)}\| | target |
|---|---|---|---|---|
| (5) | 1 | 0.525731 | 1.0000 | 1.0000 |
| (4,1) | 4 | 0.525731 | 1.0000 | 4.1097 |
| (3,2) | 5 | **0.000000** | 0.0000 | 5.2204 |
| (3,1,1) | 6 | 0.525731 | 1.0000 | 6.2204 |

- **K2 — collapse:** the nonzero marks give **one** distinct modulus
  (`0.525731 = (2/√5)sin(π/5)`, the icosahedral flat weight), not 4. Escape
  needed 4 independent moduli.
- **K1 — ratio mismatch:** `(1,1,0,1)` vs the target `(1, 4.11, 5.22, 6.22)`,
  maxdev `5.22` — the identity fails at every entry.
- **K3 — fibre wrap:** the p₃=5 Seifert fibre supports only colors `1..4`
  (SU(2)₅ Weyl reflection `α ↔ 5−α`, so `|S_0^{α=4}| = |S_0^{α=1}|`); the marks
  `≥ 5` wrap — `α=5` vanishes (split node, `sin(6π)=0`), `α=6` returns
  `[6]_ζ = 6.388 ≠ [5]_ζ+1 = 6.220`.

## Reading

The keystone `W_λ = d_ζ(λ)/D` index is **not** carried by the McKay-colored
Σ(2,3,5) false-theta S-matrix: coloring the single p₃=5 fibre with the marks
`{1,4,5,6}` collapses to one nonzero modulus plus the α=5 zero, exactly because
the fibre's SU(2)₅ label range is `1..4`. This is **scope-(a)** — it excludes
this *specific geometric object* (the McKay-mark coloring of the one exceptional
fibre), not the W_λ index question itself. As s013 already indicated, a **larger
geometric family** is required: more exceptional fibres (larger D), or genuinely
colored knot-complement blocks, so that four independent modular components exist
to carry the 4-class target. The Lean `loc_matches` derivation gate stays open.

## Follow-up

- Bib entries `lawrence-zagier-1999`, `hikami2005brieskorn` are cited as
  `# Ref:` comments in the probe; they need `references.ts` entries before any
  Lean `-- Ref:` (spec §2 bib gap) — deferred (no Lean gate is closed here).
- The productive direction per this negative: enlarge D via additional
  Brieskorn fibres or a colored knot-complement family, rather than more colors
  on the single p₃=5 fibre.

## Cross-references

- Reused machinery + prior D=2 refutation: `keystone_valuemap_genuine_smatrix_s013.py`.
- Keystone value map: `s5-so3-keystone.md` ledger; `2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`.
- Spec: `2026-07-17-three-front-attack-specs.md §2`; reassessment: `2026-07-17-1ppq-path-reassessment.md`.
