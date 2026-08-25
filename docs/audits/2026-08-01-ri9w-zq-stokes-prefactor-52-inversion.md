# 5₂ `Z[q^±]` Stokes prefactor — the inversion relation (GGM eq 4) and the FW↔GGM Jacobian tie

**Date:** 2026-08-01 · **Bean:** `qou-ri9w` (harder half — the exact
`Z[q^±]` Stokes prefactor) · **Branch:**
`claude/ri9w-zq-stokes-prefactor-2026-08-01` · **PR:** #4487 (draft) ·
**Tier:** literature transcription + identification (scope-(a)).
**No fit; nothing wired; c₃ read-off downstream and NOT claimed derived.**

**Probe:**
[`computations/probes/fivetwo_stokes_matrix_zq.py`](../../computations/probes/fivetwo_stokes_matrix_zq.py)
· witness
[`fivetwo-stokes-matrix-zq.witness.json`](../../computations/probes/fivetwo-stokes-matrix-zq.witness.json).

## Source

Garoufalidis–Gu–Mariño, *The resurgent structure of quantum knot
invariants* ([arXiv:2007.10190v2](https://arxiv.org/abs/2007.10190),
CMP 2021; `library/arxiv-2007.10190v2/2007.10190v2.pdf`), §3 (the equation `x⁻²(1−x)³ = 1`
and the 5₂ knot), eqs (22)–(29). Registered as
`garoufalidis-gu-mariño2021`. The Stokes automorphism of the 5₂
resurgent structure is a **pair of `3×3` matrices `S⁺(q), S⁻(q)` of
q-series with integer coefficients**, assembled from the fundamental
solutions `W_m(q)` of the linear q-difference equation (23).

## What was already in the corpus (cited, NOT duplicated)

The 5₂ Stokes matrices themselves were **already transcribed and
integrality-verified** before this PR — the "transcribe the matrices"
half of the deliverable was in hand:

| corpus object | PR | content |
|---|---|---|
| `qbeta_g3_5two_analytic_hm_tower.py` | #4011 | exact rational q-series for the `Hᵉ_{k,m}(q)` tower + fundamental solution `W₋₁(q)` (GGM eqs 24/25, App. A) |
| `qbeta_g3_5two_stokes_sandwich.py` | #4013 | assembles `S⁺(q)`/`S⁻(q)` from eqs (29a/b); verifies K1 (q→0 limits = printed factorizations, Stokes constants `{3,4,9}`), K2 (integrality of every entry as a `Z[q^±]` series to O(q¹⁸)), K3 (det `S± = 1`) |
| `qbeta_5two_chirality_state_integral_probe.py` | #4475 | the AK state integral `I_{0,0}=Z_{5₂}=∫Φ_b³e^{−2πiv²}dv` on the substrate ray, quadrature-vs-GGM-eq-110-factorization matched |
| `docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md` | — | the FW framing: median-Borel(`Φ_{5₂}`) is a `Z[q^±]`-combination of the `I_{m,ℓ}`, with the Stokes matrix as the wall-crossing (Jacobian) data |

This PR **reuses** the #4011 tower + #4013 assembly rather than
re-transcribing them.

## What this PR adds (genuinely new)

### V1 — the inversion relation `S⁺(q)ᵀ S⁻(q) = I` (GGM eq 4), verified exactly

GGM **Conjecture 1(b)** (eq 4) is the defining consistency/cocycle
property of the Stokes **pair**:

```
S⁺(q)ᵀ · S⁻(q) = 1 .
```

This is **not** checked anywhere else in the corpus — the sandwich probe
(#4013) verifies only the q→0 limits, integrality, and `det = 1`, none
of which constrains the *relation between* `S⁺` and `S⁻`. The probe
computes `S⁺(q)ᵀ · S⁻(q)` in exact rational q-series arithmetic and
confirms it equals the identity to **O(q¹⁸)** (and exactly on the
integer q→0 matrices `S⁺(0)ᵀ S⁻(0) = I`).

This is the **multiplicative companion** to the *additive/realness* leg
of `qou-ri9w` that landed as PR #4485
(`G3RealnessConjugationBrick.lean`, `ratio_star_fixed_of_shared_law`):
realness fixes the star-conjugation covariance; the inversion relation
fixes the pair's mutual consistency. Together they pin the two sides of
the Stokes datum.

### V2 — the fundamental-solution certificates (eqs 26, 28)

New exact-series cross-checks that make `S±` well-defined:
- `det W₋₁(q) = 2` (eq 26; the probe reports the constant `−2` under the
  sandwich probe's row orientation — magnitude 2, exact).
- The W-sandwich identity (eq 28) at `m = 0`:
  `½·W₋₁(q)·J·W₋₁(q⁻¹)ᵀ = [[1,0,0],[0,0,1],[0,1,3−q⁰]] = [[1,0,0],[0,0,1],[0,1,2]]`,
  `J = antidiag(1,2,1)` — verified to O(q¹⁸).

### V3 — Stokes constants and the DGG 3D-index tie (Conjecture 2)

The 5₂ Stokes constants are `{3, 4, 9}` (|entries|>1 of `S±(0)`). The
`σ₁σ₁` entry `S⁺₀₀(q)` is the DGG **rotated 3D-index** `Ind^rot_{5₂}(q)`
(Conjecture 2, eq 5). The probe's exact q-series

```
S⁺₀₀(q) = 1 − 12q + 3q² + 74q³ + 90q⁴ + 33q⁵ − 288q⁶ − 684q⁷ + …
```

matches GGM's **printed** `Ind^rot_{5₂}(q) = 1 − 12q + 3q² + 74q³ + 90q⁴
+ O(q⁵)` (p.19) **exactly** — an independent confirmation of both the
transcription and the Conjecture-2 identification.

### V4 — the FW↔GGM Jacobian prefactor identification

`I_{0,0}=Z_{5₂}` and `S±(q)` are two contractions of the **same**
fundamental solution `W₋₁`:
- the AK integral factorization (GGM eq-110, used by #4475) is the
  bilinear `Hᵉ·J·Hᵉ'` of the tower rows;
- `S±(q)` (eq 29) is `½·L±·W₋₁·J·W₋₁ᵀ·R±` of the same `W₋₁`.

So the integer matrices `L±, R±` together with the frame phase
`e^{πi/4}` **are** the Jacobian prefactor of the FW↔GGM
median-resummation correspondence (median-Borel(`Φ_{5₂}`) = Stokes-weighted
`Z[q^±]`-combination of the `I_{m,ℓ}`). The probe reports the leading
one-instanton weight `e^{−V(σ₁)/2πτ}` at the substrate and the leading
`σ₁σ₁` Stokes constant `−12`, whose product is the leading `(S−I)Φ`
contribution the prefactor makes to the resummation.

## Residual toward FULL numeric equality (the open gap)

Turning the identification into a numeric **equality**
`median-Borel(Φ_{5₂}) = Σ (Stokes-weighted) I_{m,ℓ}` requires the
**median-Borel resummation of the perturbative `ϕ_{σⱼ}(τ)`** (eq 20 —
the factorially-divergent series), which is **NOT** performed here. That
is the honest open gap, captured as bean **`qou-9dvz`**. This PR
delivers the *prefactor* and its defining properties, not the
resummation of the divergent series it multiplies.

## Discipline

Literature transcription + identification; primary-source read (pymupdf
on the owner-supplied PDF). No fit; no `c_k` wired; c₃ not claimed
derived; registry untouched. scope-(a). Corpus-grep confirmed the
inversion relation (eq 4) at the `S±` matrix level is absent from
`computations/` and `docs/audits/`. Bean `qou-ri9w` is not present in
this worktree's `.beans` store (the store on `main` does not carry it) —
noted rather than force-updated.

## Cross-references

- GGM 2007.10190 §3, eqs (22)–(29) (`library/arxiv-2007.10190v2/2007.10190v2.pdf`); printed
  `Ind^rot_{5₂}`, p.19.
- Corpus 5₂ chain: `qbeta_g3_5two_analytic_hm_tower.py` (#4011),
  `qbeta_g3_5two_stokes_sandwich.py` (#4013),
  `qbeta_5two_chirality_state_integral_probe.py` (#4475).
- Realness companion (additive leg of ri9w): PR #4485,
  `G3RealnessConjugationBrick.lean` (`ratio_star_fixed_of_shared_law`).
- FW reframe: [`2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`](2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md).
- 4₁ per-winding Stokes context: [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md).
- Gap bean: `qou-9dvz` (median-Borel resummation of `ϕ_{σⱼ}`).
