# Addendum — calibration-inputs taxonomy (correction to deep audit)

**Pair**:
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md),
[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md).
**Branch**: `claude/tier3-math-audit-B0wyO`.

## What this addendum corrects

The deep audit (§2·A "Tier-1 calibration") and the workplan (§P0.4)
treated the framework as having **one** allowed external scale
($m_e$) and worried that $q_0$'s pin to CODATA $m_\mu/m_e$ (audit
flag SUB-1) constituted a *second*, undeclared calibration. That
framing is wrong.

The paper's own
[`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md)
declares **exactly three** calibration inputs, and the framework
forbids all other empirical / fitting / numerological inputs:

| Input | What it fixes | Sector |
|-------|--------------|--------|
| $m_\mu / m_e$ | substrate parameter $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | dimensionless ratio (shape) |
| $m_e$ | leptonic mass scale (MeV ↔ natural units) | leptonic size |
| $Q_\beta(n)$ (free-neutron β-decay) | hadronic energy scale $E_0$ | hadronic interaction strength |

These align to (co)homology: the three Wedderburn channels
(sym / std / alt) of $H_3(R, q)$ provide the three independent real
parameters that survive the on-shell constraint
$\star_q F_\nabla = F_\nabla$ and gauge invariance
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([`prop:three-parameters-wedderburn`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md)).
The 19 free parameters of the Standard Model (6 quark masses, 3
lepton masses, 3 CKM angles + 1 phase, 3 gauge couplings, Higgs
mass / VEV, QCD theta) reduce to these three because particle
content is topological (from $\chi = -6$), mass ratios are knot
invariants, and coupling constants are $R$-matrix eigenvalues.

## Effect on the deep-audit flag taxonomy

| Audit flag | Original status | Corrected status |
|------------|-----------------|------------------|
| **CAL-1** ($m_e$) | 🟠 "honest single-scale calibration **iff** declared" | 🟢 **Approved calibration #2** (leptonic scale) |
| **SUB-1** ($q_0$ pinned to $m_\mu/m_e$) | 🟠 "second external calibration, undeclared" | 🟢 **Approved calibration #1** (dimensionless ratio) |
| **(new)** $Q_\beta(n)$ → $E_0$ | (not flagged in deep audit) | 🟢 **Approved calibration #3** (hadronic scale) |

All three are explicitly enumerated in the paper. None require
demotion; none constitute hidden fitting. The audit's
recommendation to "promote the single-scale assumption to a named
proposition `prop:single-scale-calibration`" is replaced by:
the existing `rem:calibration-inputs` (and the proposition
`prop:three-parameters-wedderburn` it references) already plays
this role at the *three-parameters* level. The audit's worry was
about the **count**; the paper has been correct on the count all
along.

## What remains forbidden (strict)

Beyond these three, the framework allows **no** empirical inputs
of any kind. The deep audit's other flags remain valid as
non-calibration empirical leaks that must be eliminated:

| Audit flag | Status | What must happen |
|------------|--------|------------------|
| **BW-8** (Hook coeff "ad hoc") | 🟠 must derive | P1.2 |
| **BW-11** (pn corr "approx") | 🟠 must derive | P1.3 |
| **MAG-1** (magic numbers from Bring) | 🟠 must derive | P1.4 |
| **SHELL-1** (compound-shell-calibration) | 🟠 must verify or eliminate | P1.5 |
| **NU-1** (neutrino off by 10⁶) | 🔴 must demote to conjecture or fix | P1.6 |
| **ALPHA-2** (1/α 399-ppb residual) | 🟠 must derive (truncation or genuine higher-order) | P1.7 |
| **(new)** Other "approx" / "ad hoc" tags discovered in `DERIVATION-STATUS.md` after re-audit | TBD | inventory pass |

The framework's three-calibration / no-fitting directive **tightens**
the workplan: any block currently tagged "approx", "ad hoc",
"empirical", or self-named "calibration" (other than the three
authorised inputs) must be derived or removed. There is no
"acceptable level of fitting" beyond the three.

## Workplan adjustments

- **P0.4** ("Single-scale-calibration block") — reformulate as
  *three-calibration-inputs block*. The
  [`rem:calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md)
  remark already lists the three; promote it (or its content) to
  a named proposition `prop:three-calibration-inputs` that the
  paper-wide sweep cites for every numerical comparison. The
  proposition's content: every mass / Q-value / binding energy is
  a $\mathbb{Q}(q_0)$-element times a fixed combination of $m_e$
  and $Q_\beta(n)$, with $q_0$ itself fixed by $m_\mu/m_e$. No
  other numerical inputs.

- **P1.1** ("Substrate parameter $q_0$ derivation chain") —
  the path-(b) "two-scale accounting" is no longer the lazy
  fallback; it is the *paper's published position* (three scales,
  not two). Path-(a) (deriving $q_0$ algebraically) is now an
  upgrade goal, not a correction.

- **(co)homology alignment** — the three calibration points
  correspond to the three Wedderburn channels of $H_3(R, q)$ — a
  cohomological statement at the level of the algebra's
  block-decomposition. A future audit pass may want to make this
  alignment explicit in `prop:three-parameters-wedderburn`'s `.md`
  by spelling out which calibration corresponds to which channel
  (sym / std / alt). This is a clarification task, not a fix.

## Effect on Tier 3 (this branch)

Tier 3 (P3, conjectural propagation) is independent of the
calibration-inputs taxonomy, so no Tier 3 deliverables need
updating. The audit-document corrections above are scoped to the
deep audit and workplan; they will be folded back to PR #498
(parent branch) as a separate update or treated as findings on
this branch.

## Recommendation

Apply this addendum's taxonomy correction to the deep audit
(§2·A) and the workplan (§P0.4, §P1.1) on the parent branch
`claude/audit-math-framework-FXlp2`. This branch (`tier3-math-audit-B0wyO`)
holds the addendum; the parent branch should consume it.
