# Which word creates the e⁻ν̄ pair in β⁻ decay — proposal for owner ruling

Bean `qou-99qc`. Owner (Carl), 2026-11-21: propose, for his ruling, the word that creates the
lepton pair. **Nothing here is ruled.** No candidate was chosen by its `Q_β` or by any residual;
CODATA is not read.

Pre-registration: `computations/probes/beta_pair_creation_word/PREREGISTRATION.md` (commit
`ee04d3c394`, before any number). Probe + witness: same directory (8/8 assertions, proton `q₀`,
70 dps, exact in `ℚ(q)`). Lean: `QOU/QBeta/PairCreationWordGammaGamma.lean` (sorry-free).

## The decision

The corpus writes the β⁻ lepton pair only as a **disjoint union** `e⁻ ⊔ ν̄` (`beta-decay-skein`,
`antineutrino-knot`, `two-photon-pair-production`, `breit-wheeler`), so any word that links the
pair to the nucleon is a choice (P2, #8680). This note lists the words that corpus principles admit
and says which principle, if any, singles one out. Choosing among them needs you, because the
principles disagree: the γγ rule and reading 3 pick one word, and the derived W exchange picks a
different one.

## Setting (stated, not derived)

* Four strands. Strands 0–2 are the nucleon, the γγ + reading-3 core `β_Bor = (σ₀σ₁⁻¹)³`, which is
  the same element for n and p (#8636). Strand 3 is one lepton strand.
* The process word is `W = X · β_Bor`: the nucleon braid acts first, then the candidate `X`.
* **Premise L** (#8673, which you left undecided): the lepton strand carries `ν = u`, `e⁻ = d`, and
  the outgoing ν̄ is the incoming ν by crossing. Every charged-current statement below uses it.
* Trace: Ocneanu–Markov, convention D. At `q₀` the Markov weights are `y_(4) = 0.3193`,
  `y_(3,1) = 0.1861` and `y_(2,2) = 0.0612`; every shape with three or more rows has weight 0. So
  reading 3 constrains exactly `χ_(4), χ_(3,1), χ_(2,2)`. Checked: `tr_D = Σ y_λ χ_λ` on all 24
  basis elements of `H₄`.
* **Reading 3 at every level reduces to `H₄`.** Every two-row shape of `H₅` restricts to two-row
  shapes of `H₄` (branching), so non-negative `H₄` characters stay non-negative higher up.

## 1. The principles as filters (exact; counts from the witness)

| principle | what it admits | forces one word? |
|---|---|---|
| **Q** charge / `T³` / `Y` conservation | every word (Hecke elements commute with `U_q`) | no, it constrains states, not words |
| **G** γγ grammar (`GammaGammaWord`, vertices `Vᵢ = σᵢσᵢ₊₁⁻¹`) | 30 words of length ≤ 8 on four strands | no |
| **CC** non-zero n⊗ν → p⊗e⁻ block `[L]` | 572 of 937 letter words of length ≤ 4 | with crossing-count minimality: **`σ₂` alone** (length 1), unique |
| **wrap** (lepton crosses ≥ 2 nucleon strands) | 368 of 937 | no |
| **R3** reading 3 on the whole word | 179 of 937 | no |
| G ∧ CC | 23 of 30 | minimal is `V₁` (length 2), unique, but it **fails R3** |
| **G ∧ CC ∧ R3** | 3 of 30: `V₁³`, `V₀V₁V₀V₁`, `V₁V₀V₁V₀` | with minimality: **`V₁³ = (σ₁σ₂⁻¹)³`**, unique |
| Ḡ (mirror vertices `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` allowed) ∧ CC ∧ R3 | 8 of 84 words of length ≤ 6 | no, 8 words tie at length 6 |
| CC ∧ wrap ∧ cross term ≠ 0 ∧ R3, no γγ | 10 letter words of length ≤ 4 | no, 6 tie at length 3 (`σ₁²σ₂`, `σ₁σ₂σ₁`, `σ₂σ₁σ₂`, `σ₁⁻¹σ₂σ₁⁻¹`, `σ₁⁻²σ₂`, `σ₂⁻¹σ₁σ₂⁻¹`) |

Lean-proved exclusions, scope (b), invariant **writhe** (every γγ word has writhe 0,
`writhe_eq_zero`). None of the following can be a γγ word:
* the derived passage `σ₀σ₁σ₂` (writhe 3);
* the electron trefoil `σ₀³` (writhe 3);
* the weak knot `T(3,5)` (writhe 10);
* the single crossing `σ₂` (writhe 1).

So the γγ rule and the corpus's odd-writhe weak objects never meet in one word.

Two of the pre-registered priors failed:
* **PR3** ("CC implies wrap") is false. A single lepton crossing already carries the W
  (`σ₂ = R₀ + h·E⊗F`, #8638 Part A), so 265 CC words cross only one nucleon strand.
* **PR4** ("no unique word") is false within the ruled grammar G, and true once mirror vertices are
  allowed.

## 2. The surviving candidates

The cross term is `C(X) = tr_D(βX) − tr_D(β)·tr_D(X)`. The order of a quantity is the power of
`(q − 1)` it carries as `q → 1`.

| candidate | γγ? | CC block | wraps | `C(X)` | R3 at `q₀` |
|---|---|---|---|---|---|
| **(a) `V₁³ = (σ₁σ₂⁻¹)³`** | yes | ≠ 0, order 2, **both chiralities** | strands 1, 2 (net signed crossings 0, 0: Borromean) | `−(q²−1)⁶(q⁴+1)²(q⁴+q²+1)/(q⁸(q²+1)⁴)`, order 6 | ✓ `χ = (1, 2.984, 2.000)` |
| (b) passage `σ₀σ₁σ₂` (#8638) | no | `= (q²−1)·T⁺`, order 1, **chiral** | 0, 1, 2 | `q(q²−1)²(q⁴+1)(q⁴+q²+1)(q⁴−2q²−1)/(q²+1)⁵`, order 2 | ✗ `χ_(3,1) = −1.218` |
| (c) single crossing `σ₂` | no | ≠ 0, order 1, chiral | strand 2 only | **0** (connected sum, nucleon-blind) | ✓ |
| (d) `T(3,5)` on strands 1–3 | no | ≠ 0, order 1 | 1, 2 | order 3 | ✗ `χ_(2,2) = −1.133` |
| (e) left-handed vertex passages `ι₀ι₁ι₂`, `Ŵ₀Ŵ₁Ŵ₂` (`−h·P_L`) | elements, not words | ≠ 0 (orders 4, 1) | — | orders 5, 2 | ✗ (see the caveat below) |
| (f) mirror family, 8 words of length 6 | Ḡ only | ≠ 0 | 1, 2 | orders 4–6 | ✓ |

Caveat on (e): `ι = −h·P_L` carries an overall minus sign, so `ι₀ι₁ι₂` fails reading 3 on sign
alone. Reading 3 is not invariant under the scale of an element, so this failure says nothing about
the vertex. The same applies to any signed element.

Normal form of `V₁³ · β_Bor`: 17 basis elements `T_w`, listed exactly in the witness. Its
identity coefficient is `−(q⁴−q²+1)(q⁸−3q⁶+3q⁴−3q²+1)/q⁶`. The p⊗e⁻ column of its CC block on the
input `udd ⊗ u` is proved in Lean (`cc_column_udd`):

* `(q²−1)⁴(q⁴−q²+2)/q⁴`,
* `(q²−1)²(q³−q−1)(q³−q+1)(q⁶−2q⁴+3q²−1)/q⁹`,
* `(q²−1)²(q⁴−q²+1)(q⁶−2q⁴+3q²−1)/q⁸`.

It vanishes at `q = 1` and is non-zero at `q = 2`. An independent sympy run straight from the Lean
matrices reproduces the same three entries.

What `V₁³` is: the **Borromean core again**, on strands 1–3 (two nucleon strands and the lepton).
By the photon ruling, `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`, so `V₁³` is literally a product of two ruled
photons straddling the nucleon and the lepton. That is a γγ pair-production event in the corpus's
own grammar. Its closure is a pure braid, so **the lepton strand closes to an unknot**. Under your
#8677 ruling the unknot strand is the up-quark type and the electron is the trefoil, so in the knot
reading `V₁³` does not produce a trefoil electron. In the strand-colour reading (premise L) the
electron is the `d` colour on that strand, and there is no conflict.

## 3. Options for ruling

### Option A — rule `V₁³` as the pair-creation word
* **What it means:** the pair is created by the cheapest word that the ruled γγ grammar, a non-zero
  W exchange and reading 3 jointly admit. It is a second Borromean core sharing two nucleon strands.
* **What it costs:** nothing to compute; record the ruling in `qou-99qc`. A `Q_β` functional on it
  is a follow-up (one probe).
* **What it risks:**
  - Uniqueness depends on excluding the mirror vertices, which `GammaGammaWord` does exclude but
    `GammaGammaFourStrandFlavour.lean` uses; with them, eight words tie.
  - It depends on four strands with ν̄ as a crossed ν, and on premise L.
  - It is **not chiral**: both the n→p and p→n blocks are non-zero, against the left-handed
    structure of #8638 and `prop:weak-vertex-left-projector`.
  - Its W coupling is O(h²), not O(h).
* **What it commits to:** the weak vertex is not a separate letter but arises inside γγ words; the
  passage and `T(3,5)` stay outside the canonical word.

### Option B — rule the derived passage `σ₀σ₁σ₂`
* **What it means:** the lepton strand passes all three nucleon strands once. This is the one word
  whose amplitude is the derived `(q²−1)·T⁺`, and it is chiral.
* **What it costs:** an amendment to `qou-ales`, because the γγ rule cannot produce it (writhe 3)
  and reading 3 rejects it (`χ_(3,1) = −1.218`).
* **What it risks:** it exempts the weak sector from both selection rules, which is a new
  per-sector dispatch.
* **What it commits to:** weak words are selected by the charged current, not by γγ.

### Option C — rule the single crossing `σ₂`
* **What it means:** the minimal W vertex. It is unique under CC plus minimality and passes
  reading 3.
* **What it costs:** nothing.
* **What it risks:** its cross term is exactly 0. The pair stays a connected sum, nucleon-blind at
  the trace level, so the factorisation no-gos (#8616, #8639, #8661, #8623, #8676) all still apply.
* **What it commits to:** the "entangled pair" idea of P2 is dropped at the trace level.

### Option D — rule the grammar question first (are mirror vertices `V̄ᵢ` γγ?)
* **What it means:** the answer decides whether A is unique (V only) or an eight-word family
  (V and V̄).
* **What it costs:** one ruling. If V̄ is admitted, a follow-up enumeration with a cost tie-breaker
  or a new principle.
* **What it risks:** none beyond the delay.
* **What it commits to:** fixes `GammaGammaWord` for every later selection, including the nucleon
  (#8636 used the V-only grammar).

### Default (nothing ruled)

The pair stays a disjoint union `e⁻ ⊔ ν̄`, as the corpus writes it. All the factorisation no-gos
stand. Nothing in the corpus or the dashboard changes, and the probe and Lean stay as records.

### Recommendation (my judgement, not a finding)

**D first, then A if the mirror vertices are excluded.** A is the only candidate that every ruled
selection principle admits at once, but it is unique only under the V-only grammar, and it is not
chiral. That is a real tension with the derived weak vertex, and you should see it before ruling,
not after.

## 4. What is NOT established

* Minimality is over the stated families: every G word up to length 8, every letter word up to
  length 4, and block products of two. The minimality of `V₁³` within G is complete, because every
  shorter G word was enumerated. Five or more strands (a separate ν̄ strand, vertex `V₂`) were
  **not** enumerated.
* Reading 3 is evaluated at `q₀` in mpmath at 70 dps, not proved in Lean.
* No energy functional and no `Q_β` is computed for any candidate.
