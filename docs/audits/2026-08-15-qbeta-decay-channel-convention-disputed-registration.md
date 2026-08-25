# The Q_β decay channel's trace convention — settled as genuinely DISPUTED, with the boundary proved

**Date:** 2026-08-15 · **Bean:** [`qou-b3nk`](../../.beans/qou-b3nk--qbeta-channel-unregistered-in-trace-convention-reg.md) (HIGH) ·
**Branch:** `claude/qbeta-channel-convention-2026-08-15` ·
**Trigger:** the merged validity audit
[`2026-08-15-c3-refutation-chain-convention-validity-audit.md`](2026-08-15-c3-refutation-chain-convention-validity-audit.md)
found the Q_β channel unregistered in
[`trace-convention-registry.json`](../coordination/trace-convention-registry.json)
while its ladder consumes the convention-C Markov parameter end-to-end. ·
**Lean:** [`QOU/QBeta/MarkovZFullBarCondition.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean)
(5 declarations, sorry-free, `lean`-direct exit 0, `#print axioms` =
`[propext, (Classical.choice,) Quot.sound]`) ·
**Probe:** [`qbeta_decay_channel_convention_status_probe.py`](../../computations/qbeta/qbeta_decay_channel_convention_status_probe.py)
(witness [`qbeta-decay-channel-convention-status.witness.json`](../../computations/qbeta/qbeta-decay-channel-convention-status.witness.json),
18/18, proton pin, 65 dps).

## Verdict up front — outcome (c) of the bean, leaning (b)

**Neither convention is DERIVED for the decay channel. The channel is
registered `disputed`** (`channels.qbeta-decay`: definitional `null`
(contradictory), production `C`, open_item = this bean + this audit), **and the
boundary between the two honest settlement routes is now a proved
dichotomy**, not an observation:

- **`decayLadder_zC_threeRow_ne_zero` (sorry-free):** any faithful normalised
  Markov trace on `H₃(q)` whose Ocneanu parameter is the ladder's
  `z_C = 1/(√q + 1/√q)` carries `y_(1³) ≠ 0` — it does not factor through
  Temperley–Lieb, for **every** substrate `s = √q > 1` (the coincidence locus
  `s⁷ + s⁵ = s⁴ + 1` factors as `(s−1)(s⁶+s⁵+2s⁴+s³+s²+s+1)` and is empty
  there). So *"keep the C-frame ladder"* and *"the mass channel's two-row
  forcing applies to the decay channel"* are **mutually exclusive**. The
  forcing cannot transfer by a z-swap; if the decay decomposition kills the
  third row, the decay trace is `z_D` and the existing ladder is *not that
  trace*.

The whole `c_k` ladder therefore remains **convention-C-conditional** exactly
as the validity audit stated, and every `c₃` / `S` / `q*_S` quote must name
its convention (registry rule).

## 1. Why C is not derived

1. **The stipulation is dangling.** The decay blocks write
   `z = 1/(√q + 1/√q)` in their own prose and name it *"the Markov–Jones
   parameter (Hecke–Skein normalization)"*
   ([`beta-decay-transfer-matrix-proof.md` line 73](../../content/quantum-observable-universe/mass-theory/beta-decay-transfer-matrix-proof.md),
   [`hoefsmit-V21-cos-symmetrization.md` line 22](../../content/quantum-observable-universe/mass-theory/hoefsmit-V21-cos-symmetrization.md)).
   Since the 2026-08-09 owner ruling, the corpus's definition of that referent
   ([`markov-axioms-primitive.md` line 5](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md))
   reads `z = q³/(q²+1)` — **convention D**. The written value and the named
   referent disagree; that intra-corpus contradiction is why the registry's
   definitional field is `null`, and why the channel is `disputed` rather than
   "agreed on C".
2. **The `y_(1³) ≠ 0` escape was cited with the wrong witness — corrected
   here, conclusion intact.** The validity audit (and the bean) cited the
   explicit weight instance `y = (z, 1/2−z, z)` of
   [`prf:qbeta-canonical-markov-weights-explicit-instance`](../../content/quantum-observable-universe/mass-endomorphism/qbeta-canonical-markov-weights-explicit-instance.md)
   as evidence the β channel "genuinely uses the third row". That instance
   inhabits a class (`CanonicalMarkovWeightsH3`) whose **only axiom is
   normalisation**; it is **not an Ocneanu z-trace at `z_C`** — its `σ₀`
   functional value is `h/2` exactly, *independently of `z`* (sympy exact;
   gap to `z_C` at `q₀` is 0.3948). The correct escape witness is the
   convention itself: the C Ocneanu solve at `q₀` has
   `y_(1³) = 0.02274494… ≠ 0` (probe, matching the registry to ≤ 1e-40), and
   the Lean brick makes it unconditional in `s > 1`. Same conclusion — C
   carries the third row — with a witness that survives scrutiny.
3. **Two structural strikes, each conditional on a named premise:**
   - **Full-bar condition.** Markov axiom M3 contains `σ_n`, which the bar
     involution inverts; a trace commuting with the full bar involution needs
     `bar(z) = z − h`. **D satisfies it exactly** — now Lean-proved,
     `zD_full_bar_covariant` (both sides are `1/(q³+q)`) — and the whole
     integer-rank fibre family `z_N = q^N/[N]_q` satisfies it symbolically
     (sympy witness
     [`markov-z-full-bar-condition.witness.json`](../../computations/markov-z-full-bar-condition.witness.json),
     2026-08-08). **A bar-even `z` — C's defining property, KC13 — satisfies
     it only at `q² = 1`** (`barEven_fullBar_forces_classical`,
     `zC_fails_fullBar`). *Premise:* trace bar-compatibility
     `tr∘bar = bar∘tr` — the standard Ocneanu-trace property, and what the
     decay channel's own bar-parity bookkeeping (KC13/KC18/KC19 splits) reads
     into the algebra — asserted context, **not** proved.
   - **Fibre integrality.** `N_eff(z_C, q₀) = 2.5995…`, and the inversion is
     `q`-dependent — `z_C` is the categorical trace on **no fixed-rank
     fibre** (probe here; symbolic `q`-dependence in the full-bar witness;
     mechanism Lean-proved in `FibreDimensionForcesTL`). *Premise:* the decay
     trace is a categorical fibre trace.

   Neither premise is derived for the decay channel, so both strikes are
   **scope-(a) narrowings, not exclusions**. But they mean C's survival
   requires the decay trace to be *neither* bar-compatible *nor* a fibre
   trace — an increasingly narrow corner that itself has no corpus support.

## 2. Why D is not derived either

1. **The mass forcing's premise is absent.** The mass channel's argument runs
   fibre → row cap `ℓ(λ) ≤ 2` → `y_(1³) = 0` → D
   ([`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md)),
   with the row cap supplied by `lem:feynman-eigenbasis-decomposition` — a
   *mass-chapter* block. **No decay analogue exists** (corpus-grep:
   `docs/audits/`, `content/`, `computations/`, coordination ledgers — no
   block derives the decay channel's fibre or decomposition; the Hoefsmit
   boxed decomposition in `hoefsmit-V21-cos-symmetrization.md` is the generic
   full-`H₃` Wedderburn expansion, not a fibre derivation).
2. **The conditional routes to D, premises named:**
   - `conj:binding-qbeta-complex-volume` /
     [`categorical-mass-markov.md`](../../content/quantum-observable-universe/mass-endomorphism/categorical-mass-markov.md):
     `𝔔_β = Im 𝔙` is the bar-odd component of the **same** Markov-trace
     object whose bar-even part is mass/binding. If that identification
     holds, the decay channel inherits the mass trace = D. *Premise: an
     unproved conjecture.*
   - Trace bar-compatibility (above) plus the full-bar condition pins the
     `z` to the fibre family; the family member is then fixed by the fibre
     rank — which is itself underived for the decay channel.
3. **A z-swap is not a migration.** Measured (sensitivity probe, 9/9):
   re-extraction under D gives `c₃ ≈ −974`, implied `c₂ ≈ −9.30`, and the
   ladder's rung convergence collapses (N2/N1 residual ratio 0.017 → 0.89).
   Adopting D means **re-deriving the ladder from the D-trace**, an open
   derivation, not an edit. (Anti-fit note: the convergence collapse is *not*
   evidence for C — the ladder was built in the C frame, so its convergence
   there is provenance, exactly as the bean's guardrail says.)

## 3. What was proved (formalize-first deliverable)

[`QOU/QBeta/MarkovZFullBarCondition.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean) — sorry-free:

| Declaration | Statement | Base ring |
|---|---|---|
| `zD_full_bar_covariant` | `bar(z_D) = z_D − h`, division-free | `CommRing` |
| `barEven_fullBar_forces_classical` | bar-even `z` + full-bar condition ⟹ `q² = 1` | `CommRing` |
| `zC_fails_fullBar` | `z_C` fails the full-bar condition for `s > 1` | ordered field |
| `decayLadder_zC_not_jones` | `z_C·[2]_q ≠ q²` for `s > 1` (locus `(s−1)(s⁶+s⁵+2s⁴+s³+s²+s+1)`) | ordered field |
| `decayLadder_zC_threeRow_ne_zero` | any faithful normalised Markov trace at `z_C` has `y_(1³) ≠ 0` | ordered field |

The last composes with `QOU.BraidsAndKnots.threeRow_ne_zero_of_ocneanu_ne`
(existing, sorry-free). The full-bar condition had been recorded in prose
(`MarkovTraceOnH3A`: "a condition this class has no field for", PR #4834
discussion) and in sympy; it is now in Lean. Per
"conditional-proved ≠ premise-established": these prove z-level algebra and
the mutual-exclusivity implication — **not** the trace-level premises.

## 4. What settling would take (the two honest routes)

1. **Derive the decay fibre.** The decision object remains the decay
   channel's `H₃` decomposition. If it kills the third row (e.g. because the
   same-object conjecture holds and the decay trace *is* the mass trace):
   **D**, and the entire ladder (`c₂ = −1` included) is re-derived from the
   D-trace; the C-frame value record is then superseded, kept as the C-frame
   history it is. If it provably needs the third row (e.g. a derived
   three-row decay decomposition): C's *shape* survives, but its specific
   `z_C` still needs a derivation — third-row presence alone leaves `z` a
   one-parameter family (`threeRow_ne_zero_of_ocneanu_ne` constrains away
   only `z_D`; it does not select `z_C`).
2. **Prove or refute the premises** behind the conditional-D routes:
   `conj:binding-qbeta-complex-volume`, or bar-compatibility of the decay
   trace. Either result collapses the dispute in D's favour or eliminates
   the main pressure on C.

Until one lands, the registry's rule governs: **convention-silent trace
values are not comparable** — and the `qbeta_utils.markov_parameter` R9
evaluator entry now asserts the C-state mechanically, so a silent z-swap
under the ladder (which breaks it) is caught by the validator.

## 5. Artifacts

- Registry: `channels.qbeta-decay` (disputed) + `evaluators.z` tripwire —
  validator PASS, 0 errors (`qbeta_utils.markov_parameter: CONFIRMED
  convention C by evaluation, |d| = 1.945e-51`).
- Lean: 5 sorry-free declarations (above).
- Probe: 18/18, proton pin, no muon cache.
- Ledger row: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- ck-dk registry §9g addendum:
  [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md).
- Bean `qou-b3nk`: in-progress, note appended (closing is a human action).
