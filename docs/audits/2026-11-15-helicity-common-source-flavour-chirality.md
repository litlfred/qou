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

## 8. Follow-up `qou-hlx7`: the corpus's parity mechanism IS eigenline-selective

The question was where a left-only weak coupling could come from, given D-H2 = no and given
that no single letter does it (`no_one_sided_letter`). The first candidate is the corpus's own
parity-violation mechanism. `predicted-spectra/force-knot-identification.md:63` locates parity
violation in the asymmetry of the q-weighted crossing difference q[L₊] − q⁻¹[L₋]. The check
named in the bean was: does that asymmetry select an **eigenline**, or only a **crossing
sign**?

**It selects an eigenline, exactly.** Read in the algebra before any trace, with L₊ = s and
L₋ = s⁻¹:

$$
q\,s - q^{-1} s^{-1} \;=\; (q - q^{-1})(q + q^{-1})\,P_+ \;=\; (q^2 - q^{-2})\,P_+ .
$$

| theorem | statement |
|---|---|
| `skein_asym_eq` | q·s − q⁻¹·s⁻¹ = h·[2]_q·P₊ |
| `skein_asym_mul_Pm` | it annihilates the (−q⁻¹)-line |
| `skein_asym_mul_Pp` | it acts on the q-line by q² − q⁻² |
| `skein_mirror_eq` | the mirror weighting q⁻¹·s − q·s⁻¹ = h·[2]_q·P₋ |
| `skein_asym_swap` | the swapped letter's skein difference is h·[2]_q·P₋ |
| `skein_asym_zero_of_h` | it vanishes when h = 0 (q = ±1) |
| `skein_asym_bar_odd` | it is odd under the orientation flip; P₊ is even, so the sign sits in h |

All are sorry-free, lean-direct exit 0, with standard axioms only.

### What this establishes

* The q-weighted skein difference is a scalar multiple of the **left projector**, under the
  D-H1 = A labelling. It is not merely sensitive to crossing sign.
* It is **not a letter**: it is h·[2]_q times an idempotent. That is consistent with
  `no_one_sided_letter`, and it is the escape that theorem leaves open: a chirality-selective
  operator does exist in K[s], just not as a Hecke letter.
* It is a **q ≠ 1 effect**: the prefactor is h·[2]_q = q² − q⁻². The corpus's "parity
  violation at q ≠ 1" then follows algebraically, from the identity alone.
* Which line it picks is fixed by which crossing carries the weight q. Weight q on L₊ gives
  P₊; the mirror weighting gives P₋.

### What this does NOT establish (scope (a))

* That the weak coupling **is** h·[2]_q·P₊. That would be an identification, and it is not
  made here or written into content.
* A charged current would also have to change flavour. The flavour flip s ↦ s⁻¹ is
  chirality-blind (§3). How a flip composes with P₊ into one vertex is not derived.
* The relation as written in the content block, q[L₊] − q⁻¹[L₋] = (q^{1/2} − q^{−1/2})[L₀],
  **cannot hold as an identity in the Hecke algebra**: by `skein_asym_eq` the left side is
  h·[2]_q·P₊, which is not a scalar whenever P₊ ≠ 0, 1. It reads like the Jones-polynomial
  skein relation for the invariant after trace and framing normalization. That is the agent's
  reading and has not been checked against the content's normalization. The content block is
  not edited (owner gate).

### Owner decision D-H3: should "weak vertex ∝ q-weighted skein difference = h·[2]_q·P₊" become a working hypothesis?

* **(yes)**
  - *Means:* a child bean that tries to *derive* the charged-current vertex from the skein
    difference composed with the flavour flip, inside the (2,1) block.
  - *Costs:* new Lean in this file's frame plus one probe; hours, no long compute.
  - *Risks:* the left/right choice reduces to "which crossing carries q", which could turn out
    to be a convention rather than a derivation. That would be a scope-(a) negative, but
    informative.
  - *Commits to:* a candidate source for V−A inside the letter algebra.
* **(no)**
  - *Means:* record the identity and leave `qou-hlx7` open with the candidate noted.
  - *Costs:* none.
* **Also, separately:** should the Hecke-vs-Jones normalization of the skein equation in
  `force-knot-identification.md:63` be checked and, if needed, corrected? This is a content
  edit, so it needs the owner's go.

**Default if nothing is said: (no), and content is untouched.** **Recommendation (judgement):
(yes).** The identity is exact and parameter-free, so testing it is cheap. The risk named
above is exactly what the test would measure.

## 9. Coordinator question 2: does knot chirality (e⁻ as the left trefoil) fix the L/R labelling?

The setup is from `breit-wheeler-vertex.md:34-36`: e⁻ = σ₀σ₁σ₀, and e⁺ is the mirror word
σ₀⁻¹σ₁⁻¹σ₀⁻¹. Stream 3 showed that u ↦ −u only relabels L/R. The question is whether fixing
the electron removes that freedom. A caution applies throughout: knot chirality is not field
chirality, and no identification is made here.

### Two maps, made precise

* **Knot mirror** = the flip σ ↦ σ⁻¹ on every letter. By §1 this is the bar involution, and
  it **preserves both eigenlines**. So knot chirality is the *orientation* bit (6a's flavour
  bit), not the eigenline bit.
* **L↔R relabelling** = replace every letter σ by the other Hecke letter at the same
  parameter, −σ⁻¹.
  - `swap_hecke`: each relabelled letter satisfies the Hecke relation at q.
  - `swap_braid`: the relabelled letters satisfy the braid relation.
  - `swap_swap`: the relabelling is an involution.
  - So it is a re-presentation of the same algebra. By the presentation it extends to an
    algebra automorphism; that extension is not formalised as an `AlgHom` here.

### The link between them, proved

| word length | relabelling vs mirror | theorem |
|---|---|---|
| even (e.g. L₊ = σ₀σ₁) | relabelling = mirror | `swap_word2` |
| odd (e.g. e⁻ = σ₀σ₁σ₀) | relabelling = −mirror | `swap_word3` |

Consequences:
* `swap_electron`: the relabelling sends **e⁻ ↦ −e⁺**.
* `electron_ne_swap`: when char ≠ 2, that image is not e⁻. The top coordinates are +1 for e⁻
  (`electron_top`) and −1 for −e⁺ (`positron_top`).
* So the electron is a positive word in exactly one of the two letter systems at parameter q.

### Verdict

1. **Relationally, yes.** Once the electron is fixed as the algebra element σ₀σ₁σ₀, written
   as a positive word with coefficient +1, the letter system is fixed. So, under D-H1 = A,
   which eigenline of each letter is L is fixed too.
2. **Intrinsically, no (scope (b)).** The relabelling respects every defining relation, so it
   carries the whole structure (labelling, electron) to (other labelling, −e⁺). A
   construction that uses only the algebra's relations is invariant under it, and therefore
   cannot single out one labelling. The invariant is the automorphism given by `swap_hecke` +
   `swap_braid`.
   - Fixing "the electron is σ₀σ₁σ₀ rather than −e⁺" is the **same** choice as fixing L. The
     choice is moved, not removed.
   - So knot chirality does not break the u ↦ −u freedom. It is tied to that freedom by a
     sign.
3. **The tie is a sign, and it is length parity.** On odd words the relabelling differs from
   the mirror by (−1)^ℓ. For the electron the relabelled image is −e⁺, not e⁺. So the L/R
   relabelling is not exactly the e⁻ ↔ e⁺ exchange; the two agree up to that sign. Whether the
   sign is observable (it flips the sign of any trace) is not settled here.

### Relation to `conj:type-b-folding-cpt` — a finding about content (scope (a))

`nuclear-interactions/type-b-folding-cpt.md` lists "P (braid mirror)", i.e. it realises
parity as σ ↔ σ⁻¹. By §1 the braid mirror **preserves** the eigenlines that the BW block calls
left and right circular. Physical parity exchanges the two helicities. So under D-H1 = A the
block's P is chirality-blind at letter level. It is the orientation/flavour bit of this audit.
The map that does exchange the eigenlines is the relabelling −σ⁻¹, which equals the mirror only
on even-length words.

**Content fix to report (not made; content edits need the owner's go):**
`type-b-folding-cpt.md` should either say that its P exchanges crossing orientation and not
letter eigenlines, or realise P as σ ↦ −σ⁻¹ (equal to the mirror on even words, minus the
mirror on odd ones). The same question applies wherever the corpus reads braid mirror as
parity.

By contrast, `force-knot-identification.md`'s skein asymmetry is **eigenline-selective**
(§8). It does not conflate the two. Its only issue is the Hecke-vs-Jones normalization noted
in §8.

### Owner decision D-H4: how should parity be realised?

* **(A) Keep P = braid mirror and add the scoping sentence.**
  - *Means:* parity is the orientation flip, and it is chirality-blind at letter level.
  - *Costs:* one sentence in `type-b-folding-cpt.md`.
  - *Risks:* it states openly that the corpus's P does not exchange helicities, which a
    physics referee will notice.
  - *Commits to:* parity and chirality being different letter-level operations.
* **(B) Re-realise P as the relabelling σ ↦ −σ⁻¹.**
  - *Means:* P exchanges the L/R eigenlines and agrees with the mirror on even words.
  - *Costs:* edits to the CPT block and its Lean sibling, plus a check of every place
    "mirror = P" is used.
  - *Risks:* on odd words, e.g. the electron, P(e⁻) = −e⁺, which carries a sign the current
    CPT story does not have.
  - *Commits to:* a sign-carrying parity.
* **Default if nothing is said:** nothing changes, and the finding stays recorded here and in
  `qou-hlx7`.
* **Recommendation (judgement): (A) now, and (B) as a separate investigation.** The scoping
  sentence is cheap and true. Whether the sign in (B) is physical needs its own derivation.
