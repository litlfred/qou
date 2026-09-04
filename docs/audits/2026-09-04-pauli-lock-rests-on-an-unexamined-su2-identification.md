# The Pauli-lock degeneracy rests on identifying two SU(2)s of different origin — and one of them is unconstructed

**Date:** 2026-09-04
**Branch:** `claude/spin-is-not-the-residue-2026-09-04`
**Bean:** `qou-brng`, arc `bk-crossing-mass-binding`
**Status:** scope statement on an existing sorry-free theorem, plus two staleness
findings met on the way. **No new compute, no new claim, no fit.**

---

## VERDICT (one line)

**`separable_interface_degenerate` — the theorem that closes the two-nucleon channel
asymmetry via the Pauli lock — holds under a hypothesis equating the projector scalars
of the corpus's spin `SU(2)` and its isospin `SU(2)`. Those are two different entries in
the corpus's own duality taxonomy with different categorical origins, and the
identification has never been examined. It is not currently decidable either way:
**D9 (isospin) is unconstructed** — no instance, and the library file its stub advertises
does not exist — while **D10 (spin) is constructed but supplies a map to rotations, not
projector scalars.** So the closure is real and conditional, and its condition is the
D9/D10 cluster the duality tracker already calls the bottleneck.**

---

## How this arose

PR #6553 retracted a claim that spin was the open route past the channel degeneracy. It
is not: in the S-wave, Pauli locks spin to isospin (`S=1 ⟺ T=0`, `S=0 ⟺ T=1`), and
`QOU.QBeta.InterfaceScalar.separable_interface_degenerate` (sorry-free) proves a
separable interface degenerate on the two np channels *for every space index*. That
retraction named the theorem's own hypothesis as the residue. This note measures what
the hypothesis asserts and whether the corpus can currently settle it.

## What the hypothesis says

```lean
theorem separable_interface_degenerate
    (fSpin : Sp → R) (fIso : Is → R) (fSpace : Sp3 → R)
    (s1 s0 : Sp) (t1 t0 : Is) (ell : Sp3)
    (hplus : fSpin s1 = fIso t1) (hminus : fSpin s0 = fIso t0) :
    fSpin s1 * fIso t0 * fSpace ell = fSpin s0 * fIso t1 * fSpace ell
```

The abstract typing is not the issue. What matters is what the docstring says the
hypotheses *mean* — *"the **same** two projector scalars `μ₊`, `μ₋` appear in each
`SU(2)` with the roles exchanged"* — and what those scalars concretely are: the **Hecke
spectral projector weights of a single `σ`**, `μ± = y_(2), y_(1,1)`
([`2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`](2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md);
`InterfaceScalar.markov_param_determined`, `weight_eq_proj_scalar`).

So concretely: **one `σ`, hence one pair of projector scalars, serving two `SU(2)`s.**
`hplus`/`hminus` assert that this is legitimate.

## Why that is a substantive assertion

The corpus does not treat spin and isospin as one symmetry. They are separate rows of
[`docs/duality-tracker.md`](../duality-tracker.md) with different constructions:

| | duality | origin in this framework |
|---|---|---|
| **D9** | Isospin `SU(2)_I` | flavour swap `u ↔ d` between proton/neutron colour-sheet flavour triples (the canonical bowtie) |
| **D10** | Spin `SU(2)_S` | `SU(2)` on colour-sheet rotation, via `S₅ → A₅ ≅ I ⊂ SO(3)` |

A flavour permutation and an icosahedral rotation subgroup are not the same
construction, and nothing obliges two `SU(2)`s of such different origin to be
represented by the same pair of scalars. The identification is a claim about this
framework, and it is what the degeneracy rests on.

## Can the corpus settle it? Measured, and the two sides differ

**D9 — unconstructed.** `class IsospinFromCanonicalBowtie`
(`mass-theory/isospin-from-canonical-bowtie.lean:26`) has **no instance** anywhere; a
corpus-wide grep for an `instance` declaration of it returns nothing, and the only
occurrence of the word in its file is the docstring line *"The class instance is the
**conjectural witness**"*. Corroborated from a third file:
`WignerSU4FromSpinIsospin.lean:4` reads *"Once SpinFromSO3Fiber and
IsospinFromCanonicalBowtie are formalized…"*. This matches the tracker's own note that
**D9 is the bottleneck**.

**D10 — constructed, but not with what this hypothesis needs.** Here my first draft of
this note was wrong and is corrected rather than quietly fixed. D10's vehicle is
`BringFiberAction` (`S5SO3FiberAction.lean:214`), and it **does** have an instance:
`bringFiberAction_icosahedral` (`BringFiberActionInstance.lean:85`). It is
content-bearing, not the falsified vacuous version — `irrepToRotation` is the genuine
icosahedral Reeb map `θ_λ = arccos(χ_λ(C₅)/dim_λ)` and `five_distinct_classes` is proved
from the A₅ character table via `reebAngle_inj`.

But what is constructed is a map **A₅ irrep → icosahedral rotation**. That is not a
supply of *projector scalars for the spin channel*, which is what `fSpin` needs to be
compared against `fIso`. The instance's own scope note is explicit that it does not
close the residual `W_λ = d_q²/D²` Plancherel/MTC-matching obligation
(`BeasleyWittenLocalization`). Separately, the D10 *conjecture stub*
`class SpinFromSo3Fiber` (`nuclear-interactions/spin-from-so3-fiber.lean:26`) has no
instance either.

**Net:** the equal-scalars question is not decidable in the corpus today, but the
obstruction is asymmetric — D9 has nothing to compute a scalar from; D10 has a
construction that computes something else.

## Two staleness findings met on the way

1. **`S5SO3FiberAction.lean` says its class is uninhabited; it is not.** Its docstring
   (≈ line 210) reads *"no global instance is provided, so downstream theorems are
   genuinely conditional on it."* `BringFiberActionInstance.lean` states in its own
   header that it **discharges** it, and `s5_so3_fiber_action_unconditional` is named
   for exactly that. A reader taking the class docstring at face value would call a
   result conditional that the corpus has made unconditional. Not fixed here — it is
   outside this branch's scope — but it should be.

2. **Both D9/D10 content stubs advertise library files that do not exist.**
   `isospin-from-canonical-bowtie.lean:8` links
   `../lean/QOU/BraidsAndKnots/IsospinFromCanonicalBowtie.lean` and declares
   `lean.ref = "qou:QOU.BraidsAndKnots.IsospinFromCanonicalBowtie"`; the same shape holds
   for `SpinFromSO3Fiber`. **Neither file exists.** So each `lean.ref` resolves by
   falling back to the co-located sibling (candidate 1 of §0a), which is where the class
   actually lives. It works, but the advertised address is dangling.

## What this changes, and what it does not

**Does not change:** the theorem. `separable_interface_degenerate` is correct and
sorry-free, and its docstring states the hypothesis openly — which is how this was
found. Nothing here is a defect in that file.

**Does not change:** the four closures this arc established. Trace subtraction
(rank `= n`), `μ̄` (selector type), the linking-data class (`lk` is `I₃`), and the
`Δ₃,₃` ceiling of 9 rest on their own arguments and do not route through D9/D10.

**Does change the reading of the fifth.** "The Pauli lock closes the channel asymmetry"
should be stated as: *it closes it **provided** the spin and isospin `SU(2)`s carry the
same projector scalars* — an identification between constructions of different origin,
one of which has no witness. That is materially weaker than the other four and should
not be listed beside them as the same kind of closure.

**Scope.** A **scope statement, not a refutation.** It does **not** claim the two
`SU(2)`s carry different scalars — that is exactly as unestablished as the claim that
they carry the same ones, and asserting it would be the mirror-image error.

## The honest next step

Every route this arc closed asked **which quantum number to attach to the interface** —
a trace functional, a Milnor invariant, a linking number, a spin factor. All four
closed. The hypothesis holding up the fifth is a different kind of question: it asks
**how the interface is constructed** — whether one `σ`'s projector scalars may serve two
symmetries of different origin.

So the useful work is not a sixth invariant. It is D9 — a witness for
`IsospinFromCanonicalBowtie` would, for the first time, make the equal-scalars question
decidable rather than assumed. That is larger than anything in this arc so far and is
already tracked (`docs/duality-tracker.md`, D9; the D9-bottleneck note).

## References

- `content/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean:628` —
  `separable_interface_degenerate` and its hypotheses.
- `content/quantum-observable-universe/lean/QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`
  — closes the non-separable `(S, L)` tensor coupling (#6488).
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean:214`
  — `class BringFiberAction`; the stale "no global instance" docstring.
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BringFiberActionInstance.lean:85`
  — `bringFiberAction_icosahedral`, the content-bearing instance.
- `content/quantum-observable-universe/mass-theory/isospin-from-canonical-bowtie.lean:26`
  — D9, no instance.
- `content/quantum-observable-universe/nuclear-interactions/spin-from-so3-fiber.lean:26`
  — D10 stub, no instance.
- [`docs/duality-tracker.md`](../duality-tracker.md) — D9/D10 rows, D9-bottleneck note.
- [`2026-09-03-two-mubars-selector-vs-magnitude.md`](2026-09-03-two-mubars-selector-vs-magnitude.md)
  — the four closures and the 2026-09-04 correction this continues.
