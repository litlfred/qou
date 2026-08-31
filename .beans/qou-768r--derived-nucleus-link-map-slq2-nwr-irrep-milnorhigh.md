---
# qou-768r
title: 'Derived nucleus->link map: SLq(2) (N,w,r)->irrep + Milnor/higher-helicity energy bound — held-lit survey and fetch list'
status: in-progress
type: task
priority: normal
created_at: 2026-08-31T03:46:30Z
updated_at: 2026-08-31T03:57:06Z
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
