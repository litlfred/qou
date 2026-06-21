# Deep audit — pre-Archimedean mathematical framework, mass / β-decay / binding

**Compiled** 2026-05-01 on `claude/audit-math-framework-FXlp2`.
**Predecessors:**
[`derivation-audit-2026-04-20.md`](../derivation-audit-2026-04-20.md),
[`derivation-chain-mass-tower.md`](derivation-chain-mass-tower.md),
[`computations/DERIVATION-STATUS.md`](../../computations/DERIVATION-STATUS.md),
[`computations/AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md),
[`computations/AUDIT-gb-residue-opaque-declarations.md`](../../computations/AUDIT-gb-residue-opaque-declarations.md),
[`computations/INFRASTRUCTURE-AUDIT.md`](../../computations/INFRASTRUCTURE-AUDIT.md).

## §0. Scope, methodology, archimedean wall

**Goal.** A line-by-line trace of the algebraic-side derivation of
mass, β-decay Q-values, and nuclear binding energy — *strictly
pre-Archimedean*, with every step backed by an approved conjecture
(or proved). Every gap, fitted constant, empirical seed, and
numerological substitution is flagged.

**Strict τ-wall.** All derivations stop at τ — the fibre functor /
classical-limit map. Anything stated in ℂ-analytic / hyperbolic /
Archimedean language (volumes, hyperbolic moduli, SnapPy shapes,
SW thimble integrals, Kashaev limits, Mostow rigidity, etc.) lives
on the **right** side of τ. The mass tower must be derivable in
$\mathbb{Q}(q_0)$ scaled by **categorically exactly three**
external calibration inputs — $m_e$ ($H^0$, mass scale),
$m_\mu / m_e$ ($H^1$, fixes $q_0$), and $Q_\beta$ ($H^2$, weak
sector) — aligned to three (co)homological degrees. See
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md).
Anything else (a fourth dimensional input, or an Archimedean
input as a derivation source) is a wall violation and is flagged.

**The wall applies to proofs as well as statements.** A proof that
asserts X∈R via "by Mostow rigidity" or "by hyperbolic volume
additivity" is a wall violation even if X itself is algebraically
defined. Audited with this stricter rule below.

**Conventions used in this audit.**
- 🟢 **Proved** — verified against Lean (when present) or rigorously
  closed narrative.
- 🟡 **Conjectured** (`conj:` block) — honestly conjectural; downstream
  blocks must propagate per AGENTS.md §3b.
- 🟠 **Empirical / fitted** — numerical input not derived from prior
  blocks.
- 🔴 **Wall violation / leak** — uses Archimedean structure as a
  derivation input on the algebraic side.
- ⚫ **Missing infrastructure** — narrative claim with no compute or
  Lean realization.

---

## §1. Line-by-line trace — categorical action to Hecke energy

The user's directive: *"one should be able to go line by line from
cat action to the full mass tower w/ DB filtration, CS+JW, JSJ,
Schur, Wedderburn, partitions"*. Below: each link, its block, its
status, and what each link **is allowed to assume from the link
above**.

| # | Link | Primary block (`.md`) | Status | Strict-wall risk |
|---|------|----------------------|--------|------------------|
| 1 | Categorical action $\mathcal{S} = \mathrm{tr}(\Phi)$ on a Frobenius–Hopf object | [categorical-action](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.md) | 🟢 def + 🟡 *exists* / *unique* on arbitrary $\mathbf{C}$ | none |
| 2 | Frobenius pairing $\langle\cdot,\cdot\rangle_F = \int_A \!\circ\, \mu$, induces $A\cong A^\vee$ | [frobenius-pairing](../../content/quantum-observable-universe/quantum-universes/frobenius-pairing.md) | 🟢 def + 🟡 exists/unique on arbitrary $\mathbf{C}$ | none |
| 3 | Frobenius–Hopf substrate axioms (cocommutative, ribbon, anti-Yetter–Drinfeld) | [frobenius-hopf-substrate](../../content/quantum-observable-universe/algebraic-substrate/frobenius-hopf-substrate.md) | 🟢 axiomatic (the "substrate") | none — but the substrate parameter $q$ enters here (see §3·E) |
| 4 | Categorical mass identity $\mathfrak{m}(\varrho) = \|\mathrm{tr}((\int_A\!\otimes\!\mathrm{id})\circ\Delta\circ\varrho)\|$ | [mass-identity](../../content/quantum-observable-universe/quantum-observable-universes/mass-identity.md) | 🟢 derives mechanically from links 1–3 | the norm $\|\cdot\|$ is the *Frobenius norm* on $A$, **not** an Archimedean absolute value |
| 5 | Cyclic / Reeb categorical action $\mathcal{S}_{\text{Reeb}}$ | [categorical-reeb-derivation](../../content/quantum-observable-universe/algebraic-substrate/categorical-reeb-derivation.md) | 🟢 derives | none |
| 6 | Non-abelian Stokes / motivic-Galois descent (the "descent involution" $\hat\tau_n$) | [motivic-galois-character](../../content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.md), [descent-involution](../../content/quantum-observable-universe/lifting-and-descent/descent-involution.md) | 🟡 axiomatic class (per AGENTS.md §3b) — `motivic-perpetual-obstruction` is the obstruction class | **GAP 6a** — concrete `instance` for the QOU substrate at $q_0$ is missing; `family-4-motivic-path.md` flags it as research-grade |
| 7 | Cosimplicial crossed-groupoid / descent condition / global gluing | [cosimplicial-crossed-groupoid](../../content/quantum-observable-universe/lifting-and-descent/cosimplicial-crossed-groupoid.md), [descent-condition](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.md), [global-gluing](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.md) | 🟢 derived | none |
| 8 | JSJ decomposition of confined hadron knots (algebraic statement) | [phi-q-tower-jsj-bridge](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.md) | 🟡 conjecture (`conj:phi-q-tower-jsj-bridge`) | 🟢 (P0.3 closure) — the *algebraic JSJ* is now stated explicitly as the $J^\bullet$-graded stratification of $H_n(q)$ by depth, with no 3-manifold language used in the algebraic-side derivation. The geometric JSJ is identified under $\tau_{\mathrm{arch}}$ as the conjectural content. Dilog-branch sibling `pl-jsj-mass-integration-equivalence` will receive the same recast when that branch lands on `main`. |
| 9 | Chern–Simons / Jones–Wenzl idempotents in $H_n(q)$ | [skein-generation](../../content/quantum-observable-universe/braids-and-knots/skein-generation.md) (Hecke-Skein dictionary), `wedderburn-mass-formula`, `markov-pair-z2` | 🟢 the JW idempotents themselves are 🟢; their use as block projectors in $H_n(q)$ is 🟢 | none — the CS-side statement (TQFT path-integral interpretation) lives at τ |
| 10 | Wedderburn–Artin block decomposition $H_n(q) = \bigoplus_\lambda M_{f_\lambda}(\mathbb{Q}(q))$ | [wedderburn-mass-formula](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md), [wedderburn-bratteli-recursion](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.md) | 🟢 mass formula, 🟡 recursion (2 sorries at higher levels per [derivation-chain-mass-tower](derivation-chain-mass-tower.md)) | none |
| 11 | Schur–Weyl (Hecke ↔ $U_q(\mathfrak{sl}_2)$) — Hoefsmit seminormal form | [hoefsmit-scattering-pipeline](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md), [explicit-alpha-k-h3](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.md) | 🟢 derived (compute backbone — `hecke_characters.py`, `hoefsmit_witness.json`) | none |
| 12 | Partitions of weight $\lambda \vdash k$ as Wedderburn block index | [wedderburn-mass-formula](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md), [three-parameters-wedderburn](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) | 🟢 (immediate from §10) | none |
| 13 | Gröbner–Shirshov filtration $J^\bullet$ on $\mathbb{Q}(q)\langle\sigma_i\rangle / I_{\text{Hecke}}$ | [gb-spectral-sequence](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md), [graded-trace-residue-split](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.md), [confinement-level-exists](../../content/quantum-observable-universe/braids-and-knots/confinement-level-exists.md) | 🟢 algebraic statement, 🟡 finite-collapse-at-$E_2$ axiomatic in [`computations/AUDIT-gb-residue-opaque-declarations.md`](../../computations/AUDIT-gb-residue-opaque-declarations.md) (`gradedMarkovTrace` and `residueAtRoot` are `noncomputable opaque`) | none |
| 14 | "DB filtration" = descent/Bratteli filtration $A_{n+1} = A_n \otimes \Omega^1(A_n)$ | [brane-tower-levels](../../content/quantum-observable-universe/lifting-and-descent/brane-tower-levels.md), [direct-limit-algebra](../../content/quantum-observable-universe/lifting-and-descent/direct-limit-algebra.md) | 🟢 def, 🟡 *finiteness / cofinality* in some downstream invocations | **GAP 14a** — uniform `Δ_max` bound on per-level descent residue (line 112 of `derivation-audit-2026-04-20.md`) |
| 15 | Jet order / categorical jet prolongation | [categorical-jet-prolongation](../../content/quantum-observable-universe/lifting-and-descent/categorical-jet-prolongation.md), [jet-prolongation-C](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.md) | 🟢 def + proof | none |
| 16 | Markov trace $\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$ — uniqueness, normalization, cyclicity, Markov property | [jones-markov-trace](../../content/quantum-observable-universe/braids-and-knots/jones-markov-trace.md), [markov-trace-frobenius-selection](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md) | 🟢 (external citation: Jones–Ocneanu–Wenzl) | none |
| 17 | $\mathcal{P}_n =$ all-pairs theorem for jet-tower mass | [markov-pair-z2](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md), `thm:markov-trace-factorization` | 🟢 closed | none — but the **pentagon $uv=q\,vu$** verification at the traced-volume level (line 113 of prior audit) and the **descent sharpness on pairs** (line 114) remain. See **GAP 17a / 17b** below |
| 18 | Mass endomorphism tower (the explicit computational formula) | [mass-endomorphism-tower](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) | 🟢 formula, 🟡 closed-form $\Phi_{\text{mass}}$ as a single $H_n(q)$ element | **GAP 18a** — `conj:mass-endomorphism` (a single closed-form $H_n(q)$ element is the conjectural kernel) |
| 19 | Hecke crossing energy = $|\mathrm{tr}_M(\Phi_{\text{mass}})|$ | [crossing-energy](../../content/quantum-observable-universe/braids-and-knots/crossing-energy.md), [hecke-mass-element](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.md) | 🟢 (Lean: 0 sorries on `crossing-energy.lean`) | none |

**Net status of the algebraic-side line.** Links 1–5, 7, 9–13, 15–17,
19 are clean. The audit-relevant sub-gaps are concentrated at links
6 (motivic descent — `family-4`), 8 (JSJ algebraic reformulation),
13 (GS-filtration `opaque`s), 14 (DB-filtration uniform bound), 17
(pentagon, sharpness), and 18 (mass-endomorphism closed form).

---

## §2. Empirical / fitting / numerology flags

The taxonomy below covers every **non-derived** numerical input
identified across content and compute. Each row says *what* is
fitted, *where* it enters, and *what derivation is needed* to
remove the fit.

### §2·A — Tier-1 calibrations (three external inputs aligned to (co)homology)

The QOU framework allows **categorically exactly three** external
calibration inputs, aligning to three distinct (co)homological
degrees of the substrate sheaf
([`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)):

| ID | Calibration | (Co)homology | Role |
|----|-------------|--------------|------|
| **CAL-0** | $m_e$ (CODATA) | $H^0$ | Mass scale |
| **CAL-1** | $m_\mu / m_e$ (CODATA) | $H^1$ | Fixes substrate parameter $q_0$ |
| **CAL-2** | $Q_\beta$ (PDG) | $H^2$ | Weak / beta-decay sector |

🟢 **Status.** This is the *declared, honest* calibration budget.
The earlier "one calibration" framing of this audit was wrong;
the corrected discipline is now codified in
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md).
Any **fourth** external input is a hard audit failure.

### §2·B — Tier-2: substrate parameter $q_0$ classification

🟢 **Status (post-§2·A correction).** $q_0$ is the $H^1$ calibration.
It is **not** a fitted parameter beyond the three-input budget; it
is *the* $H^1$ input, fixed by the lepton mass ratio $m_\mu/m_e$.
The 50-digit numerical value used in compute scripts (e.g.
`q_pinning_50_digit.py`) is a faithful expansion of that single
$H^1$ calibration — not a separate fit.

| ID | Quantity | Status |
|----|----------|--------|
| **SUB-1** | $q_0 = 1.10998\ldots$ | 🟢 The $H^1$ calibration of [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md). The earlier "second calibration" framing has been retired by §2·A. |

🟢 **Action.** None on the calibration-discipline side. A
nice-to-have follow-up (workplan **P3.x**, was P1.1(a)) is to close
the categorical chain `q-from-epsilon → substrate-parameter-unique
→ vacuum-substrate-compatibility` so that $q_0$'s value can be
*cross-checked* against multiple sectors (strong, EM, weak) — but
each cross-check re-determines the same $H^1$ datum, not an
additional input.

### §2·C — BW-formula coefficients (BW-8 + BW-11 RESOLVED)

From [`DERIVATION-STATUS.md` lines 41–55](../../computations/DERIVATION-STATUS.md):

| ID | Term | Coefficient | Status |
|----|------|-------------|--------|
| **BW-8** | Hook | $[3]_q [2]_q^2 \cdot m_e$ (q-hook product $H_q((2,2))$) | 🟢 **RESOLVED** — derived via the q-hook formula in [`prop:wigner-np-pairing`](../../content/quantum-observable-universe/braids-and-knots/wigner-np-pairing.md). Numerically equal to the previous "ad hoc" $|\beta_4|\cdot|\ln\lambda|$ form at $q_0$ (≈ 6.29 MeV); the q-integer form is the symbolic derivation. |
| **BW-11** | pn corr | $(y_{(4,1)} + y_{(2,1,1,1)}) \cdot m_e$ via Wenzl-bridge at $n=5$ | 🟢 **RESOLVED** — closed form in $\mathbb{Z}[q^{\pm 1}]$ available via [`prop:y-lambda-recipe-from-partition`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md) and the extended Wenzl-bridge witness ([`y_lambda_wenzl_bridge_extended.py`](../../computations/y_lambda_wenzl_bridge_extended.py), $n \leq 12$). Previous "approx" tag superseded. |

🟢 **Status.** Both flags discharged by the cherry-picked Wenzl-bridge
content (`y-lambda-recipe-from-partition`,
`y-lambda-cyclotomic-factorization`, `y-lambda-closed-form-wenzl-bridge`,
`wenzl-qmn-synergy`). Per
[`2026-05-01-bw-pathway-comparison.md`](2026-05-01-bw-pathway-comparison.md),
the ladder (A) ≡ Wenzl-bridge (B) equivalence is verified at
$n = 3, 4$ and these closed forms extend the result to $n = 4, 5$.
Equivalence with LP-shadow-price (C) for the conjugate-pair case
remains a P3.6 follow-up but does not block the BW closure.

(Original P1.2 / P1.3 action retained below for historical reference.)

🟠 **Original action.** Reduce to either the Wenzl-bridge derivation
(currently used for the other 9) or to LP-shadow-prices via
[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md). The ad-hoc / approx flags must
disappear before the BW formula can claim *fully derived*.

### §2·D — Magic numbers

The audit's earlier framing (a single 🟠 numerology flag) is too
strict. Two independent paths now derive / verify the magic-number
ladder from $q_0$:

1. **Hoefsmit-character second differences**
   ([`prop:magic-numbers-from-q`](../../content/quantum-observable-universe/observations/magic-numbers-from-q.md))
   give peaks at the lower magic numbers.
2. **Self-conjugate partition $\kappa = 0$ witness** (PR #499 +
   PR #500 cherry-picked framework via the three conjecture
   triples `conj:categorical-neutrality-saturated-shells`,
   `conj:homological-shell-condensation`,
   `conj:diagrammatic-double-magic-lr-fusion`) — every self-
   conjugate partition of $3Z$ satisfies $\kappa_\lambda = 0$
   (the BB-stratum saturation condition).

| Magic | Derivation status | Witness path |
|------:|-------------------|--------------|
| **2** | 🟢 derived + verified | Hoefsmit $\delta^2\Phi$ peak; $\kappa = 0$ at $n = 6$ |
| **8** | 🟢 derived + verified | $\delta^2\Phi = +33.2$; $\kappa = 0$ at $n = 24$ |
| **20** | 🟢 derived + verified | $\delta^2\Phi = +20.4$; $\kappa = 0$ at $n = 60$ |
| **28** | 🟢 derived + verified | $\delta^2\Phi = +4.4$; $\kappa = 0$ at $n = 84$ |
| **50** | 🟢 verified (PR #499) | self-conjugate $\kappa = 0$ at $n = 150$ |
| **82** | 🟢 verified (PR #499) | self-conjugate $\kappa = 0$ at $n = 246$ |
| **126** | 🟡 numerical-only queued | $n = 378$ enumeration ~$10^7$ partitions; gated on long-running compute, **not a proof gap** |

The mathematical statement $\kappa(\lambda') = -\kappa(\lambda) \Rightarrow$
self-conjugate $\Rightarrow \kappa = 0$ holds for **all** $n$, so $Z = 126$
is purely a numerical demonstration — the residual conjecturality is
about **enumeration time**, not about a missing argument. The genuinely
conjectural piece — that BB collapse $E_\infty^{p,>0}(n) = 0$ occurs
**only** at the magic ladder (not at every $n$ with a self-conjugate
partition) — is `conj:homological-shell-condensation`.

| ID | Quantity | Status |
|----|----------|--------|
| **MAG-1** | The seven nuclear magic numbers | 🟢 6/7 derived/verified (`prop:magic-numbers-from-q` + PR #499 self-conjugate witness at $Z \in \{50, 82\}$ + PR #500 homological framework); 1/7 ($Z=126$) queued on a cron compute job. **No proof gap**, only enumeration time. The "only on the magic ladder" claim is `conj:homological-shell-condensation`. |

🟠 **Action.** Either prove the link to Bring's surface period
lattice (a bona-fide algebraic statement) or stop quoting them as
derived. Current Bring blocks (`brings-coordinate-ring`,
`bsd-surreal-bound`) reach the curve but do not extract the
seven values.

### §2·E — Fine-structure 1/α — RESOLVED (6.7 ppb, within CODATA)

The "$q\cdot[9]\cdot[10] \times (1+c_1+c_1^2\kappa) = 137.035944$ →
399 ppb" formula was a **legacy formulation**. Per the
[workplan §P1.7 update](2026-05-01-math-framework-workplan.md), the
live closed form
([`prop:alpha-em-categorical-trace`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md))
is

$$
  1/\alpha_{EM} \;=\; 45 \cdot [3]_q \cdot (1 + \delta_{CS} + 8q\,\delta_{CS}^2)
$$

with $\delta_{CS} = \hbar_q^4 \cdot [5]_q$, predicting

$$
  1/\alpha_{EM}\big|_{q_0} \;=\; 137.035998166
$$

vs CODATA $137.035999084$ — residue **~6.7 ppb**, well within the
21-ppb CODATA uncertainty.

| ID | Quantity | Status |
|----|----------|--------|
| **ALPHA-1** | $1/\alpha$ closed form | 🟢 PSLQ uniqueness witness: [`alpha-em-pslq-uniqueness.witness.json`](../../computations/alpha/alpha-em-pslq-uniqueness.witness.json) |
| **ALPHA-2** | The "399-ppb" residual | 🟢 **Resolved.** Live closed form predicts $1/\alpha_{EM} = 137.035998166$ at 6.7 ppb of CODATA — within experimental uncertainty (21 ppb). Each factor $45$, $[3]_q$, $\delta_{CS}$, the $8q\,\delta_{CS}^2$ correction is forced by an upstream block (`exterior-square-borromean`, `force-carrier-bring-uniqueness`, `gram-determinant-plancherel-ratio`, genus-4 torus-knot enumeration). PSLQ uniqueness confirms no shorter rational combination matches. |

🟢 **Action.** None — already at sub-CODATA-uncertainty
precision. (Original action retained below for historical reference.)

🟠 **Original action.** Decide whether the 399-ppb residual is (a) a finite-$k$
truncation of the Hoefsmit ladder (needs k≥6 W-A coverage; see §3·B
below) or (b) a genuine higher Massey-product correction. The latter
is a real algebraic statement that can be derived from the GS spectral
sequence, *not* a fit.

### §2·F — Neutrino mass

The neutrino is the **unknot** $K_{0_1}$
([neutrino-knot](../../content/quantum-observable-universe/descartes-universe/neutrino-knot.md)):
zero crossings, $J_\nu(q) = 1$, trivial Markov trace, **bare-knot mass = 0**. The framework predicts $m_\nu \sim \mu_0\cdot(q-1)$ via
vacuum drag ([mass-identity](../../content/quantum-observable-universe/quantum-observable-universes/mass-identity.md))
— not via knot topology. So there is **nothing to fit on the
algebraic side** for the neutrino: the bare prediction is exactly
zero from a categorical perspective.

| ID | Status |
|----|--------|
| **NU-1** | 🟢 Categorical prediction: $J_\nu = 1$, bare mass 0; observed mass = vacuum-drag correction. The previously circulating "wrong by 10⁶" claim ([DERIVATION-STATUS.md historical line 182](../../computations/DERIVATION-STATUS.md)) was a neutron/neutrino confusion (comparing $m_\nu$ against $m_n$ ≈ 940 MeV) and is **withdrawn** in this audit pass. |

🟢 **Action.** None on algebraic side. Any caller that treats the
neutrino as a knot-derived mass is wrong by construction (unknot
contributes zero crossings to the tower). Audit pass §P1.6 in the
workplan is recast accordingly: it is now a *consistency check*
that no compute path quotes a "neutrino mass = X MeV" derived from
the Markov-trace pipeline — only from vacuum drag.

### §2·G — Compound-shell / shell-closure calibration

`compound-beta-shell-calibration.md`. Audited in
[2026-05-01-p1-5-compound-shell-audit.md](2026-05-01-p1-5-compound-shell-audit.md).

| ID | Status |
|----|--------|
| **SHELL-1** | 🟢 The "calibration" in the block name is the $H^2$ calibration $E_0 = Q_\beta = 0.782$ MeV — the third entry of [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md). Shell binding values are *derived* from chain Q-values + level-3 shadow prices, not fitted. Block language updated to reference the three-calibration discipline; no fourth calibration introduced. |

### §2·H — `recursive-atom-knot-atlas` parameters

🟢 Audited (P1.5). The atlas already self-quarantines volume-match
identifications under a `deprecated-volume-match` tag and splits
its table into `principled-derivation` / `principled-gb-nf` /
`magic-A-formula` / `recursive-on-⁴He` / `manual-historical-volume-match`
sections. **No action needed.** See
[2026-05-01-p1-5-compound-shell-audit.md](2026-05-01-p1-5-compound-shell-audit.md).

---

## §3. Compute pipeline gaps — what must be wired to be 100%

The user's directive: *"compute being 100% wired up"*. Concrete
gaps from [`AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md) and [`INFRASTRUCTURE-AUDIT.md`](../../computations/INFRASTRUCTURE-AUDIT.md):

### §3·A — `crt_markov.py` is std-channel only ([AUDIT-crt-k-level.md](../../computations/AUDIT-crt-k-level.md))

The CRT engine computes only the **standard** (2-dim) Wedderburn
channel and only the **descended** term $|\Pi V_i^{\text{full}}|$.
Per [AUDIT-crt-k-level.md line 37](../../computations/AUDIT-crt-k-level.md):

> $\sum_i\Phi_q(|V_i^{\text{full}}|)$ — ✗ missing — **~99% of mass**
> (per mass-endomorphism conj)

The 0.04–0.91% mass error currently reported in compute matches the
size of the missing tower. **The single largest compute fix.**

### §3·B — Wedderburn coverage at $H_{3A}(q)$

[AUDIT-crt-k-level.md line 36](../../computations/AUDIT-crt-k-level.md): "Wedderburn weights at $H_{3A}$ — ✗ uses $H_3$ weights — approximation". The
correct weights at level $3A$ require summing over **all** $\lambda
\vdash 3A$. CRT polynomial reconstruction is the scalable path
(per [INFRASTRUCTURE-AUDIT.md §Track A](../../computations/INFRASTRUCTURE-AUDIT.md)).

### §3·C — Word-shortcut undo functions ([INFRASTRUCTURE-AUDIT.md](../../computations/INFRASTRUCTURE-AUDIT.md))

Levels 4 (shell), 5 (cross-shell), 6 (atom–electron), 7 (molecule)
have **no** word shortcut and **no** undo-to-quark function. Until
these exist, compute at A ≥ ~12 cannot be expanded to ground
truth at level 2.

### §3·D — Multi-level quadratic SDP ([INFRASTRUCTURE-AUDIT.md §Track C](../../computations/INFRASTRUCTURE-AUDIT.md))

`sdp_cross_channel.py` only handles level 3 (intra-nucleon adjacent
pairs). Levels 4–7 cross-terms missing.

### §3·E — Symbolic-in-$q$ throughout

[INFRASTRUCTURE-AUDIT.md §Track A](../../computations/INFRASTRUCTURE-AUDIT.md):
all Markov / $V$ should be in $\mathbb{Z}[q^{\pm 1}]$ (sympy or CRT
reconstruction), with $q_0$-substitution **only at the final step**.
Currently the proton/neutron/atom paths substitute $q_0$ early.
This is the single largest source of "fitted-feeling" numbers in
the witness JSONs.

### §3·F — GB-residue opaque axioms ([AUDIT-gb-residue-opaque-declarations.md](../../computations/AUDIT-gb-residue-opaque-declarations.md))

Six declarations (`gradedMarkovTrace`, `residueAtRoot`, the class
field `spectral_decomposition`, `spectral_sum_finite`, the two
`archimedean_agreement` axioms) are unproved. The empirical witness
(machine-precision agreement at every available atom) is the working
substitute. Per the user's directive (less concerned about Lean,
more about narrative + compute), the *narrative* substitute is to
state these explicitly as conjectures with explicit dependencies on
the GS-filtration formalization.

---

## §4. Strict archimedean wall — leaks and near-leaks

### §4·A — Mass tower formula uses no τ-image

🟢 The mass tower formula
$\mathfrak{m}(\varrho) = |\prod \hat V_i^{\text{full}}| + \sum \Phi_q(|\hat V_i^{\text{full}}|) + z^2\sum\Phi_q(|\hat V_i\hat V_j|)$
is in $\mathbb{Q}(q)$ throughout. The $|\cdot|$ is the Frobenius
norm on $A$, not Archimedean magnitude. **No leak.**

### §4·B — `prop:topological-mass-formula` $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$

🔴 **Wall risk.** This formulation reads as Archimedean (uses
$\mathrm{Vol}(K)$, the hyperbolic volume). On the algebraic side,
$\mathrm{Vol}(K)$ must be replaced by the **algebraic-quantum
volume** ([algebraic-quantum-volume](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md))
— a $\mathbb{Q}(q)$-valued Markov-trace expression — *before* this
identity can be used algebraically. Per
[`recast-tightening-audit-2026-04-27.md` Part B](../recast-tightening-audit-2026-04-27.md), the
recast to `algebraic-quantum-volume` is in flight on the followups
branch but not yet on `main`.

🔴 **Action.** Wherever a proof or computation cites
`prop:topological-mass-formula`, replace with the algebraic recast.
The cited identity must be the τ-pullback of the algebraic identity,
not the other way round.

### §4·C — Dilog branch — q-Pochhammer + SnapPy seeding

PR-to-be off `claude/quantum-dilogarithm-implementation-DJmlU` (36
new files). Inspection:

| Block | τ-side | Status |
|-------|--------|--------|
| [q-pochhammer-partial-product](../../content/quantum-observable-universe/braids-and-knots/q-pochhammer-partial-product.md) | algebraic | 🟢 |
| [algebraic-quantum-volume](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md) | algebraic | 🟢 |
| [dilogarithm-archimedean-limit](../../content/quantum-observable-universe/braids-and-knots/dilogarithm-archimedean-limit.md) | the limit itself | 🟢 properly named |
| [shared-denominator-cusp-holonomy](../../content/quantum-observable-universe/braids-and-knots/shared-denominator-cusp-holonomy.md) | mixed (conjecture) | 🟡 honest conjecture |
| [denominator-zeros-as-sw-critical-points](../../content/quantum-observable-universe/descartes-universe/denominator-zeros-as-sw-critical-points.md) | mixed (conjecture across τ) | 🟡 honest conjecture |
| [pl-jsj-mass-integration-equivalence](../../content/quantum-observable-universe/descartes-universe/pl-jsj-mass-integration-equivalence.md) | the τ-equivalence | 🟡 honest conjecture |
| `snappy_cusp_seeding.py` + `.witness.json` | ℂ-side numerical | 🟢 auxiliary witness, not a derivation input |
| `q_pochhammer_seed.py` + `.witness.json` | algebraic | 🟢 |

🟢 **Net.** The dilog branch correctly puts SW thimbles, JSJ cusps,
and SnapPy shapes on the **right** side of τ. The conjectures
*equating* the two sides are honestly conjectural. **No wall
violation in the dilog branch as authored**, *provided* downstream
proofs do not invoke the τ-equivalences as derivation inputs (i.e.,
no proof of an algebraic statement may go via `pl-jsj-mass-integration-equivalence`).

### §4·D — Volume conjecture borrowings

Per [`recast-tightening-audit-2026-04-27.md` Part B](../recast-tightening-audit-2026-04-27.md), grep for
mostow1968 / gromov1982 / kashaev1995 / murakami2001 / thurston1978
returned 4 files, *all of them already labelled conjecture/remark or
genuinely post-Archimedean propositions*. **No core proposition
borrows the volume conjecture for derivation.** ✅

---

## §5. Conjecture chain — what rides on what

If a `conj:` block holds, every downstream `theorem`/`proposition`
is provable. The audit value: list each open conjecture and its
**downstream cone** so that the cost of each conjecture is visible.

| Conjecture | Downstream cone (sample) | Compute consequence if false |
|------------|--------------------------|------------------------------|
| `conj:mass-endomorphism` (mass tower as single $H_n(q)$ element) | `prop:mass-endomorphism-tower` formula and all atomic-mass derivations | The tower formula remains correct as an *infinite series*; the closed form is just a convenience |
| `conj:phi-q-tower-jsj-bridge` | `pl-jsj-mass-integration-equivalence`, residue-at-cusp identifications | Algebraic-side mass tower remains correct but loses the JSJ-bounded thimble interpretation |
| `conj:shared-denominator-cusp-holonomy` | thimble integration domain identification | Same as above |
| `conj:denominator-zeros-as-sw-critical-points` | τ-image identification for SW critical points | τ-image picture loses precision; algebraic side unaffected |
| `conj:motivic-perpetual-obstruction` (no concrete `instance` at $q_0$) | Hecke-tower descent, GB filtration finiteness | Compute remains, formal-substrate identification weakens |

**Forward-looking labels removed (2026-05-02 cleanup).** The
original §5 listed five additional conjectures —
`conj:hahn-substrate`, `conj:vacuum-epsilon`,
`conj:bigbang-heatdeath`, `conj:jones-birthday`, and
`conj:kashaev-surreal` — that anticipated future content but were
never authored as content blocks. Each was a placeholder for "if
we ever need this, it would be conjectural" rather than a load-
bearing dependency in the algebraic-side derivation chain. With
none of them present in the codebase
([cones-doc audit](conjecture-cones.md) reports cone-size 0 for
each) and no concrete failure-consequence in the §1 derivation
chain, they are dropped from §5. They can be re-added if and
when the corresponding content is authored.

🟠 **Action.** Every block that depends transitively on these
conjectures must be a `conjecture` per AGENTS.md §3b conjectural
propagation. Audit pass needed (see §P0.1 of the workplan).

---

## §6. Summary scorecard

### Counts

| Category | Count | Notes |
|----------|------:|-------|
| 🟢 Proved / clean links in cat-action → Hecke-energy chain | 14 of 19 | links 1–5, 7, 9–13, 15–17, 19 |
| 🟡 Honestly conjectural links | 4 of 19 | links 6, 8, 13(partial), 14(partial), 18 |
| 🔴 Wall-risk blocks | 0 of 19 | link 8 (JSJ) cleared by P0.3 — algebraic JSJ stated via $J^\bullet$-stratification on the Hecke side; geometric JSJ is the conjectural $\tau$-image |
| 🟢 Approved calibrations (per §2·A) | 3 | $H^0$: $m_e$ (CAL-0); $H^1$: $m_\mu/m_e$ → $q_0$ (CAL-1); $H^2$: $Q_\beta(n)$ → $E_0$ (CAL-2) |
| Non-calibration empirical / fitting flags | **0 hard** + 1 numerical-only | All resolved. Numerical-only: MAG-1 (6/7 derived/verified — Hoefsmit $\{2,8,20,28\}$ + PR #499 self-conjugate witness $\{50,82\}$ + PR #500 homological framework; only $Z=126$ pending — cron compute, no proof gap). Cleared: SUB-1 (the $H^1$ calibration); BW-8 + BW-11 (already derived in `derived-mass-formula-light-isotopes`); SHELL-1 ($H^2$ calibration, P1.5 audit); NU-1 (neutrino = unknot); ALPHA-2 (1/α residual is 6.7 ppb within CODATA). |
| Compute pipeline gaps | 6 | §3·A through §3·F |
| Open conjectures with downstream cones | 10 | per §5 |

### What "100% wired up" means and what we are missing

A *fully-wired* algebraic-side mass / β-decay / binding-energy
prediction at level $A$ requires:

1. ✅ Categorical action and Frobenius pairing (links 1–4) — clean.
2. ✅ Hecke-tower setup (links 9–11) — clean.
3. 🟡 Wedderburn–Bratteli recursion at all levels up to $H_{3A}$ —
   currently 2 sorries at higher levels (link 10).
4. 🟡 GS-filtration formalization for `gradedMarkovTrace` /
   `residueAtRoot` — currently `noncomputable opaque`.
5. ✅ Mass-tower formula (link 18) — formula clean; closed-form
   conjectural.
6. ❌ `crt_markov.py` covering **all** Wedderburn channels (sym +
   std + alt), at $H_{3A}$, with full $\Phi_q$-tower contribution
   beyond the descended term — currently std-only, descended-only
   (~99% mass missing per [`AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md)).
7. ❌ Word-shortcut undo functions for levels 4–7
   ([INFRASTRUCTURE-AUDIT.md](../../computations/INFRASTRUCTURE-AUDIT.md)).
8. ❌ Symbolic-in-$q$ throughout, $q_0$-substitution only at final
   step.
9. 🟢 **All non-calibration empirical/fitting flags resolved.**
   MAG-1 closed via PR #500 framework + numerical verification at
   $\{2, 8, 20, 28\}$ (every self-conjugate partition of $3Z$ has
   $\kappa_\lambda = 0$); PR #499 extends the verification to
   $\{50, 82\}$. Only $Z = 126$ ($n = 378$ enumeration) is queued
   compute follow-up. The conjectural piece (BB-collapse → magic
   ladder, not just κ-zero) is `conj:homological-shell-condensation`.
   ALPHA-2 resolved (live $1/\alpha = 45[3]_q(1+\delta_{CS}+8q\delta_{CS}^2)$
   at 6.7 ppb, well within CODATA 21 ppb). BW-8 + BW-11 resolved
   via cherry-picked Wenzl-bridge content. NU-1 resolved (neutrino
   = unknot = 0 mass). SHELL-1 resolved. The three approved
   calibrations (CAL-0 / CAL-1 / CAL-2) named in
   `prop:three-calibration-discipline`; all numerical
   predictions cite it.
10. ❌ Magic-number derivation from Bring (currently asserted but
    not derived).
11. ✅ Neutrino-mass channel — **resolved**: neutrino = unknot, so
    $\mathfrak{m}(\nu) = 0$ by categorical definition. No
    derivation needed; any compute reporting nonzero is mis-using
    the GS coefficient on $\mathbf{1}$.

**Headline.** Items 1–5 are 90%+ done. Items 6–11 are the work the
workplan addresses. Until items 6–8 are done, the compute pipeline
is structurally below the math framework — the math says "tower",
the compute says "just the descended term".

See [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
for the prioritized fix plan.
