---
# qou-768r
title: 'Derived nucleus->link map: SLq(2) (N,w,r)->irrep + Milnor/higher-helicity energy bound — held-lit survey and fetch list'
status: in-progress
type: task
priority: normal
created_at: 2026-08-31T03:46:30Z
updated_at: 2026-08-31T03:47:14Z
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
