# H9: the folded wall (pre-registration, 2026-11-21)

The user chose "Build the folded wall (H9)" on the card. Written before anything is computed.

## Construction (standard, Crisp; Lambropoulou)

The type-B braid group `B(B_n)` is the fixed subgroup of `B_{2n}` under the diagram involution
`σ_j ↦ σ_{2n−j}`. The embedding sends:
- the wall `τ` to the middle crossing `σ_n`;
- each `σ_i` to `σ_{n+i}σ_{n−i}`.

Here n = 3, so there are 6 strands. Strands 4, 5, 6 are the physical quarks, and strands 3, 2, 1 are
their mirrors.

Every generator, the wall included, then acts by the Jimbo `Ř`. So the wall obeys the crossing's
Hecke relation, with eigenvalues `{q, −q⁻¹}`. That is derived from the embedding, not chosen. The
question is what this does to the open trace.

Word: V³ = `(σ₁σ₂⁻¹)³` (ruled photon pair `γ(0,0,qh)·γ(0,0,−q⁻¹h)`), folded. One wall `σ₃` is
inserted, at every slot. The trace is pivotal, with `K^{⊗6}`. Only `M_QCD` is computed.

## Readings of p and n on 6 strands (both recorded)

- **R-sum.** Physical weight = +1 (p) or −1 (n), with the mirror strands summed.
- **R-ι.** As R-sum, but the mirror strands are fixed to the ι-image: the mirror weight is the
  negative of the physical weight, so the total weight is 0.
- **R-ptr**, a null predicted from the corpus: closing the mirror strand by a partial pivotal trace
  turns the wall into `ptr(Ř) = q²·1` (`OverStrandWeight.ptr_markov`), which is a scalar.

## Reported

For each reading, with the same λ (as in H8):
- `D = [(T_n + B_n)/(T_p + B_p)] / (T_n/T_p)`;
- the closed ratio `T_p/T_n` itself;
- whether the result depends on where the wall is inserted;
- the value at q₀, and at q = 1.

## Hit

A hit is a reading that is itself fixed by the corpus (not chosen here), gives `D ≠ 1`, and leaves no
free number. If the two readings disagree, the choice between them is an input, and that is
recorded. No fitting; `D` is not a mass.
