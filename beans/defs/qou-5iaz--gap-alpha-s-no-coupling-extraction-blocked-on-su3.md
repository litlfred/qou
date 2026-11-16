---
# qou-5iaz
title: 'GAP: alpha_s — no coupling extraction; blocked on SU(3) action (see qou-ni4b)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - sm-26
    - 8f-colour
created_at: 2026-07-31T20:15:08Z
updated_at: 2026-11-16T17:48:00Z
parent: qou-8lxd
blocked_by:
    - qou-ni4b
    - qou-lxh5
---

## Goal (owner, 2026-08-02): DERIVE alpha_S like we derived alpha_EM

α_EM is derived (to 3 sig figs, no free parameters) as a **Plancherel /
spectral ratio** of the force-carrier knot pair:
$1/\alpha_{EM} = q\,[9]_q[10]_q \approx 136.82$ at $q_0$
([`alpha-em-derivation-open-problems`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md)).
The analogous target: derive the **strong** coupling $\alpha_s$ (or
$\Lambda_{QCD}$) as a spectral/Markov-trace object of the **color** knot
$T(2,9)$ (the gluon = 3-fold cover of $T(2,3)$).

## Blocker (real)

α_s lives in the **color** sector, which needs the **SU(3) colour
action** — currently a GAP (bean `qou-ni4b`: "SU(3) colour action on
3-strand structure"). Unlike α_EM (abelian $U(1)$, a single Plancherel
ratio), α_s is the coupling of the *non-abelian* color algebra; the
running (asymptotic freedom) is a property of that action. So α_s is
genuinely **downstream of `qou-ni4b`**.

## Attack options / status

1. **Static coupling as a trace ratio** — by analogy with α_EM, try
   $\alpha_s(q_0) \sim$ (Markov trace of $T(2,9)$) / (normalisation) at
   the substrate scale. Status: **not attempted**; needs the color
   normalisation, which is `qou-ni4b`. [medium, blocked]
2. **$\Lambda_{QCD}$ from confinement scale** — the confinement SDP
   (step 10) sets a mass scale; $\Lambda_{QCD}\approx f_\pi$-adjacent.
   $\mathfrak{D}_\pi$ (CAL-3) is the meson/confinement scale — see the
   "$\mathfrak{D}_\beta/\mathfrak{D}_\pi$ ↔ SM" analysis: $f_\pi$ = T(2,3)
   Frobenius pairing normalisation; $\Lambda_{QCD}$ is indirect off it.
   [long, needs SU(3)]
3. **Asymptotic freedom = q-CLT flow** — the running $\alpha_s(\mu)$
   (decreasing at high $\mu$) should be the RG image of the q→1
   KLR→KL decategorification flow. Cross-ref the lattice-QCD-emergence
   bean (`qou-jsx5`): the continuum/UV limit is the same q-CLT limit.
   [research, long]

## Honesty gate (STRICT)
Do NOT wire any $\alpha_s$ number to production until the SU(3) colour
action (`qou-ni4b`) is derived — per AGENTS.md "Axiomatization is NOT a
Proof". A trace ratio that hits 0.118 by tuning is a **fit**, not a
derivation.

## Related
- Blocked-by: `qou-ni4b` (SU(3) colour action)
- Sibling sector: `qou-jsx5` (lattice-QCD / q-CLT UV limit)
- Session: `qou-ywj9`
- Precedent: α_EM spectral-ratio derivation (see link above)

## 🔥 Roast (2026-08-02) — "α_s = trace ratio" is a CATEGORY ERROR; reframe to Λ_QCD

α_EM worked as a single number $q[9]_q[10]_q$ because EM is **abelian** — one
$U(1)$ coupling, one Plancherel ratio, essentially non-running at this
precision. **α_s is not one number.** It runs strongly: $\alpha_s(M_Z)\approx
0.118$, $\alpha_s(1\,\text{GeV})\approx0.5$. A single categorical trace ratio
at $q_0$ yields ONE value — so "α_s = trace ratio of T(2,9)" is a
category error unless you name the scale.

**Reframe the target to $\Lambda_{QCD}$** — the RG-invariant, scale-free mass
scale. Being scale-invariant, $\Lambda_{QCD}$ *can* legitimately be a single
categorical number (a mass, i.e. a Markov-trace/confinement-scale object),
and then $\alpha_s(\mu)$ follows from $\Lambda_{QCD}$ + the RG flow:
$$\alpha_s(\mu)\sim \frac{1}{b_0\ln(\mu/\Lambda_{QCD})}.$$
The running itself is the $q\to1$ q-CLT flow (lattice bean `qou-jsx5`).

So the honest attack ladder becomes:
1. Derive $\Lambda_{QCD}$ as a confinement-scale object off $\mathfrak{D}_\pi$
   (CAL-3) / the operator-selection SDP. [blocked on SU(3) `qou-ni4b`]
2. Get $\alpha_s(\mu)$ from $\Lambda_{QCD}$ + the q-CLT RG flow. [needs `qou-jsx5`]

Do NOT chase a bare $\alpha_s(q_0)=0.118$ trace ratio — tuning $[a]_q[b]_q$ to
hit 0.118 is a **fit**, not a derivation (anti-laundering rule). Λ_QCD is the
only single-number target that isn't a category error.

## 🔥 Roast addendum (2026-09-03, qou-bsu0) — currency + tower

(i) Unchanged: Λ_QCD as a confinement-scale Markov-trace object, then α_s(μ) via the q→1 q-CLT flow (`qou-jsx5`); needs the SU(3) action on the framework's own three-strand space (`qou-ni4b`; the abstract module on O = C⊕C³ is done).
(ii) New since 2026-08-25: the λ_a↔e_a generator identification is an eighth scope-b exclusion (`OctonionicSu3RankObstruction.lean`); no object-level gate separates colour from flavour (`FlavourColourDiscriminator.no_object_gate_separates`); colour antisymmetry is located in μ̄₁₂₃ but the state's channel is not established (`qou-dg07`); the level-3 test (`qou-lxh5`, z₃ = q⁵/(q⁴+q²+1) forced by the fibre) is wired to nothing.
(iii) Trap: "no candidate formula" is stale — `1/α_s = q^p[9]_q` (p free, conditional; `alpha_k_selection_rule_conditional.py`) and the fit-shaped `q⁻¹/[7]_q = 0.1182` (`docs/beta-decay-handoff.md:181`) both exist; neither may be wired.
(iv) Next: run `qou-lxh5` — does the ℓ(λ) = 3 sector at level 3 yield any colour quantity at the three existing calibrations? PASS/FAIL is decisive.
(v) Forecast: Λ_QCD before α_s(μ); neither before `qou-ni4b`.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY so far (single bracket ratios at q₀); the level-3 Markov trace over all three-row blocks IS the full-tower formulation, and it exists as a test.

## Progress update 2026-11-16 (PR #8139, `0435e799b9eb320f989c979717153b33245cefc1`)

Recorded the 3-strand Wedderburn tower weights $y_{(3)}(q_0), y_{(2,1)}(q_0), y_{(1^3)}(q_0)$ ($y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$ to 70 dps) and the `qou-ni4b` dimension / derived-Lie-algebra / cubic-anomaly boundary in `folio/quantum-observable-universe/lean/QOU/StandardModel/ThreeStrandColourTowerCP.lean` and `computations/probes/three_strand_colour_tower_cp_probe.py` (PR #8139). Per the honesty gate, no $\alpha_s$ constant is wired; kept `in-progress`.
