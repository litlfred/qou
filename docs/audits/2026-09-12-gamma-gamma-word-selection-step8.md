# γγ word selection, step 8 — why the selected bond can unbind: the single-crossing obstruction is vacuous on γγ words

**Bean:** `qou-ales`. A **reconciliation**, not a new derivation, and it was found by the
corpus-grep that was supposed to check whether the diproton sign law already existed. It
does — and what turned up alongside it is a second sorry-free result that reads as a
contradiction of the step-3 measurement. It is not one, and the reason is worth proving.

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/GammaGammaEscapesSingleCrossing.lean`
(11 declarations; `#print axioms` on every one: at most `[propext, Classical.choice,
Quot.sound]`; no `sorryAx`; `lean -DautoImplicit=false -s 65536` exit 0, 0 warnings).
No probe: this step adds no number.

## 1. The apparent collision

`QOU/QBeta/SingleCrossingAlwaysBinds.lean` (sorry-free, on `main`) proves that a
**single-crossing** interface can never unbind. Its scalar is `μ = z + d` with the
convention-D Markov parameter `z = q³/(q²+1)` and `d ∈ [−h, 0]`; that lies in `(0,1)` at the
anchor, so `B = −α·log μ > 0` (`single_crossing_binds`). `t3_grading_cannot_unbind_pp` adds
that the `T₃` / writhe grading cannot rescue the sign, and the file's docstring states it
strongly: the framework *"picked a sign that makes unbinding **impossible**, whatever the
magnitude"*.

Step 3 (#7192) measured the opposite outcome for the γγ-selected bond: `G³ = (σ₂σ₃⁻¹)³`
**unbinds** the diproton, `B_pp = −4.47` keV, at trace ratio `tr_atom/tr_free = 1.001058`.
Steps 6–7 then proved `G³` is exactly what reading 3 selects.

Both results are correct. Two facts separate them.

## 2. No non-empty γγ word is a single crossing

`length_even` (step 1) gives every γγ word an even number of crossings; a single crossing
has one. Hence `gammaGamma_ne_singleCrossing` and `interfaceBond_ne_singleCrossing` — for
**every** `m`, not just `m ≥ 1`, since the empty word is not a single crossing either. The
selected bond has six crossings. The obstruction is a statement about words of length one;
`G³` was never in its domain.

## 3. The writhe / `T₃` grading is identically trivial on a γγ word

This is the sharper half, and it is the part that makes the owner's ruling structural rather
than lucky. The grading multiplies the channel scalar by `c^(writhe w / 2)`, and
`writhe_eq_zero` (step 1) gives **every** γγ word writhe `0` — one positive and one negative
crossing per pair-production vertex. So the factor is `c⁰ = 1` exactly
(`writhe_normalisation_eq_one_of_gammaGamma`), and `t3_grading_vacuous_on_gammaGamma` gives
`μ · c^{writheExponent w} = μ` for every `μ`, `c` and every γγ word.

So the γγ selection does not *defeat* the `T₃` obstruction. It makes the grading the
obstruction argues about **silent**. The owner's ruling of 2026-09-08 — select every
canonical braid word by γγ pair production and the confinement SDP, never by census — is
therefore the move that steps outside a previously-recorded structural "impossible", and it
does so for a reason internal to γγ words rather than by a choice of magnitude.

## 4. What is still measured

* `unbound_iff_ratio_gt_one` — for `α > 0` and `μ > 0`, `−α·log μ < 0` iff `μ > 1`. The
  sign is the direction the bond moves the trace, nothing more.
* `bound_iff_ratio_lt_one` — the mirror, stated on the ratio alone.
* `obstruction_conclusion_false_of_ratio_gt_one` — for a ratio above one carried through a
  writhe-`0` grading, the conclusion of `nonneg_writhe_cannot_unbind` is **false**, not
  merely unproved. Its `μ < 1` hypothesis is load-bearing.
* `selected_bond_unbinds_of_ratio_gt_one` — given only `1 < μ`, the selected bond unbinds
  and the obstruction does not apply.

So of the step-3 diproton result, **exactly one number remains a measurement**: the ratio
`1.001058`. Everything else about the sign is algebra, and the ratio is carried as a
hypothesis wherever it is used here — this file asserts no value.

## 5. What is NOT claimed

* The **magnitude** `4.47` keV is untouched; it needs `𝔈₀^full` and the measured ratio.
* This does not say the framework now gets the two-nucleon sector right.
  `SingleCrossingAlwaysBinds`'s own subject — that the *template* single-σ bond binds both
  the diproton and the dineutron, where nature binds neither — stands as recorded. What is
  established is that the γγ-selected bond is a different object, outside that argument.
* The `dineutron` side is untouched: this file is about why an obstruction does not apply,
  not about what the `nn` channel does.
* The two files' diproton numbers are **not** the same quantity and must not be compared:
  `SingleCrossingAlwaysBinds` cites `+2.5416` MeV from
  `two_nucleon_sector_sign_probe.py`, while step 3's template-bond figure is `+2.0710` MeV
  from the eleven-letter nucleon words. Different producers, different words.

## 6. Verification

Shadow compile with the new dependency (`QOU.QBeta.SingleCrossingAlwaysBinds`) built from
source into the same shadow: exit 0, 0 warnings. `#print axioms` on all 11 declarations
clean of `sorryAx`. Two slips on the first attempt, both mechanical: `Real.log_pos_iff`
wants `0 ≤ μ` where its sibling `Real.log_neg_iff` wants `0 < μ`, and an `m ≥ 1` hypothesis
was unused because the statement holds for every `m` (the empty word is not a single
crossing either) — dropped rather than silenced, which strengthened the lemma.
