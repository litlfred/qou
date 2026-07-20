# PentagonRigidity — the residual "Φ₁/Φ₂ entire" leg is WALLED

**Date:** 2026-07-20 **Bean:** `qou-j2v9` (z-pentagon)
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** WALLED — not axiomatized, not faked. `PentagonRigidity.uniqueUpToScalar`
stays §3b-cond open, exactly as before. Supersedes/sharpens the 2026-07-18 wall audit.

## What PR #4120 left

`DoublyPeriodicLiouville.const_of_doublyPeriodic` (Liouville for doubly-periodic
entire functions) + `SubstratePeriods.periods_linearIndependent` (PR #4120, `ib`,
`i/b` are ℝ-independent when `Im b² ≠ 0`) reduce `uniqueUpToScalar` to **one** leg:
the ratio `r = Ψ/Φ` of two `FaddeevPhi` solutions at the same `b` is **entire**
(the zeros/poles of the two `Φ_b` coincide). Given `r` entire + independent periods,
`ratio_const_of_doublyPeriodic` finishes. So: is `r` entire provable now?

## Verdict: NO — the difference equations admit genuine elliptic freedom

The `FaddeevPhi` class (`FaddeevQuantumDilogarithm.lean:60`) axiomatizes **only** the
two modular-double q-difference equations. **These do not pin the divisor.** Concretely:

> If `Φ` is any `FaddeevPhi b` solution and `h : ℂ → ℂ` is **any** elliptic function
> with period lattice `⟨ib, i/b⟩`, then `Ψ := Φ·h` is *also* a `FaddeevPhi b`
> solution. Check: `shift_b` for `Ψ` needs `h(z−ib/2) = h(z+ib/2)`, i.e. `h` has
> period `ib`; `shift_binv` needs period `i/b`. Both hold ⟺ `h` is
> `⟨ib,i/b⟩`-elliptic. The shared prefactor cancels; the guard is unchanged.

The lattice is nondegenerate (`Im b² ≠ 0` at the substrate, `SubstratePeriods`), so
**nonconstant** elliptic `h` exist (Weierstrass `℘`). Then `Ψ/Φ = h` is a nonconstant
elliptic function **with poles** — not entire. Hence "ratio entire" is **false** for
arbitrary class solutions; it holds only for the pair that carries **no spurious
elliptic factor**. This is precisely the 2026-07-19 correction in
`MeromorphicSameOrder.lean` ("double periodicity of `ord Ψ − ord Φ` does NOT force
`ord Φ = ord Ψ`; a doubly-periodic ratio can be a nonconstant elliptic function"),
and it refutes the 2026-07-18 audit's claim (§2 there) that same-divisor is *forced*
by the shared prefactor. It is not.

## The exact residual analytic fact

"`r` entire" ⟺ **the canonical minimal solution `φ_b = phiBProd` is selected among
all `phiBProd·(elliptic)` by a growth/minimality principle** — i.e. every `FaddeevPhi`
solution admitted to the rigidity statement has **no elliptic factor** (equivalently:
`ord(Ψ)−ord(Φ) ≡ 0`, the divisor of `Ψ/Φ` is empty). The difference equations give
double-periodicity of that divisor (proved: `meromorphicOrderAt_orderDiff_periodic`);
what is missing is the **degree-zero + sign** input that forces the periodic divisor to
vanish identically. That input is the Faddeev–Kashaev growth uniqueness: `Φ_b` is the
unique (up to scalar) solution of order ≤ 2 with no zeros/poles off the two lattices —
a **Hadamard/Weierstrass-factorization** fact.

## Why Mathlib lacks the closing tool

Mathlib **has**: Liouville (`Differentiable.exists_const_forall_eq_of_bounded`), Cauchy
estimates, `meromorphicOrderAt`, and — now, in-corpus — the explicit product `phiBProd`
with proved convergence + both shift equations (`PhiBProd.lean`, unconditional at the
substrate). Mathlib **lacks**: Hadamard factorization / order-and-genus theory for
entire functions, the elliptic-function divisor-degree theorem (`Σ_cell ord = 0`), and
any Phragmén–Lindelöf growth-uniqueness for q-difference equations. Any of the three
would close the leg; none is present, and `phiBProd`'s *convergence* is not its *growth
order*, so the corpus product does not substitute. Building the Meromorphic dep cone
(outside the QOU olean cache) does **not** help — the gap is a missing theorem, not a
missing import.

## Smallest honest formalizable reductions (none closes the analytic core)

1. **Divisor-on-a-cell shrink (soft, cheap).** Via `meromorphicOrderAt_orderDiff_periodic`,
   "`r` entire on ℂ" reduces to "`ord(r) ≥ 0` on one closed fundamental parallelogram"
   (the `Int.fract` lattice-translate trick of `const_of_doublyPeriodic`, applied to the
   order). Strictly smaller (whole-plane → compact cell) but the cell fact still needs
   the divisor of `Φ_b`. Needs the Meromorphic cone.
2. **Explicit target divisor (concrete, cheap, pure algebra).** `numFactor b z k = 0 ⟺
   z = i(2m+1)/(2b) − ib(2k+1)/2` (and dual for `denFactor`) is sorry-free `Complex.exp
   = −1` algebra; it makes the target lattice concrete, reducing "zeros coincide" to
   "every admitted solution has exactly the `phiBProd` divisor". Concrete but not easier.
3. **Growth-hypothesis idealization (honest label, not physics).** Add an order-≤2 /
   minimal-solution hypothesis to the reference `Φ`; then Hadamard *would* give
   entireness — but Hadamard is the absent Mathlib theorem, so this only relocates the
   wall into a named hypothesis. This is the §3b-cond move already embodied by
   `uniqueUpToScalar` itself; re-encoding it buys nothing.

**Recommendation:** leave `uniqueUpToScalar` open (no instance). The genuine unlock is a
Mathlib Hadamard-factorization / entire-order contribution (or its `Φ_b`-specific
special case), attempted in a full-build session; reduction (2) is the only cheap,
non-circular corpus step and can land independently if a concrete-divisor witness is
wanted. Nothing here is wired, fitted, or axiomatized.
