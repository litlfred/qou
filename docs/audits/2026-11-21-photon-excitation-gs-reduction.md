# Is an excited electron a non-reduced word? Gröbner–Shirshov measurements

Date 2026-11-21. Owner question (Carl): *"I think one of your siblings is exploring photon
excitation of electrons, a bound atom. Can we see this in the grobner bases calculations that an
excited electron is a non-reduced?"*

This is a measurement plus two small Lean results. It changes no consumer and no content block.

Conventions: Hecke relation `σᵢ² = hσᵢ + 1`, `h = q − q⁻¹`; the Gröbner–Shirshov (GS) normal
form of `H_n(q)` is the `T_w` basis (`w ∈ S_n`); a word is **reduced** (GS-irreducible) when it
is a reduced expression, so no quadratic rewrite applies. The photon is the ruled form
`γ(φ) = 1 + φ₀σ_a + φ₁σ_b + φ₀₁·σ_aσ_b⁻¹` (owner ruling 2026-11-20). Markov trace convention D,
`z_D = q³/(q²+1)`. Exact over `ℚ(q, φ)` (sympy). No measured value is used.

## 1. Answer

**Partly, and it depends on which excitation construction is meant.** The corpus has two, and
they disagree with each other (§4).

| construction | where | excited word non-reduced? | where the excitation shows up |
|---|---|---|---|
| R-I curl as Markov stabilisation `w ↦ w·σ_n` | `mass-theory/transfer-matrix-operator-properties.md` §"Shell transitions as R-I moves" | **No.** `σ₀σ₁σ₀σ₂…` stays reduced. | Bruhat length `+1` per curl; Markov trace `× z_D` per positive curl, `× z̄_D = z_D(q⁻¹)` per negative curl |
| writhe `+2` on the same strand, `σ^{2n+1}` | `predicted-spectra/hydrogen-orbitals.md` (`n = (w−1)/2`) | **Yes, but the ground state is non-reduced too.** `σ³ = h + (h²+1)σ`. | only in the `q`-degree of the normal-form coefficients (`2n`) and in `χ = q^{2n+1}` |
| photon multiplied onto the electron's own strands, `γ·σ₀σ₁σ₀` in `H₃` | (direct reading of the question) | **Yes**, every photon monomial reduces | it cannot excite in length: `σ₀σ₁σ₀ = T_{w₀}` is already the longest element, so the normal form never exceeds length 3 |

So "non-reduced" is not by itself the signature of excitation. In the one construction where
an excited state is non-reduced (`σ^{2n+1}`), the ground state is non-reduced as well, and the
number of rewrite steps is not an invariant of the element (#8682 measures 25 vs 30 steps on
`(σ₁σ₂)⁵` with one normal form). What **is** an invariant, and does order the levels, is:

- **the index character** `χ(Σ c_w T_w) = Σ c_w q^{ℓ(w)}` (the one-dimensional representation
  `σ ↦ q`). Proved: `χ(NF(β)) = q^{writhe(β)}` for every signed braid word (§3). So the corpus's
  shell number `n = (w − 1)/2` is a function of the normal form: `χ = q^{2n+1}`.
- under stabilisation, **the top Bruhat length** of the normal form (`3 + k` after `k` positive
  curls), and the Markov-trace ratio `z_D` per curl.

## 2. Measurements

Probe: `computations/probes/photon_excitation_gs/excitation_gs_probe.py`, **17/17 checks**, witness
`excitation_gs_probe.witness.json` beside it. Command: `python3 -u excitation_gs_probe.py`.

Ground states:

| word | GS-irreducible | NF lengths | `χ` | `tr_D` |
|---|---|---|---|---|
| `σ₀σ₁σ₀` (corpus `e⁻`) | yes (0 rewrites) | {3} | `q³` | `q³(q⁴+1)/(q²+1)²` |
| `σ₀³` (trefoil on 2 strands) | **no** (2 rewrites) | {0,1} | `q³` | `(q⁶+q²−1)/(q(q²+1))` |

Stabilisation of `σ₀σ₁σ₀` (positive curls): every word is reduced (0 rewrites); NF is the single
word of length `3, 4, 5, 6`; `χ = q³, q⁴, q⁵, q⁶`; `tr_D = q^{3+3k}(q⁴+1)/(q²+1)^{2+k}`, ratio
`z_D` each step. One negative curl `σ₀σ₁σ₀σ₂⁻¹`: two NF terms (lengths 3, 4), `χ = q²`,
trace ratio `1/(q(q²+1)) = z_D(q⁻¹)`.

Same-strand powers `σ₀^m`, `m = 3, 5, 7, 9` (shells 1–4 under `n = (m−1)/2`): NF always two
terms `b_m + a_mσ₀`; left-to-right rewrites `m − 1`; `a_m = (q^{2(m−1)} − … + 1)/q^{m−1}`, so the
`q`-degree span of the coefficient is `m − 1 = 2n`; `χ = q^m`.

Photon on the electron's strands, `H₃`: `γ(σ₀,σ₁)·σ₀σ₁σ₀` and `σ₀σ₁σ₀·γ(σ₀,σ₁)` have NF lengths
{1,2,3}, top length 3; `σ₀·w₀` and `σ₁·w₀` each take 1 quadratic rewrite, `σ₀σ₁⁻¹·w₀` takes 4;
`χ = q³(1 + q(φ₀+φ₁) + φ₀₁)`. Photon sharing one strand, `γ(σ₁,σ₂)` in `H₄`: left product reaches
length 5, right product length 4. Photon on two new strands, `γ(σ₃,σ₄)` in `H₆`: `χ` and `tr_D`
factorise.

## 3. Lean (sorry-free)

`folio/quantum-observable-universe/lean/QOU/Excitation/WritheIndexCharacterH2.lean`, Mathlib only,
generic field `R`, `q ≠ 0`:

- `chi_nf`: in `H₂(q)`, `χ(NF(w)) = q^{writhe w}` for every signed word `w`.
- `chi_nf_append_two`: two added positive crossings multiply `χ` by `q²`.
- `nf_pow`: `(q+q⁻¹)·a_m = q^m − (−q⁻¹)^m`, `(q+q⁻¹)·b_m = q⁻¹q^m + q(−q⁻¹)^m` for
  `NF(σ^m) = b_m + a_mσ`.
- `nf_trefoil`: `NF(σ³) = h + (h²+1)σ`, so the ground-state trefoil is not reduced.

Verification: `lean -DautoImplicit=false -s 65536` exit 0; `#print axioms` on all four: `propext`,
`Classical.choice`, `Quot.sound`; no `sorryAx`.

Not formalised: the general-`n` statements (`χ(NF(β)) = q^{writhe}` in `H_n`, and length
additivity under stabilisation, `ℓ(w·s_n) = ℓ(w) + 1` for `w ∈ S_n`). Both are standard
(the trivial representation of `H_n`; Humphreys, *Reflection groups and Coxeter groups* §7.4)
and are checked here only by the probe, for all 341 signed words of length ≤ 4 in `H₃` and for
`k ≤ 3` curls.

## 4. The corpus's two excitation constructions disagree

- `hydrogen-orbitals.md`: photon absorption is "two R-I moves", writhe `w → w + 2`, shell
  `n = (w−1)/2`, and "the electron remains a trefoil".
- `transfer-matrix-operator-properties.md`: one R-I move per absorption, writhe `±1`, written as
  `σ_i ↦ σ_i·σ_n` (Markov stabilisation).

Read as braids, a writhe change that keeps the knot type must be stabilisation (it adds a strand).
Read on the same two strands, `σ^{2n+1}` closes to the torus knot `T(2, 2n+1)`, which is a trefoil
only for `n = 1`, so "remains a trefoil" fails under that reading. Under stabilisation the
excitation is reduced; under same-strand powers it is non-reduced at every level including the
ground state. Which reading is meant is an owner question (bean note).

Scope (a), not (b): neither construction alone produces a `1/n²` ladder. Stabilisation gives the
geometric trace factor `z_D^k`; this says nothing about a closure with further terms.

## 4a. Under the owner's electron ruling (added 2026-11-21, same day)

**The electron is `σ₀σ₁σ₀` and its closure is the Hopf link** (owner, 2026-11-21, "for now";
the trefoil `σ₀³` on `B₂` is kept as the backup reading). PR #8724 (merged) measured the same
fact: every odd-length word in `B₃` closes to two components, and `σ₀σ₁σ₀` closes to the Hopf
link. §4 above judged the two constructions against a trefoil electron, which this ruling
retires as the primary reading. Restated against it:

- **Ground state.** `σ₀σ₁σ₀` is the longest element `w₀` of `S₃`, so in `H₃` a photon cannot
  raise it: every product `γ·e` or `e·γ` needs rewriting and stays at length ≤ 3 (§3). In `H₃`,
  "non-reduced" means the product is already at the top. It does not mean excited.
- **Strand-adding curl** (`transfer-matrix-operator-properties.md`): `σ₀σ₁σ₀ → σ₀σ₁σ₀σ₂ → …`
  is Markov stabilisation, so the closure **stays the Hopf link**. The excited word is
  **reduced**; the level shows as word length (+1 per absorption) and as a factor `z_D` on the
  Markov trace. This construction is consistent with the ruling.
- **Same-strand writhe +2** (`hydrogen-orbitals.md`) applies only to the backup trefoil reading
  (`σ^{2n+1}` on `B₂`, closing to `T(2, 2n+1)`). Under the primary ruling it does not describe
  the electron.

So, under the ruling: **an excited electron is not a non-reduced word.** It is a reduced word on
more strands, with the same closure. The non-reduced products arise only when the photon acts
inside `H₃`.

## 5. Related work

- PR #8724 (other session): which word is the electron; GS interaction criteria, measure only.
- PR #8682 (`qou-99qc` P3): `χ(x) = Σ c_w q^{ℓ(w)}` as the index character; rewrite-order
  independence of NF invariants; the rewrite-step count is not invariant.
- No branch, PR or bean on "photon excitation of a bound electron" was found (searched open PRs,
  `claude/*` branches, `beans/defs`, `docs/audits`, `computations`, `folio` for *excit*, *photon
  absorption*, *bound atom*, *Rydberg*, *energy level*). The corpus text on the topic is the two
  blocks in §4. The sibling the owner has in mind may be a session that has not pushed.
