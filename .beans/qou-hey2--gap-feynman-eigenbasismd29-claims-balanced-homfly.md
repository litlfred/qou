---
# qou-hey2
title: 'GAP: feynman-eigenbasis.md:29 claims balanced HOMFLY skein IS the braiding characteristic equation — false, nonzero Hecke residual; 11 blocks carry Form B'
status: in-progress
type: task
created_at: 2026-08-08T13:04:58Z
updated_at: 2026-08-22T03:15:00Z
---


## Re-measured and independently confirmed, 2026-08-22

Reached from the other direction: `agent:f01` flagged
`skein-generation-proof` for writing the Skein relation in HOMFLY form
against AGENTS.md §7a, and the corpus-grep before opening a new bean landed
here. This bean was title-only; below is the body.

### The claim is false, and it is decisive rather than marginal

§7a's Form A comes from the Hecke relation: multiply
`σ² = (q−q⁻¹)σ + 1` by `σ⁻¹` to get `σ − σ⁻¹ = q − q⁻¹`, i.e.
`L₊ − L₋ = (q−q⁻¹)L₀`. Form B is
`q·L₊ − q⁻¹·L₋ = (q^{1/2} − q^{−1/2})·L₀`.

Form B is **not** a consequence of the Hecke relation. Substituting
`σ⁻¹ = σ − h` with `h = q − q⁻¹`:

```
q·σ − q⁻¹·σ⁻¹ = (q − q⁻¹)σ + q⁻¹h = h(σ + q⁻¹)
```

which equals the scalar `s = q^{1/2} − q^{−1/2}` only if `σ` is the scalar
`s/h − q⁻¹`. It is not. Evaluated on σ's two Hecke eigenvalues at the proton
pin:

| eigenvalue | Form B LHS | Form B RHS (`s`) | Form A LHS | Form A RHS (`h`) |
|---|---|---|---|---|
| symmetric `q` | 0.4203986998 | 0.1043880583 | 0.2090602988 | 0.2090602988 ✓ |
| antisymmetric `−q⁻¹` | **0.0** | 0.1043880583 | 0.2090602988 | 0.2090602988 ✓ |

On the antisymmetric channel Form B reads `0 = 0.1044`. Form A holds
identically on both. So "the skein relation *is* the characteristic equation
of the braiding" is false as stated, exactly as this bean's title says, and
the residual is not small — it is the whole right-hand side.

### Current spread, with the counting criterion stated

The title records 11 blocks. Measured 2026-08-22 with a different and looser
criterion — files containing the literal `q^{1/2} - q^{-1/2}` **and** all
three of `L_+`, `L_-`, `L_0`:

| | files |
|---|---|
| carry the half-power string at all | **38** |
| state a skein relation in Form B | **17** |
| state Form A (`L₊ − L₋ = (q − q⁻¹)L₀`) | **6** |

Roughly 3:1 against the canonical form. The 6 Form-A blocks include
`climax-volume-mass/skein-bar-antisymmetry` and the definition index entry
for `prop:skein-bar-antisymmetry`, i.e. the canonical statement is the
minority in its own corpus. Do not read the 17-vs-11 gap as growth without
re-running the earlier criterion; they are different measurements.

### Why this is flag-don't-fix

`s = q^{1/2} − q^{−1/2}` is **live in the physics**, not only in prose:
`observations/hadron-half-life-verification-table1-data` lists it as the
weak coupling ("Skein amplitude (no W boson)"), and
`trace-ratio-interpretation` uses `s` and `𝔈_× = ½(q−q⁻¹)` in the *same
sentence* as distinct quantities. At the proton pin those are
**0.1043880583** and **0.1045301494** — a 0.136 % difference sitting inside
the half-life prefactor. Normalising the convention moves published numbers,
so it needs an owner decision, not an audit agent's edit.

One clean identity worth keeping either way: `s² = q + q⁻¹ − 2` exactly
(both 0.01089686671 at the proton pin).

### Note on the half-powers

`q^{±1/2}` is the same signature AGENTS.md ties to the excised Markov
convention C (`z_C = (q^{1/2}+q^{−1/2})⁻¹`). Whether the skein convention
and the Markov convention share a root is not established here — but they
should probably be decided together rather than separately.
