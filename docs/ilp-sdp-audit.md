# ILP / SDP Audit

Snapshot of every LP / ILP / SDP / MISDP optimisation in the
`computations/` engine, together with the paper
blocks that reference these computations.  Goal: identify LPs whose
feasibility predicate is already PSD (hence "SDP in disguise") and
should be lifted to a true SDP, per the 1-ppm workplan
(`docs/mass-1ppm-workplan.md`, phase 2 item 1).

Symbols in the "kind" column:

- **LP**      — linear programme (linear constraints, linear / no objective)
- **ILP**     — integer LP (integer / boolean variables, linear constraints)
- **LP(PSD)** — LP whose feasibility predicate is a Gram / Frobenius
                positivity test `G·x ≥ 0` — morally SDP, but written as LP
- **SDP**     — true semidefinite programme (PSD matrix constraint via cvxpy)
- **MISDP**   — mixed-integer SDP
- **LP-dual** — LP dual read-off
- **exhaustive** — no solver; enumerates a finite config space with a
                  feasibility predicate

## Engine computations

| File | Kind | Solver | PSD / Frobenius check | Paper cross-refs | Upgrade candidate? |
|------|:-----|--------|-----------------------|------------------|:---|
Block refs are only listed if verified to exist in
`content/quantum-observable-universe/` — many engine scripts have no
dedicated paper block yet (marked `—`).

| File | Kind | Solver | PSD / Frobenius check | Paper cross-refs | Upgrade candidate? |
|------|:-----|--------|-----------------------|------------------|:---|
| `atom-builder-lp.py`              | LP(PSD)   | (exhaustive + `G·NF ≥ 0`)  | H_3 Gram                      | `prop:atomic-braid-mass` ✓                | **yes** — morally SDP |
| `atom_crossing_lp.py`             | exhaustive| —                         | none                          | —                                          | no |
| `branching-lp.py`                 | ILP       | (enumerate)               | none                          | —                                          | lift via PSD if available |
| `ch-bond-lp.py`                   | LP(PSD)   | (enumerate + Gram)        | H_3 Gram                      | —                                          | **yes** |
| `ch-bond-writhe-lp.py`            | LP        | —                         | none                          | —                                          | no |
| `ch-valence-ilp.py`               | ILP       | (enumerate)               | none                          | —                                          | no |
| `confinement-lp.py`               | LP(PSD)   | **cvxpy LP**              | Frobenius positivity (many)   | `prop:confinement-lp` ✓                    | **yes — drop-in SDP** |
| `confinement-operator-selection.py`| LP       | (enumerate)               | Gram-weighted                 | —                                          | lift if solver-backed |
| `electron-shell-ilp.py`           | ILP       | (enumerate)               | H_3 Gram                      | —                                          | minor |
| `h2-integer-lp.py`                | ILP       | (enumerate)               | none                          | —                                          | no |
| `ilp-chain.py`                    | ILP       | (enumerate)               | Gram                          | `rem:ilp-solution-count-unwrap` ✓          | minor |
| `integer-lp-gluon.py`             | LP(PSD)   | (enumerate + H_3 Gram)    | H_3 Gram                      | — (no dedicated block yet)                 | **yes — full-atom SDP (P2.1b)** |
| `knot-operator-lp.py`             | LP-dual   | **cvxpy LP**              | Gram-based dual               | `prop:knot-operator-energy-exists` ✓       | **yes — LP-dual → SDP-dual** |
| `lp-constrained-6he.py`           | LP(PSD)   | **cvxpy LP**              | Frobenius (21 refs)           | —                                          | **yes** |
| `lp-duality-check.py`             | LP-dual   | —                         | Gram matrix                   | `prop:knot-operator-energy-exists` ✓       | **yes** |
| `misdp_cross_channel.py`          | MISDP     | **cvxpy SDP**             | 7 PSD constraints             | —                                          | already SDP ✓ (no block) |
| `molecular-frobenius-lp.py`       | LP(PSD)   | (exhaustive + Gram)       | Frobenius (23 refs)           | —                                          | **yes** |
| `molecular-full-ilp.py`           | ILP       | (enumerate)               | none                          | —                                          | no |
| `molecular-ilp.py`                | ILP       | (enumerate)               | Gram                          | —                                          | lift |
| `molecular-integer-lp.py`         | ILP       | (enumerate)               | none                          | —                                          | no |
| `multi_level_sdp.py`              | SDP       | **cvxpy SDP**             | 18 PSD blocks, levels 3–7     | —                                          | already SDP ✓ |
| `nuclear-binding-lp.py`           | LP(PSD)   | **cvxpy LP**              | Frobenius                     | —                                          | **yes** |
| `nuclear_ilp.py`                  | ILP       | (enumerate)               | Gram                          | —                                          | lift to MISDP |
| `pn_alpha_lp_dual.py`             | LP-dual   | **cvxpy SDP** (8 PSD)     | Gram                          | —                                          | already SDP ✓ |
| `recursive_alpha.py`              | fixed-pt  | —                         | none                          | —                                          | no |
| `sdp_cross_channel.py`            | SDP       | **cvxpy SDP** (7 PSD)     | Gram                          | —                                          | already SDP ✓ |
| `sdp_on_shadows.py`               | MISDP     | **cvxpy MISDP** (10 PSD, boolean) | Gram                   | —                                          | already MISDP ✓ |

## Paper blocks on LP / SDP / Frobenius

Confirmed blocks in `content/quantum-observable-universe/`:

- `prop:confinement-lp` — confinement-operator selection as LP.
- `prop:confinement-sdp` — confinement-operator selection as SDP
  with matrix Frobenius positivity.  This is the **authoritative**
  paper block matching the engine's Lasserre moment-matrix lift
  (`sdp_moment_lift.py`, `confinement_sdp.py`, `sdp_lift_audit.py`):
  the scalar LP is the rank-1 projection and the audit's 6-for-6
  Frobenius-invalid LP solutions confirm the SDP is strictly
  stronger.  Promoted in a concurrent branch (PR #384).
- `prop:knot-operator-energy-exists` — existence via LP-dual (with
  Lean formalization in `knot-operator-energy-unique.lean`).
- `prop:atomic-braid-mass` — atomic braid mass formula.
- `prop:jet-tower-convergence` — geometric-series tail bound for
  the brane-tower sum; takes `prop:confinement-sdp`'s rank-1
  regime as its hypothesis source and closes the truncation
  budget conditional on boundedness of $\Delta^{(n)}$.
- `rem:ilp-solution-count-unwrap` — ILP enumeration remark.

Engine scripts **without a dedicated paper block**:
`multi_level_sdp`, `sdp_on_shadows`, `sdp_cross_channel`,
`misdp_cross_channel`, `pn_alpha_lp_dual`, `integer-lp-gluon`,
`nuclear-binding-lp`, `molecular-frobenius-lp`, `ch-bond-lp`,
`lp-constrained-6he`, `branching-lp`, `electron-shell-ilp`,
`h2-integer-lp`, `ch-valence-ilp`, most of `atom-builder-lp` /
`atom_crossing_lp` / `*-molecular-ilp`, `recursive_alpha`.

That is a sizeable gap — the engine has six already-SDP files
producing witnesses that nothing in the paper cites directly.  A
follow-up pass should either (a) create matching blocks or (b)
fold the witnesses into existing blocks via `cites:` entries.

## Headline findings

1. **Six LP(PSD) files are really SDPs-in-disguise.** Their
   feasibility predicate is a Gram / Frobenius positivity check
   `G·x ≥ 0` applied componentwise to a certificate vector.  The
   honest form of that constraint is `x^T G x ≥ 0` (a quadratic
   positivity condition), which at the matrix level becomes an
   SDP `X ⪰ 0` with `X = x x^T`.

   The candidates, in rough order of expected mass-prediction
   leverage:

   - `integer-lp-gluon.py` ← gluon decoration per nucleon (**P2.1b**
     target: lift to full-atom H_{3A} SDP; session P2.1 showed H_3
     LP optimum does NOT transfer)
   - `confinement-lp.py` ← cvxpy LP, already solver-backed, drop-in
   - `lp-constrained-6he.py` ← cvxpy LP, 6He binding constraint
   - `molecular-frobenius-lp.py` ← molecular Frobenius constraint
   - `nuclear-binding-lp.py` ← nuclear-level binding LP
   - `ch-bond-lp.py` ← carbon-hydrogen bond

2. **Already-SDP files (no work needed).** `multi_level_sdp.py`,
   `misdp_cross_channel.py`, `sdp_cross_channel.py`,
   `sdp_on_shadows.py`, `pn_alpha_lp_dual.py` — cvxpy PSD blocks,
   correctly formulated.

3. **LP-dual files that could be promoted to SDP-dual.**
   `knot-operator-lp.py` and `lp-duality-check.py` compute LP dual
   values, but the primal's Gram-positivity already lives in a
   semidefinite cone — promoting to SDP-dual makes the duality gap
   and sensitivity analysis more meaningful.

4. **Pure ILPs** (integer-only, no PSD structure): `branching-lp`,
   `ch-valence-ilp`, `electron-shell-ilp`, `h2-integer-lp`,
   `ilp-chain`, `molecular-*-ilp`, `nuclear_ilp`.  Upgrade to MISDP
   only where physical positivity is meaningful (e.g.,
   `nuclear_ilp` → MISDP with per-configuration Gram check).

5. **Paper coverage.** `prop:confinement-lp`,
   `prop:multi-level-sdp`, `thm:cross-channel-sdp`,
   `thm:shadow-sdp`, `prop:knot-operator-energy-exists`,
   `thm:pn-alpha-duality` — all exist.  `integer-lp-gluon` has a
   corresponding remark in `mass-coefficient-shadow-price.md` but
   **no dedicated prop**; after P2.1b lands, promote to a proposition.

## Recommended session order

1. **Kähler to arbitrary order** (P2.3, next).  Prep before any
   heavy mass work — need order ≥ 3 for sub-keV targets.
2. **Full-atom SDP for gluon** (P2.1b, separate fork per user
   instruction).  Biggest single mass-prediction gain predicted.
3. **Drop-in SDP lift for `confinement-lp.py`** (one hour).  Already
   solver-backed; changing `cp.Minimize(...)` + linear constraints
   to an SDP with `X ⪰ 0` is mechanical and verifies the audit
   claim of LP(PSD) = SDP in disguise.
4. **Promote `rem:integer-lp-gluon` to a proposition** once the
   full-atom SDP lands.
