# CAL-1/2/3 reanalyzed in terms of 𝔇 (decay widths): no conflict — Re/Im of one 𝔙 (2026-06-30)

**Branch**: `claude/formula-for-q-bzym14` · **PR**: [#3183](https://github.com/litlfred/qou/pull/3183)
**Owner question**: "We have CAL-1/2/3; q is derived from there. Reanalyze in
terms of 𝔇 (decay widths). Is there a conflict between the ways of using
observational data, or are they the same thing? Can we use the literature
(AJ / Askey-Wilson / volume conjecture), generalizing beyond ℂ?"

## 1. The corpus CAL-123 (checked)

Per [`mass-theory/calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/calibration-inputs.md)
and the [canonical-derivation cheat-sheet](../canonical-derivation-cheat-sheet.md),
the **canonical** calibration is the **decay-width triple** — masses are the
*numerical proxies*:

| CAL | canonical observable (𝔇) | proxy | fixes |
|---|---|---|---|
| CAL-1 | $m_e$ (leptonic scale, $h^0$) | $m_e$ | the MeV unit (real scale) |
| CAL-2 | $\mathfrak{D}_\beta$ (neutron β-decay width, $h^2$) | $m_\mu/m_e$ | **$q_0$** |
| CAL-3 | $\mathfrak{D}_\pi$ (pion decay width, $h^3$) | $m_\pi$ | orthogonal meson scale |

So **$q_0$ is derived from CAL-2 = $\mathfrak{D}_\beta$**, confirmed. The meson
mass ratios computed this PR ($m_K/m_\pi$ 290 ppm, $m_\phi/m_\pi$ 2167 ppm) are
*downstream predictions* inside the CAL-3 sector using $q_0$ — not independent
calibrations, so no double-counting.

## 2. No conflict — the routes are the two faces of one complex volume

Reanalyzed through 𝔇, a striking pattern appears: **CAL-1 is a real/mass
scale; CAL-2 and CAL-3 are both decay widths.** And a decay width is exactly
the **imaginary / Chern–Simons / bar-odd** face of the complex volume
([`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md):
$\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta = \operatorname{Im}\mathfrak{V}$):

| | CAL-1 | CAL-2 | CAL-3 |
|---|---|---|---|
| canonical 𝔇 | $m_e$ | $\mathfrak{D}_\beta$ | $\mathfrak{D}_\pi$ |
| parity | bar-even (mass) | bar-odd (decay) | bar-odd (decay) |
| complex-volume face | $\mathrm{Re}$ (scale) | $\mathrm{Im}$ (CS) | $\mathrm{Im}$ (CS) |

This is *why* the meson sector (CAL-3) needs its own anchor and could not be
reached from the bar-symmetric ($C=\bar C$) lepton world: it carries an
intrinsic **bar-odd (Goldstone) component**
([`c-equals-bar-iff-all-1dim-proof.md`](../../content/quantum-observable-universe/particle-interactions/c-equals-bar-iff-all-1dim-proof.md)),
and a decay width is a bar-odd observable.

### The sharp statement (CAL-2)

The two CAL-2 handles — the **mass ratio** $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
and the **decay width** $\mathfrak{D}_\beta$ — are **not a conflict and not two
calibrations**: they are the **real and imaginary parts of the figure-eight's
complex volume**, the Neumann–Zagier $\mathbb{V}(4_1) = \mathrm{Vol}(4_1) +
i\,\mathrm{CS}(4_1)$:

$$\underbrace{\mathrm{Re}\,\mathbb{V}(4_1) = \mathrm{Vol}(4_1)}_{\to\ m_\mu/m_e\ \text{(mass proxy)}}, \qquad \underbrace{\mathrm{Im}\,\mathbb{V}(4_1) = \mathrm{CS}(4_1)}_{\to\ \mathfrak{D}_\beta\ \text{(decay width, conjectural)}}.$$

Since $4_1$ is the **Higgs** (this PR's muon-knot ruling), **CAL-2 is the Higgs
knot's complex volume**, read two ways. Mass-ratio vs decay-width is the
real-$q$ ($\mathrm{Li}_2^q$) saddle vs the root-of-unity ($\Phi_q$) saddle of
the **same** AJ operator $\hat A_{4_1}$. *That* is the unification the keystone
$\hat A_{4_1}$ computation (bean `2s1i`/`a6vp`) tests: one operator, both faces.

> **Scope.** $\mathrm{Re}\,\mathbb{V}(4_1)=\mathrm{Vol}(4_1)\to m_\mu/m_e$ is
> established (the Skein/Kashaev route). $\mathrm{Im}\,\mathbb{V}(4_1)=\mathrm{CS}(4_1)\to\mathfrak{D}_\beta$
> is **conjectural** — it is precisely the root-of-unity-saddle check in the
> keystone compute, not yet verified. The "no conflict" claim is established;
> the "$\mathfrak{D}_\beta = \mathrm{CS}(4_1)$" identification is the open test.

## 3. Can we use the literature? Yes — but generalize ℂ → $(R,\sigma)$

The literature anchors are real and usable:

- **AJ operator $\hat A_{4_1}$ is explicit and proved** ([nguyen-tran-2021]; the
  strong AJ conjecture for $4_1$). We can take the operator *directly*.
- **Volume conjecture for $4_1$ is proved** ([kashaev1997], [murakami-murakami2001]):
  the $\Phi_q$ root-of-unity saddle of $J_N(4_1)$ gives $\mathrm{Vol}(4_1)$.
- **Non-compact Askey-Wilson / modular double** ([koelink-stokman-2003],
  [faddeev1994]): the hyperbolic-knot ($\Phi_q$, $|q|=1$) face of the q-Askey
  scheme.
- **Torus-knot particle skeleton** has prior art ([avrin-2012]) including the
  hyperbolic-volume mass hierarchy.

**The required generalization (owner's "not just ℂ").** Every one of these is
stated over **ℂ** (analytic asymptotics, complex saddles). QOU is **pre-archimedean**:
its objects live over a generic commutative ring $R$ with bar-involution
$\sigma$ ($q \mapsto q^{-1}$), per AGENTS.md §7c. The bridge is already in the
corpus and is exactly the right one:

- $\hat A_K$ is q-holonomic **over $\mathbb{Z}[q^{\pm1}]$** — no ℝ/ℂ needed
  ([`phi-q-aj-machinery-identification.md`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md):
  "the AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$").
- The complex structure $\mathfrak{V} = \mathrm{Re} + i\,\mathrm{Im}$ is the
  **archimedean instance** ($\sigma = $ complex conjugation) of the generic
  bar-even/bar-odd split over $(R,\sigma)$
  ([`binding-qbeta-complex-volume.lean`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean):
  `invol_descent` over `CommRing` with involution).

So the recipe to **use** the literature without importing its ℂ-analysis:
take the literature's $\hat A_K$ / Askey-Wilson object over $\mathbb{Z}[q^{\pm1}]$;
replace "complex conjugation / $\mathrm{Re},\mathrm{Im}$" by the **bar-involution
$\sigma$ / bar-even, bar-odd**; replace "root-of-unity asymptotic limit" by the
**$\Phi_q$ saddle as an algebraic element of the Habiro ring**. The ℂ result is
recovered by specializing $\sigma \to \bar{\cdot}$ at $q_0$. This keeps the
whole chain on the pre-archimedean side of the τ-wall and makes the literature
theorems applicable as **generic-ring** statements, archimedean only at the
final evaluation.

## 4. Consequences / next steps (beans)

- **`2s1i` + `a6vp` (keystone):** compute $\hat A_{4_1}$; verify $\Phi_q$ saddle
  $\to \mathrm{Vol}(4_1)$ AND test $\mathrm{Im}\,\mathbb{V}(4_1) = \mathrm{CS}(4_1) \to \mathfrak{D}_\beta$ (§2 open test).
- **`m8bw`:** CAL-1 (bar-even/$m_e$) vs CAL-2,3 (bar-odd/$\mathfrak{D}$) is the
  algebraic origin of "exactly 3 calibrations" — one real scale + two decay
  widths = one $\mathrm{Re}$ + two $\mathrm{Im}$ anchors of the substrate $\mathbb{V}$.
- **`vpug`:** Lean the AJ/$(R,\sigma)$ generalization as a §3b-cond class over
  generic `CommRing` + involution, ℂ as the archimedean instance.

## Cross-references

- [`calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/calibration-inputs.md)
- [`binding-qbeta-complex-volume.md`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
- [`phi-q-aj-machinery-identification.md`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md)
- [`2026-06-30-muon-knot-id-phi-q-evidence.md`](2026-06-30-muon-knot-id-phi-q-evidence.md)
- New refs: [nguyen-tran-2021], [koelink-stokman-2003], [avrin-2012]
