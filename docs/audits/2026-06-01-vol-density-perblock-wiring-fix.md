# VolDensity per-block wiring fix — discipline-gate result (RED)

Branch: `claude/vol-density-perblock-wiring-fix-2026-06-01` (PR #1614)
Companion to the read-only audits PR #1608 (derivation trace) and
PR #1613 (compute-vs-paper). This branch is the **implementation**:
it wires the paper's dropped per-block factor into a real compute
function and exposes — does not hide — the resulting discrepancy.

## The bug

Production `vol_density_borromean` (`computations/_li_2_q_util.py`)
computes the baryon mass geometric factor as

```
VolDensity(𝓑₃, q) = [Vol(𝓑₃)/ℏ_q²] · linking_weight(q),
linking_weight(q) = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²   (H₄ Family-A scalar)
```

a **single global scalar**. The paper (`prop:hoefsmit-scattering-pipeline`
Stage 4) specifies the **forced per-block form**

```
m(K) = m_e · Geom(K) · Σ_λ w_λ χ_λ(β_K)/dim λ,
Geom(K) = Vol(K)/ℏ_q²  (hyperbolic),   w_λ = dim_q(λ)²/[k]_q!
```

over the partitions of the **knot's own strand count**. Production
DROPPED the `Σ_λ` factor and replaced it with the H₄ scalar.

## Index-set finding (H₃ vs H₄)

The Borromean baryon braid `𝓑₃` is a **3-strand** braid → `H₃` →
partitions of **3** (`(3)`, `(2,1)`, `(1,1,1)`). The chi-caches already
carry the canonical per-block Markov trace at the right level:

- `chi-proton-h3-at-q0-50dps.witness.json` → `tr_M(proton) = 1.0653…`
- `chi-neutron-h3-at-q0-50dps.witness.json` → `tr_M(neutron) = 0.9232…`

The Family-A `linking_weight = (1/4)Σ_{λ⊢4} dim_q V_λ` sums over **H₄**
(partitions of **4**) — the **wrong index set** for a 3-strand braid.
This corroborates PR #1608's finding independently.

## Discipline gate — RED (raw, zero fudge)

`computations/vol_density_per_block_wiring.py` computes
both readings at `q_0`. Verdict: the per-block sum does **NOT**
reproduce production at any order with zero fudge.

| quantity | value |
|---|---|
| `Geom_leading = Vol(𝓑₃)/ℏ_q²` | 746.418 |
| `linking_weight` (H₄ global, production) | 2.5328 |
| `tr_M(proton)` (H₃ per-block, paper) | 1.0653 |
| `tr_M(neutron)` (H₃ per-block, paper) | 0.9232 |
| implied λ that round-trips m_p, `m_p/(m_e·Vol/ℏ²)` | 2.4600 |
| **ratio** `linking_weight / tr_M(proton)` | **2.3775** |
| **ratio** `linking_weight / tr_M(neutron)` | **2.7434** |

The h-series of the global scalar **terminates** at `c_0 = 5/2`,
`c_2 = 3/4` (the proved Family-A form). The per-block trace is a
different function entirely.

### Mass predictions (raw)

| reading | formula | m_p (MeV) | err |
|---|---|---|---|
| production | `m_e·Vol/ℏ²·linking_weight` | 966.05 (m_avg) | +2.89 % |
| paper-literal | `m_e·Vol/ℏ²·tr_M` | **406.33** | **−56.69 %** |
| both factors | `m_e·Vol/ℏ²·linking_weight·tr_M` | 1029.14 | +9.68 % |

Per-block neutron (352 MeV) < per-block proton (406 MeV) — **wrong
ordering**. Recovered fraction of the +2.89 % gap by per-block
restoration: **−1963 %** (per-block is far WORSE).

## Verdict

**The global H₄ scalar is NOT the paper's per-block H₃ sum.** They
differ by ≈ 2.38×. Production's near-correct m_p does **not** derive
from the paper's per-block formula as literally written: the global
H₄ scalar lands near the CODATA-implied λ ≈ 2.46 **coincidentally**,
using the wrong index set. This is the structural reason the +2.89 %
m_p gap is "honest, not an error" — production multiplies the
hyperbolic volume by a global Wedderburn average instead of the knot's
own per-block trace content.

**This discrepancy is REPORTED, not hard-coded away.** No factor was
introduced to force the match (which would be the fit-trap the task
forbids). A wired-but-honest per-block function that exposes the real
residual is the correct deliverable.

## What this PR ships

1. `vol_density_per_block(vol_K, tr_M_K, q)` + `geom_leading(vol_K, q)`
   in `_li_2_q_util.py` (alongside the old shortcut, which is marked
   `[SHORTCUT — global-scalar collapse, NOT the paper's per-block sum]`).
   No production switch — the old function is unchanged; the new one is
   available for the paper-faithful evaluation.
2. `vol_density_per_block_wiring.py` + `vol-density-per-block-wiring.witness.json`
   — the discipline-gate verification (asserts FAILURE on the gate).
3. Lean: replaced the trivial `GeomFullFunctorial.functorial : True`
   stub with the real Stage-4 factorisation
   (`G k q = geomLeading k q · perBlock k q`), and extended
   `GeomYekutieliAlignmentContext` with the boundary-holonomy = trM
   (non-abelian Stokes) and massFactor = Geom·trM sub-claims, proved
   from the §3b-cond class fields. Compile-pending (no toolchain in
   the authoring container).

## Recommendation (owner decision)

**Do NOT switch production** to the per-block function as-is: it gives
m_p ≈ 406 MeV (−56.7 %), a large regression on the current +2.89 %. The
per-block restoration is correct **as a derivation** but exposes that
the `tr_M ↔ Geom` join (Yekutieli non-abelian Stokes) is genuinely
unresolved — the global scalar carries an unexplained ≈ 2.38× that the
per-block trace lacks. The productive next step is to derive WHERE the
2.38× comes from (it is `linking_weight / tr_M(proton)`, q-dependent,
not a clean constant), not to re-pin the global scalar. See PR #1608 §
"the gap" and PR #1611 (q-hyperbolic Stokes wiring) for the join.
