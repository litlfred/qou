---
# qou-768r
title: 'Derived nucleus->link map: SLq(2) (N,w,r)->irrep + Milnor/higher-helicity energy bound — held-lit survey and fetch list'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T03:46:30Z
updated_at: 2026-11-15T11:48:07Z
parent: qou-10v9
---

Owner picked routes **1** (SLq(2) `(N,w,r)` -> irrep) and **3** (Milnor /
higher helicity) on held material, and will fetch lit themselves. This bean
carries the held-coverage survey, the fetch list, and the state of play.

## Held-coverage survey (2026-08-31)

**Route 1 — a derived knot->irrep map is HELD and half-adopted.**
`library/arxiv-0806.3105v3` (Finkelstein, *Knots and preons*): the kinematic
eigenstates of a quantum knot are matrix elements of `SLq(2)` irreps
`D^{N/2}_{w/2,(r+1)/2}` with `(N, w, r)` = (crossings, writhe, rotation).
A dictionary read off topological invariants -- no volume, no census scan,
nothing fitted. Ten SLq(2)/braid-matter papers held in total, including
Bilson-Thompson's own `arxiv-hep-ph-0503213v2`.

- **`finkelstein2008` is in `content/schema/references.ts:10683` and cited by
  NO content block.** A registered, unused source.
- **The corpus already adopts the sibling construction at the LEPTON level**:
  `breit-wheeler-vertex-literature.md` takes Bilson-Thompson's fermion ->
  framed-braid-in-B_3 map "exactly". Nobody has pushed it up to nuclei.

**Framework already has two of the three inputs:**

| input | status |
|---|---|
| `N` crossing number | **= 10A - 2**, proved + merged (PR #6327, `qou-5vhf`) |
| `w` writhe | computed in ~6 live producers |
| `r` rotation number | **NOT computed anywhere** -- the concrete gap |

**Route 3 — energy-from-linking, held better than first measured.**
25 helicity documents; 3 Milnor triple-linking; 2 higher-order helicity;
Moffatt-Ricca `Lk = Tw + Wr` (96 % in the **ocr/** tier, invisible to the
documented `sections/` grep). "asymptotic crossing number" appears in 3 files.

## MEASUREMENT ERROR, corrected in-session

A first pass reported **0** files for `energy<->helicity`, Calugareanu, and
mu-bar/Milnor. All three were wrong: the pattern used `\|` for alternation
under `grep -E`, where it is a LITERAL pipe. Corrected counts: **7**, **13**,
**19**. Same detector-blindness class AGENTS.md catalogues; caught before it
reached the owner as an all-clear. Note also the OCR spells it both
`Calugareanu` (14x) and `Calugdreanu` (11x) -- an OCR-mangled variant that an
exact-spelling grep misses.

## NOT held

The **nuclear** Skyrme model. The two Skyrme papers held are Skyrme-**Faddeev**
(33x "Hopf charge", **0x** "baryon number"); `Houghton`: 0 files. Knotted
solitons in a sigma model are a different object from the SU(2) chiral field
whose rational-map ansatz sends nucleon number to a polyhedral geometry.
Owner deferred this (option 2 not selected).

## Constraint any fetched result must satisfy

`QOU.Mass.CoordinationSaturation` (merged, sorry-free): observed B/A saturation
forces **bounded degree**. So an energy-from-linking bound growing
superlinearly in A is ALREADY EXCLUDED -- as is the `C(A,3)` triple-count
scaling, by C4 of the A>=5 constraint table. Filter fetched results on this
before spending time on them.


## RESULT 2026-08-31 — the SLq(2) label admits the atom word at EVEN A only

Route 1 does not need the fetch to reach its first hard result, and the result
is a structural exclusion of half the periodic table.

### `r` needed no fetch

For a coherently-oriented closed braid on `n` strands the rotation number is
`n`. Finkelstein's own trefoil values confirm it: the trefoil is the closure of
`sigma_1^3` in `B_2`, and he records `r = +-2`. So `r = 3A`, the framework's own
strand count. The "r is computed nowhere" gap in the survey above is closed --
it is not a new computation, it is the strand count already in hand.

### The label is not free

`D^j_{mm'}` needs `j-m` and `j-m'` integral. `j-m = (N-w)/2` is automatic
(`w = N mod 2`). `j-m' = (N-r-1)/2` is the binding one, and Seifert on a closed
braid (`chi = n - c = 2 - 2g - mu`) turns it into

    label consistent  <=>  mu ODD.

For a knot (`mu = 1`) automatic -- which is why the dictionary is stated for
knots.

### Measured: mu = A + 1

Exactly, over eleven isotopes including asymmetric ones. Branch-INDEPENDENT: a
superposition letter and its `sigma` branch project to the same permutation, so
`mu` is the one quantity here not depending on which of the `2^(2A+1)` branches
is taken. Cross-check: the deuteron's `mu = 3` reproduces the 3 components the
2026-08-25 audit measured independently in SnapPy across all 32 branches.

Hence `mu` odd <=> **A even**:

    label consistent : 2H, 4He, 6Li, 8Be, 12C, 16O
    NO label at all  : 3H, 3He, 5Li, 7Be, 7Li   (every branch)

The excluded half is not incidental -- it contains the A=3 mirror pair this
arc's convention systematic lives on.

### Lean (sorry-free, lean-direct exit 0, axiom-clean on all four)

`QOU/Mass/SLq2LabelParity.lean` -- `seifert_label_parity` (label <=> mu odd),
`knot_label_consistent` (knots automatic), `components_odd_iff_even_A`,
`label_admits_even_A`.

### RETRACTED first attempt, recorded because the error is instructive

My first pass fed `N = 10A - 2` (genuine braid letters) into the parity test as
though it were THE crossing number and concluded the label was valid at `A = 3`
ONLY -- the exact opposite of the corrected answer. The test was ill-posed: the
word carries `2A+1` superposition letters, so its crossing count is a RANGE over
`2^(2A+1)` branches and `10A-2` is only the minimum. **A quantity that varies
across branches cannot decide a question about the closure.** The corrected test
routes through `mu`, which does not.

### What this does to the fetch list

It ANSWERS item 2 from the framework side, negatively: the dictionary as stated
is knot-flavoured, because the parity condition IS the knot condition. So the
fetch should be re-aimed at whether a **link** generalisation of the SLq(2)
labelling exists (multi-component, `mu > 1`), not at whether the knot version
extends to general N. Items 1 and 3 are unaffected; route 3's items 4-7 are
unaffected.

Scope **(a)**: this labelling applied to this word. Does not refute the SLq(2)
route -- it locates precisely what a generalisation must supply.


## ROUTE 3 RESULT 2026-08-31 — the Milnor leg is partially available, and the COUNT is the problem

Also needs no fetch. Measured on the canonical atom-word closure.

### The closure is not Brunnian, and its linking graph is a PATH

Nonzero linking pairs = `mu - 1 = A`, always the CONSECUTIVE pairs `(i, i+1)`,
so the linking graph is `P_mu` -- **bounded degree 2**, never the complete
graph. Same shape front A found for the inter-nucleon crossing set, now at the
level of linking rather than crossings.

Branch dependence, stated because it matters: an `averaged` letter is
`sigma_g - (h/2)*1`, the MIDPOINT between the two crossing SIGNS. Both swap, so
`mu` is branch-independent (the SLq(2) result above is unaffected); `lk` is not.
Resolving all averaged letters to `sigma^-1` gives uniform `lk(i,i+1) = -2`;
to `sigma` gives a `-1`/`-2` mix.

### The Milnor indeterminacy, per triple

`mubar(ijk)` is defined mod `Delta = gcd(lk ij, lk jk, lk ki)`.

  * **mutually NON-ADJACENT triples have `Delta = 0`** -> `mubar` is a genuine
    integer. A path admits these iff `mu >= 5`, i.e. **`A >= 4`**.
  * triples touching a linked pair: `Delta = 2` (one bit survives) or
    `Delta = 1` (no information).

So the route is **NOT obstructed** -- partially available, starting exactly at
`A = 4`. For `A <= 3` no genuine integer `mubar` exists at all, so the deuteron
and the A=3 mirror pair are outside its reach.

**The problem is the COUNT.** Non-adjacent triples on `P_mu` number
`C(mu-2,3) = C(A-1,3) ~ A^3`. Summing a per-triple contribution over all of
them reproduces exactly the supra-linear scaling **C4** already excludes
arithmetically and `CoordinationSaturation` refutes structurally. A Milnor
extensive term must be supported on a **bounded-degree subfamily**, and naming
that subfamily without fitting it is the open problem -- not computing the
invariants.

### What survives with the right scaling

`sum |lk| = 2A` in the uniform branch: **linear in A, bounded per-component
degree** -- precisely what saturation demands. A derived, non-volume,
correctly-scaling candidate, which the volume route is not. It supplies no
magnitude on its own.

### TWO errors, both caught by the probe rather than by review

1. **Half-integer linking numbers.** A first pass resolved `averaged` to the
   IDENTITY and produced `lk = -3/2`, totals `7/2`, `11/2`, `21/2`. Impossible
   -- two closed curves cross an even number of times. Reading
   `canonical_braid_crossings.py` settled it: `averaged` is a mixture of the two
   crossing SIGNS, not of crossing and no-crossing. Every value integral after
   the fix, which is the check that the fix was right rather than different.
2. **"No triple has Delta = 0."** Asserted outright; the probe refuted it at
   `A >= 4`. A path with `mu >= 5` has mutually non-adjacent triples whose three
   linking numbers all vanish. The corrected statement is both weaker (the route
   is available) and sharper (it is available exactly from A=4, and the count
   is what kills a naive sum).


## A canonical bounded-degree subfamily exists — counting only, no invariant computed

`qou-brng`'s open item, as sharpened by the route-3 result, was: name a
bounded-degree subfamily of the Milnor-defined triples **without fitting it**.
There is a canonical candidate, and it is the obvious one once the linking
graph is known to be a path.

**Minimal-span non-adjacent triples `{i, i+2, i+4}`.** All three of their pairs
are non-adjacent on `P_mu`, so all three linking numbers vanish and
`Delta = 0` -- these are genuinely Milnor-defined. Counted:

| A | mu | ALL non-adjacent `C(A-1,3)` | min-span `A-3` | max triples per component |
|--:|--:|--:|--:|--:|
| 4 | 5 | 1 | 1 | 1 |
| 8 | 9 | 35 | 5 | 3 |
| 16 | 17 | 455 | 13 | 3 |
| 40 | 41 | 9139 | 37 | **3** |

**Linear in A, per-component multiplicity capped at 3 independent of A.** That
is exactly what `QOU.Mass.CoordinationSaturation` demands and what the full
family (`~A^3`, excluded by C4) violates.

### What this is and is not

**Is:** a family named by a topological minimality criterion -- the tightest
triple that is Milnor-defined -- with **no reference to AME**. That is the
property the anti-fit discipline cares about.

**Is NOT** a derivation from the substrate, and **not** a result about binding.
"Canonical" here means *unique minimal span*, which is stronger than arbitrary
and weaker than derived. **No `mubar` value has been computed** -- this is
combinatorics of which triples are defined, not of what they equal. Computing
one needs the Magnus expansion of a longitude in the free group, which is real
work and is not done.

### Two consequences worth carrying

1. **It vanishes below A=4** (`A - 3` is 0 at A=3, negative below), so it
   cannot contribute to the deuteron or the A=3 mirror pair at all -- the same
   boundary the route-3 availability result found, arrived at independently.
2. **It switches on at exactly one triple at ⁴He**, which is where the arc's
   only exact coordinate sits (`QOU.Mass.PairCountMeetsDegreeBoundAtFour`).
   Suggestive, and precisely the kind of coincidence this corpus has repeatedly
   found to be generic -- do NOT read it as evidence without a genericity check
   of the kind `qou-22vu` ran.



## TAKEOVER 2026-09-04 + ROUTE 2 RESULT — the genus handle is Borromean-only

Taken over: this bean was `in-progress` with `updated_at` 2026-08-31T04:11:30Z
(four days, past the 3 h staleness threshold) and its backing work is already on
`main`. Owner opened a tranche on all three routes and asked for held-literature
links. PR #6560, branch `claude/standard-panel-qou-derivation-ixuolx`.

### Held literature, measured across BOTH library tiers

The survey above searched `sections/` only, which is blind to `procrsoclondona92`
(Moffatt & Ricca, *Helicity and the Calugareanu invariant*: 19 OCR pages against a
1-section stub). Re-measured including `ocr/`: route 1 **10** documents, route 2
**12**, route 3 **9**. Full ledger with per-document links:
`docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md`.

Acquisition gaps, stated as such: Freedman-He 1991 itself (does not touch either
eq.-43 correction, Komendarczyk's statement being held); a multi-component SLq(2)
labelling (route 1's real gap). **Route 3's gap is CODE, not acquisition** — all
nine held papers give integral formulas or geometric interpretations, none gives
the Magnus expansion of a longitude in the free group.

### ROUTE 2 IS BLOCKED, and the reason inverts the arc's framing

The corpus's only route to a NUMBER for `ac(L_k, L)` — which is an infimum over
homotopies and not directly computable — is the complement-genus lower bound in
the sentence after eq. (43). **That sentence is qualified "for borromean links",
and the corpus drops the qualifier**: `qou-a9li` and `qou-b5yi` both quote the
genus clause without it, and I repeated the elision from their wording before
reading the source.

The qualifier is load-bearing. A compact oriented `S ⊆ R³ \ L_j` with `∂S = L_k`
forces `lk(L_k, L_j) = 0`, since `[L_k] = [∂S] = 0` in `H₁(R³ \ L_j) ≅ Z` and that
class IS the linking number. So where some `lk ≠ 0` the minimised-over set is
EMPTY — the estimate is ill-posed off the Brunnian class, not merely weaker.

**Measured: 0 of 30 components** of the derived carrier have all pairwise linking
vanishing — every isotope (2H, 3H, 3He, 4He, 6Li, 8Be), BOTH crossing-resolution
branches. Checked in both because `lk` is branch-dependent, unlike `mu = A+1`.

**The inversion:** the handle applies exactly on the Brunnian class, which in this
arc means **L6a4** — the A=3 CENSUS assignment, the admitted AME-driven fit that
owner ruling 2026-08-29 retired. Route 2's only computable handle works on the
carrier that was retired, and not on the derived one.

- Lean: `QOU/Mass/FreedmanHeGenusHandleNeedsVanishingLinking.lean`, lean-direct
  exit 0, sorry-free; `no_component_is_brunnian` covers the ENDPOINT case a
  "every vertex has a successor" argument silently misses; two declarations
  depend on no axioms at all. The homological step is DELIBERATELY not
  formalised (Seifert surfaces / H₁ of a link complement are not cheaply
  available in this Mathlib; asserting them as a class would be the
  axiomatisation-is-not-a-proof pattern).
- Probe: `computations/probes/fh_genus_handle_requires_brunnian_probe.py`, 4/4.
  The qualifier check is a LIVE read of the held source, so a re-ingestion that
  changed the text fails the assertion rather than leaving a remembered reading.

**SCOPE (b) on the HANDLE**, invariant cited (complement homology). Eq. (43) is
untouched and remains a true lower bound. `ac(L_k, L)` itself is untouched —
nothing here says it is small or zero. A different lower bound on `ac`, not
routed through a complement genus, is NOT excluded and is not examined.

### A method error of mine, worth more than the fix

Both probes were emitting witnesses with no `q0Anchor`, so the q0-anchor refill
ratchet counted them as NEW-unstamped. My #6515 PR body claimed "the new files
appear nowhere in the gate log" — established by grepping the log for the
filename. **The ratchet reports a COUNT, not filenames**, and the only line
naming the file was `skipped: (new file — no HEAD copy to compare)`, which reads
like a clean bill and is not one.

    without the new files             NEW (not in baseline) : 40
    with them, no q0Anchor            NEW (not in baseline) : 41
    with both declaring independent   NEW (not in baseline) : 39   (drains one)

Fixed at the producer in both (`independent` + a reason; a `q0Value` on an
`independent` witness is a contradiction the audit flags `Q0_FLIP`). No baseline
touched. **Rule: to test whether your files affect a ratchet, REMOVE them and
diff the counts.** Grepping a gate log for your own filename cannot detect a gate
that counts.

### Still open on this bean

Routes 1 and 3, unchanged in status by the above. Route 1 needs the link
generalisation of the SLq(2) labelling (`mu > 1`); route 3 needs a first `mubar`
value on the min-span triples `{i, i+2, i+4}`, which needs the Magnus-longitude
machinery the corpus does not have.



## ROUTE 3 RESULT 2026-09-04 — the min-span triples are DEFINED exactly where they VANISH

This bean's route-3 hand-off says: *"No `mubar` value has been computed -- this is
combinatorics of which triples are defined, not of what they equal. Computing one
needs the Magnus expansion of a longitude in the free group, which is real work and
is not done."*

**The computation is unnecessary.** On this carrier every `Delta = 0` triple has
`mubar = 0`, and the reason is its own defining condition.

### The mechanism, in one step

A monotone braid closure -- one contiguous run per generator, which the canonical
atom word satisfies -- is a connected sum `#_g T(2, e_g)` (verified 32/32 in
SnapPy, 2026-08-25 audit). Each summand is ONE generator's run, so it touches only
the components holding strands `g` and `g+1`. A shared summand **links** two
components. Contrapositively a triple with `Delta = gcd(lk) = 0` -- exactly the
condition for `mubar` to be a genuine integer -- shares **no** summand, so its
sublink is a 3-component **unlink** and every Milnor invariant vanishes on it.

    the condition that makes mubar DEFINED is the condition that makes it ZERO

### Measured, 4/4

  every generator touches at most                       2 components  (the premise)
  generators joining two members of a min-span triple    0            (the result)
  mu = A + 1                                             8 of 8 isotopes
  min-span family size = A - 3                           8 of 8 isotopes

**Branch-independent**, which is the strongest thing about it: which components a
generator touches is fixed by the induced PERMUTATION, and a superposition letter
`c*sigma_g + d*1` projects to the same transposition as its `sigma` branch. So
unlike `lk` this is ONE measurement, not a sampling over `2^(2A+1)` resolutions.

### Lean

`QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean`, lean-direct exit 0,
sorry-free. `separated_of_delta_zero` -- the whole content -- depends on **no
axioms at all**, and needs no path structure, no minimality and no
`Delta`-arithmetic: it is the contrapositive of "a shared summand links", so it is
as general as the connected-sum decomposition itself. `chainCarrier` +
`chainCarrier_joins_consecutive` exhibit a configuration satisfying every
hypothesis whose `joins` is inhabited, so the separation result cannot be read as
describing an empty relation.

Deliberately NOT formalised: `mubar` itself, the connected-sum decomposition, and
"Milnor invariants vanish on an unlink" -- none cheaply available in this Mathlib,
and a class asserting them would be the axiomatisation-is-not-a-proof pattern.

### Convergence with sibling PR #6561 (`qou-kru4`)

#6561 proves from the ALGEBRA that a monotone word's Markov trace factorises over
generators, so `tr_M` cannot carry a `mubar` or an `ac`-type cross-component
quantity. Route 3 here proves from the TOPOLOGY that there is no `mubar` to carry.
**Both trace back to monotonicity.** So non-monotonicity is the single
discriminating question for the in-algebra cross term (#6513), a hyperbolic
carrier, and a nonvanishing Milnor invariant alike -- three frontiers, one
hypothesis.

### SCOPE (b) on the min-span family, invariant cited

Does **not** refute route 3 in general: on a genuinely Brunnian carrier like L6a4
the summand hypothesis fails and `mubar_123 = 1`. Does **not** touch the
`Delta = 2` triples, which touch a linked pair and retain ONE BIT -- those are the
residual and are not examined.

### Where all three routes now stand

- **Route 1** — capped at even A (`SLq2LabelParity.lean`, on main). Open question
  is a LINK generalisation (`mu > 1`) of the SLq(2) labelling; the framework half
  is finished, and this is the one route with a genuine acquisition gap.
- **Route 2** — BLOCKED. The complement-genus handle is Borromean-only; 0 of 30
  components qualify.
- **Route 3** — the min-span family gives `mubar = 0` identically. Residual: the
  `Delta = 2` one-bit triples.



## 2026-09-04 — the cyclic square BREAKS route 3's premise and does NOT reopen route 3

Answers sibling #6561's second result, which lands the one escape route 3's own
premise leaves open. Tested rather than assumed either way.

Route 3's argument is **monotone-specific**: each summand touches at most 2
components, which is what turns `Delta = 0` into separation. #6561 proves
(sorry-free, `RevisitClassCrossTerm.lean`) that the cyclic square
`(g_m g_{m+1})^2` is the ONLY non-monotone shape yielding a trace cross term --
and it spans THREE strands, so it is precisely what could break the premise.

**I guessed local knotting, and was wrong.** `(g_m g_{m+1})^2` closes to `T(3,2)`,
a knot, so the tempting reading is a knotted summand on one component (Milnor-inert).
Measured: it spans **3 distinct components in 188 of 694 insertions**. The premise
genuinely breaks.

**The conclusion survives, for a different reason than it was proved by.** In ALL
188 spanning cases at least one pairwise linking number among the three components
is nonzero, so `Delta != 0` and `mubar` is not a genuine integer there anyway. The
insertion that joins three components is the same one that links them.

`cyclic_square_does_not_reopen_milnor_probe.py`, 4/4: premise-breaks = yes;
reopening triples = **0 of 188**; insertions tested = 694; integrality violations = 0.

Two method notes, both from getting it wrong first: insertions are SAMPLED ACROSS
THE WORD, not appended (braid letters do not commute, and the first pass was
append-only, which would have read stronger than it was); and an earlier draft's
fourth assertion was VACUOUS -- a counter initialised to 0 and never incremented --
now a real odd-crossing-sum check, the same bug class as this bean's own earlier
`lk = -3/2`.

**What this does to the non-monotonicity framing.** #6561 said a trace cross term
and a hyperbolic carrier "both require a non-monotone word, so they are the same
discriminating question". The REQUIREMENT is shared; the two CONSEQUENCES are not,
and both now have verdicts:

  - trace branch   -- #6561 measured: +0.78/+0.71/+1.00/+0.68 MeV against residuals
                      1.8/7.8/7.0/27.4. Right sign, shrinks with A. Scope-(a) negative.
  - closure branch -- measured here: does not reopen mubar on that shape.

So it is one hypothesis with two testable consequences, both now tested on the one
shape that admits them. Do NOT compress that back to "the same question" -- the
shared requirement is what made it worth testing twice.

SCOPE (a), narrow: one shape, all-positive inserted crossings, sampled positions,
4 isotopes. NOT a proof that no non-monotone word reopens route 3 (a mixed-sign
insertion could cancel a linking number and is not covered). The `Delta = 2`
one-bit triples remain the stated residual. The Lean is UNCHANGED.



## 2026-09-04 — LINKS, and a correction to my own held-literature counts

Owner asked for links. Building the list exposed two errors in the counts I put in
this bean, the ledger and PR #6560 — both mine, both one cause: I reported
**keyword hits on files** and called them **held sources on a topic**.

**Files vs works.** Four hits are `duplicate_of` copies of another hit (verified
from section front-matter): `0808.1533v1` of `v3`; `0901.1612v1` of `deturck-…`;
`symmetry-11-01298` of `1910.09966v1`; `s10052-023-11923-y-a` of `2306.13098v2`.

**The patterns were far too wide.** Route 2's was `asymptotic crossing|Freedman`,
and "Freedman" matches any bibliography containing a person of that name.

                      reported   contains core term        distinct works
    route 1 SLq(2)       10       2  (`SLq(2)`)                  2 core + 6 milieu
    route 2 Freedman-He  12       4  (`asymptotic crossing`)     3
    route 3 Milnor        9       6  (`Milnor|triple linking`)   5 core + 2 adjacent

So route 2's "12 held documents" is **three works**. **Do not quote 10 / 12 / 9.**

**No verdict changes.** Every result rests on core-tier sources; the correction is
about how much surrounding literature exists, not about what the primary source
says. What changes is what "held" is worth as a claim.

**Four held sources have NO resolvable external link** — `khesin2003`,
`moffatt-ricca-helicity`, `mellor-melvin2003`, `evans-berger1992` carry neither
`DOI` nor `URL` in `references.ts`, and no arXiv/DOI stamp appears anywhere in
their held text (checked in BOTH tiers). **Two are core route-2 sources** (Khesin;
Moffatt & Ricca). No identifier is invented. Worth a bibliography pass — not done.

Also: `arxiv-2106.01332v4` is held but **not registered** in `references.ts`.

Per-work links (arXiv/DOI + held-copy path + the exact section:line for the two
load-bearing citations) are in the §Links section of
`docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md`.


## 2026-09-05 — route 3 needs only ONE component separated; the residual is the chain

The Δ = 2 residual was reopened by the cyclic-square perturbation result (#6679). Going
back to it produced a strengthening of route 3 and an exact location for what is left.

**Route 3's hypothesis was stronger than its argument.** `μ̄_abc` is the `h_a h_b`
coefficient of the Magnus expansion of `λ_c`. If **one** component splits off from the
other two, that coefficient vanishes — the remaining pair may be linked to each other
arbitrarily. The merged `MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean` asks for
all three pairwise linking numbers to vanish (`Δ = 0`); only two of the three are used.

New Lean `QOU/Mass/OneSeparatedComponentSufficesForMilnorVanishing.lean` — sorry-free,
`lean`-direct exit 0, and `splitsOff_of_unlinked` depends on **no axioms at all**.
`allSplitOff_of_delta_zero` recovers the merged result three times over, so the
strengthening is visibly a strengthening. (Symmetry of `lk` is an explicit hypothesis:
the merged theorem pairs hypotheses to conclusions in matching index order and never
needs it; `SplitsOff k i j` fixes `k` first and does.)

**Reclassify by SHAPE, not by Δ.** SEPARABLE = some component unlinked from both
others; CHAIN = none is. Measured on the carrier, 7 isotopes, **both** branches
(identical in each):

    SEPARABLE  393   0 nonzero mubar   (of which Delta = 2: 182)
    CHAIN       31   0 nonzero mubar   (all Delta = 2)

The merged theorem reaches the **211** that are separable *and* `Δ = 0`. The **182**
separable `Δ = 2` triples are reached for the first time: coverage goes `211 → 393` of
424, i.e. 49.8 % → 92.7 % — **+42.9 percentage points, or +86.3 % relative**. Both are
given because "43 % more" reads as the relative figure and is not it. All from deleting
a hypothesis rather than adding an argument.

**The residual is one shape, verified not inferred.** 31 per branch equals
`Σ (A−1) = 1+2+2+3+5+7+11`, the count of `{i, i+1, i+2}` on a path of `μ = A+1`
components — but a count match is corroboration, so the probe checks each triple's
indices: **62/62** across both branches are consecutive. `splitsOff_or_consecutive`
proves this is forced (separable or consecutive, no third case) and
`consecutive_has_no_separable_component` proves the trichotomy sharp. So the residual
cannot be chipped at further with linking-number bookkeeping.

**What would close it:** `μ̄` of length `k` vanishes unless all `k` indices lie in one
connected-sum summand. With the measured "each summand touches at most 2 components"
that closes the chain case *and* subsumes the new file. **Not asserted, not
formalised** — axiomatising it would be the axiomatisation-is-not-a-proof pattern.

**Empirically the residual vanishes, and generically for monotone words**: 0 over the
carrier's 31, 0 over 534 monotone-random chain triples (144 at `Δ = 2`). Non-monotone
control gives nonzero in both shapes (26 separable, 1 chain), so the null is about
monotonicity, not the scanner.

**Side finding — #6679's null is not vacuous.** `Δ = 1` makes `μ̄ = 0` vacuously
(`ℤ/1`). Monotone arm splits `{Δ0: 319, Δ1: 870, Δ2: 690}` — 46.3 % vacuous, but 1009
non-vacuous triples all zero, 690 at exactly `Δ = 2`. The merged null stands.

Probe `computations/probes/milnor_one_separated_component_and_the_chain_residual_probe.py`,
5/5, idempotent, integer arithmetic throughout.


## 2026-09-05 — the chain residual CLOSES, and it needed no connected-sum citation

The entry above left 31 chain triples open and named as their blocker *"`μ̄` of length
`k` vanishes unless all `k` indices lie in one connected-sum summand"* — a statement no
held source in this corpus states. **It is not needed.**

**The mechanism.** On a chain, `lk(x,y) = 0`, so with `u = lk(hub,x)`, `v = lk(hub,y)`
the indeterminacy is `Δ = gcd(u,v,0) = gcd(u,v)`. On a **monotone** closure the two far
meridians occupy contiguous, **non-interleaved** blocks of the hub's longitude — one run
per generator is what monotone means — so the degree-2 Magnus coefficient is a product
of block sums:

    eps_{x,y}(λ_hub) = u·v        eps_{y,x}(λ_hub) = 0

Measured **596/596** monotone (62 carrier, 534 random); **22/78** and **29/78** off
monotone. Then `gcd(u,v) | u | u·v` **unconditionally** ⇒ `μ̄ = 0`. New sorry-free
`QOU/Mass/ChainTripleMilnorVanishesByGcdDividesProduct.lean`; `chain_mubar_vanishes`
depends only on `propext`. **Every triple of the derived carrier is now covered — 393 by
one separated component, 31 by this.**

**Order-dependence is the point, not a defect.** `u·v` one way, `0` the other. That is
exactly what the mod-`Δ` indeterminacy absorbs: both are divisible by `Δ`, so the
invariant is zero either way and nothing rests on a convention.

**The off-monotone control is a REAL counterexample.** Of 78 non-monotone chain triples
exactly one has `Δ ≥ 2`, and divisibility **fails** on it (77/78). So `eps_eq` is
load-bearing, not decorative.

### Two of my own errors, both recorded in the probe

1. **I predicted `eps = u·v`, then wrongly recorded it refuted.** The symmetrised sum
   that `milnor_mubar_vanishes_on_every_triple_probe.py` computes gave an honest integer
   `0` on 62/62 and 534/534 — because it lands on `eps_{y,x}`, the ordering that *is*
   zero. A symmetrising scan can turn a general mechanism into what looks like a
   coincidence; only splitting the sum into its three terms separated them.
2. **I quoted "all 71 non-monotone chain triples have `Δ = 1`"** — i.e. an entirely
   vacuous control — from a scratch run building a *fresh* seeded RNG per arm. The probe
   uses **one** RNG consumed sequentially (matching the #6679 genericity probe so the
   arms stay comparable): 71 → 78, and the counterexample appears. **Same trap as
   #6679's `251/2080`, three days later.** The probe's numbers are authoritative.

The stale "what would close it" paragraph in
`OneSeparatedComponentSufficesForMilnorVanishing.lean` is corrected in place.

Probe `computations/probes/chain_triple_magnus_coefficient_is_the_product_probe.py`,
5/5, idempotent, integer arithmetic throughout.


## 2026-09-05 — `eps_eq` derived: eight sharper facts replace one opaque one

The chain closure rested on `ChainTriple.eps_eq` as a bare measured hypothesis. It is
now a **theorem given three braid-word hypotheses**, and the arithmetic that makes
`gcd u v | u·v` applicable is machine-checked.

**Decomposition, measured 596/596 monotone (62 carrier both branches + 534 random), all
degrading off monotone (78):**

*Tier 1 — braid-word facts, still assumed:* each pair crosses at ONE generator (56/78,
58/78) · the two generators differ (37/78) · `g_x < g_y ⟺ x < y` (36/78) · runs have
even length (40/78) · run length is exactly `2|lk|` (30/78).

*Tier 2 — consequences, consumed by the Lean:* signed sum of each far component's
letters in `λ_hub` equals its linking number (51/78, 53/78) · each block contiguous
(56/78, 67/78) · blocks disjoint with `x` before `y` (18/78).

**Proved** in `QOU/Mass/EpsEqFromMonotonicity.lean` (sorry-free, 0 errors):
`epsCoeff_append_of_blocks` — a block-split word has `ε_{x,y} = (Σ block A)(Σ block B)`
and `ε_{y,x} = 0`. That is the whole arithmetic of `eps_eq`, and it is a statement about
**lists**, no topology. `eps_eq_of_blocks` composes it to `ε = u·v`.
`carrier_shape_gives_four` depends on **no axioms at all**.

**Still assumed:** tier 1. Deriving it needs the strand-permutation bookkeeping of a
monotone word formalised — positions, runs, who passes under whom — a substantially
larger object than anything in this arc. Named as borrowed in the hypotheses `hA`, `hB`,
`hsum` rather than elided.

**Do not overstate the gain.** `eps_eq` was one hypothesis about a Magnus coefficient;
it is now a theorem given three about a braid word. The part that could have been subtly
wrong is checked; the combinatorics of which strand is where is not.

**Third instance of the same figure trap.** A scratch run against a *per-arm* RNG gave
`32/78` for the `2|lk|` row; the probe (one RNG consumed sequentially, matching the
merged siblings) gives **30/78**. After #6679's `251/2080` and #6726's "0 of 71" this is
three; the probe's numbers are authoritative, always.

Probe `computations/probes/eps_eq_decomposition_from_monotonicity_probe.py`, 5/5,
idempotent, integer arithmetic throughout.


## 2026-09-05 — tier 1 is a THEOREM, and the path linking graph comes with it

`EpsEqFromMonotonicity.lean` left tier 1 assumed, saying it needed "the
strand-permutation bookkeeping of a monotone word formalised … a substantially larger
object than anything in this arc". **That was wrong about the size.** It is two one-line
recursions.

**The argument.** Generator `g` moves only positions `g`, `g+1`, and a monotone word
runs them ascending — so when run `R_g` begins, **position `g+1` still holds strand
`g+1`**, untouched. Every crossing of that run is therefore between one *fixed* strand
pair `(pStart g, g+1)`. An even run restores the pair, an odd run swaps it, so the
closure permutation is `∏_{e_g odd} σ_g` and its cycles are the maximal consecutive
blocks of odd-exponent generators. Hence: an **odd** run crosses two strands of the
**same** component (self-crossings, invisible to linking); an **even** run crosses
**adjacent** components.

New sorry-free `QOU/Mass/MonotoneWordComponentStructure.lean`. Every tier-1 fact is a
reading of one theorem, `components_differ_iff_even`: even run length is
`even_of_components_differ`; one generator per component pair is
`distinct_even_generators_distinct_pairs`; generator order matching component order is
`compIdx_mono`.

**It also derives what the whole arc assumed.** `linking_only_between_adjacent` proves
that only consecutive components can be linked — i.e. the `P_μ` path shape, which
`PathCarrier` takes as a *hypothesis* and which this arc has carried as a **measurement**
across 7 isotopes and both crossing-resolution branches since the carrier was derived.

**Five predictions, measured before the Lean was written: 414/414** (400 random monotone
words + the carrier's 14 branch-isotope pairs) — inter-component crossings only at even
runs · components are strand intervals · linking graph is exactly the path · `μ = 1 +
#even runs` · every even run is wholly inter-component.

**The honest remainder, one level lower:** that `pStart`/`compIdx` really describe a
monotone closure's positions and cycles. That needs braid words and cycle decomposition
as Lean objects; the probe stands in for it.

Both sibling docstrings corrected in place — `EpsEqFromMonotonicity`'s "still assumed"
section and `OneSeparatedComponentSufficesForMilnorVanishing`'s `PathCarrier` note.

Probe `computations/probes/monotone_word_component_structure_probe.py`, 6/6, idempotent.


## 2026-09-05 — the `pStart` half of the modelling assumption is PROVED

`MonotoneWordComponentStructure.lean` named its own remainder: that `pStart` and
`compIdx` really describe a monotone closure's positions and cycles, *"not attempted"*.
The `pStart` half is now done, in `QOU/Mass/MonotoneWordPositionTracking.lean`
(sorry-free, 0 errors).

**Model.** `posAfter e g` is the position→strand map after runs `0…g-1`. `e_g` crossings
of one adjacent pair compose to the identity when `e_g` is even and to a single swap when
odd — which is why only parity survives and why this is a one-step recursion rather than
an iteration.

- `posAfter_of_le` — every position `≥ g+1` is untouched after `g` runs. **This is where
  ascending order is used**: run `h < g` moves only positions `h, h+1 ≤ g`.
- `posAfter_succ_self` — hence position `g+1` still holds **strand `g+1`** when `R_g`
  begins, so the pair that run will cross is fixed before it starts.
- `posAfter_self` — position `g` holds `pStart e g`: the recursion is the right one.
- `crossing_pair_of_run` — run `g` crosses exactly `(pStart e g, g+1)`. That is the
  sentence tier 1 was resting on, now a theorem.

Non-vacuity exercises both branches: all-odd carries the left strand to `0` (maximally
fused, matching `allOdd_compIdx`), all-even leaves position `g` holding strand `g`
(maximally split, matching `allEven_compIdx`).

**What remains is now exactly one thing:** that `compIdx` counts components — the cycle
decomposition of `∏_{e_g odd} σ_g` into maximal consecutive odd blocks. Separate
combinatorics, not attempted, and **measured not assumed**: probe P2 (components are
consecutive strand intervals) and P4 (`μ = 1 + #even runs`), 414/414.

Chain now reads: `pStart` **proved** to model the word · `compIdx` **measured** to model
the cycles · everything above them proved from those two.

Verified against the dependency compiled **from source** (`lean -o` into a scratch
LEAN_PATH), not against a restored olean — this is the first file in the arc to import a
QOU module, so the per-module cache staleness on main would otherwise reach it.


## 2026-09-05 — `compIdx` closed: the chain is proved end to end from the braid word

The last gap. `MonotoneWordPositionTracking` said `compIdx` counting components was "not
attempted" and would need "the cycle decomposition of a product of ascending adjacent
transpositions". **It needs no such thing** — the lemmas already proved give it.

**The closed form.** With `π = posAfter e N` the closure permutation, for `i < N`:

| `e i` | `π i` | stays in class because |
|---|---|---|
| **odd** | `i + 1` | `compIdx (i+1) = compIdx i` — an odd run adds 0 |
| **even** | `pStart e i` | `compIdx_pStart`, proved in #6775 |

So `π` is the **cyclic shift on each `compIdx` class**. Both inclusions drop out:
`compIdx_posAfter` puts every cycle inside one class; inside a class every step is odd
(`step_within_class`), so a class is traversed upward and closed by the even step at its
top — `pStart e i` being the class minimum (`pStart_le`, `lt_compIdx_of_lt_pStart`).
**Cycles = classes**, which is what `compIdx` was assumed to compute.

New sorry-free `QOU/Mass/MonotoneWordCycleStructure.lean`, 9 declarations.

**Five predictions, 414/414** (400 random monotone words + the carrier's 14
branch-isotope pairs). The load-bearing one is **E**: the Lean's `posAfter` recursion,
transcribed into the probe, reproduces `analyse`'s `perm` array **exactly** — entry for
entry. That is what stands in for the one step this arc never formalises, and agreeing on
the permutation is strictly stronger than agreeing on the component partition, which a
reimplementation could do by sharing an assumption.

**The chain is now proved end to end from the braid word:**
`posAfter` models positions → `compIdx` counts components → tier 1 of `eps_eq` → `eps_eq`
→ `μ̄ = 0` on every triple of the derived carrier.

**The remaining floor, and it is a definition not a gap in an argument:** that `posAfter`
*is* a monotone braid word's position map and the closure's components *are* its cycles.
"Braid word" and "closure" are not Lean objects anywhere in this arc. Named as such in
every file of the chain, and measured 414/414.

Both sibling docstrings corrected in place.


## 2026-09-05 — CORRECTION to my own framing: the canonical word is NOT monotone

Found while starting `qou-brng`. **No merged number is wrong; one framing claim is.**

**What happened.** `7db032fb48` (today **07:53Z**, `qou-hu1f`) changed
`atom_canonical_crossings`' default `intra_order` from `grouped` to `borromean`, so each
nucleon's confinement core is the alternating `(σ₀σ₁⁻¹)³` and each generator's letters are
**interleaved**. Measured on the current default:

    2H   23 letters, 19 runs over 5 generators   one_run_per_gen=False  ascending=False
    4He  47 letters, 39 runs over 11 generators  one_run_per_gen=False  ascending=False

Under `grouped` both are monotone (5 runs / 5 gens, 11 / 11, ascending).

**So "the derived carrier is a monotone closure" is FALSE for the current default word**,
and I used that sentence to carry the Lean theorems onto the carrier. The theorems are
about monotone words and are unaffected; what fails is the *application* to the canonical
word as it now stands.

**What is NOT affected — measured, both conventions, 14 branch-isotope pairs:**

    grouped    triples 848  SEP 786  CHAIN 62  nonzero mubar 0  path linking 14/14
    borromean  triples 848  SEP 786  CHAIN 62  nonzero mubar 0  path linking 14/14

Identical. Every carrier figure in #6560/#6634/#6679/#6726/#6775/#6858/#6872 stands, and
the `Δ`-classification and chain/separable split are unchanged.

**Prediction E is passing for a reason other than the one its docstring gives.**
`monotone_word_cycle_structure_probe.py` calls E the validation that `posAfter`/`compIdx`
model *a monotone closure*. The carrier is not monotone, yet `perm == pi` on **14/14**
carrier words. That is not luck — on random *non-monotone* words the same test agrees on
only **22/400 (5.5 %)**. So E is measuring something real about the carrier and mislabels
what.

**Hypothesis (not established):** the Borromean core contributes an *even* number of
letters per generator within each nucleon, so per-generator parity — which is what the
permutation depends on here — is unchanged, leaving components and linking identical while
destroying contiguity. That would explain both the identical table and the 14/14.

**What this costs.** The chain "proved end to end from the braid word" reaches *monotone*
words; the canonical word is currently outside it, with its structural consequences intact
by measurement rather than by the theorem. The honest statement is weaker than the one I
made this afternoon, and the fix is either to prove the parity hypothesis above (which
would restore the application) or to scope every carrier sentence to "the grouped word".

Not fixed here — measured and recorded. Follow-up before any further carrier claim.


### Same day, hours later — my parity hypothesis is REFUTED; option 1 is dead

The correction above proposed two fixes and said I expected option 1 (prove the
even-per-generator parity hypothesis, restoring the application). **Measured, and it does
not hold.**

**H1 — TRUE, and stronger than I guessed.** The per-generator *letter counts* are
identical between `borromean` and `grouped`. The odd-count generator sets match exactly:
²H `[0,2,3]`, ³H `[0,2,3,5,6]`, ⁴He `[0,2,3,5,6,8,9]`, ⁶Li `[0,2,3,5,6,8,9,11,12,14,15]`
— same under both conventions.

**H2 — FALSE.** The permutation is *not* determined by that parity vector. Comparing each
word's true permutation against the ascending word carrying the same per-generator
parities: **7/14** carrier words agree (the 7 grouped ones, which are monotone and for
which this is just the monotone reduction), and **70/400 (17.5 %)** random non-monotone.

So the identical closure structure — 848 triples, 786 separable, 62 chain, 0 nonzero
`μ̄`, path linking 14/14 under both conventions — is **not** explained by parity
preservation. My stated mechanism is wrong.

**The surviving candidate, not established:** the two words have *different*
permutations but the *same orbit partition*. Components are cycles, and two distinct
permutations can share their orbits — that would give identical components, linking and
triples while the permutations differ, which is exactly the pattern measured. Testing it
means comparing the two permutations' orbit partitions directly, not their values.

**Consequence for the correction above:** option 1 is dead as stated. The live options
are the orbit-partition route (if it holds, it restores the application by a different
argument) or option 2 — scope every carrier sentence to the grouped word.

Recorded rather than fixed. Noting that I wrote "the outcome I'd expect" against option 1
about an hour before measuring it to be false.


### RESOLVED — same shape, shifted components; and it is the sharper finding

The orbit-partition candidate is **also refuted**, and resolving why reconciles the two
measurements that looked contradictory.

**Measured, 14 carrier branch-isotope pairs:** permutations identical **0/14**, orbit
partitions equal **0/14**. Yet the closure table is identical under both conventions
(848 triples, 786 separable, 62 chain, 0 nonzero `μ̄`, path linking 14/14).

**Not a contradiction — the partitions are SHIFTED BY ONE STRAND:**

    4He grouped     [0,1] [2,3,4] [5,6,7] [8,9,10] [11]
    4He borromean   [0]   [1,2,3] [4,5,6] [7,8,9]  [10,11]

Same `μ = 5`, same block-size multiset `{1,2,3,3,3}`, different strands. Every count is a
function of `μ` and the path shape, so every count agrees while no component does. The two
words are **not the same link**; their linking graphs are **isomorphic**.

**So the correct statement, replacing both my earlier attempts:**

- carrier **counts** are convention-independent — every figure in #6560…#6872 stands under
  both words, now for a *reason* rather than by coincidence;
- carrier **component identity** — which strands form which component — is **not**. It
  shifts by one under the 07:53 default change.

**Why that matters beyond bookkeeping, and it bears on `qou-brng`.** Anything that
*identifies a component with a nucleon* is convention-dependent. The coordination-graph
route to the binding term needs exactly that identification: its vertices are supposed to
be nucleons. Measured here, the vertex↔nucleon assignment is not fixed by the framework —
it moves with an intra-word convention chosen for unrelated reasons (`qou-hu1f`). That is
an obstruction of the same family as `qou-m07y`'s arrangement-dependence, reached
independently and at the level of the *carrier* rather than of a bond ansatz.

**Scope (a)** — 7 isotopes, both crossing-resolution branches, two conventions. Not a
refutation of the coordination route; a statement that its vertex labelling is not
currently well-defined.

**Three hypotheses of mine, in order, all refuted by measurement within two hours:** the
even-per-generator parity route; the shared-orbit-partition route; and before them the
framing that the carrier is a monotone closure at all. The counts survived all three,
which is why they are worth more than the framings were.


### The relabelling is STRAND REVERSAL — and that restores the application, with one measured step

Chasing the "isomorphic linking graphs" candidate from the entry above.

**Measured, 14/14 carrier branch-isotope pairs:** the borromean closure's component
partition is *exactly* the grouped one under strand reversal `i ↦ n−1−i`.

    4He grouped              [0,1] [2,3,4] [5,6,7] [8,9,10] [11]
    4He grouped, reversed    [0]   [1,2,3] [4,5,6] [7,8,9]  [10,11]
    4He borromean            [0]   [1,2,3] [4,5,6] [7,8,9]  [10,11]

**And the crisper claim I reached for is FALSE — checked before asserting it.** The *words*
are not related by reversal: identical 0/7, `reverse` 0/7, `reverse + generator flip` 0/7.
²H grouped is `[0×7, 1×4, 2, 3×7, 4×4]`; borromean is `[0,1,0,1,0,1,0,0,1,0,0,2,…]`. The
relation is between the **closures' partitions**, not between the words — a much weaker
statement, and worth stating as such since "the words are reverses" would have made the
transfer a triviality.

**What it buys, and the transfer step is measured not proved.** The **grouped** word *is*
monotone, so the whole Lean chain applies to it directly. Every structural conclusion —
path linking graph, the separable/chain split, `μ̄ = 0` on all triples — then holds for the
borromean carrier via the reversal relabelling, which is measured on every invariant this
arc computes (848 triples, 786 separable, 62 chain, 0 nonzero `μ̄`, path linking 14/14, all
matching).

**So the honest chain today is:** theorems (proved, monotone words) → grouped carrier
(monotone, so they apply) → borromean carrier (by a *measured* relabelling, 14/14). One
measured link where this afternoon I claimed none. That is materially better than the two
options in the correction above — option 1 was refuted, and option 2 (scope everything to
grouped) turns out to lose nothing, because the transfer exists.

**Not established:** that the two closures are the *same link*. Same partition under
reversal plus matching linking data on every invariant computed here is evidence, not a
proof of link equivalence.

**Four of my hypotheses refuted by measurement in one evening** — carrier-is-monotone,
parity preservation, shared orbit partition, words-are-reverses. The fifth (partitions
related by reversal) held. The counts survived all five, which is the pattern worth
keeping.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

<!-- ported 2026-11-15 from PR #6359 (branch predates the beans/defs and folio/ moves) -->

## ROUTE 3 CLOSED 2026-08-31 — the DEFINED triples are exactly the TRIVIAL ones

This supersedes the "partially available from A=4" conclusion recorded above,
and it did not need the Magnus expansion the next-step entry called for.

### The cheap decisive measurement

Between non-adjacent components the closure has **ZERO crossings** -- not merely
a zero signed sum, which is all the previous probe established. Only the `mu-1`
consecutive pairs carry any crossing at all.

Stronger, and checked structurally rather than argued from the diagrammatic
"no inter-component crossings implies split":

  * every component occupies a **contiguous block** of strand positions;
  * for every minimal-span triple `{i, i+2, i+4}`, the three blocks are
    **pairwise disjoint intervals** and **zero letters act on two members**.

So the sublink is the closure of a braid on three disjoint, non-interacting
contiguous blocks -- each closes in its own annulus. **Split by construction.**

### The collapse

    Delta(ijk) = 0  =>  the triple is split  =>  mubar(ijk) = 0.

Combined with the indeterminacy split: triples touching a linked pair are
indeterminate (`Delta` 1 or 2), and triples that are well defined are zero.
**No non-trivial well-defined Milnor triple invariant exists in this closure at
any A.** The Magnus expansion would return zero on exactly the triples where it
is meaningful, so it is not worth running.

Definedness and triviality coincide **because the linking graph is a path**: on
a path, "not linked" and "never interacts" are one condition. A Brunnian link
separates them -- it interacts *without* linking, which is exactly what `L6a4`
does and this word cannot.

### Consequence for any future assignment

The requirement is now sharp and checkable: a nucleus->link map whose closure
supports a nonzero well-defined Milnor invariant must have a pair that
**interacts without linking**. The path structure of the canonical word forbids
it, so this is a requirement on the ASSIGNMENT, not on the invariant.

### Lean

`QOU/Mass/MilnorDefinedTriplesVanish.lean` -- sorry-free, lean-direct exit 0,
`#print axioms` = **[propext]** only on all four. `PathLinkingStructure` carries
the two measured facts and the classical "split implies vanishing" as
hypotheses; the theorems derive the collapse (`Delta = 0 -> mubar = 0` is NOT a
field). §3b-cond used honestly.

### The minimal-span subfamily entry above is superseded too

It named `{i, i+2, i+4}` as a canonical bounded-degree family with the right
scaling. The family is still canonical and still correctly scaling -- and its
invariants are all zero. Recorded rather than deleted: the counting was right
and the conclusion it was heading toward was not.


## The path is a CONVENTION, not a derived fact (2026-08-31)

Every route closed today died on the same structure -- the linking/interaction
graph of the atom word is a **path**. Read at the construction rather than
inferred: `mass_at_3A_proper.atom_braid_word_3A`'s own docstring says

  > for each nucleon k, apply intra g0, intra g1, then (if include_inter) the
  > appropriate pp/nn/pn crossing at **gen 3k+2**

matching "the **chain-walk convention** of
`hecke_core.atom_per_generator_volumes`". So the atom is emitted as a LINEAR
CHAIN of nucleon triples with exactly one interface per consecutive pair. The
path is the emission loop's shape, named as a convention. It is not derived
from anything, and C6 of the A>=5 constraint table already flagged the sibling
ordering choice the same way.

**Consequence.** Route 1 fails on parity (`mu = A+1` odd only for even A) and
route 3 fails because a path cannot be Brunnian. Both failures trace to the
chain walk, so the open question is no longer "which invariant" but **"is the
chain walk load-bearing, or a free choice?"** -- a much smaller question than
the one this bean opened with.

## A PRECISION FIX to my own route-3 output, before it was merged

`atom_braid_word_3A` is emphatic that it returns a **Hecke element**, not a
braid word; that there is **no single link behind it** (a weighted sum over
`2^(2A+1)` branches); and that **no topological quantity may be read off it**.

My probe and Lean said "the closure" throughout, implying an object the corpus
says does not exist. **The results survive at full strength** -- what is
measured is which strand pairs each letter acts on, and an `averaged` letter
`sigma_g - (h/2)*1` and both its resolutions project to the SAME transposition,
so the component partition, the non-interaction, and the strand blocks are
identical in every branch. The conclusion is therefore about **every one of the
`2^(2A+1)` branch closures separately**. Phrasing corrected in the probe, the
Lean docstring and the PR body rather than left to be quoted as a single-link
claim. Linking NUMBERS are genuinely branch-dependent (-1 vs -2 per bond) and
are not load-bearing for the vanishing result.

- **Round 56 Progress (`2026-11-16T21:20:58Z`)**: Opened [`litlfred/qou#8207`](https://github.com/litlfred/qou/pull/8207) (`cfc03c4131df1ea758c17554768f2274e708f38b`, Commit 1 `0a9d3f269d6c23f614dc40aac55d5f0a7b2baafd`). Keeping bean at `status: in-progress` pending owner review.
