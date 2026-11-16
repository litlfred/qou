---
# qou-hjs8
title: 'theta_res^2 vs PDG e+/e- mass split: is the 72x overshoot real or higher-order?'
status: in-progress
pr: 8192
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-09-07T12:24:19Z
updated_at: 2026-10-10T07:15:56Z
parent: qou-8lxd
---

CORRECTED 2026-09-07 before any durable use. Three fixes to the 72x claim: (1) normalisation — delta_CP is (a-b)/(a+b), PDG bounds (a-b)/avg = 2(a-b)/(a+b), so 144x not 72x; (2) the coefficient is NOT unknown — chi^(2,1) = -(h^2+1) has fractional theta^2 sensitivity [h0^2 + [2]_q^2]/|chi| = 3.9162481 exactly (verified at theta = 1e-3,1e-4,1e-5), giving 282x; (3) THE REAL WEAKNESS — delta_CP is defined on CROSSING ENERGY S_c, not mass. complex-chirality-rotation.md asserts it 'matches electron-positron mass equality' but does not derive it. Comparing a crossing-energy asymmetry to a PDG mass bound is a quantity conflation (da-arity-conflation). Scope (a). To settle: extend m(K) to complex q and compute (m+ - m-)/m_avg directly.


---

## ANSWERED 2026-09-13 (issue #7278) — the question is ill-posed: delta_CP does not depend on theta

The bean asks whether the theta_res^2 overshoot is real or higher-order, and
proposed to settle it by extending m(K) to complex q. Measured exactly in
sympy: **there is no theta^2 to be an overshoot of.**

**The mirror inverts the MODULUS, not a phase.** prop:antiparticle-crossing-
reversal item 2 fixes it with no room to guess:
E_cross(H^sigma) = -E_cross(H)|_{q <-> q^-1}. So for the trefoil
sigma_1^3, def:crossing-energy gives S_c(T) = 3q and the proposition gives
S_c(T^sigma) = -3/q. With q = r e^{i theta} the moduli are 3r and 3/r, so

    delta_CP = (r^2 - 1)/(r^2 + 1) = tanh(ln|q|),   d/d(theta) = 0 identically

At the proton pin: **0.103963710052410145676652858536**. theta cancels because a
ratio of MODULI cannot see a pure phase; what survives is the substrate's own
q <-> q^-1 asymmetry, present at theta = 0.

### Three sources, three incompatible orders for one symbol

| source | order in theta | value |
|---|---|---|
| conj:complex-chirality-rotation, as stated | O(theta^2) | -- |
| the same block's item 1, taken literally | identically 0 | 0, all orders |
| def:crossing-energy + prop:antiparticle-crossing-reversal | O(theta^0) | tanh(ln q0) |
| conj:cp-violation-spectral-form | O(theta^1) | sin(6 theta)/r^6 -> 6 theta/r^6 |

cp-violation-spectral-form cites complex-chirality-rotation as its dependency,
so the disagreement is between a block and the block it rests on.

**Row 2 needs no definition at all.** Item 1 says the particle carries
e^{+i n_c theta} and the mirror e^{-i n_c theta}. A pure phase has modulus 1,
so both moduli are equal and delta_CP = 0 exactly -- contradicting the same
block's own O(theta^2), whatever E_cross turns out to be.

**Item 1's exponent is also wrong for the definition it cites.** E_cross is a
SUM of degree-(+-1) terms, so an all-positive braid carries e^{i theta}, not
e^{i n_c theta} -- the exponent is the degree, +-1, never the crossing number.
A mixed-sign braid n_+ q - n_- q^-1 is inhomogeneous and carries no pure phase
at all. Checked at (n_+, n_-) = (3,0), (2,1), (1,2), (0,3).

### The mass question the bean actually asked

m(K) = m_e Vol(K) rho(K) / hbar_q^2. Under the mirror, Vol(K^sigma) = Vol(K)
(hyperbolic volume is mirror-invariant -- a theorem, not an assumption of this
framework) and hbar_q has no K-dependence, so only rho moves:

    (m+ - m-)/m_avg = (rho(q) - rho(1/q)) / (rho(q) + rho(1/q))

-- the same q <-> 1/q structure, again with NO theta in it. So the e+/e- mass
equality, if it holds, holds because **rho is bar-even**, NOT because delta_CP
is O(theta^2). The block cites the wrong mechanism.

### What is NOT closed (bean stays open per AGENTS.md §13a)

* **Is rho bar-even?** This is now the whole mass question, and it is not
  touched here. prop:antiparticle-crossing-reversal item 4 asserts
  m_top(H^sigma) = m_top(H); that is sound for the Vol factor and UNPROVED for
  the rho factor.
* **Which of the three readings the author intends.** An authoring decision,
  not a measurement. All three are recorded; none is picked, and no content
  block is edited.
* **Whether a genuinely theta-dependent CP discriminant exists.** Scope (a)
  throughout: this refutes the stated theta-dependence of these blocks and
  rules out no ingredient.

### Do not repeat

The 1.3e7 ratio against the PDG e+/e- bound is what follows IF one accepts the
block's identification of delta_CP with a mass asymmetry -- which is exactly
the conflation this bean already flagged. Quote it with that conditional
attached, never as a framework prediction of a 10.4% mass asymmetry.

**Artifacts.** computations/cp/delta_cp_theta_order_and_mass_asymmetry_probe.py
(exact sympy, one mpmath mpf at 60 dps, no float64, rc 0);
QOU/Observations/CrossingDiscriminantThetaFree.lean (5 theorems, sorry-free,
lean-direct exit 0 with zero warnings).


---

## 2026-09-13 — the theta-dependence is live in TWO content blocks, not one

Corpus-grepped `Sakharov` across `content/ docs/ computations/`: the claim
this bean refutes sits in **two** blocks on `main`, and neither was corrected
when `crossingDisc_norm_theta_free` landed (`7ecbd74fc6`).

1. `observations/cosmological-chirality-flip.md` — "This meets Sakharov's
   conditions: ... 2. Complex phase $\theta$ supplies CP violation."
2. `observations/cp-violation-evidence.md` lines 18-23 and 27 — the whole
   "QOU interpretation" section: "CP violation stems from a residual phase
   $\theta_{res}$", "$\delta_{CP} \sim O(\theta_{res}^2)$ for single-crossing",
   "$\delta_{CP} \sim n_c\theta_{res}$ for multi-crossing".

**Block 2 is the quantitative one and its arithmetic is measurable.** Line 27:
*"If $\theta_{res} \sim \tanh(\ln q)\cdot\alpha_{EM}$, then
$\delta_{CP} \sim 10^{-3}$. This matches kaon systems."* The theorem says
$\tanh(\ln q)$ **is** the discriminant, with no $\alpha_{EM}$ factor:

| | value |
|---|---|
| block: $\tanh(\ln q_0)\cdot\alpha_{EM}$ | 7.58659846145e-4 |
| theorem: $\tanh(\ln q_0)$ | 0.103963710052 |
| factor | 137.035999178 = $1/\alpha_{EM}$ |

So the block's own kaon comparison ($K_L\to\pi\pi$, 2e-3) goes from 0.379x to
**52.0x**. The match it claims is lost by exactly $1/\alpha_{EM}$.

**And hjs8's discriminant is already published, by a second route.** The corpus
carries $E_{asym}/E_{sym} = \tanh(\ln q)$ at $n_-=0$ for **every** $n_+$
(`prop:crossing-energy-decomposition` item 4; `coulomb-charge.md:25` with the
general $(n_++n_-)/(n_+-n_-)$ multiplicity; Lean `em_strong_ratio_tanh`,
`QOU.Braiding.coulomb_strong_ratio_q_rational`). The trefoil $\sigma_1^3$ is a
positive braid, so this bean's $\delta_{CP}$ **is** that ratio identity. Worth
citing when the blocks are fixed — it makes the correction a pointer to
existing corpus rather than a new claim.

Probe: `computations/barparity/cp_theta_defect_and_two_asymmetries_probe.py`
(all assertions pass). **No content block edited** — which of the three
readings the author intends is an authoring decision, so this bean stays open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Checklist (Round 56 — PR #8192)
- [x] Non-vacuous Lean 4 formalization in `QOU.Eightfold.CPBarParityLevel3ChannelAndWignerS3Pinning` (`0` `sorry`, `0` vacuity audit findings)
- [x] 50-dps `mpmath` probe `computations/probes/cp_bar_parity_level3_channel_and_wigner_s3_pinning_probe.py` and stamped witness `computations/probes/cp-bar-parity-level3-channel-and-wigner-s3-pinning.witness.json` (`allPassed: true`, `scriptHash: d2a06f0c494a`, `scriptCommitSha: c0214e17e49e615dc65e266a92be3d79589d2874`)
- [x] Opened PR `litlfred/qou#8192` (`82fe2aa092fb7be41555f2084a2891bcea71c295`)
- [ ] Awaiting merge and final closure verification
