# Pre-registration: hyperbolic volumes of the γγ atom-word closures

Written and pushed **before** any volume below is computed.

## Why

The A≥3 binding chain (`computations/binding_a3plus_full_theta_assembly.py`) uses
`B_pred = ρ·Vol(K_bind)·Σ y·dim·|Δθ|` with

    VOL_K = {D: Vol(Borromean), T: Vol(8_11), ³He: Vol(Borromean), ⁴He: 2·Vol(Borromean)}

imported from `substrate.knot_volumes`. PR #8722 (`computations/probes/a3plus_gg_candidate/`)
ran the chain on the γγ candidate word but kept those production volumes, which were not
derived for that word. This probe measures what the braid closures of the γγ candidate words
actually are. It adopts nothing.

## Words (fixed here; no word is added or dropped after computing)

`V = σ_a σ_{a+1}^{-1}`; generators 0-indexed as in `atom_braid_word_3A` and #8722.
Nucleon k occupies strands 3k..3k+2. Bond after nucleon k (k < A−1):
arm **L** = `V³` on generators (3k+1, 3k+2); arm **R** = `V³` on generators (3k+2, 3k+3).
Word order is nucleon 0, bond 0, nucleon 1, bond 1, …, nucleon A−1 (as in #8722's `word()`).

| id | word |
|---|---|
| N3 | single nucleon `V³` on (0,1), 3 strands — expected Borromean rings, Vol = 8G = 7.32772475… |
| N6 | single nucleon `V⁶` on (0,1), 3 strands |
| F3-A{2,3,4} | free: A disjoint `V³` nucleon blocks |
| F6-A{2,3,4} | free: A disjoint `V⁶` nucleon blocks |
| L3-A{2,3,4}, R3-A{2,3,4} | atom: `V³` nucleons + `V³` bonds, arm L / arm R |
| L6-A{2,3,4}, R6-A{2,3,4} | atom: `V⁶` nucleons + `V³` bonds, arm L / arm R |

20 words. A = 2 ↔ D, A = 3 ↔ T and ³He (same word, p = n on this candidate), A = 4 ↔ ⁴He.
Bond words admitted by a separate reading-3 derivation (branch
`claude/gg-internucleon-bond-2026-11-21`) are not in this list; the producer takes the bond as a
parameter so they can be added later as a new, separately pre-registered run.

## Method

SnapPy 3.x, `snappy.Link(braid_closure=[…])` (1-indexed signed generators).

## Reported, per word (every word, every column)

- number of link components;
- whether the diagram is split, and if so the pieces (spherogram `split_link_diagram`);
- `identify()` result where SnapPy finds one (exterior census match);
- SnapPy `solution_type` and `volume()` (double precision, ~15 digits), and `ManifoldHP` volume
  (quad-double) as a cross-check; a verified interval volume (`volume(verified=True)`) if
  available in this environment, else stated unavailable;
- for a split link: the per-piece volumes and their sum, labelled as a sum over pieces (the
  split link complement itself is not hyperbolic);
- for a non-split, non-hyperbolic closure: an attempted connected-sum decomposition
  (spherogram `deconnect_sum`) with per-piece volumes, labelled as such;
- the production `VOL_K` value the A≥3 chain uses for the matching atom, for comparison.

All volumes are floating-point; agreement is reported to the digits the arithmetic carries, never
as exact. The Borromean check is against `8·G` (Catalan) at 50 dps from `substrate.knot_volumes`.

## What would be read from it

Nothing is adopted. No word, arm, power or volume is chosen because its binding numbers are closer
to AME; that would be selection against the target. The outputs are: (i) whether the γγ closures
have a hyperbolic volume at all, and (ii) whether the production chain's "sum of Borromean volumes"
describes what the closures are.
