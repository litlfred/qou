# The deuteron deficit does not price q₀ — the gate closes one route, not the front

**Date:** 2026-08-30 · **Branch:** `claude/deuteron-deficit-off-gate-2026-08-30` ·
**Bean:** `qou-edt7` · **Axis:** extensive-term / body-order cumulants ·
**Tier:** scope correction + two proved parameter-free bounds. **Derives no magnitude.**

## 0. BLUF

Bean `qou-edt7` established today that `b₃ = 3 × (the deuteron deficit)` exactly, and
[`framework_near_unitary_channel_probe.py`](../../computations/probes/framework_near_unitary_channel_probe.py)
(#6197) then found the framework's degenerate point — the Hecke splitting
`h = q − 1/q` vanishes at `q = 1` — and concluded that the deuteron-deficit route

> terminates at the q₀ gate rather than at a wall in the mathematics.

**That is correct for the route it tested and does not generalise to the front.**
Three different things are being called "the q₀ gate":

| | what it is | status |
|---|---|---|
| **G1** | deriving `q₀`'s **value** from the substrate | **FORBIDDEN** — owner ruling 2026-08-02, bean `qou-eic1`, permanent |
| **G2** | deriving a function `F` and **evaluating** it at the calibrated `q₀` | **routine** — what every framework prediction does (`m_p/m_e`, `m_K/m_π`, `Q_β`) |
| **G3** | explaining **why** `q₀` sits near 1 | **G1 in disguise**, correctly gated |

The near-unitarity route needs **G3**, because *nearness* is a claim about `q₀`'s
value. The **deficit** needs only **G2**. So the front is an ordinary open
derivation problem, not a gated one, and it should not be recorded as closed.

Two parameter-free results were proved along the way, and one framing of my own was
retracted before anything was built on it.

## 1. The target is q-free

Every quantity a deficit derivation must hit — `b₂`, `b₃`, `b₄`, `w(1..3)`, the
deficit fraction, `B(4)/B(2)` — is a function of AME2020 alone. The probe reads and
prints `q₀` at the top and uses it **nowhere** below; that absence is the test, made
visible in the output rather than asserted. The gate cannot bind the target. It can
only bind a candidate *mechanism*, and it binds exactly one: the one that asks why
`q₀` is near 1.

## 2. The cumulant signs alone put the turnover at `A ≥ 4`

[`QOU.Mass.CoordinationWeightDifferences`](../../content/quantum-observable-universe/lean/QOU/Mass/CoordinationWeightDifferences.lean)
writes `bind w A = C(A,2)·w(A−1)`, giving `b₃ = 3·Δw(1)` and `b₄ = 6·Δ²w(1)`. It
proves the two first-order readings — `b₃ > 0 ↔ w(1) < w(2)` and
`b₄ > 0 ↔ Δw(1) < Δw(2)` — and stops. Composing them is one step:

> **`b₃ > 0 ∧ b₄ > 0 ⟹ w(1) < w(2) < w(3)`**

so the coordination weight rises **through** `z = 3` and the turnover is at `A ≥ 4`.
[`QOU.Mass.CumulantTurnoverLowerBound.max_at_three`](../../content/quantum-observable-universe/lean/QOU/Mass/CumulantTurnoverLowerBound.lean),
sorry-free, `lean`-direct exit 0, `#print axioms` clean.

**Why it is worth stating separately.** The corpus already locates the turnover at
`A = 4` by a completely different route: Wigner SU(4)'s `[1ⁿ]` has `dim = C(4,n)`,
which **vanishes** for `n ≥ 5`, so the maximally-symmetric regime ends at `A = 4`
(`QOU.Mass.AntisymmetricCasimirIsTwoBody`, `QOU.Mass.SU4CasimirIsAffineInPairCount`).
That is a **support** bound and it is an **upper** bound on where the peak can sit.
The bound here is a **lower** bound, from measured cumulant signs with no
representation theory in it at all. Different inputs, opposite directions, meeting at
`A = 4`. **Neither alone pins the location; together they do.**

Measured, both conventions:

| | `b₂` | `b₃` | `b₄` | `w(1)` | `w(2)` | `w(3)` | `w(5)` |
|---|---|---|---|---|---|---|---|
| isospin average | 2.2245662 | 1.42622016 | 9.24338456 | 2.2245662 | 2.69997292 | 4.715943733 | 2.13293248 |
| ³H Coulomb-corrected | 2.2245662 | 1.80809760 | 7.71587480 | 2.2245662 | 2.8272654 | 4.715943733 | 2.13293248 |

`w(1) < w(2) < w(3)` and `w(3) > w(5)` under both.

## 3. The absent channel carries at least the whole deficit

Every mechanism the arc has closed is *saturating*, hence **non-increasing** in the
`w` coordinate — which is exactly why each lands at `b₃ ≤ 0`
(`UniformBondSimpleGraphExclusion`, `CoordinationSaturation`,
`SU4CasimirIsAffineInPairCount`). Split `w = u + v` with `u` that background and `v`
a channel *absent* at coordination one, `v(1) = 0`. Then

> **`b₃ ≤ 3·v(2)`**, i.e. `v(2) ≥ b₃/3`

(`CumulantTurnoverLowerBound.b3_le_three_mul_channel`, with
`channel_pos_of_b3_pos`). Measured:

| convention | `v(2)` lower bound | as a fraction of `w(1)` |
|---|---|---|
| isospin average | ≥ 0.47540672 MeV/pair | 21.3708 % |
| ³H Coulomb-corrected | ≥ 0.60269920 MeV/pair | 27.0929 % |

So the missing channel is **not a perturbative correction** sitting on a background
that nearly works. The deficit is an **absence** at `z = 1`, not a suppression of
something the background already supplies.

## 4. The target is known to ~21 %, and that is a property of the target

Of the four fingerprint coordinates, **exactly one is convention-independent** — and
it is the one that never touches `A = 3`, which is where the deficit lives:

| coordinate | isospin average | Coulomb-corrected | spread |
|---|---|---|---|
| `b₃/b₂` | 0.641122822 | 0.812786601 | 26.775 % |
| `b₄/b₂` | 4.15514025 | 3.46848514 | 19.797 % |
| deficit fraction | 0.176078329 | 0.213173903 | **21.068 %** |
| `f(4) = B(4)/B(2)` | 12.7196315 | 12.7196315 | **0.0 %** |

**Consequence.** No derivation of the deficit can be *validated* better than ~21 %
until the `A = 3` convention is settled — a Coulomb correction on ³He, and its own
shift on ⁴He. A single-number near-match against the deficit fraction is therefore
uninformative **by construction**.

This is the measured reason #6197 was right to refuse `h = 0.2090603` (1.93 % from
the ³H deficit fraction) as evidence — but the reason is stronger than the one given
there, and it is stronger in a useful way. #6197 argued from *candidate density*: 3
of 8 framework small parameters land inside the band, so a hit is not discriminating.
That is true and is an argument about the candidates. The argument here is about the
**target**: the band exists because the quantity itself is only defined to 21 %, so
*no* candidate can be discriminated against it, however sparse the candidate set. The
first argument would be answered by finding a sparser candidate family; the second
would not.

**And it names the observation that would change the situation.** Settle the `A = 3`
convention and the target narrows from ~21 % to the few-percent level, at which point
a zero-parameter candidate becomes testable. That is the cheapest thing anyone could
do to make this front decidable, and it is not a derivation — it is a data-convention
question.

## 5. A retraction of my own

Mid-session I framed this front as: *`H₂(q)` is commutative for every `q`
(`TrefoilSurfaceStateSum.commutator_zero`), so a binding channel supported on the
non-commutative part of `H_A(q)` vanishes identically at `A = 2`, q-independently —
giving the deficit's location off-gate.* The shape was right and the **type was
wrong**; it is **withdrawn**, and nothing in this branch is built on it.

The deuteron's mass/binding-frame braid word is the **3A-strand** word
(`mass_at_3A_proper.atom_braid_word_3A(1,1)`), so `A = 2` sits in **`H₆(q)`, which is
non-abelian** — see
[`docs/audits/2026-08-21-deuteron-two-adjudications-reconciled.md`](2026-08-21-deuteron-two-adjudications-reconciled.md)
and its reproduction script
[`deuteron_frame_arity_reconciliation.py`](../../computations/probes/deuteron_frame_arity_reconciliation.py),
whose finding 3 records that frame 1 does **not** descend to the coordination frame.
`H₂(q)` commutativity is a **knot-level** fact about the 2-strand trefoil, and the
2026-08-02 audit that states it says so itself, naming *"the non-abelian H₆ interface
braid"* as where a deuteron commutator charge would have to live.

Recorded because the failure mode is the arc's recurring one — right structure, wrong
type — the same error as the SU(4) Casimir lead (a two-body object proposed for a
three-body role) and the Milnor `μ̄` lead (a normalised invariant proposed to carry a
magnitude). The guard that caught it was the corpus's own arity reconciliation, i.e.
corpus-grep path 3.

## 6. Scope

**Derives no magnitude. Proposes no functional.** The `qou-edt7` constraint list
stands unchanged, and the magnitude gate is untouched. What changed:

- the front is **re-opened** — it terminates at an open derivation, not at the ruling;
- the turnover location is now **pinned from both sides**, parameter-free;
- the missing channel has a **proved lower bound** equal to the whole deficit;
- any future candidate is known to be testable only to ~21 % until the `A = 3`
  convention is settled, which is a cheap and concrete next step.

## 7. Verification

CI auto-triggers are disabled repo-wide, so the agent's own verification is the gate.

| what | evidence |
|---|---|
| Lean | `lean`-direct **exit 0** on `QOU/Mass/CumulantTurnoverLowerBound.lean` (empty log) |
| axioms | all 6 declarations `[propext, Classical.choice, Quot.sound]` — no `sorryAx` |
| probe | `deuteron_deficit_off_gate_probe.py` **exit 0**, 6/6 assertions, mpmath 65 dps, `q = +Q_MP` (never `mpf(str(Q))`) |
| precision gates | `scripts/precision-gates.sh --changed` exit 1 on the **six REDs pre-existing on `main`**; **`NEW dirty witnesses: 0`, `OVER baseline: 0`**, and this branch's file appears in none of the three NEW lists |

Two environment notes for the next agent, both of which cost a cycle here:

- `QOU/Mass/CoordinationWeightDifferences.olean` is **absent** from the restored
  `lake-cache` (it landed on `main` today, after the snapshot). Build it into a
  scratch directory with `lean -o` (2.5 s) and put that directory first on
  `LEAN_PATH`. Do **not** run `lake` — it treats the restored oleans as untraced,
  rebuilds from source and evicts the restore (bean `qou-r13s`).
- `Mathlib/Tactic/Omega.olean` is **not in the restored cache** either, though
  `IntervalCases` and `Linarith` are. An `omega` call will fail at import.

The gate run regenerated four audit witnesses whose committed copies are stale on
`main`. The movement was checked and is main's, not this branch's — this branch
contributes two clean rows (`"detail": ""`, `"missing_fields": []`) — so they were
**reverted** rather than folded into a research PR as an unrelated sweep.
