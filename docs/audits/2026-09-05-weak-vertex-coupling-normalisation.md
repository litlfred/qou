# `s²` is the q-dimension minus its classical value — and no constant rescales `W` onto it

*2026-09-05 · bean `qou-pfh7` · branch `claude/weak-vertex-coupling-normalisation-2026-09-05` · follow-on to #6715 (`qou-ix74`)*

`qou-ix74` established that substituting the weak-vertex trace `|W|²` for the
single-crossing coupling `s²` in the beta-decay rate multiplies every rate by
`1.19 · 10⁴`, and left one question open: **what normalisation relates the two?**
The owner's instruction was to work that question. There is a positive answer to
half of it and a proved negative on the obvious candidate. Neither fits a
coefficient.

## 1. What `s²` actually is — and this is the useful half

Exactly, over any field:

```
s² = (q^{1/2} − q^{−1/2})² = q − 2 + q⁻¹ = [2]_q − [2]_1
```

with `[2]_q = q + q⁻¹` the `SU_q(2)` fundamental quantum dimension and
`[2]_1 = 2` its classical value. So the coupling the decay rate uses is **not an
arbitrary crossing amplitude: it is a quantum dimension minus its classical
value.** That is what makes it vanish at `q = 1` and stop beta decay classically,
and it is the first derivation of the shape of `s²` in the corpus rather than a
restatement of it. Lean: `QOU.Braiding.WeakVertexT35.sSq_eq_twoQ_sub_two`,
sorry-free.

This immediately says what a `W`-based replacement has to look like. `W(1) = 1/4`
(`weakVertexTrace_one`), so `W` does not vanish classically, and the pattern above
motivates the family

```
coupling(q) = c · (W(q) − W(1)) · X(q)
```

with `X` some bridge factor. **The motivation is derived, not assumed** — that is
what distinguishes this from writing down a residual and reasoning about it, the
failure mode AGENTS.md names under *Defined residual ≠ derived decomposition*.

## 2. The family is excluded — and not by its order

`s²` vanishes to **second** order at `q = 1`: `s²(1) = 0`, `s²′(1) = 0`,
`s²″(1) = 2`, i.e. `s² = (q−1)² − (q−1)³ + …`. But `W′(1) = 5`, so `W − W(1)`
vanishes to **first** order: `5(q−1) + (93/4)(q−1)² + …`.

An order mismatch alone would not settle it, because one bridge factor vanishing
like `q − 1` repairs it, and the corpus supplies four candidates. Measured at the
proton pin, with the leading coefficient of `(W − 1/4)·X` in `(q−1)²`:

| bridge `X` | `(W−1/4)·X / s²` at `q₀` | leading coeff |
|---|---|---|
| `h = q − q⁻¹` | 17.986 | 10 |
| `ℏ_q = 1 − q⁻¹` | 8.524 | 5 |
| `s` | 8.981 | 5 |
| `q − 1` | 9.462 | 5 |
| `h/2` | 8.993 | 5 |

against `s²`'s leading coefficient of `1`. Every one carries the factor `W′(1) = 5`,
because that is what the first-order vanishing of `W − W(1)` contributes. So no
bridge in this list lands on `s²` even at leading order.

**What actually excludes the family is that the ratio runs.** For the
order-matched `ℏ_q` candidate:

```
R(q) = (W(q) − 1/4)·ℏ_q / s² = (q+1)(4q¹²+4q¹⁰+8q⁸+8q⁶+8q⁴+7q²+1) / (4(q²+1)²)

R → 5  (q → 1)      R(q₀) = 8.5242      R(3/2) = 65.269      R(2) = 695.91
```

A normalisation **constant** cannot absorb a running ratio. Equivalently, `c`
would have to be `100/69591` at `q = 2` and `86528/5647625` at `q = 3/2`. Proved
at those two rational points, sorry-free:
`no_constant_rescaling`, `candidateRatio_two`, `candidateRatio_three_halves`.

## Scope, stated per the (a)/(b) rule

This is a **scope-(b) structural exclusion** of the parametrised family
`c·(W − W(1))·X` for `X ∈ {h, ℏ_q, s, q−1, h/2}` — a *proved non-constancy* of the
ratio, not a bad number at one anchor. The invariant cited is the mismatch of
functional form, decided at two rational points.

It is **not** an exclusion of `W`, whose closed form (`qou-egvf`) is untouched, and
it is **not** an exclusion of every `W`-based coupling. Three shapes are untested
and remain live:

- a **ratio against another trace** in the same tower — the trefoil (electron)
  Markov trace is the natural denominator, since the corpus already reads the
  electron off the trefoil's three crossings;
- a **Jones-normalised** object: `V_K(1) = 1` for *every* knot, so `V_K − 1` is
  the topologically canonical deviation and its normalisation is fixed by
  topology rather than chosen;
- a **bar-parity component** of `W`, which the corpus uses elsewhere for exactly
  this kind of separation.

None of these is measured here. The remainder is on bean `qou-pfh7`; what would
settle it is a derivation of the coupling's normalisation from the rate formula's
own construction, not a further scan over candidate factors.

## Producer and verification

`computations/markov/weak_vertex_coupling_normalisation_probe.py` →
`weak-vertex-coupling-normalisation.witness.json`, 7/7. sympy-exact identities,
mpmath at 60 dps for the numerics, serialised at 50 digits. `lean`-direct exit 0
on `WeakVertexCouplingNormalisation.lean`; `#print axioms` on all six theorems
gives `propext, Classical.choice, Quot.sound` only.

## §7c note, and a latent flag in the two merged files

`scripts/check-sidecars.sh` flagged the first draft of the new Lean as *"MIXED
generic + archimedean → split into two files per §7c"*, and it was right: the
identities are generic-field results and the derivatives plus the two-point
exclusion need `ℝ`. The file is split accordingly —
`WeakVertexCouplingNormalisation` (generic `K`) and
`…Archimedean` (`K := ℝ`) — and both now read *"generic OK"* / *"ℝ justified"*.

**The same latent flag applies to the two files merged earlier in this arc**,
`WeakVertexT35TraceClosedForm` (generic Wedderburn identities alongside the
`1.187 < W(q₀) < 1.188` bound) and `WeakVertexSubstitutionScale` (generic
`substitutionRateFactor_eq` alongside the two `10⁴` bounds). Neither is flagged
today because the gate only inspects *changed* files, and neither is touched
here. Splitting them is mechanical and behaviour-free — declaration names would
not change, so every witness and audit reference keeps resolving — but it means
editing and re-verifying two already-merged files, so it is recorded on bean
`qou-pfh7` as a follow-up rather than widening this tranche.
