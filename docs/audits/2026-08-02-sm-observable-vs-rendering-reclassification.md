# The 26 Standard-Model parameters as a *rendering* of QOU — observable vs. derived

**Date:** 2026-08-02
**Scope:** conceptual reclassification (owner-requested). Not a derivation of any parameter.
**Serves:** owner bean `qou-jsx5` (lattice-QCD-from-QOU), PR #4600 — and reframes every open-mass chip.
**Evidence base (this session):** #4589 (carrier≠mass-knot), #4584 (complex-mass scaffold), #4591 (m_τ negative), #4594 (charm block-projection negative), #4596 (θ_QCD), #4597 (hypercharge 2nd invariant).

## Thesis

The 26 Standard-Model parameters are **not** 26 fundamental QOU quantities to be matched one-to-one to knots. They are a **downstream rendering** of the categorical model under one archimedean evaluation. The pipeline is

> categorical action / Lagrangian → **q-CLT** (archimedean functor / Markov trace at $q_0$) → archimedean evaluation → **observables** → *rendered* SM Lagrangian parameters.

Some of the 26 are **fundamental observables** the framework should predict directly; others are **derived renderings** — scheme- or basis-dependent quantities the SM *elevates to inputs* but which QOU produces as downstream extractions from observables. Treating the derived ones as fundamental is where "the SM may be slightly wrong": not empirically wrong, but **over-parameterized**.

## Why the split is forced, not stylistic

Three results this session make the distinction unavoidable:

1. **All SM torus-knot *carriers* are Vol=0** (#4589, `sm_carrier_vs_mass_knot_map.py`). Every dictionary carrier — $\nu$ (unknot), $e,\mu,\tau=T(2,3/5/7)$, charm-vertex $T(3,5)$, $W,Z,H=T(2,4/6/8)$, gluon $T(2,9)$ — is a torus knot/link with zero hyperbolic volume. A carrier fixes the **channel / quantum numbers**, never a mass. Masses live in *distinct hyperbolic* objects (muon $\to 4_1$; proton $\to$ Borromean).

2. **A confined quark "mass" is not a direct observable.** In QCD it is a renormalization-scheme + scale dependent Lagrangian parameter, *extracted* from color-singlet bound states (charmonium, $D$, $\Lambda_c$) via lattice / sum rules. The charm-mass attacks all failed for the *same structural reason* — there is no observable $m_c$ for a volume to equal: the continuant tower undershoots ~100× (#4584), the carrier $T(3,5)$ is a zero-volume torus knot (scope-(b), #4584), the raw composite volume misses (#4584), and the Frobenius block ratio is $O(1)$ vs the $O(100)$ hierarchy (#4594). These are not four coincidences; they are the model correctly reporting that $m_c$ is **not a fundamental observable**.

3. **The canonical calibration triple is already three decay *widths*** (m_e, $\mathfrak{D}_\beta$, $\mathfrak{D}_\pi$; masses are the numerical proxies). The framework's own inputs are weak-sector *observables*, not quark Yukawas — it already "knows" the fundamental objects are observable masses and widths.

## The reclassified 26

| SM parameter(s) | QOU status | Where it lives |
|---|---|---|
| $m_e$ | **fundamental** (input / unit) | leptonic mass scale |
| $m_\mu, m_\tau$ | **fundamental** observables (charged-lepton masses; hyperbolic mass-knots, not carriers) | $4_1$ for $\mu$; $\tau$ mass-knot open (#4591) |
| $m_u,m_d,m_s,m_c,m_b,m_t$ (6) | **DERIVED renderings** — not direct observables; extracted from color-singlet hadron masses | the *observables* are $J/\psi, \eta_c, D, \Lambda_c, \ldots$ (hyperbolic bound-state braids) |
| CKM $\theta_{12,23,13},\delta$ (4) | **DERIVED renderings** — basis-dependent; presuppose a flavour basis | downstream of the (open) generation structure |
| PMNS $\theta_{12,23,13},\delta_{CP}$ (4) | **DERIVED renderings** (+ $m_{\nu_i}$: volume mechanism scope-(b) excluded, #4589) | neutrino sector |
| $\alpha_{\rm EM}$ | **fundamental** observable (partial: conditional fixed point) | EM coupling |
| $\sin^2\theta_W$ | **fundamental**-ish (conjectural); needs the 2nd $U(1)$ | Milnor $\bar\mu_{123}$ separates the two $U(1)$s (#4597) |
| $\alpha_s$ | **fundamental** observable (open; blocked on SU(3)) | strong coupling |
| $m_H$ | **fundamental** observable (conjectural $T(2,8)$; RT chain) | Higgs mass |
| $v$ (EW scale) | **fundamental** observable (open) | Fermi constant |
| $\theta_{\rm QCD}$ | **fundamental** observable (open; framing route gives $\{0,\pi\}$, #4596) | strong-CP |

**Accounting shift:** the "21 open" collapses. The **6 quark masses + 8 mixing angles (14 of the 21)** are *not* 14 independent open knots — they are **derived quantities of the observable spectrum** (hadron masses, and the generation/flavour structure). The genuinely-fundamental open observables are a much shorter list: the observable hadron/lepton masses, the three gauge couplings, $m_H$, $v$, $\theta_{\rm QCD}$, and the generation structure that underlies the mixings.

## The honest program (replaces "match each parameter to a knot")

1. **Predict the observables** — color-singlet masses (leptons; hadrons via hyperbolic bound-state braids) and decay widths — from the categorical action via q-CLT + archimedean evaluation. This is the load-bearing physics.
2. **Render the SM Lagrangian parameters** as downstream extractions from those observables (the quark masses via the QOU analog of lattice extraction — `qou-jsx5`; the mixings from the flavour/generation structure).

The **jet-order / GB-reduction bookkeeping** (`conj:binding-manybody-eq-jet-filtration`, Gröbner–Shirshov reduction order) tracks *where* in the binding expansion each extracted parameter is defined — a derived $m_c$ carries a jet-order label, exactly as an $\overline{\rm MS}$ mass carries a scale $\mu$.

## Honest scope (STRICT)

This is a **reframing / accounting correction, not a derivation.** It closes no parameter and predicts no number. Its value is (a) it explains *why* the direct charm-mass attacks were bound to fail (category error — targeting a non-observable), (b) it points every future mass chip at the **observable** bound-state spectrum instead of the confined-quark parameter (the J/ψ attack, `claude/jpsi-boundstate-mass-2026-08-02`, is the first instance), and (c) it re-scopes the "21 open" honestly — most are derived, not independently fundamental. The claim "the SM is over-parameterized relative to QOU" is a *structural* reading, not an empirical dispute with the SM's predictions.

## Cross-refs
- Carrier≠mass-knot + neutrino exclusion: #4589.
- Complex-mass scaffold + charm-mass negatives: #4584.
- Owner QOU→SM derivation queue (`qou-jsx5` lattice-from-QOU, `qou-ud3o` Wick): #4600.
- Decay-width calibration canon: `docs/audits/2026-06-28-calibration-canon-decay-width-ruling.md`.
