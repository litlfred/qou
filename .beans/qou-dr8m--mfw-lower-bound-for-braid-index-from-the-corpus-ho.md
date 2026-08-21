---
# qou-dr8m
title: MFW lower bound for braid index from the corpus HOMFLY/Markov trace — settle 6_1 = 4 (flagged load-bearing by qou-xpgq)
status: todo
type: task
created_at: 2026-08-21T15:39:09Z
updated_at: 2026-08-21T15:39:09Z
---


## Framing (corrected after owner pushback — "there IS a filtration and jet")

My first answer — "there's no single algebra for GS to normalize in" — was
WRONG and is retracted. There is one, and this corpus already uses it:

  B_1 ⊂ B_2 ⊂ B_3 ⊂ …  →  B_∞ = colim B_n     (strand filtration)
  H_1 ⊂ H_2 ⊂ …        →  H_∞,  with the Ocneanu/Markov trace defined
                              COMPATIBLY across the tower

Stabilisation `β ↦ βσ_n^{±1}` is *internal* to B_∞, so Markov equivalence does
live inside a single filtered object. The corpus's Bratteli/Wedderburn tower is
exactly this.

**So the obstruction is not the absence of an algebra — it is the KIND of
question.** GS/normal forms answer *"is x = y in this algebra?"* — a canonical
representative of an ELEMENT. Braid index asks for

    min { n : the Markov class of L meets B_n }

i.e. the **minimal strand-filtration degree over an equivalence class**. That is
a minimisation over a class, not a normal form of an element; a confluent
rewriting system gives the latter and says nothing about the former.

**The sharp obstruction is non-monotonicity.** A greedy GS-style reduction would
compute the braid index IF Markov reduction were filtration-NON-INCREASING. It
is not: destabilising can require STABILISING first (going up a strand before
coming down). That is precisely why Birman–Menasco's "Markov Theorem Without
Stabilisation" is a theorem rather than an observation — and its price is a much
richer move set (exchange moves, flypes), not a finite confluent system.

**But the filtration DOES deliver the bound, and that is this bean.** The
Ocneanu trace is filtration-COMPATIBLE, which is exactly what makes HOMFLY
well-defined on the tower — and MFW then gives

    braid index ≥ ½·breadth_v HOMFLY + 1

So the corpus's own Hecke/Markov-trace machinery is the natural route to the
LOWER bound even though GS cannot reach the minimum itself. Task: compute HOMFLY
for 6₁ from the in-repo trace and settle the braid index = 4 that `qou-xpgq`
flagged as literature-recalled and load-bearing for its {5,10} arithmetic.

NOTE — do not conflate filtrations: the corpus's jet-order/Δ_λ filtration is
q-adic, a DIFFERENT filtration from the strand filtration above. MFW rides the
strand one.
CAVEAT: MFW is not always sharp; known counterexamples exist. A matching bound
settles it; a gap does not.

## The formulae, and what the trace bounds ABOVE as well as below

HOMFLY convention: `v⁻¹P(L₊) − v P(L₋) = z P(L₀)`, `P(unknot) = 1`.
For `β ∈ B_n` with exponent sum (writhe) `e` and closure `L`, MFW is a PAIR:

    (1)   e − n + 1  ≤  mindeg_v P_L
    (2)                 maxdeg_v P_L  ≤  e + n − 1

**Subtract → the LOWER bound on the Markov-class minimum (braid index).**
`e` cancels — which is the point, since `e` is not a link invariant:

    maxdeg_v P − mindeg_v P ≤ 2n − 2      ⟹    n ≥ ½·spread_v P + 1
    braid_index(L) = min{n} ≥ ½·spread_v P_L + 1

**Read (1) alone → an UPPER bound on a MAXIMUM.** The self-linking number of
the transverse representative is `sl(β) = e − n`, so (1) is exactly

    sl(β) ≤ mindeg_v P_L − 1        for EVERY β in the Markov class

i.e. the trace bounds the **maximal self-linking number** above — the
HOMFLY sharpening of Bennequin's `sl ≤ 2g(L) − 1`. So the same trace bounds a
min from below and a max from above; they are the two halves of one pair.

**Why there is no "maximum braid index".** The Markov class is unbounded above:
stabilise `β ↦ βσ_n^{±1}` and n grows without limit, closure unchanged. So
`max{n}` = ∞ trivially, and the MINIMUM is the only invariant of the two. That
asymmetry is structural, not an artifact.

**Adding (1)+(2) instead** bounds the writhe at fixed n:
    |mindeg_v P + maxdeg_v P − 2e| ≤ 2n − 2

## Lean: what is provable now vs. what is research-scale

- **MFW itself is research-scale.** Its proof needs HOMFLY well-definedness =
  Markov invariance of the Ocneanu trace on the H_n tower, then a degree
  argument. Not a session-scale formalisation.
- **The derivation FROM the pair is cheap and honest** — the §3b-cond
  conditional pattern: take (1) and (2) as explicit hypotheses on a generic
  ordered field / ℤ, conclude `n ≥ ½(maxdeg − mindeg) + 1` and
  `sl ≤ mindeg − 1`. Sorry-free, no axiom, and it states plainly that MFW is
  assumed, not proved. That is the correct first Lean rung here.
- Do NOT axiomatise MFW as a class and then present the bound as derived —
  §"Axiomatization is NOT a Proof".

## 2026-08-21 — TIER 1 + the Mathlib gap LANDED (sorry-free)

Two files, both `lean`-direct exit 0, zero warnings, axiom-clean (no `sorryAx`):

**`QOU/MathlibExt/BraidGroup.lean` — Mathlib has NO braid groups.** Verified:
no `*braid*` file anywhere in `Mathlib/`; `GroupTheory/` has `Coxeter` but not
the braid group. Built on Mathlib's `PresentedGroup`:
  - `braidRelators n` — the Artin presentation (far commutation + braid relation)
  - `BraidGroup n` — braid group on `n+1` strands, `n` generators on `Fin n`.
    The offset is deliberate: `Fin (n-1)` would use truncated ℕ-subtraction and
    poison every downstream index proof. `strandCount n = n+1` is exported so
    callers never have to recall the convention.
  - **`exponentSum : BraidGroup n →* Multiplicative ℤ` — the WRITHE**, and the
    real content: it descends to the quotient because every Artin relator has
    total exponent sum zero (`lift_const_relators`, axioms [propext, Quot.sound]
    only). The writhe of a braid *word* is trivial; the writhe of a group
    *element* is not, and MFW is a statement about the latter.

**`QOU/Knot/MortonFranksWilliams.lean` — the MFW pair and its consequences.**
`MFWWitness` carries `(n, e, dmin, dmax)` plus the two MFW inequalities AS
HYPOTHESES, and derives:
  - `spread_le_two_mul_sub_two` — subtracting cancels the writhe `e` (the crux:
    `e` is not a link invariant, the degree window is)
  - `braid_bound` — `spread + 2 ≤ 2n`, division-free
  - `no_representative_of_spread_gt` — the contrapositive, the form that rules
    a strand number out
  - `selfLinking_le` — MFW (1) alone bounds `sl = e − n` ABOVE (HOMFLY-Bennequin)
  - `writhe_bounds` — adding them constrains the writhe at fixed n
  - `rep_upward` / `rep_unbounded` — from a `Markov` stabilisation class: the
    representable strand set is upward closed hence UNBOUNDED, so `max` is ∞ for
    every link. **Proves why the braid index is a minimum and never a maximum.**

**Self-correction during the build**: `writhe_bounds` needs `dmin ≤ dmax`,
which I had not assumed. It is true (mindeg ≤ maxdeg for a nonzero HOMFLY) but
is NOT derivable from the MFW pair, so it is now an explicit carried field
rather than quietly assumed.

**Anti-laundering**: `MFWWitness` carries the INPUTS; the bounds are computed.
It is deliberately not a class with `braid index ≥ …` as a field — that would
be §"Axiomatization is NOT a Proof". MFW itself remains UNPROVED here.

## Remaining tiers (honest sizing)

* **T2 — HOMFLY.** Not in Mathlib either. Needs the Ocneanu trace on the Hₙ
  tower and its Markov invariance. The corpus has the trace numerically
  (`pyhecke`) and `QOU/KnotTheory/JonesPolynomial.lean` states Jones as an
  `opaque` Laurent polynomial + conjectural class — the same idiom extends.
  Multi-session.
* **T3 — MFW itself**, i.e. discharging `mfw_lower`/`mfw_upper` rather than
  carrying them. Needs T2 plus the degree argument. Research-scale.
* **T4 — the payoff**: compute HOMFLY(6₁) from the corpus trace, instantiate
  `MFWWitness`, and settle `braid index(6₁) = 4` — currently literature-recalled
  and load-bearing for `qou-xpgq`'s {5,10}. Blocked on T2.
  CAVEAT: MFW is not always sharp. A matching upper bound settles it; a gap
  does not.

## 2026-08-21 — T2 is CHEAPER than I sized it, and one module is broken

Two measured findings while probing the compute route to T4.

**1. `pyhecke.trace` does not import on this container.** It does
`from hecke_core import …` and `from hecke_core_legacy import …`; neither module
exists here. What IS installed and imports fine is **`pyhecke_native`** (the
PyO3 binding). So the trace module's import path is stale relative to the
shipped extension. Anyone reaching for `pyhecke.trace` hits
`ModuleNotFoundError`, not a subtle wrongness. Not fixed here — it is not this
bean's file and the right fix (rename vs shim vs rebuild `hecke_core`) is the
owner's call. `maturin` and `cargo` are both on PATH if a rebuild is wanted.

**2. The characters are ALREADY computable, which shortens T2 a lot.**
`pyhecke_native` exports, among others:

    chi_lambda_braid, chi_lambdas_braid, chi_lambda_braid_mpfr,
    chi_lambdas_braid_mpfr, chi_lambda_matrix, chi_q_atomic

i.e. the irreducible Hecke characters χ_λ evaluated ON A BRAID, in both f64 and
mpfr. Since the Ocneanu trace is a weighted sum of exactly those,

    tr(β) = Σ_λ W_λ(q,z) · χ_λ(β)      ⇒      HOMFLY = (normalisation) · tr(β)

T2 is therefore NOT "formalise/implement the Ocneanu trace from scratch". It is
**assemble HOMFLY from characters that already exist**. Revised sizing:
session-to-multi-session, not research-scale.

**NOT yet verified — do not treat as done:**
  - the Ocneanu weights `W_λ(q,z)` in the corpus's convention;
  - the HOMFLY framing normalisation (the `v^{−w}` writhe correction);
  - which of the C/D trace conventions these χ_λ are in — the 2026-08-15 ruling
    makes D canonical and the corpus is mid-migration, so this MUST be pinned
    before any degree is read off. A wrong convention changes the polynomial.

**Validation gate for T4, fixed in advance**: compute HOMFLY for 4₁ and 5₂
first, whose braid indices (3 and 3) and degree spreads are known, and require
MFW to reproduce them, BEFORE reading 6₁. Same discipline that caught the
overline bug in `qou-6ort` — validate on knots with published answers first.
Note 4₁ and 5₂ both have braid index 3, so they test the machinery but do NOT
test discrimination between 3 and 4; 6₁ is the first genuinely new value.
