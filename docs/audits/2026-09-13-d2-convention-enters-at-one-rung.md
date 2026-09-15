# D2: the convention enters the `c_k` ladder at ONE rung — and that is exactly why every rung's *value* stays C-conditional

**Date** 2026-09-13 · **Ruling** D2 AUTHORISED (owner: *"work convention-D c_k
re-derivation"*) · **Beans** `qou-cds1` (parent), `qou-pdix` (the blocker)

## Read this first if you are picking it up cold

The owner authorised the convention-D re-derivation of the `Q_β` `c_k` ladder.
This measures where the convention actually enters, so that whoever does the
re-derivation knows what has to change and what does not.

**The answer is one place.** The Markov parameter reaches the ladder only
through the N=1 eigenphase `α = (z − 1)·h/2`; the four tail factors `N2…N5`
never mention `z`. That much is verifiable on two independent surfaces — the
Lean definitions (below) and the Python extractor — and it means the
re-derivation is *one phase to fix*, not five coefficients to rebuild.

**It does NOT mean four of the rungs are convention-blind.** Every extracted
`c_k` is obtained by dividing the experimental target by a partial product that
*starts* with `N1_factor`, so the single shared entry point propagates into
every rung's value rather than being confined to one. Measured on `main`
(§"What the corpus already measured"): the implied `c₂` moves **−1.0176 → −9.2989**
and `c₃` moves **−2.0693 → −974.43** when the extraction is redone under D.

AGENTS.md says, of the whole ladder, *"treat every `c_k` conclusion … as
C-conditional"* and *"the ladder must be RE-DERIVED under D, and that is not a
z-swap"*. **Both halves are correct as written.** The first draft of this
document claimed the first half was "too strong for `c₂…c₅`"; that was wrong,
and §"Correction" records how.

## The measurement: the Markov parameter enters at exactly one rung

Read at the definitions in
[`QBetaCategoricalPrecisionLadder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean),
not at the docstrings:

```lean
N1_factor q = Real.cos (alpha q - hoefsmitB q * (hbarQ' q)^2 / 2)   -- carries alpha
N2_factor q = 1 - (hoefsmitB q)^2 * (hbarQ' q)^4
N3_factor q = 1 + jonesHopfClassicalLimit * (hoefsmitB q)^3 * (hbarQ' q)^6
N4_factor q = 1 + jonesHopfClassicalLimit * (hoefsmitB q)^4 * (hoefsmitB q)^4 * (hbarQ' q)^8
N5_factor q = 1 + (-(hoefsmitB q)^2 - 1/2) * (hoefsmitB q)^5 * (hbarQ' q)^10
```

`N2…N5` are built from `hoefsmitB` and `hbarQ'` alone. **The Markov parameter
`z` does not appear in any of them.** Only `N1_factor` reads `alpha q`, and
`alpha` is the sole z-dependent input to the ladder.

That is not merely an observation about how the file happens to be written — it
is proved, twice, sorry-free, on `main`:

1. **The tail is phase-independent.**
   `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common`
   ([`LadderConventionLocalisation.lean:69`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/LadderConventionLocalisation.lean))
   — two phases `φ₁`, `φ₂` give ladders differing only in their `cos` factors,
   with `ckTail` common. Proof is `unfold; ring`.

2. **The tail's generator is a convention-D object.**
   `QOU.BraidKnot.hoefsmitB_sq_eq_one_sub_stdWeightD`: **`b² = 1 − y_(2,1)^D`**,
   where `y_(2,1)^D = q²/(q²+1)²` is the D-frame standard-block Wedderburn
   weight. The Lean's own docstring records that this is **D-specific** — under
   C the `H₃(q)` weights carry `√q`, keep `y_(1³) ≠ 0`, and the identity fails.

Verified numerically at the proton pin, `mp.dps = 50`:

```
q₀              = 1.1099785827513808076
hoefsmitB       = 0.86758406696525115565
b²              = 0.75270211325196540159
1 − y_(2,1)^D   = 0.75270211325196540159
|b² − (1−y_D)|  = 2.7e-51
```

and the tail itself (`hbarQ' = (q−1)/q = 1 − 1/q`, confirmed against three Lean
carriers):

```
ckTail = 0.999926215050140186
   N2 = 0.99992745671562   N3 = 0.99999876426366
   N4 = 0.99999999403692   N5 = 0.99999999994385
```

For contrast, the two Markov parameters that do **not** enter it:
`z_C = 0.499320334184`, `z_D = 0.612688037146`.

## What this changes

**The D2 re-derivation is one phase to fix, and five conclusions to
re-establish.** Those are different counts and the distinction is the whole
point of this document:

| object | convention-dependence |
|---|---|
| the **factors** `N2_factor … N5_factor` (Lean definitions) | **none** — no `z`, and `Q_beta_categorical_ofPhase_tail_common` proves the tail is phase-independent |
| the coupling `b` generating them | a **D** object — `b² = 1 − y_(2,1)^D`, which fails under C |
| the **N=1 factor** | carries `α = (z − 1)·h/2` — the sole entry point |
| the **extracted values** `c₂ … c₅`, and every near-match built on them | **C-conditional**, because each divides through `Q_N1` |

So the fix has one target — derive `α` in the D frame — while the *record* that
has to be re-established afterwards is all five rungs plus the near-match
conclusions hanging off them (`c₂ = −1`, `c₃ = −2 = J_Hopf(q=1)`,
`c₃^even = −Vol(4₁)`, `[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`).

`α` is precisely the open problem `qou-pdix` already isolates, so this does not
unblock anything. What it adds is a *bound on the blocker's reach*: the tail's
symbolic content survives the re-derivation intact, so the work is a phase
determination followed by a re-extraction, not a rebuild of the ansatz.

### Scope — what is NOT claimed

- **Not** that the ladder's *value* — or any rung's extracted value — is
  convention-blind. It is not: `N1_factor` carries `alpha`, every extraction
  divides through it, and `decayLadder_zC_threeRow_ne_zero` proves the C-frame
  ladder and the mass channel's three-row forcing are mutually exclusive. A
  z-swap remains invalid.
- **Not** that the original 2026-05 *derivation* of `c₂…c₅` was free of
  C-flavoured reasoning. What is established is about the objects the corpus
  now carries: those four factors are z-free as defined and phase-independent as
  proved. Whether the historical argument for them leaned on C is a separate
  question that does not touch their values.
- **Not** a derivation of `α`. Nothing is wired, no number moves.

## What the corpus already measured — and it says this, not the opposite

**This was on `main` before this document was drafted, and the first draft
missed it.** Three carriers, all predating 2026-09-13:

**1. The producer states the localisation itself.**
[`computations/qbeta/qbeta_utils.py:225`](../../computations/qbeta/qbeta_utils.py)
— *"`z` and `alpha` are the ONLY places a Markov convention enters the entire
`Q_beta` ladder"* — and enforces it: `_ConventionGuardedQuantities._WITHHELD =
("z", "alpha")` raises rather than handing out a convention unnamed. Its error
text already carries the correct conclusion:

> Under D the `c_k` ladder is NOT derived (bean `qou-cds1`): substituting `z_D`
> into `alpha = (z−1)h/2` is proved invalid by
> `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` and
> `QOU.QBeta.eigenphase_bar_defect_of_fullBar`.

The assembly one function down is where the propagation happens:
`Q_N1 = Q_A * mpcos(sub["alpha"] - sub["b"] * sub["hbar_q"]**2 / 2)` — so `Q_N1`
is a factor of every partial product the extractor divides by.

**2. A probe measured the size of it, with a committed witness.**
[`qbeta_c3_ladder_trace_convention_sensitivity_probe.py`](../../computations/qbeta/qbeta_c3_ladder_trace_convention_sensitivity_probe.py),
landed 2026-09-05, witness `computedAt` 2026-08-31, proton pin, 60 dps,
10/10 assertions PASS. From its `result` block:

| quantity | convention C | convention D |
|---|---|---|
| `z(q₀)` | 0.49932033418369445 | 0.61268803714646525 |
| `c₃` (proton) | **−2.069342577115168** | **−974.4318877467484** |
| `c₃` (muon) | −2.019860311874005 | −974.3821470795362 |
| implied `c₂` | **−1.017623798** | **−9.298862871** |
| N2 residual | −1.2785809e-6 | −6.0207045e-4 |
| distance to `−Vol(4₁)` | ~0 | **972.402004534** |

Two of its assertion names are the finding stated flatly:
`implied_c2_is_minus1_in_C_frame_only` and
`h1_volume_proximity_does_not_survive_D_reextraction`. Its docstring §4 names
the same five downstream facts AGENTS.md does — `c₃^even = −Vol(4₁)`,
`[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S` — and concludes each is *"CONDITIONAL ON
CONVENTION C"*.

**3. One pillar is convention-IMMUNE, and it is worth naming**, because it is
the part of the `c₃` record that does *not* need re-establishing: the
cross-anchor **swing**. Measured `swing_D/swing_C = 1.00522`, because its
dominant source (`Q_A(q)` sensitivity over `u³`) is z-free. So the *"REFUTED as
a real-`q` fibre element"* verdict survives the convention change; it is the
**value-level near-matches**, not the refutation, that are C-conditional.

## Correction — how the first draft got this backwards

The draft read the Lean definitions, found no `z` in `N2…N5`, and concluded
*"four of the five rungs need no re-derivation"* and *"AGENTS.md's first half is
too strong for `c₂…c₅`"*. Both sentences are withdrawn.

**The reasoning error** is the definition-versus-value conflation this corpus
warns about in several other places: `N2_factor` is a *symbolic factor* and
`c₂ = −1` is a *near-match conclusion about an extracted number*. They share a
name and are different objects. A shared input that every conclusion divides
through does not localise the dependence — it globalises it, which is the
opposite of what the draft inferred from finding that input in only one place.

**The corpus-grep error** is the more useful one to record. The six-path
checklist was run on the *topic* (`c_k`, convention D, the ladder) and the
Lean carriers; it was not run on the **claim shape** — *"does the corpus already
assert that the `c_k` conclusions survive a convention change?"* — which is the
STRICT §"Grep the claim SHAPE, not only the topic" rule. A grep on
`convention.*sensitivity` or on the five downstream fact names reaches the probe
immediately; both were tried only *after* the draft was written, and both hit on
the first attempt.

**What survives the correction.** The Lean-side reading is sound and is not
redundant: the three carriers above all argue from the *Python extractor*, and
`Q_beta_categorical_ofPhase_tail_common` + `hoefsmitB_sq_eq_one_sub_stdWeightD`
establish the same localisation from the *formalisation*, sorry-free — including
the stronger statement that the tail's generator is structurally a **D** object.
Two independent surfaces agreeing on the entry point is worth having. What is
not worth having is the inference that was drawn from it.

## 🛑 SECOND CORRECTION — on the RULED base, NO phase works. `α` is not the blocker.

**Added 2026-09-14, from a sibling result that landed on `main` while this was in
review.** Everything above about *where the convention enters* stands. The
sentence this document used to close on — *"it is waiting on a single
eigenphase"* — does not.

**The argument.** The ladder's N=2 factor is
`F_N2(α) = cos(α − u/2)·(1 − u²)`. Since `cos ≤ 1`, it is capped at `1 − u²` for
**every real `α`** — the supremum sits at `α = u/2` and is still below 1. What it
must supply is `F_required = Q_codata / Q_base`. Recomputed here independently at
`mp.dps = 70`:

```
cap = 1 − u²  =  0.99992745              (u = 0.008517628778)

  z = 1 (Form A) — RETIRED        Q_base 0.783645827375   F_req 0.998325241673   reachable
  z_D order-zero E₀ — RULED       Q_base 0.444700408522   F_req 1.75923699418    EXCLUDED
  z = q (augmentation)            Q_base 0.87989056126    F_req 0.889125812282   reachable
  dashboard scored cell — RULED   Q_base 0.65185631006    F_req 1.20016236389    EXCLUDED
```

**The two cells a cosine can reach are exactly the two the ruling does not
select.** So no value of `α` unblocks the ladder on the ruled base, and *"blocked
on `qou-pdix`"* was correct only for the retired `z = 1` cell — it did not
survive the 2026-09-08 ruling, and nothing re-checked it at the time.

**What this changes here.** "One phase to derive, five values to re-extract" is
withdrawn as a statement about the *ruled* base. What survives unchanged is the
localisation itself: the convention enters at one place, the tail factors are
`z`-free, and their generator satisfies a D-specific identity. Those are facts
about the ansatz and they hold whatever the base. What was wrong was the
inference that fixing that one place would unblock the ladder.

**The live question is therefore not the phase.** It is *what object supplies a
factor above 1 at all* — a question about the base or the assembly. An agent sent
to derive `α` as **the** `Q_β` L2 blocker is off the critical path.

**Verification.** The bound is established twice, independently and sorry-free,
in `LadderFactorBound.lean` (4 lemmas) and `EigenphaseQuantization.lean`
(base-independent table); both were still open PRs at the time. **Cite the merged
audit, not those PRs:**
[`2026-09-13-formb-probe-adjudication-and-cds1-state.md`](2026-09-13-formb-probe-adjudication-and-cds1-state.md)
§5.1, merged as `f3cb908ee7`, which recomputed all four `F_required` at 70 dps
and inspected the Lean for `sorry`. The four figures above were re-derived here
from scratch and reproduce it exactly.

**Read the section below with that in mind** — it surveys the attacks on `α`, and
`α` is no longer the thing to attack.

## The blocker, for whoever takes `α` next — all four named attacks are now closed

**Re-checked 2026-09-14 against `main` `8b367484ed`, 426 commits after this was
drafted.** The draft said *"surviving attacks are A and C"*. That was already
wrong when written and is thoroughly wrong now: `qou-pdix` grew 1742 → 2408
lines overnight and **every named attack on `α` now carries a measured negative
or is forbidden.**

| attack | live state on `main` |
|---|---|
| **A** Habiro ring / roots of unity | measured; **the recommendation was withdrawn by its own author**. Not circular as the triage claimed (`prop:habiro-precision-ladder-equivalence` has a one-element `uses[]` cone, not downstream of `qou-cds1`) — but `QbetaHabiroTaylorBridgeClass` equates two `opaque … := fun _ => 0` sequences, i.e. a **named hole**, seal verified non-leaking under six tactics. Progress there is *computational*, not deductive. |
| **B** Faddeev modular double | pruned (PR #7252: both loci inversion-invariant, dual carrier 375× too steep), then **measured INERT at the substrate**, inside a derivable z-window |
| **C** Stokes / resurgence | **closed**, by two results already on `main` (PR #7340) |
| **D** two evaluation points | forbidden — a fourth calibration under CAL-1/2/3 |

Route 5's ellipticity target was also found to sit on the **retired `z = 1`
base**, and on the ruled base it **inverts**; the gap there is **139×**, not the
"factor 11.2" first reported. And the retired base has a measured blast radius:
**42 single-base `.py` files, one of them the canonical ladder producer.**

**This does not weaken the finding above — it sharpens why it matters.** With
every route to `α` closed, the useful thing to know is exactly how much the
blocker costs. On the retired `z = 1` cell the answer was **one phase to derive,
five values to re-extract**; on the ruled base no phase suffices at all (see the
second correction above). The *factors* `N2…N5` are z-free as
defined and phase-independent as proved, and their generator `b` satisfies a
D-specific identity. So the D-frame ladder is not waiting on a five-coefficient
re-derivation behind a closed door; it is waiting on a single eigenphase, after
which the ansatz is reusable as it stands and the five *values* are re-extracted
from it. Reusable ansatz, unrecoverable numbers — those are the two halves, and
running them together is what the correction above is about.
