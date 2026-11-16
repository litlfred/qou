---
# qou-mgq3
title: 'Magic-number derivation: measured attack surface, and the two walls'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-10-04T15:14:56Z
parent: qou-v2om
---

Follows `qou-pz4m` (delta2-Phi is a parity test). That bean closed a route;
this one maps what is left, measured rather than surveyed.

## The problem decomposes, and the split is the whole game

Standard Mayer-Jensen filling, recomputed here:

| magic | closed by | 2j+1 |
|---|---|---|
| 2, 8, 20 | 1s1/2, 1p1/2, 1d3/2 | 2, 2, 4 |
| 28, 50, 82 | 1f7/2, 1g9/2, 1h11/2 | 8, 10, **12** |
| 126 | 3p1/2 | 2 |

**{2, 8, 20} are pure 3D-harmonic-oscillator closures** — cumulative
(N+1)(N+2) gives 2, 8, 20 and then 40, 70, 112. Many level schemes produce
them; they are cheap and NOT discriminating.

**{28, 50, 82, 126} require spin-orbit inversion.** This is already a proved
scope-(b) exclusion in the corpus and must not be re-attacked:
`docs/audits/2026-07-06-q-deformed-ho-spin-orbit-magic-numbers-assessment.md`
§2 — a *scalar* (q-)oscillator has state space L^2(R^3) with no C^2 factor, so
no operator `s` exists in its algebra and an l.s term is identically absent
from its spectrum. The q-deformation buys the orbit-orbit (l^2) term and the
*cluster* ladder 2, 8, 20, 40, 58, 92; it cannot buy the nuclear one.

**So the single question worth asking is: where do spin-1/2 and l.s come from
in the braid substrate?** Everything else is either already available or
already excluded.

## Wall 1 — the LP dual does not discriminate ANY nucleus at H_3

Measured on `computations/all-nuclides-sdp-admissibility.witness.json`
(3558 nuclides, canonical t=TR_M, G=gram_matrix(), no fit):

- `lp_active_count` takes **exactly one distinct value, 1**, over all 2221
  nuclides with a solvable dual.
- the active channel set is **the same singleton for every one of them**:
  `{gamma}`.

So the H_3 operator selection is flat, not merely magic-blind: there is no
shadow-price structure to change at a magic number, because there is no
per-nucleus structure at all. The witness's own finding says it — *"the
H_3-local operator selection just scales with A ... per-nucleus binding
richness must live in the tower / Delta_lambda"*. Any "does the dual change at
magic Z" probe run at H_3 will return a flat line and answer nothing.

## Wall 2 — the two highest magic numbers are not reachable

Same witness. f64 `build_atom_nf` overflows for **1337/3558 (37.6 %)**, and the
cut is at **A >= 163**:

    Z=  2   8/  8 isotopes have an LP dual
    Z=  8  18/ 18
    Z= 20  29/ 29
    Z= 28  35/ 35
    Z= 50  42/ 42
    Z= 82   0/ 43     <-- none
    Z=126   0/  0

**Z = 50 is the last testable magic number on this path.** Z = 82 is entirely
unreachable and Z = 126 has no rows at all. Reaching them needs the mpfr native
path, which the witness flags as the required infra.

The LR route hits its own wall earlier — `active-set-lr-scaling-profile.witness.json`
gives active tuples 35, 406, 3997, 32070, 229497 for A = 2..6, i.e. ~x7 per
nucleon. A = 8 is ~1e7 and A = 40 (Ca-40) is not in the same universe. The
multi-LR enumeration caps around A = 6-8.

## What the convolution is

`prop:categorical-fourier-transform-exists`: F intertwines the **q-convolution**
with the pointwise product on irreducibles (Peter-Weyl over
R_q = Z[q,q^-1]). `categorical-laplace-transform.md` pins it further — the
convolution is the **mate of the comultiplication Delta_q on H_q**, and that
uniquely characterises L. `q-resolvent.md` works in "the convolution algebra
H_q".

So the convolution is Delta_q-mate on the shuffle algebra, and on characters it
is the tensor product, i.e. **LR fusion**. That is exactly the operation
`conj:diagrammatic-double-magic-lr-fusion` conjectures is *rigid* (multiplicity
one, single self-conjugate nu) at doubly-magic (Z,N). **The convolution and the
magic-number conjecture are the same object**, which is the connection worth
exploiting. Its knot-operator realisation (connected sum? satellite? cabling?)
is NOT established in the corpus — I did not find a block identifying it, and
that is an open item rather than a measured absence.

## Attack options, ranked

1. **Spin-orbit from framing (best).** The ingredients exist and are
   unconnected: `def:q-angular-momentum` = [j]_q[j+1]_q (the SU_q(2) Casimir,
   `climax-volume-mass/q-angular-momentum.lean`), `def:strand-twist-datum` (the
   per-strand integer ribbon twist T(t), `appendix-standard-model`), and the
   writhe-derived isospin. A q-deformed l.s = (twist) . (q-angular-momentum)
   coupling is the missing Mayer-Jensen ingredient. Formalize-first: state the
   coupling, check it reproduces the 1f7/2 inversion at 28 BEFORE any sweep.
   Caution: `strand-twist-datum.md` is explicit that T(t) is a **free label**,
   not read off the ribbon structure, and does not yet descend under
   stabilisation - so a coupling built on it inherits the label's freedom.
   That is the thing to fix first, not to paper over.
2. **Move the LP off H_3.** Wall 1 says the dual is flat at H_3. Re-pose the
   operator selection at the level where the shell lives and re-ask whether the
   active set opens up at magic Z. This is the direct form of "does the shadow
   price structure change" and it has never been run anywhere but H_3.
3. **A_5 branching.** `a5-so3-branching.witness.json` +
   `a5-orbital-degeneracy-fracture` give SO(3) restricted to the icosahedral
   A_5: dims 1,3,3',4,5, max 5. With spin doubling the largest irreducible
   multiplet is 10, so **the 1h11/2 level (12) that closes 82 cannot be an
   A_5 irreducible**. Not fatal (accidental multiplet coincidence is allowed)
   but it is a sharp, cheap, checkable constraint that nobody has stated.
4. **Deprecated-producer archaeology (cheap).** `shell_closure_compute.py` is
   in `_deprecated/` yet is the only thing that reproduces the published table.
   Either restore it with a witness or retire its numbers.

## Explicitly NOT to re-attack

- l.s from a scalar q-oscillator. Proved scope-(b), see above.
- delta2-Phi at any q in (1, phi). 49-point sweep, `qou-pz4m`: Z=20 and Z=2 are
  local maxima at no sampled q.

## Full no-float64 sweep: the flat dual is real (2026-08-30)

`all_nuclides_sdp_admissibility_mp.py 92 160` -> witness. **4932 rows, 0
overflow, 0 build failures.** Z=82 is 161/161 and N=126 is 93/93, where the f64
producer had 0/43 and no rows at all.

Wall 1 SURVIVES the fix and is now measured corpus-wide rather than inferred
from 62 % of the chart:

    distinct lp_active_count      [1]
    distinct active channel sets  [{gamma}]
    double-magic nuclides         all 42, still 1
    dual_discriminates_magic      false

So the flatness is a property of **H_3**, not of the chart's light end. There
is one channel available, so there is nothing for magic structure to modulate.
Wall 2 is GONE — reachability is no longer the blocker; the algebra is.

This makes the "more intertwining, like T_{3,5}" route (option 2) the only
surviving LP-side attack, and it is now unblocked: every magic Z and N is
computable, so an LP posed above H_3 can be tested against the whole ladder
rather than against {2,8,20,28,50}.

## Parity is the pairing term — sibling convergence (qou-edt7 / PR #6197)

My `qou-pz4m` note speculated that the period-2 structure in Phi "may be the
pairing term, which IS nuclear physics — just not magic numbers." A sibling has
now derived that from the other side, and I verified it rather than taking the
comment at face value (AGENTS.md: a sibling's claim is not a primary source).

`folio/quantum-observable-universe/lean/QOU/Mass/PairingParityForcesPositiveB3.lean`
on the PR #6197 head — 108 lines, **0 sorry, 0 axiom**, checked by fetching
refs/pull/6197/head, not from the comment. `b3Contrib f2 f3 := f3 - 3*f2` with
`pairing_b3_eq : b3Contrib (-delta) 0 = 3*delta`, so pairing (f2 = -delta,
f3 = 0) forces the connected three-body cumulant `b3 > 0`, sign derived with no
fitted input.

**Why this matters HERE, beyond the coincidence.** It converts my scope-(a)
negative into a positive identification. If parity is the pairing term, then
delta^2-Phi's even-Z positivity is plausibly *measuring the pairing term* —
which is real nuclear physics and is why the signal looked meaningful — rather
than measuring shell closure. That explains the finding instead of merely
recording it, and it predicts the signal should track `delta` (the SEMF pairing
scale), not the magic ladder. Testable: correlate `delta^2 Phi(Z)` against the
SEMF pairing term across the chart.

Their stated caveat, carried honestly: the pairing scale is over-determined,
`b3` magnitude vs the SEMF fit disagreeing by 25-40x. So the SIGN transfers and
the SCALE does not — which is the same shape as every other result on this arc.

## 🛑 RETRACTION — the pairing identification above is REFUTED, and it was mine

The section immediately above claims delta^2-Phi's even-Z positivity is
"plausibly *measuring* the pairing term". **That is wrong.** I published it in a
PR comment before testing it. Tested now:
[`delta2phi_semf_pairing_probe.py`](../computations/probes/delta2phi_semf_pairing_probe.py)
-> `delta2phi-semf-pairing.witness.json`, 3/3.

**1. The sign agreement is structurally FORCED, so it is not evidence.** The
producer evaluates the **N = Z line**, so `A = 2Z` and the pairing class is
fixed by Z parity alone: Z even -> N even -> even-even -> SEMF `+delta`; Z odd
-> odd-odd -> `-delta`. **Any** quantity that alternates with Z parity
reproduces the SEMF pairing sign here. delta^2-Phi alternates (0 exceptions,
Z = 3..31), so of course it matches — that is a restatement of "delta^2-Phi
alternates", which `qou-pz4m` already established. It carries no new content,
and I presented it as if it did.

**2. The magnitude is refuted by SHAPE, not merely scale.** Decomposing
`Phi(Z) = s(Z) + (-1)^Z e(Z)` and separating by averaging / half-differencing
adjacent Z (the smooth part is only **3.4 %** of the alternating one, so e(Z)
extracts cleanly):

| quantity | SEMF requires | measured |
|---|---|---|
| `e(Z)·sqrt(Z)` | constant | **11.04x spread** (3.38 -> 37.34) |
| `e(Z)` | monotone decreasing in A | **non-monotone**, peaks at **Z = 12** |

`e(Z)` rises 8.67 -> 9.65 through Z = 12-15 and only then falls to 0.617 by
Z = 30. SEMF pairing `delta = a_P/A^(1/2)` decreases monotonically throughout.
Wrong shape, so no choice of `a_P` rescues it.

**What this does NOT touch.** PR #6197's `PairingParityForcesPositiveB3.lean`
is unaffected — verified sorry-free, and it is about the connected three-body
cumulant `b_3`, a different object. The parity finding in `qou-pz4m` is
unaffected. Only my inference *between* them is retracted.

**Contamination.** The claim reached three places, all now corrected: this bean,
the reply on PR #6201 (correction comment posted), and the PR body's beans
section. Scope **(a)**: a negative about the SEMF-pairing identification of this
statistic, not a claim that no pairing mechanism exists anywhere in the tower.

**The lesson, since it is the second time on this arc.** "Sign matches" was
worth nothing here because the sign was *determined by the sampling line*, not
by the physics. Before treating a sign agreement as evidence, check whether the
sampling forces it. `qou-o16k` is the same shape one block over: the kappa fit
lived entirely where two conventions coincide, so it could not distinguish them.

## The one SDP above H_3 already exists — and it cannot see magic numbers

Chasing option 2 ("re-pose the LP above H_3") turned up that it partly exists,
and that it fails for a reason worth recording.

**`gram.py` is hardwired to H_3.** `gram_matrix()`, `gram_matrix_mp()`,
`gram_matrix_mp_strings()` take **no `n` parameter**; the LP channel space is
the 6-element NF basis `['γ','σ₀','σ₁','L₊','L₋','e⁻']` = dim H_3(q) = 3!. So a
general-n Gram does not exist and is not a matter of passing `n=4`.

**But `pyhecke.sdp.solve_shell_magic_sdp` DOES pose an SDP above H_3** — at
`H_{3·A_magic}`, i.e. H_24 for the 8-shell. It forms `[[1,y],[y,1]]` with
`y = shell_shadow_price(a_magic)["shadow_price_abs"]` and declares feasibility
iff `|y| ≤ 1`, its docstring saying magic numbers satisfy it "by construction".

**Measured, it cannot discriminate — two defects**
([`shell_shadow_price_magic_contrast_probe.py`](../computations/probes/shell_shadow_price_magic_contrast_probe.py), 3/3):

1. **The wrapper refuses non-magic input** (`a_magic in MAGIC_NUMBERS` or
   infeasible), so no contrast can be produced through it. The underlying
   `sigma_shell_characterization.shell_shadow_price` has **no such guard**, so
   the contrast was always computable and had simply never been run.
2. **The quantity has no feature at magic A.** Over A = 2..30 at the default
   partition `(3A−1, 1)`, `shadow_price_abs` is **smooth and monotone
   decreasing**, ~6 orders per unit A, from `5.3e-3` at A=2 to `2.6e-237` at
   A=30. **Zero local extrema anywhere.** Magic and non-magic interleave on one
   curve.

   And the feasibility test is vacuous: `|y| ≤ 1` holds for **29/29** — 4/4
   magic and 25/25 non-magic — by up to **237 orders** of margin. The
   docstring's "by construction" is literally true, which is exactly why
   passing it carries no shell-closure content. It cannot fail for any A.

Scope **(a)**: the default standard-rep partition only. Other partitions of 3A
are untested and are the live remainder of option 2.

**Third instance of one pattern today, and that is the transferable finding.**
The corpus keeps producing magic-number "signals" whose apparatus is
constitutionally unable to see a non-magic counterexample:

| # | site | mechanism |
|---|---|---|
| 1 | `conj:magic-numbers-from-q` table | tabulates only magic Z |
| 2 | `magic_vs_nonmagic_report.json` `magic_ladder_member` | hardcoded copy of `MAGIC_LADDER` |
| 3 | `solve_shell_magic_sdp` | rejects non-magic `a_magic` at the door |

In all three the magic set is an **input** presented as an output. Any future
magic-number claim should be required to state, up front, what its
non-magic control is and what result would have falsified it.

### Exhaustive partition sweep closes the remaining caveat

The scope-(a) caveat above ("other partitions of 3A are untested") is now
tested. All **11,660** partitions of 3A for A = 2..10:

| A | k=3A | partitions | max\|y\| | n with \|y\|>1 |
|---|---|---|---|---|
| 2 | 6 | 11 | 0.0212226 | **0** |
| 4 | 12 | 77 | 2.46806e-5 | **0** |
| 8 | 24 | 1575 | 3.29685e-11 | **0** |
| 10 | 30 | 5604 | 2.28167e-13 | **0** |

`max|y|` over the entire partition space is monotone decreasing in A, ranking
exactly `[2,3,4,5,6,7,8,9,10]` — pure A order, no magic feature. And **not one
partition of the 11,660 violates `|y| ≤ 1`**.

So the vacuity is a property of **the criterion**, not of the partition choice:
the level-4 PSD condition cannot fail anywhere in the partition space. Option 2
("re-pose the LP above H_3") is closed in the form the corpus already
implements it.

**Honest limit.** Exhaustive only to A = 10 — `p(60) = 966,467` and `p(84)` is
~1e9 — so the exhaustive claim covers magic **{2, 8}**. Magic 20 and 28 are
covered by the default-partition sweep to A = 30; 50, 82, 126 by neither.
`min|y|` is exactly 0.0 at some partitions for A = 3,4,5,10, so its cross-A
ranking is degenerate and carries no signal either way — do not read it as one.


---

## Round 48 Execution Update (2026-11-16, PR #8181)

- **PR:** https://github.com/litlfred/qou/pull/8181 (`e3a0c2e1773d8a4bc1635ead95154cb8d9babb4d`)
- **Lean 4 Formalisation (`0` `sorry`, `0` `axiom`, wired into `QOU.lean`):**
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/FramingSpinOrbitMagicLadder.lean`
    - Formalises both magic-number walls:
      1. The oscillator-vs-intruder bifurcation (`hoCumulative_first_seven` `[2, 8, 20, 40, 70, 112, 168]` vs `soIntruderCumulative_magic_upper` `[28, 50, 82, 126]` and `mayer_jensen_intruder_splits`).
      2. The `A₅` icosahedral branching obstruction (`a5IrrepDims_burnside`, `a5_spin_doubled_max_lt_h11_half`, `a5_l5_branching_dimension_split`): every spin-doubled `A₅ × SU(2)` irreducible multiplet has dimension `2d ≤ 10 < 12` (`1h_{11/2}` closing `82`) and `< 14` (`1i_{13/2}` closing `126`), and under `SO(3) ↓ A₅` the `ℓ = 5` (`dim 11`) orbital representation splits into `3 + 3 + 5 = 11`.
- **Probe & 50-dps Witness:**
  - `computations/probes/spin_orbit_magic_rstar_mirror_probe.py`
  - `computations/probes/spin-orbit-magic-rstar-mirror-probe.witness.json`
- **Status:** Kept at `in-progress` pending owner review and PR merge.
