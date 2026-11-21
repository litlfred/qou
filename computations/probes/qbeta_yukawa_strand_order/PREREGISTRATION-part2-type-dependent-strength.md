# Pre-registration, part 2: is a type-dependent (quark vs lepton) Yukawa strength derived?

Bean `qou-99qc`. Written 2026-11-21, after the corpus-grep and BEFORE the Lean file or the probe.
Owner (Carl, 2026-11-21) chose option 3 of PR #8740: *"Research type-dependent strength"*.
Part 1 (`PREREGISTRATION.md`) found the strand order not forced and the four strengths not
derived; the type-only split is `∓(y_q² − y_ℓ²)(q² − 1)/(q² + 1)` (∓ by strand order).

**Disclosure.** Before writing this file I ran one exact scratch computation (sympy, `ℚ(q)`, no
floats, no comparison with any measurement): the right pivotal partial trace of the Jimbo
closure keeping strand 0, for `σ₀²` (Hopf), `σ₀σ₁σ₀` (the ruled electron) and
`V³ = (σ₀σ₁⁻¹)³` (Borromean). The values are stated below as found; nothing was compared with
`Q_β`, `m_n − m_p` or any mass, and no split was evaluated.

## Corpus-grep (six paths + `bun scripts/corpus-search.ts --limit 200`)

`corpus-search` returned 0 seeds for "Yukawa", "quark lepton coupling strength", "colour factor",
"per-component trace", "Hopf link Markov trace" (graph not populated in this checkout; silence is
not evidence). Grep found:

| object | where | bears on |
|---|---|---|
| ring-coloured trace; per-ring flavour NOT a link invariant (scope b); RT colours components by representations, `u,d` are weights of the one rep `V`; normalisation `[2]_q` per component | `BorromeanRingColouredTrace.lean` (#8706) | candidate 1 |
| electron `σ₀σ₁σ₀ ∈ B₃`, closure Hopf link (2 components); backup trefoil `σ₀³ ∈ B₂` | owner ruling 2026-11-21; `ElectronWordCandidates.lean` | candidates 1, 2 |
| up quark = unknot strand, a component of the Borromean braid | owner ruling 2026-11-20 | candidate 1 |
| neutrino carrier = the unknot | `docs/audits/2026-09-03-sm-26-term-status.md` §7 | candidate 1 |
| sl_N colour framing `σ^{sl} = q^{-1/N}σ`, for colour observables only | `Braiding/SlNFramingColourFactor.lean`, `sl-n-color-frame-scope.md` | candidate 4 |
| no object-level gate separates colour from flavour | `Eightfold/FlavourColourDiscriminator.lean` | candidate 4 |
| per-strand pairings are type-blind (`split_typeBlind`), compression of `a + bŘ` by the vev | `YukawaVacuumPairing.lean` (#8694) | candidate 5 |
| `m(K) = m_e Vol(K) ρ(K)/ℏ_q²`; absolute mass excised (2026-08-11); `m_e Vol(𝓑₃)ρ/ℏ_q²` not canonical (2026-06-24) | AGENTS.md | candidate 3 |
| quark masses all open; "Yukawa parameterisation … unreconciled" | `sm-params-quark-masses.md`, `2026-09-03-sm-26-term-status.md` §5 | all |
| no Yukawa field on `CategoricalHiggsIdempotent` | part 1 | all |

## Predictions (one verdict per candidate: derived / naming convention / new)

1. **Amplitude of the matter object in its own closure.** Three readings, none forced:
   * *per-component quantum dimension*: `[2]_q` on every component of both links → type-blind;
   * *the quark as its own knot type*: the ruled unknot, amplitude 1 — the same as the neutrino's
     unknot carrier, so it does not separate quark from lepton;
   * *cut-open closure* (right partial trace keeping one component): a scalar on `V` (Schur),
     and it does differ between the links. Scratch values: `σ₀²` ↦ `(q⁴+1)/q`;
     `σ₀σ₁σ₀` ↦ `q(q⁴+1)`; `V³` ↦ `−(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1)/q⁶` (`= 4` at `q = 1`). It is a
     FRAMED invariant: `σ₀σ₁σ₀` and `σ₀²` close to the same Hopf link and differ by the twist
     `θ = q²` (one unit of writhe). Using it as a Yukawa strength needs four unforced choices
     (the identification itself; framing; amplitude vs square; which reading).
   Verdict predicted: **new**.
2. **Strand number / Hecke level.** Under the ruling the electron word and `V³` both live in
   `B₃ / H₃(q)`, so any rule through the level gives `y_q = y_ℓ` and split `0`. Under the backup
   trefoil (`B₂`) the levels differ, but a level → strength rule is still new. Verdict:
   **naming convention** (under the ruling it is type-blind).
3. **Mass formula component-wise.** `Vol(Hopf) = Vol(unknot) = 0` (torus links), so the formula
   gives the electron strength `0`, contradicting `m_e ≠ 0` (CAL-1). The Borromean volume is a
   link invariant with no corpus rule distributing it over components; absolute mass is excised.
   Verdict: **excluded for the electron (scope b, invariant `Vol(Hopf) = 0` with `m_e ≠ 0`); the
   component split is new**.
4. **Colour factor 3.** The sl_N colour framing is a scalar rescaling of the crossing, so it leaves
   every eigenline projector, hence the vev weights `q²/(q²+1)`, `1/(q²+1)`, unchanged; the Higgs is
   a colour singlet. A colour multiplicity `N_c` per quark strand has no corpus object (colour and
   flavour are not separated at object level). Verdict: **new**.
5. **Higgs-vacuum compression on a 3-strand vs 1-strand object.** Local pairing on (strand, Higgs)
   is type-blind (#8694). A non-local Higgs line threading the object picks up, per crossed strand,
   `1` or `q` (over) / `q⁻¹` (under) according to the crossed strand's WEIGHT — flavour, not type —
   and the threading (position, over/under) is a choice. Verdict: **new**.

**Overall prediction: no type-dependent strength is derived** → a scope-(a) negative: these five
constructions, as the corpus states them, do not fix `y_q ≠ y_ℓ`. The strand order is then not
re-examined (it was conditional on a derived strength). No split is evaluated and nothing is
compared with CODATA.

## Scope

No strength is fitted, chosen or tuned; no reading, framing or order is selected by `Q_β`,
`m_n − m_p` or any mass. Lean: generic `Field`, sorry-free. Probe: exact `ℚ(q)` only.
