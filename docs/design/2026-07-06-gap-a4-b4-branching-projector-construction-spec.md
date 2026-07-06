# Construction spec — the [1⁴] branching projector for the connected `b₄` value

**Date:** 2026-07-06 · **Kind:** design / construction spec (multi-session
infrastructure thread; owner-directed 2026-07-06). **No compute in this doc** —
it specifies HOW to build the [1⁴]-projected connected 4-nucleon Markov trace
correctly, so the value computation is a *gated execution*, not a rushed scan.

The value leg's surroundings are all proved/merged: the gate
(`su4_supermultiplet_dim_vanishes_iff`, `C(4,A)=0 ↔ A>4`), the three invariants
(I-par bar-even projection, I-conn irreducibly connected, I-ceil ~14% headroom),
the exact target (`b₄ ≈ 9.243 MeV`, AME Ursell inversion), and the Lean-proved
orthogonality (`BodyOrderCumulant`: no 1-/2-body form supplies it). The one
remaining object is the **`b₄^even` value**, which needs the projector below.

## 1. Available data (on main)

`computations/chi-helium-4-h12-at-q0-50dps.witness.json` — the ⁴He (n=12 strands)
character table, `by_partition`: **77 entries**, each
`{partition, y_lambda, chi_lambda, contribution}` for a partition `λ ⊢ 12`
(convention `colour-weighted-averaged-crossing`), with the full trace
`tr_M = Σ_λ y_λ χ_λ` (`tr_M_at_q0`). The `-at-qinv-` sibling gives the
bar-conjugate `tr_M(q⁻¹)` needed for the I-par bar-even projection. The
`-free-` sibling gives the disjoint-nucleon vacuum word (for the connected
subtraction).

## 2. The construction (three steps)

> **CORRECTION (2026-07-06, gate-verified — supersedes the earlier
> quark-plethysm framing).** The [1^A] projector acts at the **nucleon** level,
> not the quark level. Its dimension must equal the proved gate `C(4,A)`
> (`su4_supermultiplet_dim_vanishes_iff`). Checked directly:
>
> | A | gate `C(4,A)` | nucleon `Λ^A(4)` | quark `e_A[h₃] = Λ^A(Sym³ℂ⁴) = C(20,A)` |
> |---|---|---|---|
> | 3 | 4 | **4 ✓** | 1140 ✗ |
> | 4 | 1 | **1 ✓** | 4845 ✗ |
> | 5 | 0 | **0 ✓** | 15504 ✗ (does not vanish!) |
>
> So the projector is **`Λ^A` of the nucleon's SU(4) FUNDAMENTAL 4** (the 4
> single-particle spin-flavor states p↑,p↓,n↑,n↓) — a Slater determinant of A
> nucleons — **not** the quark plethysm `e_A[h₃]` (which is `C(20,A)`, non-zero
> for A>4, inconsistent with the gate). The 3-quark `h₃` content is the
> INTRA-nucleon structure, already carried by `τ_p`/`τ_n` (the intra-nucleon
> Markov trace); it is **not** a flavor tensor factor. This eliminates the hard
> quark-level Schur–Weyl S₁₂ branching (Step A below is deleted) and makes the
> value a nucleon-flavor computation.

**Step A′ — the nucleon-flavor Slater/antisymmetrizer `P_{[1^A]} = Λ^A(4)`.**
Each nucleon carries one of the 4 SU(4) single-particle states. `P_{[1^A]}` is
the Young antisymmetrizer over the A nucleon FLAVOR indices (the `sgn` rep of the
`S_A` that permutes nucleons), acting on `(ℂ⁴)^{⊗A}` — NOT on the 3A quark
strands. Its rank is `C(4,A)` (gate), zero for A>4: locality is structural. The
intra-nucleon 3-quark content enters only through the scalar traces `τ_p, τ_n`
(and their pairwise dressings `z, z−h, z−h/2`).

**Step C — the projected trace and its connected part.** Compute
`τ_{[1⁴]}(q) = tr_M(P_{[1⁴]} · β_{⁴He})` as the `y_λ χ_λ`-sum restricted to the
partitions in `Im P_{[1⁴]}`. Then the **connected** `b₄` = Mayer subtraction:
`b₄^conn = τ_{[1⁴]}(full) − (disconnected 2+2, 3+1, 2+1+1, 1⁴ parts)`, each
disconnected part a product of lower-A projected traces (reuse
`interface_4body_assembly_probe`'s `τ_p, τ_n` and the ³He/³H/D projected traces).

**Step D — the bar-even projection (I-par).** `b₄^even = ½[b₄^conn(q₀) +
b₄^conn(q₀⁻¹)]` using the `-at-q0-` and `-at-qinv-` witnesses. This is the
binding magnitude (the bar-odd part is radiated; proved-mixed in
`b4-connected-bar-parity`). Dress to MeV via `E₀ = m_e/(q₀(q₀−1))`.

## 3. Formalize-first gate (already proved — do not re-derive)

`QOU.MassTheory.SU4SupermultipletGate.su4_supermultiplet_dim_vanishes_iff` gives
`C(4,A)=0 ↔ A>4` — `P_{[1⁴]}` is rank-0 for A>4, forcing `b₄(A>4)=0`. This is the
`e_A[h₃]` `A>4` vanishing the parent scoping note (Lever 1) requires. No further
gate needed; the projector construction is *licensed*.

## 4. Correctness cross-checks (the probe must pass these before any claim)

1. **A=6 vanishing.** Run the same projector on ⁶Li (n=18): `P_{[1⁴]}` rank-0 ⇒
   `b₄(⁶Li) = 0` (matches the measured `super× = 0.94 ≤ 1` return-to-pairwise).
2. **Reconstruction.** `Σ_λ (all 77) y_λ χ_λ = tr_M_at_q0` (sanity on the χ read).
3. **Body-order consistency.** The extracted `b₄^even` compared to the AME
   cumulant target `9.243 MeV` — reported as a scope-(a)/(b) **verdict**, NOT
   fitted. A value within ~10–20% is a genuine partial closure; a large miss is
   an honest scope-(a) negative (the [1⁴] term alone is insufficient) — either
   is a real result. **Do NOT tune any convention to hit 9.243** (Rule-14).
4. **I-ceil consistency.** `b₄^even ≤ 16.8 MeV` (the trace-magnitude room).

## 5. Infrastructure to build (the deliverable of the next sessions)

- `computations/su4_slater_antisymmetrizer.py` — Step A′: the nucleon-flavor
  `Λ^A(4)` Slater antisymmetrizer over the 4 SU(4) single-particle states; expose
  `slater_dim(A) -> C(4,A)` + the antisymmetrized flavor-index structure. **Unit-test
  against the gate: rank = `C(4,A)`** (already verified in the §2 correction table).
- extend `interface_4body_assembly_probe.py` with a `connected_b4(Z,N)` using
  Steps C–D and the `by_partition` witness reads (q₀ and q⁻¹).
- emit `b4-connected-value.witness.json` with the A=4 value, the A=6 check, and
  the scope verdict vs the 9.243 target.

## 6. Risks / open sub-questions (flag before executing)

- **The block-exchange embedding — RESOLVED by the §2 correction.** The earlier
  worry (does `S_A` act strand-for-strand on the 3A quarks, entangling
  intra-block braiding?) is moot: the antisymmetrizer acts on the A **nucleon
  flavor** indices `(ℂ⁴)^{⊗A}`, and the intra-nucleon braiding is already summed
  into the scalars `τ_p, τ_n`. Still verify against the ³He/³H connected `b₃`
  (target `1.426 MeV`) as the cheaper first cross-check **before** ⁴He — now a
  `Λ³(4)` (dim-4) computation, not an S₉ branching.
- **Convention lock (I-6).** Use the dim-λ-normalised chi-cache convention
  (pinned canonical in `TraceConventionGate`); do not mix in the F_Bor framing.
- **Feasibility.** n=12 dense is at the wall; use `gram_transfer_quadratic` if a
  norm/Frobenius object is needed, but the `by_partition` `y_λ χ_λ` read is
  already O(77) and cheap — the cost is in *correctly identifying* `Im P_{[1⁴]}`,
  not the arithmetic.

## 7. Cross-references

- Value leg: `computations/probes/b4_value_cumulant_target_probe.py`,
  `QOU/MassTheory/BodyOrderCumulant.lean` (orthogonality, sorry-free).
- Gates: `QOU/MassTheory/SU4SupermultipletGate.lean`,
  `b4-connected-bar-parity` (I-par), `b4-iconn-irreducibly-connected` (I-conn),
  `b4-iceil-norm-ceiling` (I-ceil).
- Scoping: `docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md`,
  `docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md` (Lever 1).
- Data: `computations/chi-helium-4-h12-at-{q0,qinv}-50dps.witness.json`.
