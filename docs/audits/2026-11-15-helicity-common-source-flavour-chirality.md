# Do flavour and chirality share the letter orientation as their source?

Bean `qou-hlx6` (epic `qou-qs0e`). Lean file:
`folio/quantum-observable-universe/lean/QOU/QuarkState/HelicityCommonSource.lean`.
Built on stream 6a (PR #7827, `PhotonPairNormalForm.lean`) and read against stream 6b
(PR #7825, `PolarizationActionHecke.lean`, `ChiralityPolarizationHopf.lean`). Verification
is in §6.

## 0. Result

The hypothesis under test was the coordinator's, **not a finding**: *the letter orientation
σ vs σ⁻¹ (6a's net-flavour bit) is the same datum as the choice of which eigenline of that
letter (eigenvalue q or −q⁻¹) is called left-handed (6b's chirality pair).*

**Verdict: refuted, scope (b).** The orientation flip and the eigenline swap are two
different involutions of a single letter. The flip keeps both eigenlines and inverts both
eigenvalues; the swap exchanges the eigenlines and keeps the Hecke parameter. The invariant
that excludes the identification is a proved identity: the flip fixes both eigenprojectors
(`flip_Pp`, `flip_Pm`), the swap exchanges them (`swap_Pp`), and the two projectors differ
whenever P₊ ≠ 0 (`flip_ne_swap`).

The physics consistency checks of §3 come out the same way. Under the corpus flavour flip, u
and d of one letter share the same L/R pair, so nothing forces u and d to differ by
chirality. The flip is also chirality-blind, so it cannot by itself be a weak isospin acting
on L only.

## 1. One letter, two projectors, two involutions

Take a letter s in any K-algebra A with s² = h·s + 1, h = q − q⁻¹, q ≠ 0, q + q⁻¹ ≠ 0. This
is the BW "photon helicity equation" (`breit-wheeler-vertex.md:14`).

| object | definition | eigenvalue on P₊ | eigenvalue on P₋ | Hecke parameter |
|---|---|---|---|---|
| s | the letter | q | −q⁻¹ | q |
| **flip** s = s⁻¹ = s − h | 6a's flavour flip | **q⁻¹** | **−q** | **q⁻¹** |
| **swap** s = −s⁻¹ = h − s | exchange L ↔ R | −q⁻¹ | q | **q** |
| −s | composite | −q | q⁻¹ | q⁻¹ |

Here P₊ = (s + q⁻¹)/(q + q⁻¹) and P₋ = (q − s)/(q + q⁻¹). Lean: `eigen_plus`,
`eigen_minus`, `Pp_add_Pm`, `Pp_mul_Pm`, `Pp_idem`, `inv_letter`, `flip_hecke`,
`flip_eigen_plus`, `flip_eigen_minus`, `swap_hecke`, `swap_eq_neg_flip`.

The four elements are the orbit of s under a Klein four-group. Its two generators answer two
different questions:

* **the flip is the Kazhdan–Lusztig bar involution on one letter** (σ ↦ σ⁻¹ with q ↦ q⁻¹).
  It fixes both idempotents: `flip_Pp : Pp q⁻¹ (flip q s) = Pp q s`.
* **the swap is the q-linear sign involution** σ ↦ −σ⁻¹. It is the only other letter at
  the same parameter q in K[s], and it exchanges P₊ and P₋.

### Item 1 of the brief: does σ ↦ σ⁻¹ swap the eigenlines?

**No.** The two lines are the same idempotents, and the eigenvalues are inverted on both
(q → q⁻¹, −q⁻¹ → −q). This is the coordinator's note ("same eigenlines with eigenvalues
inverted"), now proved.

**One labelling makes it look like a swap. It is recorded here so nobody rediscovers it as
a confirmation.** Suppose "L" is defined as *the line carrying the eigenvalue of larger
modulus*. That is an archimedean rule, and it needs a real q > 1. Under that rule the flip
moves the label from P₊ (|q| > 1) to P₋ (|−q| > 1). But this moves the label, not the line:
it is a statement about the spectrum, which the flip inverts. Under the two algebraic
labellings it does not happen:
* labelling by the Hecke parameter (the eigenvalue equal to the letter's own parameter);
* labelling by sign.

The 6b/BW labelling is by the roots +q and −q⁻¹ of the Hecke relation, which is the
parameter labelling. Under it the flip preserves L.

## 2. Item 2: is net flavour a function of the L/R labelling?

6a's `netFlavour` is the h¹ coefficient of the unit coordinate, with h formal. The three
letter forms of one generator give:

| letter | netFlavour | eigenline pair |
|---|---|---|
| σ | 0 | (P₊, P₋) |
| σ⁻¹ | −1 | (P₊, P₋), the same idempotents (`corpus_flavours_same_lines`) |
| −σ⁻¹ | +1 | (P₋, P₊), swapped |

Lean: `netFlavour_swapLetter`, `netFlavour_flavours_differ`, `corpus_flavours_same_lines`.

**On the corpus letter set {σ, σ⁻¹}, net flavour is not a function of the eigenline
labelling.** The two flavours have identical labelled eigenlines and different net flavour.

**On the fixed-parameter set {σ, −σ⁻¹}, net flavour does separate L from R** (0 vs +1). This
is the strongest positive statement available. But −σ⁻¹ is not a corpus flavour, and the flip
and the swap move net flavour in opposite directions (−1 and +1). So net flavour responds to
both involutions. It is one coordinate that reads a combination of the two bits, and it is
neither bit by itself.

## 3. Item 3: physics consistency

**u and d do not differ by chirality.** Under the corpus flavour flip, u (σ) and d (σ⁻¹)
carry the same pair of L/R projectors. A u_L, u_R, d_L, d_R assignment is therefore not
obstructed by this construction. Nothing here contradicts the existence of all four.

**Weak isospin acting only on L.** The corpus flip is chirality-blind: it inverts the
eigenvalue on both lines (`flip_eigen_plus`, `flip_eigen_minus`). A one-sided version would
invert the eigenvalue on P₊ and leave P₋ alone. `no_one_sided_letter` proves that such an
element satisfies a Hecke relation at some parameter p only if q² = 1, given char ≠ 2 and both
projectors nonzero. So a left-only flavour flip is **not a letter**.

* **Scope (b) for the claim "a letter realises a left-only flip"**, with the invariant being
  that proved identity.
* **Scope (a) for "the corpus cannot carry V−A"**: a chiral isospin could still be a
  non-letter operator, or live elsewhere in the tower.

## 4. Item 4: the photon orientation bit as photon helicity

The BW block (`breit-wheeler-vertex.md:14`) calls the two roots +q and −q⁻¹ of one letter
the left and right circular polarisations. By §1, the flip σ ↦ σ⁻¹ does not exchange them.
So **the photon's letter orientation is not its helicity** in the BW sense. The helicity
exchange on one letter is the swap σ ↦ −σ⁻¹.

For completeness, here is what γγ gives if the photon's letters are swapped instead of
flipped. Define γ̃(ψ) = 1 + ψ₀(h−σ₀) + ψ₁(h−σ₁) + ψ₀₁(h−σ₀)(h−σ₁) (`photonSwap`):

| pair | net flavour | source |
|---|---|---|
| γ(φ)·γ(ψ) | 0 | 6a `pairNF_netFlavour` |
| γ(φ)·γ_flip(ψ) | −(ψ₀+ψ₁) − (φ₀+φ₁)ψ₀₁ | 6a `pairBar_netFlavour` |
| γ(φ)·γ̃(ψ) | +(ψ₀+ψ₁) − (φ₀+φ₁)ψ₀₁ | `pair_id_swap_netFlavour` |
| γ̃(φ)·γ(ψ) | (φ₀+φ₁) − φ₀₁(ψ₀+ψ₁) | `pair_swap_id_netFlavour` |

Two observations. They are measured, and neither is an identification:

* On the polarization part (ψ₀ + ψ₁) the flip and the swap contribute with **opposite
  sign**. On the ψ₀₁ cross term they agree. This is the §2 pattern lifted to the pair.
* In every row, net flavour depends on the continuous colour content. A per-letter integer
  flavour (6a's 0 / −1) is therefore not produced by γγ in any of these orientation or
  helicity combinations, which extends 6a's scope-(b) result for σ-photons.

Swap–swap and flip–swap pairs were computed symbolically (sympy, exact). They are not in Lean:
* swap–swap gives (φ₀+φ₁)(1+ψ₀₁) + (ψ₀+ψ₁)(1+φ₀₁);
* flip–swap gives −(φ₀+φ₁)(1+ψ₀₁) + (ψ₀+ψ₁)(1+φ₀₁).

## 5. What is NOT established

* γ̃ ("swapped photon") is a construct of this file. The corpus does not define a photon with
  −σ⁻¹ letters, and nothing here proposes one.
* Whether the "larger-modulus" labelling of §1 is the one physics should use is not decided
  here. It would make the flip look like a swap. Stated as an owner decision in §7.
* Nothing in this audit is written into content blocks. In particular, no identification of
  either bit with a physical quantum number has been written.

## 6. Verification

Restored the Mathlib cache from `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`, plus its
gap-module addon. The 6a dependencies were compiled lean-direct into a scratch olean
directory:
* `MarkovTraceOnHecke`
* `HeckeH3AlgebraLaws`
* `HeckeH3AlgebraInstance`
* `PhotonPairNormalForm`

All four exited 0. Then:

```
source scripts/lean-direct-env.sh
LEAN_PATH=<scratch>:$LEAN_PATH lean -DautoImplicit=false -s 65536 \
  folio/quantum-observable-universe/lean/QOU/QuarkState/HelicityCommonSource.lean   # exit 0, no warnings
```

`#print axioms` on 10 declarations reports `[propext, Classical.choice, Quot.sound]` only:
* `flip_ne_swap`
* `no_one_sided_letter`
* `corpus_flavours_same_lines`
* `netFlavour_flavours_differ`
* `netFlavour_swapLetter`
* `pair_id_swap_netFlavour`
* `pair_swap_id_netFlavour`
* `flip_eigen_minus`
* `swap_hecke`
* `sig1_letter`

The file has 0 `sorry`.

`scripts/lean-library-sweep.py` could not be used. This container's paper-tree Mathlib
oleans are absent (98 against 3566 in the root tree), so the sweep reports UNVERIFIED on a
missing Mathlib olean. That is about the cache, not the source.

## 7. Owner decisions

> **Decided 2026-11-15 (relayed by the coordinator, session_01M5GA1LmsEf8tSMxFjMkmnn):
> D-H1 = A, D-H2 = no.** The Hecke-parameter labelling is canonical (BW's +q root is L), and the
> swap is not added as a second per-letter bit: chirality stays on the cone side. The left-only
> weak coupling therefore still needs a separate source (scope (a) for V−A), tracked as bean
> `qou-hlx7`.

### D-H1: which labelling of L/R is canonical for a letter?

* **(A) By the Hecke parameter.** L is the line whose eigenvalue equals the parameter; this
  is BW's +q root. *Means:* the orientation bit and the chirality bit are independent, as
  proved here. *Costs:* nothing; it is the corpus reading. *Risks:* none new. *Commits to:*
  flavour and chirality being separate per-letter data. A V−A mechanism must then come from
  outside the single letter (`no_one_sided_letter`).
* **(B) By modulus (archimedean, q > 1).** *Means:* the flip DOES relabel L ↔ R, so
  "orientation = chirality" becomes true by convention. *Costs:* it requires real q > 1 at
  the letter level, which breaks the generic-R discipline (§7c). *Risks:* this is an
  identification by labelling choice, the kind the owner has forbidden. It also makes u and
  d differ by chirality, which contradicts u_L, u_R, d_L, d_R. *Commits to:* an archimedean
  definition of chirality.

**Default if nothing is said: (A).** Nothing changes; the hypothesis stays refuted.
**Recommendation (judgement): (A).** (B) only manufactures the hypothesis.

### D-H2: should the photon's helicity exchange (the swap σ ↦ −σ⁻¹) enter the quark-state work as a separate bit?

* **(yes)** *Means:* carry a second per-letter bit in 6a's `quarkLetter`, giving four
  letter forms. *Costs:* one Lean definition plus re-running 6a's γγ reachability with it;
  the §4 table is the start. *Risks:* γ̃ is not a corpus object, so this is new modelling
  and has to be stated as such. *Commits to:* a two-bit letter.
* **(no)** *Means:* leave chirality on the cone side (6b, the polarization point u) and keep
  flavour as the letter orientation. *Costs:* none.

**Default if nothing is said: (no).** **Recommendation (judgement): (no) for now.** §4 shows
the swap does not produce integer flavours from γγ either, so adding it buys no reachability.
