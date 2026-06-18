# Q_β q-Bessel tower vs z-Habiro / binding tower — they SEPARATE (argument- vs order-recurrence); Option-1 resolved

> **Discipline.** Corpus-grep + formalize-first. This doc is a **consolidation of
> already-proven corpus results into one settled verdict**, NOT a new probe run.
> No compute was launched; no production wiring changes. Its value is (a) recording
> that a recurring structural question is *already answered* (so it is not re-opened),
> (b) the argument-vs-order map across three faces of the same q-special function, and
> (c) the one verified coordination gap it closes.

## 0. The question (and why it kept coming back)

A recurring "what next" hypothesis — most recently surfaced as the keystone-tower
Option 1 (2026-06-18) — asks:

> *Are the §4a bar-odd **q-Bessel tower** (Q_β `c_k` ladder) and the **z-Habiro Φ_q
> tower** (mass / binding) the **same** construction? If yes, q-Bessel contiguity ↔
> z-Habiro Cauchy-limit would constrain each other, turning two open problems into
> one shared keystone.*

**Verdict: they are NOT the same construction, and they do NOT cross-constrain.**
The corpus already proves the precise sense in which they separate. The hoped-for
"shared keystone" is the wrong unification; the genuine open keystones are two
*distinct* objects (§4). Pursuing Option-1-as-a-fresh-probe re-treads refuted
ground (the joint lever is a documented NO-GO, §2).

## 1. Shared analytic home — yes (this much is true)

Both ladders live in the **same analytic family**: the Hahn–Exton q-Bessel function,
the matrix coefficient of the quantum motion group `E_q(2)`, reached as the
`SU_q(2) → E_q(2)` **group-contraction limit** (n→∞) of the substrate
(Vaksman–Korogodsky 1989, Koelink 1994; PR #2279). The Q_β block states this
directly — the q-Bessel object "lives in the n→∞ brane-tower (contraction) limit …
**where the binding Δ_λ ladder also lives**"
([`q-beta-c-k-recursion-from-habiro-q-difference.md` §"The q-Bessel identification of F"](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).

So a reader could be forgiven for guessing "same object." The shared *home* is real.
The shared *recurrence* is not.

## 2. The separation — argument recurrence ≠ order recurrence (PROVED / documented)

The decisive pruning is the Stage-C scope §2
([`2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md)),
grounded three independent ways and **distinguished in Lean**:

| | Q_β `c_k` ladder | binding Δ_λ ladder |
|---|---|---|
| recurrence | **argument** q-difference (contiguity) | **order** three-term |
| index | power-series order **k** | order index ν / mass number **A** |
| class | first-order **q-holonomic** | **C-finite** (constant-b) |
| explicit form | `c_{k+1}(1−q^{k+1})(1−a q^k) = −q^k c_k`, `a=q^{ν+1}` | `a(n+2)=b·a(n+1)−a(n)`, `b=q₀¹⁰+q₀⁻¹⁰` |
| Δ_λ shape | — | geometric `Δ_λ(K) ≈ q₀^{10A−5}` |
| Lean | [`QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean) (`qbessel_second_order_recurrence`) | [`QLommelOrderRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QLommelOrderRecurrence.lean) (`two_root_geometric`) |

The C-finite constant-b class is only the `q→1` **degeneration** of the q-holonomic
argument recurrence. Modelling the Q_β `c_k` with the binding ladder's constant `b`
is therefore **"dead on arrival"** (scope §2): seeding `c_2=−1, c_3=−2` gives
`c_4 = b·c_3 − c_2 ≈ −5.38` against the canonical-anchor `c_4 ≈ −0.97` — a ~5.5×
mismatch, on top of the structural argument. The C-finite class was independently
searched and refuted earlier (PR #1839; registry rows C5/C6,
[`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)).

**The natural "they're one object" lever was tested and retired.** The joint
`J_ν ⊕ I_ν` combiner — the most direct way the two would constrain each other — is a
documented **NO-GO**
([`2026-06-14-qbessel-joint-ji-binding-probe.md`](2026-06-14-qbessel-joint-ji-binding-probe.md)):
applied as the binding operator-valued combiner it degrades every data-complete
case (³He +17.4% → +117.9%, a 6.8× regression; the lone ⁴He "improvement" sits on a
volume already flagged wrong). PR #2279's q-Bessel identification is sound *as
mathematics* but is **not load-bearing for the binding frontier** — it stands on its
own merit and does not rescue A≥3 binding.

## 3. Three faces of the q-Pochhammer skeleton — the map

The confusion is that **three** corpus constructions are built on the same
q-Pochhammer `(·;q)_n` skeleton and all gesture at the `E_q(2)` contraction limit,
yet are distinct objects:

1. **z-Habiro brane tower** — the cyclotomic-in-`z` completion of the Faddeev
   quantum dilogarithm `Φ_q(z)=∏_{k≥1}(1−q^{-k}z)^{-1}` at the ideal
   `P_n(q,z)=(zq^{-1};q^{-1})_n`
   ([`def:z-habiro-ring`](../../content/quantum-observable-universe/mass-theory/z-habiro-ring.md),
   [`conj:brane-tower-z-habiro`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md)).
   Open keystone: the analytic↔algebraic identification — which localised Euler
   family `c_n = q^{-n}/∏(1−q^{-j})` has `zHabiroLimit` equal to the analytic `Φ_q`
   (ZHabiroCauchy is sorry-free; the *identification* is the gap), plus `n_⋆`
   (refuted in six forms).
2. **Q_β `c_k` ladder** — the q-Bessel **argument** recurrence; open keystone is the
   fibre-level q-difference **kernel `R(q,ξ)`** in `F(qξ)=R(q,ξ)·F(ξ)`
   (Stage-C scope §1; owner-gated multi-session).
3. **binding Δ_λ ladder** — the q-Lommel **order** recurrence; open frontier is
   Option-E / GAP-A-3 / GAP-A-4 and the ⁴He JSJ volume
   ([`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)).

The Faddeev quantum dilogarithm (face 1) and the Hahn–Exton q-Bessel (faces 2, 3)
share the `(·;q)_n` skeleton and the contraction-limit home, but a quantum
*dilogarithm* is not a q-*Bessel* function, and the argument and order recurrences
of the q-Bessel are themselves distinct. So the three open keystones are the **same
type** of obstruction — "identify the algebraic q-difference data that reproduces a
transcendental q-special function at its poles/zeros" — without being the same
object or cross-constraining each other.

## 4. Consequence — the open keystones are distinct, not one

| was hoped (Option 1) | is true (corpus) |
|---|---|
| one shared keystone | **two distinct** keystones: Q_β kernel `R(q,ξ)` (argument) and binding Option-E (order) |
| q-Bessel contiguity ↔ z-Habiro Cauchy-limit cross-constrain | **no cross-constraint**; joint J⊕I lever refuted (2026-06-14) |
| connecting the two open problems | **cleanly separating** them is the result |

Do **not** open a probe that models the Q_β `c_k` with the binding constant-b order
recurrence, or that re-runs a joint `J_ν ⊕ I_ν` binding combiner — both are closed.

## 5. The one coordination gap this doc closes

Corpus-grep (2026-06-18) confirms the q-Bessel / q-Lommel / contraction structure is
documented on the **Q_β side** (the block above + the whole 2026-06-14 audit cluster
+ the Stage-C scope) but is **absent from the z-Habiro / brane-tower side**:
`grep -n 'q-Bessel|q-Lommel|contraction|E_q|Hahn'` over
`brane-tower-z-habiro.md` → **no matches**. A reader of the brane-tower block has no
pointer to the fact that its binding Δ_λ ladder *is* the q-Lommel order recurrence
(`QLommelOrderRecurrence.lean`), nor to the refuted joint lever. A one-paragraph
cross-reference on the brane-tower block closes this asymmetry (companion commit).

## 6. Cross-references

- [`q-beta-c-k-recursion-from-habiro-q-difference.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md) — §"The q-Bessel identification of F" (the shared-home statement)
- [`2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md) — §2 argument-vs-order pruning (the proof of separation)
- [`2026-06-14-qbessel-joint-ji-binding-probe.md`](2026-06-14-qbessel-joint-ji-binding-probe.md) — the joint J⊕I NO-GO
- [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) — C1–C12 refuted, the open kernel axis
- [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) — per-rung canonical/empirical tiers; C5/C6 constant-kernel refutation
- [`brane-tower-z-habiro.md`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md) / [`z-habiro-ring.md`](../../content/quantum-observable-universe/mass-theory/z-habiro-ring.md) — face 1
- Lean: `QBesselContiguityRecurrence.lean` (argument), `QLommelOrderRecurrence.lean` (order), `ZHabiroCauchy` / `PhiQConvergence` (z-Habiro)
