# Homological shell condensation: what a well-posed statement needs

Bean `qou-6qbv`. Owner, 2026-11-20: "Can you prove the conjecture", then chose
option 1, "make it well-posed, then attempt it".
Block: [`conj:homological-shell-condensation`](../../folio/quantum-observable-universe/mass-endomorphism/homological-shell-condensation.md).

## 1. The statement as written

For `n ∈ 𝔐 = {2, 8, 20, 28, 50, 82, 126}`, the Białynicki-Birula (BB) spectral
sequence on the jet algebra `A_n` has `E_∞^{p,q}(n) = 0` for `p ∈ ℕ`, `q > 0`.

## 2. Gaps, each checked against the corpus

| # | Object | What the corpus says | Gap |
|---|---|---|---|
| G1 | `A_n` | `A_{n+1} = J¹(A_n) = A_n ⊗ Ω¹(A_n)`, `Ω¹ = ker(m)` (`prop:jet-prolongation`) | A tensor product of an algebra with a bimodule. No multiplication is defined on it; "inherits a canonical Frobenius–Hopf structure" is asserted, not constructed. |
| G2 | the index `n` | `n` is the tower level | The magic numbers are nucleon counts. `magic-numbers-bring` reads them as ranks of period sub-lattices, not as tower levels. Level 126 of the tower has `dim A_126` growing like `d^(3^126)`, which no reading of the physics uses. |
| G3 | the ℂ^× action | induced by the "descent involution" `τ̂` | `def:descent-involution` proves `τ̂² = τ̂`: it is an **idempotent**, not an involution. An idempotent gives at best the weight split `im τ̂ ⊕ ker τ̂` (weights 0 and 1), so a BB filtration with two steps. |
| G4 | `H^q(gr^p_F A_n)` | not specified | Sheaf, Hochschild, or the cohomology of some complex: none is named. |
| G5 | the "equivalently" clause | the trace on `J^ℓ/J^{ℓ+1}` | That is the confinement filtration on the Hecke algebra, a different object; and that filtration is not preserved by the Hochschild differential (`gb_spectral_sequence_h3_probe.py`). |

## 3. The Lean carrier is satisfiable with no content

`QOU.ShellCondensation.HomologicalConjecture` takes the page entries `EInfty p q`
as free types. Setting every entry to `PUnit` gives an instance for every
saturated `n`; this compiles (`lean -DautoImplicit=false`, exit 0, scratch
file, not committed). So the Lean class records the shape of the claim but
constrains nothing.

## 4. Readings that make it precise, and what each gives

| Reading | Algebra | Filtration | Cohomology | Result |
|---|---|---|---|---|
| R1 | `H_n(q)`, `n` = nucleon count | Coxeter length (`prop:gb-spectral-sequence`) | Hochschild | `HH^k = 0` for `k > 0` whenever `H_n(q)` is semisimple (Hochschild 1945), which holds at the real `q₀` for every `n`. So `E_∞^{p,q} = 0` for `p ≥ 0, q > 0` at **every** `n`. Checked exactly at `n = 3`: `E_∞` lies in total degree 0 at filtration degrees `0, −2, −3`. |
| R2 | any commutative `A_n` | any | sheaf cohomology on `Spec A_n` | Affine, so `H^q = 0` for `q > 0` at **every** `n` (Serre vanishing). |
| R3 | `End(A_{n+1})` with `τ̂` | two-step split `im τ̂ ⊕ ker τ̂` | Hochschild | Needs G1 first. When `C` is semisimple, `End_C(A_{n+1})` is a finite product of matrix algebras, hence separable, so `HH^{>0} = 0` at **every** level. |

## 5. Conclusion

Under every precise reading found, the vanishing holds for all `n`, so it does
not single out the magic numbers. That is a scope-(a) finding about these
readings, not an exclusion: a reading under which non-magic `n` fail would need
a non-separable algebra or a cohomology with coefficients other than the
algebra itself, and none is in the corpus. The conjecture's intended content,
that the vanishing is special to `𝔐`, is therefore not yet stated.

What would make it attemptable:

1. Fix `n` as the nucleon count (G2).
2. Name the algebra, the grading and the cohomology (G1, G3, G4), choosing ones
   under which some non-magic `n` gives a nonzero entry. Otherwise the
   statement is true and empty.
3. Rebuild the Lean carrier on that construction, so the page entries are
   computed rather than supplied.
