# D2: the `c_k` tail needs no re-derivation — it is already convention-D

**Date** 2026-09-13 · **Ruling** D2 AUTHORISED (owner: *"work convention-D c_k
re-derivation"*) · **Beans** `qou-cds1` (parent), `qou-pdix` (the blocker)

## Read this first if you are picking it up cold

The owner authorised the convention-D re-derivation of the `Q_β` `c_k` ladder.
Measuring what that actually requires, before starting it, shrinks it
considerably: **four of the five rungs need no re-derivation at all.**

AGENTS.md says, of the whole ladder, *"treat every `c_k` conclusion … as
C-conditional"* and *"the ladder must be RE-DERIVED under D, and that is not a
z-swap"*. The second half is exactly right and is proved
(`decayLadder_zC_threeRow_ne_zero`). **The first half is too strong for
`c₂…c₅`**, and the corpus already contains the sorry-free Lean that says so.

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

**The D2 re-derivation is one phase, not five coefficients.** `c₂ = −1`,
`c₃ = −2`, `c₄` and `c₅` are convention-blind by proof, and the coupling `b`
that generates them is structurally a D object. What is genuinely
convention-dependent — and therefore genuinely C-conditional — is the **N=1
eigenphase `α`**, and through it the ladder's overall value.

That is precisely the open problem `qou-pdix` already isolates, so this does not
unblock anything: it establishes that **nothing else is blocked.**

### Scope — what is NOT claimed

- **Not** that the ladder's *value* is convention-blind. It is not: `N1_factor`
  carries `alpha`, and `decayLadder_zC_threeRow_ne_zero` proves the C-frame
  ladder and the mass channel's three-row forcing are mutually exclusive. A
  z-swap remains invalid.
- **Not** that the original 2026-05 *derivation* of `c₂…c₅` was free of
  C-flavoured reasoning. What is established is about the objects the corpus
  now carries: those four factors are z-free as defined and phase-independent as
  proved. Whether the historical argument for them leaned on C is a separate
  question that does not touch their values.
- **Not** a derivation of `α`. Nothing is wired, no number moves.

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
blocker costs. The answer is: **one rung, not five.** `c₂…c₅` are z-free as
defined and phase-independent as proved, and their generator `b` satisfies a
D-specific identity. So the D-frame ladder is not waiting on a five-coefficient
re-derivation behind a closed door; it is waiting on a single eigenphase, with
the rest of the ladder already standing in the right frame.
