# Coordination ledger — deuteron `E_unit` as a function of the 3 CALs (via 𝔇)

**Correction (owner, 2026-07-07).** The earlier framing of `E_unit` as a
*new derivable absolute scale* was wrong: a fourth calibrated energy is
**CAL-4, a cohomological violation** — H¹(Bring) = 2W has exactly three real
DOF, so exactly three calibrations (m_e, 𝔇_β, 𝔇_π). `E_unit` **must** be a
function of those three, not a new input. The "narrow Subgoal-2 scope for a
new bar-even scale" request is **withdrawn** as mis-posed; no Subgoal-2
reversal is in force. `E_unit` closure is an *in-scope* 3-CAL derivation, not
an absolute-scale derivation.

**Owner steer:** reinterpret `E_unit` in terms of **𝔇** (the decay width /
CAL-2 datum), i.e. `E_unit = ℏ/𝔇` for a 𝔇 already fixed by the calibration
triple.

## Why 𝔇 is the natural carrier

- CAL-2 is the neutron β-decay width **𝔇_β**; its energy proxy is
  `Q_β = ℏ/𝔇_β ≈ 0.784 MeV`. This is a genuine calibration datum, **not** a
  new input.
- The reeb-flow rate `g` **is a rate** (linking number per unit Reeb
  parameter). A rate is dimensionally a **width**. So the deuteron law
  `B = 5g·E_unit` is naturally read as `B = 5g·(ℏ/𝔇)` — a *width-derived
  energy*, with `𝔇` set by the bond dynamics from CAL-2, and `E_unit` the
  reciprocal-width energy. Nothing here is a fourth calibration.
- The deuteron is uniquely the **β-threshold nucleus** (one weak decay from
  instability), so its binding carrying a decay-width (weak-sector) character
  is physically coherent, and consistent with the sibling result that the
  pn sign is a weak-sector (bar-odd) observable
  (`ReebPnMagnitude.pn_sign_trace_blind`).

## Parity reconsideration (supersedes the D5 bar-even premise)

D5 concluded `E_unit` is bar-even and excluded the bar-odd 𝔇/Q_β sector.
That rested on the premise **"B(²H) is a bar-even binding"**. The 𝔇
reinterpretation puts that premise in question: if `E_unit = ℏ/𝔇` is the
bar-**odd** decay-width energy, then B(²H) is a **weak-sector (bar-odd)
magnitude** — appropriate for the β-threshold nucleus, and distinct from the
bar-even nuclear binding of e.g. ⁴He. The Lean lemmas `barEven_of_mul` /
`barEven_ne_barOdd` stand as *conditional* statements (they correctly say:
IF B is bar-even THEN E_unit is, and a bar-even E_unit ≠ bar-odd Q_β); what
the correction changes is the **antecedent** — B(²H)'s parity is the open
question, not settled bar-even. This is the (a)-scoped re-scoping of a
premise, not a refutation of the lemmas.

## The clean decomposition (bar-even structure × bar-odd unit)

The tension — the reeb-flow magnitude `5g` is built bar-**even** (the
marginal-stability `ss_det`), yet the deuteron is a weak-sector (bar-odd) pn
object — resolves as a **factorization by parity**:

```
B(²H)  =  (5g)          ×  E_unit
       =  bar-EVEN          bar-ODD
          geometric rate    decay-width energy  ℏ/𝔇
       =  bar-ODD  (weak-sector binding)
```

The dimensionless structure `5g` (fusion count × linking rate) is bar-even
and geometric; the **energy unit is the bar-odd decay-width quantum
`ℏ/𝔇`** — a CAL-2 datum. Their product is bar-odd: the deuteron binding is a
**weak-sector energy**, distinct in parity from the bar-even α-particle
binding of ⁴He. This is why the transition/decay sector is the right home
for `E_unit` (owner steer) and why the D5 "bar-even E_unit" premise was the
error: it is `B(²H)` that is bar-odd, carried entirely by the unit.

## Open question this ledger tracks

Is `E_unit = ℏ/𝔇` for a `𝔇` derived from CAL-2 (the β-width `𝔇_β`, dressed
by the bond's 2-body structure), reproducing `0.995940 MeV` **with a derived
`O(1)` factor and the correct parity** — keeping the deuteron law inside the
three calibrations? Predicted-first, no fishing; the golden-ratio-adjacent
`E_unit/Q_β ≈ √φ` (0.09 %) is a **numerology trap** (the #3444 cut), not a
candidate.

## Reconciliation with the landed sibling §2h (tranche 6, `ss_det_no_linear_term`)

A sibling reeb-flow tranche landed on main
([`…-reeb-flow-pn-magnitude…` §2h](../audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md))
directly on `E_unit`, and it **supersedes the optimistic read of the 𝔇
route**:

- **§2h.1 (proved):** the deuteron is one *open* pn bond, so `B` is the
  `O(g)` linear `5g` (the ss-matrix is traceless ⇒ no linear loop term;
  `ss_det_no_linear_term`, sorry-free). The `g`-order is derived.
- **§2h.2 (scope-a limit):** the exchange sector is **scale-free** — `g` and
  `√5` are dimensionless Hecke matrix data — so `E_unit` is external, and
  among canonical energies **the bar-even `2mₑ` is closest (+2.6 %)** while
  the bar-odd **`Q_β` is the worst (−21 %)**.

**Predicted-first 𝔇 test** (`e-unit-decay-width-reconcile-probe.witness.json`):
`E_unit = Q_β·F` needs `F = 1.2709`; the genuine 2-body factors (`2`,
`3/[2]_v`, `[3]_v/[2]_v`) miss by 18–57 %. So:

- **The 𝔇 reinterpretation is architecturally correct** — it removes the
  CAL-4 violation: `E_unit` must be a 3-CAL function, and `ℏ/𝔇` names *what
  kind* of object it is. This stands.
- **But numerically the decay-width sector is the worst**, and the landed
  §2h data actually favor a **bar-even** unit (`2mₑ`), contradicting the
  clean "bar-even × bar-odd = bar-odd" decomposition I proposed. The `√φ`
  factor that would rescue `Q_β` is numerology (walled off).

**Honest conclusion.** The parity *decomposition* is a hypothesis the numbers
disfavor; the deuteron's binding parity is **empirically open** (§2h weakly
favors bar-even). The `𝔇` route closes the *cohomology* question (no CAL-4)
but **not the number** — it confirms the §2h scale-free wall from the
decay-width side rather than crossing it.

## Sibling coordination (2026-07-07)

| PR | branch | relationship | action |
|---|---|---|---|
| §2h reeb-flow (merged) | — | **dependency** — proved `ss_det_no_linear_term` (deuteron = open bond ⇒ linear 5g; exchange sector scale-free) | reconciled above; my work adds the CAL-4 correction + parity framing |
| [#3429](https://github.com/litlfred/qou/pull/3429) | `claude/c3-derivation-q-beta-lhsg1a` | **overlap (bar-parity Lean)** — formalizing bar-even/ζ₄ prune lemmas for the Q_β f-map | posted intent: offered my `BarEven`/`BarOdd` σ-involution abstraction for reuse; shared the finding that bar-odd Q_β is the worst E_unit candidate (favors their bar-even constraint) |
| [#3437](https://github.com/litlfred/qou/pull/3437) | `claude/open-conjecture-5nx8-2026-07-06` | **overlap (binding/decay parity)** — §3b `binding-qbeta-complex-volume` class | posted light intent: my 5g·E_unit parity factorization ↔ their Re/Im(𝔙) split; flagged deuteron parity empirically open |

No §6 escalations: the sibling §2h and my `𝔇`-reconcile **agree** (unit
external / scale-free), no inconsistent findings to reconcile. #3429's
bar-even/ζ₄ constraint is **consistent** with my bar-odd-Q_β-is-worst
finding.

## Status

Open, in-scope (3-CAL), **wall confirmed from two sides** (exchange-sector
scale-free §2h; decay-width numerically worst, this ledger). No Subgoal-2
reversal. The honest landing point: `B(²H)` is a physically-motivated
near-match (`g`-order + `√5` derived; unit external), `E_unit` is a 3-CAL
function (not CAL-4) of open parity. Not a closed derivation — matching the
§3f NEAR-MATCH ruling.
