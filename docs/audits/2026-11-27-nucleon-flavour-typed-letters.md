# Flavour letters on the full tower: no second flavour factor under the corrected trace

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-flavour-typed-letters-2026-11-27`
**Beans:** `qou-myts`, `qou-99qc` · **Thread:** "Derive the nucleon flavour factor" (sibling of
"Derive the neutron-proton mass split")
**Ruling in force:** owner ruling A, 2026-11-27 (`docs/coordination/owner-rulings.md`): the split
uses the framing-corrected trace of `def:mass-identity`; a curl contributes 0; *"the flavour split
must come from the flavour letters themselves"*.
**Lean:** [`QOU/Nuclear/NucleonFlavourTypedLetters.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonFlavourTypedLetters.lean)
(lean-direct `-DautoImplicit=false -s 65536`, exit 0; `#print axioms` on `typed_V_pow_tau_ratio`,
`typed_V_pow_trW_eq`, `conj_gen0`: propext, Classical.choice, Quot.sound; no `sorryAx`; generic
`[Field R]`, no numerical value)
**Probe:** [`computations/probes/nucleon_flavour_typed_letters/`](../../computations/probes/nucleon_flavour_typed_letters/)
(pre-registration with a disclosure that scratch runs came first; exact sympy over ℚ(q) on `H₃`,
exact `Fraction` on `n = 6`, 80 dps at the proton `q₀`; witness `nucleon-flavour-typed-letters.witness.json`)

## 1. Question

The derived flavour cell is `2E₀·log q = 0.873537 MeV` (`K`-weight, `NucleonSplitFullTower`).
Is there a second flavour-letter contribution, on the full tower and under the corrected trace,
that derives a factor of about 2?

## 2. Short answer

**No.** Three results.

1. **The letters of the γγ nucleon word contribute exactly 1 (proved).** Type every crossing of
   the word by the flavours of the two strands that meet there, with the corpus rule of
   `NucleonFlavourIsDetermined` (`uu` = the crossing, `dd` = the reversed crossing, mixed = the
   average). Then for every γγ word on three strands, `Vᵏ = (σ₀σ₁⁻¹)ᵏ`, every `k`, and for every
   typing (raw trace or framing-corrected), `τ_p = q²·τ_n` (`typed_V_pow_tau_ratio`). The split
   stays `2E₀·log q`.
2. **On the tower the same holds for disjoint nucleon blocks** (`V³ ⊗ V³`, leftmost block
   tagged, the other summed over all colourings): exactly `q²` at `q = 11/10` and `3/2`, both
   traces. Interface letters between blocks move it, but the interface word is not ruled (#7876)
   and the direction depends on which letter is placed (§4).
3. **The only exact factor 2 is in the raw trace, and the corrected trace removes it.** One
   extra typed quark letter, placed by hand, gives `τ_p/τ_n = q⁴` exactly in the raw trace
   (`4E₀·log q = 1.747 MeV`, the same number as the raw curl CM). Under the corrected trace the
   writhe weight swaps the letter's `uu`/`dd` scalars (`corrScalars_swap_raw`), so the letter's
   diagonal ratio becomes `q⁻²` and cancels the cell: total exponent −0.13 / −0.05 (split
   −0.058 MeV). Extra letters are not γγ-producible and their placement is not ruled; the census
   recipe's three letters give 16 different values over the 48 placements.

So under ruling A the flavour letters do not double the cell. The near-factor-2 seen in the raw
trace (letter or curl) is the writhe, which the corrected trace is built to remove.

## 3. Why the typed letters cancel (the proof in one paragraph)

On `V ⊗ V` a typed letter is weight-preserving with a scalar `α` on `uu`, `β` on `dd` and a
block `m` on the mixed states, and reversing the crossing swaps `α, β` and keeps `m`
(raw: `(α, β) = (q, q⁻¹)`; corrected: `(q⁻¹, q)`). Let `φ(a, b, c) = (c̄, b̄, ā)` be the flavour
flip composed with strand reversal. `φ` exchanges `W_p` and `W_n`
(`trW_two_eq_trW_one_conj`) and carries a typed `σ₀` to a typed `σ₁⁻¹` and a typed `σ₁⁻¹` to a
typed `σ₀` (`conj_gen0`, `conj_gen1`). So `φ` sends `(AB)ᵏ` to `(BA)ᵏ`, and the restricted trace
of `(BA)ᵏ` equals that of `(AB)ᵏ` because the letters preserve weight (`trW_pow_swap`). The two
weight spaces therefore have equal plain traces, and only `K = diag(q, q⁻¹)` separates them.
Nothing about `α, β, m` is used, which is why raw and corrected agree.

**Invariant cited for scope (b):** the `φ`-conjugation identity plus cyclicity, for words whose
cyclic class is fixed by `φ`. Every γγ word on `H₃` is one. Measured, not proved: the widened γγ
words of fork G2 (`V̄ = σ₀⁻¹σ₁`; `V̄³`, `VV̄`, `(VV̄)²`, `V²V̄`, `VV̄V`) also give `q²` exactly in
both traces; random writhe-0 words do not (12 of 28 fail), so the identity is about the γγ
symmetry, not about writhe 0.

## 4. Numbers (proton `q₀ = 1.10997858275138…`)

| object | raw trace | corrected trace |
|---|---|---|
| typed `Vᵏ`, `k = 1..6`, `H₃` | `q²` exactly | `q²` exactly |
| typed `V³ ⊗ V³`, `n = 6`, leftmost block | `q²` exactly | `q²` exactly |
| `V³ σ₂ V³` (interface, unruled), `q = 11/10` | exponent 2.659 | 1.305 |
| `V³ σ₂⁻¹ V³` (interface, unruled), `q = 11/10` | 1.341 | 2.648 |
| `V³ V(2,3) V³` (γγ interface vertex), `q = 11/10` | 1.988 | 1.990 |
| one bare typed letter | `q⁴` exactly | `q²(q⁶−q⁴−3q²+1)/(q⁶−3q⁴−q²+1)` |
| `V³` + one typed letter on `σ₀` / `σ₁` | exponent 4.035 / 3.959 | −0.133 / −0.045 |
| `V³` + census three letters, 48 placements | 1.71 … 8.36 | −2.40 … 5.31 |

MeV with order-zero `E₀ = 4.18598136329`: cell `2E₀ log q` = 0.873537 (tower `E₀`: 0.882197);
raw extra letter `4E₀ log q` = 1.747073; corrected extra letter on `σ₀`: −0.057921.

## 5. Comparison boundary (the only place data enters)

CODATA `m_n − m_p = 1.29333 MeV`. Literature quark-mass part, for comparison only:
`+1.87 ± 0.16 MeV` (Gasser–Leutwyler–Rusetsky, arXiv 2008.05806) and `+2.52 MeV` (BMW,
arXiv 1406.4088). The derived cell 0.874 MeV is about 0.47 of the first. The raw 1.747 MeV sits
near 1.87, but it is the raw trace, which ruling A excludes; choosing it because of that match
would be selection against the target. Nothing here is adopted on accuracy.

## 6. Scope

* **(b)** within the typed-letter model and the corrected or raw trace: the flavour letters of
  any γγ word on `H₃` contribute a factor exactly 1. Invariant: `φ`-conjugation + cyclicity (Lean).
* **(a)** hand-placed extra letters and interface letters: they move the ratio, but by amounts
  that depend on an unruled placement; none is derived.
* **Not formalised:** the `n = 6` statements (exact at two rational `q`, not for all `q`); the
  G2 words (measured).

## 7. Where a factor of about 2 could still come from (not decided here)

The letters are closed as a source under ruling A. What is left is outside them: the nuclear
interface word (#7876), the scale `E` (the sibling thread on the EM self-energy), or a down strand
that is not the Weyl flip of the up strand (fork F1 of `2026-11-27-nucleon-down-strand-self-energy.md`).

## 8. Reproduce

    lean -DautoImplicit=false -s 65536 folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonFlavourTypedLetters.lean
    python3 -u computations/probes/nucleon_flavour_typed_letters/nucleon_flavour_typed_letters_probe.py
