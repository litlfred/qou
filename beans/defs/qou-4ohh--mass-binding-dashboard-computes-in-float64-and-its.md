---
# qou-4ohh
title: mass_binding_dashboard computes in float64 — and its own accuracy claim is the f64 floor
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:32:21Z
updated_at: 2026-11-19T17:42:00Z
parent: qou-9nnz
---

MEASURED 2026-09-05 (compute-precision-auditor subagent) while producing the
low-isotope dashboard for the owner. Two defects, one of them a claim that must
be RETRACTED — and the retraction makes the underlying result STRONGER, not
weaker.

## DEFECT 1 — the dashboard computes in float64

computations/mass_binding_dashboard.py:314 `_scalars()` returns
`float(mex), float(q0x), float(e0x)` — m_e, q0 and alpha = E_0 are downcast —
and from there every binding number is float64 with math.log / math.exp:

  :493  tp = float(tr_m_atom_zn(1, 0, dps=50)[1])
  :495  return -alpha * math.log(tp), ...
  :632  ta, tf = float(ta), float(tf)
  :633  B_sym_exact = alpha * math.log(tf / ta)
  :562  B_lin = alpha * (1.0 - math.exp(-B_sym/alpha))

NO-FLOAT64 violation under the 2026-08-18 directive. This is a PRODUCER, and
probes are not exempt either.

INVISIBLE TO EVERY GATE, and the reason is the same detector-blindness class as
the sympy -> numpy.complex128 route: the two ratchets scan WITNESSES and this
script emits none; the three source-level gates key on mpf(<float>) / mp.dps /
module-consts; and mpf_mixed_arithmetic_audit looks for mpmath<->f64 MIXING,
which this evades by collapsing to pure float BEFORE any arithmetic.

Second float64 site, separate file: canonical_mass.py:51 does
`float(preds["m_p_MeV"])` — the witness stores 25-digit strings and the facade
throws away everything past digit 16.

## DEFECT 2 — RETRACT the "max|Delta| = 8.9e-16 MeV" claim

The dashboard prints:
  "B_sym closed-form chain = exact p(3A) trace: max|Delta| = 8.9e-16 MeV"

8.9e-16 MeV on an ~8.7 MeV quantity is 1.0e-16 RELATIVE = exactly float64
epsilon. That is the FLOOR OF THE ARITHMETIC, not a measurement of the
factorisation, and per the directive it may not be reported as an identity.

REDONE IN EXACT ARITHMETIC (mpf end to end, tr_m_atom_zn at 50 dps, 9.1 s):

  2H   1.897e-51 MeV   rel 6.70e-52
  3H   4.276e-50       rel 6.97e-51
  3He  4.276e-50       rel 7.96e-51
  4He  2.138e-50       rel 2.46e-51
  6Li  2.138e-50       rel 1.47e-51
  7Li  4.276e-50       rel 2.40e-51

max = 4.28e-50 MeV, at the 50-dps SERIALISATION floor — 34 ORDERS better than
the dashboard claims. So the writhe-normalised bond factorisation
B_sym = alpha[(Z-1)L_pp + L_pn + (N-1)L_nn] reproduces the full p(3A) Markov
trace to the compute floor. The good news is bigger than reported; the number
printed for it is meaningless as stated.

HONEST PHRASING for the fixed line: "agrees to 4.3e-50 MeV at 50-dps compute
precision."

## WITNESS FRESHNESS — traced, not inferred

EXACTLY ONE witness is read, established by instrumenting open /
Path.read_text / Path.read_bytes and running under runpy:
computations/m-p-substrate-identity-50dps.witness.json. Everything else —
tr_m_atom_zn, L_pp/L_pn/L_nn, B_sym, B_qCLT_fac, E_C, alpha — is computed live
in-process at 50 dps, so most of the dashboard CANNOT be stale.

That witness is self-stale by scriptHash (d4e739a31ca7 vs live d579ee01c97e)
and its commitSha is UNRESOLVABLE (the `rewritten` class), so
`git diff <commitSha> -- <producer>` is unrunnable. Re-ran instead (0.76 s):
the payload moves by ~1.7e-17 relative, and the cause is unambiguous —
  /parameters/m_e_MeV  '0.510998950690000009' -> '0.51099895069'
0.510998950690000009 is the float64 double nearest 0.51099895069, so the
COMMITTED witness was produced from a float64 M_E_MEV and codata_constants has
since been drained to mpf. IMPORT-CONE DRIFT IN THE DRAIN DIRECTION.

DID NOT REFRESH IT, and the producer said why on stdout: this container's run
would drop clarabel, downgrade mpmath 1.4.1 -> 1.3.0, and introduce 4 NEW raw
float64 fields. A 1.7e-17 improvement bought with a weaker environment stamp
and four new dirty fields is a baseline walking backwards.

allPassed:false is REAL and is the physics: m_n misses CODATA by 501.43 ppb
against a 10 ppb target (50x), matching the dashboard's own n row.

Triage, FIFTH independent run: 564 decided, substantive 223 / 39.5 %,
cosmetic 0 / 0.0 %, rewritten 254 / 45.0 %, unresolvable 81. Denominator moved
559 -> 564; quote these. Not one self-stale witness is safe to refresh.

## DOC DEFECT — .claude/commands/dashboard-low.md is stale on 3 of 5 forms

It advertises B_lin / B_sym / B_qCLT / B_qCLT_fac / B_magic. The headline table
prints B_can0 / B_sym / B_tetra / B_qCLT_fac / E_C. B_lin and B_qCLT are
demoted; B_magic occurs ZERO times in the producer (grep -c = 0). It also cites
standard-part-functor.md as the defining block, which the producer's own
docstring explicitly retracts.

## NOT FIXED HERE

Read-only run; the tree was left clean and nothing was committed. The float64
drain of mass_binding_dashboard.py is the actionable item and is NOT done.

## DEFECT 1 + DEFECT 2 FIXED — PR #6881 (stacked on #6864)

**The retraction landed, and it made the claim stronger exactly as this bean
predicted.**

FOUR f64 downcasts sat on the chain-vs-exact path, not one:

    _constants()            returned float(mex), float(q0x), float(e0x)
    _bond_type_L()          returned float(...) per bond
    _chain_writhe_shift()   returned float(...)
    exact-trace branch      did ta, tf = float(ta), float(tf) before math.log

**Why it survived, which is the reusable part.** The file was MID-migration,
not un-migrated. `_disp` already existed as the display boundary with the
invariant spelled out in its docstring. And `_bond_type_L`'s own docstring
already claimed *'the values are now mpmath end to end — the old body did
math.log(float(tf)/float(ta)), an f64 collapse the owner directive forbids'*.
That was true of the BODY and false of the RETURN: mpmath throughout, downcast
one line later. **The docstring and the internals agreed with each other and
both were wrong about what came out of the function.**

MEASURED, before/after, 2H/3H/3He at --max-strands 9:

    headline max|d|   8.9e-16  ->  2.1e-49 MeV
    2H                4.4e-16  ->  2.1e-49
    3H                0.0e+00  ->  4.3e-50
    3He               8.9e-16  ->  5.3e-50

Rendered dashboard diff is **12 lines** — the residual column and its headline.
Every other number byte-identical, so purely precision; no value moved.

**3H printed exactly `0.0e+00` before.** Not agreement — the difference
underflowing below f64 resolution. A perfect zero from an f64 subtraction of two
~8 MeV quantities is the signature, not the result. Worth remembering as a
detector: an exact 0.0 residual in a float pipeline is evidence of underflow,
not of identity.

The stale in-source comment claiming `|chain − exact| ≈ 1e-13` is corrected to
the measured 2e-49 in the same commit.

## What this does NOT fix

The dashboard still cannot complete at 4He and above (~21 min, then hours) —
that is the general-word kernel's d_lambda cost from `qou-wdij`, not a float64
issue. So this fixes the arithmetic of a producer that remains capacity-limited
above A=3.

## Still open on this bean

`canonical_mass.py:51` `_from_witness()` does
`float(preds['m_p_MeV']), float(preds['m_n_MeV'])`. MEASURED: the witness
carries **25** significant digits and float() keeps ~17, a relative loss of
**5.7e-17 (m_p) / 6.0e-17 (m_n)**. Correcting my own earlier framing — that is
~8 digits lost, not ~34, and it sits INSIDE the 1 ppQ (1e-15) L1 target rather
than breaking it. It is still a NO-FLOAT64 defect and still a hard ceiling on
55 consumers, but it is not urgent and a return-type change across 55 call sites
is not a small fix. Deliberately not bundled into #6881.

## Gate attribution (control run) + a detector blind spot the fix exposed

**Attribution: my change introduces ZERO new gate failures.** `precision-gates.sh
--changed` on the parent commit (the regression branch, WITHOUT the dashboard
change) returns a RED list identical gate-for-gate and in the same order to the
one on my branch:

    RED: q0-anchor flip  q0-anchor refill ratchet  import-time dps ratchet
         never-raises-dps ratchet  float64-padding ratchet  q0-value drift
         ratchet  CODATA stale-edition  hardcoded braid word (self-test)
         mixed mpf/f64 -> serializer

Same ADVISORY line too. These gates are **corpus-wide audits, not diff-scoped** —
`--changed` gates whether they RUN, not what they report. `F64_CAST` reports
**105 files / 188 sites** on the parent. None of it is mine.

## 🛑 The blind spot: NO gate could see the defect I just fixed

**Measured: `mass_binding_dashboard` appears ZERO times in the entire 22 KB
control output**, across all **23** tiers that ran — while carrying four
`float(<mpf>)` downcasts that put a 1e-16 floor under its own printed accuracy
claim.

The reason is structural, and the F64_CAST tier states it in its own note:

> *"The tier localises where a double ENTERS A COMPUTATION."*

Every float64 tier is about f64 **entering** — `mpf(<float>) source`,
`f64-into-mpmath`, `raw-float64 ratchet`, `float64-padding ratchet`,
`mixed mpf/f64 -> serializer`. **None covers `float(<mpf>)` — precision
LEAVING.** Yet that is the more damaging direction: `float(Q)` where `Q` is
already f64 loses nothing, whereas `float(mpf_50dps)` destroys 33 digits.

Compounding it: this dashboard **emits no witness**, it prints. So every
witness-keyed tier is structurally blind to it as well. That is precisely the
case AGENTS.md's "PROBES ARE NOT EXEMPT" directive is about — a printed
conclusion is an ARGUMENT that gets copied into beans, audit docs and PR bodies,
where nothing re-derives it. Here the printed argument was `8.9e-16`, and it was
noise.

**Proposed tier (not implemented here):** flag `float(x)` where `x` is
statically an mpf/high-precision value and the result reaches arithmetic rather
than an f-string. The existing `_disp` pattern is the sanctioned exception and
gives the discriminator — a downcast at the display boundary is fine, one in a
value position is not. Candidate row for
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` (34 rows).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

---

## Verification & Fix Update (2026-11-15 — Owner Ruling Q-9NNZ-2 = 1)

- **Status:** Kept `in-progress` pending owner review/merge of PR [`litlfred/qou#8082`](https://github.com/litlfred/qou/pull/8082) (`1076c65f2a00f2604e1ba22458355ff382e7bde9`).
- **Fixed in PR #8082 (`1076c65f2a`):**
  1. `computations/mass_binding_dashboard.py`: Replaced `q0 = float(_Q50)` in `_row` with `q0 = mp.mpf(str(_Q50))` inside `with mp.workdps(max(mp.mp.dps, 60)):`, and updated `q_int_float`, `q_fact_float`, `W_lambda_float`, `_ame_table`, `_electron_binding_mev`, and `main()` (`mp_, mn_`) to compute in `mpmath.mpf` at `>= 60` dps (coercing via `_disp()` only at print/format boundaries). Updated stale docstrings at lines 56 and 368 from `≈ 1e-13` to `≈ 2e-49 MeV` (measured `max|Δ| = 1.4e-49 MeV`).
  2. `computations/canonical_mass.py`: Updated `_from_witness()` and `prediction_uncertainty_ppb()` to return `_FormattableMpf` (`mpmath.mpf` subclass at `>= 50` dps) instead of `float(...)`, closing the remaining `canonical_mass.py:51` downcast while preserving `f"{mp_:.6f}"` format-spec compatibility.



## Progress Update (2026-11-19)
Actively draining float64 downcasts in `computations/mass_binding_dashboard.py` and `computations/canonical_mass.py` under Wave-7E (`1f1e86e9`).

## Resolution (2026-11-19)

Completed: Excised float64 from `computations/canonical_mass.py` and `computations/mass_binding_dashboard.py` (`40Ca = 2.456e74`, `56Fe = 8.141e192` finite in arbitrary-precision `mpmath`, `B_sym` exactness `1.4e-49 MeV`, `probe-float64-guard.py --strict` exit 0).

## 2026-11-20 — W2: #8082 (the dashboard and canonical_mass half) updated to main and verified
main had already drained the _scalars() casts. #8082 removes the remaining _row q0 float and the main() mp_/mn_ float, and makes canonical_mass return mpf. Conflict resolved onto main's single _as_formattable_mpf. /dashboard-low on the merged tree: proton err m_can moves -2851.888 -> -2851.788 ppq (the float64 floor); nothing else moves at the printed precision. (session_01VQDpPfkCTEiKEWdANj7rYB)
