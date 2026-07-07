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

## Status

Open, in-scope (3-CAL). No Subgoal-2 reversal. Next step: state the bond-width
`𝔇` construction from CAL-2 predicted-first, then evaluate once.
