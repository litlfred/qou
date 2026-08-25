# Complex-volume ($\mathrm{Vol} + i\,\mathrm{CS}$) extension of the $m_\tau$ knot search — a sharpened negative

> **Provenance.** Executes queued **extension #1** ("Volume + Chern–Simons
> pair") of
> [`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md).
> Probe:
> [`computations/m_tau_complex_volume_search.py`](../../computations/m_tau_complex_volume_search.py);
> witness:
> [`computations/m-tau-complex-volume-search.witness.json`](../../computations/m-tau-complex-volume-search.witness.json).
> Branch `claude/tau-mass-complex-volume-2026-08-02`, PR #4591.

## The question

The muon identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^{2}$ uses the
**real** hyperbolic volume. The prior $m_\tau$ search evaluated 25 hyperbolic
knots for $m_\tau/m_e \approx \mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$ and was
refuted (best $\mathrm{Vol}(8_1)/\hbar_q^3 = +1.33\%$). Hyperbolic knot
complements carry a *complex* invariant $\mathrm{Vol}(K) + i\,\mathrm{CS}(K)$
(SnapPy `M.volume()`, `M.chern_simons()`). Does opening the search to the
**complex** volume, the **full $\le 12$-crossing census**, and **composite**
carriers recover $m_\tau/m_e \approx 3477.23$?

**Answer: no — and now for structural reasons, not just a wider miss.**

## Method (derive-then-check, anti-fit)

$q_0$ is the canonical muon-pinned substrate value
($\hbar_q = (q_0-1)/q_0$); the muon sanity check
$\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$ reproduces to $2\times10^{-7}$.
Two questions are kept separate so a wide census cannot masquerade as a
derivation.

**Fixed functionals** (chosen *before* scoring, never per-knot tuned):

- $F_{\mathrm{re}} = \mathrm{Re}(\mathrm{Vol} + i\,\mathrm{CS}) = \mathrm{Vol}$ — the muon-derived choice;
- $F_{\mathrm{abs}} = |\mathrm{Vol} + i\,\mathrm{CS}| = \sqrt{\mathrm{Vol}^2 + \mathrm{CS}^2}$.

**Fixed exponents** $k \in \{2,3,4,5\}$ ($k=3$ is the "generation-step in
$\hbar_q$" guess, one power above the muon's $k=2$). Scoring is by **hit
counts** (how many census knots land within a tolerance) plus a
search-entropy bound — **not** a "closest knot" cherry-pick.

## Part A — the *derived* carrier is non-hyperbolic

The framework's $\tau$ decay carrier is $T(3,5)$-adjacent — the $T(2,7)$
generation column, $n=7$. Computed as braid closures:

| Carrier | SnapPy volume | Solution type | Hyperbolic? |
|---|---|---|---|
| $T(2,7)$ | $-4.3\times10^{-14}$ | degenerate tetrahedra | no |
| $T(3,5)$ | $0$ | flat tetrahedra | no |
| $T(3,4)=8_{19}$ | $0$ | flat tetrahedra | no |

Torus-knot complements are Seifert-fibered, hence have **Gromov norm $0$**
and identically zero hyperbolic volume. The complex volume is
$(0,\ \text{non-geometric})$: SnapPy cannot even return a geometric
Chern–Simons for a degenerate solution.

> **Structural exclusion (scope-(b)), cited invariant.** For the *genuinely
> derived* carrier the hyperbolic-volume reading — **real or complex** —
> does not apply, because the torus carrier has zero simplicial volume
> (Gromov). This excludes the $\mathrm{Vol} + i\,\mathrm{CS}$ **invariant
> class** for the $T(p,q)$ carrier; it does **not** exclude a $\tau$ carrier
> altogether, nor a *different* invariant of the torus complement (e.g. a
> Seifert/Reidemeister-torsion or framing invariant).

## Part B — the wide census cannot identify $m_\tau$ even in principle

$2970$ hyperbolic knots ($\le 12$ crossings, all with computed $\mathrm{CS}$).
Hit counts within each tolerance, per fixed $(F,k)$:

| $(F,k)$ | $<1\%$ | $<0.1\%$ | $<100$ ppm | closest knot (rel. err.) |
|---|---|---|---|---|
| $F_{\mathrm{re}},\,k{=}3$ | 0 | 0 | 0 | $K8a11{=}8_1$ ($1.33\%$) |
| $F_{\mathrm{abs}},\,k{=}3$ | 0 | 0 | 0 | $K7a4$ ($1.48\%$) |
| $F_{\mathrm{re}},\,k{=}2$ | 0 | 0 | 0 | $K12a868$ ($31\%$) |
| all other $(F,k)$ | 0 | 0 | 0 | — |

Composite carriers $K_1\#K_2$ (additive volume, $496$ pairs at $k{=}3$):
**0 hits at $1\%$**, closest $4_1\#4_1$ at $20\%$.

Two independent facts:

1. **Empirical floor unchanged.** Going from $25$ knots to $2970$ knots, and
   from real volume to complex volume, the best miss is *still* $1.33\%$ —
   the same $8_1$, $k{=}3$ candidate. Adding the Chern–Simons part
   ($F_{\mathrm{abs}}$) makes the floor **worse** ($1.48\%$), not better.

2. **The muon anchor is Chern–Simons-blind.** $\mathrm{CS}(4_1)\approx
   -5.6\times10^{-17}$ (the figure-eight is amphichiral). The one anchor that
   fixes the functional therefore carries **no information** about how
   $\mathrm{CS}$ should enter $F$. Any $F(\mathrm{Vol},\mathrm{CS})$ reducing
   to $\mathrm{Vol}$ at $\mathrm{CS}=0$ is equally "muon-consistent" — a whole
   function's worth of undetermined freedom. This is the anti-fit trap made
   explicit: the complex axis *adds* free parameters rather than deriving them.

### Search-entropy vs precision (scope-(b), information bound)

With $N = 2970 \times 2\ (\text{functionals}) \times 4\ (\text{exponents}) =
23760$ free choices, the search carries $\log_2 N \approx 14.5$ bits of
entropy. A match at fractional tolerance $w$ pins the $4$-sig-fig target to
$\log_2(1/2w)$ bits. Identification is credible only when match-bits $>$
search-bits:

| tolerance $w$ | match bits | $>14.5$? |
|---|---|---|
| $10^{-2}$ | $5.6$ | no |
| $10^{-3}$ | $9.0$ | no |
| $10^{-4}$ | $12.3$ | no |
| $5\times10^{-5}$ (exp. precision) | $13.3$ | **no** |

> **Even at the experimental precision of $m_\tau/m_e$, a census match would
> carry less specificity than the search's own entropy.** No
> $\mathrm{Vol}+i\,\mathrm{CS}$ census identification of $m_\tau$ is possible
> *in principle*, independent of the observed $0$ hits — the same
> information-theoretic prune that killed the 12-constant PSLQ basis
> (PR #1805). Widening the census (more crossings, satellites, more
> functionals) only **raises** the search entropy and makes any hit *less*
> meaningful.

## Conclusion — sharpened negative

The complex-volume axis does **not** yield a *derived* identification of
$m_\tau$:

- **(b)** the derived $T(p,q)$ carrier has zero hyperbolic volume, so the
  $\mathrm{Vol}+i\,\mathrm{CS}$ reading does not apply to it (Gromov);
- **(a)** for a hyperbolic-knot carrier the census floor is unchanged at
  $1.33\%$ ($F_{\mathrm{abs}}$ worse at $1.48\%$), and
- **(b)** the muon anchor is $\mathrm{CS}$-blind, so $F$'s
  $\mathrm{CS}$-dependence is a free function, and the search entropy
  ($14.5$ bits) exceeds the specificity of any reachable match — the census
  cannot pin $m_\tau$ even at experimental precision.

This **narrows** the surviving routes rather than closing $m_\tau$: any real
$m_\tau$ identification must either (i) use a *different invariant* of the
$n=7$ / $T(3,5)$-adjacent carrier (Seifert data, framing, torsion — not the
hyperbolic $\mathrm{Vol}+i\,\mathrm{CS}$), or (ii) *derive* the carrier and
functional from the substrate so the search entropy collapses to a single
parameter-free prediction. A wider hyperbolic-knot census is **not** a
productive direction — it worsens the entropy bound.

## What this does not claim

Not a $4$th calibration, not a fit, not an ansatz. The remaining audit
extensions (polylog tower $\mathrm{Li}_n$; multi-stratum KR sum; substrate
derivation of the carrier) are untouched by this negative — it rules out the
hyperbolic $\mathrm{Vol}+i\,\mathrm{CS}$ family, not cohomological
derivability of $m_\tau$ in general.

## See also

- [`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md) — the refuted real-volume 25-knot search (this audit executes its extension #1)
- [`rem:m-tau-knot-prediction`](../../content/quantum-observable-universe/observations/m-tau-knot-prediction.md) — the paper's forward-reference block
- PR #1805 — PSLQ search-entropy precedent

---

## Independent re-run (2026-08-09)

Re-verified from scratch on a clean SnapPy 3.3.2 install, at the rebased HEAD.
**The negative reproduces exactly.** Of the witness's 199 keys, all but two
volatile provenance fields (`commitSha`, `computedAt`) are bit-identical to
the committed run:

- Part A — the derived carriers `T(2,7)`, `T(3,5)`, `T(3,4)=8_19` return
  degenerate solutions (Seifert-fibered ⟹ Gromov norm 0). Scope-(b), invariant
  cited.
- Part B — 0 hits at `<1%` for every `(F, k)`; the closest remains `1.33%`.
  Composite search: 496 pairs, 0 hits.
- Entropy — search `N = 23760` = **14.54 bits**; a match at the experimental
  `5e-5` carries **13.29 bits**, so `identifiable = False` with an expected
  **2.38 chance hits**. The census cannot identify `m_τ` even in principle.

### Two defects found and fixed by the re-run

1. **The probe could not regenerate its own witness.** `json.dumps` raised
   `TypeError: Object of type mpf is not JSON serializable` *after* all compute
   completed, so the run died emitting nothing. Fixed with a `default=` hook
   (`_witness_default`) serializing `mpf`/`mpc` as full-precision decimal
   strings, matching the convention already used for `substrate_q0` and
   `hbar_q`.
2. **A float64 leak in the witness.** With the serializer fixed,
   `muon_sanity.vol_4_1` now records
   `2.0298832128193072500424051085490405718833786150606` (50 dps) where the
   committed witness held the float64-truncated `2.029883212819307`. This is
   the raw-float64 class tracked by bean `qou-gqt5`.

Neither defect touches a result: every scored number is unchanged.
