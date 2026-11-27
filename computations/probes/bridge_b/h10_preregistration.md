# H10: derive the wall's Hecke parameter, i.e. the folding level (pre-registration, 2026-11-21)

The user chose "Keep both, pause" on the level card and then wrote "Derive". Both arms are kept;
H10 tries to derive which level holds instead of choosing one. Written before anything is computed.

## Setting

Every invertible strand-1 reflection solution (H5, `d = 0`) has eigenvalues `{x, y}`. In Hecke
normalisation (`xy = −1`) that is `{Q, −Q⁻¹}`, a type-B Hecke algebra `H(B₃; q, Q)` with the bulk
letters kept in `H₃(q)`. So the level question is the value of `Q`:
- equal parameters is `Q = q`;
- `Q` is otherwise free.

The reflection equation alone holds for every `Q`; H5 showed that.

## Candidates, listed before evaluation

- **L Lusztig folding of lengths.** For a quasi-split folding `A_{2n−1} → B_n`, the fixed-point Coxeter
  group carries the weight function inherited from the length: the bulk generator `σ_{n+i}σ_{n−i}`
  has length 2, and the wall `σ_n` has length 1. So the Hecke parameters are bulk `q²` and wall
  `q`, in the `T`-normalisation. In the ruled normalisation, with the bulk at `q`, this gives
  `Q = q^{1/2}`.
  - Literature: Lusztig, *Hecke algebras with unequal parameters*.
  - Status: a standard consequence of folding. Conditional on `conj:type-b-folding-cpt`.
- **E Equal parameters, `Q = q`.** This would need a reason the wall's weight equals a crossing's. I
  will look for one in the corpus. Expected: none.
- **M Type-B Markov / pivotal compatibility.** Check whether requiring the type-B trace (the pivot
  `K` on every strand, `y = tr(K𝒦)/tr(K)`) to be Markov under the pivot fixes `Q`. Expected: it fixes
  a trace parameter, not `Q`.
- **C Coideal / Schur–Weyl.** Check whether the commutant of `H(B₃; q, Q)` on `V^{⊗3}` (a quantum
  symmetric pair coideal) is fixed by an object already in the corpus. Expected: the corpus does not
  define one.

## Reported

For each candidate that gives a `Q`:
- its status;
- `D(q₀)` and `D(1)`, using H8's open-trace `D` with `s = Q − Q⁻¹`, for V³;
- for L, the comparison with the doubled-strand H9 arm.

## Hit

`Q` follows from a corpus statement, or from a literature theorem applied to a corpus statement, with
no choice made here. A conditional hit is recorded as conditional. No fitting; `D` is not a mass.
