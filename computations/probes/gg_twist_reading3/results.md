# Reading 3 with the photon twist L± added to the γγ words — results

Pre-registration: `preregistration.md` (commit 72aa0c3f14b, before any run). Proton pin q₀, convention D,
mpmath 40 dps, levels 1..12. Nothing fitted or selected against data. Whether L₊ = σ₀σ₁, L₋ = σ₀⁻¹σ₁⁻¹
join the γγ rule is an owner ruling; this probe only measures what happens if they do.

## Stage 1 — single 3-strand words over {V, V⁻¹, L₊, L₋}, length 1–6

Witness `gg-twist-reading3.witness.json`.

| | count |
|---|---|
| words | 5460 |
| pass reading 3 at every level | 1778, all 3-component (pure) |
| fail | 3682, all 1-component (knots) |

- Pass ⟺ pure braid, on this whole set. No knot passes.
- Passing writhes run −12..12, symmetric counts, so L± does give chiral passing words.
- Shortest chiral passers: V⁻¹L₊ = σ₁² (min level char 1.128) and V⁻¹L₋ (0.8117).
- L₊³ min level char 1.0; L₋³ 0.5347.
- Control L₊σ₀ = σ₀σ₁σ₀ (the weak-vertex thread's trefoil route) is 2-component and fails at
  level 3, block (2,1), character 0. It is not reachable as a passing γγ+L± word.

## Stage 2 — H₂ with the length-2 chiral electrons

Witness `gg-twist-reading3-stage2.witness.json`. Nucleon V³ or V⁶; electron one of V⁻¹L₊, V⁻¹L₋,
L₊V⁻¹, L₋V⁻¹; both atom orders; bonds none, V, V², V³ at sites 4, 5.

| electron | bare H₂ (both orders, both nucleons) | bonds passing every level |
|---|---|---|
| V⁻¹L₊ (= σ₁²) | passes | V²@4, V³@4, V³@5 |
| V⁻¹L₋ | passes | V³@4, V³@5 |
| L₊V⁻¹ | passes | V³@4, V³@5 |
| L₋V⁻¹ | passes | V³@4, V³@5 |

Identical for nucleon V³ and V⁶. Trace ratio for V³ ≈ 0.9968–0.9986 (reported, not used to select).

Baseline (h2_gg_atom, T_w0 electron): bonds passing = exactly V³@4, V³@5. So:

1. The chiral L± electrons are admissible in H₂ exactly as the achiral Vᵏ electrons are.
2. V³ stays the bond in every one of the 16 cells.
3. One electron, V⁻¹L₊ = σ₁², also admits V² at site 4. With that electron the bond is no longer unique.

Scope (a): these are statements about this word set and these levels; nothing here excludes an ingredient.

## Trefoil (owner question 2026-11-16)

Script `trefoil_reading3_probe.py`, witness `trefoil-reading3.witness.json`. All 11 trefoil words and
trefoil composites fail reading 3 at q₀ (both handednesses; square and granny knots; trefoil plus a crossing;
trefoil ⊔ mirror on 4 strands, with and without a joining crossing).

The failure is q-independent (exact, from the Hecke relation σ² = hσ + 1, h = q − q⁻¹):
- 2 strands: χ_(2)(σᵏ)·χ_(1,1)(σᵏ) = qᵏ(−q⁻¹)ᵏ = (−1)ᵏ, negative for the odd k a knot needs, at every real q.
- 3 strands, block (2,1): tr(σ₀σ₁) = −1, tr σ₁ = h, σ₀³ = (h²+1)σ₀ + h, so tr(σ₀³σ₁) = −1; and tr((σ₀σ₁)²) = −1.
Readings 1 and 2 (block PSD, symmetric part PSD) imply a nonnegative trace, so they fail too. The only escape is
a Markov parameter giving these blocks zero weight (the one-row truncation z = q), which is not convention D.

### Complex q (owner card 2026-11-16)

`trefoil_complex_q_check.py` (sympy, formal q): every 3-strand trefoil braid has (2,1) trace exactly −1 as a
rational function of q, so at every complex q that block's trace is the negative real number −1. Any positivity
notion on ℂ that contains the positive reals and excludes −1 (Re ≥ 0, a sector, the real cone) fails it; only
the modulus passes it, and the modulus passes every word.
On 2 strands χ_(2)(σ³) = q³, χ_(1,1)(σ³) = −q⁻³: both real parts ≥ 0 only when cos(arg q³) = 0, where both are
exactly 0 (e.g. q = e^{iπ/6}, a 12th root of unity) — a boundary point, not a pass with positive weight, and
it is not q₀.

## Stage 3 — full-photon γγ words (pre-registered in 3df55fdc6d7)

**Word set.** The photon is γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁, and two-photon products span H₃(q)
(`gamma-gamma-generates-particles`, theorems `gamma_gamma_chirality_surjective`,
`gamma_gamma_reaches_Lminus`). With γ and γ̄ the words are all of B₃, so L± = σ₀σ₁, σ₀⁻¹σ₁⁻¹ are
included. The probe takes every freely reduced word over {σ₀^±1, σ₁^±1} of length 1..7
(4372 words). Reading 3, levels 1..3, convention D, proton pin, mpmath 40 dps. About 5 s.

**Pre-registered prediction: "pass ⟺ pure braid". It FAILED as stated.**

| closure | words | pass (site reading) |
|---|---|---|
| knot (1 component) | 720 | 0 |
| pure (3 components) | 372 | 372 |
| 2-component | 3280 | 1214 (954 strictly, 260 at exactly 0) |

The 2-component passes depend on placement. Every word whose permutation is (1,0,2), so that the
linked pair sits on strands 0–1, fails (1112/1112). On permutations (0,2,1) and (2,1,0) about half
pass, and the mirror of every strict passer fails (954/954). So level-by-level reading 3 is not
invariant under conjugation: it sees which strands carry the pair, because the level-1 and level-2
restrictions privilege strand 0.

**Conjugation-invariant reading 3.** A word passes only if every word in its orbit passes, where
the orbit is its cyclic rotations, conjugations by each letter (freely reduced), and the σ₀↔σ₁
flip. Under this reading the prediction holds exactly: pure 372/372 pass, 2-component 0/3280,
knots 0/720 (`conj_invariant_pass_iff_pure`, 0 violations).

Scope (a): this is a finite computation on words of length ≤ 7 at one q. It is not a proof for B₃.
Witness: `gg-full-photon-stage3.witness.json`.
