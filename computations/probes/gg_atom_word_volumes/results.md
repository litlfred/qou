# Results: braid-closure volumes of the γγ atom-word candidates

Pre-registration: [`preregistration.md`](preregistration.md), commit `b2bbde3e9f`, pushed before
computing. Producer `gg_atom_word_volumes_probe.py`, witness `gg-atom-word-volumes.witness.json`
(2/2 checks). SnapPy 3.3.2 + Regina 7.4, about 10 s in total.

**Adopts nothing.** The γγ candidate word is not ruled (#7876), and no word, arm or power was
chosen by its numbers.

## Precision

- Volumes come from SnapPy and are floating point. The quad-double `ManifoldHP` value is quoted
  and the double `volume()` value is a cross-check. The largest relative gap between the two,
  over all 56 hyperbolic pieces, is 1.07e-11. Neither value is certified.
- Verified (interval) volumes are **unavailable** here. `volume(verified=True)` raises
  `SageNotAvailable` because it needs SnapPy inside Sage.
- N3 against `8·G` (Catalan, 50 dps from `substrate.knot_volumes`): |diff| = 5.1e-51. This
  matches to the 50 digits compared. It is not a proof of equality.
- Regina's normal-surface enumeration and its `isIncompressible()` test are exact
  algorithms. Hyperbolicity of each piece is SnapPy's uncertified floating-point
  structure, retried over 12 randomisations.

## Table

`v₃‖M‖` is v₃ times the simplicial volume, which equals the sum of the volumes of the hyperbolic
JSJ pieces (Gromov–Thurston). It adds over split unions and connected sums. **It is the hyperbolic
volume of the closure only when the closure is itself hyperbolic.** That happens for N3 and N6
only.

| id | comp. | structure of the closure | hyperbolic? | volume (HP, 20 sig.) | v₃‖M‖ (HP) | v₃‖M‖ / 8G | production VOL_K (same A) |
|---|---|---|---|---|---|---|---|
| N3 | 3 | L6a4 = Borromean rings | yes | 7.3277247534177521204 | 7.3277247534177521204 | 1 | — |
| N6 | 3 | L12a1882 | yes | 21.631598679192658970 | 21.631598679192658970 | 2.9520211808 | — |
| F3-A2 | 6 | split: 2 × Borromean | no (split) | — | 14.655449506835504241 | 2 | D: 7.3277247534 |
| F3-A3 | 9 | split: 3 × Borromean | no (split) | — | 21.983174260253256361 | 3 | T: 8.2863168178; ³He: 7.3277247534 |
| F3-A4 | 12 | split: 4 × Borromean | no (split) | — | 29.310899013671008482 | 4 | ⁴He: 14.655449507 |
| F6-A2 | 6 | split: 2 × L12a1882 | no (split) | — | 43.263197358385317939 | 5.9040423616 | D |
| F6-A3 | 9 | split: 3 × L12a1882 | no (split) | — | 64.894796037577976909 | 8.8560635424 | T / ³He |
| F6-A4 | 12 | split: 4 × L12a1882 | no (split) | — | 86.526394716770635879 | 11.808084723 | ⁴He |
| L3-A2, R3-A2 | 6 | Borromean # P₄ | no (composite) | — | 14.655449506835504241 | 2 | D |
| L3-A3, R3-A3 | 9 | Borromean # P₄ # P₄ | no | — | 21.983174260253256361 | 3 | T / ³He |
| L3-A4, R3-A4 | 12 | Borromean # 3 × P₄ | no | — | 29.310899013671008482 | 4 | ⁴He |
| L6-A2, R6-A2 | 6 | L12a1882 # Q₄ | no (composite) | — | 48.607621187904689063 | 6.6333852353 | D |
| L6-A3, R6-A3 | 9 | L12a1882 # Q₄ # Q₄ | no | — | 75.583643696616719155 | 10.314749290 | T / ³He |
| L6-A4, R6-A4 | 12 | L12a1882 # 3 × Q₄ | no | — | 102.55966620532874925 | 13.996113344 | ⁴He |

The prime pieces:

- **P₄** has 4 components and is not hyperbolic. Regina finds one incompressible torus that is not
  a cusp torus. Cutting along it leaves a 3-cusped hyperbolic piece that SnapPy identifies as
  L6a4 (the Borromean rings), volume 7.3277247534, and a 3-boundary Seifert-fibred piece. Regina
  names that piece `SFS [Or, g=0 + 3 punctures: (1,b)]` or `Or, g=0 + 3 punctures x S1`,
  depending on the triangulation. These are the same space, a pair of pants × S¹, since a (1,b)
  fibre can be absorbed into a boundary. The two components that the nucleon and the bond do
  **not** share are therefore parallel fibres of that S¹. So P₄ is the Borromean rings with one
  component replaced by two parallel copies, and v₃‖P₄‖ = Vol(Borromean).
- **Q₄** has 4 components and is hyperbolic, volume 26.976022508712030093. It is not in the SnapPy
  census (`identify()` returns nothing).
- The connected-sum splitting is diagrammatic (spherogram `deconnect_sum`). It is a genuine
  composite because both sides are non-trivial, being hyperbolic or containing an essential
  torus. A non-trivial connected sum has an essential annulus, so the whole closure is not
  hyperbolic. On the whole closure SnapPy also returns `contains degenerate tetrahedra` in all
  12 attempts, which agrees with this.

## What the closures are

1. **No γγ atom closure is hyperbolic** for A ≥ 2, under either arm and with either nucleon
   power. The free words are split links. The bonded words are non-split composites. So none of
   them has a hyperbolic volume that could serve as Vol(K_bind) in the A≥3 chain.
2. **Arms L and R give identical structure and identical numbers.** This matches #8722, where the
   two arms agreed in Σ|Δθ|.
3. **With V³ nucleons and V³ bonds, the bond adds no simplicial volume.** v₃‖M‖ = A·Vol(Borromean)
   for free and bonded words alike, to about 50 digits. The V³ bond adds only Seifert-fibred
   (zero-volume) JSJ pieces. Each bond turns one Borromean summand into P₄, the same Borromean
   with a doubled component.
4. **With V⁶ nucleons, each V³ bond adds 5.3444238795** to v₃‖M‖ (Q₄ − N6 = 26.9760225087 −
   21.6315986792).
5. **The production `sum of Borromean volumes` does not describe these closures.** Compare by A,
   using the V³ word on which #8722 ran the chain:

   | atom | A | production VOL_K | γγ V³ closure v₃‖M‖ | ratio |
   |---|---|---|---|---|
   | D | 2 | 7.3277247534 (1·Vol B) | 14.655449507 (2·Vol B) | 2 |
   | T | 3 | 8.2863168178 (Vol 8₁₁) | 21.983174260 (3·Vol B) | 2.6529 |
   | ³He | 3 | 7.3277247534 (1·Vol B) | 21.983174260 (3·Vol B) | 3 |
   | ⁴He | 4 | 14.655449507 (2·Vol B) | 29.310899014 (4·Vol B) | 2 |

   The production values are neither the closures' hyperbolic volume, which does not exist, nor
   their simplicial volume, which is A·Vol(B). Production counts Vol(B) as (A−1, A−2, 2) at
   A = 2, 3, 4 for D, ³He and ⁴He, and uses 8₁₁ for T. The γγ closure counts one Vol(B) per
   nucleon and nothing per V³ bond.

## Not claimed

- That v₃‖M‖ is the right binding volume. It is one derived invariant of the closure that exists
  when the hyperbolic volume does not. Other candidates exist, for example the bond-only
  difference, which is 0 for V³. Which one the chain should use is not decided here.
- Anything about binding energies. No B_pred was recomputed.
- Bond words other than V³. The reading-3 bond derivation (branch
  `claude/gg-internucleon-bond-2026-11-21`) is separate. The producer takes `bond_power` and the arm
  as parameters of `word()`, so its survivors can be added as a new pre-registered run.
