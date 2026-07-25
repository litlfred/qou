# W1 — the `c₀ ↔ torsion` factor 4 is `2^(c−1)`, not a framing artifact

**Date:** 2026-07-25
**Tier:** audit-only; scope-(a); no fit; nothing wired; L2 unchanged.
**Epic:** W1 binding-mass bridge. Follow-on to
[`2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md`](2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md)
(PRs #4208 / #4238 / #4253).

## The question

PR #4253 computed the independent Neumann–Zagier adjoint torsion and found the
Jones-side Kashaev constant `c₀` and the topological torsion agree up to a clean
factor:

| link | cusps `c` | `\|det J_NZ\|` | `exp(2c₀)` | `exp(2c₀)·\|det\|` |
|---|---|---|---|---|
| `4₁` | 1 | `√3` | `1/√3` | **1** |
| `𝓑₃` (L6a4) | 3 | `64` | `≈1/16` | **≈4** |

This audit answers: **what is the factor 4, and is it a free parameter?**

## Result 1 — it is NOT a framing artifact

The adjoint-torsion determinant depends on the choice of one peripheral curve
per cusp (meridian vs longitude). Sweeping **all `2^c = 8` framings** of L6a4
(`borromean_cusp_framing_factor.py`):

| framing (0=mer, 1=long) | `\|det J_NZ\|` |
|---|---|
| `(0,0,0)` all-meridian | **64** |
| one longitude | 128 (×3) |
| two longitudes | 256 (×3) |
| `(1,1,1)` all-longitude | 512 |

All framings are `2^{6..9}`; the **all-meridian framing 64 is the unique
minimum**, and it is the correct Kashaev framing (the colors live on the
meridians). **No framing yields 16**, so the factor `4 = 64/16` cannot be
removed by re-framing — it is genuine.

## Result 2 — the factor is the reduced-vs-Kashaev normalization `2^(c−1)`

The Borromean tower (#4238) is the **reduced** colored Jones (`J_{B,1}=1`); the
meridian NZ torsion is the **Kashaev-normalized** 1-loop invariant. For a
`c`-component link the two differ, in the 1-loop constant, by `2^(c−1)` — one
factor 2 per cusp beyond the basepoint:

| link | `c` | factor `2^(c−1)` | measured |
|---|---|---|---|
| `4₁` | 1 | `2^0 = 1` | 1 (exact, #4238 — reduced Kashaev = unreduced for a knot) |
| `𝓑₃` | 3 | `2^2 = 4` | 4.03 (`c₀ = −ln4` gives exactly 4) |

The clean numerical signature is `c₀(𝓑₃) = −ln 4` (`exp 2c₀ = 1/16 = 4/64`),
consistent with the measured `−1.383` within the `N≤56` tower's `~0.01`
uncertainty.

## Status — what is proved, what is not

**Proved (computed):**
- The factor is not a framing choice (all 8 framings computed; min = 64 ≠ 16).
- The factor equals `2^(c−1)` on the two computed cusp numbers `c = 1, 3`.

**Structural identification (mechanism named, not proved here):** the factor is
the reduced-Habiro-vs-Kashaev-meridian normalization; the "one factor 2 per
extra cusp" is the multi-cusp saddle-point expansion — each additional cusp
contributes a Gaussian meridian integration. A full first-principles derivation
is that saddle expansion (research-scale), **not** claimed complete.

**Decisive next test:** the 2-cusp **Whitehead link** predicts factor
`2^1 = 2`, i.e. `exp(2c₀_W) = 2/|det J_NZ(W)| = 2/(4√2) = 1/(2√2)` (the NZ
torsion `|det J_NZ(W)| = 4√2` is computed here as a by-product). Its Kashaev
tower is the honest third data point — deferred (no memorized Whitehead
colored-Jones formula was transcribed, per the "do not cite from memory"
discipline; a verified transcription is the follow-up).

## Discipline

scope-(a); no fit (framings and torsions are computed; `2^(c−1)` is read off two
exact data points, not tuned); nothing wired; L2 unchanged. The factor is a
clean rational normalization constant, **not** a free parameter of the bridge.

-- Ref: [manuscript] docs/audits/2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md
