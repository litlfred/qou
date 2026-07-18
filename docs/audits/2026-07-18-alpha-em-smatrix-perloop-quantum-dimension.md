# α_EM per-loop measure: the RT/WRT modular-S-matrix total quantum dimension — the redirect tested and its π located

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) on the value axis, (b)-structural on the π axis; no `α_k` wired; no
fit; `1/(8π)` stays a phase-4 identification) · **Branch:**
`claude/alpha-em-perloop-Smatrix-2026-07-18` · **Probe:**
[`alpha_em_smatrix_perloop_probe.py`](../../computations/alpha_em/alpha_em_smatrix_perloop_probe.py)
· **Witness:**
[`alpha-em-smatrix-perloop.witness.json`](../../computations/alpha_em/alpha-em-smatrix-perloop.witness.json).

## The constraint this probe inherits (from #3870 + #3882)

#3870 ruled out the naive flat-torus Maxwell 1-loop partition function on the
photon target `J(M) = Jac(Bring) ~ T^8` as the per-loop measure
`1/(π·b₁) = 1/(8π)` (`b₁ = dim H¹(M_Bring) = 2g = 8`), sharpening the target into
a **three-axis constraint**. #3882 (Ray–Singer torsion) then showed every
flat-torus spectral invariant is either **extensive** in `b₁` or a **covolume**
— never reciprocal — and concluded the measure must live **off** the flat-torus
determinant, on the **RT/WRT modular-`S`-matrix total quantum dimension**:

$$
  D \;=\; \sqrt{\textstyle\sum_i d_i^{\,2}}, \qquad S_{00} \;=\; \frac1D ,
$$

the Verlinde per-handle measure. The three axes any valid object must meet:

| axis | requirement |
|---|---|
| **(i)** | area / covolume-**free** (topological) |
| **(ii)** | π-power **exactly −1** — a **bare** π, not `2π` |
| **(iii)** | **reciprocal** in the mode count (`b₁^{−1}`, a `1/(total-count)` democratic average) |

This probe tests that redirect directly, each axis measured **independently**
and only then compared — **never** solving `D` from CODATA, **never** inserting a
π by hand to reach `8π` (AGENTS.md §"Axiomatization is NOT a Proof",
§"Before declaring refuted", α_EM standing rule).

## Method — reuse the genuine Σ(2,3,5) S-matrix (do not rebuild it)

The redirect names the photon's candidate category as the nonabelian `S`-matrix
of the `W_λ` keystone — the Σ(2,3,5) (Poincaré sphere `S³/2I`, binary-icosahedral)
WRT / false-theta modular data. That `S`-matrix was transcribed from the primary
source (Hikami, math-ph/0405028, eq. 3.8) and **machine-validated** in #3822
([`keystone_valuemap_genuine_smatrix_s013.py`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py):
`S² = 1`, vacuum row = Corollary-12 flat-connection weights, `φ(2,3,5) = 181/30`,
Theorem 10 exact to `1e−28`). This probe **imports** `s_entry` from that module
and reads off the total quantum dimension — it does not re-derive the `S`-matrix.

**Controls (all pass, `|err| < 1e−40`).**

- `D(2,3,5) = (p₁−1)(p₂−1)(p₃−1)/4 = 2` primary fields (Hikami §5).
- `S² = 1` (involution).
- vacuum row `= (2/√5)(sin π/5, sin 2π/5)` (Corollary 12).
- unitary row normalization `Σ_i |S_{0i}|² = 1` (exactly `5/4·4/5 = 1`).
- row ratio `= sin(2π/5)/sin(π/5) = 2cos(π/5) = φ` (golden ratio).

## Result — the total quantum dimension in closed form

The vacuum row gives quantum dimensions `d_i = S_{0i}/S_{00}` = the
**icosahedral / Fibonacci pair `{1, φ}`**, hence

$$
  \sum_i d_i^{\,2} = 1 + \varphi^2 = 2 + \varphi = \frac{5+\sqrt5}{2} \approx 3.6180,
  \qquad
  D = \sqrt{\tfrac{5+\sqrt5}{2}} \approx 1.9021,
  \qquad
  S_{00} = \frac1D = \frac{2}{\sqrt5}\sin\frac\pi5 \approx 0.5257 .
$$

All three are **algebraic in `ℚ(√5)`** — there is **no π**. `S_{00} = 1/D` is
reproduced to `1e−40` (the vacuum entry *is* the reciprocal of the total quantum
dimension).

## Comparison to the target (no CODATA, no fit)

| quantity | value | `/8` | `/8π` | `= 8`? | `= 8π`? |
|---|---|---|---|---|---|
| `D = √(Σd_i²)` | `1.9021` | `0.2378` | `0.0757` | no | no |
| `Σ d_i²` | `3.6180` | `0.4523` | `0.1440` | no | no |
| target `π·b₁` | `8π = 25.133` | — | — | — | — |

Neither the total quantum dimension nor its square is `b₁ = 8` or `8π`.

**Cross-check — the other natural "keystone `S`-matrix" reading (#3853).** The
`n=5` Hecke hook-content pseudo-dimensions `d_q(λ) = [n]_q!/∏[hook]_q` at the
*observable* `q₀` (a non-unitary object, not a root-of-unity `S`-matrix) give
`D(q₀) = √(Σ_{λ⊢5} d_q²) = 11.357` — **also** `∉ {8, 8π}`. Both natural readings
of "the photon's keystone `S`-matrix" miss `b₁ = 8`: a robust double-negative on
the value axis.

## Three-axis verdict

| axis | verdict | why |
|---|---|---|
| **(i)** area-free | **✓** | the magnitudes are `√(Reidemeister torsion)` (Hikami Thm 14) — a topological invariant, no length scale |
| **(ii)** π-power `−1` | **✗ (b)-structural** | `D, Σd_i², S_{00} ∈ ℚ(√5)` are **algebraic**. Every MTC quantum dimension is a cyclotomic algebraic integer's ratio (`2cos(πk/n)`-type), so `S_{00} = 1/D` carries **no bare π** — π-power `0`, not `−1` — for **any** root-of-unity `S`-matrix, not just this one |
| **(iii)** reciprocal | **✓ FORM / ✗ VALUE** | `S_{00} = 1/D` **is** the redirect's `1/(total-count)` democratic average — but the count is `D ≈ 1.902` (or `Σd_i² ≈ 3.618`), **not** `b₁ = 8`; the genuine Σ(2,3,5) family has only **2** primary fields, far too few to be the `b₁ = 8` harmonic-1-form count |

## Verdict — scope-(a) NEGATIVE on value; the redirect's *form* confirmed; the π located

The RT/WRT `S`-matrix supplies the **correct reciprocal-`1/D` FORM** the redirect
predicted (axis iii shape ✓), but:

- **on VALUE (a):** the genuine Σ(2,3,5) family gives `D = √((5+√5)/2) ≈ 1.902`,
  neither `8` nor `8π`; the `n=5` Hecke reading gives `11.357`, also neither. Not
  excluded: a **larger** MTC (more primary fields than the `D=2` Σ(2,3,5) family)
  whose total quantum dimension equals `b₁ = 8` could still carry the reciprocal
  count.
- **on the π (b)-structural:** **no** `S`-matrix supplies the bare π. `D` is a
  cyclotomic algebraic integer, so the "**`D = π·b₁ = 8π` (π categorical)**"
  branch of the #3853 acceptance gate is **structurally impossible**, not merely
  unmatched. This *decides* that gate's open ambiguity in favour of the other
  branch: **π is the universal archimedean 1-loop factor, never categorical.**

## Where the π must come from (named, not hand-inserted)

The RT/WRT normalization's **only** π's are in **unit-modulus framing /
Chern–Simons phases** — the Gauss-sum prefactor `e^{πi/4}` of `τ_N` (eq. 2.11),
the CS invariants `(−1/120, −49/120)` as `e^{−πiN·CS}` (Cor. 12), the surgery
phase `e^{−n²πi/(2PN)}`. These have **magnitude 1**, so they cannot supply a real
`1/π` to the measure either. The bare real π in `1/(π·b₁)` is therefore
**archimedean**: the 1-loop determinant / heat-kernel eigenvalue normalization
`4π²` (the `log(4π²)` in `ζ'_{Δ₀}(0)`, #3882), consistent with the ledger's
standing boundary **"`b₁` topological, π archimedean, `[2]_q` substrate"** (PR
#2114).

**The two factors of `1/(π·b₁)` have different homes.** `1/b₁` is a categorical
`1/(total-count)` reciprocal (RT total-quantum-dimension *shape*, confirmed here);
`1/π` is an archimedean 1-loop determinant factor. The "one object supplies both"
hypothesis (the shared-wall `S_{00} = 1/D` with `D = 8π`) is refuted; the measure
is a **product** of a categorical count-reciprocal and an archimedean π.

## The sharpened redirect

The reciprocal-`1/D` form is the right structural home for `1/b₁`. Two separated
open items remain:

1. **Value (`1/b₁`):** find the MTC whose total quantum dimension is the *count*
   `b₁ = 8` (or equivalently `Σd_i² = 8`). The `D=2` Σ(2,3,5) family (`D≈1.902`)
   and the `n=5` Hecke reading (`11.357`) both miss; the object must have exactly
   the `b₁ = 8` harmonic-1-form content of the genus-4 Jacobian, i.e. a **genus-4
   / `2g`-field** modular object, not the icosahedral `D=2` family. (A total
   quantum dimension `Σd_i² = 8` is realised e.g. by `𝔻(ℤ/2)^{×3}` or an
   `su(2)_6`-type datum — a *count*-carrying nonabelian object — but which one is
   the photon's is the open identification, and must be **derived**, never fitted
   to `8`.)
2. **π (`1/π`):** the archimedean 1-loop determinant normalization `4π²`
   (`ζ'_{Δ₀}(0)`, #3882) — **not** the `S`-matrix. This is the same
   heat-kernel object as the proved zero-mode measure `1/Area = 1/(12π)`;
   deriving the *specific* `1/(π·b₁)` from it is the honest multi-week item the
   derivability map (#3612 / 2026-07-14) already isolated.

## Kill criteria (pre-stated, and how they resolved)

- **Negative** if `D ∉ {8, 8π}` or the `S`-matrix carries no bare π → report
  scope-(a)/(b) negative, do **not** stretch conventions to manufacture `8π`. →
  **Both hit**; reported negative; nothing stretched.
- **Positive-partial** only if `1/D` reproduces `1/(π·b₁)` with **each** factor
  sourced. → **Did not occur** — the π has no `S`-matrix source; the value misses.

Anti-laundering respected: no CODATA read, no convention tuned toward `8π`,
controls checked against #3822's machine-validated closed forms.

## Cross-references

- #3882 torsion redirect (the immediate predecessor / the "measure lives on the S-matrix" lead): [`2026-07-18-alpha-em-torsion-perloop-redirect.md`](2026-07-18-alpha-em-torsion-perloop-redirect.md)
- #3870 flat-torus Maxwell (the three-axis constraint origin): [`2026-07-18-alpha-em-flat-torus-maxwell-perloop.md`](2026-07-18-alpha-em-flat-torus-maxwell-perloop.md)
- #3853 shared-wall acceptance gate (the `D = 8` vs `D = 8π` ambiguity this probe decides): [`alpha_em_2I_total_quantum_dimension_gate_test_probe.py`](../../computations/alpha_em/alpha_em_2I_total_quantum_dimension_gate_test_probe.py)
- #3822 genuine Σ(2,3,5) S-matrix (the reused machinery): [`keystone_valuemap_genuine_smatrix_s013.py`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py), [`2026-07-17-lr-modulus-identification.md`](2026-07-17-lr-modulus-identification.md)
- Derivability map / the wall + the `H = [2]_q/(π·D)` target: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md), [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
