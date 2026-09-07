---
# qou-pdg9
title: 'DERIVE c1(A): the hbar_q^1 coefficient of tr_M(W_free) - tr_M(W_atom), exactly, from the Laurent trace'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T08:32:06Z
updated_at: 2026-09-06T11:35:23Z
---

Successor to qou-zrx2. c0(A) = 2^-A - 2^(1-2A) is DERIVED (Schur-Weyl + cycle count, ClassicalTraceFloor.lean). c1 = lim (Dtr - c0)/hbar_q is currently six MEASURED dyadic rationals (pp 19/8, pn 37/16, nn 9/4, T 163/64, 3He 85/32, 4He 259/128), entered into PairwiseChainLeadingOrder.lean as defs. Goal: (1) obtain them EXACTLY via laurent_q_trace.tr_M_atomic_lq (formal (z,h)-polynomial with LaurentQ coefficients) expanded at q = e^eta to first order -- no Richardson; (2) find and prove the closed form in A, by the same route as c0 (first-order term of a permutation-character sum). Branch claude/logz-hbarq-rung-operator-class-2026-09-03 (branch name predates the corpus-grep that found qou-ap3d/qou-ssz6 had already closed the log Z rung question).


## 2026-09-03 — DERIVED, both ways, and the six defs are now conditional theorems

Probe: `computations/probes/c1_leading_coefficient_derived_probe.py`.
Lean: `QOU/MassTheory/LeadingOrderTraceCoefficient.lean` (lean-direct exit 0; axioms
`[propext, Classical.choice, Quot.sound]` on every declaration, no `sorryAx`).

### Part A — exact, no extrapolation

The validated exact-`Fraction` seminormal pipeline (`exact_rational_chi_gauge_probe`,
11/11 vs the cached deuteron characters) is duck-typed on `+ − × ÷ **`; run over
truncated power series in `ε = q − 1` with valuation tracking (the `h/(1−q^{−2ρ})`
entries are 0/0 at ε = 0), it returns `Δtr(1+ε)` as exact rationals order by order.

    case   a0 (=c0 derived)   c1 exact   recorded   c2 exact
    pp     1/8               19/8       19/8       357/32
    pn     1/8               37/16      37/16      403/32
    nn     1/8               9/4        9/4        217/16
    T      3/32              163/64     163/64     3285/128
    3He    3/32              85/32      85/32      3451/128
    4He    7/128             259/128    259/128    (P=3, not computed)

`a0` reproduces the DERIVED floor by a completely different computation than the
cycle count (an independent check of `ClassicalTraceFloor`). `c1` equals the six
Richardson-measured rationals EXACTLY. `c2` is new and exact — recorded, not
claimed closed-form.

### Part B — derived: a permutation count, like c0

Expanding the quantum trace `Tr(K ρ(word))/(1+q²)^n` at `q = 1+ε`:
(1) the Hecke relation forces `σ = s + ε(1 + Y)` with `sY = −Ys`
(`hecke_first_order_anticommutes`, `hecke_relation_snd` in the dual numbers);
(2) `Tr(Y·P) = 0` for every permutation `P` by the spin-flip symmetry (NOT
formalised — needs Schur–Weyl); (3) the `K′` term `n·2^c` cancels the
normaliser's `−n·2^c`; (4) each letter's own first-order term is the scalar
`1 + d′(0) ∈ {+1, −1, 0, 0}` for σ/σ⁻¹/averaged/colour-weighted — δ = O(ε³) is
invisible at this order (measured: weighted vs blind agree to ε³, differ at ε⁴).

    d tr_M/dε|₀ = 2^{−n} Σ_ℓ w_ℓ 2^{c(σ with letter ℓ deleted)}      [★]

`c1 = [★](free) − [★](atom)` equals Part A's exact `c1` in all six cases
(Fraction equality). Per-letter data: every intra σ deletion raises the cycle
count by 1, every σ⁻¹ deletion lowers it → proton `4·6−3 = 21`, neutron
`4·5−4 = 16`, interface pp `+4`, nn `−4`, pn `0`, all times `2^{c−1}`:

    c1(Z,N) = (21Z + 16N)·(2^{−A−1} − 2^{−2A}) − 4·(I_pp − I_nn)·2^{−2A}

verified against [★] for every (Z,N) with A = 2..20 (asserted in the probe) and
in Lean (`c1Closed_*`, `c1_defs_eq_closed`, `c1_from_letters` from the explicit
12 letter lists). Also `c1(pp) + c1(nn) = 2·c1(pn)` exactly
(`c1Closed_bond_symmetry`), and the affine step in Z at fixed A (`c1Closed_step`).

### Honest split (same as ClassicalTraceFloor)

Proved: the ring/dual-number identity of step 1; dyadicity of any [★]-sum; the
closed form's values; [★] from the letter data. Assumed: quantum Schur–Weyl
(tr_M = Tr(K ρ)/Z with K = diag(1,q²)^⊗n) and the trace-invisibility of Y.
The six `def c1_*` in `PairwiseChainLeadingOrder.lean` are therefore derived
CONDITIONAL on those two, not unconditionally.

### What this does NOT change

Nothing about the scale (`qou-59j5`) or the log channel. It removes one
"measured" from the pairwise-chain leading-order story: `c0` and `c1` are both
derived now, so `24/7` at 4He etc. are derived ratios.



PR #6492 (branch claude/logz-hbarq-rung-operator-class-2026-09-03), commits 2ef2369a71 (Lean) + fd616e8240 (probe, 8/8). Open: the permutation-half formalisation (orbit count under a deleted transposition) — tracked in qou-zrx2 follow-up (5), now needed for both c0 and c1; and the c2 closed form (exact values recorded, no formula attempted).


## 2026-09-06 — REOPENED: the six c1 values are the PRE-2026-09-05 word

Probe: `computations/probes/c1_is_stale_on_the_reordered_atom_word_probe.py`.
Audit: `docs/audits/2026-09-06-c1-is-stale-on-the-reordered-atom-word.md`.

This bean completed **2026-09-03**. The atom word changed **2026-09-05** (owner ruling
`qou-hu1f`): each nucleon's confinement core moved from grouped `s0^3 s1^-3` to the
alternating `(s0 s1^-1)^3`, moving absolute traces 3.785x (2H) to 14.325x (4He). All six
recorded c1 are the **grouped** word's:

    case   recorded (grouped)   canonical (borromean)   ratio
    pp     19/8                 1/8                     19
    pn     37/16                1/16                    37
    nn     9/4                  0                       inf
    T      163/64               1/64                    163
    3He    85/32                1/8                     85/4
    4He    259/128              7/128                   37

**Two independent routes, neither trusting the other.** (1) This bean's own Part-B formula
[*] `d tr_M/deps|0 = 2^-n Sum_l w_l 2^{c(word minus l)}`, reimplemented — its self-test is
that it reproduces all six RECORDED rationals exactly under `grouped`, so the canonical
column is a statement about the word, not about the code. (2) `tr_m_atom_via_transfer.
tr_m_atom_zn` swept along q = exp(eta), no reference to [*]: deuteron (Dtr - c0)/hbar_q
runs 0.063287 -> 0.0625782 -> 0.0625078 -> 0.06250078, converging on 1/16, not 37/16.

**Why nothing flagged it.** c0 = 2^-A - 2^(1-2A) is a pure CYCLE COUNT and cycle counts are
blind to letter order — measured invariant under intra_order AND pn_convention. So the
sibling result in the same arc survived and nothing looked stale. c1 is the FIRST order
that can see letter order. **A reordering that provably cannot move the leading term is not
evidence about the next one.**

**Stale:** `PairwiseChainLeadingOrder.lean` (six c1 defs), `LeadingOrderTraceCoefficient.
lean` (Part B, stated for the old word), the closed form
`c1(Z,N) = (21Z+16N)(2^(-A-1) - 2^-2A) - 4(I_pp - I_nn)2^-2A`.
**Not stale:** c0, `ClassicalTraceFloor.lean`, the floor closed form, every hbar_q^0 claim.

**No new closed form is proposed.** Six canonical values are recorded as data; guessing a
form from six points is how this arc has been burned before. That is this bean's work now.


## 2026-09-06 — CLOSED FORM ON THE CANONICAL WORD (PR #6920)

Probe: `computations/probes/canonical_c1_closed_form_probe.py`.

    c1(Z,N) = (Z*S_p + N*S_n)/2 * (2^(-A-1) - 2^(-2A)) - 4*(I_pp - I_nn)*2^(-2A)

with S_X the PER-NUCLEON DELETION SUM on that nucleon's own three strands,
S_X = Sum_{l in X} w_l * 2^(c(3-strand word minus l)). The ONLY ordering-dependent input:

    borromean (CANONICAL)   S = ( 6, -4)  ->  ( 3Z - 2N)
    grouped   (this bean)   S = (42, 32)  ->  (21Z + 16N)

So the old form was not wrong in SHAPE — it is this form at the wrong (S_p, S_n). The
interface term -4(I_pp - I_nn)2^(-2A) is UNCHANGED, as it must be: interfaces are single
letters outside the nucleon blocks. Verified, not asserted.

**Verified A = 1..8, exact Fractions, BOTH HALVES SEPARATELY** so a compensating error in
the two cannot cancel: [*](free) 44/44, [*](atom) 44/44, c1 44/44 — under BOTH orderings.
A = 8 did not enter the pattern search (A <= 7 did), so its 9 isotopes are held out.

**Control:** S/2 under grouped reproduces this bean's independently-derived (21, 16)
exactly, with no adjustment — which is what makes the canonical row the same formula rather
than a fresh fit.

**Mechanism: cancellation** (the qou-hu1f contiguity theme, quantitative). Per-letter
deletion contributions for one proton:

    grouped     +2^3 +2^3 +2^3 +2^3  .  +2^3 +2^3 -2^1 -2^1 -2^1  .   = 48 - 6 = 42
    borromean   +2^1 -2^1 +2^3 -2^1 +2^1 -2^3 +2^1  .  .  +2^1 +2^1   =          6

Contiguous sigma runs leave the same cycle count and add coherently; alternation interleaves
them with opposite-sign sigma^-1 deletions and they largely cancel. The NEUTRON's sum CHANGES
SIGN (32 -> -4), which is why canonical c1 is negative for neutron-rich isotopes
((0,7) = -429/8192) where the grouped one was positive throughout.

Canonical values: D 1/16, T 1/64, 3He 1/8, 4He 7/128, 6Li 93/4096, 7Li 67/16384.

**Still open on this bean:** (1) c2 is untouched — the six recorded c2 (357/32, 403/32,
217/16, 3285/128, 3451/128) are grouped-word values and have NOT been recomputed;
(2) the Lean still carries the dead coefficients — `PairwiseChainLeadingOrder.lean` (six
c1 defs) and `LeadingOrderTraceCoefficient.lean` (c1Closed + letters_pnAtom). Repairing
that is a separate change with its own verification and is deliberately not attempted in
#6920.


### 2026-09-06 — the LEAN is repaired too (PR #6920), all three files sorry-free

Not two files but **three** — `MirrorAsymmetrySign.lean` also consumes `c1Closed`; found by
corpus grep, and verified rather than assumed.

- **PairwiseChainLeadingOrder.lean** — rewritten GENERICALLY in (S_p, S_n); the six values are now
  instantiations, so a future reordering is a two-number change. Both columns checked
  (`c1_canonical_values` at (6,-4), `c1_grouped_values` at (42,32)).
  **The headline claim got STRONGER:** `chain_over_atom_He4_generic` proves the 4He over-count is
  24/7 for EVERY (S_p, S_n) — the deletion sums cancel identically — so it survives ANY
  intra-nucleon reordering, not just the two computed. (4He has Z = N = 2, so its interface term
  vanishes, and the pp `-4` and nn `+4` cancel across the three A=2 bonds; both sides go as
  (S_p + S_n).) T and 3He do NOT cancel and really move (292/163 -> 4, 30/17 -> 3/2), recorded as
  `chain_ratios_T_He3_not_invariant` (a disequality, so it makes no claim about which is right).
- **LeadingOrderTraceCoefficient.lean** — c1Closed -> (3Z - 2N), the six c1Closed_* values, and ALL
  TWELVE hardcoded letter tables regenerated. Those tables were a WRONG DATUM (the grouped word's
  per-letter (w,c) data), not merely mis-scoped theorems. c1_defs_eq_closed and c1_from_letters
  retargeted to the generic defs.
- **MirrorAsymmetrySign.lean** — survives UNCHANGED. The mirror difference cancels everything but
  the coefficient GAP, so mirrorBracket depends on P - Q alone, and P - Q = (S_p - S_n)/2 is 5 under
  both orderings. Docstring flags this as MEASURED ON TWO WORDS, not structural — unlike the 4He
  24/7, which is. Do not conflate the two when quoting either.

**Verification:** lean-direct with `-DautoImplicit=false -s 65536` (a bare `lean` is weaker than
lake — autoImplicit defaults true and the lakefile sets it false), each dependency compiled into a
shadow first, lake never invoked so the olean cache is not evicted. All three exit 0.
`#print axioms` on all eight touched declarations: [propext, Classical.choice, Quot.sound] — no
sorryAx.

**Still open:** c2 only. Its six recorded values (357/32, 403/32, 217/16, 3285/128, 3451/128) are
grouped-word and have not been recomputed. No Lean carries them.


### The closed form turns up again one order up: `|S| = 1` is `c₁`, halved (2026-09-06, PR #6920)

Worth recording here rather than only on `qou-qqm4`, because it is a fact about **this bean's**
closed form. The second-order coefficient `c₂` splits by insertion class (`[◇]`, `|S| = 0, 1, 2`),
and the single-insertion class is `c₁` itself:

    |S| = 1  −  c₁/2  =  k(A),   species-independent

    A = 2   pp, pn, nn         all  13/16   = 13/2⁴
    A = 3   3p, T, ³He, 3n     all  61/64   = 61/2⁶
    A = 4   ⁴He                     193/256 = 193/2⁸

Eight species, three constants — five degrees of freedom of test, exact on all eight. It was not
looked for: a leave-one-out affine fit of `|S| = 1` in `(u, D)` at `A = 3` returned
`(a, b) = (3/128, −1/32)`, and that is exactly half of the `(3/64, −1/16)` this bean's closed form
gives at `A = 3`. So `c₁` is not just the first-order answer; it is the whole species-dependence of
the single-insertion class at second order too.

**What that buys, and what it does not.** It says the closed form is structural rather than an
`A`-by-`A` coincidence — the same `(u, D)` combination governs two different orders. It does **not**
extend to `c₂`: the letter-**pair** class `|S| = 2` is NOT affine in `(u, D)` (4/4 leave-one-out
MISS at `A = 3`, against a `c₁` control that hits 4/4 and returns the derived coefficients exactly),
and that is the entire reason `c₂` has no affine form.

🛑 **REFUTED the same day.** The `A`-dependence of `k` was a **zero-dof fit** —
`m(A) = (3/8)4^A + (15/2)2^A − 23` on three points with three parameters, so it could not fail on
its own data. `⁵He` (`n = 15`, 49 min) settled it: predicted `m(5) = 601`, **measured 521**. The
sequence is `13, 61, 193, 521` at `A = 2…5` and **no closed form is offered** — a fourth point does
not license a four-parameter fit.

🛑 And I quoted the prediction wrong before it was refuted: this line said `k(5) = 663/2¹⁰`, and
`(3/8)·4⁵ + (15/2)·2⁵ − 23 = 601`. The verdict is unaffected (601 misses 521 too), but the same
wrong number went into `c2_pairwise_shape_holdout_probe.py` and PR #6920's body; all three are
corrected.

**What the run establishes positively, and it is this bean's business:** `c₁`'s closed form holds at
`A = 5` — measured `1/256`, predicted `1/256`. Eighth independent size, and the largest word ever
put through `[◇]` (`2¹⁵` basis states). New exact values there: `c₂(⁵He) = 1001/2048`, class split
`|S|=0: 67/512`, `|S|=1: 523/1024`, `|S|=2: −313/2048`.

⚠ The `A = 5` run used **one** species, so it tests the *formula*, not the species-independence of
`k` at that `A`. That remains measured at `A = 2, 3, 4` only (8 species, 3 constants). A second
`A = 5` species would test it, at another ~49 min.

Quote the species-independence, not any formula.

Probe: `computations/probes/c2_pairwise_shape_holdout_probe.py` (exact `Fraction`s, no `q`).
