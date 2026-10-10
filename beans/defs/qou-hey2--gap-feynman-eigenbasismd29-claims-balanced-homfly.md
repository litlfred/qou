---
# qou-hey2
title: 'GAP: feynman-eigenbasis.md:29 claims balanced HOMFLY skein IS the braiding characteristic equation — false, nonzero Hecke residual; 11 blocks carry Form B'
status: completed
type: task
priority: normal
created_at: 2026-08-08T13:04:58Z
updated_at: 2026-09-05T18:17:48Z
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


## Superseded on the convention question; the ONE claim that is false regardless is fixed (2026-09-05)

**Corpus-grep first, and it landed on a sibling working this today.**
[`docs/audits/2026-09-05-two-skein-normalisations-are-live.md`](../docs/audits/2026-09-05-two-skein-normalisations-are-live.md)
(bean `qou-8bxv`) covers the spread question with a producer (8/8), a witness
and sorry-free Lean, and does it better than this bean does. It **proves** the
two relations are not rescalings of one another (`no_rescaling_of_skein_weights`
— the weight ratio on `(L₊ : L₋)` is `1` in (H) and `q²` in (J), and no constant
`c` in `[L] ↦ c[L]` fixes that except at `q² = 1`), gives the exact bridge
`h₁ = s·(q^{1/2} + q^{-1/2})` with `h₁²/s² = [2]_q + 2 = 4.0108968667` at the
proton pin, explains why bar-parity could not see the split (the cofactor is
bar-**even**), and traces a live consequence into the β-decay rate. Its verdict
on (H)-vs-(J) is the same as this bean's — an author decision touching a STRICT
rule — and it is now the carrier. **Do not duplicate it.**

Re-measured here for the record, same criterion as this bean's 2026-08-22 pass
(`q^{1/2} - q^{-1/2}` plus all of `L_+`, `L_-`, `L_0`): **38 → 48** files carry
the half-power string, **17 → 20** state a skein relation in Form B. The
problem grew by three in fourteen days. `qou-8bxv`'s narrower "**8 live content
blocks in five chapters**" is the better number — mine counts `docs/`, an
archive file, and Lean.

## 🛑 This bean's ARGUMENT is retracted. Its conclusion is not.

The table above evaluates Form B on σ's two Hecke eigenvalues and reports
`0 = 0.1044` on the antisymmetric channel. **That is not evidence about Form B**,
because Form B is not an operator identity in `H_n(q)` — it is a relation among
the *invariants* `[L_±], [L_0]` of three links. Plugging eigenvalues into it
tests a claim nobody makes. This is exactly the arity conflation AGENTS.md
§"Grep the claim SHAPE, not only the topic" describes: two statements sharing
symbols while quantifying over different objects.

**What IS false is the identification**, and it is false whichever convention
wins. `braids-and-knots/feynman-eigenbasis.md:29` said the displayed Form B
relation *"is simply the characteristic equation of the braiding `c_{V,V}`
evaluated under the categorical trace."* Tracing the characteristic equation
gives `m(L₊) − m(L₋) = (q − q⁻¹)·m(L₀)` — Form **A** at invariant level. The
`q^{±1}` weights are the **writhe/framing correction** (`L₊` and `L₋` differ in
writhe by two), which is a further step, not "simply" the traced characteristic
equation.

**Measured: exactly 1 of the 20 files carries that identification.** The other
19 write Form B as a relation among invariants, which is correct as written and
must **not** be swept — replacing them with Form A would make them
framing-incorrect. So this bean's implied action ("normalise ~17 sites; moves
published numbers by 0.136 %") collapses to **one sentence in one file, and no
number moves**.

Fixed in place, citing `qou-8bxv`'s audit for the non-rescaling result.
`detangler-no-forward-ref` (major) on that block is **pre-existing** — present
in the committed sidecar at HEAD before this edit.

**Remaining on this bean: nothing that is not `qou-8bxv`'s.** Closing as
superseded.
