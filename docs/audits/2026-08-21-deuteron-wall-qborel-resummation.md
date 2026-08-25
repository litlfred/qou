# q-Borel–Laplace resummation of the deuteron wall Z_n(q₀) — negative on the right object + right transform (2026-08-21)

**Branch:** `claude/deuteron-qborel-2026-08-21`
**Probe:** [`computations/deltalambda/deuteron_wall_qborel_resummation_probe.py`](../../computations/deltalambda/deuteron_wall_qborel_resummation_probe.py) (exit 0)
**Witness:** `computations/deltalambda/deuteron-wall-qborel-resummation.witness.json`
**Tier:** numerical **scope-(a)** negative · **Discipline:** no fit, nothing wired, no tier change, EXPLORATORY / audit-only.
**Pin:** proton `q_at(30)` (owner default 2026-08-07). **Precision:** mpmath 60 dps, all arithmetic in `mpf` (no float64); exact transfer-operator `Z_n`.

## Why this probe exists — the transform was wrong

The prior verdict *"resummation closes the deuteron wall negatively"*
([`deuteron_wall_full_transseries_probe.py`](../../computations/deltalambda/deuteron_wall_full_transseries_probe.py),
audit [2026-07-13](2026-07-13-deuteron-wall-full-transseries-negative.md)) resummed the
**q = 1** telephone period `a_D^(n) = I(n)/n` with a **classical Γ-Borel** divisor
`Γ(n/2+1)` (Gevrey-1/2). But the substrate binding object is the **q-deformed**
statistic

```
Z_n(q) = S^bal(n;q)·q^{n(n-1)/2} = Σ_{w∈Inv} q^{2·maj + content}
```

built by the descent transfer operator `T_k = A_k + q^{2k}·B_k`
([`lever1_transfer_operator_spectral_qgevrey.py`](../../computations/lever1_transfer_operator_spectral_qgevrey.py)),
and at the substrate `q₀` it is **q-Gevrey, not classical Gevrey**. A classical Γ
divisor cannot tame q-Gevrey growth, so the negative closure had been argued on
the wrong object with the wrong transform. The correct test — a **q-Borel–Laplace
resummation of `Z_n(q₀)`** with a q-Gevrey-matched divisor — had never been run.
This probe runs it, **parameter-free**, at the substrate coupling.

## The object's growth (measured here)

At the proton `q₀ ≈ 1.10998`:

| quantity | value | reading |
|---|---|---|
| `log Z_30 / 30²` | **0.10964** | → `ln q₀ = 0.10434` from above |
| per-level `m_n / (n·ln q₀)` | → **2** | `m_n ≈ 2n·ln q₀` |

⇒ `log Z_n ~ (ln q₀)·n²`, i.e. **`Z_n(q₀) ~ q₀^{n²}`** — the `deg_q(cₙ) = n²`
growth budget that the C1/W2 q-Borel programme names
([2026-08-08-w2-stokes-qborel-attack-plan.md](2026-08-08-w2-stokes-qborel-attack-plan.md)).

## The q-convention (stated explicitly; corpus-justified — nothing invented)

**q-Borel kernel.** The corpus q-Borel is the RSZ / Ramis–Zhang level-`d` theta
kernel `tₙ` with growth `q^{n²/2d}` (w2 audit: `QBorelKernel`, level-1
`tₙ = q^{C(n,2)}`; `B_{q,d}(Σ fₙzⁿ) = Σ (fₙ/tₙ)ξⁿ`). Root tests on
`aₙ / tₙ` (probe check **C2**) show:

| divisor | `|aₙ/div|^{1/n}` at n = 10, 20, 30 | reading |
|---|---|---|
| level-1 `q₀^{C(n,2)}` (~`q₀^{n²/2}`) | 2.07 → 3.43 → **5.27** (rises, no plateau) | **under-tames** (radius → 0) |
| level-1/2 `q₀^{n²}` | 1.17 → 1.15 → **1.05** (bounded, settling) | **matched** (finite radius ≈ 0.955) |

So the level-1 theta kernel — and *a fortiori* the classical Γ — under-tames
`q₀^{n²}`; the matched level is **d = 1/2, `tₙ = q₀^{n²}`**. This is the q-lift
of the classical Gevrey-1/2 moment `Γ(n/2+1)` **at the same level 1/2** — the
honest q-analogue of the wrong-transform probe's own divisor.

**q-Laplace kernel.** A **positive theta measure** carries `tₙ` as an *exact*
q-moment: points `u_k = q₀^{2k}`, weights `p_k = q₀^{-k²}/Θ` (`k ∈ ℤ`,
`Θ = Σ q₀^{-k²}`). Completing the square,

```
Σ_k p_k · u_k^n = Σ_k q₀^{-k²+2kn}/Θ = q₀^{n²}·Σ_j q₀^{-j²}/Θ = q₀^{n²} = tₙ  (exact)
```

(probe check **C3**: reldiff 0 to n ≤ 7). Hence

```
f(x) = Σ_n aₙ xⁿ = Σ_k p_k · φ(x·q₀^{2k}),    φ(ξ) = Σ_n (aₙ/tₙ) ξⁿ
```

with `φ` the q-Borel transform (Padé-continued past its radius ≈ 0.955). This is
the discrete theta-kernel (Jackson / Zhang) q-Laplace and the **exact q-analogue**
of the classical `P(x) = ∫₀^∞ e^{−u} φ(x√u) du`: there the positive measure
`e^{−u}du` carries the `Γ(n/2+1)` moments; here the theta measure carries the
`q₀^{n²}` moments. Positive-kernel, parameter-free.

## Result (scope-(a) NEGATIVE, no fit)

Binding candidate `B = m_e·M₂·f(x)`, `M₂ = (2−1) = 1` bond; `B_D = 2.22452 MeV`,
`B_D/m_e = 4.3533`.

| substrate coupling `x` | `x` | `m_e·f` (MeV) | % of `B_D` | alien `|Im|` (MeV) |
|---|---|---|---|---|
| `ℏ_q²` | 0.00982 | 0.00507 | 0.228 % | 0.0005 |
| `ℏ_q` | 0.09908 | 0.05750 | 2.585 % | 0.0066 |
| `t = ln q₀` | 0.10434 | 0.06107 | **2.745 %** | 0.0071 |

**Best substrate value = 2.745 % of `B_D` — undershoots by ~36×.**

**Robustness.** Stable in truncation `N ∈ {24,28,30}`, Padé order `L ∈ {12…15}`,
theta cutoff `KM ∈ {30,40}` (`f(t)` moves only in the 4th digit), and in the
period convention (`Z_n/n` → 2.75 %, `Z_n` → 3.24 % — both undershoot). The
Stokes/alien jump at the substrate is ~0.007 MeV (negligible; not a contour
artifact).

**The match is a fit.** `f` reaches `B_D` only at `x ≈ 1.12` (probe diagnostic),
**beyond the Borel radius 0.955** (through the singularity) and far above every
substrate coupling (`x ≤ 0.104`). Adopting that coupling would be tuning to the
singularity — a fit, forbidden.

## Verdict and scope

**Scope-(a) — scope-limited negative:** *this* construction (level-1/2 q-Borel
kernel `q₀^{n²}` + positive theta-measure q-Laplace of `Z_n(q₀)`), **alone**, at
the substrate coupling, does not reproduce `B_D`; it undershoots ~36× and reaches
`B_D` only through the Borel singularity (a fit).

It is **not** scope-(b): no invariant is proved forbidding *every* resummation
route. A different binding period, a different positive measure, or a different
bond count could differ — the probe measures the *magnitude of the miss* of this
canonical construction, it does not exclude the resummation ingredient.

**What this adds.** It **corrects the transform** of the prior negative-closure
probe (classical Γ-Borel on the q=1 telephone period) and **confirms its
conclusion was robust**: the correct q-Borel–Laplace on the correct q-Gevrey
object `Z_n(q₀)` reaches the same verdict (both ~2.7–3.2 % of `B_D`, both reach
`B_D` only at the Borel singularity). The negative closure of the resummation
hypothesis for the deuteron now stands on the **right object + right transform**.
The deuteron wall is a **distinct-mechanism** problem — the working channel is the
separate q-rotational `μ₀·ℏ_q·J_q²` route (cheat-sheet "Bind" row, `B_D` to −9 %,
0 params) — not a resummation-coupling problem. **No fit; no wiring; no tier
change.**

## Corpus-grep compliance

Prior art checked:
[`deuteron_wall_full_transseries_probe.py`](../../computations/deltalambda/deuteron_wall_full_transseries_probe.py)
+ [audit](2026-07-13-deuteron-wall-full-transseries-negative.md) (the wrong-transform
predecessor this corrects); the q-Borel corpus
([2026-08-01-qborel-ecalle-resum-barodd.md](2026-08-01-qborel-ecalle-resum-barodd.md)
— theta-kernel over-suppression of a super-exponential ladder;
[2026-08-08-w2-stokes-qborel-attack-plan.md](2026-08-08-w2-stokes-qborel-attack-plan.md)
— the `QBorelKernel`/level-`d`/`deg_q=n²` framework);
[`lever1_transfer_operator_spectral_qgevrey.py`](../../computations/lever1_transfer_operator_spectral_qgevrey.py)
(the `Z_n(q)` object + its q-Gevrey characterization). This is the first
q-Borel–Laplace resummation-to-a-value of `Z_n(q₀)` for the deuteron; no route is
re-opened, no refuted item re-declared open, no `c_k`/binding constant wired.
