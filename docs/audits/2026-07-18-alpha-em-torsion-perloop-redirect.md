# α_EM per-loop measure: Ray–Singer torsion and graded determinants — the redirect off the flat-torus determinant

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a); no `α_k` wired; no fit; `1/(8π)` stays a phase-4 identification until
genuinely derived) · **Branch:** `claude/alpha-em-perloop-torsion-2026-07-18`.

## The constraint this probe inherits (from #3870)

#3870 ruled out the naive flat-torus Maxwell 1-loop partition function
`Z_Maxwell(T^{b₁})` as the per-loop measure `1/(π·b₁) = 1/(8π)`, and in doing so
**sharpened the target into a three-axis constraint.** Any valid normalization
object must be simultaneously:

| axis | requirement | what the naive Maxwell `Z` produced instead |
|---|---|---|
| **(i)** | area / covolume-**free** (as `ζ_{Δ₁}(0) = −b₁` is) | covolume `Vol(J) ∝ L^{d(d−2)/2}` survives (exp. 24 at `d=8`) |
| **(ii)** | π-power **exactly −1** — a **bare** π, not `2π` | `π ∝ b₁` as `(2π)^{−b₁/2}` (measure `2π`, not `π`) |
| **(iii)** | **reciprocal** in `b₁` (`b₁^{−1}`) | `b₁` in the **exponent** — exponential, not `1/b₁` |

The area-free **numerator** count `ζ_{Δ₁}(0) = −b₁` (#3834) is untouched — it is
the correct home of the mode-*count*. Only the **measure** (the bare π + the
reciprocal form) is open. This probe tests the next-obvious spectral/torsion
objects on the photon target `J(M) = Jac(Bring) ~ T^8` against those three axes,
**each measured independently and only then compared** (never solved from CODATA,
never tuned toward `8π`).

## Approach (STRICT — anti-laundering)

Compute each candidate's π-power, `b₁`-dependence, and covolume-dependence from
its own definition, using a ζ-regularized determinant. This required extending
the #3834 Epstein machinery from `E_Λ(0)` (the ζ(0) count) to **`E'_Λ(0)`** (the
ζ'(0) determinant): for the self-dual cubic lattice `ℤ^d`,

$$
  E'_{\mathbb Z^d}(0) \;=\; \int_1^\infty\!\Big(\tfrac1t + t^{d/2-1}\Big)\big(\theta_d(t)-1\big)\,dt
    \;-\;\tfrac2d\;-\;\gamma\;-\;\log\pi ,
$$

derived from `π^{−s}Γ(s)E(s) = F(s)` (the completed-zeta heat-kernel split) via
`1/Γ(s) = s + \gamma s^2 + \cdots`. The scalar-Laplacian determinant on the
torus `ℝ^d/(Lℤ)^d` is then
`ζ'_{Δ₀}(0) = -2\log L + \log(4\pi^2) + E'_Λ(0)` — the eigenvalue normalization
`4π²` is the **π source**.

## Results (probe [`alpha_em_torsion_perloop_probe.py`](../../computations/alpha_em/alpha_em_torsion_perloop_probe.py), witness [`alpha-em-torsion-perloop.witness.json`](../../computations/alpha_em/alpha-em-torsion-perloop.witness.json))

**Controls (all pass).**

- `ζ_{Δ₁}(0) = −b₁` reproduced (`d = 1, 2, 8`; `|err| < 1e−7`).
- The new `E'_Λ(0)` machinery reproduces the `d=1` closed form
  `E'_{ℤ}(0) = 4ζ_R'(0) = −2\log(2π) = −3.67575\ldots` to `|err| = 0`.
- The **circle determinant control** `ζ'_{S¹}(0) = −2\log L`
  (`det{}'\Delta_{S¹} = L^2`) reproduced through the *same* machinery for
  `L = 1, 2, 3.7` (`det{}'\Delta = 1, 4, 13.69`; `|err| < 1e−10`).
- Torsion combinatorial weight `Σ_q (−1)^q q\binom{d}{q} = −1` (`d=1`), `0`
  (`d ≥ 2`).

### Candidate A — Ray–Singer analytic torsion `τ_RS(T^d) = exp(½ Σ_q (−1)^q q ζ'_{Δq}(0))`

On the flat, parallelizable torus the Hodge Laplacian on `q`-forms is
`Δq = \binom{d}{q}` decoupled scalar copies, so
`ζ'_{Δq}(0) = \binom{d}{q}·ζ'_{Δ₀}(0)` and

$$
  \log\tau_{RS}(T^d) \;=\; \tfrac12\,ζ'_{Δ₀}(0)\cdot\sum_{q=0}^{d}(-1)^q q\binom{d}{q}.
$$

The alternating weight **vanishes for every `d ≥ 2`**
(`\sum_q (-1)^q q\binom{d}{q} = -d\sum_{j}(-1)^j\binom{d-1}{j} = -d\,(1-1)^{d-1} = 0`),
so at `d = b₁ = 8`:

- `ζ'_{Δ₀}(0)` on the unit `T^8` `= 2.5787\ldots` and **contains
  `\log(4π^2) = 3.6758\ldots`** — the π *is* present in a single determinant …
- … but `\log\tau_{RS} = ½·ζ'_{Δ₀}(0)·0 = 0`, so **`τ_RS(T^8) = 1`** exactly.
  The analytic torsion of the flat torus is **trivial**, and the π **cancels** in
  the alternating sum.
- The residual metric-on-cohomology normalization (Cheeger–Müller: `τ_RS`
  equals Reidemeister torsion with the integral cohomology basis) is the
  **covolume `√det G`** — shape-dependent, the `1/Area`-category object **data-
  excluded at −1419 ppb** (#3842 / the abelian-torsion probe).

### Candidate B — graded / per-mode determinant ratio

- **(B1)** the alternating determinant ratio
  `∏_q (det{}'\Delta_q)^{(-1)^q q/2} = 1/τ_RS = 1` (by A) — no reciprocal-`b₁`.
- **(B2)** the per-mode derivative `d(\log Z_{Maxwell})/db₁`. From #3870,
  `\log Z = \log Vol(J) + ½ζ_{Δ₁}(0)\log(2π) + \cdots`, and
  `½ζ_{Δ₁}(0) = −b₁/2` is **linear** in `b₁`, so
  `d(\log Z)/db₁ = −½\log(2π) + \text{const} = −0.9189\ldots` — a
  **`b₁`-independent constant**, never `1/b₁`.

### Per-candidate three-axis table

| candidate | (i) covolume-free | (ii) π-power `−1` | (iii) reciprocal `1/b₁` | verdict |
|---|---|---|---|---|
| **A** Ray–Singer torsion `τ_RS(T^8)` | ✗ covolume `√det G` survives (metric part) | ✗ π-power **0** (`τ=1`; π cancels) | ✗ `τ=1` (no `b₁`); covolume `∝ dim`, not `1/b₁` | **NEGATIVE** |
| **B1** alt. det ratio `∏(det'Δq)^{(-1)^q q/2}` | ✗ (`= τ_RS` residue) | ✗ π-power **0** (`= 1`) | ✗ `= 1`, no `b₁` | **NEGATIVE** |
| **B2** per-mode `d(logZ)/db₁` | — (a slope, not a measure) | ✗ carries `\log(2π)`, not `π^{−1}` | ✗ `b₁`-**independent** constant | **NEGATIVE** |
| target `1/(π·b₁)` | area-free | `π^{−1}` (bare) | `b₁^{−1}` | — |

## Verdict — scope-(a) NEGATIVE (the anticipated, and good, outcome)

No flat-torus determinant / torsion object is simultaneously area-free,
`π^{−1}`, and reciprocal-in-`b₁`. Analytic torsion is **trivial** on the flat
torus (`τ_RS = 1`; π cancels in the alternating sum), leaving only the covolume
(the data-excluded `1/Area` category); the graded and per-mode ratios are either
`1` or a `b₁`-independent constant. The `1/(8π)` identification is **not** a
flat-torus spectral invariant. Anti-laundering respected: no CODATA read, no
convention stretched toward `8π`, controls checked against closed forms.

## The sharpened redirect (Candidate C) — where the measure MUST live

The structural reason every flat-torus route fails axis (iii) is uniform:
**every flat-torus spectral invariant is either EXTENSIVE in `b₁` or a
COVOLUME**, never reciprocal —

| object | `b₁`-scaling | class |
|---|---|---|
| `ζ_{Δ₁}(0) = −b₁` | linear (numerator count, #3834) | area-free count ✓ |
| `ζ'_{Δ₁}(0) ∝ b₁` | linear | extensive |
| `\log Z_{Maxwell} ∝ b₁` | exponential measure (#3870) | extensive |
| `τ_RS = 1`, `√det G` | none / covolume | covolume (A, #3842) |

A **reciprocal `1/b₁`** is, by definition, a `1/(\text{total count})`
**democratic-average** normalization — one photon shared over the `b₁`
harmonic-1-form directions. No determinant or torsion on the Jacobian produces
that intrinsically; obtaining it by *dividing* a determinant by the count `b₁`
is precisely the forbidden fitting move.

**Therefore the measure lives OFF the flat-torus determinant, on the RT/WRT
modular-`S`-matrix normalization.** The `1/(\text{total count})` with a single
bare `π` is the hallmark of the **total quantum dimension `D = Σ_i d_i²`**
(`S_{00} = 1/D`) / the Verlinde per-handle measure — a nonabelian object. This is
the same target the abelian-torsion probe (#3842) already narrowed to ("the
`b₁`-democratic per-mode weight ⇒ nonabelian RT S-matrix route, Front 2 / `W_λ`
keystone"); the present probe closes the *analytic-torsion* and *graded-
determinant* branches explicitly, confirming the redirect is forced rather than
merely available. The next honest step is the nonabelian `S`-matrix / `W_λ`
keystone computation, **not** a further flat-torus determinant variant.

## Kill criteria (pre-stated, and how they resolved)

- **Negative** if each candidate's π-power ≠ 1, or its `b₁`-dependence is not the
  reciprocal, or it carries covolume — report scope-(a) negative, do **not**
  stretch normalization conventions to manufacture `8π`. → **All three
  candidates hit this**; reported negative; no convention stretched.
- **Positive-partial** only if `π^{−1}` and reciprocal-`b₁` emerge from a
  candidate's determinant normalization independently of CODATA. → **Did not
  occur.**

## Cross-references

- #3870 flat-torus Maxwell (the immediate predecessor / constraint): [`2026-07-18-alpha-em-flat-torus-maxwell-perloop.md`](2026-07-18-alpha-em-flat-torus-maxwell-perloop.md)
- #3842 abelian RT/RS torsion = covolume: [`alpha_em_rt_abelian_torsion_count_vs_covolume_probe.py`](../../computations/alpha_em/alpha_em_rt_abelian_torsion_count_vs_covolume_probe.py)
- #3834 ζ-anomaly `ζ_{Δ₁}(0) = −b₁` (area-free numerator count): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Derivability map / the wall: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
