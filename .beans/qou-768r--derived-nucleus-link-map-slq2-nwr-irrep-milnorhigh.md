---
# qou-768r
title: 'Derived nucleus->link map: SLq(2) (N,w,r)->irrep + Milnor/higher-helicity energy bound — held-lit survey and fetch list'
status: in-progress
type: task
priority: normal
created_at: 2026-08-31T03:46:30Z
updated_at: 2026-09-04T03:05:14Z
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
