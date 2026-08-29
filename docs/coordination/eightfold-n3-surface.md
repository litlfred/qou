# Coordination ledger — the eightfold `N = 3` surface

Goal: settle whether the framework can supply the three-dimensional object the
eightfold-way classification needs, and whether flavour and colour `SU(3)` are
one construction or two.

| Date | PR | Agent finding | Effect on other branches |
|---|---|---|---|
| 2026-08-26 | #5819 | Route A's requirement (non-self-duality) proved from the `Sym²` gate + FS trichotomy. **Not new** — `qou-dwsh` recorded it 2026-08-03 from the row cap. Second independent route. | #5744: gives the surviving `N = 3` direction a stated necessary condition, and a pre-`Sym²` screen (`screen_out_selfDual_candidate`). |
| 2026-08-26 | #5819 | Generator-identification route to octonionic `SU(3)` excluded as a class (dimension `8 → 7`; rank-2 Cartan collapse). Observation already in the 2026-08-25 upload triage; the class exclusion is new. | None — no sibling consumes that route. |
| 2026-08-26 | #5819 | Flavour/colour: **no** gate reading only object data can separate the two triples, and that forecloses the whole tensor-construction family (`Sym³`, `Λ³` included). Discriminator located in the Young-symmetry channel — located, not established. | #5744: narrows what a gerbe candidate has to exhibit. |
| 2026-08-25 | #5744 | Provenance audit of the seven `N = 3` exclusions: none rests on float64 or convention C; route 3 strengthened from a finite sample to a proved identity. | #5819: the prune holds, so effort belongs on the surviving direction, not on re-auditing exclusions. |

## Names for one object

`qou-8pl3` **Route A** (multi-fibre groupoid), `qou-8p1i` **T3b**, `qou-dwsh`
**T3b distinct-fibre groupoid**, `qou-y7vg` **T3g non-neutral Tannakian gerbe**,
and #5744's *"surviving direction"* are all the same open problem. `qou-8p1i` is
scrapped as a duplicate of `qou-dwsh`; **`qou-y7vg` is the live carrier**. Check
it before opening anything new on this surface.

## Standing hazards on this surface

- **Self-duality alone does not decide the `Sym²` gate.** Even-dimensional
  (symplectic) summands pass. The valid criterion is parity
  (`Sym2GateParity.gate_fails_iff_odd_dim`) or, for decomposable objects, the FS
  trichotomy with `QuaternionicEvenDim` carried explicitly. The invalid inference
  was live in the corpus once and was deliberately fenced off by
  `self_duality_does_not_decide_gate`; do not re-derive it.
- **The `rem:fivefold-affine-charts-generations` claim is a remark**, not a
  theorem — five inequivalent fibre functors are *asserted*, with no `.lean`, no
  proof and no witness. It cannot be cited as settling the existence question.
  Its `3` is also the wrong `3`: three of five sheets carry *generations*.
- **The shelf is empty.** `library/` returns one Tannakian hit and zero on
  gerbes or inequivalent fibre functors (#5744, bean `qou-tzfm`). Anything here
  is derived, not cited.
