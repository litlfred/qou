---
# qou-tekm
title: 'SIDE QUESTION (owner): what does QOU say about a Boyle resonance at q_0?'
status: in-progress
type: task
priority: normal
tags:
    - 8f-decide
    - reorg-2026-10-04
created_at: 2026-09-01T20:07:53Z
updated_at: 2026-11-16T17:50:00Z
parent: qou-8lxd
---

## Verified 50+ dps Assessment (PR `litlfred/qou#8140`, `468e210bfac6c8438bd4b6331f2fa807f91853e8`)

- **Probe & Witness:** `computations/probes/boyle_virial_eos_assessment_probe.py` and `computations/probes/boyle-virial-eos-assessment.witness.json` (4 assertions, `allPassed: true`, proton pin).
- **Verified findings:**
  1. **Corpus & EOS scan across all 7 statistical-mechanics / EOS blocks** (`eos-borromean-cfl.md`, `color-superconductivity-borromean.md`, `cfl-neutron-star-observables.md`, `phase-transitions-intro.md`, `phase-transition-interpretation.md`, `stat-mech-computational-horizon.md`, `hydrogen-partition-function.md`): `"Boyle"` occurs 0 times and QOU defines **no** density virial expansion $P / (\rho k_B T) = 1 + B_2(q)\rho + B_3(q)\rho^2 + \dots$. Specifically, `eos-borromean-cfl.md` defines a cold degenerate Fermi-gas polytrope $P_B(n_B) \propto n_B^{5/3}/M_B(q_0)$ and $P_D(n_B) \propto (3n_B)^{5/3}/M_D(q_0) + 3\Delta_{\text{CFL}}^2\mu_q^2/\pi^2$ with kinetic stiffness ratio $(M_B/M_D)\cdot 3^{5/3} \approx 6948.8935$ at $q_0$ ($M_B(q_0) \approx 746.4180$, $M_D(q_0) \approx 0.670299$) and zero $n_B^2$ virial term; `stat-mech-computational-horizon.md` and `hydrogen-partition-function.md` define $P_q V_q = N T_q (1 + (\hbar_q^2/[2]_q)\langle\mathfrak{S}_q\rangle)$, where the $q$-correction is a density-independent single-knot boundary factor ($\hbar_q^2/[2]_q \approx 0.004882$ at $q_0$).
  2. **Natural 2-body Mayer / cluster trace excess $B_2^{\text{trace}}(q)$:** At $q = 1$, $\operatorname{tr}_M(\mathcal{A}_1)|_{q=1} = 1/2$ and $\operatorname{tr}_M(\mathcal{A}_2)|_{q=1} = 1/8 = c_0(2)$, giving raw 2-body cluster excess $B_2^{\text{raw}}(1) = \operatorname{tr}_M(\mathcal{A}_2) - \operatorname{tr}_M(\mathcal{A}_1)^2 = -1/8 = -c_0(2)$, unknot shift $c_0(2) - 1 = -7/8$, and reduced Mayer factor $B_2^{\text{red}}(1) = f(1) - 1 = -1/2$. Across the entire physical interval $q \in [1, 23/20]$ (including $q_0$), $B_2^{\text{red}}(q) = f(q) - 1 < -0.345$ and $B_2^{\text{raw}}(q_0) = \tau_{N_1}(q_0)\tau_{N_2}(q_0)(f_{N_1 N_2}(q_0) - 1) \in \{-0.1534, -0.1470, -0.1346\}$ for $(pp, pn, nn)$ — strictly negative and bounded away from $0$ everywhere (no Boyle point $B_2 = 0$ exists near $q_0$).

Raised by the owner mid-session 2026-09-01, verbatim: *"bean up side question what
does QOU boyle resonance at q_0"*. Recorded rather than answered — the term is not
in the corpus and the reading needs the author's confirmation before anyone spends
a tranche on it.

## MEASURED: "Boyle" appears NOWHERE in the corpus

`rg '[Bb]oyle'` over `folio/quantum-observable-universe/**/*.md` returns **no
files**. So this is not a term the framework uses, and there is no existing block,
audit or probe to pick up. Whoever takes this bean starts from the question, not
from prior work.

## The likely reading, flagged as MINE not the author's

**Boyle temperature / Boyle point**: the temperature at which a real gas's second
virial coefficient `B(T) = 0`, so it behaves ideally to first order in density. A
"Boyle resonance at `q_0`" would then ask: does the substrate modulus
`q_0 ~ 1.1099785827513808` sit at, or near, such a point in some QOU-derived
equation of state — i.e. is there a density-expansion coefficient that vanishes
there?

**This reading is not confirmed.** "Resonance" is not the usual word for the Boyle
point, so the author may mean something else entirely. Do not build on the reading
without asking.

## The adjacent surface that DOES exist

There is no virial expansion in the corpus that I found, but there is an
equation-of-state and phase-transition surface the question would have to connect
to:

  * `observations/eos-borromean-cfl.md` — the Borromean vs CFL equation of state
    (records the CFL EOS as ~7000x stiffer at equal baryon density). This is the
    only file with an explicit "equation of state", and it carries **no virial
    coefficients**.
  * `observations/color-superconductivity-borromean.md`,
    `observations/cfl-neutron-star-observables.md`, `observations/strangelet-intro.md`
  * `information-theory/phase-transitions-intro.md`,
    `information-theory/phase-transition-interpretation.md`,
    `information-theory/stat-mech-computational-horizon.md`
  * `information-theory/hydrogen-partition-function.md` — the closest thing to a
    statistical-mechanical generating function

## What answering it would require

1. Confirm the reading with the author (Boyle point? something else?).
2. Establish whether QOU derives a density/virial expansion at all. From the grep,
   it appears **not** — the EOS work is a stiffness comparison, not an expansion.
   If there is no second virial coefficient in the framework, the question as
   posed may have no object to attach to, and saying so is the answer.
3. Only if (2) yields an expansion: check whether any coefficient vanishes at or
   near `q_0`, and — per the anti-fit discipline — whether that vanishing is
   *forced* or merely *in range*. A coefficient that happens to cross zero
   somewhere near `q_0` is the "defined residual != derived decomposition" trap;
   compute the window width before claiming a coincidence.

## Status

Not started. No claim made either way. Cheap to close if step 2 shows the
framework has no virial expansion — that is a legitimate and useful answer.
