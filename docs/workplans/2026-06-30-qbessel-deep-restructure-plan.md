# Plan — q-Bessel proof-cluster deep restructure (kehn keystone)

Tracked by bean `c370`. Owner: the Q_β / Habiro keystone (bean `kehn`) — the
*statement wording* is a math-content call in that feature's territory.

## Problem

`prf:jackson-q-bessel-contiguity` has `of: "rem:brings-q-hyperbolic-geometry"`
— a **proof of a remark** (inverted; a `proof` must prove a provable block).
The contiguity *claim* currently lives only inside the remark's prose, and the
remark carries `interprets: 0`. (The sibling proofs
`prf:q-bessel-c-k-recurrence-cfinite` and
`prf:q-bessel-second-order-qdifference` already correctly target
`prop:q-beta-c-k-recursion-from-habiro-q-difference`; only the Jackson one is
inverted.)

Backing is solid: `content/quantum-observable-universe/lean/QOU/QBeta/`
`QBesselContiguityRecurrence.lean` is **sorry-free** (8 theorems), incl.
`qbessel_first_kind_coeff_closed_form` / `qbessel_second_kind_coeff_closed_form`;
compute witness `computations/qbeta/qbessel-jackson-contiguity.witness.json`.

## Target structure (§3a-canonical)

```
prop:jackson-q-bessel-contiguity-recurrence   .ts + .md + .lean→QOU.QBeta.qbessel_*_kind_coeff_closed_form
   └─ prf:jackson-q-bessel-contiguity        of: → the new prop          [retarget]
rem:brings-q-hyperbolic-geometry               interprets: → the new prop  [add]
```

## Block operations

1. **New `prop:jackson-q-bessel-contiguity-recurrence`** (mass-theory): `.ts`
   (`proposition`) + `.md` (move the contiguity statement + closed form out of
   the remark) + `.lean` sibling resolving to the existing sorry-free
   `qbessel_first_kind_coeff_closed_form` / `qbessel_second_kind_coeff_closed_form`.
2. **Retarget** `prf:jackson-q-bessel-contiguity` `of:` → the new prop.
3. **Remark** `rem:brings-q-hyperbolic-geometry`: add
   `interprets: "prop:jackson-q-bessel-contiguity-recurrence"`; drop
   `proof:jackson-...` from `uses` (replace with the new prop); keep only the
   q-hyperbolic-geometry interpretation. Clears its `remNoInt` flag.
4. **Register** the new prop in `mass-theory.ts` beside the q-Bessel cluster
   (immediately before its proof).
5. **Validate**: corpus structural check (refs resolve / registered / prop has
   `.lean`) + lean-direct on the new sibling (restored lake-cache oleans).

## kehn math-judgment points (why deferred)

- **Statement scope**: which of the 8 sorry-free theorems the prop asserts
  (first-kind only vs both kinds; whether to include the q-weight / `SU_q(1,1)`
  Casimir structure); exact hypotheses.
- **Tiering**: the prop must read **fibre-level** (formal `q`, radial algebra),
  NOT as a production `Q_β`/`c_k` claim — the flip-flop-sensitive zone
  (AGENTS.md §"c_k is a TRUNCATION ORDER"). Wording is the keystone owner's call.
- **Remark scope**: interpret the narrow new prop, or a broader Bring's-curve /
  `SU_q(1,1)` statement.

## Risk / cost

Low: 1 new block + 2 edits + 1 manifest line; no other blocks reference these.
Content-block change only — no overlap with the active `.lean` orphan-drain PRs
(#3134/#3126) in the same chapters.
