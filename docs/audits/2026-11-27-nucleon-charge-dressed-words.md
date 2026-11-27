# Distinct proton and neutron words: the crossing-local charge dressing (C2 replaced)

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-uud-udd-words-2026-11-27`
**Beans:** `qou-2skq` (this item), parent `qou-myts`; related `qou-99qc`
**Lean:** [`QOU/Nuclear/NucleonChargeDressedWords.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonChargeDressedWords.lean) (lean-verify exit 0; axioms propext, Classical.choice, Quot.sound; generic `[Field R]`)
**Probe:** [`computations/probes/nucleon_charge_dressed_words_probe.py`](../../computations/probes/nucleon_charge_dressed_words_probe.py) → `nucleon-charge-dressed-words.witness.json` (exact sympy over ℚ(q,c,a,b) from the full 8-dim Jimbo action, then 80 dps at both q₀ anchors; 7/7 assertions)

## 1. Short answer

Owner, 2026-11-27: *"Build different proton and neutron elements. Use uud and udd words under the
three-colour working assumption. This changes C2"*. Card choice: option 1, crossing-local charge
words (all recommended options taken, 17:16 UTC).

* **C2 as it stood** (`DecayConjectures.NucleonElementsAreGammaGammaBase`): both nucleons carry the
  same word `V³ = (σ₀σ₁⁻¹)³` on their weight spaces. PR #9453 proved that one shared element has
  equal plain traces on `W_p` and `W_n`, so only the Cartan weight `K` separates them.
* **Colour cannot separate them.** Under the 2026-11-22 three-colour working assumption the colour
  singlet `ε_q` is one-dimensional and shared by `p` and `n`, and on it the strand braid is `−q⁻¹`
  times the flavour braid (`JimboGl3Singlet.singlet_unique`,
  `ColourSingletDownstream.trace_word_smul`; `2026-11-22-strand-colour-downstream-impact.md` §5).
  Colour is a common factor. A word-dependent split must carry flavour inside the word.
* **Construction.** Dress every crossing with the charge product of the two strands that meet:
  `σ_k^{±1} ↦ σ_k^{±1}(1 + c·Q_kQ_{k+1})`, `Q = diag(a, b)`. `Q_kQ_{k+1}` commutes with the crossing
  (proved), so the dressing is well defined; it is not in the image of the braid algebra, so the
  single-element theorem does not cover it.
* **Result (proved, every `q ≠ 0`, every `a, b, c`):**
  `tr Mn − tr Mp = c·(a − b)·(1 + abc)³·G(q,a,b,c)/q⁶`, `G` explicit and quadratic in `c`.
  The split vanishes when undressed (`c = 0`, consistent with #9453) and when the two charges are
  equal; otherwise it is non-zero and depends on the word through `G`.
  First order: `∂_c(tr Mn − tr Mp)|₀ = 3(a − b)(a·G₁(q) + b·G₂(q))/q⁶`, `G₁(1) = G₂(1) = −2`.

The coupling `c` is **not derived** here. It is the same undetermined coupling as the two-term
`c_em`; route 1 of the nucleon split (thread "Derive the neutron-proton mass split") is the one
deriving it. `NucleonElementsAreChargeDressed` states the replacement C2′ as a `Prop` class with
no instance.

## 2. Evidence

| statement | Lean | probe |
|---|---|---|
| dressing commutes with its crossing | `chP12_comm`, `chP23_comm`, `chN12_comm`, `chN23_comm` | `dressing_commutes_s1/s2` (8-dim) |
| one period closed forms | `Lp_eq`, `Ln_eq` | — |
| split closed form | `trace_dressed_split` | `lean_closed_form` (from the 8-dim action, not the 3×3 matrices) |
| `c = 0` ⇒ equal | `trace_dressed_split_zero_of_c` | `undressed_equal` |
| `a = b` ⇒ equal | `trace_dressed_split_zero_of_charge_eq` | `equal_charges_equal` |
| non-zero split | `trace_dressed_split_ne_zero` | first-order coefficient ≠ 0 at both anchors |
| first-order coefficient | `firstOrder_eq`, `G₁_one`, `G₂_one` | — |

Numbers at the proton `q₀ = 1.10997858275138080759…`, charges `a = 2/3`, `b = −1/3`
(muon anchor agrees to 8 digits):

| quantity | value |
|---|---|
| `t(V³) = tr_{W_p}(V³)` | 2.99418581297996 |
| `∂_c(tr Mn − tr Mp)` at `c = 0` | −1.99028185862 (−0.6647 relative to `t`) |
| Gibbs cell `E₀(2 log q − log(tr Mn/tr Mp))` at `c = 0`, `E₀` order zero | 0.873537 MeV |
| its slope `∂_c` at `c = 0` | +2.78249 MeV |

## 3. Comparison boundary (the only place data enters)

CODATA 2022 `m_n − m_p = 1.293332 MeV`. **Diagnostic, not adopted:** under the Gibbs map the
dressing reaches it at `c = 0.15747` (order-zero `E₀`) or `0.15250` (tower `E₀`). The two-term
diagnostic of PR #9453 (a `K`-level scalar coupling) needed `c ≈ 0.258`; the crossing-local
dressing needs less because it acts inside the word. Neither value is derived, and selecting one
would be a fit.

**Sign caveat.** With `c > 0` the dressing makes the neutron heavier. The classical Coulomb
self-energy makes the proton heavier (`NeutronProtonEMSign`). So if `c` is read as the Coulomb
coupling with its classical sign, the dressing moves the cell away from CODATA; with `c > 0` it moves
towards it. The sign of `c` is part of what route 1 must derive. Nothing here fixes it.

## 4. Scope

* (a) This construction, with an underived `c`, gives distinct proton and neutron elements with a
  word-dependent split. It does not by itself give a number.
* Not excluded: the position-labelled reading of the pure braid `V³` (diagonal entries
  `⟨uud|V³|uud⟩ = −(q²−2)(q⁴−q²+1)`, already in `BorromeanRingColouredTrace.lean`), which is
  parameter-free but needs a choice of which strand holds the odd quark; and the four-strand
  lepton reading (`NeutronFourStrand.lean`).

## 5. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonChargeDressedWords.lean
python3 -u computations/probes/nucleon_charge_dressed_words_probe.py
```

`scripts/precision-gates.sh --changed`: Q0_FLIP 0, no NEW dirty witnesses; the reds (q0-anchor
flip, witness-value copy ratchet, CODATA stale-edition) are corpus-wide and name no file of this
change.

## 6. Addendum: charges in the ruled photon's weights (follow-up, same day)

Owner standing pick (17:16 UTC): the recommended follow-up, "put the charges into the ruled
photon's weights". Question: does the ruled photon fix the coupling `c`?

The Borromean core is the ruled photon pair, `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h) = 1 + h²W − h²W²`,
`W = σ₀σ₁⁻¹`, and the 2026-11-25 linking-neutrality ruling derives the weights from that identity.
Dress the photon's vertex: `W ↦ L` (the dressed period of §1). Two results, Lean §5 of the same file:

1. **The factorisation forces `c = 0`.** `ac_eq_zero_of_photon_factorisation`: if
   `L³ = 1 + h²L − h²L²` on `W_p`, then `a·c = 0`, away from the loci `q² = 1`, `1 + a²c = 0`,
   `1 + abc = 0`, `a²bc + a + b = 0` (read off the `(1,0)` entry,
   `photonFactorisationDefect_one_zero`). The probe checks all nine entries on each weight space
   with the quark charges: for generic `q` the only common root in `c` is `c = 0`, on `W_p` and on
   `W_n`. So the ruled photon does **not** fix a non-zero coupling. It excludes one, as long as
   the dressed `V³` must still be the ruled photon pair. Scope: this is (b) for that class (the
   factorisation identity is the invariant), and it says nothing about a dressing that is not
   required to factor.
2. **The dressed photon pair, taken on its own terms, still splits, but only at order `(q²−1)⁴`.**
   `trace_photonPair_split`: `tr Γ(Ln) − tr Γ(Lp) = c(a − b)(q² − 1)⁴(1 + abc)·H/q⁶`. At the
   proton `q₀` with quark charges, `∂_c` at `c = 0` is `+0.005205`. That is about 1/380 of the
   dressed-word value `−1.990`, and it has the opposite sign.

Consequence for C2′: the two dressings are different elements once `c ≠ 0`, and only the
dressed word keeps the `V³` shape. The coupling stays underived.
